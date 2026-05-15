# C25 Mac Sync and Demo Acceptance
## Status
Mac demo sync executed; core services are healthy and Agent Runtime acceptance passed on Mac.
## Git HEAD
`5ac47b8fe6a646ac038bf9277bb12c69cda607ae`
## Acceptance Result
`core-platform/data/mac_acceptance/c25/mac_acceptance_result.json`
## Checked
- Git latest main
- Python compile
- Runtime hardcode guard
- Desktop JS syntax
- Ollama local availability
- Core service health
- Agent Runtime smoke
- Time tool smoke
- Repo asset query smoke
- Team Runtime smoke
## Notes
- On Mac, `model_gateway` / `model_bootstrap_service` / `workflow_store_service` need `uvicorn module:app` startup because their `main.py` files expose FastAPI apps without self-running a server.
- Added keyword-rule fallback in Agent Runtime planner so demo-critical queries stay grounded even when planner model is degraded.
## Next
Use Mac as the route demo machine first. Windows packaging resource issue remains separate C25-C13.
