# C25-C11-FIX4 Runtime Bootstrap Version + Stale Job Cleanup

## Problem

Windows still returned old download state such as `ollama-pull-light.out.log` and `download_process_not_alive`. That means the installed app/runtime was reading stale bootstrap/job data instead of the FIX3 Ollama HTTP pull path.

## Fix

- Added `MAOMIAI_BOOTSTRAP_RUNTIME_VERSION = c25-c11-fix4-http-pull`.
- Added `bootstrap_version` to JSON responses and model download job state.
- Added `provider = ollama_http_pull` to model download jobs and responses.
- Renamed HTTP pull logs to `ollama-http-pull-*`.
- Cleared old pre-FIX3 job/log/script files before starting a new download.
- Frontend detects stale old download jobs and stops treating them as current progress.

## Expected

New Windows download job JSON should contain:

- `bootstrap_version`
- `provider: ollama_http_pull`
- `progress`
- optional `completed` / `total`

It should not contain:

- `ollama-pull-light.out.log`
- `ollama-pull-light.err.log`
- `download_process_not_alive`
