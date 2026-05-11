"""Pydantic data models for artifact registry service."""

from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class ArtifactType(str, Enum):
    execution_result = "execution_result"
    code_artifact = "code_artifact"
    test_result = "test_result"
    documentation = "documentation"
    log_file = "log_file"
    config_file = "config_file"
    model_output = "model_output"
    data_export = "data_export"
    custom = "custom"


class Lifecycle(str, Enum):
    draft = "draft"
    active = "active"
    archived = "archived"
    deleted = "deleted"


class ArtifactRecord(BaseModel):
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    source: str = "runtime_execution"
    version: str = "0.1.0"
    enabled: bool = True
    type: ArtifactType = ArtifactType.execution_result
    path: str = ""
    lifecycle: Lifecycle = Lifecycle.active
    trace_id: str = ""
    run_id: str = ""
    payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())
    updated_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())

    @field_validator("path")
    @classmethod
    def validate_path(cls, v: str) -> str:
        if v and not v.startswith("/"):
            # Absolute path required
            return v
        return v


class StoreFile(BaseModel):
    store_version: str = "1.0.0"
    items: List[ArtifactRecord] = Field(default_factory=list)


# Request models
class RegisterExecutionResultRequest(BaseModel):
    name: Optional[str] = None
    title: Optional[str] = None
    type: ArtifactType = ArtifactType.execution_result
    path: str = ""
    lifecycle: Lifecycle = Lifecycle.active
    trace_id: str = ""
    run_id: str = ""
    source: str = "runtime_execution"
    version: str = "0.1.0"
    payload: Dict[str, Any] = Field(default_factory=dict)

    @field_validator("name")
    @classmethod
    def validate_name(cls, v: Optional[str], info) -> str:
        # Use title as fallback
        if not v:
            payload = info.data.get("payload", {})
            return payload.get("title") or "execution-result"
        return v


class UpdateLifecycleRequest(BaseModel):
    lifecycle: Lifecycle = Field(..., description="New lifecycle state")
    reason: Optional[str] = None


class FileStatus(BaseModel):
    path: str
    exists: bool
    size_bytes: int
    download_ready: bool
    note: str = ""


class DownloadInfo(BaseModel):
    item_id: str
    path: str
    exists: bool
    size_bytes: int
    download_ready: bool
    message: str = ""


# Response models
class ArtifactListResponse(BaseModel):
    items: List[ArtifactRecord]
    count: int

    @classmethod
    def from_records(cls, records: List[ArtifactRecord]) -> "ArtifactListResponse":
        return cls(items=records, count=len(records))


class FileStatusResponse(BaseModel):
    ok: bool
    item_id: str
    path: str
    exists: bool
    size_bytes: int
    download_ready: bool
    note: str = ""


class LifecycleUpdateResponse(BaseModel):
    ok: bool
    item: Optional[ArtifactRecord] = None
    item_id: str
    error: Optional[str] = None
