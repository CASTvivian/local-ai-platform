"""LLM replanner for observation-driven agent loops."""

from __future__ import annotations

import json
from typing import Any, Dict, List

from ..planning.llm_planner import (
    call_planner_model,
    extract_json_object,
    planner_context,
    validate_tool_names,
)
from .models import Observation, ReplanDecision


def build_replan_prompt(user_message: str, observations: List[Observation]) -> str:
    payload = {
        "role": "MAOMIAI Agent Replanner",
        "instruction": [
            "Return one strict JSON object only.",
            "Decide whether the goal is resolved from observations.",
            "If resolved, provide final_answer.",
            "If unresolved, select next tools from the registry and provide args.",
            "Do not invent facts that require tools.",
            "Do not use hardcoded user phrases; use tool schemas and observations.",
        ],
        "schema": {
            "resolved": "boolean",
            "final_answer": "string or null",
            "next_intent": "string or null",
            "next_tools": ["tool.name"],
            "reason": "short reason",
            "args": {},
            "confidence": "number from 0 to 1",
        },
        "context": planner_context(),
        "user_goal": user_message,
        "observations": [item.model_dump() for item in observations],
    }
    return json.dumps(payload, ensure_ascii=False)


def parse_replan(data: Dict[str, Any]) -> ReplanDecision | None:
    if not isinstance(data, dict):
        return None
    tools = data.get("next_tools") or []
    if not isinstance(tools, list):
        tools = []
    if not validate_tool_names([str(item) for item in tools]):
        return None
    args = data.get("args") or {}
    if not isinstance(args, dict):
        args = {}
    try:
        confidence = float(data.get("confidence", 0.5))
    except Exception:
        confidence = 0.5
    return ReplanDecision(
        resolved=bool(data.get("resolved", False)),
        final_answer=data.get("final_answer"),
        next_intent=data.get("next_intent"),
        next_tools=[str(item) for item in tools if str(item).strip()],
        reason=str(data.get("reason") or "llm replanner"),
        args=args,
        confidence=confidence,
    )


def replan(user_message: str, observations: List[Observation]) -> ReplanDecision | None:
    text = call_planner_model(build_replan_prompt(user_message, observations))
    data = extract_json_object(text or "")
    if not data:
        return None
    return parse_replan(data)
