"""User-facing answer rendering for agent runtime results.

Data-driven renderer: no task_type/intent-specific branches.
Loads templates from external JSON and renders by tool name + result data.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

from .models import AgentPlan, ToolResult


# ---------------------------------------------------------------------------
# Template loader
# ---------------------------------------------------------------------------

def _core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        if (parent / "data").exists() and (parent / "services").exists():
            return parent
    return Path.cwd().resolve()


def _template_path() -> Path:
    return _core_platform_dir() / "data" / "agent_policy" / "renderer_templates.json"


_templates_cache: dict[str, Any] | None = None


def load_renderer_templates() -> dict[str, Any]:
    global _templates_cache
    if _templates_cache is not None:
        return _templates_cache
    path = _template_path()
    if not path.exists():
        _templates_cache = {
            "version": "missing",
            "default": {
                "empty": "No renderable result.",
                "tool_error": "Tool execution failed.",
                "model_unavailable": "Model unavailable.",
            },
            "tool_summaries": {},
        }
        return _templates_cache
    try:
        _templates_cache = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        _templates_cache = {
            "version": "error",
            "default": {"empty": "No renderable result."},
            "tool_summaries": {},
        }
    return _templates_cache


def invalidate_templates_cache() -> None:
    global _templates_cache
    _templates_cache = None


# ---------------------------------------------------------------------------
# Text extraction helpers
# ---------------------------------------------------------------------------

def _as_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return value
    if hasattr(value, "model_dump"):
        try:
            return value.model_dump()
        except Exception:
            pass
    if hasattr(value, "dict"):
        try:
            return value.dict()
        except Exception:
            pass
    return {}


def _text_from_value(value: Any) -> str:
    """Extract best text representation from a tool result value."""
    if value is None:
        return ""
    if isinstance(value, str):
        return value.strip()
    if isinstance(value, (int, float, bool)):
        return str(value)

    data = _as_dict(value)
    if data:
        # Try common key names for text content.
        for key in ("final_answer", "answer", "text", "content", "message", "stdout", "result", "response", "output"):
            item = data.get(key)
            if isinstance(item, str) and item.strip():
                return item.strip()
        # If ok=False with error, show error.
        if data.get("ok") is False and data.get("error"):
            return str(data.get("error"))
        try:
            return json.dumps(data, ensure_ascii=False, indent=2)
        except Exception:
            return str(data)

    if isinstance(value, list):
        parts = [_text_from_value(x) for x in value]
        return "\n".join(x for x in parts if x).strip()

    return str(value).strip()


def _format_template(template: str, text: str, payload: dict[str, Any] | None = None) -> str:
    """Format a template string with {text} and optional payload keys."""
    payload = payload or {}
    # Remove 'text' from payload to avoid duplicate keyword argument.
    safe_payload = {k: v for k, v in payload.items() if k != "text"}
    try:
        return template.format(text=text, **safe_payload)
    except Exception:
        return text or template


# ---------------------------------------------------------------------------
# Tool result rendering
# ---------------------------------------------------------------------------

def render_tool_result(tool_name: str, result: Any) -> str:
    """Render a single tool result using external templates."""
    templates = load_renderer_templates()
    tool_templates = templates.get("tool_summaries", {})
    item = tool_templates.get(tool_name, {}) if isinstance(tool_templates, dict) else {}
    template = item.get("template") if isinstance(item, dict) else None

    text = _text_from_value(result)
    data = _as_dict(result)

    if template:
        return _format_template(str(template), text=text, payload=data).strip()
    # No template — return raw text.
    return text.strip()


# ---------------------------------------------------------------------------
# Main render function (backward-compatible signature)
# ---------------------------------------------------------------------------

def render_answer(plan: AgentPlan, results: list[ToolResult]) -> str:
    """Render a grounded answer from execution results.

    No task_type/intent-specific branches. Priority:
    1. model.generate tool result (if present and ok)
    2. First successful tool result with template
    3. First successful tool result raw text
    4. Error information from failed tools
    5. Default empty template
    """
    templates = load_renderer_templates()
    defaults = templates.get("default", {}) if isinstance(templates.get("default"), dict) else {}

    if not results:
        return str(defaults.get("empty") or "No renderable result.")

    # 1. Prefer model.generate result.
    for item in results:
        if item.tool == "model.generate" and item.ok:
            rendered = render_tool_result("model.generate", item.data)
            if rendered:
                return rendered

    # 2. Collect all successful results.
    successful = [r for r in results if r.ok]
    failed = [r for r in results if not r.ok]

    if successful:
        # Render each with its template and join.
        parts: list[str] = []
        for item in successful:
            rendered = render_tool_result(item.tool, item.data)
            if rendered:
                parts.append(rendered)
        if parts:
            return "\n".join(parts)

    # 3. Show error information.
    if failed:
        error_parts: list[str] = []
        for item in failed:
            err = item.error or "unknown error"
            error_parts.append(f"{item.tool}: {err}")
        return str(defaults.get("tool_error") or "Tool error.") + "\n" + "\n".join(error_parts)

    return str(defaults.get("empty") or "No renderable result.")


# Backward-compatible aliases.
def render(plan: AgentPlan, results: list[ToolResult]) -> str:
    return render_answer(plan, results)
