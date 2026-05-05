"""Pydantic data models for code review gate service."""

from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class RiskLevel(str, Enum):
    """Risk level assessment."""
    low = "low"
    medium = "medium"
    high = "high"
    critical = "critical"


class ReviewDecision(str, Enum):
    """Decision for code review."""
    approve = "approve"
    reject = "reject"
    request_changes = "request_changes"
    needs_review = "needs_review"


class FindingType(str, Enum):
    """Types of security findings."""
    dangerous_shell = "dangerous_shell"
    secret_leak = "secret_leak"
    dynamic_exec = "dynamic_exec"
    file_access = "file_access"
    network_access = "network_access"
    injection = "injection"
    path_traversal = "path_traversal"


class Finding(BaseModel):
    """Security finding."""
    type: FindingType
    pattern: str
    line: Optional[int] = None
    file: Optional[str] = None
    severity: RiskLevel = RiskLevel.medium
    description: str = ""


class ReviewRequest(BaseModel):
    """Request for code review."""
    diff: str = Field(..., min_length=1, description="Code diff to review")
    files: List[str] = Field(default_factory=list, description="Affected files")
    commit_id: Optional[str] = None
    author: Optional[str] = None
    branch: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ReviewResult(BaseModel):
    """Result of code review."""
    review_id: str
    risk_level: RiskLevel
    decision: ReviewDecision
    findings: List[Finding] = Field(default_factory=list)
    test_suggestions: List[str] = Field(default_factory=list)
    summary: str = ""
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class StoreFile(BaseModel):
    """Store file structure."""
    store_version: str = "1.0.0"
    items: List[ReviewResult] = Field(default_factory=list)


# Request models
class SuggestTestsRequest(BaseModel):
    """Request for test suggestions."""
    code: str = Field(..., min_length=1)
    language: str = "python"
    coverage_threshold: float = 0.8


class TestSuggestion(BaseModel):
    """Test suggestion."""
    type: str  # unit, integration, e2e
    description: str
    code: str = ""
    priority: str = "medium"  # high, medium, low


class ReviewSummary(BaseModel):
    """Summary of review results."""
    total_reviews: int
    high_risk_count: int
    medium_risk_count: int
    low_risk_count: int
    approval_rate: float
    average_findings: float
