# P3.14-D7-C4 Windows Runtime Bootstrap

## Status
Implemented initial bootstrap.

## Added
- `core-platform/services/model_bootstrap_service/main.py`
- `core-platform/scripts/windows/start_all.ps1`
- `core-platform/scripts/windows/status_all.ps1`
- `core-platform/scripts/windows/stop_all.ps1`

## Purpose
Enable Windows package to check and prepare local AI capability through:
- `GET /bootstrap/status`
- `POST /bootstrap/start`

## Notes
This enables real model preparation only if the local inference backend is installed and available on Windows.
If the backend is missing, the UI will display Chinese guidance instead of appearing unresponsive.
