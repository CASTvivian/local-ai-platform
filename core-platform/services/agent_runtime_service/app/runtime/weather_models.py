"""Weather runtime models."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class WeatherQueryRequest(BaseModel):
    """Weather query request resolved through provider geocoding."""

    location: str
    run_id: Optional[str] = None
    session_id: Optional[str] = None
    days: int = 1


class WeatherQueryResponse(BaseModel):
    """Normalized weather provider response."""

    ok: bool
    location: str
    resolved_location: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    current: Dict[str, Any] = Field(default_factory=dict)
    daily: List[Dict[str, Any]] = Field(default_factory=list)
    error: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
