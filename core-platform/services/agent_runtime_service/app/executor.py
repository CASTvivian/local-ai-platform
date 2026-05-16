"""Plan executor for the MAOMIAI agent runtime.

Tool dispatch is now registry-driven.  Handlers are registered once at import
time via ``register_default_executor_tools()``; ``execute_plan`` resolves each
tool through the registry and falls back to ``tool_not_registered`` for unknown
names — no more if/elif chains.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, List

from .capability.models import CapabilityMatchRequest
from .capability.service import match_capability
from .builtin.code_agent_core import execute_code_agent_core
from .execution.tool_dispatch_registry import (
    execute_registered_tool,
    has_registered_tool,
    list_registered_tools,
    register_tool,
)
from .mcp.invoker import invoke_mcp
from .mcp.models import MCPInvokeRequest
from .models import AgentPlan, AgentRunRequest, ToolResult
from .security.guard import guard_tool
from .tools import (
    catalog_search,
    disabled,
    model_generate,
    repo_memory_search,
    skill_store_list,
    time_date_math,
    time_now,
    workflow_store_list,
)


def _core_platform_dir_for_executor() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    # Walk upward from __file__ until we find data/agent_policy — that dir is core-platform root.
    for parent in Path(__file__).resolve().parents:
        if (parent / "data" / "agent_policy").is_dir():
            return parent
    # Fallback: same depth as app/executor.py (5 levels up = core-platform).
    return Path(__file__).resolve().parents[3]


def load_capability_status_config() -> dict[str, Any]:
    path = _core_platform_dir_for_executor() / "data" / "agent_policy" / "capability_status.json"
    if not path.exists():
        return {
            "version": "missing",
            "status": {},
            "error": f"capability_status.json not found: {path}",
        }
    return json.loads(path.read_text(encoding="utf-8"))


def execute_mcp_tool(
    tool_name: str,
    arguments: dict,
    run_id: str | None = None,
    session_id: str | None = None,
) -> ToolResult:
    """Invoke a registered MCP-style tool and return a ToolResult."""

    result = invoke_mcp(
        MCPInvokeRequest(
            tool=tool_name,
            arguments=arguments,
            run_id=run_id,
            session_id=session_id,
        )
    )
    return ToolResult(
        tool=tool_name,
        ok=result.ok,
        data={
            **result.result,
            "approval_required": result.approval_required,
            "approval_id": result.approval_id,
        },
        error=result.error,
    )


# ---------------------------------------------------------------------------
# Registry handlers — each receives a flat args dict and returns a ToolResult
# ---------------------------------------------------------------------------

def _handler_time_now(args: dict[str, Any]) -> ToolResult:
    return time_now()


def _handler_time_date_math(args: dict[str, Any]) -> ToolResult:
    offset_days = args.get("offset_days")
    if offset_days is None:
        return ToolResult(
            tool="time.date_math",
            ok=False,
            data={"planner_args": args},
            error="missing offset_days from planner",
        )
    return time_date_math(int(offset_days))


def _handler_weather_query(args: dict[str, Any]) -> ToolResult:
    return execute_mcp_tool(
        "weather.query",
        {
            "location": args.get("location") or args.get("normalized_query", ""),
            "days": 1,
        },
        run_id=args.get("run_id"),
        session_id=args.get("session_id"),
    )


def _handler_web_search(args: dict[str, Any]) -> ToolResult:
    return execute_mcp_tool(
        "web.search",
        {
            "query": args.get("query") or args.get("normalized_query", ""),
            "limit": 5,
            "fetch_top": True,
        },
        run_id=args.get("run_id"),
        session_id=args.get("session_id"),
    )


def _handler_capability_match(args: dict[str, Any]) -> ToolResult:
    result = match_capability(
        CapabilityMatchRequest(
            query=args.get("normalized_query", ""),
            intent=args.get("intent", ""),
            limit=5,
        )
    )
    return ToolResult(tool="capability.match", ok=True, data=result.model_dump())


def _handler_repo_memory_search(args: dict[str, Any]) -> ToolResult:
    mcp_result = execute_mcp_tool(
        "repo_memory.search",
        {"query": args.get("query") or args.get("normalized_query", ""), "limit": 8},
        run_id=args.get("run_id"),
        session_id=args.get("session_id"),
    )
    return mcp_result if mcp_result.ok else repo_memory_search(args.get("query") or args.get("normalized_query", ""))


def _handler_catalog_search(args: dict[str, Any]) -> ToolResult:
    return catalog_search(args.get("normalized_query", ""))


def _handler_skill_store_list(args: dict[str, Any]) -> ToolResult:
    mcp_result = execute_mcp_tool("skill_store.list", {}, run_id=args.get("run_id"), session_id=args.get("session_id"))
    return mcp_result if mcp_result.ok else skill_store_list()


def _handler_workflow_store_list(args: dict[str, Any]) -> ToolResult:
    mcp_result = execute_mcp_tool("workflow_store.list", {}, run_id=args.get("run_id"), session_id=args.get("session_id"))
    return mcp_result if mcp_result.ok else workflow_store_list()


def _handler_capability_status(args: dict[str, Any]) -> ToolResult:
    config = load_capability_status_config()
    return ToolResult(
        tool="capability.status",
        ok=True,
        data={
            "source": "external_config",
            "version": config.get("version"),
            "status": config.get("status", {}),
            "error": config.get("error"),
        },
    )


def _handler_model_generate(args: dict[str, Any]) -> ToolResult:
    mcp_result = execute_mcp_tool(
        "model.generate",
        {
            "prompt": args.get("prompt", ""),
            "profile": args.get("profile"),
            "model": args.get("model"),
        },
        run_id=args.get("run_id"),
        session_id=args.get("session_id"),
    )
    return mcp_result if mcp_result.ok else model_generate(args.get("prompt", ""), args.get("profile"), args.get("model"))


def _handler_builtin_code_agent_core_execute(args: dict[str, Any]) -> ToolResult:
    result = execute_code_agent_core(args or {})
    return ToolResult(
        tool="builtin.code_agent_core.execute",
        ok=bool(result.get("ok")),
        data=result,
        error=result.get("error"),
    )


# ---------------------------------------------------------------------------
# Handler registration — called once at import time
# ---------------------------------------------------------------------------

_DEFAULT_TOOLS_REGISTERED = False


def register_default_executor_tools() -> None:
    """Populate the global dispatch registry with built-in tool handlers."""
    global _DEFAULT_TOOLS_REGISTERED
    if _DEFAULT_TOOLS_REGISTERED:
        return
    _DEFAULT_TOOLS_REGISTERED = True

    register_tool("time.now", _handler_time_now)
    register_tool("time.date_math", _handler_time_date_math)
    register_tool("weather.query", _handler_weather_query)
    register_tool("web.search", _handler_web_search)
    register_tool("capability.match", _handler_capability_match)
    register_tool("repo_memory.search", _handler_repo_memory_search)
    register_tool("catalog.search", _handler_catalog_search)
    register_tool("skill_store.list", _handler_skill_store_list)
    register_tool("workflow_store.list", _handler_workflow_store_list)
    register_tool("capability.status", _handler_capability_status)
    register_tool("model.generate", _handler_model_generate)
    register_tool("builtin.code_agent_core.execute", _handler_builtin_code_agent_core_execute)


register_default_executor_tools()


# ---------------------------------------------------------------------------
# Plan execution — registry-driven, no if/elif
# ---------------------------------------------------------------------------

def execute_plan(
    plan: AgentPlan,
    request: AgentRunRequest,
    run_id: str | None = None,
    session_id: str | None = None,
) -> List[ToolResult]:
    """Execute planner-selected tools in order via the dispatch registry."""

    results: List[ToolResult] = []
    # Pre-index steps by tool name so per-step args can be merged into payloads.
    steps_by_tool: dict[str, dict[str, Any]] = {}
    for step in plan.args.get("steps") or []:
        if isinstance(step, dict) and step.get("tool"):
            steps_by_tool.setdefault(str(step["tool"]), step)
    for tool in plan.tools:
        payload = {
            "run_id": run_id,
            "session_id": session_id or request.session_id,
            "intent": plan.intent,
            "normalized_query": plan.normalized_query,
            "args": plan.args,
            "command": plan.args.get("command", ""),
            # model.generate needs these from the request
            "prompt": request.message_text(),
            "profile": request.model_profile(),
            "model": request.model,
            # time.date_math / weather / repo_memory etc. read from plan.args
            "offset_days": plan.args.get("offset_days"),
            "location": plan.args.get("location"),
            "query": plan.args.get("query"),
            "limit": plan.args.get("limit"),
        }
        # Merge step-level args into the payload so builtin tools receive
        # their structured parameters (task, workspace_root, files, patch, etc.)
        step = steps_by_tool.get(tool)
        if step and isinstance(step.get("args"), dict):
            payload.update(step["args"])

        # Security gate
        blocked = guard_tool(tool, payload)
        if blocked:
            results.append(blocked)
            continue

        # Registry dispatch
        if has_registered_tool(tool):
            dispatch_result = execute_registered_tool(tool, payload)
            if isinstance(dispatch_result, ToolResult):
                results.append(dispatch_result)
            elif isinstance(dispatch_result, dict):
                ok = dispatch_result.get("ok", False)
                data = dispatch_result.get("data", dispatch_result.get("result", {}))
                if isinstance(data, dict):
                    pass
                else:
                    data = {"value": data}
                results.append(
                    ToolResult(
                        tool=tool,
                        ok=ok,
                        data=data,
                        error=dispatch_result.get("error"),
                    )
                )
            else:
                results.append(ToolResult(tool=tool, ok=False, error=f"unexpected handler return type: {type(dispatch_result)}"))
        else:
            results.append(ToolResult(tool=tool, ok=False, error="tool_not_registered"))

    return results


def dispatch_tool_via_registry(tool_name: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
    """Convenience wrapper for ad-hoc registry dispatch outside execute_plan."""
    payload = args if isinstance(args, dict) else {}
    return execute_registered_tool(tool_name, payload)
