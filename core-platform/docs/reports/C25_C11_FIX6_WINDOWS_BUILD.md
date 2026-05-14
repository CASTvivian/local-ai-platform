# C25-C11-FIX6 Windows Build

## Status

Windows artifact rebuilt after PowerShell path quoting fix.

## Run

- Run ID: `25890318852`
- Conclusion: `success`
- Head SHA: `fa3bf38dda51914ca577da8198d7d5e1abc60042`
- Workflow: `build-win-release.yml`

## Artifact

`core-platform/releases/windows-c25-c11-fix6`

## Files

- `desktop_lib.exe` - 8.4M
- `Local AI Platform_0.1.0_x64-setup.exe` - 1.9M
- `Local AI Platform_0.1.0_x64_en-US.msi` - 2.9M
- `BUILD_INFO.json` - 150B

## BUILD_INFO

```json
{
  "commit": "fa3bf38",
  "label": "win-artifact-only",
  "workflow": "build-win-release",
  "built_at": "2026-05-14T22:55:07.9463880+00:00"
}
```

## Windows Validation Focus

Install this package and test model download.

Expected job JSON:

- `bootstrap_version: c25-c11-fix6-powershell-path-quoting`
- `provider: ollama_cli_pull_stable`
- no path truncation to `C:\Users\Administrator\AppData\Local\Local`
- worker reaches real `ollama pull qwen2.5:1.5b`
