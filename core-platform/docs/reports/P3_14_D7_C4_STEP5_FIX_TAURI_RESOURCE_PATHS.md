# P3.14-D7-C4 Step 5: Fix Tauri Resource Paths

## Status
✅ Fixed and verified

## Problem
Windows build failed because Tauri resource paths were incorrect.

### Root Cause
The `tauri.conf.json` file is located at:
```
core-platform/apps/desktop/src-tauri/tauri.conf.json
```

The resource paths were configured as:
```json
"../../scripts/windows/bootstrap_runtime.ps1"
```

This resolves to:
```
core-platform/apps/scripts/windows/...
```

But the actual files are at:
```
core-platform/scripts/windows/...
```

### Error Message
```
resource path `../../scripts/windows/bootstrap_runtime.ps1` doesn't exist
```

## Fix Applied

Changed all resource paths from `../../` to `../../../`:

```json
{
  "bundle": {
    "resources": [
      "resources/scripts/start_all.sh",
      "resources/scripts/stop_all.sh",
      "../../../scripts/windows/bootstrap_runtime.ps1",
      "../../../scripts/windows/start_all.ps1",
      "../../../scripts/windows/stop_all.ps1",
      "../../../scripts/windows/status_all.ps1",
      "../../../services/model_bootstrap_service",
      "../../../services/model_gateway"
    ]
  }
}
```

This now resolves correctly to:
- `core-platform/scripts/windows/*`
- `core-platform/services/*`

## Verification

### Path Validation
From `core-platform/apps/desktop/src-tauri/`:
```bash
../../../scripts/windows/bootstrap_runtime.ps1     ✅ OK
../../../scripts/windows/start_all.ps1             ✅ OK
../../../scripts/windows/stop_all.ps1             ✅ OK
../../../scripts/windows/status_all.ps1            ✅ OK
../../../services/model_bootstrap_service/main.py  ✅ OK
../../../services/model_gateway/main.py            ✅ OK
```

### Cargo Check
```bash
cd core-platform/apps/desktop/src-tauri
cargo check
```
Result: `Finished dev profile [unoptimized + debuginfo] target(s) in 1.90s`

## GitHub Workflow Update

Also updated `.github/workflows/build-win-release.yml` to use the correct paths in `Test-Path` checks:

```powershell
if (!(Test-Path "..\..\..\scripts\windows\start_all.ps1")) {
    throw "missing scripts/windows/start_all.ps1"
}
```

## Expected Result

Windows build should now succeed with all runtime files properly packaged.

## Files Modified
1. `core-platform/apps/desktop/src-tauri/tauri.conf.json`
2. `.github/workflows/build-win-release.yml`

## Next Steps

Trigger a new Windows build to verify the fix works.
