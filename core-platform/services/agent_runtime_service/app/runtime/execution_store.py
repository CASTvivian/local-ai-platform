"""JSON-file execution audit store for Agent Runtime replay."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .execution_models import ExecutionRecord


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
EXECUTION_ROOT = CORE_PLATFORM_ROOT / "data" / "execution_store"
EXECUTION_ROOT.mkdir(parents=True, exist_ok=True)


def execution_file(execution_id: str) -> Path:
    return EXECUTION_ROOT / f"{execution_id}.json"


def save_execution(record: ExecutionRecord) -> ExecutionRecord:
    execution_file(record.execution_id).write_text(record.model_dump_json(indent=2), encoding="utf-8")
    return record


def load_execution(execution_id: str) -> Optional[ExecutionRecord]:
    path = execution_file(execution_id)
    if not path.exists():
        return None
    return ExecutionRecord.model_validate_json(path.read_text(encoding="utf-8"))


def list_executions(
    run_id: Optional[str] = None,
    approval_id: Optional[str] = None,
    limit: int = 100,
) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    for path in sorted(EXECUTION_ROOT.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if run_id and data.get("run_id") != run_id:
            continue
        if approval_id and data.get("approval_id") != approval_id:
            continue
        items.append(data)
        if len(items) >= limit:
            break
    return items
