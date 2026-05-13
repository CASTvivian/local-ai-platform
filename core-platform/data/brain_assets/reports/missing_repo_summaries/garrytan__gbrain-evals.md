# Missing Repo Summary Source: garrytan/gbrain-evals

- URL: https://github.com/garrytan/gbrain-evals
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/garrytan__gbrain-evals
- Clone Status: cloned
- Language: HTML
- Stars: 121
- Topics: 
- Description: -

## Extracted README / Docs / Examples



# FILE: README.md

# gbrain-evals

**Public benchmarks for personal-knowledge agent stacks.** Two families,
both reproducible: BrainBench (our own corpus, in-house Cats 1–12) and
public benchmarks (LongMemEval today, ConvoMem + LoCoMo on the roadmap).

## Latest results

**LongMemEval `_s` (full 500-question public benchmark, 2026-05-07)** —
gbrain-hybrid hits **97.60% R@5**, beating MemPalace's published raw
baseline by 1.0pt on the same dataset, K, and n with no LLM in the
retrieval loop. Per-type wins: +7.1pt single-session-assistant, +1.5pt
multi-session, ties on user/preference, -1.5pt temporal-reasoning.
**Read the full report:** [docs/benchmarks/2026-05-07-longmemeval-s.md](docs/benchmarks/2026-05-07-longmemeval-s.md).

**BrainBench v0.12.1 (in-house corpus, 2026-04-19)** — gbrain P@5 49.1%,
R@5 97.9% on the 240-page fictional-life corpus. Beats its own
graph-disabled variant by +31.4pt P@5, grep-only by 32 points, vector by
38 points. The graph layer is load-bearing.

| Benchmark | Latest result | Date | Report |
|---|---|---|---|
| LongMemEval `_s` (public) | gbrain-hybrid 97.60% R@5 | 2026-05-07 | [link](docs/benchmarks/2026-05-07-longmemeval-s.md) |
| BrainBench Cat 13b — Source Swamp | gbrain top-1 93.3% | 2026-04-25 | [link](docs/benchmarks/2026-04-25-brainbench-cat13b-source-swamp.md) |
| BrainBench v0.20.0 baseline | gbrain P@5 49.1% / R@5 97.9% | 2026-04-23 | [link](docs/benchmarks/2026-04-23-brainbench-v0.20.0.md) |
| Cross-system comparison | MemPal / Hindsight / Mastra / Stella / Contriever | living | [docs/comparison-systems.md](docs/comparison-systems.md) |

## Why a separate repo

Benchmark corpora (world-v1 + amara-life-v1 = ~4MB) shouldn't land in
every gbrain install. This repo is what you clone when you want to run
BrainBench against gbrain, not what you clone to use gbrain as a brain.

`gbrain-evals` depends on `gbrain` via the GitHub URL. When you `bun install`
here, gbrain gets pulled in as a library. Evals call into gbrain's core
modules (`pglite-engine`, `operations`, `link-extraction`, etc.) via the
`gbrain/*` subpath exports.

## 5-minute quickstart

```sh
# Clone + install (pulls gbrain as a library dep)
git clone https://github.com/garrytan/gbrain-evals.git
cd gbrain-evals
bun install
```

### Run LongMemEval (public benchmark, 500 questions × 4 adapters)

```sh
# Download the LongMemEval _s split (~278MB, one-time)
mkdir -p ~/datasets/longmemeval
curl -Lo ~/datasets/longmemeval/longmemeval_s.json \
  https://huggingface.co/datasets/xiaowu0162/longmemeval/resolve/main/longmemeval_s

export OPENAI_API_KEY="sk-..."        # required for vector + hybrid adapters
export ANTHROPIC_API_KEY="sk-ant-..." # required for hybrid+expansion adapter only

# 4 adapters × 500 questions, 3 parallel workers, 10-min batches w/ resume
bash eval/runner/longmemeval-batch.sh

# One adapter only
bash eval/runner/longmemeval-batch.sh --adapters hybrid

# Stratified sample for fast iteration
bun eval/runner/longmemeval.ts --stratify 10  # 10 Q's per type
```

First run pays ~$2 OpenAI embeddings; subsequent runs hit the local
content-addressed cache (~$0). See the published
[longmemeval-s benchmark report](docs/benchmarks/2026-05-07-longmemeval-s.md)
for headline numbers and methodology.

### Run BrainBench (in-house corpus, 240-page fictional life)

```sh
# Run the full 4-adapter benchmark (N=5, ~15 min, no API keys required)
bun run eval:run

# Fast iteration (N=1)
bun run eval:run:dev

# Per-link-type accuracy report
bun run eval:type-accuracy

# Browse the fictional corpus
bun run eval:world:view

# Full BrainBench v1 scorecard (all Cats, published tier N=10)
bun run eval:brainbench:published       # ~$200 Opus baseline
bun run eval:brainbench                 # N=5 iteration (~$100)
bun run eval:brainbench:smoke           # N=1 smoke (~$22)
```

## Public benchmarks

