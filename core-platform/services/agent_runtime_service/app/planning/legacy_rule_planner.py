"""Legacy rule planner isolated from the public planner runtime.

This file is retained only for rollback/debug during C25-C14 migration.
Production planner.py must not contain query keyword routing.

Functions here were extracted from planner.py in C25-C14-B2:
  - _keyword_plan: hardcoded Chinese query keyword matching
  - _llm_plan: LLM planner bridge
  - _fallback_local_chat: final fallback to model.generate
  - build_plan_legacy: composite legacy chain (keyword -> llm -> fallback)
"""

from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from ..models import AgentPlan
from .llm_planner import get_last_planner_error, llm_create_plan
from ..health.planner_health import planner_runtime_state
from ..policy.loader import load_entity_aliases


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
            "planner_mode": "legacy",
        },
    )


def _keyword_plan(normalized: str, corrections: List[Dict[str, Any]]) -> AgentPlan | None:
    """Handle demo-critical grounded intents without depending on the LLM planner.

    LEGACY: This keyword-matching logic is isolated here for rollback only.
    planner.py must never import or call this directly.
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

    Only used when MAOMIAI_LEGACY_PLANNER=1 is explicitly set.
    This function must not be called from the default planner path.
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
