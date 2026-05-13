# P3.14-D7-C18 Fix Chinese Prompt Input Encoding

## Status

Implemented.

## Problem

Local inference worked, but Chinese input was misunderstood by the model. The model responded as if it received corrupted or unreadable characters.

## Root Cause

The Windows runtime path still passed Chinese prompt text through Windows PowerShell / JSON / HTTP body boundaries, where encoding could be corrupted.

## Fix

1. Rust encodes prompt as UTF-8 Base64.
2. PowerShell receives ASCII-only `MAOMIAI_PROMPT_B64`.
3. PowerShell decodes Base64 back to UTF-8 string.
4. PowerShell sends Ollama request body as UTF-8 bytes with `charset=utf-8`.

## Expected Result

Chinese prompt should reach Ollama correctly and receive Chinese response.
