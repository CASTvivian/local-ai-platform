"""Runtime capability registry — schema-driven matching, no hardcoded keyword tables."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from .models import Capability


# ---------------------------------------------------------------------------
# Path resolution
# ---------------------------------------------------------------------------

def _core_platform_dir() -> Path:
    """Resolve core-platform root from env or file location."""
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    return Path(__file__).resolve().parents[4]


def _schema_registry_path() -> Path:
    """Path to the external capability registry JSON."""
    return _core_platform_dir() / "data" / "agent_policy" / "capability_registry.json"


def _runtime_registry_path() -> Path:
    """Path to the runtime capability registry (persisted edits)."""
    root = _core_platform_dir() / "data" / "capability_registry"
    root.mkdir(parents=True, exist_ok=True)
    return root / "capabilities.json"


# ---------------------------------------------------------------------------
# External schema loader
# ---------------------------------------------------------------------------

def load_capability_schema() -> Dict[str, Any]:
    """Load the external capability_registry.json schema."""
    path = _schema_registry_path()
    if not path.exists():
        return {"version": "missing", "capabilities": []}
    return json.loads(path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Tokenisation / term extraction
# ---------------------------------------------------------------------------

def _terms(value: str) -> set[str]:
    """Extract search terms from a string — CJK n-gram aware."""
    text = str(value or "").lower()
    tokens: set[str] = set()
    current: list[str] = []
    for ch in text:
        if ch.isalnum() or ch in {"_", "-", "."}:
            current.append(ch)
        else:
            if current:
                tokens.add("".join(current))
                current = []
    if current:
        tokens.add("".join(current))
    # CJK n-grams for Chinese/Japanese/Korean text
    compact = "".join(ch for ch in str(value or "") if not ch.isspace())
    for n in (2, 3, 4):
        for i in range(max(0, len(compact) - n + 1)):
            tokens.add(compact[i:i + n].lower())
    return {x for x in tokens if x}


def _capability_text(capability: dict[str, Any]) -> str:
    """Collect all descriptive text from a capability dict for term matching."""
    parts: list[str] = []
    for key in ("id", "name", "type", "description", "runtime", "target"):
        if capability.get(key):
            parts.append(str(capability.get(key)))
    for item in capability.get("tags", []) or []:
        parts.append(str(item))
    for item in capability.get("aliases", []) or []:
        parts.append(str(item))
    return " ".join(parts)


# ---------------------------------------------------------------------------
# Capability loading — merge schema + runtime overrides
# ---------------------------------------------------------------------------

_DEFAULT_CAPABILITIES: Optional[List[Capability]] = None


def _capabilities_from_schema() -> List[Capability]:
    """Build Capability objects from the external schema."""
    schema = load_capability_schema()
    caps: List[Capability] = []
    for entry in schema.get("capabilities", []):
        try:
            caps.append(Capability(
                id=entry["id"],
                name=entry.get("name", entry["id"]),
                type=entry.get("type", "model"),
                description=entry.get("description", ""),
                runtime=entry.get("runtime", "model"),
                target=entry.get("target", ""),
                priority=entry.get("priority", 50),
                enabled=entry.get("enabled", True),
                tags=entry.get("tags", []),
                metadata=entry.get("metadata", {}),
            ))
        except Exception:
            continue
    return caps


def load_capabilities() -> List[Capability]:
    """Load capabilities: runtime overrides if present, else schema."""
    global _DEFAULT_CAPABILITIES
    runtime_path = _runtime_registry_path()
    if runtime_path.exists():
        try:
            data = json.loads(runtime_path.read_text(encoding="utf-8"))
            return [Capability.model_validate(item) for item in data]
        except Exception:
            pass
    # Fallback to schema
    caps = _capabilities_from_schema()
    if caps:
        _DEFAULT_CAPABILITIES = caps
        return caps
    # Last resort: empty list
    return []


def ensure_registry() -> None:
    """Create runtime registry file when missing (from schema)."""
    caps = load_capabilities()
    if caps and not _runtime_registry_path().exists():
        save_capabilities(caps)


def list_capabilities(enabled_only: bool = False) -> List[dict]:
    """Return capability dictionaries for API responses."""
    items = load_capabilities()
    if enabled_only:
        items = [item for item in items if item.enabled]
    return [item.model_dump() for item in items]


def get_capability(capability_id: str) -> Optional[Capability]:
    """Return one capability by id."""
    for item in load_capabilities():
        if item.id == capability_id:
            return item
    return None


def save_capabilities(items: List[Capability]) -> None:
    """Persist runtime capability registry."""
    path = _runtime_registry_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps([item.model_dump() for item in items], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def upsert_capability(capability: Capability) -> Capability:
    """Insert or replace one capability."""
    items = load_capabilities()
    for index, item in enumerate(items):
        if item.id == capability.id:
            items[index] = capability
            save_capabilities(items)
            return capability
    items.append(capability)
    save_capabilities(items)
    return capability


# ---------------------------------------------------------------------------
# Schema-driven matching — no hardcoded keyword tables
# ---------------------------------------------------------------------------

def match_capabilities(
    query: str,
    intent: str | None = None,
    tags: list[str] | None = None,
    limit: int = 5,
) -> List[Capability]:
    """Match a query to enabled capabilities using schema text overlap scoring.

    Scoring is based on term overlap between the query and the combined
    descriptive text of each capability (id, name, type, description,
    tags, aliases).  No hardcoded Chinese keyword tables are used.
    """
    tags = tags or []
    query_terms = _terms(query)
    if not query_terms:
        return []

    # Load schema to get aliases for scoring
    schema = load_capability_schema()
    alias_map: Dict[str, set[str]] = {}
    for entry in schema.get("capabilities", []):
        cap_id = entry.get("id", "")
        entry_terms: set[str] = set()
        for item in entry.get("aliases", []) or []:
            entry_terms.update(_terms(str(item)))
        for item in entry.get("tags", []) or []:
            entry_terms.update(_terms(str(item)))
        alias_map[cap_id] = entry_terms

    scored: list[tuple[float, Capability]] = []
    for capability in load_capabilities():
        if not capability.enabled:
            continue
        # Build text from capability fields
        cap_text = " ".join([
            capability.id,
            capability.name,
            capability.type,
            capability.description,
            " ".join(capability.tags),
            capability.runtime,
            capability.target,
        ])
        cap_terms = _terms(cap_text)
        # Merge schema alias terms
        cap_terms.update(alias_map.get(capability.id, set()))

        # Compute overlap score
        overlap = query_terms.intersection(cap_terms)
        base_score = len(overlap) / max(1, min(len(query_terms), len(cap_terms)))

        # Bonus for explicit tag match
        tag_bonus = 0.0
        for tag in tags:
            if tag in capability.tags:
                tag_bonus += 0.1

        # Bonus for intent match
        intent_bonus = 0.0
        if intent:
            intent_terms = _terms(intent)
            if intent_terms.intersection(cap_terms):
                intent_bonus = 0.15

        # Small priority-based tiebreaker (0..1 range, max ~1.0)
        priority_bonus = capability.priority / 1000.0

        score = round(base_score + tag_bonus + intent_bonus + priority_bonus, 4)
        if score > 0:
            scored.append((score, capability))

    scored.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in scored[:limit]]
