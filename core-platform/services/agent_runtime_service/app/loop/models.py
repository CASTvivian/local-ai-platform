"""Observation and replanning models for Agent Runtime."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Observation(BaseModel):
    step: int
    plan: Dict[str, Any]
    tool_results: List[Dict[str, Any]] = Field(default_factory=list)
    summary: str = ""
    answer: str = ""
    blocked: bool = False
    resolved: bool = False
    needs_more_steps: bool = False
    error: Optional[str] = None


class ReplanDecision(BaseModel):
    resolved: bool = False
    final_answer: Optional[str] = None
    next_intent: Optional[str] = None
    next_tools: List[str] = Field(default_factory=list)
    reason: str = ""
    args: Dict[str, Any] = Field(default_factory=dict)
    confidence: float = 0.5
