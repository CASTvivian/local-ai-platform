# Missing Repo Summary Source: HKUDS/OpenHarness

- URL: https://github.com/HKUDS/OpenHarness
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness
- Clone Status: cloned
- Language: Python
- Stars: 12429
- Topics: 
- Description: "OpenHarness: Open Agent Harness with a Built-in Personal Agent--Ohmo!"

## Extracted README / Docs / Examples



# FILE: README.md

<h1 align="center">
  <img src="assets/logo.png" alt="OpenHarness" width="64" style="vertical-align: middle;">
  &nbsp;&nbsp;
  <img src="assets/ohmo.png" alt="ohmo" width="64" style="vertical-align: middle;">
  <br>
  <code>oh</code> — OpenHarness &amp; <code>ohmo</code>
</h1>

<p align="center">
  <a href="README.md"><strong>English</strong></a> ·
  <a href="README.zh-CN.md"><strong>简体中文</strong></a>
</p>

**OpenHarness** delivers core lightweight agent infrastructure: tool-use, skills, memory, and multi-agent coordination.

**ohmo** is a personal AI agent built on OpenHarness — not another chatbot, but an assistant that actually works for you over long sessions. Chat with ohmo in Feishu / Slack / Telegram / Discord, and it forks branches, writes code, runs tests, and opens PRs on its own. ohmo runs on your existing Claude Code or Codex subscription — no extra API key needed.

**Join the community**: contribute **Harness** for open agent development.

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-5_min-blue?style=for-the-badge" alt="Quick Start"></a>
  <a href="#-harness-architecture"><img src="https://img.shields.io/badge/Harness-Architecture-ff69b4?style=for-the-badge" alt="Architecture"></a>
  <a href="#-features"><img src="https://img.shields.io/badge/Tools-43+-green?style=for-the-badge" alt="Tools"></a>
  <a href="#-test-results"><img src="https://img.shields.io/badge/Tests-114_Passing-brightgreen?style=for-the-badge" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/React+Ink-TUI-61DAFB?logo=react&logoColor=white" alt="React">
  <img src="https://img.shields.io/badge/pytest-114_pass-brightgreen" alt="Pytest">
  <img src="https://img.shields.io/badge/E2E-6_suites-orange" alt="E2E">
  <img src="https://img.shields.io/badge/output-text_|_json_|_stream--json-blueviolet" alt="Output">
  <a href="https://github.com/HKUDS/OpenHarness/actions/workflows/ci.yml"><img src="https://github.com/HKUDS/OpenHarness/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

One Command (**oh**) to Launch **OpenHarness** and Unlock All Agent Harnesses. 

Supports CLI agent integration including OpenClaw, nanobot, Cursor, and more.

<p align="center">
  <img src="assets/cli-typing.gif" alt="OpenHarness Terminal Demo" width="800">
</p>

---
## ✨ OpenHarness's Key Harness Features

<table align="center" width="100%">
<tr>
<td width="20%" align="center" style="vertical-align: top; padding: 15px;">

<h3>🔄 Agent Loop</h3>

<div align="center">
  <img src="https://img.shields.io/badge/Engine-06B6D4?style=for-the-badge&logo=lightning&logoColor=white" alt="Engine" />
</div>

<img src="assets/scene-agentloop.png" width="140">

<p align="center"><strong>• Streaming Tool-Call Cycle</strong></p>
<p align="center"><strong>• API Retry with Exponential Backoff</strong></p>
<p align="center"><strong>• Parallel Tool Execution</strong></p>
<p align="center"><strong>• Token Counting & Cost Tracking</strong></p>

</td>
<td width="20%" align="center" style="vertical-align: top; padding: 15px;">

<h3>🔧 Harness Toolkit</h3>

<div align="center">
  <img src="https://img.shields.io/badge/43+_Tools-10B981?style=for-the-badge&logo=toolbox&logoColor=white" alt="Toolkit" />
</div>

<img src="assets/scene-toolkit.png" width="140">

<p align="center"><strong>• 43 Tools (File, Shell, Search, Web, MCP)</strong></p>
<p align="center"><strong>• On-Demand Skill Loading (.md)</strong></p>
<p align="center"><strong>• Plugin Ecosystem (Skills + Hooks + Agents)</strong></p>
<p align="center"><strong>• Compatible with anthropics/skills & plugins</strong></p>

</td>
<td width="20%" align="center" style="vertical-align: top; padding: 15px;">

<h3>🧠 Context & Memory</h3>

