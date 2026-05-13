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

    if plan.intent in ("weather", "web_fact"):
        return True, "This question requires a live tool that is not enabled."

    if plan.intent in ("project_knowledge", "catalog_knowledge"):
        if not any(result.ok for result in results):
            return True, "Project-specific answer requires repo memory or catalog evidence."

    return False, ""
