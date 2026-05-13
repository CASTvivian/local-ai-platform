# Repo Summary Source: sickn33/antigravity-awesome-skills
- URL: https://github.com/sickn33/antigravity-awesome-skills
- Local Path: core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills
- Buckets: agent, mcp
- Stars: 37331
- Language: Python
- Description: Installable GitHub library of 1,400+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows, and official/community skill collections.
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

<!-- registry-sync: version=11.1.0; skills=1453; stars=37158; updated_at=2026-05-11T15:17:43+00:00 -->
# 🌌 Antigravity Awesome Skills: 1,453+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **Installable GitHub library of 1,453+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.**

Antigravity Awesome Skills is an installable GitHub library and npm installer for reusable `SKILL.md` playbooks. It is designed for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, GitHub Copilot, and other AI coding assistants that benefit from structured operating instructions. Instead of collecting one-off prompt snippets, this repository gives you a searchable, installable catalog of skills, bundles, workflows, plugin-safe distributions, and practical docs that help agents perform recurring tasks with better context, stronger constraints, and clearer outputs.

You can use this repo to install a broad multi-tool skill library, start from role-based bundles, or jump into workflow-driven execution for planning, coding, debugging, testing, security review, infrastructure, product work, and growth tasks. The root README is intentionally a high-signal landing page: understand what the project is, install it quickly, choose the right tool path, and then follow deeper docs only when you need them.

**Start here:** [Star the repo](https://github.com/sickn33/antigravity-awesome-skills/stargazers) · [Install in 1 minute](#installation) · [Choose your tool](#choose-your-tool) · [Best skills by tool](#best-skills-by-tool) · [📚 Browse 1,453+ Skills](#browse-1453-skills) · [Bundles](docs/users/bundles.md) · [Workflows](docs/users/workflows.md) · [Plugins for Claude Code and Codex](docs/users/plugins.md)

[![GitHub stars](https://img.shields.io/badge/⭐%2037%2C000%2B%20Stars-gold?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Latest Release](https://img.shields.io/github/v/release/sickn33/antigravity-awesome-skills?display_name=tag&style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/releases/latest)
[![Install with NPX](https://img.shields.io/badge/Install-npx%20antigravity--awesome--skills-black?style=for-the-badge&logo=npm)](#installation)
[![Kiro](https://img.shields.io/badge/Kiro-AWS-orange?style=for-the-badge)](https://kiro.dev)
[![Copilot](https://img.shields.io/badge/Copilot-GitHub-lightblue?style=for-the-badge)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray?style=for-the-badge)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-AI%20IDE-red?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills)

**Current release: V11.1.0.** Trusted by 37k+ GitHub stargazers, this repository combines official and community skill collections with bundles, workflows, installation paths, and docs that help you go from first install to daily use quickly.

## Why This Repo

- **Installable, not just inspirational**: use `npx antigravity-awesome-skills` to put skills where your tool expects them.
- **Built for major agent workflows**: Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, Copilot, and more.
- **Broad coverage with real utility**: 1,453+ skills across development, testing, security, infrastructure, product, and marketing.
- **Faster onboarding**: bundles and workflows reduce the time from "I found this repo" to "I used my first skill".
- **Useful whether you want breadth or curation**: browse the full catalog, start with top bundles, or compare alternatives before installing.

## Table of Contents

- [Why This Repo](#why-this-repo)
- [Installation](#installation)
- [Choose Your Tool](#choose-your-tool)
- [Quick FAQ](#quick-faq)
- [Best Skills By Tool](#best-skills-by-tool)
- [Bundles & Workflows](#bundles--workflows)
- [Browse 1,453+ Skills](#browse-1453-skills)
- [Troubleshooting](#troubleshooting)
- [Support the Project](#support-the-project)
- [Contributing](#contributing)
- [Community](#community)
- [Credits & Sources](#credits--sources)
- [Repo Contributors](#repo-contributors)
- [Star History](#star-history)
- [License](#license)

## Installation

Most users should start with the full library install and use bundles or workflows to narrow down what to try first.

### Full library install

```bash
# Default: ~/.gemini/antigravity/skills (Antigravity global). Use --path for other locations.
npx antigravity-awesome-skills
```

The npm installer uses a shallow clone by default so first-run installs stay lighter than a full repository history checkout.

### Verify the install

```bash
test -d ~/.gemini/antigravity/skills && echo "Skills installed in ~/.gemini/antigravity/skills"
```

### Run your first skill

```text
Use @brainstorming to plan a SaaS MVP.
```

### Prefer plugins for Claude Code or Codex?

- Use the full library install when you want the broadest catalog and direct control over your installed skills directory.
- Use the plugin route when you want a marketplace-style, plugin-safe distribution for Claude Code or Codex.
- Read [Plugins for Claude Code and Codex](docs/users/plugins.md) for the full breakdown of full-library install vs plugin install vs bundle plugins.

## Choose Your Tool

Use the same repository, but install or invoke it in the way your host expects.

| Tool           | Install                                        


# FILE: docs/SKILLS_DATE_TRACKING.md

# Skills Date Tracking

This document moved to [`maintainers/skills-date-tracking.md`](maintainers/skills-date-tracking.md).



# FILE: docs/EXAMPLES.md

# Examples

This document moved to [`contributors/examples.md`](contributors/examples.md).



# FILE: docs/SMART_AUTO_CATEGORIZATION.md

# Smart Auto Categorization

This document moved to [`maintainers/smart-auto-categorization.md`](maintainers/smart-auto-categorization.md).



# FILE: docs/WORKFLOWS.md

# Workflows

This document moved to [`users/workflows.md`](users/workflows.md).



# FILE: docs/DATE_TRACKING_IMPLEMENTATION.md

# Date Tracking Implementation

This document moved to [`maintainers/date-tracking-implementation.md`](maintainers/date-tracking-implementation.md).



# FILE: docs/KIRO_INTEGRATION.md

# Kiro Integration

This document moved to [`users/kiro-integration.md`](users/kiro-integration.md).



# FILE: docs/SEC_SKILLS.md

# Security Skills

This document moved to [`users/security-skills.md`](users/security-skills.md).



# FILE: docs/SOURCES.md

# Sources

This document moved to [`sources/sources.md`](sources/sources.md).



# FILE: docs/USAGE.md

# Usage Guide

This document moved to [`users/usage.md`](users/usage.md).



# FILE: docs/SECURITY_GUARDRAILS.md

# Security Guardrails

This document moved to [`contributors/security-guardrails.md`](contributors/security-guardrails.md).

