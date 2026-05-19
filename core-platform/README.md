# Local AI Platform
> Local-first AI Agent workspace with local models, tools, memory, code execution, browser research, approval gates, and auditable runtime.

Local AI Platform 是一套面向个人、团队和企业的本地 AI 智能体工作平台。
它不是单一聊天机器人，而是一套可以在本地环境中完成任务规划、工具调用、代码处理、知识检索、浏览器研究、权限审批和审计追踪的智能体运行系统。

---

## Current Status

| Area | Status |
|---|---|
| Core platform architecture | Completed |
| Capability parity audit | 14 covered / 0 partial / 0 gap |
| High-risk capability gaps | 0 |
| Builtin capability modules | 12 |
| Skill assets | 338 |
| Execution contracts | 12 |
| Source logic records | 274 |
| Executable builtin adapters | 3 |
| macOS desktop package | Ready |
| Windows MSI package | Built, smoke validation next |

---

## What Is Confirmed

The platform core has been rebuilt into a real agent runtime architecture.

Confirmed capabilities:
- Schema-driven planning
- Executor tool registry
- Data-driven rendering
- Agentic loop foundation
- Task state machine
- Workspace patch / diff engine
- Build / test / repair loop
- Permission approval gate
- Code agent core
- Memory / RAG core
- Browser research core
- Skill store
- Local model gateway
- macOS and Windows desktop packaging

---

## Important Boundary

The platform currently contains **338 skill assets**.

These skills have been:
- imported
- classified
- state-managed
- assigned to builtin modules
- linked with module-level capability records
- connected to the planner/capability system

The correct claim is:
> Skill assets have been fused into the builtin capability system.

The incorrect claim is:
> Every skill is already an independent executable tool.

Currently executable builtin adapters include:
- `builtin.code_agent_core`
- `builtin.browser_operator`
- `builtin.memory_rag_core`

Other modules remain part of the capability system and can be deepened into executable adapters over time.

---

## Core Capabilities

### Local Model Runtime
- Local model gateway
- Model health check
- Runtime profile management
- Desktop runtime auto-start
- Offline model pack extension path

### Agent Planner
- Schema-driven planning
- Capability matching
- Builtin module selection
- Execution contract recognition
- Structured tool selection

### Executor Runtime
- Tool registry dispatch
- Safe unknown-tool handling
- Builtin adapter execution
- Approval-gated high-risk tools

### Code Agent Core
- Workspace file inspection
- Patch planning
- Unified diff generation
- Build/test execution
- Repair loop
- Task state tracking
- Audit record generation

### Memory / RAG Core
- Local project knowledge search
- Evidence normalization
- Repo memory retrieval
- Context summary
- Audit output

### Browser Research Core
- Browser/research action planning
- Web search
- Findings extraction
- Citation structure
- Audit output

### Approval System
- Pending approval request
- Approve / reject / cancel
- High-risk execution gate
- Approval audit trail

### Skill System
- 338 skill assets
- 12 builtin modules
- Capability registry
- Skill lifecycle state
- Skill store UI
- Planner skill context

---

## Builtin Modules

| Module | Purpose | Skill Assets | Execution Mode | Status |
|---|---|---:|---|---|
| `builtin.code_agent_core` | 代码智能体核心模块 | 103 | workspace_agent | implemented_adapter |
| `builtin.mcp_tool_hub` | MCP 工具协议模块 | 73 | tool_registry | planned |
| `builtin.memory_rag_core` | 记忆与 RAG 检索模块 | 36 | retrieval | implemented_adapter |
| `builtin.browser_operator` | 浏览器自动化模块 | 31 | browser_plan | implemented_adapter |
| `builtin.local_model_runtime` | 本地模型运行模块 | 9 | model_runtime | planned |
| `builtin.prompt_skill_engine` | Prompt 技能引擎模块 | 7 | prompt_template | planned |
| `builtin.agent_runtime_core` | 通用 Agent Runtime 模块 | 5 | agent_plan | planned |
| `builtin.eval_benchmark` | 评估与基准模块 | 4 | evaluation | planned |
| `builtin.workflow_orchestrator` | 工作流编排模块 | 3 | workflow_plan | planned |
| `builtin.artifact_report_engine` | 产物与报告生成模块 | 1 | report_generation | planned |
| `builtin.security_sandbox` | 安全沙箱与策略模块 | 1 | policy_gate | planned |
| `builtin.ui_desktop_operator` | 桌面 UI 操作模块 | 1 | ui_binding | planned |

---

## Skill Tag Distribution

| Tag | Count |
|---|---:|
| agent_runtime | 287 |
| code_agent | 108 |
| mcp_tool | 92 |
| python | 63 |
| prompt_framework | 58 |
| local_model | 56 |
| memory | 47 |
| ui_component | 43 |
| general_skill | 38 |
| workflow | 34 |
| browser_agent | 33 |
| claude_code | 33 |
| typescript | 30 |
| llm | 22 |
| ai | 20 |
| claude | 19 |
| agent | 19 |
| agent_skills | 18 |
| ai_agents | 16 |
| javascript | 15 |

---

## Demo Prompts

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
- private local AI workspace
- enterprise local deployment
- offline model pack
- deeper builtin adapters
- workflow orchestration
- desktop operations console
- auditable AI execution environment

---

## One-line Summary

Local AI Platform is a local-first AI Agent workspace with 338 skill assets, 12 builtin capability modules, code execution, memory retrieval, browser research, approval gates, and auditable runtime execution.
