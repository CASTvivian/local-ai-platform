# C25-C12-FIX Tauri Startup Auto Start Runtime

## Problem
Windows Desktop chat failed with:
```
tauri_invoke_unavailable
```

Frontend JS could not access `window.__TAURI__.core.invoke`, so it could not call
`start_local_ai_runtime`. The only way to start 18131 agent_runtime_service was
through a JS → Tauri invoke → Rust chain that was broken.

## Root Cause
The startup chain was:
```
JS click → window.__TAURI__.core.invoke("start_local_ai_runtime") → Rust → powershell start_all.ps1
```
If `window.__TAURI__` is undefined (timing, config, or packaging issue), the entire
chain breaks and no services start.

## Fix

### 1. Rust: Auto-start on app launch (enhanced)
- `run_windows_start_all_background()` runs in `.setup()` hook when Tauri app starts
- **Enhanced**: Added 2-second initial delay so Tauri window loads first
- **Enhanced**: Added error logging and result logging for diagnostics
- **New**: Added macOS auto-start support for dev/debug
- `start_local_ai_runtime` command retained as manual retry path

### 2. tauri.conf.json: `withGlobalTauri: true`
- Enables `window.__TAURI__` global injection for all webviews

### 3. Frontend: Graceful degradation when invoke unavailable
- `auto-start-services.js`: Falls back to HTTP health checks if Tauri invoke is unavailable
- `windows-demo-stable-router.js`:
  - `maomiaiTryStartWindowsRuntime()`: Returns `ok: true` with `source: "rust_autostart"` when invoke is unavailable
  - `maomiaiEnsureAgentRuntimeBeforeSend()`: Polls health endpoint up to 6 times (12s total) to wait for Rust autostart

### Startup flow after fix:
```
Tauri App Launch
  → Rust .setup() → run_windows_start_all_background()
    → thread::sleep(2s) → powershell start_all.ps1
  → JS DOMContentLoaded → autoStartServices()
    → Try Tauri invoke (if available)
    → Fallback: Wait 5s → HTTP health checks on all ports
  → User sends chat message
    → maomiaiEnsureAgentRuntimeBeforeSend()
      → If 18131 healthy: proceed immediately
      → If not: poll up to 12s waiting for Rust autostart
```

## Files Changed
1. `core-platform/apps/desktop/src-tauri/src/lib.rs` - Enhanced autostart with logging + macOS support
2. `core-platform/apps/desktop/src-tauri/tauri.conf.json` - withGlobalTauri: true
3. `core-platform/apps/desktop/src/js/auto-start-services.js` - Health-check fallback
4. `core-platform/apps/desktop/src/js/windows-demo-stable-router.js` - Graceful invoke degradation
5. `core-platform/docs/reports/C25_C12_FIX_TAURI_STARTUP_AUTOSTART_RUNTIME.md` - This report

## Expected After Fix
1. Desktop app launches → Rust automatically starts `start_all.ps1` in background
2. 18131 agent_runtime_service becomes healthy within ~5 seconds
3. Chat `/agent/run` works even if JS invoke is unavailable
4. Frontend gracefully waits for services to come up instead of failing immediately