<div align="center">
  <img src="https://img.shields.io/badge/Persistent-8B5CF6?style=for-the-badge&logo=brain&logoColor=white" alt="Context" />
</div>

<img src="assets/scene-context.png" width="140">

<p align="center"><strong>• CLAUDE.md Discovery & Injection</strong></p>
<p align="center"><strong>• Context Compression (Auto-Compact)</strong></p>
<p align="center"><strong>• MEMORY.md Persistent Memory</strong></p>
<p align="center"><strong>• Session Resume & History</strong></p>

</td>
<td width="20%" align="center" style="vertical-align: top; padding: 15px;">

<h3>🛡️ Governance</h3>

<div align="center">
  <img src="https://img.shields.io/badge/Permissions-F59E0B?style=for-the-badge&logo=shield&logoColor=white" alt="Governance" />
</div>

<img src="assets/scene-governance.png" width="140">

<p align="center"><strong>• Multi-Level Permission Modes</strong></p>
<p align="center"><strong>• Path-Level & Command Rules</strong></p>
<p align="center"><strong>• PreToolUse / PostToolUse Hooks</strong></p>
<p align="center"><strong>• Interactive Approval Dialogs</strong></p>

</td>
<td width="20%" align="center" style="vertical-align: top; padding: 15px;">

<h3>🤝 Swarm Coordination</h3>

<div align="center">
  <img src="https://img.shields.io/badge/Multi--Agent-EC4899?style=for-the-badge&logo=network&logoColor=white" alt="Swarm" />
</div>

<img src="assets/scene-swarm.png" width="140">

<p align="center"><strong>• Subagent Spawning & Delegation</strong></p>
<p align="center"><strong>• Team Registry & Task Management</strong></p>
<p align="center"><strong>• Background Task Lifecycle</strong></p>
<p align="center"><strong>• <a href="https://github.com/HKUDS/ClawTeam">ClawTeam</a> Integration (Roadmap)</strong></p>

</td>
</tr>
</table>

---

## 🤔 What is an Agent Harness?

An **Agent Harness** is the complete infrastructure that wraps around an LLM to make it a functional agent. The model provides intelligence; the harness provides **hands, eyes, memory, and safety boundaries**.

<p align="center">
  <img src="assets/harness-equation.png" alt="Harness = Tools + Knowledge + Observation + Action + Permissions" width="700">
</p>

OpenHarness is an open-source Python implementation designed for **researchers, builders, and the community**:

- **Understand** how production AI agents work under the hood
- **Experiment** with cutting-edge tools, skills, and agent coordination patterns
- **Extend** the harness with custom plugins, providers, and domain knowledge
- **Build** specialized agents on top of proven architecture

---

## 📰 What's New

- **Unreleased** 🔍 **Dry-run safe preview**:
  - `oh --dry-run` previews resolved runtime settings, auth state, skills, commands, tools, and configured MCP servers without executing the model, tools, or subagents.
  - Dry-run now reports a `ready` / `warning` / `blocked` readiness verdict with concrete next-step suggestions such as fixing auth, fixing MCP config, or running the prompt directly.
  - Prompt previews include likely matching skills and tools, while slash-command previews show whether the command is mostly read-only or stateful.
- **2026-04-18** ⚙️ **v0.1.7** — Packaging & TUI polish:
  - Install script now links `oh`, `ohmo`, and `openharness` into `~/.local/bin` instead of prepending the virtualenv `bin` directory to `PATH`, which avoids clobbering Conda-managed shells.
  - React TUI now supports `Shift+Enter` to insert a newline while keeping plain `Enter` as submit.
  - Busy-state animation in the React TUI is quieter and less error-prone on Windows terminals, with conservative spinner frames and reduced flashing.
- **2026-04-10** 🧠 **v0.1.6** — Auto-Compaction & Markdown TUI:
  - Auto-Compaction preserves task state and channel logs across context compression — agents can run multi-day sessions without manual compact/clear
  - Subprocess teammates run in headless worker mode; agent team creation stabilized
  - Assistant messages now render full Markdown in the React TUI
  - `ohmo` gains channel slash commands and multimodal attachment support
- **2026-04-08** 🔌 **v0.1.5** — MCP HTTP transport & Swarm polling:
  - MCP protocol adds HTTP transport, auto-reconnect on disconnect, and tool-only server compatibility
  - JSON Schema types inferred for MCP tool inputs — no manual type mapping needed
  - `ohmo` channels support file attachments and multimodal gateway messages
  - Subprocess agents are now pollable in real runs; permission modals serialized to prevent input swallowing
