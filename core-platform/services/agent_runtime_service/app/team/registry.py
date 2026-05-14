from __future__ import annotations
import json
from pathlib import Path
from typing import Optional, List, Dict, Any
from .models import AgentTeamSpec


REGISTRY_FILE = Path("core-platform/data/agent_team/team_registry.json")


def load_team_registry() -> Dict[str, Any]:
    if not REGISTRY_FILE.exists():
        return {
            "default_team": "default_local_team",
            "teams": [],
        }
    return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))


def list_teams() -> List[dict]:
    data = load_team_registry()
    return data.get("teams") or []


def get_team(team_id: Optional[str] = None) -> Optional[AgentTeamSpec]:
    data = load_team_registry()
    selected = team_id or data.get("default_team")
    for item in data.get("teams") or []:
        if item.get("id") == selected and item.get("enabled", True):
            return AgentTeamSpec.model_validate(item)
    return None