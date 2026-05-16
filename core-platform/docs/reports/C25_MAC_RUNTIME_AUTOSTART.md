# C25 Mac Runtime Autostart

## Problem

Mac .app opened successfully, but returned dry-run diagnostic instead of real Agent Runtime response:

```
"dry_run": true
"本地模型暂未接通或 model_gateway 不可用"
```

Root cause: Rust `run_windows_start_all_background()` macOS branch failed to locate and execute `start_all.sh` in the .app bundle, so backend services were never started.

## Fix

### 1. New `scripts/mac/start_all.sh`
- Starts 6 core services in dependency order:
  - 18125 repo_memory_service
  - 18121 skill_store_service
  - 18126 workflow_store_service
  - 18100 model_bootstrap_service
  - 18080 model_gateway
  - 18131 agent_runtime_service
- Accepts `MAOMIAI_RUNTIME_ROOT` env var for correct `services/` directory resolution
- Falls back to heuristic path resolution (SCRIPT_DIR, walk-up, dev-time path)
- Prioritizes venv python3, then system python3/python

### 2. New `scripts/mac/status_all.sh`
- Health check for ollama + 6 services

### 3. Tauri resources
- Added `../../../scripts/mac` to `tauri.conf.json` bundle resources
- Tauri maps this to `_up_/_up_/_up_/scripts/mac/` inside .app bundle

### 4. Rust `run_windows_start_all_background()` macOS branch
- Expanded search candidates to include `_up_/_up_/_up_/scripts/mac/start_all.sh`
- Passes `MAOMIAI_RUNTIME_ROOT` env var pointing to the directory containing `services/`
- Added debug logging for `resource_dir` and `RUNTIME_ROOT`
- Falls back to exe directory walk-up for dev mode

### 5. Frontend JS
- Added `maomiaiAgentRuntimeReadyForMac()` health check function

## Verification

| Item | Status |
|------|--------|
| `bash -n start_all.sh` | PASS |
| `bash -n status_all.sh` | PASS |
| JS syntax check | PASS |
| `scripts/mac` in tauri.conf.json resources | PASS |
| Tauri build | PASS (10 warnings, 0 errors) |
| .app contains `scripts/mac/start_all.sh` | PASS |
| .app contains 6 services | PASS |
| Git push | PASS (8603bfd) |

## Build Artifacts

- **App**: `core-platform/releases/macos-c25-runtime-autostart/macos/Local AI Platform.app`
- **DMG**: `core-platform/releases/macos-c25-runtime-autostart/dmg/Local AI Platform_0.1.0_aarch64.dmg`
- **Commit**: 8603bfd4a7d051a27d62059dd35796525784c4e0

## Test Plan

Open `Local AI Platform.app`, then test:
1. `你好，请用一句话介绍你自己` — should not return dry_run diagnostic
2. `今天是几月几号，现在几点` — should return real time
3. `我们现在有哪些 Agent 和 MCP 相关仓库资产` — should use Agent Runtime with repo_memory

Expected: no dry_run diagnostic; real Agent Runtime responses via 18131.
