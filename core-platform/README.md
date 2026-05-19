# Local AI Platform

> A private, local-first AI Agent workspace for models, tools, memory, code, browser research, approvals, and auditable execution.

本地 AI 智能体平台是一套面向个人、团队和企业的私有化 AI Agent 工作平台。  
它不是一个普通聊天机器人，而是一套能够在本地环境中理解任务、选择工具、执行步骤、记录过程，并在高危动作前进行权限审批的智能体操作平台。

---

## What It Is

Local AI Platform combines:

- Local model runtime
- Agent planning
- Tool execution
- Code agent workflow
- Local knowledge memory
- Browser research
- Permission approval
- Task state tracking
- Audit trail
- Cross-platform desktop app

The goal is simple:

> Let AI run inside your own machine, use your own knowledge, call your own tools, and keep the execution process visible, controllable, and auditable.

---

## Current Status

| Area | Status |
|---|---|
| Core Agent Runtime | Ready |
| Planner / Tool Selection | Ready |
| Executor Tool Registry | Ready |
| Code Agent Core | Ready |
| Memory / RAG Core | Ready |
| Browser Research Core | Ready |
| Permission Approval System | Ready |
| Task State Machine | Ready |
| Patch / Diff Engine | Ready |
| Build / Test / Repair Loop | Ready |
| Skill Store | Ready |
| macOS Desktop Package | Ready |
| Windows MSI Package | Built, ready for real-machine smoke |
| Capability Audit | 14 covered / 0 partial / 0 gap |

---

## Key Capabilities

### 1. Local AI Conversation

Run local AI conversations through the Agent Runtime and local model gateway.

Example:

```text
你好，请用一句话介绍你自己
```

---

### 2. Local Model Runtime

The platform supports local model management and model gateway integration.

Capabilities include:

- Local model health check
- Runtime profile management
- Lightweight model profile
- Coding model profile
- Local model gateway
- Desktop runtime auto-start
- Future offline model pack support

---

### 3. Schema-driven Agent Planner

The planner converts user requests into structured execution plans.

It supports:

- Task understanding
- Capability matching
- Tool selection
- Builtin module selection
- Execution contract recognition
- Model-assisted structured planning
- Agentic loop foundation

Execution chain:

```
User Task
  → Planner
  → Capability Registry
  → Execution Contract
  → Executor Registry
  → Tool / Builtin Adapter
  → Result Renderer
```

---

### 4. Executor Tool Registry

All executable tools are registered through a unified tool registry.

Supported tool categories:

- Time tools
- Model generation
- Local memory retrieval
- Capability matching
- Code agent execution
- Browser research execution
- Workflow store access
- Skill store access
- Approval-gated high-risk actions

Unknown tools fail safely instead of silently executing.

---

### 5. Code Agent Core

The platform includes an owned code agent core module.

It can:

- Inspect workspace files
- Generate patch plans
- Produce unified diffs
- Run build/test commands
- Run repair loops
- Track task progress
- Generate audit records
- Trigger approval gates before high-risk file operations

Example:

```text
请用代码智能体检查项目文件并生成 patch
```

Execution chain:

```
Planner
  → builtin.code_agent_core.execute
  → Approval Gate
  → Workspace Patch Engine
  → Build/Test/Repair Loop
  → Task State
  → Audit
```

---

### 6. Local Knowledge and Memory

The platform includes local memory and project knowledge retrieval.

It can:

- Search local project knowledge
- Retrieve repository memory
- Normalize evidence
- Summarize findings
- Use skill context during planning
- Produce auditable retrieval outputs

Example:

```text
我们现在有哪些 Agent 和 MCP 相关技能？
```

---

### 7. Browser Research Core

The platform includes a browser research module for web-oriented research tasks.

It can:

- Create browser/research action plans
- Run web search
- Normalize findings
- Generate citations
- Produce audit records
- Work with approval gates for controlled execution

Example:

```text
帮我做浏览器自动化和网页研究
```

---

### 8. Permission Approval System

High-risk actions are protected by an interactive approval system.

Supported states:

- pending
- approved
- rejected
- cancelled

High-risk tools can be blocked until approval is granted.

Flow:

