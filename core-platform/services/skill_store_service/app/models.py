"""Pydantic data models for skill store service."""

from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class SkillSource(str, Enum):
    """Source of the skill definition."""
    desktop_skill_md = "desktop_skill_md"
    skill_marketplace = "skill_marketplace"
    manual = "manual"
    ai_generated = "ai_generated"


class SignatureStatus(str, Enum):
    """Signature verification status."""
    unsigned = "unsigned"
    verified = "verified"
    revoked = "revoked"
    pending = "pending"


class SkillStatus(str, Enum):
    """Status of the skill."""
    active = "active"
    disabled = "disabled"
    deprecated = "deprecated"
    archived = "archived"


class AgentBinding(BaseModel):
    """Agent binding configuration."""
    agent_id: str = Field(..., min_length=1)
    enabled: bool = True
    config: Dict[str, Any] = Field(default_factory=dict)


class SkillRecord(BaseModel):
    """Complete skill record."""
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    description: str = ""
    source: SkillSource = SkillSource.desktop_skill_md
    version: str = "0.1.0"
    enabled: bool = True
    status: SkillStatus = SkillStatus.active
    signature_status: SignatureStatus = SignatureStatus.unsigned
    agents: List[str] = Field(default_factory=list)
    tags: List[str] = Field(default_factory=list)
    agent_bindings: List[AgentBinding] = Field(default_factory=list)
    payload: Dict[str, Any] = Field(default_factory=dict)
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())
    updated_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())

    @field_validator("version")
    @classmethod
    def validate_version(cls, v: str) -> str:
        """Validate semantic version format."""
        import re
        if not re.match(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$', v):
            return "0.1.0"
        return v


class StoreFile(BaseModel):
    """Store file structure."""
    store_version: str = "1.0.0"
    items: List[SkillRecord] = Field(default_factory=list)


# Request models
class ParseSkillMdRequest(BaseModel):
    """Request to parse SKILL.md content."""
    text: str = Field(..., min_length=1)
    source: Optional[str] = None


class InstallSkillMdRequest(BaseModel):
    """Request to install a skill from SKILL.md content."""
    text: str = Field(..., min_length=1)
    source: SkillSource = SkillSource.desktop_skill_md
    signature: Optional[str] = None
    agent_bindings: List[AgentBinding] = Field(default_factory=list)


class UpdateSkillRequest(BaseModel):
    """Request to update skill metadata."""
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    status: Optional[SkillStatus] = None


class EnableSkillRequest(BaseModel):
    """Request to enable a skill."""
    agent_bindings: Optional[List[AgentBinding]] = None


# Response models
class ParsedSkillMd(BaseModel):
    """Parsed SKILL.md content."""
    name: str
    version: str
    description: str
    agents: List[str]
    tags: List[str]
    format: str = "SKILL.md"


class SkillListResponse(BaseModel):
    """Response for skill list endpoint."""
    items: List[SkillRecord]
    count: int

    @classmethod
    def from_records(cls, records: List[SkillRecord]) -> "SkillListResponse":
        return cls(items=records, count=len(records))


class SkillInstallResponse(BaseModel):
    """Response for skill installation."""
    ok: bool
    skill: Optional[SkillRecord] = None
    item_id: Optional[str] = None
    error: Optional[str] = None


class SkillEnableResponse(BaseModel):
    """Response for skill enable/disable."""
    ok: bool
    changed: bool = False
    item_id: str
    skill: Optional[SkillRecord] = None
    error: Optional[str] = None
