"""Owned builtin adapter: builtin.code_agent_core

First owned builtin execution adapter that connects:
- task_state (progress tracking)
- patch_engine (workspace file operations)
- repair_loop (build/test/repair cycle)
- audit JSON (execution record)

This adapter does NOT guess arbitrary code changes by itself.
It only executes structured payloads through owned workspace tools.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from services.agent_runtime_service.app.task_state.state_machine import (
    create_task_run,
    start_next_pending_task,
    task_progress,
    update_task_status,
)
from services.agent_runtime_service.app.workspace.patch_engine import (
    plan_replace_file,
    read_workspace_file,
)
from services.agent_runtime_service.app.workspace.repair_loop import (
    run_build_test_repair_loop,
)


@dataclass
class CodeAgentCoreResult:
    ok: bool
    builtin_id: str
    task_run_id: str | None
    summary: str
    patches: list[dict[str, Any]]
    tests: list[dict[str, Any]]
    audit: dict[str, Any]
    error: str | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "builtin_id": self.builtin_id,
            "task_run_id": self.task_run_id,
            "summary": self.summary,
            "patches": self.patches,
            "tests": self.tests,
            "audit": self.audit,
            "error": self.error,
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


def _audit_dir() -> Path:
    path = _core_platform_dir() / "data" / "builtin_runs"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _write_audit(result: CodeAgentCoreResult) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"code_agent_core_{stamp}.json"
    out.write_text(
        json.dumps(
            {
                "created_at": datetime.utcnow().isoformat() + "Z",
                **result.model_dump(),
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return str(out)


def execute_code_agent_core(payload: dict[str, Any]) -> dict[str, Any]:
    """Execute owned builtin.code_agent_core adapter.

    This first version is a safe adapter foundation:
    - tracks task progress via task_state
    - reads requested files via patch_engine
    - plans a full-file patch when new_text is supplied
    - runs a build/test command through repair_loop
    - writes audit JSON

    It does not guess arbitrary code changes by itself.
    """
    task = str(payload.get("task") or "").strip()
    files = payload.get("files") or []
    patch = payload.get("patch") or {}
    test_command = payload.get("test_command")
    workspace_root = payload.get("workspace_root")

    if workspace_root:
        os.environ["MAOMIAI_WORKSPACE_ROOT"] = str(workspace_root)

    # --- guard: missing task ---
    if not task:
        result = CodeAgentCoreResult(
            ok=False,
            builtin_id="builtin.code_agent_core",
            task_run_id=None,
            summary="missing task",
            patches=[],
            tests=[],
            audit={},
            error="missing_task",
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data

    # --- create task run ---
    run = create_task_run(
        title=f"builtin.code_agent_core: {task}",
        tasks=[
            "inspect requested files",
            "plan patch if patch payload provided",
            "run build/test command if provided",
            "summarize result",
        ],
        metadata={
            "builtin_id": "builtin.code_agent_core",
            "source": "owned_builtin_adapter",
        },
    )

    patches: list[dict[str, Any]] = []
    tests: list[dict[str, Any]] = []
    inspected: list[dict[str, Any]] = []

    try:
        # --- step 1: inspect files ---
        run = start_next_pending_task(run.id)
        for file_path in files:
            inspected.append(read_workspace_file(str(file_path)))
        run = update_task_status(
            run.id,
            "task_1",
            "completed",
            result={
                "file_count": len(files),
                "inspected": inspected,
            },
        )

        # --- step 2: plan patch ---
        run = start_next_pending_task(run.id)
        if patch:
            kind = patch.get("kind")
            if kind == "replace_file":
                planned = plan_replace_file(
                    str(patch.get("path") or ""),
                    str(patch.get("new_text") or ""),
                )
                patches.append(planned)
            else:
                patches.append({
                    "ok": False,
                    "error": "unsupported_patch_kind",
                    "kind": kind,
                })
        run = update_task_status(
            run.id,
            "task_2",
            "completed",
            result={"patches": patches},
        )

        # --- step 3: run test command via repair loop ---
        run = start_next_pending_task(run.id)
        if test_command:
            loop_result = run_build_test_repair_loop(
                str(test_command),
                cwd=payload.get("cwd"),
                repair_action=payload.get("repair_action"),
                timeout=int(payload.get("timeout") or 120),
            )
            tests.append(loop_result)
        run = update_task_status(
            run.id,
            "task_3",
            "completed",
            result={"tests": tests},
        )

        # --- step 4: summarize ---
        run = start_next_pending_task(run.id)
        progress = task_progress(run)
        summary = (
            f"builtin.code_agent_core completed foundation run. "
            f"files={len(files)}, patches={len(patches)}, tests={len(tests)}, "
            f"progress={progress.get('percent')}%"
        )
        run = update_task_status(
            run.id,
            "task_4",
            "completed",
            result={"summary": summary},
        )

        result = CodeAgentCoreResult(
            ok=True,
            builtin_id="builtin.code_agent_core",
            task_run_id=run.id,
            summary=summary,
            patches=patches,
            tests=tests,
            audit={
                "progress": task_progress(run),
                "inspected_count": len(inspected),
            },
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data

    except Exception as exc:
        try:
            update_task_status(run.id, "task_4", "failed", error=str(exc))
        except Exception:
            pass
        result = CodeAgentCoreResult(
            ok=False,
            builtin_id="builtin.code_agent_core",
            task_run_id=run.id,
            summary="builtin.code_agent_core failed",
            patches=patches,
            tests=tests,
            audit={},
            error=str(exc),
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data
