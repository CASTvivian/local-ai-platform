"""Unit tests for design system service."""

import pytest
from app.models import (
    DesignSystem,
    BrandProfile,
    DesignToken,
    ComponentSpec,
    ColorToken,
    SpacingToken,
    ComponentType,
)
from app.parser import parse_design_md_text
from app.validation import (
    validate_design_system,
    validate_brand_profile,
    validate_design_token,
    validate_component_spec,
)


def test_parse_design_md_simple():
    """Test parsing simple DESIGN.md."""
    text = """# My Design System
Name: my-design
Version: 1.0.0

## Colors
Primary: #3B82F6
Secondary: #10B981

## Fonts
Regular: Inter
"""
    parsed = parse_design_md_text(text)
    assert parsed["name"] == "my-design"
    assert parsed["version"] == "1.0.0"
    assert parsed["colors"]["primary"] == "#3B82F6"
    assert parsed["fonts"]["regular"] == "Inter"


def test_parse_design_md_with_components():
    """Test parsing DESIGN.md with components."""
    text = """# Design System
Name: test-design

## Components
Button, Card, Modal, Form

## Spacing
xs: 4px
sm: 8px
"""
    parsed = parse_design_md_text(text)
    assert parsed["name"] == "test-design"
    assert "button" in parsed["components"]
    assert "card" in parsed["components"]
    assert parsed["spacing"]["xs"] == "4px"


def test_validate_design_system_valid():
    """Test validation of valid design system."""
    record = DesignSystem(
        id="design_123",
        name="test-design",
        version="1.0.0",
    )
    errors = validate_design_system(record)
    assert len(errors) == 0


def test_validate_design_system_invalid_name():
    """Test validation with invalid name."""
    record = DesignSystem(
        id="design_123",
        name="invalid name with spaces",
        version="1.0.0",
    )
    errors = validate_design_system(record)
    assert len(errors) > 0


def test_validate_brand_profile_valid():
    """Test validation of valid brand profile."""
    profile = BrandProfile(
        id="brand_123",
        colors={"primary": "#3B82F6", "secondary": "#10B981"},
        fonts={"regular": "Inter"},
        border_radius={"sm": "4px", "md": "8px"},
    )
    errors = validate_brand_profile(profile)
    assert len(errors) == 0


def test_validate_brand_profile_invalid_colors():
    """Test validation with invalid colors."""
    profile = BrandProfile(
        id="brand_123",
        colors={"primary": "not-a-hex"},
        fonts={"regular": "Inter"},
        border_radius={},
    )
    errors = validate_brand_profile(profile)
    assert len(errors) > 0
    assert any("hex" in e.lower() for e in errors)


def test_validate_design_token_valid():
    """Test validation of valid design token."""
    token = DesignToken(
        id="token_123",
        category="colors",
        name="primary",
        value="#3B82F6",
    )
    errors = validate_design_token(token)
    assert len(errors) == 0


def test_validate_design_token_invalid_category():
    """Test validation with invalid category."""
    token = DesignToken(
        id="token_123",
        category="invalid",
        name="primary",
        value="#3B82F6",
    )
    errors = validate_design_token(token)
    assert len(errors) > 0


def test_validate_component_spec_valid():
    """Test validation of valid component spec."""
    spec = ComponentSpec(
        id="component_123",
        component_type=ComponentType.button,
        name="PrimaryButton",
        props={"size": "md", "variant": "primary"},
    )
    errors = validate_component_spec(spec)
    assert len(errors) == 0


def test_validate_component_spec_invalid_type():
    """Test validation with invalid component type."""
    spec = ComponentSpec(
        id="component_123",
        component_type="invalid_type",
        name="TestComponent",
        props={},
    )
    errors = validate_component_spec(spec)
    assert len(errors) > 0
