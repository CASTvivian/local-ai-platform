# C26-GAP-C2 Executor Approval Gate

## Goal
Integrate interactive approval system into high-risk executor paths.

## Implemented
Three builtin tools now require approval before execution:

| Tool | Risk Level | Reason |
|------|-----------|--------|
| `builtin.code_agent_core.execute` | high | Can inspect/patch/test workspace files |
| `builtin.browser_operator.execute` | high | Can perform browser/research actions |
| `builtin.memory_rag_core.execute` | high | Can access repo memory/knowledge |

## Architecture

### `_HIGH_RISK_TOOLS` map
```python
_HIGH_RISK_TOOLS: dict[str, str] = {
    "builtin.code_agent_core.execute": "high",
    "builtin.browser_operator.execute": "high",
    "builtin.memory_rag_core.execute": "high",
}
```

### `_approval_gate_for_tool()` helper
- Extracts `approval_id` from args
- Calls `ensure_approved_or_request()` from `approval_store`
- Returns `None` if approved (allow execution)
- Returns `ToolResult(ok=False, error="approval_required")` if not

### Safe tools NOT gated
- `time.now`, `time.date_math`, `weather.query`, `web.search`
- `capability.match`, `capability.status`, `repo_memory.search`
- `catalog.search`, `skill_store.list`, `workflow_store.list`, `model.generate`

## Flow
```text
execute builtin.*.execute
→ no approval_id
→ _approval_gate_for_tool() returns ToolResult(error="approval_required")
→ reviewer approves via decide_approval()
→ execute again with approval_id in args
→ _approval_gate_for_tool() returns None
→ execution proceeds
```

## Validation
- py_compile: PASS ✅
- First execution returns approval_required: PASS ✅
- Approval can be approved: PASS ✅
- Second execution with approval_id succeeds: PASS ✅
- task_run_id generated: PASS ✅
- All 3 builtin tools gated: PASS ✅
- Safe tools NOT gated: PASS ✅
- Hardcode guard: PASS ✅
- Audit 7/7: PASS ✅

## Next
C26-SOURCE-PARITY-AUDIT-LITE rerun to confirm 0 high-risk gaps.
