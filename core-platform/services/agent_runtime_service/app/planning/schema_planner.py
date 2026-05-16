"""Schema-driven planner for the MAOMIAI agent runtime.

Plans execution from tool/capability schemas instead of hardcoded
keyword matching.  Falls back gracefully when no planner model is
available, but never parses concrete business entities or product
names from the user query at runtime.
"""

from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass
from typing import Any

from .schema_loader import compact_schema_for_prompt, list_tool_names, load_planner_schema


@dataclass
class SchemaPlanResult:
    ok: bool
    plan: dict[str, Any]
    source: str
    error: str | None = None


def _normalize_message(message: Any) -> str:
    if message is None:
        return ""
    return str(message).strip()


def _step(tool: str, args: dict[str, Any] | None = None, reason: str = "") -> dict[str, Any]:
    return {
        "id": f"step_{uuid.uuid4().hex[:8]}",
        "tool": tool,
        "args": args or {},
        "reason": reason,
        "depends_on": [],
    }


def _base_plan(
    message: str,
    task_type: str,
    steps: list[dict[str, Any]],
    confidence: float,
    source: str,
    fallback_reason: str | None = None,
) -> dict[str, Any]:
    return {
        "task_type": task_type,
        "confidence": confidence,
        "steps": steps,
        "source": source,
        "planner_mode": "schema_driven",
        "requires_model_reasoning": any(s.get("tool") == "model.generate" for s in steps),
        "fallback_reason": fallback_reason,
        "input": message,
    }


def _text_terms(value: str) -> set[str]:
    """Extract generic terms for schema matching.

    This is not a business/entity router. It is only a lightweight lexical
    similarity fallback when planner model is unavailable.
    """
    text = value.lower()
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
    # For CJK, keep short character n-grams for generic lexical overlap with schema text.
    compact = "".join(ch for ch in value if not ch.isspace())
    for n in (2, 3, 4):
        for i in range(max(0, len(compact) - n + 1)):
            tokens.add(compact[i:i + n].lower())
    return {t for t in tokens if t}


def _schema_text_for_tool(tool: dict[str, Any]) -> str:
    """Collect all descriptive text from a tool schema for scoring."""
    parts: list[str] = []
    for key in ("name", "kind", "description"):
        if tool.get(key):
            parts.append(str(tool.get(key)))
    for item in tool.get("capabilities", []) or []:
        parts.append(str(item))
    hints = tool.get("planner_hints") or {}
    for item in hints.get("request_shapes", []) or []:
        parts.append(str(item))
    for key, value in (tool.get("input_schema") or {}).items():
        parts.append(str(key))
        parts.append(str(value))
    return " ".join(parts)


def _score_tool_for_request(message: str, tool: dict[str, Any]) -> float:
    """Score a tool's relevance to a user request using schema text overlap."""
    request_terms = _text_terms(message)
    schema_terms = _text_terms(_schema_text_for_tool(tool))
    if not request_terms or not schema_terms:
        return 0.0
    overlap = request_terms.intersection(schema_terms)
    score = len(overlap) / max(1, min(len(request_terms), len(schema_terms)))
    kind = str(tool.get("kind") or "")
    name = str(tool.get("name") or "")
    # General safe context tools are useful as low-risk planning context.
    if kind == "safe":
        score += 0.05
    # Final natural-language generation is almost always needed.
    if name == "model.generate":
        score += 0.12
    # Restricted tools must not be selected by weak lexical overlap.
    if kind == "restricted":
        score -= 0.10
    return round(max(0.0, score), 4)


def _rank_tools(message: str, schema: dict[str, Any]) -> list[dict[str, Any]]:
    """Rank all tools by relevance score for a given request."""
    ranked: list[dict[str, Any]] = []
    for tool in schema.get("tools", []) or []:
        if not isinstance(tool, dict) or not tool.get("name"):
            continue
        ranked.append({
            "tool": tool,
            "score": _score_tool_for_request(message, tool),
        })
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked


def _builtin_contract_context_step(message: str) -> dict[str, Any]:
    """Request capability context including builtin execution contracts."""
    return _step(
        "capability.match",
        {
            "query": message,
            "limit": 12,
            "include_skills": True,
            "include_builtin_contracts": True,
            "source": "builtin_contract_aware_planner",
        },
        "discover relevant builtin modules, default skills and execution contracts",
    )


def _skill_context_steps(message: str) -> list[dict[str, Any]]:
    """Add skill/builtin discovery context without hardcoded query routing.

    This uses capability.match over the external capability registry.
    Since C26-B/C26-R3 expose skill.* and builtin.* capabilities, the planner can
    discover relevant owned modules and default skills through the same schema-driven path.
    """
    return [_builtin_contract_context_step(message)]


