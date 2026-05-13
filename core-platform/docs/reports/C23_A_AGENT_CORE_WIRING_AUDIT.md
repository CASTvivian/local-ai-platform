# C23-A Agent Core Wiring Audit

## Status

Completed on May 13, 2026.

## Executive Conclusion

The current Windows desktop chat path is **not** wired to a unified Agent Runtime.

What is currently observable:

```text
Desktop Chat
  -> windows-demo-stable-router.js
  -> direct Tauri / PowerShell / Ollama local inference
  -> selected side-service calls such as Repo Memory
```

What is **not** currently observable on the desktop main path:

```text
Desktop Chat
  -> /agent/run or equivalent runtime endpoint
  -> Planner
  -> Tool Router
  -> Skill Store / Repo Memory / Workflow Store as callable tools
  -> Executor
  -> Validator
```

This explains why the current app behaves like a local-model desktop demo with partial grounding rather than a Claude Code-style agent loop.

## 1. Current Git Context

Recent commits at audit time:

- `bfdaabc feat: add runtime context router for chat grounding`
- `4743166 docs: record final Windows package preflight`
- `89bffc4 docs: add context engine research direction for brain upgrade`
- `805601b feat: seed brain assets into repo memory`

## 2. Existing Agent-Adjacent Service Surface

Readable services and service families found in the repository:

- `core-platform/services/agent_orchestrator`
- `core-platform/services/auto_router_service`
- `core-platform/services/model_gateway`
- `core-platform/services/repo_memory_service`
- `core-platform/services/skill_store_service`
- `core-platform/services/workflow_store_service`

The following services are clearly implemented and expose concrete APIs:

### Repo Memory

Observed endpoints include:

- `/repo/list`
- `/repo/{repo_id}`
- `/repo/register`
- `/knowledge/add`
- `/knowledge/search`
- `/brain/assets`
- `/brain/seed`
- `/brain/search`

### Skill Store

Observed endpoints include:

- `/list`
- `/parse_skill_md`
- `/install_skill_md`
- `/skill/{skill_id}`
- `/enable/{skill_id}`
- `/disable/{skill_id}`
- `/skill/{skill_id}/update`

### Workflow Store

The desktop UI has workflow management screens and service references, but this audit did not find evidence that chat messages are routed through a workflow runtime.

## 3. Desktop Chat Wiring Evidence

The current desktop app has:

- Skill Store UI screens
- Workflow Store UI screens
- Repo Memory UI screens
- A frontend runtime context router
- Direct local model inference through `generate_local_ai_response`
- Direct Repo Memory fetches to `http://127.0.0.1:18125/brain/search`

Important distinction:

- Repo Memory is currently called as a frontend side-service.
- It is **not** shown as a planner-selected tool inside a central agent loop.

The desktop router currently decides some categories itself:

- time query
- live-data blocked query
- repo-memory query
- capability query
- normal local chat

That is useful as an anti-hallucination guard, but it is still frontend routing, not a reusable agent runtime.

## 4. Missing Unified Agent Runtime Evidence

This audit did **not** find desktop-facing evidence for:

- `POST /agent/run`
- `POST /agent/chat`
- `POST /agent/plan`
- a tool router endpoint consumed by desktop chat
- a planner/executor/validator loop used by desktop chat

No concrete desktop path was found that sends a user task into:

```text
planner -> tool router -> executor -> validator
```

## 5. Windows Packaging Evidence

The current Tauri resource list includes:

- bootstrap PowerShell scripts
- service start/stop scripts
- `model_bootstrap_service`
- `model_gateway`

The current Tauri resource list does **not** include:

- `repo_memory_service`
- `skill_store_service`
- `workflow_store_service`
- `agent_orchestrator`
- a dedicated `agent_runtime_service`

This means the packaged Windows app cannot currently be assumed to ship a full agent-service stack.

## 6. Local Source Readability Risks

Two core-looking files are macOS `compressed,dataless` placeholders in this checkout:

- `core-platform/services/agent_orchestrator/main.py`
- `core-platform/services/model_gateway/main.py`

Because of that, this audit could not inspect their readable source from the local workspace.

Additional observation:

- `core-platform/services/auto_router_service` currently has no readable runtime source beyond an empty `__init__.py`; only stale `pyc` files were visible locally.

These source-readability issues must be resolved before claiming an existing complete Agent Core can simply be reconnected.

## 7. Audit Findings

1. The Windows desktop app does not currently use a unified Agent Runtime as its main chat path.
2. Repo Memory, Skill Store, and Workflow Store exist as platform components, but desktop chat does not currently orchestrate them through a planner/tool loop.
3. The packaged Windows resources do not include enough backend services to behave like a full local agent platform.
4. Current desktop behavior is consistent with:
   - local model chat
   - direct model inference
   - selective frontend routing
   - optional Repo Memory lookup
5. Current desktop behavior is not yet consistent with:
   - Claude Code-style planning
   - tool choice
   - tool execution
   - validator-driven correction loop
6. Agent-oriented service source must be made readable before deciding whether to reuse it or replace it.

## 8. Recommended C23-B Direction

Stop adding frontend-only intelligent routing as the main architecture.

Create or restore one explicit runtime entrypoint:

```text
Desktop Chat
  -> POST /agent/run
  -> Planner
  -> Tool Router
  -> Skill Store / Repo Memory / Model Gateway / future MCP tools
  -> Executor
  -> Validator
  -> Final Answer
```

Suggested first implementation target:

- `agent_runtime_service`
- Port: `18130`
- Core endpoints:
  - `POST /agent/run`
  - `GET /agent/tools`
  - `GET /agent/skills`
  - `POST /agent/plan`
  - `POST /agent/execute`

## 9. Immediate Prerequisites Before C23-B

1. Make `agent_orchestrator/main.py` readable locally.
2. Make `model_gateway/main.py` readable locally.
3. Decide whether the existing orchestrator is reusable or whether a clean `agent_runtime_service` should be built.
4. Define which services are first-class runtime tools:
   - Repo Memory
   - Skill Store
   - Model Gateway
   - Workflow Store
5. Update Windows packaging once the runtime service contract is real.

## 10. Bottom Line

The user's diagnosis is correct:

- The current desktop product is not yet exercising a real Agent Core main path.
- Asset catalogs and side services exist.
- Runtime orchestration is the missing bridge.

C23-B should wire that bridge explicitly.
