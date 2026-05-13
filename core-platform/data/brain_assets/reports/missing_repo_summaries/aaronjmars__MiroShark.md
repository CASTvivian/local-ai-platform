# Missing Repo Summary Source: aaronjmars/MiroShark

- URL: https://github.com/aaronjmars/MiroShark
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/aaronjmars__MiroShark
- Clone Status: cloned
- Language: Python
- Stars: 1142
- Topics: ai-simulation, financial-forecasting, future-prediction, mirofish, swarm, swarm-intelligence
- Description: Simulate anything, for $1 & less than 10 min — Universal Swarm Intelligence Engine

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="./docs/images/miroshark.jpg" alt="MiroShark" width="120" />
</p>

<h1 align="center">MiroShark</h1>

<p align="center">
  <a href="https://github.com/aaronjmars/MiroShark/stargazers"><img src="https://img.shields.io/github/stars/aaronjmars/MiroShark?style=flat-square&logo=github" alt="GitHub stars"></a>
  <a href="https://github.com/aaronjmars/MiroShark/network/members"><img src="https://img.shields.io/github/forks/aaronjmars/MiroShark?style=flat-square&logo=github" alt="GitHub forks"></a>
  <a href="https://x.com/miroshark_"><img src="https://img.shields.io/badge/Follow-%40miroshark__-black?style=flat-square&logo=x&labelColor=000000" alt="Follow on X"></a>
  <a href="https://bankr.bot/discover/0xd7bc6a05a56655fb2052f742b012d1dfd66e1ba3"><img src="https://img.shields.io/badge/MiroShark%20on-Bankr-orange?style=flat-square&labelColor=1a1a2e" alt="MiroShark on Bankr"></a>
</p>

<p align="center">
  <a href="#english">English</a> · <a href="#中文">中文</a>
</p>

<p align="center">
  <img src="./docs/images/miroshark.gif" alt="MiroShark Demo" />
</p>

---

<a id="english"></a>

## English

> **Simulate anything, for $1 & less than 10 min — Universal Swarm Intelligence Engine**
> Drop in anything — a press release, a news headline, a policy draft, a question you can't answer, a historical what-if — and MiroShark spawns hundreds of agents that react to it hour by hour. Posting, arguing, trading, changing their minds.

### What it does

- You bring a scenario. MiroShark builds the world around it.
- Hundreds of grounded agents. Twitter, Reddit, and a prediction market. Hour by hour.
- Chat with any of them. Drop breaking news mid-run. Fork the timeline.
- Get a report on what happened, citing actual posts and trades.

### Quick start

