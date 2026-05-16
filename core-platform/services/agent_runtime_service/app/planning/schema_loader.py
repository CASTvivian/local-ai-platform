"""Schema loader for the schema-driven planner.

Loads tool and capability schemas from the agent policy directory,
providing a compact representation suitable for planner prompts.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


def _core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    # app/planning/schema_loader.py -> agent_runtime_service -> services -> core-platform
    return Path(__file__).resolve().parents[4]


def planner_schema_path() -> Path:
    return _core_platform_dir() / "data" / "agent_policy" / "planner_tool_schema.json"


def load_planner_schema() -> dict[str, Any]:
    path = planner_schema_path()
    if not path.exists():
        return {
            "version": "missing",
            "tools": [],
            "capabilities": [],
            "policy": {},
            "error": f"planner schema not found: {path}",
        }
    return json.loads(path.read_text(encoding="utf-8"))


def list_tool_names(schema: dict[str, Any] | None = None) -> list[str]:
    schema = schema or load_planner_schema()
    return [str(item.get("name")) for item in schema.get("tools", []) if item.get("name")]


def compact_schema_for_prompt(schema: dict[str, Any] | None = None) -> dict[str, Any]:
    schema = schema or load_planner_schema()
    return {
        "version": schema.get("version"),
        "planner_contract": schema.get("planner_contract", {}),
        "tools": [
            {
                "name": tool.get("name"),
                "kind": tool.get("kind"),
                "description": tool.get("description"),
                "input_schema": tool.get("input_schema", {}),
                "capabilities": tool.get("capabilities", []),
            }
            for tool in schema.get("tools", [])
        ],
        "capabilities": schema.get("capabilities", []),
        "policy": schema.get("policy", {}),
    }
