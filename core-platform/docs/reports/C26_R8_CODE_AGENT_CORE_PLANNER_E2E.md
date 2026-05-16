# C26-R8 Code Agent Core Planner E2E

## Goal
Let schema planner select `builtin.code_agent_core.execute` for code/workspace tasks through builtin execution contracts.

## Implemented

### schema_planner.py
- Added `_contract_tool_steps_from_capabilities(message, schema)` — discovers builtin capabilities via `capability.match`, then checks whether their `allowed_tools` contain an implemented builtin tool that exists in `planner_tool_schema.json`. If found, inserts that tool step.
- Modified `_schema_only_default_plan()` — calls `_contract_tool_steps_from_capabilities()` before skill context, inserting builtin tool steps at position 0.

### executor.py
- Added step-level args merging: executor now indexes `plan.args.steps` by tool name and merges each step's `args` dict into the dispatch payload. This allows builtin tools to receive structured parameters (task, workspace_root, files, patch, test_command, etc.) from planner steps.

### security/sandbox.py
- Added `builtin.code_agent_core.execute` to `SAFE_TOOLS`. Owned builtin adapters have fully controlled execution paths with task_state tracking and audit logging.

## Validation

| Check | Result |
|-------|--------|
| py_compile schema_planner.py | ✅ |
| py_compile executor.py | ✅ |
| py_compile sandbox.py | ✅ |
| build_plan selects builtin.code_agent_core.execute (3/3 queries) | ✅ |
| execute_plan runs builtin tool successfully | ✅ |
| task_run_id generated | ✅ |
| patches generated | ✅ |
| tests generated | ✅ |
| audit JSON written | ✅ |
| hardcode guard | ✅ |

## Meaning

`builtin.code_agent_core` is now usable through the planner/executor main chain, not just direct unit test. The full flow is:

```
user says "检查代码/生成 patch/跑测试"
→ planner auto-selects builtin.code_agent_core.execute
→ executor dispatches to registered handler
→ code_agent_core adapter runs (task_state → patch_engine → repair_loop → audit)
→ result flows back through executor
```

## Files Changed

1. `services/agent_runtime_service/app/planning/schema_planner.py` — added `_contract_tool_steps_from_capabilities()`, modified `_schema_only_default_plan()`
2. `services/agent_runtime_service/app/executor.py` — added step-level args merging for builtin tool payloads
3. `services/agent_runtime_service/app/security/sandbox.py` — added `builtin.code_agent_core.execute` to `SAFE_TOOLS`

## Next

C26-R9:
- Add `/agent/run` end-to-end route test
- Add frontend demo action for code agent core
