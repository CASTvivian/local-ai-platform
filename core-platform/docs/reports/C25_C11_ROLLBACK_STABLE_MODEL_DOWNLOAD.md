# C25-C11-ROLLBACK Stable Model Download

## Problem

The original model download path could complete, but the HTTP pull progress refactor made the download path less stable on Windows.

## Decision

Rollback the actual download mechanism to the stable Ollama CLI path:

```text
ollama pull <model>
```

Keep only non-invasive observability around that command:

- job status
- stdout/stderr logs
- elapsed seconds
- PID/process status
- installed verification
- frontend polling and auto refresh

## Runtime Markers

- `bootstrap_version: c25-c11-rollback-stable-ollama-pull`
- `provider: ollama_cli_pull_stable`

## Expected

- The download behavior returns to the previously working `ollama pull` path.
- The UI still shows state, elapsed time, PID, logs, and installed verification.
- No HTTP pull worker is used for model download.
