"""Pydantic data models for design system service."""

from enum import Enum
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class ColorToken(str, Enum):
    """Color token types."""
    primary = "primary"
    secondary = "secondary"
    accent = "accent"
    success = "success"
    warning = "warning"
    error = "error"
    neutral = "neutral"


class SpacingToken(str, Enum):
    """Spacing token types."""
    xs = "xs"
    sm = "sm"
    md = "md"
    lg = "lg"
    xl = "xl"
    xxl = "xxl"


class ComponentType(str, Enum):
    """Component types."""
    button = "button"
    input = "input"
    card = "card"
    modal = "modal"
    dropdown = "dropdown"
    table = "table"
    form = "form"


class DesignSystem(BaseModel):
    """Design system configuration."""
    id: str = Field(..., min_length=1)
    name: str = Field(..., min_length=1)
    version: str = "1.0.0"
    description: str = ""
    source: str = "manual"
    enabled: bool = True
    created_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())
    updated_at: float = Field(default_factory=lambda: datetime.utcnow().timestamp())


class BrandProfile(BaseModel):
    """Brand configuration."""
    id: str
    colors: Dict[str, str] = Field(default_factory=dict)
    fonts: Dict[str, str] = Field(default_factory=dict)
    border_radius: Dict[str, str] = Field(default_factory=dict)
    spacing: Dict[str, str] = Field(default_factory=dict)
    shadows: List[str] = Field(default_factory=list)
    logo: str = ""


class DesignToken(BaseModel):
    """Design token definition."""
    id: str
    category: str = "colors"  # colors, fonts, spacing, radius, shadows
    name: str
    value: Any
    description: str = ""
    tokens: Dict[str, Any] = Field(default_factory=dict)


class ComponentSpec(BaseModel):
    """Component specification."""
    id: str
    component_type: ComponentType
    name: str
    props: Dict[str, Any] = Field(default_factory=dict)
    variants: str = Field(default="")
    description: str = ""


class ParsedDesignMd(BaseModel):
    """Parsed DESIGN.md content."""
    name: str
    version: str
    description: str
    colors: Dict[str, str] = Field(default_factory=dict)
    fonts: Dict[str, str] = Field(default_factory=dict)
    spacing: Dict[str, str] = Field(default_factory=dict)
    border_radius: Dict[str, str] = Field(default_factory=dict)
    components: List[str] = Field(default_factory=list)
    ui_constraints: Dict[str, Any] = Field(default_factory=dict)


class StoreFile(BaseModel):
    """Store file structure."""
    store_version: str = "1.0"
    design_systems: List[DesignSystem] = Field(default_factory=list)
    brand_profiles: List[BrandProfile] = Field(default_factory=list)
    design_tokens: List[DesignToken] = Field(default_factory=list)
    component_specs: List[ComponentSpec] = Field(default_factory=list)


# Request models
class RegisterDesignSystemRequest(BaseModel):
    """Request to register design system."""
    name: str = Field(..., min_length=1)
    version: str = "1.0.0"
    description: str = ""
    source: str = "manual"


class ParseDesignMdRequest(BaseModel):
    """Request to parse DESIGN.md."""
    text: str = Field(..., min_length=1)
    source: str = "manual"


class RegisterBrandProfileRequest(BaseModel):
    """Request to register brand profile."""
    design_system_id: str
    colors: Dict[str, str] = Field(default_factory=dict)
    fonts: Dict[str, str] = Field(default_factory=dict)
    border_radius: Dict[str, str] = Field(default_factory=dict)
    spacing: Dict[str, str] = Field(default_factory=dict)
    shadows: List[str] = Field(default_factory=list)
    logo: str = ""


class AddDesignTokenRequest(BaseModel):
    """Request to add design token."""
    design_system_id: str = ""
    category: str
    name: str = Field(..., min_length=1)
    value: Any
    description: str = ""
    tokens: Dict[str, Any] = Field(default_factory=dict)


class RegisterComponentSpecRequest(BaseModel):
    """Request to register component spec."""
    design_system_id: str = ""
    component_type: ComponentType
    name: str = Field(..., min_length=1)
    props: Dict[str, Any] = Field(default_factory=dict)
    variants: Dict[str, Dict[str, Any]] = Field(default_factory=dict)


class SuggestUiConstraintsRequest(BaseModel):
    """Request for UI constraint suggestions."""
    component_type: Optional[ComponentType] = None
    design_system_id: str = ""
