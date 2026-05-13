"""Pydantic models for the MAOMIAI agent runtime service."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentRunRequest(BaseModel):
    """Input payload for agent planning and execution."""

    message: str
    profile: Optional[str] = None
    model: Optional[str] = None
    session_id: Optional[str] = None
    mode: str = "auto"


class AgentPlan(BaseModel):
    """Planner output describing how to handle a message."""

    intent: str
    normalized_query: str
    tools: List[str] = Field(default_factory=list)
    reason: str
    must_not_hallucinate: bool = True
    delegate_to_model: bool = False
    args: Dict[str, Any] = Field(default_factory=dict)


class ToolResult(BaseModel):
    """Normalized tool execution result."""

    tool: str
    ok: bool
    data: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None


class AgentRunResponse(BaseModel):
    """End-to-end agent runtime response."""

    ok: bool
    answer: str
    plan: AgentPlan
    tool_results: List[ToolResult] = Field(default_factory=list)
    delegated_to_model: bool = False
    error: Optional[str] = None
