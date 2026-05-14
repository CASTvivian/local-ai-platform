# C25-C3 LLM Observation / Replan Loop

Implemented:
- Observation model
- observation builder
- LLM replanner prompt
- replan JSON parser
- service-level observation loop
- run_store persistence for observations and replan decisions

Runtime behavior:
- plan
- execute
- observe
- validate
- replan when unresolved
- execute again when replanner selects next tools
- final answer

This moves Agent Runtime beyond single-step planning without reintroducing hardcoded user-query routing.

Next:
- C25-C4 should strengthen autonomous loop recovery when planner/model gateway is unavailable.
- C25-C5 should add run replay UI for observations and replans.
