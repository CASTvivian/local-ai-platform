from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Optional, List, Dict, Any
from .models import TeamRunState


BASE_DIR = Path(os.environ.get("MAOMIAI_CORE_PLATFORM_DIR", Path(__file__).parent.parent.parent.parent.parent))
ROOT = BASE_DIR / "data" / "agent_team" / "runs"
ROOT.mkdir(parents=True, exist_ok=True)


def run_file(team_run_id: str) -> Path:
    return ROOT / f"{team_run_id}.json"


def save_team_run(state: TeamRunState) -> TeamRunState:
    run_file(state.team_run_id).write_text(
        state.model_dump_json(indent=2),
        encoding="utf-8",
    )
    return state


def load_team_run(team_run_id: str) -> Optional[TeamRunState]:
    p = run_file(team_run_id)
    if not p.exists():
        return None
    return TeamRunState.model_validate_json(p.read_text(encoding="utf-8"))


def list_team_runs(limit: int = 100) -> List[Dict[str, Any]]:
    items = []
    for p in sorted(ROOT.glob("*.json"), key=lambda x: x.stat().st_mtime, reverse=True):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            items.append({
                "team_run_id": data.get("team_run_id"),
                "session_id": data.get("session_id"),
                "team_id": data.get("team_id"),
                "input": data.get("input"),
                "status": data.get("status"),
                "final_answer": data.get("final_answer"),
                "created_at": data.get("created_at"),
                "updated_at": data.get("updated_at"),
            })
        except Exception:
            continue
        if len(items) >= limit:
            break
    return items