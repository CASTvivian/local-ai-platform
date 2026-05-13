"""Service orchestration for MAOMIAI agent runtime requests."""

from __future__ import annotations

from .executor import execute_plan
from .models import AgentRunRequest, AgentRunResponse
from .planner import build_plan
from .renderer import render_answer
from .validator import should_block_hallucination


def run_agent(request: AgentRunRequest) -> AgentRunResponse:
    """Plan, execute, validate, and render a single agent request."""

    plan = build_plan(request.message)
    results = execute_plan(plan, request)
    blocked, reason = should_block_hallucination(plan, results)
    answer = render_answer(plan, results)

    if blocked and not answer:
        answer = f"我不能在没有证据或工具的情况下回答这个问题。原因：{reason}"

    return AgentRunResponse(
        ok=True,
        answer=answer,
        plan=plan,
        tool_results=results,
        delegated_to_model=plan.delegate_to_model,
    )
