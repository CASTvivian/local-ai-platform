# C25-C14-B7-C Desktop JS Runtime Config

## Goal
Move Desktop JS away from scattered hardcoded local service URLs to a centralized `runtime-config.js`.

## Implemented

### New File
```
apps/desktop/src/js/config/runtime-config.js
```

Exposes:
- `window.MAOMIAI_RUNTIME_CONFIG` — full config object
- `window.maomiaiRuntimeService(name)` — get service config
- `window.maomiaiRuntimeBaseUrl(name)` — get base URL
- `window.maomiaiRuntimeHealthUrl(name)` — get health check URL
- `window.maomiaiRuntimeApiUrl(name, path)` — build API URL
- `window.maomiaiRuntimeServiceNames()` — list all service keys
- `window.maomiaiRuntimeAllPorts()` — list all ports
- `window.maomiaiRuntimeServiceByPort(port)` — lookup by port

Contains 19 service definitions (ollama, modelGateway, autoRouter, modelBootstrap, referenceSkill, capabilityLearning, runtimeExecution, policyEngine, traceObservability, evalGateway, documentIngestion, skillStore, jobOrchestrator, artifactRegistry, codeReviewGate, repoMemory, workflowStore, designSystem, agentRuntime).

### Modified Files
| File | Changes |
|------|---------|
| `api.js` | 12 hardcoded URLs → `window.maomiaiRuntimeBaseUrl()` with fallback |
| `services.js` | `CORE_SERVICES` port list built from `MAOMIAI_RUNTIME_CONFIG.services` with fallback |
| `auto-start-services.js` | `C25_BACKEND_PORTS` from `maomiaiRuntimeAllPorts()` with fallback, host from config |
| `windows-demo-stable-router.js` | 5 `fetch()` calls → `maomiaiRuntimeHealthUrl/ApiUrl/BaseUrl` with fallback |
| `windows-click-model-setup.js` | `API.bootstrap/gateway` → `maomiaiRuntimeBaseUrl` with fallback |
| `index.html` | `<script src="./js/config/runtime-config.js">` added before `api.js` |

### Load Order
```
runtime-config.js → api.js → utils.js → ... → auto-start-services.js → windows-click-model-setup.js → windows-demo-stable-router.js
```

## Validation
- JS syntax: 6/6 files pass
- Hardcode guard: PASS
- After scan: 19 remaining URL literals, all are fallback defaults in ternary expressions (`: "http://..."`)
- `runtime-config.js` itself: 19 URL literals (single source of truth)

## Remaining (B7-D)
- Remove fallback literals in production builds
- Generate `runtime-config.js` from `data/runtime_config/runtime_config.json` at build time
- CORS origins migration
