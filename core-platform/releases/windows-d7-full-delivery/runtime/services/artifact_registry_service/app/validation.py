"""Validation logic for artifact records."""

from typing import List

from .models import (
    ArtifactRecord,
    ArtifactType,
    Lifecycle,
    RegisterExecutionResultRequest,
)


def validate_artifact_record(record: ArtifactRecord) -> List[str]:
    """
    Validate an artifact record and return list of validation errors.
    Returns empty list if validation passes.
    """
    errors: List[str] = []

    # Check required fields
    if not record.id:
        errors.append("id is required")
    if not record.name:
        errors.append("name is required")

    # Validate path format
    if record.path:
        if not record.path.startswith("/"):
            errors.append(f"path must be absolute, got: {record.path}")

    # Validate lifecycle
    try:
        Lifecycle(record.lifecycle)
    except ValueError:
        errors.append(f"invalid lifecycle: {record.lifecycle}")

    # Validate artifact type
    try:
        ArtifactType(record.type)
    except ValueError:
        errors.append(f"invalid type: {record.type}")

    # Validate timestamps
    if record.created_at <= 0:
        errors.append("created_at must be positive")
    if record.updated_at < record.created_at:
        errors.append("updated_at cannot be before created_at")

    return errors


def validate_register_request(req: RegisterExecutionResultRequest) -> List[str]:
    """
    Validate a register request and return list of validation errors.
    Returns empty list if validation passes.
    """
    errors: List[str] = []

    # Name validation
    name = req.name or req.title or req.payload.get("title")
    if not name:
        errors.append("name or title is required")

    # Run ID validation
    if not req.run_id and not req.trace_id:
        errors.append("run_id or trace_id is required")

    # Lifecycle validation
    try:
        Lifecycle(req.lifecycle)
    except ValueError:
        errors.append(f"invalid lifecycle: {req.lifecycle}")

    # Type validation
    try:
        ArtifactType(req.type)
    except ValueError:
        errors.append(f"invalid type: {req.type}")

    return errors


def validate_lifecycle_transition(current: Lifecycle, proposed: Lifecycle) -> bool:
    """
    Validate that a lifecycle transition is allowed.
    
    Allowed transitions:
    - draft -> active
    - active -> archived
    - active -> deleted
    - archived -> deleted
    - Any state -> draft
    """
    if current == Lifecycle.draft:
        return True  # Can go anywhere from draft

    if current == Lifecycle.active:
        return proposed in {Lifecycle.active, Lifecycle.archived, Lifecycle.deleted, Lifecycle.draft}

    if current == Lifecycle.archived:
        return proposed in {Lifecycle.archived, Lifecycle.deleted, Lifecycle.draft}

    if current == Lifecycle.deleted:
        return proposed in {Lifecycle.deleted, Lifecycle.draft}  # Can only undelete to draft

    return False


def is_valid_artifact_type(artifact_type: str) -> bool:
    """Check if artifact type is valid."""
    try:
        ArtifactType(artifact_type)
        return True
    except ValueError:
        return False


def is_valid_lifecycle(lifecycle: str) -> bool:
    """Check if lifecycle is valid."""
    try:
        Lifecycle(lifecycle)
        return True
    except ValueError:
        return False
