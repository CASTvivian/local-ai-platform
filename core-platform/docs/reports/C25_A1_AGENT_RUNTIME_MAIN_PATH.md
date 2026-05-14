# C25-A1 Agent Runtime Main Path

## Status

Implemented.

## What Changed

Desktop chat now sends user messages to:

```text
POST http://127.0.0.1:18131/agent/run
```

The previous frontend-owned routing path has been removed from the main send flow:

- no frontend time/weather/project if-else routing
- no direct `generate_local_ai_response` call from chat
- no direct `18080 /generate` fallback from chat

The local model path is now only reachable through Agent Runtime tool planning.

## Backend Compatibility

`AgentRunRequest` now accepts desktop-style payloads:

```json
{
  "input": "user text",
  "session_id": "desktop-default",
  "source": "desktop-chat",
  "current_profile": "light"
}
```

The response now includes both:

- `answer`
- `final_answer`
- `steps`

## Runtime Loop

`agent_runtime_service` now exposes a minimal loop boundary:

```text
planner -> executor -> validator -> renderer
```

This is still a one-step controlled loop. C25-B should add:

- run_store
- session persistence
- approval gate
- sandbox
- retry / self-correction
- multi-step tool execution

## Windows Packaging

Tauri resources now include:

- `agent_runtime_service`
- `repo_memory_service`
- `skill_store_service`
- `workflow_store_service`

Windows startup now requests:

- `18121 skill_store`
- `18125 repo_memory`
- `18126 workflow_store`
- `18131 agent_runtime`

## Verification

Passed:

- Python compile for `agent_runtime_service`
- Tauri config JSON validation
- JavaScript syntax compile via `new Function(source)`
- `/agent/run` HTTP smoke test with desktop payload
- `/agent/plan` HTTP smoke test with `input`

Note:

`node --check` timed out in the local environment, but direct Node syntax compilation succeeded.
