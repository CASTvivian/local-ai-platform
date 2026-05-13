# Missing Repo Summary Source: howardpen9/hermes-gbrain-bridge

- URL: https://github.com/howardpen9/hermes-gbrain-bridge
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/howardpen9__hermes-gbrain-bridge
- Clone Status: cloned
- Language: TypeScript
- Stars: 30
- Topics: agent-memory, ai-agent, bun, claude-code, codex-cli, developer-tools, gbrain, hermes, knowledge-graph, llm-tools, markdown, mcp, memory-management, openclaw, typescript
- Description: Convert Hermes / OpenClaw agent memory (JSONL sessions, MEMORY.md) to markdown for gBrain ingest

## Extracted README / Docs / Examples



# FILE: README.md

# hermes-gbrain-bridge

> A small, dependency-free bridge that converts scattered agent memory (Hermes, Claude Code, Codex, OpenClaw) into clean markdown for [gBrain](https://github.com/garrytan/gbrain) to ingest.

> 🇹🇼 繁體中文版本：[README.zh-TW.md](README.zh-TW.md)

Most agent tools write memory in their own format — JSONL event streams, flat-key text, SQLite. gBrain only imports markdown. If you want one searchable brain across everything you've ever asked an agent, you need a bridge. This is that bridge.

---

## Why this exists

On one normal developer machine, agent memory lives in at least **five** different places — each in its own format:

| Tool | Location | Format |
|------|----------|--------|
| [Hermes](https://github.com/NousResearch/hermes-agent) | `~/.hermes/sessions/*.jsonl` + `memories/*.md` | JSONL + `§`-delimited markdown |
| Claude Code | `~/.claude/projects/<path-hash>/*.jsonl` | Event stream JSONL |
| Codex CLI | `~/.codex/sessions/**/*.jsonl` | JSONL with `session_meta` header |
| OpenClaw archive | `~/.openclaw.pre-migration/workspace/**/*.md` | Markdown with legacy paths |
| Conductor workspaces | Encoded into the Claude Code path | Same as Claude Code |

gBrain is an excellent knowledge brain, but out of the box it only reads markdown. You don't want to lose the last three years of conversations just because they're in the wrong container. This repo is the converter that makes them ingestible — one command per source, with mtime windows, size floors, secret redaction, and a canonical event format under the hood.

---

## Architecture

```
┌──────────────────────────────────┐       ┌───────────────────────┐
│        Local machine             │       │   Cloud (Railway)     │
│                                  │       │                       │
│  ~/.hermes/sessions/             │       │   Postgres            │
│  ~/.hermes/memories/             │─┐     │   + pgvector          │
│  ~/.claude/projects/             │ │     │   + pg_trgm           │
│  ~/.codex/sessions/              │ │     │                       │
│  ~/.openclaw.pre-migration/      │ │     │   gBrain schema:      │
│                                  │ │     │    pages              │
│  ┌──────────────────────────┐    │ │     │    content_chunks     │
│  │ hermes-gbrain-bridge     │    │ │     │    timeline_entries   │
│  │  discover → filter →     │◀───┘ │     │    ...                │
│  │  adapt → redact →        │      │     │                       │
│  │  canonical event →       │      │     │                       │
│  │  markdown (one per src)  │      │     │                       │
│  └──────────────────────────┘      │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  /tmp/gbrain-staging/*.md          │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  gbrain import → embed ────────────┼────▶│                       │
│  gbrain query / serve ◀────────────┼─────│                       │
└────────────────────────────────────┘     └───────────────────────┘
```

The bridge never touches the database directly. It only produces markdown files. gBrain handles ingestion, chunking, embedding, and storage. This keeps the bridge small and the blast radius tight: if the bridge has a bug, the worst it can do is produce bad markdown in a staging dir — your brain stays safe.

---

## Quickstart

```bash
# 1. Clone and install
git clone https://github.com/howardpen9/hermes-gbrain-bridge
cd hermes-gbrain-bridge
bun install

# 2. See what's out there before committing to anything
bun run src/cli.ts discover --days 30

# 3. Dry-run the source you want to ingest
bun run src/cli.ts export --source=claude-code --dry-run --days 30

# 4. Export for real to a staging directory
bun run src/cli.ts export --source=all --out=/tmp/gbrain-staging --days 30

# 5. Hand it to gBrain
gbrain import /tmp/gbrain-staging --no-embed
gbrain embed --stale    # requires OPENAI_API_KEY
gbrain query "What was the Railway deployment decision for PredictMe?"
```

For the complete walkthrough — provisioning Railway, installing gBrain, setting up keys, connecting the MCP server — see [**docs/SETUP.md**](docs/SETUP.md).

To add an adapter for a new memory source, see [**docs/EXTENDING.md**](docs/EXTENDING.md).

---

## Supported sources

| Source | Path | Status | Notes |
|--------|------|--------|-------|
| Hermes sessions | `~/.hermes/sessions/*.jsonl` | ✅ | One md per session, tool schemas stripped |
| Hermes long-term memory | `~/.hermes/memories/MEMORY.md` | ✅ | Pass-through, `§`-delimited entries |
| Hermes user profile | `~/.hermes/memories/USER.md` | ✅ | Pass-through |
| Claude Code sessions | `~/.claude/projects/**/*.jsonl` | ✅ | `user` / `assistant` turns only; event noise stripped |
| Codex sessions | `~/.codex/sessions/**/*.jsonl` | ✅ | `session_meta` + typed role payloads |
| OpenClaw workspace archive | `~/.openclaw.pre-migration/workspace/**/*.md` | ✅ | Pass-through with mtime + min-size filter |
| OpenClaw memory DBs | `~/.openclaw/memory/*.sqlite` | 🚧 | Requires SQLite reader |
| Gemini CLI history | `~/.gemini/` | 🚧 | Not yet |
| Kimi CLI history | `~/.kimi/` | 🚧 | Not yet |
| Slock agent memory | `~/.slock/agents/*/MEMORY.md` + `notes/` | 🚧 | Not yet |

Want to add one? Read [`docs/EXTENDING.md`](docs/EXTENDING.md) — the adapter interface is ~100 lines of TypeScript.

---

## Case study: one developer's brain, end to end

We ran this bridge on a working developer's machine (Hermes + Claude Code + Codex + OpenClaw archive, 30-day mtime window for the live sources, 1-year window for the archive) and pushed everything into gBrain on Railway Postgres. Real numbers:

| Metric | Value |
|--------|-------|
| Sources enabled | 4 (Hermes, Claude Code, Codex, OpenClaw archive) |
| Raw input — Claude Code jsonl | 1,988 files / 1.4 GB |
| Raw input — Codex jsonl | 636 files / 123 MB |
| Raw input — OpenClaw md (1 year, ≥1 KB) | 1,148 files / 9.6 MB |
| Raw input — Hermes | 4 files / 104 KB |
| **After bridge filter + conversion** | **3,775 markdown docs** |
| Pages in gBrain after dedup | 3,762 |
| Chunks produced | 57,627 |
| Embeddings (text-embedding-3-large) | 57,627 / 57,627 ✅ |
| Total embedding cost | **< $2** |
| Total ingest time (import + embed) | ~55 minutes |
| DB size on Railway | ~400 MB |

The most striking number: Claude Code raw jsonl was **1.4 GB**, but after filtering event-stream noise (`progress`, `queue-operation`, `tool_use` plumbing) and keeping only user/assistant turns, it dropped to **~200 MB** of useful markdown. That filter is the difference between a $50 embedding bill for useless noise and a $2 bill for actual conversation content.

---

## What we learned

Lessons from building this bridge for a real multi-agent setup that saved us weeks of rework and a meaningful chunk of embedding spend. If you're building something similar, read this before you write adapters.

1. **gBrain imports markdown — everything else needs a bridge.** Don't expect gBrain to parse your agent's native format. Every non-markdown source (JSONL, SQLite, event streams, proprietary session formats) needs a converter. Budget for this up front.

2. **"Agent memory" is a discovery problem, not an adapter problem.** On one machine we found agent memory in 5+ scattered locations: global Claude Code, global Codex, Hermes sessions, Conductor workspaces (encoded in the Claude Code path), and a pre-migration archive. Start every bridge project with a `discover` step that reports counts per source. Don't start writing adapters until you know what you're actually up against.

3. **Per-project `.claude/` folders do not contain sessions.** Claude Code always writes session jsonls to `~/.claude/projects/<encoded-path>/` regardless of where you launched it. The per-project `.claude/` folder holds `CLAUDE.md` and `settings.json` only. Don't waste time walking project trees — the path-encoded directory name under the global `projects/` dir **is** the workspace identifier.

4. **Claude Code jsonl is an event stream, and 90% of it is noise.** Event types include `progress`, `queue-operation`, `tool_use`, `tool_result`, `user`, and `assistant`. Only the last two are conversation. Our aggressive filter dropped 1.4 GB of raw jsonl to ~200 MB of useful markdown — the rest was tool plumbing and queue events nobody ever needs to semantically search.

5. **Volume explodes faster than your intuition.** 30 days of normal usage on one machine produced ~2,000 Claude Code sessions and ~600 Codex sessions. Always enforce an mtime window **and** a size floor before running any ingest loop. "Just grab everything" becomes a $50 surprise invoice from OpenAI.

6. **Codex's session format is cleaner than Claude Code's.** Codex has a single `session_meta` event first (with `cwd`, `model`, `id`), then typed `payload.role` events. Claude Code nests content under `message.content` which may be a string, an array of parts, or an array containing `tool_use` / `tool_result` objects you need to unwrap. Write Codex first if you want an easy win; save Claude Code for when you're warmed up.

7. **Pre-migration archives defeat mtime filters.** Our `~/.openclaw.pre-migration/` was 2.1 GB but only 2 files matched a 30-day mtime — because the whole archive is, by definition, old. Historical archives need their own policy: relax mtime to 1 year, enforce a size floor (we used 1 KB), and treat them as cold-storage ingest rather than daily sync.

8. **Embedding cost is tractable — but chunker quality is the real bottleneck.** 57k chunks at `text-embedding-3-large` cost us under $2. That's not the problem. The problem is that default recursive chunking produces broad chunks, so cosine similarity for obvious queries sits around 0.03–0.07. You are paying full price for mediocre r

# FILE: README.zh-TW.md

# hermes-gbrain-bridge

> 一個輕量、零相依的橋接工具，把散落在各個 agent 裡的記憶（Hermes、Claude Code、Codex、OpenClaw）轉成乾淨的 markdown，丟給 [gBrain](https://github.com/garrytan/gbrain) 吸收。

多數 agent 工具都用自己的格式儲存記憶 —— JSONL 事件流、扁平 key 文字檔、SQLite。但 gBrain 只吃 markdown。如果你想把過去問過 agent 的所有事情都整理成一個可搜尋的 brain，就需要一個橋。這個 repo 就是那座橋。

> 🇬🇧 English version: [README.md](README.md)

---

## 為什麼需要這個工具

在一台普通開發機上，agent 記憶至少散落在 **5** 個不同地方，而且每個都用自己的格式：

| 工具 | 位置 | 格式 |
|------|------|------|
| [Hermes](https://github.com/NousResearch/hermes-agent) | `~/.hermes/sessions/*.jsonl` + `memories/*.md` | JSONL + `§` 分隔的 markdown |
| Claude Code | `~/.claude/projects/<path-hash>/*.jsonl` | 事件流 JSONL |
| Codex CLI | `~/.codex/sessions/**/*.jsonl` | 帶 `session_meta` header 的 JSONL |
| OpenClaw archive | `~/.openclaw.pre-migration/workspace/**/*.md` | 帶舊路徑的 markdown |
| Conductor workspaces | 編碼進 Claude Code 的路徑裡 | 同 Claude Code |

gBrain 是個很棒的知識 brain，但預設只能讀 markdown。你不會只因為格式不對，就想放棄過去三年跟 agent 的對話紀錄。這個 repo 就是讓它們能被吸收的轉換器 —— 每個來源一個指令，底層走 mtime 時間窗、大小門檻、機密字串遮罩，全部收斂到同一種 canonical event 格式。

---

## 架構

```
┌──────────────────────────────────┐       ┌───────────────────────┐
│        本機                       │       │   雲端 (Railway)       │
│                                  │       │                       │
│  ~/.hermes/sessions/             │       │   Postgres            │
│  ~/.hermes/memories/             │─┐     │   + pgvector          │
│  ~/.claude/projects/             │ │     │   + pg_trgm           │
│  ~/.codex/sessions/              │ │     │                       │
│  ~/.openclaw.pre-migration/      │ │     │   gBrain schema:      │
│                                  │ │     │    pages              │
│  ┌──────────────────────────┐    │ │     │    content_chunks     │
│  │ hermes-gbrain-bridge     │    │ │     │    timeline_entries   │
│  │  discover → filter →     │◀───┘ │     │    ...                │
│  │  adapt → redact →        │      │     │                       │
│  │  canonical event →       │      │     │                       │
│  │  markdown (一來源一檔)    │      │     │                       │
│  └──────────────────────────┘      │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  /tmp/gbrain-staging/*.md          │     │                       │
│           │                        │     │                       │
│           ▼                        │     │                       │
│  gbrain import → embed ────────────┼────▶│                       │
│  gbrain query / serve ◀────────────┼─────│                       │
└────────────────────────────────────┘     └───────────────────────┘
```

橋本身從不直接動資料庫，只產出 markdown 檔。資料吸收、切 chunk、embedding、寫入資料庫全部由 gBrain 負責。這樣設計讓橋保持小、爆炸半徑極小：就算橋有 bug，最糟也只是在 staging 目錄生出壞掉的 markdown，你的 brain 本身不會被汙染。

---

## Quickstart

```bash
# 1. Clone 並安裝
git clone https://github.com/howardpen9/hermes-gbrain-bridge
cd hermes-gbrain-bridge
bun install

# 2. 先看看本機到底有什麼東西（什麼都不會改）
bun run src/cli.ts discover --days 30

# 3. 用 dry-run 試跑想吸收的來源
bun run src/cli.ts export --source=claude-code --dry-run --days 30

# 4. 正式匯出到 staging 目錄
bun run src/cli.ts export --source=all --out=/tmp/gbrain-staging --days 30

# 5. 交給 gBrain 吸收
gbrain import /tmp/gbrain-staging --no-embed
gbrain embed --stale    # 需要 OPENAI_API_KEY
gbrain query "PredictMe 的 Railway 部署方案當初是怎麼決定的？"
```

完整走查（Railway 開機、安裝 gBrain、金鑰設定、MCP server 串接）請看 [**docs/SETUP.md**](docs/SETUP.md)。

想幫新的記憶來源加 adapter，請看 [**docs/EXTENDING.md**](docs/EXTENDING.md)。

---

## 支援來源

| 來源 | 路徑 | 狀態 | 備註 |
|------|------|------|------|
| Hermes sessions | `~/.hermes/sessions/*.jsonl` | ✅ | 一個 session 一個 md，tool schema 會被剝掉 |
| Hermes 長期記憶 | `~/.hermes/memories/MEMORY.md` | ✅ | 直接轉送，`§` 分隔 |
| Hermes 使用者輪廓 | `~/.hermes/memories/USER.md` | ✅ | 直接轉送 |
| Claude Code sessions | `~/.claude/projects/**/*.jsonl` | ✅ | 只留 `user` / `assistant` turn，事件雜訊濾掉 |
| Codex sessions | `~/.codex/sessions/**/*.jsonl` | ✅ | `session_meta` + typed role payload |
| OpenClaw workspace 封存 | `~/.openclaw.pre-migration/workspace/**/*.md` | ✅ | 直接轉送，帶 mtime + 最小檔案大小過濾 |
| OpenClaw memory DBs | `~/.openclaw/memory/*.sqlite` | 🚧 | 需要 SQLite reader |
| Gemini CLI 歷史 | `~/.gemini/` | 🚧 | 未支援 |
| Kimi CLI 歷史 | `~/.kimi/` | 🚧 | 未支援 |
| Slock agent 記憶 | `~/.slock/agents/*/MEMORY.md` + `notes/` | 🚧 | 未支援 |

想加新來源？看 [`docs/EXTENDING.md`](docs/EXTENDING.md) —— adapter 介面大約 100 行 TypeScript。

---

## 案例研究：一位開發者的腦袋，端到端

我們在一台開發機上實際跑了這個橋（Hermes + Claude Code + Codex + OpenClaw archive，對活躍來源用 30 天 mtime 窗、對封存用 1 年窗），全部丟進 Railway Postgres 上的 gBrain。真實數據：

| 指標 | 數值 |
|------|------|
| 啟用的來源數 | 4（Hermes、Claude Code、Codex、OpenClaw archive） |
| 原始輸入 — Claude Code jsonl | 1,988 個檔 / 1.4 GB |
| 原始輸入 — Codex jsonl | 636 個檔 / 123 MB |
| 原始輸入 — OpenClaw md（1 年、≥1 KB） | 1,148 個檔 / 9.6 MB |
| 原始輸入 — Hermes | 4 個檔 / 104 KB |
| **經過橋接過濾 + 轉換後** | **3,775 份 markdown** |
| 去重後寫入 gBrain 的 page 數 | 3,762 |
| 產生的 chunk 數 | 57,627 |
| Embedding（text-embedding-3-large） | 57,627 / 57,627 ✅ |
| Embedding 總花費 | **< $2** |
| 總吸收時間（import + embed） | 約 55 分鐘 |
| Railway DB 大小 | 約 400 MB |

最驚人的數字：Claude Code 原始 jsonl 有 **1.4 GB**，但過濾掉事件流雜訊（`progress`、`queue-operation`、`tool_use` 管線事件）、只留 user / assistant 對話之後，剩下 **約 200 MB** 的有用 markdown。這個過濾器就是「一張 $50 的 embedding 帳單」跟「一張 $2 的帳單」之間的差別。

---

## 踩過的雷

這些是我們在真實多 agent 環境下做這個橋時學到的教訓，幫我們省下好幾週的重工、跟一筆很有感的 embedding 費用。如果你也在做類似的東西，請在寫 adapter 之前先讀完。

1. **gBrain 只吃 markdown —— 其他所有東西都需要橋。** 不要期望 gBrain 能解析你 agent 的原生格式。所有非 markdown 來源（JSONL、SQLite、事件流、私有 session 格式）都需要轉換器。專案一開始就要把這個成本算進去。

2. **「Agent 記憶」是個發現問題，不是 adapter 問題。** 在一台機器上我們找到 agent 記憶散落在 5 個以上的地方：全域 Claude Code、全域 Codex、Hermes sessions、Conductor workspaces（編在 Claude Code 路徑裡）、以及遷移前的封存目錄。任何橋接專案的第一步都應該是一個 `discover` 指令，把每個來源的數量報告出來。在你知道自己到底要對付什麼之前，不要開始寫 adapter。

3. **專案層級的 `.claude/` 資料夾裡沒有 session 紀錄。** 不管你在哪裡啟動 Claude Code，它都會把 session jsonl 寫到 `~/.claude/projects/<encoded-path>/`。專案下的 `.claude/` 只放 `CLAUDE.md` 和 `settings.json`。不要浪費時間在專案樹裡亂爬 —— 全域 `projects/` 下那個 path 編碼過的目錄名 **就是** workspace 識別碼。

4. **Claude Code 的 jsonl 是事件流，其中 90% 是雜訊。** 事件類型包括 `progress`、`queue-operation`、`tool_use`、`tool_result`、`user`、`assistant`。只有最後兩種是真正的對話。我們那個兇一點的過濾器把 1.4 GB 的原始 jsonl 砍到約 200 MB 有用 markdown，剩下的都是工具管線跟佇列事件，沒人會想語意搜尋的東西。

5. **資料量膨脹得比你直覺的還快。** 單台機器一個月的正常使用，可以產出約 2,000 份 Claude Code session 跟約 600 份 Codex session。做任何吸收流程之前，**一定**要同時套 mtime 時間窗 **跟** 檔案大小下限。「先全部抓進來再說」會變成一張 $50 的 OpenAI 驚喜帳單。

6. **Codex 的 session 格式比 Claude Code 乾淨得多。** Codex 開頭是單一個 `session_meta` 事件（裡面有 `cwd`、`model`、`id`），之後是帶 typed `payload.role` 的事件。Claude Code 的內容則塞在 `message.content` 下面 —— 可能是字串、可能是 parts array、也可能是一個含 `tool_use` / `tool_result` 物件的 array，你要自己展開。想賺個快的就先寫 Codex，Claude Code 留到你熱身完再動。

7. **遷移前的封存檔會讓 mtime filter 失效。** 我們的 `~/.openclaw.pre-migration/` 有 2.1 GB，但用 30 天 mtime 視窗只有 2 個檔案符合 —— 因為那整個目錄照定義就是「舊的」。歷史封存要有自己的策略：把 mtime 放寬到 1 年、強制檔案大小下限（我們用 1 KB）、當成冷儲存吸收而不是每日同步。

8. **Embedding 成本其實可控 —— 真正的瓶頸是 chunker 的品質。** 57k 個 chunk 用 `text-embedding-3-large` 花不到 $2，這不是問題。問題是預設的 recursive chunking 會切出太寬的 chunk，導致明顯 query 的 cosine similarity 只有 0.03–0.07。你花了全價買了平庸的 recall。LLM-based semantic chunking 才是讓 embedding 錢花得值的地方；沒有它，那你不如直接用 grep。

9. **高量來源會在語意搜尋裡壓死低量來源。** 我們的情況是 Claude Code 貢獻了 57,627 中的 53,191 個 chunk —— **92%** 的 brain 是它。對明顯屬於 Hermes 記憶的 query（例如「我在哪個時區？」），結果竟然都是 Claude Code session，因為它量太大直接壓掉排名。如果你的來源分布這麼不平均，就得規劃 per-source 權重、來源過濾查詢、或者乾脆分成多個 brain。

---

## 設計原則

- **先 discovery，再 adapter。** 任何轉換程式之前，都要先產出「每個來源的數量」報告。實際分布永遠不是你以為的那樣。
- **一進一出。** 一個來源 session 對應一個 markdown 檔。這樣 import、去重、重跑邏輯都會很簡單。
- **用 canonical event 當中間格式。** 每個 adapter 在序列化成 markdown 前，都先發 `CanonicalEvent`。以後要換輸出格式，不用動任何 adapter。
- **預設安全。** Mtime 窗、檔案大小下限、機密遮罩預設全開，要明確下指令才能關掉。
- **執行期零相依。** 純 Bun / TS + Node stdlib，安裝不到一秒，沒有供應鏈攻擊面。
- **橋絕對不碰資料庫。** 只有 gBrain 寫 Postgres，橋只產出檔案。

---

## 安全

符合常見模式的機密字串（`sk-*`、`xoxb-*`、`ghp_*`、`AKIA*`、`postgres://` 等）會在匯出前被遮罩。遮罩清單刻意保守，不求窮盡。**在 import 到共用 brain 之前，請先檢查你的 staging 目錄。** 確切的 pattern 請看 `src/normalize.ts`。

機密遮罩是在 canonical-event 這層做的，所以每個 adapter 都免費繼承。加新 adapter 時，你不用特別去想機密 —— 只要在轉換路徑上呼叫一次 `redactSecrets(text)` 就好。

---

## 專案狀態

這是一個在單台開發機上每天實際在用的 working MVP，不是一個打磨過的產品 —— 它是一份食譜、一組 adapter，跟一份踩雷筆記。程式刻意寫得小，小到你可以一次讀完、然後改成你自己 agent stack 的版本。

歡迎 PR，特別是新 adapter。看 [`docs/EXTENDING.md`](docs/EXTENDING.md)。

---

## 把 AI 工具接上你的 brain

gBrain 吸收完、跑起來之後，下一個問題是：其他寫程式用的 AI 工具要怎麼存取？

### 走 MCP（推薦）

gBrain 內建一個 MCP server（`gbrain serve`），講 stdio 協議。任何支援 MCP 的工具都可以直接接 —— AI 會拿到 30 個工具（search、query、get_page、put_page、list_pages、add_timeline_entry、traverse_graph 等等），光看工具定義就知道怎麼用。

```bash
# Claude Code —— 註冊一次，之後所有 session 都可用
claude mcp add gbrain -s user -- \
  /path/to/.bun/bin/bun run /path/to/gbrain/src/cli.ts serve
```

| 工具 | 接法 | 備註 |
|------|------|------|
| Claude Code | `claude mcp add gbrain -s user -- bun run gbrain/src/cli.ts serve` | ✅ stdio MCP，30 個工具自動發現 |
| Claude Desktop | 加進 `claude_desktop_config.json` | 看 gBrain 的 [`docs/mcp/CLAUDE_DESKTOP.md`](https://github.com/garrytan/gbrain/blob/main/docs/mcp/CLAUDE_DESKTOP.md) |
| Cursor / Windsurf | 兩個都支援 MCP —— 用同一個 stdio 設定 | `bun run gbrain/src/cli.ts serve` |
| Hermes Agent | `hermes mcp add gbrain --command bun --args run gbrain/src/cli.ts serve` | ✅ stdio MCP，30 個工具自動發現 |
| Codex CLI | 不支援 MCP —— 把 CLI 寫進 base instruction | 見下 |
| Gemini CLI / Kimi | 不支援 MCP —— 用 CLI 或 HTTP endpoint | 見下 |

### 走 CLI（給不支援 MCP 的工具）

如果你的 AI 工具能跑 shell 指令但不支援 MCP，把這段貼進它的 system prompt、`CLAUDE.md`、`AGENTS.md` 或 base instruction：

```markdown
## Knowledge Brain
You have access to a gBrain knowledge base via CLI.
- Search: `gbrain search "keyword"`
- Semantic query: `gbrain query "question"`
- Read a page: `gbrain get <slug>`
- List pages: `gbrain list`
Use these commands when you need historical context about past decisions,
conversations, or project details.
```

AI 之後需要歷史脈絡時，會自己學著 shell out 到 `gbrain`。沒有 MCP 那麼滑順（它得自己解析 CLI 輸出，而不是直接吃結構化工具回應），但任何能跑 Bash 的 agent 都可以用。

### HTTP endpoint（給遠端 agent 或 we

# FILE: docs/SETUP.md

# Setup Guide

End-to-end walkthrough: from zero to a working gBrain on Railway Postgres, ingesting memory from Hermes / Claude Code / Codex / OpenClaw, with semantic search and an MCP server connected to Claude Code.

**Expected time:** 30–60 minutes (excluding embedding time, which runs in the background).

**Expected cost:** under $2 for the one-shot embedding of ~60k chunks (one developer's 30-day history).

---

## Prerequisites

- **macOS or Linux** (tested on macOS 25.2)
- **Bun** (`curl -fsSL https://bun.sh/install | bash`)
- **psql** (from `libpq`: `brew install libpq` then `export PATH="/opt/homebrew/opt/libpq/bin:$PATH"`)
- **Railway CLI** (`brew install railway` or `npm i -g @railway/cli`, then `railway login`)
- **gh CLI** (for cloning private repos; `brew install gh`)
- **OpenAI API key** (for embeddings — text-embedding-3-large)
- **Anthropic API key** (for optional LLM-based chunking)

You do **not** need Docker. Everything runs against managed Railway Postgres.

---

## Step 1 — Provision Railway Postgres

```bash
railway login
railway init --name gbrain-memory
railway add -d postgres
```

Then fetch the credentials:

```bash
railway variables --service Postgres | grep DATABASE_PUBLIC_URL
```

You want the **public TCP proxy URL** (looks like `postgresql://postgres:***@tramway.proxy.rlwy.net:XXXXX/railway`). Do **not** use the internal `postgres.railway.internal` URL — that only resolves inside Railway.

Enable the extensions gBrain needs:

```bash
psql "$DATABASE_PUBLIC_URL" <<SQL
CREATE EXTENSION IF NOT EXISTS vector;
CREATE EXTENSION IF NOT EXISTS pg_trgm;
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SELECT extname, extversion FROM pg_extension ORDER BY extname;
SQL
```

You should see `pg_trgm`, `vector`, `uuid-ossp`, `plpgsql`. If `vector` is missing, the Railway Postgres image is too old — open an issue on Railway or switch to the pgvector-enabled template.

---

## Step 2 — Install gBrain

gBrain is not on npm at the time of writing. Clone from source:

```bash
cd ~/Projects
git clone https://github.com/garrytan/gbrain
cd gbrain
bun install
```

Initialize the brain against your Railway URL:

```bash
bun run src/cli.ts init --url "$DATABASE_PUBLIC_URL"
```

This applies the full schema (pages, content_chunks, timeline_entries, etc.), saves the URL to `~/.gbrain/config.json`, and prints `Brain ready. 0 pages.`

Run the health check:

```bash
bun run src/cli.ts doctor
```

Everything should be green except `embeddings: No embeddings yet` — that's expected until Step 6.

---

## Step 3 — Configure API keys

gBrain reads keys from `process.env` only — it does **not** load `.env` files. Add both keys to your shell profile so every new shell picks them up:

```bash
echo 'export OPENAI_API_KEY=sk-proj-...'       >> ~/.zshrc
echo 'export ANTHROPIC_API_KEY=sk-ant-api03-...' >> ~/.zshrc
exec zsh   # reload
```

Verify without exposing the full values:

```bash
echo "O:${OPENAI_API_KEY:0:7} A:${ANTHROPIC_API_KEY:0:10}"
# Expected: O:sk-proj A:sk-ant-api
```

**Gotcha:** Claude Code's Bash tool runs non-interactive shells, which may not source `~/.zshrc` by default. If you're calling `gbrain embed` from inside Claude Code, prefix commands with `source ~/.zshrc 2>/dev/null;` to force it.

---

## Step 4 — Install the bridge

```bash
cd ~/Projects
git clone https://github.com/howardpen9/hermes-gbrain-bridge
cd hermes-gbrain-bridge
bun install    # dev-only, no runtime deps
```

See what's available on your machine before committing:

```bash
bun run src/cli.ts discover --days 30
```

Sample output from a real machine:

```
=== Discovery (last 30 days) ===

Claude Code:  1988 jsonl files
Codex:        636 jsonl files
OpenClaw:     1148 md files (1y, >1KB)

Total input candidates: 3772
```

Note the mix: Claude Code dominates by a factor of ~3× over Codex and OpenClaw. This is normal — daily conversational agents produce far more data than tooling agents.

---

## Step 5 — Export memory to staging

Dry-run first so you can see what will be produced without writing anything:

```bash
bun run src/cli.ts export --source=claude-code --dry-run --days 30
```

The dry-run prints kept/skipped counts and sample slugs. If it looks sane, run for real:

```bash
bun run src/cli.ts export --source=hermes      --out=/tmp/gbrain-staging
bun run src/cli.ts export --source=claude-code --out=/tmp/gbrain-staging --days 30
bun run src/cli.ts export --source=codex       --out=/tmp/gbrain-staging --days 30
bun run src/cli.ts export --source=openclaw    --out=/tmp/gbrain-staging --days 365
```

(The `--source=all` shortcut exists but applies the same `--days` value to every source — not ideal for OpenClaw archives, which need a longer window. Run them separately when scopes differ.)

Check staging size:

```bash
du -sh /tmp/gbrain-staging/*
```

On a reference machine this produces roughly:

```
206M    /tmp/gbrain-staging/claude-code
5.2M    /tmp/gbrain-staging/codex
104K    /tmp/gbrain-staging/hermes
 10M    /tmp/gbrain-staging/openclaw
```

The 1.4 GB of raw Claude Code jsonl became ~206 MB of useful markdown — the rest was event-stream noise that the filter dropped.

---

## Step 6 — Import into gBrain

Import with `--no-embed` first so you can confirm everything lands in Postgres before paying for embeddings:

```bash
cd ~/Projects/gbrain
bun run src/cli.ts import /tmp/gbrain-staging/hermes      --no-embed
bun run src/cli.ts import /tmp/gbrain-staging/claude-code --no-embed    # ~25 min for 2k sessions
bun run src/cli.ts import /tmp/gbrain-staging/codex       --no-embed    # ~7 min
bun run src/cli.ts import /tmp/gbrain-staging/openclaw    --no-embed    # ~12 min
```

Verify counts against Railway:

```bash
psql "$DATABASE_PUBLIC_URL" -c "
  SELECT COUNT(*) AS pages FROM pages;
  SELECT COUNT(*) AS chunks FROM content_chunks;
"
```

Then generate embeddings for everything at once:

```bash
bun run src/cli.ts embed --stale
```

This hits OpenAI text-embedding-3-large in batches of 100, with exponentia

# FILE: docs/EXTENDING.md

# Extending the Bridge

How to add an adapter for a new memory source. Takes about an hour end to end for a straightforward source, longer if the format is unusual or has a lot of noise to filter.

---

## Before you write code

1. **Find the data.** Where does the source actually put its files? Not the docs-claimed path — the real, observed path on a working machine. Run `ls`, `find`, `du -sh`. Don't trust the README of the source tool.
2. **Count the files.** How many are there in 30 days? In a year? This determines whether you need mtime filters, size floors, or per-project sharding.
3. **Sample the format.** `head -c 500 one-file.ext` and read it. Is it JSONL? Event stream? Markdown? Does it have a header? Is content nested under `payload.content` or at the top level? Are there tool-noise event types you need to drop?
4. **Write one paragraph explaining what the source is.** If you can't, you don't understand it well enough to adapt it yet.

This is the same `discover → sample → understand` loop the bridge's `hgb discover` command encourages. Skipping it is how you end up writing an adapter that silently produces 10× the data you expected.

---

## The adapter contract

An adapter is a module that exports two functions:

```ts
// Return a list of candidate files on disk, already filtered by mtime / size / etc.
export async function discoverXxxSessions(maxAgeDays: number, ...opts): Promise<string[]>

// Convert one file into a MarkdownDoc — or return null if it should be skipped.
export async function convertXxxSession(filePath: string, ...opts): Promise<MarkdownDoc | null>
```

The `MarkdownDoc` shape is defined in `src/types.ts`:

```ts
export interface MarkdownDoc {
  slug: string;                        // unique path, used as the gBrain page slug
  frontmatter: Record<string, unknown>; // serialized as YAML by toMarkdown()
  body: string;                        // the markdown body
}
```

The bridge CLI wires discover + convert together, handles dry-run, writes the markdown files. You don't need to touch the CLI — just add your adapter and register it.

---

## Required frontmatter fields

Every adapter **must** set these five fields on `frontmatter`:

| Field | Type | Purpose |
|-------|------|---------|
| `source_system` | string | Short identifier: `hermes`, `claude-code`, `codex`, `openclaw`, etc. |
| `source_type` | string | Sub-type if the source has more than one, e.g. `session`, `memory`, `workspace-md` |
| `source_path` | string | Absolute path to the original file (useful for debugging and re-runs) |
| `content_hash` | string | `sha256(body)` — used for dedup when the same content appears in multiple paths |
| `ingested_at` | string | ISO 8601 timestamp of when the adapter ran |

Everything else is adapter-specific. Examples:

- Hermes sessions also set `session_id`, `session_start`, `session_end`, `model`, `platform`, `turn_count`
- Claude Code sessions also set `project_path` (decoded from the path hash) and `session_id`
- Codex sessions also set `cwd`, `model`, `session_id`

More metadata is fine. Missing the five required fields breaks dedup and traceability.

---

## Required safety behaviors

### Secret redaction

Always run content through `redactSecrets()` from `src/normalize.ts` before writing it into the body. This catches common key patterns (`sk-*`, `xoxb-*`, `ghp_*`, `AKIA*`, `postgres://`). It's not exhaustive — add new patterns to `SECRET_PATTERNS` in `normalize.ts` if you find a source that leaks something new.

```ts
import { redactSecrets } from "../normalize.ts";

body.push(redactSecrets(turn.text));
```

### mtime filter

Every `discover*` function must accept a `maxAgeDays: number` parameter and filter out files older than that cutoff. This prevents accidentally re-ingesting years of history when you just want the last month.

```ts
const cutoff = Date.now() - maxAgeDays * 86400_000;
if (st.mtimeMs < cutoff) continue;
```

### Size floor (where appropriate)

If the source is noisy — lots of tiny operational files mixed in with real content — add a size floor. The OpenClaw adapter uses `>1KB` to cut out empty state files.

### Null returns for skipped files

If a file is technically valid but contains no useful content (e.g. a session with zero user/assistant turns, just tool noise), return `null` from the convert function. The CLI tracks skip counts and reports them at the end of export.

---

## Adapter template

Copy this into `src/adapters/<your-source>.ts` and fill in the blanks:

```ts
import { readdir, readFile, stat } from "node:fs/promises";
import { join, basename } from "node:path";
import { homedir } from "node:os";
import { sha256, redactSecrets } from "../normalize.ts";
import type { MarkdownDoc } from "../types.ts";

// Replace with the actual event/row shape from your source.
interface YourSourceEvent {
  role?: string;
  content?: unknown;
  timestamp?: string;
  [k: string]: unknown;
}

/**
 * Convert one source file to a single MarkdownDoc.
 * Return null if the file is empty or contains no useful content.
 */
export async function convertYourSourceSession(filePath: string): Promise<MarkdownDoc | null> {
  const raw = await readFile(filePath, "utf8");
  const lines = raw.split("\n").filter(Boolean); // assumes JSONL; adjust for other formats

  const turns: { role: string; text: string; ts?: string }[] = [];

  for (const line of lines) {
    let obj: YourSourceEvent;
    try { obj = JSON.parse(line); } catch { continue; }

    // ——— FILTER: only keep conversation events ———
    const role = obj.role;
    if (role !== "user" && role !== "assistant") continue;

    // ——— EXTRACT: get plain text from whatever content shape the source uses ———
    const text = typeof obj.content === "string" ? obj.content : "";
    if (!text || text.length < 3) continue;

    turns.push({ role, text, ts: obj.timestamp });
  }

  if (turns.length === 0) return null;

  const sessionId = basename(filePath).replace(/\.[^.]+$/, "");
  const firstTs = tu
