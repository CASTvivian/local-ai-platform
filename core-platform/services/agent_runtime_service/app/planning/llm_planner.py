"""LLM-driven structured planner for Agent Runtime."""

from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, ValidationError

from ..capability.registry import list_capabilities
from ..mcp.registry import list_tools
from ..health.planner_health import record_planner_error, clear_planner_error, is_circuit_open


LAST_PLANNER_ERROR: Optional[str] = None
BUILTIN_TOOLS = {
    "time.now",
    "time.date_math",
    "catalog.search",
    "capability.status",
    "capability.match",
}


class LLMPlan(BaseModel):
    intent: str
    tools: List[str] = Field(default_factory=list)
    reason: str = "llm structured planner"
    must_not_hallucinate: bool = True
    delegate_to_model: bool = False
    args: Dict[str, Any] = Field(default_factory=dict)
    confidence: float = 0.0


def _planner_schema() -> Dict[str, Any]:
    return {
        "intent": "string",
        "tools": ["tool.id"],
        "reason": "short planner reason",
        "must_not_hallucinate": "boolean",
        "delegate_to_model": "boolean",
        "args": {
            "offset_days": "integer when date arithmetic is needed",
            "query": "string when a retrieval/search tool needs a query",
            "location": "string when a weather tool needs a location",
            "command": "string when a restricted shell tool is requested",
        },
        "confidence": "number from 0 to 1",
    }


def planner_context() -> Dict[str, Any]:
    return {
        "available_tools": list_tools(),
        "available_capabilities": list_capabilities(enabled_only=True),
    }


def _build_prompt(message: str) -> str:
    context = planner_context()
    payload = {
        "role": "MAOMIAI Agent Planner",
        "instruction": [
            "Return one strict JSON object only.",
            "Select tools from the supplied tool registry.",
            "Use capability metadata to decide whether model, memory, web, weather, file, browser, shell, or catalog tools are needed.",
            "For current clock questions, use the current-time tool.",
            "For calendar arithmetic, use the date-math tool and provide integer offset_days in args.",
            "For fresh factual questions, use web evidence tools.",
            "For project-specific questions, use memory or capability tools.",
            "For restricted local execution, use an approval-gated tool.",
            "If no tool is needed, delegate to model generation.",
            "Never invent real-time facts or project facts without tools.",
        ],
        "schema": _planner_schema(),
        **context,
        "user_message": message,
    }
    return json.dumps(payload, ensure_ascii=False)


def extract_json_object(raw: str) -> Optional[Dict[str, Any]]:
    text = (raw or "").strip()
    if not text:
        return None
    candidates = [text]
    start = text.find("{")
    end = text.rfind("}")
    if start >= 0 and end > start:
        candidates.append(text[start : end + 1])
    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except Exception:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def call_planner_model(prompt: str) -> Optional[str]:
    global LAST_PLANNER_ERROR
    if is_circuit_open():
        raise RuntimeError("planner circuit is open; model gateway recently failed")
    endpoint = os.environ.get("MAOMIAI_PLANNER_MODEL_ENDPOINT", "http://127.0.0.1:18080/generate")
    timeout = float(os.environ.get("MAOMIAI_PLANNER_TIMEOUT", "30"))
    payload = json.dumps(
        {
            "prompt": prompt,
            "profile": os.environ.get("MAOMIAI_PLANNER_PROFILE", "reasoning"),
        },
        ensure_ascii=False,
    ).encode("utf-8")
    request = urllib.request.Request(
        endpoint,
        data=payload,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8", errors="replace"))
        clear_planner_error()
    except Exception as exc:
        record_planner_error(str(exc))
        LAST_PLANNER_ERROR = f"model_gateway_error: {exc}"
        return None
    for key in ("response", "output", "text", "answer"):
        value = data.get(key)
        if isinstance(value, str) and value.strip():
            return value
    message = data.get("message")
    if isinstance(message, dict):
        content = message.get("content")
        if isinstance(content, str) and content.strip():
            return content
    return None


def llm_create_plan(message: str) -> Optional[LLMPlan]:
    global LAST_PLANNER_ERROR
    LAST_PLANNER_ERROR = None
    raw = call_planner_model(_build_prompt(message))
    parsed = extract_json_object(raw or "")
    if not parsed:
        if not LAST_PLANNER_ERROR:
            LAST_PLANNER_ERROR = "planner_output_empty_or_not_json"
        return None
    try:
        plan = LLMPlan.model_validate(parsed)
    except ValidationError as exc:
        LAST_PLANNER_ERROR = f"planner_schema_error: {exc}"
        return None
    if not validate_tool_names(plan.tools):
        LAST_PLANNER_ERROR = "planner_returned_unknown_tool"
        return None
    return plan


def validate_tool_names(tools: List[str]) -> bool:
    known_tools = {item["name"] for item in list_tools()} | BUILTIN_TOOLS
    return all(tool in known_tools for tool in tools)


def get_last_planner_error() -> Optional[str]:
    return LAST_PLANNER_ERROR
