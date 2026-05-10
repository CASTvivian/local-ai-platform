"""Unit tests for skill store service."""

import pytest
from app.models import (
    SkillRecord,
    SkillSource,
    SignatureStatus,
    SkillStatus,
    AgentBinding,
)
from app.parser import parse_skill_md_text, validate_skill_md_text
from app.validation import (
    validate_skill_record,
    validate_skill_name,
    validate_version,
    validate_agent_bindings,
)


def test_parse_skill_md_simple():
    """Test parsing simple SKILL.md."""
    text = """# Test Skill
Name: test-skill
Version: 1.0.0
Description: A test skill
"""
    parsed = parse_skill_md_text(text)
    assert parsed["name"] == "test-skill"
    assert parsed["version"] == "1.0.0"
    assert parsed["description"] == "A test skill"


def test_parse_skill_md_with_agents():
    """Test parsing SKILL.md with agents."""
    text = """# Multi-Agent Skill
Name: multi-skill
Version: 0.2.0
Agents: coder, reviewer, tester
Tags: automation, testing
"""
    parsed = parse_skill_md_text(text)
    assert parsed["name"] == "multi-skill"
    assert "coder" in parsed["agents"]
    assert "reviewer" in parsed["agents"]
    assert "automation" in parsed["tags"]


def test_validate_skill_record_valid():
    """Test validation of valid skill record."""
    record = SkillRecord(
        id="skill_test123",
        name="test-skill",
        source=SkillSource.desktop_skill_md,
        version="1.0.0",
    )
    errors = validate_skill_record(record)
    assert len(errors) == 0


def test_validate_skill_record_invalid_name():
    """Test validation with invalid name."""
    record = SkillRecord(
        id="skill_test123",
        name="invalid name with spaces",
        version="1.0.0",
    )
    errors = validate_skill_record(record)
    assert any("name" in e.lower() for e in errors)


def test_validate_skill_record_invalid_version():
    """Test validation with invalid version."""
    record = SkillRecord(
        id="skill_test123",
        name="test-skill",
        version="invalid",
    )
    errors = validate_skill_record(record)
    assert any("version" in e.lower() for e in errors)


def test_validate_skill_name_valid():
    """Test validation of valid skill name."""
    errors = validate_skill_name("my-skill_v1")
    assert len(errors) == 0


def test_validate_skill_name_invalid():
    """Test validation of invalid skill names."""
    assert len(validate_skill_name("")) > 0  # Empty
    assert len(validate_skill_name("a")) > 0  # Too short
    assert len(validate_skill_name("invalid name")) > 0  # Has spaces


def test_validate_version_valid():
    """Test validation of valid versions."""
    assert len(validate_version("1.0.0")) == 0
    assert len(validate_version("2.3.1-beta.1")) == 0


def test_validate_version_invalid():
    """Test validation of invalid versions."""
    assert len(validate_version("1")) > 0  # Too short
    assert len(validate_version("invalid")) > 0  # Not semver


def test_validate_agent_bindings_valid():
    """Test validation of valid agent bindings."""
    bindings = [
        AgentBinding(agent_id="coder", enabled=True),
        AgentBinding(agent_id="tester", enabled=False),
    ]
    errors = validate_agent_bindings(bindings)
    assert len(errors) == 0


def test_validate_agent_bindings_duplicate():
    """Test validation with duplicate agent IDs."""
    bindings = [
        AgentBinding(agent_id="coder", enabled=True),
        AgentBinding(agent_id="coder", enabled=False),
    ]
    errors = validate_agent_bindings(bindings)
    assert any("duplicate" in e.lower() for e in errors)


def test_validate_skill_md_text():
    """Test SKILL.md validation."""
    text = """# Test Skill
Name: test
Version: 1.0.0
Description: A test skill
"""
    result = validate_skill_md_text(text)
    assert result["valid"] is True
    assert len(result["errors"]) == 0
