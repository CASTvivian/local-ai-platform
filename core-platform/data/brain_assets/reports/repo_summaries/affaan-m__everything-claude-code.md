# Repo Summary Source: affaan-m/everything-claude-code
- URL: https://github.com/affaan-m/everything-claude-code
- Local Path: core-platform/data/brain_assets/repos/github_stars/affaan-m__everything-claude-code
- Buckets: agent, mcp, llm_runtime
- Stars: 180549
- Language: JavaScript
- Description: The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development for Claude Code, Codex, Opencode, Cursor and beyond.
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

**Language:** English | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md)

# Everything Claude Code

![Everything Claude Code — the performance system for AI agent harnesses](assets/hero.png)

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![npm ecc-universal](https://img.shields.io/npm/dw/ecc-universal?label=ecc-universal%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-universal)
[![npm ecc-agentshield](https://img.shields.io/npm/dw/ecc-agentshield?label=ecc-agentshield%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-agentshield)
[![GitHub App Install](https://img.shields.io/badge/GitHub%20App-150%20installs-2ea44f?logo=github)](https://github.com/marketplace/ecc-tools)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Perl](https://img.shields.io/badge/-Perl-39457E?logo=perl&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **140K+ stars** | **21K+ forks** | **170+ contributors** | **12+ language ecosystems** | **Anthropic Hackathon Winner**

---

<div align="center">

**Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ**

[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md)
 | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md)

</div>

---

**The performance optimization system for AI agent harnesses. From an Anthropic hackathon winner.**

Not just configs. A complete system: skills, instincts, memory optimization, continuous learning, security scanning, and research-first development. Production-ready agents, skills, hooks, rules, MCP configurations, and legacy command shims evolved over 10+ months of intensive daily use building real products.

Works across **Claude Code**, **Codex**, **Cursor**, **OpenCode**, **Gemini**, and other AI agent harnesses.

ECC v2.0.0-rc.1 adds the public Hermes operator story on top of that reusable layer: start with the [Hermes setup guide](docs/HERMES-SETUP.md), then review the [rc.1 release notes](docs/releases/2.0.0-rc.1/release-notes.md) and [cross-harness architecture](docs/architecture/cross-harness.md).

---

## The Guides

This repo is the raw code only. The guides explain everything.

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="./assets/images/guides/shorthand-guide.png" alt="The Shorthand Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="./assets/images/guides/longform-guide.png" alt="The Longform Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="./assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>Shorthand Guide</b><br/>Setup, foundations, philosophy. <b>Read this first.</b></td>
<td align="center"><b>Longform Guide</b><br/>Token optimization, memory persistence, evals, parallelization.</td>
<td align="center"><b>Security Guide</b><br/>Attack vectors, sandboxing, sanitization, CVEs, AgentShield.</td>
</tr>
</table>

| Topic | What You'll Learn |
|-------|-------------------|
| Token Optimization | Model selection, system prompt slimming, background processes |
| Memory Persistence | Hooks that save/load context across sessions automatically |
| Continuous Learning | Auto-extract patterns from sessions into reusable skills |
| Verification Loops | Checkpoint vs continuous evals, grader types, pass@k metrics |
| Parallelization | Git worktrees, cascade method, when to scale instances |
| Subagent Orchestration | The context problem, iterative retrieval pattern |

---

## What's New

### v2.0.0-rc.1 — Surface Refresh, Operator Workflows, and ECC 2.0 Alpha (Apr 2026)

- **Dashboard GUI** — New Tkinter-based desktop application (`ecc_dashboard.py` or `npm run dashboard`) with dark/light theme toggle, font customization, and project logo in header and taskbar.
- **Public surface synced to the live repo** — metadata, catalog counts, plugin manifests, and install-facing docs now match the actual OSS surface: 55 agents, 208 skills, and 72 legacy command shims.
- **Operator and outbound workflow expansion** — `brand-voice`, `social-graph-ranker`, `connections-optimizer`, `customer-billing-ops`, `ecc-tools-cost-audit`, `google-workspace-ops`, `project-flow-ops`, and `workspace-surface-audit` round out the operator lane.
- **Media and launch tooling** — `manim-video`, `remotion-video-creation`, and upgraded social publishing surfaces make technical explainers and launch content part of the same system.
- **Framework and product surface growth** — `nestjs-patterns`, richer Codex/OpenCo


# FILE: README.zh-CN.md

# Everything Claude Code

[![Stars](https://img.shields.io/github/stars/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/stargazers)
[![Forks](https://img.shields.io/github/forks/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/network/members)
[![Contributors](https://img.shields.io/github/contributors/affaan-m/everything-claude-code?style=flat)](https://github.com/affaan-m/everything-claude-code/graphs/contributors)
[![npm ecc-universal](https://img.shields.io/npm/dw/ecc-universal?label=ecc-universal%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-universal)
[![npm ecc-agentshield](https://img.shields.io/npm/dw/ecc-agentshield?label=ecc-agentshield%20weekly%20downloads&logo=npm)](https://www.npmjs.com/package/ecc-agentshield)
[![GitHub App Install](https://img.shields.io/badge/GitHub%20App-150%20installs-2ea44f?logo=github)](https://github.com/marketplace/ecc-tools)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Shell](https://img.shields.io/badge/-Shell-4EAA25?logo=gnu-bash&logoColor=white)
![TypeScript](https://img.shields.io/badge/-TypeScript-3178C6?logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Go](https://img.shields.io/badge/-Go-00ADD8?logo=go&logoColor=white)
![Java](https://img.shields.io/badge/-Java-ED8B00?logo=openjdk&logoColor=white)
![Perl](https://img.shields.io/badge/-Perl-39457E?logo=perl&logoColor=white)
![Markdown](https://img.shields.io/badge/-Markdown-000000?logo=markdown&logoColor=white)

> **140K+ stars** | **21K+ forks** | **170+ 贡献者** | **12+ 语言系统** | **Anthropic黑客松获胜者**

---

<div align="center">

**Language / 语言 / 語言 / Dil / Язык / Ngôn ngữ**

[**English**](README.md) | [Português (Brasil)](docs/pt-BR/README.md) | [简体中文](README.zh-CN.md) | [繁體中文](docs/zh-TW/README.md) | [日本語](docs/ja-JP/README.md) | [한국어](docs/ko-KR/README.md) | [Türkçe](docs/tr/README.md) | [Русский](docs/ru/README.md) | [Tiếng Việt](docs/vi-VN/README.md)

</div>

---

**来自 Anthropic 黑客马拉松获胜者的完整 Claude Code 配置集合。**

不止是配置文件，而是一整套完整系统：技能体系、本能行为、记忆优化、持续学习、安全扫描，以及研究优先的开发模式。
包含可直接用于生产环境的智能体、技能模块、钩子、规则、MCP 配置，以及兼容传统命令的适配层——所有内容均经过 10 个多月高强度日常使用与真实产品开发迭代打磨而成。

可在 **Claude Code**、**Codex**、**Cursor**、**OpenCode**、**Gemini** 及其他 AI 智能体框架中通用。

---

## 指南

这个仓库只包含原始代码。指南解释了一切。

<table>
<tr>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2012378465664745795">
<img src="https://github.com/user-attachments/assets/1a471488-59cc-425b-8345-5245c7efbcef" alt="The Shorthand Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2014040193557471352">
<img src="https://github.com/user-attachments/assets/c9ca43bc-b149-427f-b551-af6840c368f0" alt="The Longform Guide to Everything Claude Code" />
</a>
</td>
<td width="33%">
<a href="https://x.com/affaanmustafa/status/2033263813387223421">
<img src="./assets/images/security/security-guide-header.png" alt="The Shorthand Guide to Everything Agentic Security" />
</a>
</td>
</tr>
<tr>
<td align="center"><b>精简指南</b><br/>设置、基础、理念。<b>先读这个。</b></td>
<td align="center"><b>详细指南</b><br/>Token 优化、内存持久化、评估、并行化。</td>
<td align="center"><b>安全指南</b><br/>攻击向量、沙箱技术、数据净化、CVE漏洞、Agent防护</td>
</tr>
</table>

| 主题 | 你将学到什么 |
|-------|-------------------|
| Token 优化 | 模型选择、系统提示精简、后台进程 |
| 内存持久化 | 自动跨会话保存/加载上下文的钩子 |
| 持续学习 | 从会话中自动提取模式到可重用的技能 |
| 验证循环 | 检查点 vs 持续评估、评分器类型、pass@k 指标 |
| 并行化 | Git worktrees、级联方法、何时扩展实例 |
| 子代理编排 | 上下文问题、迭代检索模式 |

---

## 最新动态

### v2.0.0-rc.1 — 表面同步、运营工作流与 ECC 2.0 Alpha（2026年4月）

- **公共表面已与真实仓库同步** —— 元数据、目录数量、插件清单以及安装文档现在都与实际开源表面保持一致。
- **运营与外向型工作流扩展** —— `brand-voice`、`social-graph-ranker`、`customer-billing-ops`、`google-workspace-ops` 等运营型 skill 已纳入同一系统。
- **媒体与发布工具补齐** —— `manim-video`、`remotion-video-creation` 以及社媒发布能力让技术讲解和发布流程直接在同一仓库内完成。
- **框架与产品表面继续扩展** —— `nestjs-patterns`、更完整的 Codex/OpenCode 安装表面，以及跨 harness 打包改进，让仓库不再局限于 Claude Code。
- **ECC 2.0 alpha 已进入仓库** —— `ecc2/` 下的 Rust 控制层现已可在本地构建，并提供 `dashboard`、`start`、`sessions`、`status`、`stop`、`resume` 与 `daemon` 命令。
- **生态加固持续推进** —— AgentShield、ECC Tools 成本控制、计费门户工作与网站刷新仍围绕核心插件持续交付。

## 快速开始

在 2 分钟内快速上手：

### 第一步：安装插件

> 注意：插件安装方式较为便捷，但如果你的 Claude Code 版本无法正常解析自托管市场条目，建议使用下方的开源安装脚本，稳定性更高。

```bash
# 添加市场
/plugin marketplace add https://github.com/affaan-m/everything-claude-code

# 安装插件
/plugin install ecc@ecc
```

> 安装名称说明：较早的帖子里可能还会出现较长的旧标识符。Anthropic 的 marketplace/plugin 安装是按规范化插件标识符寻址的，因此 ECC 现在统一为 `ecc@ecc`，让工具名和 slash command 命名空间保持简短。

### 第二步：仅在需要时安装规则

> WARNING: **重要提示：** Claude Code 插件无法自动分发 `rules`。
>
> 如果你已经通过 `/plugin install` 安装了 ECC，**不要再运行 `./install.sh --profile full`、`.\install.ps1 --profile full` 或 `npx ecc-install --profile full`**。插件已经会自动加载 ECC 的技能、命令和 hooks；此时再执行完整安装，会把同一批内容再次复制到用户目录，导致技能重复以及运行时行为重复。
>
> 对于插件安装路径，请只手动复制你需要的 `rules/` 目录。只有在你完全不走插件安装、而是选择“纯手动安装 ECC”时，才应该使用完整安装器。

```bash
# 首先克隆仓库
git clone https://github.com/affaan-m/everything-claude-code.git
cd everything-claude-code

# 安装依赖（选择你常用的包管理器）
npm install        # 或：pnpm install | yarn install | bun install

# 插件安装路径：只复制规则
mkdir -p ~/.claude/rules
cp -R rules/common ~/.claude/rules/
cp -R rules/typescript ~/.claude/rules/

# 纯手动安装 ECC（不要和 /plugin install 叠加）
# ./install.sh --profile full
```

```powershell
# Windows 系统（PowerShell）

# 插件安装路径：只复制规则
New-Item -ItemType Directory -Force -Path "$HOME/.claude/rules" | Out-Null
Copy-Item -Recurse rules/common "$HOME/.claude/rules/"
Copy-Item -Recurse rules/typescript "$HOME/.claude/rules/"

# 纯手动安装 ECC（不要和 /plugin install 叠加）
# .\install.ps1 --profile full
# npx ecc-install --profile full
```

如需手动安装说明，请查看 `rules/` 文件夹中的 README 文档。手动复制规则文件时，请直接复制**整个语言目录**（例如 `rules/common` 或 `rules/golang`），而非目录内的单个文件，以保证相对路径引用正常、文件名不会冲突。

### 第三步：开始使用

```bash
# 尝试一个命令（插件安装使用命名空间形式）
/ecc:plan "添加用户认证"

# 手动安装（选项2）使用简短形式：
# /plan "添加用户认证"

# 查看可用命令
/plugin list ecc@ecc
```

**完成！** 你现在可以使用 60 个代理、228 个技能和 75 个命令。

### mu


# FILE: docs/ECC-2.0-REFERENCE-ARCHITECTURE.md

# ECC 2.0 Reference Architecture

Current execution mirror:
[`ECC-2.0-GA-ROADMAP.md`](ECC-2.0-GA-ROADMAP.md).

This document turns the May 2026 reference sweep into concrete ECC backlog
shape. It is not a second strategy memo: every reference pressure below should
land as an adapter, check, observable signal, security policy, PR review
surface, or release-readiness gate.

## Reference Baseline

Snapshot date: 2026-05-12.

| Reference | Primary pressure on ECC 2.0 | Concrete ECC delta |
| --- | --- | --- |
| [`stablyai/orca`](https://github.com/stablyai/orca) | Worktree-native multi-agent IDE with terminals, source control, GitHub integration, SSH, notifications, design/browser mode, account switching, and per-worktree context. | Treat worktree lifecycle, review state, notification state, and account/provider identity as first-class adapter signals. |
| [`superset-sh/superset`](https://github.com/superset-sh/superset) | Desktop AI-agent workspace with parallel execution, worktree isolation, diff review, workspace presets, and broad CLI-agent compatibility. | Add workspace preset taxonomy and make ECC2 session/worktree state exportable enough for external editors to consume. |
| [`standardagents/dmux`](https://github.com/standardagents/dmux) | Tmux/worktree orchestration, lifecycle hooks, multi-select agent control, smart merging, file browser, notifications, and cleanup. | Add lifecycle-hook coverage to the harness matrix and define merge/conflict queue events. |
| [`aidenybai/ghast`](https://github.com/aidenybai/ghast) | Native macOS terminal multiplexer with cwd-grouped workspaces, panes, tabs, drag/drop, search, and notifications. | Preserve terminal-native ergonomics while adding cwd/session grouping and searchable handoff/session records. |
| [`jarrodwatts/claude-hud`](https://github.com/jarrodwatts/claude-hud) | Always-visible Claude Code statusline for context, tools, agents, todos, and transcript-backed activity. | Formalize the ECC HUD/status payload for context, cost, tool calls, active agents, todos, queue state, checks, and risk. |
| [`stanford-iris-lab/meta-harness`](https://github.com/stanford-iris-lab/meta-harness) | Automated search over task-specific harness design: what to store, retrieve, and show. | Split ECC improvement loops into scenario spec, proposer trace, verifier result, and promoted playbook. |
| [`greyhaven-ai/autocontext`](https://github.com/greyhaven-ai/autocontext) | Recursive harness improvement using traces, reports, artifacts, datasets, playbooks, and role-separated evaluators. | Store reusable traces and playbooks before mutating installed harness assets. |
| [`NousResearch/hermes-agent`](https://github.com/NousResearch/hermes-agent) | Self-improving operator shell with memories, skills, scheduler, gateways, subagents, terminal backends, and migration tooling. | Keep ECC portable across local, SSH, container, and hosted terminal backends without hiding the underlying commands. |
| [`anthropics/claude-code`](https://github.com/anthropics/claude-code), [`sst/opencode`](https://github.com/sst/opencode), Zed, Codex, Cursor, Gemini | Different agent harnesses expose different hooks, plugin surfaces, session stores, config files, and review loops. | Maintain a public adapter compliance matrix instead of treating one harness as the canonical UX. |
| Local Claude Code source review | Session, tool, permission, hook, remote, analytics, task, and context-suggestion surfaces are more structured than the public CLI UX suggests. | Model status and risk events around session messages, permission requests, tool progress, context pressure, and summary state. |

## Architecture Shape

ECC 2.0 should be a harness operating system, not only a catalog of commands,
agents, and skills.

```text
┌──────────────────────────────────────────────────────────────┐
│ Operator Surface                                             │
│ CLI, plugin, TUI, HUD/statusline, release gates, PR checks   │
├──────────────────────────────────────────────────────────────┤
│ Harness Adapter Layer                                        │
│ Claude Code, Codex, OpenCode, Cursor, Gemini, Zed, dmux,     │
│ Orca, Superset, Ghast, terminal-only                         │
├──────────────────────────────────────────────────────────────┤
│ Worktree, Session, And Queue Runtime                         │
│ worktrees, panes, sessions, todos, checks, merge/conflict    │
│ queues, notification state, ownership, handoff exports       │
├──────────────────────────────────────────────────────────────┤
│ Observability And Evaluation Loop                            │
│ JSONL traces, status snapshots, risk ledger, harness audit,  │
│ scenario specs, verifiers, promoted playbooks, RAG sets      │
├──────────────────────────────────────────────────────────────┤
│ Security And Commercial Platform                             │
│ AgentShield policies/SARIF, ECC Tools checks, billing,       │
│ Linear/GitHub sync, enterprise reports                       │
└──────────────────────────────────────────────────────────────┘
```

## Reference-To-Backlog Map

### Worktree And Session Orchestration

Adopt from Orca, Superset, dmux, and Ghast:

- Worktree lifecycle events: create, resume, pause, stop, diff, review, PR,
  merge-ready, conflict, stale, close, salvage.
- Session grouping by repo, branch, cwd, task, owner, and harness.
- Workspace presets for release lane, PR triage lane, docs lane, security lane,
  and test-writer lane.
- Notifications for blocked CI, dirty worktrees, merge conflicts, stale review,
  and finished autonomous runs.
- Review loops that can annotate diffs and PRs without taking ownership away
  from maintainers.

Repo work:

- `everything-claude-code`: extend the adapter compliance matrix and public
  scorecard onramp.
- `ecc2`: surface session/worktree state through a stable local payload before
  adding hosted telemetry.
- `ECC-Tools`: consume the same lifecycle events for PR checks, issue routing,
  and


# FILE: docs/ANTIGRAVITY-GUIDE.md

# Antigravity Setup and Usage Guide

Google's [Antigravity](https://antigravity.dev) is an AI coding IDE that uses a `.agent/` directory convention for configuration. ECC provides first-class support for Antigravity through its selective install system.

## Quick Start

```bash
# Install ECC with Antigravity target
./install.sh --target antigravity typescript

# Or with multiple language modules
./install.sh --target antigravity typescript python go
```

This installs ECC components into your project's `.agent/` directory, ready for Antigravity to pick up.

## How the Install Mapping Works

ECC remaps its component structure to match Antigravity's expected layout:

| ECC Source | Antigravity Destination | What It Contains |
|------------|------------------------|------------------|
| `rules/` | `.agent/rules/` | Language rules and coding standards (flattened) |
| `commands/` | `.agent/workflows/` | Slash commands become Antigravity workflows |
| `agents/` | `.agent/skills/` | Agent definitions become Antigravity skills |

> **Note on `.agents/` vs `.agent/` vs `agents/`**: The installer only handles three source paths explicitly: `rules` → `.agent/rules/`, `commands` → `.agent/workflows/`, and `agents` (no dot prefix) → `.agent/skills/`. The dot-prefixed `.agents/` directory in the ECC repo is a **static layout** for Codex/Antigravity skill definitions and `openai.yaml` configs — it is not directly mapped by the installer. Any `.agents/` path falls through to the default scaffold operation. If you want `.agents/skills/` content available in the Antigravity runtime, you must manually copy it to `.agent/skills/`.

### Key Differences from Claude Code

- **Rules are flattened**: Claude Code nests rules under subdirectories (`rules/common/`, `rules/typescript/`). Antigravity expects a flat `rules/` directory — the installer handles this automatically.
- **Commands become workflows**: ECC's `/command` files land in `.agent/workflows/`, which is Antigravity's equivalent of slash commands.
- **Agents become skills**: ECC agent definitions map to `.agent/skills/`, where Antigravity looks for skill configurations.

## Directory Structure After Install

```
your-project/
├── .agent/
│   ├── rules/
│   │   ├── coding-standards.md
│   │   ├── testing.md
│   │   ├── security.md
│   │   └── typescript.md          # language-specific rules
│   ├── workflows/
│   │   ├── plan.md
│   │   ├── code-review.md
│   │   ├── tdd.md
│   │   └── ...
│   ├── skills/
│   │   ├── planner.md
│   │   ├── code-reviewer.md
│   │   ├── tdd-guide.md
│   │   └── ...
│   └── ecc-install-state.json     # tracks what ECC installed
```

## The `openai.yaml` Agent Config

Each skill directory under `.agents/skills/` contains an `agents/openai.yaml` file at the path `.agents/skills/<skill-name>/agents/openai.yaml` that configures the skill for Antigravity:

```yaml
interface:
  display_name: "API Design"
  short_description: "REST API design patterns and best practices"
  brand_color: "#F97316"
  default_prompt: "Design REST API: resources, status codes, pagination"
policy:
  allow_implicit_invocation: true
```

| Field | Purpose |
|-------|---------|
| `display_name` | Human-readable name shown in Antigravity's UI |
| `short_description` | Brief description of what the skill does |
| `brand_color` | Hex color for the skill's visual badge |
| `default_prompt` | Suggested prompt when the skill is invoked manually |
| `allow_implicit_invocation` | When `true`, Antigravity can activate the skill automatically based on context |

## Managing Your Installation

### Check What's Installed

```bash
node scripts/list-installed.js --target antigravity
```

### Repair a Broken Install

```bash
# First, diagnose what's wrong
node scripts/doctor.js --target antigravity

# Then, restore missing or drifted files
node scripts/repair.js --target antigravity
```

### Uninstall

```bash
node scripts/uninstall.js --target antigravity
```

### Install State

The installer writes `.agent/ecc-install-state.json` to track which files ECC owns. This enables safe uninstall and repair — ECC will never touch files it didn't create.

## Adding Custom Skills for Antigravity

If you're contributing a new skill and want it available on Antigravity:

1. Create the skill under `skills/your-skill-name/SKILL.md` as usual
2. Add an agent definition at `agents/your-skill-name.md` — this is the path the installer maps to `.agent/skills/` at runtime, making your skill available in the Antigravity harness
3. Add the Antigravity agent config at `.agents/skills/your-skill-name/agents/openai.yaml` — this is a static repo layout consumed by Codex for implicit invocation metadata
4. Mirror the `SKILL.md` content to `.agents/skills/your-skill-name/SKILL.md` — this static copy is used by Codex and serves as a reference for Antigravity
5. Mention in your PR that you added Antigravity support

> **Key distinction**: The installer deploys `agents/` (no dot) → `.agent/skills/` — this is what makes skills available at runtime. The `.agents/` (dot-prefixed) directory is a separate static layout for Codex `openai.yaml` configs and is not auto-deployed by the installer.

See [CONTRIBUTING.md](../CONTRIBUTING.md) for the full contribution guide.

## Comparison with Other Targets

| Feature | Claude Code | Cursor | Codex | Antigravity |
|---------|-------------|--------|-------|-------------|
| Install target | `claude-home` | `cursor-project` | `codex-home` | `antigravity` |
| Config root | `~/.claude/` | `.cursor/` | `~/.codex/` | `.agent/` |
| Scope | User-level | Project-level | User-level | Project-level |
| Rules format | Nested dirs | Flat | Flat | Flat |
| Commands | `commands/` | N/A | N/A | `workflows/` |
| Agents/Skills | `agents/` | N/A | N/A | `skills/` |
| Install state | `ecc-install-state.json` | `ecc-install-state.json` | `ecc-install-state.json` | `ecc-install-state.json` |

## Troubleshooting

### Skills not loading in Antigravity

- Verify the `.agent/` directory e


# FILE: docs/SKILL-PLACEMENT-POLICY.md

# Skill Placement and Provenance Policy

This document defines where generated, imported, and curated skills belong, how they are identified, and what gets shipped.

## Skill Types and Placement

| Type | Root Path | Shipped | Provenance |
|------|-----------|---------|------------|
| Curated | `skills/` (repo) | Yes | Not required |
| Learned | `~/.claude/skills/learned/` | No | Required |
| Imported | `~/.claude/skills/imported/` | No | Required |
| Evolved | `~/.claude/homunculus/evolved/skills/` (global) or `projects/<hash>/evolved/skills/` (per-project) | No | Inherits from instinct source |

Curated skills live in the repo under `skills/`. Install manifests reference only curated paths. Generated and imported skills live under the user home directory and are never shipped.

## Curated Skills

Location: `skills/<skill-name>/` with `SKILL.md` at root.

- Included in `manifests/install-modules.json` paths.
- Validated by `scripts/ci/validate-skills.js`.
- No provenance file. Use `origin` in SKILL.md frontmatter (ECC, community) for attribution.

## Learned Skills

Location: `~/.claude/skills/learned/<skill-name>/`.

Created by continuous-learning (evaluate-session hook, /learn command). Default path is configurable via `skills/continuous-learning/config.json` → `learned_skills_path`.

- Not in repo. Not shipped.
- Must have `.provenance.json` sibling to `SKILL.md`.
- Loaded at runtime when directory exists.

## Imported Skills

Location: `~/.claude/skills/imported/<skill-name>/`.

User-installed skills from external sources (URL, file copy, etc.). No automated importer exists yet; placement is by convention.

- Not in repo. Not shipped.
- Must have `.provenance.json` sibling to `SKILL.md`.

## Evolved Skills (Continuous Learning v2)

Location: `~/.claude/homunculus/evolved/skills/` (global) or `~/.claude/homunculus/projects/<hash>/evolved/skills/` (per-project).

Generated by instinct-cli evolve from clustered instincts. Separate system from learned/imported.

- Not in repo. Not shipped.
- Provenance inherited from source instincts; no separate `.provenance.json` required.

## Provenance Metadata

Required for learned and imported skills. File: `.provenance.json` in the skill directory.

Required fields:

| Field | Type | Description |
|-------|------|-------------|
| source | string | Origin (URL, path, or identifier) |
| created_at | string | ISO 8601 timestamp |
| confidence | number | 0–1 |
| author | string | Who or what produced the skill |

Schema: `schemas/provenance.schema.json`. Validation: `scripts/lib/skill-evolution/provenance.js` → `validateProvenance`.

## Validator Behavior

### validate-skills.js

Scope: Curated skills only (`skills/` in repo).

- If `skills/` does not exist: exit 0 (nothing to validate).
- For each subdirectory: must contain `SKILL.md`, non-empty.
- Does not touch learned/imported/evolved roots.

### validate-install-manifests.js

Scope: Curated paths only. All `paths` in modules must exist in the repo.

- Generated/imported roots are out of scope. No manifest references them.
- Missing path → error. No optional-path handling.

### Scripts That Use Generated Roots

`scripts/skills-health.js`, `scripts/lib/skill-evolution/health.js`, session hooks: they probe `~/.claude/skills/learned` and `~/.claude/skills/imported`. Missing directories are treated as empty; no errors.

## Publishable vs Local-Only

| Publishable | Local-Only |
|-------------|------------|
| `skills/*` (curated) | `~/.claude/skills/learned/*` |
| | `~/.claude/skills/imported/*` |
| | `~/.claude/homunculus/**/evolved/**` |

Only curated skills appear in install manifests and get copied during install.

## Implementation Roadmap

1. Policy document and provenance schema (this change).
2. Add provenance validation to learned-skill write paths (evaluate-session, /learn output) so new learned skills always get `.provenance.json`.
3. Update instinct-cli evolve to write optional provenance when generating evolved skills.
4. Add `scripts/validate-provenance.js` to CI for any repo paths that must not contain learned/imported content (if needed).
5. Document learned/imported roots in CONTRIBUTING.md or user docs so contributors know not to commit them.



# FILE: docs/SELECTIVE-INSTALL-ARCHITECTURE.md

# ECC 2.0 Selective Install Discovery

## Purpose

This document turns the March 11 mega-plan selective-install requirement into a
concrete ECC 2.0 discovery design.

The goal is not just "fewer files copied during install." The actual target is
an install system that can answer, deterministically:

- what was requested
- what was resolved
- what was copied or generated
- what target-specific transforms were applied
- what ECC owns and may safely remove or repair later

That is the missing contract between ECC 1.x installation and an ECC 2.0
control plane.

## Current Implemented Foundation

The first selective-install substrate already exists in-repo:

- `manifests/install-modules.json`
- `manifests/install-profiles.json`
- `schemas/install-modules.schema.json`
- `schemas/install-profiles.schema.json`
- `schemas/install-state.schema.json`
- `scripts/ci/validate-install-manifests.js`
- `scripts/lib/install-manifests.js`
- `scripts/lib/install/request.js`
- `scripts/lib/install/runtime.js`
- `scripts/lib/install/apply.js`
- `scripts/lib/install-targets/`
- `scripts/lib/install-state.js`
- `scripts/lib/install-executor.js`
- `scripts/lib/install-lifecycle.js`
- `scripts/ecc.js`
- `scripts/install-apply.js`
- `scripts/install-plan.js`
- `scripts/list-installed.js`
- `scripts/doctor.js`

Current capabilities:

- machine-readable module and profile catalogs
- CI validation that manifest entries point at real repo paths
- dependency expansion and target filtering
- adapter-aware operation planning
- canonical request normalization for legacy and manifest install modes
- explicit runtime dispatch from normalized requests into plan creation
- legacy and manifest installs both write durable install-state
- read-only inspection of install plans before any mutation
- unified `ecc` CLI routing install, planning, and lifecycle commands
- lifecycle inspection and mutation via `list-installed`, `doctor`, `repair`,
  and `uninstall`

Current limitation:

- target-specific merge/remove semantics are still scaffold-level for some modules
- legacy `ecc-install` compatibility still points at `install.sh`
- publish surface is still broad in `package.json`

## Current Code Review

The current installer stack is already much healthier than the original
language-first shell installer, but it still concentrates too much
responsibility in a few files.

### Current Runtime Path

The runtime flow today is:

1. `install.sh`
   thin shell wrapper that resolves the real package root
2. `scripts/install-apply.js`
   user-facing installer CLI for legacy and manifest modes
3. `scripts/lib/install/request.js`
   CLI parsing plus canonical request normalization
4. `scripts/lib/install/runtime.js`
   runtime dispatch from normalized requests into install plans
5. `scripts/lib/install-executor.js`
   argument translation, legacy compatibility, operation materialization,
   filesystem mutation, and install-state write
6. `scripts/lib/install-manifests.js`
   module/profile catalog loading plus dependency expansion
7. `scripts/lib/install-targets/`
   target root and destination-path scaffolding
8. `scripts/lib/install-state.js`
   schema-backed install-state read/write
9. `scripts/lib/install-lifecycle.js`
   doctor/repair/uninstall behavior derived from stored operations

That is enough to prove the selective-install substrate, but not enough to make
the installer architecture feel settled.

### Current Strengths

- install intent is now explicit through `--profile` and `--modules`
- request parsing and request normalization are now split from the CLI shell
- target root resolution is already adapterized
- lifecycle commands now use durable install-state instead of guessing
- the repo already has a unified Node entrypoint through `ecc` and
  `install-apply.js`

### Current Coupling Still Present

1. `install-executor.js` is smaller than before, but still carrying too many
   planning and materialization layers at once.
   The request boundary is now extracted, but legacy request translation,
   manifest-plan expansion, and operation materialization still live together.
2. target adapters are still too thin.
   Today they mostly resolve roots and scaffold destination paths. The real
   install semantics still live in executor branches and path heuristics.
3. the planner/executor boundary is not clean enough yet.
   `install-manifests.js` resolves modules, but the final install operation set
   is still partly constructed in executor-specific logic.
4. lifecycle behavior depends on low-level recorded operations more than on
   stable module semantics.
   That works for plain file copy, but becomes brittle for merge/generate/remove
   behaviors.
5. compatibility mode is mixed directly into the main installer runtime.
   Legacy language installs should behave like a request adapter, not as a
   parallel installer architecture.

## Proposed Modular Architecture Changes

The next architectural step is to separate the installer into explicit layers,
with each layer returning stable data instead of immediately mutating files.

### Target State

The desired install pipeline is:

1. CLI surface
2. request normalization
3. module resolution
4. target planning
5. operation planning
6. execution
7. install-state persistence
8. lifecycle services built on the same operation contract

The main idea is simple:

- manifests describe content
- adapters describe target-specific landing semantics
- planners describe what should happen
- executors apply those plans
- lifecycle commands reuse the same plan/state model instead of reinventing it

### Proposed Runtime Layers

#### 1. CLI Surface

Responsibility:

- parse user intent only
- route to install, plan, doctor, repair, uninstall
- render human or JSON output

Should not own:

- legacy language translation
- target-specific install rules
- operation construction

Suggested files:

```text
scripts/ecc.js
scripts/install-apply.js
scripts/install-plan.js
scripts/doctor.js
scripts/repair.js
scr


# FILE: docs/HERMES-OPENCLAW-MIGRATION.md

# Hermes / OpenClaw -> ECC Migration

This document is the public migration guide for moving a Hermes or OpenClaw-style operator setup into the current ECC model.

The goal is not to reproduce a private operator workspace byte-for-byte.

The goal is to preserve the useful workflow surface:

- reusable skills
- stable automation entrypoints
- cross-harness portability
- schedulers / reminders / dispatch
- durable context and operator memory

while removing the parts that should stay private:

- secrets
- personal datasets
- account tokens
- local-only business artifacts

## Migration Thesis

Treat Hermes and OpenClaw as source systems, not as the final runtime.

ECC is the durable public system:

- skills
- agents
- commands
- hooks
- install surfaces
- session adapters
- ECC 2.0 control-plane work

Hermes and OpenClaw are useful inputs because they contain repeated operator workflows that can be distilled into ECC-native surfaces.

That means the shortest safe path is:

1. extract the reusable behavior
2. translate it into ECC-native skills, hooks, docs, or adapter work
3. keep secrets and personal data outside the repo

## Current Workspace Model

Use the current workspace split consistently:

- live code work happens in cloned repos under `~/GitHub`
- repo-specific active execution context lives in repo-level `WORKING-CONTEXT.md`
- broader non-code context can live in KB/archive layers
- durable cross-machine truth should prefer GitHub, Linear, and the knowledge base

Do not rebuild a shadow private workspace inside the public repo.

## Translation Map

### 1. Scheduler / cron layer

Source examples:

- `cron/scheduler.py`
- `jobs.py`
- recurring readiness or accountability loops

Translate into:

- Claude-native scheduling where available
- ECC hook / command automation for local repeatability
- ECC 2.0 scheduler work under issue `#1050`

Today, the repo already has the right public framing:

- hooks for low-latency repo-local automation
- commands for explicit operator actions
- ECC 2.0 as the future long-lived scheduling/control plane

### 2. Gateway / dispatch layer

Source examples:

- Hermes gateway
- mobile dispatch / remote nudges
- operator routing between active sessions

Translate into:

- ECC session adapter and control-plane work
- orchestration/session inspection commands
- ECC 2.0 control-plane backlog under:
  - `#1045`
  - `#1046`
  - `#1047`
  - `#1048`

The public repo should describe the adapter boundary and control-plane model, not pretend the remote operator shell is already fully GA.

### 3. Memory layer

Source examples:

- `memory_tool.py`
- local operator memory
- business / ops context stores

Translate into:

- `knowledge-ops`
- repo `WORKING-CONTEXT.md`
- GitHub / Linear / KB-backed durable context
- future deep memory work under `#1049`

The important distinction is:

- repo execution context belongs near the repo
- broader non-code memory belongs in KB/archive systems
- the public repo should document the boundary, not store private memory dumps

### 4. Skill layer

Source examples:

- Hermes skills
- OpenClaw skills
- generated operator playbooks

Translate into:

- ECC-native top-level skills when the workflow is reusable
- docs/examples when the content is only a template
- hooks or commands when the behavior is procedural rather than knowledge-shaped

Recent examples already salvaged this way:

- `knowledge-ops`
- `github-ops`
- `hookify-rules`
- `automation-audit-ops`
- `email-ops`
- `finance-billing-ops`
- `messages-ops`
- `research-ops`
- `terminal-ops`
- `ecc-tools-cost-audit`

### 5. Tool / service layer

Source examples:

- custom service wrappers
- API-key-backed local tools
- browser automation glue

Translate into:

- MCP-backed surfaces when a connector exists
- ECC-native operator skills when the workflow logic is the real asset
- adapter/control-plane work when the missing piece is session/runtime coordination

Do not import opaque third-party runtimes into ECC just because a private workflow depended on them.

If a workflow is valuable:

1. understand the behavior
2. rebuild the minimum ECC-native version
3. document the auth/connectors required locally

## What Already Exists Publicly

The current repo already covers meaningful parts of the migration:

- ECC 2.0 adapter/control-plane discovery docs
- orchestration/session inspection substrate
- operator workflow skills
- cost / billing / workflow audit skills
- cross-harness install surfaces
- AgentShield for config and agent-surface scanning

This means the migration problem is no longer "start from zero."

It is mostly:

- distilling missing private workflows
- clarifying public docs
- continuing the ECC 2.0 operator/control-plane buildout

ECC 2.0 now ships a bounded migration audit entrypoint:

- `ecc migrate audit --source ~/.hermes`
- `ecc migrate plan --source ~/.hermes --output migration-plan.md`
- `ecc migrate scaffold --source ~/.hermes --output-dir migration-artifacts`
- `ecc migrate import-skills --source ~/.hermes --output-dir migration-artifacts/skills`
- `ecc migrate import-tools --source ~/.hermes --output-dir migration-artifacts/tools`
- `ecc migrate import-plugins --source ~/.hermes --output-dir migration-artifacts/plugins`
- `ecc migrate import-schedules --source ~/.hermes --dry-run`
- `ecc migrate import-remote --source ~/.hermes --dry-run`
- `ecc migrate import-env --source ~/.hermes --dry-run`
- `ecc migrate import-memory --source ~/.hermes`

Use that first to inventory the legacy workspace and map detected surfaces onto the current ECC2 scheduler, remote dispatch, memory graph, templates, and manual-translation lanes.

## What Still Belongs In Backlog

The remaining large migration themes are already tracked:

- `#1051` Hermes/OpenClaw migration
- `#1049` deep memory layer
- `#1050` autonomous scheduling
- `#1048` universal harness compatibility layer
- `#1046` agent orchestrator
- `#1045` multi-session TUI manager
- `#1047` visual worktree manager

That is the rig


# FILE: docs/skill-adaptation-policy.md

# Skill Adaptation Policy

ECC accepts ideas from outside repos, but shipped skills need to become ECC-native surfaces.

## Default Rule

When a contribution starts from another open-source repo, prompt pack, plugin, harness, or personal config:

- copy the underlying idea, workflow, or structure
- adapt it to ECC's current install surfaces, validation flow, and repo conventions
- remove unnecessary external branding, dependency assumptions, and upstream-specific framing

The goal is reuse without turning ECC into a thin wrapper around someone else's runtime.

## When To Keep The Original Name

Keep the original skill name only when all of the following are true:

- the contribution is close to a direct port
- the name is already descriptive and neutral
- the surface still behaves like the upstream concept
- there is no better ECC-native name already in the repo

Examples:

- framework names like `nestjs-patterns`
- protocol or product names that are the subject matter, not the vendor pitch

## When To Rename

Rename the skill when ECC meaningfully expands, narrows, or repackages the original work.

Typical triggers:

- ECC adds substantial new behavior, structure, or guidance
- the original name is vendor-forward or community-brand-forward instead of workflow-forward
- the contribution overlaps an existing ECC surface and needs a clearer boundary
- the contribution now fits as a capability, operator workflow, or policy layer rather than a literal port

Examples:

- keep a reusable graph primitive as `social-graph-ranker`, but make broader workflow layers `lead-intelligence` or `connections-optimizer`
- prefer ECC-native names like `product-capability` over vague imported planning labels if the scope changed materially

## Dependency Policy

ECC prefers the narrowest native surface that gets the job done:

- `rules/` for deterministic constraints
- `skills/` for on-demand workflows
- MCP when a long-lived interactive tool boundary is justified
- local scripts/CLI for deterministic one-shot execution
- direct APIs when the remote call is narrow and does not justify MCP

Avoid shipping a skill that exists mainly to tell users to install or trust an unvetted third-party package.

If external functionality is worth keeping:

- vendor or recreate the relevant logic inside ECC when practical
- or keep the integration optional and clearly marked as external
- never let a new external dependency become the default path without explicit justification

## Review Questions

Before merging a contributed skill, answer these:

1. Is this a real reusable surface in ECC, or just documentation for another tool?
2. Does the current name still match the ECC-shaped surface?
3. Is there already an ECC skill that owns most of this behavior?
4. Are we importing a concept, or importing someone else's product identity?
5. Would an ECC user understand the purpose of this skill without knowing the upstream repo?

If those answers are weak, adapt more, narrow the scope, or do not ship it.



# FILE: docs/SELECTIVE-INSTALL-DESIGN.md

# ECC Selective Install Design

## Purpose

This document defines the user-facing selective-install design for ECC.

It complements
`docs/SELECTIVE-INSTALL-ARCHITECTURE.md`, which focuses on internal runtime
architecture and code boundaries.

This document answers the product and operator questions first:

- how users choose ECC components
- what the CLI should feel like
- what config file should exist
- how installation should behave across harness targets
- how the design maps onto the current ECC codebase without requiring a rewrite

## Problem

Today ECC still feels like a large payload installer even though the repo now
has first-pass manifest and lifecycle support.

Users need a simpler mental model:

- install the baseline
- add the language packs they actually use
- add the framework configs they actually want
- add optional capability packs like security, research, or orchestration

The selective-install system should make ECC feel composable instead of
all-or-nothing.

In the current substrate, user-facing components are still an alias layer over
coarser internal install modules. That means include/exclude is already useful
at the module-selection level, but some file-level boundaries remain imperfect
until the underlying module graph is split more finely.

## Goals

1. Let users install a small default ECC footprint quickly.
2. Let users compose installs from reusable component families:
   - core rules
   - language packs
   - framework packs
   - capability packs
   - target/platform configs
3. Keep one consistent UX across Claude, Cursor, Antigravity, Codex, and
   OpenCode.
4. Keep installs inspectable, repairable, and uninstallable.
5. Preserve backward compatibility with the current `ecc-install typescript`
   style during rollout.

## Non-Goals

- packaging ECC into multiple npm packages in the first phase
- building a remote marketplace
- full control-plane UI in the same phase
- solving every skill-classification problem before selective install ships

## User Experience Principles

### 1. Start Small

A user should be able to get a useful ECC install with one command:

```bash
ecc install --target claude --profile core
```

The default experience should not assume the user wants every skill family and
every framework.

### 2. Build Up By Intent

The user should think in terms of:

- "I want the developer baseline"
- "I need TypeScript and Python"
- "I want Next.js and Django"
- "I want the security pack"

The user should not have to know raw internal repo paths.

### 3. Preview Before Mutation

Every install path should support dry-run planning:

```bash
ecc install --target cursor --profile developer --with lang:typescript --with framework:nextjs --dry-run
```

The plan should clearly show:

- selected components
- skipped components
- target root
- managed paths
- expected install-state location

### 4. Local Configuration Should Be First-Class

Teams should be able to commit a project-level install config and use:

```bash
ecc install --config ecc-install.json
```

That allows deterministic installs across contributors and CI.

## Component Model

The current manifest already uses install modules and profiles. The user-facing
design should keep that internal structure, but present it as four main
component families.

Near-term implementation note: some user-facing component IDs still resolve to
shared internal modules, especially in the language/framework layer. The
catalog improves UX immediately while preserving a clean path toward finer
module granularity in later phases.

### 1. Baseline

These are the default ECC building blocks:

- core rules
- baseline agents
- core commands
- runtime hooks
- platform configs
- workflow quality primitives

Examples of current internal modules:

- `rules-core`
- `agents-core`
- `commands-core`
- `hooks-runtime`
- `platform-configs`
- `workflow-quality`

### 2. Language Packs

Language packs group rules, guidance, and workflows for a language ecosystem.

Examples:

- `lang:typescript`
- `lang:python`
- `lang:go`
- `lang:java`
- `lang:rust`

Each language pack should resolve to one or more internal modules plus
target-specific assets.

### 3. Framework Packs

Framework packs sit above language packs and pull in framework-specific rules,
skills, and optional setup.

Examples:

- `framework:react`
- `framework:nextjs`
- `framework:django`
- `framework:springboot`
- `framework:laravel`

Framework packs should depend on the correct language pack or baseline
primitives where appropriate.

### 4. Capability Packs

Capability packs are cross-cutting ECC feature bundles.

Examples:

- `capability:security`
- `capability:research`
- `capability:orchestration`
- `capability:media`
- `capability:content`

These should map onto the current module families already being introduced in
the manifests.

## Profiles

Profiles remain the fastest on-ramp.

Recommended user-facing profiles:

- `core`
  minimal baseline, safe default for most users trying ECC
- `developer`
  best default for active software engineering work
- `security`
  baseline plus security-heavy guidance
- `research`
  baseline plus research/content/investigation tools
- `full`
  everything classified and currently supported

Profiles should be composable with additional `--with` and `--without` flags.

Example:

```bash
ecc install --target claude --profile developer --with lang:typescript --with framework:nextjs --without capability:orchestration
```

## Proposed CLI Design

### Primary Commands

```bash
ecc install
ecc plan
ecc list-installed
ecc doctor
ecc repair
ecc uninstall
ecc catalog
```

### Install CLI

Recommended shape:

```bash
ecc install [--target <target>] [--profile <name>] [--with <component>]... [--without <component>]... [--config <path>] [--dry-run] [--json]
```

Examples:

```bash
ecc install --target claude --profile core
ecc install --target cursor --profile developer --with lang:typescript --with framework:nextjs
ecc install --target antigravity --wit


# FILE: docs/capability-surface-selection.md

# Capability Surface Selection

Use this as the routing guide when deciding whether a capability belongs in a rule, a skill, an MCP server, or a plain CLI/API workflow.

ECC does not treat these surfaces as interchangeable. The goal is to put each capability in the narrowest surface that preserves correctness, keeps token cost under control, and does not create unnecessary runtime or supply-chain drag.

## The Short Version

- `rules/` are for deterministic, always-on constraints that should be injected when a path or event matches.
- `skills/` are for on-demand workflows, richer playbooks, and token-expensive guidance that should load only when relevant.
- `MCP` is for interactive structured capabilities that benefit from a long-lived tool/resource surface across sessions or clients.
- local `CLI` or repo scripts are for simple deterministic actions that do not need a persistent server.
- direct `API` calls inside a skill are for narrow remote actions where a full MCP server would be heavier than the problem.

## Decision Order

Ask these questions in order:

1. Should this happen every time a path or event matches, with no model judgment involved?
   - Use a `rule`.
2. Is this mostly a playbook, workflow, or advisory layer that should load only when the task actually needs it?
   - Use a `skill`.
3. Does the capability need a structured interactive tool/resource interface that multiple harnesses or clients should call repeatedly?
   - Use `MCP`.
4. Is it a simple local action that can run as a script without keeping a server alive?
   - Use a local `CLI` entrypoint or repo script, then wrap it with a skill if needed.
5. Is it just one narrow remote integration step inside a larger workflow?
   - Call the external `API` directly from the skill or script.

## Surface-by-Surface Guidance

### Rules

Use rules for:

- path-scoped coding invariants
- safety floors and permission constraints
- harness/runtime constraints that should always apply
- deterministic reminders that should not depend on model discretion

Do not use rules for:

- large playbooks that would bloat every matching edit
- optional workflows
- expensive domain context that only matters some of the time

### Skills

Use skills for:

- multi-step workflows
- judgment-heavy guidance
- domain playbooks that are expensive enough to load only on demand
- orchestration across scripts, APIs, MCP tools, and adjacent skills

Do not use skills as a dumping ground for static invariants that really want deterministic routing.

### MCP

Use MCP when the capability benefits from:

- structured tool inputs/outputs
- reusable resources or prompts
- repeated cross-client usage
- a stable interface that should work across Claude Code, Codex, Cursor, OpenCode, and related harnesses
- a long-lived server process being worth the operational overhead

Avoid MCP when:

- the job is a one-shot local command
- the only thing the server would do is shell out once
- the server adds more install/runtime burden than product value

### CLI / Repo Scripts

Prefer a local script or CLI when:

- the action is deterministic
- startup is cheap
- the workflow is mostly local
- there is no benefit to exposing a persistent tool/resource surface

This is often the right choice for:

- lint/test/build wrappers
- local transforms
- small installers
- content generation that runs once per invocation

### Direct API Calls

Prefer direct API calls inside an existing skill or script when:

- the integration is narrow
- the remote action is part of a larger workflow
- you do not need a reusable transport surface yet

If the same remote integration becomes central, repeated, and multi-client, that is the signal to graduate it into an MCP surface.

## Cost and Reliability Bias

When two options are both viable:

- prefer the smaller runtime surface
- prefer the lower token overhead
- prefer the path with fewer external moving parts
- prefer ECC-native packaging over introducing another third-party dependency

Do not normalize external plugin or package dependencies as first-class ECC surfaces unless the capability is clearly worth the maintenance, security, and install burden.

## Repo Policy

When bringing in ideas from external repos:

- copy the underlying idea, not the external dependency
- repackage it as an ECC-native rule, skill, script, or MCP surface
- rename it if the functionality has been materially expanded or reshaped for ECC
- avoid shipping instructions that require users to install unrelated third-party packages unless that dependency is intentional, audited, and central to the workflow

## Examples

- A backend auth invariant that should always apply to `api/**` edits:
  - `rule`
- A deeper API design and pagination playbook:
  - `skill`
- A reusable remote search surface used across multiple harnesses:
  - `MCP`
- A one-shot repo analyzer that reads local files and writes a report:
  - local `CLI` or script, optionally wrapped by a `skill`
- A single billing-portal session creation step inside a broader customer-ops workflow:
  - direct `API` call inside the workflow

## Practical Heuristic

If you are unsure, start smaller:

- start with a `rule` for deterministic invariants
- start with a `skill` for guidance/workflow
- start with a script for one-shot execution
- promote to `MCP` only when the structured server boundary is clearly paying for itself



# FILE: docs/QWEN-GUIDE.md

# Qwen CLI Adapter Guide

ECC can install its managed command, agent, skill, rule, and MCP surfaces into the Qwen CLI home directory.

## Install

From the ECC repository root:

```bash
./install.sh --target qwen --profile minimal
```

Preview a larger install before copying files:

```bash
./install.sh --target qwen --profile full --dry-run
```

The Qwen adapter writes into `~/.qwen/` and records managed file ownership in `~/.qwen/ecc-install-state.json`.

## Installed Layout

The managed install can populate:

```text
~/.qwen/
  QWEN.md
  agents/
  commands/
  mcp-configs/
  rules/
  skills/
  ecc-install-state.json
```

The installer preserves the source layout for rules, so language rule sets stay under paths such as `~/.qwen/rules/common/` and `~/.qwen/rules/typescript/`.

## Updating

Rerun the same install command after pulling ECC updates. The installer uses the install-state file to update ECC-managed files without claiming unrelated user files in `~/.qwen/`.

## Uninstalling

Use the managed uninstall path rather than deleting the whole Qwen directory:

```bash
node scripts/uninstall.js --target qwen
```

That removes files recorded in `~/.qwen/ecc-install-state.json` and leaves unrelated Qwen configuration alone.

## Scope

This target is intentionally narrower than stale PR #1352. It ports the maintainable Qwen install-target intent onto the current selective installer and avoids unverified hook-runtime claims until Qwen's hook/event contract is confirmed.



# FILE: docs/continuous-learning-v2-spec.md

# Continuous Learning v2 Spec

This document captures the v2 continuous-learning architecture:

1. Hook-based observation capture
2. Background observer analysis loop
3. Instinct scoring and persistence
4. Evolution of instincts into reusable skills/commands

Primary implementation lives in:
- `skills/continuous-learning-v2/`
- `scripts/hooks/`

Use this file as the stable reference path for docs and translations.