```
High-risk action
  → Approval request
  → Pending
  → Approved / Rejected
  → Continue / Block
```

This is designed for local file operations, code execution, browser operations, and other sensitive actions.

---

### 9. Task State Machine

The platform includes a persistent task state system.

Supported task states:

- pending
- in_progress
- completed
- failed
- blocked
- cancelled

It can track multi-step runs, append tasks, calculate progress, and persist task history.

---

### 10. Patch / Diff / Repair Engine

The workspace engine supports:

- File read
- Patch planning
- Text replacement
- Full-file replacement
- Unified diff generation
- Workspace boundary protection
- Patch audit records
- Build/test/repair loops

This gives the platform a real developer-agent foundation instead of plain text suggestions.

---

## Builtin Skill System

The platform currently includes **338** skill assets and organizes them into **12** owned builtin capability modules.

These skills are not exposed as loose fragments.  
They are normalized, classified, and fused into the platform's builtin modules.

### Builtin Modules

| Builtin Module | Purpose | Skill / Reference Count |
|---|---|---|
| `builtin.code_agent_core` | 代码智能体核心模块 | 103 |
| `builtin.mcp_tool_hub` | MCP 工具协议模块 | 73 |
| `builtin.memory_rag_core` | 记忆与 RAG 检索模块 | 36 |
| `builtin.browser_operator` | 浏览器自动化模块 | 31 |
| `builtin.local_model_runtime` | 本地模型运行模块 | 9 |
| `builtin.prompt_skill_engine` | Prompt 技能引擎模块 | 7 |
| `builtin.agent_runtime_core` | 通用 Agent Runtime 模块 | 5 |
| `builtin.eval_benchmark` | 评估与基准模块 | 4 |
| `builtin.workflow_orchestrator` | 工作流编排模块 | 3 |
| `builtin.artifact_report_engine` | 产物与报告生成模块 | 1 |
| `builtin.security_sandbox` | 安全沙箱与策略模块 | 1 |
| `builtin.ui_desktop_operator` | 桌面 UI 操作模块 | 1 |

---

## What Makes It Different

### Not Just Chat

Most AI applications stop at text generation.

Local AI Platform goes further:

```
Understand
  → Plan
  → Select tools
  → Execute
  → Observe
  → Approve high-risk actions
  → Record audit
```

---

### Local-first

The platform is designed around local execution:

- Local model support
- Local runtime services
- Local knowledge
- Local audit files
- Local desktop app
- Private deployment path

---

### Agent Runtime, Not Prompt Wrapper

The system includes real runtime components:

- Planner
- Executor
- Tool registry
- Builtin adapters
- Task state
- Approval system
- Audit logs
- Desktop runtime manager

---

### Builtin Skills, Not Random Plugins

The platform includes **338** skill assets, organized into a controlled builtin capability system.

This allows the agent to select capabilities based on task context rather than relying on scattered plugins.

---

### Approval and Audit by Design

High-risk actions are not blindly executed.

The platform supports:

- approval request
- approval decision
- execution gate
- audit trail

This makes it suitable for serious local and enterprise use cases.

---

### Desktop App

The desktop app supports:

- macOS package
- Windows MSI package
- Local service auto-start
- Model status
- Agent conversation
- Skill store
- Runtime diagnostics
- Service health inspector

---

## Demo Prompts

Try:

```text
你好，请用一句话介绍你自己
今天是几月几号，现在几点
我们现在有哪些 Agent 和 MCP 相关技能？
请用代码智能体检查项目文件并生成 patch
帮我做浏览器自动化和网页研究
```

---

## Product Direction

Local AI Platform is moving toward:

- Fully local AI Agent workspace
- Private enterprise deployment
- Offline model package
- More builtin adapters
- More advanced workflow orchestration
- Desktop-first AI operations console
- Auditable AI execution environment

---

## Current Build Outputs

Current packaging status:

- macOS App: available
- macOS DMG: available
- Windows MSI: available
- Windows real-machine smoke: next validation step

---

## One-line Summary

Local AI Platform is a local-first AI Agent workspace with **338+** builtin skills, code-agent execution, memory retrieval, browser research, permission approval, and auditable tool-based runtime execution.
