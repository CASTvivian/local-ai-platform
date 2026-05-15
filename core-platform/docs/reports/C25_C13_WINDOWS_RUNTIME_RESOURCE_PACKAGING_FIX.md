# C25-C13 Windows Runtime Resource Packaging Fix

## Problem

Windows Desktop could not auto-start Agent Runtime because installed runtime resources were incomplete:

```text
start_all.ps1 not found in runtime resources
```

Root cause: The Windows MSI bundle did not include all runtime folders needed under `%LOCALAPPDATA%\Local AI Platform\maomiai-runtime`.

## Fix

### 1. Added missing Tauri bundle resources (`tauri.conf.json`)

New resources added:
- `../../../data/brain_assets`
- `../../../data/github_stars`

Already present (confirmed):
- `../../../scripts/windows/ensure_runtime.ps1`
- `../../../scripts/windows/bootstrap_runtime.ps1`
- `../../../scripts/windows/start_all.ps1`
- `../../../scripts/windows/stop_all.ps1`
- `../../../scripts/windows/status_all.ps1`
- `../../../services/model_bootstrap_service`
- `../../../services/model_gateway`
- `../../../services/agent_runtime_service`
- `../../../services/repo_memory_service`
- `../../../services/skill_store_service`
- `../../../services/workflow_store_service`
- `../../../data/agent_policy`
- `../../../data/sandbox_policy`
- `../../../data/agent_team`

Total resources: 18

### 2. Added `runtime_resources` verification action (`bootstrap_runtime.ps1`)

New action: `-Action runtime_resources`

Checks all required runtime files/directories exist after installation:
- `scripts\windows\start_all.ps1`
- `scripts\windows\status_all.ps1`
- `scripts\windows\bootstrap_runtime.ps1`
- `services\agent_runtime_service\main.py`
- `services\model_gateway\main.py`
- `services\model_bootstrap_service\main.py`
- `services\repo_memory_service\main.py`
- `services\skill_store_service\main.py`
- `services\workflow_store_service\main.py`
- `data\agent_policy`
- `data\agent_team`
- `data\sandbox_policy`

Returns `{ ok, missing[], runtime_root, bootstrap_version }`.

### 3. Updated bootstrap version

`c25-c11-fix8-ascii-download-classifier` -> `c25-c13-runtime-resource-packaging`

## Validation Results

| Check | Result |
|-------|--------|
| resource_count | 18 |
| All resources exist in source tree | YES |
| tauri.conf.json valid JSON | YES |
| bootstrap_runtime.ps1 ASCII-only | YES (0 non-ASCII bytes) |
| Hardcode guard | PASS (pre-existing planner keywords unrelated) |

## Expected After Fix

After installing new Windows MSI:
1. `scripts/windows/start_all.ps1` exists in runtime directory
2. `scripts/windows/status_all.ps1` exists in runtime directory
3. All service `main.py` files present
4. All data directories present (agent_policy, agent_team, sandbox_policy, brain_assets, github_stars)
5. Agent Runtime 18131 can auto-start
6. Desktop chat `/agent/run` works
7. `bootstrap_runtime.ps1 -Action runtime_resources` reports `ok: true`
