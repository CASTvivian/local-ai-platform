"""Service orchestration for MAOMIAI agent runtime requests."""

from __future__ import annotations

from datetime import datetime

from .executor import execute_plan
from .loop.models import Observation
from .loop.observer import build_observation
from .loop.replanner import replan
from .models import AgentPlan, AgentRunRequest, AgentRunResponse
from .planner import build_plan
from .renderer import render_answer
from .run_store.models import AgentRunStep
from .run_store.store import create_run, save_run
from .session_store.store import append_run
from .validator import build_validation, should_block_hallucination


MAX_AGENT_STEPS = 6


def _step_dict(
    plan: AgentPlan,
    results,
    validation: dict,
    observation: Observation,
    replan_decision=None,
) -> dict:
    return {
        "plan": plan.model_dump(),
        "tool_results": [item.model_dump() for item in results],
        "validation": validation,
        "observation": observation.model_dump(),
        "replan": replan_decision.model_dump() if replan_decision else None,
    }


def _plan_from_replan(decision, previous_plan: AgentPlan) -> AgentPlan:
    return AgentPlan(
        intent=decision.next_intent or previous_plan.intent,
        normalized_query=previous_plan.normalized_query,
        tools=decision.next_tools or previous_plan.tools,
        reason=decision.reason or "llm replan",
        must_not_hallucinate=True,
        delegate_to_model=False,
        args={
            **(decision.args or {}),
            "planner_source": "llm_replan",
            "planner_confidence": decision.confidence,
        },
    )


async def run_agent_loop(request: AgentRunRequest) -> AgentRunResponse:
    """Run an observation-driven Agent Runtime loop."""

    message = request.message_text()
    session_id = request.session_id or "desktop-default"
    if not message:
        plan = build_plan("")
        answer = "Agent Runtime received an empty input."
        return AgentRunResponse(
            ok=False,
            answer=answer,
            final_answer=answer,
            session_id=session_id,
            plan=plan,
            error="empty_input",
        )

    run_state = create_run(session_id=session_id, user_input=message)
    append_run(session_id, run_state.run_id)

    history: list[dict] = []
    observations: list[Observation] = []
    final_answer = ""
    final_plan = build_plan(message)
    final_results = []
    plan = final_plan

    for step in range(MAX_AGENT_STEPS):
        results = execute_plan(plan, request, run_id=run_state.run_id, session_id=session_id)
        blocked, reason = should_block_hallucination(plan, results)
        answer = render_answer(plan, results)
        if blocked and not answer:
            answer = f"我不能在没有证据或工具的情况下回答这个问题。原因：{reason}"

        resolved = bool(answer) and not blocked
        validation = build_validation(answer, blocked, reason, retryable=not resolved)
        observation = build_observation(
            step=step,
            plan=plan,
            results=results,
            answer=answer,
            blocked=blocked,
            reason=reason,
            resolved=resolved,
        )
        observations.append(observation)

        replan_decision = None
        if not resolved and step < MAX_AGENT_STEPS - 1:
            replan_decision = replan(message, observations)

        step_payload = _step_dict(plan, results, validation, observation, replan_decision)
        run_state.current_step = step
        run_state.steps.append(
            AgentRunStep(
                step=step,
                plan=plan.model_dump(),
                tool_result={
                    "items": [item.model_dump() for item in results],
                    "observation": observation.model_dump(),
                    "replan": replan_decision.model_dump() if replan_decision else None,
                },
                validation=validation,
                created_at=datetime.utcnow(),
            )
        )
        run_state.task_graph.append(
            {
                "step": step,
                "goal": message,
                "intent": plan.intent,
                "tools": plan.tools,
                "reason": plan.reason,
                "observation": observation.summary,
                "replan": replan_decision.model_dump() if replan_decision else None,
            }
        )
        save_run(run_state)

        history.append(step_payload)
        final_answer = answer
        final_plan = plan
        final_results = results

        if resolved:
            run_state.status = "completed"
            run_state.final_answer = final_answer
            save_run(run_state)
            break

        if replan_decision and replan_decision.resolved:
            final_answer = replan_decision.final_answer or answer or "Task resolved."
            run_state.status = "completed"
            run_state.final_answer = final_answer
            save_run(run_state)
            break

        if replan_decision and replan_decision.next_tools:
            plan = _plan_from_replan(replan_decision, plan)
            continue

        if answer:
            run_state.status = "completed"
            run_state.final_answer = answer
            save_run(run_state)
            break

        run_state.status = "failed"
        run_state.final_answer = "Agent loop ended without a resolved answer."
        save_run(run_state)
        break
    else:
        final_answer = "Agent loop exceeded max steps."
        run_state.status = "failed"
        run_state.final_answer = final_answer
        save_run(run_state)

    if not final_answer:
        final_answer = run_state.final_answer or ""

    return AgentRunResponse(
        ok=run_state.status == "completed",
        answer=final_answer,
        final_answer=final_answer,
        run_id=run_state.run_id,
        session_id=session_id,
        plan=final_plan,
        tool_results=final_results,
        steps=history,
        task_graph=run_state.task_graph,
        delegated_to_model=final_plan.delegate_to_model,
        error=None if run_state.status == "completed" else run_state.status,
    )


def run_agent(request: AgentRunRequest) -> AgentRunResponse:
    """Compatibility wrapper for existing synchronous tests."""

    import asyncio

    return asyncio.run(run_agent_loop(request))
