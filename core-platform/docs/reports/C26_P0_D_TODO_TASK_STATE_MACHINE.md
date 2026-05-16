# C26-P0-D Todo / Task State Machine

## Goal

Add Claude/Claw-style task/todo execution state tracking.

## Implemented

New module:

```text
services/agent_runtime_service/app/task_state/state_machine.py
```

Capabilities:

* create task run
* persist tasks to JSON
* update task status
* start next pending task
* append task
* derive run status
* calculate progress
* list and load task runs

Statuses:

* pending
* in_progress
* completed
* failed
* blocked
* cancelled

## Validation

* py_compile: PASS
* create/start/update/complete/list/load tests: ALL PASS
* hardcode guard: PASS

## Next

Integrate this with:

* repair loop
* agent replay timeline
* desktop task progress UI
