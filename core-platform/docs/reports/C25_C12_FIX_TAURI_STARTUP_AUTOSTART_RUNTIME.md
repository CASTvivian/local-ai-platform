# C25-C12-FIX Tauri Startup Auto Start Runtime

## Problem

Windows Desktop chat failed with:

```text
tauri_invoke_unavailable
```

This means frontend JavaScript could not access Tauri invoke, so it could not call `start_local_ai_runtime`.

## Fix

- Enabled `app.withGlobalTauri = true` in `tauri.conf.json`.
- Added a Rust startup hook that runs `start_all.ps1` in the background when the Tauri app starts.
- Kept `start_local_ai_runtime` as a manual retry command.
- Updated frontend error reporting to distinguish invoke unavailability/global Tauri bridge issues.

## Expected

After launching the Windows desktop app:

- `start_all.ps1` runs automatically.
- `18131 agent_runtime_service` should become healthy.
- Chat `/agent/run` should work even if frontend invoke is unavailable.
