# C25-C8 Multi-Agent Runtime

Implemented:
- external agent team registry
- team models
- team registry loader
- team run store
- coordinator
- worker agent execution through existing Agent Runtime
- agent message records
- team timeline
- team APIs

New APIs:
- GET /agent/team/registry
- GET /agent/team/{team_id}
- POST /agent/team/run
- GET /agent/team/runs
- GET /agent/team/run/{team_run_id}

Design:
Agent roles are external config, not hardcoded runtime routing.
Workers reuse existing Agent Runtime:
planner -> execute -> observe -> replan -> final.

Current scope:
This is a local multi-agent orchestration layer.
C26 should improve recursive delegation, agent-to-agent planning, and role-specific memory.