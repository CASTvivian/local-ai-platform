# C25-C12 Windows Build Agent Runtime Autostart

## Status

Windows artifact rebuilt after Agent Runtime autostart fix.

## Run

- Run ID: `25895794570`
- Conclusion: `success`
- Head SHA: `6f1c51a3b185bdd2b69dd51798d880f9cee1977e`

## Artifact

`core-platform/releases/windows-c25-c12-agent-autostart`

## Files

- `desktop_lib.exe`: `8.4M`
- `Local AI Platform_0.1.0_x64-setup.exe`: `1.9M`
- `Local AI Platform_0.1.0_x64_en-US.msi`: `2.9M`
- `BUILD_INFO.json`: `133B`

## BUILD_INFO

```json
{
  "commit": "6f1c51a",
  "label": "",
  "workflow": "build-win-release",
  "built_at": "2026-05-15T01:48:06.4243298+00:00"
}
```

## Windows Validation Focus

Install this package and test chat send.

Expected:

- `qwen2.5:1.5b` remains installed.
- Desktop checks `18131` before sending.
- If `18131` is down, app runs `start_all.ps1` through Tauri.
- `http://127.0.0.1:18131/health` becomes reachable.
- `/agent/run` returns an answer.

If it still fails, collect:

- `start_all.ps1` output
- `logs/windows/agent_runtime_service.err.log`
- `logs/windows/model_gateway.err.log`
