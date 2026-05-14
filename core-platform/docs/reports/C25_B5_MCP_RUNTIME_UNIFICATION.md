# C25-B5 MCP Runtime Unification

## Status
Implemented.

## What Changed
- Added MCP-style runtime tool metadata models.
- Added runtime tool registry with default tools.
- Added unified MCP invoke API.
- Added approval-aware local tool invocation for restricted tools.
- Added disabled placeholders for web and weather tools.
- Added executor helper to invoke registered tools while preserving existing direct fallbacks.

## New APIs
- `GET /agent/mcp/tools`
- `GET /agent/mcp/tool/{tool_name}`
- `POST /agent/mcp/tool`
- `POST /agent/mcp/invoke`

## Default Tools
- `repo_memory.search`
- `skill_store.list`
- `workflow_store.list`
- `model.generate`
- `shell.exec`
- `filesystem.write`
- `web.search`
- `weather.query`

## Runtime Effect
External and local capabilities now have one registry surface:

```text
tool registry -> tool router -> approval -> sandbox -> execution
```

`shell.exec` returns an approval requirement through the MCP invoke path, then continues through the existing approval execution API.

## Remaining Work
- Capability registry.
- Filesystem sandbox executor.
- Browser runtime.
- Stronger sandbox isolation.
- MCP tool discovery from external servers.
