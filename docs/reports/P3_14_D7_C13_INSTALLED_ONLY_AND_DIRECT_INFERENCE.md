# P3.14-D7-C13 Installed-only Model Use and Direct Inference

## Status

Implemented.

## Fixes

1. Only installed models can be set as current.
2. Chat model selector now prefers installed models only.
3. Chat inference now tries a direct Tauri command first.
4. Direct Tauri inference calls local Ollama `/api/generate`.
5. `18080` gateway is now a fallback, not the only inference path.
6. Background download startup now uses a quoted PowerShell command line instead of the fragile argument array.

## Expected Behavior

- Undownloaded models cannot be selected as current.
- Downloaded models can be selected and used immediately.
- Sending a message should trigger local inference directly through Ollama when available.
