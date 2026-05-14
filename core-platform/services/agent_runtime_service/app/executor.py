"""Plan executor for the MAOMIAI agent runtime."""

from __future__ import annotations

from typing import List

from .capability.models import CapabilityMatchRequest
from .capability.service import match_capability
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


def execute_plan(
    plan: AgentPlan,
    request: AgentRunRequest,
    run_id: str | None = None,
    session_id: str | None = None,
) -> List[ToolResult]:
    """Execute planner-selected tools in order."""

    results: List[ToolResult] = []
    for tool in plan.tools:
        payload = {
            "run_id": run_id,
            "session_id": session_id or request.session_id,
            "intent": plan.intent,
            "normalized_query": plan.normalized_query,
            "args": plan.args,
            "command": plan.args.get("command", ""),
        }
        blocked = guard_tool(tool, payload)
        if blocked:
            results.append(blocked)
            continue

        if tool == "time.now":
            results.append(time_now())
        elif tool == "time.date_math":
            if "offset_days" not in plan.args:
                results.append(
                    ToolResult(
                        tool="time.date_math",
                        ok=False,
                        data={"planner_args": plan.args},
                        error="missing offset_days from planner",
                    )
                )
            else:
                results.append(time_date_math(int(plan.args.get("offset_days"))))
        elif tool == "weather.query":
            results.append(
                execute_mcp_tool(
                    "weather.query",
                    {
                        "location": plan.args.get("location") or plan.normalized_query,
                        "days": 1,
                    },
                    run_id=run_id,
                    session_id=session_id,
                )
            )
        elif tool == "web.search":
            results.append(
                execute_mcp_tool(
                    "web.search",
                    {
                        "query": plan.args.get("query") or plan.normalized_query,
                        "limit": 5,
                        "fetch_top": True,
                    },
                    run_id=run_id,
                    session_id=session_id,
                )
            )
        elif tool == "capability.match":
            result = match_capability(
                CapabilityMatchRequest(
                    query=plan.normalized_query,
                    intent=plan.intent,
                    limit=5,
                )
            )
            results.append(ToolResult(tool="capability.match", ok=True, data=result.model_dump()))
        elif tool == "repo_memory.search":
            mcp_result = execute_mcp_tool(
                "repo_memory.search",
                {"query": plan.args.get("query") or plan.normalized_query, "limit": 8},
                run_id=run_id,
                session_id=session_id,
            )
            results.append(mcp_result if mcp_result.ok else repo_memory_search(plan.args.get("query") or plan.normalized_query))
        elif tool == "catalog.search":
            results.append(catalog_search(plan.normalized_query))
        elif tool == "skill_store.list":
            mcp_result = execute_mcp_tool("skill_store.list", {}, run_id=run_id, session_id=session_id)
            results.append(mcp_result if mcp_result.ok else skill_store_list())
        elif tool == "workflow_store.list":
            mcp_result = execute_mcp_tool("workflow_store.list", {}, run_id=run_id, session_id=session_id)
            results.append(mcp_result if mcp_result.ok else workflow_store_list())
        elif tool == "capability.status":
            results.append(
                ToolResult(
                    tool="capability.status",
                    ok=True,
                    data={
                        "status": "demo_kernel",
                        "enabled": [
                            "desktop_app",
                            "local_model_runtime",
                            "model_download",
                            "model_selection",
                            "repo_memory_assets",
                            "agent_runtime_planner",
                        ],
                        "pending": [
                            "web_search",
                            "weather_tool",
                            "mcp_gateway",
                            "graph_memory",
                            "video_generation_runtime",
                        ],
                    },
                )
            )
        elif tool == "model.generate":
            mcp_result = execute_mcp_tool(
                "model.generate",
                {
                    "prompt": request.message_text(),
                    "profile": request.model_profile(),
                    "model": request.model,
                },
                run_id=run_id,
                session_id=session_id,
            )
            results.append(
                mcp_result if mcp_result.ok else model_generate(request.message_text(), request.model_profile(), request.model)
            )
        else:
            results.append(ToolResult(tool=tool, ok=False, error="Unknown tool"))
    return results
