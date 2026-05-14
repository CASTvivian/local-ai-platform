"""External policy loader for the MAOMIAI agent planner."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


ROOT = Path("core-platform/data/agent_policy")
PLANNER_POLICY = ROOT / "planner_policy.json"
ENTITY_ALIASES = ROOT / "entity_aliases.json"


def _read_json(path: Path, default: Dict[str, Any]) -> Dict[str, Any]:
    try:
        if path.exists():
            return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        pass
    return default


def load_planner_policy() -> Dict[str, Any]:
    return _read_json(
        PLANNER_POLICY,
        {
            "intents": [],
            "fallback": {
                "intent": "local_chat",
                "tools": ["model.generate"],
                "reason": "fallback",
                "must_not_hallucinate": False,
                "delegate_to_model": True,
            },
        },
    )


def load_entity_aliases() -> List[Dict[str, Any]]:
    data = _read_json(ENTITY_ALIASES, {"aliases": []})
    aliases = data.get("aliases") or []
    if not isinstance(aliases, list):
        return []
    return aliases