- **2026-04-08** 🌙 **v0.1.4** — Multi-provider auth & Moonshot/Kimi:
  - Native Moonshot/Kimi provider with `reasoning_content` support for thinking models
  - Auth overhaul: fixed provider-switching key mismatch, `OPENAI_BASE_URL` env override, profile-scoped credential priority
  - MCP gracefully handles disconnected servers in `call_tool` / `read_resource`
  - Security: built-in sensitive-path protection in PermissionChecker, hardened `web_fetch` URL validation
  - Stability: EIO crash recovery in Ink TUI, `--debug` logging, Windows cmd flash fix
- **2026-04-06** 🚀 **v0.1.2** — Unified setup flows and `ohmo` personal-agent app:
  - `oh setup` now guides provider selection as workflows instead of exposing raw auth/provider internals
  - Compatible API setup is now profile-scoped, so Anthropic/OpenAI-compatible endpoints can keep separate keys
  - `ohmo` ships as a packaged app with `~/.ohmo` workspace, gateway, bootstrap prompts, and channel config flow
- **2026-04-01** 🎨 **v0.1.0** — Initial **OpenHarness** open-source release featuring complete Harness architecture: 

<p align="center">
  <strong>Start here:</stro

# FILE: README.zh-CN.md

# <img src="assets/logo.png" alt="OpenHarness" width="40" style="vertical-align: middle;"> `oh` — OpenHarness 中文说明

<p align="center">
  <a href="README.md"><strong>English</strong></a> ·
  <a href="README.zh-CN.md"><strong>简体中文</strong></a>
</p>

**OpenHarness** 是一个面向开源社区的 Agent Harness。它提供轻量、可扩展、可检查的 Agent 基础设施，包括：

- Agent loop
- tools / skills / plugins
- memory / session resume
- permissions / hooks
- multi-agent coordination
- provider workflows
- React TUI
- `ohmo` personal-agent app

---

## 最新更新

### Unreleased · Dry-run 安全预览

- 新增 `oh --dry-run`，可以在**不执行模型、不执行工具、不 spawn subagent** 的前提下，预览当前会话会使用的配置、skills、commands、tools 和 MCP 配置。
- Dry-run 会给出 `ready / warning / blocked` 结论，并直接告诉你下一步该做什么，例如先修认证、先修 MCP 配置，或者可以直接运行。
- 对普通 prompt，会给出可能命中的 skills / tools；对 slash command，会展示它更偏只读还是会改本地状态。

### 2026-04-06 · v0.1.2

- 新增统一配置入口 `oh setup`
- provider 配置从“auth -> provider -> model”收敛成 workflow 视角
- Anthropic/OpenAI 兼容接口支持 profile 级凭据，不再强制共用一把全局 key
- 新增 `ohmo` personal-agent app
- `ohmo` 使用 `~/.ohmo` 作为 home workspace，支持 gateway、bootstrap prompts 和交互式 channel 配置

---

## 快速开始

### 一键安装

```bash
curl -fsSL https://raw.githubusercontent.com/HKUDS/OpenHarness/main/scripts/install.sh | bash
```

常用安装参数：

- `--from-source`：从源码安装，适合贡献者
- `--with-channels`：一并安装 IM channel 依赖

例如：

```bash
curl -fsSL https://raw.githubusercontent.com/HKUDS/OpenHarness/main/scripts/install.sh | bash -s -- --from-source --with-channels
```

### 本地运行

```bash
git clone https://github.com/HKUDS/OpenHarness.git
cd OpenHarness
uv sync --extra dev
uv run oh
```

---

## 配置模型与 Provider

现在最推荐的入口是：

```bash
oh setup
```

`oh setup` 会按下面的顺序引导：

1. 选择一个 workflow
2. 如果需要，完成认证
3. 选择具体后端 preset
4. 确认模型
5. 保存并激活 profile

当前内置 workflow 包括：

- `Anthropic-Compatible API`
- `Claude Subscription`
- `OpenAI-Compatible API`
- `Codex Subscription`
- `GitHub Copilot`

### Anthropic-Compatible API

适合这类后端：

- Claude 官方 API
- Moonshot / Kimi
- Zhipu / GLM
- MiniMax
- 其他 Anthropic-compatible endpoint

### OpenAI-Compatible API

适合这类后端：

- OpenAI 官方 API
- OpenRouter
- DashScope
- DeepSeek
- GitHub Models
- SiliconFlow
- Google Gemini
- Groq
- Ollama
- 其他 OpenAI-compatible endpoint