The recommended path: **one [OpenRouter](https://openrouter.ai/) key + the `./miroshark` launcher.** First simulation in ~10 min, ~$1.

**Prereqs** — Python 3.11+, Node 18+, Neo4j, and an [OpenRouter key](https://openrouter.ai/).

Install Neo4j — the launcher starts it for you:

- **macOS** — `brew install neo4j`
- **Linux** — `sudo apt install neo4j` *(or your distro's equivalent)*
- **Windows** — install [Neo4j Desktop](https://neo4j.com/download/) *(native, GUI — start the DB there, then run the launcher from WSL2 or Git Bash)*, or run the whole stack inside [WSL2](https://learn.microsoft.com/windows/wsl/install) and follow the Linux steps
- **Zero-install** — create a free [Neo4j Aura](https://neo4j.com/cloud/aura-free/) cloud instance and point `NEO4J_URI` / `NEO4J_PASSWORD` at it in `.env`

Then:

```bash
git clone https://github.com/aaronjmars/MiroShark.git && cd MiroShark
cp .env.example .env
# Paste your OpenRouter key into the LLM_API_KEY / SMART_API_KEY /
# NER_API_KEY / OPENAI_API_KEY / EMBEDDING_API_KEY slots (same key,
# 5 places). Default lineup is Mimo V2 Flash + Grok-4.1 Fast.
./miroshark
```

The launcher checks dependencies, starts Neo4j, installs frontend + backend, and serves `:3000` + `:5001`. Ctrl+C stops everything. Open `http://localhost:3000` and drop in a document.

**Other paths** — [one-click Railway / Render deploy](docs/INSTALL.md#one-click-cloud), [Docker + Ollama](docs/INSTALL.md#option-b-docker--local-ollama), [manual Ollama](docs/INSTALL.md#option-c-manual--local-ollama), [Claude Code CLI](docs/INSTALL.md#option-d-claude-code-no-api-key) — all in **[docs/INSTALL.md](docs/INSTALL.md)**.

<p align="center">
  <img src="./docs/images/miroshark-overview.jpg" alt="MiroShark Overview" />
</p>

### Interface language

After launching, click the **中 / EN** toggle in the top-right of the navbar to switch between English and Chinese. Your choice is persisted in the browser, and the public gallery card titles + descriptions follow the active locale.

### Features

| Feature | What it does |
|---|---|
| **Smart Setup** | Drop in a doc → three auto-generated Bull / Bear / Neutral scenarios in ~2s |
| **What's Trending** | Pick a live news item from RSS feeds; pre-fills the scenario in one click |
| **Just Ask** | Type a question with no document — MiroShark researches and writes the seed briefing |
| **Shareable Scenario Links** | Drop a `?scenario=...&url=...` URL into a tweet or blog post — readers land on the New Sim form already pre-filled. `?template=<slug>` auto-launches one of the preset templates. The un-run-scenario counterpart to "Fork this scenario" on `/watch` and `/share` |
| **Counterfactual Branching** | Fork a running simulation with an injected event ("what if the CEO resigns in round 24?") |
| **Director Mode** | Inject breaking news into the *current* timeline without forking |
| **Preset Templates** | 6 benchmarked scenarios: crypto launch, corporate crisis, political debate, product announcement, campus controversy, historical what-if |
| **Live Oracle Data** | Opt-in grounded seeds from the [FeedOracle](https://mcp.feedoracle.io/mcp) MCP (484 tools) |
| **Per-Agent MCP Tools** | Personas can invoke real MCP tools (web search, APIs) during simulation |
| **Custom Wonderwall Endpoint** | Point the simulation loop at any OpenAI-compatible endpoint (self-hosted vLLM, Modal, fine-tunes…) without affecting Default/Smart/NER. Set `WONDERWALL_BASE_URL` + `WONDERWALL_API_KEY` |
| **Embed & Publish** | Public/private toggle + embed URLs for sharing finished runs |
| **Social Share Card** | 1200×630 PNG that auto-unfurls scenario, status, quality, and belief split on Twitter/X, Discord, Slack, LinkedIn |
| **Animated Belief Replay** | 1200×630 GIF — one frame per round, belief bars sliding to each round's distribution. Discord and Slack auto-play GIFs from the direct URL |
| **Transcript Export** | Per-round agent posts + stance labels as Markdown (YAML front matter for Notion / Obsidian / Substack) or structured JSON (for SDKs and LLM-as-judge pipelines) |
| **Trajectory Export** | One row per round as RFC 4180 CSV or JSONL — `pandas.read_csv("…/trajectory.csv")` lands ready for Pandas / Excel / Tableau / R / Observable. Same ±0.2 stance threshold as every other surface |
| **Tweet Thread Export** | `GET /api/simulation/<id>/thread.txt` — auto-formatted X / Twitter thread, intro tweet + one tweet per belief inflection point + close tweet (with watch + share URLs). Each tweet ≤280 chars; copy individual tweets or the whole thread. Pairs with the share card / replay GIF / transcript / trajectory / watch page as the sixth share format |
| **Live Watch Page** | `/watch/<sim_id>` — minimal full-viewport broadcast page with a vanilla-JS poller that refreshes the belief bar, round counter, and progress bar every 15 s while the simulation runs. Auto-unfurls as a 1200×630 image card when tweeted; the "tweet a sim mid-run" format alongside the finished-result share card |
| **Public Gallery** | `/explore` browses every published simulation as a card grid — preview the share card, consensus split, and quality health; click to open or one-click fork |
| **Gallery Search & Filter** | Keyword search + bullish/neutral/bearish + excellent/good/fair/poor + sort by date/rounds/agents/trending on `/explore` and `/verified`. `trending` ranks by cumulative share-surface serves so the most-distributed sims float to the top. URL-encoded so `?q=aave&consensus=bearish` is bookmarkable. Same ±0.2 stance threshold as every other surface |
| **Verified Predictions** | Annotate any public sim with the real-world outcome (called it / partial / called wrong + URL). `/verified` is the dedicated hall of calls that landed |
| **RSS / Atom Feeds** | `/api/feed.atom` + `/api/feed.rss` — every newly published simulation lands in Feedly / Readwise / Inoreader / NetNewsWire / Obsidian RSS without anyone curating it. `?verified=1` for the verified-only stream |
| **Article Generation** | Substack-style write-up of what happened, grounded in actual posts and trades |
| **Interaction Network** | Force-directed agent-to-agent graph with echo-chamber metrics |
| **Demographics** | Archetype clustering (analyst / influencer / retail / observer…) |
| **Quality Diagnostics** | Health score per run — engagement, coherence, diversity, variance |
| **History Database** | Search, clone, export, or delete any past simulation |
| **Trace Interview** | See the full reasoning chain behind an agent's reply, not just the reply |
| **Push Notifications** | Web-push alerts when long-running graph / sim / report jobs finish |
| **Completion Webhook** | POST a JSON summary the moment a sim finishes — wires Slack, Discord, Zapier, Make, n8n, or any custom endpoint with one URL field |
| **Webhook Signature Verification** | Optional `WEBHOOK_SECRET` HMAC-signs every dispatched payload with an `X-MiroShark-Signature: sha256=<hex>` header. Recipients verify in three lines of stdlib `hmac` — same scheme Stripe and GitHub use. Empty secret = no header, fully backward compatible |
| **Webhook Delivery Log** | Per-sim `webhook-log.jsonl` records every dispatch attempt (status code, latency, error). Inspect from the EmbedDialog and re-fire any failed delivery with a "Retry" button — closes the operational blindspot every Zapier / n8n integration eventually hits |
| **Surface Usage Analytics** | `GET /api/simulation/<id>/surface-stats` — per-share-surface request counters (share card / replay GIF / transcript / trajectory / thread / watch page / Atom / RSS / reproduce.json / lineage / notebook.ipynb) with a synthetic `total`. Inbound observability for the distribution loop the webhook log tracks on the outbound side |
| **Reproducibility Config** | `GET /api/simulation/<id>/reproduce.json` — citation primitive for the share surfaces. A v1-schema JSON blob carrying every parameter another operator needs to re-run the same simulation: scenario, agent count, total rounds, platform toggles, time-config knobs, director events, and fork / counterfactual lineage. Identical exports of a finished sim are bytewise-identical, so the file hash is a stable citation key |
| **Jupyter Notebook Export** | `GET /

# FILE: docs/ARCHITECTURE.md

# Architecture

<sup>English · [中文](ARCHITECTURE.zh-CN.md)</sup>

## Pipeline overview

1. **Graph build** — Extracts entities and relationships from your document into a Neo4j knowledge graph. NER uses few-shot examples and rejection rules to filter garbage entities. Chunk processing is parallelized with batched Neo4j writes (UNWIND).

2. **Agent setup** — Generates personas grounded in the knowledge graph. Each entity gets 5 layers of context: graph attributes, relationships, semantic search, related nodes, and LLM-powered web research (auto-triggers for public figures or when graph context is thin). Individual vs. institutional personas are detected automatically via keyword matching.

3. **Simulation** — All three platforms (Twitter, Reddit, Polymarket) run simultaneously via `asyncio.gather`. A single LLM-generated prediction market with non-50/50 starting price drives Polymarket trading. Agents see cross-platform context: traders read Twitter/Reddit posts, social media agents see market prices. A sliding-window round memory compacts old rounds via background LLM calls. Belief states track stance, confidence, and trust per agent with heuristic updates each round.

4. **Report** — A ReACT agent writes analytical reports using `simulation_feed` (actual posts/comments/trades), `market_state` (prices/P&L), graph search, belief trajectory, and Nash equilibrium tools. Reports cite what agents actually said and how markets moved.

5. **Interaction** — Chat directly with any agent via persona chat, send questions to groups, or branch the simulation with a counterfactual event at any round to explore "what if" scenarios side-by-side. Click any agent to view their full profile and simulation history.

## Cross-platform simulation engine

All three platforms execute simultaneously each round. Data flows between them:

```
                    ┌─────────────────────────────────────────┐
                    │         Round Memory (sliding window)    │
                    │  Old rounds: LLM-compacted summaries     │
                    │  Previous round: full action detail       │
                    │  Current round: live (partial)            │
                    └──────┬──────────┬──────────┬────────────┘
                           │          │          │
                    ┌──────▼───┐ ┌────▼─────┐ ┌─▼────────────┐
                    │ Twitter  │ │  Reddit  │ │  Polymarket   │
                    │          │ │          │ │               │
                    │ Posts    │ │ Comments │ │ Trades (AMM)  │
                    │ Likes    │ │ Upvotes  │ │ Single market │
                    │ Reposts  │ │ Threads  │ │ Buy/Sell/Wait │
                    └──────┬───┘ └────┬─────┘ └─┬────────────┘
                           │          │          │
                    ┌──────▼──────────▼──────────▼────────────┐
                    │         Market-Media Bridge              │
                    │  Social sentiment → trader prompts       │
                    │  Market prices → social media prompts    │
                    │  Social posts → trader observation       │
                    └──────┬──────────┬──────────┬────────────┘
                           │          │          │
                    ┌──────▼──────────▼──────────▼────────────┐
                    │         Belief State (per agent)         │
                    │  Positions: topic → stance (-1 to +1)    │
                    │  Confidence: topic → certainty (0 to 1)  │
                    │  Trust: agent → trust level (0 to 1)     │
                    └─────────────────────────────────────────┘
```

## Polymarket integration

A single prediction market is generated by the LLM during config creation, tailored to the simulation's core question. Market-title generation routes through the **Smart** slot (see [Models](MODELS.md)) so phrasing is sharp, time-bound, and resolvable — this is the prompt that frames the entire simulation, so it's worth the stronger model. The AMM uses constant-product pricing with non-50/50 initial prices based on the LLM's probability estimate. Traders see actual Twitter/Reddit posts in their observation prompt alongside portfolio and market data.

## Performance

| Optimization | Before | After |
|---|---|---|
| Neo4j writes | 1 transaction per entity | Batched UNWIND (10x faster) |
| Chunk processing | Sequential | Parallel ThreadPoolExecutor (3x faster) |
| Config generation | Sequential batches | Parallel batches (3x faster) |
| Platform execution | Twitter+Reddit parallel, Polymarket sequential | All 3 parallel |
| Memory compaction | Blocking | Background thread |

## Web enrichment

When generating personas for public figures (politicians, CEOs, founders) or when graph context is thin (<150 chars), the system makes an LLM research call to enrich the profile with real-world data. Set `WEB_SEARCH_MODEL=perplexity/sonar-pro` in `.env` for grounded web search via OpenRouter.

## Per-round frame API

`GET /api/simulation/<id>/frame/<round>` returns a compact snapshot of a single round — actions, active-agent count, market prices at that round, and belief state — for scrubbing UIs on large simulations. Alternative to loading all N × M actions upfront via `/run-status/detail`. Query params: `platforms=twitter,reddit,polymarket`, `include_belief`, `include_market`. Used by **ReplayView** for timeline scrubbing and by the CLI (`miroshark-cli frame <id> <round>`).

## Memory & retrieval pipeline

Beyond the simulation engine, MiroShark ships a research-grade graph memory stack inspired by Hindsight, Graphiti, Letta, and HippoRAG. Every ingested document and simulation action flows through:

### Ingestion

```
text → NER (with ontology)
     → batch embed (OpenRouter text-embedding-3-large or local Ollama)
     → Entity resolution (fuzzy + vector + LLM reflection — dedups "NeuralCoin"/"Neural Coin"/"NC")
     → MERGE entities into Neo4j with canonical UUIDs
     → Contradiction detection (LLM adjudicates same-endpoi

# FILE: docs/MCP.zh-CN.md

<sup>[English](MCP.md) · 中文</sup>

# MCP

MiroShark 提供两套 MCP 表面:一个**独立 MCP server**,让你可以在 Claude Desktop、Cursor、Windsurf 或 Continue 里查询自己的知识图谱;还有一组**报告智能体工具**,被 ReACT 报告智能体内部使用。

> **提示:** 打开 MiroShark → **设置 → AI Integration · MCP**,可以为每个客户端拿到自动生成的、可直接复制粘贴的配置片段。设置面板会调用 `GET /api/mcp/status`,并把你机器上的绝对路径打进片段里。

## 暴露了什么

`backend/mcp_server.py` 跑在 **stdio** 上(无需开端口、无需常驻守护进程 — 你的 MCP 客户端按需启动它),并使用你已有的 `.env` 中的 Neo4j + LLM 凭据。

| 工具 | 作用 |
|---|---|
| `list_graphs` | 浏览图谱 + 实体/边数量 |
| `search_graph` | 完整的混合 + 重排流水线,带 `kinds` / `as_of` 过滤 |
| `browse_clusters` | 社区缩放(首次调用时自动构建) |
| `search_communities` | 直接在簇摘要上做语义检索 |
| `get_community` | 展开一个簇及其成员 |
| `list_reports` | 某个图谱上生成过的报告 |
| `list_report_sections` | 一份报告的各个章节 |
| `get_reasoning_trace` | 一个章节的完整 ReACT 决策链 |

**示例提示词:** *"列出我的 MiroShark 图谱,在最大的那个上 browse clusters 找任何与 oracle 漏洞相关的内容,然后给我看那个图谱上最近一份报告的推理链。"*

---

## Claude Desktop

打开 **Claude Desktop → Settings → Developer → Edit Config**。文件位置:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

把下面这块加进 `mcpServers`(或合并进去) — 把 `/absolute/path/to/MiroShark/backend` 替换成你机器上的路径:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

重启 Claude Desktop。`miroshark` 工具会出现在锤子 / 🛠️ 菜单里。

> **没有 `uv`?** 直接用 Python 解释器:
> ```json
> "command": "/absolute/path/to/MiroShark/backend/.venv/bin/python",
> "args": ["/absolute/path/to/MiroShark/backend/mcp_server.py"]
> ```

---

## Cursor

Cursor 从下面任意一处读 `mcpServers`:

- 工作区配置:你正在工作的仓库里 `.cursor/mcp.json`,**或者**
- 全局配置:`~/.cursor/mcp.json`

加上:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

重新加载 Cursor 窗口(`Cmd/Ctrl+Shift+P → Reload Window`)。当你在聊天里 `@mention` MCP 时,miroshark 工具就会出现。

---

## Windsurf

Windsurf 从 `~/.codeium/windsurf/mcp_config.json` 读 MCP 服务器:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

然后打开 **Cascade → MCP Servers → Refresh**。miroshark 工具就可以从 Cascade 对话中调用了。

---

## Continue(VS Code / JetBrains)

Continue ≥ 0.9.x 通过 `~/.continue/config.json` 支持 MCP:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "uv",
          "args": [
            "run",
            "--directory",
            "/absolute/path/to/MiroShark/backend",
            "python",
            "mcp_server.py"
          ]
        }
      }
    ]
  }
}
```

保存后重新加载你的编辑器。

---

## 验证它能跑

1. 启动你的 MCP 客户端。几秒内它应该会以子进程方式启动 `mcp_server.py`。
2. 提问:*"用 `list_graphs` 工具列出我的 MiroShark 图谱。"* — 助手应当返回每个图谱一行,以及实体/边数量。如果返回为空(`No graphs found.`),先在 MiroShark UI 中至少构建一个图谱(步骤 1:图谱构建)。
3. MiroShark UI 中 **设置 → AI Integration · MCP** 面板暴露了相同的 Neo4j 健康探测 — 如果面板说 *Neo4j down*,MCP 工具会以同样的方式失败。

## 故障排查

| 现象 | 可能原因 | 修复 |
|---|---|---|
| 客户端 MCP 日志中出现 `uv: command not found` | `uv` 不在客户端继承的 PATH 上 | 切换到 **没有 uv?** 那段(直接解释器路径),或者全局安装 `uv`。 |
| `list_graphs` 返回 `No graphs found.` | Neo4j 是空的 | 在 MiroShark UI 跑一次模拟,至少写入一个图谱。 |
| `Neo.ClientError.Security.Unauthorized` | `.env` 中的 `NEO4J_PASSWORD` 已过期 | 更新 `.env` 并重启任何已经派发过该 server 的客户端。 |
| Server 启动后立刻退出 | 缺少 `mcp` Python 包 | MCP SDK 在 `pyproject.toml` 中 — 确认 `uv sync`(或 `pip install -e backend/`)正常完成。 |
| 设置面板上片段显示 `mcp_script: missing` | 你正在跑后端的 checkout 与含 `mcp_server.py` 的 checkout 不是同一个 | 重新克隆或 `git pull`,确保 `backend/mcp_server.py` 存在。 |

## 报告智能体工具

ReACT 报告智能体在内部暴露这些工具(通过 `REPORT_AGENT_MAX_TOOL_CALLS` 配置):

| 工具 | 用途 |
|---|---|
| `insight_forge` | 围绕一个具体问题做多轮深度分析 |
| `panorama_search` | 混合 vector + BM25 + 图谱检索 |
| `quick_search` | 轻量关键词检索 |
| `interview_agents` | 与模拟智能体实时对话 |
| `analyze_trajectory` | 信念漂移 — 收敛、极化、转折点 |
| `analyze_equilibrium` | 在拟合到最终信念分布的 2 人立场博弈上求纳什均衡 — 揭示观察到的结果是否与自利博弈一致(需要 `nashpy`) |
| `analyze_graph_structure` | 中心性 / 社区 / 桥接分析 |
| `find_causal_path` | 两个实体之间的图谱遍历 |
| `detect_contradictions` | 图中互相冲突的边 |
| `simulation_feed` | 原始动作日志,按平台 / 查询 / 轮次过滤 |
| `market_state` | Polymarket 价格、交易、组合 |
| `browse_clusters` | 社区缩放(用于全局定位) |


# FILE: docs/CLI.zh-CN.md

<sup>[English](CLI.md) · 中文</sup>

# CLI

为运行中的 MiroShark 后端提供一个依赖极少的 HTTP 客户端。

## 安装

```bash
# From a checkout with the backend installed:
pip install -e backend/
miroshark-cli ask "Will the EU AI Act survive trilogue?"

# Or run directly — no install, no third-party deps:
python backend/cli.py --help
```

设置 `MIROSHARK_API_URL` 即可指向远程部署。

## 命令

| 命令 | 作用 |
|---|---|
| `ask "<question>"` | 从一个问题合成种子简报 |
| `list` | 列出模拟 / 项目 |
| `status <sim_id>` | runner 状态 + 当前轮次/总数 |
| `frame <sim_id> <round>` | 单轮的紧凑快照 |
| `publish <sim_id> [--unpublish]` | 切换嵌入公开标志 |
| `report <sim_id>` | 渲染分析报告 |
| `trending` | 拉取 RSS/Atom 热门条目 |
| `health` | Ping `/health` |

所有命令都接受 `--json` 以便脚本化使用。


# FILE: docs/API.md

# HTTP API Reference

<sup>English · [中文](API.zh-CN.md)</sup>

Base URL is `http://localhost:5001` in dev. Every endpoint returns JSON unless otherwise noted.

> **Interactive docs:** the running backend serves Swagger UI at `/api/docs` and the OpenAPI 3.1 spec at `/api/openapi.yaml` (or `/api/openapi.json`). Point [`openapi-generator`](https://openapi-generator.tech/) at the spec to produce a Python / TypeScript / Go SDK in one command.

## Setup & Discovery

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/simulation/suggest-scenarios` | Scenario auto-suggest (Bull / Bear / Neutral) from a document preview |
| `GET` | `/api/simulation/trending` | Pull RSS/Atom items for the "What's Trending" panel |
| `POST` | `/api/simulation/ask` | Just Ask — synthesize a seed briefing from a question |
| `POST` | `/api/graph/fetch-url` | Fetch + extract text from a URL |
| `GET` | `/api/templates/list` | Preset templates |
| `GET` | `/api/templates/<id>?enrich=true` | Template + live FeedOracle enrichment |

## Graph Build (Step 1)

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/graph/ontology/generate` | NER + ontology extraction |
| `POST` | `/api/graph/build` | Build Neo4j graph from ontology |
| `GET` | `/api/graph/task/<task_id>` | Poll async task status |
| `GET` | `/api/graph/data/<graph_id>` | Paginated graph nodes + edges |
| `GET` | `/api/simulation/entities/<graph_id>` | Browse entities |
| `GET` | `/api/simulation/entities/<graph_id>/<uuid>` | Single entity + neighborhood |

## Simulation Lifecycle

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/simulation/create` | Create simulation from seed + prompt |
| `POST` | `/api/simulation/prepare` | Kick off profile generation (Step 2) |
| `POST` | `/api/simulation/prepare/status` | Poll Step 2 |
| `POST` | `/api/simulation/start` | Launch Wonderwall subprocess (Step 3) |
| `POST` | `/api/simulation/stop` | Terminate |
| `POST` | `/api/simulation/branch-counterfactual` | Fork with counterfactual injection |
| `POST` | `/api/simulation/fork` | Duplicate config |
| `POST` | `/api/simulation/<id>/director/inject` | Director mode — live event injection |
| `GET` | `/api/simulation/<id>/director/events` | List director events |

## Live State & Data

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/simulation/<id>/run-status` | Current round / totals |
| `GET` | `/api/simulation/<id>/run-status/detail` | Per-platform progress |
| `GET` | `/api/simulation/<id>/frame/<round>` | Compact per-round snapshot |
| `GET` | `/api/simulation/<id>/timeline` | Round-by-round summary |
| `GET` | `/api/simulation/<id>/actions` | Raw agent action log |
| `GET` | `/api/simulation/<id>/posts` | Paginated posts (Twitter + Reddit) |
| `GET` | `/api/simulation/<id>/profiles` | Agent personas |
| `GET` | `/api/simulation/<id>/profiles/realtime` | Live belief updates |
| `GET` | `/api/simulation/<id>/polymarket/markets` | Markets + current prices |
| `GET` | `/api/simulation/<id>/polymarket/market/<mid>/prices` | Price history |

## Analytics

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/api/simulation/<id>/belief-drift` | Stance drift per topic per round |
| `GET` | `/api/simulation/<id>/counterfactual` | Original vs branch comparison |
| `GET` | `/api/simulation/<id>/agent-stats` | Per-agent engagement + posting |
| `GET` | `/api/simulation/<id>/influence` | Influence leaderboard |
| `GET` | `/api/simulation/<id>/interaction-network` | Agent-to-agent graph |
| `GET` | `/api/simulation/<id>/demographics` | Archetype distribution |
| `GET` | `/api/simulation/<id>/quality` | Run health diagnostics |
| `POST` | `/api/simulation/compare` | Side-by-side belief comparison |

## Interaction

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/simulation/interview` | Chat with one agent |
| `POST` | `/api/simulation/interview/batch` | Ask a group in parallel |
| `POST` | `/api/simulation/<id>/agents/<name>/trace-interview` | Chat with full reasoning trace |
| `GET` | `/api/simulation/<id>/interviews/<name>` | Past transcripts with an agent |

## Publish / Embed / Export

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/simulation/<id>/publish` | Toggle `is_public` |
| `GET` | `/api/simulation/<id>/embed-summary` | Embed payload (public sims only) |
| `GET` | `/api/simulation/<id>/share-card.png` | 1200×630 OG image (auto-unfurls) |
| `GET` | `/api/simulation/<id>/replay.gif` | Animated belief-bar replay |
| `GET` | `/api/simulation/<id>/transcript.md` | Markdown transcript (Notion / Obsidian / Substack) |
| `GET` | `/api/simulation/<id>/transcript.json` | Structured JSON transcript (SDKs / LLM-as-judge) |
| `GET` | `/api/simulation/<id>/trajectory.csv` | Per-round belief CSV (`pandas.read_csv()` / Excel / Tableau / R) |
| `GET` | `/api/simulation/<id>/trajectory.jsonl` | Per-round belief JSONL (DuckDB / pipelines) |
| `GET` | `/api/simulation/<id>/thread.txt` | Auto-formatted X / Twitter tweet thread (one tweet per belief inflection point, ≤280 chars each) |
| `GET` | `/api/simulation/<id>/thread.json` | Same tweet thread as `thread.txt` but as `{tweets, total, inflections_recorded, truncated}` for programmatic consumers |
| `GET` | `/api/simulation/<id>/surface-stats` | Per-share-surface request counters — share card / replay GIF / transcript / trajectory / thread / watch page / Atom / RSS / reproduce.json / lineage / notebook.ipynb, plus a synthetic `total` |
| `GET` | `/api/simulation/<id>/reproduce.json` | Citation primitive — v1-schema reproducibility config blob carrying scenario, agent count, total rounds, platform toggles, time-config knobs, director events, and fork / counterfactual lineage. Identical exports of a finished sim are bytewise-identical (citation-hash friendly) |
| `GET` | `/api/simulation/<id>/notebook.ipynb` | Pre-populated Jupyter notebook — trajectory CSV embedded directly + belief-evolution / final-consensus / quality-summary cells scaffolded. Runs air-gapped (no network call back req

# FILE: docs/ARCHITECTURE.zh-CN.md

<sup>[English](ARCHITECTURE.md) · 中文</sup>

# 架构

## 流水线总览

1. **图谱构建** — 把你文档中的实体和关系抽取到一个 Neo4j 知识图谱里。NER 使用少样本示例和拒绝规则来过滤垃圾实体。分块处理通过批量 Neo4j 写入(UNWIND)做了并行。

2. **智能体配置** — 基于知识图谱生成人设。每个实体获得 5 层上下文:图谱属性、关系、语义检索、相邻节点,以及 LLM 驱动的网络调研(在涉及公众人物或图谱上下文不足时自动触发)。个体 vs 机构人设通过关键词匹配自动检测。

3. **模拟** — 三个平台(Twitter、Reddit、Polymarket)通过 `asyncio.gather` 同时运行。一个由 LLM 生成、初始价格非 50/50 的预测市场驱动 Polymarket 交易。智能体能看到跨平台上下文:交易者读 Twitter/Reddit 帖子,社交媒体智能体能看到市场价格。一个滑动窗口式的轮次记忆通过后台 LLM 调用压缩旧轮次。信念状态记录每个智能体的立场、置信度和信任度,每轮都用启发式更新。

4. **报告** — 一个 ReACT 智能体使用 `simulation_feed`(真实的帖子/评论/交易)、`market_state`(价格/盈亏)、图谱搜索、信念轨迹、纳什均衡等工具来撰写分析报告。报告会引用智能体真实的发言和市场实际的走势。

5. **交互** — 通过人设对话直接和任意智能体聊天,向群组提问,或者在任意轮次给模拟分叉一个反事实事件,以并排对比"如果"情景。点击任意智能体可以查看其完整画像和模拟历史。

## 跨平台模拟引擎

每一轮三个平台同时执行。数据在它们之间流动:

```
                    ┌─────────────────────────────────────────┐
                    │         Round Memory (sliding window)    │
                    │  Old rounds: LLM-compacted summaries     │
                    │  Previous round: full action detail       │
                    │  Current round: live (partial)            │
                    └──────┬──────────┬──────────┬────────────┘
                           │          │          │
                    ┌──────▼───┐ ┌────▼─────┐ ┌─▼────────────┐
                    │ Twitter  │ │  Reddit  │ │  Polymarket   │
                    │          │ │          │ │               │
                    │ Posts    │ │ Comments │ │ Trades (AMM)  │
                    │ Likes    │ │ Upvotes  │ │ Single market │
                    │ Reposts  │ │ Threads  │ │ Buy/Sell/Wait │
                    └──────┬───┘ └────┬─────┘ └─┬────────────┘
                           │          │          │
                    ┌──────▼──────────▼──────────▼────────────┐
                    │         Market-Media Bridge              │
                    │  Social sentiment → trader prompts       │
                    │  Market prices → social media prompts    │
                    │  Social posts → trader observation       │
                    └──────┬──────────┬──────────┬────────────┘
                           │          │          │
                    ┌──────▼──────────▼──────────▼────────────┐
                    │         Belief State (per agent)         │
                    │  Positions: topic → stance (-1 to +1)    │
                    │  Confidence: topic → certainty (0 to 1)  │
                    │  Trust: agent → trust level (0 to 1)     │
                    └─────────────────────────────────────────┘
```

## Polymarket 集成

模拟配置创建期间,LLM 会生成单个预测市场,围绕该模拟的核心问题量身定制。市场标题生成走 **Smart** 槽位(见 [Models](MODELS.zh-CN.md)),让措辞精准、有时间界限、可结算 — 这是定义整场模拟的提示词,值得用更强的模型。AMM 使用恒定乘积定价,初始价格依据 LLM 的概率估计而非 50/50。交易者在他们的观察提示里能看到 Twitter/Reddit 上真实的帖子,以及自己的投资组合和市场数据。

## 性能

| 优化项 | 优化前 | 优化后 |
|---|---|---|
| Neo4j 写入 | 每个实体一个事务 | 批量 UNWIND(快 10 倍) |
| 分块处理 | 顺序 | 并行 ThreadPoolExecutor(快 3 倍) |
| 配置生成 | 顺序批量 | 并行批量(快 3 倍) |
| 平台执行 | Twitter+Reddit 并行,Polymarket 顺序 | 三者全并行 |
| 记忆压缩 | 阻塞 | 后台线程 |

## Web 增强

在为公众人物(政治家、CEO、创始人)生成画像时,或当图谱上下文太薄(<150 字符)时,系统会发起一次 LLM 调研调用,用真实世界数据丰富画像。在 `.env` 中设置 `WEB_SEARCH_MODEL=perplexity/sonar-pro`,通过 OpenRouter 进行接地的网络搜索。

## 单轮帧 API

`GET /api/simulation/<id>/frame/<round>` 返回某一轮的紧凑快照 — 动作、活跃智能体计数、当轮市场价格和信念状态 — 适合大型模拟的 scrub UI。这是不必通过 `/run-status/detail` 一次性加载全部 N × M 动作的替代方案。查询参数:`platforms=twitter,reddit,polymarket`、`include_belief`、`include_market`。被 **ReplayView** 用于时间轴拖动,也被 CLI(`miroshark-cli frame <id> <round>`)使用。

## 记忆与检索流水线

除了模拟引擎,MiroShark 还自带一个研究级的图谱记忆栈,灵感来自 Hindsight、Graphiti、Letta 和 HippoRAG。每个被摄入的文档和模拟动作都流过下面的过程:

### 摄入

```
text → NER (with ontology)
     → batch embed (OpenRouter text-embedding-3-large or local Ollama)
     → Entity resolution (fuzzy + vector + LLM reflection — dedups "NeuralCoin"/"Neural Coin"/"NC")
     → MERGE entities into Neo4j with canonical UUIDs
     → Contradiction detection (LLM adjudicates same-endpoint pairs → invalidate old)
     → CREATE RELATION edges with {valid_at, invalid_at, kind, source_type, source_id}
```

### 检索(`storage.search(...)`)

```
query
  ├─ vector edge search (Neo4j HNSW)   ─┐
  ├─ BM25 edge search (Neo4j fulltext) ─┼─ temporal + kind filters → fused candidates (top 30)
  └─ BFS traversal from seed entities  ─┘
                                        ↓
                           BGE-reranker-v2-m3 cross-encoder (Apple MPS / CUDA / CPU)
                                        ↓
                         top `limit` with _sources tag ("v" / "k" / "g" / combos)
```

### 缩放层(`storage.build_communities(...)`)

- 在实体图上做 Leiden 社区检测(通过 igraph)
- 每个簇由 LLM 生成标题 + 2 句话摘要
- 持久化为带有 `MEMBER_OF` 边的 `:Community` 节点
- 通过 `browse_clusters` 智能体工具对簇摘要做语义检索

### 推理记忆

每次报告生成都会把完整的 ReACT 轨迹持久化为可遍历子图:

```
(:Report)-[:HAS_SECTION]->(:ReportSection)-[:HAS_STEP]->(:ReasoningStep)
```

步骤类别有 `thought | tool_call | observation | conclusion`。可以用 `storage.get_reasoning_trace(section_uuid)` 查询历史报告的推理过程。

### 这些能给你什么

- 多跳查询能用上(图遍历能抓到只有连接关系匹配的事实)
- 时间维度查询能用上(`as_of="2026-04-10T14:00Z"` 返回那一刻所知的世界)
- 认识论过滤(`kinds=["belief"]` 只返回智能体观点,不返回事实)
- 报告可以被反复查询("为什么这个智能体得出 X 结论?")
- 首次召回足够高,所以报告智能体那 5 次工具调用预算能用得更远

11 个特性默认全部开启,都可以通过 `.env` 开关单独关闭 — 见 [Configuration](CONFIGURATION.zh-CN.md#特性开关汇总)。


# FILE: docs/WEBHOOKS.zh-CN.md

<sup>[English](WEBHOOKS.md) · 中文</sup>

# Webhook

MiroShark 会在某次模拟到达终态(`completed` 或 `failed`)的瞬间,向你指定的 URL 发起一次出站 HTTP **POST**。载荷包含情景、最终共识、质量评估,以及一个公开的分享卡 URL — 这样 Slack 和 Discord 等消费方能自动展开成富预览。

> **提示:** 打开 MiroShark → **设置 → Integrations · Webhook**,即可在不离开应用的情况下粘贴你的 URL 并触发一次测试事件。同一个 URL 也会被 runner 在真实运行时读取。

---

## 为什么要有 webhook

完成回调 webhook 是 MiroShark 之外一切外部世界的集成面:

- **Slack / Discord / Teams** — 粘贴一个 Incoming Webhook URL;每次长时间模拟一结束,聊天频道就会亮起来,并自带分享卡片图。
- **Zapier / Make / n8n / IFTTT** — 把 Zap/Scenario/Workflow 指向 MiroShark,然后从那里发散开:邮件摘要、Notion 行、Airtable 记录、Google 表格更新、自定义仪表板。
- **自定义应用** — 你自己的 Cloud Run / Lambda / Express 端点收到 JSON;之后随便你怎么处理(启动下游分析、追加到队列、写 BigQuery 等)。

无 bot、无 OAuth、无托管基础设施。只要一个 URL 字段。

---

## 配置

要么在启动 MiroShark 之前设置环境变量:

```bash
WEBHOOK_URL=https://hooks.slack.com/services/T0XXX/B0YYY/abcSECRETxyz
PUBLIC_BASE_URL=https://miroshark.app           # optional, see below
WEBHOOK_SECRET=                                  # optional,见下方「验证 webhook 签名」
```

……要么打开 **设置 → Integrations · Webhook** 在那里粘贴 URL。设置改动会在运行时生效 — 无需重启。

`PUBLIC_BASE_URL` 是你 MiroShark 部署对外公开可达的根地址(例如 `https://miroshark.app`)。设置之后,载荷会包含绝对路径的 `share_url` 与 `share_card_url` 字段,让 Slack / Discord 自动展开模拟卡片。如果你只需要相对路径并且消费方能自己拼绝对 URL,留空即可。

`WEBHOOK_SECRET` 是用于对每次出站载荷做 HMAC 签名的共享密钥 — 详见下文[验证 webhook 签名](#验证-webhook-签名)。留空可跳过签名(已有集成无需任何改动即可继续工作)。用 `python -c 'import secrets; print(secrets.token_hex(32))'` 生成一个新的随机值,并把它同时设置到 MiroShark 的 `.env` 和你的消费端环境中。

---

## 载荷结构

```json
{
  "event": "simulation.completed",
  "sim_id": "sim_abc123def456",
  "scenario": "Will the SEC approve a spot Solana ETF before Q3 2026?",
  "status": "completed",
  "current_round": 20,
  "total_rounds": 20,
  "agent_count": 248,
  "quality_health": "Excellent",
  "final_consensus": {
    "bullish": 62.0,
    "neutral": 13.0,
    "bearish": 25.0
  },
  "resolution_outcome": "YES",
  "share_path": "/share/sim_abc123def456",
  "share_card_path": "/api/simulation/sim_abc123def456/share-card.png",
  "share_url": "https://miroshark.app/share/sim_abc123def456",
  "share_card_url": "https://miroshark.app/api/simulation/sim_abc123def456/share-card.png",
  "created_at": "2026-04-26T10:12:34",
  "completed_at": "2026-04-26T10:35:11",
  "parent_simulation_id": null,
  "fired_at": "2026-04-26T10:35:11.842113+00:00"
}
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `event` | string | `simulation.completed`、`simulation.failed` 或 `simulation.test` |
| `sim_id` | string | 稳定标识符 — 同时也在 `X-MiroShark-Sim-Id` 头部里 |
| `scenario` | string | 截断到 280 字符,带 Unicode 省略号 |
| `status` | string | `completed`、`failed` 或 `test` |
| `current_round` | int | 完成时已结束的最后一轮 |
| `total_rounds` | int | 配置的总轮数 — 未知时为 `0` |
| `agent_count` | int | 智能体画像数量 |
| `quality_health` | string \| null | `Excellent` / `Good` / `Fair` / `Poor`,跳过评估时为 `null` |
| `final_consensus` | object \| null | 最后一份信念快照中的 看涨 / 中立 / 看跌 百分比 |
| `resolution_outcome` | string \| null | 当本次运行有 polymarket 结算时存在(`YES` / `NO`) |
| `share_path` | string | 永远是相对路径;打日志安全 |
| `share_card_path` | string | 永远是相对路径 |
| `share_url` | string \| absent | 仅在设置了 `PUBLIC_BASE_URL` 时存在 |
| `share_card_url` | string \| absent | 仅在设置了 `PUBLIC_BASE_URL` 时存在 |
| `created_at` | string \| null | ISO 8601,模拟创建时间 |
| `completed_at` | string \| null | ISO 8601,达到终态的时间 |
| `parent_simulation_id` | string \| null | 当此次运行是从其他运行分叉而来时存在 |
| `fired_at` | string | 带时区的 ISO 8601,webhook 离开 MiroShark 的时间 |
| `error` | string \| absent | 仅在 `simulation.failed` 上 — 截断到 1000 字符 |
| `test` | bool \| absent | 仅在 `simulation.test` 事件上为 `true` |

### HTTP 头

| 头 | 值 |
|---|---|
| `Content-Type` | `application/json; charset=utf-8` |
| `User-Agent` | `MiroShark-Webhook/1.0` |
| `X-MiroShark-Event` | 与 `event` 相同的值 |
| `X-MiroShark-Sim-Id` | 与 `sim_id` 相同的值 |
| `X-MiroShark-Signature` | 原始 body 的 `sha256=<hex>` HMAC。仅在设置了 `WEBHOOK_SECRET` 时存在。详见[验证 webhook 签名](#验证-webhook-签名)。 |

---

## 投递语义

- **发了就忘** — POST 跑在守护线程上,所以慢的接收端永远不会拖慢模拟 runner。
- **尽力而为,不重试** — 单次尝试,5 秒超时。需要可靠送达的消费方应该把 webhook 接进队列,并尽快用 HTTP 2xx 应答。
- **进程内去重** — runner 会通过两条路径检测完成(进程退出码 + 各平台的 `simulation_end` 事件)。两者都会调进 webhook 服务;每个 `(sim_id, status)` 只有第一次会真的发出。
- **只送 `completed` 与 `failed`** — 暂停 / 恢复 / running 事件*不*下发。
- **2xx 即成功** — 其他都会被记录为投递失败,但永远不会抛出。
- **投递日志** — 每次投递尝试(自动触发*或*手动重发)都会在 `<sim_dir>/webhook-log.jsonl` 追加一行 JSON,包含时间戳、掩码 URL、HTTP 状态码、延迟和触发标签。磁盘上限 50 行;`GET /api/simulation/<id>/webhook-log`(需管理员 token)返回最近 10 条记录(从新到旧)以及全程 `total_attempts` 计数器。
- **手动重试** — `POST /api/simulation/<id>/webhook-retry`(需管理员 token)重发已经处于终止状态的模拟的完成 webhook。原投递偶发 5xx、URL 当时配错、消费集成当时宕机时有用。重发载荷带 `retry: true`,下游消费者可据此对重放去重。重发会绕过自动触发使用的进程内 `(sim_id, status)` 去重门(那道门只防止 runner 的两条终止代码路径自动双发;运维者显式重试理应总能通过)。未配置 webhook URL 时返回 400,模拟尚未到达终止状态时返回 409。

---

## 验证 webhook 签名

当你的 MiroShark 实例配置了 `WEBHOOK_SECRET` 时,每一份出站载荷都会用 HMAC-SHA256 签名,签名通过 `X-MiroShark-Signature` 头部一并送达。签名让消费方能够证明载荷确实来自你的 MiroShark 实例、并且在传输途中没有被伪造 — [Stripe](https://stripe.com/docs/webhooks/signatures) 和 [GitHub](https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries) 用的就是同一套方案。

签名是对**原始请求 body**(不是解析后的 JSON)计算的,所以消费方必须在解析*之前*完成验证 — 重新序列化 JSON 可能改变字段顺序或空白,从而破坏摘要。

**向后兼容。** 当 MiroShark 一侧未设置或留空 `WEBHOOK_SECRET` 时,签名头部会被完全省略,已有的集成无需任何改动即可继续工作。消费方应当把「没有签名头」当作「未配置签名」处理,自行决定是否接受未签名的投递。

生成一个强随机密钥,并在两边设置**相同的值**:

```bash
python -c 'import secrets; print(secrets.token_hex(32))'
# → 64 个十六进制字符;把它粘贴到两端的 WEBHOOK_SECRET
```

### Python(Flask / FastAPI / 纯 WSGI)

```python
import hashlib, hmac, os

WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"].encode()

def verify(raw_body: bytes, header: str) -> bool:
    expected = "sha256=" + hmac.new(WEBHOOK_SECRET, raw_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, header or "")
```

`hmac.compare_digest` 是常数时间比较,所以网络上的攻击者无法通过时序差侧信道试出签名。

### Node.js(Express)

```javascript
const crypto = require('crypto');
const SECRET = process.env.WEBHOOK_SECRET;

function verify(rawBody, header) {
  const expected = 'sha256=' + crypto.createHmac('sh

# FILE: docs/MCP.md

# MCP

<sup>English · [中文](MCP.zh-CN.md)</sup>

MiroShark ships two MCP surfaces: a **standalone MCP server** so you can query your knowledge graphs from Claude Desktop, Cursor, Windsurf, or Continue, and a set of **report agent tools** used internally by the ReACT report agent.

> **Tip:** open MiroShark → **Settings → AI Integration · MCP** for an auto-generated, copy-paste-ready config snippet for each client. The Settings panel reads `GET /api/mcp/status` and stamps the snippet with the absolute paths on your machine.

## What's exposed

`backend/mcp_server.py` runs over **stdio** (no port to open, no daemon to keep alive — your MCP client launches it on demand) and uses your existing `.env` for Neo4j + LLM credentials.

| Tool | What it does |
|---|---|
| `list_graphs` | Survey graphs + entity/edge counts |
| `search_graph` | Full hybrid + rerank pipeline with `kinds` / `as_of` filters |
| `browse_clusters` | Community zoom-out (auto-builds on first call) |
| `search_communities` | Direct semantic search over cluster summaries |
| `get_community` | Expand one cluster with members |
| `list_reports` | Reports generated on a graph |
| `list_report_sections` | Sections of a report |
| `get_reasoning_trace` | Full ReACT decision chain for one section |

**Example prompt:** *"List my MiroShark graphs, browse clusters on the biggest one for anything about oracle exploits, then show me the reasoning trace from the most recent report on that graph."*

---

## Claude Desktop

Open **Claude Desktop → Settings → Developer → Edit Config**. The file lives at:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`
- **Linux:** `~/.config/Claude/claude_desktop_config.json`

Add (or merge into) the `mcpServers` block — replace `/absolute/path/to/MiroShark/backend` with the path on your machine:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

Restart Claude Desktop. The `miroshark` tools appear in the hammer / 🛠️ menu.

> **No `uv`?** Use the Python interpreter directly:
> ```json
> "command": "/absolute/path/to/MiroShark/backend/.venv/bin/python",
> "args": ["/absolute/path/to/MiroShark/backend/mcp_server.py"]
> ```

---

## Cursor

Cursor reads `mcpServers` from either:

- a workspace config: `.cursor/mcp.json` in the repo you're working in, **or**
- a global config: `~/.cursor/mcp.json`

Add:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

Reload the Cursor window (`Cmd/Ctrl+Shift+P → Reload Window`). The miroshark tools appear when you `@mention` MCP in chat.

---

## Windsurf

Windsurf reads MCP servers from `~/.codeium/windsurf/mcp_config.json`:

```json
{
  "mcpServers": {
    "miroshark": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "/absolute/path/to/MiroShark/backend",
        "python",
        "mcp_server.py"
      ]
    }
  }
}
```

Then open **Cascade → MCP Servers → Refresh**. The miroshark tools become callable from Cascade conversations.

---

## Continue (VS Code / JetBrains)

Continue ≥ 0.9.x supports MCP via `~/.continue/config.json`:

```json
{
  "experimental": {
    "modelContextProtocolServers": [
      {
        "transport": {
          "type": "stdio",
          "command": "uv",
          "args": [
            "run",
            "--directory",
            "/absolute/path/to/MiroShark/backend",
            "python",
            "mcp_server.py"
          ]
        }
      }
    ]
  }
}
```

Reload your editor after saving.

---

## Verifying it works

1. Start your MCP client. Within a few seconds it should spawn `mcp_server.py` as a child process.
2. Ask: *"Use the `list_graphs` tool to show my MiroShark graphs."* — the assistant should respond with one row per graph and entity/edge counts. If the response is empty (`No graphs found.`), build at least one graph in the MiroShark UI first (Step 1: Graph Build).
3. The MiroShark UI's **Settings → AI Integration · MCP** panel surfaces the same Neo4j health probe — if the panel says *Neo4j down*, the MCP tools will fail the same way.

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `uv: command not found` in your client's MCP logs | `uv` is not on the PATH the client inherited | Switch to the **No uv?** snippet (direct interpreter path), or install `uv` system-wide. |
| `No graphs found.` from `list_graphs` | Empty Neo4j | Run a simulation in the MiroShark UI to populate at least one graph. |
| `Neo.ClientError.Security.Unauthorized` | Stale `NEO4J_PASSWORD` in `.env` | Update `.env` and restart any client that already spawned the server. |
| Server starts then dies immediately | `mcp` Python package missing | The MCP SDK is in `pyproject.toml` — make sure `uv sync` (or `pip install -e backend/`) ran cleanly. |
| Snippet shows `mcp_script: missing` in the Settings panel | You're running the backend from a different checkout than the one with `mcp_server.py` | Re-clone or `git pull` so `backend/mcp_server.py` exists. |

## Report Agent Tools

The ReACT report agent exposes these tools internally (configured via `REPORT_AGENT_MAX_TOOL_CALLS`):

| Tool | Purpose |
|---|---|
| `insight_forge` | Multi-round deep analysis on a specific question |
| `panorama_search` | Hybrid vector + BM25 + graph retrieval |
| `quick_search` | Lightweight keyword search |
| `interview_agents` | Live conversation with sim agents |
| `analyze_trajectory` | Belief drift — convergence, polarization, turning points |
| `analyze_equilibrium` | Nash equilibria on a 2-player stance game fit to the final belief distribution — reveals whether

# FILE: docs/CONFIGURATION.zh-CN.md

<sup>[English](CONFIGURATION.md) · 中文</sup>

# 配置

所有设置都在 `.env`(从 `.env.example` 拷贝)。下面这份完整参考按关注点分组。模型选择(哪个槽位用哪个模型、基准、Ollama 上下文覆盖)请见 [Models](MODELS.zh-CN.md)。

## 最低必填项

```bash
# LLM
LLM_API_KEY=your-api-key
LLM_BASE_URL=https://openrouter.ai/api/v1     # or http://localhost:11434/v1 for Ollama
LLM_MODEL_NAME=xiaomi/mimo-v2-flash

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=miroshark

# Embeddings
EMBEDDING_PROVIDER=openai                     # or "ollama"
EMBEDDING_MODEL=openai/text-embedding-3-large
EMBEDDING_API_KEY=your-api-key
EMBEDDING_DIMENSIONS=768
```

## 模型槽位

MiroShark 把不同的工作流路由到不同的模型。共有四个相互独立的槽位:

| 槽位 | 环境变量 | 作用 | 调用量 |
|---|---|---|---|
| **Default** | `LLM_MODEL_NAME` | 画像、模拟配置、记忆压缩 | ~75–126 次调用 |
| **Smart** | `SMART_MODEL_NAME` | 报告、本体、图谱推理 | ~19 次调用 |
| **NER** | `NER_MODEL_NAME` | 实体抽取(结构化 JSON) | ~85–250 次调用 |
| **Wonderwall** | `WONDERWALL_MODEL_NAME` | 模拟循环中的智能体决策 | ~850–1650 次调用 |

未设置的槽位会回退到 Default 模型。如果只设置了 `SMART_MODEL_NAME`(没有设 `SMART_PROVIDER`/`SMART_BASE_URL`/`SMART_API_KEY`),smart 模型会继承 default 的提供商设置。`WONDERWALL_MODEL_NAME` 也是同样的逻辑 — 设置 `WONDERWALL_BASE_URL` 和/或 `WONDERWALL_API_KEY` 就能把 Wonderwall 指向另一个 OpenAI 兼容端点(例如自部署的 vLLM/Modal 部署),而不影响其他槽位。

每个槽位经过基准测试的推荐配置见 [Models](MODELS.zh-CN.md)。

## 完整 `.env` 参考

```bash
# ─── LLM (default — profiles, sim config, memory compaction) ───
LLM_PROVIDER=openai                # "openai" (default) or "claude-code"
LLM_API_KEY=ollama
LLM_BASE_URL=http://localhost:11434/v1
LLM_MODEL_NAME=qwen2.5:32b

# ─── Smart model (reports, ontology, graph reasoning — #1 quality lever) ───
# SMART_PROVIDER=openai
# SMART_MODEL_NAME=x-ai/grok-4.1-fast          # Cloud preset

# ─── Wonderwall (agent sim loop — #1 cost driver, use cheapest viable) ───
# WONDERWALL_MODEL_NAME=xiaomi/mimo-v2-flash
# Optional: route Wonderwall to a custom OpenAI-compatible endpoint
# (self-hosted vLLM, Modal, custom fine-tune…). Both fields are
# optional — leaving either blank inherits LLM_BASE_URL / LLM_API_KEY.
# WONDERWALL_BASE_URL=https://your-endpoint.example.com/v1
# WONDERWALL_API_KEY=not-checked

# ─── NER (entity extraction — needs reliable JSON, no hidden CoT) ───
# NER_MODEL_NAME=x-ai/grok-4.1-fast

# ─── Disable chain-of-thought on reasoning-capable OpenRouter models ───
# ~3x lower latency on Qwen3-Flash / Grok-4.1-Fast. Flip to false
# per-deployment if a slot needs CoT.
LLM_DISABLE_REASONING=true

# ─── Claude Code mode (only when LLM_PROVIDER=claude-code) ───
# CLAUDE_CODE_MODEL=claude-sonnet-4-20250514

# ─── Neo4j ───
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=miroshark

# ─── Embeddings ───
EMBEDDING_PROVIDER=ollama          # "ollama" or "openai"
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_BASE_URL=http://localhost:11434
EMBEDDING_DIMENSIONS=768

# ─── Reranker (BGE cross-encoder, ~1GB one-time download) ───
RERANKER_ENABLED=true
RERANKER_MODEL=BAAI/bge-reranker-v2-m3
RERANKER_CANDIDATES=30             # pool size before rerank

# ─── Graph-traversal retrieval (Zep/Graphiti-style BFS from seed entities) ───
GRAPH_SEARCH_ENABLED=true
GRAPH_SEARCH_HOPS=1                # 1 or 2
GRAPH_SEARCH_SEEDS=5               # seed entities per query

# ─── Entity resolution (fuzzy + vector + optional LLM reflection) ───
ENTITY_RESOLUTION_ENABLED=true
ENTITY_RESOLUTION_USE_LLM=true

# ─── Automatic contradiction detection ───
CONTRADICTION_DETECTION_ENABLED=true

# ─── Community clustering (Leiden + LLM summaries) ───
COMMUNITY_MIN_SIZE=3
COMMUNITY_MAX_COUNT=30

# ─── Reasoning trace persistence (:Report subgraph with full ReACT decisions) ───
REASONING_TRACE_ENABLED=true

# ─── Web Enrichment (auto-researches public figures during persona gen) ───
# Also powers the /api/graph/fetch-url URL importer — models without native
# browsing must use an ":online" variant.
WEB_ENRICHMENT_ENABLED=true
# WEB_SEARCH_MODEL=x-ai/grok-4.1-fast:online

# ─── Embedding batching ───
# How many texts per HTTP request. Higher is faster on graph builds;
# drop to 32 if your provider returns 413.
EMBEDDING_BATCH_SIZE=128

# ─── Anthropic prompt caching ───
# Attaches cache_control to the system message when the active model is
# Claude-family. ~10% cost on cache reads; big win on the ReACT report loop.
# Silent no-op for non-Anthropic models.
LLM_PROMPT_CACHING_ENABLED=true

# ─── Live oracle seeds (FeedOracle MCP) ───
# Opt-in grounded data for templates that declare `oracle_tools`.
ORACLE_SEED_ENABLED=false
# FEEDORACLE_MCP_URL=https://mcp.feedoracle.io/mcp
# FEEDORACLE_API_KEY=

# ─── Per-agent MCP tools ───
# Lets personas with `tools_enabled: true` invoke MCP servers during sim.
# Configure servers in config/mcp_servers.yaml.
MCP_AGENT_TOOLS_ENABLED=false
# MCP_SERVERS_CONFIG=./config/mcp_servers.yaml
# MCP_MAX_CALLS_PER_TURN=2
# MCP_CALL_TIMEOUT_SEC=30

# ─── What's Trending (RSS/Atom feeds) ───
# Override the default Reuters/Verge/HN/CoinDesk list.
# TRENDING_FEEDS=https://techcrunch.com/feed/,https://www.theverge.com/rss/index.xml,https://hnrss.org/frontpage,https://www.coindesk.com/arc/outboundfeeds/rss/

# ─── Wonderwall / CAMEL-AI ───
# The simulation engine reads these directly. When LLM_PROVIDER=openai
# they usually match LLM_*. Leave as-is for Ollama.
OPENAI_API_KEY=ollama
OPENAI_API_BASE_URL=http://localhost:11434/v1

# ─── Observability ───
# Full prompt/response logging for debugging.
# (large JSONL files — disable in production)
# MIROSHARK_LOG_PROMPTS=true
# MIROSHARK_LOG_LEVEL=info          # debug|info|warn

# ─── Admin auth (mutation endpoints) ───
# Shared operator secret guarding POST /publish, /resolve, /outcome.
# Send as `Authorization: Bearer <token>`. Compared in constant time.
# UNSET ⇒ those endpoints return 503 (fail-closed). See "Admin auth"
# below for the full story.
# MIROSHARK_ADMIN_TOKEN=
```

## 管理员认证(写操作端点)

有三个端点会写入某个模拟的本地状态,它们都受同一把运维者密钥保护:

- `POST /api/simulation/<id>/publish` — 切换 `is_public`
- `POST /api/simulation/<id>/resolve` — 记录真实结果
- `POST /api/simulation/<id>/outco

# FILE: docs/CLI.md

# CLI

<sup>English · [中文](CLI.zh-CN.md)</sup>

A dependency-light HTTP client for a running MiroShark backend.

## Install

```bash
# From a checkout with the backend installed:
pip install -e backend/
miroshark-cli ask "Will the EU AI Act survive trilogue?"

# Or run directly — no install, no third-party deps:
python backend/cli.py --help
```

Set `MIROSHARK_API_URL` to point at a remote deployment.

## Commands

| Command | What it does |
|---|---|
| `ask "<question>"` | Synthesize a seed briefing from a question |
| `list` | List simulations / projects |
| `status <sim_id>` | Runner status + round/total |
| `frame <sim_id> <round>` | Compact per-round snapshot |
| `publish <sim_id> [--unpublish]` | Toggle the embed public flag |
| `report <sim_id>` | Render the analytical report |
| `trending` | Pull RSS/Atom trending items |
| `health` | Ping `/health` |

All commands accept `--json` for scripting.


# FILE: docs/FEATURES.zh-CN.md

<sup>[English](FEATURES.md) · 中文</sup>

# 特性

每个特性的深入介绍。一个特性一个标题,大致按你在一次典型运行中遇到它们的顺序排列。

## 智能配置(情景自动建议)

模拟提示词输入框是上传文档与开始模拟之间唯一的"白纸难题"。智能配置把它移除:你刚把一个 `.md`/`.txt` 文件拖进来或者贴上一个 URL,MiroShark 就会把抽取出来的文本短预览(约 2K 字符)发给已配置的 LLM,大约 2 秒后返回三张预测市场风格的情景卡片 — 一张 **看涨**、一张 **看跌**、一张 **中立** 框架,每张都带一个具体的 YES/NO 问题、一个合理的初始概率区间,以及一句基于文档的简短理由。

点击任一卡片上的 **使用此项 →** 就能填进模拟提示词字段,或者忽略它们自己输入。建议会按文档缓存(预览的 SHA-256),所以离开页面再回来不会再一次调用 LLM。如果 LLM 调用失败或超时,这个面板会静默不显示 — 你输入的情景仍然完全可用。

- **端点:** `POST /api/simulation/suggest-scenarios`

## 热门(自动发现)

智能配置照顾的是带着文档来的用户。"热门"照顾的是另一半 — 想模拟点和 AI、加密、或地缘相关的*某事*,但手头没有具体文章的人。该面板位于 URL 导入框下方,展示一份可配置的公共 RSS/Atom 源中最新的 5 条目(默认:Reuters tech、The Verge、Hacker News、CoinDesk)。

点击任意卡片,MiroShark 会预填 URL 字段、抓取文章,并立刻基于抓取到的文本触发情景自动建议 — 一键就能从白纸到三张情景卡。运维者可以用 `TRENDING_FEEDS` 环境变量(逗号分隔的 URL)覆盖默认订阅列表。服务端缓存保留结果 15 分钟;如果所有源都报错,该面板会静默消失。

- **端点:** `GET /api/simulation/trending`

## 直接提问(纯问题模式)

没有文档,也没有特定文章在脑子里?在主页输入一个问题("欧盟 AI 法案的生物特征条款会在最终三方会谈中存活吗?"),MiroShark 会让 Smart 模型调研这一话题,并合成一段 1500–3000 字符的简报 — 中立、按 上下文 / 关键角色 / 近期事件 / 待解问题 结构组织。该简报作为 `miroshark://ask/...` 的种子文档进入 URL 列表并预填模拟提示词,这样下游流水线(本体 → 图谱 → 画像 → 模拟)按原样跑。每个问题缓存以便快速重跑。

- **端点:** `POST /api/simulation/ask`

## 可分享情景链接

之前的所有分享表面(`/share/<id>`、`/watch/<id>`、回放 GIF、转录、RSS、轨迹 CSV、画廊搜索)都把读者指向一次*已完成的*模拟。可分享情景链接覆盖了另一半 — *尚未运行的*情景。在推文、博客文章或 Discord 消息中放入这样一个 URL,读者就会落在已预填情景的「新建模拟」表单上,只差一键即可启动他们自己的运行,使用完全相同的设置。

该 URL 接受四个可选查询参数,每个都可独立使用:

| 参数 | 作用 | 上限 |
|---|---|---|
| `scenario` | 预填模拟提示词文本框 | 500 字符 |
| `url` | 自动抓取到 URL 导入列表(必须以 `http://` 或 `https://` 开头) | 2000 字符 |
| `ask` | 预填「直接提问」问题字段 — *不会*自动运行(避免意外的 LLM 费用) | 300 字符 |
| `template` | 自动启动指定的预设模板(完全跳过主页) | 仅限 slug |

任意组合都可以使用。`?scenario=模拟稳定币脱锚&url=https://example.com/incident-report` 会同时预填提示词*并且*在同一流程中抓取该文章。`?template=corporate_crisis` 直接跳到模板启动路径。当预填发生时,控制台上方会出现一条可关闭的橙色边线提示横幅,这样操作者在按下「启动」之前就知道表单是由分享链接填入的。

输入在读取时会经过净化 — HTML / `javascript:` URI / 控制字符会被剥除,长度上限避免兆字节级的载荷,`url=` 必须以 `http://` 或 `https://` 起头才会被接受。一旦表单填好,URL 参数会通过 `router.replace` 被剥除,这样刷新页面不会重放预填,从地址栏复制时反映的是用户编辑后的状态,而不是最初的分享链接。

反向方向住在两个地方。在主页,模拟提示词文本框下方有一个低调的 **🔗 分享为链接** 按钮 — 它会基于当前表单状态构造一个 `?scenario=...&url=...&ask=...` URL 并复制到剪贴板,是 `/watch` 与 `/share` 页面上 **派生此情景** 按钮的「未运行情景」对应版本。每张预设模板卡片上,启动按钮旁还有一个小 **🔗** 图标,点击即可复制一个 `?template=<slug>` URL — Aaron 的「试试这个模拟」推文也能拥有一键 CTA,直接把读者送入对应模板的启动流程。

纯前端实现;无后端改动。净化逻辑住在 `frontend/src/utils/urlParams.js` 中(由 DOMPurify 兜底),`/` 上的读取路径与主页 + 模板画廊上的写入路径都复用同一份。

## 反事实分支

跑完一次模拟,暂停查看,然后问:"如果 CEO 在第 24 轮辞职会怎样?" — 在模拟工作区点击 **⤷ 分支**,输入触发轮次和一段突发新闻注入,MiroShark 就会把模拟分叉一份,带着父级的全部智能体人群。当 runner 到达触发轮次时,该注入会被提升为一次导演事件,并以 BREAKING 区块的形式预置到每个智能体的观察提示词。可以用现有的 **对比** 视图把分支与原始版本并排比较。

预设模板可以声明 `counterfactual_branches`(例如 `ceo_resigns`、`class_action`、`rug_pull`、`sec_notice`),这样分支对话框会提供一键情景。

- **端点:** `POST /api/simulation/branch-counterfactual`

## 导演模式(实时事件注入)

分支会分叉出新的时间线;导演模式则编辑*当前*这一条。模拟运行期间,可以注入一条突发新闻事件,会落到每个智能体下一次观察提示词中 — 不分叉、不重启。适合在不消耗一次完整分支的算力下,对一个情景做压力测试("竞争对手开源了他们的模型"、"SEC 刚刚立案调查")。

每次模拟最多 10 条事件,每条最多 500 字符。UI 控件就在 run-status 头部旁边。事件随模拟状态一同持久化,并在单轮帧 API 中回放,所以它们也会出现在导出和嵌入中。

- **端点:** `POST /api/simulation/<id>/director/inject`、`GET /api/simulation/<id>/director/events`

## 预设模板

`backend/app/preset_templates/` 中自带六个经过基准的情景模板 — 一键起步点,会预填种子文档、模拟提示词、智能体组成,以及(可选的)`counterfactual_branches` 与 `oracle_tools`:

| 模板 | 这次运行的形态 |
|---|---|
| `crypto_launch` | 代币 / 协议发布 — 分析师、散户、KOL、交易者对 TGE 的反应 |
| `corporate_crisis` | 企业事件(数据泄露、产品故障、高管丑闻),媒体 + 市场参与 |
| `political_debate` | 政策 / 选举议题,意识形态光谱与媒体回路 |
| `product_announcement` | 主题演讲 / 功能发布 — 评测周期、开发者反馈、消费者上手 |
| `campus_controversy` | 学生 / 教职 / 行政围绕一起争议事件的互动 |
| `historical_whatif` | 反事实历史 — "如果事件 X 没有发生会怎样?" |

可以在配置页面的 **Templates** 画廊中浏览,或者调用 `GET /api/templates/list`。用 `GET /api/templates/<id>` 获取单个模板;附加 `?enrich=true` 会在返回前对所有声明的 `oracle_tools` 实时求值 FeedOracle。

## 实时 Oracle 数据(FeedOracle MCP)

可选启用 [FeedOracle MCP server](https://mcp.feedoracle.io/mcp) 提供的接地种子数据(484 个工具,覆盖 MiCA 合规、DORA 评估、宏观/FRED 数据、DEX 流动性、制裁、碳市场等)。模板声明它们想用的工具:

```json
"oracle_tools": [
  {"server": "feedoracle_core", "tool": "peg_deviation", "args": {"token_symbol": "USDT"}},
  {"server": "feedoracle_core", "tool": "macro_risk",    "args": {}}
]
```

把 `.env` 里的 `ORACLE_SEED_ENABLED=true`,在任意模板卡上勾选 **使用实时 oracle 数据**,MiroShark 就会派发这些调用,并在摄入前把结果以一个 markdown "Oracle Evidence" 区块附加到种子文档。禁用或调用失败时静默 no-op — 静态种子仍然能用。

## 单智能体 MCP 工具

可选启用,OpenMiro 风格:挑选出来的人设(记者、分析师、交易者)可以在模拟期间调用真实的 MCP 工具。在人设的 profile JSON 中标记 `"tools_enabled": true`,在 `config/mcp_servers.yaml` 配置服务器,并设置 `MCP_AGENT_TOOLS_ENABLED=true`。

每一轮 runner 会:

1. **注入**工具目录到智能体的系统消息(用标记分隔,这样每轮会刷新)。
2. **解析**智能体帖子里类似 `<mcp_call server="web_search" tool="search" args='{"q":"..."}' />` 的自闭合标签(每回合最多 2 次调用)。
3. 通过每个 server 一个的池化 stdio 子进程**派发**它们(每次模拟一个进程,反复复用)。
4. **把结果注入**回智能体的下一轮系统消息。

调用失败会变成 `{"_error": "..."}` 形式的 payload,而不是抛异常 — 智能体提示词保持良好结构。这座桥每次调用有 30 秒的超时(`MCP_CALL_TIMEOUT_SEC`),并在模拟结束时(或异常退出时通过 `atexit`)拆掉子进程。

## 自定义 Wonderwall 端点

模拟循环是 MiroShark 中最重的模型消费者 — 每次运行 850–1650 次调用,7M+ tokens,全部走 CAMEL-AI 单智能体动作循环。Wonderwall 槽位有自己独立的 `WONDERWALL_BASE_URL` + `WONDERWALL_API_KEY` 环境变量(以及 **设置 → 高级 → Wonderwall** 中对应的输入),所以你可以把这些高频调用路由到任意 OpenAI 兼容端点,而不用动 Default/Smart/NER 槽位 — 把图谱构建、报告和实体抽取留在 OpenRouter/Anthropic,智能体那边则可以指向自部署的 vLLM、Modal/Replicate 部署、另一块 GPU 上的 Ollama 实例,或者你自己训的微调。

两个字段都可以独立省略。`WONDERWALL_BASE_URL` 留空就继承 `LLM_BASE_URL`;`WONDERWALL_API_KEY` 留空就继承 `LLM_API_KEY`。开放式端点(无鉴权)只要传一个非空占位符例如 `not-checked` 即可。

```bash
WONDERWALL_BASE_URL=https://your-endpoint.example.com/v1
WONDERWALL_API_KEY=not-checked
WONDERWALL_MODEL_NAME=your-model-id
```

接线在三个地方:(1) `backend/scripts/run_parallel_simulation.py`(以及 twitter / reddit 变体)在子进程启动读取环境时,会优先选 `WONDERWALL_*` 而非 `LLM_*`。(2) `backend/app/services/simulation_runner.py` 在 spawn 子进程时把 `Config.WONDERWALL_*` 转发到子进程 `env`,所以设置 UI 的更新无需重启 Flask 就能在下一次运行生效。(3) Settings API(`POST /api/settings`)以及 `SettingsPanel.vue` 中对应的部分接受这三个字段。

适用场景:
- Wonderwall 角色/人设提示词在你自己训过的微调上效果更好。
- 你想把成本绑定到一台固定费率的自部署 GPU,而不是按 token 计费。
- 你想通过保持除 Wonderwall 之外所有槽位不变的两次匹配模拟,来对比一个自定义小模型的信念漂移 / 连贯

# FILE: docs/WEBHOOKS.md

# Webhooks

<sup>English · [中文](WEBHOOKS.zh-CN.md)</sup>

MiroShark fires an outbound HTTP **POST** to a URL of your choosing the moment a simulation reaches a terminal state — `completed` or `failed`. The payload includes the scenario, final consensus, quality assessment, and a public share-card URL so consumers like Slack and Discord auto-unfurl with a rich preview.

> **Tip:** open MiroShark → **Settings → Integrations · Webhook** to paste your URL and fire a test event without leaving the app. The same URL is read by the runner for live runs.

---

## Why a webhook

The completion webhook is the integration surface for everything that lives outside MiroShark itself:

- **Slack / Discord / Teams** — paste an Incoming Webhook URL; chat channels light up the moment a long simulation finishes, with the share-card image inline.
- **Zapier / Make / n8n / IFTTT** — point the Zap/Scenario/Workflow at MiroShark and fan out from there: email digests, Notion rows, Airtable records, Google Sheet updates, custom dashboards.
- **Custom apps** — your own Cloud Run / Lambda / Express endpoint receives the JSON; do whatever you like with it (kick off downstream analysis, append to a queue, write to BigQuery, …).

No bot, no OAuth, no hosted infrastructure. One URL field.

---

## Configuration

Either set environment variables before launching MiroShark:

```bash
WEBHOOK_URL=https://hooks.slack.com/services/T0XXX/B0YYY/abcSECRETxyz
PUBLIC_BASE_URL=https://miroshark.app           # optional, see below
WEBHOOK_SECRET=                                  # optional, see "Verifying webhook signatures" below
```

…or open **Settings → Integrations · Webhook** and paste the URL there. Settings changes apply at runtime — no restart.

`PUBLIC_BASE_URL` is the publicly-reachable base of your MiroShark deployment (e.g. `https://miroshark.app`). When set, the payload contains absolute `share_url` and `share_card_url` fields so Slack / Discord auto-unfurl with the simulation card. Leave it blank if you only need relative paths and your consumer can build absolute URLs itself.

`WEBHOOK_SECRET` is the shared secret used to HMAC-sign every dispatched payload — see [Verifying webhook signatures](#verifying-webhook-signatures) below. Leave it blank to skip signing (existing integrations continue working unchanged). Generate a fresh value with `python -c 'import secrets; print(secrets.token_hex(32))'` and paste it into both the MiroShark `.env` and your consumer's environment.

---

## Payload schema

```json
{
  "event": "simulation.completed",
  "sim_id": "sim_abc123def456",
  "scenario": "Will the SEC approve a spot Solana ETF before Q3 2026?",
  "status": "completed",
  "current_round": 20,
  "total_rounds": 20,
  "agent_count": 248,
  "quality_health": "Excellent",
  "final_consensus": {
    "bullish": 62.0,
    "neutral": 13.0,
    "bearish": 25.0
  },
  "resolution_outcome": "YES",
  "share_path": "/share/sim_abc123def456",
  "share_card_path": "/api/simulation/sim_abc123def456/share-card.png",
  "share_url": "https://miroshark.app/share/sim_abc123def456",
  "share_card_url": "https://miroshark.app/api/simulation/sim_abc123def456/share-card.png",
  "created_at": "2026-04-26T10:12:34",
  "completed_at": "2026-04-26T10:35:11",
  "parent_simulation_id": null,
  "fired_at": "2026-04-26T10:35:11.842113+00:00"
}
```

| Field | Type | Notes |
|---|---|---|
| `event` | string | `simulation.completed`, `simulation.failed`, or `simulation.test` |
| `sim_id` | string | Stable identifier — also in the `X-MiroShark-Sim-Id` header |
| `scenario` | string | Truncated to 280 characters with a Unicode ellipsis |
| `status` | string | `completed`, `failed`, or `test` |
| `current_round` | int | Last completed round at completion time |
| `total_rounds` | int | Configured total — `0` if not yet known |
| `agent_count` | int | Number of agent profiles |
| `quality_health` | string \| null | `Excellent` / `Good` / `Fair` / `Poor`, or `null` if assessment skipped |
| `final_consensus` | object \| null | Bullish / neutral / bearish percentages from the last belief snapshot |
| `resolution_outcome` | string \| null | Set when the run had a polymarket resolution (`YES` / `NO`) |
| `share_path` | string | Always relative; safe to log |
| `share_card_path` | string | Always relative |
| `share_url` | string \| absent | Only present when `PUBLIC_BASE_URL` is set |
| `share_card_url` | string \| absent | Only present when `PUBLIC_BASE_URL` is set |
| `created_at` | string \| null | ISO 8601, simulation creation time |
| `completed_at` | string \| null | ISO 8601, terminal-state time |
| `parent_simulation_id` | string \| null | Set when this run was forked from another |
| `fired_at` | string | ISO 8601 with timezone, when the webhook left MiroShark |
| `error` | string \| absent | Only on `simulation.failed` — truncated to 1000 chars |
| `test` | bool \| absent | `true` only on the `simulation.test` event |

### HTTP headers

| Header | Value |
|---|---|
| `Content-Type` | `application/json; charset=utf-8` |
| `User-Agent` | `MiroShark-Webhook/1.0` |
| `X-MiroShark-Event` | The same value as `event` |
| `X-MiroShark-Sim-Id` | The same value as `sim_id` |
| `X-MiroShark-Signature` | `sha256=<hex>` HMAC of the raw body. Present only when `WEBHOOK_SECRET` is set. See [Verifying webhook signatures](#verifying-webhook-signatures). |

---

## Delivery semantics

- **Fire-and-forget** — the POST runs on a daemon thread, so a slow endpoint never delays the simulation runner.
- **Best-effort, no retries** — a single attempt with a 5-second timeout. Consumers that need durability should accept the webhook into a queue and acknowledge with HTTP 2xx as fast as possible.
- **Deduped per process** — the runner can detect completion via two paths (process exit code + per-platform `simulation_end` events). Both call into the webhook service; only the first fire per `(sim_id, status)` actually sends.
- **`completed` and `failed` only** — pause / resume / ru

# FILE: docs/INSTALL.md

# Install

<sup>English · [中文](INSTALL.zh-CN.md)</sup>

Pick one of the paths below.

| Path | GPU? | Best for |
|---|---|---|
| [Railway / Render](#one-click-cloud) | No | Fastest path to a live deployment |
| [`./miroshark` (OpenRouter)](#quick-start-miroshark-launcher) | Optional | Local dev, lowest friction |
| [Cloud API — OpenRouter](#option-a1-openrouter) | No | One key covers every slot + embeddings |
| [Cloud API — OpenAI](#option-a2-openai) | No | You already have an OpenAI key |
| [Cloud API — Anthropic](#option-a3-anthropic) | No | You already have an Anthropic key |
| [Docker + Ollama](#option-b-docker--local-ollama) | Yes | Fully self-hosted, one command |
| [Manual + Ollama](#option-c-manual--local-ollama) | Yes | Fully self-hosted, manual control |
| [Claude Code CLI](#option-d-claude-code-no-api-key) | No | Uses your Claude Pro/Max subscription |

## Prerequisites

- An OpenAI-compatible API key (OpenRouter, OpenAI, Anthropic…), Ollama for local inference, **or** Claude Code CLI
- Python 3.11+, Node.js 18+, Neo4j 5.15+

**Installing Neo4j** (the `./miroshark` launcher starts it for you — you only need to install the package):

- **macOS** — `brew install neo4j`
- **Linux** — `sudo apt install neo4j` *(or your distro's equivalent)*
- **Windows** — install [Neo4j Desktop](https://neo4j.com/download/) (GUI — start the DB there, then run the launcher from WSL2 or Git Bash), or run the whole stack inside [WSL2](https://learn.microsoft.com/windows/wsl/install) and follow the Linux steps
- **Zero-install** — create a free [Neo4j Aura](https://neo4j.com/cloud/aura-free/) cloud instance and set `NEO4J_URI` / `NEO4J_PASSWORD` in `.env`

> The `./miroshark` launcher is a bash script — on Windows it needs WSL2 or Git Bash.

Set the password once on macOS/Linux native installs — MiroShark's default is `miroshark` to match `.env.example`:

```bash
neo4j-admin dbms set-initial-password miroshark
```

## Hardware

**Local (Ollama):**

| | Minimum | Recommended |
|---|---|---|
| RAM | 16 GB | 32 GB |
| VRAM | 10 GB | 24 GB |
| Disk | 20 GB | 50 GB |

**Cloud mode:** no GPU needed — just Neo4j and an API key. Any 4 GB RAM machine works.

---

## One-click cloud

Deploy to the cloud in under 3 minutes — no local setup required.

**Before you deploy, create:**

1. A free [Neo4j Aura](https://neo4j.com/cloud/aura-free/) instance — grab the `NEO4J_URI` (starts with `neo4j+s://`) and password.
2. An [OpenRouter](https://openrouter.ai/) API key — used for LLM calls and embeddings.

### Railway (recommended — persistent storage, free trial)

[![Deploy on Railway](https://railway.com/button.svg)](https://railway.app/new/template?template=https://github.com/aaronjmars/MiroShark)

After clicking, set these environment variables in the Railway dashboard:

| Variable | Value |
|---|---|
| `LLM_API_KEY` | Your OpenRouter key (`sk-or-v1-...`) |
| `NEO4J_URI` | Your Aura URI (`neo4j+s://...`) |
| `NEO4J_PASSWORD` | Your Aura password |
| `EMBEDDING_API_KEY` | Same OpenRouter key |
| `OPENAI_API_KEY` | Same OpenRouter key |

### Render (free tier — 750 hrs/month, spins down after 15 min idle)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/aaronjmars/MiroShark)

Render reads `render.yaml` automatically. Set the same env vars above when prompted.

> Cloud deploys use OpenRouter for all LLM calls — Ollama is not available in this mode. Both platforms expose MiroShark on a public HTTPS URL, no port forwarding needed.

---

## Quick start: `./miroshark` launcher

**The recommended path** — one [OpenRouter](https://openrouter.ai/) key and the launcher.

**Prereqs** — Python 3.11+, Node 18+, Neo4j (`brew install neo4j` / `sudo apt install neo4j`), and an OpenRouter key.

```bash
git clone https://github.com/aaronjmars/MiroShark.git && cd MiroShark
cp .env.example .env
```

`.env.example` ships with the Cloud preset (Mimo V2 Flash + Grok-4.1 Fast) as the active default. Open `.env` and paste your OpenRouter key into the five blank `*_API_KEY=` lines (`LLM_`, `SMART_`, `NER_`, `OPENAI_`, `EMBEDDING_` — same key in all of them). No model edits needed unless you want a different lineup.

Then launch:

```bash
./miroshark
```

What the launcher does:

1. Checks Python 3.11+, Node 18+, uv, Neo4j/Docker
2. Starts Neo4j if not already running (Docker or native)
3. Installs frontend + backend deps if missing
4. Kills stale processes on ports 3000/5001
5. Launches Vite dev server (`:3000`) and Flask API (`:5001`)
6. Ctrl+C to stop everything

Open `http://localhost:3000`. First simulation in ~10 min, ~$1. See [Models](MODELS.md) for the full preset breakdown.

> Prefer to run everything local? Skip to [Option B (Docker + Ollama)](#option-b-docker--local-ollama) or [Option C (manual Ollama)](#option-c-manual--local-ollama) below.

---

## Option A: Cloud API (no GPU)

Only Neo4j runs locally. LLM and embeddings use a cloud provider. Three flavours below — pick the one that matches the key you already have.

```bash
# Common prep for all three flavours
brew install neo4j       # macOS  (Linux: sudo apt install neo4j)
cp .env.example .env
```

### Option A.1: OpenRouter

One key covers every slot, including embeddings. Easiest to set up and the path benchmarked in [Models](MODELS.md).

```bash
LLM_API_KEY=sk-or-v1-YOUR_KEY
LLM_BASE_URL=https://openrouter.ai/api/v1
LLM_MODEL_NAME=xiaomi/mimo-v2-flash

SMART_PROVIDER=openai
SMART_API_KEY=sk-or-v1-YOUR_KEY
SMART_BASE_URL=https://openrouter.ai/api/v1
SMART_MODEL_NAME=x-ai/grok-4.1-fast

NER_MODEL_NAME=x-ai/grok-4.1-fast
NER_BASE_URL=https://openrouter.ai/api/v1
NER_API_KEY=sk-or-v1-YOUR_KEY

WONDERWALL_MODEL_NAME=xiaomi/mimo-v2-flash
WEB_SEARCH_MODEL=x-ai/grok-4.1-fast:online

OPENAI_API_KEY=sk-or-v1-YOUR_KEY
OPENAI_API_BASE_URL=https://openrouter.ai/api/v1

EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=openai/text-embedding-3-large
EMBEDDING_BASE_URL=https://openrouter.ai/api
EMBEDDING_API_KEY=sk-or-v
