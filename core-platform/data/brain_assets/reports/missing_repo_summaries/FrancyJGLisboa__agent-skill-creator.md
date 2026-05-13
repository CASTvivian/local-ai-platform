# Missing Repo Summary Source: FrancyJGLisboa/agent-skill-creator

- URL: https://github.com/FrancyJGLisboa/agent-skill-creator
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/FrancyJGLisboa__agent-skill-creator
- Clone Status: cloned
- Language: Python
- Stars: 905
- Topics: 
- Description: Turn any workflow into reusable AI agent skills that install on 14+ tools — Claude Code, Copilot, Cursor, Windsurf, Codex, Gemini, Kiro, and more. One SKILL.md, every platform.

## Extracted README / Docs / Examples



# FILE: README.md

# Agent Skill Creator

**Turn any workflow into reusable AI agent software that installs on 14+ tools — no spec writing, no prompt engineering, no coding required.**

[![Agent Skills Open Standard](https://img.shields.io/badge/Agent%20Skills-Open%20Standard-blue)](https://github.com/anthropics/agent-skills-spec)
[![Version](https://img.shields.io/badge/version-5.0.0-brightgreen)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

![Agent Skill Creator Overview](Dynamous/agentskillimage.png)

---

## The Problem

Every AI coding tool — Claude Code, GitHub Copilot, Cursor, Windsurf, Codex, Gemini, Kiro, and more — starts from zero. It doesn't know your company's processes, data sources, or compliance requirements. So every person re-explains the same workflows in every conversation. Knowledge stays in individual chat histories. New hires start from scratch.

**Agent skills fix this.** A skill is structured knowledge your agent loads automatically — like installing an app. Once installed, anyone on your team can invoke it and get consistent results, every time, on any platform.

**The catch:** building a proper skill requires understanding the spec format, writing clear prompt instructions, designing how information loads progressively, writing functional code, and getting activation keywords right. Even simple skills take [multiple rounds of iteration](https://www.youtube.com/watch?v=izJkgLqlbN8) to get right.

**Agent Skill Creator removes that barrier entirely.** You pass in whatever you have — messy docs, links, code, PDFs, transcripts, vague descriptions — and it produces a validated, security-scanned skill ready to install on 14+ tools and share with your team. You describe what you do; it builds the software.

---

## Quick Start

### 1. Install

**Option A — One-liner (installs to all detected tools):**

```bash
curl -fsSL https://raw.githubusercontent.com/FrancyJGLisboa/agent-skill-creator/main/scripts/bootstrap.sh | sh
```

This clones to `~/.agents/skills/agent-skill-creator` and symlinks to every detected global platform (Claude Code, Gemini CLI, Goose, OpenCode, Copilot). Run `git pull` once to update everywhere.

**Option B — Git clone (pick your tool):**

```bash
# Claude Code / VS Code Copilot (global — works in all projects)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git ~/.claude/skills/agent-skill-creator

# Cursor (per-project)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git .cursor/rules/agent-skill-creator

# Codex CLI / Gemini CLI / Kiro / Antigravity (universal path)
git clone https://github.com/FrancyJGLisboa/agent-skill-creator.git ~/.agents/skills/agent-skill-creator
```

**Option C — Already cloned? Symlink to all tools:**

```bash
cd agent-skill-creator
./install.sh              # Symlink to all detected platforms
./install.sh --dry-run    # Preview without changes
./install.sh --uninstall  # Remove all symlinks
```

One install at `~/.claude/skills/` works for both Claude Code and VS Code Copilot. One install at `~/.agents/skills/` works for Codex CLI, Gemini CLI, Kiro, Antigravity, and other tools that read the universal path.

All 14 platforms: [see full list below](#all-platforms).

### 2. Use it

Open your agent and type `/agent-skill-creator` followed by whatever you have:

```
/agent-skill-creator Every week I pull sales data from our CRM, clean
duplicate entries, calculate regional totals, and generate a PDF report.
```

You can pass anything — plain English, documentation links, existing code, API docs, PDFs, database schemas, transcripts. Combine multiple sources in one message. The more context, the better the result.

```
/agent-skill-creator Based on our deployment runbook: https://wiki.internal/deploy-process
```

```
/agent-skill-creator See scripts/invoice_processor.py — turn it into a reusable skill
```

### 3. What comes out

A complete skill, automatically installed on your platform:

```
Skill installed successfully.

To use it, open a new session and type:

  /sales-report-skill Generate the weekly report for the West region

Installed at: ~/.claude/skills/sales-report-skill
```

The agent detects your platform, installs the skill to the right location, and tells you exactly how to invoke it. No manual steps.

The generated skill includes a cross-platform installer (`install.sh`) that auto-detects all 14 supported tools, generates format adapters for Cursor (.mdc) and Windsurf (.md rules) automatically, and creates a universal `~/.agents/skills/` symlink so the skill is discoverable by multiple tools at once.

```
sales-report-skill/
├── SKILL.md          # Skill definition (activates with /sales-report-skill)
├── scripts/          # Functional Python code
├── references/       # Detailed documentation
├── assets/           # Templates, configs
├── install.sh        # Cross-platform installer (14 tools, format adapters, --all flag)
└── README.md         # Installation instructions
```

Your team installs it the same way — one `git clone` to their tool's path — and invokes it with `/sales-report-skill`.

---

## How It Works

You don't need to understand any of this to use it. But if you're curious:

The agent doesn't just follow your description literally. Humans describe what they *do*, not what they *need*. "I pull sales data and make a report" hides a dozen implicit requirements — who reads the report, what format, what happens when data is missing. The agent reads all your material, uncovers these implicit requirements, and generates its own internal specification before writing any code. It builds from that deeper understanding, not from your surface description.

```
UNDERSTAND    Read all material → uncover real intent → generate internal spec
BUILD         Structure directory → write code and docs → craft activation keywords
VERIFY        Spec validation → security scan → block delivery if either fails
```

Every skill is automatically validated (correct structure, naming, metadata) and security-scanned (no hardcoded keys, no credential exposure, no injection risks) before delivery. Skills that fail these checks are blocked.

---

## Share Skills Across Your Team

After the agent builds and installs your skill, it asks:

```
Want to share this skill with your team so they can install it too?
```

Say yes. The agent detects whether your team uses GitHub or GitLab, creates a repo, pushes the skill, and gives you a one-liner to share:

```
Shared! Your colleagues can install it by pasting this in their terminal:

  git clone https://github.com/your-org/sales-report-skill.git ~/.agents/skills/sales-report-skill
```

One `git clone` to `~/.agents/skills/` makes it available on Codex CLI, Gemini CLI, Kiro, and Antigravity simultaneously. For Claude Code users: `~/.claude/skills/sales-report-skill`. For Cursor: `.cursor/rules/sales-report-skill`.

Send that line to your colleague on Slack or Teams. They paste it. Done. They can now type `/sales-report-skill` in their agent.

No registry commands, no publishing steps, no terminal knowledge beyond paste. The agent handles the repo creation, the push, and generates install commands for every platform.

### The result over time

Each team member creates skills from their own domain and shares them. Over months the organization accumulates a library of reusable skills:

- Sales team shares `/sales-report-skill`
- Engineering shares `/deploy-checklist-skill`
- Legal shares `/quarterly-compliance-skill`
- Data science shares `/customer-churn-skill`
- SRE shares `/incident-runbook-skill`

Any colleague installs any skill with one `git clone`. Any agent on any platform can invoke it. Knowledge compounds instead of evaporating.

### For teams and consultants: the skill registry

When an organization has more than a few skills, the agent offers to set up a **team skill registry** — a shared git repo where all team members publish their skills and anyone can browse and install them.

The consultant (or team lead) sets it up once:

```bash
python3 scripts/skill_registry.py init --name "Acme Corp Skills"
```

Then every team member can:

```bash
# Publish a skill they created
python3 scripts/skill_registry.py publish ./sales-report-skill/ --tags sales,reports

# Browse what's available
python3 scripts/skill_registry.py list

# Search for a specific skill
python3 scripts/skill_registry.py search "sales"

# Install a colleague's skill (auto-detects platform)
python3 scripts/skill_registry.py install sales-report-skill
```

The registry is a git repo on GitHub or GitLab. Clone it once, and every team member can publish and install. No servers, no databases — just git.

**For AI consultants:** The engagement model is teach, not build. Install agent-skill-creator on each team member's machine, create the shared `{team}-skills-registry` repo, teach the team the 5-step workflow (install, clone registry, create skill, publish, install from registry), and hand over a self-sustaining system. After you leave, the team keeps creating and sharing skills on their own. They know their workflows better than you do — your job is to remove the friction.

---

## All Platforms

14 tools supported. Same skill, same invocation, same results everywhere.

### How it works

Skills are authored as **SKILL.md** (the open standard). Tools in **Tier 1** read SKILL.md natively. Tools in **Tier 2** need a different format — the installer auto-generates it (`.mdc` for Cursor, `.md` rules for Windsurf, plain markdown for Cline/Roo/Trae). You never deal with format conversion.

| Tier | Platforms | What happens |
|------|-----------|-------------|
| **Tier 1 — Native** | Claude Code, Copilot, Codex CLI, Gemini CLI, Kiro, Antigravity, Goose, OpenCode | Reads SKILL.md directly |
| **Tier 2 — Auto-adapted** | Cursor, Windsurf, Cline, Roo Code, Trae | Installer converts SKILL.md to native format |
| **Tier 3 — Manual** | Zed, Junie, Aider | Copy skill body into tool's config file |

### Universal p
