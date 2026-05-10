"""Unit tests for repo memory service."""

import pytest
from app.models import (
    RepoRecord,
    FixRecord,
    ContextSnapshot,
    KnowledgeEntry,
    FixResult,
    RegisterRepoRequest,
    RecordFixRequest,
)
from app.validation import (
    validate_repo_name,
    validate_repo_path,
    validate_fix_record,
    validate_context_snapshot,
    validate_knowledge_entry,
    is_valid_fix_result,
)


def test_validate_repo_name_valid():
    """Test validation of valid repo name."""
    errors = validate_repo_name("my-repo")
    assert len(errors) == 0


def test_validate_repo_name_invalid():
    """Test validation of invalid repo names."""
    assert len(validate_repo_name("")) > 0  # Empty
    assert len(validate_repo_name("a")) > 0  # Too short
    assert len(validate_repo_name("x" * 101)) > 0  # Too long


def test_validate_repo_path_valid():
    """Test validation of valid repo path."""
    errors = validate_repo_path("/Users/test/repo")
    assert len(errors) == 0


def test_validate_repo_path_relative():
    """Test validation of relative path."""
    errors = validate_repo_path("./repo")
    assert len(errors) > 0


def test_validate_fix_record_valid():
    """Test validation of valid fix record."""
    record = FixRecord(
        id="fix_123",
        repo_id="repo_456",
        title="Fix bug",
        problem="Bug description",
        solution="Fix implementation",
        result=FixResult.success,
    )
    errors = validate_fix_record(record)
    assert len(errors) == 0


def test_validate_fix_record_missing_fields():
    """Test validation with missing required fields."""
    record = FixRecord(
        id="fix_123",
        repo_id="repo_456",
        title="",
        problem="",
        solution="",
        result=FixResult.success,
    )
    errors = validate_fix_record(record)
    assert len(errors) >= 3  # title, problem, solution


def test_validate_context_snapshot_valid():
    """Test validation of valid context snapshot."""
    snapshot = ContextSnapshot(
        id="snapshot_123",
        repo_id="repo_456",
        title="Main branch",
        summary="Summary",
        files=["file1.py", "file2.py"],
        services=["service1", "service2"],
        tokens_estimate=1000,
    )
    errors = validate_context_snapshot(snapshot)
    assert len(errors) == 0


def test_validate_context_snapshot_missing_fields():
    """Test validation with missing required fields."""
    snapshot = ContextSnapshot(
        id="snapshot_123",
        repo_id="repo_456",
        title="",
        summary="",
        tokens_estimate=-100,  # Invalid
    )
    errors = validate_context_snapshot(snapshot)
    assert len(errors) >= 3  # title, summary, tokens_estimate


def test_validate_knowledge_entry_valid():
    """Test validation of valid knowledge entry."""
    entry = KnowledgeEntry(
        id="knowledge_123",
        title="Best practice",
        content="Content here",
        category="general",
        tags=["tag1", "tag2"],
    )
    errors = validate_knowledge_entry(entry)
    assert len(errors) == 0


def test_validate_knowledge_entry_missing_fields():
    """Test validation with missing required fields."""
    entry = KnowledgeEntry(
        id="knowledge_123",
        title="",
        content="",
        category="general",
    )
    errors = validate_knowledge_entry(entry)
    assert len(errors) >= 2  # title, content


def test_is_valid_fix_result():
    """Test fix result validation."""
    assert is_valid_fix_result("success") is True
    assert is_valid_fix_result("failed") is True
    assert is_valid_fix_result("partial") is True
    assert is_valid_fix_result("unknown") is True
    assert is_valid_fix_result("invalid") is False


def test_register_repo_request():
    """Test register repo request model."""
    req = RegisterRepoRequest(
        name="test-repo",
        path="/Users/test/repo",
        description="Test repo",
        tags=["python", "api"],
        services=["service1", "service2"],
    )
    assert req.name == "test-repo"
    assert len(req.tags) == 2


def test_record_fix_request():
    """Test record fix request model."""
    req = RecordFixRequest(
        repo_id="repo_123",
        title="Fix bug",
        problem="Bug description",
        solution="Fix",
        files_changed=["file1.py"],
        commands_run=["pytest"],
        result=FixResult.success,
    )
    assert req.repo_id == "repo_123"
    assert req.result == FixResult.success
