"""Owned builtin adapter: builtin.browser_operator

Browser/research planning adapter — safe foundation version.

Connects:
- task_state (progress tracking)
- web.search (optional internet search)
- evidence normalization (structured findings + citations)
- audit JSON (execution record)

This adapter creates browser/research action plans, optionally runs web search,
normalizes findings and citations, and produces summaries.
It does NOT perform uncontrolled browser actions.
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from services.agent_runtime_service.app.runtime.web_search_models import WebSearchRequest
from services.agent_runtime_service.app.runtime.web_search_runtime import search_web
from services.agent_runtime_service.app.task_state.state_machine import (
    create_task_run,
    start_next_pending_task,
    task_progress,
    update_task_status,
)


@dataclass
class BrowserOperatorResult:
    ok: bool
    builtin_id: str
    task_run_id: str | None
    research_task: str
    action_plan: list[dict[str, Any]]
    findings: list[dict[str, Any]]
    citations: list[dict[str, Any]]
    audit: dict[str, Any]
    error: str | None = None

    def model_dump(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "builtin_id": self.builtin_id,
            "task_run_id": self.task_run_id,
            "research_task": self.research_task,
            "action_plan": self.action_plan,
            "findings": self.findings,
            "citations": self.citations,
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


def _write_audit(result: BrowserOperatorResult) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"browser_operator_{stamp}.json"
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


def _build_action_plan(task: str, allowed_domains: list[str]) -> list[dict[str, Any]]:
    """Generate a structured browser/research action plan."""
    steps = [
        {
            "step": 1,
            "action": "clarify_research_goal",
            "description": "Identify the exact information needed and expected evidence.",
        },
        {
            "step": 2,
            "action": "search_web",
            "description": "Run a web search using the research task.",
        },
        {
            "step": 3,
            "action": "extract_evidence",
            "description": "Extract structured findings, sources, dates and confidence notes.",
        },
        {
            "step": 4,
            "action": "summarize",
            "description": "Return findings with citations and audit trail.",
        },
    ]
    if allowed_domains:
        steps.insert(
            2,
            {
                "step": 3,
                "action": "apply_domain_constraint",
                "description": "Restrict evidence to allowed domains.",
                "allowed_domains": allowed_domains,
            },
        )
        for index, step in enumerate(steps, 1):
            step["step"] = index
    return steps


def _normalize_web_results(raw: Any) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Normalize web search results into structured findings and citations."""
    if hasattr(raw, "model_dump"):
        raw = raw.model_dump()
    if not isinstance(raw, dict):
        return [], []

    data = raw.get("data") if "data" in raw else raw
    if not isinstance(data, dict):
        return [], []

    rows = data.get("results") or data.get("items") or data.get("matches") or []
    findings: list[dict[str, Any]] = []
    citations: list[dict[str, Any]] = []

    if isinstance(rows, list):
        for item in rows[:8]:
            if hasattr(item, "model_dump"):
                item = item.model_dump()
            if not isinstance(item, dict):
                item = {"text": str(item)}
            title = item.get("title") or item.get("name") or ""
            url = item.get("url") or item.get("link") or item.get("source") or ""
            snippet = item.get("snippet") or item.get("summary") or item.get("text") or ""
            findings.append({
                "title": title,
                "snippet": snippet,
                "url": url,
            })
            if url:
                citations.append({
                    "title": title,
                    "url": url,
                })

    return findings, citations


def execute_browser_operator(payload: dict[str, Any]) -> dict[str, Any]:
    """Execute owned builtin.browser_operator adapter.

    Creates a browser/research action plan, optionally calls web search,
    normalizes findings/citations, and writes audit JSON.

    Three tracked steps: plan → search → normalize.
    """
    task = str(
        payload.get("research_task")
        or payload.get("task")
        or payload.get("query")
        or ""
    ).strip()
    allowed_domains = payload.get("allowed_domains") or []
    do_search = bool(payload.get("do_search", True))

    if not isinstance(allowed_domains, list):
        allowed_domains = []

    if not task:
        result = BrowserOperatorResult(
            ok=False,
            builtin_id="builtin.browser_operator",
            task_run_id=None,
            research_task=task,
            action_plan=[],
            findings=[],
            citations=[],
            audit={},
            error="missing_research_task",
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data

    run = create_task_run(
        title=f"builtin.browser_operator: {task}",
        tasks=[
            "create browser/research action plan",
            "run optional web search",
            "normalize findings and citations",
        ],
        metadata={
            "builtin_id": "builtin.browser_operator",
            "source": "owned_builtin_adapter",
        },
    )

    findings: list[dict[str, Any]] = []
    citations: list[dict[str, Any]] = []
    action_plan = _build_action_plan(task, allowed_domains)

    try:
        # --- step 1: create action plan ---
        run = start_next_pending_task(run.id)
        run = update_task_status(
            run.id,
            "task_1",
            "completed",
            result={"action_plan": action_plan},
        )

        # --- step 2: optional web search ---
        run = start_next_pending_task(run.id)
        if do_search:
            try:
                search_result = search_web(
                    WebSearchRequest(query=task, limit=8)
                )
                if hasattr(search_result, "model_dump"):
                    raw = search_result.model_dump()
                elif hasattr(search_result, "__dict__"):
                    raw = search_result.__dict__
                else:
                    raw = search_result if isinstance(search_result, dict) else {}
                findings, citations = _normalize_web_results(raw)
            except Exception as exc:
                findings = []
                citations = []
                run = update_task_status(
                    run.id,
                    "task_2",
                    "completed",
                    result={"search_error": str(exc), "search_used": False},
                )
            else:
                run = update_task_status(
                    run.id,
                    "task_2",
                    "completed",
                    result={"search_used": True, "finding_count": len(findings)},
                )
        else:
            run = update_task_status(
                run.id,
                "task_2",
                "completed",
                result={"search_used": False},
            )

        # --- step 3: normalize findings and citations ---
        run = start_next_pending_task(run.id)
        run = update_task_status(
            run.id,
            "task_3",
            "completed",
            result={
                "finding_count": len(findings),
                "citation_count": len(citations),
            },
        )

        result = BrowserOperatorResult(
            ok=True,
            builtin_id="builtin.browser_operator",
            task_run_id=run.id,
            research_task=task,
            action_plan=action_plan,
            findings=findings,
            citations=citations,
            audit={
                "progress": task_progress(run),
                "finding_count": len(findings),
                "citation_count": len(citations),
                "search_used": do_search,
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
        result = BrowserOperatorResult(
            ok=False,
            builtin_id="builtin.browser_operator",
            task_run_id=run.id,
            research_task=task,
            action_plan=action_plan,
            findings=findings,
            citations=citations,
            audit={},
            error=str(exc),
        )
        audit_path = _write_audit(result)
        data = result.model_dump()
        data["audit"]["audit_path"] = audit_path
        return data
