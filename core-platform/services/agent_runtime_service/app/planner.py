"""Schema-driven planner entrypoint for the MAOMIAI agent runtime.

C25-C14-B2: Public ``build_plan()`` now uses only schema-driven planning.
The legacy keyword/LLM rule chain is fully isolated in
``app/planning/legacy_rule_planner.py`` and is only reachable through
the ``MAOMIAI_LEGACY_PLANNER=1`` env var for rollback/debug.

This file must NOT contain:
  - _keyword_plan or any keyword-matching logic
  - re.search query parsing
  - hardcoded Chinese query words (天气, 几点, MCP, 仓库, 资产, etc.)
  - direct LLM planner calls (those belong in planning/legacy_rule_planner.py)
"""

from __future__ import annotations

import os
from typing import Any

from .models import AgentPlan
from .planning.schema_planner import build_schema_plan
from .policy.loader import load_entity_aliases


def normalize_query(text: str) -> tuple[str, list[dict[str, Any]]]:
    """Normalize user text using external alias policy only."""

    query = (text or "").strip()
    corrections: list[dict[str, Any]] = []
    for item in load_entity_aliases():
        source = str(item.get("from") or "")
        target = str(item.get("to") or "")
        if source and target and source in query:
            query = query.replace(source, target)
            corrections.append(
                {
                    "from": source,
                    "to": target,
                    "reason": item.get("reason") or "external_entity_alias",
                }
            )
    return query, corrections


# ---------------------------------------------------------------------------
# Schema-driven planner bridge
# ---------------------------------------------------------------------------

def _schema_plan_to_agent_plan(
    schema_plan: dict[str, Any],
    normalized: str,
    corrections: list[dict[str, Any]],
) -> AgentPlan:
    """Convert a schema-driven plan dict into the existing AgentPlan model."""
    tools = [str(s.get("tool")) for s in schema_plan.get("steps", []) if s.get("tool")]
    delegate = any(t == "model.generate" for t in tools)
    must_not = not delegate

    args: dict[str, Any] = {
        "corrections": corrections,
        "planner_source": schema_plan.get("source", "schema_driven"),
        "planner_mode": "schema_driven",
        "confidence": schema_plan.get("confidence"),
        "steps": schema_plan.get("steps", []),
    }
    if schema_plan.get("fallback_reason"):
        args["fallback_reason"] = schema_plan["fallback_reason"]
    if schema_plan.get("session_id"):
        args["session_id"] = schema_plan["session_id"]
    if schema_plan.get("current_profile"):
        args["current_profile"] = schema_plan["current_profile"]

    return AgentPlan(
        intent=schema_plan.get("task_type", "schema_general"),
        normalized_query=normalized,
        tools=tools,
        reason=f"schema-driven planner: {schema_plan.get('source', 'unknown')}",
        must_not_hallucinate=must_not,
        delegate_to_model=delegate,
        args=args,
    )


def _schema_error_fallback_plan(
    message: str,
    normalized: str,
    corrections: list[dict[str, Any]],
    error: str | None = None,
) -> AgentPlan:
    """Fallback when schema planner itself fails structurally.

    This is NOT the legacy rule planner.  It simply delegates to
    model.generate so the user still gets a response.
    """
    return AgentPlan(
        intent="schema_planner_error",
        normalized_query=normalized,
        tools=["model.generate"],
        reason="schema planner failed; final response delegated to model",
        must_not_hallucinate=False,
        delegate_to_model=True,
        args={
            "corrections": corrections,
            "planner_source": "schema_error_fallback",
            "planner_mode": "schema_driven",
            "fallback_reason": error or "schema_planner_failed",
            "requires_model_reasoning": True,
        },
    )


def build_plan_schema_first(
    message: str,
    session_id: str | None = None,
    current_profile: str | None = None,
    **kwargs: Any,
) -> AgentPlan:
    """Schema-driven planner entry.

    This is the preferred and only production planner path.
    Legacy rule planner is available only through MAOMIAI_LEGACY_PLANNER=1.
    """
    normalized, corrections = normalize_query(message)

    result = build_schema_plan(
        message,
        session_id=session_id,
        current_profile=current_profile,
        memory_context=kwargs.get("memory_context"),
    )

    if result.ok and result.plan.get("steps"):
        return _schema_plan_to_agent_plan(result.plan, normalized, corrections)

    # Schema planner produced nothing useful — use schema error fallback,
    # NOT legacy rule planner.  Legacy is only reachable via env switch.
    return _schema_error_fallback_plan(
        message=message,
        normalized=normalized,
        corrections=corrections,
        error=result.error or "schema_planner_produced_no_steps",
    )


# ---------------------------------------------------------------------------
# Public API — schema-driven by default
# ---------------------------------------------------------------------------

def build_plan(message: str, **kwargs: Any) -> AgentPlan:
    """Public planner API.

    Defaults to schema-driven planning.  Set
    ``MAOMIAI_LEGACY_PLANNER=1`` only for rollback/debug.
    """
    if os.environ.get("MAOMIAI_LEGACY_PLANNER", "").lower() in {"1", "true", "yes", "on"}:
        from .planning.legacy_rule_planner import build_plan_legacy
        legacy = build_plan_legacy(message=message, **kwargs)
        if isinstance(legacy, AgentPlan):
            legacy.args["planner_mode"] = "legacy_rule_forced"
            legacy.args["fallback_reason"] = legacy.args.get("fallback_reason") or "legacy_env_forced"
        return legacy
    return build_plan_schema_first(message=message, **kwargs)
