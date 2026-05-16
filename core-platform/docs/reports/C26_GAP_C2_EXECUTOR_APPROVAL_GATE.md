# C26-GAP-C2 Executor Approval Gate

## Goal
Integrate interactive approval system into high-risk executor paths.

## Implemented
Three builtin executor tools now require approval before execution:

| Tool | Risk | Rationale |
|------|------|-----------|
| `builtin.code_agent_core.execute` | high | Can inspect/patch/test workspace files |
| `builtin.browser_operator.execute` | high | Can browse external websites |
| `builtin.memory_rag_core.execute` | high | Can access repository memory and knowledge |

## Flow
```text
execute builtin.* tool
→ no approval_id
→ _approval_gate_for_tool() called
→ ensure_approved_or_request()
→ requires_approval(action, risk) → True for high risk
→ create_approval_request()
→ return ToolResult(ok=False, error="approval_required")
→ reviewer approves
→ execute again with approval_id
→ ensure_approved_or_request() → ok=True
→ _approval_gate_for_tool() returns None
→ actual handler executes
→ ToolResult(ok=True)
```

## Safe Tools (NOT gated)
time.now, time.date_math, weather.query, web.search, capability.match,
repo_memory.search, catalog.search, skill_store.list, workflow_store.list,
capability.status, model.generate — all pass through without approval.

## Code Changes
- `executor.py`: Added `ensure_approved_or_request` import, `_HIGH_RISK_TOOLS` map,
  `_approval_gate_for_tool()` helper, gate calls in 3 builtin handlers.

## Validation
- py_compile: PASS
- First execution returns `approval_required`: PASS
- Approval can be approved: PASS
- Second execution with approval_id succeeds: PASS
- task_run_id generated: PASS
- browser_operator gated: PASS
- memory_rag_core gated: PASS
- Safe tools NOT gated: PASS
- hardcode guard: PASS
- Audit JSON: 8/8 green

## Next
C26-SOURCE-PARITY-AUDIT-LITE rerun to confirm 0 high-risk gaps.
