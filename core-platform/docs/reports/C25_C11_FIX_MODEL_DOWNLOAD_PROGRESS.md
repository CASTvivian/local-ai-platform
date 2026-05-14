# C25-C11-FIX Model Download Progress + Auto Refresh

Implemented:
- model download job state normalization
- background download completion/failure writes to job file
- `job_status` returns `running/completed/failed`, `last_log`, `elapsed_seconds`, and `installed`
- per-model-card progress UI
- frontend polling every 2 seconds
- download log display
- auto refresh after completion
- current model selection after completion
- completion custom event for future UI hooks

User experience:
- Click download.
- See progress state on the model card.
- See elapsed time and latest logs.
- Completion refreshes model state automatically.
- Installed model becomes current without manually clicking check.

Note:
Ollama pull percentage is not guaranteed in all environments, so this version uses observable job state plus logs. When provider output includes percentages, the existing parser still surfaces progress.
