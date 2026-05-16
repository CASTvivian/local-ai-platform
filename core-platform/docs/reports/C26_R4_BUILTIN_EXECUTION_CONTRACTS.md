# C26-R4 Builtin Execution Contracts

## Goal

Define execution contracts for own builtin fusion modules.

## Output

`data/skill_brain/builtin_execution_contracts.json`

## Contract Fields

Each builtin module has:

- `execution_mode` — how this module is executed (workspace_agent, agent_plan, tool_registry, etc.)
- `allowed_tools` — which tools this module may invoke during execution
- `input_schema` — JSON Schema describing required and optional input
- `output_schema` — JSON Schema describing expected output structure
- `acceptance_tests` — list of testable criteria for implementation validation
- `runtime_dependency_policy` — always `owned_code_only` (no external runtime deps)

## Execution Modes (12 unique)

| Module | execution_mode |
|--------|---------------|
| builtin.code_agent_core | workspace_agent |
| builtin.agent_runtime_core | agent_plan |
| builtin.mcp_tool_hub | tool_registry |
| builtin.browser_operator | browser_plan |
| builtin.memory_rag_core | retrieval |
| builtin.workflow_orchestrator | workflow_plan |
| builtin.local_model_runtime | model_runtime |
| builtin.prompt_skill_engine | prompt_template |
| builtin.security_sandbox | policy_gate |
| builtin.eval_benchmark | evaluation |
| builtin.ui_desktop_operator | ui_binding |
| builtin.artifact_report_engine | report_generation |

## Specialized Tool Access

4 modules have tools beyond the default (capability.match, repo_memory.search, model.generate):

- **builtin.code_agent_core**: filesystem.read, filesystem.write, shell.exec
- **builtin.browser_operator**: web.search
- **builtin.workflow_orchestrator**: workflow_store.list
- **builtin.local_model_runtime**: model.generate (primary tool, no repo_memory.search)

## Validation Results

| Check | Result |
|-------|--------|
| contract_count | 12 |
| all_have_input_schema | ✅ true |
| all_have_output_schema | ✅ true |
| all_have_allowed_tools | ✅ true |
| all_owned_code_only | ✅ true |
| unique_acceptance_tests | 35 |
| implementation_status | 12 planned, 0 implemented |

## Meaning

This makes builtin.* modules more than labels.

They now have a structured contract describing:

- **what input they accept** — via input_schema
- **what tools they may use** — via allowed_tools
- **what output they should produce** — via output_schema
- **how they are validated** — via acceptance_tests
- **whether they are implemented** — via implementation_status

## Next

C26-R5:

- Load contracts into capability registry.
- Attach execution contract to each builtin.* capability.
- Let planner use contract metadata when selecting tools.
