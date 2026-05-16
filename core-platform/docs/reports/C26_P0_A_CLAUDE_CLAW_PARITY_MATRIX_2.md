# C26-P0-A Claude/Claw Parity Matrix 2.0

## Summary

| Metric | Value |
|--------|-------|
| Total capabilities | 41 |
| Implemented | 29 |
| Partial | 10 |
| Gap | 2 |
| Average score | 88.4 |

## Verdict

- Core rebuild: **DONE**
- Claude/Claw full parity: **NOT DONE**
- Own skill rebuild: **NOT DONE**
- Can demo Mac: **YES**

## P0 Missing or Partial

| ID | Status | Score | Missing Terms |
|----|--------|-------|---------------|
| skills.own_builtin | partial | 55 | our_builtin_skills, builtin_skill |
| own.core_skill_modules | partial | 78 | skill module |

## Full Matrix

| ID | Capability | Status | Score |
|----|-----------|--------|-------|
| workspace.file_tree | Workspace file tree awareness | implemented | 96 |
| workspace.file_read | Read project files safely | implemented | 96 |
| workspace.file_write | Write project files with approval | implemented | 96 |
| workspace.diff_review | Diff review and patch summary | partial | 74 |
| workspace.repo_memory | Repo memory search | implemented | 100 |
| planner.schema | Schema-driven planner | implemented | 100 |
| planner.structured_output | Planner model structured output | implemented | 100 |
| planner.replan | Observation and replan loop | partial | 64 |
| planner.todo_state | Todo/task state machine | partial | 62 |
| planner.session_resume | Session resume | partial | 64 |
| executor.registry_dispatch | Tool registry dispatch | implemented | 100 |
| executor.shell | Shell execution with sandbox | partial | 74 |
| executor.build_test_loop | Build/test/repair loop | partial | 78 |
| executor.approval_gate | Approval gate for risky actions | implemented | 87 |
| executor.artifacts | Artifact generation and report chain | implemented | 100 |
| renderer.data_driven | Data-driven renderer | implemented | 100 |
| replay.timeline | Run timeline replay | gap | 28 |
| trace.observability | Trace observability | partial | 55 |
| mcp.runtime | MCP runtime and invoke | partial | 78 |
| skills.default_generation | Default skills from repo assets | implemented | 100 |
| skills.capability_registry | Skills as capabilities | implemented | 100 |
| skills.planner_context | Planner discovers skills | implemented | 100 |
| skills.desktop_store | Desktop skill store | implemented | 100 |
| skills.own_builtin | Own rebuilt builtin skills | partial | 55 |
| skills.lifecycle_state | Skill lifecycle state | implemented | 100 |
| model.ollama | Ollama local model runtime | implemented | 87 |
| model.gateway | Model gateway | implemented | 100 |
| model.bootstrap | Model bootstrap/download | implemented | 100 |
| model.offline_pack | Offline model preseed pack | gap | 0 |
| desktop.mac | macOS packaged app | implemented | 96 |
| desktop.windows | Windows MSI package | partial | 78 |
| desktop.runtime_autostart | Desktop runtime autostart | implemented | 100 |
| desktop.runtime_config_generated | Generated runtime config | implemented | 100 |
| policy.sandbox_config | Sandbox policy config | implemented | 87 |
| policy.audit_guard | Runtime hardcode guard | implemented | 100 |
| policy.enterprise_config | Enterprise configurable policy | implemented | 87 |
| team.runtime | Multi-agent runtime | partial | 78 |
| team.failure_isolation | Team failure isolation | partial | 64 |
| own.skill_rebuild_matrix | External→own rebuild matrix | partial | 78 |
| own.core_skill_modules | Own built-in skill modules | partial | 78 |
| own.continuous_audit | Self audit and integrity check | implemented | 100 |

## Next Required

1. **C26-P0-B**: workspace diff/patch engine
2. **C26-P0-C**: build-test-repair loop
3. **C26-P0-D**: task todo state machine
4. **C26-R1**: skill rebuild grading (147 skills → must/optional/reference/exclude)
5. **C26-R2**: own builtin skill modules
6. **C25-WIN-FINAL-SMOKE**: Windows final smoke test
