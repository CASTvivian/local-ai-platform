# C26-R6 Code Agent Core Adapter

## Goal
Implement first owned builtin execution adapter: `builtin.code_agent_core`

## Status: COMPLETED ✅

## New Module
`services/agent_runtime_service/app/builtin/code_agent_core.py`

## Architecture

```
builtin.code_agent_core
├── task_state      → create_task_run / update_task_status / task_progress
├── patch_engine    → read_workspace_file / plan_replace_file
├── repair_loop     → run_build_test_repair_loop
└── audit           → _write_audit (JSON)
```

## Execution Flow

1. **Guard**: Missing task → early return with error + audit
2. **Create Task Run**: 4-step tracked execution
3. **Step 1 — Inspect**: Read requested files via `read_workspace_file`
4. **Step 2 — Plan Patch**: Generate diff via `plan_replace_file` when patch payload provided
5. **Step 3 — Test**: Run command through `run_build_test_repair_loop` when test_command provided
6. **Step 4 — Summarize**: Compute progress, write final audit

## Capabilities
- Creates task run with 4-step tracking
- Reads workspace files (with boundary enforcement)
- Plans full-file patches (replace_file kind)
- Runs build/test commands with optional repair action
- Writes per-run audit JSON to `data/builtin_runs/`

## Safety
- Does NOT guess arbitrary code changes by itself
- Only executes structured payloads through owned workspace tools
- Workspace path boundary enforced by patch_engine
- All operations tracked in task_state

## Validation Results

| Check | Result |
|-------|--------|
| py_compile | ✅ PASS |
| Functional test (ok=true) | ✅ PASS |
| builtin_id = builtin.code_agent_core | ✅ PASS |
| task_run_id created | ✅ PASS |
| patches generated (1 patch with diff) | ✅ PASS |
| repair_loop invoked (test passed) | ✅ PASS |
| audit JSON written | ✅ PASS |
| hardcode guard | ✅ PASS |

## Audit
`data/agent_core_audit/c26/skill_brain/c26_r6_code_agent_core_adapter.json`

- has_execute: true
- uses_task_state: true
- uses_patch_engine: true
- uses_repair_loop: true
- writes_audit: true
- owned_builtin_id: true

## Next: C26-R7
Register builtin adapter into executor tool registry:
- Tool name: `builtin.code_agent_core.execute`
- Wire dispatch through `tool_dispatch_registry`
