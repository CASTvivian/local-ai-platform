# C25-C8-FIX Team Runtime Failure Isolation
## Problem
`/agent/team/run` could fail with HTTP 500 when worker `run_agent()` failed due to model gateway 503 or planner circuit issues.
## Fix
- Worker execution is wrapped.
- Worker failure becomes structured output.
- Team run always creates `team_run_id`.
- Team state is saved even when internal worker fails.
- Timeline records worker fallback/error.
- `/agent/team/run/{team_run_id}` can replay partial or failed runs.
## Expected behavior
Even if model gateway is down:
- `/agent/team/run` returns a `team_run_id`
- `state.messages` exists
- `state.timeline` exists
- `agent_outputs` contains worker fallback records
- service does not return HTTP 500