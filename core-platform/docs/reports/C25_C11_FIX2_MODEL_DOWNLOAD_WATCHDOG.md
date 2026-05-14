# C25-C11-FIX2 Model Download Watchdog + Diagnostics

Implemented:
- PID tracking for background model download jobs
- `process_alive` detection in `job_status`
- `elapsed_seconds` update on every status check
- `exit_code` persistence when pull exits
- stdout `last_log` and stderr `error_log` diagnostics
- installed verification during status checks
- `unknown` state when process is dead and model is not installed
- UI diagnostics for PID, alive state, elapsed time, exit code, logs, and error logs

Purpose:
Fix the issue where model download UI stayed at `running` with no useful diagnostics.

Expected behavior:
- Running downloads show PID, process alive state, elapsed time, and latest logs.
- Completed installs auto-mark `completed` when the model appears in `ollama list`.
- Dead process without installed model becomes `unknown`, not endless `running`.
- `unknown` and `failed` stop the polling loop and show retry diagnostics.