### 常用命令

```bash
# 统一配置入口
oh setup

# 查看已有 workflow/profile
oh provider list

# 切换当前 workflow
oh provider use codex

# 查看认证状态
oh auth status
```

### 高级：添加自定义兼容接口

如果内置 preset 不够，可以直接新增 profile：

```bash
oh provider add my-endpoint \
  --label "My Endpoint" \
  --provider anthropic \
  --api-format anthropic \
  --auth-source anthropic_api_key \
  --model my-model \
  --base-url https://example.com/anthropic
```

这一版开始，兼容接口可以按 profile 绑定凭据。  
也就是说，`Kimi`、`GLM`、`MiniMax` 这类 Anthropic-compatible 后端，不需要再共用一把全局 `anthropic` key。

---

## 交互模式与 TUI

运行：

```bash
oh
```

你会得到 React/Ink TUI，支持：

- `/` 命令选择器
- 交互式权限确认
- `/model` 模型切换
- `/permissions` 权限模式切换
- `/resume` 会话恢复
- `/provider` workflow 选择

非交互模式也支持：

```bash
oh -p "Explain this repository"
oh -p "List all functions in main.py" --output-format json
oh -p "Fix the bug" --output-format stream-json
```

### Dry-run 安全预览

如果你想先看 OpenHarness **会怎么跑**，但又不想真的执行模型或工具，可以用：

```bash
# 预览交互会话本身
oh --dry-run

# 预览一个普通 prompt
oh --dry-run -p "Review this bug fix and grep for failing tests"

# 预览 slash command
oh --dry-run -p "/plugin list"

# 输出结构化 JSON，方便脚本或 channel 使用
oh --dry-run -p "Explain this repository" --output-format json
```

Dry-run 的边界是明确的：

- **不会**调用模型
- **不会**执行 tools
- **不会**启动 subagent
- **不会**连接 MCP server
- **会**解析 settings、auth 状态、system prompt、skills、commands、tools，以及明显错误的 MCP 配置

Readiness 结论说明：

- `ready`：当前配置基本可直接运行
- `warning`：能解析会话，但仍有重要问题需要先处理，比如 MCP 配置错误或后续模型调用缺认证
- `blocked`：按当前状态直接运行会失败，比如 slash command 不存在，或者普通 prompt 无法解析 runtime client

Dry-run 输出里的 `next actions` 会直接给出下一步建议，例如：

- 先执行 `oh auth login`
- 先修或禁用坏掉的 MCP 配置
- 直接运行 `oh -p "..."` 或进入 `oh`

---

## Provider 兼容性概览

OpenHarness 现在把 provider 视为 **workflow + profile**，而不是只暴露底层协议名。

| Workflow | 说明 |
|----------|------|
| `Anthropic-Compatible API` | Anthropic 风格接口，适合 Claude/Kimi/GLM/MiniMax 等 |
| `Claude Subscription` | 复用本地 `~/.claude/.credentials.json` |
| `OpenAI-Compatible API` | OpenAI 风格接口，适合 OpenAI/OpenRouter/各种兼容网关 |
| `Codex Subscription` | 复用本地 `~/.codex/auth.json` |
| `GitHub Copilot` | GitHub Copilot OAuth workflow |

日常推荐用法：

```bash
oh setup
oh provider list
oh provider use <profile>
```

---

## `ohmo` Personal Agent

`ohmo` 是基于 OpenHarness 的 personal-agent app，不是 core 的一个 mode。

### 初始化

```bash
ohmo init
```

这会创建：

- `~/.ohmo/soul.md`
- `~/.ohmo/identity.md`
- `~/.ohmo/user.md`
- `~/.ohmo/BOOTSTRAP.md`
- `~/.ohmo/memory/`
- `~/.ohmo/gateway.json`

其中：

- `soul.md`：长期人格与行为原则
- `identity.md`：`ohmo` 自己是谁
- `user.md`：用户画像、偏好、关系信息
- `BOOTSTRAP.md`：首轮 landing / onboarding ritual
- `memory/`：personal memory
- `gateway.json`：gateway 的 profile 和 channel 配置

### 配置

```bash
ohmo config
```

`ohmo config` 会用和 `oh setup` 一致的 workflow 语言来配置 gateway，例如：

- `Anthropic-Compatible API`
- `Claude Subscription`
- `OpenAI-Compatible API`
- `Codex Subscription`
- `GitHub Copilot`

