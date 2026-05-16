# C26-R8 Code Agent Core Planner E2E

## Goal

Let schema planner select `builtin.code_agent_core.execute` for code/workspace tasks through builtin execution contracts.

## Implemented

schema_planner.py checks discovered builtin capabilities and their execution contracts.

If a builtin module has an implemented builtin tool in planner_tool_schema.json, the planner adds that tool step.

## Validation

- ✅ build_plan selects `builtin.code_agent_core.execute`
- ✅ execute_plan can run the selected tool
- ✅ tool creates task_run, patch plan and repair loop result
- ✅ hardcode guard passes

## Test Queries

| Query | Selected builtin tool |
|-------|---------------------|
| 请用代码智能体检查项目文件并生成 patch | ✅ builtin.code_agent_core.execute |
| 帮我检查 workspace 代码并运行测试 | ✅ builtin.code_agent_core.execute |
| 我想让代码智能体修复一个文件 | ✅ builtin.code_agent_core.execute |

## Executor E2E Result

```
builtin.code_agent_core.execute ok=True
task_run_id=taskrun_7feab84c5a2e40c18dc3b7f563e5606d
patches=[{ok: True, path: demo.py, diff: -print('hello') +print('hello patched')}]
tests=[{ok: True, status: passed_initial}]
```

## Meaning

builtin.code_agent_core is now usable through the planner/executor main chain, not just direct unit test.

## Next

C26-R9:
- Add /agent/run end-to-end route test.
- Add frontend demo action for code agent core.
