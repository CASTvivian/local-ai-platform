"""JSON-file session store for MAOMIAI Agent Runtime."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Optional

from .models import AgentSessionState


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
SESSION_ROOT = CORE_PLATFORM_ROOT / "data" / "session_store"
SESSION_ROOT.mkdir(parents=True, exist_ok=True)


def _session_path(session_id: str) -> Path:
    safe = "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in session_id)
    return SESSION_ROOT / f"{safe or 'desktop-default'}.json"


def load_session(session_id: str) -> Optional[AgentSessionState]:
    """Load a session state by id."""

    path = _session_path(session_id or "desktop-default")
    if not path.exists():
        return None
    return AgentSessionState.model_validate_json(path.read_text(encoding="utf-8"))


def save_session(state: AgentSessionState) -> None:
    """Persist a session state to disk."""

    state.updated_at = datetime.utcnow()
    _session_path(state.session_id).write_text(state.model_dump_json(indent=2), encoding="utf-8")


def append_run(session_id: str, run_id: str) -> AgentSessionState:
    """Append a run id to a session, creating it if needed."""

    now = datetime.utcnow()
    sid = session_id or "desktop-default"
    state = load_session(sid) or AgentSessionState(
        session_id=sid,
        run_ids=[],
        created_at=now,
        updated_at=now,
    )
    if run_id not in state.run_ids:
        state.run_ids.append(run_id)
    save_session(state)
    return state
