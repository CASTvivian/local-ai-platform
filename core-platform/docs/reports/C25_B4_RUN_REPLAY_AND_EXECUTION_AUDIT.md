# C25-B4 Run Replay + Execution Audit

## Status
Implemented.

## What Changed
- Added persistent execution records for approved runtime execution.
- Added execution audit store under `core-platform/data/execution_store`.
- Approval execution now records `execution_id`, `approval_id`, `run_id`, `session_id`, tool, command, return code, stdout, stderr and sandbox id.
- Added APIs to list, inspect and replay execution records.

## New APIs
- `GET /agent/executions`
- `GET /agent/execution/{execution_id}`
- `GET /agent/replay/run/{run_id}`
- `GET /agent/replay/approval/{approval_id}`

## Runtime Effect
Approved sandbox executions can now be audited and replayed by approval id or run id.

This continues Claude/Claw Runtime recovery:

```text
approval -> sandbox -> execution -> audit -> replay
```

## Remaining Work
- Run replay UI.
- Stronger sandbox isolation.
- Filesystem and browser runtime executors.
- MCP runtime unification.
