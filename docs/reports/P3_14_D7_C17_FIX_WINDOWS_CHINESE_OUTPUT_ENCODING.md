# P3.14-D7-C17 Fix Windows Chinese Output Encoding

## Status

Implemented.

## Problem

Local inference worked, but Chinese model responses were mojibake in the Windows desktop UI.
Root cause: Windows PowerShell stdout encoding was not reliably UTF-8 when Rust captured stdout.

## Fix

PowerShell no longer writes raw Chinese JSON to stdout.
Instead, `Write-Json` now emits an ASCII-only envelope:

```json
{
  "ok": true,
  "maomiai_payload_encoding": "utf8-base64-json",
  "maomiai_payload_b64": "..."
}
```

The frontend decodes the payload using `TextDecoder("utf-8")`.

## Expected Result

Chinese model responses should display correctly in the UI.
