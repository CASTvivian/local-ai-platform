# Missing Repo Summary Source: bergside/awesome-design-skills

- URL: https://github.com/bergside/awesome-design-skills
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/bergside__awesome-design-skills
- Clone Status: cloned
- Language: None
- Stars: 479
- Topics: agent-skills, agentic-ai, agentic-workflow, agents, ai, ai-agents, ai-tools, awesome, awesome-list, awesome-readme, claude-design, codex, cursor, design, design-md, design-system, google-stitch, skills
- Description: List of 67 awesome DESIGN.md and SKILL.md design skill files for agentic tools like Claude Design, Google Stitch, Codex, Cursor, and other AI tools

## Extracted README / Docs / Examples



# FILE: README.md

# Awesome Design Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<img width="1200" height="630" alt="og-awesome-design-skills" src="https://github.com/user-attachments/assets/d392937a-a0a3-408d-b3f8-4d8920f836f9" />

<br>

> A curated registry of 67 design system skill files for AI-powered agentic tools like [Claude Code](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview), [Cursor](https://www.cursor.com/), [Codex](https://openai.com/index/codex/), and others. Pull any skill into your project with a single command.

Each skill now ships as a folder with:
- `SKILL.md` for AI-agent instructions (tokens, component rules, accessibility constraints, quality gates)
- `DESIGN.md` for human-readable design intent, rationale, and implementation notes

**[Preview all design skills on Type UI](https://typeui.sh/design-skills)**

## Quick Start

Pull any design skill directly into your project using the [TypeUI CLI](https://github.com/bergside/typeui.sh):

```bash
npx typeui.sh pull <slug>
```

For example, to pull the Glassmorphism design skill:

```bash
npx typeui.sh pull glassmorphism
```

Or browse all available skills interactively:

```bash
npx typeui.sh list
```

## What is a Design Skill?

A design skill is a folder containing `SKILL.md` and `DESIGN.md`.

`SKILL.md` acts as the instruction source for AI agents and LLMs. It contains:

- **Brand & mission** — the design philosophy and visual identity
- **Style foundations** — typography scale, color palette, spacing system
- **Component families** — buttons, inputs, cards, modals, navigation, and more
- **Accessibility rules** — WCAG 2.2 AA compliance, keyboard-first interactions
- **Writing tone** — content and voice guidelines
- **Do/Don't rules** — explicit patterns and anti-patterns
- **Quality gates** — testable acceptance criteria for code review

`DESIGN.md` is a companion document for human readers and maintainers. It captures:

- **Design overview** — concise summary of the visual direction
- **Rationale and references** — context for why patterns/tokens exist
- **Maintenance notes** — guidance for keeping design decisions aligned over time

When an AI agent reads a skill file, it follows the `SKILL.md` guidelines to generate UI code that is consistent, accessible, and true to the design system.

## Design Skills

Browse and preview all design skills at [typeui.sh/design-skills](https://typeui.sh/design-skills) before pulling them into your project.

**Total skills:** 67

| Skill | Thumbnail | Preview | Pull Command |
|-------|-----------|---------|-------------|
| **Agentic** | [<img src="https://www.typeui.sh/registry-examples/agentic.png" alt="Agentic thumbnail" width="280" />](https://typeui.sh/design-skills/agentic) | [Preview](https://typeui.sh/design-skills/agentic) | `npx typeui.sh pull agentic` |
| **Ant** | [<img src="https://www.typeui.sh/registry-examples/ant.png" alt="Ant thumbnail" width="280" />](https://typeui.sh/design-skills/ant) | [Preview](https://typeui.sh/design-skills/ant) | `npx typeui.sh pull ant` |
| **Application** | [<img src="https://www.typeui.sh/registry-examples/application.png" alt="Application thumbnail" width="280" />](https://typeui.sh/design-skills/application) | [Preview](https://typeui.sh/design-skills/application) | `npx typeui.sh pull application` |
| **Artistic** | [<img src="https://www.typeui.sh/registry-examples/artistic.png" alt="Artistic thumbnail" width="280" />](https://typeui.sh/design-skills/artistic) | [Preview](https://typeui.sh/design-skills/artistic) | `npx typeui.sh pull artistic` |
| **Bento** | [<img src="https://www.typeui.sh/registry-examples/bento.png" alt="Bento thumbnail" width="280" />](https://typeui.sh/design-skills/bento) | [Preview](https://typeui.sh/design-skills/bento) | `npx typeui.sh pull bento` |
| **Bold** | [<img src="https://www.typeui.sh/registry-examples/bold.png" alt="Bold thumbnail" width="280" />](https://typeui.sh/design-skills/bold) | [Preview](https://typeui.sh/design-skills/bold) | `npx typeui.sh pull bold` |
| **Brutalism** | [<img src="https://www.typeui.sh/registry-examples/brutalism.png" alt="Brutalism thumbnail" width="280" />](https://typeui.sh/design-skills/brutalism) | [Preview](https://typeui.sh/design-skills/brutalism) | `npx typeui.sh pull brutalism` |
| **Cafe** | [<img src="https://www.typeui.sh/registry-examples/cafe.png" alt="Cafe thumbnail" width="280" />](https://typeui.sh/design-skills/cafe) | [Preview](https://typeui.sh/design-skills/cafe) | `npx typeui.sh pull cafe` |
| **Claymorphism** | [<img src="https://www.typeui.sh/registry-examples/claymorphism.png" alt="Claymorphism thumbnail" width="280" />](https://typeui.sh/design-skills/claymorphism) | [Preview](https://typeui.sh/design-skills/claymorphism) | `npx typeui.sh pull claymorphism` |
| **Claude** | [<img src="https://www.typeui.sh/registry-examples/claude.png" alt="Claude thumbnail" width="280" />](https://typeui.sh/design-skills/claude) | [Preview](https://typeui.sh/design-skills/claude) | `npx typeui.sh pull claude` |
| **Clean** | [<img src="https://www.typeui.sh/registry-examples/clean.png" alt="Clean thumbnail" width="280" />](https://typeui.sh/design-skills/clean) | [Preview](https://typeui.sh/design-skills/clean) | `npx typeui.sh pull clean` |
| **Codex** | [<img src="https://www.typeui.sh/registry-examples/open.png" alt="Codex thumbnail" width="280" />](https://typeui.sh/design-skills/codex) | [Preview](https://typeui.sh/design-skills/codex) | `npx typeui.sh pull codex` |
| **Colorful** | [<img src="https://www.typeui.sh/registry-examples/colorful.png" alt="Colorful thumbnail" width="280" />](https://typeui.sh/design-skills/colorful) | [Preview](https://typeui.sh/design-skills/colorful) | `npx typeui.sh pull colorful` |
| **Contemporary** | [<img src="https://www.typeui.sh/registry-examples/contemporary.png" alt="Contemporary thumbnail" width="280" />](https://typeui.sh/design-skills/contemporary) | [Preview](https://typeui.sh/design-skills/contemporary) | `npx typeui.sh pull contemporary` |
| **Corporate** | [<img src="https://www.typeui.sh/registry-examples/corporate.png" alt="Corporate thumbnail" width="280" />](https://typeui.sh/design-skills/corporate) | [Preview](https://typeui.sh/design-skills/corporate) | `npx typeui.sh pull corporate` |
| **Cosmic** | [<img src="https://www.typeui.sh/registry-examples/cosmic.png" alt="Cosmic thumbnail" width="280" />](https://typeui.sh/design-skills/cosmic) | [Preview](https://typeui.sh/design-skills/cosmic) | `npx typeui.sh pull cosmic` |
| **Creative** | [<img src="https://www.typeui.sh/registry-examples/creative.png" alt="Creative thumbnail" width="280" />](https://typeui.sh/design-skills/creative) | [Preview](https://typeui.sh/design-skills/creative) | `npx typeui.sh pull creative` |
| **Dashboard** | [<img src="https://www.typeui.sh/registry-examples/dashboard.png" alt="Dashboard thumbnail" width="280" />](https://typeui.sh/design-skills/dashboard) | [Preview](https://typeui.sh/design-skills/dashboard) | `npx typeui.sh pull dashboard` |
| **Dithered** | [<img src="https://www.typeui.sh/registry-examples/dithered.png" alt="Dithered thumbnail" width="280" />](https://typeui.sh/design-skills/dithered) | [Preview](https://typeui.sh/design-skills/dithered) | `npx typeui.sh pull dithered` |
| **Doodle** | [<img src="https://www.typeui.sh/registry-examples/hand-drawn.png" alt="Doodle thumbnail" width="280" />](https://typeui.sh/design-skills/doodle) | [Preview](https://typeui.sh/design-skills/doodle) | `npx typeui.sh pull doodle` |
| **Dramatic** | [<img src="https://www.typeui.sh/registry-examples/dramatic.png" alt="Dramatic thumbnail" width="280" />](https://typeui.sh/design-skills/dramatic) | [Preview](https://typeui.sh/design-skills/dramatic) | `npx typeui.sh pull dramatic` |
| **Editorial** | [<img src="https://www.typeui.sh/registry-examples/editorial.png" alt="Editorial thumbnail" width="280" />](https://typeui.sh/design-skills/editorial) | [Preview](https://typeui.sh/design-skills/editorial) | `npx typeui.sh pull editorial` |
| **Elegant** | [<img src="https://www.typeui.sh/registry-examples/elegant.png" alt="Elegant thumbnail" width="280" />](https://typeui.sh/design-skills/elegant) | [Preview](https://typeui.sh/design-skills/elegant) | `npx typeui.sh pull elegant` |
| **Energetic** | [<img src="https://www.typeui.sh/registry-examples/energetic.png" alt="Energetic thumbnail" width="280" />](https://typeui.sh/design-skills/energetic) | [Preview](https://typeui.sh/design-skills/energetic) | `npx typeui.sh pull energetic` |
| **Enterprise** | [<img src="https://www.typeui.sh/registry-examples/enterprise.png" alt="Enterprise thumbnail" width="280" />](https://typeui.sh/design-skills/enterprise) | [Preview](https://typeui.sh/design-skills/enterprise) | `npx typeui.sh pull enterprise` |
| **Expressive** | [<img src="https://www.typeui.sh/registry-examples/expressive.png" alt="Expressive thumbnail" width="280" />](https://typeui.sh/design-skills/expressive) | [Preview](https://typeui.sh/design-skills/expressive) | `npx typeui.sh pull expressive` |
| **Fantasy** | [<img src="https://www.typeui.sh/registry-examples/fantasy.png" alt="Fantasy thumbnail" width="280" />](https://typeui.sh/design-skills/fantasy) | [Preview](https://typeui.sh/design-skills/fantasy) | `npx typeui.sh pull fantasy` |
| **Fiction** | [<img src="https://www.typeui.sh/registry-examples/fiction.png" alt="Fiction thumbnail" width="280" />](https://typeui.sh/design-skills/fiction) | [Preview](https://typeui.sh/design-skills/fiction) | `npx typeui.sh pull fiction` |
| **Flat** | [<img src="https://www.typeui.sh/registry-examples/flat.png" alt="Flat thumbnail" width="280" />](https://typeui.sh/design-skills/flat) | [Preview](https://typeui.sh/design-skills/flat) | `npx typeui.sh pull flat` |
| **Friendly** | [<img src="https://www.typeui.sh/registry-examples/friendly.png" alt="Friendly thumbnail" width="280" />](https://typeui.sh/design-
