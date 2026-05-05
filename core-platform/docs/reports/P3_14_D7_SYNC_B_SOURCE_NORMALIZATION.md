# P3.14-D7-SYNC-B Source Normalization

## Status
Implemented ✅

## Canonical Source

The project now treats the following paths as the only active source:

```text
apps/desktop/
scripts/
services/
manifests/
docs/
.github/workflows/
```

## Removed / Deprecated

The following duplicate or stale paths were removed:

- `core-platform/apps/`
- `core-platform/scripts/`
- `core-platform/services/`
- `apps/desktop/bundle/backend/`

## Windows Build

GitHub Actions now builds only from:

- `apps/desktop`

and verifies runtime files from:

- `scripts/windows`
- `services/model_bootstrap_service`
- `services/model_gateway`

## Purpose

Avoid Mac / Windows divergence and prevent stale Windows test UI from being packaged again.

## Verification

All canonical paths verified:
- ✅ `apps/desktop/src/index.html` - Contains MAOMIAI markers
- ✅ `scripts/windows/*` - Complete Windows runtime scripts
- ✅ `services/model_bootstrap_service/main.py` - Python syntax OK
- ✅ `services/model_gateway/main.py` - Python syntax OK
- ✅ `apps/desktop/src-tauri/tauri.conf.json` - Resource paths normalized
- ✅ Tauri resources point to `../../../scripts/windows/` and `../../../services/`

## Next Steps

1. Push changes to origin
2. Trigger Windows build to verify
3. Confirm no stale UI markers in remote canonical source

## Commit

`chore: normalize Mac and Windows desktop source paths`
