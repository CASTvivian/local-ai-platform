# C26-P0-B Workspace Diff/Patch Engine

## Goal

Add Claude/Claw-style workspace file read, diff planning, and safe patch apply foundation.

## Implemented

New module:

```text
services/agent_runtime_service/app/workspace/patch_engine.py
```

Capabilities:

* `read_workspace_file` — read file with truncation guard
* `plan_replace_file` — preview unified diff before applying
* `unified_diff` — standard difflib unified diff generator
* `apply_replace_file` — full file replace with backup
* `apply_text_replacement` — exact string replacement (1st match)
* `_resolve_workspace_path` — workspace boundary enforcement
* `_write_patch_audit` — per-patch JSON audit trail
* `_audit_dir` — auto-created `data/workspace_patches/`

Safety:

* Workspace boundary check prevents path traversal outside root
* Backups created with UTC timestamp before every mutation
* Every successful patch writes an audit JSON to `data/workspace_patches/`
* `MAOMIAI_WORKSPACE_ROOT` env var override supported
* `MAOMIAI_CORE_PLATFORM_DIR` env var for platform dir override

## Validation

* py_compile: PASS
* read / plan diff / text replacement / file replace tests: PASS
* hardcode guard: PASS

## Next

C26-P0-C: Build/Test/Repair loop — use patch engine output as repair action.