def _ensure_skill_context(message: str, steps: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Ensure capability.match context is present for skill discovery.

    If steps already include a capability.match step, no duplication.
    Otherwise prepend one so the planner always has skill awareness.
    """
    if any(step.get("tool") == "capability.match" for step in steps):
        return steps
    return _skill_context_steps(message) + steps


def _contract_tool_steps_from_capabilities(message: str, schema: dict[str, Any]) -> list[dict[str, Any]]:
    """Select implemented builtin contract tools through schema metadata.

    This is not keyword routing. It uses capability.match to discover builtin
    modules, then asks the tool schema whether a corresponding implemented
    builtin execution tool exists.
    """
    try:
        from ..capability.registry import match_capabilities
    except Exception:
        return []

    available_tool_names = {
        str(tool.get("name"))
        for tool in schema.get("tools", [])
        if isinstance(tool, dict) and tool.get("name")
    }

    try:
        matches = match_capabilities(message, limit=8)
    except Exception:
        return []

    steps: list[dict[str, Any]] = []
    for cap in matches:
        cap_id = str(getattr(cap, "id", "") or "")
        metadata = getattr(cap, "metadata", {}) or {}
        if not cap_id.startswith("builtin."):
            continue
        contract = metadata.get("execution_contract") or {}
        allowed_tools = contract.get("allowed_tools") or metadata.get("allowed_tools") or []
        for tool_name in allowed_tools:
            tool_name = str(tool_name)
            if not tool_name.startswith("builtin."):
                continue
            if tool_name not in available_tool_names:
                continue
            steps.append(
                _step(
                    tool_name,
                    {
                        "task": message,
                        "source_builtin": cap_id,
                        "planner_source": "builtin_contract_tool_selection",
                    },
                    f"execute owned builtin module {cap_id}",
                )
            )
            return steps
    return steps


def _schema_only_default_plan(message: str, schema: dict[str, Any]) -> dict[str, Any]:
    """Schema scoring fallback when planner model is unavailable.

    It does not parse concrete user entities or hardcoded query words.
    It ranks tools by similarity between request text and tool/capability schema.
    """
    ranked = _rank_tools(message, schema)
    selected: list[dict[str, Any]] = []
    for item in ranked:
        tool = item["tool"]
        score = item["score"]
        name = str(tool.get("name"))
        if name == "model.generate":
            continue
        kind = str(tool.get("kind") or "")
        if kind == "restricted" and score < 0.65:
            continue
        if score >= 0.08:
            selected.append(
                _step(
                    name,
                    {"query": message} if name in {"repo_memory.search", "capability.match", "web.search"} else {},
                    f"schema score {score}",
                )
            )
        if len(selected) >= 3:
            break
    # Builtin contract tool selection (C26-R8): if a discovered builtin
    # capability has an implemented tool in planner_tool_schema, add it.
    contract_steps = _contract_tool_steps_from_capabilities(message, schema)
    if contract_steps:
        existing_tools = {str(step.get("tool")) for step in selected}
        for step in contract_steps:
            if str(step.get("tool")) not in existing_tools:
                selected.insert(0, step)
                existing_tools.add(str(step.get("tool")))
    # Ensure skill discovery context is present (C26-D skill-aware planner).
    selected = _ensure_skill_context(message, selected)
    # Final composition.
    if any(t.get("name") == "model.generate" for t in schema.get("tools", [])):
        selected.append(_step("model.generate", {"prompt": message}, "compose final answer from selected tool observations and skill context"))
    if not selected:
        selected.append(_step("model.generate", {"prompt": message}, "last resort final answer"))
    avg = 0.0
    if ranked:
        avg = sum(x["score"] for x in ranked[:3]) / max(1, min(3, len(ranked)))
    return _base_plan(
        message=message,
        task_type="schema_scored",
        steps=selected,
        confidence=round(max(0.45, min(0.85, avg + 0.45)), 4),
        source="schema_scoring",
        fallback_reason=None,
    )


def _build_planner_prompt(message: str, schema: dict[str, Any], memory_context: Any = None) -> str:
    compact = compact_schema_for_prompt(schema)
    payload = {
        "instruction": (
            "Create a structured execution plan for the user request. "
            "Use only tools listed in tool_schema. "
            "Do not rely on hardcoded keywords. "
            "If a tool requires an argument such as location or offset, infer it semantically from the request. "
            "Return JSON only with fields: task_type, confidence, steps."
        ),
        "user_request": message,
        "tool_schema": compact,
        "memory_context": memory_context or [],
        "output_schema": {
            "task_type": "string",
            "confidence": "number",
            "steps": [
                {
                    "id": "string",
                    "tool": "string",
                    "args": "object",
                    "reason": "string",
                    "depends_on": "array",
                }
            ],
        },
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def _extract_json_object(text: str) -> dict[str, Any] | None:
    """Extract a JSON object from model text."""
    if not text:
        return None
    stripped = text.strip()
    try:
        obj = json.loads(stripped)
        if isinstance(obj, dict):
            return obj
    except Exception:
        pass
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start >= 0 and end > start:
        try:
            obj = json.loads(stripped[start:end + 1])
            if isinstance(obj, dict):
                return obj
        except Exception:
            return None
    return None


def _normalize_model_plan(obj: dict[str, Any], schema: dict[str, Any]) -> dict[str, Any] | None:
    """Normalize model generated plan into the planner contract."""
    if not isinstance(obj, dict):
        return None
    available_tools = set(list_tool_names(schema))
    raw_steps = obj.get("steps")
    if not isinstance(raw_steps, list):
        return None
    steps: list[dict[str, Any]] = []
    for index, raw in enumerate(raw_steps):
        if not isinstance(raw, dict):
            continue
        tool = str(raw.get("tool") or "").strip()
        if not tool or tool not in available_tools:
            continue
        args = raw.get("args")
        if not isinstance(args, dict):
            args = {}
        depends_on = raw.get("depends_on")
        if not isinstance(depends_on, list):
            depends_on = []
        steps.append({
            "id": str(raw.get("id") or f"model_step_{index + 1}"),
            "tool": tool,
            "args": args,
            "reason": str(raw.get("reason") or "planner model selected this tool"),
            "depends_on": depends_on,
        })
    if not steps:
        return None
    # Ensure final natural language composition unless the model explicitly planned one.
    if "model.generate" in available_tools and not any(s.get("tool") == "model.generate" for s in steps):
        steps.append(_step("model.generate", {"prompt": obj.get("final_prompt") or ""}, "compose final answer"))
    confidence = obj.get("confidence")
    try:
        confidence = float(confidence)
    except Exception:
        confidence = 0.75
    steps = _ensure_skill_context(str(obj.get("input") or obj.get("query") or obj.get("prompt") or ""), steps)
    return {
        "task_type": str(obj.get("task_type") or "schema_model"),
        "confidence": max(0.0, min(1.0, confidence)),
        "steps": steps,
    }


def _call_planner_model(prompt: str, schema: dict[str, Any]) -> dict[str, Any] | None:
    """Best-effort structured planner model call.

    B4 changes behavior:
    - planner model is enabled by default unless explicitly disabled.
    - if model_gateway/llm planner is unavailable, schema scoring fallback is used.
    - output must be normalized against available tool schema.
    """
    mode = os.environ.get("MAOMIAI_SCHEMA_PLANNER_MODEL", "auto").lower().strip()
    if mode in {"0", "false", "no", "off", "disabled"}:
        return None
    try:
        from .llm_planner import call_planner_model  # type: ignore[attr-defined]

        raw = call_planner_model(prompt)
        obj: dict[str, Any] | None = None
        if isinstance(raw, dict):
            obj = raw
        elif isinstance(raw, str):
            obj = _extract_json_object(raw)
        if not obj:
            return None
        return _normalize_model_plan(obj, schema)
    except Exception:
        return None


def build_schema_plan(
    message: Any,
    *,
    session_id: str | None = None,
    current_profile: str | None = None,
    memory_context: Any = None,
) -> SchemaPlanResult:
    msg = _normalize_message(message)
    schema = load_planner_schema()

    if not msg:
        plan = _base_plan(
            message="",
            task_type="empty",
            steps=[],
            confidence=1.0,
            source="schema_empty",
            fallback_reason="empty_message",
        )
        return SchemaPlanResult(ok=True, plan=plan, source="schema_empty")

    prompt = _build_planner_prompt(msg, schema, memory_context=memory_context)
    model_plan = _call_planner_model(prompt, schema)

    if isinstance(model_plan, dict) and model_plan.get("steps"):
        plan = {
            "task_type": model_plan.get("task_type") or "schema_model",
            "confidence": float(model_plan.get("confidence") or 0.7),
            "steps": model_plan.get("steps") or [],
            "source": "schema_model_structured",
            "planner_mode": "schema_driven",
            "requires_model_reasoning": any(
                str(s.get("tool")) == "model.generate" for s in model_plan.get("steps", []) if isinstance(s, dict)
            ),
            "fallback_reason": None,
            "input": msg,
            "session_id": session_id,
            "current_profile": current_profile,
        }
        return SchemaPlanResult(ok=True, plan=plan, source="schema_model")

    plan = _schema_only_default_plan(msg, schema)
    plan["session_id"] = session_id
    plan["current_profile"] = current_profile
    return SchemaPlanResult(ok=True, plan=plan, source="schema_default")
