# C21-A AI Research and Context Engine Direction

## Status

Completed.

## Added

- `core-platform/docs/brain/context_engine_architecture.md`
- `core-platform/docs/brain/no_hallucination_policy.md`
- `core-platform/docs/brain/c21_research_notes.md`
- `core-platform/data/brain_assets/manifests/context_engine_research_catalog.json`

## Summary

MAOMIAI should evolve from a local model chat shell into a context-engine-driven
local AI platform.

The intended direction is:

```text
Repo Memory
+ Graph Memory
+ Agentic RAG
+ MCP Gateway
+ Cache Context
+ No-Hallucination Policy
```

## Next

C21-B should add a runtime context router:

- project questions -> repo memory
- real-time questions -> tool required
- model questions -> model catalog
- video questions -> video catalog
- normal chat -> local model

