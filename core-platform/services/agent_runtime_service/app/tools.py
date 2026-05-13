"""Tool adapters used by the initial MAOMIAI agent runtime."""

from __future__ import annotations

import json
import urllib.request
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict

from .models import ToolResult


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[3]


def ok(tool: str, data: Dict[str, Any]) -> ToolResult:
    return ToolResult(tool=tool, ok=True, data=data)


def fail(tool: str, error: str, data: Dict[str, Any] | None = None) -> ToolResult:
    return ToolResult(tool=tool, ok=False, error=error, data=data or {})


def time_now() -> ToolResult:
    now = datetime.now()
    return ok(
        "time.now",
        {
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "hour": now.hour,
            "minute": now.minute,
            "weekday": ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][
                now.weekday()
            ],
            "iso": now.isoformat(timespec="seconds"),
        },
    )


def time_date_math(offset_days: int) -> ToolResult:
    now = datetime.now()
    target = now + timedelta(days=offset_days)
    return ok(
        "time.date_math",
        {
            "base": now.date().isoformat(),
            "offset_days": offset_days,
            "target": target.date().isoformat(),
            "target_cn": f"{target.year}年{target.month}月{target.day}日",
            "weekday": ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][
                target.weekday()
            ],
        },
    )


def disabled(tool: str, reason: str) -> ToolResult:
    return fail(tool, reason, {"disabled": True, "reason": reason})


def _post_json(url: str, payload: Dict[str, Any], timeout: int) -> Dict[str, Any]:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="ignore")
    return json.loads(raw)


def _get_json(url: str, timeout: int) -> Dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={"Accept": "application/json"},
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        raw = response.read().decode("utf-8", errors="ignore")
    return json.loads(raw)


def repo_memory_search(query: str, limit: int = 8) -> ToolResult:
    try:
        data = _post_json(
            "http://127.0.0.1:18125/brain/search",
            {"query": query, "limit": limit},
            timeout=5,
        )
        return ok("repo_memory.search", data)
    except Exception as exc:
        return fail("repo_memory.search", str(exc))


def catalog_search(query: str) -> ToolResult:
    files = [
        CORE_PLATFORM_ROOT / "data/brain_assets/model_catalog/open_llm_catalog.json",
        CORE_PLATFORM_ROOT / "data/brain_assets/video_catalog/open_video_model_catalog.json",
        CORE_PLATFORM_ROOT / "data/brain_assets/manifests/context_engine_research_catalog.json",
    ]
    keywords = [token.strip().lower() for token in query.split() if token.strip()]
    results = []

    for path in files:
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            serialized = json.dumps(data, ensure_ascii=False).lower()
            if not keywords or any(keyword in serialized for keyword in keywords):
                results.append({"file": str(path), "data": data})
        except Exception as exc:
            results.append({"file": str(path), "error": str(exc)})

    return ok("catalog.search", {"results": results, "count": len(results)})


def skill_store_list() -> ToolResult:
    try:
        return ok("skill_store.list", _get_json("http://127.0.0.1:18121/list", timeout=5))
    except Exception as exc:
        return fail("skill_store.list", str(exc))


def workflow_store_list() -> ToolResult:
    try:
        return ok("workflow_store.list", _get_json("http://127.0.0.1:18126/list", timeout=5))
    except Exception as exc:
        return fail("workflow_store.list", str(exc))


def model_generate(prompt: str, profile: str | None = None, model: str | None = None) -> ToolResult:
    try:
        data = _post_json(
            "http://127.0.0.1:18080/generate",
            {"prompt": prompt, "profile": profile, "model": model},
            timeout=180,
        )
        return ok("model.generate", data)
    except Exception as exc:
        return fail("model.generate", str(exc))
