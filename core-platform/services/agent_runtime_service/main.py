"""FastAPI entrypoint for the MAOMIAI agent runtime service."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.agent_runtime_service.app.health.service import agent_health
from services.agent_runtime_service.app.health.planner_health import (
    planner_runtime_state,
    check_model_gateway,
)


SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from services.agent_runtime_service.app.capability.models import Capability, CapabilityMatchRequest
from services.agent_runtime_service.app.capability.registry import (
    get_capability,
    list_capabilities,
    upsert_capability,
)
from services.agent_runtime_service.app.capability.service import match_capability
from services.agent_runtime_service.app.models import AgentRunRequest
from services.agent_runtime_service.app.mcp.invoker import invoke_mcp
from services.agent_runtime_service.app.team.models import TeamRunRequest
from services.agent_runtime_service.app.team.registry import list_teams, get_team
from services.agent_runtime_service.app.team.coordinator import run_team
from services.agent_runtime_service.app.team.store import load_team_run, list_team_runs
from services.agent_runtime_service.app.mcp.models import MCPInvokeRequest, MCPTool
from services.agent_runtime_service.app.mcp.registry import get_tool, list_tools, upsert_tool
from services.agent_runtime_service.app.planner import build_plan
from services.agent_runtime_service.app.replay.timeline import build_run_timeline
from services.agent_runtime_service.app.run_store.store import load_run
from services.agent_runtime_service.app.runtime.approval_executor import execute_approved_action
from services.agent_runtime_service.app.runtime.browser_models import BrowserFetchRequest
from services.agent_runtime_service.app.runtime.browser_runtime import (
    fetch_url,
    list_snapshots,
    load_snapshot,
)
from services.agent_runtime_service.app.runtime.execution_store import (
    list_executions,
    load_execution,
)
from services.agent_runtime_service.app.runtime.filesystem_models import (
    FileDeleteRequest,
    FileListRequest,
    FileReadRequest,
    FileWriteRequest,
)
from services.agent_runtime_service.app.runtime.filesystem_sandbox import (
    create_sandbox,
    delete_file,
    export_manifest,
    list_files,
    read_file,
    write_file,
)
from services.agent_runtime_service.app.runtime.sandbox_policy import (
    load_sandbox_policy,
    get_sandbox_profile,
)
from services.agent_runtime_service.app.runtime.web_search_models import WebSearchRequest
from services.agent_runtime_service.app.runtime.web_search_runtime import list_web_searches, search_web
from services.agent_runtime_service.app.runtime.weather_models import WeatherQueryRequest
from services.agent_runtime_service.app.runtime.weather_runtime import list_weather_queries, query_weather
from services.agent_runtime_service.app.security.approval_models import ApprovalDecision
from services.agent_runtime_service.app.security.approval_store import (
    list_approvals,
    load_approval,
    resolve_approval,
)
from services.agent_runtime_service.app.session_store.store import load_session
from services.agent_runtime_service.app.service import run_agent_loop


app = FastAPI(title="MAOMIAI Agent Runtime Service", version="0.1.0-c23-b")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "ok": True,
        "service": "agent_runtime_service",
        "version": "0.1.0-c23-b",
        "port": 18131,
    }


@app.get("/agent/tools")
def tools() -> Dict[str, Any]:
    return {
        "ok": True,
        "tools": [
            {"id": "time.now", "enabled": True},
            {"id": "time.date_math", "enabled": True},
            {"id": "repo_memory.search", "enabled": True, "depends_on": "18125"},
            {"id": "catalog.search", "enabled": True},
            {"id": "skill_store.list", "enabled": True, "depends_on": "18121"},
            {"id": "workflow_store.list", "enabled": True, "depends_on": "18126"},
            {"id": "model.generate", "enabled": True, "depends_on": "18080"},
            {"id": "weather.query", "enabled": False},
            {"id": "web.search", "enabled": False},
        ],
    }


@app.post("/agent/plan")
def plan(request: AgentRunRequest) -> Dict[str, Any]:
    return {"ok": True, "plan": build_plan(request.message_text()).model_dump()}


@app.post("/agent/run")
async def run(request: AgentRunRequest) -> Dict[str, Any]:
    return (await run_agent_loop(request)).model_dump()


@app.get("/agent/run/{run_id}")
async def get_run(run_id: str) -> Dict[str, Any]:
    run_state = load_run(run_id)
    if not run_state:
        return {"ok": False, "error": "run_not_found", "run_id": run_id}
    return {"ok": True, "run": run_state.model_dump()}


@app.get("/agent/session/{session_id}")
async def get_session(session_id: str) -> Dict[str, Any]:
    session_state = load_session(session_id)
    if not session_state:
        return {"ok": False, "error": "session_not_found", "session_id": session_id}
    return {"ok": True, "session": session_state.model_dump()}


@app.get("/agent/approvals")
def agent_approvals() -> Dict[str, Any]:
    return {
        "ok": True,
        "items": [item.model_dump() for item in list_approvals()],
    }


@app.get("/agent/approval/{approval_id}")
def agent_approval(approval_id: str) -> Dict[str, Any]:
    item = load_approval(approval_id)
    if not item:
        return {"ok": False, "error": "approval_not_found", "approval_id": approval_id}
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/approval/resolve")
def agent_approval_resolve(decision: ApprovalDecision) -> Dict[str, Any]:
    item = resolve_approval(decision)
    if not item:
        return {"ok": False, "error": "approval_not_found", "approval_id": decision.approval_id}
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/approval/execute/{approval_id}")
def execute_approval(approval_id: str) -> Dict[str, Any]:
    return execute_approved_action(approval_id)


@app.get("/agent/executions")
def agent_executions(
    run_id: str | None = None,
    approval_id: str | None = None,
    limit: int = 100,
) -> Dict[str, Any]:
    return {
        "ok": True,
        "items": list_executions(run_id=run_id, approval_id=approval_id, limit=limit),
    }


@app.get("/agent/execution/{execution_id}")
def agent_execution(execution_id: str) -> Dict[str, Any]:
    item = load_execution(execution_id)
    if not item:
        return {"ok": False, "error": "execution_not_found", "execution_id": execution_id}
    return {"ok": True, "item": item.model_dump()}


@app.get("/agent/replay/run/{run_id}")
def agent_replay_run(run_id: str) -> Dict[str, Any]:
    return {
        "ok": True,
        "run_id": run_id,
        "executions": list_executions(run_id=run_id, limit=500),
    }


@app.get("/agent/replay/approval/{approval_id}")
def agent_replay_approval(approval_id: str) -> Dict[str, Any]:
    return {
        "ok": True,
        "approval_id": approval_id,
        "executions": list_executions(approval_id=approval_id, limit=500),
    }


@app.get("/agent/replay/timeline/{run_id}")
def agent_replay_timeline(run_id: str) -> Dict[str, Any]:
    return build_run_timeline(run_id).model_dump()


@app.get("/agent/mcp/tools")
def agent_mcp_tools() -> Dict[str, Any]:
    return {"ok": True, "items": list_tools()}


@app.get("/agent/mcp/tool/{tool_name}")
def agent_mcp_tool(tool_name: str) -> Dict[str, Any]:
    item = get_tool(tool_name)
    if not item:
        return {"ok": False, "error": "tool_not_found", "tool": tool_name}
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/mcp/tool")
def agent_mcp_upsert_tool(tool: MCPTool) -> Dict[str, Any]:
    item = upsert_tool(tool)
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/mcp/invoke")
def agent_mcp_invoke(request: MCPInvokeRequest) -> Dict[str, Any]:
    return invoke_mcp(request).model_dump()


@app.get("/agent/capabilities")
def agent_capabilities(enabled_only: bool = False) -> Dict[str, Any]:
    return {"ok": True, "items": list_capabilities(enabled_only=enabled_only)}


@app.get("/agent/capability/{capability_id}")
def agent_capability(capability_id: str) -> Dict[str, Any]:
    item = get_capability(capability_id)
    if not item:
        return {"ok": False, "error": "capability_not_found", "capability_id": capability_id}
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/capability")
def agent_upsert_capability(capability: Capability) -> Dict[str, Any]:
    item = upsert_capability(capability)
    return {"ok": True, "item": item.model_dump()}


@app.post("/agent/capabilities/match")
def agent_match_capabilities(request: CapabilityMatchRequest) -> Dict[str, Any]:
    return match_capability(request).model_dump()


@app.post("/agent/filesystem/sandbox")
def agent_filesystem_create_sandbox() -> Dict[str, Any]:
    return create_sandbox()


@app.post("/agent/filesystem/write")
def agent_filesystem_write(request: FileWriteRequest) -> Dict[str, Any]:
    return write_file(request.sandbox_id, request.path, request.content)


@app.post("/agent/filesystem/read")
def agent_filesystem_read(request: FileReadRequest) -> Dict[str, Any]:
    return read_file(request.sandbox_id, request.path)


@app.post("/agent/filesystem/list")
def agent_filesystem_list(request: FileListRequest) -> Dict[str, Any]:
    return list_files(request.sandbox_id, request.path)


@app.post("/agent/filesystem/delete")
def agent_filesystem_delete(request: FileDeleteRequest) -> Dict[str, Any]:
    return delete_file(request.sandbox_id, request.path)


@app.get("/agent/filesystem/manifest/{sandbox_id}")
def agent_filesystem_manifest(sandbox_id: str) -> Dict[str, Any]:
    return export_manifest(sandbox_id)


@app.post("/agent/browser/fetch")
def agent_browser_fetch(request: BrowserFetchRequest) -> Dict[str, Any]:
    return fetch_url(request)


@app.get("/agent/browser/snapshots")
def agent_browser_snapshots(limit: int = 100) -> Dict[str, Any]:
    return list_snapshots(limit=limit)


@app.get("/agent/browser/snapshot/{snapshot_id}")
def agent_browser_snapshot(snapshot_id: str) -> Dict[str, Any]:
    return load_snapshot(snapshot_id)


@app.post("/agent/web/search")
def agent_web_search(request: WebSearchRequest) -> Dict[str, Any]:
    return search_web(request)


@app.get("/agent/web/searches")
def agent_web_searches(limit: int = 100) -> Dict[str, Any]:
    return list_web_searches(limit=limit)


@app.post("/agent/weather/query")
def agent_weather_query(request: WeatherQueryRequest) -> Dict[str, Any]:
    return query_weather(request)


@app.get("/agent/weather/queries")
def agent_weather_queries(limit: int = 100) -> Dict[str, Any]:
    return list_weather_queries(limit=limit)


@app.get("/agent/health")
def agent_health_api(check_live: bool = False) -> Dict[str, Any]:
    return agent_health(check_live=check_live)


@app.get("/agent/health/planner")
def agent_planner_health_api(check_live: bool = False) -> Dict[str, Any]:
    if check_live:
        check_model_gateway()
    return planner_runtime_state(check_live=False).model_dump()


@app.get("/agent/team/registry")
def agent_team_registry():
    return {
        "ok": True,
        "items": list_teams(),
    }


@app.get("/agent/team/{team_id}")
def agent_team_get(team_id: str):
    item = get_team(team_id)
    if not item:
        return {
            "ok": False,
            "message": "team not found",
        }
    return {
        "ok": True,
        "item": item.model_dump(),
    }


@app.post("/agent/team/run")
def agent_team_run(req: TeamRunRequest):
    return run_team(req)


@app.get("/agent/team/runs")
def agent_team_runs(limit: int = 100):
    return {
        "ok": True,
        "items": list_team_runs(limit=limit),
    }


@app.get("/agent/team/run/{team_run_id}")
def agent_team_run_get(team_run_id: str):
    item = load_team_run(team_run_id)
    if not item:
        return {
            "ok": False,
            "message": "team run not found",
        }
    return {
        "ok": True,
        "item": item.model_dump(),
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=18131)
