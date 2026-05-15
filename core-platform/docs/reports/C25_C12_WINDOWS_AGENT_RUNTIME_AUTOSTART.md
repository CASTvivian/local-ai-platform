# C25-C12 Windows Agent Runtime Auto Start

## Problem

Windows model install can succeed while Desktop chat still fails because `agent_runtime_service` on port `18131` is not running.

## Fix

- `start_all.ps1` now starts required local services and validates health.
- `status_all.ps1` now includes `agent_runtime_service` on `18131`.
- Added Tauri command `start_local_ai_runtime`.
- Desktop checks `http://127.0.0.1:18131/health` before sending to `/agent/run`.
- If `18131` is down, Desktop invokes `start_local_ai_runtime`, waits, then checks health again.

## Services

- `18100` model_bootstrap_service
- `18080` model_gateway
- `18125` repo_memory_service
- `18121` skill_store_service
- `18126` workflow_store_service
- `18131` agent_runtime_service

## Notes

The PowerShell startup path uses encoded command execution from Tauri to avoid Windows path splitting when the install path contains spaces.
