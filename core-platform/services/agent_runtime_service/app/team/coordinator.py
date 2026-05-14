from __future__ import annotations
from datetime import datetime
from typing import Dict, Any, List
from .models import TeamRunRequest, TeamRunState, TeamMessage, AgentSpec
from .registry import get_team
from .store import save_team_run
from ..capability.models import CapabilityMatchRequest
from ..capability.service import match_capability
from ..models import AgentRunRequest
from ..service import run_agent


def _event(state: TeamRunState, event_type: str, title: str, detail: Dict[str, Any]):
    state.timeline.append(
        {
            "index": len(state.timeline),
            "type": event_type,
            "title": title,
            "detail": detail,
            "created_at": datetime.utcnow().isoformat(),
        }
    )


def _message(state: TeamRunState, round_id: int, from_agent: str, to_agent: str, msg_type: str, content: str, payload: Dict[str, Any] | None = None):
    msg = TeamMessage(
        team_run_id=state.team_run_id,
        round=round_id,
        from_agent=from_agent,
        to_agent=to_agent,
        type=msg_type,
        content=content,
        payload=payload or {},
    )
    state.messages.append(msg)
    return msg


def _match_for_agent(goal: str, agent: AgentSpec):
    result = match_capability(
        CapabilityMatchRequest(
            query=goal,
            tags=agent.capability_tags,
            limit=5,
        )
    )
    return result.model_dump()


def _run_worker(goal: str, session_id: str, team_run_id: str, agent: AgentSpec, context: Dict[str, Any]):
    prompt = (
        "You are a worker agent. Use the available runtime tools if needed.\n"
        f"Agent name: {agent.name}\n"
        f"Agent role: {agent.role}\n"
        f"Task: {goal}\n"
        "Use evidence and tools. Do not invent unsupported facts.\n"
        f"Context: {context}"
    )
    req = AgentRunRequest(
        message=prompt,
        input=prompt,
        session_id=session_id,
        source="team-runtime",
        metadata={
            "team_run_id": team_run_id,
            "agent_id": agent.id,
            "agent_name": agent.name,
        },
    )
    try:
        return run_agent(req).model_dump()
    except Exception as e:
        return {
            "ok": False,
            "answer": "",
            "final_answer": "",
            "error": str(e),
            "agent_id": agent.id,
            "agent_name": agent.name,
            "fallback": True,
            "steps": [
                {
                    "step": 0,
                    "observation": {
                        "error": str(e),
                        "source": "team_worker_failure_isolation"
                    },
                    "validation": {
                        "resolved": False,
                        "retryable": True,
                        "error": str(e)
                    }
                }
            ]
        }


def run_team(req: TeamRunRequest) -> Dict[str, Any]:
    team = get_team(req.team_id)
    if not team:
        return {
            "ok": False,
            "message": "team not found",
        }

    state = TeamRunState(
        session_id=req.session_id,
        team_id=team.id,
        input=req.input,
    )
    try:
        _event(
            state,
            "team.created",
            "Team run created",
            {
                "team_id": team.id,
                "input": req.input,
            },
        )

        enabled_agents = [a for a in team.agents if a.enabled]

        _message(
            state,
            0,
            "user",
            "coordinator",
            "goal",
            req.input,
            {"metadata": req.metadata},
        )

        shared_context: Dict[str, Any] = {
            "goal": req.input,
            "capabilities": {},
            "worker_outputs": {},
        }

        for agent in enabled_agents:
            try:
                caps = _match_for_agent(req.input, agent)
            except Exception as e:
                caps = {
                    "ok": False,
                    "error": str(e),
                    "matches": [],
                }
            shared_context["capabilities"][agent.id] = caps
            _event(
                state,
                "agent.capability_match",
                f"{agent.name} capability match",
                {
                    "agent_id": agent.id,
                    "capabilities": caps,
                },
            )

        for round_id in range(max(1, min(req.max_rounds, 6))):
            state.current_round = round_id

            for agent in enabled_agents:
                if agent.id == "coordinator":
                    continue

                _message(
                    state,
                    round_id,
                    "coordinator",
                    agent.id,
                    "task",
                    req.input,
                    {"context": shared_context},
                )

                output = _run_worker(
                    goal=req.input,
                    session_id=req.session_id,
                    team_run_id=state.team_run_id,
                    agent=agent,
                    context=shared_context,
                )

                state.agent_outputs[agent.id] = output
                shared_context["worker_outputs"][agent.id] = output

                answer_text = output.get("answer") or output.get("final_answer") or output.get("error") or ""
                _message(
                    state,
                    round_id,
                    agent.id,
                    "coordinator",
                    "result",
                    answer_text,
                    {"raw": output},
                )

                _event(
                    state,
                    "agent.output",
                    f"{agent.name} output",
                    {
                        "agent_id": agent.id,
                        "ok": output.get("ok"),
                        "answer": output.get("answer") or output.get("final_answer"),
                        "error": output.get("error"),
                        "fallback": output.get("fallback"),
                        "steps": output.get("steps"),
                    },
                )

            # Single coordination round is enough for now; later C26 can implement recursive delegation.
            break

        final_parts = []
        for agent in enabled_agents:
            if agent.id == "coordinator":
                continue
            output = state.agent_outputs.get(agent.id) or {}
            answer = output.get("answer") or output.get("final_answer")
            error = output.get("error")
            if answer:
                final_parts.append(f"[{agent.name}]\n{answer}")
            elif error:
                final_parts.append(f"[{agent.name}]\nWorker unavailable: {error}")

        state.final_answer = "\n\n".join(final_parts) if final_parts else "Team run completed without worker output."
        state.status = "completed"
        _event(
            state,
            "team.completed",
            "Team run completed",
            {
                "final_answer": state.final_answer,
            },
        )
    except Exception as e:
        state.status = "failed"
        state.final_answer = f"Team run failed but state was preserved: {e}"
        _event(
            state,
            "team.failed",
            "Team run failed",
            {
                "error": str(e),
            },
        )
    state.updated_at = datetime.utcnow().isoformat()
    save_team_run(state)
    return {
        "ok": state.status == "completed",
        "team_run_id": state.team_run_id,
        "team_id": state.team_id,
        "answer": state.final_answer,
        "final_answer": state.final_answer,
        "state": state.model_dump(),
    }