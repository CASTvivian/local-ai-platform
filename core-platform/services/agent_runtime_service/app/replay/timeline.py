"""Build replayable timelines from run_store and execution audit data."""

from __future__ import annotations

from typing import Any, Dict, List

from .models import RunTimeline, TimelineEvent
from ..run_store.store import load_run
from ..runtime.execution_store import list_executions


def _append_event(
    events: List[TimelineEvent],
    event_type: str,
    title: str,
    detail: Dict[str, Any],
) -> None:
    events.append(
        TimelineEvent(
            index=len(events),
            type=event_type,
            title=title,
            detail=detail or {},
        )
    )


def _step_observation(step) -> Dict[str, Any]:
    direct = getattr(step, "observation", None)
    if isinstance(direct, dict) and direct:
        return direct
    tool_result = step.tool_result or {}
    observation = tool_result.get("observation")
    return observation if isinstance(observation, dict) else {}


def _step_replan(step) -> Dict[str, Any]:
    direct = getattr(step, "replan", None)
    if isinstance(direct, dict) and direct:
        return direct
    tool_result = step.tool_result or {}
    replan = tool_result.get("replan")
    return replan if isinstance(replan, dict) else {}


def build_run_timeline(run_id: str) -> RunTimeline:
    run = load_run(run_id)
    if not run:
        return RunTimeline(
            ok=False,
            run_id=run_id,
            events=[
                TimelineEvent(
                    index=0,
                    type="error",
                    title="Run not found",
                    detail={"run_id": run_id},
                )
            ],
        )

    events: List[TimelineEvent] = []
    _append_event(
        events,
        "run.created",
        "Run created",
        {
            "run_id": run.run_id,
            "session_id": run.session_id,
            "input": run.input,
            "created_at": str(run.created_at),
        },
    )

    for step in run.steps:
        plan = step.plan or {}
        validation = step.validation or {}
        tool_result = step.tool_result or {}
        _append_event(
            events,
            "plan",
            f"Step {step.step}: plan",
            {
                "step": step.step,
                "intent": plan.get("intent"),
                "tools": plan.get("tools"),
                "reason": plan.get("reason"),
                "args": plan.get("args"),
            },
        )
        _append_event(
            events,
            "tool_result",
            f"Step {step.step}: tool result",
            {
                "step": step.step,
                "tool_result": tool_result,
            },
        )
        observation = _step_observation(step)
        if observation:
            _append_event(
                events,
                "observation",
                f"Step {step.step}: observation",
                {
                    "step": step.step,
                    "observation": observation,
                },
            )
        _append_event(
            events,
            "validation",
            f"Step {step.step}: validation",
            {
                "step": step.step,
                "validation": validation,
            },
        )
        replan = _step_replan(step)
        if replan:
            _append_event(
                events,
                "replan",
                f"Step {step.step}: replan",
                {
                    "step": step.step,
                    "replan": replan,
                },
            )

    for item in list_executions(run_id=run_id, limit=500):
        _append_event(
            events,
            "execution",
            f"Execution: {item.get('tool')}",
            {
                "execution_id": item.get("execution_id"),
                "tool": item.get("tool"),
                "ok": item.get("ok"),
                "status": item.get("status"),
                "sandbox_id": item.get("sandbox_id"),
                "returncode": item.get("returncode"),
                "stdout": item.get("stdout"),
                "stderr": item.get("stderr"),
                "error": item.get("error"),
            },
        )

    _append_event(
        events,
        "run.completed",
        "Run completed",
        {
            "status": run.status,
            "final_answer": run.final_answer,
            "updated_at": str(run.updated_at),
        },
    )
    return RunTimeline(
        ok=True,
        run_id=run.run_id,
        session_id=run.session_id,
        status=run.status,
        final_answer=run.final_answer,
        events=events,
    )
