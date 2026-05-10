"""Validation logic for design system service."""

import re
from typing import List

from .models import (
    DesignSystem,
    BrandProfile,
    DesignToken,
    ComponentSpec,
    ColorToken,
    SpacingToken,
    ComponentType,
)


def validate_design_system(record: DesignSystem) -> List[str]:
    """Validate design system record."""
    errors: List[str] = []
    
    # Check required fields
    if not record.id:
        errors.append("id is required")
    if not record.name:
        errors.append("name is required")
    
    # Validate name format
    if record.name:
        if len(record.name) < 2:
            errors.append("name must be at least 2 characters")
        if not re.match(r'^[a-zA-Z0-9_-]+$', record.name):
            errors.append("name must contain only alphanumeric characters, hyphens, and underscores")
    
    # Validate version format
    if not re.match(r'^\d+\.\d+\.\d+', record.version):
        errors.append(f"invalid version format: {record.version}")
    
    # Validate timestamps
    if record.created_at <= 0:
        errors.append("created_at must be positive")
    if record.updated_at < record.created_at:
        errors.append("updated_at cannot be before created_at")
    
    return errors


def validate_brand_profile(profile: BrandProfile) -> List[str]:
    """Validate brand profile."""
    errors: List[str] = []
    
    # Check required fields
    if not profile.id:
        errors.append("id is required")
    
    # Validate colors (should be hex codes)
    for color_name, color_value in profile.colors.items():
        if not color_value.startswith("#"):
            errors.append(f"color {color_name} must be hex code starting with #")
        elif len(color_value) not in [7, 9]:  # #RRGGBB or #RRGGBBAA
            errors.append(f"color {color_name} has invalid hex format")
    
    return errors


def validate_design_token(token: DesignToken) -> List[str]:
    """Validate design token."""
    errors: List[str] = []
    
    # Check required fields
    if not token.id:
        errors.append("id is required")
    if not token.name:
        errors.append("name is required")
    if not token.category:
        errors.append("category is required")
    
    # Validate category
    valid_categories = ["colors", "fonts", "spacing", "radius", "shadows"]
    if token.category not in valid_categories:
        errors.append(f"invalid category: {token.category}")
    
    # Validate timestamps
    # (DesignToken doesn't have timestamps by default)
    
    return errors


def validate_component_spec(spec: ComponentSpec) -> List[str]:
    """Validate component specification."""
    errors: List[str] = []
    
    # Check required fields
    if not spec.id:
        errors.append("id is required")
    if not spec.name:
        errors.append("name is required")
    
    # Validate component type
    try:
        ComponentType(spec.component_type)
    except ValueError:
        errors.append(f"invalid component_type: {spec.component_type}")
    
    return errors


def is_valid_color_token(token: str) -> bool:
    """Check if color token is valid."""
    try:
        ColorToken(token)
        return True
    except ValueError:
        return False


def is_valid_spacing_token(token: str) -> bool:
    """Check if spacing token is valid."""
    try:
        SpacingToken(token)
        return True
    except ValueError:
        return False


def is_valid_component_type(component_type: str) -> bool:
    """Check if component type is valid."""
    try:
        ComponentType(component_type)
        return True
    except ValueError:
        return False
