"""Pydantic data models for repo memory service."""

from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class FixResult(str, Enum):
    """Result of fix attempt."""
    unknown = "unknown"
    success = "success"
    failed = "failed"
    partial = "partial"


class RepoRecord(BaseModel):
    """Repository record."""
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    path: str = ""
    description: str = ""
    tags: List[str] = Field(default_factory=list)
    services: List[str] = Field(default_factory=list)
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())
    updated_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class FixRecord(BaseModel):
    """Fix history record."""
    id: str = Field(..., min_length=1)
    repo_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    problem: str = Field(..., min_length=1)
    solution: str = Field(..., min_length=1)
    files_changed: List[str] = Field(default_factory=list)
    commands_run: List[str] = Field(default_factory=list)
    tests_run: List[str] = Field(default_factory=list)
    result: FixResult = FixResult.unknown
    commit_hash: str = ""
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class ContextSnapshot(BaseModel):
    """Context snapshot for repository."""
    id: str = Field(..., min_length=1)
    repo_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    summary: str = Field(..., min_length=1)
    files: List[str] = Field(default_factory=list)
    services: List[str] = Field(default_factory=list)
    tokens_estimate: int = 0
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class KnowledgeEntry(BaseModel):
    """Knowledge base entry."""
    id: str = Field(..., min_length=1)
    repo_id: str = ""
    category: str = "general"
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    tags: List[str] = Field(default_factory=list)
    source: str = "manual"
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class StoreFile(BaseModel):
    """Store file structure."""
    store_version: str = "1.0"
    repos: List[RepoRecord] = Field(default_factory=list)
    fixes: List[FixRecord] = Field(default_factory=list)
    snapshots: List[ContextSnapshot] = Field(default_factory=list)
    knowledge: List[KnowledgeEntry] = Field(default_factory=list)


# Request models
class RegisterRepoRequest(BaseModel):
    """Request to register a repository."""
    name: str = Field(..., min_length=1)
    path: str = ""
    description: str = ""
    tags: List[str] = Field(default_factory=list)
    services: List[str] = Field(default_factory=list)


class RecordFixRequest(BaseModel):
    """Request to record a fix."""
    repo_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    problem: str = Field(..., min_length=1)
    solution: str = Field(..., min_length=1)
    files_changed: List[str] = Field(default_factory=list)
    commands_run: List[str] = Field(default_factory=list)
    tests_run: List[str] = Field(default_factory=list)
    result: FixResult = FixResult.unknown
    commit_hash: str = ""


class SnapshotContextRequest(BaseModel):
    """Request to create context snapshot."""
    repo_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    summary: str = Field(..., min_length=1)
    files: List[str] = Field(default_factory=list)
    services: List[str] = Field(default_factory=list)
    tokens_estimate: int = 0


class AddKnowledgeRequest(BaseModel):
    """Request to add knowledge entry."""
    repo_id: str = ""
    category: str = "general"
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    tags: List[str] = Field(default_factory=list)
    source: str = "manual"


class SearchKnowledgeRequest(BaseModel):
    """Request to search knowledge."""
    query: str = Field(..., min_length=1)
    category: Optional[str] = None
    repo_id: Optional[str] = None
    limit: int = 10
