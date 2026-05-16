# C25-C14-B9 Executor Tool Dispatch Registry

## Goal
Move executor away from hardcoded tool dispatch if/elif chains to a registry-driven lookup.

## Problem
`executor.py` had a 13-branch `if tool == "xxx": … elif tool == "yyy": …` chain in `execute_plan()`. Adding a new tool required editing the executor — a structural hardcode.

## Implemented

### New file: `app/execution/tool_dispatch_registry.py`
- `ToolDispatchRegistry` class with `register()`, `has()`, `names()`, `execute()`
- Module-level singleton with convenience API: `register_tool()`, `execute_registered_tool()`, `list_registered_tools()`, `has_registered_tool()`
- Handlers can return `ToolResult` (Pydantic) or `dict`; unknown tools return `{"error": "tool_not_registered"}`

### Rewritten: `app/executor.py`
- All 11 tool handlers extracted as `_handler_*` functions
- `register_default_executor_tools()` registers all handlers at import time (idempotent)
- `execute_plan()` now uses registry dispatch — **zero if/elif tool branches**
- `dispatch_tool_via_registry()` convenience wrapper for ad-hoc calls

### Registered tools (11)
| Tool | Handler |
|------|---------|
| `time.now` | `_handler_time_now` |
| `time.date_math` | `_handler_time_date_math` |
| `weather.query` | `_handler_weather_query` |
| `web.search` | `_handler_web_search` |
| `capability.match` | `_handler_capability_match` |
| `repo_memory.search` | `_handler_repo_memory_search` |
| `catalog.search` | `_handler_catalog_search` |
| `skill_store.list` | `_handler_skill_store_list` |
| `workflow_store.list` | `_handler_workflow_store_list` |
| `capability.status` | `_handler_capability_status` |
| `model.generate` | `_handler_model_generate` |

## Validation
- ✅ `py_compile` both files PASS
- ✅ `list_registered_tools()` returns all 11 tools
- ✅ `capability.status` returns `source=external_config` through registry
- ✅ Unknown tool returns `tool_not_registered`
- ✅ `grep -c 'tool ==' executor.py` → **0** (no if/elif branches)
- ✅ Hardcode guard PASS

## Hardcode Guard
- `tool_dispatch_registry.py` added to `allowed_files` in `hardcode_guard.json`
- No `tool ==` or `elif tool` patterns remain in executor.py

## Migration Notes
- Adding a new tool: define a handler function, call `register_tool("name", handler)` in `register_default_executor_tools()`
- No need to edit `execute_plan()` anymore
- Handlers receive a flat `args` dict with all plan/request context merged
