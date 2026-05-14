# C25-C11-FIX8 ASCII-only PowerShell Download Classifier

## Problem

FIX7 inserted Chinese user-facing strings into `bootstrap_runtime.ps1`.
Windows PowerShell 5.1 can parse scripts with a non-UTF8 codepage, which can break the entire runtime before model download starts.

## Fix

- PowerShell runtime is ASCII-only again.
- Download classifier returns ASCII codes only:
  - `network_timeout`
  - `network_connect_failed`
  - `model_not_found`
  - `permission_denied`
  - `download_failed`
  - `unknown`
- Frontend JS maps those codes to Chinese user-facing text.
- Validation includes a non-ASCII byte check for `bootstrap_runtime.ps1`.

## Rule

PowerShell runtime must not contain Chinese user-facing strings.
Chinese belongs in frontend JS, docs, or UTF-8-safe JSON resources.
