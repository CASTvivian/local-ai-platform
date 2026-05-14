"""Capability registry models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Capability(BaseModel):
    """A model, tool, workflow, skill, or catalog capability."""

    id: str
    name: str
    type: str
    description: str
    runtime: str
    target: str
    priority: int = 50
    enabled: bool = True
    tags: List[str] = Field(default_factory=list)
    input_schema: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class CapabilityMatchRequest(BaseModel):
    """Request to match a user task to runtime capabilities."""

    query: str
    intent: Optional[str] = None
    tags: List[str] = Field(default_factory=list)
    limit: int = 5


class CapabilityMatchResult(BaseModel):
    """Capability matching response."""

    ok: bool
    query: str
    matches: List[Capability] = Field(default_factory=list)
