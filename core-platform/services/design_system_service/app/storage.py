"""Storage layer for design system service with atomic writes and locking."""

import json
import os
import tempfile
import threading
from pathlib import Path
from typing import Any, Dict, List
from datetime import datetime

from .models import StoreFile


# Global lock for write operations
_store_lock = threading.RLock()

# Path resolution
def resolve_core_platform_dir() -> Path:
    """Resolve core platform directory using environment variable or relative path detection."""
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        root = Path(env).expanduser().resolve()
        if root.exists():
            return root

    # Try relative path detection from current file
    here = Path(__file__).resolve()
    for parent in [here, *here.parents]:
        if (
            (parent / "services").exists()
            and (parent / "apps").exists()
            and (parent / "scripts").exists()
        ):
            return parent

    # Fallback to cwd
    cwd = Path.cwd().resolve()
    for parent in [cwd, *cwd.parents]:
        if (
            (parent / "services").exists()
            and (parent / "apps").exists()
            and (parent / "scripts").exists()
        ):
            return parent

    return cwd


BASE_DIR = resolve_core_platform_dir()
DATA_DIR = BASE_DIR / "data" / "design_system"
STORE_PATH = DATA_DIR / "store.json"
EVENTS_PATH = DATA_DIR / "events.jsonl"
ERRORS_PATH = DATA_DIR / "errors.jsonl"


def ensure_data_dir() -> None:
    """Ensure data directory exists."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def atomic_write_json(path: Path, data: Dict[str, Any]) -> None:
    """Write JSON atomically using temp file + rename."""
    ensure_data_dir()
    fd, tmp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")
        os.replace(tmp_name, path)  # Atomic replacement
    finally:
        if os.path.exists(tmp_name):
            try:
                os.remove(tmp_name)
            except OSError:
                pass


def load_store() -> StoreFile:
    """Load store from disk. Returns empty store if file doesn't exist."""
    if not STORE_PATH.exists():
        ensure_data_dir()
        store = StoreFile()
        atomic_write_json(STORE_PATH, store.model_dump())
        return store

    try:
        with open(STORE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return StoreFile.model_validate(data)
    except json.JSONDecodeError as e:
        # JSON parse error - file is corrupted
        append_error("load_store", str(e), {"file": str(STORE_PATH)})
        # Create a backup and start fresh
        backup_path = DATA_DIR / f"store.corrupt.{int(datetime.now().timestamp())}.json"
        try:
            os.replace(STORE_PATH, backup_path)
        except OSError:
            pass
        return StoreFile()
    except OSError as e:
        # IO error - return empty store but don't corrupt
        append_error("load_store", str(e), {"file": str(STORE_PATH)})
        return StoreFile()


def save_store(store: StoreFile) -> None:
    """Save store to disk atomically."""
    with _store_lock:
        atomic_write_json(STORE_PATH, store.model_dump())


def append_event(event_type: str, data: Dict[str, Any]) -> None:
    """Append event to events log."""
    with _store_lock:
        ensure_data_dir()
        event = {
            "ts": datetime.utcnow().isoformat(),
            "type": event_type,
            "data": data,
        }
        with open(EVENTS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")


def append_error(where: str, message: str, extra: Dict[str, Any] | None = None) -> None:
    """Append error to errors log."""
    with _store_lock:
        ensure_data_dir()
        error = {
            "ts": datetime.utcnow().isoformat(),
            "where": where,
            "message": message,
            "extra": extra or {},
        }
        with open(ERRORS_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(error, ensure_ascii=False) + "\n")


def recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Read recent events from log."""
    if not EVENTS_PATH.exists():
        return []

    events: List[Dict[str, Any]] = []
    with open(EVENTS_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    events.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return events[-limit:]


def make_design_system_id(name: str) -> str:
    """Generate design system ID from name."""
    import hashlib
    import uuid

    content = f"{name}:{datetime.utcnow().timestamp()}:{uuid.uuid4().hex}"
    h = hashlib.sha256(content.encode()).hexdigest()[:12]
    return f"design_{h}"


def make_brand_profile_id() -> str:
    """Generate brand profile ID."""
    import hashlib
    import uuid

    content = f"brand:{datetime.utcnow().timestamp()}:{uuid.uuid4().hex}"
    h = hashlib.sha256(content.encode()).hexdigest()[:12]
    return f"brand_{h}"


def make_token_id() -> str:
    """Generate token ID."""
    import hashlib
    import uuid

    content = f"token:{datetime.utcnow().timestamp()}:{uuid.uuid4().hex}"
    h = hashlib.sha256(content.encode()).hexdigest()[:12]
    return f"token_{h}"


def make_component_spec_id() -> str:
    """Generate component spec ID."""
    import hashlib
    import uuid

    content = f"component:{datetime.utcnow().timestamp()}:{uuid.uuid4().hex}"
    h = hashlib.sha256(content.encode()).hexdigest()[:12]
    return f"component_{h}"
