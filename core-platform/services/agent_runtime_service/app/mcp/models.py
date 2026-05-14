"""Models for the Agent Runtime MCP-style tool registry."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class MCPTool(BaseModel):
    """Registered runtime tool metadata."""

    name: str
    description: str
    endpoint: Optional[str] = None
    method: str = "POST"
    input_schema: Dict[str, Any] = Field(default_factory=dict)
    risk: str = "low"
    enabled: bool = True
    requires_approval: bool = False
    tags: List[str] = Field(default_factory=list)


class MCPInvokeRequest(BaseModel):
    """Request to invoke a registered runtime tool."""

    tool: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    run_id: Optional[str] = None
    session_id: Optional[str] = None


class MCPInvokeResult(BaseModel):
    """Normalized MCP tool invocation result."""

    ok: bool
    tool: str
    result: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None
    approval_required: bool = False
    approval_id: Optional[str] = None
