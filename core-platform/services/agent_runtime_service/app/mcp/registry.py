"""Runtime MCP-style tool registry."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from .models import MCPTool


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
REGISTRY_ROOT = CORE_PLATFORM_ROOT / "data" / "mcp_registry"
REGISTRY_FILE = REGISTRY_ROOT / "tools.json"

DEFAULT_TOOLS = [
    MCPTool(
        name="repo_memory.search",
        description="Search local repository memory and brain asset summaries.",
        endpoint="http://127.0.0.1:18125/brain/search",
        method="POST",
        input_schema={"query": "string", "limit": "integer"},
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["memory", "repo", "rag"],
    ),
    MCPTool(
        name="skill_store.list",
        description="List local skill store capabilities.",
        endpoint="http://127.0.0.1:18121/skills",
        method="GET",
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["skills", "capability"],
    ),
    MCPTool(
        name="workflow_store.list",
        description="List local workflow store definitions.",
        endpoint="http://127.0.0.1:18126/workflows",
        method="GET",
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["workflow"],
    ),
    MCPTool(
        name="model.generate",
        description="Generate local model response through model gateway.",
        endpoint="http://127.0.0.1:18080/generate",
        method="POST",
        input_schema={"prompt": "string", "profile": "string", "model": "string"},
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["model", "llm"],
    ),
    MCPTool(
        name="shell.exec",
        description="Execute shell command in sandbox after approval.",
        endpoint=None,
        method="LOCAL",
        input_schema={"command": "string"},
        risk="high",
        enabled=True,
        requires_approval=True,
        tags=["shell", "sandbox"],
    ),
    MCPTool(
        name="filesystem.write",
        description="Write file inside filesystem sandbox after approval.",
        endpoint=None,
        method="LOCAL",
        input_schema={"sandbox_id": "string", "path": "string", "content": "string"},
        risk="high",
        enabled=True,
        requires_approval=True,
        tags=["filesystem", "sandbox", "write"],
    ),
    MCPTool(
        name="filesystem.read",
        description="Read file from filesystem sandbox.",
        endpoint=None,
        method="LOCAL",
        input_schema={"sandbox_id": "string", "path": "string"},
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["filesystem", "sandbox", "read"],
    ),
    MCPTool(
        name="filesystem.list",
        description="List files in filesystem sandbox.",
        endpoint=None,
        method="LOCAL",
        input_schema={"sandbox_id": "string", "path": "string"},
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["filesystem", "sandbox", "list"],
    ),
    MCPTool(
        name="filesystem.delete",
        description="Delete file or directory inside filesystem sandbox after approval.",
        endpoint=None,
        method="LOCAL",
        input_schema={"sandbox_id": "string", "path": "string"},
        risk="high",
        enabled=True,
        requires_approval=True,
        tags=["filesystem", "sandbox", "delete"],
    ),
    MCPTool(
        name="browser.fetch",
        description="Fetch public http/https webpage into a local browser snapshot with SSRF protection.",
        endpoint=None,
        method="LOCAL",
        input_schema={"url": "string", "timeout": "integer", "max_bytes": "integer"},
        risk="medium",
        enabled=True,
        requires_approval=False,
        tags=["browser", "web", "fetch", "snapshot"],
    ),
    MCPTool(
        name="web.search",
        description="Search public web and optionally fetch the top result into a browser snapshot.",
        endpoint=None,
        method="LOCAL",
        input_schema={"query": "string", "limit": "integer", "fetch_top": "boolean"},
        risk="medium",
        enabled=True,
        requires_approval=False,
        tags=["web", "search", "realtime", "browser"],
    ),
    MCPTool(
        name="weather.query",
        description="Query weather through provider geocoding and Open-Meteo forecast APIs.",
        endpoint=None,
        method="LOCAL",
        input_schema={"location": "string", "days": "integer"},
        risk="low",
        enabled=True,
        requires_approval=False,
        tags=["weather", "realtime", "geocoding"],
    ),
]


def ensure_registry() -> None:
    """Create runtime registry file when it does not exist."""

    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    if not REGISTRY_FILE.exists():
        save_tools(DEFAULT_TOOLS)


def load_tools() -> List[MCPTool]:
    """Load registered tools from runtime registry."""

    ensure_registry()
    data = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    return [MCPTool.model_validate(item) for item in data]


def list_tools() -> List[dict]:
    """Return registered tools as dictionaries for API responses."""

    return [tool.model_dump() for tool in load_tools()]


def get_tool(name: str) -> Optional[MCPTool]:
    """Return one registered tool by name."""

    for tool in load_tools():
        if tool.name == name:
            return tool
    return None


def save_tools(tools: List[MCPTool]) -> None:
    """Persist runtime tool registry."""

    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    REGISTRY_FILE.write_text(
        json.dumps([tool.model_dump() for tool in tools], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def upsert_tool(tool: MCPTool) -> MCPTool:
    """Insert or replace a runtime tool definition."""

    tools = load_tools()
    for index, existing in enumerate(tools):
        if existing.name == tool.name:
            tools[index] = tool
            save_tools(tools)
            return tool
    tools.append(tool)
    save_tools(tools)
    return tool
