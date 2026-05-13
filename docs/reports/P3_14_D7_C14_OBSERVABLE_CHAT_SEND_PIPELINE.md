# P3.14-D7-C14 Observable Chat Send Pipeline

## Status

Implemented.

## Purpose

The Windows chat send path now has visible diagnostics.

## Changes

- Added visible debug box on the chat page.
- Added direct "test local inference" button.
- Send handler now always displays the captured stage, current model, raw Tauri result, parsed result, or errors.
- Direct local inference is attempted first.
- `18080` gateway remains fallback.

## Expected Use

If normal send has no response, click "测试本地推理".
The debug box will show whether Tauri invoke is available and what the local inference command returned.
