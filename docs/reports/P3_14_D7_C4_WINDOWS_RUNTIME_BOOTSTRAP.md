# P3.14-D7-C4 Windows Runtime Bootstrap

## Status
Implemented initial bootstrap.

## Added
- `core-platform/services/model_bootstrap_service/main.py` (18100 service)
- `core-platform/scripts/windows/start_all.ps1`
- `core-platform/scripts/windows/status_all.ps1`
- `core-platform/scripts/windows/stop_all.ps1`

## Purpose
Enable Windows package to check and prepare local AI capability through:
- `GET /bootstrap/status`
- `POST /bootstrap/start`

## Notes
This enables real model preparation only if local inference backend is installed and available on Windows.
If backend is missing, UI will display Chinese guidance instead of appearing unresponsive.

## Capabilities
- Detect Ollama installation on Windows
- Check local model status via `ollama list`
- Download models via `ollama pull`
- Map abstract UI profiles (standard-chat, code-capability) to actual model names
- Cross-platform support (Windows, macOS, Linux)
