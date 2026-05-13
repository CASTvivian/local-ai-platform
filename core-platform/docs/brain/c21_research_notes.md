# C21 Research Notes

## Direction

The target is not "RAG or no RAG".
The target is a hybrid context system that uses the right mechanism for the task.

Important directions:

1. Agentic RAG
2. GraphRAG and graph memory
3. MCP tool orchestration
4. Cache-augmented generation
5. Long-context repo memory
6. Codebase graph memory
7. Hybrid context orchestration

## Implication for MAOMIAI

MAOMIAI should evolve from:

```text
local model chat
```

to:

```text
local model
+ context engine
+ tool router
+ repo memory
+ graph memory
+ MCP gateway
```

## Implementation Priority

### P0

- No-hallucination policy
- Tool requirement for real-time questions
- Repo memory query before project-specific answers

### P1

- Context router
- Repo memory integration in chat
- Model catalog grounding

### P2

- Graph memory
- Tree-Sitter code graph
- MCP gateway

### P3

- ComfyUI and video model router
- Remote GPU generation service

