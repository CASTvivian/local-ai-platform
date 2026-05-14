# C25-B3 Sandboxed Execution Loop

## Status

Implemented.

## What Changed

Approved restricted actions can now execute only through the sandbox runtime:

```text
restricted tool -> approval record -> approval resolve -> sandbox execution
```

## New Runtime Modules

- `agent_runtime_service/app/runtime/sandbox_executor.py`
- `agent_runtime_service/app/runtime/approval_executor.py`

## New API

```text
POST /agent/approval/execute/{approval_id}
```

## Execution Model

Current behavior:

- `shell.exec` is blocked by approval gate.
- Approval must be explicitly resolved before execution.
- Approved command executes in a unique sandbox runtime directory.
- Execution result is persisted as `execution.json`.
- Non-allowlisted binaries are blocked.

Allowlisted binaries:

- `python`
- `python3`
- `node`
- `bash`
- `sh`

## Verification

Passed:

- Python compile.
- Unit smoke: approved `python3 -c "print(123)"` executed in sandbox.
- Unit smoke: `rm -rf ...` blocked by allowlist.
- HTTP smoke: execute before approval returns `approval not granted`.
- HTTP smoke: approval resolve then execute returns stdout.

## Known Boundary

This is a local working-directory sandbox, not a VM/container sandbox.
C25-B4 should add stronger isolation before enabling broader filesystem/browser/shell tools.
