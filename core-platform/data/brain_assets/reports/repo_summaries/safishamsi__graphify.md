# Repo Summary Source: safishamsi/graphify
- URL: https://github.com/safishamsi/graphify
- Local Path: core-platform/data/brain_assets/repos/github_stars/safishamsi__graphify
- Buckets: agent, rag, video
- Stars: 47241
- Language: Python
- Description: AI coding assistant skill (Claude Code, Codex, OpenCode, Cursor, Gemini CLI, and more). Turn any folder of code, SQL schemas, R scripts, shell scripts, docs, papers, images, or videos into a queryable knowledge graph. App code + database schema + infrastructure in one graph.
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

<p align="center">
  <a href="https://graphifylabs.ai"><img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/></a>
</p>

<p align="center">
  🇺🇸 <a href="README.md">English</a> | 🇨🇳 <a href="docs/translations/README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="docs/translations/README.ja-JP.md">日本語</a> | 🇰🇷 <a href="docs/translations/README.ko-KR.md">한국어</a> | 🇩🇪 <a href="docs/translations/README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="docs/translations/README.fr-FR.md">Français</a> | 🇪🇸 <a href="docs/translations/README.es-ES.md">Español</a> | 🇮🇳 <a href="docs/translations/README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="docs/translations/README.pt-BR.md">Português</a> | 🇷🇺 <a href="docs/translations/README.ru-RU.md">Русский</a> | 🇸🇦 <a href="docs/translations/README.ar-SA.md">العربية</a> | 🇮🇹 <a href="docs/translations/README.it-IT.md">Italiano</a> | 🇵🇱 <a href="docs/translations/README.pl-PL.md">Polski</a> | 🇳🇱 <a href="docs/translations/README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="docs/translations/README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="docs/translations/README.uk-UA.md">Українська</a> | 🇻🇳 <a href="docs/translations/README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="docs/translations/README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="docs/translations/README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="docs/translations/README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="docs/translations/README.ro-RO.md">Română</a> | 🇨🇿 <a href="docs/translations/README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="docs/translations/README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="docs/translations/README.da-DK.md">Dansk</a> | 🇳🇴 <a href="docs/translations/README.no-NO.md">Norsk</a> | 🇭🇺 <a href="docs/translations/README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="docs/translations/README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="docs/translations/README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://safishamsi.gumroad.com/l/qetvlo"><img src="https://img.shields.io/badge/Book-The%20Memory%20Layer-2ea44f?style=flat&logo=gitbook&logoColor=white" alt="The Memory Layer"/></a>
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v7" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://clickpy.clickhouse.com/dashboard/graphifyy"><img src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fsql-clickhouse.clickhouse.com%2F%3Fquery%3DSELECT%2520concat%2528toString%2528round%2528sum%2528count%2529%2F1000%2529%2529%2C%2520%2527k%2527%2529%2520AS%2520c%2520FROM%2520pypi.pypi_downloads%2520WHERE%2520project%253D%2527graphifyy%2527%2520FORMAT%2520JSON%26user%3Ddemo&query=%24.data%5B0%5D.c&label=downloads&color=blue" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
  <a href="https://x.com/graphifyy"><img src="https://img.shields.io/badge/X-graphifyy-000000?logo=x&logoColor=white" alt="X"/></a>
</p>

<p align="center">
  <a href="https://star-history.com/#safishamsi/graphify&Date">
    <img src="https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date" alt="Star History Chart" width="370"/>
  </a>
</p>

Type `/graphify` in your AI coding assistant and it maps your entire project — code, docs, PDFs, images, videos — into a knowledge graph you can query instead of grepping through files.

Works in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kimi Code, Kiro, Pi, and Google Antigravity.

```
/graphify .
```

That's it. You get three files:

```
graphify-out/
├── graph.html       open in any browser — click nodes, filter, search
├── GRAPH_REPORT.md  the highlights: key concepts, surprising connections, suggested questions
└── graph.json       the full graph — query it anytime without re-reading your files
```

For a readable architecture page with Mermaid call-flow diagrams, run:

```bash
graphify export callflow-html
```

---

## Install

**Requires Python 3.10+**

```bash
uv tool install graphifyy && graphify install
# or: pipx install graphifyy && graphify install
# or: pip install graphifyy && graphify install
```

> **Official package:** The PyPI package is `graphifyy` (double-y). Other `graphify*` packages on PyPI are not affiliated. The CLI command is still `graphify`.

> **PowerShell note:** Use `graphify .` not `/graphify .` — the leading slash is a path separator in PowerShell and will cause a "not recognized" error.

> **`graphify: command not found`?** Use `uv tool install graphifyy` or `pipx install graphifyy` — both put the CLI on PATH automatically. With plain `pip`, add `~/.local/bin` (Linux) or `~/Library/Python/3.x/bin` (Mac) to your PATH, or run `python -m graphify`.

### Pick your platform

| Platform | Install command |
|----------|----------------|
| Claude Code (Linux/Mac) | `graphify install` |
| Claude Code (Windows) | `graphify install --platform windows` |
| Codex | `graphify install --platform codex` |
| OpenCode | `graphify install --platform opencode` |
| GitHub Copilot CLI | `graphify install --platform copilot` |
| VS Code Copilot Chat | `graphify vscode install` |
| Aider | `graphify install --platform aider` |
| OpenClaw | `graphify install --platform claw` |
| Factory Droid | `graphify install --platform droid` |
| Trae | `graphify install --platform trae` |
| Trae CN | `graphify install --platform trae-cn` |
| Gemini CLI | `graphify install --platform gemini` |
| Hermes | `graphify install --platform hermes` |
| Kimi Code | `graphify install --platform kimi` |
| Kir


# FILE: docs/how-it-works.md

# How graphify works

## The three passes

graphify processes your files in three passes:

**Pass 1 — Code structure (free, no API calls)**
Tree-sitter parses your code files and extracts classes, functions, imports, call graphs, and inline comments. This runs locally with no LLM involved. 25 languages supported. SQL files get special treatment: tables, views, foreign keys, and JOIN relationships are extracted deterministically.

