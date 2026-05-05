"""Validation logic for repo memory service."""

import re
from typing import List

from .models import (
    RepoRecord,
    FixRecord,
    ContextSnapshot,
    KnowledgeEntry,
    FixResult,
)


def validate_repo_name(name: str) -> List[str]:
    """Validate repository name."""
    errors: List[str] = []

    if not name:
        errors.append("name is required")
    elif len(name) < 2:
        errors.append("name must be at least 2 characters")
    elif len(name) > 100:
        errors.append("name must not exceed 100 characters")

    return errors


def validate_repo_path(path: str) -> List[str]:
    """Validate repository path."""
    errors: List[str] = []

    if path and not path.startswith("/"):
        errors.append("path must be absolute if provided")

    return errors


def validate_fix_record(record: FixRecord) -> List[str]:
    """Validate fix record."""
    errors: List[str] = []

    if not record.id:
        errors.append("id is required")
    if not record.repo_id:
        errors.append("repo_id is required")
    if not record.title:
        errors.append("title is required")
    if not record.problem:
        errors.append("problem is required")
    if not record.solution:
        errors.append("solution is required")

    # Validate result enum
    try:
        FixResult(record.result)
    except ValueError:
        errors.append(f"invalid result: {record.result}")

    # Validate timestamps
    if record.created_at <= 0:
        errors.append("created_at must be positive")

    return errors


def validate_context_snapshot(snapshot: ContextSnapshot) -> List[str]:
    """Validate context snapshot."""
    errors: List[str] = []

    if not snapshot.id:
        errors.append("id is required")
    if not snapshot.repo_id:
        errors.append("repo_id is required")
    if not snapshot.title:
        errors.append("title is required")
    if not snapshot.summary:
        errors.append("summary is required")

    # Validate tokens_estimate
    if snapshot.tokens_estimate < 0:
        errors.append("tokens_estimate cannot be negative")

    # Validate timestamps
    if snapshot.created_at <= 0:
        errors.append("created_at must be positive")

    return errors


def validate_knowledge_entry(entry: KnowledgeEntry) -> List[str]:
    """Validate knowledge entry."""
    errors: List[str] = []

    if not entry.id:
        errors.append("id is required")
    if not entry.title:
        errors.append("title is required")
    if not entry.content:
        errors.append("content is required")

    # Validate category
    if not entry.category:
        errors.append("category cannot be empty")

    # Validate timestamps
    if entry.created_at <= 0:
        errors.append("created_at must be positive")

    return errors


def is_valid_fix_result(result: str) -> bool:
    """Check if fix result is valid."""
    try:
        FixResult(result)
        return True
    except ValueError:
        return False
