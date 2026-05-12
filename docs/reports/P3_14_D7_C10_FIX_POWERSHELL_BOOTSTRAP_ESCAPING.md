# P3.14-D7-C10 Fix PowerShell Bootstrap Escaping

## Status

Implemented.

## Problem

The embedded `bootstrap_runtime.ps1` was released correctly, but PowerShell failed to parse it.

The reported failing pattern was:

```text
\"runtime\\downloads\"
```

That escape style is valid for JSON or JavaScript strings, but not for native PowerShell source.

## Fix

Rewrote `core-platform/scripts/windows/bootstrap_runtime.ps1` with valid PowerShell quoting only, for example:

```powershell
Join-Path $Root 'runtime\downloads'
```

The rewritten script also uses ASCII-only status messages to avoid Windows PowerShell encoding noise.

## Result

The embedded runtime script should now parse and execute correctly after being released from the Rust binary.
