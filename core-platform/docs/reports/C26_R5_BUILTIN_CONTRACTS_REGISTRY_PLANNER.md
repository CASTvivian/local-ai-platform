# C26-R5 Builtin Contracts Registry Planner

## Goal
Attach execution contracts to `builtin.*` capabilities and expose contract context to planner.

## Implemented

### Capability Registry (`registry.py`)

Added `load_builtin_contracts()` — loads `data/skill_brain/builtin_execution_contracts.json` keyed by module id.

`_builtin_module_to_capability()` now merges contract fields:

```text
execution_contract     → full contract dict
execution_mode         → e.g. workspace_agent, tool_registry, retrieval
allowed_tools          → from contract (e.g. filesystem.read, shell.exec)
input_schema           → from contract
output_schema          → from contract
acceptance_tests       → from contract
runtime_dependency_policy → owned_code_only
```

### Planner (`schema_planner.py`)

Added `_builtin_contract_context_step()` — requests `capability.match` with `include_builtin_contracts: True`.

`_skill_context_steps()` now delegates to `_builtin_contract_context_step()`.

## Validation

| Check | Result |
|-------|--------|
| py_compile registry.py | PASS |
| py_compile schema_planner.py | PASS |
| contract_count >= 12 | 12 PASS |
| builtin_capability_count >= 12 | 12 PASS |
| all_builtin_have_contract | true PASS |
| all_builtin_have_allowed_tools | true PASS |
| all_builtin_owned_code_only | true PASS |
| hardcode guard | PASS |

### 5 Query Tests

| Query | Top Builtin | Mode | Has Contract |
|-------|-------------|------|-------------|
| 我想做代码智能体 | builtin.code_agent_core | workspace_agent | YES |
| 有没有 MCP 工具协议能力 | builtin.mcp_tool_hub | tool_registry | YES |
| 浏览器自动化怎么做 | builtin.browser_operator | browser_plan | YES |
| 本地记忆和 RAG 能力 | builtin.memory_rag_core | retrieval | YES |
| 本地模型运行能力 | builtin.local_model_runtime | model_runtime | YES |

## System Upgrade

Before C26-R5: "I know there is builtin.code_agent_core"

After C26-R5: "I know builtin.code_agent_core can use filesystem.read/write, shell.exec, model.generate, and outputs patches/tests/audit"

## Next

C26-R6: Implement first owned builtin execution adapter (`builtin.code_agent_core`), connect to workspace patch engine + repair loop + task state.
