# C25-C11-FIX3 Ollama HTTP Pull Progress

## Problem

Windows installs the Ollama client, but the previous background `ollama pull` process could exit without logs. The UI then showed `unknown`, the model list stayed empty, and there was no reliable progress signal.

## Fix

Model downloads now use the local Ollama HTTP API instead of shelling out to `ollama pull`:

- Verify/start Ollama service.
- POST `http://127.0.0.1:11434/api/pull`.
- Read streaming JSON lines.
- Persist `progress`, `completed`, `total`, status, and logs into the model job file.
- Verify completion through `/api/tags`.
- Render real progress and downloaded bytes in the Windows model setup UI.

## Expected Result

- Progress moves when Ollama reports `completed` / `total`.
- Last log shows Ollama pull streaming events.
- Completion requires `/api/tags` verification.
- The UI no longer depends on a silent black-box `ollama pull` process.
