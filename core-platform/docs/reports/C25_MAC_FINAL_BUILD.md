# C25 Mac Final Build

## Goal
Build final macOS package after C25-C14 structural rebuild.

## Git
- HEAD: `2eeebb1476696b085139baec4fef9622412fdcce`
- Branch: main

## Validation Pipeline
| Step | Result |
|------|--------|
| runtime-config regenerated | ✅ 19 services, AUTO-GENERATED |
| py_compile (7 files) | ✅ PASSED |
| JS syntax (3 files) | ✅ PASSED |
| hardcode guard | ✅ PASSED |
| npm install | ✅ 0 vulnerabilities |
| Tauri macOS build | ✅ SUCCESS (10 warnings, 0 errors) |

## Artifacts
| Artifact | Path | Size |
|----------|------|------|
| .app | `releases/macos-c25-final/app/Local AI Platform.app` | 50 MB |
| .dmg | `releases/macos-c25-final/dmg/Local AI Platform_0.1.0_aarch64.dmg` | 6.0 MB |

## App Resource Checks (11/11 PASS)
- ✅ `scripts/mac/start_all.sh`
- ✅ `services/agent_runtime_service`
- ✅ `data/runtime_config/runtime_config.json`
- ✅ `data/capability_registry/`
- ✅ `data/planner_runtime/`
- ✅ `services/artifact_registry_service`
- ✅ `services/code_review_gate_service`
- ✅ `services/design_system_service`
- ✅ `services/document_ingestion_service`
- ✅ `services/agent_orchestrator`
- ✅ `data/agent_policy/`

## tauri.conf.json Resources Added (C25-C14 delta)
1. `services/artifact_registry_service`
2. `services/code_review_gate_service`
3. `services/design_system_service`
4. `services/document_ingestion_service`
5. `services/agent_orchestrator`
6. `data/runtime_config`
7. `data/capability_registry`
8. `data/planner_runtime`

## C25-C14 Structural Features Included
- schema-driven planner
- structured planner model output
- schema capability registry
- executor registry dispatch (11 tools)
- data-driven renderer templates
- centralized runtime config
- generated desktop runtime-config.js
- mac runtime autostart resources
- 11 services bundled (6 core + 5 enterprise)

## Rust Warnings (non-blocking, 10 total)
- 2 unused imports (`std::process::Command`)
- 5 unused variables (Windows-only functions)
- 3 dead code (Windows-only bootstrap functions)

## Next
Run **C25-MAC-FINAL-SMOKE** against the built `.app`.
