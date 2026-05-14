"""Filesystem sandbox restricted to a runtime-owned working directory."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List
import json
import shutil
import uuid

CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
SANDBOX_ROOT = CORE_PLATFORM_ROOT / "data" / "filesystem_sandbox"
SANDBOX_ROOT.mkdir(parents=True, exist_ok=True)


def _sandbox_dir(sandbox_id: str | None = None) -> Path:
    sid = sandbox_id or str(uuid.uuid4())
    path = SANDBOX_ROOT / sid
    path.mkdir(parents=True, exist_ok=True)
    return path


def _safe_path(root: Path, relative_path: str) -> Path:
    if not relative_path:
        raise ValueError("empty path")
    clean = relative_path.replace("\\", "/").lstrip("/")
    target = (root / clean).resolve()
    root_resolved = root.resolve()
    try:
        target.relative_to(root_resolved)
    except ValueError as exc:
        raise ValueError("path escapes sandbox") from exc
    if target == root_resolved:
        raise ValueError("path escapes sandbox")
    return target


def _error(sandbox_id: str | None, path: str, error: Exception) -> Dict[str, Any]:
    return {
        "ok": False,
        "sandbox_id": sandbox_id,
        "path": path,
        "message": str(error),
    }


def create_sandbox() -> Dict[str, Any]:
    root = _sandbox_dir()
    return {
        "ok": True,
        "sandbox_id": root.name,
        "root": str(root),
    }


def write_file(sandbox_id: str | None, path: str, content: str) -> Dict[str, Any]:
    root = _sandbox_dir(sandbox_id)
    try:
        target = _safe_path(root, path)
    except Exception as exc:
        return _error(root.name, path, exc)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content or "", encoding="utf-8")
    return {
        "ok": True,
        "sandbox_id": root.name,
        "path": path,
        "bytes": len((content or "").encode("utf-8")),
    }


def read_file(sandbox_id: str, path: str) -> Dict[str, Any]:
    root = _sandbox_dir(sandbox_id)
    try:
        target = _safe_path(root, path)
    except Exception as exc:
        return _error(root.name, path, exc)
    if not target.exists() or not target.is_file():
        return {
            "ok": False,
            "sandbox_id": root.name,
            "path": path,
            "message": "file not found",
        }
    data = target.read_text(encoding="utf-8", errors="replace")
    return {
        "ok": True,
        "sandbox_id": root.name,
        "path": path,
        "content": data,
    }


def list_files(sandbox_id: str, path: str = ".") -> Dict[str, Any]:
    root = _sandbox_dir(sandbox_id)
    try:
        if path == ".":
            target = root.resolve()
        else:
            target = _safe_path(root, path)
    except Exception as exc:
        return _error(root.name, path, exc)
    if not target.exists():
        return {
            "ok": False,
            "sandbox_id": root.name,
            "path": path,
            "message": "path not found",
        }
    items: List[Dict[str, Any]] = []
    for p in target.iterdir():
        items.append({
            "name": p.name,
            "path": str(p.relative_to(root)),
            "is_dir": p.is_dir(),
            "size": p.stat().st_size if p.is_file() else None,
        })
    return {
        "ok": True,
        "sandbox_id": root.name,
        "path": path,
        "items": items,
    }


def delete_file(sandbox_id: str, path: str) -> Dict[str, Any]:
    root = _sandbox_dir(sandbox_id)
    try:
        target = _safe_path(root, path)
    except Exception as exc:
        return _error(root.name, path, exc)
    if not target.exists():
        return {
            "ok": False,
            "sandbox_id": root.name,
            "path": path,
            "message": "path not found",
        }
    if target.is_dir():
        shutil.rmtree(target)
    else:
        target.unlink()
    return {
        "ok": True,
        "sandbox_id": root.name,
        "path": path,
        "deleted": True,
    }


def export_manifest(sandbox_id: str) -> Dict[str, Any]:
    root = _sandbox_dir(sandbox_id)
    files = []
    for p in root.rglob("*"):
        if p.is_file():
            files.append({
                "path": str(p.relative_to(root)),
                "size": p.stat().st_size,
            })
    manifest = {
        "sandbox_id": root.name,
        "files": files,
    }
    (root / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return {
        "ok": True,
        "sandbox_id": root.name,
        "manifest": manifest,
    }
