"""Owned builtin adapter: builtin.memory_rag_core

Second owned builtin execution adapter that connects:
- task_state (progress tracking)
- repo_memory search (knowledge retrieval)
- evidence normalization (structured results)
- audit JSON (execution record)

This adapter retrieves local project knowledge, normalizes evidence,
and produces summaries — no keyword routing, no hardcoded queries.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from services.agent_runtime_service.app.tools import repo_memory_search
from services.agent_runtime_service.app.task_state.state_machine import (
    create_task_run,
    start_next_pending_task,
    task_progress,
    update_task_status,
)


@dataclass
class MemoryRagCoreResult:
    ok: bool
    builtin_id: str
    task_run_id: str | None
    query: str
    matches: list[dict[str, Any]]
    summary: str
    evidence: list[dict[str, Any]]
    audit: dict[str, Any]
    error: str | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "builtin_id": self.builtin_id,
            "task_run_id": self.task_run_id,
            "query": self.query,
            "matches": self.matches,
            "summary": self.summary,
            "evidence": self.evidence,
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


def _write_audit(result: MemoryRagCoreResult) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"memory_rag_core_{stamp}.json"
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


def _normalize_match(raw: Any) -> dict[str, Any]:
    if hasattr(raw, "model_dump"):
        raw = raw.model_dump()
    if isinstance(raw, dict):
        return raw
    return {"text": str(raw)}


def execute_memory_rag_core(payload: dict[str, Any]) -> dict[str, Any]:
    """Execute owned builtin.memory_rag_core adapter.

    Retrieves local project memory, normalizes evidence, and summarizes.
    Three tracked steps: search → normalize → summarize.
    """
    query = str(payload.get("query") or payload.get("task") or "").strip()
    top_k = int(payload.get("top_k") or 8)

    if not query:
        result = MemoryRagCoreResult(
            ok=False,
            builtin_id="builtin.memory_rag_core",
            task_run_id=None,
            query=query,
            matches=[],
            summary="missing query",
            evidence=[],
            audit={},
            error="missing_query",
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data

    run = create_task_run(
        title=f"builtin.memory_rag_core: {query}",
        tasks=[
            "search repo memory",
            "normalize evidence",
            "summarize retrieval result",
        ],
        metadata={
            "builtin_id": "builtin.memory_rag_core",
            "source": "owned_builtin_adapter",
        },
    )

    try:
        # --- step 1: search repo memory ---
        run = start_next_pending_task(run.id)
        tool_result = repo_memory_search(query=query, limit=top_k)
        raw_data = tool_result.data if tool_result.ok else {}
        raw_matches = raw_data.get("matches", []) if isinstance(raw_data, dict) else []
        matches = [_normalize_match(x) for x in raw_matches][:top_k]
        run = update_task_status(
            run.id,
            "task_1",
            "completed",
            result={"match_count": len(matches)},
        )

        # --- step 2: normalize evidence ---
        run = start_next_pending_task(run.id)
        evidence: list[dict[str, Any]] = []
        for item in matches:
            evidence.append({
                "title": item.get("title") or item.get("repo_name") or item.get("source") or "",
                "text": item.get("text") or item.get("summary") or item.get("description") or "",
                "score": item.get("score"),
                "source": item.get("source") or item.get("path") or item.get("repo_url"),
            })
        run = update_task_status(
            run.id,
            "task_2",
            "completed",
            result={"evidence_count": len(evidence)},
        )

        # --- step 3: summarize ---
        run = start_next_pending_task(run.id)
        if evidence:
            summary = "已从本地项目记忆中检索到相关资料：" + "；".join(
                str(x.get("title") or x.get("text") or "")[:80] for x in evidence[:5]
            )
        else:
            summary = "本地项目记忆未检索到明确匹配资料。"
        run = update_task_status(
            run.id,
            "task_3",
            "completed",
            result={"summary": summary},
        )

        result = MemoryRagCoreResult(
            ok=True,
            builtin_id="builtin.memory_rag_core",
            task_run_id=run.id,
            query=query,
            matches=matches,
            summary=summary,
            evidence=evidence,
            audit={
                "progress": task_progress(run),
                "match_count": len(matches),
                "evidence_count": len(evidence),
            },
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data

    except Exception as exc:
        try:
            update_task_status(run.id, "task_3", "failed", error=str(exc))
        except Exception:
            pass
        result = MemoryRagCoreResult(
            ok=False,
            builtin_id="builtin.memory_rag_core",
            task_run_id=run.id,
            query=query,
            matches=[],
            summary="builtin.memory_rag_core failed",
            evidence=[],
            audit={},
            error=str(exc),
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data
