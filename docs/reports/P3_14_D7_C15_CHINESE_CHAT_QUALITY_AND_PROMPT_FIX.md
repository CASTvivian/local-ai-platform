# P3.14-D7-C15 Chinese Chat Quality and Prompt Fix

## Status

Implemented.

## Problem

Local inference was technically successful, but the model responded as if no user prompt was provided and answered in English.

## Root Cause

The prompt was passed through an environment variable. On Windows this may cause encoding or quoting issues for Chinese text.
The runtime also used Ollama `/api/generate` without a system prompt.

## Fix

1. Rust writes prompt into a UTF-8 temp file.
2. PowerShell reads the prompt file using UTF-8.
3. PowerShell calls Ollama `/api/chat`.
4. A Chinese system prompt is added.
5. Debug output is collapsed by default.

## Expected Result

For Chinese input, local AI should respond in Chinese and should no longer say it did not receive a prompt.
