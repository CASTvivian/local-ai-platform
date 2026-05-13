# C23-B Agent Runtime Service

## Status

Implemented.

## Why

The desktop chat path was not using a real Agent Core. This step adds a backend Agent Runtime service with:

- Planner
- Tool Router
- Executor
- Validator
- Renderer

## Service

```text
core-platform/services/agent_runtime_service
```

Port:

```text
18131
```

Endpoints:

- `GET /health`
- `GET /agent/tools`
- `POST /agent/plan`
- `POST /agent/run`

## Tools

- `time.now`
- `time.date_math`
- `repo_memory.search`
- `catalog.search`
- `skill_store.list`
- `workflow_store.list`
- `model.generate`
- `weather.query` disabled
- `web.search` disabled

## Next

C23-C should route desktop chat to `18131 /agent/run`.

If `delegated_to_model=true`, desktop may still call direct local model.
