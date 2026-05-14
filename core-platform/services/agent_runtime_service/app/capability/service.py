"""Capability matching service helpers."""

from __future__ import annotations

from .models import CapabilityMatchRequest, CapabilityMatchResult
from .registry import match_capabilities


def match_capability(request: CapabilityMatchRequest) -> CapabilityMatchResult:
    """Match a request to registered capabilities."""

    items = match_capabilities(
        query=request.query,
        intent=request.intent,
        tags=request.tags,
        limit=request.limit,
    )
    return CapabilityMatchResult(ok=True, query=request.query, matches=items)
