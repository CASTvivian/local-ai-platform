# C25-C13 Windows Build Runtime Resources

## Status
Windows MSI rebuilt after runtime resource packaging fix.

## Run
- Run ID: `25946620575`
- Conclusion: `success`
- Head SHA: `4eb9866781b223486eeea77f2c26bff672827ddf`

## Artifact
`core-platform/releases/windows-c25-c13-runtime-resources/`

## BUILD_INFO
```json
{
  "commit": "4eb9866",
  "built_at": "2026-05-15T23:41:26.7361726+00:00",
  "workflow": "build-win-release",
  "label": "win-artifact-only"
}
```

## Artifact Files
| File | Size |
|------|------|
| `Local AI Platform_0.1.0_x64_en-US.msi` | 4.9 MB |
| `desktop_lib.exe` | 8.4 MB |
| `BUILD_INFO.json` | 150 B |

## Windows validation focus
Install the MSI and check:
1. Runtime resources exist:
   - scripts/windows/start_all.ps1
   - scripts/windows/status_all.ps1
   - services/agent_runtime_service/main.py
   - services/model_gateway/main.py
   - data/brain_assets
   - data/github_stars
2. Run:
   ```powershell
   powershell -ExecutionPolicy Bypass -File "$env:LOCALAPPDATA\Local AI Platform\maomiai-runtime\scripts\windows\bootstrap_runtime.ps1" -Action runtime_resources
   ```
3. Launch app and verify:
   - http://127.0.0.1:18131/health
   - chat /agent/run
