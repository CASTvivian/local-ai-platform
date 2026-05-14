"""Browser runtime request and result models."""

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


class BrowserFetchRequest(BaseModel):
    """Read-only public web fetch request."""

    url: str
    run_id: Optional[str] = None
    session_id: Optional[str] = None
    timeout: int = 20
    max_bytes: int = 300000


class BrowserSnapshotRequest(BaseModel):
    """Snapshot lookup request."""

    snapshot_id: str


class BrowserRuntimeResult(BaseModel):
    """Normalized browser runtime result."""

    ok: bool
    snapshot_id: Optional[str] = None
    url: Optional[str] = None
    status_code: Optional[int] = None
    title: Optional[str] = None
    text: Optional[str] = None
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
