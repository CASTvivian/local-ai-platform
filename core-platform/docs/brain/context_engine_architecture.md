# MAOMIAI Context Engine Architecture

## Why

MAOMIAI should not rely on raw local model chat alone.
The platform needs a context engine that decides when to use:

- local model inference
- repo memory
- graph memory
- web or real-time tools
- MCP tools
- cached context
- video generation services

## Target Architecture

```text
User Input
  -> Intent Classifier
  -> Context Router
      -> Local Model
      -> Repo Memory
      -> Graph Memory
      -> MCP Gateway
      -> Web / Weather / Time Tool
      -> Video Generation Router
  -> Evidence / Result Validator
  -> Final Answer
```

## Core Modules

### 1. Repo Memory

Stores local repository summaries, GitHub starred repository summaries,
service docs, API surfaces, and integration notes.

### 2. Graph Memory

Builds structured knowledge relations:

```text
repo -> service -> API -> capability -> model -> tool -> workflow
```

Future upgrade: Tree-Sitter code graph for source-level understanding.

### 3. Agentic RAG

Uses retrieval as a step inside planning, not as a one-shot vector search.

### 4. MCP Gateway

Connects MAOMIAI to external tools, APIs, file systems, GitHub, web search,
weather, databases, and video generation services.

### 5. Cache-Augmented Context

Stores stable and frequently used context to reduce repeated retrieval.

### 6. No-Hallucination Policy

- Real-time questions must use tools.
- Project questions must query repo memory.
- If evidence is unavailable, answer with uncertainty.
- Do not claim unavailable capabilities.

