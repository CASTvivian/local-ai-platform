# C26-GAP-B Browser Operator Adapter

## Goal
Close source parity gap: `browser_operator` gap → covered

## New Adapter
`services/agent_runtime_service/app/builtin/browser_operator.py`

## Registered Tool
`builtin.browser_operator.execute` (14th executor tool)

## Current Scope — Safe Foundation Version
- Creates browser/research action plan (4-5 steps depending on domain constraints)
- Optionally calls `search_web` via owned runtime
- Normalizes findings and citations from web results
- Writes audit JSON to `data/builtin_runs/`
- **Does NOT perform uncontrolled browser actions**

## Task State Tracking
Three tracked steps: plan → search → normalize

## Validation Results
| Check | Status |
|-------|--------|
| py_compile | ✅ PASS |
| registered_tool_count | 14 |
| has_browser_tool | ✅ true |
| schema_has_tool | ✅ true |
| contract_allows_tool | ✅ true |
| contract_status | implemented_adapter |
| direct execute_registered_tool | ✅ PASS |
| task_run_id generated | ✅ |
| action_plan generated | ✅ (5 steps with domain constraint) |
| audit_path generated | ✅ |
| hardcode guard | ✅ PASS |
| capability.match("浏览器自动化") | ✅ top-1 hit |

## Files Changed
1. **NEW** `app/builtin/browser_operator.py` — BrowserOperatorResult dataclass + execute_browser_operator()
2. **UPDATED** `app/executor.py` — import + handler + register (14th tool)
3. **UPDATED** `data/agent_policy/planner_tool_schema.json` — added builtin.browser_operator.execute tool definition
4. **UPDATED** `data/skill_brain/builtin_execution_contracts.json` — browser_operator: planned → implemented_adapter

## Source Parity Gap Status
- ~~browser_operator: gap~~ → **covered**
- agent_runtime: covered (C26-GAP-A)
- security_sandbox: partial (40%, next target)

## Next
C26-GAP-C: security_sandbox interactive permission/approval system
