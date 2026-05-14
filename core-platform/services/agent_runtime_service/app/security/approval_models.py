"""Approval models for Agent Runtime restricted actions."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ApprovalRequest(BaseModel):
    """Request to approve a restricted tool action."""

    action: str
    tool: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    risk: str = "medium"


class ApprovalDecision(BaseModel):
    """Local reviewer decision for a pending approval."""

    approval_id: str
    approved: bool
    reviewer: str = "local_user"
    reason: Optional[str] = None


class ApprovalRecord(BaseModel):
    """Persisted approval record."""

    approval_id: str
    created_at: str
    action: str
    tool: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    risk: str
    approved: bool = False
    resolved_at: Optional[str] = None
    reviewer: Optional[str] = None
    reason: Optional[str] = None


def build_record(request: ApprovalRequest) -> ApprovalRecord:
    """Build a new pending approval record."""

    return ApprovalRecord(
        approval_id=str(uuid.uuid4()),
        created_at=datetime.utcnow().isoformat(),
        action=request.action,
        tool=request.tool,
        payload=request.payload,
        risk=request.risk,
    )
