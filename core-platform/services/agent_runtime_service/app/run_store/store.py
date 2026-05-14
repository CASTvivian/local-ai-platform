"""JSON-file run store for MAOMIAI Agent Runtime."""

from __future__ import annotations

import uuid
from datetime import datetime
from pathlib import Path
from typing import Optional

from .models import AgentRunState


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
RUN_ROOT = CORE_PLATFORM_ROOT / "data" / "run_store"
RUN_ROOT.mkdir(parents=True, exist_ok=True)


def create_run(session_id: str, user_input: str) -> AgentRunState:
    """Create and persist a new run state."""

    now = datetime.utcnow()
    state = AgentRunState(
        run_id=str(uuid.uuid4()),
        session_id=session_id or "desktop-default",
        status="running",
        input=user_input,
        created_at=now,
        updated_at=now,
    )
    save_run(state)
    return state


def save_run(state: AgentRunState) -> None:
    """Persist a run state to disk."""

    state.updated_at = datetime.utcnow()
    path = RUN_ROOT / f"{state.run_id}.json"
    path.write_text(state.model_dump_json(indent=2), encoding="utf-8")


def load_run(run_id: str) -> Optional[AgentRunState]:
    """Load a run state by id."""

    path = RUN_ROOT / f"{run_id}.json"
    if not path.exists():
        return None
    return AgentRunState.model_validate_json(path.read_text(encoding="utf-8"))
