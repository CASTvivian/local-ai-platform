# Missing Repo Summary Source: multica-ai/multica

- URL: https://github.com/multica-ai/multica
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/multica-ai__multica
- Clone Status: cloned
- Language: TypeScript
- Stars: 27728
- Topics: 
- Description: The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="docs/assets/banner.jpg" alt="Multica — humans and agents, side by side" width="100%">
</p>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/logo-light.svg">
  <img alt="Multica" src="docs/assets/logo-light.svg" width="50">
</picture>

# Multica

**Your next 10 hires won't be human.**

The open-source managed agents platform.<br/>
Turn coding agents into real teammates — assign tasks, track progress, compound skills.

[![CI](https://github.com/multica-ai/multica/actions/workflows/ci.yml/badge.svg)](https://github.com/multica-ai/multica/actions/workflows/ci.yml)
[![GitHub stars](https://img.shields.io/github/stars/multica-ai/multica?style=flat)](https://github.com/multica-ai/multica/stargazers)

[Website](https://multica.ai) · [Cloud](https://multica.ai) · [X](https://x.com/MulticaAI) · [Self-Hosting](SELF_HOSTING.md) · [Contributing](CONTRIBUTING.md)

**English | [简体中文](README.zh-CN.md)**

</div>

## What is Multica?

Multica turns coding agents into real teammates. Assign issues to an agent like you'd assign to a colleague — they'll pick up the work, write code, report blockers, and update statuses autonomously.

No more copy-pasting prompts. No more babysitting runs. Your agents show up on the board, participate in conversations, and compound reusable skills over time. Think of it as open-source infrastructure for managed agents — vendor-neutral, self-hosted, and designed for human + AI teams. Works with **Claude Code**, **Codex**, **GitHub Copilot CLI**, **OpenClaw**, **OpenCode**, **Hermes**, **Gemini**, **Pi**, **Cursor Agent**, **Kimi**, and **Kiro CLI**.

<p align="center">
  <img src="docs/assets/hero-screenshot.png" alt="Multica board view" width="800">
</p>

## Why "Multica"?

Multica — **Mul**tiplexed **I**nformation and **C**omputing **A**gent.

The name is a nod to Multics, the pioneering operating system of the 1960s that introduced time-sharing — letting multiple users share a single machine as if each had it to themselves. Unix was born as a deliberate simplification of Multics: one user, one task, one elegant philosophy.

We think the same inflection is happening again. For decades, software teams have been single-threaded — one engineer, one task, one context switch at a time. AI agents change that equation. Multica brings time-sharing back, but for an era where the "users" multiplexing the system are both humans and autonomous agents.

In Multica, agents are first-class teammates. They get assigned issues, report progress, raise blockers, and ship code — just like their human colleagues. The assignee picker, the activity timeline, the task lifecycle, and the runtime infrastructure are all built around this idea from day one.

Like Multics before it, the bet is on multiplexing: a small team shouldn't feel small. With the right system, two engineers and a fleet of agents can move like twenty.

## Features

Multica manages the full agent lifecycle: from task assignment to execution monitoring to skill reuse.

- **Agents as Teammates** — assign to an agent like you'd assign to a colleague. They have profiles, show up on the board, post comments, create issues, and report blockers proactively.
- **Autonomous Execution** — set it and forget it. Full task lifecycle management (enqueue, claim, start, complete/fail) with real-time progress streaming via WebSocket.
- **Reusable Skills** — every solution becomes a reusable skill for the whole team. Deployments, migrations, code reviews — skills compound your team's capabilities over time.
- **Unified Runtimes** — one dashboard for all your compute. Local daemons and cloud runtimes, auto-detection of available CLIs, real-time monitoring.
- **Multi-Workspace** — organize work across teams with workspace-level isolation. Each workspace has its own agents, issues, and settings.

---

## Quick Install

### macOS / Linux (Homebrew - recommended)

```bash
brew install multica-ai/tap/multica
```

Use `brew upgrade multica-ai/tap/multica` to keep the CLI current.

### macOS / Linux (install script)

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
```

Use this if Homebrew is not available. The script installs the Multica CLI on macOS and Linux by using Homebrew when it is on `PATH`, otherwise it downloads the binary directly.

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
```

Then configure, authenticate, and start the daemon in one command:

```bash
multica setup          # Connect to Multica Cloud, log in, start daemon
```

> **Self-hosting?** Add `--with-server` to deploy a full Multica server on your machine:
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server
> multica setup self-host
> ```
>
> This pulls the official Multica images from GHCR (latest stable by default). Requires Docker. See the [Self-Hosting Guide](SELF_HOSTING.md) for details.
> If the selected GHCR tag has not been published yet, fall back to `make selfhost-build` from a checkout.

---

## Getting Started

### 1. Set up and start the daemon

```bash
multica setup           # Configure, authenticate, and start the daemon
```

The daemon runs in the background and auto-detects agent CLIs (`claude`, `codex`, `copilot`, `openclaw`, `opencode`, `hermes`, `gemini`, `pi`, `cursor-agent`, `kimi`, `kiro-cli`) on your PATH.

### 2. Verify your runtime

Open your workspace in the Multica web app. Navigate to **Settings → Runtimes** — you should see your machine listed as an active **Runtime**.

> **What is a Runtime?** A Runtime is a compute environment that can execute agent tasks. It can be your local machine (via the daemon) or a cloud instance. Each runtime reports which agent CLIs are available, so Multica knows where to route work.

### 3. Create an agent

Go to **Settings → Agents** and click **New Agent**. Pick the runtime you just connected and choose a provider (Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, or Kiro CLI). Give your agent a name — this is how it will appear on the board, in comments, and in assignments.

### 4. Assign your first task

Create an issue from the board (or via `multica issue create`), then assign it to your new agent. The agent will automatically pick up the task, execute it on your runtime, and report progress — just like a human teammate.

---

## Multica vs Paperclip

| | Multica | Paperclip |
|---|---------|-----------|
| **Focus** | Team AI agent collaboration platform | Solo AI agent company simulator |
| **User model** | Multi-user teams with roles & permissions | Single board operator |
| **Agent interaction** | Issues + Chat conversations | Issues + Heartbeat |
| **Deployment** | Cloud-first | Local-first |
| **Management depth** | Lightweight (Issues / Projects / Labels) | Heavy governance (Org chart / Approvals / Budgets) |
| **Extensibility** | Skills system | Skills + Plugin system |

**TL;DR — Multica is built for teams that want to collaborate with AI agents on real projects together.**

---

## CLI

The `multica` CLI connects your local machine to Multica — authenticate, manage workspaces, and run the agent daemon.

| Command | Description |
|---------|-------------|
| `multica login` | Authenticate (opens browser) |
| `multica daemon start` | Start the local agent runtime |
| `multica daemon status` | Check daemon status |
| `multica setup` | One-command setup for Multica Cloud (configure + login + start daemon) |
| `multica setup self-host` | Same, but for self-hosted deployments |
| `multica issue list` | List issues in your workspace |
| `multica issue create` | Create a new issue |
| `multica update` | Update to the latest version |

See the [CLI and Daemon Guide](CLI_AND_DAEMON.md) for the full command reference.

---

## Architecture

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Next.js    │────>│  Go Backend  │────>│   PostgreSQL     │
│   Frontend   │<────│  (Chi + WS)  │<────│   (pgvector)     │
└──────────────┘     └──────┬───────┘     └──────────────────┘
                            │
                     ┌──────┴───────┐
                     │ Agent Daemon │  runs on your machine
                     └──────────────┘  (Claude Code, Codex, GitHub Copilot CLI,
                                        OpenCode, OpenClaw, Hermes, Gemini,
                                        Pi, Cursor Agent, Kimi, Kiro CLI)
```

| Layer | Stack |
|-------|-------|
| Frontend | Next.js 16 (App Router) |
| Backend | Go (Chi router, sqlc, gorilla/websocket) |
| Database | PostgreSQL 17 with pgvector |
| Agent Runtime | Local daemon executing Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, or Kiro CLI |

## Development

For contributors working on the Multica codebase, see the [Contributing Guide](CONTRIBUTING.md).

**Prerequisites:** [Node.js](https://nodejs.org/) v20+, [pnpm](https://pnpm.io/) v10.28+, [Go](https://go.dev/) v1.26+, [Docker](https://www.docker.com/)

```bash
make dev
```

`make dev` auto-detects your environment (main checkout or worktree), creates the env file, installs dependencies, sets up the database, runs migrations, and starts all services.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full development workflow, worktree support, testing, and troubleshooting.


# FILE: README.zh-CN.md

<p align="center">
  <img src="docs/assets/banner.jpg" alt="Multica — 人类与 AI，并肩前行" width="100%">
</p>

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/logo-light.svg">
  <img alt="Multica" src="docs/assets/logo-light.svg" width="50">
</picture>

# Multica

**你的下一批员工，不是人类。**

开源的 Managed Agents 平台。<br/>
将编码 Agent 变成真正的队友——分配任务、跟踪进度、积累技能。

[![CI](https://github.com/multica-ai/multica/actions/workflows/ci.yml/badge.svg)](https://github.com/multica-ai/multica/actions/workflows/ci.yml)
[![GitHub stars](https://img.shields.io/github/stars/multica-ai/multica?style=flat)](https://github.com/multica-ai/multica/stargazers)

[官网](https://multica.ai) · [云服务](https://multica.ai) · [X](https://x.com/MulticaAI) · [自部署指南](SELF_HOSTING.md) · [参与贡献](CONTRIBUTING.md)

**[English](README.md) | 简体中文**

</div>

## Multica 是什么？

Multica 将编码 Agent 变成真正的队友。像分配给同事一样分配给 Agent——它们会自主接手工作、编写代码、报告阻塞问题、更新状态。

不再需要复制粘贴 prompt，不再需要盯着运行过程。你的 Agent 出现在看板上、参与对话、随着时间积累可复用的技能。可以理解为开源的 Managed Agents 基础设施——厂商中立、可自部署、专为人类 + AI 团队设计。支持 **Claude Code**、**Codex**、**GitHub Copilot CLI**、**OpenClaw**、**OpenCode**、**Hermes**、**Gemini**、**Pi**、**Cursor Agent**、**Kimi** 和 **Kiro CLI**。

<p align="center">
  <img src="docs/assets/hero-screenshot.png" alt="Multica 看板视图" width="800">
</p>

## 为什么叫 "Multica"？

Multica——**Mul**tiplexed **I**nformation and **C**omputing **A**gent。

这个名字是在向 20 世纪 60 年代具有开创意义的操作系统 Multics 致意。Multics 首创了分时系统，让多个用户能够共享同一台机器，同时又像各自独占它一样使用。Unix 则是在有意简化 Multics 的基础上诞生的，强调一个用户、一个任务、一种优雅的哲学。

我们认为，类似的转折点正在再次出现。几十年来，软件团队一直处于一种单线程的工作模式，一个工程师处理一个任务，一次只专注于一个上下文。AI agents 改变了这个等式。Multica 将"分时"重新带回这个时代，只不过今天在系统中进行多路复用的"用户"，既包括人类，也包括自主代理。

在 Multica 中，agents 是一级团队成员。它们会被分配 issue，汇报进展，提出阻塞，并交付代码，就像人类同事一样。任务分配、活动时间线、任务生命周期，以及运行时基础设施，Multica 从第一天起就是围绕这一理念构建的。

和当年的 Multics 一样，这一判断建立在"多路复用"之上。一个小团队不该因为人数少就显得能力有限。有了合适的系统，两名工程师加上一组 agents，就能发挥出二十人团队的推进速度。

## 功能特性

Multica 管理完整的 Agent 生命周期：从任务分配到执行监控再到技能复用。

- **Agent 即队友** — 像分配给同事一样分配给 Agent。它们有个人档案、出现在看板上、发表评论、创建 Issue、主动报告阻塞问题。
- **自主执行** — 设置后无需管理。完整的任务生命周期管理（排队、认领、执行、完成/失败），通过 WebSocket 实时推送进度。
- **可复用技能** — 每个解决方案都成为全团队可复用的技能。部署、数据库迁移、代码审查——技能让团队能力随时间持续增长。
- **统一运行时** — 一个控制台管理所有算力。本地 daemon 和云端运行时，自动检测可用 CLI，实时监控。
- **多工作区** — 按团队组织工作，工作区级别隔离。每个工作区有独立的 Agent、Issue 和设置。

---

## 快速安装

### macOS / Linux（推荐 Homebrew）

```bash
brew install multica-ai/tap/multica
```

后续可用 `brew upgrade multica-ai/tap/multica` 更新 CLI。

### macOS / Linux（安装脚本）

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
```

如果没有 Homebrew，可以使用安装脚本。脚本会安装 Multica CLI：检测到 `brew` 时通过 Homebrew 安装，否则直接下载二进制。

### Windows (PowerShell)

```powershell
irm https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.ps1 | iex
```

安装完成后，一条命令完成配置、认证和启动：

```bash
multica setup          # 连接 Multica Cloud，登录，启动 daemon
```

> **自部署？** 加上 `--with-server` 在本地部署完整的 Multica 服务：
>
> ```bash
> curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash -s -- --with-server
> multica setup self-host
> ```
>
> 需要 Docker。详见 [自部署指南](SELF_HOSTING.md)。

---

## 快速上手

安装好 CLI（或注册 [Multica 云服务](https://multica.ai)）后，按以下步骤将第一个任务分配给 Agent：

### 1. 配置并启动 daemon

```bash
multica setup           # 配置、认证、启动 daemon（一条命令搞定）
```

daemon 在后台运行，保持你的机器与 Multica 的连接。它会自动检测 PATH 中可用的 Agent CLI（`claude`、`codex`、`copilot`、`openclaw`、`opencode`、`hermes`、`gemini`、`pi`、`cursor-agent`、`kimi`、`kiro-cli`）。

### 2. 确认运行时已连接

在 Multica Web 端打开你的工作区，进入 **设置 → 运行时（Runtimes）**，你应该能看到你的机器已作为一个活跃的 **Runtime** 出现在列表中。

> **什么是 Runtime（运行时）？** Runtime 是可以执行 Agent 任务的计算环境。它可以是你的本地机器（通过 daemon 连接），也可以是云端实例。每个 Runtime 会上报可用的 Agent CLI，Multica 据此决定将任务路由到哪里执行。

### 3. 创建 Agent

进入 **设置 → Agents**，点击 **新建 Agent**。选择你刚连接的 Runtime，选择 Provider（Claude Code、Codex、GitHub Copilot CLI、OpenClaw、OpenCode、Hermes、Gemini、Pi、Cursor Agent、Kimi 或 Kiro CLI），并为 Agent 起个名字——它将以这个名字出现在看板、评论和任务分配中。

### 4. 分配你的第一个任务

在看板上创建一个 Issue（或通过 `multica issue create` 命令创建），然后将其分配给你的新 Agent。Agent 会自动接手任务、在你的 Runtime 上执行、并实时汇报进度——就像一个真正的队友一样。

大功告成！你的 Agent 现在是团队的一员了。 🎉

---

## Multica vs Paperclip

| | Multica | Paperclip |
|---|---------|-----------|
| **定位** | 团队 AI Agent 协作平台 | 个人 AI Agent 公司模拟器 |
| **用户模型** | 多人团队，角色权限 | 单人 Board Operator |
| **Agent 交互** | Issue + Chat 对话 | Issue + Heartbeat |
| **部署** | 云端优先 | 本地优先 |
| **管理深度** | 轻量（Issue / Project / Labels） | 重度（组织架构 / 审批 / 预算） |
| **扩展** | Skills 系统 | Skills + 插件系统 |

**简单来说：Multica 专为团队协作打造，让团队和 AI Agent 一起高效完成项目。**

## 架构

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│   Next.js    │────>│  Go 后端     │────>│   PostgreSQL     │
│   前端       │<────│  (Chi + WS)  │<────│   (pgvector)     │
└──────────────┘     └──────┬───────┘     └──────────────────┘
                            │
                     ┌──────┴───────┐
                     │ Agent Daemon │  运行在你的机器上
                     └──────────────┘  （Claude Code、Codex、GitHub Copilot CLI、
                                        OpenCode、OpenClaw、Hermes、Gemini、
                                        Pi、Cursor Agent、Kimi、Kiro CLI）
```

| 层级 | 技术栈 |
|------|--------|
| 前端 | Next.js 16 (App Router) |
| 后端 | Go (Chi router, sqlc, gorilla/websocket) |
| 数据库 | PostgreSQL 17 with pgvector |
| Agent 运行时 | 本地 daemon 执行 Claude Code、Codex、GitHub Copilot CLI、OpenClaw、OpenCode、Hermes、Gemini、Pi、Cursor Agent、Kimi 或 Kiro CLI |

## 开发

参与 Multica 代码贡献，请参阅 [贡献指南](CONTRIBUTING.md)。

**环境要求：** [Node.js](https://nodejs.org/) v20+, [pnpm](https://pnpm.io/) v10.28+, [Go](https://go.dev/) v1.26+, [Docker](https://www.docker.com/)

```bash
pnpm install
cp .env.example .env
make setup
make start
```

完整的开发流程、worktree 支持、测试和问题排查请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 开源协议

[Apache 2.0](LICENSE)


# FILE: docs/product-overview.md

# Multica 产品全景文档

> **文档说明**
>
> 这份文档的目的是：**让任何没有写过代码的新同事，在 30 分钟内完全理解 Multica 这个产品到底有哪些功能、每个功能在整体中处于什么位置、一个功能和另一个功能如何协同**。
>
> 它的受众包括：
>
> - **新加入的工程师 / 产品 / 设计 / 运营**——用它做 onboarding 的第一份材料
> - **产品介绍工作**——需要对外讲解 Multica 时的事实基础
> - **文案工作者**——写交互文案、营销文案、帮助文档时，需要知道某个词（比如 "Skill"、"Runtime"、"Autopilot"）在产品体系里代表什么
> - **任何需要在修改某个局部前，先理解它与整体关系的人**
>
> 它**不是**：开发者文档、架构决策记录（ADR）、或者销售话术。它是**功能事实的汇总**——每一条描述都能在代码、schema 或 API 里找到对应。
>
> 文档基于对整个 monorepo（server、apps、packages、migrations、daemon、CLI）的系统性调研生成，数据截止日期 2026-04-21。

---

## 目录

1. [Multica 是什么](#1-multica-是什么)
2. [核心概念词典](#2-核心概念词典)
3. [功能全景（按模块）](#3-功能全景按模块)
   - 3.1 [Workspace 工作区](#31-workspace-工作区)
   - 3.2 [Issue 议题管理](#32-issue-议题管理)
   - 3.3 [Project 项目](#33-project-项目)
   - 3.4 [Agent 智能体](#34-agent-智能体)
   - 3.5 [Runtime 运行时 & Daemon 守护进程](#35-runtime-运行时--daemon-守护进程)
   - 3.6 [Skill 技能](#36-skill-技能)
   - 3.7 [Autopilot 自动驾驶](#37-autopilot-自动驾驶)
   - 3.8 [Chat 对话](#38-chat-对话)
   - 3.9 [Inbox 收件箱与通知](#39-inbox-收件箱与通知)
   - 3.10 [成员、邀请与权限](#310-成员邀请与权限)
   - 3.11 [搜索与命令面板](#311-搜索与命令面板)
   - 3.12 [认证、登录与 Onboarding](#312-认证登录与-onboarding)
   - 3.13 [设置与个人资料](#313-设置与个人资料)
   - 3.14 [CLI 命令行工具](#314-cli-命令行工具)
4. [系统架构全景](#4-系统架构全景)
5. [产品地图（全部路由）](#5-产品地图全部路由)
6. [跨平台差异：Web vs 桌面](#6-跨平台差异web-vs-桌面)
7. [附录：关键数据表速查](#7-附录关键数据表速查)

---

## 1. Multica 是什么

### 一句话定位

**Multica 把编码智能体变成真正的团队成员。**

像给同事分配任务一样，把一个 issue 指派给一个 agent，它会自己认领、写代码、汇报进度、更新状态——不需要你一直守着。

### 解决的问题

传统方式用 AI coding agent 的痛点：

- 每次都要复制粘贴 prompt
- 必须盯着终端，看它跑不跑得完
- 没有跨任务的记忆，每次都从零开始
- 多个 agent 同时工作时，没有一个"看板"能看到全局

Multica 做的事：

- Agent 和人**共用同一个任务看板**（issue board）
- Agent **有 profile**，会出现在 assignee 下拉里、会在评论区发言、会自己创建 issue
- 同一个 (agent, issue) 的多轮对话**自动恢复会话**——上一次的上下文、工作目录都保留
- **Skill 系统**让历史上解决过的问题沉淀成可复用的能力
- **Autopilot** 让 agent 按定时规则自动开工（比如每天早上 9 点做 bug triage）

### 定位一句话版本

> Multica 不是一个 AI 工具，而是一个**人 + AI 协作的任务管理平台**。agent 是一等公民，和人在同一个工作流里。

### 部署形态

- **云版本（Multica Cloud）**：官方托管服务，agent 通过你本地跑的 daemon 执行
- **自托管（Self-Host）**：完整后端可以部署在自己的服务器
- **客户端**：Next.js web 版 + Electron 桌面版（两端体验基本一致，桌面独有：多标签、原生托盘、自动更新）

### 支持的 Coding Agent

Multica **不自己训模型**，也不锁定某一家厂商。它是调度器，本地 daemon 会自动探测以下 CLI 工具并接入：

Claude Code · Codex · OpenClaw · OpenCode · Hermes · Gemini · Pi · Cursor Agent · Kimi · Kiro CLI

每个 agent 可以配置自己的模型、API Key、环境变量、MCP 服务器。

---

## 2. 核心概念词典

**理解这些名词是理解产品的前提。每个概念的定义都严格对应数据库表。**

| 概念 | 定义 | 映射的数据表 |
|------|------|-------------|
| **User 用户** | 一个人类账号，可以登录，属于多个 workspace | `user` |
| **Workspace 工作区** | 一切资源的容器。issue、agent、project、skill 全部隔离在 workspace 里。就是 Linear/Notion 里的 workspace/team 概念 | `workspace` |
| **Member 成员** | 用户在某个 workspace 里的身份。一个用户在不同 workspace 可以有不同角色（owner/admin/member） | `member` |
| **Agent 智能体** | 可被指派任务的 AI 工作者。有 profile（名字、头像、说明）、会指定 runtime 和 provider、可以配自定义 prompt 和技能 | `agent` |
| **Runtime 运行时** | Agent 实际跑在哪里的**执行环境**。可以是用户本地机器（通过 daemon）或云端实例。**一个 runtime = 一台可以跑 agent 的机器** | `agent_runtime` |
| **Daemon 守护进程** | 用户本地运行的后台程序，自动发现已安装的 coding CLI 并注册为 runtime，然后不停轮询 server 认领任务 | （进程，不是表） |
| **Issue 议题** | 一个工作单元——任务、bug、feature。最核心的产品对象。可以分配给人或 agent | `issue` |
| **Comment 评论** | Issue 下的讨论回复。人和 agent 都能发。在评论里 `@某个 agent` 会自动触发这个 agent 的新任务 | `comment` |
| **Task 任务** | Agent 执行一次 issue 所产生的一次运行。本质是"一次 agent 跑起来的会话"。队列化执行 | `agent_task_queue` |
| **Skill 技能** | 工作区级别的可复用说明文档。作用是给 agent 提供"怎么做某件事"的上下文。Agent 开跑时会把挂载的 skill 内容注入到工作目录让 CLI 能读到 | `skill`, `skill_file`, `agent_skill` |
| **Project 项目** | 议题的高层归属，类似"里程碑"或"版本"。issue 可以归属到 project | `project` |
| **Autopilot 自动驾驶** | 定时或被触发的自动化规则。按 cron 或 webhook 触发，自动创建 issue 并分配给 agent | `autopilot`, `autopilot_trigger`, `autopilot_run` |
| **Chat 对话** | 用户和 agent 的持久化多轮对话。不依附于 issue | `chat_session`, `chat_message` |
| **Inbox 收件箱** | 个人通知中心。被 @、被分配、订阅的 issue 有更新都会进这里 | `inbox_item` |
| **Subscriber 订阅者** | 谁关注某个 issue。被分配、被 @、评论过都会自动订阅。订阅者会收到 inbox 通知 | `issue_subscriber` |
| **Activity 活动 / Timeline 时间线** | 所有关键动作的审计记录。issue 详情页的"时间线"就是这个表的数据 | `activity_log` |
| **Pin 固定** | 个人侧边栏快捷方式，把常用的 issue/project 置顶 | `pinned_item` |
| **Reaction 反应** | Issue 或评论上的 emoji 反应，跟 GitHub/Slack 一样 | `issue_reaction`, `comment_reaction` |
| **Attachment 附件** | Issue 或评论的文件上传，支持 S3/CloudFront 或本地存储 | `attachment` |
| **Personal Access Token (PAT)** | 用户级 API token，CLI 和自动化用。`mul_` 前缀 | `personal_access_token` |
| **Daemon Token** | 单 workspace 单 daemon 的 token。`mdt_` 前缀，比 PAT 权限范围更小 | `daemon_token` |
| **Session Resumption 会话恢复** | 同一对 (agent, issue) 的下一次任务会自动复用上次 Claude Code 的 `session_id` 和工作目录——历史对话、文件状态都保留 | `agent_task_queue.session_id`, `.work_dir` |
| **MCP (Model Context Protocol)** | Anthropic 提出的协议，让 agent 通过标准接口调用外部工具。每个 agent 可配自己的 MCP server 列表 | `agent.mcp_config` (JSONB) |
| **Workspace Context 工作区上下文** | 工作区级别的 agent 系统提示词。所有该工作区的 agent 都会感知到它 | `workspace.context` |
| **Polymorphic Actor 多态行动者** | 设计范式：几乎所有"谁做了什么"的字段都是 `actor_type` (`member`/`agent`) + `actor_id`。这就是为什么 agent 能像人一样创建 issue、发评论、被订阅 | 贯穿所有表 |

---

## 3. 功能全景（按模块）

### 3.1 Workspace 工作区

> **角色**：一切的容器。Multica 的多租户边界。

#### 功能

- **多工作区**：一个用户可以属于多个 workspace，每个 workspace 完全隔离（issue、agent、skill、成员都独立）。
- **创建工作区**：只需要一个名字；自动生成 slug（URL 中使用的短 ID）。
- **切换工作区**：侧边栏下拉；桌面端每个工作区有独立的标签组。
- **离开工作区**：非 owner 成员可自行离开。
- **删除工作区**：只有 owner 可以，硬删除+级联。
- **Workspace 设置**：名称、slug、描述、**Workspace Context**（给该工作区所有 agent 的统一系统提示）、**仓库列表**（workspace 允许 agent 访问的 Git 仓库 URL 白名单）。
- **Workspace 头像 / issue 前缀**：每个工作区可以有自己的 issue 编号前缀（如 `ACME-42`）。

#### 产品里的位置

Workspace 不是一个功能，而是**所有功能的坐标系**。URL 的形态永远是 `/{workspace-slug}/...`，API 请求永远带 `X-Workspace-Slug` 头。一个 issue、一个 agent、一个 skill，脱离了 workspace 就没有意义。

#### 对应表

`workspace`, `member`, `workspace_invitation`

---

### 3.2 Issue 议题管理

> **角色**：Multica 的核心工作对象。

Issue 对应的概念在 Linear 叫 Issue、在 Jira 叫 Ticket、在 GitHub 叫 Issue——就是一个任务单元。Multica 的特色在于**issue 可以分配给 agent，和分配给人完全对等**。

#### 核心字段

- 标题、描述（Tiptap 富文本）、状态、优先级
- 编号（自动递增，带 workspace 前缀）
- **Assignee（可以是 member 或 agent）**
- **Creator（可以是 member 或 agent）**——agent 也能创建 issue
- Parent issue（用来做子任务）
- Project（归属的项目）


# FILE: docs/codex-sandbox-troubleshooting.md

# Codex sandbox troubleshooting (macOS `no such host`)

This doc explains the failure mode that caused [MUL-963][mul-963] and the
matrix the daemon now follows when writing Codex's per-task `config.toml`.

[mul-963]: https://multica-api.copilothub.ai/issues/28c34ad2-102a-4f46-91ac-336ed78c5859

## Symptom fingerprint

| Error text                                                    | Likely cause                                                                    |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `dial tcp: lookup HOST: no such host`                         | **Codex Seatbelt sandbox blocking DNS** (macOS, `workspace-write` mode). |
| `dial tcp IP:PORT: connect: connection refused`               | Server/daemon not running on that port (app-level, not sandbox).                |
| `dial tcp IP:PORT: i/o timeout`                               | Container-level network policy or firewall (not Codex sandbox).                 |
| `x509: certificate signed by unknown authority`               | TLS/CA issue, unrelated.                                                        |

If you see `no such host` *inside a Codex session on macOS* but `curl https://multica-api.copilothub.ai` from a plain shell on the same machine works, you are hitting the Seatbelt bug below.

## Root cause

Upstream issue: [openai/codex#10390][codex-10390]. On macOS, Codex's Seatbelt
profile for `sandbox_mode = "workspace-write"` silently ignores the
`[sandbox_workspace_write] network_access = true` setting. The seatbelt
policy hard-codes `CODEX_SANDBOX_NETWORK_DISABLED=1`, which blocks DNS/UDP
syscalls. Go's `net.LookupHost` surfaces that as `no such host`.

Linux (Landlock) is **not** affected — only macOS Seatbelt.

[codex-10390]: https://github.com/openai/codex/issues/10390

## What the daemon does now

The daemon writes a *multica-managed* block into each task's
`$CODEX_HOME/config.toml`, delimited by `# BEGIN multica-managed` /
`# END multica-managed` markers. Anything outside the markers is left
untouched so users can still tune Codex behavior.

Decision matrix (see [`server/internal/daemon/execenv/codex_sandbox.go`](../server/internal/daemon/execenv/codex_sandbox.go)):

| Host OS   | Codex version                                    | Managed block emits                                                       |
| --------- | ------------------------------------------------ | ------------------------------------------------------------------------- |
| non-darwin | any                                              | `sandbox_mode = "workspace-write"` + `sandbox_workspace_write.network_access = true` (dotted-key form) |
| darwin    | ≥ `CodexDarwinNetworkAccessFixedVersion`         | same as above (upstream fix in effect)                                    |
| darwin    | older / unknown (current default)                | `sandbox_mode = "danger-full-access"` + warn-level log                     |

The managed block is always hoisted to the top of `config.toml` and uses
TOML dotted-key syntax rather than a `[sandbox_workspace_write]` section
header. Both are load-bearing: if the block sat after a user table like
`[permissions.multica]`, a bare `sandbox_mode = "..."` line would be parsed
as `permissions.multica.sandbox_mode` and Codex would silently ignore it.

`CodexDarwinNetworkAccessFixedVersion` is an empty string today, meaning *no
known fixed release yet*. Bump it once a tagged Codex release includes the
upstream fix.

When the daemon falls back to `danger-full-access`, it logs at `WARN`:

```
codex sandbox: falling back to danger-full-access on macOS
  reason=codex on macOS: seatbelt ignores sandbox_workspace_write.network_access (openai/codex#10390) ...
  codex_version=0.121.0
  hint=upgrade Codex CLI (e.g. `brew upgrade codex` or `npm i -g @openai/codex`) ...
  config_path=/.../codex-home/config.toml
```

## Quick self-check commands

From the host shell (outside the sandbox):

```bash
# Is the Multica API reachable at all?
curl -sSf https://multica-api.copilothub.ai/healthz
```

From inside a Codex session (after the daemon writes its config):

```bash
multica issue list --limit 1 --output json >/dev/null && echo OK
```

If the host curl works but the Codex-session call fails with `no such host`,
the sandbox is the culprit; confirm the daemon picked the right policy by
looking at the managed block in `$CODEX_HOME/config.toml`.

## Options and trade-offs

- **A. Domain-scoped `permissions` profile** (tight): when the upstream
  `network_access` fix is available, prefer writing a `permissions.multica`
  profile that allows only `multica-api.copilothub.ai` and
  `multica-static.copilothub.ai`. Keeps filesystem sandbox intact.
- **B. `danger-full-access`** (current macOS fallback): drops the whole
  Seatbelt profile. Simplest reliable workaround until the upstream fix is
  released.
- **C. Upgrade Codex CLI**: `brew upgrade codex` or `npm i -g @openai/codex`.
  Once a release containing [openai/codex#10390][codex-10390] is installed,
  bump `CodexDarwinNetworkAccessFixedVersion` in `codex_sandbox.go` and
  option A/the workspace-write path takes over automatically.

## If you need to hand-verify

```bash
# Inspect the managed block the daemon wrote for a given task.
sed -n '/# BEGIN multica-managed/,/# END multica-managed/p' \
  ~/multica_workspaces/$WORKSPACE_ID/$TASK_SHORT/codex-home/config.toml
```

The block is idempotent — re-running a task rewrites it in place.


# FILE: docs/docs-rewrite-plan.md

# Multica Docs 站重写规划（v2）

> **本规划是什么**：Multica 对外 doc 站（`apps/docs/`，Fumadocs + Next.js）的从零重写方案。它替换 v1 规划——v1 之前在代码调研之前写的，很多对概念的切分现在看是错的。
>
> **v2 的数据基础**：4 份并行 subagent 的代码级调研，覆盖 Workspace/Members/Issues/Projects、Agent/Runtime/Daemon/Tasks、Skill/MCP/Autopilot/Chat、Inbox/Realtime/Auth 四大领域。每一处涉及产品行为的陈述都能在代码里找到对应位置。
>
> **本文档语言**：中文（团队内部规划，你要逐篇 review）。
> **doc 站本身语言**：英文先行，中文作为 Phase 10 的 i18n。
>
> **风格目标**：排版/布局对标 Anthropic docs（奶油底、serif heading、宽松行距、窄行宽、深色代码块的灵魂），但**色板继续用 Multica 自己的 tokens**（冷蓝 brand）——visual 上是"Multica 色 + Anthropic 排版语法"。

---

## 一、产品定位（文档的落脚点）

Multica = **人 + AI agent 在同一个看板上协作的任务管理平台**。

这个定位决定了它的文档**和普通 SaaS 文档有三个不一样的地方**，贯穿全规划：

1. **术语负担重**。Workspace/Agent/Runtime/Daemon/Skill/Autopilot/MCP/Trigger/Session Resumption——对新用户**没有一个是 obvious** 的。**Concepts 是文档第一支柱**。
2. **分布式执行架构要讲透**。Server 不跑 agent，agent 跑在用户本地的 daemon 上——这是所有"我的 agent 怎么不工作"问题的根源。Architecture Overview 要早出现。
3. **文档也被 agent 读**。现有 `cloud-quickstart.mdx` 已经有"把这段指令给你的 agent，让它自己按文档安装"的模式——意味着文档**要能被 agent 跟着做**：每一步命令要完整、可执行、独立（不能"把上面那个替换一下"）。这直接影响 code block 写法。

---

## 二、读者画像（按优先级排）

| 优先级 | 读者 | 关心什么 |
|---|---|---|
| P0 | **新用户 / Evaluator** | "这是啥？5 分钟跑起来" |
| P0 | **自托管运维 (DevOps)** | "怎么部署？资源要多少？出问题怎么查？" |
| P1 | **团队管理员 / Workspace owner** | "怎么配 agent？管权限？设 autopilot？" |
| P1 | **重度 CLI / 开发者用户** | "CLI 全集？直接调 API？" |
| P2 | **Agent 本身** | "这个命令怎么用？这个概念是什么？" |
| ✗ | OSS 贡献者 | 暂不做 —— 用 `CONTRIBUTING.md` 顶着 |

> **关键**：P2 的 agent 不会逛导航，只会被人类用 `Fetch https://docs.multica.ai/...` 指向某一页。所以每一页都要**自包含**。

---

## 三、设计原则

1. **Concepts First, Tasks Second**。先建立词汇表，再讲操作。
2. **每个概念独立讲透，不合并糊弄**。宁可多一页也不要把 MCP 塞进 Agents 糊弄过去。
3. **「入口」概念独立于「对象」概念**。Trigger 不是 Task 的属性——它是跨入口的共通机制，值得自己一页。
4. **每篇 < 8 分钟读完**。Concept 页可以稍长，Guide/Reference 页聚焦单一主题。
5. **命令块可独立复制运行**——不写"把上面那个改成 XXX"，这对 agent 读者不友好。
6. **版本敏感的事实用代码注释标记来源**——比如"支持的 agent provider"列表，来自哪个文件，后期可以做成自动扫描。

---

## 四、信息架构（v2）

**六大板块，共 56 篇。**

### 板块 1. Introduction（2 篇）

让读者用 2 分钟理解这是什么产品。

| 篇目 | 核心内容 |
|---|---|
| **Welcome** | 定位 + 核心价值 + 一张架构图 + 3 种部署形态（Cloud / Self-Host / Desktop）导航 |
| **How Multica works** | 一张大图把 User / Issue / Agent / Runtime / Daemon / Skill / Task / Trigger 之间的关系串起来——目标是建立**正确心智模型**，而不是记名词 |

### 板块 2. Getting Started（3 篇）

| 篇目 | 核心内容 |
|---|---|
| **Cloud Quickstart** | 5 分钟：signup → install CLI → `multica setup` → 第一个 agent → 第一个 issue |
| **Self-Host Quickstart** | 10 分钟：`install.sh --with-server` → `multica setup self-host` |
| **Your first task** | 从 issue 创建 → assign 给 agent → 看 agent 流式工作 → review 结果（截图 + GIF） |

### 板块 3. Concepts（17 篇 —— 灵魂）

**每页统一模板**：What · Why it exists · How it connects · Related。

| # | 篇目 | 它回答的问题 | 代码事实高光 |
|---|---|---|---|
| 1 | **Workspaces** | 多租户边界；slug / issue prefix / issue_counter 管什么 | slug 正则 `^[a-z0-9]+(?:-[a-z0-9]+)*$`；issue number **per-workspace 自增**；硬删除级联 |
| 2 | **Members & Access** | owner/admin/member 3 级权限；邀请流程；角色约束 | **邀请不存在的邮箱会自动创建 user**（用 email 当名字）；每个 workspace 至少保留 1 个 owner |
| 3 | **Issues** | 最核心工作对象；polymorphic assignee（member 或 agent） | **分配给 agent 会自动入队 task**；private agent 只能被 owner/admin 分配；`acceptance_criteria`/`position`/`first_executed_at` 等字段在代码里**未实装**，不写进文档 |
| 4 | **Projects** | issue 容器；lead 可以是 agent | 非常薄（9 个字段）；删除 project 只是把 issue.project_id 设 NULL |
| 5 | **Agents** | AI 工作者身份；provider/instructions/custom_env/custom_args/model 分别影响什么 | **`custom_env` 在 DB 里明文存储，无加密**——醒目警告；archive 用 `archived_at` 软删除；API 响应对非 owner 做 redact |
| 6 | **Runtimes** | 一台机器 × 一个 provider 一行；注册/在线/离线生命周期 | **唯一约束 (workspace_id, daemon_id, provider)**——同一台机器同一 provider 不会有重复 runtime；daemon 重启复用旧 runtime 行 |
| 7 | **The Daemon** | 分布式执行的灵魂；poll + heartbeat + concurrent execution | 每 30s heartbeat；75s 无心跳 → 离线；启动时调 `recover-orphans` 回收孤儿任务；max_concurrent_tasks 有双层（daemon + agent） |
| 8 | **Tasks** | 任务是什么；生命周期 queued→dispatched→running→completed/failed | **session_id mid-flight pinning**（agent 首条 system message 一到就持久化，不等完成）；失败自动重试只对 issue-sourced 任务（max_attempts=3），chat 和 autopilot 不自动重试 |
| 9 | **Triggers & Entry Points** ← **独立页** | 5 种让 task 产生的入口：Assignment / Comment @mention / Chat / Autopilot / Rerun；每种的行为对比 | 每种的 FK 字段不同（trigger_comment_id / chat_session_id / autopilot_run_id）；**对比表**：哪种有 session resume / 自动重试 / priority 来源 / dedup |
| 10 | **Skills** | 工作区 skill + 本地 skill；按 provider 的注入路径 | 8 种 provider 有不同 skill 根路径（Claude=`.claude/skills/`、Codex=`$CODEX_HOME/skills/`、Pi=`.pi/skills/`、etc）；skill 不参与执行，只参与上下文注入 |
| 11 | **MCP** | 独立协议；怎么给 agent 配 MCP server；和 skill 的区别 | **目前只 Claude Code 真用**——其他 provider 收到 McpConfig 但 CLI 没对应 flag；JSONB 明文存储，非 owner redact |
| 12 | **Autopilots** | 让 agent 自动开工的调度器；两种执行模式；三种触发；并发策略 | **Webhook trigger 字段有但没接路由**——第一版不文档化；concurrency policy 只对 `run_only` 模式生效；`create_issue` 模式由 issue FSM 自然 gate |
| 13 | **Chat** | 和 issue comment 的区别；session 复用 | **完全沙盒**——chat 里的 agent 不能发 comment 到 issue；session_id 用 COALESCE 持久化，agent crash 不会抹掉 |
| 14 | **Inbox** | 个人通知中心；10 种通知类型 | **Agents 可以被加入 subscriber 表但永远收不到 inbox 通知**——`notifyIssueSubscribers` 显式过滤；mention dedup 只在单 event 内生效（一 comment 里 @alice 5 次 = 1 inbox） |
| 15 | **Subscriptions** | 谁会自动订阅；如何手动订阅 | **取消分配后旧 assignee 不会被取消订阅**；parent issue 冒泡只对 `status_changed` 生效 |
| 16 | **Authentication & Tokens** | 3 种凭证 + signup flow + OAuth | JWT cookie（30 天）/ PAT（`mul_` 前缀）/ Daemon Token（`mdt_` 前缀）；Daemon Token **不能命中 user-scoped 路由**；PAT 几乎什么都能命中；signup 白名单优先级：`ALLOWED_EMAILS` > `ALLOWED_EMAIL_DOMAINS` > `ALLOW_SIGNUP` |
| 17 | **Realtime & Events** | WebSocket hub + room model + 事件目录 | **40+ event types**（按命名空间分：issue:* / task:* / inbox:* / chat:* 等）；WS 是 **push-only**（client→server 走 HTTP）；room 按 workspace；inbox:* 用 SendToUser 定向推送 |

### 板块 4. Guides（12 篇，任务导向）

| 篇目 | 核心内容 |
|---|---|
| Assign an issue to an agent | UI + CLI 两种方式 |
| Create and configure an agent | provider、instructions、custom_env、mcp、skills |
| Connect a runtime (local daemon) | daemon install → login → start → 出现在 Runtimes 页 |
| Write and share a skill | 新建 / 编辑 / 挂载到 agent |
| Import a skill from GitH

# FILE: docs/analytics.md

# Product Analytics

This document is the source of truth for the analytics events Multica ships
to PostHog. Events feed the acquisition → activation → expansion funnel that
drives our weekly Active Workspaces (WAW) north-star metric.

See [MUL-1122](https://github.com/multica-ai/multica) for the design context.

## Configuration

All analytics shipping is toggled by environment variables (see `.env.example`):

| Variable | Meaning | Default |
|---|---|---|
| `POSTHOG_API_KEY` | PostHog project API key. Empty = no events are shipped. | `""` |
| `POSTHOG_HOST` | PostHog host (US or EU cloud, or self-hosted URL). | `https://us.i.posthog.com` |
| `ANALYTICS_ENVIRONMENT` | Optional override for the standard `environment` event property. Normalized to `production`, `staging`, or `dev`; defaults from `APP_ENV`. | `APP_ENV` / `dev` |
| `ANALYTICS_DISABLED` | Set to `true`/`1` to force the no-op client even when `POSTHOG_API_KEY` is set. | `""` |

Local dev and self-hosted instances run with `POSTHOG_API_KEY=""`, so **no
events leave the process unless the operator explicitly opts in**.

### Self-hosted instances

Self-hosters should **never inherit a Multica-issued `POSTHOG_API_KEY`** —
that would route their users' behavior to our analytics project. The
defaults guarantee this:

- `.env.example` ships `POSTHOG_API_KEY=` empty. The Docker self-host
  compose does not set a default either.
- With the key unset, `NewFromEnv` returns `NoopClient` and logs
  `analytics: POSTHOG_API_KEY not set, using noop client` at startup — a
  visible confirmation that nothing is shipped.
- Operators who want their own analytics can set `POSTHOG_API_KEY` and
  `POSTHOG_HOST` to point at their own PostHog project (Cloud or
  self-hosted PostHog).
- The frontend receives the key via `/api/config` (planned for PR 2), so
  self-hosts' blank server config also disables frontend event shipping
  automatically — no separate frontend opt-out plumbing required.

## Architecture

```
handler → analytics.Client.Capture(Event)   ← non-blocking, returns immediately
                    │
                    ▼
           bounded queue (1024 events)
                    │
                    ▼
     background worker: batch + POST /batch/
                    │
                    ▼
                PostHog
```

- `analytics.Capture` is **never allowed to block a request handler**. A
  broken backend must not degrade the product — when the queue is full,
  events are dropped and counted (visible via `slog` + the `dropped` counter
  on shutdown).
- Batches flush either when `BatchSize` is reached or every `FlushEvery`
  (default 10 s), whichever comes first.
- `Close()` drains remaining events during graceful shutdown. Called from
  `server/cmd/server/main.go` via `defer`.

## Identity model

- **`distinct_id`** — always the user's UUID for logged-in events. The
  frontend's `posthog.identify(user.id)` merges any prior anonymous events
  under the same identity, so acquisition attribution (UTM / referrer) stays
  intact across signup.
- **`workspace_id`** — added to every event as a property when present. v1
  uses event property filtering (free tier) rather than PostHog Groups
  Analytics (paid) to compute workspace-level metrics.
- **PII** — events carry `email_domain` (e.g. `gmail.com`), not the full
  email. Full email is stored once in person properties via `$set_once` so
  it's available for individual debugging but not broadcast with every
  event.
- **Person properties (`$set`)** — use for mutable cohort signals
  (role, use_case, team_size, platform_preference) that a user can
  legitimately change during onboarding. `Event.Set` on the backend
  maps to `$set`; the frontend helper is
  `setPersonProperties()` in `@multica/core/analytics`. Use
  `$set_once` only for values that must never be overwritten (email,
  initial attribution, first-completion timestamp).

## Taxonomy

Every event is assigned to one dashboard category:

| Category | Events |
|---|---|
| `core_loop` | `workspace_created`, `runtime_registered`, `runtime_ready`, `runtime_failed`, `runtime_offline`, `agent_created`, `issue_created`, `chat_message_sent`, `agent_task_queued`, `agent_task_dispatched`, `agent_task_started`, `agent_task_completed`, `agent_task_failed`, `agent_task_cancelled`, `autopilot_run_started`, `autopilot_run_completed`, `autopilot_run_failed` |
| `onboarding_support` | `onboarding_started`, `onboarding_questionnaire_submitted`, `onboarding_completed`, `onboarding_runtime_path_selected`, `onboarding_runtime_detected`, `starter_content_decided` |
| `acquisition` | `signup`, `download_intent_expressed`, `download_page_viewed`, `download_initiated`, `cloud_waitlist_joined` |
| `ops_feedback` | `feedback_opened`, `feedback_submitted` |
| `system/noise` | `$pageview`, `$set`, `$identify`, `$autocapture`, `$rageclick` |

The v0 core dashboard must use only `core_loop` plus the specific
`onboarding_support` steps used by the activation funnel. Acquisition,
feedback, and system/noise events stay in separate dashboards.

## Standard core properties

Canonical core events should carry these properties whenever the entity exists:

| Property | Type | Notes |
|---|---|---|
| `environment` | string | `production` / `staging` / `dev`; stamped by backend and frontend analytics clients. |
| `event_schema_version` | int | Current version: `2`. |
| `user_id` | string UUID | Human user ID when known. Agent/system events may omit it. |
| `workspace_id` | string UUID | Required for workspace-scoped events. |
| `agent_id` | string UUID | Required for agent/task events. |
| `task_id` | string UUID | Required for `agent_task_*` events. |
| `issue_id` / `chat_session_id` / `autopilot_run_id` | string UUID | Relevant source entity for the task/entry event. |
| `source` | string | Canonical values: `onboarding`, `manual`, `chat`, `autopilot`, `api`. UI surface details use `surface` or `trigger_source`. |
| `runtime_mode` | string | `cloud` / `local` when a runtime

# FILE: docs/docs-outline.md

# Multica Docs 执行大纲

> 这份是**执行文档 + 协作 tracker**。每篇文档都有独立条目，委派出去的人直接在对应条目里认领、更新状态。
>
> 战略思路（产品定位、读者画像、设计原则、视觉方向）保留在 [`docs-rewrite-plan.md`](./docs-rewrite-plan.md)。
>
> **语言**：只写中文版。英文版暂不做。
> **V1 目标**：25 篇覆盖所有核心功能。v2 留 24 篇深度/边缘内容 pending。

---

## 一、协作规则（接手任何一篇前必读）

### 1.1 写作守则（硬约束）

1. **源码优先**：每一条事实陈述必须能在源码里找到对应位置。不能从"产品宣传册"、"直觉"、"上一版本的文档"或"记忆"出发。
2. **代码里没有的功能一律不写**。即使 UI 疑似有、DB 有字段、handler 有接口但 service 层无真实读写逻辑，都视为"未实装"。遇到边界不确定的情况，标 ⚠️ 让 reviewer 再看一眼，不要硬写。
3. **下笔前先读源码验证本文件里的"写什么"清单**。这个清单是指引，不是真相。可能已过时、可能当时调研就不准。
4. **跨篇共通事实集中写**（例如 10 provider 矩阵写在 §4.3 Providers Matrix，其他篇 cross-link 过去），避免同一事实分散在多篇里。
5. **服务于产品定位**：Multica 的核心差异化是 **"BYO-agent 的 Linear—— agent 跑在你自己的机器，你掌控计算和 provider 选择"**。每篇的语气和深度都应该为这个叙事服务。
6. **为目标读者写**。不同读者期待不同深度。P0 新用户不关心 SQL 字段，P1 开发者愿意看架构图，P2 agent 读者需要命令自包含能复制。
7. **v1 认领优先**：先把 v1 的 25 篇 ship 出去，再开 v2。

### 1.2 目标读者分级

| 级别 | 读者 | 期待 |
|---|---|---|
| P0 | 新用户 / Evaluator | "这是啥？5 分钟跑起来" |
| P0 | 自托管运维 | "怎么部署？出问题怎么查？" |
| P1 | 团队管理员 / Workspace owner | "怎么配 agent？管权限？设 routines？" |
| P1 | 重度 CLI / 开发者用户 | "CLI 全集？架构细节？" |
| P2 | Agent 本身（被人类指向某页）| "每步命令要完整、可独立复制执行" |

### 1.3 状态码

- ⬜ Not started
- 🔍 Source research（正在读源码验证）
- ✍️ Drafting（正在写初稿）
- 👀 In review（待 review）
- ✅ Shipped

### 1.4 Flag（只在需要决策时填）

- 🤔 **Propose merge/drop** —— 认领后读源码发现这篇独立成页价值低，写一行理由，@ owner（Naiyuan）决策。

### 1.5 分工流程

1. **认领**：把 `Owner` 改成你的名字，`Status` 改成 🔍
2. **读源码**：用本条目的 "Source files" 作为起点，扩展看相关代码
3. **验证"写什么"清单**：发现过时/缺失/错误，直接改这个条目
4. **写初稿**：`Status` 改成 ✍️
5. **提 review**：`Status` 改成 👀，发消息 @ reviewer
6. **交付**：`Status` 改成 ✅

### 1.6 每篇目标字数

| 页面类型 | 字数范围 | 理由 |
|---|---|---|
| Concept 页（§2-§6 多数）| 800-1500 字 | 讲清一个概念 + 示例 + 关联 |
| Quickstart / Tutorial（§1.3-§1.4 / §2.1）| 500-1200 字 | 命令优先，解释从简 |
| Reference 页（§4.3 / §7-§8 多数）| 1000-2500 字 | 对照表 / env 清单 / 命令 cheatsheet，信息密度高 |
| Overview / Welcome（§1.1）| 300-600 字 | 定位 + 导航，不展开 |

**原则**：写到目标字数上限还没写完，说明该拆页或该压缩；写到下限还不够，说明内容薄，考虑合并。

### 1.7 Review Checklist（提 review 前自查）

- [ ] 每条事实陈述都能在 Source files 里找到对应代码位置
- [ ] 所有代码示例（shell / CLI）可以独立复制、独立运行（不依赖"把上面那个替换一下"）
- [ ] 术语和其他页一致：workspace / agent / runtime / daemon / task / skill / routine
- [ ] 所有 cross-link 指向的目标页存在（不是死链）
- [ ] 字数在目标范围内
- [ ] 本条目"不写"清单里的字段没被写进去
- [ ] 没有从记忆或旧文档复制过来的未验证事实

### 1.8 MDX 样例模板

> 这是 §2.3 Issues 的 mdx skeleton，用来统一标题层级 / callout / code block / cross-link 风格。所有 v1 文档按这个骨架写。

```mdx
---
title: Issues
description: Issue 是 Multica 的核心工作对象——人和 agent 都能被分配、评论、改状态。
---

# Issues

## 什么是 Issue

Issue 是 Multica 的核心工作对象……（1-2 段话说清楚"是什么"）

## 关键概念

### Polymorphic Assignee

Issue 的 assignee 可以是 member（人）或 agent。这是 Multica 和传统 task manager
最重要的区别——**agent 是 first-class assignee**。

<Callout type="info">
分配给 agent 会**立即**入队一个 task。详见 [Tasks](/docs/tasks)。
</Callout>

### 状态（Status）

| Status | 含义 | 默认 |
|---|---|---|
| backlog | 还没规划 | ✓ |
| todo | 准备开工 | |
| in_progress | 正在做 | |
| ... | ... | |

**注意**：状态转换无强制约束——任意状态可以直接互转。

## 操作

### 创建 Issue（CLI）

```bash
multica issue create \
  --title "Fix login bug" \
  --assignee @alice
```

### 分配给 Agent（触发自动执行）

```bash
multica issue assign <issue-id> --agent <agent-slug>
```

分配给 agent 时，Multica 会立刻入队一个 task 到对应 runtime。详见
[Assigning Issues to Agents](/docs/assign-agents)。

## 删除和级联

删除 issue 会级联删除：
- 所有评论 / reactions（硬删除）
- 该 issue 上 queued / dispatched 的 task（取消）
- 附件（异步清理 S3）

## Related

- [Comments](/docs/comments)
- [Projects](/docs/projects) —— Issue 的容器
- [Assigning Issues to Agents](/docs/assign-agents)
- [Tasks](/docs/tasks)
```

**关键约定**：

- **Callout**：`<Callout type="info|warning|tip">...</Callout>`。warning 用于陷阱（如固定测试验证码），info 用于补充说明，tip 用于最佳实践
- **代码块**：shell 命令用 \`\`\`bash；配置用 \`\`\`yaml / \`\`\`env；JSON 用 \`\`\`json
- **Cross-link**：用 markdown 链接 `[显示文字](/docs/page-slug)`，不要写成 "详见 Tasks 章节"
- **表格**：有 3 行以上对照才用表格，不要 1-2 行也用
- **标题层级**：H1 只能一个（等于页面 title），H2 是主要分段，H3 是小节

---

## 二、版本规划

### V1（25 篇，第一次 ship）

覆盖所有核心功能，让新用户能"5 分钟懂产品 + 10 分钟跑起来 + 30 分钟用上 agent"。

### V2（24 篇 Pending）

深度 reference / 开发者向 / 高级部署。等 v1 ship + 用户反馈后再补。

### V1 篇目清单

| 板块 | V1 篇数 | V2 推迟篇数 |
|---|---|---|
| 1. Welcome & Quickstart | 4 | 0 |
| 2. Workspace & Team | 4 | 0 |
| 3. Agents | 3 | 1（MCP）|
| 4. How Agents Run | 3 | 0 |
| 5. Working with Agents | 4 | 0 |
| 6. Staying Informed | 1 | 2（Subscriptions 合并 / Realtime）|
| 7. Administration | 3 | 5（Self-Host Overview / Docker Compose / Storage / Email / Upgrading / Signup Controls）|
| 8. Reference | 3 | 13（CLI 各子命令详细页）|
| **合计** | **25** | **24** |

---

## 三、大纲概览（v1 导航）

| # | 板块 | 定位 | 篇数 |
|---|---|---|---|
| 1 | [Welcome & Quickstart](#板块-1welcome--quickstart) | 这是什么 + 5 分钟跑起来 | 4 |
| 2 | [Workspace & Team](#板块-2workspace--team) | 人能理解的部分（Linear-like） | 4 |
| 3 | [Agents](#板块-3agents) | 引入 agent 这个新物种 | 3 |
| 4 | [How Agents Run](#板块-4how-agents-run) | 执行架构（daemon / runtime / task / providers） | 3 |
| 5 | [Working with Agents](#板块-5working-with-agents) | **4 种触发方式——产品核心特色** | 4 |
| 6 | [Staying Informed](#板块-6staying-informed) | Inbox + Subscriptions | 1 |
| 7 | [Administration](#板块-7administration) | Env / Auth Setup / Troubleshooting | 3 |
| 8 | [Reference](#板块-8reference) | CLI / Tokens / Desktop | 3 |

---

## 板块 1：Welcome & Quickstart

### 1.1 Welcome — 👀 In review [v1]

- **Source files**: `README.md`, `docs/docs-rewrite-plan.md`（定位段）, `apps/docs/content/docs/index.mdx`（现状）
- **目标读者**: P0 新用户 / evaluator（第一次听说 Multica）
- **叙事位置**: 第一页。定义整个产品。读完应该能回答"这是啥"。
- **Punch line（推荐）**: **"Your agents, your machine, your backlog."**
  > The task manager where AI teammates run on your own laptop.
- **写什么**（300-600 字）:
  - Punch line + 副标题
  - 三段展开：
    1. Agent 是 first-class（能被分配 / 评论 / 改状态 / 作为 project lead）
    2. Agent 跑在你自己的 daemon 上——你掌控计算和 API key
    3. Provider-agnostic：支持 Claude Code / Codex / Cursor CLI / Copilot 等 10 种
  - 一句借势："Speaks MCP natively. Compatible with Anthropic Agent Skills."
  - 3 种部署形态导航（Cloud / Self-Host / Desktop）
- **不写**:
  - 不用 "AI-native"（已贬值）
  - 不用 "autonomous"（撞 Autopilot 大军）
  - 不暗示对标 Devin（分类不同）
  - 架构细节（下一页）
- **写前要验证**: 产品定位文案和团

# FILE: docs/design.md

# Multica Design System

本文档定义 Multica 的视觉语言和交互规范。所有 UI 开发以此为准。

---

## 1. 设计哲学

三条核心原则：

1. **克制即高级。** 默认做减法。每个元素必须有存在的理由——多余的分割线、装饰性图标、"以防万一"的提示文字，都是噪音。留白本身就是设计。
2. **层次靠灰度，颜色是信号。** 界面的主体是中性色。颜色只在需要传递语义时出现（状态、品牌、错误）。如果两个区域在视觉上竞争注意力，解法是让一个退后，而不是两个都加色。
3. **一致性大于个性。** 同类交互必须有相同的视觉反馈。一个 hover 效果在 sidebar、dropdown、table row 里应该"感觉一样"。这种一致性通过 token 而非硬编码实现。

---

## 2. 颜色体系

基于 OKLCh 色彩空间，通过 CSS 变量定义。所有颜色使用 shadcn token，**禁止硬编码 Tailwind 色值**（如 `text-gray-500`、`bg-blue-600`）。

### 2.1 中性色阶梯

界面 90% 的面积由中性色构成。灰度等级即信息层级：

| 角色 | Light Token | Dark Token | 用途 |
|------|-------------|------------|------|
| 背景 | `background` | `background` | 页面底色 |
| 卡片/浮层 | `card` / `popover` | `card` / `popover` | 容器表面 |
| 次级表面 | `muted` / `secondary` | `muted` / `secondary` | hover 背景、标签底色 |
| 边框 | `border` | `border` | 分隔线、输入框边框 |
| 输入框边框 | `input` | `input` | 比 border 略重 |
| 主要文字 | `foreground` | `foreground` | 标题、正文 |
| 次要文字 | `muted-foreground` | `muted-foreground` | 描述、元数据、placeholder |
| 最强调文字 | `primary` | `primary` | 按钮文字（反色）、关键标签 |

**规则：** 同一屏幕内，文字颜色最多使用 3 个层级（`foreground` / `muted-foreground` / 某个语义色）。超过 3 级说明层次设计有问题。

### 2.2 语义色

颜色只用于传递含义，不做装饰：

| Token | 含义 | 使用场景 |
|-------|------|----------|
| `brand` | 品牌标识 | Logo、品牌按钮、极少量强调 |
| `destructive` | 危险/错误 | 删除按钮、表单校验错误、危险操作 |
| `success` | 成功 | 状态标签（完成、已解决） |
| `warning` | 警告 | 注意状态、到期提醒 |
| `info` | 信息 | 提示、链接、次要信息标记 |
| `priority` | 优先级 | 高优先级标签 |

**规则：**
- 语义色主要用于小面积元素（badge、icon、border）。大面积着色用该色的 10%-20% 透明度变体（如 `bg-destructive/10`）。
- 每屏同时出现的语义色不宜超过 2-3 种。如果一个界面同时有红黄绿蓝紫，说明信息密度过高，需要重新组织。

### 2.3 暗色模式

暗色模式不是简单的反转。它是独立设计的一套配色：

- 背景使用深灰（`oklch(0.18 ...)`），不是纯黑——纯黑在 LCD 屏上刺眼。
- 边框使用 `oklch(1 0 0 / 10%)`（白色 10% 透明度），比 light 模式更微妙。
- 语义色在 dark 模式下适当提亮（如 `success` 从 `0.55` 提到 `0.65`），保证对比度。
- 所有 UI 变更必须同时在两个模式下验证。

---

## 3. 字体规范

### 3.1 字体家族

| 角色 | 字体 | 用途 |
|------|------|------|
| 正文/UI | Inter (`--font-sans`) | 所有界面文字的默认字体；CJK 字符自动 fallback 到系统字体（PingFang SC / Microsoft YaHei / Noto Sans CJK SC） |
| 代码/数据 | Geist Mono (`--font-mono`) | 代码块、ID、时间戳、等宽数据 |
| 标题 | `--font-heading`（= `--font-sans`） | 页面标题、区块标题 |

字体栈在 `apps/web/app/layout.tsx` 和 `apps/desktop/src/renderer/src/globals.css` 两处声明，修改时需同步。

### 3.2 字号纪律

**整个项目只使用 3 个核心字号 + 1 个特殊字号：**

| Tailwind Class | 大小 | 角色 | 使用场景 |
|----------------|------|------|----------|
| `text-base` (16px) | 正文 | 页面标题、主要内容 | 页面标题、编辑器正文、空状态说明 |
| `text-sm` (14px) | 默认 | 界面的主力字号 | 菜单项、按钮、表单、列表项、正文 |
| `text-xs` (12px) | 辅助 | 元数据、标签 | badge 文字、时间戳、状态栏、次要信息 |
| `text-[0.8rem]` | 过渡 | 仅限 sm 按钮 | shadcn button size="sm" 专用 |

**禁止：**
- 使用 `text-lg`、`text-xl`、`text-2xl` 等——任务管理工具追求信息密度，不需要大字号。
- 使用任意像素值如 `text-[11px]`、`text-[13px]`——坚持 Tailwind 内置 scale。
- 在同一个区块里混用超过 2 个字号。如果需要第 3 个字号来区分层次，先试试用 `font-medium` vs `font-normal` 或 `text-muted-foreground` 来解决。

### 3.3 字重

只使用两个：

| 字重 | 用途 |
|------|------|
| `font-normal` (400) | 正文、描述、大部分文字 |
| `font-medium` (500) | 标签、按钮、导航项、标题、选中状态 |

**禁止** `font-bold` / `font-semibold`——任务管理工具追求信息密度和"轻"感，加粗会破坏层次节奏。如果需要更强的强调，用更大的字号或 `foreground` 色值，而不是加粗。

---

## 4. 间距体系

基于 Tailwind 的 4px 基础网格。间距传递信息——它不只是"好看"，而是告诉用户"什么属于什么"。

### 4.1 间距语义

| 间距 | Tailwind | 含义 |
|------|----------|------|
| 4px | `gap-1` / `p-1` | **紧密关联** — icon 与文字、label 与值 |
| 6px | `gap-1.5` / `p-1.5` | **组件内部** — 按钮内部 padding、列表项间距 |
| 8px | `gap-2` / `p-2` | **同组不同项** — 表单字段间、列表项间 |
| 12px | `gap-3` / `p-3` | **小节内** — 卡片内部 padding |
| 16px | `gap-4` / `p-4` | **组间分隔** — 不同区块之间 |
| 24px | `gap-6` / `p-6` | **大节分隔** — 页面主要区域间 |

**规则：如果需要分割线，说明间距不够。** 优先通过增大间距来分隔内容，而不是加 `<Separator />`。分割线应该是最后手段。

### 4.2 容器策略（按优先级排序）

当需要在视觉上分隔两个区域时：

1. **仅间距** — 增大两个区域的间距（首选）
2. **单条分割线** — 一根细线 `border-border`
3. **背景色变化** — 一个区域用 `bg-muted` 或 `bg-card`
4. **完整卡片** — border + radius + padding（最重手段）

用最轻的工具完成分隔。

---

## 5. 交互状态

这是设计一致性的核心。每种状态必须在所有组件中表现一致。

### 5.1 状态层级概览

```
默认 (rest) → hover → active/pressed → selected/active → focused → disabled
```

### 5.2 Hover 状态

Hover 是"我注意到你了"，视觉变化应该轻微、即时：

| 元素类型 | Hover 效果 | Token |
|----------|-----------|-------|
| 列表项/菜单项 | 背景变浅灰 | `hover:bg-muted` |
| Ghost 按钮 | 背景变浅灰 + 文字变前景色 | `hover:bg-muted hover:text-foreground` |
| 次要按钮 | 背景加深 20% | `hover:bg-secondary/80` |
| 主按钮 | 背景加深 20% | `hover:bg-primary/80` |
| 文字链接 | 下划线出现 | `hover:underline` |
| Tab 标签 | 文字从次要变主要 | `hover:text-foreground`（从 `text-muted-foreground`） |
| 图标按钮 | 背景变浅灰 | `hover:bg-muted` |
| 危险按钮 | 背景透明度加深 | `hover:bg-destructive/20` |

**规则：**
- hover 时不改变尺寸（无 `scale`）、不加阴影（无 `shadow`）。
- hover 的背景色永远比 selected/active 更淡。这样用户能区分"悬停"和"已选中"。
- 所有 hover 使用 `transition-colors` 或 `transition-all`，时长由 Tailwind 默认值（150ms）处理，不需要自定义。

### 5.3 Active / Selected 状态

Active 是"我已经被选中了"，视觉比 hover 更重：

| 元素类型 | Active 效果 | Token |
|----------|------------|-------|
| Sidebar 菜单项 | 背景 + 文字加重 + font-medium | `data-active:bg-sidebar-accent data-active:font-medium` |
| Tab | 下方指示条 + 文字变前景色 + font-medium | `data-[state=active]:text-foreground` |
| 列表选中行 | 背景加深 | `bg-muted` 或 `bg-accent` |
| Toggle（开） | 背景反色 | `data-[state=on]:bg-primary data-[state=on]:text-primary-foreground` |

**关键区分：** Hover = `bg-muted`，Active = `bg-muted` + `font-medium` + `text-foreground`。Active 始终比 hover 多一个视觉维度（字重或颜色变化），而不仅仅是背景更深。

### 5.3.1 Active 不被 Hover 覆盖

这是最容易出 bug 的地方：用户 hover 到一个已选中的项目上，hover 样式覆盖了 active 样式，导致选中态"闪回"普通 hover 态，视觉上像取消了选中。

**原则：Active 状态在任何时候都必须保持可辨识——包括被 hover 时。**

实现方式：

**方式一：Active 使用 hover 不涉及的维度**

如果 hover 只改背景，那 active 用字重 + 文字颜色来区分。即使 hover 背景叠上去，字重和颜色不变，用户仍能识别"这个是选中的"：

```
// ✅ hover 只管背景，active 靠字重和颜色
hover:bg-muted                          // hover：浅灰背景
data-active:font-medium data-active:text-foreground  // active：字重+颜色（hover 不会覆盖）
```

**方式二：Active + Hover 组合样式**

当 active 也用了背景色时，需要显式定义 "active 且 hover" 的复合状态，确保 hover 不会把 active 的背景拉回低层级：

```tsx
// ✅ 显式处理 active+hover 复合态
cn(
  "hover:bg-muted/50",                              // 普通 hover
  "data-active:bg-muted data-active:text-foreground", // active
  "data-active:hover:bg-muted"                       // active+hover：保持 active 背景，不降级
)
```

```tsx
