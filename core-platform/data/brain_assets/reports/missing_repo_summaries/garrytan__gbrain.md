# Missing Repo Summary Source: garrytan/gbrain

- URL: https://github.com/garrytan/gbrain
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/garrytan__gbrain
- Clone Status: cloned
- Language: TypeScript
- Stars: 15199
- Topics: 
- Description: Garry's Opinionated OpenClaw/Hermes Agent Brain

## Extracted README / Docs / Examples



# FILE: README.md

# GBrain

Your AI agent is smart but forgetful. GBrain gives it a brain.

Built by the President and CEO of Y Combinator to run his actual AI agents. The production brain powering his OpenClaw and Hermes deployments: **17,888 pages, 4,383 people, 723 companies**, 21 cron jobs running autonomously, built in 12 days. The agent ingests meetings, emails, tweets, voice calls, and original ideas while you sleep. It enriches every person and company it encounters. It fixes its own citations and consolidates memory overnight. You wake up and the brain is smarter than when you went to bed.

The brain wires itself. Every page write extracts entity references and creates typed links (`attended`, `works_at`, `invested_in`, `founded`, `advises`) with zero LLM calls. Hybrid search. Self-wiring knowledge graph. Structured timeline. Backlink-boosted ranking. Ask "who works at Acme AI?" or "what did Bob invest in this quarter?" and get answers vector search alone can't reach. Benchmarked side-by-side against the category: gbrain lands **P@5 49.1%, R@5 97.9%** on a 240-page Opus-generated rich-prose corpus, beating its own graph-disabled variant by **+31.4 points P@5** and ripgrep-BM25 + vector-only RAG by a similar margin. The graph layer plus v0.12 extract quality together carry the gap. Full BrainBench scorecards + corpus live in the sibling [gbrain-evals](https://github.com/garrytan/gbrain-evals) repo.

GBrain is those patterns, generalized. 34 skills. Install in 30 minutes. Your agent does the work. As Garry's personal agent gets smarter, so does yours.

**New in v0.25.0 — BrainBench-Real (session capture, contributor opt-in):** with `GBRAIN_CONTRIBUTOR_MODE=1` set in your shell, every real `query` + `search` call through MCP, CLI, or the subagent tool-bridge gets captured (PII-scrubbed) into an `eval_candidates` table. Snapshot with `gbrain eval export`, replay against your code change with `gbrain eval replay`. Three numbers come back: mean Jaccard@k between captured and current retrieved slugs, top-1 stability, and latency Δ. **Off by default** for production users — no surprise data accumulation. Walkthrough: [docs/eval-bench.md](docs/eval-bench.md). NDJSON wire format: [docs/eval-capture.md](docs/eval-capture.md).

