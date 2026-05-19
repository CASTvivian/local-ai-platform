# 本地 AI 智能体平台：项目状态与能力清单

## 当前阶段结论

本项目已经完成核心智能体架构建设，并进入产品化验收与演示打磨阶段。

当前平台已经具备完整的本地 AI Agent 工作链路：

```text
用户任务
  → 智能体规划
  → 能力匹配
  → 工具执行
  → 任务状态追踪
  → 权限审批
  → 结果渲染
  → 审计记录
```

## 项目进度

| 项目 | 状态 |
|---|---|
| 核心 Agent 架构 | 已完成 |
| 能力对齐审计 | 14 covered / 0 partial / 0 gap |
| 高优缺口 | 0 |
| 自有 builtin 模块 | 12 个 |
| 内置技能资产 | 338 个 |
| 已启用技能 | 338 个 |
| 执行合约 | 12 个 |
| 源能力逻辑保留 | 274 条 |
| Mac 桌面包 | 已完成 |
| Windows MSI 包 | 已完成构建，待实机 smoke |
| 当前阶段 | 产品化验收 / 离线包 / 路演体验打磨 |

## 准确定性

### 可以对外表达为

本地 AI 智能体平台已经完成核心架构建设，具备本地模型、智能体规划、工具执行、代码处理、本地知识、浏览器研究、权限审批、技能商店和审计追踪等完整能力，当前进入产品化验收阶段。

### 不建议对外表达为

源码逐行一致，或所有实际体验已经全面超越市场成熟产品。

### 更准确的表述是

核心能力链路已经完成，并在本地化、自有技能体系、权限审批、审计追踪和桌面交付方向具备进一步超越的基础。

## 当前核心能力

### 本地模型运行

- 本地模型网关与健康检查
- 模型 profile 管理
- 轻量模型与代码模型切换
- 本地运行时自动启动
- 离线模型包扩展接口

### 智能体规划

- Schema-driven planner
- 结构化 tool selection
- builtin capability 匹配
- execution contract 识别
- agentic loop: plan → act → observe → validate → replan

### 代码智能体

- 工作区文件读取
- patch / diff 生成
- build / test / repair loop
- task run 状态追踪
- 高危写入动作 approval gate
- 审计记录输出

### 本地知识与记忆

- Repo Memory 检索
- RAG 证据归一化
- 技能上下文召回
- 项目资料查询
- 结果摘要与审计

### 浏览器研究

- 浏览器/网页研究计划
- Web 搜索
- findings / citations 结构化
- URL fetch 扩展基础
- 研究任务审计

### 工具系统

- Executor tool registry
- MCP tool hub 基础
- 工具 schema 注册
- builtin adapter 注册
- 未知工具安全失败

### 权限与安全

- 交互式 approval request
- pending / approved / rejected / cancelled 状态
- 高危工具执行前审批
- 审批审计
- sandbox policy 基础

### 桌面端与交付

- Mac 桌面包
- Windows MSI 包
- 本地服务自动启动
- 运行状态检查
- 技能商店展示
- 本地诊断面板


## 12 个自有 Builtin 能力模块

| Builtin 模块 | 定位 | 引用技能/能力数 | 核心逻辑条目 | 执行模式 | 状态 |
|---|---|---:|---:|---|---|
| `builtin.code_agent_core` | 代码智能体核心模块 | 103 | 485 | workspace_agent | implemented_adapter |
| `builtin.mcp_tool_hub` | MCP 工具协议模块 | 73 | 294 | tool_registry | planned |
| `builtin.memory_rag_core` | 记忆与 RAG 检索模块 | 36 | 226 | retrieval | implemented_adapter |
| `builtin.browser_operator` | 浏览器自动化模块 | 31 | 167 | browser_plan | implemented_adapter |
| `builtin.local_model_runtime` | 本地模型运行模块 | 9 | 62 | model_runtime | planned |
| `builtin.prompt_skill_engine` | Prompt 技能引擎模块 | 7 | 25 | prompt_template | planned |
| `builtin.agent_runtime_core` | 通用 Agent Runtime 模块 | 5 | 12 | agent_plan | planned |
| `builtin.eval_benchmark` | 评估与基准模块 | 4 | 42 | evaluation | planned |
| `builtin.workflow_orchestrator` | 工作流编排模块 | 3 | 25 | workflow_plan | planned |
| `builtin.artifact_report_engine` | 产物与报告生成模块 | 1 | 2 | report_generation | planned |
| `builtin.security_sandbox` | 安全沙箱与策略模块 | 1 | 19 | policy_gate | planned |
| `builtin.ui_desktop_operator` | 桌面 UI 操作模块 | 1 | 2 | ui_binding | planned |

