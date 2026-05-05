# P3.14-D7-SYNC-D Enterprise Services Repaired

## Status
Implemented.

## Context
During Mac / Windows source synchronization, the active Windows packaging root was confirmed as:
```text
core-platform/
```

The desktop app is packaged from:
```text
core-platform/apps/desktop
```

and Tauri resources point to:
```text
core-platform/scripts
core-platform/services
```

## Problem
Six enterprise services existed with full code under the repository root `services/`, while the canonical packaging path `core-platform/services/` only had empty shells.

## Fix
The full enterprise service implementations were synchronized into:
```text
core-platform/services/
```

## Repaired Services
- skill_store_service
- artifact_registry_service
- code_review_gate_service
- repo_memory_service
- workflow_store_service
- design_system_service

## Safety
The original root `services/` directory was not deleted. This step only repairs the active Windows/macOS packaging path.
