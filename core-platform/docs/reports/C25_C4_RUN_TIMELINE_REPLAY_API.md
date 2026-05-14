# C25-C4 Run Timeline + Replay API

Implemented:
- timeline event model
- run timeline builder
- replay timeline API
- run_store step observation/replan compatibility fields
- execution audit events merged into timeline

New API:
- `GET /agent/replay/timeline/{run_id}`

Timeline event types:
- `run.created`
- `plan`
- `tool_result`
- `observation`
- `validation`
- `replan`
- `execution`
- `run.completed`

Purpose:
This makes Agent execution inspectable and prepares the Desktop Replay UI.