## 技能资产概览

平台当前内置 338 个技能资产，统一进入自有 builtin 能力体系，系统可根据用户任务自动进行能力匹配、上下文召回和执行合约选择。

### 标签分布 Top 30

| 标签 | 数量 |
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
| codex | 14 |
| skills | 13 |
| anthropic | 12 |
| ai_agent | 11 |
| mcp | 10 |
| shell | 10 |
| claude_skills | 10 |
| security | 9 |
| cli | 8 |
| agentic_ai | 8 |

### 语言分布 Top 20

| 语言 | 数量 |
|---|---:|
| Python | 126 |
| TypeScript | 62 |
| JavaScript | 28 |
| Shell | 16 |
| Java | 13 |
| None | 12 |
| HTML | 12 |
| Rust | 9 |
| Go | 7 |
| C++ | 5 |
| Jupyter Notebook | 4 |
| C# | 3 |
| Vue | 2 |
| PowerShell | 2 |
| Elixir | 1 |
| Swift | 1 |
| Objective-C | 1 |
| Kotlin | 1 |
| CSS | 1 |
| MDX | 1 |

## 当前可以演示的任务

### 1. 本地 AI 对话

**示例**：

> 你好，请用一句话介绍你自己

**能力链路**：

Agent Runtime → Model Gateway → 本地模型

### 2. 时间与基础工具

**示例**：

> 今天是几月几号，现在几点

**能力链路**：

Planner → time.now / time.date_math → Renderer

### 3. 本地项目知识查询

**示例**：

> 我们现在有哪些 Agent 和 MCP 相关技能

**能力链路**：

Planner → capability.match → memory_rag_core / repo_memory → evidence summary

### 4. 代码智能体任务

**示例**：

> 请用代码智能体检查项目文件并生成 patch

**能力链路**：

Planner
  → builtin.code_agent_core.execute
  → approval gate
  → workspace patch
  → build/test/repair
  → task_state
  → audit

### 5. 浏览器研究任务

**示例**：

> 帮我做浏览器自动化和网页研究

**能力链路**：

Planner
  → builtin.browser_operator.execute
  → browser/research action plan
  → findings / citations
  → audit

### 6. 权限审批流程

**示例**：

> 执行会修改本地文件的高危代码任务

**能力链路**：

高危工具
  → approval request
  → pending
  → approved / rejected
  → executor continue / block

### 7. 技能商店

**能力**：

- 展示全部内置技能
- 按标签筛选
- 搜索技能
- 查看技能来源能力与模块归属
- 与 planner/capability registry 联动

## 产品化待办

| 事项 | 状态 |
|---|---|
| Windows 实机 smoke | 待执行 |
| 离线模型包 | 待制作 |
| 更多 builtin adapter 深化 | 进行中 |
| 桌面端 UI/UX 打磨 | 进行中 |
| 路演脚本与演示数据 | 待整理 |
| 企业部署文档 | 待整理 |

## 一句话介绍

本地 AI 智能体平台是一套可在本地机器运行、具备 338 个内置技能资产、支持代码智能体、本地知识、浏览器研究、任务规划、权限审批和审计追踪的私有化 AI Agent 工作平台。
