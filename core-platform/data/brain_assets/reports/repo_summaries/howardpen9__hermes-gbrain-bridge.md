# Repo Summary Source: howardpen9/hermes-gbrain-bridge
- URL: https://github.com/howardpen9/hermes-gbrain-bridge
- Local Path: core-platform/data/brain_assets/repos/github_stars/howardpen9__hermes-gbrain-bridge
- Buckets: agent, rag, mcp, llm_runtime
- Stars: 30
- Language: TypeScript
- Description: Convert Hermes / OpenClaw agent memory (JSONL sessions, MEMORY.md) to markdown for gBrain ingest
- Clone Status: cloned
## Extracted README / Docs


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
| Raw input — Claud


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

3. **專案層級的 `.claude/` 資料夾裡沒有 session 紀錄。** 不管你在哪裡啟動 Claude Code，它都會把 session jsonl 寫到 `~/.claude/projects/<encoded-path>/`。專案下的 `.claude/` 只放 `CLAUDE.md`


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
