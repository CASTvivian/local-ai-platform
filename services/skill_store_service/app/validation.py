"""Validation logic for skill records."""

import re
from typing import List

from .models import (
    SkillRecord,
    SkillSource,
    SignatureStatus,
    SkillStatus,
    AgentBinding,
)


def validate_skill_record(record: SkillRecord) -> List[str]:
    """
    Validate a skill record and return list of validation errors.
    Returns empty list if validation passes.
    """
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
    if not re.match(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$', record.version):
        errors.append(f"invalid version format: {record.version}")

    # Validate enums
    try:
        SkillSource(record.source)
    except ValueError:
        errors.append(f"invalid source: {record.source}")

    try:
        SignatureStatus(record.signature_status)
    except ValueError:
        errors.append(f"invalid signature_status: {record.signature_status}")

    try:
        SkillStatus(record.status)
    except ValueError:
        errors.append(f"invalid status: {record.status}")

    # Validate agent bindings
    for i, binding in enumerate(record.agent_bindings):
        if not binding.agent_id:
            errors.append(f"agent_bindings[{i}].agent_id is required")
        if not re.match(r'^[a-zA-Z0-9_-]+$', binding.agent_id):
            errors.append(f"agent_bindings[{i}].agent_id has invalid format")

    # Validate timestamps
    if record.created_at <= 0:
        errors.append("created_at must be positive")
    if record.updated_at < record.created_at:
        errors.append("updated_at cannot be before created_at")

    return errors


def validate_skill_name(name: str) -> List[str]:
    """Validate skill name."""
    errors: List[str] = []

    if not name:
        errors.append("name is required")
    elif len(name) < 2:
        errors.append("name must be at least 2 characters")
    elif len(name) > 100:
        errors.append("name must not exceed 100 characters")
    elif not re.match(r'^[a-zA-Z0-9_-]+$', name):
        errors.append("name must contain only alphanumeric characters, hyphens, and underscores")

    return errors


def validate_version(version: str) -> List[str]:
    """Validate semantic version format."""
    errors: List[str] = []

    if not version:
        errors.append("version is required")
    elif not re.match(r'^\d+\.\d+\.\d+(-[a-zA-Z0-9.]+)?$', version):
        errors.append(f"invalid semantic version format: {version}")

    return errors


def validate_agent_bindings(bindings: List[AgentBinding]) -> List[str]:
    """Validate agent bindings."""
    errors: List[str] = []

    agent_ids = set()
    for i, binding in enumerate(bindings):
        if not binding.agent_id:
            errors.append(f"agent_bindings[{i}].agent_id is required")
        elif not re.match(r'^[a-zA-Z0-9_-]+$', binding.agent_id):
            errors.append(f"agent_bindings[{i}].agent_id has invalid format")
        elif binding.agent_id in agent_ids:
            errors.append(f"duplicate agent_id: {binding.agent_id}")
        else:
            agent_ids.add(binding.agent_id)

    return errors


def is_valid_skill_source(source: str) -> bool:
    """Check if skill source is valid."""
    try:
        SkillSource(source)
        return True
    except ValueError:
        return False


def is_valid_signature_status(status: str) -> bool:
    """Check if signature status is valid."""
    try:
        SignatureStatus(status)
        return True
    except ValueError:
        return False


def is_valid_skill_status(status: str) -> bool:
    """Check if skill status is valid."""
    try:
        SkillStatus(status)
        return True
    except ValueError:
        return False
