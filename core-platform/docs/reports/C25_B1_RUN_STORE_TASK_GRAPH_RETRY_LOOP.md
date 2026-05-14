# C25-B1 Run Store, Task Graph and Retry Loop

## Status

Implemented.

## What Changed

Agent Runtime now persists every run to disk:

```text
core-platform/data/run_store/{run_id}.json
```

Sessions now persist run ids:

```text
core-platform/data/session_store/{session_id}.json
```

Both directories are ignored by git because they are runtime state.

## New Runtime Modules

- `agent_runtime_service/app/run_store/models.py`
- `agent_runtime_service/app/run_store/store.py`
- `agent_runtime_service/app/session_store/models.py`
- `agent_runtime_service/app/session_store/store.py`

## Loop State

Each run now records:

- `run_id`
- `session_id`
- `status`
- `input`
- `current_step`
- `final_answer`
- `task_graph`
- `steps`

Each step records:

- planner output
- tool results
- validation result
- timestamp

## Retry Boundary

The validator now exposes:

- `build_validation(...)`
- `should_retry(validation)`

The loop can continue while validation is retryable.

## Multi-Step Smoke Case

Input:

```text
帮我分析这个项目架构
```

Expected task graph:

1. Query service/runtime architecture evidence.
2. Query catalog, skill store and workflow store.
3. Summarize architecture state.

## API

Added:

- `GET /agent/run/{run_id}`
- `GET /agent/session/{session_id}`

## Verification

Passed:

- Python compile
- Direct `run_agent(...)` smoke tests
- HTTP `/agent/run` smoke test
- HTTP `/agent/run/{id}` reload test
- HTTP `/agent/session/{id}` reload test

Observed:

- `repo_memory.search` correctly routes but reports unavailable when `18125` is not running.
- Date math now supports Chinese numerals such as `三天后`.

## Next

C25-B2 should add:

- approval gate
- sandbox boundary
- safer tool permission classes
- durable retry/self-correction policy
