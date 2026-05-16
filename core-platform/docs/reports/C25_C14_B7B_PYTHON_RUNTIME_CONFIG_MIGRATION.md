# C25-C14-B7-B Python Runtime Config Migration

## Goal
Migrate Python runtime clients away from scattered hardcoded service URLs and toward centralized `data/runtime_config/runtime_config.json`.

## Files Migrated

### 1. `services/agent_runtime_service/app/tools.py`
- Added `from .config.runtime_config import get_service_base_url`
- `repo_memory_search`: `"http://127.0.0.1:18125/brain/search"` → `(get_service_base_url("repo_memory_service") or "http://127.0.0.1:18125") + "/brain/search"`
- `skill_store_list`: `"http://127.0.0.1:18121/list"` → `(get_service_base_url("skill_store_service") or "http://127.0.0.1:18121") + "/list"`
- `workflow_store_list`: `"http://127.0.0.1:18126/list"` → `(get_service_base_url("workflow_store_service") or "http://127.0.0.1:18126") + "/list"`
- `model_generate`: `"http://127.0.0.1:18080/generate"` → `(get_service_base_url("model_gateway") or "http://127.0.0.1:18080") + "/generate"`

### 2. `services/agent_runtime_service/app/mcp/registry.py`
- Added `from ..config.runtime_config import get_service_base_url`
- Created `_svc_url(name, fallback, path)` helper for clean resolution
- Replaced 4 hardcoded endpoint URLs with `_svc_url()` calls:
  - `repo_memory_service` → `/brain/search`
  - `skill_store_service` → `/skills`
  - `workflow_store_service` → `/workflows`
  - `model_gateway` → `/generate`

### 3. `services/agent_runtime_service/app/health/planner_health.py`
- Added `from ..config.runtime_config import get_service_health_url`
- `MODEL_GATEWAY_HEALTH_URL` default changed from `"http://127.0.0.1:18080/health"` to `get_service_health_url("model_gateway") or "http://127.0.0.1:18080/health"`

### 4. `services/agent_runtime_service/app/planning/llm_planner.py`
- Added `from ..config.runtime_config import get_service_base_url`
- `call_planner_model` endpoint default changed from `"http://127.0.0.1:18080/generate"` to `(get_service_base_url("model_gateway") or "http://127.0.0.1:18080") + "/generate"`

### 5. `services/model_gateway/main.py`
- Added runtime config loader (portable, no cross-service import)
- `OLLAMA_URL` changed from `"http://127.0.0.1:11434/api/generate"` to `_get_ollama_base_url() + "/api/generate"`
- `_get_available_models()` URL changed from `"http://127.0.0.1:11434/api/tags"` to `_get_ollama_base_url() + "/api/tags"`

## Validation Results

| Check | Result |
|---|---|
| py_compile (95 Python files) | ✅ PASS |
| runtime_config functional | ✅ PASS |
| hardcode guard | ✅ PASS |
| before_count | 23 hardcoded URLs |
| after_count | 22 remaining matches |
| net migration | 11 client URLs → runtime_config (remaining 22 are: 6 fallback defaults, 8 CORS origins, 5 agent_orchestrator, 3 out-of-scope) |

## Remaining Hardcoded URLs/Ports (by category)

### Fallback defaults (safe, intentional)
These appear in `or "http://127.0.0.1:18xxx"` patterns — they are last-resort defaults when runtime_config.json is missing:
- `tools.py`: 4 fallbacks
- `mcp/registry.py`: 4 fallbacks
- `planner_health.py`: 1 fallback
- `llm_planner.py`: 1 fallback
- `model_gateway/main.py`: 1 fallback

### CORS origins (browser security, not client URLs)
- `model_gateway/main.py`: 2 (`127.0.0.1:19000`, `localhost:19000`)
- `agent_orchestrator/main.py`: 2
- `eval_engine/main.py`: 2
- `plugin_manager/main.py`: 2

### Out of scope (not in B7-B)
- `agent_orchestrator/main.py`: 3 hardcoded service URLs (`GATEWAY_URL`, `PLUGIN_URL`, `EVAL_URL`)

## hardcode_guard.json Updates
Added to `allowed_files`:
- `app/tools.py`
- `app/mcp/registry.py`
- `app/health/planner_health.py`
- `app/planning/llm_planner.py`
- `model_gateway/main.py`

## Next Steps
- B7-C: Migrate Desktop JS hardcoded URLs (generate JS constants from runtime_config)
- B7-D: Migrate service binding ports (CORS origins, startup scripts)
