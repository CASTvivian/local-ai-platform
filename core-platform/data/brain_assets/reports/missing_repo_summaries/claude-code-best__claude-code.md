# Missing Repo Summary Source: claude-code-best/claude-code

- URL: https://github.com/claude-code-best/claude-code
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/claude-code-best__claude-code
- Clone Status: cloned
- Language: TypeScript
- Stars: 18111
- Topics: 
- Description: 原汁原昧 Claude Code 可运行,可构建, 可调试版; 生产级工程化, 企业级可靠性; 安全无毒, 内存泄露修复

## Extracted README / Docs / Examples



# FILE: README.md

# Claude Code Best V5 (CCB)

[![GitHub Stars](https://img.shields.io/github/stars/claude-code-best/claude-code?style=flat-square&logo=github&color=yellow)](https://github.com/claude-code-best/claude-code/stargazers)
[![GitHub Contributors](https://img.shields.io/github/contributors/claude-code-best/claude-code?style=flat-square&color=green)](https://github.com/claude-code-best/claude-code/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/claude-code-best/claude-code?style=flat-square&color=orange)](https://github.com/claude-code-best/claude-code/issues)
[![GitHub License](https://img.shields.io/github/license/claude-code-best/claude-code?style=flat-square)](https://github.com/claude-code-best/claude-code/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/claude-code-best/claude-code?style=flat-square&color=blue)](https://github.com/claude-code-best/claude-code/commits/main)
[![Bun](https://img.shields.io/badge/runtime-Bun-black?style=flat-square&logo=bun)](https://bun.sh/)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=flat-square&logo=discord)](https://discord.gg/uApuzJWGKX)

> Which Claude do you like? The open source one is the best.

牢 A (Anthropic) 官方 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI 工具的源码反编译/逆向还原项目。目标是将 Claude Code 大部分功能及工程化能力复现 (问就是老佛爷已经付过钱了)。虽然很难绷, 但是它叫做 CCB(踩踩背)... 而且, 我们实现了企业版或者需要登陆 Claude 账号才能使用的特性, 实现技术普惠

> 我们将会在五一期间进行整个代码仓库的 lint 规范化, 这个期间提交的 PR 可能会有非常多的冲突, 所以大的功能请尽量在这之前提交哈

[文档在这里, 支持投稿 PR](https://ccb.agent-aura.top/) | [留影文档在这里](./Friends.md) | [Discord 群组](https://discord.gg/uApuzJWGKX)


| 特性                        | 说明                                                                                                                         | 文档                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude 群控技术**         | Pipe IPC 多实例协作：同机 main/sub 自动编排 + LAN 跨机器零配置发现与通讯，`/pipes` 选择面板 + `Shift+↓` 交互 + 消息广播路由 | [Pipe IPC](https://ccb.agent-aura.top/docs/features/uds-inbox) / [LAN](https://ccb.agent-aura.top/docs/features/lan-pipes)                |
| **ACP 协议一等一支持**      | 支持接入 Zed、Cursor 等 IDE，支持会话恢复、Skills、权限桥接                                                                  | [文档](https://ccb.agent-aura.top/docs/features/acp-zed)                                                                                  |
| **Remote Control 私有部署** | Docker 自托管远程界面, 可以手机上看 CC                                                                                       | [文档](https://ccb.agent-aura.top/docs/features/remote-control-self-hosting)                                                              |
| **Langfuse 监控**           | 企业级 Agent 监控, 可以清晰看到每次 agent loop 细节, 可以一键转化为数据集                                                    | [文档](https://ccb.agent-aura.top/docs/features/langfuse-monitoring)                                                                      |
| **Web Search**              | 内置网页搜索工具, 支持 bing 和 brave 搜索                                                                                    | [文档](https://ccb.agent-aura.top/docs/features/web-browser-tool)                                                                         |
| **Poor Mode**               | 穷鬼模式，关闭记忆提取和键入建议,大幅度减少并发请求                                                                          | /poor 可以开关                                                                                                                            |
| **Channels 频道通知**       | MCP 服务器推送外部消息到会话（飞书/Slack/Discord/微信等），`--channels plugin:name@marketplace` 启用                         | [文档](https://ccb.agent-aura.top/docs/features/channels)                                                                                 |
| **自定义模型供应商**        | OpenAI/Anthropic/Gemini/Grok 兼容  (`/login`)                                                                                          | [文档](https://ccb.agent-aura.top/docs/features/all-features-guide)                                                                        |
| Voice Mode                  | 语音输入，支持豆包语言输入（`/voice doubao`）                                                                   | [文档](https://ccb.agent-aura.top/docs/features/voice-mode)                                                                               |
| Computer Use                | 屏幕截图、键鼠控制                                                                                                           | [文档](https://ccb.agent-aura.top/docs/features/computer-use)                                                                             |
| Chrome Use                  | 浏览器自动化、表单填写、数据抓取                                                                                             | [自托管](https://ccb.agent-aura.top/docs/features/chrome-use-mcp) [原生版](https://ccb.agent-aura.top/docs/features/claude-in-chrome-mcp) |
| Sentry                      | 企业级错误追踪                                                                                                               | [文档](https://ccb.agent-aura.top/docs/internals/sentry-setup)                                                                            |
| GrowthBook                  | 企业级特性开关                                                                                                               | [文档](https://ccb.agent-aura.top/docs/internals/growthbook-adapter)                                                                      |
| /dream 记忆整理             | 自动整理和优化记忆文件                                                                                                       | [文档](https://ccb.agent-aura.top/docs/features/auto-dream)                                                                               |

- 🚀 [想要启动项目](#-快速开始源码版)
- 🐛 [想要调试项目](#vs-code-调试)
- 📖 [想要学习项目](#teach-me-学习项目)

## ⚡ 快速开始(安装版)

不用克隆仓库, 从 NPM 下载后, 直接使用

```sh
npm i -g claude-code-best

# bun 安装比较多问题, 推荐 npm 装
# bun  i -g claude-code-best
# bun pm -g trust claude-code-best @claude-code-best/mcp-chrome-bridge

ccb # 以 nodejs 打开 claude code
ccb-bun # 以 bun 形态打开
ccb update # 更新到最新版本
CLAUDE_BRIDGE_BASE_URL=https://remote-control.claude-code-best.win/ CLAUDE_BRIDGE_OAUTH_TOKEN=test-my-key ccb --remote-control # 我们有自部署的远程控制
```

> **安装/更新失败？** 先 `npm rm -g claude-code-best` 清理旧版本，再 `npm i -g claude-code-best@latest`。仍失败则指定版本号：`npm i -g claude-code-best@<版本号>`

## ⚡ 快速开始(源码版)

### ⚙️ 环境要求

一定要最新版本的 bun 啊, 不然一堆奇奇怪怪的 BUG!!! bun upgrade!!!

- 📦 [Bun](https://bun.sh/) >= 1.3.11

**安装 Bun：**

```bash
# Linux 和 macOS
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"
```

**安装后的操作：**

1. **让当前终端识别 `bun` 命令**

   安装脚本会把 `~/.bun/bin` 写入对应的 shell 配置文件。macOS 默认 zsh 环境通常会看到：

   ```text
   Added "~/.bun/bin" to $PATH in "~/.zshrc"
   ```

   可以按安装脚本提示重启当前 shell：

   ```bash
   exec /bin/zsh
   ```

   如果你使用 bash，重新加载 bash 配置：

   ```bash
   source ~/.bashrc
   ```

   Windows PowerShell 用户关闭并重新打开 PowerShell 即可。

2. **验证 Bun 是否可用**

   ```bash
   bun --help
   bun --version
   ```

3. **如果已经安装过 Bun，更新到最新版本**

   ```bash
   bun upgrade
   ```

- ⚙️ 常规的配置 CC 的方式, 各大提供商都有自己的配置方式

### 📍 命令执行位置

- 安装或检查 Bun 的命令可以在任意目录执行：
  `curl -fsSL https://bun.sh/install | bash`、`bun --help`、`bun --version`、`bun upgrade`
- 安装本项目依赖、启动开发模式、构建项目时，必须先进入本仓库根目录，也就是包含 `package.json` 的目录。

### 📥 安装

```bash
cd /path/to/claude-code
bun install
```

### ▶️ 运行

```bash
# 开发模式, 看到版本号 888 说明就是对了
bun run dev

# 构建
bun run build
```

构建采用 code splitting 多文件打包（`build.ts`），产物输出到 `dist/` 目录（入口 `dist/cli.js` + 约 450 个 chunk 文件）。

构建出的版本 bun 和 node 都可以启动, 你 publish 到私有源可以直接启动

如果遇到 bug 请直接提一个 issues, 我们优先解决

### 👤 新人配置 /login

首次运行后，在 REPL 中输入 `/login` 命令进入登录配置界面，选择 **Anthropic Compatible** 即可对接第三方 API 兼容服务（无需 Anthropic 官方账号）。
选择 OpenAI 和 Gemini 对应的栏目都是支持相应协议的

需要填写的字段：


| 📌 字段      | 📝 说明       | 💡 示例                      |
| ------------ | ------------- | ---------------------------- |
| Base URL     | API 服务地址  | `https://api.example.com/v1` |
| API Key      | 认证密钥      | `sk-xxx`                     |
| Haiku Model  | 快速模型 ID   | `claude-haiku-4-5-20251001`  |
| Sonnet Model | 均衡模型 ID   | `claude-sonnet-4-6`          |
| Opus Model   | 高性能模型 ID | `claude-opus-4-6`            |

- ⌨️ **Tab / Shift+Tab** 切换字段，**Enter** 确认并跳到下一个，最后一个字段按 Enter 保存

> ℹ️ 支持所有 Anthropic API 兼容服务（如 OpenRouter、AWS Bedrock 代理等），只要接口兼容 Messages API 即可。

## Feature Flags

所有功能开关通过 `FEATURE_<FLAG_NAME>=1` 环境变量启用，例如：

```bash
FEATURE_BUDDY=1 FEATURE_FORK_SUBAGENT=1 bun run dev
```

各 Feature 的详细说明见 [`docs/features/`](docs/features/) 目录，欢迎投稿补充。

## VS Code 调试

TUI (REPL) 模式需要真实终端，无法直接通过 VS Code launch 启动调试。使用 **attach 模式**：

### 步骤

1. **终端启动 inspect 服务**：

   ```bash
   bun run dev:inspect
   ```

   会输出类似 `ws://localhost:8888/xxxxxxxx` 的地址。
2. **VS Code 附着调试器**：

   - 在 `src/` 文件中打断点
   - F5 → 选择 **"Attach to Bun (TUI debug)"**

## Teach Me 学习项目

我们新加了一个 teach-me skills, 通过问答式引导帮你理解这个项目的任何模块。(调整 [sigma skill 而来](https://github.com/sanyuan0704/sanyuan-skills))

```bash
# 在 REPL 中直接输入
/teach-me Claude Code 架构
/teach-me React Ink 终端渲染 --level beginner
/teach-me Tool 系统 --resume
```

### 它能做什么

- **诊断水平** — 自动评估你对相关概念的掌握程度，跳过已知的、聚焦薄弱的
- **构建学习路径** — 将主题拆解为 5-15 个原子概念，按依赖排序逐步推进
- **苏格拉底式提问** — 用选项引导思考，而非直接给答案
- **错误概念追踪** — 发现并纠正深层误解
- **断点续学** — `--resume` 从上次进度继续

### 学习记录

学习进度保存在 `.claude/skills/teach-me/` 目录下，支持跨主题学习者档案。

## 相关文档及网站

- **在线文档（Mintlify）**: [ccb.agent-aura.top](https://ccb.agent-aura.top/) — 文档源码位于 [`docs/`](docs/) 目录，欢迎投稿 PR
- **DeepWiki**: [https://deepwiki.com/claude-code-best/claude-code](https://deepwiki.com/claude-code-best/claude-code

# FILE: README_EN.md

# Claude Code Best V5 (CCB)

[![GitHub Stars](https://img.shields.io/github/stars/claude-code-best/claude-code?style=flat-square&logo=github&color=yellow)](https://github.com/claude-code-best/claude-code/stargazers)
[![GitHub Contributors](https://img.shields.io/github/contributors/claude-code-best/claude-code?style=flat-square&color=green)](https://github.com/claude-code-best/claude-code/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/claude-code-best/claude-code?style=flat-square&color=orange)](https://github.com/claude-code-best/claude-code/issues)
[![GitHub License](https://img.shields.io/github/license/claude-code-best/claude-code?style=flat-square)](https://github.com/claude-code-best/claude-code/blob/main/LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/claude-code-best/claude-code?style=flat-square&color=blue)](https://github.com/claude-code-best/claude-code/commits/main)
[![Bun](https://img.shields.io/badge/runtime-Bun-black?style=flat-square&logo=bun)](https://bun.sh/)

> Which Claude do you like? The open source one is the best.

A reverse-engineered / decompiled source restoration of Anthropic's official [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI tool. The goal is to reproduce most of Claude Code's functionality and engineering capabilities. It's abbreviated as CCB.

[Documentation (Chinese)](https://ccb.agent-aura.top/) — PR contributions welcome.

Sponsor placeholder.

- [x] v1: Basic runability and type checking pass
- [x] V2: Complete engineering infrastructure
  - [ ] Biome formatting may not be implemented first to avoid code conflicts
  - [x] Build pipeline complete, output runnable on both Node.js and Bun
- [x] V3: Extensive documentation and documentation site improvements
- [x] V4: Large-scale test suite for improved stability
  - [x] Buddy pet feature restored [Docs](https://ccb.agent-aura.top/docs/features/buddy)
  - [x] Auto Mode restored [Docs](https://ccb.agent-aura.top/docs/safety/auto-mode)
  - [x] All features now configurable via environment variables instead of `bun --feature`
- [x] V5: Enterprise-grade monitoring/reporting, missing tools补全, restrictions removed
  - [x] Removed anti-distillation code
  - [x] Web search capability (using Bing) [Docs](https://ccb.agent-aura.top/docs/features/web-browser-tool)
  - [x] Debug mode support [Docs](https://ccb.agent-aura.top/docs/features/debug-mode)
  - [x] Disabled auto-updates
  - [x] Custom Sentry error reporting support [Docs](https://ccb.agent-aura.top/docs/internals/sentry-setup)
  - [x] Custom GrowthBook support (GB is open source — configure your own feature flag platform) [Docs](https://ccb.agent-aura.top/docs/internals/growthbook-adapter)
  - [x] Custom login mode — configure Claude models your way
- [ ] V6: Large-scale refactoring, full modular packaging
  - [ ] V6 will be a new branch; main branch will be archived as a historical version

> I don't know how long this project will survive. Star + Fork + git clone + .zip is the safest bet.
>
> This project updates rapidly — Opus continuously optimizes in the background, with new changes almost every few hours.
>
> Claude has burned over $1000, out of budget, switching to GLM to continue; @zai-org GLM 5.1 is quite capable.

## Quick Start

### Prerequisites

Make sure you're on the latest version of Bun, otherwise you'll run into all sorts of weird bugs. Run `bun upgrade`!

- [Bun](https://bun.sh/) >= 1.3.11

**Install Bun:**

```bash
# Linux and macOS
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
powershell -c "irm bun.sh/install.ps1 | iex"
```

**Post-installation steps:**

1. **Make `bun` available in the current terminal**

   The installer adds `~/.bun/bin` to the matching shell configuration file. On macOS with the default zsh shell, you may see:

   ```text
   Added "~/.bun/bin" to $PATH in "~/.zshrc"
   ```

   Restart the current shell as the installer suggests:

   ```bash
   exec /bin/zsh
   ```

   If you use bash, reload the bash configuration:

   ```bash
   source ~/.bashrc
   ```

   Windows PowerShell users can close and reopen PowerShell.

2. **Verify that Bun is available:**
   ```bash
   bun --help
   bun --version
   ```

3. **Update to latest version (if already installed):**
   ```bash
   bun upgrade
   ```

- Standard Claude Code configuration — each provider has its own setup method

### Command Execution Location

- Bun installation and checking commands can be run from any directory:
  `curl -fsSL https://bun.sh/install | bash`, `bun --help`, `bun --version`, `bun upgrade`
- Project dependency installation, development mode, and builds must be run from this repository root, the directory containing `package.json`.

### Install

```bash
cd /path/to/claude-code
bun install
```

### Run

```bash
# Dev mode — if you see version 888, it's working
bun run dev

# Build
bun run build
```

The build uses code splitting (`build.ts`), outputting to `dist/` (entry `dist/cli.js` + ~450 chunk files).

The build output runs on both Bun and Node.js — you can publish to a private registry and run directly.

If you encounter a bug, please open an issue — we'll prioritize it.

### First-time Setup /login

After the first run, enter `/login` in the REPL to access the login configuration screen. Select **Anthropic Compatible** to connect to third-party API-compatible services (no Anthropic account required).

Fields to fill in:

| Field | Description | Example |
|-------|-------------|---------|
| Base URL | API service URL | `https://api.example.com/v1` |
| API Key | Authentication key | `sk-xxx` |
| Haiku Model | Fast model ID | `claude-haiku-4-5-20251001` |
| Sonnet Model | Balanced model ID | `claude-sonnet-4-6` |
| Opus Model | High-performance model ID | `claude-opus-4-6` |

- **Tab / Shift+Tab** to switch fields, **Enter** to confirm and move to the next, press Enter on the last field to save
- Model fields auto-fill from current environment variables
- Configuration saves to `~/.claude/settings.json` under the `env` key, effective immediately

You can also edit `~/.claude/settings.json` directly:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.example.com/v1",
    "ANTHROPIC_AUTH_TOKEN": "sk-xxx",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "claude-haiku-4-5-20251001",
    "ANTHROPIC_DEFAULT_SONNET_MODEL": "claude-sonnet-4-6",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "claude-opus-4-6"
  }
}
```

> Supports all Anthropic API-compatible services (e.g., OpenRouter, AWS Bedrock proxies, etc.) as long as the interface is compatible with the Messages API.

## Feature Flags

All feature toggles are enabled via `FEATURE_<FLAG_NAME>=1` environment variables, for example:

```bash
FEATURE_BUDDY=1 FEATURE_FORK_SUBAGENT=1 bun run dev
```

See [`docs/features/`](docs/features/) for detailed descriptions of each feature. Contributions welcome.

## VS Code Debugging

The TUI (REPL) mode requires a real terminal and cannot be launched directly via VS Code's launch config. Use **attach mode**:

### Steps

1. **Start inspect server in terminal**:
   ```bash
   bun run dev:inspect
   ```
   This outputs an address like `ws://localhost:8888/xxxxxxxx`.

2. **Attach debugger from VS Code**:
   - Set breakpoints in `src/` files
   - Press F5 → select **"Attach to Bun (TUI debug)"**

## Documentation & Links

- **Online docs (Mintlify)**: [ccb.agent-aura.top](https://ccb.agent-aura.top/) — source in [`docs/`](docs/), PR contributions welcome
- **DeepWiki**: https://deepwiki.com/claude-code-best/claude-code

## Contributors

<a href="https://github.com/claude-code-best/claude-code/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=claude-code-best/claude-code" />
</a>

## Star History

<a href="https://www.star-history.com/?repos=claude-code-best%2Fclaude-code&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=claude-code-best%2Fclaude-code&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=claude-code-best%2Fclaude-code&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=claude-code-best%2Fclaude-code&type=date&legend=top-left" />
 </picture>
</a>

## License

This project is for educational and research purposes only. All rights to Claude Code belong to [Anthropic](https://www.anthropic.com/).


# FILE: docs/external-dependencies.md

# Claude Code 远程服务器依赖

> 只列出代码中实际发起网络请求的远程服务。本地服务、npm 包依赖、展示用 URL 不包含在内。

## 总览表

| # | 服务 | 远程端点 | 协议 | 状态 |
|---|---|---|---|---|
| 1 | Anthropic API | `api.anthropic.com` | HTTPS | 默认启用 |
| 2 | AWS Bedrock | `bedrock-runtime.*.amazonaws.com` | HTTPS | 需 `CLAUDE_CODE_USE_BEDROCK=1` |
| 3 | Google Vertex AI | `{region}-aiplatform.googleapis.com` | HTTPS | 需 `CLAUDE_CODE_USE_VERTEX=1` |
| 4 | Azure Foundry | `{resource}.services.ai.azure.com` | HTTPS | 需 `CLAUDE_CODE_USE_FOUNDRY=1` |
| 5 | OAuth (Anthropic) | `platform.claude.com`, `claude.com`, `claude.ai` | HTTPS | 用户登录时 |
| 6 | GrowthBook | `api.anthropic.com` (remoteEval) | HTTPS | 默认启用 |
| 7 | Sentry | 可配置 (`SENTRY_DSN`) | HTTPS | 需设环境变量 |
| 8 | Datadog | 可配置 (`DATADOG_LOGS_ENDPOINT`) | HTTPS | 需设环境变量 |
| 9 | OpenTelemetry Collector | 可配置 (`OTEL_EXPORTER_OTLP_ENDPOINT`) | gRPC/HTTP | 需设环境变量 |
| 10 | 1P Event Logging | `api.anthropic.com/api/event_logging/batch` | HTTPS | 默认启用 |
| 11 | BigQuery Metrics | `api.anthropic.com/api/claude_code/metrics` | HTTPS | 默认启用 |
| 12 | MCP Proxy | `mcp-proxy.anthropic.com` | HTTPS+WS | 使用 MCP 工具时 |
| 13 | MCP Registry | `api.anthropic.com/mcp-registry` | HTTPS | 查询 MCP 服务器时 |
| 14 | Web Search Pages | `www.bing.com`, `search.brave.com` | HTTPS | WebSearch 工具，可通过 `WEB_SEARCH_ADAPTER=bing|brave` 切换 |
| 15 | Google Cloud Storage (更新) | `storage.googleapis.com` | HTTPS | 版本检查 |
| 16 | GitHub Raw (Changelog/Stats) | `raw.githubusercontent.com` | HTTPS | 更新提示 |
| 17 | Claude in Chrome Bridge | `bridge.claudeusercontent.com` | WSS | Chrome 集成 |
| 18 | CCR Upstream Proxy | `api.anthropic.com` | WS | CCR 远程会话 |
| 19 | Voice STT | `api.anthropic.com/api/ws/...` | WSS | Voice Mode |
| 20 | Desktop App Download | `claude.ai/api/desktop/...` | HTTPS | 下载引导 |

---

## 详细说明

### 1. Anthropic Messages API

核心 LLM 推理服务，发送对话消息、接收流式响应。

- **端点**: `https://api.anthropic.com` (生产) / `https://api-staging.anthropic.com` (staging)
- **覆盖**: `ANTHROPIC_BASE_URL` 环境变量
- **认证**: API Key / OAuth Token
- **文件**: `src/services/api/client.ts`, `src/services/api/claude.ts`

### 2. AWS Bedrock

- **端点**: `bedrock-runtime.{region}.amazonaws.com`
- **认证**: AWS 凭证链 / `AWS_BEARER_TOKEN_BEDROCK`
- **文件**: `src/services/api/client.ts:153-190`, `src/utils/aws.ts`

### 3. Google Vertex AI

- **端点**: `{region}-aiplatform.googleapis.com`
- **认证**: `GoogleAuth` + `cloud-platform` scope
- **文件**: `src/services/api/client.ts:221-298`

### 4. Azure Foundry

- **端点**: `https://{resource}.services.ai.azure.com/anthropic/v1/messages`
- **认证**: API Key 或 Azure AD `DefaultAzureCredential`
- **文件**: `src/services/api/client.ts:191-220`

### 5. OAuth

OAuth 2.0 + PKCE 授权码流程。

- **端点**:
  - `https://platform.claude.com/oauth/authorize` — 授权页
  - `https://claude.com/cai/oauth/authorize` — Claude.ai 授权
  - `https://platform.claude.com/v1/oauth/token` — Token 交换
  - `https://api.anthropic.com/api/oauth/claude_cli/create_api_key` — 创建 API Key
  - `https://api.anthropic.com/api/oauth/claude_cli/roles` — 获取角色
  - `https://claude.ai/oauth/claude-code-client-metadata` — MCP 客户端元数据
  - `https://claude.fedstart.com` — FedStart 政府部署
- **文件**: `src/constants/oauth.ts`, `src/services/oauth/`

### 6. GrowthBook (功能开关)

- **端点**: `https://api.anthropic.com/` (remoteEval 模式) 或 `CLAUDE_GB_ADAPTER_URL`
- **SDK Keys**: `sdk-zAZezfDKGoZuXXKe` (外部), `sdk-xRVcrliHIlrg4og4` (ant prod), `sdk-yZQvlplybuXjYh6L` (ant dev)
- **文件**: `src/services/analytics/growthbook.ts`, `src/constants/keys.ts`

### 7. Sentry (错误追踪)

- **激活**: 设置 `SENTRY_DSN` (默认未配置)
- **行为**: 仅错误上报，自动过滤敏感 header
- **文件**: `src/utils/sentry.ts`

### 8. Datadog (日志)

- **激活**: 同时设 `DATADOG_LOGS_ENDPOINT` + `DATADOG_API_KEY` (默认未配置)
- **文件**: `src/services/analytics/datadog.ts`

### 9. OpenTelemetry Collector

- **激活**: `CLAUDE_CODE_ENABLE_TELEMETRY=1` 或 `OTEL_*` 环境变量
- **协议**: gRPC / HTTP / Protobuf，支持 OTLP 和 Prometheus 导出
- **文件**: `src/utils/telemetry/instrumentation.ts`

### 10. 1P Event Logging (内部事件)

- **端点**: `https://api.anthropic.com/api/event_logging/batch`
- **协议**: 批量导出 (10s 间隔, 每批 200 事件)
- **文件**: `src/services/analytics/firstPartyEventLoggingExporter.ts`

### 11. BigQuery Metrics

- **端点**: `https://api.anthropic.com/api/claude_code/metrics`
- **文件**: `src/utils/telemetry/bigqueryExporter.ts`

### 12. MCP Proxy

Anthropic 托管的 MCP 服务器代理。

- **端点**: `https://mcp-proxy.anthropic.com/v1/mcp/{server_id}`
- **认证**: Claude.ai OAuth tokens
- **文件**: `src/services/mcp/client.ts`, `src/constants/oauth.ts`

### 13. MCP Registry

获取官方 MCP 服务器列表。

- **端点**: `https://api.anthropic.com/mcp-registry/v0/servers?version=latest&visibility=commercial`
- **文件**: `src/services/mcp/officialRegistry.ts`

### 14. Web Search Pages

WebSearch 工具支持直接抓取 Bing 搜索结果页面，也支持通过 Brave 的 LLM Context API
获取搜索上下文；可通过 `WEB_SEARCH_ADAPTER=bing|brave` 显式切换后端。

- **Bing 端点**: `https://www.bing.com/search?q={query}&setmkt=en-US`
- **Brave 端点**: `https://api.search.brave.com/res/v1/llm/context?q={query}`
- **文件**:
  - `packages/builtin-tools/src/tools/WebSearchTool/adapters/bingAdapter.ts`
  - `packages/builtin-tools/src/tools/WebSearchTool/adapters/braveAdapter.ts`

另外还有 Domain Blocklist 查询:
- **端点**: `https://api.anthropic.com/api/web/domain_info?domain={domain}`
- **文件**: `packages/builtin-tools/src/tools/WebFetchTool/utils.ts`

### 15. Google Cloud Storage (自动更新)

- **端点**: `https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases`
- **文件**: `src/utils/autoUpdater.ts`

### 16. GitHub Raw Content

- **端点**: `https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md`
- **端点**: `https://raw.githubusercontent.com/anthropics/claude-plugins-official/refs/heads/stats/stats/plugin-installs.json`
- **文件**: `src/utils/releaseNotes.ts`, `src/utils/plugins/installCounts.ts`

### 17. Claude in Chrome Bridge

- **端点**: `wss://bridge.claudeusercontent.com` (生产) / `wss://bridge-staging.claudeusercontent.com` (staging)
- **文件**: `src/utils/claudeInChrome/mcpServer.ts`

### 18. CCR

# FILE: docs/lsp-integration.md

# LSP Integration

Claude Code 内置了 Language Server Protocol (LSP) 集成，提供代码智能功能（跳转定义、查找引用、悬停信息、文档符号等）和被动的诊断反馈。

## 快速开始

### 1. 安装 LSP 插件

在 Claude Code REPL 中使用 `/plugin` 命令搜索并安装 LSP 插件：

```
/plugin
```

搜索 `lsp`，找到对应语言的插件（如 `typescript-lsp`），选择安装。

安装后运行 `/reload-plugins` 使插件生效。

LSP 插件安装后，后台的 LSP Server Manager 会自动加载并启动对应的语言服务器，无需手动配置。

### 2. 启用 LSP Tool

LSP Tool 需要通过环境变量显式启用，Claude 才能主动发起代码智能查询：

```bash
ENABLE_LSP_TOOL=1 bun run dev
```

不启用时，LSP 服务器仍然在后台运行并推送被动的诊断反馈（类型错误等）。

## 自动推荐

除了手动 `/plugin` 搜索安装外，Claude Code 会在编辑文件时自动检测：

1. 监听 `fileHistory.trackedFiles`，发现有新文件被编辑
2. 扫描已安装的 marketplace，找到声明支持该文件扩展名的 LSP 插件
3. 检查系统上是否已安装对应的 LSP 二进制（如 `typescript-language-server`）
4. 满足条件时弹出推荐对话框，可选择安装

```
┌───── LSP Plugin Recommendation ─────────────┐
│                                               │
│  LSP provides code intelligence like          │
│  go-to-definition and error checking          │
│                                               │
│  Plugin: typescript-lsp                       │
│  Triggered by: .ts files                     │
│                                               │
│  Would you like to install this LSP plugin?   │
│                                               │
│  > Yes, install typescript-lsp               │
│    No, not now                                │
│    Never for typescript-lsp                   │
│    Disable all LSP recommendations            │
└───────────────────────────────────────────────┘
```

- 30 秒不操作自动关闭（算作 "No"）
- 选 "Never" 不再推荐该插件
- 选 "Disable" 关闭所有 LSP 推荐
- 连续忽略 5 次后自动禁用推荐

## 架构概览

```
┌─────────────────────────────────────────────────────┐
│                    LSP Tool                         │
│  packages/builtin-tools/src/tools/LSPTool/LSPTool.ts│
│  (Claude 可调用的工具，9 种操作)                       │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              LSP Server Manager (Singleton)          │
│  src/services/lsp/manager.ts                        │
│  - initializeLspServerManager()                     │
│  - reinitializeLspServerManager()                   │
│  - shutdownLspServerManager()                       │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│           LSP Server Manager (实例)                   │
│  src/services/lsp/LSPServerManager.ts               │
│  - 管理多个 LSPServerInstance                        │
│  - 按文件扩展名路由请求                               │
│  - 文件同步 (didOpen/didChange/didSave/didClose)     │
└──────────────────────┬──────────────────────────────┘
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ LSPServer    │ │ LSPServer    │ │ LSPServer    │
│ Instance     │ │ Instance     │ │ Instance     │
│ (typescript) │ │ (python)     │ │ (rust...)    │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
┌──────▼───────┐ ┌──────▼───────┐ ┌──────▼───────┐
│ LSPClient    │ │ LSPClient    │ │ LSPClient    │
│ (JSON-RPC)   │ │ (JSON-RPC)   │ │ (JSON-RPC)   │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
  子进程 (stdio)    子进程 (stdio)    子进程 (stdio)
```

### 被动诊断反馈

```
LSP Server ──publishDiagnostics──▶ passiveFeedback.ts
                                          │
                                          ▼
                                   LSPDiagnosticRegistry
                                   (去重、容量限制)
                                          │
                                          ▼
                                   Attachment System
                                   (异步注入到对话)
```

LSP 服务器会异步推送 `textDocument/publishDiagnostics` 通知，经去重和容量限制后作为 attachment 注入到 Claude 的对话上下文中。

## 核心模块

| 文件 | 职责 |
|------|------|
| `src/services/lsp/manager.ts` | 全局单例，初始化/重初始化/关闭生命周期管理 |
| `src/services/lsp/LSPServerManager.ts` | 多服务器管理，按文件扩展名路由，文件同步 |
| `src/services/lsp/LSPServerInstance.ts` | 单个 LSP 服务器实例生命周期（启动/停止/重启/健康检查） |
| `src/services/lsp/LSPClient.ts` | JSON-RPC 通信层（基于 `vscode-jsonrpc`），子进程管理 |
| `src/services/lsp/config.ts` | 从插件加载 LSP 服务器配置 |
| `src/services/lsp/LSPDiagnosticRegistry.ts` | 诊断信息注册、去重、容量限制 |
| `src/services/lsp/passiveFeedback.ts` | 注册 `publishDiagnostics` 通知处理器 |
| `packages/builtin-tools/src/tools/LSPTool/LSPTool.ts` | LSP Tool 实现（暴露给 Claude） |
| `packages/builtin-tools/src/tools/LSPTool/schemas.ts` | 输入 schema（9 种操作的 discriminated union） |
| `packages/builtin-tools/src/tools/LSPTool/formatters.ts` | 各操作结果的格式化 |
| `packages/builtin-tools/src/tools/LSPTool/prompt.ts` | Tool 描述文本 |
| `src/utils/plugins/lspPluginIntegration.ts` | 从插件加载、验证、环境变量解析、作用域管理 |

## LSP Tool 支持的操作

| 操作 | LSP Method | 说明 |
|------|-----------|------|
| `goToDefinition` | `textDocument/definition` | 跳转到符号定义 |
| `findReferences` | `textDocument/references` | 查找所有引用 |
| `hover` | `textDocument/hover` | 获取悬停信息（文档、类型） |
| `documentSymbol` | `textDocument/documentSymbol` | 获取文档内所有符号 |
| `workspaceSymbol` | `workspace/symbol` | 全工作区符号搜索 |
| `goToImplementation` | `textDocument/implementation` | 查找接口/抽象方法的实现 |
| `prepareCallHierarchy` | `textDocument/prepareCallHierarchy` | 获取位置处的调用层级项 |
| `incomingCalls` | `callHierarchy/incomingCalls` | 查找调用此函数的所有函数 |
| `outgoingCalls` | `callHierarchy/outgoingCalls` | 查找此函数调用的所有函数 |

所有操作需要 `filePath`、`line`（1-based）和 `character`（1-based）参数。

## 插件开发：LSP 服务器配置

LSP 服务器通过插件提供。插件的 `manifest.json` 中可以声明 LSP 服务器，支持三种格式：

**1. 内联配置（在 manifest 中直接定义）**

```json
{
  "lspServers": {
    "typescript": {
      "command": "typescript-language-server",
      "args": ["--stdio"],
      "extensionToLanguage": {
        ".ts": "typescript",
        ".tsx": "typescriptreact"
      }
    }
  }
}
```

**2. 引用外部 .lsp.json 文件**

```json
{
  "lspServers": "path/to/.lsp.json"
}
```

**3. 数组混合格式**

```json
{
  "lspServers": [
    "path/to/.lsp.j

# FILE: docs/memory-leak-audit.md

# 内存泄漏排查报告

> 基于官方 CHANGELOG 记录的 11 个已修复内存泄漏 + 1 个代码注释中的已知问题，对反编译代码库进行逐文件验证。
> 审计日期：2026-04-28

## TODO

- [x] #1 图片处理无限内存增长 — 确认已实现 ✅
- [x] #2 /usage 命令泄漏约 2GB — 确认已实现 ✅
- [x] #3 长时间运行工具进度事件泄漏 — 确认已实现 ✅
- [x] #4 空闲重新渲染循环 — **已确认完整**：所有 10 个 useAnimationFrame 调用者均正确传递 null 暂停时钟，keepAlive 机制工作正常
- [x] #5 虚拟滚动器保留历史消息拷贝 — 确认已实现 ✅
- [x] #6 管道模式超宽行过度分配 — 确认已实现 ✅
- [x] #7 语言语法按需加载 — **已修复**：改用 highlight.js/lib/core + 静态注册 26 个常用语言，从 190+ 语言降至 ~25，内存减少 ~80%
- [x] #8 NO_FLICKER 模式流状态泄漏 — **已修复**：StreamingToolExecutor.discard() 现在完整释放 tools 数组、中止 siblingAbortController、清理 turnSpan，7 tests
- [x] #9 Remote Control 权限条目保留 — **已修复**：pendingPermissionHandlers 提升至 useEffect 作用域，cleanup 时显式 clear()，8 tests
- [x] #10 MCP HTTP/SSE 缓冲区累积 — 确认已实现 ✅
- [x] #11 LRU 缓存键保留大 JSON — **已确认完整实现**：FileStateCache 使用 LRU 双重限制（max 100 条目 + maxSize 25MB）+ sizeCalculation，22 tests
- [x] #12 QueryEngine.mutableMessages 不收缩 — **已修复**：实现 snipCompactIfNeeded（按 removedUuids 过滤）+ snipProjection（边界检测 + 视图投影），28 tests
- [x] #18 Permission Polling Interval 泄漏 — **已修复**：inProcessRunner 权限响应后未调用 cleanup()，导致 setInterval 永远运行 + abort listener 挂载，6 tests
- [x] #17 LSP Opened Files Map 不收缩 — **已修复**：LSPServerManager 添加 closeAllFiles() 方法，postCompactCleanup 集成调用，compaction 后释放 openedFiles Map，5 tests

## 总览
---

## 1. 图片处理无限内存增长 (v2.1.121)

**CHANGELOG 描述**：Fixed unbounded memory growth (multi-GB RSS) when processing many images in a session

### 实现位置

- `src/utils/imageStore.ts` — 核心修复
- `src/commands/clear/caches.ts` — 缓存清理
- `src/screens/REPL.tsx` — UI 层释放

### 修复方式

三层防护机制：

1. **LRU 内存缓存**：`storedImagePaths` Map 上限 200 条目（`MAX_STORED_IMAGE_PATHS`），超出自动驱逐最早条目
2. **磁盘持久化**：图片 base64 数据写入 `~/.claude/image-cache/<sessionId>/`，内存中仅保留路径字符串
3. **立即释放**：`setPastedContents({})` 在消息提交/命令执行后清空 React state 中的 base64 数据

### 关键代码

```typescript
// imageStore.ts:10
const MAX_STORED_IMAGE_PATHS = 200

// imageStore.ts:115-124
function evictOldestIfAtCap(): void {
  while (storedImagePaths.size >= MAX_STORED_IMAGE_PATHS) {
    const oldest = storedImagePaths.keys().next().value
    if (oldest !== undefined) {
      storedImagePaths.delete(oldest)
    } else {
      break
    }
  }
}

// imageStore.ts:129-167 — 清理旧会话目录
export async function cleanupOldImageCaches(): Promise<void> { ... }
```

---

## 2. /usage 命令泄漏约 2GB (v2.1.121)


**CHANGELOG 描述**：Fixed /usage leaking up to ~2GB of memory on machines with large transcript histories

### 实现位置

- `src/utils/sessionStoragePortable.ts:716-792` — 核心流式读取
- `src/utils/attribution.ts` — 调用方

### 修复方式

1. **分块流式读取**：使用 `TRANSCRIPT_READ_CHUNK_SIZE = 1MB` 固定块大小，通过 `fd.read()` 逐块处理，避免一次性加载整个 transcript
2. **字节级过滤**：在 fd 层面直接跳过 `attribution-snapshot` 类型的行（占长会话 84% 的字节空间）
3. **边界截断**：搜索 `compact_boundary` 标记，只保留边界之后的数据
4. **缓冲区控制**：初始缓冲区限制 `Math.min(fileSize, 8MB)`

### 关键代码

```typescript
// sessionStoragePortable.ts:716-792
export async function readTranscriptForLoad(
  filePath: string,
  fileSize: number,
): Promise<{
  boundaryStartOffset: number
  postBoundaryBuf: Buffer
  hasPreservedSegment: boolean
}> {
  const s: LoadState = {
    out: {
      buf: Buffer.allocUnsafe(Math.min(fileSize, 8 * 1024 * 1024)),
      len: 0,
      cap: fileSize + 1,
    },
    // ...
  }
  const chunk = Buffer.allocUnsafe(CHUNK_SIZE)
  const fd = await fsOpen(filePath, 'r')
  try {
    let filePos = 0
    while (filePos < fileSize) {
      const { bytesRead } = await fd.read(chunk, 0, Math.min(CHUNK_SIZE, fileSize - filePos), filePos)
      if (bytesRead === 0) break
      filePos += bytesRead
      // ... 分块处理逻辑
    }
    finalizeOutput(s)
  } finally {
    await fd.close()
  }
}
```

---

## 3. 长时间运行工具进度事件泄漏 (v2.1.121)


**CHANGELOG 描述**：Fixed memory leak when long-running tools fail to emit a clear progress event

### 实现位置

- `src/screens/REPL.tsx:3054-3114` — progress 消息替换逻辑
- `src/utils/sessionStorage.ts:186-196` — 临时消息类型定义

### 修复方式

1. **向后扫描替换**：从只检查最后一条消息改为向后遍历所有 progress 消息，找到匹配的 `parentToolUseID` + `type` 后替换（修复交错消息导致 13k+ 条目堆积）
2. **全屏模式硬上限**：`MAX_FULLSCREEN_SCROLLBACK = 500`，超出截断
3. **临时消息识别**：`isEphemeralToolProgress()` 区分 `bash_progress`、`sleep_progress` 等一次性消息与需要保留的 `agent_progress` 等

### 关键代码

```typescript
// REPL.tsx:3094-3114
setMessages(oldMessages => {
  const newData = newMessage.data as Record<string, unknown>;
  // Scan backwards to find the last ephemeral progress with matching
  // parentToolUseID and type.
  for (let i = oldMessages.length - 1; i >= 0; i--) {
    const m = oldMessages[i]!
    if (m.type !== 'progress') break
    const mData = m.data as Record<string, unknown> | undefined
    if (
      m.parentToolUseID === newMessage.parentToolUseID &&
      mData?.type === newData.type
    ) {
      const copy = oldMessages.slice();
      copy[i] = newMessage;
      return copy;
    }
  }
  return [...oldMessages, newMessage];
});

// REPL.tsx:3058-3064 — 全屏模式硬上限
const MAX_FULLSCREEN_SCROLLBACK = 500
const kept = postBoundary.length > MAX_FULLSCREEN_SCROLLBACK
  ? postBoundary.slice(-MAX_FULLSCREEN_SCROLLBACK)
  : postBoundary
return [...kept, newMessage]
```

---

## 4. 空闲重新渲染循环 (v2.1.117)

**状态：已确认完整**

**CHANGELOG 描述**：Fixed idle re-render loop when background tasks are present, reducing memory growth on Linux

### 实现位置

- `packages/@ant/ink/src/components/ClockContext.tsx` — 核心时钟管理

### 已实现部分

`ClockContext` 的 `keepAlive` 订阅者分类机制完整存在：

```typescript
// ClockContext.tsx:11-43
function createClock(tickIntervalMs: number): Clock {
  const subscribers = new Map<() => void, boolean>()
  let interval: ReturnType<typeof setInterval> | null = null

  function updateInterval(): void {
    const anyKeepAlive = [...subscribers.values()].some(Boolean)
    if (anyKeepAlive) {
      // 有 keepAlive 订阅者时启动 interval
      interval = setInterval(tick, currentTickIntervalMs)
    } else if (interval) {
      // 无 keepAlive 订阅者时停止 interval
      clearInterval(interval)
      interval = null
    }
  }

  return {
    subscribe(onChange, keepAlive) {
      subscribers.set(onChange, keepAlive)
      updateInterval

# FILE: docs/auto-updater.md

# 自动更新机制

## 概述

Claude Code 拥有一套复杂的多策略自动更新系统，支持三种安装方式、后台静默更新、手动 CLI 命令、服务端版本门控以及更新日志展示。系统设计目标是在最小用户干预下保持 CLI 最新，同时提供回滚和手动控制的兜底手段。

---

## 安装类型与更新策略

更新策略由安装方式决定，通过 `src/utils/doctorDiagnostic.ts` 检测：

| 安装类型 | 更新策略 | 自动安装？ |
|---|---|---|
| `native` | 从 GCS/Artifactory 下载二进制文件，通过符号链接激活 | 是（静默） |
| `npm-global` | `npm install -g` / `bun install -g` | 是（静默） |
| `npm-local` | `npm install` 到 `~/.claude/local/` | 是（静默） |
| `package-manager` | 显示通知，附带对应操作系统的升级命令 | 否（仅通知） |
| `development` | 不适用 — 执行 `claude update` 时报错 | 不适用 |

### 策略路由

`src/components/AutoUpdaterWrapper.tsx` — 挂载在 React/Ink UI 树中 — 检测安装类型并渲染对应的更新组件：

- `native` → `NativeAutoUpdater`（二进制下载 + 符号链接）
- `package-manager` → `PackageManagerAutoUpdater`（仅通知）
- 其他 → `AutoUpdater`（基于 JS/npm）

---

## 后台自动更新循环

三个更新组件共享相同的轮询模式：

```typescript
useInterval(checkForUpdates, 30 * 60 * 1000); // 每 30 分钟
```

组件挂载时（即启动时）也会执行一次检查。

### 前置检查门控

任何更新尝试之前，系统会依次检查：

1. **自动更新是否被禁用？** — `getAutoUpdaterDisabledReason()`（`src/utils/config.ts:1737`）
   - `NODE_ENV === 'development'`
   - 设置了 `DISABLE_AUTOUPDATER` 环境变量
   - 仅限必要流量模式
   - `config.autoUpdates === false`（native 安装的保护模式除外）
2. **最大版本上限？** — `getMaxVersion()`（`src/utils/autoUpdater.ts:108`）— 服务端熔断开关，防止更新到已知有问题的版本
3. **是否跳过该版本？** — `shouldSkipVersion()`（`src/utils/autoUpdater.ts:145`）— 尊重用户的 `minimumVersion` 设置，防止切换到 stable 频道时发生意外的版本降级

### Native 自动更新器（`src/components/NativeAutoUpdater.tsx`）

1. 调用 `src/utils/nativeInstaller/installer.ts` 中的 `installLatest()`
2. 通过 `src/utils/nativeInstaller/download.ts` 下载二进制文件（GCS 或 Artifactory）
3. 验证 SHA256 校验和（3 次重试，60 秒卡顿检测）
4. 将版本化二进制文件存储到 XDG 目录
5. 更新符号链接（`~/.local/bin/claude` → 新版本二进制文件）
6. 保留最近 2 个版本，清理旧版本
7. 将错误分类上报分析（超时、校验和、权限、磁盘空间不足、npm、网络）

### JS/npm 自动更新器（`src/components/AutoUpdater.tsx`）

1. 调用 `getLatestVersion()` 获取当前 npm dist-tag
2. 通过 semver `gte()` 比较版本
3. 根据安装类型路由到本地或全局安装
4. 使用文件锁（`acquireLock()` / `releaseLock()`）防止并发更新

### 包管理器通知器（`src/components/PackageManagerAutoUpdater.tsx`）

每 30 分钟通过 GCS 存储桶（非 npm）检查更新。**不会自动安装** — 仅显示对应操作系统的升级命令：

- macOS: `brew upgrade claude-code`
- Windows: `winget upgrade Anthropic.ClaudeCode`
- Alpine: `apk upgrade claude-code`

---

## 启动版本门控

`src/utils/autoUpdater.ts:70` — `assertMinVersion()`

定义于 `src/utils/autoUpdater.ts:70`，设计上在启动时调用（当前未接入启动流程）：

```typescript
void assertMinVersion();
```

1. 从 GrowthBook 动态配置获取 `tengu_version_config`
2. 如果 `MACRO.VERSION < minVersion`，打印错误信息并调用 `gracefulShutdownSync(1)` — 强制用户更新
3. 这是一个**硬性门控** — 低于最低版本的 CLI 将无法启动

---

## 手动 CLI 命令

### `claude update` / `claude upgrade`

**文件**: `src/cli/update.ts`

完整流程：
1. 运行 `getDoctorDiagnostic()` 检查系统健康状态
2. 检查是否存在多个安装及配置不一致
3. 根据安装类型路由：
   - `development` → 报错（"开发版本不支持自动更新"）
   - `package-manager` → 打印对应操作系统的更新命令
   - `native` → 使用原生安装器的 `updateLatest()`
   - `npm-local` → 在 `~/.claude/local/` 执行 `npm install`
   - `npm-global` → 执行 `npm install -g`（含权限检查）
4. 报告当前版本、最新版本、成功/失败状态

### `claude rollback [target]`（仅限内部）

回滚到之前的版本。支持 `--list`、`--dry-run`、`--safe` 标志。

### `claude install [target]`

安装或重新安装原生构建版本。接受可选的版本目标参数。

### `claude doctor`

检查自动更新器的健康状态，报告状态、权限和配置信息。

---

## 原生安装器架构

**文件**: `src/utils/nativeInstaller/installer.ts`

### 二进制文件存储布局

```
~/.local/share/claude-code/
├── versions/          # 版本化二进制文件 (claude-1.0.3, claude-1.0.4, ...)
├── staging/           # 临时下载暂存区
└── locks/             # 基于 PID 和 mtime 的锁文件

~/.local/bin/claude    # 指向当前版本二进制文件的符号链接
```

Windows 系统使用文件复制而非符号链接。

### 核心操作

| 函数 | 说明 |
|---|---|
| `updateLatest()` | 核心更新流程：最大版本上限 → 跳过检查 → 加锁 → 下载 → 安装 → 更新符号链接 |
| `installLatest()` | Singleflight 包装版本，防止重复的进行中安装 |
| `cleanupOldVersions()` | 保留最近 2 个版本，清理过期的暂存区和临时文件 |
| `lockCurrentVersion()` | 进程生命周期锁，防止正在运行的版本被删除 |
| `cleanupNpmInstallations()` | 迁移到原生安装时清理旧的 npm 安装 |

### 下载与校验

**文件**: `src/utils/nativeInstaller/download.ts`

1. 路由到 Artifactory（内部用户）或 GCS 存储桶（外部用户）
2. 下载二进制文件并跟踪进度
3. SHA256 校验和验证
4. 60 秒卡顿检测（中止停滞的下载）
5. 失败时自动重试 3 次

---

## 文件锁机制

**文件**: `src/utils/autoUpdater.ts:176-268`

防止并发更新进程破坏安装：

- 锁文件：`~/.claude/update.lock`（或等效路径）
- 5 分钟超时 — 超过 5 分钟的锁被视为过期，强制获取
- 进程将其 PID 写入锁文件
- `acquireLock()` 和 `releaseLock()` 同时被 JS/npm 和原生安装器使用

---

## 配置

### 设置项

**文件**: `src/utils/settings/types.ts`

| 设置项 | 类型 | 说明 |
|---|---|---|
| `autoUpdatesChannel` | `'latest' \| 'stable'` | 自动更新的发布频道 |
| `minimumVersion` | string | 最低版本要求，防止意外的版本降级 |

### 全局配置

**文件**: `src/utils/config.ts:191-193`

| 字段 | 类型 | 说明 |
|---|---|---|
| `autoUpdates` | boolean | 启用/禁用自动更新（旧版） |
| `autoUpdatesProtectedForNative` | boolean | 原生安装始终自动更新 |

### 配置迁移

**文件**: `src/migrations/migrateAutoUpdatesToSettings.ts`

一次性将旧版 `globalConfig.autoUpdates = false` 迁移为 settings 中的 `DISABLE_AUTOUPDATER=1` 环境变量。定义于 `src/migrations/migrateAutoUpdatesToSettings.ts`（当前未接入启动流程）。

---

## 更新通知去重

**文件**: `src/hooks/useUpdateNotification.ts`

React hook `useUpdateNotification(updatedVersion)` — 确保每次 semver 变更（major.minor.patch）只显示一次"重启以更新"消息，避免同一版本的重复通知。

---

## 更新日志

**文件**: `src/utils/releaseNotes.ts`

1. 从 `src/setup.ts:387` 在每次启动时调用
2. 从 GitHub 获取 changelog
3. 缓存到 `~/.claude/cache/changelog.md`
4. 展示比 `lastReleaseNotesSeen` 更新的版本的更新日志
5. 使用 semver 比较确定需要展示哪些日志

---

## 版本比较

**文件**: `src/utils/semver.ts`

- 提供 `gt()`、`gte()`、`lt()`、`lte()`、`satisfies()`、`order()`
- 在 Bun 环境下使用 `Bun.semver.order()`（快 20 倍）
- 在 Node.js 环境下回退到 npm `semver` 包

---

## 分析事件

所有更新相关的遥测数据使用 `tengu_` 前缀的事件：

| 类别 | 事件 |
|---|---|
| 版本检查 | `tengu_version_check_success`、`tengu_version_check_failure` |
| JS 自动更新器 | `tengu_auto_updater_start/success/fail/up_to_date/lock_contention` |
| 原生自动更新器 | `tengu_native_auto_updater_start/success/fail` |
| 原生更新 | `tengu_native_update_complete/skipped_max_version/skipped_minimum_version` |
| 锁机制 | `tengu_version_lock_acquired/failed`、`tengu_native_update_lock_failed` |
| 二进制下载 | `tengu_binary_download_attempt/success/failure`、`tengu_binary_manifest_fetch_failure` |
| 清理 | `tengu_native_version_cleanup`、`tengu_native_staging_cleanup`、`tengu_native_stale_locks_cleanup` |
| 安装 | `tengu_native_install_package_succ

# FILE: docs/telemetry-remote-config-audit.md

# 遥测与远程配置下发系统审计（除 Sentry 外）

## 1. Datadog 日志

**文件**: `src/services/analytics/datadog.ts`

- **端点**: 通过环境变量 `DATADOG_LOGS_ENDPOINT` 配置（默认为空，即禁用）
- **客户端 token**: 通过环境变量 `DATADOG_API_KEY` 配置（默认为空，即禁用）
- **行为**: 批量发送日志（15s flush 间隔，100 条上限），仅限 1P（直连 Anthropic API）用户
- **事件白名单**: `tengu_*` 系列事件（启动、错误、OAuth、工具调用等 ~35 种）
- **基线数据**: 收集 model、platform、arch、version、userBucket（用户 hash 到 30 个桶）等
- **仅限**: `NODE_ENV === 'production'`
- **配置示例**: `DATADOG_LOGS_ENDPOINT=https://http-intake.logs.datadoghq.com/api/v2/logs DATADOG_API_KEY=xxx bun run dev`

## 2. 1P 事件日志（BigQuery）

**文件**: `src/services/analytics/firstPartyEventLogger.ts` + `firstPartyEventLoggingExporter.ts`

- **端点**: `https://api.anthropic.com/api/event_logging/batch`（staging 可切换）
- **行为**: 使用 OpenTelemetry SDK 的 `BatchLogRecordProcessor`，批量导出到 Anthropic 自有的 BQ 管道
- **数据**: 完整事件 metadata（session、model、env context、用户数据、subscription type 等）
- **弹性**: 本地磁盘持久化失败事件（JSONL），二次退避重试，最多 8 次尝试
- **Proto schema**: 事件序列化为 `ClaudeCodeInternalEvent` / `GrowthbookExperimentEvent` protobuf 格式
- **Auth fallback**: 401 时自动去掉 auth header 重试

## 3. GrowthBook 远程 Feature Flags / 动态配置

**文件**: `src/services/analytics/growthbook.ts`

- **服务端**: `https://api.anthropic.com/`（remote eval 模式）
- **行为**: 启动时拉取全量 feature flags，每 6h（外部用户）/ 20min（ant）定时刷新
- **磁盘缓存**: feature values 写入 `~/.claude.json` 的 `cachedGrowthBookFeatures`
- **用途**:
  - 控制 Datadog 开关（`tengu_log_datadog_events`）
  - 控制事件采样率（`tengu_event_sampling_config`）
  - 控制 sink killswitch（`tengu_frond_boric`）
  - 控制 BQ batch 配置（`tengu_1p_event_batch_config`）
  - 控制版本上限/自动更新 kill switch
  - 控制远程管理设置的安全检查 gate
- **用户属性**: 发送 deviceId, sessionId, organizationUUID, accountUUID, email, subscriptionType 等

## 4. Remote Managed Settings（企业远程配置下发）

**文件**: `src/services/remoteManagedSettings/index.ts`

- **端点**: `{BASE_API_URL}/api/claude_code/settings`
- **行为**: 企业用户配置下发，支持 ETag/304 缓存，每小时后台轮询
- **安全**: 变更包含"危险设置"时弹窗让用户确认
- **适用**: API key 用户全部可拉取；OAuth 用户仅 Enterprise/C4E/Team
- **Fail-open**: 请求失败时使用本地缓存，无缓存则跳过

## 5. Settings Sync（设置同步）

**文件**: `src/services/settingsSync/index.ts`

- **端点**: `{BASE_API_URL}/api/claude_code/user_settings`
- **行为**: CLI 上传本地设置/memory 到远程；CCR 模式从远程下载
- **同步内容**: userSettings、userMemory、projectSettings、projectMemory
- **Feature gate**: `UPLOAD_USER_SETTINGS` / `DOWNLOAD_USER_SETTINGS`
- **文件大小限制**: 500KB/文件

## 6. OpenTelemetry 三方遥测

**文件**: `src/utils/telemetry/instrumentation.ts`

- **行为**: 完整的 OTEL SDK 初始化，支持 metrics / logs / traces 三种信号
- **协议**: gRPC / http-json / http-protobuf（通过 `OTEL_EXPORTER_OTLP_PROTOCOL` 选择）
- **exporter**: console / otlp / prometheus
- **触发**: `CLAUDE_CODE_ENABLE_TELEMETRY=1` 环境变量
- **增强 trace**: `feature('ENHANCED_TELEMETRY_BETA')` + GrowthBook gate `enhanced_telemetry_beta`

## 7. BigQuery Metrics Exporter（内部指标）

**文件**: `src/utils/telemetry/bigqueryExporter.ts`

- **端点**: `https://api.anthropic.com/api/claude_code/metrics`
- **行为**: 定期（5min 间隔）导出 OTel metrics 到内部 BQ
- **适用**: API 客户、C4E/Team 订阅者
- **组织级 opt-out**: 通过 `checkMetricsEnabled()` API 查询（见下方第 8 项）

## 8. 组织级 Metrics Opt-out 查询

**文件**: `src/services/api/metricsOptOut.ts`

- **端点**: `https://api.anthropic.com/api/claude_code/organizations/metrics_enabled`
- **行为**: 查询组织是否启用了 metrics，二级缓存（内存 1h + 磁盘 24h）
- **作用**: 控制 BigQuery metrics exporter 是否导出

## 9. Startup Profiling

**文件**: `src/utils/startupProfiler.ts`

- **行为**: 采样启动性能数据（100% ant / 0.5% 外部），通过 `logEvent('tengu_startup_perf')` 上报
- **详细模式**: `CLAUDE_CODE_PROFILE_STARTUP=1` 输出完整性能报告到文件

## 10. Beta Session Tracing

**文件**: `src/utils/telemetry/betaSessionTracing.ts`

- **行为**: 详细调试 trace，发送 system prompt、model output、tool schema 等
- **触发**: `ENABLE_BETA_TRACING_DETAILED=1` + `BETA_TRACING_ENDPOINT`
- **外部用户**: SDK/headless 模式自动启用，交互模式需要 GrowthBook gate `tengu_trace_lantern`

## 11. Bridge Poll Config（远程轮询间隔配置）

**文件**: `src/bridge/pollConfig.ts`

- **行为**: 从 GrowthBook 拉取 bridge 轮询间隔配置（`tengu_bridge_poll_interval_config`）
- **控制**: 单会话和多会话的各种 poll interval

## 12. Plugin/MCP 遥测

**文件**: `src/utils/plugins/fetchTelemetry.ts`

- **行为**: 记录 plugin/marketplace 的网络请求（安装计数、marketplace clone/pull 等）
- **事件**: `tengu_plugin_remote_fetch`，包含 host（已脱敏）、outcome、duration

---

## 全局禁用方式

```bash
# 禁用所有遥测（Datadog + 1P + 调查问卷）
DISABLE_TELEMETRY=1

# 更激进：禁用所有非必要网络（包括自动更新、grove、release notes 等）
CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1

# 3P 提供商自动禁用
CLAUDE_CODE_USE_BEDROCK=1  # 或 VERTEX/FOUNDRY
```

`src/utils/privacyLevel.ts` 是集中控制点，三个级别：`default < no-telemetry < essential-traffic`。

---

## 数据流架构

```
用户操作 → logEvent()
              ↓
         sink.ts (路由层)
           ↙        ↘
   trackDatadogEvent()   logEventTo1P()
          ↓                      ↓
   Datadog HTTP API     OTel BatchLogRecordProcessor
   (us5.datadoghq.com)       ↓
                    FirstPartyEventLoggingExporter
                             ↓
                    api.anthropic.com/api/event_logging/batch
                             ↓
                    BigQuery (ClaudeCodeInternalEvent proto)
```

GrowthBook 作为独立通道，同时驱动上述两个 sink 的开关和配置。


# FILE: docs/memory-peak-analysis.md

# 内存与性能峰值分析报告

> 进程 bun，RSS 基线 **682 MB**，最差 **1.8 GB** | 2026-05-02 | **调研完成**（12 轮迭代）
> 修复 commit：`ef10ad28` + `ab0bbbc4`（降 100-300 MB）| 架构限制：Bun mimalloc/JSC 不归还内存页（~150-250 MB 永久占用）

## 已修复（10 项）

| 问题 | 原峰值 | 修复 | 位置 |
|------|--------|------|------|
| 流式字符串拼接 O(n²) | 2-20 MB | `+=` → 数组累积 | `claude.ts:1834,2271` |
| Messages.tsx 多次遍历 | 100-270 MB | 合并单次 pass | `Messages.tsx:417-418` |
| ColorFile 无缓存 | 50-100 MB | LRU-50 | `HighlightedCode.tsx:14-61` |
| Ink StylePool 无界 | 10-50+ MB | 1000 上限 | `@ant/ink/screen.ts:122` |
| CompanionSprite 高频 | CPU | TICK_MS→1000ms | `CompanionSprite.tsx:15` |
| MCP stderr 缓冲 | 1-640 MB | 64→8MB/server | `mcp-client/connection.ts:117` |
| BashTool 输出缓冲 | 30-330 MB | 32→2MB | `stringUtils.ts:88` |
| Transcript 写入队列 | 5-50 MB | 1000 上限 | `sessionStorage.ts:613-619` |
| contentReplacementState | 持续增长 | compact 清理 | `compact/compact.ts` |
| SSE 缓冲 | 无上限 | 1MB cap | SSE 处理代码 |

## P0 — 核心瓶颈（6 项）

| # | 问题 | 峰值 | 位置 | 建议 |
|---|------|------|------|------|
| 1 | 消息数组 7-8x spread 拷贝（turn 尾部 3-4 份同时驻留） | 120-320 MB | `query.ts` 7 处（:477,:491,:897,:1135,:1745,:1857,:1878） | 去掉 spread / 传引用 / 改 push |
| 2 | AutoCompact 时序缺陷（检查在 API 前，增长在 API 后） | API 超限 | `query.ts:575` | 加入预测式阈值检查 |
| 3 | reactiveCompact 空存根（API 413 时无紧急压缩） | 无降级 | `reactiveCompact.ts` 全文 | 实现真实逻辑 |
| 4 | buildMessageLookups 8 Map/Set 重建（流式每个 delta 触发） | GC STW 100-173ms | `Messages.tsx:519` | 增量更新 / 拆分 useMemo 链 |
| 5 | useDeferredValue 双缓冲 | 100-200 MB | `REPL.tsx:1569` | React 调度机制固有，优化空间有限 |
| 6 | Compact 峰值窗口（preCompactReadFileState + summary + attachments） | 20-80 MB | `compact.ts:524-644` | 提前释放 preCompactReadFileState/summaryResponse |

## P1 — 重要瓶颈（14 项）

| # | 问题 | 峰值 | 位置 | 建议 |
|---|------|------|------|------|
| 7 | OpenAI/Gemini/Grok 兼容层 O(n²) 拼接 | 25-75 MB | 3 文件 9 处（`openai/index.ts:386`, `gemini/index.ts:148`, `grok/index.ts:163`） | 改数组累积（同 claude.ts 模式） |
| 8 | messages.ts O(n²) 拼接 | 10-25 MB | `messages.ts:3252,3268` | 改数组累积 |
| 9 | highlight.js 全量 192 语言（仅需 26 种） | 8-12 MB | `color-diff-napi/index.ts:21` | 自定义构建 |
| 10 | hlLineCache 模块级单例 2048 条目 | ~4 MB | `color-diff-napi/index.ts:508` | 改 LRU + size 上限 |
| 11 | colorFileCache 3x 代码存储 | 2-5 MB | `HighlightedCode.tsx:14` | 移除 value 中 code 字段 |
| 12 | 虚拟滚动 200 组件常驻 | 50 MB | `useVirtualScroll.ts` | 降低 OVERSCAN_ROWS / MAX_MOUNTED_ITEMS |
| 13 | FileReadTool 大文件（输出上限 100K 字符，但读取期间完整加载） | 临时数 MB | `FileReadTool.ts:342` | 读取前检测大小，流式截断 |
| 14 | Session 恢复全量加载（磁盘→JSON→REPL 三阶段） | 200-300 MB | `sessionStorage.ts:3482` | 流式 JSONL / 增量恢复 |
| 15 | Session 写入 100MB 累积 | ~100 MB | `sessionStorage.ts:652` | 流式写入 |
| 16 | Forked Agent FileStateCache 完整克隆 | 50N MB | `forkedAgent.ts:382` | 共享/分层缓存（agent 用 10MB） |
| 17 | GC 阈值 350MB < 基线（每秒无意义强制 GC） | CPU 浪费 | `cli/print.ts:554` | 提高到 800MB+ |
| 18 | PDF 100 页处理 | ~100 MB | `apiLimits.ts:54` | 分页流式处理 |
| 19 | 图片单张处理（base64→解码→resize） | ~16 MB/张 | `apiLimits.ts:22` | 流式 resize |
| 20 | token 估算 ±25-50% 误差放大时序问题 | 阈值不准 | `tokenEstimation.ts:215` | 内容类型感知估算 |

## P2 — 次要问题（10 项）

| # | 问题 | 峰值 | 位置 |
|---|------|------|------|
| 21 | lastAPIRequestMessages 常驻 | 30-50 MB | `bootstrap/state.ts:118` |
| 22 | MCP Tool Schema 双重存储 | ~40 MB | `manager.ts:73` + `AppStateStore.ts:175` |
| 23 | ContentReplacementState 单调增长 | 0.5-2 MB | `toolResultStorage.ts:390` |
| 24 | Perfetto 100K 事件 | ~30 MB | `perfettoTracing.ts:106` |
| 25 | StreamingMarkdown 双渲染 | 临时 | `Markdown.tsx:185` |
| 26 | MarkdownTable 3 次遍历 | CPU 峰值 | `MarkdownTable.tsx:99` |
| 27 | 搜索索引 WeakMap | 5-10 MB | `transcriptSearch.ts:17` |
| 28 | ACP FileStateCache/会话 | 50 MB | `acp/agent.ts:554` |
| 29 | Agent initialMessages 浅拷贝 | 1-5 MB/agent | `runAgent.ts:382` |
| 30 | Hook 结果累积 | ~1 MB+ | `toolExecution.ts:1474` |

## CPU / 渲染热点

| # | 问题 | 影响 | 位置 |
|---|------|------|------|
| C2 | Ink 每次 React commit 触发 Yoga 布局 | ~1-3ms/commit | `reconciler.ts:279` → `ink.tsx:323` |
| C3 | MessageRow 挂载 ~1.5ms（React/Yoga/Ink 管线开销） | 批量挂载 ~290ms 卡顿 | `useVirtualScroll.ts` |
| C4 | 布局偏移触发全屏 damage | O(rows×cols) | `ink.tsx:655-661` |
| C9 | 同步 fs 操作阻塞主线程 | 间歇卡顿 | `projectOnboardingState.ts:20` 等 |

已有缓解：React ConcurrentRoot 批处理、帧率限制 16ms、虚拟滚动 overscan 80 + SLIDE_STEP=25 + useDeferredValue、Markdown tokenCache LRU-500 + hasMarkdownSyntax 快速路径、Yoga 增量缓存。

## 已否认（12 轮汇总）

VSZ 516 GB 是虚拟映射 | Zod ~650KB | Markdown LRU-500 已优化 | useSkillsChange/useSettingsChange 正确 cleanup | useInboxPoller 收敛设计（非循环）| React Compiler `_c(N)` 未使用 | File watchers ~5KB | React reconciler WeakMap + freeRecursive | Ink 屏幕缓冲 ~86KB | CharPool/HyperlinkPool ~1-5MB 5min 重置 | AWS/Google/Azure SDK 均懒加载 | Sentry 空实现 | useCallback 闭包通过 messagesRef 规避（无泄漏）| MCP stderrHandler 有 64MB cap + cleanup | useRef 有 clearConversation/compact 清理 | apiMetricsRef turn 结束重置 | useEffect 有 cleanup 函数 | lodash-es tree-shakable | AppState useSyncExternalStore 仅相关切片更新 | SDK 无全局重试队列 | Ink unmount 有清理

## 结论

**内存根因排序**：
1. 消息数组 7-8x spread 拷贝（120-320 MB）— 核心瓶颈
2. useDeferredValue 双缓冲 + React useMemo 链全量重算（100-200 MB + GC STW）
3. Session 恢复/写入峰值（200-300 MB）
4. AutoCompact 时序缺陷 + reactiveCompact 空存根（API 超限风险）
5. Forked Agent FileStateCache 克隆（50N MB）
6. 虚拟滚动 200 组件 ~50MB 常驻
7. Bun/JSC 不归还内存页（架构级）

**CPU 根因**：useInboxPoller 每秒轮询 → React commit → Yoga 布局 → 全屏 Ink diff 完整管线。Markdown 渲染批量挂载时 ~290ms 卡顿。

**预估优化空间**：

| 优先级 | 措施数 | 预估降低 |
|--------|--------|----------|
| P0 | 6 | 240-600 MB |
| P1 | 14 | 300-600 MB |
| P2 | 10 | 80-200 MB |
| **合计** | **30 项** | **620-1400 MB** |

理论可从 400-700 MB 降至 **200-350 MB**（受 mimalloc/JSC 架构限制约束）。


# FILE: docs/design/tool-search-design-guide.md

# ToolSearch 设计指南

> 基于 feature/tool_search 分支的 4 次 commit 迭代，系统性地记录 ToolSearch 的架构、核心机制、演进历史和维护指南。

## 1. 问题背景

Claude Code 内置了 60+ 工具，加上用户连接的 MCP 服务器可能引入数十甚至上百个额外工具。将所有工具的完整 schema 一次性发送给模型，会产生几个严重问题：

1. **Token 爆炸** — 每个工具定义（name + description + inputSchema）平均消耗数百 token，60 个工具就是数万 token 的常量开销。
2. **Prompt Cache 失效** — 工具列表作为 prompt 的一部分参与缓存计算。任何工具的增减（如 MCP 服务器连接/断开）都会导致整段缓存失效。
3. **模型注意力稀释** — 过多的工具定义干扰模型对核心工具的选择准确性。

## 2. 解决方案概览

ToolSearch 采用 **延迟加载（Deferred Loading）** 模式：

- 将工具分为 **Core Tools**（始终加载）和 **Deferred Tools**（按需发现）
- 模型通过 `SearchExtraTools` 工具搜索并发现 deferred tools
- 通过 `ExecuteExtraTool` 工具代理执行发现的 deferred tools
- **工具数组在会话中保持稳定**，不再动态注入已发现的 deferred tools（v3 修复的关键决策）

## 3. 核心架构

### 3.1 工具分类体系

```
┌─────────────────────────────────────────────────────────────┐
│                     All Tools (60+ built-in + MCP)          │
├───────────────────────────┬─────────────────────────────────┤
│    Core Tools (29 个)     │     Deferred Tools (其余全部)    │
│    始终加载，直接调用      │     不加载 schema，按需发现      │
│    CORE_TOOLS 白名单定义   │     isDeferredTool() 判定       │
└───────────────────────────┴─────────────────────────────────┘
```

**Core Tools**（`src/constants/tools.ts` 中的 `CORE_TOOLS` Set）：

| 类别 | 工具 |
|------|------|
| 文件操作 | Bash/Shell, Read, Edit, Write, Glob, Grep, NotebookEdit |
| Agent 交互 | Agent, AskUserQuestion |
| 任务管理 | TaskOutput, TaskStop, TaskCreate, TaskGet, TaskList, TaskUpdate, TodoWrite |
| 规划 | EnterPlanMode, ExitPlanMode, VerifyPlanExecution |
| Web | WebFetch, WebSearch |
| 代码智能 | LSP |
| 技能 | Skill |
| 调度/监控 | Sleep |
| 工具发现 | SearchExtraTools, ExecuteExtraTool, SyntheticOutput |

**isDeferredTool 判定逻辑**（`packages/builtin-tools/src/tools/SearchExtraToolsTool/prompt.ts`）：

```
isDeferredTool(tool) =
  tool.alwaysLoad === true?  → false（显式跳过延迟）
  CORE_TOOLS.has(tool.name)? → false（核心工具不延迟）
  otherwise                  → true（其余全部延迟）
```

### 3.2 三层组件架构

```
┌──────────────────────────────────────────────────────┐
│  API Layer (src/services/api/claude.ts)              │
│  ├─ 判定是否启用 ToolSearch                          │
│  ├─ 过滤 deferred tools 不进入 API tools 数组         │
│  ├─ 注入 <available-deferred-tools> 或 delta 附件    │
│  └─ 处理 tool_reference/text 格式的消息归一化         │
├──────────────────────────────────────────────────────┤
│  Query Loop (src/query.ts)                           │
│  ├─ Turn-zero 预取：用户输入时触发                    │
│  └─ Inter-turn 预取：assistant turn 后异步触发        │
├──────────────────────────────────────────────────────┤
│  Search Engine                                       │
│  ├─ SearchExtraToolsTool — 搜索入口（4 种查询模式）  │
│  ├─ TF-IDF Index (toolIndex.ts) — 语义搜索          │
│  ├─ Keyword Search — 精确匹配                       │
│  └─ ExecuteExtraTool — 代理执行                      │
└──────────────────────────────────────────────────────┘
```

### 3.3 搜索引擎设计

SearchExtraToolsTool 支持四种查询模式：

| 模式 | 语法 | 行为 | 返回 |
|------|------|------|------|
| **Select** | `select:CronCreate,Snip` | 按名称直接获取，逗号分隔多选 | 精确匹配列表 |
| **Discover** | `discover:schedule cron job` | 纯发现模式，返回描述+schema | 工具信息文本 |
| **Keyword** | `notebook jupyter` | 关键词搜索 | 按相关性排序 |
| **Required** | `+slack send` | `+` 前缀强制包含 | 包含必选词的结果 |

**混合搜索算法**：

```
最终分数 = 关键词分数 × 0.4 + TF-IDF 分数 × 0.6
```

- **Keyword Search**：基于工具名解析（CamelCase 分词、MCP 前缀拆解）、searchHint 匹配、描述文本匹配，加权计分
- **TF-IDF Search**：复用 `skillSearch/localSearch.ts` 的算法，对 name (3.0)、searchHint (2.5)、description (1.0) 三个字段加权计算 TF-IDF 向量

**MCP 工具名解析**：

```
mcp__slack__send_message → parts: ["slack", "send", "message"]
CamelCase → parts: ["cron", "create"]
```

### 3.4 执行管道

```
模型调用 ExecuteExtraTool({tool_name: "CronCreate", params: {...}})
  ↓
ExecuteTool.call() 在全局工具注册表中查找 CronCreate
  ↓
检查目标工具 isEnabled() — 桥接/条件工具可能不可用
  ↓
委托目标工具的 checkPermissions() — 权限传递给实际工具
  ↓
调用目标工具的 call() — 与直接调用完全等价
  ↓
返回结果（包装为 ExecuteExtraTool 的 output schema）
```

关键设计：ExecuteExtraTool 的 `checkPermissions()` 返回 `passthrough`，将权限决策完全委托给目标工具。它本身不引入额外的权限层。

### 3.5 Prompt Cache 稳定性策略（v3 关键修复）

**问题**：早期版本在发现 deferred tool 后会将其注入 API tools 数组，导致每次发现新工具时 tools JSON 变化，prompt cache 全面失效。

**修复**（commit `c14b7ead`）：deferred tools **始终不进入 API tools 数组**。tools 数组在整个会话中只包含 core tools + SearchExtraTools + ExecuteExtraTool，保持稳定。

```
API Tools 数组（会话期间不变）:
  [Core Tools (29)] + [SearchExtraTools, ExecuteExtraTool, SyntheticOutput]
  
  不包含: 任何 deferred tool（即使已被发现）
  执行方式: 通过 ExecuteExtraTool 代理调用
```

## 4. 预取机制（Prefetch）

### 4.1 两个触发时机

1. **Turn-zero**（`getTurnZeroSearchExtraToolsPrefetch`）— 用户输入第一轮时，基于输入文本搜索相关 deferred tools，以 attachment 形式注入
2. **Inter-turn**（`startSearchExtraToolsPrefetch`）— assistant turn 结束后，基于对话上下文异步搜索

### 4.2 Attachment 管道

```
prefetch → Attachment(type: 'tool_discovery')
  → messages.ts 转换为 system-reminder
  → "The following tools were discovered... Use ExecuteExtraTool to invoke..."
```

### 4.3 会话去重

`discoveredToolsThisSession` Set 跟踪已发现的工具，避免重复推荐。该 Set 独立于 skill prefetch 的去重集合，互不影响。使用 `addBoundedSessionEntry()` 保持上限 500 条，超出时裁剪到 400 条。

## 5. 模式切换系统

通过环境变量 `ENABLE_SEARCH_EXTRA_TOOLS` 控制：

| 环境变量值 | 模式 | 行为 |
|-----------|------|------|
| 未设置 | `tst` | 默认启用，始终延迟非核心工具 |
| `true` | `tst` | 强制启用 |
| `false` | `standard` | 完全禁用，所有工具内联加载 |
| `auto` | `tst-auto` | 仅当 deferred tools 超过上下文窗口 10% 时启用 |
| `auto:N` | `tst-auto` | 自定义阈值百分比（N=0 启用，N=100 禁用） |
| `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` | `standard` | 全局 kill switch |

`isSearchExtraToolsEnabledOptimistic()` — 快速判断（不检查阈值），用于工具注册
`isSearchExtraToolsEnabled()` — 完整判断（含阈值检查），用于 API 调用

## 6. Deferred Tools Delta 机制

对于 Anthropic 内部用户（`USER_TYPE=ant`）或启用了 `tengu_glacier_2xr` feature flag 的用户，使用 **delta attachment** 替代 `<available-deferred-tools>` 头部注入：

- 首次：注入完整的 deferred tools 列表
- 后续：只注入增量变化（新增/移除）
- 优势：不会因为工具池变化导致整个头部缓存失效

Delta attachment 扫描历史消息中的 `deferred_tools_delta` 类型 attachment，重建已宣告集合，然后差分计算当前 deferred pool 的变化。

## 7. 演进历史

### v1: 基础设施层（`7be08f53`）

**34 个文件，+4040/-90 行**

- 定义 `CORE_TOOLS` 白名单（31 个核心工具）
- 实现 TF-IDF 工具索引模块 `toolIndex.ts`
- 创建 `ExecuteTool` 作为统一执行入口
- 增强 ToolS

# FILE: docs/test-plans/openclaw-autonomy-baseline.md

# OpenClaw Autonomy Baseline Test Spec

## Purpose

This test spec locks the current behavior of the existing trigger and context layers before any formal autonomy-subsystem implementation begins.

At this stage, production code is read-only. Only test files, fixtures, and planning documents may change.

## Goal

Establish a stable baseline around the parts of `Claude-code-bast` that later autonomy work is most likely to touch:

- proactive state handling
- cron task storage semantics
- cron scheduler helper semantics
- user-context cache and `CLAUDE.md` injection behavior

## Out of Scope for This Baseline Round

- New authority behavior (`AGENTS.md` / `HEARTBEAT.md`)
- New detached-run ledger behavior
- New flow behavior
- UI redesign

## Files Under Baseline Protection

- `src/proactive/index.ts`
- `src/utils/cronTasks.ts`
- `src/utils/cronScheduler.ts`
- `src/context.ts`

## Test Files Added In This Round

- `src/proactive/__tests__/state.baseline.test.ts`
- `src/commands/__tests__/proactive.baseline.test.ts`
- `src/utils/__tests__/cronTasks.baseline.test.ts`
- `src/utils/__tests__/cronScheduler.baseline.test.ts`
- `src/__tests__/context.baseline.test.ts`

## Baseline Assertions

### Proactive state

1. Activating proactive mode sets active state and activation source.
2. Pausing proactive mode suppresses `shouldTick()` and clears `nextTickAt`.
3. Blocking context suppresses `shouldTick()` and clears `nextTickAt`.
4. Subscribers are notified on state transitions.
5. The `/proactive` command enables proactive mode and emits the expected hidden reminder.
6. The `/proactive` command disables proactive mode on the second invocation.

### Cron task storage

1. Session-only cron tasks remain in memory only.
2. Durable cron tasks are persisted to `.claude/scheduled_tasks.json`.
3. Daemon-style `dir`-scoped reads exclude session-only cron tasks.
4. `removeCronTasks()` without `dir` can remove session-only tasks.
5. `removeCronTasks()` with `dir` does not mutate session-only task storage.

### Cron scheduler helpers

1. `isRecurringTaskAged()` preserves current aging semantics.
2. `buildMissedTaskNotification()` preserves the current AskUserQuestion safety wording.
3. `buildMissedTaskNotification()` preserves code-fence hardening for prompt bodies that contain backticks.

### User context caching

1. `getUserContext()` includes `currentDate`.
2. `getUserContext()` includes mocked `claudeMd` content when memory loading is enabled.
3. `CLAUDE_CODE_DISABLE_CLAUDE_MDS` suppresses `claudeMd`.
4. `setSystemPromptInjection()` clears the memoized user-context cache.
5. `getSystemContext()` reflects the injection after cache invalidation.

## Remaining Baseline Gaps

The following areas are intentionally deferred because they require higher-cost harnessing and should still avoid production-code changes:

1. `useScheduledTasks.ts` hook-level runtime behavior
2. `src/cli/print.ts` full headless scheduler loop behavior
3. `useProactive.ts` hook timer behavior
4. end-to-end queue interaction between proactive ticks and `SleepTool`

## Acceptance

This baseline round is complete when:

1. The four new test files pass.
2. No production source files are modified.
3. The tests are stable enough to serve as a pre-implementation guardrail.


# FILE: docs/features/computer-use-mcp-test-report.md

# Computer Use MCP 工具测试报告

> 测试日期: 2026-04-04
> 测试环境: macOS Darwin 25.4.0, Cursor (IDE tier: click)
> MCP Server: `@ant/computer-use-mcp`

## 工具总览

共 17 个工具（含 batch 复合操作），分为 5 大类：

| 类别 | 工具 | 数量 |
|------|------|------|
| 截图/显示 | `screenshot`, `switch_display`, `zoom` | 3 |
| 鼠标操作 | `left_click`, `right_click`, `double_click`, `triple_click`, `middle_click`, `left_click_drag`, `mouse_move` | 7 |
| 键盘操作 | `key`, `type`, `hold_key` | 3 |
| 状态查询 | `cursor_position`, `request_access` | 2 |
| 复合/辅助 | `computer_batch`, `wait` | 2 |

---

## 测试结果

### 1. 权限管理

#### `request_access` — 请求应用访问权限

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 行为 | 弹出系统对话框请求用户授权，支持批量申请多个应用 |
| 返回 | `{ granted: [...], denied: [...], tierGuidance: "..." }` |
| 权限分级 | `click`（仅点击）, `full`（完整控制） |
| 说明 | IDE 类应用（Cursor、VSCode、Terminal）默认授予 `click` tier，限制键盘输入和右键操作；系统应用（System Settings）授予 `full` tier |

#### 已授权应用

| 应用 | Tier | 能力 |
|------|------|------|
| Cursor | click | 可见 + 纯左键点击（无键盘输入、右键、修饰键点击、拖拽） |
| Terminal | click | 同上 |
| System Settings | full | 完整控制（键鼠、拖拽等） |
| Finder | — | 已授权 |

---

### 2. 截图与显示

#### `screenshot` — 截取屏幕截图

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 部分通过 |
| 执行 | 工具成功执行，返回 `ok: true` |
| 图片 | **未返回可视图片内容**（output 为空字符串） |
| `save_to_disk` | 设置后仍无输出 |
| 分析 | 可能原因：(1) macOS 屏幕录制权限未授予；(2) 当前前台应用未被过滤导致截图为空；(3) MCP 传输层未正确编码图片数据 |
| 建议 | 检查 **系统设置 → 隐私与安全性 → 屏幕录制** 是否授权给运行 Claude Code 的应用 |

#### `switch_display` — 切换显示器

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 行为 | 接受显示器名称或 `"auto"`（自动选择） |
| 返回 | 确认消息 |

#### `zoom` — 区域放大截图

| 项目 | 结果 |
|------|------|
| 状态 | ⏭️ 跳过 |
| 原因 | 依赖 `screenshot` 返回的图片坐标，截图未返回图片无法测试 |

---

### 3. 鼠标操作

> 以下测试在 Cursor 窗口上执行（tier: click）

#### `mouse_move` — 移动鼠标

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `coordinate: [500, 500]` |
| 返回 | `"Moved."` |

#### `left_click` — 左键单击

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `coordinate: [500, 500]` |
| 返回 | `"Clicked."` |

#### `double_click` — 双击

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `coordinate: [500, 500]` |
| 返回 | `"Clicked."` |

#### `triple_click` — 三击

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `coordinate: [500, 500]` |
| 返回 | `"Clicked."` |

#### `right_click` — 右键点击

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — `"Code" is granted at tier "click" — right-click, middle-click, and clicks with modifier keys require tier "full"` |
| Finder (full tier) | ✅ 通过 — 返回 `"Clicked."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

#### `middle_click` — 中键点击

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — 同 `right_click`，需要 full tier |
| Finder (full tier) | ✅ 通过 — 返回 `"Clicked."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

#### `left_click_drag` — 拖拽

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — 拖拽被视为修饰键点击，需要 full tier |
| Finder (full tier) | ✅ 通过 — 返回 `"Dragged."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

#### `scroll` — 滚轮滚动

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `coordinate: [500, 500]`, `scroll_direction: "down"`, `scroll_amount: 3` |
| 返回 | `"Scrolled."` |
| 反向 | ✅ `scroll_direction: "up"` 也通过 |

---

### 4. 键盘操作

> 以下测试在 Cursor 窗口上执行（tier: click）— 所有键盘操作均被拒绝

#### `key` — 按键/快捷键

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — IDE tier 限制键盘输入 |
| Finder (full tier) | ✅ 通过 — `escape` 按键成功，返回 `"Key pressed."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

#### `type` — 输入文本

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — IDE tier 限制文本输入 |
| Finder (full tier) | ✅ 通过 — 输入 `"hello"` 成功，返回 `"Typed 5 grapheme(s)."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

#### `hold_key` — 按住按键

| 项目 | 结果 |
|------|------|
| 状态 | ⚠️ 受 tier 限制 |
| Cursor (click tier) | ❌ 被拒绝 — IDE tier 限制键盘输入 |
| Finder (full tier) | ✅ 通过 — 按住 `shift` 1 秒成功，返回 `"Key held."` |
| 结论 | 功能正常，IDE 安全限制符合预期 |

---

### 5. 状态查询

#### `cursor_position` — 获取鼠标位置

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 返回 | `{"x": null, "y": null, "coordinateSpace": "image_pixels"}` |
| 说明 | 坐标为 null 是因为没有成功截图，无参考坐标系 |

---

### 6. 复合/辅助操作

#### `computer_batch` — 批量执行操作

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 行为 | 按顺序执行操作列表，遇到失败则停止后续操作 |
| 返回 | `{ completed: [...], failed: {...}, remaining: N }` |
| 特点 | 单次 API 调用执行多个操作，减少往返延迟 |
| 错误处理 | 失败的操作会中断后续操作，返回已完成和剩余数量 |

#### `wait` — 等待

| 项目 | 结果 |
|------|------|
| 状态 | ✅ 通过 |
| 输入 | `duration: 1` (秒) |
| 返回 | `"Waited 1s."` |
| 最大值 | 100 秒 |

---

## 汇总统计

| 状态 | 数量 | 工具 |
|------|------|------|
| ✅ 通过 | 10 | `request_access`, `switch_display`, `mouse_move`, `left_click`, `double_click`, `triple_click`, `scroll`, `cursor_position`, `computer_batch`, `wait` |
| ⚠️ 部分通过 | 7 | `screenshot`（执行成功但无图片返回）, `right_click`, `middle_click`, `left_click_drag`, `key`, `type`, `hold_key`（均在 full tier 应用上通过，IDE click tier 限制是预期行为） |
| ❌ 被拒绝 | 0 | — |
| ⏭️ 跳过 | 1 | `zoom`（依赖截图） |

---

## 已知问题

### P0: 截图无图片返回

`screenshot` 工具执行成功但未返回图片内容，导致：
- 无法获取屏幕坐标参考
- `cursor_position` 返回 null 坐标
- `zoom` 无法使用
- 所有点击操作只能盲点（无截图验证）

**可能原因**:
1. macOS 屏幕录制权限未授予
2. MCP 图片传输/编码问题
3. 截图内容被安全过滤机制过滤

**建议排查**: 检查 `系统设置 → 隐私与安全性 → 屏幕录制` 权限。

### P1: IDE 应用键盘操作受限 — ✅ 已确认功能正常

IDE 类应用（Cursor、VSCode、Terminal）被限制在 `click` tier，无法执行：
- 键盘输入（`key`, `type`, `hold_key`）
- 右键/中键点击（`right_click`, `middle_click`）
- 拖拽操作（`left_click_drag`）

这是安全设计，防止 AI 操控 IDE 终端。**在 full tier 应用（Finder、System Settings）上，以上 6 个操作均测试通过，功能完全正常。**

---

## 权限模型说明

Computer Use MCP 采用分级权限模型：

```
┌─────────────────────────────────────────┐
│  Tier: full                             │
│  - 所有鼠标操作（左键、右键、中键、拖拽）  │
│  - 键盘输入（type, key, hold_key）       │
│  - 适用于: 系统应用、Finder 等           │
├─────────────────────────────────────────┤
│  Tier: click                            │
│  - 仅纯左键点击                          │
│  - 滚轮滚动                             │
│  - 适用于: IDE、Terminal 等              │
├─────────────────────────────────────────┤
│  未授权                                  │
│  - 所有操作被拒绝                        │
│  - 需通过 request_access 申请            │


# FILE: docs/features/daemon-restructure-design.md

# Daemon 重构设计方案

> 分支: `feat/integrate-5-branches`
> 基于: `f41745cb` (= main `11bb3f62` 内容)
> 日期: 2026-04-13

## 一、问题概述

### 1.1 命令结构散乱

当前后台进程相关的命令分布在三个不同的位置，没有统一的命名空间：

| 命令 | 注册位置 | 入口 |
|------|---------|------|
| `claude daemon start/status/stop` | `cli.tsx` 快速路径 L203 | `daemon/main.ts` |
| `claude ps` | `cli.tsx` 快速路径 L220 | `cli/bg.ts` |
| `claude logs <x>` | `cli.tsx` 快速路径 L232 | `cli/bg.ts` |
| `claude attach <x>` | `cli.tsx` 快速路径 L236 | `cli/bg.ts` |
| `claude kill <x>` | `cli.tsx` 快速路径 L238 | `cli/bg.ts` |
| `claude --bg` | `cli.tsx` 快速路径 L244 | `cli/bg.ts` |
| `claude new/list/reply` | `cli.tsx` 快速路径 L250 | `cli/handlers/templateJobs.ts` |
| `claude rollback` | `main.tsx` Commander.js L6525 | `cli/rollback.ts` |
| `claude up` | `main.tsx` Commander.js L6511 | `cli/up.ts` |

**问题**:
- `ps/logs/attach/kill` 与 `daemon` 逻辑上都是后台进程管理，但互不关联
- 这些命令都**只有 CLI 入口**，REPL 里输入 `/daemon` 或 `/ps` 不存在
- `new/list/reply` 是模板任务系统的顶级命令，容易与其他命令冲突（特别是 `list`）

### 1.2 Windows 不支持

`--bg` 和 `attach` 硬依赖 tmux：
- `bg.ts:handleBgFlag()` 第一步就检查 tmux，不可用直接报错退出
- `bg.ts:attachHandler()` 用 `tmux attach-session`，无 tmux 替代方案
- Windows (包括 VS Code 终端) 完全无法使用后台会话功能

### 1.3 无 REPL 入口

对比 `/mcp` 的双注册模式：
- **CLI**: `claude mcp serve/add/remove/list` (Commander.js, `main.tsx:5760`)
- **REPL**: `/mcp enable/disable/reconnect` (slash command, `commands/mcp/index.ts`)

`daemon`/`bg`/`job` 系列只有 CLI 快速路径，REPL 中完全不可用。

## 二、目标

1. **层级化命令结构**: 参照 `/mcp` 模式，将后台管理收归 `/daemon`，模板任务收归 `/job`
2. **跨平台后台会话**: Windows / macOS / Linux 都能启动、附着、终止后台会话
3. **双注册**: CLI (`claude daemon ...`) + REPL (`/daemon ...`) 同时可用
4. **向后兼容**: 旧命令保留但输出 deprecation 提示

## 三、命令结构设计

### 3.1 `/daemon` — 后台进程管理

合并 daemon supervisor + bg sessions 为统一命名空间：

```
claude daemon <subcommand>     ← CLI 入口 (cli.tsx 快速路径)
/daemon <subcommand>           ← REPL 入口 (slash command, local-jsx)

子命令:
  status                       综合状态面板 (daemon + 所有会话)
  start [--dir <path>]         启动 daemon supervisor
  stop                         停止 daemon
  bg [args...]                 启动后台会话
  attach [target]              附着到后台会话
  logs [target]                查看会话日志
  kill [target]                终止会话
  (无参数)                     等同于 status
```

**CLI 快速路径路由** (`cli.tsx`):
```typescript
// 新: 统一入口
if (feature('DAEMON') && args[0] === 'daemon') {
  const sub = args[1] || 'status'
  switch (sub) {
    case 'start': case 'stop': case 'status':
      await daemonMain([sub, ...args.slice(2)])
      break
    case 'bg':
      await bg.handleBgStart(args.slice(2))
      break
    case 'attach': case 'logs': case 'kill':
      await bg[`${sub}Handler`](args[2])
      break
  }
}

// 向后兼容 (deprecated)
if (feature('BG_SESSIONS') && ['ps','logs','attach','kill'].includes(args[0])) {
  console.warn(`[deprecated] Use: claude daemon ${args[0] === 'ps' ? 'status' : args[0]}`)
  // ... delegate to daemon subcommand
}
```

**REPL 斜杠命令** (`commands/daemon/index.ts`):
```typescript
const daemon = {
  type: 'local-jsx',
  name: 'daemon',
  description: 'Manage background sessions and daemon',
  argumentHint: '[status|start|stop|bg|attach|logs|kill]',
  isEnabled: () => feature('DAEMON') || feature('BG_SESSIONS'),
  load: () => import('./daemon.js'),
} satisfies Command
```

### 3.2 `/job` — 模板任务管理

```
claude job <subcommand>        ← CLI 入口
/job <subcommand>              ← REPL 入口

子命令:
  list                         列出模板和活跃任务
  new <template> [args]        从模板创建任务
  reply <id> <text>            回复任务
  status <id>                  查看任务状态
  (无参数)                     等同于 list
```

### 3.3 独立命令 (不变)

```
claude up                      保持顶级 (简短的 bootstrap 命令)
claude rollback [target]       保持顶级 (低频运维命令)
```

## 四、跨平台后台引擎

### 4.1 引擎抽象

```typescript
// src/cli/bg/engine.ts
export interface BgEngine {
  readonly name: string

  /** 当前平台是否可用 */
  available(): Promise<boolean>

  /** 启动后台会话 */
  start(opts: BgStartOptions): Promise<BgStartResult>

  /** 附着到后台会话（blocking） */
  attach(session: SessionEntry): Promise<void>
}

export interface BgStartOptions {
  sessionName: string
  args: string[]
  env: Record<string, string | undefined>
  logPath: string
  cwd: string
}

export interface BgStartResult {
  pid: number
  sessionName: string
  logPath: string
  engineUsed: string
}
```

### 4.2 三种引擎实现

| 引擎 | 平台 | 启动方式 | attach 方式 |
|------|------|---------|------------|
| TmuxEngine | macOS/Linux (有 tmux) | `tmux new-session -d` | `tmux attach-session` |
| DetachedEngine | Windows / 无 tmux 的 macOS/Linux | `spawn({ detached, stdio→logFile })` | `tail -f` 日志文件 |

#### DetachedEngine 详细设计

**启动 (`start`)**:
```typescript
// 1. 打开日志文件 fd
const logFd = fs.openSync(logPath, 'a')
// 2. detached spawn, stdout/stderr 重定向到日志
const child = spawn(process.execPath, execArgs, {
  detached: true,
  stdio: ['ignore', logFd, logFd],
  env,
  cwd,
})
child.unref()
fs.closeSync(logFd)
// 3. 写 sessions/<PID>.json
```

**附着 (`attach`)**:
```typescript
// 跨平台 tail -f 实现
// 1. 读取已有日志内容输出到 stdout
// 2. fs.watch(logPath) 监听变化
// 3. 每次变化读取新增内容
// 4. Ctrl+C 退出 tail（不杀后台进程）
```

#### 引擎选择逻辑

```typescript
// src/cli/bg/engines/index.ts
export async function selectEngine(): Promise<BgEngine> {
  if (process.platform === 'win32') {
    return new DetachedEngine()
  }

  const tmux = new TmuxEngine()
  if (await tmux.available()) {
    return tmux
  }

  return new DetachedEngine()
}
```

### 4.3 SessionEntry 扩展

```typescript
interface SessionEntry {
  // ... 现有字段
  engine: 'tmux' | 'detached'   // 新增: 记录使用的引擎
  tmuxSessionName?: string       // tmux 引擎才有
  logPath?: string               // 两种引擎都有
}
```

`attach` 时根据 `session.engine` 选择对应的 attach 策略。

## 五、文件变更清单

### 新增文件 (10 个)

```
src/cli/bg/engine.ts                   BgEngine 接口定义
src/cli/bg/engines/tmux.ts             TmuxEngine (从 bg.ts 提取)
src/cli/bg/engines/detached.ts         DetachedEngine (新实现)
src/cli/bg/engines/index.ts            引擎选择 + re-export
src/cli/bg/tail.ts                     跨平台日志 tail (用于 detached attach)
src/commands/daemon/index.ts           /daemon 

# FILE: docs/features/lan-pipes.md

# LAN Pipes — 局域网多机器群控指南

## 什么是 LAN Pipes

LAN Pipes 让多台机器上的 Claude Code 实例通过局域网自动发现并协作。你可以在一台机器（main）上操控其他机器（sub）上的 Claude Code，发送 prompt、查看执行结果、审批权限请求——全程零配置。

基于本机 Pipe IPC（`UDS_INBOX`）扩展，新增 TCP 传输层 + UDP Multicast 发现。

## 前置条件

- 两台或以上机器在同一局域网
- 每台机器安装了 CCB 并能 `bun run dev`
- Feature flag `LAN_PIPES`（dev/build 默认开启）
- 防火墙允许 UDP 7101 + TCP 动态端口（见下方配置）

## 快速开始

### 第一步：配置防火墙

**每台机器都需要执行。**

**Windows**（管理员 PowerShell）：
```powershell
New-NetFirewallRule -DisplayName "CCB LAN Beacon (UDP)" -Direction Inbound -Protocol UDP -LocalPort 7101 -Action Allow -Profile Private
New-NetFirewallRule -DisplayName "CCB LAN Pipes (TCP)" -Direction Inbound -Protocol TCP -LocalPort 1024-65535 -Program (Get-Command bun).Source -Action Allow -Profile Private
New-NetFirewallRule -DisplayName "CCB LAN Beacon Out (UDP)" -Direction Outbound -Protocol UDP -RemotePort 7101 -Action Allow -Profile Private
```

验证网络为"专用"（非公共）：`Get-NetConnectionProfile`

**macOS**：
首次运行时系统弹出"允许接受传入连接"对话框，点击"允许"。

如果使用 pf 防火墙：
```bash
echo "pass in proto udp from any to any port 7101" | sudo pfctl -ef -
```

**Linux**（firewalld）：
```bash
sudo firewall-cmd --zone=trusted --add-port=7101/udp --permanent
sudo firewall-cmd --zone=trusted --add-port=1024-65535/tcp --permanent
sudo firewall-cmd --reload
```

**Linux**（iptables）：
```bash
sudo iptables -A INPUT -p udp --dport 7101 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 1024:65535 -m owner --uid-owner $(id -u) -j ACCEPT
```

### 第二步：启动

```bash
# 机器 A（例如 192.168.50.22）
bun run dev

# 机器 B（例如 192.168.50.27）
bun run dev
```

启动后等待 3-5 秒（beacon 广播间隔），两边自动发现并连接。

### 第三步：查看和操作

在任一台机器上：
```
/pipes
```

输出示例：
```
pipe: cli-a91bad56 (main) 192.168.50.22  2/3 selected

Main machine: 205d6c3a... (this machine)
  [main] cli-a91bad56  XC/192.168.50.22  [alive] (you)
  ☑ [sub-1] cli-da029538  XC/192.168.50.22  [alive] [connected]

LAN Peers:
  ☐ [main] cli-04d67950  vmwin11/192.168.50.27  tcp:192.168.50.27:58853  [LAN]
```

### 第四步：选中目标并发送任务

1. 按 `Shift+↓` 展开选择面板
2. `↑↓` 移动到 LAN peer
3. `Space` 选中
4. `Enter` 确认
5. 输入 prompt，自动路由到远端执行

远端执行结果会流式回传到你的消息列表：
```
[main vmwin11/192.168.50.27 / cli-04d67950] 正在检查 git status...
[main vmwin11/192.168.50.27 / cli-04d67950] Completed
```

## 完整命令参考

| 命令 | 说明 |
|------|------|
| `/pipes` | 显示所有实例（本机 + LAN），Shift+↓ 展开选择面板 |
| `/pipes select <name>` | 选中某实例 |
| `/pipes all` | 全选 |
| `/pipes none` | 取消全选 |
| `/attach <name>` | 手动 attach（自动识别 LAN peer 并通过 TCP 连接） |
| `/detach <name>` | 断开连接 |
| `/send <name> <msg>` | 向指定 pipe 发送消息 |
| `/send tcp:host:port <msg>` | 直接通过 TCP 地址发送 |
| `/claim-main` | 强制声明为 main |
| `/pipe-status` | 显示详细状态 |
| `/peers` | 列出所有已发现的 peer |

## 快捷键

| 快捷键 | 场景 | 作用 |
|--------|------|------|
| `Shift+↓` | 状态栏可见时 | 展开/收起选择面板 |
| `↑ / ↓` | 面板展开时 | 移动光标 |
| `Space` | 面板展开时 | 选中/取消 |
| `Enter` | 面板展开时 | 确认关闭 |
| `Esc` | 面板展开时 | 取消关闭 |
| `← / →` | 有选中 pipe 时 | 切换路由模式 |
| `M` | 面板展开时 | 同 ←/→ 切换路由模式 |

## 路由模式

| 模式 | 显示 | 行为 |
|------|------|------|
| `selected pipes only` | 绿色 | prompt 仅发送到选中的 pipe，本地不执行 |
| `local main` | 灰色 | prompt 仅在本地执行，不转发 |

切换路由模式不会清空选择。

## 权限转发

当远端 slave 执行需要权限的工具（如 BashTool）时：
1. slave 发送 `permission_request` 到 main
2. main 弹出权限确认对话框，显示 `[role hostname/ip / pipeName]`
3. 用户确认/拒绝
4. 结果发回 slave，继续或中断

## 工作原理

### 发现机制

- 每台机器启动时创建 UDP multicast beacon
- 组地址 `224.0.71.67`，端口 `7101`，TTL=1（不跨路由器）
- 每 3 秒广播一次自身信息（pipeName、IP、TCP 端口、角色）
- 15 秒未收到广播则标记 peer 丢失

### 通信机制

- 本机实例：UDS（Unix Domain Socket / Named Pipe）
- 跨机器：TCP（动态端口，通过 beacon 发现）
- 协议：NDJSON（每行一个 JSON 对象）
- 消息类型：ping/pong、attach/detach、prompt/stream/done/error、permission

### 角色模型

| 角色 | 说明 |
|------|------|
| `main` | 首个启动的实例 |
| `sub` | 同机后续启动的实例 |
| `master` | attach 了至少一个 slave 的实例 |
| `slave` | 被 master attach 的实例 |

跨机器 attach 时，两边都可以是 main——不要求对方必须是 sub。

## 常见问题

### 看不到 LAN peer

1. 检查防火墙是否放行 UDP 7101
2. `Get-NetConnectionProfile`（Windows）确认网络为"专用"
3. 确认两台机器在同一子网（`ping` 能通）
4. 路由器未开启 AP 隔离

### 连接超时

1. 检查 TCP 入站防火墙规则
2. 确认没有 VPN 劫持流量
3. 尝试 `/send tcp:ip:port hello` 直接测试

### beacon 绑到了错误网卡

Windows 上 WSL/Docker 虚拟网卡可能劫持 multicast。beacon 会自动选择非内部 IPv4 接口。如果选错，检查 `getLocalIp()` 返回值。

## 安全说明

- TCP 连接当前**无认证**——同 LAN 内知道端口号即可连接
- Multicast TTL=1，不跨路由器
- AI 通过 `SendMessageTool` 发送 `tcp:` 消息时需**用户显式确认**
- 建议仅在信任的局域网中使用


# FILE: docs/features/acp-zed.md

# ACP (Agent Client Protocol) — Zed / IDE 集成

> Feature Flag: `FEATURE_ACP=1`（build 和 dev 模式默认启用）
> 实现状态：可用（支持 Zed、Cursor 等 ACP 客户端）
> 源码目录：`src/services/acp/`

## 一、功能概述

ACP (Agent Client Protocol) 是一种标准化的 stdio 协议，允许 IDE 和编辑器通过 stdin/stdout 的 NDJSON 流驱动 AI Agent。CCB 实现了完整的 ACP agent 端，可以被 Zed、Cursor 等支持 ACP 的客户端直接调用。

### 核心特性

- **会话管理**：新建 / 恢复 / 加载 / 分叉 / 关闭会话
- **历史回放**：恢复会话时自动加载并回放对话历史
- **权限桥接**：ACP 客户端的权限决策映射到 CCB 的工具权限系统
- **斜杠命令 & Skills**：加载真实命令列表，支持 `/commit`、`/review` 等 prompt 型 skill
- **Context Window 跟踪**：精确的 usage_update，含 model prefix matching
- **Prompt 排队**：支持连续发送多条 prompt，自动排队处理
- **模式切换**：auto / default / acceptEdits / plan / dontAsk / bypassPermissions
- **模型切换**：运行时切换 AI 模型

## 二、架构

```
┌──────────────┐    NDJSON/stdio    ┌──────────────────┐
│  Zed / IDE   │ ◄────────────────► │  CCB ACP Agent   │
│  (Client)    │   stdin / stdout   │  (Agent)         │
└──────────────┘                    │                  │
                                    │  entry.ts        │ ← stdio → NDJSON stream
                                    │  agent.ts        │ ← ACP protocol handler
                                    │  bridge.ts       │ ← SDKMessage → ACP SessionUpdate
                                    │  permissions.ts  │ ← 权限桥接
                                    │  utils.ts        │ ← 通用工具
                                    │                  │
                                    │  QueryEngine     │ ← 内部查询引擎
                                    └──────────────────┘
```

### 文件职责

| 文件 | 职责 |
|------|------|
| `entry.ts` | 入口，创建 stdio → NDJSON stream，启动 `AgentSideConnection` |
| `agent.ts` | 实现 ACP `Agent` 接口：会话 CRUD、prompt、cancel、模式/模型切换 |
| `bridge.ts` | `SDKMessage` → ACP `SessionUpdate` 转换：文本/思考/工具/用量/编辑 diff |
| `permissions.ts` | ACP `requestPermission()` → CCB `CanUseToolFn` 桥接 |
| `utils.ts` | Pushable、流转换、权限模式解析、session fingerprint、路径显示 |

## 三、配置 Zed 编辑器

### 3.1 Zed settings.json 配置

打开 Zed 的 `settings.json`（`Cmd+,` → Open Settings），添加 `agent_servers` 配置：

```json
{
  "agent_servers": {
    "ccb": {
      "type": "custom",
      "command": "ccb",
      "args": ["--acp"]
    }
  }
}
```

### 3.3 API 认证配置

CCB 的 ACP agent 在启动时会自动加载 `settings.json` 中的环境变量（`ANTHROPIC_BASE_URL`、`ANTHROPIC_AUTH_TOKEN` 等）。确保已通过 `/login` 配置好 API 供应商。

也可通过环境变量传入：

```json
{
  "agent_servers": {
    "claude-code": {
      "command": "ccb",
      "args": ["--acp"],
      "env": {
        "ANTHROPIC_BASE_URL": "https://api.example.com/v1",
        "ANTHROPIC_AUTH_TOKEN": "sk-xxx"
      }
    }
  }
}
```

### 3.4 在 Zed 中使用

1. 配置完成后重启 Zed
2. 打开任意项目目录
3. 按 `Cmd+'`（macOS）或 `Ctrl+'`（Linux）打开 Agent Panel
4. 在 Agent Panel 顶部的下拉菜单中选择 **claude-code**
5. 开始对话

### 3.5 功能说明

| 功能 | 操作 |
|------|------|
| 对话 | 在 Agent Panel 中直接输入消息 |
| 斜杠命令 | 输入 `/` 查看可用 skills 列表（如 `/commit`、`/review`） |
| 工具权限 | 弹出权限请求时选择 Allow / Reject / Always Allow |
| 模式切换 | 通过 Agent Panel 的设置菜单切换 auto/default/plan 等模式 |
| 模型切换 | 通过 Agent Panel 的设置菜单切换 AI 模型 |
| 会话恢复 | 关闭重开 Zed 后，之前的会话可自动恢复（含历史消息） |

## 四、配置其他 ACP 客户端

ACP 是开放协议，任何支持 ACP 的客户端都可以连接 CCB。通用配置模式：

```
命令: ccb --acp
参数: ["--acp"]
通信: stdin/stdout NDJSON
协议版本: ACP v1
```

### 4.1 Cursor

在 Cursor 的设置中配置 MCP / Agent Server，使用同样的 `ccb --acp` 命令。

### 4.2 自定义客户端

使用 `@agentclientprotocol/sdk` 可以快速构建 ACP 客户端：

```typescript
import { ClientSideConnection, ndJsonStream } from '@agentclientprotocol/sdk'

// 创建连接（将 ccb --acp 作为子进程启动）
const child = spawn('ccb', ['--acp'])
const stream = ndJsonStream(
  Writable.toWeb(child.stdin),
  Readable.toWeb(child.stdout),
)

const client = new ClientSideConnection(stream)

// 初始化
await client.initialize({ clientCapabilities: {} })

// 创建会话
const { sessionId } = await client.newSession({
  cwd: '/path/to/project',
})

// 发送 prompt
const response = await client.prompt({
  sessionId,
  prompt: [{ type: 'text', text: 'Hello, explain this project' }],
})

// 监听 session 更新
client.on('sessionUpdate', (update) => {
  console.log('Update:', update)
})
```

## 五、ACP 协议支持矩阵

| 方法 | 状态 | 说明 |
|------|------|------|
| `initialize` | ✅ | 返回 agent 信息和能力 |
| `authenticate` | ✅ | 无需认证（自托管） |
| `newSession` | ✅ | 创建新会话 |
| `resumeSession` | ✅ | 恢复已有会话（含历史回放） |
| `loadSession` | ✅ | 加载指定会话（含历史回放） |
| `listSessions` | ✅ | 列出可用会话 |
| `forkSession` | ✅ | 分叉会话 |
| `closeSession` | ✅ | 关闭会话 |
| `prompt` | ✅ | 发送消息，支持排队 |
| `cancel` | ✅ | 取消当前/排队的 prompt |
| `setSessionMode` | ✅ | 切换权限模式 |
| `setSessionModel` | ✅ | 切换 AI 模型 |
| `setSessionConfigOption` | ✅ | 动态修改配置 |

### SessionUpdate 类型

| 类型 | 状态 | 说明 |
|------|------|------|
| `agent_message_chunk` | ✅ | 助手文本消息 |
| `agent_thought_chunk` | ✅ | 思考/推理内容 |
| `user_message_chunk` | ✅ | 用户消息（历史回放） |
| `tool_call` | ✅ | 工具调用开始 |
| `tool_call_update` | ✅ | 工具调用结果/状态更新 |
| `usage_update` | ✅ | token 用量 + context window |
| `plan` | ✅ | TodoWrite → plan entries |
| `available_commands_update` | ✅ | 斜杠命令 & skills 列表 |
| `current_mode_update` | ✅ | 模式切换通知 |
| `config_option_update` | ✅ | 配置更新通知 |

