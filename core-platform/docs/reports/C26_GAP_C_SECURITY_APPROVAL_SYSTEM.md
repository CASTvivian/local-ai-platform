# C26-GAP-C Security Approval System

## Goal

Close source parity gap:
```
security_sandbox: partial 40% → covered
```

## Implemented

New module: `services/agent_runtime_service/app/security/approval_store.py`

### Capabilities

- `create_approval_request()` — create approval request for high-risk action
- `decide_approval()` — approve or reject a pending request
- `cancel_approval()` — cancel a pending request
- `list_approvals()` — list approval requests with optional status filter
- `load_approval()` / `save_approval()` — persistence
- `requires_approval()` — check whether action needs approval (risk high/critical OR dangerous action set)
- `ensure_approved_or_request()` — combined check+request gate for executor integration

### Data Model

```text
ApprovalRequest: id, action, risk, reason, payload, status, requester, reviewer, decision_reason, timestamps
ApprovalStatus: pending | approved | rejected | expired | cancelled
RiskLevel: low | medium | high | critical
```

### Dangerous Actions (require approval even at medium risk)

- `shell.exec`, `filesystem.write`, `filesystem.delete`
- `network.post`, `credential.access`, `external.browser.action`

### Flow

```
high-risk action
→ requires_approval() → true
→ create_approval_request() → pending
→ decide_approval(approved=true/false) → approved/rejected
→ executor may continue only if approved
→ audit JSON written at each state transition
```

### Audit Trail

- Every request, decision, and cancel event writes a timestamped JSON to `data/approval_audit/`
- Approval objects persisted to `data/approvals/`

## Validation

| Test | Result |
|------|--------|
| py_compile | ✅ PASS |
| pending approval generated | ✅ |
| approve decision works | ✅ |
| reject decision works | ✅ |
| cancel works | ✅ |
| approved action allowed via ensure_approved_or_request | ✅ |
| low-risk action not_required | ✅ |
| list_approvals returns results | ✅ |
| audit files generated (6 events) | ✅ |
| hardcode guard | ✅ PASS |
| all 10 audit checks | ✅ PASS |

## Source Parity Impact

| Area | Before | After |
|------|--------|-------|
| security_sandbox | partial 40% | covered ✅ |
| agentic loop | covered | covered ✅ |
| browser_operator | covered | covered ✅ |
| code_agent_core | covered | covered ✅ |

**All 3 high-risk gaps now closed.**

## Next

- C26-GAP-C2: Integrate approval checks into shell/file/builtin high-risk executor paths
- C26-GAP-D: Desktop UI approval dialog (pending → approve/reject)
- Windows final smoke test
- Offline model pack
