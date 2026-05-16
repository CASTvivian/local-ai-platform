from __future__ import annotations
import json
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Callable


@dataclass
class LoopObservation:
    step_index: int
    tool: str
    ok: bool
    data: dict[str, Any] | None = None
    error: str | None = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def model_dump(self) -> dict[str, Any]:
        return {
            "step_index": self.step_index,
            "tool": self.tool,
            "ok": self.ok,
            "data": self.data,
            "error": self.error,
            "created_at": self.created_at,
        }


@dataclass
class AgentLoopResult:
    ok: bool
    status: str
    observations: list[LoopObservation]
    final_answer: str | None = None
    replan_count: int = 0
    error: str | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "status": self.status,
            "observations": [x.model_dump() for x in self.observations],
            "final_answer": self.final_answer,
            "replan_count": self.replan_count,
            "error": self.error,
        }


def default_validator(observations: list[LoopObservation]) -> dict[str, Any]:
    if not observations:
        return {
            "ok": False,
            "status": "no_observations",
            "should_replan": False,
            "reason": "no observations produced",
        }
    failed = [x for x in observations if not x.ok]
    if failed:
        return {
            "ok": False,
            "status": "tool_failed",
            "should_replan": True,
            "reason": failed[-1].error or "tool failed",
        }
    return {
        "ok": True,
        "status": "validated",
        "should_replan": False,
        "reason": "all observations passed",
    }


def run_agentic_loop(
    initial_plan: dict[str, Any],
    execute_step: Callable[[dict[str, Any]], dict[str, Any]],
    replan: Callable[[dict[str, Any], list[dict[str, Any]]], dict[str, Any]] | None = None,
    validator: Callable[[list[LoopObservation]], dict[str, Any]] = default_validator,
    max_iterations: int = 3,
) -> AgentLoopResult:
    """Run a minimal agentic loop.

    This is the Claude/Claw-style foundation:
    plan -> act -> observe -> validate -> optional replan.
    """
    plan = dict(initial_plan or {})
    all_observations: list[LoopObservation] = []
    replan_count = 0

    for iteration in range(max_iterations):
        steps = plan.get("steps") or []
        if not isinstance(steps, list):
            return AgentLoopResult(
                ok=False,
                status="invalid_plan",
                observations=all_observations,
                error="plan.steps must be a list",
            )

        iter_start = len(all_observations)
        for index, step in enumerate(steps):
            tool = str(step.get("tool") or "unknown")
            try:
                raw = execute_step(step)
                ok = bool(raw.get("ok"))
                all_observations.append(
                    LoopObservation(
                        step_index=index,
                        tool=tool,
                        ok=ok,
                        data=raw.get("data") if isinstance(raw.get("data"), dict) else raw,
                        error=raw.get("error"),
                    )
                )
            except Exception as exc:
                all_observations.append(
                    LoopObservation(
                        step_index=index,
                        tool=tool,
                        ok=False,
                        data=None,
                        error=str(exc),
                    )
                )

        # Validate only current iteration's observations
        current_observations = all_observations[iter_start:]
        validation = validator(current_observations)

        if validation.get("ok"):
            return AgentLoopResult(
                ok=True,
                status="completed",
                observations=all_observations,
                final_answer=validation.get("final_answer") or validation.get("reason"),
                replan_count=replan_count,
            )

        if not validation.get("should_replan") or replan is None:
            return AgentLoopResult(
                ok=False,
                status=str(validation.get("status") or "failed"),
                observations=all_observations,
                error=str(validation.get("reason") or "validation failed"),
                replan_count=replan_count,
            )

        replan_count += 1
        plan = replan(plan, [x.model_dump() for x in all_observations])

    return AgentLoopResult(
        ok=False,
        status="max_iterations_reached",
        observations=all_observations,
        error="agentic loop reached max iterations",
        replan_count=replan_count,
    )


def serialize_loop_result(result: AgentLoopResult) -> dict[str, Any]:
    return result.model_dump()


def loop_result_to_json(result: AgentLoopResult) -> str:
    return json.dumps(result.model_dump(), ensure_ascii=False, indent=2)
