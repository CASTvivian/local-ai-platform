# Missing Repo Summary Source: luongnv89/claude-howto

- URL: https://github.com/luongnv89/claude-howto
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/luongnv89__claude-howto
- Clone Status: cloned
- Language: Python
- Stars: 32542
- Topics: claude-code, guide, tutorial
- Description: A visual, example-driven guide to Claude Code — from basic concepts to advanced agents, with copy-paste templates that bring immediate value.

## Extracted README / Docs / Examples



# FILE: README.md

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.138-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова:** [English](README.md) | [Tiếng Việt](vi/README.md) | [中文](zh/README.md) | [Українська](uk/README.md) | [日本語](ja/README.md)

# Master Claude Code in a Weekend

Go from typing `claude` to orchestrating agents, hooks, skills, and MCP servers — with visual tutorials, copy-paste templates, and a guided learning path.

**[Get Started in 15 Minutes](#get-started-in-15-minutes)** | **[Find Your Level](#not-sure-where-to-start)** | **[Browse the Feature Catalog](CATALOG.md)**

---

## Table of Contents

- [The Problem](#the-problem)
- [How Claude How To Fixes This](#how-claude-how-to-fixes-this)
- [How It Works](#how-it-works)
- [Not Sure Where to Start?](#not-sure-where-to-start)
- [Get Started in 15 Minutes](#get-started-in-15-minutes)
- [What Can You Build With This?](#what-can-you-build-with-this)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## The Problem

You installed Claude Code. You ran a few prompts. Now what?

- **The official docs describe features — but don't show you how to combine them.** You know slash commands exist, but not how to chain them with hooks, memory, and subagents into a workflow that actually saves hours.
- **There's no clear learning path.** Should you learn MCP before hooks? Skills before subagents? You end up skimming everything and mastering nothing.
- **Examples are too basic.** A "hello world" slash command doesn't help you build a production code review pipeline that uses memory, delegates to specialized agents, and runs security scans automatically.

You're leaving 90% of Claude Code's power on the table — and you don't know what you don't know.

---

## How Claude How To Fixes This

This isn't another feature reference. It's a **structured, visual, example-driven guide** that teaches you to use every Claude Code feature with real-world templates you can copy into your project today.

| | Official Docs | This Guide |
|--|---------------|------------|
| **Format** | Reference documentation | Visual tutorials with Mermaid diagrams |
| **Depth** | Feature descriptions | How it works under the hood |
| **Examples** | Basic snippets | Production-ready templates you use immediately |
| **Structure** | Feature-organized | Progressive learning path (beginner to advanced) |
| **Onboarding** | Self-directed | Guided roadmap with time estimates |
| **Self-Assessment** | None | Interactive quizzes to find your gaps and build a personalized path |

### What you get:

- **10 tutorial modules** covering every Claude Code feature — from slash commands to custom agent teams
- **Copy-paste configs** — slash commands, CLAUDE.md templates, hook scripts, MCP configs, subagent definitions, and full plugin bundles
- **Mermaid diagrams** showing how each feature works internally, so you understand *why*, not just *how*
- **A guided learning path** that takes you from beginner to power user in 11-13 hours
- **Built-in self-assessment** — run `/self-assessment` or `/lesson-quiz hooks` directly in Claude Code to identify gaps

**[Start the Learning Path  ->](LEARNING-ROADMAP.md)**

---

## How It Works

### 1. Find your level

Take the [self-assessment quiz](LEARNING-ROADMAP.md#-find-your-level) or run `/self-assessment` in Claude Code. Get a personalized roadmap based on what you already know.

### 2. Follow the guided path

Work through 10 modules in order — each builds on the last. Copy templates directly into your project as you learn.

### 3. Combine features into workflows

The real power is in combining features. Learn to wire slash commands + memory + subagents + hooks into automated pipelines that handle code reviews, deployments, and documentation generation.

### 4. Test your understanding

Run `/lesson-quiz [topic]` after each module. The quiz pinpoints what you missed so you can fill gaps fast.

**[Get Started in 15 Minutes](#get-started-in-15-minutes)**

---

## Trusted by Developers

- **GitHub stars** from developers who use Claude Code daily
- **Forks** from teams adapting this guide for their own workflows
- **Actively maintained** — synced with every Claude Code release (latest: v2.1.138, May 2026)
- **Community-driven** — contributions from developers who share their real-world configurations

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## Not Sure Where to Start?

Take the self-assessment or pick your level:

| Level | You can... | Start here | Time |
|-------|-----------|------------|------|
| **Beginner** | Start Claude Code and chat | [Slash Commands](01-slash-commands/) | ~2.5 hours |
| **Intermediate** | Use CLAUDE.md and custom commands | [Skills](03-skills/) | ~3.5 hours |
| **Advanced** | Configure MCP servers and hooks | [Advanced Features](09-advanced-features/) | ~5 hours |

**Full learning path with all 10 modules:**

| Order | Module | Level | Time |
|-------|--------|-------|------|
| 1 | [Slash Commands](01-slash-commands/) | Beginner | 30 min |
| 2 | [Memory](02-memory/) | Beginner+ | 45 min |
| 3 | [Checkpoints](08-checkpoints/) | Intermediate | 45 min |
| 4 | [CLI Basics](10-cli/) | Beginner+ | 30 min |
| 5 | [Skills](03-skills/) | Intermediate | 1 hour |
| 6 | [Hooks](06-hooks/) | Intermediate | 1 hour |
| 7 | [MCP](05-mcp/) | Intermediate+ | 1 hour |
| 8 | [Subagents](04-subagents/) | Intermediate+ | 1.5 hours |
| 9 | [Advanced Features](09-advanced-features/) | Advanced | 2-3 hours |
| 10 | [Plugins](07-plugins/) | Advanced | 2 hours |

**[Complete Learning Roadmap ->](LEARNING-ROADMAP.md)**

---

## Get Started in 15 Minutes

> **Installation note**: Starting in v2.1.113, Claude Code ships as a native per-platform binary (macOS/Linux/Windows). `npm install -g @anthropic-ai/claude-code` still works — the native binary is downloaded as an optional dep on first use. As of v2.1.116, downloads come from `https://downloads.claude.ai/claude-code-releases` — corporate proxies must allowlist this host.

```bash
# 1. Clone the guide
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. Copy your first slash command
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. Try it — in Claude Code, type:
# /optimize

# 4. Ready for more? Set up project memory:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. Install a skill:
cp -r 03-skills/code-review ~/.claude/skills/
```

Want the full setup? Here's the **1-hour essential setup**:

```bash
# Slash commands (15 min)
cp 01-slash-commands/*.md .claude/commands/

# Project memory (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Install a skill (15 min)
cp -r 03-skills/code-review ~/.claude/skills/

# Weekend goal: add hooks, subagents, MCP, and plugins
# Follow the learning path for guided setup
```

**[View the Full Installation Reference](#get-started-in-15-minutes)**

---

## What Can You Build With This?

| Use Case | Features You'll Combine |
|----------|------------------------|
| **Automated Code Review** | Slash Commands + Subagents + Memory + MCP |
| **Team Onboarding** | Memory + Slash Commands + Plugins |
| **CI/CD Automation** | CLI Reference + Hooks + Background Tasks |
| **Documentation Generation** | Skills + Subagents + Plugins |
| **Security Audits** | Subagents + Skills + Hooks (read-only mode) |
| **DevOps Pipelines** | Plugins + MCP + Hooks + Background Tasks |
| **Complex Refactoring** | Checkpoints + Planning Mode + Hooks |

---

## FAQ

**Is this free?**
Yes. MIT licensed, free forever. Use it in personal projects, at work, in your team — no restrictions beyond including the license notice.

**Is this maintained?**
Actively. The guide is synced with every Claude Code release. Current version: v2.1.138 (May 2026), compatible with Claude Code 2.1+.

**How is this different from the official docs?**
The official docs are a feature reference. This guide is a tutorial with diagrams, production-ready templates, and a progressive learning path. They complement each other — start here to learn, reference the docs when you need specifics.

**How long does it take to go through everything?**
11-13 hours for the full path. But you'll get immediate value in 15 minutes — just copy a slash command template and try it.

**Can I use this with Claude Sonnet / Haiku / Opus?**
Yes. All templates work with Claude Sonnet 4.6, Claude Opus 4.7, and Claude Haiku 4.5.

**Can I contribute?**
Absolutely. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome new examples, bug fixes, documentation improvements, and community templates.

**Can I read this offline?**
Yes. Run `uv run scripts/build_epub.py` to generate an EPUB ebook with all content and rendered diagrams.

---

## Start Mastering Claude Code Today

You already have Claude Code installed. The only thing between you and 10x productivity is knowing how to use it. This guide gives you the structured path, the visual explanations, and the copy-pa

# FILE: docs/ROADMAP-20260401.md

# Roadmap: claude-howto 2026–2027

> April 2026 – March 2027 · Dual-Layer Knowledge Base | Full plan: `TASKS-20260401.md`

---

## Vision

Transform claude-howto from a static tutorial repo into a **living, dual-audience knowledge system**:

- **For humans** — interactive, scenario-based learning with progressive difficulty, decision trees, and named patterns that experts bookmark
- **For AI agents** — structured metadata index that agents query before performing Claude Code tasks, making this repo infrastructure, not just content

No competitor targets AI agents as a primary audience. This is the moat.

---

## The 7 Pillars

| # | Pillar | What it delivers |
|---|--------|-----------------|
| P1 | Fun Layer | Scenario intros + "Try It Now" blocks in every module |
| P2 | AI Agent Index | Generated `agent-manifest.json` + `AGENT-INDEX.md` + lookup skill |
| P3a | Expert Reference (in-module) | Decision trees + named patterns per module |
| P3b | Expert Reference (cross-module) | `RECIPES.md` — compound multi-feature workflows |
| P4 | Newcomer Onboarding | `quickstart.sh` + `QUICKSTART.md` + difficulty badges |
| P5 | Community Showcase | `COMMUNITY-PROJECTS.md` — curated user projects |
| P6 | Content Quality | Expand weakest modules; project `CLAUDE.md` |
| P7 | Living Curriculum | `WHATS-NEW.md` + version badges + weekly staleness CI action |

---

## Timeline at a Glance

```
Apr 2026   May–Jun 2026   Jul–Aug 2026   Sep 2026   Oct–Nov 2026   Dec 2026–Mar 2027
   |             |              |             |             |               |
  [M1]          [M2]           [M3]          [M4]          [M5]            [M6]
Infrastructure  6/10 modules   10/10         Agent layer   Version audit   Self-sustaining
+ hooks/checks  complete       complete      + recipes     complete        system
```

---

## Milestones

### M1 — Infrastructure Live · End of April 2026

**What ships:**
- `scripts/quickstart.sh` — one-command setup for new users (idempotent)
- `QUICKSTART.md` — First 15 Minutes visual guide
- Difficulty badges + "What you'll build" previews on all 10 modules
- `WHATS-NEW.md` + version badges on all modules
- `.github/workflows/staleness-check.yml` — weekly Monday issue if module unverified 30+ days
- Root `CLAUDE.md` — project's own configuration as a best-practice example
- `scripts/build-agent-index.py` — generator that reads all 10 modules → outputs `agent-manifest.json` + `AGENT-INDEX.md`
- **06-hooks** — full deep pass: 5 complete hook scripts, decision tree, Try It Now, patterns
- **08-checkpoints** — full deep pass: 311 → 800+ lines, 3 workflow templates, decision tree, patterns

**Why start here:** Infrastructure benefits every future phase. Hooks and checkpoints are the weakest modules and most likely to lose new visitors.

---

### M2 — 6/10 Modules Complete · End of June 2026

**What ships (one deep pass per module):**
- **01-slash-commands** — scenario intro, decision tree, Try It Now, named patterns
- **02-memory** — scenario intro, decision tree, Try It Now, named patterns
- **03-skills** — scenario intro, decision tree, Try It Now, named patterns
- **10-cli** — scenario intro, decision tree, Try It Now, named patterns
- CI step: validate `agent-manifest.json` schema on every push

Each module pass = run the generator to confirm valid manifest output.

---

### M3 — All 10 Modules Complete · End of August 2026

**What ships:**
- **04-subagents** — full deep pass (incl. "The Multi-Agent Review Pattern")
- **05-mcp** — full deep pass
- **07-plugins** — full deep pass
- **09-advanced-features** — full deep pass

Every module now has: scenario intro, 2+ Try It Now blocks, Mermaid decision tree, 2+ named patterns.

---

### M4 — Agent Layer Live · End of September 2026

**What ships:**
- Final `agent-manifest.json` covering 100% of modules (generated from completed content)
- `AGENT-INDEX.md` linked from `README.md`
- `skills/claude-howto-lookup/SKILL.md` — lightweight agent skill that queries the manifest
- `RECIPES.md` — 5+ compound workflows (schema: name, modules-used, problem, solution, expected outcome)
- `COMMUNITY-PROJECTS.md` — static curated list with PR-based submission format

**Why September:** The agent index is only meaningful once all 10 modules are content-complete.

---

### M5 — Version Audit Complete · End of November 2026

**What ships:**
- Full version audit: all 10 modules verified against current CC version
- Updated `cc_version_verified` frontmatter + version badges everywhere
- `RECIPES.md` expanded to 8+ recipes based on observed community patterns
- Pinned GitHub Discussion: "Share your Claude Code workflows" — signal collection for agent usage

---

### M6 — Self-Sustaining System · End of March 2027

**What ships / runs continuously:**
- `/docs-sync-claude-code` skill runs after every CC release → `WHATS-NEW.md` updated
- Agent manifest CI regression: 100% module coverage enforced
- `RECIPES.md` at 10+ recipes
- `COMMUNITY-PROJECTS.md` growing organically
- Agent usage signal evaluated → if validated, promote the lookup skill (marketing, asm registry)

---

## Deliverables Summary

| Deliverable | Type | Phase |
|-------------|------|-------|
| `scripts/quickstart.sh` | Script | P1 |
| `QUICKSTART.md` | Doc | P1 |
| Root `CLAUDE.md` | Config | P1 |
| `WHATS-NEW.md` | Doc | P1 |
| `.github/workflows/staleness-check.yml` | CI | P1 |
| `scripts/build-agent-index.py` | Script | P1 |
| 10 module deep passes (scenario + Try It Now + decision tree + patterns) | Content | P1–P3 |
| `agent-manifest.json` (generated) | Data | P4 |
| `AGENT-INDEX.md` (generated) | Doc | P4 |
| `skills/claude-howto-lookup/SKILL.md` | Skill | P4 |
| `RECIPES.md` (5 → 8 → 10+ recipes) | Doc | P4–P6 |
| `COMMUNITY-PROJECTS.md` | Doc | P4 |

---

## What Is NOT in Scope

Deferred to `TODOS.md` — do not let these creep in:

- Skill marketplace or installable registry
- Custom website or dashboard
- Completion tracking (cc-progress)
- Community tutorial CI validation
- Auto-g

# FILE: docs/TASKS-20260401.md

# Tasks: Dual-Layer Knowledge Base — claude-howto

> Created: 2026-04-01

---

## Milestones

| # | Milestone | Target | Description |
|---|-----------|--------|-------------|
| M1 | Infrastructure Live | End of April 2026 | quickstart.sh, CLAUDE.md, staleness action, agent index generator live; 2 weakest modules upgraded |
| M2 | 6/10 Modules Complete | End of June 2026 | Slash commands, memory, skills, CLI modules fully upgraded; generator producing valid manifest |
| M3 | All 10 Modules Complete | End of August 2026 | Every module has scenario intro, Try It Now blocks, decision tree, named patterns |
| M4 | Agent Layer Live | End of September 2026 | agent-manifest.json + AGENT-INDEX.md generated; lookup skill in repo; RECIPES.md + COMMUNITY-PROJECTS.md live |
| M5 | Version Audit Complete | End of November 2026 | All 10 modules verified against current CC version; RECIPES.md at 8+ recipes |
| M6 | Self-Sustaining System | End of March 2027 | Agent manifest covers 100% modules (CI-validated); RECIPES.md at 10+; community page growing organically |

---

## Phase 1 — Infrastructure & Weak Modules (April 2026)

**Target milestone: M1**

### Pillar 4: Newcomer Onboarding

- [ ] **T-001** — Write `scripts/quickstart.sh`
  - Detects `~/.claude/` directory (creates with user confirmation if missing)
  - Copies first slash command + CLAUDE.md + skill to user's setup
  - Appends agent-discovery line to CLAUDE.md linking to AGENT-INDEX.md
  - Idempotent: skips existing files with a warning, never overwrites
  - Prints next steps on completion

- [ ] **T-002** — Create `QUICKSTART.md` (First 15 Minutes visual guide)
  - Annotated terminal steps as code blocks (avoid PNG screenshots where possible; prefer ASCII or Mermaid)
  - Document which commands produce each visual so they can be re-captured

- [ ] **T-003** — Add difficulty badges to all 10 module READMEs
  - Format: `> 🟢 **Beginner** | ⏱ 30 minutes` at top of each module README
  - Add "What you'll build" bullet preview below the badge

### Pillar 7: Living Curriculum

- [ ] **T-004** — Create `WHATS-NEW.md`
  - Format: `## CC vX.X — DATE` with bullet items per feature change
  - Add at least one entry for current CC version

- [ ] **T-005** — Add version badges to all 10 module READMEs
  - Format: `> ✅ Verified against Claude Code **vX.X.X** · Last verified: YYYY-MM-DD`
  - Add `cc_version_verified` to each module's frontmatter

- [ ] **T-006** — Create `.github/workflows/staleness-check.yml`
  - Schedule: weekly Monday 09:00 UTC
  - Reads each module's `last_verified` date from frontmatter (use `yq` or 10-line Python script)
  - Creates a GitHub Issue for any module not verified in 30+ days
  - Skips if open issue with same title already exists

### Pillar 6: Content Quality (CLAUDE.md)

- [ ] **T-007** — Create root `CLAUDE.md` for the project
  - Demonstrates best practices as the project's own configuration
  - Documents contributing conventions, module structure, and maintenance workflow

### Pillar 2: AI Agent Index (Generator)

- [ ] **T-008** — Write `scripts/build-agent-index.py`
  - Reads all 10 module README files
  - Extracts: headings (→ topics), code blocks (→ examples with language tags), tables (→ reference data)
  - Outputs `agent-manifest.json` with schema defined in CEO plan
  - Outputs `AGENT-INDEX.md` (human-readable summary)
  - Validates references point to actual files

### Module 08-checkpoints: Full Deep Pass (311 → 800+ lines)

- [ ] **T-009** — Rewrite module intro with real-world scenario
  - Example: "Your refactor just broke 3 things. Here's how checkpoints save you..."

- [ ] **T-010** — Add checkpoint strategy decision tree (Mermaid flowchart)
  - "I want to do X" → follow arrows → land on checkpoint pattern

- [ ] **T-011** — Add 3 workflow templates
  - Safe refactoring workflow
  - A/B testing with checkpoints
  - Disaster recovery workflow

- [ ] **T-012** — Add integration with planning mode section

- [ ] **T-013** — Add Mermaid diagram for checkpoint lifecycle

- [ ] **T-014** — Add 2+ "Try It Now" blocks with verifiable commands
  - Each: context sentence, command to run, expected output description

- [ ] **T-015** — Add "Patterns & Recipes" section with 2+ named patterns
  - Each pattern: problem, solution code, when to use, when NOT to use

### Module 06-hooks: Full Deep Pass

- [ ] **T-016** — Rewrite module intro with real-world scenario
  - Example: "Your CI caught a lint error after 20 minutes. Hooks catch it in 2 seconds..."

- [ ] **T-017** — Add hooks decision tree (Mermaid flowchart)
  - "I want to trigger X when Y happens" → follow arrows → land on hook type

- [ ] **T-018** — Add 5 complete hook examples with full scripts (~80 lines each)
  1. Auto-format on write (prettier/black)
  2. Security scan on commit (trufflehog/bandit)
  3. Test runner on file change
  4. Notification on session end
  5. Prompt validation (block dangerous patterns)

- [ ] **T-019** — Add 2+ "Try It Now" blocks with verifiable commands

- [ ] **T-020** — Add "Patterns & Recipes" section with 2+ named patterns

**M1 Checkpoint: infrastructure live, 2 weakest modules fully upgraded**

---

## Phase 2 — Deep Pass: Strong Modules Batch 1 (May–June 2026)

**Target milestone: M2**

### Module 01-slash-commands: Full Deep Pass

- [ ] **T-021** — Rewrite intro with scenario ("Your teammate just pushed 47 files...")
- [ ] **T-022** — Add decision tree (Mermaid)
- [ ] **T-023** — Add 2+ "Try It Now" blocks
- [ ] **T-024** — Add "Patterns & Recipes" section with 2+ named patterns

### Module 02-memory: Full Deep Pass

- [ ] **T-025** — Rewrite intro with real-world scenario
- [ ] **T-026** — Add decision tree (Mermaid)
- [ ] **T-027** — Add 2+ "Try It Now" blocks
- [ ] **T-028** — Add "Patterns & Recipes" section with 2+ named patterns

### Module 03-skills: Full Deep Pass

- [ ] **T-029** — Rewrite intro with real-world scenario
- [ ] **T-030** — Add decision tree (Mermaid)
- [ ] **T-031** — Add 2+ "Try It Now" blocks
-
