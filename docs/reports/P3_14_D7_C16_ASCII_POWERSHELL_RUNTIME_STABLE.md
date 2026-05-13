# P3.14-D7-C16 ASCII PowerShell Runtime Stable Fix

## Status

Implemented.

## Problem

Windows PowerShell failed to parse `bootstrap_runtime.ps1` after Chinese strings were added.
PowerShell 5.1 can misread UTF-8 without BOM, causing `ParserError` around hashtable entries.

## Fix

Rewrote `bootstrap_runtime.ps1` as ASCII-only.

- No Chinese strings in PowerShell.
- No bad escaped quotes.
- Hashtable entries use semicolons.
- `/api/chat` is retained.
- System prompt is ASCII: `Always answer in Simplified Chinese.`

## Expected Result

The released runtime script should parse correctly in Windows PowerShell 5.1.
