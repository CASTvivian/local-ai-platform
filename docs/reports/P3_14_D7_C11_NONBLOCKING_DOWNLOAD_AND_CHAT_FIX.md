# P3.14-D7-C11 Non-blocking Download and Chat Fix

## Status

Implemented.

## Fixes

1. Model download no longer blocks the desktop UI thread.
2. Background model download job starts immediately and reports status separately.
3. The local model page polls job status and refreshes installed state.
4. Model status is cached in `window.__MAOMIAI_MODEL_STATUS__`.
5. Entering the local model page triggers a fresh status check.
6. Clicking `新对话` now routes back through the original chat/session path.
7. Clicking `发送` now has a direct gateway fallback to `18080 /generate`.

## Expected Windows behavior

- Download should no longer freeze the app window.
- Returning to the local model page should refresh installed state automatically.
- Clicking `新对话` should enter a usable chat session.
- Clicking `发送` should produce either a model response or a clear error message.
