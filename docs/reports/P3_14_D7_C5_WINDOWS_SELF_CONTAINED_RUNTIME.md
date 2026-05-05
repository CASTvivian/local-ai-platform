# P3.14-D7-C5 Windows Self-contained Runtime

## Status
Implemented initial runtime manager.

## Purpose
Avoid relying on user-installed Python for Windows backend services.

## Added
- `scripts/windows/ensure_runtime.ps1`

## Behavior
On Windows startup:
1. Download Python embeddable package if missing.
2. Enable `import site`.
3. Install pip if missing.
4. Install FastAPI / Uvicorn / Pydantic.
5. Start local backend services with embedded Python.

## Notes
This requires network access on first run. Real validation must happen on Windows.
