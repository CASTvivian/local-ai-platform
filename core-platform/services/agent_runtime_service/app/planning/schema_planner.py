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


def _schema_only_default_plan(message: str, schema: dict[str, Any]) -> dict[str, Any]:
    """Default plan when no planner model is available.

    This function must not parse concrete business entities or
    hardcoded product/city/date names.  It uses schema-level
    capability/tool descriptions and generic request-shape signals only.
    """
    available = set(list_tool_names(schema))
    steps: list[dict[str, Any]] = []

    # Generic safe discovery first: capability.match can inspect schema/registry.
    if "capability.match" in available:
        steps.append(_step("capability.match", {"query": message}, "match request against capability schema"))

    # Local project knowledge/memory is safe and useful as context for many requests.
    if "repo_memory.search" in available:
        steps.append(_step("repo_memory.search", {"query": message, "limit": 8}, "retrieve local project/repo memory context"))

    # Final answer should normally be composed by the model from observations.
    if "model.generate" in available:
        steps.append(_step("model.generate", {"prompt": message}, "compose final answer from observations and context"))

    if not steps:
        steps = [_step("model.generate", {"prompt": message}, "fallback to model response")]

    return _base_plan(
        message=message,
        task_type="schema_general",
        steps=steps,
        confidence=0.55,
        source="schema_default",
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


def _call_planner_model(prompt: str) -> dict[str, Any] | None:
    """Optional planner model call.

    This is deliberately best-effort. If unavailable, schema default
    planner is used.  The model gateway integration can be tightened in
    C25-C14-B2.
    """
    mode = os.environ.get("MAOMIAI_SCHEMA_PLANNER_MODEL", "").lower().strip()
    if mode not in {"1", "true", "yes", "on"}:
        return None
    try:
        from .llm_planner import call_planner_model  # type: ignore[attr-defined]

        raw = call_planner_model(prompt)
        if isinstance(raw, dict):
            return raw
        if isinstance(raw, str):
            return json.loads(raw)
    except Exception:
        return None
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
    model_plan = _call_planner_model(prompt)

    if isinstance(model_plan, dict) and model_plan.get("steps"):
        plan = {
            "task_type": model_plan.get("task_type") or "schema_model",
            "confidence": float(model_plan.get("confidence") or 0.7),
            "steps": model_plan.get("steps") or [],
            "source": "schema_model",
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
