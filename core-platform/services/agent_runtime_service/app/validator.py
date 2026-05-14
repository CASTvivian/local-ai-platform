"""No-hallucination checks for the MAOMIAI agent runtime."""

from __future__ import annotations

from .models import AgentPlan, ToolResult


def should_block_hallucination(
    plan: AgentPlan,
    results: list[ToolResult],
) -> tuple[bool, str]:
    """Decide whether the runtime must refuse to fabricate an answer."""

    if not plan.must_not_hallucinate:
        return False, ""

    if plan.intent == "weather":
        if not any(result.tool == "weather.query" and result.ok for result in results):
            return True, "Weather answer requires weather.query evidence."
        return False, ""

    if plan.intent == "web_fact":
        if not any(result.tool == "web.search" and result.ok for result in results):
            return True, "Web factual answer requires web.search evidence."
        return False, ""

    if plan.intent in ("project_knowledge", "catalog_knowledge"):
        if not any(result.ok for result in results):
            return True, "Project-specific answer requires repo memory or catalog evidence."

    return False, ""


def build_validation(answer: str, blocked: bool, reason: str, retryable: bool = False) -> dict:
    """Build a normalized validation payload for run_store persistence."""

    return {
        "resolved": bool(answer) and not retryable,
        "retryable": retryable,
        "blocked": blocked,
        "reason": reason,
        "final_answer": answer,
    }


def should_retry(validation: dict) -> bool:
    """Return whether Agent Runtime should retry a step."""

    if validation.get("resolved"):
        return False
    if validation.get("retryable"):
        return True
    return False
