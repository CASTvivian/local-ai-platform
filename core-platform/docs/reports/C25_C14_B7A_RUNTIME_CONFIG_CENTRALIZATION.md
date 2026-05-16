# C25-C14-B7-A Runtime Config Centralization Foundation

## Goal

Centralize fixed runtime configuration such as ports, service URLs, model profiles, and packaging script paths.

## Implemented

Added:

```text
data/runtime_config/runtime_config.json
```

Added loader:

```text
services/agent_runtime_service/app/config/__init__.py
services/agent_runtime_service/app/config/runtime_config.py
```

Config includes:

- **7 services**: ollama (11434), model_gateway (18080), model_bootstrap_service (18100), skill_store_service (18121), repo_memory_service (18125), workflow_store_service (18126), agent_runtime_service (18131)
- **3 model profiles**: light (qwen2.5:1.5b), balanced (qwen2.5:7b), coder (qwen2.5-coder:7b)
- **defaults**: profile=light, planner_model_mode=auto, agent_runtime_required=true, dry_run_enabled=false
- **packaging**: single_source=true, mac/windows start script paths

Loader API:

- `find_core_platform_dir()` — walk-up path resolution with MAOMIAI_CORE_PLATFORM_DIR env override
- `load_runtime_config()` — load and return full config dict
- `get_service_config(name)` — get service config by name
- `get_service_base_url(name)` — get service base URL
- `get_service_health_url(name)` — get service health check URL
- `get_model_profile(profile)` — get model profile (defaults to config default)
- `list_model_profiles()` — list all model profiles
- `runtime_defaults()` — get runtime defaults

## Validation

- py_compile PASS
- runtime config loads OK
- `get_service_health_url("agent_runtime_service")` == `http://127.0.0.1:18131/health`
- `get_model_profile("light")["model"]` == `qwen2.5:1.5b`
- hardcode guard PASS
- audit JSON generated

## Remaining

This is B7-A foundation only.

- **B7-B**: Migrate Python service clients to use this loader (model_gateway, executor, planner, etc.)
- **B7-C**: Align Desktop JS and platform scripts with this config or generate constants from it
