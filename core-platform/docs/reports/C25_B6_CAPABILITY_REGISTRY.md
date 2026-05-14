# C25-B6 Capability Registry

## Status
Implemented.

## What Changed
- Added capability schema.
- Added runtime capability registry.
- Added capability matching service.
- Added model, tool, workflow and catalog capability abstraction.
- Added planner and executor integration for `capability.match`.

## New APIs
- `GET /agent/capabilities`
- `GET /agent/capability/{capability_id}`
- `POST /agent/capability`
- `POST /agent/capabilities/match`

## Default Capabilities
- `chat.light`
- `chat.standard`
- `code.standard`
- `reasoning.standard`
- `repo.memory`
- `skill.store`
- `workflow.store`
- `shell.sandbox`
- `web.search` disabled
- `weather.query` disabled
- `video.catalog`

## Runtime Effect
Agent Runtime can now match a user task to model, tool, workflow or catalog capabilities.

This starts moving model/tool selection from manual UI choice toward runtime selection:

```text
goal -> capability match -> tool/model routing -> execution
```

## Remaining Work
- Automatic model switching through capability match results.
- Capability to MCP tool execution binding.
- Filesystem sandbox.
- Browser runtime.
- Multi-agent runtime.
