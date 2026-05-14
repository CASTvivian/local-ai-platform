"""Build compact observations from executed agent steps."""

from __future__ import annotations

from typing import List

from ..models import AgentPlan, ToolResult
from .models import Observation


def summarize_tool_result(result: ToolResult) -> str:
    if not result.ok:
        return f"{result.tool}: failed: {result.error or 'unknown error'}"
    data = result.data or {}
    if "items" in data and isinstance(data["items"], list):
        return f"{result.tool}: returned {len(data['items'])} items"
    if "matches" in data and isinstance(data["matches"], list):
        return f"{result.tool}: returned {len(data['matches'])} matches"
    if "answer" in data:
        return f"{result.tool}: returned answer"
    if "response" in data:
        return f"{result.tool}: returned response"
    if "current" in data or "daily" in data:
        return f"{result.tool}: returned weather data"
    if "snapshot_id" in data:
        return f"{result.tool}: returned snapshot {data.get('snapshot_id')}"
    if data.get("approval_required"):
        return f"{result.tool}: requires approval {data.get('approval_id')}"
    return f"{result.tool}: ok"


def build_observation(
    step: int,
    plan: AgentPlan,
    results: List[ToolResult],
    answer: str,
    blocked: bool,
    reason: str,
    resolved: bool,
) -> Observation:
    summaries = [summarize_tool_result(item) for item in results]
    failures = [item.error or "" for item in results if not item.ok]
    return Observation(
        step=step,
        plan=plan.model_dump(),
        tool_results=[item.model_dump() for item in results],
        summary="; ".join(summaries),
        answer=answer,
        blocked=blocked,
        resolved=resolved,
        needs_more_steps=not resolved,
        error=reason or "; ".join(failures) or None,
    )
