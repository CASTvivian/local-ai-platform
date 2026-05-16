# C26-R7 Code Agent Core Executor Registry

## Goal

Register the first owned builtin adapter as an executor tool:

```
builtin.code_agent_core.execute
```

## Changes

### 1. executor.py

- Import `execute_code_agent_core` from `builtin.code_agent_core`
- Add `_handler_builtin_code_agent_core_execute` handler
- Register `builtin.code_agent_core.execute` in `register_default_executor_tools()`

### 2. planner_tool_schema.json

- Add `builtin.code_agent_core.execute` tool definition with:
  - kind: builtin, risk: medium
  - input_schema: task, workspace_root, files, patch, test_command, cwd, timeout
  - output_schema: ok, task_run_id, patches, tests, audit
  - capabilities: code, workspace, patch, diff, repair, test, task_state
  - planner_hints: inspect code, plan patch, run tests, repair build

### 3. builtin_execution_contracts.json

- `builtin.code_agent_core` contract updated:
  - `allowed_tools` prepended with `builtin.code_agent_core.execute`
  - `implementation_status`: planned → implemented_adapter
  - `acceptance_tests` expanded from 5 → 8 (3 new registry-related tests)

## Validation

| Check | Result |
|-------|--------|
| py_compile | PASS |
| has_registered_tool("builtin.code_agent_core.execute") | true |
| registered_tool_count | 12 |
| direct execute_registered_tool test | PASS |
| task_run_id created | PASS |
| patches produced | PASS (1) |
| tests produced | PASS (1) |
| hardcode guard | PASS |
| schema_has_tool | true |
| contract_allows_tool | true |
| code_contract_status | implemented_adapter |
| contract_acceptance_test_count | 8 |

## Registered Tools (12)

1. time.now
2. time.date_math
3. weather.query
4. web.search
5. capability.match
6. repo_memory.search
7. catalog.search
8. skill_store.list
9. workflow_store.list
10. capability.status
11. model.generate
12. **builtin.code_agent_core.execute** ← NEW

## Next

C26-R8:
- Let planner select `builtin.code_agent_core.execute` for code workspace tasks
- Add end-to-end `/agent/run` test for code-agent task
