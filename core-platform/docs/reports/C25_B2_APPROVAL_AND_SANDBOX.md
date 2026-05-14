# C25-B2 Approval and Sandbox Boundary

## Status

Implemented.

## What Changed

Agent Runtime now has a security boundary before tool execution:

```text
planner -> sandbox policy -> approval gate -> executor
```

Safe tools execute automatically.
Restricted or unknown tools are blocked and persisted as approval records.

## New Modules

- `agent_runtime_service/app/security/sandbox.py`
- `agent_runtime_service/app/security/guard.py`
- `agent_runtime_service/app/security/approval_models.py`
- `agent_runtime_service/app/security/approval_store.py`

## Safe Tools

- `time.now`
- `time.date_math`
- `repo_memory.search`
- `catalog.search`
- `skill_store.list`
- `workflow_store.list`
- `model.generate`
- `capability.status`
- disabled realtime placeholders such as `weather.query` and `web.search`

## Restricted Tools

- `shell.exec`
- `filesystem.write`
- `filesystem.delete`
- `browser.open`
- `browser.control`
- `os.command`

## Approval APIs

- `GET /agent/approvals`
- `GET /agent/approval/{approval_id}`
- `POST /agent/approval/resolve`

## Verification

Passed:

- Python compile
- Safe tool smoke test
- Restricted `shell.exec` smoke test
- Approval persistence test
- Approval list/get/resolve HTTP tests

## Notes

This stage only blocks and records restricted tool requests.
It does not execute approved restricted tools yet.

That is intentional: C25-B3 should add sandboxed execution for approved actions.
