# C26-R9 Agent Run Code Agent Core E2E

## Goal
Verify the main agent runtime chain can use `builtin.code_agent_core.execute` end-to-end, not just in unit tests.

## Chain

```
prompt
→ planner (schema_driven)
→ builtin.code_agent_core.execute (auto-selected as first tool)
→ executor registry dispatch
→ code_agent_core adapter
→ task_state (create_task_run, update_task_status, task_progress)
→ patch_engine (plan_replace_file)
→ repair_loop (run_build_test_repair_loop)
→ renderer (render_answer)
```

## Results

| Check | Status |
|-------|--------|
| planner selected builtin tool | ✅ auto-selected as first tool |
| executor executed builtin tool | ✅ ok=true |
| task_run generated | ✅ taskrun_* |
| patch plan generated | ✅ 1 patch with diff |
| test result generated | ✅ 1 test (passed_initial) |
| audit path generated | ✅ data/builtin_runs/code_agent_core_*.json |
| renderer returned answer | ✅ |

## Plan Output

- **intent**: schema_scored
- **tools**: [builtin.code_agent_core.execute, capability.match, time.now, model.generate]
- **planner_mode**: schema_driven
- **builtin tool is FIRST in plan**: yes

## Builtin Execution Details

- **task_run_id**: generated per run
- **patches**: 1 patch (replace_file action, diff generated)
- **tests**: 1 test (command passed, stdout captured)
- **audit**: full JSON with progress tracking (4/4 tasks, 100%)

## Hardcode Guard

PASS — no runtime hardcode violations

## Meaning

The first owned builtin module (`builtin.code_agent_core`) is now part of the main agent execution path. The schema-driven planner automatically selects it for code/workspace tasks, and the executor dispatches it through the registry — no if/elif, no keyword routing.

## Next

C26-R10 — connect more builtin modules to execution adapters (memory_rag_core, mcp_tool_hub, browser_operator, etc.)
