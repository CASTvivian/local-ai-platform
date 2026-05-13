"""FastAPI entrypoint for the MAOMIAI agent runtime service."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from services.agent_runtime_service.app.models import AgentRunRequest
from services.agent_runtime_service.app.planner import build_plan
from services.agent_runtime_service.app.service import run_agent


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
    return {"ok": True, "plan": build_plan(request.message).model_dump()}


@app.post("/agent/run")
def run(request: AgentRunRequest) -> Dict[str, Any]:
    return run_agent(request).model_dump()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=18131)
