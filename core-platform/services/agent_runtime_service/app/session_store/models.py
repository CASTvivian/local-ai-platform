"""Session store models for Agent Runtime."""

from __future__ import annotations

from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class AgentSessionState(BaseModel):
    """A session containing multiple Agent Runtime runs."""

    session_id: str
    run_ids: List[str] = Field(default_factory=list)
    created_at: datetime
    updated_at: datetime
