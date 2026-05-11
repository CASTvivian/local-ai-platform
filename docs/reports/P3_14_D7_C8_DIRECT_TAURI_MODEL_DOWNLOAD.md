# P3.14-D7-C8 Direct Tauri Model Download Runtime
## Status
Implemented.
## Problem
Model download depended on 18100. If 18100 was down, frontend showed `Failed to fetch`.
## Fix
The frontend now calls Tauri directly:
- `local_ai_status_direct`
- `install_local_inference_backend`
- `download_local_model_capability`

Rust invokes the bundled PowerShell runtime script directly.
This means model install/download no longer depends on 18100 being available first.
## UX Goal
Customers click a model capability and the app installs, downloads, verifies, and connects automatically.
