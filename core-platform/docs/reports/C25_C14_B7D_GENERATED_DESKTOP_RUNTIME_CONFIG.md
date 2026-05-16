# C25-C14-B7-D: Generate Desktop Runtime Config from JSON

## Goal

Make Desktop JS `runtime-config.js` auto-generated from the single JSON source, eliminating manual JS editing.

```text
data/runtime_config/runtime_config.json  →  generate  →  apps/desktop/src/js/config/runtime-config.js
```

## Changes

### 1. Expanded `runtime_config.json` (7 → 19 services)

Added 12 missing services to match the existing hand-written JS config:
- auto_router (18093)
- reference_skill (18101)
- capability_learning (18102)
- runtime_execution (18104)
- policy_engine (18110)
- trace_observability (18111)
- eval_gateway (18112)
- document_ingestion (18120)
- job_orchestrator (18122)
- artifact_registry (18123)
- code_review_gate (18124)
- design_system (18127)

Added `js_key` override field for 5 services to maintain backward compatibility with existing JS consumers:
- `model_bootstrap_service` → `modelBootstrap` (not `modelBootstrapService`)
- `skill_store_service` → `skillStore` (not `skillStoreService`)
- `repo_memory_service` → `repoMemory` (not `repoMemoryService`)
- `workflow_store_service` → `workflowStore` (not `workflowStoreService`)
- `agent_runtime_service` → `agentRuntime` (not `agentRuntimeService`)

Version bumped: `c25-c14-b7a` → `c25-c14-b7d`

### 2. New Generator: `scripts/build/generate_desktop_runtime_config.py`

- Reads `data/runtime_config/runtime_config.json`
- Converts snake_case service names to camelCase (respects `js_key` override)
- Sorts services by port for consistent output
- Generates IIFE with AUTO-GENERATED marker
- Preserves all helper functions from hand-written version
- Adds `modelProfile()` helper (new)
- Output: `apps/desktop/src/js/config/runtime-config.js`

### 3. Generated JS Exposes

- `window.MAOMIAI_RUNTIME_CONFIG` — full config object
- `window.maomiaiRuntimeService(name)` — get service config
- `window.maomiaiRuntimeBaseUrl(name)` — get base URL
- `window.maomiaiRuntimeHealthUrl(name)` — get health URL
- `window.maomiaiRuntimeApiUrl(name, path)` — build API URL
- `window.maomiaiRuntimeServiceNames()` — all service keys
- `window.maomiaiRuntimeAllPorts()` — all ports array
- `window.maomiaiRuntimeServiceByPort(port)` — lookup by port
- `window.maomiaiRuntimeModelProfile(name)` — get model profile

### 4. Updated `hardcode_guard.json`

Added `generate_desktop_runtime_config.py` to allowed_files.

## Validation Results

| Check | Result |
|-------|--------|
| Generator runs | ✅ |
| JS syntax | ✅ |
| AUTO-GENERATED marker | ✅ |
| Service count | 19 |
| Profile count | 3 |
| Output URL count | 19 |
| Backward-compatible keys | ✅ (modelBootstrap, skillStore, repoMemory, workflowStore, agentRuntime) |
| Helper functions | ✅ (service, baseUrl, healthUrl, apiUrl, serviceNames, allPorts, serviceByPort, modelProfile) |
| Hardcode guard | ✅ PASS |

## Audit JSON

`data/agent_core_audit/c25/schema_planner/c25_c14_b7d_generated_desktop_runtime_config.json`

## Next Step

B7-E: Wire generator into build scripts (npm scripts / Tauri build hooks) so JS config is always regenerated before packaging.
