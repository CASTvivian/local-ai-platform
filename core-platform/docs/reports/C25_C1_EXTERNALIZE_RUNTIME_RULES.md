# C25-C1 Externalize Runtime Rules

Implemented:
- planner business/entity hardcode removed
- entity aliases moved to external JSON policy
- planner intent rules moved to external JSON policy
- planner.py no longer contains product/game/company/city-specific correction logic
- date math stays as generic deterministic tool routing
- restricted-action markers moved to policy metadata

Files:
- core-platform/data/agent_policy/planner_policy.json
- core-platform/data/agent_policy/entity_aliases.json
- core-platform/services/agent_runtime_service/app/policy/loader.py
- core-platform/services/agent_runtime_service/app/planner.py

Why:
Runtime code should not hardcode concrete business entities or case-specific fixes.
Concrete entities should come from:
- memory
- provider APIs
- capability registry
- external policy data
- model-driven planner

Next:
C25-C2 should replace policy matching with LLM-driven planner over tool/capability schema.
