# C25-C11-FIX6 PowerShell Path Quoting

## Problem

Windows failed before the model download started:

```text
处理 -File “C:\Users\Administrator\AppData\Local\Local” 失败
```

The runtime path contains a space:

```text
C:\Users\Administrator\AppData\Local\Local AI Platform\...
```

`Start-Process powershell -ArgumentList @("-File", $WorkerScript)` was split incorrectly by Windows PowerShell 5.1, so the worker script path was truncated.

## Fix

Use `-EncodedCommand` instead of `-File` for launching the worker:

```powershell
& 'C:\full path with spaces\model-download-light-stable.ps1'
```

The command is encoded as UTF-16LE Base64, which avoids path splitting.

## Expected

- `bootstrap_version: c25-c11-fix6-powershell-path-quoting`
- `provider: ollama_cli_pull_stable`
- no more `C:\Users\Administrator\AppData\Local\Local` truncation
- worker reaches the stable `ollama pull <model>` path