**Pass 2 — Video and audio (local, no API calls)**
Video and audio files are transcribed with faster-whisper. To focus the transcript on your domain, the transcription prompt is seeded with your top god nodes (the most-connected concepts in your code graph so far). Transcripts are cached — re-runs skip already-processed files.

**Pass 3 — Docs, papers, images (Claude subagents, costs tokens)**
Claude runs in parallel over markdown, PDFs, images, and transcripts. Each subagent reads a batch of files and outputs a JSON fragment: nodes, edges, and any group relationships. The fragments are merged into a single graph.

Before Pass 3, optional converters turn supported pointer/binary formats into
Markdown sidecars under `graphify-out/converted/`. Office files (`.docx`,
`.xlsx`) use the `[office]` extra. Google Workspace shortcuts (`.gdoc`,
`.gsheet`, `.gslides`) are opt-in with `--google-workspace` or
`GRAPHIFY_GOOGLE_WORKSPACE=1` and require an authenticated `gws` CLI.

---

## How community detection works

Communities are found using the [Leiden algorithm](https://www.nature.com/articles/s41598-019-41695-z) — a graph-clustering method that groups nodes by edge density. Nodes with many connections between them end up in the same community.

**No embeddings needed.** The semantic similarity edges that Claude extracts (`semantically_similar_to`) are already in the graph, so they influence community shape directly. The graph structure is the similarity signal — there's no separate embedding step or vector database.

---

## Confidence tagging

Every relationship is tagged with one of three labels:

| Tag | Meaning |
|-----|---------|
| `EXTRACTED` | Found directly in the source (e.g. a function call, an import) |
| `INFERRED` | A reasonable inference Claude made, with a `confidence_score` (0.0–1.0) |
| `AMBIGUOUS` | Uncertain — flagged in the report for manual review |

EXTRACTED edges always have confidence 1.0. INFERRED edges use a discrete rubric:
- **0.95** — near-certain (explicit cross-file reference, one plausible target)
- **0.85** — strong evidence (naming + context align)
- **0.75** — reasonable (contextual but not explicit)
- **0.65** — weak (naming similarity only)
- **0.55** — speculative

---

## Token benchmark

The first run extracts and builds the graph — this costs tokens. Every subsequent query reads the compact graph instead of raw files. That's where the savings compound.

On a mixed corpus (Karpathy repos + 5 papers + 4 images, 52 files): **71.5x fewer tokens per query** vs reading the raw files directly.

| Corpus | Files | Reduction |
|--------|-------|-----------|
| Karpathy repos + papers + images | 52 | **71.5x** |
| graphify source + Transformer paper | 4 | **5.4x** |
| httpx (synthetic Python library) | 6 | ~1x |

Token reduction scales with corpus size. Six files already fits in a context window — the graph value there is structural clarity, not compression. At 52 files the savings compound quickly.

Each `worked/` folder in the repo has the raw input files and actual output (`GRAPH_REPORT.md`, `graph.json`) so you can run it yourself and verify.

---

## Parallel extraction

Code files are extracted in parallel using `ProcessPoolExecutor` — bypasses Python's GIL for genuine multiprocessing. Doc/paper/image batches are dispatched as parallel Claude subagents. On a corpus of 84 code files, parallel AST extraction runs in about 1.66x less time than sequential.

---

## SHA256 cache

Every extracted file is fingerprinted by content hash. Re-runs skip unchanged files entirely — only new or modified files go through extraction again. The cache lives in `graphify-out/cache/`.

---

## The graph format

The output `graph.json` uses NetworkX's node-link format. Each node has:
- `id` — stable identifier
- `label` — human-readable name
- `file_type` — `code`, `document`, `paper`, `image`, `rationale`
- `source_file` — where it came from

Each edge has:
- `source`, `target` — node IDs
- `relation` — verb phrase (e.g. `calls`, `imports`, `implements`, `semantically_similar_to`)
- `confidence` — `EXTRACTED`, `INFERRED`, or `AMBIGUOUS`
- `confidence_score` — float (INFERRED only)
- `source_file` — where the relationship was found

Hyperedges (group relationships connecting 3+ nodes) live in `G.graph["hyperedges"]`.



# FILE: docs/docker-mcp-sqlite.md

# Docker MCP Toolkit + SQLite MCP server

A reproducible runbook for installing the **SQLite MCP server** into the
[Docker MCP Toolkit](https://docs.docker.com/desktop/features/mcp/) so any
connected MCP client (Claude Code, Claude Desktop, Cursor, VS Code, etc.) gains
six SQLite tools: `read_query`, `write_query`, `create_table`, `list_tables`,
`describe_table`, and `append_insight`.

This document is *not* required to use graphify — it lives here as a known-good
recipe for users who want a lightweight, persistent SQL workspace exposed to
their AI clients alongside graphify's knowledge-graph tools.

## Why SQLite (and not `sqlite-mcp-server`)
At time of writing the catalog ships two SQLite MCP images:

| Catalog name        | Image                  | Status |
| ------------------- | ---------------------- | ------ |
| `SQLite`            | `mcp/sqlite`           | Marked "Archived" in catalog metadata, but **boots and serves correctly** |
| `sqlite-mcp-server` | `mcp/sqlite-mcp-server`| **Broken**: entrypoint `/app/.venv/bin/mcp-server-sqlite` does not exist in the published layer |

Use `SQLite` (`mcp/sqlite`) until the newer image is fixed upstream.

## Prerequisites
- Docker Desktop running and healthy
  - `docker info` returns a `Server Version`
  - Public socket present at `/var/run/docker.sock` (or its symlink to
    `~/.docker/run/docker.sock`)
- Docker MCP Toolkit CLI plugin (`docker mcp`)
  - Bundled with recent Docker Desktop releases; `docker mcp --version` should
    print a version string

## Install
```bash
# Add the working SQLite server to the default MCP profile
docker mcp profile server add default \
  --server catalog://mcp/docker-mcp-catalog/SQLite

# Pre-pull the image so the first tool call is fast
docker pull mcp/sqlite:latest
```

Verify the profile now contains both `fetch` (built-in) and `SQLite`:
```bash
docker mcp profile show default | grep -E '^[[:space:]]+name:'
```

Expected output:
```
            name: fetch
            name: SQLite
```

The Docker MCP gateway should now expose 6 additional tools:
```bash
docker mcp tools count
# → 15 tools (was 9 before adding SQLite)
```

## Smoke test
The CLI can call MCP tools directly (each call boots a fresh gateway, ~5s
overhead per call):
```bash
docker mcp tools call list_tables
docker mcp tools call create_table \
  query='CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, body TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)'
docker mcp tools call write_query \
  query="INSERT INTO notes(body) VALUES ('first row'), ('second row')"
docker mcp tools call read_query \
  query='SELECT * FROM notes ORDER BY id'
docker mcp tools call describe_table table_name=notes
docker mcp tools call append_insight insight='3 rows inserted; aggregates work.'
```

`read_query` should return the inserted rows with timestamps.

## Storage layout
Database file lives in a Docker named volume `mcp-sqlite`, mounted at `/mcp`
inside containers:
```
mcp-sqlite (named volume) → /mcp/db.sqlite
```

Inspect from the host:
```bash
docker volume inspect mcp-sqlite
docker run --rm -v mcp-sqlite:/mcp:ro alpine ls -la /mcp
docker run --rm -v mcp-sqlite:/mcp:ro keinos/sqlite3 \
  sqlite3 /mcp/db.sqlite '.schema'
```

The volume persists across `docker run --rm` invocations of the SQLite MCP
container, so writes from one MCP tool call are visible to the next.

## Wiring into MCP clients
Connect once per client; the gateway exposes every server in the active profile:
```bash
docker mcp client connect claude-code   # already connected for many users
docker mcp client connect cursor
docker mcp client connect vscode
docker mcp client connect claude-desktop
# Supported: claude-code, claude-desktop, cline, codex, continue, crush,
#            cursor, gemini, goose, gordon, kiro, lmstudio, opencode, sema4,
#            vscode, zed
```

Verify wiring:
```bash
docker mcp client ls
```

## Uninstall / reset
```bash
# Remove server from the profile
docker mcp profile server remove default SQLite

# Drop the database volume (irreversible)
docker volume rm mcp-sqlite

# Remove the image
docker rmi mcp/sqlite:latest
```

## Troubleshooting
- **`starting client: calling "initialize": EOF`** — the requested server
  failed its MCP handshake. Run the image directly to see the error:
  ```bash
  printf '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"smoke","version":"0.0"}}}\n' \
    | docker run --rm -i -v mcp-sqlite:/mcp <image-ref> --db-path /mcp/db.sqlite
  ```
  Common causes: missing entrypoint binary in the image (the
  `sqlite-mcp-server` failure mode) or missing required env/secrets.
- **`cannot use --enable-all-servers with --servers flag`** — these gateway
  args are mutually exclusive; pick one.
- **No new tools appear in `docker mcp tools count` after install** — the
  gateway may be running with `dynamic-tools` enabled, exposing only meta-tools
  (`mcp-add`, `mcp-find`, …) until a profile is activated mid-session. Either
  invoke `docker mcp tools` (which spins up an ephemeral gateway against the
  default profile) or call `mcp-activate-profile` from inside an MCP session.



# FILE: docs/translations/README.no-NO.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**En ferdighet for AI-kodeassistenter.** Skriv `/graphify` i Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro eller Google Antigravity — den leser filene dine, bygger en kunnskapsgraf og gir deg tilbake strukturen du ikke visste eksisterte. Forstå en kodebase raskere. Finn «hvorfor» bak arkitektoniske beslutninger.

Fullt multimodal. Legg til kode, PDF-er, markdown, skjermbilder, diagrammer, whiteboardbilder, bilder på andre språk eller video- og lydfiler — graphify ekstraherer begreper og relasjoner fra alt og kobler dem i én graf. Videoer transkriberes lokalt med Whisper. Støtter 25 programmeringsspråk via tree-sitter AST.

> Andrej Karpathy opprettholder en `/raw`-mappe der han legger artikler, tweets, skjermbilder og notater. graphify er svaret på det problemet — **71,5x** færre tokens per spørring sammenlignet med å lese råfiler, vedvarende mellom sesjoner.

```
/graphify .
```

```
graphify-out/
├── graph.html       interaktiv graf — åpne i en hvilken som helst nettleser
├── GRAPH_REPORT.md  gudnoder, overraskende forbindelser, foreslåtte spørsmål
├── graph.json       vedvarende graf — forespørselbar uker senere
└── cache/           SHA256-cache — gjentatte kjøringer behandler bare endrede filer
```

## Hvordan det fungerer

graphify arbeider i tre gjennomganger. Først ekstraherer et deterministisk AST-gjennomgang struktur fra kodefiler uten LLM. Deretter transkriberes video- og lydfiler lokalt med faster-whisper. Til slutt kjører Claude-underagenter parallelt på dokumenter, artikler, bilder og transkripsjoner. Resultatene slås sammen i en NetworkX-graf, klynges med Leiden og eksporteres som interaktiv HTML, forespørselbar JSON og revisjonsrapport.

Hver relasjon er merket `EXTRACTED`, `INFERRED` (med konfidenspoeng) eller `AMBIGUOUS`.

## Installasjon

**Krav:** Python 3.10+ og én av: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) og andre.

```bash
uv tool install graphifyy && graphify install
# eller med pipx
pipx install graphifyy && graphify install
# eller pip
pip install graphifyy && graphify install
```

> **Offisiell pakke:** PyPI-pakken heter `graphifyy`. Det eneste offisielle depotet er [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Bruk

```
/graphify .
/graphify ./raw --update
/graphify query "hva kobler Attention til optimizeren?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Hva du får

**Gudnoder** — begreper med høyest grad · **Overraskende forbindelser** — rangert etter poeng · **Foreslåtte spørsmål** · **«Hvorfor»** — docstrings og designbegrunnelse ekstrahert som noder · **Token-benchmark** — **71,5x** færre tokens på blandet korpus.

## Personvern

Kodefiler behandles lokalt via tree-sitter AST. Videoer transkriberes lokalt med faster-whisper. Ingen telemetri.

## Bygget på graphify — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) er enterprise-laget oppå graphify. **Gratis prøveperiode kommer snart.** [Bli med på ventelisten →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)



# FILE: docs/translations/README.it-IT.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**Una skill per assistenti di codice IA.** Scrivi `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro o Google Antigravity — legge i tuoi file, costruisce un grafo della conoscenza e ti restituisce struttura che non sapevi esistesse. Comprendi una codebase più velocemente. Trova il "perché" dietro le decisioni architetturali.

Completamente multimodale. Aggiungi codice, PDF, markdown, screenshot, diagrammi, foto di lavagne, immagini in altre lingue, o file video e audio — graphify estrae concetti e relazioni da tutto e li connette in un unico grafo. I video vengono trascritti localmente con Whisper. Supporta 25 linguaggi di programmazione via tree-sitter AST.

> Andrej Karpathy mantiene una cartella `/raw` dove deposita paper, tweet, screenshot e note. graphify è la risposta a quel problema — **71,5x** meno token per query rispetto alla lettura dei file grezzi, persistente tra le sessioni.

```
/graphify .                        # funziona con qualsiasi cartella
```

```
graphify-out/
├── graph.html       grafo interattivo — apri in qualsiasi browser
├── GRAPH_REPORT.md  nodi dio, connessioni sorprendenti, domande suggerite
├── graph.json       grafo persistente — interrogabile settimane dopo
└── cache/           cache SHA256 — le riesecuzioni elaborano solo i file modificati
```

## Come funziona

graphify esegue in tre passaggi. Prima, un passaggio AST deterministico estrae la struttura dai file di codice senza LLM. Poi, i file video e audio vengono trascritti localmente con faster-whisper. Infine, i subagenti Claude eseguono in parallelo su documenti, paper, immagini e trascrizioni. I risultati vengono uniti in un grafo NetworkX, raggruppati con Leiden e esportati come HTML interattivo, JSON interrogabile e report di audit.

Ogni relazione è etichettata `EXTRACTED`, `INFERRED` (con punteggio di confidenza) o `AMBIGUOUS`.

## Installazione

**Requisiti:** Python 3.10+ e uno tra: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Aider](https://aider.chat) e altri.

```bash
uv tool install graphifyy && graphify install
# oppure con pipx
pipx install graphifyy && graphify install
# oppure pip
pip install graphifyy && graphify install
```

> **Pacchetto ufficiale:** Il pacchetto PyPI si chiama `graphifyy`. L'unico repository ufficiale è [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Utilizzo

```
/graphify .
/graphify ./raw --update           # solo file modificati
/graphify ./raw --mode deep
/graphify query "cosa connette Attention all'ottimizzatore?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Cosa ottieni

**Nodi dio** — concetti con il grado più alto · **Connessioni sorprendenti** — classificate per punteggio · **Domande suggerite** — 4-5 domande che il grafo è in grado di rispondere in modo unico · **Il "perché"** — docstring e rationale di design estratti come nodi · **Benchmark token** — **71,5x** meno token su corpus misto.

## Privacy

I file di codice vengono elaborati localmente via tree-sitter AST. I video vengono trascritti localmente con faster-whisper. Nessuna telemetria.

## Costruito su graphify — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) è il livello enterprise su graphify. **Prova gratuita in arrivo.** [Unisciti alla lista d'attesa →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)



# FILE: docs/translations/README.ar-SA.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

<div dir="rtl">

**مهارة لمساعد برمجة الذكاء الاصطناعي.** اكتب `/graphify` في Claude Code أو Codex أو OpenCode أو Cursor أو Gemini CLI أو GitHub Copilot CLI أو VS Code Copilot Chat أو Aider أو OpenClaw أو Factory Droid أو Trae أو Hermes أو Kiro أو Google Antigravity — يقرأ ملفاتك ويبني رسماً بيانياً للمعرفة ويعيد إليك البنية التي لم تكن تعلم بوجودها. افهم قاعدة الكود بشكل أسرع. اكتشف "السبب" وراء القرارات المعمارية.

متعدد الوسائط بالكامل. أضف كوداً أو ملفات PDF أو markdown أو لقطات شاشة أو رسوماً بيانية أو صور سبورة أو صوراً بلغات أخرى أو ملفات فيديو وصوت — يستخرج graphify المفاهيم والعلاقات من كل ذلك ويربطها في رسم بياني واحد. يتم نسخ مقاطع الفيديو محلياً باستخدام Whisper. يدعم 25 لغة برمجة عبر tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> يحتفظ Andrej Karpathy بمجلد `/raw` يضع فيه الأوراق البحثية والتغريدات ولقطات الشاشة والملاحظات. graphify هو الإجابة على تلك المشكلة — **71.5 مرة** أقل في الرموز لكل استعلام مقارنةً بقراءة الملفات الخام، مستمر عبر الجلسات، صادق حول ما تم العثور عليه مقابل ما تم استنتاجه.

</div>

```
/graphify .                        # يعمل مع أي مجلد — الكود، الملاحظات، الأوراق البحثية، كل شيء
```

```
graphify-out/
├── graph.html       رسم بياني تفاعلي — افتحه في أي متصفح، انقر على العقد، ابحث، صفّ
├── GRAPH_REPORT.md  عقد الإله، الاتصالات المفاجئة، الأسئلة المقترحة
├── graph.json       رسم بياني دائم — استعلم بعد أسابيع دون إعادة القراءة
└── cache/           ذاكرة تخزين مؤقت SHA256 — إعادة التشغيل تعالج الملفات المتغيرة فقط
```

<div dir="rtl">

أضف ملف `.graphifyignore` لاستبعاد المجلدات:

</div>

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

<div dir="rtl">

نفس صيغة `.gitignore`.

## كيف يعمل

يعمل graphify في ثلاث مراحل. أولاً، تمريرة AST حتمية تستخرج البنية من ملفات الكود (الفئات، الدوال، الاستيرادات، رسوم بيانية الاستدعاء، docstrings، تعليقات المبرر) — دون الحاجة إلى LLM. ثانياً، يتم نسخ ملفات الفيديو والصوت محلياً باستخدام faster-whisper. ثالثاً، تعمل عوامل Claude الفرعية بالتوازي على المستندات والأوراق البحثية والصور والنصوص المكتوبة لاستخراج المفاهيم والعلاقات ومبررات التصميم. يتم دمج النتائج في رسم بياني NetworkX وتجميعها باستخدام Leiden وتصديرها كـ HTML تفاعلي وJSON قابل للاستعلام وتقرير تدقيق بلغة طبيعية.

**التجميع مبني على طوبولوجيا الرسم البياني — بدون embeddings.** يجد Leiden المجتمعات بواسطة كثافة الحواف. حواف التشابه الدلالي التي يستخرجها Claude (`semantically_similar_to`، مصنفة INFERRED) موجودة بالفعل في الرسم البياني. بنية الرسم البياني هي إشارة التشابه — لا حاجة لخطوة embedding منفصلة أو قاعدة بيانات متجهية.

كل علاقة مصنفة كـ `EXTRACTED` (وجدت مباشرة في المصدر) أو `INFERRED` (استنتاج معقول مع درجة ثقة) أو `AMBIGUOUS` (مُعلَّمة للمراجعة).

## التثبيت

**المتطلبات:** Python 3.10+ وواحد من: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes, أو [Google Antigravity](https://antigravity.google)

</div>

```bash
# موصى به — يعمل على Mac وLinux دون إعداد PATH
uv tool install graphifyy && graphify install
# أو مع pipx
pipx install graphifyy && graphify install
# أو pip العادي
pip install graphifyy && graphify install
```

<div dir="rtl">

> **الحزمة الرسمية:** اسم حزمة PyPI هو `graphifyy` (تثبيت بـ `pip install graphifyy`). الحزم الأخرى المسماة `graphify*` على PyPI ليست تابعة لهذا المشروع. المستودع الرسمي الوحيد هو [safishamsi/graph


# FILE: docs/translations/README.id-ID.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**Keterampilan untuk asisten kode AI.** Ketik `/graphify` di Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro, atau Google Antigravity — membaca file Anda, membangun graf pengetahuan, dan mengembalikan struktur yang tidak Anda ketahui ada. Pahami codebase lebih cepat. Temukan "mengapa" di balik keputusan arsitektur.

Sepenuhnya multimodal. Tambahkan kode, PDF, markdown, tangkapan layar, diagram, foto papan tulis, gambar dalam bahasa lain, atau file video dan audio — graphify mengekstrak konsep dan hubungan dari semuanya dan menghubungkannya dalam satu graf. Video ditranskrip secara lokal dengan Whisper. Mendukung 25 bahasa pemrograman melalui tree-sitter AST.

> Andrej Karpathy memelihara folder `/raw` tempat ia menyimpan makalah, tweet, tangkapan layar, dan catatan. graphify adalah jawaban untuk masalah itu — **71,5x** lebih sedikit token per kueri dibandingkan membaca file mentah, persisten di antara sesi.

```
/graphify .
```

```
graphify-out/
├── graph.html       graf interaktif — buka di browser mana saja
├── GRAPH_REPORT.md  node dewa, koneksi mengejutkan, pertanyaan yang disarankan
├── graph.json       graf persisten — dapat dikueri berminggu-minggu kemudian
└── cache/           cache SHA256 — pengulangan hanya memproses file yang berubah
```

## Cara Kerja

graphify bekerja dalam tiga tahap. Pertama, tahap AST deterministik mengekstrak struktur dari file kode tanpa LLM. Kemudian file video dan audio ditranskrip secara lokal dengan faster-whisper. Terakhir, sub-agen Claude berjalan secara paralel pada dokumen, makalah, gambar, dan transkripsi. Hasilnya digabungkan ke dalam graf NetworkX, dikelompokkan dengan Leiden, dan diekspor sebagai HTML interaktif, JSON yang dapat dikueri, dan laporan audit.

Setiap hubungan diberi label `EXTRACTED`, `INFERRED` (dengan skor kepercayaan), atau `AMBIGUOUS`.

## Instalasi

**Persyaratan:** Python 3.10+ dan salah satu dari: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) dan lainnya.

```bash
uv tool install graphifyy && graphify install
# atau dengan pipx
pipx install graphifyy && graphify install
# atau pip
pip install graphifyy && graphify install
```

> **Paket resmi:** Paket PyPI bernama `graphifyy`. Satu-satunya repositori resmi adalah [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Penggunaan

```
/graphify .
/graphify ./raw --update
/graphify query "apa yang menghubungkan Attention dengan optimizer?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Apa yang Anda Dapatkan

**Node dewa** — konsep dengan derajat tertinggi · **Koneksi mengejutkan** — diurutkan berdasarkan skor · **Pertanyaan yang disarankan** · **"Mengapa"** — docstring dan alasan desain diekstrak sebagai node · **Benchmark token** — **71,5x** lebih sedikit token pada corpus campuran.

## Privasi

File kode diproses secara lokal melalui tree-sitter AST. Video ditranskrip secara lokal dengan faster-whisper. Tidak ada telemetri.

## Dibangun di atas graphify — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) adalah lapisan enterprise di atas graphify. **Uji coba gratis segera hadir.** [Bergabunglah dengan daftar tunggu →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)



# FILE: docs/translations/README.de-DE.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

**Eine KI-Coding-Assistent-Skill.** Tippe `/graphify` in Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro oder Google Antigravity — es liest deine Dateien, baut einen Wissensgraphen und gibt dir Struktur zurück, die du vorher nicht sehen konntest. Verstehe eine Codebasis schneller. Finde das „Warum" hinter Architekturentscheidungen.

Vollständig multimodal. Leg Code, PDFs, Markdown, Screenshots, Diagramme, Whiteboard-Fotos, Bilder in anderen Sprachen oder Video- und Audiodateien ab — graphify extrahiert Konzepte und Beziehungen aus allem und verbindet sie in einem einzigen Graphen. Videos werden lokal mit Whisper transkribiert, angetrieben durch einen domänenspezifischen Prompt aus deinem Korpus. 25 Programmiersprachen werden über tree-sitter AST unterstützt (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Andrej Karpathy führt einen `/raw`-Ordner, in dem er Papers, Tweets, Screenshots und Notizen ablegt. graphify ist die Antwort auf dieses Problem — 71,5-fach weniger Tokens pro Abfrage gegenüber dem Lesen der Rohdateien, persistent über Sitzungen hinweg, ehrlich darüber, was gefunden vs. erschlossen wurde.

```
/graphify .                        # funktioniert mit jedem Ordner — Codebase, Notizen, Papers, alles
```

```
graphify-out/
├── graph.html       interaktiver Graph — im Browser öffnen, Knoten anklicken, suchen, filtern
├── GRAPH_REPORT.md  Gott-Knoten, überraschende Verbindungen, vorgeschlagene Fragen
├── graph.json       persistenter Graph — Wochen später abfragen, ohne neu zu lesen
└── cache/           SHA256-Cache — erneute Ausführungen verarbeiten nur geänderte Dateien
```

Füge eine `.graphifyignore`-Datei hinzu, um Ordner auszuschließen:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Gleiche Syntax wie `.gitignore`. Du kannst eine einzelne `.graphifyignore` im Repo-Stammverzeichnis behalten — Muster funktionieren korrekt, auch wenn graphify auf einem Unterordner ausgeführt wird.

## So funktioniert es

graphify läuft in drei Durchgängen. Zuerst extrahiert ein deterministischer AST-Durchgang Strukturen aus Code-Dateien (Klassen, Funktionen, Importe, Aufrufgraphen, Docstrings, Begründungskommentare) — ohne LLM. Zweitens werden Video- und Audiodateien lokal mit faster-whisper transkribiert, angetrieben durch einen domänenspezifischen Prompt aus Korpus-Gott-Knoten — Transkripte werden gecacht, sodass erneute Ausführungen sofort sind. Drittens laufen Claude-Subagenten parallel über Dokumente, Papers, Bilder und Transkripte, um Konzepte, Beziehungen und Designbegründungen zu extrahieren. Die Ergebnisse werden in einem NetworkX-Graphen zusammengeführt, mit Leiden-Community-Erkennung geclustert und als interaktives HTML, abfragbares JSON und ein Klartext-Audit-Report exportiert.

**Clustering basiert auf Graph-Topologie — keine Embeddings.** Leiden findet Communities durch Kantendichte. Die semantischen Ähnlichkeitskanten, die Claude extrahiert (`semantically_similar_to`, markiert als INFERRED), sind bereits im Graphen, sodass sie die Community-Erkennung direkt beeinflussen. Die Graphstruktur ist das Ähnlichkeitssignal — kein separater Embedding-Schritt oder Vektordatenbank nötig.

Jede Beziehung ist markiert als `EXTRACTED` (direkt in der Quelle gefunden), `INFERRED` (begründete Schlussfolgerung mit Konfidenzwert) oder `AMBIGUOUS` (zur Überprüfung markiert). Du weißt immer, was gefunden vs. erschlossen wurde.

## Installation

**Voraussetzungen:** Python 3.10+ und eines von: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github


# FILE: docs/translations/README.ru-RU.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
  <a href="https://www.linkedin.com/in/safi-shamsi"><img src="https://img.shields.io/badge/LinkedIn-Safi%20Shamsi-0077B5?logo=linkedin" alt="LinkedIn"/></a>
</p>

**Навык для AI-ассистента по написанию кода.** Введите `/graphify` в Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro или Google Antigravity — он прочитает ваши файлы, построит граф знаний и вернёт вам структуру, о существовании которой вы не подозревали. Понимайте кодовую базу быстрее. Находите «почему» за архитектурными решениями.

Полностью мультимодальный. Добавляйте код, PDF, markdown, скриншоты, диаграммы, фотографии досок, изображения на других языках, видео и аудиофайлы — graphify извлекает концепции и связи из всего этого и объединяет их в один граф. Видео транскрибируются локально с Whisper, используя доменный промпт из вашего корпуса. Поддерживается 25 языков программирования через tree-sitter AST (Python, JS, TS, Go, Rust, Java, C, C++, Ruby, C#, Kotlin, Scala, PHP, Swift, Lua, Zig, PowerShell, Elixir, Objective-C, Julia, Verilog, SystemVerilog, Vue, Svelte, Dart).

> Андрей Карпати ведёт папку `/raw`, куда складывает статьи, твиты, скриншоты и заметки. graphify — ответ на эту проблему: в **71,5 раза** меньше токенов на запрос по сравнению с чтением сырых файлов, сохранение между сессиями, честность относительно того, что найдено, а что выведено.

```
/graphify .                        # работает с любой папкой — код, заметки, статьи, всё что угодно
```

```
graphify-out/
├── graph.html       интерактивный граф — открыть в браузере, кликать по узлам, искать, фильтровать
├── GRAPH_REPORT.md  бог-узлы, неожиданные связи, предлагаемые вопросы
├── graph.json       постоянный граф — запрашивать через недели без повторного чтения
└── cache/           SHA256-кэш — повторные запуски обрабатывают только изменённые файлы
```

Добавьте файл `.graphifyignore` для исключения папок:

```
# .graphifyignore
vendor/
node_modules/
dist/
*.generated.py
```

Синтаксис аналогичен `.gitignore`.

## Как это работает

graphify работает в три прохода. Сначала детерминированный AST-проход извлекает структуру из файлов кода (классы, функции, импорты, графы вызовов, docstrings, комментарии с обоснованием) — без LLM. Затем видео и аудиофайлы транскрибируются локально с faster-whisper. Наконец, Claude-субагенты запускаются параллельно над документами, статьями, изображениями и транскриптами для извлечения концепций, связей и обоснований дизайна. Результаты объединяются в граф NetworkX, кластеризуются с помощью Leiden-детекции сообществ и экспортируются как интерактивный HTML, запрашиваемый JSON и аудит-отчёт на естественном языке.

**Кластеризация основана на топологии графа — без эмбеддингов.** Leiden находит сообщества по плотности рёбер. Рёбра семантического сходства, извлечённые Claude (`semantically_similar_to`, помечены как INFERRED), уже в графе. Структура графа — это сигнал сходства. Отдельный шаг с эмбеддингами или векторная база данных не нужны.

Каждая связь помечена как `EXTRACTED` (найдена непосредственно в источнике), `INFERRED` (обоснованный вывод с оценкой уверенности) или `AMBIGUOUS` (помечена для проверки).

## Установка

**Требования:** Python 3.10+ и одно из: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli), [VS Code Copilot Chat](https://code.visualstudio.com/docs/copilot/overview), [Aider](https://aider.chat), [OpenClaw](https://openclaw.ai), [Factory Droid](https://factory.ai), [Trae](https://trae.ai), [Kiro](https://kiro.dev), Hermes или [Google Antigravity](https://antigravity.google)

```bash
# Рекомендуется — работает на Mac и Linux без настройки PATH
uv tool install graphifyy && graphify install
# или с pipx
pipx install graphifyy && graphify install
# или обычн


# FILE: docs/translations/README.uk-UA.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**Навичка для ШІ-асистентів кодування.** Введіть `/graphify` у Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro або Google Antigravity — він читає ваші файли, будує граф знань і повертає вам структуру, про яку ви не знали. Розумійте кодову базу швидше. Знайдіть «чому» за архітектурними рішеннями.

Повністю мультимодальний. Додавайте код, PDF, markdown, знімки екрана, діаграми, фотографії дошок, зображення іншими мовами або відео- та аудіофайли — graphify витягує концепції та зв'язки з усього і з'єднує їх в один граф. Відео транскрибуються локально за допомогою Whisper. Підтримує 25 мов програмування через tree-sitter AST.

> Андрій Карпатій веде папку `/raw`, куди кладе статті, твіти, знімки екрана та нотатки. graphify — відповідь на цю проблему — **71,5x** менше токенів на запит порівняно з читанням сирих файлів, зберігається між сесіями.

```
/graphify .
```

```
graphify-out/
├── graph.html       інтерактивний граф — відкрийте в будь-якому браузері
├── GRAPH_REPORT.md  вузли-боги, несподівані зв'язки, запропоновані питання
├── graph.json       постійний граф — можна запитувати через тижні
└── cache/           SHA256-кеш — повторні запуски обробляють лише змінені файли
```

## Як це працює

graphify працює в три проходи. Спочатку детерміністичний прохід AST витягує структуру з файлів коду без LLM. Потім відео та аудіофайли транскрибуються локально за допомогою faster-whisper. Нарешті субагенти Claude працюють паралельно над документами, статтями, зображеннями та транскрипціями. Результати об'єднуються в граф NetworkX, кластеризуються з Leiden і експортуються як інтерактивний HTML, JSON для запитів і звіт аудиту.

Кожен зв'язок позначений як `EXTRACTED`, `INFERRED` (з оцінкою впевненості) або `AMBIGUOUS`.

## Встановлення

**Вимоги:** Python 3.10+ та одне з: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) та інші.

```bash
uv tool install graphifyy && graphify install
# або з pipx
pipx install graphifyy && graphify install
# або pip
pip install graphifyy && graphify install
```

> **Офіційний пакет:** Пакет PyPI називається `graphifyy`. Єдиний офіційний репозиторій — [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Використання

```
/graphify .
/graphify ./raw --update
/graphify query "що пов'язує Attention з оптимізатором?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Що ви отримуєте

**Вузли-боги** — концепції з найвищим ступенем · **Несподівані зв'язки** — відсортовані за оцінкою · **Запропоновані питання** · **«Чому»** — рядки документації та обґрунтування дизайну витягнуті як вузли · **Бенчмарк токенів** — **71,5x** менше токенів на змішаному корпусі.

## Конфіденційність

Файли коду обробляються локально через tree-sitter AST. Відео транскрибуються локально за допомогою faster-whisper. Без телеметрії.

## Побудовано на graphify — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) — корпоративний рівень над graphify. **Безкоштовна пробна версія незабаром.** [Приєднайтесь до списку очікування →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)



# FILE: docs/translations/README.pl-PL.md

<p align="center">
  <img src="https://raw.githubusercontent.com/safishamsi/graphify/v4/docs/logo-text.svg" width="260" height="64" alt="Graphify"/>
</p>

<p align="center">
  🇺🇸 <a href="../../README.md">English</a> | 🇨🇳 <a href="README.zh-CN.md">简体中文</a> | 🇯🇵 <a href="README.ja-JP.md">日本語</a> | 🇰🇷 <a href="README.ko-KR.md">한국어</a> | 🇩🇪 <a href="README.de-DE.md">Deutsch</a> | 🇫🇷 <a href="README.fr-FR.md">Français</a> | 🇪🇸 <a href="README.es-ES.md">Español</a> | 🇮🇳 <a href="README.hi-IN.md">हिन्दी</a> | 🇧🇷 <a href="README.pt-BR.md">Português</a> | 🇷🇺 <a href="README.ru-RU.md">Русский</a> | 🇸🇦 <a href="README.ar-SA.md">العربية</a> | 🇮🇹 <a href="README.it-IT.md">Italiano</a> | 🇵🇱 <a href="README.pl-PL.md">Polski</a> | 🇳🇱 <a href="README.nl-NL.md">Nederlands</a> | 🇹🇷 <a href="README.tr-TR.md">Türkçe</a> | 🇺🇦 <a href="README.uk-UA.md">Українська</a> | 🇻🇳 <a href="README.vi-VN.md">Tiếng Việt</a> | 🇮🇩 <a href="README.id-ID.md">Bahasa Indonesia</a> | 🇸🇪 <a href="README.sv-SE.md">Svenska</a> | 🇬🇷 <a href="README.el-GR.md">Ελληνικά</a> | 🇷🇴 <a href="README.ro-RO.md">Română</a> | 🇨🇿 <a href="README.cs-CZ.md">Čeština</a> | 🇫🇮 <a href="README.fi-FI.md">Suomi</a> | 🇩🇰 <a href="README.da-DK.md">Dansk</a> | 🇳🇴 <a href="README.no-NO.md">Norsk</a> | 🇭🇺 <a href="README.hu-HU.md">Magyar</a> | 🇹🇭 <a href="README.th-TH.md">ภาษาไทย</a> | 🇹🇼 <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <a href="https://github.com/safishamsi/graphify/actions/workflows/ci.yml"><img src="https://github.com/safishamsi/graphify/actions/workflows/ci.yml/badge.svg?branch=v4" alt="CI"/></a>
  <a href="https://pypi.org/project/graphifyy/"><img src="https://img.shields.io/pypi/v/graphifyy" alt="PyPI"/></a>
  <a href="https://pepy.tech/project/graphifyy"><img src="https://static.pepy.tech/badge/graphifyy" alt="Downloads"/></a>
  <a href="https://github.com/sponsors/safishamsi"><img src="https://img.shields.io/badge/sponsor-safishamsi-ea4aaa?logo=github-sponsors" alt="Sponsor"/></a>
</p>

**Umiejętność dla asystenta kodowania AI.** Wpisz `/graphify` w Claude Code, Codex, OpenCode, Cursor, Gemini CLI, GitHub Copilot CLI, VS Code Copilot Chat, Aider, OpenClaw, Factory Droid, Trae, Hermes, Kiro lub Google Antigravity — czyta Twoje pliki, buduje graf wiedzy i zwraca Ci strukturę, o której nie wiedziałeś, że istnieje. Rozumiej bazę kodu szybciej. Znajdź „dlaczego" za decyzjami architektonicznymi.

W pełni multimodalny. Dodaj kod, PDF, markdown, zrzuty ekranu, diagramy, zdjęcia tablic, obrazy w innych językach lub pliki wideo i audio — graphify wyodrębnia koncepcje i relacje ze wszystkiego i łączy je w jeden graf. Wideo są transkrybowane lokalnie za pomocą Whisper. Obsługuje 25 języków programowania przez tree-sitter AST.

> Andrej Karpathy prowadzi folder `/raw`, gdzie wrzuca artykuły, tweety, zrzuty ekranu i notatki. graphify jest odpowiedzią na ten problem — **71,5x** mniej tokenów na zapytanie w porównaniu z czytaniem surowych plików, trwały między sesjami.

```
/graphify .                        # działa na dowolnym folderze
```

```
graphify-out/
├── graph.html       interaktywny graf — otwórz w dowolnej przeglądarce
├── GRAPH_REPORT.md  węzły boga, zaskakujące połączenia, sugerowane pytania
├── graph.json       trwały graf — zapytaj tygodnie później
└── cache/           cache SHA256 — ponowne uruchomienia przetwarzają tylko zmienione pliki
```

## Jak to działa

graphify działa w trzech przebiegach. Najpierw deterministyczny przebieg AST wyodrębnia strukturę z plików kodu bez LLM. Następnie pliki wideo i audio są transkrybowane lokalnie za pomocą faster-whisper. Na koniec subagenci Claude działają równolegle na dokumentach, artykułach, obrazach i transkrypcjach. Wyniki są łączone w graf NetworkX, grupowane za pomocą Leiden i eksportowane jako interaktywny HTML, JSON i raport audytu.

Każda relacja jest oznaczona `EXTRACTED`, `INFERRED` (z wynikiem pewności) lub `AMBIGUOUS`.

## Instalacja

**Wymagania:** Python 3.10+ i jedno z: [Claude Code](https://claude.ai/code), [Codex](https://openai.com/codex), [OpenCode](https://opencode.ai), [Cursor](https://cursor.com) i inne.

```bash
uv tool install graphifyy && graphify install
# lub z pipx
pipx install graphifyy && graphify install
# lub pip
pip install graphifyy && graphify install
```

> **Oficjalny pakiet:** Pakiet PyPI nazywa się `graphifyy`. Jedyne oficjalne repozytorium to [safishamsi/graphify](https://github.com/safishamsi/graphify).

## Użycie

```
/graphify .
/graphify ./raw --update           # tylko zmienione pliki
/graphify ./raw --mode deep
/graphify query "co łączy Attention z optymalizatorem?"
/graphify path "DigestAuth" "Response"
graphify hook install
graphify update ./src
```

## Co otrzymujesz

**Węzły boga** — koncepcje o najwyższym stopniu · **Zaskakujące połączenia** — posortowane według wyniku · **Sugerowane pytania** — 4-5 pytań, na które graf jest wyjątkowo zdolny odpowiedzieć · **„Dlaczego"** — docstringi i uzasadnienia projektowe wyodrębnione jako węzły · **Benchmark tokenów** — **71,5x** mniej tokenów na mieszanym korpusie.

## Prywatność

Pliki kodu są przetwarzane lokalnie przez tree-sitter AST. Wideo transkrybowane lokalnie z faster-whisper. Brak telemetrii.

## Zbudowane na graphify — Penpax

[**Penpax**](https://safishamsi.github.io/penpax.ai) to warstwa enterprise nad graphify. **Bezpłatna wersja próbna wkrótce.** [Dołącz do listy oczekujących →](https://safishamsi.github.io/penpax.ai)

[![Star History Chart](https://api.star-history.com/svg?repos=safishamsi/graphify&type=Date)](https://star-history.com/#safishamsi/graphify&Date)

