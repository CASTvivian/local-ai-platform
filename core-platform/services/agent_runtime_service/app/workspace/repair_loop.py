from __future__ import annotations
import json
import os
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class CommandResult:
    ok: bool
    command: str
    cwd: str
    exit_code: int
    stdout: str
    stderr: str
    elapsed_seconds: float

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "command": self.command,
            "cwd": self.cwd,
            "exit_code": self.exit_code,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "elapsed_seconds": self.elapsed_seconds,
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


def _workspace_root() -> Path:
    env = os.environ.get("MAOMIAI_WORKSPACE_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    return _core_platform_dir()


def _audit_dir() -> Path:
    path = _core_platform_dir() / "data" / "repair_loops"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _resolve_cwd(cwd: str | None = None) -> Path:
    root = _workspace_root().resolve()
    target = Path(cwd).expanduser() if cwd else root
    if not target.is_absolute():
        target = root / target
    target = target.resolve()
    if root not in [target, *target.parents]:
        raise ValueError(f"cwd outside workspace: {target}")
    return target


def run_command(command: str, cwd: str | None = None, timeout: int = 120, max_output: int = 12000) -> CommandResult:
    start = datetime.utcnow()
    target_cwd = _resolve_cwd(cwd)
    proc = subprocess.run(
        command,
        cwd=str(target_cwd),
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=timeout,
    )
    elapsed = (datetime.utcnow() - start).total_seconds()
    return CommandResult(
        ok=proc.returncode == 0,
        command=command,
        cwd=str(target_cwd),
        exit_code=proc.returncode,
        stdout=proc.stdout[-max_output:],
        stderr=proc.stderr[-max_output:],
        elapsed_seconds=elapsed,
    )


def build_repair_context(result: CommandResult) -> dict[str, Any]:
    combined = "\n".join([result.stdout or "", result.stderr or ""]).strip()
    return {
        "ok": False,
        "command": result.command,
        "cwd": result.cwd,
        "exit_code": result.exit_code,
        "stdout_tail": result.stdout[-4000:],
        "stderr_tail": result.stderr[-4000:],
        "error_summary": combined[-4000:],
        "repair_hints": [
            "Inspect the failing file and line from stderr.",
            "Use workspace patch engine to produce a minimal diff.",
            "Re-run the same command after applying patch.",
        ],
    }


def run_build_test_repair_loop(
    command: str,
    cwd: str | None = None,
    repair_action: dict[str, Any] | None = None,
    timeout: int = 120,
) -> dict[str, Any]:
    """Run command once, optionally apply a provided repair action, then re-run.

    This is a foundation loop. It does not guess edits by itself.
    A future agent step can generate ``repair_action`` using model reasoning and
    patch_engine.
    """
    first = run_command(command, cwd=cwd, timeout=timeout)
    steps: list[dict[str, Any]] = [
        {
            "type": "run",
            "phase": "initial",
            "result": first.model_dump(),
        }
    ]
    applied_repair: dict[str, Any] | None = None

    if first.ok:
        summary = {
            "ok": True,
            "status": "passed_initial",
            "steps": steps,
        }
        _write_repair_audit(summary)
        return summary

    repair_context = build_repair_context(first)
    steps.append({
        "type": "repair_context",
        "phase": "after_initial_failure",
        "context": repair_context,
    })

    if repair_action:
        applied_repair = _apply_repair_action(repair_action)
        steps.append({
            "type": "repair_action",
            "phase": "apply_repair",
            "result": applied_repair,
        })
        second = run_command(command, cwd=cwd, timeout=timeout)
        steps.append({
            "type": "run",
            "phase": "after_repair",
            "result": second.model_dump(),
        })
        summary = {
            "ok": second.ok,
            "status": "passed_after_repair" if second.ok else "failed_after_repair",
            "repair_context": repair_context,
            "applied_repair": applied_repair,
            "steps": steps,
        }
        _write_repair_audit(summary)
        return summary

    summary = {
        "ok": False,
        "status": "repair_needed",
        "repair_context": repair_context,
        "steps": steps,
    }
    _write_repair_audit(summary)
    return summary


def _apply_repair_action(action: dict[str, Any]) -> dict[str, Any]:
    from services.agent_runtime_service.app.workspace.patch_engine import (
        apply_replace_file,
        apply_text_replacement,
    )

    kind = action.get("kind")
    if kind == "text_replacement":
        result = apply_text_replacement(
            str(action.get("path") or ""),
            str(action.get("old") or ""),
            str(action.get("new") or ""),
            create_backup=bool(action.get("create_backup", True)),
        )
        return result.model_dump()
    if kind == "replace_file":
        result = apply_replace_file(
            str(action.get("path") or ""),
            str(action.get("new_text") or ""),
            create_backup=bool(action.get("create_backup", True)),
        )
        return result.model_dump()
    return {
        "ok": False,
        "error": "unsupported_repair_action",
        "kind": kind,
    }


def _write_repair_audit(summary: dict[str, Any]) -> None:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"repair_loop_{stamp}.json"
    out.write_text(
        json.dumps(
            {
                "created_at": datetime.utcnow().isoformat() + "Z",
                **summary,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