目前 `ohmo init` / `ohmo config` 已支持引导式配置这些 channel：

- Telegram
- Slack
- Discord
- Feishu

如果 gateway 已经在运行，配置完成后也可以直接选择是否重启。

### 运行

```bash
# 运行 personal agent
ohmo

# 前台运行 gateway
ohmo gateway run

# 查看 gateway 状态
ohmo gateway status

# 重启 gateway
ohmo gateway restart
```

---

## OpenHarness 的核心能力

### Agent Loop

- streaming tool-call cycle
- tool execution / observation / loop
- retry + exponential backoff
- token counting 与成本跟踪

### Tools / Skills / Plugins

- 43+ tools
- Markdown skills 按需加载
- 插件生态
- 兼容 `anthropics/skills`
- 兼容 Claude-style plugins

### Memory / Session

- `CLAUDE.md` 自动发现与注入
- `MEMORY.md` 持久记忆
- session resume
- auto-compact

### Governance

- 多级 permission mode
- path rules
- denied commands
- hooks
- interactive approval

### Multi-Agent

- subagent spawning
- team registry
- task lifecycle
- background task execution

---

## 常见命令

### `oh`

```bash
oh setup
oh provider list
oh provider use codex
oh auth status
oh -p "Explain this codebase"
oh
```

### `ohmo`

```bash
ohmo init
ohmo config
ohmo
ohmo gateway run
ohmo gateway status
ohmo gateway restart
```

---

## 测试

```bash
uv run pytest -q
python scripts/test_harness_features.py
python scripts/test_real_skills_plugins.py
```

---

## 贡献

欢迎贡献：

- tools
- skills
- plugins
- providers
- multi-agent coordination
- tests
- 文档与中文翻译

开发环境：

```bash
git clone https://github.com/HKUDS/OpenHarness.git
cd OpenHarness
uv sync --extra dev
uv run pytest -q
```

更多信息：

- [贡献指南](CONTRIBUTING.md)
- [更新日志](CHANGELOG.md)
- [Showcase](docs/SHOWCASE.md)

---

## License

MIT，见 [LICENSE](LICENSE)。


# FILE: docs/SHOWCASE.md

# OpenHarness Showcase

This page collects concrete ways to use OpenHarness without overselling the project. Each example is intended to be small, reproducible, and easy to extend.

## 1. Repository-aware coding assistant

Use OpenHarness as a lightweight local coding agent for reading code, making edits, and running validation commands.

```bash
uv run oh
```

Example prompt:

```text
Review this repo, identify the highest-risk bug, patch it, and run the relevant tests.
```

## 2. Headless automation for scripts and CI

The print mode is useful when you want structured output in shell pipelines or automation jobs.

```bash
uv run oh -p "Summarize the purpose of this repository" --output-format json
uv run oh -p "List files that define the permission system" --output-format stream-json
```

## 3. Skill and plugin playground

OpenHarness can load Markdown skills and Claude-style plugin layouts, which makes it useful for experimentation with custom workflows.

Examples:

- Put a custom skill in `~/.openharness/skills/`.
- Install a plugin into `~/.openharness/plugins/`.
- Use the same workflow conventions across multiple local projects.

## 4. Multi-agent and background task experiments

The repo includes team coordination primitives, background task management, and task inspection tools.

Example prompts:

```text
Spawn a worker to audit the test suite while you inspect the CLI command registry.
```

```text
Create a background task that runs the slow integration script and report back when it finishes.
```

## 5. Provider compatibility testbed

OpenHarness is useful when you need to compare Anthropic-compatible backends behind one harness.

Typical scenarios:

- Default Anthropic setup.
- Moonshot/Kimi through an Anthropic-compatible endpoint.
- Vertex-compatible and Bedrock-compatible gateways.
- Internal proxies that expose an Anthropic-style API surface.

See the provider compatibility table in [`README.md`](../README.md#-provider-compatibility).

## 6. Documentation-first onboarding

If you are evaluating the project rather than contributing code, start here:

- [`README.md`](../README.md) for install, usage, and architecture.
- [`CONTRIBUTING.md`](../CONTRIBUTING.md) for contributor workflow.
- [`CHANGELOG.md`](../CHANGELOG.md) for visible repo changes.

## How to contribute a showcase entry

Good showcase additions are:

- Based on a real workflow you ran.
- Short enough to reproduce locally.
- Honest about prerequisites and limitations.
- Focused on what OpenHarness makes easier, not on generic LLM claims.

