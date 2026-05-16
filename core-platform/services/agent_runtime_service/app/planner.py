"""LLM-first planner entrypoint for the MAOMIAI agent runtime.

C25-C14-B1: Public ``build_plan()`` now defaults to schema-driven
planning.  The legacy keyword/LLM rule chain is retained as
``build_plan_legacy()`` and is only used when
``MAOMIAI_LEGACY_PLANNER=1`` is set for rollback/debug.
"""

from __future__ import annotations

import os
from typing import Any, Dict, List

from .models import AgentPlan
from .planning.llm_planner import get_last_planner_error, llm_create_plan
from .planning.schema_planner import build_schema_plan
from .policy.loader import load_entity_aliases
from .health.planner_health import planner_runtime_state


LAST_PLAN_ERROR: str | None = None


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

    args: Dict[str, Any] = {
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


def build_plan_schema_first(
    message: str,
    session_id: str | None = None,
    current_profile: str | None = None,
    **kwargs: Any,
) -> AgentPlan:
    """Schema-driven planner entry.

    This is the preferred planner path.  Legacy rule planner remains
    only as fallback during C25-C14 migration.
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

    # Schema planner produced nothing useful — fall through to legacy.
    legacy = build_plan_legacy(message=message, session_id=session_id, current_profile=current_profile, **kwargs)
    if isinstance(legacy, AgentPlan):
        legacy.args["planner_mode"] = "legacy_rule_fallback"
        legacy.args["fallback_reason"] = legacy.args.get("fallback_reason") or "schema_planner_produced_no_steps"
    return legacy


# ---------------------------------------------------------------------------
# Legacy planner (keyword rules + LLM + fallback)
# ---------------------------------------------------------------------------

def _fallback_local_chat(normalized: str, corrections: List[Dict[str, Any]]) -> AgentPlan:
    health = planner_runtime_state(check_live=False)
    return AgentPlan(
        intent="local_chat",
        normalized_query=normalized,
        tools=["model.generate"],
        reason="planner fallback: delegate to local model",
        must_not_hallucinate=False,
        delegate_to_model=True,
        args={
            "corrections": corrections,
            "planner_source": "fallback_local_chat",
            "fallback_reason": "llm_planner_unavailable",
            "planner_health": health.model_dump(),
            "planner_error": LAST_PLAN_ERROR,
            "planner_mode": "legacy",
        },
    )


def _keyword_plan(normalized: str, corrections: List[Dict[str, Any]]) -> AgentPlan | None:
    """Handle demo-critical grounded intents without depending on the LLM planner.

    LEGACY: This keyword-matching logic is retained for rollback only.
    C25-C14-B2 will remove or isolate it.
    """

    lowered = normalized.lower()

    if any(token in normalized for token in ["现在几点", "现在几号", "今天几月几号", "今天是几月几号", "当前时间", "现在时间"]):
        return AgentPlan(
            intent="time_now",
            normalized_query=normalized,
            tools=["time.now"],
            reason="keyword rule: current local time/date query",
            must_not_hallucinate=True,
            delegate_to_model=False,
            args={"corrections": corrections, "planner_source": "keyword_rule", "planner_mode": "legacy"},
        )

    if any(token in normalized for token in ["仓库资产", "repo 资产", "mcp 相关仓库", "agent 和 mcp", "agent与mcp", "agent mcp"]):
        return AgentPlan(
            intent="project_knowledge",
            normalized_query=normalized,
            tools=["repo_memory.search"],
            reason="keyword rule: repo or MCP asset query",
            must_not_hallucinate=True,
            delegate_to_model=False,
            args={
                "query": normalized,
                "corrections": corrections,
                "planner_source": "keyword_rule",
                "planner_mode": "legacy",
            },
        )

    if (
        ("能力" in normalized or "capability" in lowered)
        and any(token in normalized for token in ["智能体", "平台", "agent"])
    ):
        return AgentPlan(
            intent="capability_status",
            normalized_query=normalized,
            tools=["capability.status"],
            reason="keyword rule: platform capability status query",
            must_not_hallucinate=True,
            delegate_to_model=False,
            args={"corrections": corrections, "planner_source": "keyword_rule", "planner_mode": "legacy"},
        )

    return None


def _llm_plan(message: str) -> AgentPlan | None:
    global LAST_PLAN_ERROR
    normalized, corrections = normalize_query(message)
    try:
        llm_plan = llm_create_plan(normalized)
    except Exception as exc:
        LAST_PLAN_ERROR = str(exc)
        return None
    if not llm_plan:
        LAST_PLAN_ERROR = get_last_planner_error()
        return None
    LAST_PLAN_ERROR = None
    args = dict(llm_plan.args or {})
    args["corrections"] = corrections
    args["planner_source"] = "llm"
    args["planner_confidence"] = llm_plan.confidence
    args["planner_mode"] = "legacy"
    return AgentPlan(
        intent=llm_plan.intent,
        normalized_query=normalized,
        tools=llm_plan.tools,
        reason=llm_plan.reason,
        must_not_hallucinate=llm_plan.must_not_hallucinate,
        delegate_to_model=llm_plan.delegate_to_model,
        args=args,
    )


def build_plan_legacy(message: str, **kwargs: Any) -> AgentPlan:
    """Legacy planner: keyword rules -> LLM planner -> fallback chat.

    Only used when schema-driven planner fails or when
    MAOMIAI_LEGACY_PLANNER=1 is explicitly set.
    """

    normalized, corrections = normalize_query(message)
    keyword_plan = _keyword_plan(normalized, corrections)
    if keyword_plan:
        return keyword_plan

    mode = os.environ.get("MAOMIAI_PLANNER_MODE", "llm_first").strip().lower()
    if mode in {"llm", "llm_first"}:
        plan = _llm_plan(message)
        if plan:
            return plan
    return _fallback_local_chat(normalized, corrections)


# ---------------------------------------------------------------------------
# Public API — schema-driven by default
# ---------------------------------------------------------------------------

def build_plan(message: str, **kwargs: Any) -> AgentPlan:
    """Public planner API.

    Defaults to schema-driven planning.  Set
    ``MAOMIAI_LEGACY_PLANNER=1`` only for rollback/debug.
    """
    if os.environ.get("MAOMIAI_LEGACY_PLANNER", "").lower() in {"1", "true", "yes", "on"}:
        legacy = build_plan_legacy(message=message, **kwargs)
        if isinstance(legacy, AgentPlan):
            legacy.args["planner_mode"] = "legacy_rule_forced"
        return legacy
    return build_plan_schema_first(message=message, **kwargs)
