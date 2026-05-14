# C25-C11-FIX7 Model Download Retry + Offline Pack Hook

## Problem

The latest Windows failure reached the real stable download command:

```text
ollama pull qwen2.5:1.5b
```

The failure was a model source network timeout:

```text
max retries exceeded
dial tcp 172.64.66.2:443: i/o timeout
```

This is no longer a local launcher, path quoting, or Ollama installation problem.

## Fix

- Keep the stable `ollama pull` download path.
- Strip ANSI terminal sequences from Ollama logs.
- Classify common download failures:
  - `network_timeout`
  - `network_connect_failed`
  - `model_not_found`
  - `permission_denied`
  - `download_failed`
- Show a friendly user message for model source network timeouts.
- Add a visible retry button.
- Add an offline model pack entry point for demo/customer environments.

## Product Decision

For customer demos, do not depend only on live access to Ollama model sources. Use one of:

- retry when the network improves
- prepared offline model pack import
- pre-seeded Windows demo machine
- future company mirror/model gateway
