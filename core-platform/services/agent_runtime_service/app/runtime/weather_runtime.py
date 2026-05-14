"""Weather connector using provider geocoding without city-specific maps."""

from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from .execution_models import new_execution_record
from .execution_store import save_execution
from .weather_models import WeatherQueryRequest, WeatherQueryResponse


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
WEATHER_ROOT = CORE_PLATFORM_ROOT / "data" / "weather_runtime"
WEATHER_ROOT.mkdir(parents=True, exist_ok=True)


def _runtime_file(weather_id: str) -> Path:
    return WEATHER_ROOT / f"{weather_id}.json"


def _geocode(location: str) -> Dict[str, Any]:
    query = (location or "").strip()
    if not query:
        raise ValueError("empty location")
    url = "https://geocoding-api.open-meteo.com/v1/search?" + urllib.parse.urlencode(
        {
            "name": query,
            "count": 1,
            "language": "zh",
            "format": "json",
        }
    )
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "MAOMIAI-AgentRuntime/0.1"},
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.loads(response.read(300000).decode("utf-8", errors="replace"))
    results = data.get("results") or []
    if not results:
        raise ValueError(f"location not found: {query}")
    top = results[0]
    return {
        "query": query,
        "name": top.get("name") or query,
        "latitude": top.get("latitude"),
        "longitude": top.get("longitude"),
        "country": top.get("country"),
        "admin1": top.get("admin1"),
        "timezone": top.get("timezone"),
    }


def _pick(values: list | None, index: int):
    if not values or index >= len(values):
        return None
    return values[index]


def _save_weather_audit(request: WeatherQueryRequest, payload: dict) -> None:
    save_execution(
        new_execution_record(
            run_id=request.run_id,
            session_id=request.session_id,
            tool="weather.query",
            command=request.location,
            status="completed" if payload.get("ok") else "failed",
            ok=bool(payload.get("ok")),
            stdout=json.dumps(
                {
                    "location": payload.get("location"),
                    "resolved_location": payload.get("resolved_location"),
                    "current": payload.get("current"),
                    "metadata": payload.get("metadata"),
                },
                ensure_ascii=False,
            ),
            error=payload.get("error"),
            metadata={"source": "weather_runtime", **(payload.get("metadata") or {})},
        )
    )


def query_weather(request: WeatherQueryRequest) -> dict:
    """Query weather through Open-Meteo geocoding and forecast APIs."""

    weather_id = hashlib.sha256(f"{request.location}:{datetime.utcnow().isoformat()}".encode("utf-8")).hexdigest()[:24]
    try:
        location = _geocode(request.location)
        days = max(1, min(int(request.days or 1), 7))
        url = "https://api.open-meteo.com/v1/forecast?" + urllib.parse.urlencode(
            {
                "latitude": location["latitude"],
                "longitude": location["longitude"],
                "current": (
                    "temperature_2m,relative_humidity_2m,apparent_temperature,"
                    "precipitation,weather_code,wind_speed_10m,wind_direction_10m"
                ),
                "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
                "forecast_days": days,
                "timezone": "auto",
            }
        )
        api_request = urllib.request.Request(
            url,
            headers={"User-Agent": "MAOMIAI-AgentRuntime/0.1"},
            method="GET",
        )
        with urllib.request.urlopen(api_request, timeout=20) as response:
            data = json.loads(response.read(800000).decode("utf-8", errors="replace"))
        current = data.get("current") or {}
        current_summary = {
            "temperature_2m": current.get("temperature_2m"),
            "apparent_temperature": current.get("apparent_temperature"),
            "relative_humidity_2m": current.get("relative_humidity_2m"),
            "precipitation": current.get("precipitation"),
            "weather_code": current.get("weather_code"),
            "wind_speed_10m": current.get("wind_speed_10m"),
            "wind_direction_10m": current.get("wind_direction_10m"),
            "time": current.get("time"),
        }
        daily_raw = data.get("daily") or {}
        daily = []
        for index, day in enumerate(daily_raw.get("time") or []):
            daily.append(
                {
                    "date": day,
                    "weather_code": _pick(daily_raw.get("weather_code"), index),
                    "temperature_max": _pick(daily_raw.get("temperature_2m_max"), index),
                    "temperature_min": _pick(daily_raw.get("temperature_2m_min"), index),
                    "precipitation_sum": _pick(daily_raw.get("precipitation_sum"), index),
                    "wind_speed_max": _pick(daily_raw.get("wind_speed_10m_max"), index),
                }
            )
        payload = WeatherQueryResponse(
            ok=True,
            location=request.location,
            resolved_location=", ".join(
                str(value)
                for value in [location.get("name"), location.get("admin1"), location.get("country")]
                if value
            ),
            latitude=location.get("latitude"),
            longitude=location.get("longitude"),
            current=current_summary,
            daily=daily,
            metadata={
                "weather_id": weather_id,
                "provider": "open-meteo",
                "geocoding": "open-meteo",
                "created_at": datetime.utcnow().isoformat(),
                "run_id": request.run_id,
                "session_id": request.session_id,
                "source_url": url,
                "location_query": location.get("query"),
            },
        )
        result = payload.model_dump()
        _runtime_file(weather_id).write_text(payload.model_dump_json(indent=2), encoding="utf-8")
        _save_weather_audit(request, result)
        return result
    except Exception as exc:
        payload = WeatherQueryResponse(
            ok=False,
            location=request.location,
            error=str(exc),
            metadata={
                "weather_id": weather_id,
                "provider": "open-meteo",
                "geocoding": "open-meteo",
                "created_at": datetime.utcnow().isoformat(),
                "run_id": request.run_id,
                "session_id": request.session_id,
            },
        )
        result = payload.model_dump()
        _save_weather_audit(request, result)
        return result


def list_weather_queries(limit: int = 100) -> dict:
    """List persisted weather queries."""

    items = []
    for path in sorted(WEATHER_ROOT.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        items.append(
            {
                "weather_id": data.get("metadata", {}).get("weather_id"),
                "location": data.get("location"),
                "resolved_location": data.get("resolved_location"),
                "ok": data.get("ok"),
                "created_at": data.get("metadata", {}).get("created_at"),
                "run_id": data.get("metadata", {}).get("run_id"),
                "session_id": data.get("metadata", {}).get("session_id"),
            }
        )
        if len(items) >= limit:
            break
    return {"ok": True, "items": items}