**New in v0.28.8 — LongMemEval in the box:** `gbrain eval longmemeval <dataset.jsonl>` runs the public [LongMemEval](https://huggingface.co/datasets/xiaowu0162/longmemeval) benchmark against gbrain's hybrid retrieval. One in-memory PGLite per run, `TRUNCATE` between questions (runtime-enumerated tables, schema-migration-safe), 25.9ms p50 per question on Apple Silicon. Your `~/.gbrain` brain is never touched. Retrieved chat content is sanitized with the same `INJECTION_PATTERNS` that protect takes — one source of truth for prompt-injection defense. Hand the JSONL output to LongMemEval's `evaluate_qa.py` to score.

> **~30 minutes to a fully working brain.** Database ready in 2 seconds (PGLite, no server). You just answer questions about API keys.

> **LLMs:** fetch [`llms.txt`](llms.txt) for the documentation map, or [`llms-full.txt`](llms-full.txt) for the same map with core docs inlined in one fetch. **Agents:** start with [`AGENTS.md`](AGENTS.md) (or [`CLAUDE.md`](CLAUDE.md) if you're Claude Code).

> **Embedding providers:** OpenAI is the default, but gbrain ships with **14 recipes** covering Voyage, Google Gemini, Azure OpenAI, MiniMax, Alibaba DashScope, Zhipu, Ollama (local), llama.cpp llama-server (local), LiteLLM proxy (universal), and 5 more. Run `gbrain providers list` to see them, or read [`docs/integrations/embedding-providers.md`](docs/integrations/embedding-providers.md) for setup, pricing, and a decision tree. `gbrain doctor` will surface alternative providers whose env vars you already have set.

> **New in v0.32.3.0 — compress your AGENTS.md without losing accuracy:** if your downstream agent fork has grown a 25KB+ `AGENTS.md` / `RESOLVER.md`, the new [`functional-area-resolver`](skills/functional-area-resolver/SKILL.md) skill ships a two-layer dispatch pattern that compresses 25KB → 13KB (48% the size) while **beating** the verbose baseline by +13 to +17pp across Opus 4.7, Sonnet 4.6, and Haiku 4.5. A/B eval harness, cross-model receipts, and reproduction instructions live at [`evals/functional-area-resolver/`](evals/functional-area-resolver/). The static-prompt analog of AnyTool / RAG-MCP / Anthropic Agent Skills progressive disclosure — single-LLM-pass dispatch, no second routing call.

## Install

### On an agent platform (recommended)

GBrain is designed to be installed and operated by an AI agent. If you don't have one running yet:

- **[OpenClaw](https://openclaw.ai)** ... Deploy [AlphaClaw on Render](https://render.com/deploy?repo=https://github.com/chrysb/alphaclaw) (one click, 8GB+ RAM)
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** ... Deploy on [Railway](https://github.com/praveen-ks-2001/hermes-agent-template) (one click)

Paste this into your agent:

```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

That's it. The agent clones the repo, installs GBrain, sets up the brain, loads 34 skills, and configures recurring jobs. You answer a few questions about API keys. ~30 minutes.

If your agent doesn't auto-read `AGENTS.md`, point it at that file first:
`https://raw.githubusercontent.com/garrytan/gbrain/master/AGENTS.md` is the non-Claude
agent operating protocol (install, read order, trust boundary, common tasks). For
the full doc map, use `llms.txt` at the same URL root.

### Standalone CLI (no agent)

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain && bun install && bun link
gbrain init                     # local brain, ready in 2 seconds
gbrain import ~/notes/          # index your markdown
gbrain query "what themes show up across my notes?"
```

**Do NOT use `bun install -g github:garrytan/gbrain`.** Bun blocks the top-level
postinstall hook on global installs, so schema migrations never run and the CLI
aborts with `Aborted()` the first time it opens PGLite. Use `git clone + bun install
&& bun link` as shown above. See [#218](https://github.com/garrytan/gbrain/issues/218).

**Do NOT use `bun add -g gbrain` or `npm install -g gbrain`.** The npm registry
has an unrelated package squatting that name (`gbrain@1.3.x`) — you'd silently
install the wrong binary and overwrite the canonical one. v0.28.5+ detects this
and prints a recovery message on `gbrain upgrade`, but the `git clone + bun link`
path above is the only reliable install method until we publish under
`@garrytan/gbrain` (tracked v0.29 follow-up). See
[#658](https://github.com/garrytan/gbrain/issues/658).

```
3 results (hybrid search, 0.12s):

1. concepts/do-things-that-dont-scale (score: 0.94)
   PG's argument that unscalable effort teaches you what users want.
   [Source: paulgraham.com, 2013-07-01]

2. originals/founder-mode-observation (score: 0.87)
   Deep involvement isn't micromanagement if it expands the team's thinking.

3. concepts/build-something-people-want (score: 0.81)
   The YC motto. Connected to 12 other brain pages.
```

### MCP server (Claude Code, Cursor, Windsurf)

GBrain exposes 30+ MCP tools via stdio:

```json
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

Add to `~/.claude/server.json` (Claude Code), Settings > MCP Servers (Cursor), or your client's MCP config.

### Remote MCP with OAuth 2.1 (ChatGPT, Claude Desktop, Cowork, Perplexity)

`gbrain serve --http` starts a production-grade OAuth 2.1 server with an embedded admin dashboard. Zero external infrastructure. Every major AI client connects, every request is scoped, every action is logged.

```bash
# Start the HTTP server (prints admin bootstrap token on first start)
gbrain serve --http --port 3131

# Open the admin dashboard, paste the bootstrap token, register a client
open http://localhost:3131/admin

# Expose publicly (set --public-url so the OAuth issuer matches)
ngrok http 3131 --url your-brain.ngrok.app
gbrain serve --http --port 3131 --public-url https://your-brain.ngrok.app

# ChatGPT and other OAuth-aware clients can also connect:
claude mcp add gbrain -t http https://your-brain.ngrok.app/mcp -H "Authorization: Bearer TOKEN"
```

Register OAuth clients from the `/admin` dashboard — click **Register client**,
pick scopes, save the credentials shown once in the reveal modal. Programmatic
registration via `oauthProvider.registerClientManual(...)` and the
`gbrain auth register-client` CLI are also available.

- **OAuth 2.1 via the MCP SDK** — client credentials (machine-to-machine: Perplexity, Claude), authorization code + PKCE (browser-based: ChatGPT), refresh token rotation, revocation, protected resource metadata. Optional Dynamic Client Registration behind `--enable-dcr` (DCR redirect_uris must be `https://` or loopback per RFC 6749 §3.1.2.1).
- **Scoped operations** — 30 operations tagged `read | write | admin`. `sync_brain` and `file_upload` are `localOnly`, rejected over HTTP.
- **React admin dashboard** — 7 screens baked into the binary (~65KB gzip). Live SSE activity feed, agents table, credential reveal, filterable request log, per-client config export.
- **Legacy bearer tokens still work** — pre-v0.26 `gbrain auth create` tokens continue to authenticate as `read+write+admin`. v0.22.7's simpler `src/mcp/http-transport.ts` path stays compiled in for backward compat callers; v0.26+ deployments use the OAuth-aware `serve-http.ts`.

Per-client guides: [`docs/mcp/`](docs/mcp/DEPLOY.md). Hardening defaults, env vars, and threat model: [SECURITY.md](SECURITY.md).

### Using gbrain with GStack

If your engineering agent runs on [GStack](https://github.com/garrytan/gstack), point it at gbrain for code lookup instead of grep+read. Cathedral II (v0.21.0) ships call-graph edges and two-pass retrieval — `/investigate`, `/review`, `/plan-eng-review`, and `/office-hours` all benefi

# FILE: docs/eval-capture.md

# Eval capture — NDJSON schema reference

**Status:** stable from v0.21.0. Schema versioning via `schema_version`
on every row; additive changes increment the minor version; removals
are breaking-schema-v2.

**Audience:** downstream consumers (primarily the sibling
[gbrain-evals](https://github.com/garrytan/gbrain-evals) repo) that
replay captured real-world queries as a BrainBench-Real fixture.

## The pipeline

```
MCP / CLI / subagent tool-bridge caller
     │
     ▼
src/core/operations.ts — query + search op handlers
     │
     │ (hybridSearch or searchKeyword)
     │
     ▼
{results, meta: HybridSearchMeta}                 ┌── captureEvalCandidate
     │                                             │    (fire-and-forget)
     ▼                                             │
return to caller                                   ▼
                                            scrubPii(query) ←── src/core/eval-capture-scrub.ts
                                                   │
                                                   ▼
                                           buildEvalCandidateInput
                                                   │
                                                   ▼
                                           engine.logEvalCandidate
                                                   │
                                    ┌──────────────┴──────────────┐
                                    │ success                     │ fail
                                    ▼                             ▼
                                INSERT into eval_candidates    engine.logEvalCaptureFailure
                                                                 (reason: db_down | rls_reject |
                                                                  check_violation |
                                                                  scrubber_exception | other)
```

## `gbrain eval export` — the consumer contract

```sh
gbrain eval export [--since DUR] [--limit N] [--tool query|search]
```

Emits NDJSON to **stdout**. One JSON object per `\n`-terminated line.
stderr receives progress heartbeats. Every line starts with
`"schema_version": 1` so a forward-compat parser can fail loudly on
schema v2 instead of silently misparsing.

Typical usage from gbrain-evals:

```sh
# Snapshot the last week of real traffic for replay
gbrain eval export --since 7d > brainbench-real.ndjson
```

```sh
# Stream through jq for ad-hoc analysis
gbrain eval export --tool query | jq -c 'select(.latency_ms > 500)'
```

## Row schema (v1)

Every exported row has this shape. Field order in JSON output is not
guaranteed; consumers MUST key by name, not position.

| Field | Type | Notes |
|---|---|---|
| `schema_version` | number | Always `1` on v1 rows. Forward-compat gate. |
| `id` | number | Autoincrement primary key. Stable across exports. |
| `tool_name` | `"query"` \| `"search"` | Which MCP operation captured this row. |
| `query` | string | **Already PII-scrubbed** by `scrubPii` unless `eval.scrub_pii: false`. Emails / phones / SSN / Luhn-verified credit cards / JWTs / bearer tokens replaced with `[REDACTED]`. Max length 50KB (CHECK-enforced). |
| `retrieved_slugs` | string[] | Deduplicated slugs that came back in `SearchResult[]`. |
| `retrieved_chunk_ids` | number[] | Every chunk id in result order (duplicates preserved — one per hit). |
| `source_ids` | string[] | Distinct `sources.id` values across the result set (v0.18 multi-source). Empty for pre-v0.18 rows that lacked the column. |
| `expand_enabled` | boolean \| null | Whether the caller **requested** Haiku expansion. `null` for `search` (no expansion concept). |
| `detail` | `"low"` \| `"medium"` \| `"high"` \| null | Detail level the caller **requested**. `null` when omitted. |
| `detail_resolved` | `"low"` \| `"medium"` \| `"high"` \| null | What `hybridSearch` **actually used** after auto-detect. `null` when neither caller nor heuristic classified. |
| `vector_enabled` | boolean | True iff vector search actually ran. `false` when `OPENAI_API_KEY` was missing or the embed call failed. **Replay MUST respect this** — rows with `false` only exercised the keyword path. |
| `expansion_applied` | boolean | True iff Haiku expansion actually produced variants (not just "was requested"). |
| `latency_ms` | number | Wall-clock duration of the op handler (includes capture itself — negligible since it's fire-and-forget). |
| `remote` | boolean | `true` for MCP callers (untrusted), `false` for local CLI. Partitions "real agent traffic" from "operator probing." |
| `job_id` | number \| null | `OperationContext.jobId` when the caller was a subagent tool-bridge. Null for MCP + CLI. |
| `subagent_id` | number \| null | `OperationContext.subagentId` for subagent-owned runs. |
| `created_at` | string (ISO 8601) | UTC timestamp of insert. |

## Ordering + determinism

`listEvalCandidates` orders by `created_at DESC, id DESC`. Same-
millisecond inserts tie on `created_at`; `id DESC` is the stable
tiebreaker. Replay tools can consume rows in order and assume:
- no duplicate rows across calls with non-overlapping `--since` windows
- no missed rows across calls that chain `--since` windows (window end
  of run 1 is the strict upper bound, not a soft cursor)

## Schema versioning promise

- **v1 (shipped v0.21.0)** — this document. All fields listed above.
- **Additive changes** increment gbrain minor version (v0.25.0, v0.23.0
  …) and ship with new optional fields. Consumers keyed on known fields
  ignore unknown keys and keep working.
- **Breaking changes** (rename, type change, removal) increment
  `schema_version` to 2. Consumers MUST branch on `schema_version` to
  stay compatible.

## `eval_capture_failures` — companion audit table

Not exported by `gbrain eval export`. Surfaced via `gbrain doctor`:

```sh
gbrain doctor   # warns when failures in last 24h > 0
```

Reason enum (stable): `db_down` | `rls_reject` | `check_violation` |
`scrubber_exception

# FILE: docs/GBRAIN_VERIFY.md

# GBrain Installation Verification Runbook

Run these checks after install to confirm every part of GBrain is working.
Each check includes the command, expected output, and what to do if it fails.

The most important check is #4 (live sync). "Sync ran" is not the same as
"sync worked." A sync that silently skips pages because of a pooler bug is
worse than no sync at all, because you think it's working.

---

## 1. Schema Verification

**Command:**

```bash
gbrain doctor --json
```

**Expected:** All checks return `"ok"`:
- `connection`: connected, N pages
- `pgvector`: extension installed
- `rls`: enabled on all tables
- `schema_version`: current
- `embeddings`: coverage percentage

**If it fails:** The doctor output includes specific fix instructions for each
check. See `skills/setup/SKILL.md` Error Recovery table.

---

## 2. Skillpack Loaded

**Check:** Ask the agent: "What is the brain-agent loop?"

**Expected:** The agent references GBRAIN_SKILLPACK.md Section 2 and describes
the read-write cycle: detect entities, read brain, respond with context, write
brain, sync.

**If it fails:** The agent hasn't loaded the skillpack. Run step 6 from the
install paste (read `docs/GBRAIN_SKILLPACK.md`).

---

## 3. Auto-Update Configured

**Command:**

```bash
gbrain check-update --json
```

**Expected:** Returns JSON with `current_version`, `latest_version`,
`update_available` (boolean). The cron `gbrain-update-check` is registered.

**If it fails:** Run step 7 from the install paste. See GBRAIN_SKILLPACK.md
Section 17.

---

## 4. Live Sync Actually Works

This is the most important check. Three parts.

### 4a. Coverage Check

Compare page count in the DB against syncable file count in the repo:

```bash
gbrain stats
```

Then count syncable files:

```bash
find /data/brain -name '*.md' \
  -not -path '*/.*' \
  -not -path '*/.raw/*' \
  -not -path '*/ops/*' \
  -not -name 'README.md' \
  -not -name 'index.md' \
  -not -name 'schema.md' \
  -not -name 'log.md' \
  | wc -l
```

**Expected:** Page count in `gbrain stats` should be close to the file count.
Some difference is normal (files added since last sync), but if page count is
less than half the file count, sync is silently skipping pages.

**If page count is way too low:** The #1 cause is the connection pooler bug.
Check your `DATABASE_URL`:
- If it contains `pooler.supabase.com:6543`, verify it's using **Session mode**,
  not Transaction mode.
- Transaction mode breaks `engine.transaction()` and causes `.begin() is not a
  function` errors.
- Fix: switch to Session mode pooler string, then run `gbrain sync --full`
  to reimport everything.

### 4b. Embed Check

```bash
gbrain stats
```

**Expected:** Embedded chunk count should be close to total chunk count.

**If embedded is much lower than total:**

```bash
gbrain embed --stale
```

If `OPENAI_API_KEY` is not set, embeddings can't be generated. Keyword search
still works without embeddings, but hybrid/semantic search won't.

### 4c. End-to-End Test

This is the real test. Edit a brain page, push, wait, search.

1. Edit a page in the brain repo (e.g., correct a fact on a person's page):

```bash
# Example: fix a line in Gustaf's page
cd /data/brain
# Make a small edit to any .md file
git add -A && git commit -m "test: verify live sync" && git push
```

2. Wait for the next sync cycle (cron interval or `--watch` poll).

3. Search for the corrected text:

```bash
gbrain search "<text from the correction>"
```

**Expected:** The search returns the **corrected** text, not the old version.

**If it returns old text:** Sync failed silently. Check:
- Is the sync cron registered and running?
- Is `gbrain sync --watch` still alive (if using watch mode)?
- Run `gbrain config get sync.last_run` to see when sync last ran.
- Run `gbrain sync --repo /data/brain` manually and check for errors.
- If you see `.begin() is not a function`, fix the pooler (see 4a above).

---

## 5. Embedding Coverage

**Command:**

```bash
gbrain stats
```

**Expected:** Embedded chunk count matches (or is close to) total chunk count.

**If zero or very low:** `OPENAI_API_KEY` may be missing or invalid. Check:

```bash
echo $OPENAI_API_KEY | head -c 10
```

If blank, set the key. Then:

```bash
gbrain embed --stale
```

---

## 6. Brain-First Lookup Protocol

**Check:** Ask the agent about a person or concept that exists in the brain.

**Expected:** The agent uses `gbrain search` or `gbrain query` FIRST, not grep
or external APIs. The response includes brain-sourced context with source
attribution.

**If it fails:** The brain-first lookup protocol isn't injected into the agent's
system context. See `skills/setup/SKILL.md` Phase D.

---

## 7. Knowledge Graph Wired

The v0.12.0 graph layer needs to be populated for existing brains. New writes are
auto-linked, but historical pages need a one-time backfill.

**Command:**

```bash
gbrain stats | grep -E 'links|timeline'
```

**Expected:** Both `links` and `timeline_entries` are non-zero (assuming the brain
has content with entity references and dated markdown).

**If it's zero on a brain with imported content:** Run the backfill.

```bash
gbrain extract links --source db --dry-run | head -5    # preview
gbrain extract links --source db                         # commit
gbrain extract timeline --source db
gbrain stats                                             # confirm > 0
```

**Bonus check** — graph traversal works:

```bash
# Pick any well-connected slug from your brain
gbrain graph-query people/<some-person-slug> --depth 2
```

**Expected:** Indented tree of typed edges (`--attended-->`, `--works_at-->`, etc.).
If the slug has no inbound or outbound links, try a different one or run extract
again.

**If extract finds nothing:** Your pages may not use entity-reference syntax. The
extractor matches `[Name](people/slug)`, `[Name](../people/slug.md)`, and bare
`people/slug` references. If your brain uses a different format, the auto-link
heuristics won't find them — file an iss

# FILE: docs/progress-events.md

# Progress events

Canonical reference for the JSONL progress stream that `gbrain` writes to
`stderr` when a bulk command runs with `--progress-json`. Stable from
v0.15.2. Additive changes only; no renames or removals without a major
version bump.

Most humans won't read this page. Agents parsing progress will.

## When do I get these events?

Any of these commands stream events when `--progress-json` is set:

- `gbrain doctor` (DB checks, JSONB integrity, markdown body completeness,
  integrity sample)
- `gbrain orphans`
- `gbrain embed`
- `gbrain files sync`
- `gbrain export`
- `gbrain extract [links|timeline|all]` (fs or db source)
- `gbrain import`
- `gbrain sync`
- `gbrain migrate --to …`
- `gbrain repair-jsonb`
- `gbrain check-backlinks`
- `gbrain lint`
- `gbrain integrity auto`
- `gbrain eval`
- `gbrain apply-migrations` (the orchestrator + every child command)

Non-bulk commands (`stats`, `graph-query`, `get`, `put`, etc.) don't emit
events — they return in under a second.

## Channel

- Progress events: **`stderr`**, one JSON object per line, `\n`-terminated.
- Data results (`--json` payloads from each command): **`stdout`**.
- Final human summaries: **`stdout`**.

Agents can safely capture stdout for their result parsing and read stderr
separately for progress.

## Flags

| Flag | Behavior |
|---|---|
| *(none)* | Auto. TTY: `\r`-rewriting single line. Non-TTY: plain line-per-event on stderr. |
| `--progress-json` | Force JSON-lines mode on stderr (this doc). |
| `--quiet` | Suppress progress entirely. Warnings and final output still print. |
| `--progress-interval=<ms>` | Override the minimum interval between tick emits (default 1000). |

Global flags: parsed by `src/core/cli-options.ts` before command dispatch,
so `gbrain --progress-json doctor` works the same as
`gbrain doctor --progress-json` (the latter also works — per-command
parsers see the flag via the shared `CliOptions` singleton).

## Event types

Every event is a single-line JSON object with these common fields:

| Field | Type | Notes |
|---|---|---|
| `event` | string | One of: `start`, `tick`, `heartbeat`, `finish`, `abort`. |
| `phase` | string | Machine-stable snake_case, dot-separated. See "Phase names" below. |
| `ts` | ISO 8601 UTC string | Event emission time. |
| `elapsed_ms` | number | Ms since the phase started. Present on `tick`/`heartbeat`/`finish`/`abort`. |

### `start`

Emitted when a phase begins.

```json
{"event":"start","phase":"doctor.db_checks","ts":"2026-04-20T12:34:56.789Z"}
{"event":"start","phase":"import.files","total":52000,"ts":"2026-04-20T12:34:56.789Z"}
```

Optional fields:

- `total` — the total item count if known at start.

### `tick`

Emitted periodically during iteration. Time- and item-gated: the reporter
won't emit more often than `minIntervalMs` (default 1000) and
`minItems` (default `max(10, ceil(total/100))`).

```json
{"event":"tick","phase":"orphans.scan","done":15000,"total":52000,"pct":28.8,"elapsed_ms":4200,"eta_ms":10300,"ts":"..."}
```

Fields:

- `done` — items completed in this phase.
- `total` — total items, if known. Omitted when the scan doesn't have a
  total up front (e.g. a streaming iterator).
- `pct` — `done/total * 100`, one decimal. Omitted when `total` is unknown.
- `eta_ms` — projected ms until `done === total`, from the observed rate.
  Omitted when `total` is unknown.
- `note` — optional string with the current item (e.g. a slug or filename).

### `heartbeat`

Emitted for long-running single operations that don't iterate
(e.g. `SELECT` against a 50K-row table). No `done`, no `total` — just a
signal that work is still happening.

```json
{"event":"heartbeat","phase":"doctor.markdown_body_completeness","note":"scanning pages for truncation…","elapsed_ms":1000,"ts":"..."}
```

### `finish`

Emitted when a phase completes normally.

```json
{"event":"finish","phase":"import.files","done":52000,"total":52000,"elapsed_ms":187000,"ts":"..."}
```

### `abort`

Emitted by a single process-level SIGINT/SIGTERM handler that tracks every
live phase. After `abort`, no further events emit for that phase.

```json
{"event":"abort","phase":"doctor.markdown_body_completeness","reason":"SIGINT","elapsed_ms":5300,"ts":"..."}
```

## Phase names

Phases use `snake_case.dot.path` naming. A fresh reporter starts at the
root; `child()` composition appends to the parent's current phase, so a
sync that calls import emits `sync.import.<file>`, not `import.<file>`.

Stable phase names shipped in v0.15.2:

- `doctor.db_checks` (umbrella for all DB-side doctor checks)
- `orphans.scan`
- `embed.pages`
- `extract.links_fs`, `extract.timeline_fs`, `extract.links_db`, `extract.timeline_db`
- `import.files`
- `sync.deletes`, `sync.renames`, `sync.imports`
- `migrate.copy_pages`, `migrate.copy_links`
- `repair_jsonb.run`, `repair_jsonb.<table>.<column>`
- `backlinks.scan`
- `lint.pages`
- `integrity.auto`
- `eval.single`, `eval.ab`
- `export.pages`
- `files.sync`

Sub-phases exposed via `child()`:

- `sync.import.files` — nested inside a sync
- `apply_migrations.v0_12_2.jsonb_repair` — nested inside the orchestrator

## Subprocess inheritance

When a parent CLI spawns `gbrain …` child processes (mostly in
`src/commands/migrations/*`), global flags (`--quiet`, `--progress-json`,
`--progress-interval`) are propagated to the child's argv via the
`childGlobalFlags()` helper in `src/core/cli-options.ts`. Child stderr
passes straight through `stdio: 'inherit'` so the event stream is one
merged JSONL feed on the parent's stderr.

One exception: the orchestrator phase in `migrations/v0_12_2.ts` that
captures child stdout (`repair-jsonb --dry-run --json` for verification)
does not pass `--progress-json` to avoid any risk of stdout pollution
breaking the orchestrator's `JSON.parse`. Its stdio is explicit:
`['ignore', 'pipe', 'inherit']` so stderr still flows through.

## Minion jobs

`gbrain jobs work` (the Minion worker daemon) keeps progress in the DB,
not on stderr. Each Minion handler that 

# FILE: docs/storage-tiering.md

# Storage Tiering: db-tracked vs db-only directories

## Overview

GBrain supports storage tiering to separate version-controlled content from bulk machine-generated data. This prevents git repositories from becoming bloated with large amounts of automatically generated content while still preserving it in the database.

> Note on naming: prior to v0.22.11 the keys were `git_tracked` / `supabase_only`. The canonical names are now `db_tracked` / `db_only` (engine-agnostic — works on both PGLite and Postgres). The deprecated keys still load with a once-per-process warning. Run `gbrain doctor --fix` for an automated rename when that path lands.

## Configuration

Add a `storage` section to your `gbrain.yml` file in the brain repository root:

```yaml
storage:
  # Directories that are version-controlled (human-edited, committed to git).
  db_tracked:
    - people/
    - companies/
    - deals/
    - concepts/
    - yc/
    - ideas/
    - projects/

  # Directories persisted via the brain database only (bulk machine-generated
  # content). Written to disk as a local cache but not committed to git;
  # `gbrain sync` auto-manages .gitignore for these paths. `gbrain export
  # --restore-only` repopulates missing files from the database.
  db_only:
    - media/x/
    - media/articles/
    - meetings/transcripts/
```

Path requirements:

- Each directory must end with `/` for canonical form. The validator auto-normalizes missing trailing slashes (one-time info note shows what changed).
- A directory cannot appear in both tiers — that's a tier-overlap error and `loadStorageConfig` throws `StorageConfigError`. Edit `gbrain.yml` to remove the overlap and try again.

## Behavior Changes

### 1. `gbrain sync` — automatic .gitignore management

When storage configuration is present, `gbrain sync` automatically manages `.gitignore` entries on every successful sync:

- Adds missing `db_only` directory patterns to `.gitignore`.
- Idempotent — re-running adds no duplicate entries.
- Stable comment header so the managed block is grep-able.
- Skipped on `--dry-run` (don't mutate disk in preview mode).
- Skipped on `blocked_by_failures` status (sync state is inconsistent).
- Skipped when the repo is a git submodule (`.git` is a file, not a directory) — submodule .gitignore changes don't survive parent updates. A warning explains.
- Skipped entirely when `GBRAIN_NO_GITIGNORE=1` is set (escape hatch for shared-repo setups where a maintainer wants gbrain to leave .gitignore alone).
- Failures (write permission denied, etc.) are caught and logged, never crash sync.

Example `.gitignore` addition:

```gitignore
# Auto-managed by gbrain (db_only directories)
media/x/
media/articles/
meetings/transcripts/
```

### 2. `gbrain export --restore-only` — repopulate missing db_only files

```bash
# Restore only missing db_only files from the database.
gbrain export --restore-only --repo /path/to/brain

# Filter by page type.
gbrain export --restore-only --type media --repo /path/to/brain

# Filter by slug prefix.
gbrain export --restore-only --slug-prefix media/x/ --repo /path/to/brain

# Combine filters.
gbrain export --restore-only --type media --slug-prefix media/x/ --repo /path/to/brain
```

The `--restore-only` flag:

- Resolves repoPath via the chain `--repo` → typed `sources.getDefault()` → hard error.
  Never falls through to the current directory.
- Only exports pages that match `db_only` patterns AND are missing from disk.
- Ideal for container restart recovery and fresh clones.

### 3. `gbrain storage status` — storage-tier health dashboard

```bash
# Human-readable status.
gbrain storage status --repo /path/to/brain

# JSON output for scripts and orchestrators.
gbrain storage status --repo /path/to/brain --json
```

Output includes:

- Total page counts by storage tier.
- Disk usage breakdown by tier.
- Missing files that need restoration (top 10 shown; full list in `--json`).
- Configuration validation warnings.
- Current tier directory listing.

Example output:

```
Storage Status
==============

Repository: /data/brain
Total pages: 15,243

Storage Tiers:
-------------
DB tracked:     2,156 pages
DB only:        12,887 pages
Unspecified:    200 pages

Disk Usage:
-----------
DB tracked:     45.2 MB
DB only:        2.1 GB

Missing Files (need restore):
-----------------------------
  media/x/tweet-1234567890
  media/x/tweet-0987654321
  ... and 47 more

Use: gbrain export --restore-only --repo "/data/brain"

Configuration:
--------------
DB tracked directories:
  - people/
  - companies/
  - deals/

DB-only directories:
  - media/x/
  - media/articles/
  - meetings/transcripts/
```

## Validation

`loadStorageConfig` runs `normalizeAndValidateStorageConfig` after parsing:

- Auto-fixes (silent, with one-time info note showing what changed):
  - Missing trailing `/` is added: `'media/x'` → `'media/x/'`.
- Throws `StorageConfigError` (caller sees a clean exit-1 with actionable message):
  - Same directory in both `db_tracked` and `db_only` (ambiguous routing).

## Use cases

### Brain repository scaling

Perfect for brain repositories crossing 50K-200K+ files where:

- Core knowledge (people, companies, deals) remains git-tracked.
- Bulk data (tweets, articles, transcripts) moves to db_only.
- Development stays fast with smaller git repos.
- Full data remains available via the database.

### Container-based deployments

Essential for ephemeral container environments:

- Git repo contains only essential files.
- Container restarts don't lose db_only data.
- `gbrain export --restore-only` quickly restores bulk files when needed.
- Local disk acts as a cache layer.

### Multi-environment consistency

Enables consistent data access across environments:

- Development: small git clone, restore bulk data on demand.
- Production: full dataset via the database, selective local caching.
- CI/CD: fast tests with git-tracked data only.

## Migration strategy

1. **Assess current repository**: use `gbrain storage status` to

# FILE: docs/contradictions.md

# gbrain eval suspected-contradictions (v0.32.6)

The contradiction probe samples retrieval results, asks an LLM judge whether
any pair contradicts on a factual claim relevant to the user's query, and
aggregates into a calibrated report. The output is data — the operator
decides what to act on. This doc covers the architecture, severity rubric,
how to interpret the headline number, and when to act.

## Why this exists

gbrain handles contradictions for *curated* pages via compiled-truth-plus-
timeline and source-boost: when `companies/acme.md` says MRR is $2M and a
chat transcript from 2024 says MRR was $50K, the curated page outranks the
chat. `takes.active` filtering hides explicitly-superseded takes. Recency
decay biases ranking toward fresher content per source-tier.

What none of those mechanisms measure: how often do unmarked semantic
contradictions actually surface in retrieval? Without a probe, every
"should we build the bigger swing (chunk-level `revises` field + ranking
change)" decision is vibes. The probe produces evidence.

## Architecture

```
        ┌──────────────────────────────────────┐
        │ gbrain eval suspected-contradictions │
        └──────────────────┬───────────────────┘
                           │
        ┌──────────────────▼───────────────────┐
        │ For each query: hybridSearch top-K   │
        │ → cross_slug_chunks + intra_page     │
        │   chunk-vs-take pairs                │
        └──────────────────┬───────────────────┘
                           │
        ┌──────────────────▼───────────────────┐
        │ Date pre-filter: skip pairs whose    │
        │ dates are >30d apart (Codex fix:     │
        │ same-paragraph-dual-date overrides)  │
        └──────────────────┬───────────────────┘
                           │
        ┌──────────────────▼───────────────────┐
        │ Persistent cache lookup              │
        │ (chunk_a_hash, chunk_b_hash, model,  │
        │  prompt_version, truncation_policy)  │
        └────────┬─────────┬────────────────────┘
              hit│         │miss
                 │         ▼
                 │   ┌─────────────────────────┐
                 │   │ LLM judge call          │
                 │   │ → JudgeVerdict          │
                 │   │ confidence floor ≥ 0.7  │
                 │   └─────────┬───────────────┘
                 │             │
                 ▼             ▼
        ┌──────────────────────────────────────┐
        │ Aggregate per-query + global stats   │
        │ Wilson 95% CI on headline %          │
        │ source-tier breakdown                │
        │ hot pages + resolution proposals     │
        └──────────────────┬───────────────────┘
                           │
                           ▼
                  ProbeReport JSON
                           │
        ┌──────────────────┼──────────────────────┬───────────────┐
        ▼                  ▼                      ▼               ▼
   doctor (M1)         MCP (M3)             synthesize (M2)   trend (M5)
   surfaces           find_contradictions    informational     persistent
   findings           op for agents          block in prompt   tracking
```

## Severity rubric

The judge assigns severity per finding:

| Level | Rubric | Example |
|---|---|---|
| `low` | naming/format differences | "Alice Smith" vs "A. Smith" |
| `medium` | factual values that may be stale | revenue figure, headcount, valuation |
| `high` | identity / structural claims | founder/CEO/CFO role, company status |

Doctor sorts findings by severity DESC. The MCP op accepts a severity filter
so agents can fetch just the high-priority items.

## How to interpret the headline number

The probe outputs `queries_with_contradiction / queries_evaluated` with a
Wilson 95% confidence interval:

```
Queries with >=1 contradiction: 12 / 50 (24%)  Wilson CI 95%: 14–37%
```

What this says: with 95% confidence, the true rate is between 14% and 37%.
The 24% point estimate is the most-likely-value but bounded by sampling
noise. **`small_sample_note` fires when n < 30** — at that scale the CI is
too wide to act on.

Decision criteria for the bigger swing (chunk-level `revises` field):

| Wilson CI lower bound | What it says | Action |
|---|---|---|
| < 5% | Source-boost + recency-decay + curated pages handle the load | Stop here; this is the right scope |
| 5–15% | Real but bounded | Operator decides whether the cost justifies the swing |
| > 15% | Real and substantial | Plan the bigger swing in v0.34+ |

## When to act on findings

Each finding ships with a `resolution_command` field — paste-ready:

- `gbrain takes supersede <slug> --row N` — newer take should replace
  the older chunk text on the same page (intra_page kind).
- `gbrain dream --phase synthesize --slug <slug>` — compiled_truth for
  the curated entity needs an update (cross_slug curated-vs-bulk).
- `gbrain takes mark-debate <slug> --row N` — intentional disagreement
  (e.g., two opinions you want to keep both of).
- `# manual review: <a> vs <b>` — judge wasn't sure; operator decides.

Run `gbrain eval suspected-contradictions review --severity high` to
inspect findings without re-running the probe.

## Cost model

Default judge is `claude-haiku-4-5` at ~$1/Mtok in, $5/Mtok out. With
the v0.32.6 truncation at 1500 chars per pair, ~500 input + 80 output
tokens per judge call. Budget cap defaults to $5 in TTY / $1 non-TTY.

- ~$0.0006 per judge call
- ~$0.005 per query (after date pre-filter + cache hits)
- ~$0.50 per 100 queries

The persistent cache means nightly runs against the same query set
pay near-zero on re-runs (until you bump PROMPT_VERSION).

## Trust posture

- Probe never mutates the brain. Runs only read pages/takes/chunks.
  Writes go only to `eval_contradictions_runs` and `eval_contradictions_cache`.
- MCP `find_contradictions` is read-scope. NOT in the subagent allowlist —
  user-initiated only, not autonomous-action surface.
- Build-fixture script is local-only. The r

# FILE: docs/GBRAIN_SKILLPACK.md

<!-- skillpack-version: 0.7.0 -->
<!-- source: https://raw.githubusercontent.com/garrytan/gbrain/master/docs/GBRAIN_SKILLPACK.md -->
# GBrain Skillpack: Reference Architecture for AI Agents

This is a reference architecture for how a production AI agent uses gbrain as its
knowledge backbone. Based on patterns from a real deployment with 14,700+ brain
files, 40+ skills, and 20+ cron jobs running continuously.

**The memex vision, realized.** Vannevar Bush imagined a device where an individual
stores everything, mechanized so it may be consulted with exceeding speed. GBrain is
that device, except the memex builds itself. The agent detects entities, enriches
pages, creates cross-references, and maintains compiled truth automatically.

Each section below is a standalone guide. Click through to the full content.

---

## Core Patterns

The foundational read-write loop and data model.

| Guide | What It Covers |
|-------|---------------|
| [The Brain-Agent Loop](guides/brain-agent-loop.md) | The read-write cycle that makes the brain compound over time |
| [Entity Detection](guides/entity-detection.md) | Run it on every message. Capture original thinking + entity mentions |
| [The Originals Folder](guides/originals-folder.md) | Capturing WHAT YOU THINK, not just what you found |
| [Brain-First Lookup](guides/brain-first-lookup.md) | Check the brain before calling any external API |
| [Compiled Truth + Timeline](guides/compiled-truth.md) | Above the line: current synthesis. Below: append-only evidence |
| [Source Attribution](guides/source-attribution.md) | Every fact needs a citation. Format and hierarchy |

## Data Pipelines

Getting data in and keeping it current.

| Guide | What It Covers |
|-------|---------------|
| [Enrichment Pipeline](guides/enrichment-pipeline.md) | 7-step protocol, tier system (Tier 1/2/3 by importance) |
| [Meeting Ingestion](guides/meeting-ingestion.md) | Always pull complete transcript, propagate to all entity pages |
| [Content & Media Ingestion](guides/content-media.md) | YouTube, social media bundles, PDFs/documents |
| [Diligence Ingestion](guides/diligence-ingestion.md) | Data room materials: pitch decks, financial models, cap tables |
| [Deterministic Collectors](guides/deterministic-collectors.md) | Code for data, LLMs for judgment. The collector pattern |
| [Idea Capture & Originals](guides/idea-capture.md) | Depth test, originality distribution, deep cross-linking |
| [Getting Data In](integrations/README.md) | Integration recipes: voice, email, X, calendar |

## Operations

Running a production brain.

| Guide | What It Covers |
|-------|---------------|
| [Reference Cron Schedule](guides/cron-schedule.md) | 20+ recurring jobs, quiet hours, dream cycle |
| [Cron via Minions](../skills/conventions/cron-via-minions.md) | Why scheduled work runs as Minion jobs, not `agentTurn`. Auto-applied by v0.11.0 migration for built-in handlers; host-specific handlers use the plugin contract below. |
| [Plugin Handlers](guides/plugin-handlers.md) | Registering host-specific Minion handlers via code (no data-file exec surface). |
| [Minions fix](guides/minions-fix.md) | Repairing a half-migrated v0.11.0 install. |
| [Shell jobs (v0.14.0+)](guides/minions-shell-jobs.md) | Move deterministic crons (API fetch, token refresh, scrape+write) off the LLM gateway. Zero tokens per fire, ~60% gateway headroom. Follow `skills/migrations/v0.14.0.md` for the adoption playbook. |
| [Quiet Hours & Timezone](guides/quiet-hours.md) | Hold notifications during sleep, timezone-aware delivery |
| [Executive Assistant Pattern](guides/executive-assistant.md) | Email triage, meeting prep, scheduling |
| [Operational Disciplines](guides/operational-disciplines.md) | Signal detection, brain-first, sync-after-write, heartbeat, dream cycle |
| [Skill Development Cycle](guides/skill-development.md) | 5-step cycle: concept, prototype, evaluate, codify, cron |

**Subagent routing (v0.11.0+):** agents that dispatch background work should route through
`skills/conventions/subagent-routing.md` — it reads `~/.gbrain/preferences.json#minion_mode`
and branches between native subagents and Minion jobs. The v0.11.0 migration auto-injects
a marker into AGENTS.md pointing at this convention.

**Cron routing (v0.11.0+):** scheduled work goes through Minions, not OpenClaw's `agentTurn`.
See `skills/conventions/cron-via-minions.md` for the rewrite pattern. The v0.11.0 migration
auto-rewrites entries whose handler is a gbrain builtin; host-specific handlers (e.g.
`ea-inbox-sweep`) need a code-level registration per `docs/guides/plugin-handlers.md`.

## Architecture

How to structure your system.

| Guide | What It Covers |
|-------|---------------|
| [Two-Repo Architecture](guides/repo-architecture.md) | Agent repo vs brain repo, boundary rules, decision tree |
| [Sub-Agent Model Routing](guides/sub-agent-routing.md) | Which model for which task, signal detector pattern, cost optimization |
| [The Three Search Modes](guides/search-modes.md) | Keyword, hybrid, direct. When to use each |
| [Brain vs Agent Memory](guides/brain-vs-memory.md) | 3 layers: GBrain (world knowledge), agent memory, session |

## Integrations

Wiring up your life.

| Guide | What It Covers |
|-------|---------------|
| [Credential Gateway](integrations/credential-gateway.md) | ClawVisor / Hermes for Gmail, Calendar, Contacts |
| [Meeting & Call Webhooks](integrations/meeting-webhooks.md) | Circleback transcripts + Quo/OpenPhone SMS/calls |
| [Voice-to-Brain](../recipes/twilio-voice-brain.md) | Phone calls + WebRTC browser calls create brain pages. 25 production patterns: identity separation, bid system, conversation timing, proactive advisor, prompt compression, caller routing, dynamic VAD, real-time logging, belt-and-suspenders post-call |
| [Email-to-Brain](../recipes/email-to-brain.md) | Gmail messages flow into entity pages via deterministic collector |
| [X-to-Brain](../recipes/x-to-brain.md) | Twitter monitoring with deletion detection

# FILE: docs/UPGRADING_DOWNSTREAM_AGENTS.md

# Upgrading Downstream Agents

GBrain ships skills in `skills/`. Downstream agents (custom OpenClaw deployments,
agent forks of any kind) often **copy** these skill files into their own workspace and
diverge over time — adding agent-specific phases, removing irrelevant ones, tightening
language. Once that happens, gbrain can't push updates to those forks. The agent has
to apply the diffs by hand.

This doc lists the exact diffs each downstream agent needs to apply when upgrading.
Cross-reference against your fork's local skill files.

## Why this exists

`gbrain upgrade` ships the new binary. `gbrain post-upgrade [--execute --yes]` runs
the schema migrations and backfills the data. But the **skill files themselves**
that tell the agent how to behave — those are user-owned. If your `~/git/<your-agent>/workspace/skills/brain-ops/SKILL.md`
says `# Based on gbrain v0.10.0` at the top, it doesn't know about v0.12.0 features.

The agent will keep manually calling `gbrain link` after every `put_page` (now redundant —
auto-link does it), miss out on `gbrain graph-query` for relationship questions, and
not know to backfill the structured timeline.

## How to apply

1. Identify your forked skill files. Typically at `~/git/<your-agent>/workspace/skills/` or wherever your agent's skill directory lives.
2. For each skill listed below, find the matching phase/section in your fork.
3. Apply the diff (paste the new block in the indicated location).
4. Update the version banner at the top of your fork (`# Based on gbrain v0.12.0`).
5. Verify: ask the agent to write a test page and confirm the response includes
   `auto_links: { created, removed, errors }`.

Total time: ~10 minutes for all four skills.

---

## 1. brain-ops/SKILL.md

**Where:** Insert a new `### Phase 2.5` section immediately after `### Phase 2: On Every Inbound Signal`.

**Why:** Phase 2.5 declares that auto-link runs automatically. Without this, the
agent's mental model says it must call `gbrain link` after every `put_page`, which
is now redundant and can cause double-add warnings.

```markdown
### Phase 2.5: Structured Graph Updates (automatic)

Every `put_page` call automatically extracts entity references and writes them
to the graph (`links` table) with inferred relationship types. Stale links
(refs no longer in the page text) are removed in the same call. This is
"auto-link" reconciliation.

- No manual `add_link` calls needed for ordinary page writes.
- Inferred link types: `attended` (meeting -> person), `works_at`, `invested_in`,
  `founded`, `advises`, `source` (frontmatter), `mentions` (default).
- The `put_page` MCP response includes `auto_links: { created, removed, errors }`
  so the agent can verify outcomes.
- To disable: `gbrain config set auto_link false`. Default is on.
- Timeline entries with specific dates still need explicit `gbrain timeline-add`
  (or batch via `gbrain extract timeline --source db`).
```

**Also update the Iron Law section.** If your fork still says "Back-links maintained
on every brain write (Iron Law)" without qualification, append:

```markdown
**v0.12.0 update:** Auto-link satisfies the Iron Law for entity-reference links
on every `put_page`. The agent's Iron Law obligation is now: include the
entity reference in the page content (e.g., `[Alice](people/alice)`); auto-link
handles the structured row. Manual `add_link` calls are reserved for
relationships you can't express in markdown content.
```

---

## 2. meeting-ingestion/SKILL.md

**Where:** Append to the end of `### Phase 3: Attendee enrichment`.

**Why:** Eliminates redundant `gbrain link` calls per attendee (auto-link handles them
when the meeting page references attendees as `[Name](people/slug)`).

```markdown
**Note (v0.12.0):** Once the meeting page is written via `gbrain put`, the
auto-link post-hook automatically creates `attended` links from the meeting
to each attendee whose page is referenced as `[Name](people/slug)`. You don't
need to call `gbrain link` for attendees. You DO still need `gbrain timeline-add`
for dated events (auto-link only handles links, not timeline entries).
```

**Where:** In `### Phase 4: Entity propagation`, the line "Back-link from entity page
to meeting page" can be replaced with:

```markdown
4. Entity references in the meeting page body auto-create the link via auto-link.
   For incoming references on the entity page (entity page → meeting page), edit
   the entity page to mention the meeting and `put_page` it — auto-link handles
   the rest.
```

---

## 3. signal-detector/SKILL.md

**Where:** Append to the end of `### Phase 2: Entity Detection`.

**Why:** Same logic as brain-ops — eliminates manual `gbrain link` after writing
originals/ideas pages that reference people or companies.

```markdown
**Auto-link (v0.12.0):** When you write/update an originals or ideas page that
references a person or company, the auto-link post-hook on `put_page`
automatically creates the link from the new page to that entity. You don't
need to call `gbrain link` manually. Timeline entries still need explicit calls.
```

---

## 4. enrich/SKILL.md

**Where:** Replace `### Step 7: Cross-reference` with the v0.12.0 version.

**Why:** Step 7 used to be primarily about creating links between related entity
pages. With auto-link, that's automatic. Step 7 is now about content updates,
not link creation.

Old (delete):
```markdown
### Step 7: Cross-reference

- Update company pages from person enrichment (and vice versa)
- Update related project/deal pages if relevant context surfaced
- Check index files if the brain uses them
- Add back-links manually via `gbrain link` for any new entity references
```

New (paste):
```markdown
### Step 7: Cross-reference

- Update company pages from person enrichment (and vice versa)
- Update related project/deal pages if relevant context surfaced
- Check index files if the brain uses them

**Note (v0.12.0):** Links between brain pages are auto-created on every
`put_page` call (auto-link post-h

# FILE: docs/GBRAIN_RECOMMENDED_SCHEMA.md

<!-- schema-version: 0.5.0 -->
<!-- source: https://raw.githubusercontent.com/garrytan/gbrain/master/docs/GBRAIN_RECOMMENDED_SCHEMA.md -->
# Brain: The LLM-Maintained Knowledge Base

A system prompt for any AI agent that wants to build and maintain a personal knowledge base. This describes the pattern, the architecture, and the operational discipline that makes it work.

Drop this into your agent's workspace as a skill or system prompt. Your agent will build the rest.

---

## What this is

A personal intelligence system where your AI agent builds and maintains an interlinked wiki of everything you know about your world — people, companies, deals, projects, meetings, ideas — as structured, cross-referenced markdown files. The agent writes and maintains all of it. You direct, curate, and think.

This is Karpathy's LLM wiki pattern, but extended from research notes into a full operational knowledge base — one that integrates with your calendar, email, meetings, social media, and contacts to stay continuously current.

The key insight: **knowledge management has failed for 30 years because maintenance falls on humans. LLM agents change the equation — they don't get bored, don't forget to update cross-references, and can touch 50 files in one pass.** Your wiki stays alive because the cost of maintenance is near zero.

## Three Founding Principles

### 1. Every Piece of Knowledge Has a Primary Home (MECE Directories)

Every piece of knowledge passes through a decision tree and lands in exactly one directory. No duplicated pages, no ambiguity about where something goes.

This is the single most important structural decision. Without it, knowledge bases rot — the same fact lives in three places with three different versions, nobody knows which is current, and the agent (or human) stops trusting the system. MECE directories with explicit resolver rules prevent this.

Every directory has a `README.md` (the resolver) that answers two questions:
1. **What goes here** — a positive definition with a concrete test
2. **What does NOT go here** — the key distinctions from neighboring directories that the agent might confuse

The brain also has a top-level `RESOLVER.md` — a numbered decision tree the agent walks when filing anything. When two directories seem to fit, disambiguation rules break the tie. When nothing fits, the item goes in `inbox/` — which is itself a signal the schema needs to evolve.

**The agent must read the resolver before creating any new page.** This is not optional.

**Important nuance: MECE applies to directories, not to reality.** Real people and entities are multi-faceted — a political founder can also be a friend, donor, media actor, and hiring candidate. The resolver picks the *primary home* for their page (people/), but the page itself uses typed backlinks and cross-references to surface all their facets. The MECE rule prevents duplicate pages, not duplicate relationships. Cross-references are how adjacency is preserved without breaking the one-page-per-entity rule.

### 2. Compiled Truth + Timeline (Two-Layer Pages)

Every brain page has two layers, separated by a horizontal rule (`---`):

**Above the line — Compiled Truth.** Always current, always rewritten when new information arrives. Starts with a one-paragraph executive summary. If you read only this, you know the state of play. Followed by structured State fields, Open Threads (active items — removed when resolved), and See Also (cross-links).

**Below the line — Timeline.** Append-only, never rewritten. Reverse-chronological evidence log. Each entry: date, source, what happened. When an open thread gets resolved, it moves here with its resolution.

If someone asks "what's the current state?" — read above the line. If someone asks "what happened?" — read below the line. The top is the current summary. The bottom is the source log.

This is the Karpathy wiki pattern's killer feature: **the synthesis is pre-computed.** Unlike RAG, where the LLM re-derives knowledge from scratch every query, your brain has already done the work. The cross-references are already there. The contradictions have already been flagged.

### 3. Enrichment Fires on Every Signal

Every time any signal touches a person or company — meeting, email, tweet, calendar event, contact sync, conversation mention — the enrichment pipeline fires. The brain grows as a side effect of normal operations, not as a separate task you remember to do.

This is what distinguishes an operational brain from Karpathy's research wiki. He describes ingesting sources you manually add. An operational brain goes further — every pipeline (meetings, email, social media, contacts) automatically triggers enrichment on every entity it touches. You never have to remember to update someone's page. The system does it because the plumbing is wired correctly.

## Wiring It Into Your Agent

The brain must be referenced in your agent's configuration (AGENTS.md or equivalent) as a hard rule, not a suggestion. Specifically:

1. **Before creating any brain page → read RESOLVER.md.** This should be in your agent's operational rules, not buried in documentation.
2. **Before answering any question about people, companies, deals, or strategy → search the brain first.** Even if the agent thinks it knows the answer. File contents are current; the agent's memory of them goes stale.
3. **The enrich skill fires on every signal.** Every ingest pathway — meeting processing, email triage, social monitoring, contact sync — should call the enrichment pipeline when it encounters a person or company. This is wiring, not discipline. If it depends on the agent remembering, it will eventually be forgotten.
4. **Corrections are the highest-value data.** If the user corrects the agent about a person, company, deal, or decision — it gets written to the brain immediately. No batching, no deferring.

The chain of authority: **Agent config (AGENTS.md) says "read RESOLVER.md" → RESOLVER.md is the decision tree → eac

# FILE: docs/takes-vs-facts.md

# Takes vs Facts — Architectural Distinction

gbrain has two epistemological storage layers that serve different purposes.
**Never conflate them.**

## Takes (cold storage — `takes` table)

The epistemological layer. WHO believes WHAT, with confidence weight and time.

- **Source:** Extracted from brain pages (markdown) by LLM analysis
- **Scope:** Multi-holder — captures beliefs from *any* speaker, not just the brain owner
- **Kinds:** `take` (opinion), `fact` (verifiable), `bet` (prediction), `hunch` (intuition)
- **Lifecycle:** Cold storage, retrospective. Updated when pages change or re-extraction runs.
- **Scale:** 100K+ rows across thousands of holders in a mature brain

**Example takes:**
- `holder=people/garry-tan kind=bet` "AI will replace 50% of coding by 2030" (w=0.75)
- `holder=people/jared-friedman kind=take` "Momo has strong retention" (w=0.80)
- `holder=world kind=fact` "Clipboard raised $100M Series C" (w=1.0)
- `holder=brain kind=hunch` "Garry has a hero/rescuer pattern" (w=0.70)

**Query surface:** `gbrain takes list`, `gbrain takes search`, `gbrain think`

## Facts (hot memory — `facts` table, v0.31)

Personal knowledge from the brain owner's conversations. Real-time capture.

- **Source:** Extracted per-turn from conversation by the facts hook (Haiku)
- **Scope:** Single-user — only the brain owner's stated knowledge
- **Kinds:** `event`, `preference`, `commitment`, `belief`, `fact`
- **Lifecycle:** Hot storage, real-time. Captured as conversations happen.
- **Bridge:** Dream cycle `consolidate` phase promotes hot facts → cold takes nightly

**Example facts:**
- `kind=event` "I have a meeting with Brian tomorrow"
- `kind=preference` "I don't drink coffee"
- `kind=commitment` "We decided on nesting custody"
- `kind=belief` "I think the market is overheated"

**Query surface:** `gbrain recall`, MCP `_meta.brain_hot_memory`

## The Category Error

**Never dump takes into the facts table.** Takes include other people's attributed
beliefs (Jared's assessment of a company, PG's view on schools, a founder's
revenue claims). These are NOT the brain owner's personal facts.

**Never dump facts into the takes table without transformation.** Facts are
scoped to what the owner said in conversation. They become takes only through
the dream cycle's consolidate phase, which adds proper attribution, deduplication,
and temporal reasoning.

## The Bridge

The dream cycle's `consolidate` phase (v0.31) is the one-way bridge:

```
hot facts → [dream consolidate] → cold takes
```

Facts flow in ONE direction. The consolidate phase:
1. Groups related facts by entity
2. Deduplicates against existing takes
3. Promotes durable facts to takes with proper holder/weight
4. Marks consolidated facts with `consolidated_at` + `consolidated_into`

## Production Extraction Data (2026-05-10)

First full takes extraction run on a ~100K-page brain:
- **Model:** Azure GPT-5.5 (ties Opus quality at 1/8th cost — $0.033 vs $0.260/page)
- **Result:** 100,720 takes from 28,256 on-disk pages, $361.49, 83 errors (0.3%)
- **Breakdown:** 70,960 takes / 24,342 facts / 2,875 bets / 2,649 hunches
- **Holders:** 6,239 unique holders
- **Cross-modal eval:** 6.8/10 overall (GPT-5.5 + Opus 4.6 scored independently)

### Eval Dimensions

| Dimension | Score | Notes |
|-----------|-------|-------|
| Accuracy | 7.5 | Claims faithfully represent sources |
| Attribution | 6.5 | Holder/subject confusion was #1 issue |
| Weight calibration | 7.0 | Good range usage, some false precision |
| Kind classification | 6.5 | Occasional fact/take misclassification |
| Signal density | 6.5 | Some trivial extractions pass through |

### Key Learnings for Extraction Prompts

1. **Holder ≠ subject.** "Garry has a hero/rescuer pattern" → holder=brain, NOT people/garry-tan
2. **Atomic claims.** Split compound claims into separate rows
3. **Amplification ≠ endorsement.** Retweet-only → max weight 0.55
4. **Self-reported ≠ verified.** "Reports 7 figures" → holder=person, weight=0.75, NOT world/1.0
5. **No false precision.** Use 0.05 increments (0.35, 0.55, 0.75), not 0.74 or 0.82
6. **"So what" test.** Skip Twitter handles, follower counts, obvious metadata


# FILE: docs/GBRAIN_V0.md

# GBrain v0: Postgres-Native Personal Knowledge Brain

## What this is

GBrain is a compiled intelligence system. Not a note-taking app. Not "chat with your notes."

Every page is an intelligence assessment. Above the line: compiled truth (your current best understanding, rewritten when evidence changes). Below the line: timeline (append-only evidence trail). AI agents maintain the brain. MCP clients query it. The intelligence lives in fat markdown skills, not application code.

The core insight: personal knowledge at scale is an intelligence problem, not a storage problem.

## Why it exists

A 7,471-file / 2.3GB markdown wiki is choking git. Git doesn't scale past ~5K files for wiki-style use. The compiled truth + timeline model (Karpathy-style knowledge pages) is right, but it needs a real database underneath.

There's already a production-grade RAG system (Ruby on Rails, Postgres + pgvector) with 3-tier chunking, hybrid search with RRF, multi-query expansion, and 4-layer dedup. GBrain ports these proven patterns to a standalone Bun + TypeScript tool.

## The knowledge model

```
+--------------------------------------------------+
|  Page: concepts/do-things-that-dont-scale         |
|                                                   |
|  --- frontmatter (YAML) ---                       |
|  type: concept                                    |
|  tags: [startups, growth, pg-essay]               |
|                                                   |
|  === COMPILED TRUTH ===                           |
|  Current best understanding.                      |
|  Rewritten on new evidence.                       |
|  This is the "what we know now" section.          |
|                                                   |
|  ---                                              |
|                                                   |
|  === TIMELINE ===                                 |
|  Append-only evidence trail.                      |
|  - 2013-07-01: Published on paulgraham.com        |
|  - 2024-11-15: Referenced in batch kickoff talk   |
|  Never edited, only appended.                     |
+--------------------------------------------------+
          |                    |
          v                    v
  [Semantic chunks]     [Recursive chunks]
  (best quality for     (predictable format
   compiled truth)       for timeline)
          |                    |
          v                    v
     [Embeddings: text-embedding-3-large, 1536 dims]
          |
          v
  [HNSW index + tsvector + pg_trgm]
          |
          v
  [Hybrid search: vector + keyword + RRF fusion]
```

## Architecture decisions

### v0 stack

| Layer | Choice | Why |
|-------|--------|-----|
| Database | Postgres + pgvector | Proven RAG patterns, production-tested. World-class hybrid search. |
| Hosting | Supabase Pro ($25/mo) | Zero-ops. Managed Postgres, pgvector, connection pooling. 8GB storage. |
| Runtime | Bun + TypeScript | Consistent with GStack ecosystem. Fast. Compiles to single binary. |
| Embeddings | OpenAI text-embedding-3-large | 1536 dims (reduced from 3072 via dimensions API). ~$0.13/1M tokens. |
| LLM (chunking/expansion) | Claude Haiku | Cheapest model for topic boundary detection and query expansion. |
| Background jobs | Trigger.dev | Serverless. Embed backfill, stale detection, orphan audit, tag consistency. |
| Distribution | npm package + compiled binary + MCP server | Library for OpenClaw, CLI for humans, MCP for agents. |

### What we chose and why

**Postgres over SQLite.** We have 3+ years of proven RAG patterns running on Postgres. tsvector for full-text search, pgvector HNSW for semantic search, pg_trgm for fuzzy slug matching. Porting these to SQLite would mean reimplementing search from scratch. SQLite is a future pluggable engine for lightweight open source users (see `docs/ENGINES.md`).

**Supabase over self-hosted.** Zero maintenance. The brain should be infrastructure that AI agents use, not something you administer. Free tier has pgvector but only 500MB (not enough for 7K+ pages with embeddings, which need ~750MB). Pro tier at $25/mo gives 8GB. No Docker, no self-hosted Postgres in v1.

**Full port over minimal viable.** The patterns are proven. The port is mechanical. Shipping the full 3-tier chunking + hybrid search + 4-layer dedup means world-class RAG from day one. "We'll add that later" means rebuilding everything later.

**Library-first distribution.** gbrain is an npm package. OpenClaw installs it as a dependency (`bun add gbrain`), imports the engine directly. Zero-overhead function calls, shared connection pool, TypeScript types. The CLI and MCP server are thin wrappers over the same engine.

**Trigger-based tsvector (not generated column).** To include timeline_entries content in full-text search, the tsvector needs to span multiple tables. Generated columns can't do cross-table references. A trigger on pages + timeline_entries updates the search_vector.

**Auto-embed during import.** No separate embed step. `gbrain import` chunks and embeds in one pass. Progress bar shows status. `--no-embed` flag for users who want to defer. `embedded_at` column enables `gbrain embed --stale` for backfill.

## Distribution model

```
+-------------------+     +-------------------+     +-------------------+
|   npm package     |     |  Compiled binary  |     |   MCP server      |
|   (library)       |     |  (CLI)            |     |   (stdio)         |
+-------------------+     +-------------------+     +-------------------+
|                   |     |                   |     |                   |
| bun add gbrain    |     | GitHub Releases   |     | gbrain serve      |
| import { Postgres |     | npx gbrain        |     | in mcp.json       |
|   Engine }        |     |                   |     |                   |
|                   |     |                   |     |                   |
| WHO: OpenClaw,    |     | WHO: Humans       |     | WHO: Claude Code,  |
| AlphaClaw        

# FILE: docs/ENGINES.md

# Pluggable Engine Architecture

## The idea

Every GBrain operation goes through `BrainEngine`. The engine is the contract between "what the brain can do" and "how it's stored." Swap the engine, keep everything else.

v0 shipped `PostgresEngine` backed by Supabase. v0.7 adds `PGLiteEngine` -- embedded Postgres 17.5 via WASM (@electric-sql/pglite), zero-config default. The interface is designed so a `DuckDBEngine`, `TursoEngine`, or any custom backend could slot in without touching the CLI, MCP server, skills, or any consumer code.

## Why this matters

Different users have different constraints:

| User | Needs | Best engine |
|------|-------|-------------|
| Getting started | Zero-config, no accounts, no server | PGLiteEngine (default since v0.7) |
| Power user (you) | World-class search, 7K+ pages, zero-ops | PostgresEngine + Supabase |
| Open source hacker | Single file, no server, git-friendly | PGLiteEngine |
| Team/enterprise | Multi-user, RLS, audit trail | PostgresEngine + self-hosted |
| Researcher | Analytics, bulk exports, embeddings | DuckDBEngine (someday) |
| Edge/mobile | Offline-first, sync later | PGLiteEngine + sync (someday) |

The engine interface means we don't have to choose. PGLite is the zero-friction default. Supabase is the production scale path. `gbrain migrate --to supabase/pglite` moves between them.

## The interface

```typescript
// src/core/engine.ts

export interface BrainEngine {
  // Lifecycle
  connect(config: EngineConfig): Promise<void>;
  disconnect(): Promise<void>;
  initSchema(): Promise<void>;
  transaction<T>(fn: (engine: BrainEngine) => Promise<T>): Promise<T>;

  // Pages CRUD
  getPage(slug: string): Promise<Page | null>;
  putPage(slug: string, page: PageInput): Promise<Page>;
  deletePage(slug: string): Promise<void>;
  listPages(filters: PageFilters): Promise<Page[]>;

  // Search
  searchKeyword(query: string, opts?: SearchOpts): Promise<SearchResult[]>;
  searchVector(embedding: Float32Array, opts?: SearchOpts): Promise<SearchResult[]>;

  // Chunks
  upsertChunks(slug: string, chunks: ChunkInput[]): Promise<void>;
  getChunks(slug: string): Promise<Chunk[]>;

  // Links
  addLink(from: string, to: string, context?: string, linkType?: string): Promise<void>;
  removeLink(from: string, to: string): Promise<void>;
  getLinks(slug: string): Promise<Link[]>;
  getBacklinks(slug: string): Promise<Link[]>;
  traverseGraph(slug: string, depth?: number): Promise<GraphNode[]>;

  // Tags
  addTag(slug: string, tag: string): Promise<void>;
  removeTag(slug: string, tag: string): Promise<void>;
  getTags(slug: string): Promise<string[]>;

  // Timeline
  addTimelineEntry(slug: string, entry: TimelineInput): Promise<void>;
  getTimeline(slug: string, opts?: TimelineOpts): Promise<TimelineEntry[]>;

  // Raw data
  putRawData(slug: string, source: string, data: object): Promise<void>;
  getRawData(slug: string, source?: string): Promise<RawData[]>;

  // Versions
  createVersion(slug: string): Promise<PageVersion>;
  getVersions(slug: string): Promise<PageVersion[]>;
  revertToVersion(slug: string, versionId: number): Promise<void>;

  // Stats + health
  getStats(): Promise<BrainStats>;
  getHealth(): Promise<BrainHealth>;

  // Ingest log
  logIngest(entry: IngestLogInput): Promise<void>;
  getIngestLog(opts?: IngestLogOpts): Promise<IngestLogEntry[]>;

  // Config
  getConfig(key: string): Promise<string | null>;
  setConfig(key: string, value: string): Promise<void>;

  // Migration + advanced (added v0.7)
  runMigration(sql: string): Promise<void>;
  getChunksWithEmbeddings(slug: string): Promise<ChunkWithEmbedding[]>;
}
```

### Key design choices

**Slug-based API, not ID-based.** Every method takes slugs, not numeric IDs. The engine resolves slugs to IDs internally. This keeps the interface portable... slugs are strings, IDs are database-specific.

**Embedding is NOT in the engine.** The engine stores embeddings and searches by vector, but it doesn't generate embeddings. `src/core/embedding.ts` handles that. This is intentional: embedding is an external API call (OpenAI), not a storage concern. All engines share the same embedding service.

**Chunking is NOT in the engine.** Same logic. `src/core/chunkers/` handles chunking. The engine stores and retrieves chunks. All engines share the same chunkers.

**Search returns `SearchResult[]`, not raw rows.** The engine is responsible for its own search implementation (tsvector vs FTS5, pgvector vs sqlite-vss) but must return a uniform result type. RRF fusion and dedup happen above the engine, in `src/core/search/hybrid.ts`.

**`traverseGraph` exists but is engine-specific.** Postgres uses recursive CTEs. SQLite would use a loop with depth tracking. The interface is the same: give me a slug and max depth, return the graph.

## How search works across engines

```
                        +-------------------+
                        |  hybrid.ts        |
                        |  (RRF fusion +    |
                        |   dedup, shared)  |
                        +--------+----------+
                                 |
                    +------------+------------+
                    |                         |
           +--------v--------+       +--------v--------+
           | engine.search   |       | engine.search   |
           |   Keyword()     |       |   Vector()      |
           +-----------------+       +-----------------+
                    |                         |
        +-----------+-----------+   +---------+---------+
        |                       |   |                   |
+-------v-------+  +-------v---+   +-------v---+  +----v--------+
| Postgres:     |  | PGLite:   |   | Postgres: |  | PGLite:     |
| tsvector +    |  | tsvector +|   | pgvector  |  | pgvector    |
| ts_rank +     |  | ts_rank   |   | HNSW      |  | HNSW        |
| websearch_to_ |  | (same SQL)|   | cosine    |  | cosine      |
| tsquery       |  |           |   |           |  | (same SQL)  |
+------

# FILE: docs/embedding-migrations.md

# Switching embedding models or dimensions on an existing brain

GBrain stores embeddings in a fixed-dimension `vector(N)` column on
`content_chunks`. If you switch to a model with a different dimension
(e.g. `text-embedding-3-large` 1536 → `voyage-multilingual-large-2` 2048,
or back to a smaller model like `nomic-embed-text` 768), the on-disk
column type doesn't change automatically.

`gbrain init` and `gbrain doctor` both detect and refuse to silently
proceed in this case. This doc is the recipe they point at.

## Why we don't do this automatically

Switching dimensions requires:

1. Dropping the HNSW vector index (pgvector won't survive an `ALTER COLUMN TYPE`).
2. Altering the column type.
3. Wiping every existing embedding (the old vectors are unusable in the new space).
4. Re-embedding the entire corpus (can take hours on a 50K-page brain and costs $1-100 in API calls depending on model).
5. Conditionally recreating the index (HNSW supports up to 2000 dimensions per pgvector; above that you must use exact scans).

That's not an upgrade-time auto-run. It's a deliberate, expensive
operation. Run it when you've decided you actually want the new model.

## Recipe — manual `psql` against your brain

Replace `<NEW_DIMS>` with your target dimension count.

```sql
BEGIN;

-- 1. Drop the HNSW index. It can't survive the column type change.
DROP INDEX IF EXISTS idx_chunks_embedding;

-- 2. Alter the column type. (You can DROP COLUMN + ADD COLUMN instead
--    if the existing data is already gone — same end state.)
ALTER TABLE content_chunks ALTER COLUMN embedding TYPE vector(<NEW_DIMS>);

-- 3. Clear stale embeddings so they don't survive into the new space.
--    Either truncate (faster, drops all chunks) or null out (preserves
--    chunk text so re-embed regenerates without re-chunking):
UPDATE content_chunks SET embedding = NULL, embedded_at = NULL;

-- 4. Recreate the HNSW index ONLY IF dims <= 2000. Above that, leave it
--    indexless and rely on exact scans (gbrain searchVector handles this
--    automatically — search just gets slower, not broken).
-- For dims <= 2000 (e.g. 1024, 1536, 768):
CREATE INDEX IF NOT EXISTS idx_chunks_embedding
  ON content_chunks USING hnsw (embedding vector_cosine_ops);
-- For dims > 2000 (e.g. 2048 Voyage 4 Large): skip step 4.

COMMIT;
```

Then update gbrain's config so it knows the new dim:

```bash
gbrain config set embedding_model <model>
gbrain config set embedding_dimensions <NEW_DIMS>
```

And re-embed the corpus:

```bash
gbrain embed --stale
```

## PGLite (local brain)

Same recipe, but you connect to the embedded database differently:

```bash
gbrain config get database_url   # confirm engine: pglite
# Open a psql-equivalent — for PGLite, the easiest path is to write a small
# script that imports PGLiteEngine and runs the SQL via engine.executeRaw.
# Or migrate to Postgres temporarily (gbrain migrate --to supabase) if you
# want a real psql connection.
```

For most PGLite users the simpler path is to **wipe and re-init** if your
corpus is small enough that re-syncing is faster than hand-crafting the
migration:

```bash
mv ~/.gbrain/brain.pglite ~/.gbrain/brain.pglite.bak
gbrain init --pglite --embedding-dimensions <NEW_DIMS>
gbrain sync   # re-imports your brain repo from disk
```

## Verify

After the recipe lands, `gbrain doctor --fast` should report green and
`gbrain doctor` (full) should say check 8b passes:

```
✓ embedding_provider     dim parity: config 768 / column vector(768) / live probe 768
```

If it doesn't, file an issue with the doctor output and the SQL you ran.

## v0.29+ plans

`gbrain migrate-embedding-dim --to <N>` is a tracked TODO. It will run
the recipe above with progress reporting + an explicit confirmation
gate. Until that lands, this manual recipe is the canonical path.