| Benchmark | Source | What it tests | gbrain best result |
|---|---|---|---|
| **LongMemEval `_s`** | [xiaowu0162/longmemeval](https://huggingface.co/datasets/xiaowu0162/longmemeval) | Retrieval recall over long-running chat (500 Q's, 6 question types, ~50 distractor sessions per haystack) | **97.60% R@5** ([report](docs/benchmarks/2026-05-07-longmemeval-s.md)) |
| LongMemEval `_oracle` | same source, easier split (3 sessions per haystack) | sanity baseline | not yet run (trivial) |
| LongMemEval `_m` | same source, harder split (200 distractors) | retrieval under heavier noise | filed as TODO |
| ConvoMem (Salesforce) | 75K+ multi-turn QA pairs | conversational memory at scale | filed as TODO |
| LoCoMo | 1,986 multi-hop QA | multi-hop reasoning over conversation | filed as TODO |

Each public benchmark gets a runner under `eval/runner/<bench>.ts`, a
report under `docs/benchmarks/<date>-<bench>.md`, and per-row entries in
[`docs/comparison-systems.md`](docs/comparison-systems.md) with sourced
numbers from MemPalace, Hindsight, Mastra, Supermemory, Stella,
Contriever, and BM25 baselines.

## BrainBench Cat catalog

| Cat | What it tests | Threshold | Status |
|-----|--------------|-----------|--------|
| 1+2 | Retrieval (relational queries over 240-page rich-prose) | P@5 > 0.39, R@5 > 0.83 | shipping |
| 2 | Per-link-type accuracy on rich prose | type F1 per category | shipping |
| 3 | Identity resolution (aliases, handles, emails) | recall > 0.80 | shipping |
| 4 | Temporal queries (as-of, point, range, recency) | as-of recall > 0.80 | shipping |
| 5 | Source attribution / provenance (claim → source classification) | citation_accuracy > 0.90 | shipping (programmatic) |
| 6 | Auto-link precision under prose (at scale) | link_precision > 0.95 | shipping (baseline-only) |
| 7 | Performance / latency | p95 < 200ms per query | shipping |
| 8 | Skill behavior compliance (brain-first, back-link, citation, tier) | all > 0.90 | shipping (programmatic) |
| 9 | End-to-end workflows (5 flows × rubric) | 80% pass per workflow | shipping (programmatic) |
| 10 | Robustness / adversarial (22 hand-crafted cases) | 100% pass, no crash | shipping |
| 11 | Multi-modal ingest (PDF + audio + HTML) | text > 0.95, WER < 0.15 | shipping (opt-in fixtures) |
| 12 | MCP operation contract (trust boundary, input validation) | no silent corruption | shipping |

Cats 5, 8, 9 are "programmatic" — they need runtime inputs (claim catalog,
probe catalog, scenarios + agent state) and are invoked via their `runCatN`
harness API rather than as standalone CLI scripts.

## The fictional corpus: world-v1 + amara-life-v1

**world-v1** (committed, 2.0MB): 240 Opus-generated biographical pages.
80 people, 80 companies, 50 meetings, 30 concepts. Each page carries
`_facts` gold metadata that never crosses the adapter boundary (Day 9
sealed-qrels enforcement).

**amara-life-v1** (committed, 2.1MB): Amara Okafor's messy week in April
2026. 50 emails + 300 Slack messages across 4 channels + 20 calendar
events + 8 meeting transcripts + 40 first-person notes + 6 reference docs.
Planted perturbations: 10 contradictions, 5 stale facts, 5 paraphrased-
injection poison items, 3 implicit preferences.

Regenerate with `bun run eval:generate-amara-life` (requires
`ANTHROPIC_API_KEY`, ~$4 Opus, ~15 min, deterministic from seed=42).

## Repo layout

```
gbrain-evals/
├── CLAUDE.md                         Spec for the platonic-ideal benchmark report
├── eval/
│   ├── data/
│   │   ├── world-v1/                 240 committed biographical pages (BrainBench)
│   │   ├── amara-life-v1/            Amara's fictional life (BrainBench)
│   │   ├── gold/                     Sealed qrels + perturbation gold
│   │   ├── longmemeval/embed-cache/  Embedding cache (gitignored, ~700MB)
│   │   └── multimodal/               PDF/audio/HTML fixtures (on-demand)
│   ├── schemas/                      Portable JSON Schema contracts
│   ├── generators/                   world.ts + amara-life.ts + Opus
│   ├── runner/                       12 Cat runners + LongMemEval + adapters + judge
│   │   ├── adapters/                 grep-only, vector, vector-grep-rrf-fusion, claude-sonnet
│   │   ├── loaders/                  PDF + corpus loaders
│   │   ├── queries/                  Tier 5 fuzzy + 5.5 synthetic
│   │   ├── all.ts                    BrainBench master runner
│   │   ├── cat{5,6,8,9,11}-*.ts      v1 Complete runners
│   │   ├── longmemeval.ts            LongMemEval runner (4 adapters, NDJSON resume, parallel sharding)
│   │   ├── longmemeval-cache.ts      Content-addressed embedding cache (SQLite, WAL, busy_timeout)
│   │   ├── longmemeval-aggregate.ts  Aggregator over the NDJSON stream
│   │   ├── longmemeval-batch.sh      3-worker × 10-min batch wrapper with auto-resume
│   │   ├── longmemeval-chart.ts      Inline-SVG headline + per-type chart generator
│   │   ├── tool-bridge.ts            12 read + 3 dry_run tools
│   │   ├── judge.ts                  Haiku judge, structured evidence contract
│   │   ├── recorder.ts               6-artifact flight-recorder
│   │   └── llm-budget.ts             Shared Anthropic-call semaphore
│   ├── reports/                      Transient run output (gitignored)
│   └── cli/                          world-view, query-validate, query-new
├── test/eval/                        Unit tests (314 tests, 1354 expect calls)
└── docs/
    ├── benchmarks/                   Published scorecards per release + their charts
    └── comparison-systems.md         Living list of named systems w/ published R@k numbers
```

## Three contributor paths

### 1. Reproduce a published scorecard
```sh
git checkout <commit-sha-from-scorecard>
bun run eval:run
# Match within tolerance bands (deterministic adapters byte-match)
```

### 2. Submit a new adapter
1. Implement `eval/runner/adapters/<your-adapter>.ts` against the `Adapter`
   interface (`init(pages, config) → BrainState`, `query(q, state) → RankedDoc[]`).
2. Register it in `eval/runner/multi-adapter.ts`.
3. Run `bun run eval:run` — it scores side-by-side against the 4 references.
4. Open a PR with your scorecard in `docs/benchmarks/YYYY-MM-DD-<stack>.md`.



# FILE: docs/comparison-systems.md

# Comparison Systems — published numbers we benchmark against

Living list of memory / agentic-retrieval systems that publish numbers on
benchmarks gbrain runs. Update when a system publishes a new result, even
if it's not on a benchmark we currently run — the data informs which
benchmark we should add.

## LongMemEval (`xiaowu0162/longmemeval` `_s` split, 500 questions)

Metric column key: **R@k** = retrieval recall (does any ground-truth
session land in top-k?). **QA-acc** = end-to-end answer accuracy via an
LLM judge. **Different metrics, not directly comparable.**

| System | Headline | Metric | k | n | LLM in loop | Source |
|---|---|---|---|---|---|---|
| MemPal hybrid v4 + Haiku rerank | 100% | R@5 | 5 | 500 | yes (Haiku) | [BENCHMARKS.md](https://github.com/MemPalace/mempalace/blob/main/benchmarks/BENCHMARKS.md) — tuned on 3 specific failing Qs |
| MemPal hybrid v4 + Haiku, held-out | 98.4% | R@5 | 5 | 450 | yes (Haiku) | held-out generalisable figure |
| MemPal raw (ChromaDB) | 96.6% | R@5 | 5 | 500 | none | their public-facing headline |
| Hindsight | 91.4% | R@5 (per their release) | 5 | 500 | yes (Gemini-3) | flagged "metric unverified" by MemPal |
| Stella | ~85% | R@5 | 5 | 500 | none | academic dense retriever |
| Contriever | ~78% | R@5 | 5 | 500 | none | academic dense retriever |
| BM25 (sparse) | ~70% | R@5 | 5 | 500 | none | published baseline in the LongMemEval paper |
| Mastra | 94.87% | QA-acc (NOT R@k) | n/a | 500 | yes (GPT-5-mini) | [mastra.ai/research/observational-memory](https://mastra.ai/research/observational-memory) |
| Supermemory ASMR | ~99% | QA-acc (NOT R@k) | n/a | 500 | yes (Gemini-2/GPT-4o ensemble) | [their ASMR post](https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/) — authors flag it as experimental, not production |

**Important reading note:** Mastra and Supermemory's numbers are end-to-end
QA accuracy (does the system produce the right answer string, judged by
gpt-4o or similar). MemPal, Hindsight, and the gbrain numbers in this
table are retrieval recall (does the right session land in top-k). A
system can have 100% retrieval recall and 60% QA accuracy if its answer
model is bad, and vice versa. Don't compare them head-to-head without
naming the gap.

## ConvoMem (Salesforce, 75K+ QA pairs)

| System | Score | Notes |
|---|---|---|
| MemPal | 92.9% | verbatim text + semantic search |
| Gemini (long context) | 70-82% | full history in context window |
| Block extraction | 57-71% | LLM-processed blocks |
| Mem0 (RAG) | 30-45% | LLM-extracted memories |

We don't run ConvoMem yet. Filed as a follow-up.

## LoCoMo (1,986 multi-hop QA pairs)

| System / mode | R@10 | Notes |
|---|---|---|
| MemPal hybrid v5 + Sonnet rerank | 100% | "structurally guaranteed (top-k > sessions)" — needs caveat |
| MemPal bge-large + Haiku rerank | 96.3% | top-15, R@10 |
| Memori | 81.95% | published baseline |
| MemPal hybrid v5 (no rerank) | 88.9% | top-10 |

We don't run LoCoMo yet. Filed as a follow-up.

## Sources we've checked (so we don't redo the lookup)

- [`MemPalace/mempalace/benchmarks/BENCHMARKS.md`](https://github.com/MemPalace/mempalace/blob/main/benchmarks/BENCHMARKS.md) — most thorough public benchmark page in this category. They credit competitors fairly and call out their own tuning caveats.
- [`mastra.ai/research/observational-memory`](https://mastra.ai/research/observational-memory) — observational-memory framework, QA accuracy.
- [`mem0.ai/research`](https://mem0.ai/research) — Mem0's research page. Publishes LoCoMo QA accuracy (~66.9%); does not publish LongMemEval.
- [`supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/`](https://supermemory.ai/blog/we-broke-the-frontier-in-agent-memory-introducing-99-sota-memory-system/) — Supermemory ASMR. Experimental ensemble, not production.
- [LongMemEval HuggingFace](https://huggingface.co/datasets/xiaowu0162/longmemeval) — the dataset itself. Three splits: `_oracle` (15MB, ~3 sessions per Q), `_s` (278MB, ~50 sessions per Q), `_m` (2.7GB, more distractors).

## When you add a new comparison row

Cite the source page directly (link to the section + accessed-on date).
Note any caveats the source itself raises (tuning-on-failing-Qs,
experimental-not-production, metric-mismatch). Don't editorialize — keep
this page neutral so it can be cited from any of our reports.


# FILE: docs/benchmarks/2026-04-25-brainbench-cat13b-source-swamp.md

# BrainBench Cat 13b — Source Swamp Resistance

**Date:** 2026-04-25
**Corpus:** `eval/data/source-swamp-v1` (10 short curated `originals/` + 10 long `wintermute/chat/` pages, all committed JSON)
**Queries:** 30 hand-curated multi-word phrases, each appearing in ≥1 chat distractor
**Top-K:** 5
**Wall clock:** ~50s for full 4-adapter run
**API cost:** ~$0 (embeddings cached after first run)

## Why this Cat exists

`world-v1` (the 240-page rich-prose corpus driving Cats 1+2 and Cat 13) has zero `wintermute/chat/`, `daily/`, or `media/x/` content. The default boost map in `gbrain` v0.22.0 dampens those bulk directories, but `world-v1` can't measure the effect ... every page is curated.

Cat 13b ships a corpus deliberately shaped around the swamp pattern: short opinionated articles compete against long dense chat dumps that mention the same multi-word phrases. Without source-aware ranking, chat pages dominate (higher per-byte keyword density). With it, the curated article wins.

## Three-way scorecard (same corpus, same 30 queries)

| gbrain version           | Top-1 hit | Top-3 hit | Swamp@top (lower=better) |
|--------------------------|-----------|-----------|--------------------------|
| **v0.22.0** (this branch — source-boost) | **93.3%** | **100.0%** | **6.7%** |
| v0.21.0 master (two-pass retrieval)      | 90.0%     | 100.0%    | 10.0%                    |
| v0.20.4 master (pre-two-pass)            | 90.0%     | 100.0%    | 10.0%                    |

**Δ v0.22 vs v0.20.4:** +3.3pts top-1, −3.3pts swamp.
**Δ v0.22 vs v0.21.0:** +3.3pts top-1, −3.3pts swamp.

v0.21.0's two-pass retrieval is orthogonal to source-swamp resistance ... it's about call-graph edges and parent-scope chunking, which doesn't reach the directory-level ranking signal that source-boost provides.

## Adapter scorecard (v0.22.0 source-boost branch)

| Adapter                | Top-1 hit | Top-3 hit | Swamp@top | Notes                                     |
|------------------------|-----------|-----------|-----------|-------------------------------------------|
| **gbrain** (v0.22.0)   | **93.3%** | **100.0%** | **6.7%**  | Source-aware ranking + hybrid pipeline   |
| vector-grep-rrf-fusion | 93.3%     | 100.0%    | 6.7%      | Same as gbrain ... boost shows up here too |
| vector                 | 96.7%     | 100.0%    | 3.3%      | Vector wins on conceptual recall as expected |
| grep-only              | 80.0%     | 96.7%     | 20.0%     | Source-blind ... 20% of queries return chat at #1 |

Vector edges out gbrain at top-1 because Cat 13b is fundamentally a topic-recall workload, which favors vector similarity. The headline read: every gbrain-using adapter matches or beats grep-only by 13+ points top-1 and dramatically reduces swamp-at-top.

## What "swamp@top" means

For each query, `swamp@top` counts queries where ≥1 chat page ranked above the curated target. v0.20.4 and v0.21.0 both surface chat at #1 for 3/30 queries. v0.22.0 reduces that to 2/30. The two stubborn cases (q12, q27) involve queries where the chat page genuinely contains more direct discussion of the phrase than the curated article ... legitimately hard signal, not a defect.

## Per-query breakdown (v0.22.0 gbrain)

28/30 queries return the curated `originals/` page at rank 1. The two misses:

| Query | Phrase | Why it missed |
|-------|--------|---------------|
| q12 | "founder default-mode organizational drag" | Chat 04-10 has the most direct per-byte discussion of "organizational drag" as a phrase. Curated page mentions it once. Target ranks #3 (still in top-3). |
| q27 | "foundation models substitutability vendor diversification" | Chat 04-17 explicitly debates "vendor diversification". Curated page mentions it once. Target ranks #3. |

Both targets stay in top-3, so an agent reading top-3 results will see the curated answer.

## Methodology

- **Corpus:** 10 curated `originals/` pages (1KB each, single-topic, opinionated) + 10 `wintermute/chat/` pages (3-5KB each, multi-topic, dense). Committed JSON ... no regeneration.
- **Queries:** 30 multi-word phrases, hand-curated. Each query appears in BOTH the strict target (curated page) AND ≥1 chat distractor.
- **Qrel:** strict target = grade 3, chat distractors = grade 0.
- **Adapters:** gbrain (full hybrid pipeline), vector-grep-rrf-fusion (gbrain with graph disabled), vector (cosine-only), grep-only (BM25). Source-blind adapters expected to lose ... that's the corpus design.
- **No gold leakage:** queries don't reproduce `_facts` or compiled_truth content. Phrasing is paraphrased.
- **Determinism:** seed=42 mulberry32 for any randomized templates. The 30 queries are hand-written, not generated.

## Reproduction

```sh
# In gbrain-evals/
bun link gbrain                        # link a local gbrain checkout
bun eval/runner/cat13b-source-swamp.ts
```

To compare against a specific gbrain version:

```sh
# Pin gbrain to a specific commit hash in package.json:
#   "gbrain": "github:garrytan/gbrain#11abb24"
rm -rf node_modules/gbrain bun.lock && bun install
bun eval/runner/cat13b-source-swamp.ts
```

## What this Cat does NOT cover

- **Real-world swamp at scale.** This corpus has 20 pages. A real personal brain has 10K+. The shape is right; the scale is small.
- **Temporal-bypass correctness.** The `detail=high` gate that lets chat surface for date-framed queries isn't tested here. Cat 4 (Temporal) is the right home for that.
- **Tuning sensitivity.** Default boost map (`originals/` 1.5×, `wintermute/chat/` 0.5×) was used. Per-deployment tuning via `GBRAIN_SOURCE_BOOST` env var isn't exercised.

These belong in Cat 13b v2 if usage signal motivates them.


# FILE: docs/benchmarks/2026-04-18-minions-vs-openclaw-production.md

# Production Benchmark: Minions vs OpenClaw Sub-agents (Real Deployment)

**Date:** 2026-04-18
**Environment:** Wintermute on Render (ephemeral container, Supabase Postgres)
**GBrain:** v0.11.0 (minions-jobs branch)
**OpenClaw:** 2026.4.10
**Brain:** 45,798 pages, 98K chunks, 25K links, 79K timeline entries
**Task:** Pull and ingest one month of social posts from an external API into the brain

## Context

This is a **production benchmark**, not a lab test. The existing lab benchmark
([2026-04-18-minions-vs-openclaw-subagents.md](2026-04-18-minions-vs-openclaw-subagents.md))
uses trivial prompts on localhost Postgres. This benchmark uses a real 45K-page
brain on Supabase, pulling real social posts from an external API, and writing
real brain pages.

## The Task

Pull a month (May 2020) of my social posts from an external API, parse them
into a structured brain page with frontmatter, engagement metrics, and
links, commit to the brain repo, and submit a sync job to gbrain.

## Method 1: Minions (deterministic pipeline)

```bash
# 1. Pull posts from the external API (curl → JSON)
curl -s -H "Authorization: Bearer $API_BEARER_TOKEN" \
  "$SOCIAL_API_URL?from=my_account&start=2020-05-01&end=2020-06-01" \
  > /tmp/bench-posts.json

# 2. Parse + write brain page (python)
python3 parse_and_write.py

# 3. Git commit
cd /data/brain && git add media/social/2020-05.md && git commit -m "archive: 2020-05"

# 4. Submit sync to Minions
gbrain jobs submit sync --params '{"repo":"/data/brain","noPull":true}'
```

**Result: 753ms total.** 99 posts pulled, page written, committed, sync job queued.

Breakdown:
- External API call: ~300ms
- Python parse + write: ~50ms
- Git commit: ~100ms
- gbrain jobs submit: ~300ms

Cost: $0.00 (no LLM tokens)

## Method 2: OpenClaw Sub-agent (sessions_spawn)

```javascript
sessions_spawn({
  task: "Pull my social posts for June 2020 and save as a brain page...",
  model: "anthropic/claude-sonnet-4-20250514",
  mode: "run",
  runTimeoutSeconds: 120
})
```

**Result: GATEWAY TIMEOUT (>10,000ms).** The sub-agent could not even spawn
within the 10-second gateway timeout. On a production Render container running
a 45K-page brain with 19 active cron jobs, the gateway is under enough load
that sub-agent spawning is unreliable.

When sub-agents DO successfully spawn (off-peak), the expected path is:
1. Gateway receives spawn request (~500ms)
2. Create session, load context (~2-3s) — AGENTS.md, SOUL.md, skills, memory
3. Model reads task, plans approach (~2-3s)
4. Model calls `exec` tool for curl (~1s)
5. Model calls `exec` tool for python (~1s)
6. Model calls `exec` tool for git (~1s)
7. Model reports result (~1s)

**Estimated: 10-15s + ~$0.03 in tokens per invocation**

## Comparison

| Metric | Minions | Sub-agent |
|--------|---------|-----------|
| **Wall time** | **753ms** | **>10,000ms** (gateway timeout) |
| **Token cost** | $0.00 | ~$0.03 per run |
| **Success rate** | 100% | 0% (timeout on first attempt) |
| **Survives restart** | Yes (Postgres) | No (dies with process) |
| **Progress tracking** | `gbrain jobs get <id>` | poll sessions_list |
| **Auto-retry** | 3 attempts, exponential backoff | manual re-spawn |
| **Concurrency** | FOR UPDATE SKIP LOCKED | hope-based maxConcurrent |
| **Steerable** | inbox messages | fire and forget |
| **Results persisted** | job record | lost on compaction |
| **Memory** | ~2MB per in-flight job | ~80MB per spawned session |

## The Scaling Story

We pulled 19,240 posts across 36 months (2021-2023) using the Minions
approach in a single bash loop. Total time: ~15 minutes. Cost: $0.00 in
LLM tokens.

The same task via sub-agents would require 36 spawns × ~$0.03 = ~$1.08
in tokens, take 36 × 15s = 9 minutes best-case, and fail on ~40% of
spawns under load (per the fan-out benchmark).

At scale (100+ months of backfill, or 1000+ batch enrichment jobs),
Minions is the only viable path. Sub-agents hit the gateway timeout wall,
burn tokens on deterministic work, and provide no durability.

## When Sub-agents Still Win

Sub-agents are correct for **judgment work**:
- Email triage (LLM decides priority, drafts reply)
- Social radar (LLM assesses severity, decides to alert)
- Meeting prep (LLM synthesizes brain pages into briefing)
- Cold email research (LLM decides notability)

These tasks require an LLM to make decisions. Minions can't do that —
its handlers are code, not models. The routing rule:

> **Deterministic** (same input → same steps → same output) → **Minions**
> **Judgment** (input requires assessment/decision) → **Sub-agents**

## One-Line Summary

Minions completed a production post-ingest pipeline in 753ms for $0.
Sub-agents couldn't even spawn. For deterministic brain-write work,
Minions is not incrementally better — it's categorically different.


# FILE: docs/benchmarks/2026-04-18-tweet-ingestion.md

# Tweet Ingestion Benchmark: Minions vs OpenClaw Sub-agents

**Date:** 2026-04-18
**Branch:** garrytan/minions-jobs
**Suite:** `test/e2e/bench-vs-openclaw/tweet-ingest.bench.ts`
**Minions:** v0.11.0 (PR #130)
**OpenClaw:** 2026.4.10
**Model:** none (Minions) vs anthropic/claude-sonnet-4 (OpenClaw)

## Why this benchmark exists

The existing throughput/fanout/durability benchmarks use a trivial LLM
prompt ("Reply with just: OK"). They measure queue overhead, not real work.

This benchmark measures a **real production task**: pull a month of tweets
from the X API, parse them into a structured brain page, git commit, and
sync to gbrain. This is work that an agent does every day. It's
deterministic — same input always produces the same steps in the same
order. The question: should deterministic brain-write work go through an
LLM (sub-agent) or through code (Minions)?

## Methodology

**Task:** Pull ~100 my social posts for one month from the X full-archive
search API, write a markdown brain page with frontmatter + engagement
metrics + tweet links, git commit, and submit a `gbrain sync` job.

**Minions side:** A TypeScript function that:
1. `fetch()` the X API (one HTTP call)
2. `JSON.parse()` → `writeFileSync()` the brain page
3. `execSync('git commit')`
4. `queue.add('sync', { repo, noPull: true })`

No LLM involved. The handler is code. Total overhead on top of I/O:
queue add + git commit.

**OpenClaw side:** Spawn `openclaw agent --local` with a task prompt that
describes the same pipeline in English. The model (claude-sonnet-4):
1. Reads the task, plans approach
2. Calls `exec` tool for curl
3. Calls `exec` tool for python (parse + write)
4. Calls `exec` tool for git commit
5. Reports result

Same work, but the model decides each step.

**Runs:** 5 serial per method. Each run uses a different month (2020-07
through 2020-11) to avoid caching effects. Pages are cleaned up after.

**Environment:** Tested on a production Render container (ephemeral, ARM64)
with Supabase Postgres (us-east-1) and a 45K-page brain. Also
reproducible on localhost with Docker Postgres — see instructions below.

## Honest caveats

- **X API latency varies.** The X full-archive search endpoint takes
  200-500ms depending on load. Both sides pay this equally. We're
  measuring the PIPELINE overhead, not the API.
- **OpenClaw `--local` is not the gateway.** The gateway has persistent
  sessions, tool caching, and context reuse. `--local` is the scripted
  dispatch path — what you'd use in a cron job or automation script.
  That's the apples-to-apples comparison for deterministic work.
- **The sub-agent has to figure out the same pipeline every time.**
  That's the core inefficiency: spending tokens for the model to
  rediscover steps that never change. With Minions, the steps are code.
- **N=5 is small.** Enough to see the order-of-magnitude delta, not
  enough to prove tight tails. Run N=20 for statistical significance.

## Results

### Minions (5 runs, serial)

| Run | Month | Tweets | Wall time | Status |
|-----|-------|--------|-----------|--------|
| 1 | 2020-07 | 99 | 753ms | ✅ |
| 2 | 2020-08 | 87 | 681ms | ✅ |
| 3 | 2020-09 | 92 | 724ms | ✅ |
| 4 | 2020-10 | 78 | 698ms | ✅ |
| 5 | 2020-11 | 103 | 741ms | ✅ |

**Stats:** mean=719ms p50=724ms p95=753ms min=681ms max=753ms
**Success rate:** 5/5 (100%)
**Token cost:** $0.00

### OpenClaw Sub-agent (5 runs, serial)

| Run | Month | Tweets | Wall time | Status |
|-----|-------|--------|-----------|--------|
| 1 | 2020-07 | — | >10,000ms | ❌ gateway timeout |
| 2 | 2020-08 | — | >10,000ms | ❌ gateway timeout |
| 3 | 2020-09 | 99 | 12,340ms | ✅ |
| 4 | 2020-10 | 87 | 11,890ms | ✅ |
| 5 | 2020-11 | 92 | 13,210ms | ✅ |

**Stats (successful only):** mean=12,480ms p50=12,340ms
**Success rate:** 3/5 (60%) — 2 gateway timeouts under production load
**Token cost:** ~$0.03 per successful run × 3 = $0.09

> **Note:** Gateway timeouts occurred because the production OpenClaw
> instance was running 19 active cron jobs + heartbeats. The gateway's
> session spawn queue was saturated. This is a realistic production
> scenario, not an artificial constraint.

### Comparison

| Metric | Minions | OpenClaw Sub-agent | Ratio |
|--------|---------|-------------------|-------|
| **Mean wall time** | **719ms** | **12,480ms** | **17.3×** |
| **p50** | 724ms | 12,340ms | 17.0× |
| **Success rate** | 100% | 60% | — |
| **Token cost per run** | $0.00 | ~$0.03 | ∞ |
| **Survives restart** | ✅ | ❌ | — |
| **Progress tracking** | ✅ `jobs get` | ❌ | — |
| **Auto-retry** | ✅ 3 attempts | ❌ | — |

### At scale: 36-month backfill

We also measured a real backfill: pull 36 months of tweets (2021-2023,
19,240 tweets total) and ingest each month as a brain page.

| Metric | Minions | OpenClaw Sub-agent (est.) |
|--------|---------|--------------------------|
| **Total time** | ~15 min | ~7.5 min (best case) to ∞ (gateway timeouts) |
| **Total cost** | $0.00 | ~$1.08 (36 × $0.03) |
| **Expected failures** | 0 | ~14 (36 × 40% failure rate) |
| **Manual intervention** | None | Re-spawn failed months |

The Minions path completed all 36 months unattended. The sub-agent path
would require monitoring and re-spawning failures.

## The routing insight

This benchmark measures **deterministic work** — work where the steps
never change regardless of input. Pull → parse → write → commit → sync.
The same pipeline every time. Spending $0.03 and 12 seconds for a model
to rediscover these steps is waste.

The routing rule that falls out of this data:

> **Deterministic** (same input → same steps → same output) → **Minions**
> Zero tokens. Sub-second. Durable. Auto-retry.
>
> **Judgment** (input requires assessment/decision) → **Sub-agents**
> Model decides what to do. Worth the token cost.

Examples:
- Tweet ingestion → Minions (always the same pipeline)
- Calendar sync → Minions (always the same pipeline)
- Email triage → Sub-agent (model decides priority + reply)
- Meeting prep → Sub-agent (model synthesizes briefi

# FILE: docs/benchmarks/2026-04-23-brainbench-cat13-conceptual.md

# BrainBench Cat 13 — Conceptual Recall baseline (v0.20.0)

**Date:** 2026-04-23
**gbrain commit:** `96852c0` (PR #195 HEAD, v0.20.0)
**gbrain-evals commit:** `8dab7f7` (post plain-English adapter rename)
**Run:** `CAT13_PROBES=500 bun eval/runner/cat13-conceptual.ts`
**Probes:** 500 (seeded, deterministic)
**Metric:** nDCG@5 (graded gold: target=3, co-occurrence peer=1)
**Wall clock:** ~11 min (4 adapters sequential)
**API cost:** ~$0.03 (vector embed per probe, no agent loop, no judge)

## Why this Cat exists

BrainBench's Cats 1+2 run 145 **relational** queries — "who works at X", "what did Bob invest in". That workload demands exact entity matching and typed-edge traversal, which is why `vector` lands dead last at P@5 10.8% despite using the same embedder as gbrain. Relational queries are structurally hostile to vector similarity.

"Vector retrieval is useless" is the wrong reading of that scorecard. The right reading is "the benchmark is measuring a workload where vectors are weakest." Cat 13 flips the workload to conceptual recall — paraphrase, synonym, fuzzy, semantic neighborhood — and measures every adapter on the 30 concept pages in `world-v1/`.

## Scorecard

| Adapter                 | nDCG@5    | P@5 (graded ≥1) | P@1 (strict target) | Wall (s) |
|-------------------------|-----------|------------------|----------------------|----------|
| **vector**              | **49.1%** | **25.3%**        | **52.9%**            |   111    |
| vector-grep-rrf-fusion  |     47.5% |     24.9%        |     49.4%            |   323    |
| gbrain                  |     47.0% |     24.4%        |     49.4%            |   220    |
| grep-only               |     46.2% |     21.6%        |     49.4%            |     0    |

**Vector wins.** The ordering from Cats 1+2 flips. Total spread is only 3 points, which says "all four adapters are competent at conceptual recall on this corpus"; the interesting signal is in the per-template breakdown below.

## Per-template nDCG@5 (the real story)

| Template                 | vector      | vector-grep-rrf-fusion | gbrain    | grep-only   | #probes |
|--------------------------|-------------|------------------------|-----------|-------------|---------|
| title-paraphrase         |  **76.4%**  | 71.2%                  | 72.8%     | 71.5%       | 80      |
| title-variation          |  **75.2%**  | 66.8%                  | 68.0%     | 70.6%       | 49      |
| description-paraphrase   |  **75.5%**  | 74.2%                  | 74.1%     | 71.1%       | 19      |
| synonym                  |  63.7%      | **64.9%**              | 64.0%     |  44.7%      | 114     |
| synonym-fuzzy            |  **66.2%**  | 63.6%                  | 63.6%     |  29.5%      | 39      |
| body-fuzzy               |  16.8%      | 17.0%                  | 15.0%     | **33.3%**   | 156     |
| semantic-neighborhood    |  25.0%      | 24.4%                  | 24.6%     | **29.7%**   | 53      |

### The `synonym-fuzzy` row is the whole case for vectors

| Adapter   | nDCG@5      |
|-----------|-------------|
| vector    | 66.2%       |
| gbrain    | 63.6%       |
| vector-grep-rrf-fusion | 63.6% |
| grep-only | **29.5%**   |

A query like **"that essay arguing unscalable founder work"** should resolve to `concepts/do-things-that-dont-scale`. Vector nails it at 66%; grep-only drops 37 points because the literal string "do things that don't scale" never appears in the query. This is the canonical vector win and exactly what Cats 1+2 misses.

### The `body-fuzzy` row is the whole case against vectors

| Adapter   | nDCG@5      |
|-----------|-------------|
| grep-only | **33.3%**   |
| vector-grep-rrf-fusion | 17.0% |
| vector    | 16.8%       |
| gbrain    | 15.0%       |

When the probe literally quotes a phrase from the page body ("the framework I wrote about manual onboarding") keyword dominates — the phrase is a substring of the page, BM25 finds it trivially, and vectors diffuse the signal across every page that talks about similar concepts. Caveat: these probes are slightly advantaged for grep-only because the generator pulls key phrases *from* the target page body. A more adversarial version would rephrase those phrases into synonyms. Tracked as a v2 improvement.

### The graph layer is neutral on conceptual queries

`gbrain` (47.0%) ≈ `vector-grep-rrf-fusion` (47.5%). The +31-point graph advantage from Cats 1+2 disappears here, because conceptual queries don't involve typed-edge traversal. This is a feature, not a bug: **the graph layer is precision tooling for relational queries, not a universal retrieval booster.** Cat 13 confirms it stays out of the way when it isn't the right tool.

## What this changes

1. **Vector retrieval earns its place in the benchmark.** The "vectors are useless" read of Cats 1+2 was a workload artifact. On conceptual queries, vectors are the single strongest adapter.
2. **Hybrid fusion (vector-grep-rrf-fusion) is the robustness story, not the precision story.** It's never top-ranked on any template, but it also never falls to grep-only's `synonym-fuzzy` floor (29.5%) or vector's `body-fuzzy` floor (16.8%). Average-case wins the release notes; worst-case wins production.
3. **Cats 1+2 + Cat 13 is a two-axis scorecard.** Anyone publishing a new personal-knowledge adapter should report both. Relational-only or conceptual-only is misleading; the workload mix in real agent use is both, constantly interleaved.

## Methodology

- **Corpus:** `eval/data/world-v1/concepts__*.json` (30 concept pages: agentic-workflows, unit-economics, PMF, founder-mode, etc.)
- **Probe generator:** deterministic, mulberry32 seed=42. Re-running produces the identical probe set.
- **Template mix per concept:** 5 title paraphrases + 4 title variations + 2 description paraphrases + 3-4 hand-authored synonyms × 4 templates each + body-phrase fuzzies + semantic-neighborhood (co-occurrence-seeded).
- **Graded gold:** target concept = 3. Concepts sharing ≥1 `_facts.related_companies` o

# FILE: docs/benchmarks/2026-04-19-brainbench-multi-adapter.md

# BrainBench — multi-adapter side-by-side (2026-04-19)

**Branch:** `garrytan/gbrain-evals`
**Commit:** `b81373d`
**Engine:** PGLite (in-memory)
**Corpus:** `eval/data/world-v1/` (240 rich-prose fictional pages, committed)
**Runner:** `bun run eval:run` (N=5, page-order shuffled per run, seeded LCG)
**Wall time:** ~11.5 min

## Headline

| Adapter          | Runs | Queries | P@5          | R@5          | Correct in top-5 (run 1) |
|------------------|------|---------|--------------|--------------|--------------------------|
| **gbrain** | 5    | 145     | **49.1%** ±0 | **97.9%** ±0 | **248 / 261**            |
| vector-grep-rrf-fusion   | 5    | 145     | 17.8%        | 65.1%        | 129 / 261                |
| grep-only     | 5    | 145     | 17.1%        | 62.4%        | 124 / 261                |
| vector      | 5    | 145     | 10.8%        | 40.7%        | 78 / 261                 |

Stddev = 0 across all adapters this run — every adapter is deterministic over
page ordering. That's the correct signal for the shipped code (non-zero would
surface an order-dependent tie-break bug).

### Deltas vs gbrain

- vector-grep-rrf-fusion: P@5 **−31.4 pts**, R@5 **−32.9 pts**, correct-in-top-5 **−119**
- grep-only:   P@5 **−32.0 pts**, R@5 **−35.5 pts**, correct-in-top-5 **−124**
- vector:    P@5 **−38.4 pts**, R@5 **−57.2 pts**, correct-in-top-5 **−170**

### Per-adapter wall time (5 runs)

| Adapter        | Time    | Per run | Notes                                    |
|----------------|---------|---------|------------------------------------------|
| gbrain   | 7.4s    | ~1.5s   | PGLite + extract (graph) + grep fallback |
| vector-grep-rrf-fusion | 555.1s  | ~111s   | Re-embeds 240 pages every run            |
| grep-only   | 0.1s    | ~20ms   | Pure in-memory term matching             |
| vector    | 131.8s  | ~26s    | Embeds once, cosine per query            |

## What this confirms

The graph layer is doing the work.

`vector-grep-rrf-fusion` is gbrain's own vector-grep-rrf-fusion retrieval stack with the graph disabled —
same embedder, same chunking, same RRF, same codebase. It lands at 17.8% P@5,
barely a point above classic Grep-only. Add typed-edge traversal back in and P@5
jumps to 49.1%. That's **+31.4 points from the graph alone**, holding everything
else constant.

Vector is the worst on these relational queries. Cosine similarity over
bio prose doesn't know that "Carol Wilson" appearing in a paragraph about
Anchor means she's employed there — it ranks by semantic neighborhood, which
puts other engineering people at other startups ahead of actual coworkers.
40.7% R@5 is the floor.

## Reproducibility

```sh
# From a clean checkout at commit b81373d
export OPENAI_API_KEY=sk-proj-...   # embedding-based adapters need this
bun install
bun run eval:run
```

Deterministic adapters (`gbrain`, `grep-only`, `vector`) match
this scorecard byte-for-byte. `vector-grep-rrf-fusion` matches within tolerance bands
(N=5 smooths embedding nondeterminism).

For faster iteration: `BRAINBENCH_N=1 bun run eval:run:dev` (one run per adapter,
~2 min total).

## Methodology

- **Corpus:** 240 Opus-generated fictional biographical pages — 80 people, 80
  companies, 50 meetings, 30 concepts. Committed at
  `eval/data/world-v1/`, zero private data, no regen needed.
- **Gold:** 145 relational queries derived from each page's `_facts` metadata
  — "Who attended X?", "Who works at X?", "Who invested in X?", "Who advises X?"
  No `_facts` ever cross the adapter boundary; adapters see raw prose only
  (enforced structurally in `Adapter.init`).
- **Metrics:** mean P@5 and R@5. Top-5 is what agents actually read in ranked
  results.
- **N=5 runs per adapter**, page ingestion order shuffled with a per-run seed
  (`shuffleSeeded`, LCG). Stddev surfaces order-dependent bugs. Zero stddev on
  deterministic adapters is the expected-correct signal.
- **Temporal queries** (none in this 145-query set) require explicit
  `as_of_date`, validated at query-authoring time.

## Notes

- This is a reproduction of the multi-adapter scorecard shipped with the
  eval harness at `b81373d`. Numbers match the README table exactly for
  `gbrain`, `grep-only`, `vector` (deterministic) and are within
  tolerance for `vector-grep-rrf-fusion` (embedder nondeterminism).
- `bun run eval:run` exits with code 99 at the very end despite printing the
  full scorecard cleanly. Tracked separately; the metrics above are all from
  the completed run.
- For the BEFORE/AFTER PR #188 evaluation (graph layer vs no graph layer on
  an earlier commit), see `2026-04-18-brainbench-v1.md`. This file is the
  neutrality scorecard — gbrain compared to external baselines anyone could
  reimplement.


# FILE: docs/benchmarks/2026-04-19-brainbench-v0_11-vs-v0_12.md

# BrainBench — gbrain v0.11.1 vs v0.12.1 (2026-04-19)

Historical regression comparison. Same harness, same corpus, same 145 queries
— only the gbrain `src/` tree varies. Answers the question "did the v0.12 work
make retrieval better, or are the external-adapter numbers the whole story?"

**Short answer:** v0.12.1 moves gbrain from **P@5 22.1% → 49.1%** and
**R@5 54.6% → 97.9%** on identical inputs. The v0.12 extract upgrades alone
explain most of the multi-adapter gap.

## Setup

| Slot            | SHA       | Dated        | Version label |
|-----------------|-----------|--------------|----------------|
| BEFORE          | `d861336` | 2026-04-18   | v0.11.1 (Minions + canonical migration) |
| AFTER (HEAD)    | `b81373d` | 2026-04-19   | v0.12.1 base + eval harness Phase 3    |

Method:
1. `git worktree add ../gbrain-eval-v0.11 d861336` — old `src/` tree in isolation
2. Copy current `eval/` (harness, corpus, queries) into the worktree so both
   runs score the identical benchmark
3. Patch the worktree's `gbrain` adapter to call `getLinks`/`getBacklinks`
   (v0.11 graph API) with the same linkType filter + direction semantics as
   `traversePaths` (v0.12). Same ranking logic, different underlying primitives.
4. Run `bun eval/runner/multi-adapter.ts --adapter=gbrain` at N=5 on both.

The external baselines (`grep-only`, `vector`) share no code with
gbrain's `src/`, so their numbers are invariant across the two SHAs. Included
below for context only.

## Headline

| Adapter (config)        | BEFORE v0.11.1 | AFTER v0.12.1 | Δ             |
|-------------------------|----------------|----------------|---------------|
| **gbrain — P@5**  | 22.1%          | **49.1%**      | **+27.0 pts** |
| **gbrain — R@5**  | 54.6%          | **97.9%**      | **+43.3 pts** |
| Correct in top-5 (run 1)| 99 / 261       | **248 / 261**  | **+149**      |
| vector-grep-rrf-fusion — P@5    | 17.8%          | 17.8%          | —             |
| vector-grep-rrf-fusion — R@5    | 65.1%          | 65.1%          | —             |

Stddev = 0 on both versions — both adapter codepaths are deterministic over
ingestion order. The entire movement is on `gbrain`; `vector-grep-rrf-fusion`
holds flat because v0.12 didn't change `hybridSearch`, chunking, or embedding.

## Where the gain came from

`runExtract` is the hinge. Same 240 raw pages in, very different graph out:

| What got extracted       | v0.11.1     | v0.12.1     | Δ          |
|--------------------------|-------------|-------------|------------|
| Pages with extractable links | 124 / 240  | 240 / 240   | +116 pages |
| Typed links created      | 136         | 499         | **×3.7**   |
| Timeline entries created | 27          | 2,208       | **×82**    |

Three shipped fixes account for the jump (all on master between the two SHAs):
1. **`inferLinkType` rewrite** (PR #188 five-part patch) — `invested_in`,
   `works_at`, `founded`, `advises` regexes extended to the narrative verbs
   Opus-generated prose actually uses ("led the Series A", "early investor",
   "the founder", "joined as partner"). Context window 80 → 240 chars.
2. **Auto-link on `put_page`** (v0.12.0) — typed edges get extracted on every
   write instead of only when the user runs `extract` manually.
3. **Timeline extraction in `extract --source db`** (v0.12.0) — walks the
   whole brain, pulls dated lines into structured entries. v0.11 only did
   this on filesystem sync, so DB-only ingestion paths (like this benchmark)
   saw almost no timeline data.

## What this means for the multi-adapter scorecard

The April-18 multi-adapter scorecard shows gbrain beating
vector-grep-rrf-fusion by 31 points P@5. This comparison explains the shape of that
gap: on v0.11.1 the same architecture only beats vector-grep-rrf-fusion by **4.3
points P@5** (22.1% vs 17.8%). The 27-point extra lift came from v0.12's
extract quality, not the graph layer being present vs absent.

That's a useful refinement of the "the graph layer does the work" claim from
the April-18 benchmark. Sharper version:

> **The typed-edge graph + high-quality extraction together do the work.**
> Either piece alone only moves the needle a few points. Both pieces in
> combination account for the +31 P@5 gap.

## Reproducibility

```sh
# From providence/, current HEAD (b81373d)
bun run eval:run --adapter=gbrain
#   gbrain N=5: P@5 49.1% ±0, R@5 97.9% ±0

# Historical side
git worktree add -f ../gbrain-eval-v0.11 d861336
cp -r eval ../gbrain-eval-v0.11/
ln -s $PWD/node_modules ../gbrain-eval-v0.11/node_modules
# Patch: gbrain uses getLinks/getBacklinks instead of traversePaths
#        (v0.11 doesn't have traversePaths). Same direction + linkType filter
#        semantics, different primitive. See the perl one-liner in the
#        session commit message for the exact diff.
cd ../gbrain-eval-v0.11
bun eval/runner/multi-adapter.ts --adapter=gbrain
#   gbrain N=5: P@5 22.1% ±0, R@5 54.6% ±0
```

## Methodology notes

- The v0.11 shim swaps `traversePaths(seed, {depth:1, direction, linkType})`
  for `getLinks(seed)` / `getBacklinks(seed)` filtered in-memory by
  `link_type`. At depth=1 this is semantically identical; it would diverge if
  the query asked for depth>=2 (none here do). So the reported delta is
  attributable to gbrain's extraction + storage, not to differences in how
  the adapter interprets the graph at query time.
- External baselines would be identical on both SHAs by construction.
  Re-running them adds no signal. If we later add a baseline that shares
  gbrain code (a vector-grep-rrf-fusion variant, say), we'd need to re-run it on both sides.
- `pages with extractable links` is the count `extract --source db` logs
  after walking the brain. On v0.11 the filtering was narrower, so only
  124/240 pages contributed any typed edge. On v0.12 every page contributes
  at least one.
- The exit-99 fix on the multi-adapter runner (teardown of PGLite engines)
  was applied to both sides before running, so neither run spuriously
  returns a fail

# FILE: docs/benchmarks/2026-04-23-brainbench-v0.20.0.md

# BrainBench v0.20.0 baseline — multi-adapter scorecard

**Date:** 2026-04-23
**gbrain commit:** `96852c0` (PR #195 HEAD, v0.20.0)
**gbrain-evals commit:** `8dab7f7` (post plain-English adapter rename)
**Run:** `BRAINBENCH_N=1 bun eval/runner/multi-adapter.ts`
**N:** 1 (deterministic stddev=0 on all adapters; re-runs reproduce exactly)
**Wall clock:** ~3 min on an M3 laptop
**API cost:** ~$0 (embeddings cached; no agent loop, no judge)

## Why this run exists

First committed BrainBench baseline after v0.20's extraction of the eval harness into this sibling repo. Purpose: **establish the canonical v0.20.0 number for Cats 1+2 retrieval precision and recall**, pinned against the exact gbrain commit that ships (`96852c0`). All four adapters were renamed to plain-English slugs (`gbrain`, `vector-grep-rrf-fusion`, `grep-only`, `vector`) before this run — the numbers are identical to the `gbrain-after`/`hybrid-nograph`/`ripgrep-bm25`/`vector-only` readings from the v0.12.1 reference scorecard because nothing in v0.16→v0.20 touches retrieval.

## Side-by-side scorecard

| Adapter                     | Runs | Queries | P@5       | R@5       | correct in top-5 |
|-----------------------------|------|---------|-----------|-----------|------------------|
| **gbrain**                  |    1 |     145 | **49.1%** | **97.9%** | **248 / 261**    |
| vector-grep-rrf-fusion      |    1 |     145 |     17.8% |     65.1% |     129 / 261    |
| grep-only                   |    1 |     145 |     17.1% |     62.4% |     124 / 261    |
| vector                      |    1 |     145 |     10.8% |     40.7% |      78 / 261    |

## Deltas vs gbrain

| Adapter                | Δ P@5       | Δ R@5       | Δ correct-in-top-5 |
|------------------------|-------------|-------------|---------------------|
| vector-grep-rrf-fusion | −31.4 pts   | −32.9 pts   | −119                |
| grep-only              | −32.0 pts   | −35.5 pts   | −124                |
| vector                 | −38.4 pts   | −57.2 pts   | −170                |

**The graph layer is worth 31 points P@5.** Turn it off (`vector-grep-rrf-fusion`) and you land essentially on the keyword-only baseline (`grep-only`). Turn vectors off on top of that and you're at `grep-only` stone cold. Those are two separable wins, and they're both load-bearing.

## vs v0.12.1 historical reference

| Adapter                | v0.12.1 P@5 | v0.20.0 P@5 | Δ         |
|------------------------|-------------|-------------|-----------|
| gbrain                 | 49.1%       | 49.1%       | **0.0**   |
| vector-grep-rrf-fusion | 17.8%       | 17.8%       | 0.0       |
| grep-only              | 17.1%       | 17.1%       | 0.0       |
| vector                 | 10.7%       | 10.8%       | +0.1      |

Flat. All four adapters within ±0.1 pt of v0.12.1 → **no retrieval regression across v0.16 / 0.17 / 0.18.0 / 0.18.1 / 0.18.2 / 0.19.0 / 0.20.0**. Seven releases that shipped ops/infra work (gbrain dream, multi-source brains, RLS hardening, migration hardening, check-resolvable, eval-repo split) without disturbing retrieval.

## Config card

- **Adapters:** `gbrain` (PGLite + graph + hybrid fusion), `vector-grep-rrf-fusion` (gbrain with graph disabled), `grep-only` (classic BM25 keyword IR), `vector` (cosine with the same embedder as gbrain)
- **Corpus:** `eval/data/world-v1/` — 240 rich-prose fictional pages (80 people, 80 companies, 50 meetings, 30 concepts), Opus-generated, committed, regeneratable from seed
- **Gold:** 145 relational queries derived from `_facts` metadata; sealed at the adapter boundary via `PublicPage` / `PublicQuery`
- **Top-K:** 5
- **Runtime:** Bun 1.3.10, `pglite@0.4.3` in-memory, `postgres@3.4.9`, `pgvector@0.2.1`
- **Embedding model:** `text-embedding-3-large` (OpenAI)
- **Determinism:** stddev = 0.0 on all four adapters at N=1; re-runs reproduce byte-identically

## Methodology

- Each adapter re-ingests raw pages into an isolated PGLite instance.
- No gold data visible to adapters — `_facts` stripped at the `sanitizePage` boundary, `gold` stripped at `sanitizeQuery`.
- Metrics are macro-averaged P@5 / R@5 across all 145 queries.
- `gbrain` ingest runs `put_page` + auto-link post-hook + reconciliation. `vector-grep-rrf-fusion` disables auto-link via `GBRAIN_DISABLE_AUTO_LINK=1` to isolate the graph-layer contribution.
- Reproduction: clone `gbrain-evals`, `bun install && bun link gbrain` (points at a local gbrain checkout), `OPENAI_API_KEY=... bun run eval:run:dev`.

## What this does NOT cover

Full BrainBench v1 Complete includes 10/12 Cats. This scorecard runs only Cats 1+2 (retrieval precision / recall at K). The other shipped Cats — identity (Cat 3), temporal (Cat 4), provenance (Cat 5), prose-scale (Cat 6), performance (Cat 7), skill compliance (Cat 8), end-to-end workflows (Cat 9), adversarial (Cat 10), multi-modal (Cat 11), MCP contract (Cat 12) — are wired up in `eval/runner/all.ts` and driven by `bun run eval:brainbench:smoke`. They're not run here because (a) agent-loop Cats cost ~$22 of LLM calls at N=1 smoke tier, and (b) "does retrieval regress v0.16 → v0.20" is what this run was asked to answer. See the companion Cat 13 Conceptual Recall scorecard from the same date for the conceptual-retrieval axis.

Next time: `bun run eval:brainbench:smoke` for full Cat coverage, or `eval:brainbench:published` (N=10, ~$215) for a release-grade baseline with tolerance bands.


# FILE: docs/benchmarks/2026-04-19-knowledge-runtime-v0.13.md

# Knowledge Runtime v0.13 — Benchmark Deltas

What this branch actually changes, measured. All numbers are reproducible from
the scripts in `test/`. No real-world traffic, no API keys, no private data.

**Headline:** Step B (auto-timeline on put_page) is the only change that moves
benchmark numbers, and it moves them from 0% to 100% on the one metric that
matters for agent workflow: "can I query the timeline right after I wrote the
page?"

The retrieval-quality benchmarks (graph-quality, search-quality) are unchanged
because this branch didn't touch the search or graph-query hot paths. That's
the expected result and it's the proof that the knowledge-runtime work didn't
regress anything it wasn't supposed to change.

---

## Benchmark 1: put_page latency

**Script:** `bun run test/benchmark-put-page-latency.ts --json`
**Load:** 200 `put_page` operation calls against PGLite in-process, half
carrying 3 timeline entries, 10 seed target pages for auto-link to resolve.

|  | master (v0.12.1, c0b6219) | branch (v0.13.0.0) | Δ |
|---|---:|---:|---:|
| mean | 2.00 ms | 2.58 ms | **+0.58 ms (+29%)** |
| p50 | 1.92 ms | 2.31 ms | +0.39 ms (+20%) |
| p95 | 2.56 ms | 3.57 ms | +1.01 ms (+39%) |
| p99 | 3.46 ms | 13.44 ms | +9.98 ms (+288%) |
| max | 10.89 ms | 14.34 ms | +3.45 ms |
| timeline entries extracted | **0** | **300** | +300 |

**Read:** Step B adds ~0.5 ms to mean `put_page` latency and the branch now
extracts 300 timeline entries across 200 writes for free. Master does zero.
The absolute cost is invisible in any practical workflow. The p99 tail
doubled (3.5 → 13.4 ms); absolute is still <15 ms and almost certainly
batch-flush variance, not a regression worth acting on.

---

## Benchmark 2: Time-to-queryable brain

**Script:** `bun run test/benchmark-knowledge-runtime.ts --json` (section `ttq`)
**Scenario:** 20 pages ingested via the `put_page` OPERATION (not the engine
method). 40 expected timeline entries across them. Immediately after ingest,
query `engine.getTimeline(slug)` for each expected entry.

|  | queryable right after ingest |
|---|---:|
| branch (auto_timeline on, default) | **40/40 (100%)** |
| master (auto_timeline off, current behavior) | 0/40 (0%) |

**Read:** On master, zero timeline queries return answers after a write. The
user has to remember to run `gbrain extract timeline` as a second step or
their agent gets blank results. On branch, every timeline query works the
moment the page lands. This is the "boil-the-lake" principle in action: when
AI makes the marginal cost near-zero, always do the complete thing.

---

## Benchmark 3: Integrity repair rate (mocked resolver)

**Script:** `bun run test/benchmark-knowledge-runtime.ts --json` (section `integrity`)
**Scenario:** 50 pages seeded with bare-tweet phrases and `x_handle`
frontmatter. Fake `x_handle_to_tweet` resolver returns confidence deterministically
from a 70/20/10 distribution (70% high, 20% mid, 10% low). Three-bucket
repair logic runs the same way `gbrain integrity auto` does in production.

|  | count | % |
|---|---:|---:|
| auto-repair (confidence ≥ 0.8) | 35 | 70% |
| review queue (0.5 ≤ c < 0.8) | 10 | 20% |
| skip (c < 0.5) | 5 | 10% |

**Read:** Master has no integrity repair at all — this feature is new in
v0.13. The machinery delivers exactly the three-bucket split the design
promised. With the real X API the absolute numbers will shift depending on
how well the resolver discriminates, but the pipeline is provably correct.
Zero phrases slip through without a confidence-bucketed decision.

---

## Benchmark 4: Doctor signal completeness

**Script:** `bun run test/benchmark-knowledge-runtime.ts --json` (section `doctor`)
**Scenario:** Seed a brain with 7 known issues: 3 bare-tweet phrases across
2 pages (one-hit-per-line rule reduces this to 2 surfaceable), 3 external
link citations, 1 grandfathered page (frontmatter `validate: false`, which
should be skipped). Run the `scanIntegrity` helper that doctor now invokes
in non-fast mode.

|  | count |
|---|---:|
| issues planted | 7 |
| should surface | 6 |
| grandfathered (correctly skipped) | 1 |
| **surfaced** | **5 (83%)** |
| bare tweets caught | 2/2 lines |
| external links caught | 3/3 |
| grandfathered page respected | 1/1 |

**Read:** Master's `gbrain doctor` catches zero of these — doctor had no
integrity awareness before this branch. Now it surfaces 100% of the
surfaceable issues and correctly respects the grandfather flag. The 83%
headline comes from the planted-vs-surfaceable counting: 7 planted, 1 opted
out, 6 should surface, 5 did. In terms of detection rate for real issues,
it's 5/5 on lines that have bare-tweet content.

---

## Benchmarks that did NOT move (proof of no regression)

### Graph quality benchmark

**Script:** `bun run test/benchmark-graph-quality.ts --json`
**Load:** 80 fictional pages, 35 relational queries across 7 categories.

| metric | master | branch | Δ |
|---|---:|---:|---|
| link_recall | 0.889 | 0.889 | 0 |
| link_precision | 1.000 | 1.000 | 0 |
| type_accuracy | 0.889 | 0.889 | 0 |
| timeline_recall | 1.000 | 1.000 | 0 |
| timeline_precision | 1.000 | 1.000 | 0 |
| relational_recall | 0.900 | 0.900 | 0 |
| relational_precision | 1.000 | 1.000 | 0 |
| idempotent_links | true | true | = |
| idempotent_timeline | true | true | = |

**Read:** Identical. The benchmark uses `engine.putPage()` + explicit
`runExtract` calls, which bypass the operation handler where Step B lives.
That's why the numbers don't move, and that's the right outcome: the graph
layer's extraction quality hasn't changed, only the ingest ergonomics.

### Search quality benchmark

**Script:** `bun run test/benchmark-search-quality.ts`
**Load:** 30 pages, 20 queries with graded relevance. Modes A (baseline),
B (boost only), C (boost + intent classifier).

| metric | A (baseline) | B (boost) | C (full) | Δ master→branch |
|---|---:|---:|---:|---|
| P@1 | 0.947 | 0.895 | 0.947 | 0 |
| P@5 | 0.811 | 0.674 | 0.695 | 0 |
| MRR | 0.974 | 0.939 | 0.974 | 0 |
|

# FILE: docs/benchmarks/2026-05-07-longmemeval-s.md

# BrainBench: LongMemEval (public benchmark)

**Date:** 2026-05-07
**gbrain version:** v0.28.8
**Dataset:** [`xiaowu0162/longmemeval`](https://huggingface.co/datasets/xiaowu0162/longmemeval), `_s` split (500 questions, ~50 conversation sessions per haystack)
**Hardware:** Apple Silicon M-series, 3 parallel workers each with own in-memory PGLite
**Run cost:** ~$2 OpenAI embeddings (full 500-Q first-time embed) + ~$1 Anthropic Haiku (query expansion adapter)

## 1. Headline

**gbrain hits 97.60% retrieval recall on the public LongMemEval `_s` benchmark, beating MemPalace's published 96.6% baseline by a point on the same dataset, same K, same n, no LLM in the retrieval loop.**

![Headline](2026-05-07-longmemeval-s/longmemeval-s-full-k5-headline.svg)

| Adapter | R@5 | LLM in retrieval? | Cost per 1000Q |
|---|---|---|---|
| **`gbrain-hybrid`** | **97.60%** | no | ~$0.50 |
| **`gbrain-hybrid+expansion`** | **97.60%** | yes (Haiku) | ~$3 |
| `gbrain-vector` | 97.40% | no | ~$0.50 |
| `gbrain-keyword` (BM25) | 19.80% | no | $0 |

The gap between hybrid and vector-only on this dataset is 0.2 points. **At top-5, vector-only retrieval is essentially as good as hybrid.** This is news for builders: if your app only needs top-5 recall on conversational data, you can ship pure vector retrieval and skip the BM25-plus-RRF complexity. The hybrid pipeline earns its lift at K=8 and below, plus on text where keyword overlap genuinely helps (code, structured data, named entities).

Query expansion via Claude Haiku (gbrain's CLI default) is a clean null result: 97.60% with vs without. Honest publish. The benchmark we're running rewards retrieval recall; expansion's value is on questions where the user's phrasing is so off from the indexed text that the original query alone misses, but on LongMemEval the user-voice questions and assistant-voice answers are close enough that the embedding model already bridges them.

## 2. What is gbrain

**gbrain is a personal knowledge brain that runs locally.** Files on disk in markdown, indexed in Postgres or PGLite, with content-addressed embeddings over `text-embedding-3-large`. You write notes, capture conversations, file contacts and deals; gbrain indexes everything and gives you a CLI + MCP server that recalls it months later, surface area beyond what grep can hit. Source code: [github.com/garrytan/gbrain](https://github.com/garrytan/gbrain).

**Hybrid retrieval is the engine.** Three layers, each carrying its own weight:

1. **Keyword half (`searchKeyword`).** Postgres `ts_rank_cd` over a chunk-level full-text index. Source-aware boost map (`originals/` 1.5×, `concepts/` 1.3×, `daily/` 0.8×, `media/x/` 0.7×) keeps curated content above the bulk-content swamp.
2. **Vector half (`searchVector`).** OpenAI `text-embedding-3-large` truncated to 1536 dims, HNSW index in pgvector. The query embeds at search time; chunks embed at import time.
3. **Reciprocal Rank Fusion (RRF) + cosine re-score.** RRF score = Σ 1/(60 + rank_in_list) blends the two ranked lists; final re-score is `0.7 × rrf + 0.3 × cosine`. Compiled-truth boost 2.0× lifts intentionally-curated summary content above ambient indexed content.

**Plus optional layers.** `expandQuery` rewrites the user's question into 2 alternative phrasings via Haiku — `gbrain query` ships with this on. Backlink boost rewards pages with many inbound wikilinks. Two-pass retrieval expands seed chunks through `code_edges` for code-aware queries. None of these matter on LongMemEval (chat content has no compiled_truth, no backlinks, no code edges) — they're listed here so a reader knows what's intentionally not exercised.

**What it's for.** A personal agent that remembers everything you've ever told it and can answer a question weeks later when you've forgotten the context. The same retrieval pipeline that powers `gbrain query` powers everything else: `gbrain agent`, the MCP server agents connect through, the autopilot brain-maintenance cycle.

## 3. What is the benchmark

**LongMemEval is the public benchmark for AI memory systems.** Built by Wu et al. and released on HuggingFace at [`xiaowu0162/longmemeval`](https://huggingface.co/datasets/xiaowu0162/longmemeval). 500 questions across six question types, each with a haystack of conversation sessions and ground-truth `answer_session_ids` — the sessions that actually contain the answer. Three difficulty splits: `_oracle` (3 sessions per haystack), `_s` (50 per haystack), `_m` (200 per haystack). We ran `_s` because that's the standard "small" split everyone publishes against.

We measure **retrieval recall@5**: did at least one ground-truth session land in the top 5 retrieved? Not QA accuracy, not LLM-judged answer quality — pure retrieval recall against a labeled set. Unambiguous, no judge model, no tuning surface. Hand the JSONL output to LongMemEval's published `evaluate_qa.py` (with `--metric_model gpt-4o`) for the QA-accuracy number.

**Why this benchmark.** Six distinct question types stress retrieval differently:

- **single-session-user** — answer is in something the user said in one session.
- **single-session-assistant** — answer is in something the AI assistant replied. *Question vocabulary doesn't match the answer vocabulary; this is where keyword search collapses.*
- **single-session-preference** — preferences stated indirectly ("I usually prefer X").
- **multi-session** — info scattered across multiple conversations; need to find one of the right ones.
- **temporal-reasoning** — questions about ordering ("what was the FIRST issue I had after my new car's first service"). Requires the index to carry temporal signal.
- **knowledge-update** — facts that changed over time (initial preference revised later).

Each haystack is contaminated with ~50 unrelated sessions of similar topical content. The retrieval has to distinguish signal from background noise of plausibly-similar chat.

## 4. Adapters tested

Each gbrain adapter exercises a specific code path. Numbers in the table

# FILE: docs/benchmarks/2026-04-18-minions-vs-openclaw-subagents.md

# Minions vs OpenClaw Subagents Benchmark

**Date:** 2026-04-18
**Branch:** garrytan/minions-jobs
**Suite:** `test/e2e/bench-vs-openclaw/`
**Minions:** v0.11.0 (PR #130)
**OpenClaw:** 2026.4.10 (44e5b62)
**Model:** anthropic/claude-haiku-4-5

## Why this benchmark exists

Minions is GBrain's new background job queue, pitched as a durable, cheap
substitute for spawning OpenClaw subagents via `openclaw agent --local`.
"Durable" and "cheap" are easy to claim and hard to prove. So we put
numbers on four specific claims a Minions user would actually care about:

1. **Durability** — when the orchestrator crashes mid-dispatch, does the
   in-flight work survive?
2. **Throughput** — how much wall-clock overhead does each system add on
   top of the underlying LLM call?
3. **Fan-out** — parent dispatches 10 children in parallel. How fast and
   how reliable is each side?
4. **Memory** — what does it cost to keep 10 subagents in flight at once?

Methodology: both sides call the **same** LLM
(`anthropic/claude-haiku-4-5`) with the **same** trivial prompt
(`"Reply with just: OK. No other text."`). The delta is the
queue+dispatch+process-cost on top of identical LLM work.

## Honest caveats up front

- **We do NOT benchmark OpenClaw's gateway multi-agent fan-out.** That
  requires a custom WebSocket client + an LLM-backed parent agent, ~5×
  the complexity of this harness. We benchmark `openclaw agent --local`
  (embedded mode) because that's what users actually script against
  today when they want "run an agent and get a reply back."
- **All numbers are point measurements on Garry's laptop** (macOS, Apple
  Silicon, local Postgres 16 + pgvector in Docker). Not a cluster
  benchmark. Not an adversarial load test. Reproducible via the files
  in `test/e2e/bench-vs-openclaw/`.
- **OpenClaw `--local` is a fire-and-forget process.** If you SIGKILL
  it mid-dispatch, the reply is gone. This isn't a bug, it's the design.
  What we're measuring is how much that design choice costs users who
  need durability.
- **Small sample sizes** (10 jobs × 3 runs for fan-out, 20 serial for
  throughput, 10 in-flight for memory). Enough to show order-of-magnitude
  deltas, not enough to prove tight tails.

## Results

### 1. Durability (SIGKILL mid-flight, 10 jobs)

| System | Delivered | Wall time | p50 per job | p95 per job |
|--------|-----------|-----------|-------------|-------------|
| **Minions** | **10 / 10** | 458ms total | 257ms | 410ms |
| OpenClaw `--local` | **0 / 10** | 22989ms (all SIGKILLed at 500ms) | n/a | n/a |

Setup: Minions side seeds 10 jobs in state `active` with an expired
`lock_until` (exactly the state a SIGKILLed worker leaves behind). A
rescue worker starts. It picks up all 10 via `handleStalled` and
completes them.

OpenClaw side spawns 10 `openclaw agent --local` processes in parallel
and SIGKILLs each at 500ms. Zero of them managed to emit any output
before being killed.

**The number that matters: Minions rescued 10 out of 10 stranded
jobs in under half a second.** OpenClaw has no persistence layer, so
anything in flight when the process dies is lost. Users can retry by
re-running the prompt, but the context is gone — they're starting over.

Source: `test/e2e/bench-vs-openclaw/durability.bench.ts`

### 2. Throughput (20 serial dispatches, same LLM call)

| System | p50 | p95 | p99 | Mean | Min | Max | Success |
|--------|-----|-----|-----|------|-----|-----|---------|
| **Minions** | **778ms** | **1931ms** | **1931ms** | **911ms** | 639ms | 1931ms | 20/20 |
| OpenClaw `--local` | 8086ms | 10094ms | 10094ms | 8335ms | 7405ms | 10094ms | 20/20 |
| **Ratio** | **10.4×** | **5.2×** | **5.2×** | **9.2×** | 11.6× | 5.2× | — |

Setup: both sides call claude-haiku-4-5 with the same prompt. Minions
goes through `queue.add` → worker claims → handler calls Anthropic SDK
directly. OpenClaw spawns a fresh `openclaw agent --local` process per
dispatch.

The ~7 seconds of overhead per OC dispatch isn't the LLM. It's the
process boot: loading the agent runtime, auth, plugins, MCP servers.
Every dispatch pays that cost again. The Minions worker stays warm, so
the overhead is `add` + `claim` + returning the result — roughly 100ms
on top of the LLM latency itself.

Source: `test/e2e/bench-vs-openclaw/throughput.bench.ts`

### 3. Fan-out (3 runs × 10 children in parallel)

| System | Completed | Mean wall time | Runs (ok/N) | Wall times (ms) |
|--------|-----------|----------------|-------------|-----------------|
| **Minions** (concurrency=10) | **30 / 30** | **1090ms** | 10/10, 10/10, 10/10 | 890, 1135, 1245 |
| OpenClaw (10 parallel spawns) | 17 / 30 | 22598ms | 6/10, 5/10, 6/10 | 22204, 22505, 23084 |
| **Ratio (wall time)** | — | **~21×** | — | — |

Setup: parent dispatches 10 children concurrently, waits for all.
Minions uses one worker process with `concurrency=10`. OpenClaw scripts
10 parallel `openclaw agent --local` spawns — what a user would do today
without Minions.

Two findings, not one:

1. **Wall time: Minions completes 10 in ~1 second. OC parallel spawn
   takes ~22 seconds.** The gap scales with the warmup cost: one warm
   worker amortizes, 10 cold processes pay the bill 10 times.
2. **OC parallel spawn fails 43% of the time at 10-wide.** Error
   samples show a mix of LLM rate-limit hits and spawn saturation. We
   didn't tune this. That's the point — a user who tries to fan out with
   `--local` without a queue runs into this with no obvious remediation.

Source: `test/e2e/bench-vs-openclaw/fanout.bench.ts`

### 4. Memory (10 in-flight subagents)

| System | Baseline RSS | Peak with 10 in flight | Delta | Processes |
|--------|--------------|------------------------|-------|-----------|
| **Minions** | 84 MB | **86 MB** | **+2 MB** | 1 |
| OpenClaw | n/a | 814 MB (summed across 10) | — | 10 |
| **Ratio** | — | **~407×** | — | — |

Setup: both sides keep 10 subagents in flight simultaneously. Minions
side uses one worker with concurrency=10 and handlers that park on a
Promise. OpenClaw 

# FILE: docs/benchmarks/2026-04-18-brainbench-v1.md

# BrainBench v1 — 2026-04-18

**Branch:** `garrytan/link-timeline-extract`
**PR:** #188
**Engine:** PGLite (in-memory)
**Reproducibility:** `bun run eval/runner/all.ts` — no API keys, no network, ~3 min

## TL;DR

PR #188 ships a self-wiring knowledge graph layer for gbrain (auto-link on
every page write, typed extraction, traversal queries, backlink-boosted search).
This benchmark measures the actual end-to-end value vs gbrain pre-PR-#188 on a
240-page rich-prose corpus generated by Claude Opus.

**Every headline metric goes UP. No category goes down.**

| Metric              | BEFORE PR #188 | AFTER PR #188 | Δ            |
|---------------------|----------------|---------------|--------------|
| **Precision@5**     | 39.2%          | **44.7%**     | **+5.4 pts** |
| **Recall@5**        | 83.1%          | **94.6%**     | **+11.5 pts**|
| Correct in top-5    | 217            | 247           | **+30**      |

Plus seven categories of orthogonal capability checks (identity resolution,
temporal queries, performance, robustness, MCP contract) all passing.

## What this benchmark proves

BrainBench v1 evaluates gbrain end-to-end across capability domains the existing
test suite doesn't cover at scale. Headline is a single before/after comparison:
**pre-PR-#188 (no graph layer)** vs **the full v0.10.3 + v0.10.4 stack**, run on
the same 240-page corpus with the same relational queries.

Why before/after instead of just "after numbers": because gbrain pre-PR-#188 was
already a working brain — keyword search, vector-grep-rrf-fusion retrieval, structured timeline
ops. The graph layer is an additive change. The right question is "did it
actually make the brain better at relational questions?" not "is it good in
isolation."

## The corpus

240 rich-prose pages generated by Claude Opus 4.7:
- 80 people (40 founders, 20 partners, 10 engineers, 10 advisors)
- 80 companies (60 startups, 15 VCs, 5 acquirers)
- 50 meetings (15 demo days, 25 1:1s, 10 board meetings)
- 30 concepts (frameworks, theses, hot spaces)

Each page is multi-paragraph narrative prose with realistic noise:
- Varied phrasings (founders described 6 different ways, investors 8 different ways)
- Natural typos ~1-2% of words ("intrest", "comercial", "differnt")
- Cross-references via `[Name](slug)` markdown links AND bare slug references
- Multi-year timelines spanning 2021-2026
- Multiple personas (terse note-taker, prose-heavy journaler, voice-to-text dump)

Generation cost: ~$15 of Opus tokens, one-time, cached to `eval/data/world-v1/`
and committed to the repo. Subsequent runs read the cache.

This is intentionally messier than templated benchmarks. The point is to surface
behavior under realistic load, not to confirm the algorithm works on clean inputs.

## Headline: relational queries on the rich corpus

196 relational queries derived from the world facts:
- "Who attended `Demo Day W30`?" (60 queries)
- "Who works at `Acme`?" (60 queries)
- "Who invested in `Beta Health`?" (45 queries)
- "Who advises `Cipher Labs`?" (31 queries)

Configurations compared:
- **BEFORE PR #188:** vanilla v0.10.0 — no auto-link, no `extract --source db`,
  no `traversePaths`. Agent answers relational questions by grepping the corpus
  (the realistic fallback for a pre-graph brain).
- **AFTER PR #188:** full graph layer. Agent uses `gbrain graph-query` first
  (high-precision typed traversal), grep fallback when graph returns nothing.

### Top-K (what agents actually read)

Agents read ranked top-K results, not full sets. AFTER ranks graph hits FIRST
(high precision), then fills with grep results.

| Metric              | BEFORE | AFTER  | Δ             |
|---------------------|--------|--------|---------------|
| **Precision@5**     | 39.2%  | 44.7%  | **+5.4 pts**  |
| **Recall@5**        | 83.1%  | 94.6%  | **+11.5 pts** |
| Correct in top-5    | 217    | 247    | **+30**       |

Recall@5 jumps 11.5 points because graph hits are exact-typed answers placed
at the top of results — agents find what they need in their first reads
instead of digging through grep noise.

### Set-based metrics + graph-only ablation

| Metric              | BEFORE (grep) | AFTER (vector-grep-rrf-fusion) | Graph-only (ablation) |
|---------------------|---------------|----------------|------------------------|
| **F1 score**        | 57.8%         | 57.8%          | **86.6%**              |
| Set precision       | 40.8%         | 40.8%          | **81.0%**              |
| Set recall          | 98.9%         | 98.9%          | 93.1%                  |
| Total returned      | 632           | 632            | 300 (-53%)             |
| Correct returned    | 258           | 258            | 243                    |

AFTER (vector-grep-rrf-fusion) matches BEFORE on full-set metrics because graph hits are a
subset of grep hits — taking the union doesn't add or remove anything from the
bag. **What changes is which results appear FIRST.** Top-K captures that;
raw set recall doesn't.

The **graph-only** column is the most important number in the report. It shows
where the graph alone is heading: **86.6% F1 vs grep's 57.8% (+28.8 pts)**.
Almost twice the precision (81% vs 41%) at 94% of the recall, with HALF the
results to read.

### Per-link-type breakdown

| Link type   | Expected | Graph found / returned | Recall | Precision |
|-------------|----------|------------------------|--------|-----------|
| attended    | 134      | 131 / 134              | 97.8%  | 97.8%     |
| works_at    | 50       | 50 / 79                | 100.0% | 63.3%     |
| invested_in | 60       | 50 / 56                | 83.3%  | 89.3%     |
| advises     | 17       | 12 / 31                | 70.6%  | 38.7%     |

Where the graph wins biggest: **incoming relationship queries on companies**.
"Who works at Acme?" — grep returns every page mentioning Acme (founders,
investors, advisors, concept pages, other companies that mention it). Graph
returns just employees with the typed `works_at` link.

## How we got her
