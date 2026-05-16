# C25-C14-B12 Executor Capability Status Config

## Problem
Executor had hardcoded capability/status data in `execute_plan()` — a static list of `demo_kernel`, `enabled`, and `pending` entries inline in Python code.

## Fix
Moved capability status data to external config:
```
data/agent_policy/capability_status.json
```

Executor now loads external config via:
```python
load_capability_status_config()
```

### Changes

| File | Change |
|------|--------|
| `data/agent_policy/capability_status.json` | NEW — external capability status config (10 capabilities, version c25-c14-b12) |
| `services/agent_runtime_service/app/executor.py` | Replaced hardcoded `capability.status` branch with `load_capability_status_config()` call; added `_core_platform_dir_for_executor()` with walk-up path resolution |
| `data/agent_policy/hardcode_guard.json` | Added `capability_status.json` to allowed_files, `capability.status` to allowed_literal_exact |

### Path Resolution
Uses walk-up search from `__file__` looking for `data/agent_policy/` directory, with `parents[3]` fallback. This is robust regardless of PYTHONPATH.

### Capability Status Entries (10)
- agent_runtime (enabled)
- schema_planner (enabled)
- mcp_runtime (enabled)
- repo_memory (enabled)
- capability_registry (enabled)
- approval_sandbox (enabled)
- browser_web (enabled)
- team_runtime (partial)
- offline_model_pack (pending)
- desktop_production_cleanup (pending)

## Validation
- ✅ py_compile passed
- ✅ config loads (version c25-c14-b12, 10 status entries)
- ✅ executor uses external_config source
- ✅ hardcoded status markers removed (demo_kernel, desktop_app, etc.)
- ✅ hardcode guard passed

## Remaining
B9 should still registry-ize executor tool dispatch, because executor still uses explicit if/elif branches for tool execution.
