"""Plan executor for the MAOMIAI agent runtime."""

from __future__ import annotations

from typing import List

from .models import AgentPlan, AgentRunRequest, ToolResult
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


def execute_plan(plan: AgentPlan, request: AgentRunRequest) -> List[ToolResult]:
    """Execute planner-selected tools in order."""

    results: List[ToolResult] = []
    for tool in plan.tools:
        if tool == "time.now":
            results.append(time_now())
        elif tool == "time.date_math":
            results.append(time_date_math(int(plan.args.get("offset_days") or 0)))
        elif tool == "weather.query":
            results.append(disabled("weather.query", "Weather tool is not enabled yet."))
        elif tool == "web.search":
            results.append(disabled("web.search", "Web search tool is not enabled yet."))
        elif tool == "repo_memory.search":
            results.append(repo_memory_search(plan.normalized_query))
        elif tool == "catalog.search":
            results.append(catalog_search(plan.normalized_query))
        elif tool == "skill_store.list":
            results.append(skill_store_list())
        elif tool == "workflow_store.list":
            results.append(workflow_store_list())
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
            results.append(model_generate(request.message, request.profile, request.model))
        else:
            results.append(ToolResult(tool=tool, ok=False, error="Unknown tool"))
    return results
