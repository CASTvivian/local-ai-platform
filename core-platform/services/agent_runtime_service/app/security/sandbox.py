"""Tool sandbox policy for Agent Runtime execution."""

from __future__ import annotations

from typing import Any, Dict


SAFE_TOOLS = {
    "time.now",
    "time.date_math",
    "repo_memory.search",
    "catalog.search",
    "skill_store.list",
    "workflow_store.list",
    "model.generate",
    "capability.match",
    "capability.status",
    "filesystem.read",
    "filesystem.list",
    "weather.query",
    "web.search",
    # Owned builtin adapters — execution paths are fully controlled by
    # owned code with task_state tracking and audit logging.
    "builtin.code_agent_core.execute",
}

RESTRICTED_TOOLS = {
    "shell.exec",
    "filesystem.write",
    "filesystem.delete",
    "browser.open",
    "browser.control",
    "os.command",
}


def evaluate_tool(tool_name: str, payload: Dict[str, Any] | None = None) -> Dict[str, Any]:
    """Evaluate whether a tool can run automatically."""

    if tool_name in SAFE_TOOLS:
        return {
            "allowed": True,
            "requires_approval": False,
            "risk": "low",
        }

    if tool_name in RESTRICTED_TOOLS:
        return {
            "allowed": False,
            "requires_approval": True,
            "risk": "high",
        }

    return {
        "allowed": False,
        "requires_approval": True,
        "risk": "unknown",
    }
