# P3.14-D7-C4 Step 4A Fix Missing Windows Runtime Files

## Status
Implemented.

## Problem
Windows package resources pointed to missing runtime files:
- `scripts/windows/start_all.ps1`
- `services/model_bootstrap_service/main.py`
- `services/model_gateway/main.py`

## Fix
Added runtime files to the actual Windows build path under `core-platform/`.

## Added
- `core-platform/scripts/windows/start_all.ps1` - PowerShell startup script for services
- `core-platform/scripts/windows/stop_all.ps1` - PowerShell stop script for all services
- `core-platform/scripts/windows/status_all.ps1` - PowerShell status check script
- `core-platform/services/model_bootstrap_service/main.py` - Model bootstrap service (port 18100)
- `core-platform/services/model_gateway/main.py` - Model gateway service (port 18080)

## Next
Rebuild Windows package and test whether App can start 18100 and 18080.
