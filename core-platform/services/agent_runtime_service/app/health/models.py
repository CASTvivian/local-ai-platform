from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime


class ComponentHealth(BaseModel):
    name: str
    ok: bool
    status: str
    detail: Dict[str, Any] = Field(default_factory=dict)
    checked_at: str


class PlannerRuntimeState(BaseModel):
    ok: bool
    planner_mode: str
    model_gateway_ok: bool
    circuit_open: bool
    last_error: Optional[str] = None
    fallback_active: bool = False
    checked_at: str
    detail: Dict[str, Any] = Field(default_factory=dict)