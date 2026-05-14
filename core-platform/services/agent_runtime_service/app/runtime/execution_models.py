"""Execution audit models for Agent Runtime replay."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class ExecutionRecord(BaseModel):
    """Persisted execution record for an approved runtime action."""

    execution_id: str
    approval_id: Optional[str] = None
    run_id: Optional[str] = None
    session_id: Optional[str] = None
    tool: str
    command: Optional[str] = None
    status: str
    ok: bool
    returncode: Optional[int] = None
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    error: Optional[str] = None
    sandbox_id: Optional[str] = None
    created_at: str
    metadata: Dict[str, Any] = Field(default_factory=dict)


def new_execution_record(
    tool: str,
    status: str,
    ok: bool,
    approval_id: Optional[str] = None,
    run_id: Optional[str] = None,
    session_id: Optional[str] = None,
    command: Optional[str] = None,
    returncode: Optional[int] = None,
    stdout: Optional[str] = None,
    stderr: Optional[str] = None,
    error: Optional[str] = None,
    sandbox_id: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> ExecutionRecord:
    """Create a new execution audit record."""

    return ExecutionRecord(
        execution_id=str(uuid.uuid4()),
        approval_id=approval_id,
        run_id=run_id,
        session_id=session_id,
        tool=tool,
        command=command,
        status=status,
        ok=ok,
        returncode=returncode,
        stdout=stdout,
        stderr=stderr,
        error=error,
        sandbox_id=sandbox_id,
        created_at=datetime.utcnow().isoformat(),
        metadata=metadata or {},
    )
