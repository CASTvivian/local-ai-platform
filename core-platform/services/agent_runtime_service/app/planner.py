"""LLM-first planner entrypoint for the MAOMIAI agent runtime."""

from __future__ import annotations

import os
from typing import Any, Dict, List

from .models import AgentPlan
from .planning.llm_planner import get_last_planner_error, llm_create_plan
from .policy.loader import load_entity_aliases


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
        },
    )


def _llm_plan(message: str) -> AgentPlan | None:
    global LAST_PLAN_ERROR
    normalized, corrections = normalize_query(message)
    llm_plan = llm_create_plan(normalized)
    if not llm_plan:
        LAST_PLAN_ERROR = get_last_planner_error()
        return None
    LAST_PLAN_ERROR = None
    args = dict(llm_plan.args or {})
    args["corrections"] = corrections
    args["planner_source"] = "llm"
    args["planner_confidence"] = llm_plan.confidence
    return AgentPlan(
        intent=llm_plan.intent,
        normalized_query=normalized,
        tools=llm_plan.tools,
        reason=llm_plan.reason,
        must_not_hallucinate=llm_plan.must_not_hallucinate,
        delegate_to_model=llm_plan.delegate_to_model,
        args=args,
    )


def build_plan(message: str) -> AgentPlan:
    """Build a plan through the LLM planner, with local-chat fallback only."""

    normalized, corrections = normalize_query(message)
    mode = os.environ.get("MAOMIAI_PLANNER_MODE", "llm_first").strip().lower()
    if mode in {"llm", "llm_first"}:
        plan = _llm_plan(message)
        if plan:
            return plan
    return _fallback_local_chat(normalized, corrections)
