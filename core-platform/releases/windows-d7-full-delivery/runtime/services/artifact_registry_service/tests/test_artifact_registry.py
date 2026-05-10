"""Unit tests for artifact registry service."""

import pytest
from app.models import (
    ArtifactRecord,
    ArtifactType,
    Lifecycle,
    RegisterExecutionResultRequest,
    UpdateLifecycleRequest,
)
from app.validation import (
    validate_artifact_record,
    validate_register_request,
    validate_lifecycle_transition,
)


def test_validate_artifact_record_valid():
    """Test validation of valid artifact record."""
    record = ArtifactRecord(
        id="artifact_test123",
        name="test-result",
        type=ArtifactType.execution_result,
        lifecycle=Lifecycle.active,
    )
    errors = validate_artifact_record(record)
    assert len(errors) == 0


def test_validate_artifact_record_missing_id():
    """Test validation with missing ID."""
    record = ArtifactRecord(
        id="",
        name="test-result",
        type=ArtifactType.execution_result,
        lifecycle=Lifecycle.active,
    )
    errors = validate_artifact_record(record)
    assert any("id is required" in e for e in errors)


def test_validate_artifact_record_invalid_path():
    """Test validation with relative path."""
    record = ArtifactRecord(
        id="artifact_test123",
        name="test-result",
        path="relative/path.txt",
        type=ArtifactType.execution_result,
        lifecycle=Lifecycle.active,
    )
    errors = validate_artifact_record(record)
    assert any("path must be absolute" in e for e in errors)


def test_validate_register_request_valid():
    """Test validation of valid register request."""
    req = RegisterExecutionResultRequest(
        name="test-result",
        type=ArtifactType.execution_result,
        run_id="run_123",
    )
    errors = validate_register_request(req)
    assert len(errors) == 0


def test_validate_register_request_missing_name():
    """Test validation with missing name."""
    req = RegisterExecutionResultRequest(
        type=ArtifactType.execution_result,
    )
    errors = validate_register_request(req)
    assert any("name or title is required" in e for e in errors)


def test_validate_lifecycle_transition_valid():
    """Test valid lifecycle transitions."""
    # draft -> active
    assert validate_lifecycle_transition(Lifecycle.draft, Lifecycle.active) is True
    # active -> archived
    assert validate_lifecycle_transition(Lifecycle.active, Lifecycle.archived) is True
    # archived -> deleted
    assert validate_lifecycle_transition(Lifecycle.archived, Lifecycle.deleted) is True
    # Any -> draft
    assert validate_lifecycle_transition(Lifecycle.deleted, Lifecycle.draft) is True


def test_validate_lifecycle_transition_invalid():
    """Test invalid lifecycle transitions."""
    # deleted -> active (should be invalid)
    assert validate_lifecycle_transition(Lifecycle.deleted, Lifecycle.active) is False
    # archived -> active (should be invalid)
    assert validate_lifecycle_transition(Lifecycle.archived, Lifecycle.active) is False
