# C25-B7 Filesystem Sandbox

## Status
Implemented.

## What Changed
- Added sandbox-local filesystem root.
- Added safe path resolver that blocks path escape.
- Added sandbox create, write, read, list and delete operations.
- Added filesystem manifest export.
- Added MCP registry entries for filesystem tools.
- Added approval-gated `filesystem.write` and `filesystem.delete`.
- Added execution audit integration for approved filesystem actions.

## New APIs
- `POST /agent/filesystem/sandbox`
- `POST /agent/filesystem/write`
- `POST /agent/filesystem/read`
- `POST /agent/filesystem/list`
- `POST /agent/filesystem/delete`
- `GET /agent/filesystem/manifest/{sandbox_id}`

## Runtime Effect
Agent Runtime can now read and write files inside a dedicated filesystem sandbox only.

```text
filesystem action -> approval -> sandbox -> audit
```

## Safety Notes
- Direct filesystem API operations are still restricted to the sandbox root.
- MCP `filesystem.write` and `filesystem.delete` require approval.
- Path traversal such as `../outside.txt` is blocked by resolved-path containment checks.
