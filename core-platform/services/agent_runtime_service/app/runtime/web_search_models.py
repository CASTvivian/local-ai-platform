"""Web search runtime models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class WebSearchRequest(BaseModel):
    """Public web search request."""

    query: str
    run_id: Optional[str] = None
    session_id: Optional[str] = None
    limit: int = 5
    fetch_top: bool = True


class WebSearchResultItem(BaseModel):
    """One normalized search result."""

    title: str
    url: str
    snippet: str = ""
    snapshot_id: Optional[str] = None


class WebSearchResponse(BaseModel):
    """Normalized web search response."""

    ok: bool
    query: str
    items: List[WebSearchResultItem] = Field(default_factory=list)
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
