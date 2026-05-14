"""Planner health and circuit breaker implementation."""

from __future__ import annotations

import json
import os
import time
import urllib.request
from pathlib import Path
from datetime import datetime
from typing import Dict, Any

from .models import PlannerRuntimeState


# Resolve path relative to workspace root
# __file__ is at: .../本地ai/core-platform/services/agent_runtime_service/app/health/planner_health.py
# Workspace root (本地ai/): parent.parent.parent.parent.parent.parent
WORKSPACE_ROOT = Path(__file__).parent.parent.parent.parent.parent.parent
ROOT = WORKSPACE_ROOT / "core-platform" / "data" / "planner_runtime"
ROOT.mkdir(parents=True, exist_ok=True)
STATE_FILE = ROOT / "planner_health.json"
MODEL_GATEWAY_HEALTH_URL = os.environ.get("MAOMIAI_MODEL_GATEWAY_HEALTH_URL", "http://127.0.0.1:18080/health")
CIRCUIT_TTL_SECONDS = int(os.environ.get("MAOMIAI_PLANNER_CIRCUIT_TTL_SECONDS", "60"))


def _now() -> str:
    return datetime.utcnow().isoformat()


def _load_raw_state() -> Dict[str, Any]:
    if not STATE_FILE.exists():
        return {}
    try:
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _save_state(data: Dict[str, Any]):
    STATE_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def record_planner_error(error: str):
    data = _load_raw_state()
    data.update(
        {
            "ok": False,
            "model_gateway_ok": False,
            "circuit_open": True,
            "last_error": error,
            "last_error_at": time.time(),
            "checked_at": _now(),
        }
    )
    _save_state(data)


def clear_planner_error():
    data = _load_raw_state()
    data.update(
        {
            "ok": True,
            "model_gateway_ok": True,
            "circuit_open": False,
            "last_error": None,
            "checked_at": _now(),
        }
    )
    _save_state(data)


def is_circuit_open() -> bool:
    data = _load_raw_state()
    if not data.get("circuit_open"):
        return False
    last_error_at = float(data.get("last_error_at") or 0)
    if time.time() - last_error_at > CIRCUIT_TTL_SECONDS:
        return False
    return True


def check_model_gateway(timeout: int = 3) -> Dict[str, Any]:
    try:
        req = urllib.request.Request(MODEL_GATEWAY_HEALTH_URL, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read(200000).decode("utf-8", errors="replace")
        try:
            data = json.loads(raw)
        except Exception:
            data = {"raw": raw}
        clear_planner_error()
        return {
            "ok": True,
            "status": "healthy",
            "detail": data,
        }
    except Exception as e:
        record_planner_error(str(e))
        return {
            "ok": False,
            "status": "unhealthy",
            "detail": {
                "error": str(e),
                "url": MODEL_GATEWAY_HEALTH_URL,
            },
        }


def planner_runtime_state(check_live: bool = False) -> PlannerRuntimeState:
    if check_live:
        check_model_gateway()
    data = _load_raw_state()
    circuit = is_circuit_open()
    planner_mode = os.environ.get("MAOMIAI_PLANNER_MODE", "llm_first")
    model_gateway_ok = bool(data.get("model_gateway_ok", False))
    return PlannerRuntimeState(
        ok=(not circuit) and model_gateway_ok,
        planner_mode=planner_mode,
        model_gateway_ok=model_gateway_ok,
        circuit_open=circuit,
        last_error=data.get("last_error"),
        fallback_active=circuit or not model_gateway_ok,
        checked_at=_now(),
        detail={
            "model_gateway_health_url": MODEL_GATEWAY_HEALTH_URL,
            "circuit_ttl_seconds": CIRCUIT_TTL_SECONDS,
            "raw_state": data,
        },
    )