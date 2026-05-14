"""Replay timeline response models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TimelineEvent(BaseModel):
    index: int
    type: str
    title: str
    detail: Dict[str, Any] = Field(default_factory=dict)


class RunTimeline(BaseModel):
    ok: bool
    run_id: str
    session_id: Optional[str] = None
    status: Optional[str] = None
    final_answer: Optional[str] = None
    events: List[TimelineEvent] = Field(default_factory=list)
