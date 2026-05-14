"""Approval gate helpers for tool execution."""

from __future__ import annotations

from typing import Any, Dict

from ..models import ToolResult
from .approval_models import ApprovalRequest, build_record
from .approval_store import save_approval
from .sandbox import evaluate_tool


def guard_tool(tool_name: str, payload: Dict[str, Any] | None = None) -> ToolResult | None:
    """Return a blocking ToolResult when approval is required."""

    policy = evaluate_tool(tool_name, payload or {})
    if not policy["requires_approval"]:
        return None

    record = build_record(
        ApprovalRequest(
            action="tool_execution",
            tool=tool_name,
            payload=payload or {},
            risk=policy["risk"],
        )
    )
    save_approval(record)
    return ToolResult(
        tool=tool_name,
        ok=False,
        data={
            "blocked": True,
            "requires_approval": True,
            "approval_id": record.approval_id,
            "risk": record.risk,
        },
        error="Tool execution requires approval.",
    )
