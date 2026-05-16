from __future__ import annotations

import json
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

TaskStatus = Literal["pending", "in_progress", "completed", "failed", "blocked", "cancelled"]


@dataclass
class TaskItem:
    id: str
    title: str
    status: TaskStatus = "pending"
    detail: str | None = None
    result: dict[str, Any] | None = None
    error: str | None = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def model_dump(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "detail": self.detail,
            "result": self.result,
            "error": self.error,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


@dataclass
class TaskRun:
    id: str
    title: str
    status: TaskStatus
    tasks: list[TaskItem]
    created_at: str
    updated_at: str
    metadata: dict[str, Any] = field(default_factory=dict)

    def model_dump(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "tasks": [x.model_dump() for x in self.tasks],
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
        }


def _core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        if (parent / "data").exists() and (parent / "services").exists():
            return parent
    return Path.cwd().resolve()


def _task_state_dir() -> Path:
    path = _core_platform_dir() / "data" / "task_runs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _now() -> str:
    return datetime.utcnow().isoformat() + "Z"


def _run_path(run_id: str) -> Path:
    safe = "".join(ch for ch in run_id if ch.isalnum() or ch in {"-", "_"})
    return _task_state_dir() / f"{safe}.json"


def create_task_run(title: str, tasks: list[str | dict[str, Any]], metadata: dict[str, Any] | None = None) -> TaskRun:
    run_id = "taskrun_" + uuid.uuid4().hex
    now = _now()
    items: list[TaskItem] = []
    for index, raw in enumerate(tasks, 1):
        if isinstance(raw, dict):
            item_title = str(raw.get("title") or f"Task {index}")
            detail = raw.get("detail")
        else:
            item_title = str(raw)
            detail = None
        items.append(
            TaskItem(
                id=f"task_{index}",
                title=item_title,
                detail=str(detail) if detail is not None else None,
                created_at=now,
                updated_at=now,
            )
        )
    run = TaskRun(
        id=run_id,
        title=title,
        status="pending",
        tasks=items,
        created_at=now,
        updated_at=now,
        metadata=metadata or {},
    )
    save_task_run(run)
    return run


def save_task_run(run: TaskRun) -> None:
    _run_path(run.id).write_text(json.dumps(run.model_dump(), ensure_ascii=False, indent=2), encoding="utf-8")


def load_task_run(run_id: str) -> TaskRun:
    path = _run_path(run_id)
    data = json.loads(path.read_text(encoding="utf-8"))
    tasks = [
        TaskItem(
            id=item["id"],
            title=item["title"],
            status=item.get("status", "pending"),
            detail=item.get("detail"),
            result=item.get("result"),
            error=item.get("error"),
            created_at=item.get("created_at", _now()),
            updated_at=item.get("updated_at", _now()),
        )
        for item in data.get("tasks", [])
    ]
    return TaskRun(
        id=data["id"],
        title=data.get("title", data["id"]),
        status=data.get("status", "pending"),
        tasks=tasks,
        created_at=data.get("created_at", _now()),
        updated_at=data.get("updated_at", _now()),
        metadata=data.get("metadata", {}),
    )


def list_task_runs(limit: int = 50) -> list[dict[str, Any]]:
    files = sorted(_task_state_dir().glob("taskrun_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    rows = []
    for path in files[:limit]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            rows.append({
                "id": data.get("id"),
                "title": data.get("title"),
                "status": data.get("status"),
                "task_count": len(data.get("tasks", [])),
                "updated_at": data.get("updated_at"),
            })
        except Exception:
            continue
    return rows


def update_task_status(
    run_id: str,
    task_id: str,
    status: TaskStatus,
    result: dict[str, Any] | None = None,
    error: str | None = None,
) -> TaskRun:
    run = load_task_run(run_id)
    found = False
    for task in run.tasks:
        if task.id == task_id:
            task.status = status
            task.result = result
            task.error = error
            task.updated_at = _now()
            found = True
            break
    if not found:
        raise ValueError(f"task not found: {task_id}")
    run.status = derive_run_status(run)
    run.updated_at = _now()
    save_task_run(run)
    return run


def start_next_pending_task(run_id: str) -> TaskRun:
    run = load_task_run(run_id)
    for task in run.tasks:
        if task.status == "pending":
            task.status = "in_progress"
            task.updated_at = _now()
            run.status = "in_progress"
            run.updated_at = _now()
            save_task_run(run)
            return run
    run.status = derive_run_status(run)
    run.updated_at = _now()
    save_task_run(run)
    return run


def derive_run_status(run: TaskRun) -> TaskStatus:
    statuses = [task.status for task in run.tasks]
    if not statuses:
        return "completed"
    if any(status == "failed" for status in statuses):
        return "failed"
    if any(status == "blocked" for status in statuses):
        return "blocked"
    if all(status == "completed" for status in statuses):
        return "completed"
    if any(status == "in_progress" for status in statuses):
        return "in_progress"
    if all(status == "cancelled" for status in statuses):
        return "cancelled"
    return "pending"


def task_progress(run: TaskRun) -> dict[str, Any]:
    total = len(run.tasks)
    completed = sum(1 for task in run.tasks if task.status == "completed")
    failed = sum(1 for task in run.tasks if task.status == "failed")
    in_progress = sum(1 for task in run.tasks if task.status == "in_progress")
    pending = sum(1 for task in run.tasks if task.status == "pending")
    return {
        "run_id": run.id,
        "status": run.status,
        "total": total,
        "completed": completed,
        "failed": failed,
        "in_progress": in_progress,
        "pending": pending,
        "percent": round((completed / total) * 100, 2) if total else 100.0,
    }


def append_task(run_id: str, title: str, detail: str | None = None) -> TaskRun:
    run = load_task_run(run_id)
    next_index = len(run.tasks) + 1
    run.tasks.append(
        TaskItem(
            id=f"task_{next_index}",
            title=title,
            detail=detail,
            created_at=_now(),
            updated_at=_now(),
        )
    )
    run.status = derive_run_status(run)
    run.updated_at = _now()
    save_task_run(run)
    return run
