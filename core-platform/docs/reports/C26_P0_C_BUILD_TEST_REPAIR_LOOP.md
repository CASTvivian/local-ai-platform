# C26-P0-C Build/Test/Repair Loop

## Goal
Add foundation for Claude/Claw-style build/test/repair loop.

## Implemented

New module:
```text
services/agent_runtime_service/app/workspace/repair_loop.py
```

Capabilities:

- run command in workspace (with cwd boundary enforcement)
- capture stdout/stderr/exit_code
- create repair context (error summary + repair hints)
- optionally apply patch action (via patch_engine)
- re-run command after repair
- write repair loop audit JSON per loop run
- enforce workspace cwd boundary

### API

| Function | Purpose |
|---|---|
| `run_command(command, cwd, timeout, max_output)` | Run shell command, return `CommandResult` |
| `build_repair_context(result)` | Extract error info + hints from failed `CommandResult` |
| `run_build_test_repair_loop(command, cwd, repair_action, timeout)` | Full loop: run → fail? → repair → re-run |

### Repair Actions

- `text_replacement`: uses `patch_engine.apply_text_replacement`
- `replace_file`: uses `patch_engine.apply_replace_file`

## Validation

- py_compile ✅
- failing command detected ✅
- repair context generated ✅
- patch action applied ✅
- command passed after repair ✅
- hardcode guard ✅
- audit 8/8 green ✅

## Next

C26-P0-D: Todo/task state machine — integrate patch/repair loop as task steps.
