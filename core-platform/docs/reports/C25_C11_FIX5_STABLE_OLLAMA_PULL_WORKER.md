# C25-C11-FIX5 Stable Ollama Pull Worker

## Problem

FIX4 proved the new bootstrap script was installed, but the HTTP pull worker could still exit quickly without a useful error in the UI.

## Fix

- Replaced the background `pull_model` bootstrap reuse path with a standalone generated worker script.
- The worker contains only the Ollama HTTP pull logic it needs.
- The worker writes job state before and after each critical stage.
- Worker stdout/stderr are redirected to `ollama-http-worker-*` logs.
- Job status surfaces worker stdout/stderr when the process exits before installation.
- Bootstrap version is now `c25-c11-fix5-stable-http-worker`.

## Expected

If model download fails again, the UI should show a real cause:

- Ollama executable not found.
- Ollama API did not become ready on `127.0.0.1:11434`.
- `/api/pull` returned an HTTP error.
- A PowerShell exception with stderr/stdout tails.

The UI should no longer show an empty “process not alive” failure.
