"""Run store models for persistent Agent Runtime execution state."""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class AgentRunStep(BaseModel):
    """A single persisted planner/executor/validator step."""

    step: int
    plan: Dict[str, Any]
    tool_result: Dict[str, Any]
    validation: Dict[str, Any]
    observation: Dict[str, Any] = Field(default_factory=dict)
    replan: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime


class AgentRunState(BaseModel):
    """Persistent state for one Agent Runtime run."""

    run_id: str
    session_id: str
    status: str
    input: str
    current_step: int = 0
    final_answer: Optional[str] = None
    task_graph: List[Dict[str, Any]] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
    steps: List[AgentRunStep] = Field(default_factory=list)
