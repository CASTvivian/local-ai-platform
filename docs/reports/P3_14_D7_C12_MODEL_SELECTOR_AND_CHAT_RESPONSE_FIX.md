# P3.14-D7-C12 Model Selector and Chat Response Fix

## Status

Implemented.

## Problems

1. After sending a message, no assistant reply was shown reliably.
2. After downloading multiple models, there was no explicit current model selection.

## Fixes

1. Added current model profile storage in `localStorage`.
2. Added `设为当前使用` action on local model cards.
3. Downloaded models are set as current automatically after success.
4. Chat page now shows a current model selector in the top bar.
5. Send fallback now includes current `profile` and `model` when calling the local gateway.
6. Response extraction supports `response`, `output`, `text`, `content`, `message`, and common OpenAI-style fields.
7. If the model-aware call path fails, the fallback retries a plain `prompt` request before surfacing an error.

## Expected Behavior

- User can choose which local capability to use.
- Chat uses the currently selected capability by default.
- Sending shows either a real assistant response or a clear gateway error.
