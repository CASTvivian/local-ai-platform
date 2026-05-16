from __future__ import annotations
import difflib
import json
import os
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass
class PatchResult:
    ok: bool
    path: str
    action: str
    backup_path: str | None
    diff: str
    message: str
    error: str | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "path": self.path,
            "action": self.action,
            "backup_path": self.backup_path,
            "diff": self.diff,
            "message": self.message,
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


def _workspace_root() -> Path:
    env = os.environ.get("MAOMIAI_WORKSPACE_ROOT")
    if env:
        return Path(env).expanduser().resolve()
    return _core_platform_dir()


def _audit_dir() -> Path:
    path = _core_platform_dir() / "data" / "workspace_patches"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _resolve_workspace_path(path: str | Path) -> Path:
    root = _workspace_root().resolve()
    target = Path(path)
    if not target.is_absolute():
        target = root / target
    target = target.resolve()
    if root not in [target, *target.parents]:
        raise ValueError(f"path outside workspace: {target}")
    return target


def read_workspace_file(path: str, max_bytes: int = 512_000) -> dict[str, Any]:
    target = _resolve_workspace_path(path)
    if not target.exists():
        return {
            "ok": False,
            "path": str(target),
            "error": "file_not_found",
        }
    if not target.is_file():
        return {
            "ok": False,
            "path": str(target),
            "error": "not_a_file",
        }
    data = target.read_bytes()
    truncated = len(data) > max_bytes
    data = data[:max_bytes]
    return {
        "ok": True,
        "path": str(target),
        "text": data.decode("utf-8", errors="replace"),
        "size": target.stat().st_size,
        "truncated": truncated,
    }


def unified_diff(old: str, new: str, fromfile: str = "before", tofile: str = "after") -> str:
    return "".join(
        difflib.unified_diff(
            old.splitlines(True),
            new.splitlines(True),
            fromfile=fromfile,
            tofile=tofile,
        )
    )


def plan_replace_file(path: str, new_text: str) -> dict[str, Any]:
    target = _resolve_workspace_path(path)
    old_text = ""
    if target.exists() and target.is_file():
        old_text = target.read_text(encoding="utf-8", errors="replace")
    diff = unified_diff(old_text, new_text, fromfile=str(target), tofile=str(target))
    return {
        "ok": True,
        "path": str(target),
        "action": "replace_file",
        "diff": diff,
        "old_size": len(old_text.encode("utf-8")),
        "new_size": len(new_text.encode("utf-8")),
    }


def apply_replace_file(path: str, new_text: str, create_backup: bool = True) -> PatchResult:
    target = _resolve_workspace_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    old_text = ""
    backup_path = None
    if target.exists() and target.is_file():
        old_text = target.read_text(encoding="utf-8", errors="replace")
        if create_backup:
            stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
            backup = _audit_dir() / f"{target.name}.{stamp}.bak"
            shutil.copy2(target, backup)
            backup_path = str(backup)

    diff = unified_diff(old_text, new_text, fromfile=str(target), tofile=str(target))
    target.write_text(new_text, encoding="utf-8")

    result = PatchResult(
        ok=True,
        path=str(target),
        action="replace_file",
        backup_path=backup_path,
        diff=diff,
        message="file replaced",
    )
    _write_patch_audit(result)
    return result


def apply_text_replacement(path: str, old: str, new: str, create_backup: bool = True) -> PatchResult:
    target = _resolve_workspace_path(path)
    if not target.exists():
        return PatchResult(
            ok=False,
            path=str(target),
            action="text_replacement",
            backup_path=None,
            diff="",
            message="file not found",
            error="file_not_found",
        )

    old_text = target.read_text(encoding="utf-8", errors="replace")
    if old not in old_text:
        return PatchResult(
            ok=False,
            path=str(target),
            action="text_replacement",
            backup_path=None,
            diff="",
            message="old text not found",
            error="old_text_not_found",
        )

    new_text = old_text.replace(old, new, 1)
    diff = unified_diff(old_text, new_text, fromfile=str(target), tofile=str(target))

    backup_path = None
    if create_backup:
        stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
        backup = _audit_dir() / f"{target.name}.{stamp}.bak"
        shutil.copy2(target, backup)
        backup_path = str(backup)

    target.write_text(new_text, encoding="utf-8")

    result = PatchResult(
        ok=True,
        path=str(target),
        action="text_replacement",
        backup_path=backup_path,
        diff=diff,
        message="text replaced",
    )
    _write_patch_audit(result)
    return result


def _write_patch_audit(result: PatchResult) -> None:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"patch_{stamp}.json"
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
