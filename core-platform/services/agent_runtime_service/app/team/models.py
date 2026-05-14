from pydantic import BaseModel, Field
from typing import Any, Dict, List, Optional
import uuid
from datetime import datetime


class AgentSpec(BaseModel):
    id: str
    name: str
    role: str
    capability_tags: List[str] = Field(default_factory=list)
    max_steps: int = 4
    enabled: bool = True


class AgentTeamSpec(BaseModel):
    id: str
    name: str
    description: str = ""
    enabled: bool = True
    agents: List[AgentSpec] = Field(default_factory=list)


class TeamRunRequest(BaseModel):
    input: str
    session_id: str = "desktop-default"
    team_id: Optional[str] = None
    max_rounds: int = 3
    metadata: Dict[str, Any] = Field(default_factory=dict)


class TeamMessage(BaseModel):
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    team_run_id: str
    round: int
    from_agent: str
    to_agent: str
    type: str
    content: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())


class TeamRunState(BaseModel):
    team_run_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    session_id: str
    team_id: str
    input: str
    status: str = "running"
    current_round: int = 0
    final_answer: Optional[str] = None
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    messages: List[TeamMessage] = Field(default_factory=list)
    agent_outputs: Dict[str, Any] = Field(default_factory=dict)
    timeline: List[Dict[str, Any]] = Field(default_factory=list)