"""Bridge approved actions into sandboxed runtime execution."""

from __future__ import annotations

import json
from typing import Any, Dict

from ..security.approval_store import load_approval
from .execution_models import new_execution_record
from .execution_store import save_execution
from .sandbox_executor import execute_sandboxed
from .filesystem_sandbox import write_file, delete_file


def execute_approved_action(approval_id: str) -> Dict[str, Any]:
    """Execute an approved restricted action through the sandbox boundary."""

    record = load_approval(approval_id)
    if not record:
        audit = save_execution(
            new_execution_record(
                approval_id=approval_id,
                tool="unknown",
                status="failed",
                ok=False,
                error="approval not found",
                metadata={"source": "approval_executor"},
            )
        )
        return {
            "ok": False,
            "execution_id": audit.execution_id,
            "message": "approval not found",
            "approval_id": approval_id,
        }

    run_id = record.payload.get("run_id")
    session_id = record.payload.get("session_id")

    if not record.approved:
        audit = save_execution(
            new_execution_record(
                approval_id=approval_id,
                run_id=run_id,
                session_id=session_id,
                tool=record.tool,
                command=str(record.payload.get("command") or "").strip() or None,
                status="blocked",
                ok=False,
                error="approval not granted",
                metadata={"source": "approval_executor"},
            )
        )
        return {
            "ok": False,
            "execution_id": audit.execution_id,
            "message": "approval not granted",
            "approval_id": approval_id,
        }

    if record.tool == "shell.exec":
        command = str(record.payload.get("command") or "").strip()
        if not command:
            audit = save_execution(
                new_execution_record(
                approval_id=approval_id,
                run_id=run_id,
                session_id=session_id,
                tool=record.tool,
                command=command,
                status="failed",
                    ok=False,
                    error="approved shell.exec payload has no command",
                    metadata={"source": "approval_executor"},
                )
            )
            return {
                "ok": False,
                "execution_id": audit.execution_id,
                "message": "approved shell.exec payload has no command",
                "approval_id": approval_id,
            }
        result = execute_sandboxed(command)
        audit = save_execution(
            new_execution_record(
                approval_id=approval_id,
                run_id=run_id,
                session_id=session_id,
                tool=record.tool,
                command=command,
                status="completed" if result.get("ok") else "failed",
                ok=bool(result.get("ok")),
                returncode=result.get("returncode"),
                stdout=result.get("stdout"),
                stderr=result.get("stderr"),
                error=result.get("message"),
                sandbox_id=result.get("sandbox_id"),
                metadata={
                    "source": "approval_executor",
                    "workdir": result.get("workdir"),
                    "argv": result.get("argv"),
                },
            )
        )
        result["execution_id"] = audit.execution_id
        result["approval_id"] = approval_id
        result["tool"] = record.tool
        return result

    if record.tool == "filesystem.write":
        result = write_file(
            sandbox_id=record.payload.get("sandbox_id"),
            path=str(record.payload.get("path") or ""),
            content=str(record.payload.get("content") or ""),
        )
        audit = save_execution(
            new_execution_record(
                approval_id=approval_id,
                run_id=run_id,
                session_id=session_id,
                tool=record.tool,
                command=f"filesystem.write:{record.payload.get('path') or ''}",
                status="completed" if result.get("ok") else "failed",
                ok=bool(result.get("ok")),
                stdout=json.dumps(result, ensure_ascii=False),
                error=result.get("message"),
                sandbox_id=result.get("sandbox_id"),
                metadata={"source": "approval_executor", "filesystem": True},
            )
        )
        result["execution_id"] = audit.execution_id
        result["approval_id"] = approval_id
        result["tool"] = record.tool
        return result

    if record.tool == "filesystem.delete":
        result = delete_file(
            sandbox_id=str(record.payload.get("sandbox_id") or ""),
            path=str(record.payload.get("path") or ""),
        )
        audit = save_execution(
            new_execution_record(
                approval_id=approval_id,
                run_id=run_id,
                session_id=session_id,
                tool=record.tool,
                command=f"filesystem.delete:{record.payload.get('path') or ''}",
                status="completed" if result.get("ok") else "failed",
                ok=bool(result.get("ok")),
                stdout=json.dumps(result, ensure_ascii=False),
                error=result.get("message"),
                sandbox_id=result.get("sandbox_id"),
                metadata={"source": "approval_executor", "filesystem": True},
            )
        )
        result["execution_id"] = audit.execution_id
        result["approval_id"] = approval_id
        result["tool"] = record.tool
        return result

    audit = save_execution(
        new_execution_record(
            approval_id=approval_id,
            run_id=run_id,
            session_id=session_id,
            tool=record.tool or "unknown",
            status="failed",
            ok=False,
            error=f"unsupported approved tool: {record.tool}",
            metadata={"source": "approval_executor"},
        )
    )
    return {
        "ok": False,
        "execution_id": audit.execution_id,
        "message": f"unsupported approved tool: {record.tool}",
        "approval_id": approval_id,
    }
