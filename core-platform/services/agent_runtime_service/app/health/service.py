"""Health service aggregator for agent runtime."""

from __future__ import annotations

from typing import Dict, Any
from datetime import datetime

from .planner_health import check_model_gateway, planner_runtime_state


def agent_health(check_live: bool = False) -> Dict[str, Any]:
    gateway = check_model_gateway() if check_live else {}
    planner = planner_runtime_state(check_live=False)
    return {
        "ok": planner.ok,
        "checked_at": datetime.utcnow().isoformat(),
        "components": {
            "planner": planner.model_dump(),
            "model_gateway": gateway,
        },
    }