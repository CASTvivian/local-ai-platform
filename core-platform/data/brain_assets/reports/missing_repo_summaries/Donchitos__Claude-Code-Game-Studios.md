# Missing Repo Summary Source: Donchitos/Claude-Code-Game-Studios

- URL: https://github.com/Donchitos/Claude-Code-Game-Studios
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/Donchitos__Claude-Code-Game-Studios
- Clone Status: cloned
- Language: Shell
- Stars: 18524
- Topics: ai-agents, ai-assisted-development, anthropic, claude, claude-code, game-design, game-development, gamedev, godot, indie-game-dev, unity, unreal-engine
- Description: Turn Claude Code into a full game dev studio — 49 AI agents, 72 workflow skills, and a complete coordination system mirroring real studio hierarchy.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <h1 align="center">Claude Code Game Studios</h1>
  <p align="center">
    Turn a single Claude Code session into a full game development studio.
    <br />
    49 agents. 72 skills. One coordinated AI team.
  </p>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License"></a>
  <a href=".claude/agents"><img src="https://img.shields.io/badge/agents-49-blueviolet" alt="49 Agents"></a>
  <a href=".claude/skills"><img src="https://img.shields.io/badge/skills-72-green" alt="72 Skills"></a>
  <a href=".claude/hooks"><img src="https://img.shields.io/badge/hooks-12-orange" alt="12 Hooks"></a>
  <a href=".claude/rules"><img src="https://img.shields.io/badge/rules-11-red" alt="11 Rules"></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/built%20for-Claude%20Code-f5f5f5?logo=anthropic" alt="Built for Claude Code"></a>
  <a href="https://www.buymeacoffee.com/donchitos3"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Support%20this%20project-FFDD00?logo=buymeacoffee&logoColor=black" alt="Buy Me a Coffee"></a>
  <a href="https://github.com/sponsors/Donchitos"><img src="https://img.shields.io/badge/GitHub%20Sponsors-Support%20this%20project-ea4aaa?logo=githubsponsors&logoColor=white" alt="GitHub Sponsors"></a>
</p>

---

## Why This Exists

Building a game solo with AI is powerful — but a single chat session has no structure. No one stops you from hardcoding magic numbers, skipping design docs, or writing spaghetti code. There's no QA pass, no design review, no one asking "does this actually fit the game's vision?"

**Claude Code Game Studios** solves this by giving your AI session the structure of a real studio. Instead of one general-purpose assistant, you get 49 specialized agents organized into a studio hierarchy — directors who guard the vision, department leads who own their domains, and specialists who do the hands-on work. Each agent has defined responsibilities, escalation paths, and quality gates.

The result: you still make every decision, but now you have a team that asks the right questions, catches mistakes early, and keeps your project organized from first brainstorm to launch.

---

## Table of Contents

- [What's Included](#whats-included)
- [Studio Hierarchy](#studio-hierarchy)
- [Slash Commands](#slash-commands)
- [Getting Started](#getting-started)
- [Upgrading](#upgrading)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [Design Philosophy](#design-philosophy)
- [Customization](#customization)
- [Platform Support](#platform-support)
- [Community](#community)
- [Supporting This Project](#supporting-this-project)
- [License](#license)

---

## What's Included

| Category | Count | Description |
|----------|-------|-------------|
| **Agents** | 49 | Specialized subagents across design, programming, art, audio, narrative, QA, and production |
| **Skills** | 72 | Slash commands for every workflow phase (`/start`, `/design-system`, `/create-epics`, `/create-stories`, `/dev-story`, `/story-done`, etc.) |
| **Hooks** | 12 | Automated validation on commits, pushes, asset changes, session lifecycle, agent audit trail, and gap detection |
| **Rules** | 11 | Path-scoped coding standards enforced when editing gameplay, engine, AI, UI, network code, and more |
| **Templates** | 39 | Document templates for GDDs, UX specs, ADRs, sprint plans, HUD design, accessibility, and more |

## Studio Hierarchy

Agents are organized into three tiers, matching how real studios operate:

```
Tier 1 — Directors (Opus)
  creative-director    technical-director    producer

Tier 2 — Department Leads (Sonnet)
  game-designer        lead-programmer       art-director
  audio-director       narrative-director    qa-lead
  release-manager      localization-lead

Tier 3 — Specialists (Sonnet/Haiku)
  gameplay-programmer  engine-programmer     ai-programmer
  network-programmer   tools-programmer      ui-programmer
  systems-designer     level-designer        economy-designer
  technical-artist     sound-designer        writer
  world-builder        ux-designer           prototyper
  performance-analyst  devops-engineer       analytics-engineer
  security-engineer    qa-tester             accessibility-specialist
  live-ops-designer    community-manager
```

### Engine Specialists

The template includes agent sets for all three major engines. Use the set that matches your project:

| Engine | Lead Agent | Sub-Specialists |
|--------|-----------|-----------------|
| **Godot 4** | `godot-specialist` | GDScript, Shaders, GDExtension |
| **Unity** | `unity-specialist` | DOTS/ECS, Shaders/VFX, Addressables, UI Toolkit |
| **Unreal Engine 5** | `unreal-specialist` | GAS, Blueprints, Replication, UMG/CommonUI |

## Slash Commands

Type `/` in Claude Code to access all 72 skills:

**Onboarding & Navigation**
`/start` `/help` `/project-stage-detect` `/setup-engine` `/adopt`

**Game Design**
`/brainstorm` `/map-systems` `/design-system` `/quick-design` `/review-all-gdds` `/propagate-design-change`

**Art & Assets**
`/art-bible` `/asset-spec` `/asset-audit`

**UX & Interface Design**
`/ux-design` `/ux-review`

**Architecture**
`/create-architecture` `/architecture-decision` `/architecture-review` `/create-control-manifest`

**Stories & Sprints**
`/create-epics` `/create-stories` `/dev-story` `/sprint-plan` `/sprint-status` `/story-readiness` `/story-done` `/estimate`

**Reviews & Analysis**
`/design-review` `/code-review` `/balance-check` `/content-audit` `/scope-check` `/perf-profile` `/tech-debt` `/gate-check` `/consistency-check`

**QA & Testing**
`/qa-plan` `/smoke-check` `/soak-test` `/regression-suite` `/test-setup` `/test-helpers` `/test-evidence-review` `/test-flakiness` `/skill-test` `/skill-improve`

**Production**
`/milestone-review` `/retrospective` `/bug-report` `/bug-triage` `/reverse-document` `/playtest-report`

**Release**
`/release-checklist` `/launch-checklist` `/changelog` `/patch-notes` `/hotfix`

**Creative & Content**
`/prototype` `/onboard` `/localize`

**Team Orchestration** (coordinate multiple agents on a single feature)
`/team-combat` `/team-narrative` `/team-ui` `/team-release` `/team-polish` `/team-audio` `/team-level` `/team-live-ops` `/team-qa`

## Getting Started

### Prerequisites

- [Git](https://git-scm.com/)
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`npm install -g @anthropic-ai/claude-code`)
- **Recommended**: [jq](https://jqlang.github.io/jq/) (for hook validation) and Python 3 (for JSON validation)

All hooks fail gracefully if optional tools are missing — nothing breaks, you just lose validation.

### Setup

1. **Clone or use as template**:
   ```bash
   git clone https://github.com/Donchitos/Claude-Code-Game-Studios.git my-game
   cd my-game
   ```

2. **Open Claude Code** and start a session:
   ```bash
   claude
   ```

3. **Run `/start`** — the system asks where you are (no idea, vague concept,
   clear design, existing work) and guides you to the right workflow. No assumptions.

   Or jump directly to a specific skill if you already know what you need:
   - `/brainstorm` — explore game ideas from scratch
   - `/setup-engine godot 4.6` — configure your engine if you already know
   - `/project-stage-detect` — analyze an existing project

## Upgrading

Already using an older version of this template? See [UPGRADING.md](UPGRADING.md)
for step-by-step migration instructions, a breakdown of what changed between
versions, and which files are safe to overwrite vs. which need a manual merge.

## Project Structure

```
CLAUDE.md                           # Master configuration
.claude/
  settings.json                     # Hooks, permissions, safety rules
  agents/                           # 49 agent definitions (markdown + YAML frontmatter)
  skills/                           # 72 slash commands (subdirectory per skill)
  hooks/                            # 12 hook scripts (bash, cross-platform)
  rules/                            # 11 path-scoped coding standards
  statusline.sh                     # Status line script (context%, model, stage, epic breadcrumb)
  docs/
    workflow-catalog.yaml           # 7-phase pipeline definition (read by /help)
    templates/                      # 39 document templates
src/                                # Game source code
assets/                             # Art, audio, VFX, shaders, data files
design/                             # GDDs, narrative docs, level designs
docs/                               # Technical documentation and ADRs
tests/                              # Test suites (unit, integration, performance, playtest)
tools/                              # Build and pipeline tools
prototypes/                         # Throwaway prototypes (isolated from src/)
production/                         # Sprint plans, milestones, release tracking
```

## How It Works

### Agent Coordination

Agents follow a structured delegation model:

1. **Vertical delegation** — directors delegate to leads, leads delegate to specialists
2. **Horizontal consultation** — same-tier agents can consult each other but can't make binding cross-domain decisions
3. **Conflict resolution** — disagreements escalate up to the shared parent (`creative-director` for design, `technical-director` for technical)
4. **Change propagation** — cross-department changes are coordinated by `producer`
5. **Domain boundaries** — agents don't modify files outside their domain without explicit delegation

### Collaborative, Not Autonomous

This is **not** an auto-pilot system. Every agent follows a strict collaboration protocol:

1. **Ask** — agents ask questions before proposing solutions
2. **Present options** — agents show 2-4 options with pros/cons
3. **You decide** — the user always makes the call
4. **Draft** — agents show work before finalizing
5. **Approve** — nothing gets written without your sign-off

Y

# FILE: docs/WORKFLOW-GUIDE.md

# Claude Code Game Studios -- Complete Workflow Guide

> **How to go from zero to a shipped game using the Agent Architecture.**
>
> This guide walks you through every phase of game development using the
> 48-agent system, 68 slash commands, and 12 automated hooks. It assumes you
> have Claude Code installed and are working from the project root.
>
> The pipeline has 7 phases. Each phase has a formal gate (`/gate-check`)
> that must pass before you advance. The authoritative phase sequence is
> defined in `.claude/docs/workflow-catalog.yaml` and read by `/help`.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Phase 1: Concept](#phase-1-concept)
3. [Phase 2: Systems Design](#phase-2-systems-design)
4. [Phase 3: Technical Setup](#phase-3-technical-setup)
5. [Phase 4: Pre-Production](#phase-4-pre-production)
6. [Phase 5: Production](#phase-5-production)
7. [Phase 6: Polish](#phase-6-polish)
8. [Phase 7: Release](#phase-7-release)
9. [Cross-Cutting Concerns](#cross-cutting-concerns)
10. [Appendix A: Agent Quick-Reference](#appendix-a-agent-quick-reference)
11. [Appendix B: Slash Command Quick-Reference](#appendix-b-slash-command-quick-reference)
12. [Appendix C: Common Workflows](#appendix-c-common-workflows)

---

## Quick Start

### What You Need

Before you start, make sure you have:

- **Claude Code** installed and working
- **Git** with Git Bash (Windows) or standard terminal (Mac/Linux)
- **jq** (optional but recommended -- hooks fall back to `grep` if missing)
- **Python 3** (optional -- some hooks use it for JSON validation)

### Step 1: Clone and Open

```bash
git clone <repo-url> my-game
cd my-game
```

### Step 2: Run /start

If this is your first session:

```
/start
```

This guided onboarding asks where you are and routes you to the right phase:

- **Path A** -- No idea yet: routes to `/brainstorm`
- **Path B** -- Vague idea: routes to `/brainstorm` with seed
- **Path C** -- Clear concept: routes to `/setup-engine` and `/map-systems`
- **Path D1** -- Existing project, few artifacts: normal flow
- **Path D2** -- Existing project, GDDs/ADRs exist: runs `/project-stage-detect`
  then `/adopt` for brownfield migration

### Step 3: Verify Hooks Are Working

Start a new Claude Code session. You should see output from the
`session-start.sh` hook:

```
=== Claude Code Game Studios -- Session Context ===
Branch: main
Recent commits:
  abc1234 Initial commit
===================================
```

If you see this, hooks are working. If not, check `.claude/settings.json` to
make sure the hook paths are correct for your OS.

### Step 4: Ask for Help Anytime

At any point, run:

```
/help
```

This reads your current phase from `production/stage.txt`, checks which
artifacts exist, and tells you exactly what to do next. It distinguishes
between REQUIRED next steps and OPTIONAL opportunities.

### Step 5: Create Your Directory Structure

Directories are created as needed. The system expects this layout:

```
src/                  # Game source code
  core/               # Engine/framework code
  gameplay/           # Gameplay systems
  ai/                 # AI systems
  networking/         # Multiplayer code
  ui/                 # UI code
  tools/              # Dev tools
assets/               # Game assets
  art/                # Sprites, models, textures
  audio/              # Music, SFX
  vfx/                # Particle effects
  shaders/            # Shader files
  data/               # JSON config/balance data
design/               # Design documents
  gdd/                # Game design documents
  narrative/          # Story, lore, dialogue
  levels/             # Level design documents
  balance/            # Balance spreadsheets and data
  ux/                 # UX specifications
docs/                 # Technical documentation
  architecture/       # Architecture Decision Records
  api/                # API documentation
  postmortems/        # Post-mortems
tests/                # Test suites
prototypes/           # Throwaway prototypes
production/           # Sprint plans, milestones, releases
  sprints/
  milestones/
  releases/
  epics/              # Epic and story files (from /create-epics + /create-stories)
  playtests/          # Playtest reports
  session-state/      # Ephemeral session state (gitignored)
  session-logs/       # Session audit trail (gitignored)
```

> **Tip:** You do not need all of these on day one. Create directories as you
> reach the phase that needs them. The important thing is to follow this
> structure when you do create them, because the **rules system** enforces
> standards based on file paths. Code in `src/gameplay/` gets gameplay rules,
> code in `src/ai/` gets AI rules, and so on.

---

## Phase 1: Concept

### What Happens in This Phase

You go from "no idea" or "vague idea" to a structured game concept document
with defined pillars and a player journey. This is where you figure out
**what** you are making and **why**.

### Phase 1 Pipeline

```
/brainstorm  -->  game-concept.md  -->  /design-review  -->  /setup-engine
     |                                        |                    |
     v                                        v                    v
  10 concepts     Concept doc with       Validation          Engine pinned in
  MDA analysis    pillars, MDA,          of concept          technical-preferences.md
  Player motiv.   core loop, USP         document
                                                                   |
                                                                   v
                                                             /map-systems
                                                                   |
                                                                   v
                                                            systems-index.md
                                                            (all systems, deps,
                                                             priority ti

# FILE: docs/COLLABORATIVE-DESIGN-PRINCIPLE.md

# Collaborative Design Principle

**Last Updated:** 2026-02-13

---

## 🎯 Core Philosophy

This agent architecture is designed for **USER-DRIVEN COLLABORATION**, not autonomous AI generation.

### ✅ The Right Model: Collaborative Consultant

```
Agent = Expert Consultant
User = Creative Director (Final Decision Maker)

Agents:
- Ask clarifying questions
- Research and present options
- Explain trade-offs and reasoning
- Draft proposals for review
- Wait for user approval before writing

Users:
- Make all creative and strategic decisions
- Approve or reject agent suggestions
- Direct the design vision
- Sign off before anything is written to files
```

### ❌ The Wrong Model: Autonomous Generator

```
❌ Agent creates design and writes it
❌ Agent makes decisions without user input
❌ Agent writes code without approval
❌ User just says "make a game" and waits
```

---

## 🔄 Collaborative Workflow Pattern

Every agent interaction should follow this pattern:

### Pattern: Question → Options → Decision → Draft → Approval

```
1. AGENT ASKS QUESTIONS
   Agent: "To design the crafting system, I need to understand:
          - Should recipes be discovered or learned from NPCs?
          - How punishing should failed attempts be?
          - Is there a resource cost to experimentation?"

2. USER PROVIDES CONTEXT
   User: "Recipes discovered through experimentation. Failed attempts should consume
         materials but give partial XP. We're targeting Explorers primarily."

3. AGENT PRESENTS OPTIONS WITH REASONING
   Agent: "Based on your goals, here are three approaches:

          **Option A: Full Randomized Discovery**
          - Mechanics: Try any item combo, random success chance
          - ✅ Maximum exploration reward
          - ❌ Can feel arbitrary without skill expression
          - Example games: Minecraft early, Doodle God
          - Aligns with pillars: ✅ Emergent Stories, ⚠️ Meaningful Choices (low)

          **Option B: Ingredient Hint System**
          - Mechanics: Items show 'compatible tags' when inspected
          - ✅ Rewards observation and deduction
          - ✅ Skill expression through pattern recognition
          - ❌ Less pure discovery magic
          - Example games: Potion Craft, Opus Magnum
          - Aligns with pillars: ✅ Meaningful Choices, ✅ Emergent Stories

          **Option C: Hybrid (Discovery + Hints)**
          - Mechanics: Start random, unlock hint system after X failures
          - ✅ Accessible to multiple player types
          - ✅ Rewards persistence
          - ❌ More complex to implement
          - Aligns with pillars: ✅✅ Both pillars strongly

          Which approach aligns best with your vision?"

4. USER DECIDES
   User: "Option C feels right. Let's set X = 5 failures to unlock hints."

5. AGENT DRAFTS BASED ON DECISION
   Agent: "Great. Here's a draft of the core mechanic:

          ### Core Loop
          1. Player selects 2-4 ingredients from inventory
          2. System checks against recipe database
          3. If match: Success! Recipe learned, item created, full XP
          4. If no match: Failure. Materials consumed, 25% XP gained
          5. After 5 failures on any item combo, hint system unlocks for those items
          6. Hints show ingredient 'tags' (e.g., 'Fire', 'Healing', 'Metal')

          ### Formula Proposal
          success_xp = base_xp * recipe_tier^1.5
          failure_xp = success_xp * 0.25
          hint_unlock_threshold = 5  # Failures to unlock hints

          Does this match your intent?"

6. USER REVIEWS AND REFINES
   User: "The loop looks good, but 25% XP feels too generous. Make it 15%.
         Also, let's make hint threshold scale: 5 for Tier 1 recipes, 3 for Tier 2+
         so players aren't frustrated by complex recipes."

7. AGENT UPDATES DRAFT
   Agent: "Updated:
          failure_xp = success_xp * 0.15
          hint_unlock_threshold = 5 if recipe_tier == 1 else 3

          Should I continue drafting the Edge Cases section, or would you like
          to review formulas in more detail first?"

8. USER APPROVES NEXT STEP
   User: "Formulas are good. Continue with Edge Cases."

9. [REPEAT CYCLE FOR EACH SECTION]

10. FINAL APPROVAL BEFORE WRITING
    Agent: "The full GDD draft is complete. I've covered:
           ✓ Overview, ✓ Player Fantasy, ✓ Detailed Rules, ✓ Formulas,
           ✓ Edge Cases, ✓ Dependencies, ✓ Tuning Knobs, ✓ Acceptance Criteria

           May I write this to design/gdd/crafting-system.md?"

    User: "Yes, write it."  ← ONLY NOW does file get created

11. AGENT WRITES FILE
    Agent: [Uses Write tool]
           "Created design/gdd/crafting-system.md. Would you like me to run
            /design-review to validate it against the standard?"
```

---

## 📋 How This Applies to Different Tasks

### 🎨 Design Tasks

**Example:** "Design the combat system"

```
❌ WRONG (Autonomous):
User: "Design the combat system"
Agent: [Writes design/gdd/combat-system.md with full design]
Agent: "Done! Here's your combat system."

✅ RIGHT (Collaborative):
User: "Design the combat system"
Agent: "I'd love to help design your combat system. First, some questions:
       1. What's the core fantasy? (precise timing? tactical positioning? resource management?)
       2. Real-time or turn-based?
       3. How much depth vs accessibility? (think Celeste vs Dark Souls)
       4. Any reference games that nail the feel you want?"

User: [Answers questions]
Agent: [Presents 3 combat approaches with pros/cons]
User: [Picks one, refines it]
Agent: [Drafts mechanics section]
User: [Reviews, requests changes]
Agent: [Iterates until user approves]
Agent: "Ready to write to design/gdd/combat-system.md?"
User: "Yes"
Agent: [Writes file]
```

### 💻 Coding Tasks

**Example:** "Implement the damage calculation"

```
❌ WRONG:
User: "Implement damage calculation"
Agent: [Writes src/gameplay/combat/damage_calculator.gd]
Agent: "Implemented!"

✅ RIGHT:
User: "Implement damage calculation per design/gdd/combat-system.

# FILE: docs/CLAUDE.md

# Docs Directory

When authoring or editing files in this directory, follow these standards.

## Architecture Decision Records (`docs/architecture/`)

Use the ADR template: `.claude/docs/templates/architecture-decision-record.md`

**Required sections:** Title, Status, Context, Decision, Consequences,
ADR Dependencies, Engine Compatibility, GDD Requirements Addressed

**Status lifecycle:** `Proposed` → `Accepted` → `Superseded`
- Never skip `Accepted` — stories referencing a `Proposed` ADR are auto-blocked
- Use `/architecture-decision` to create ADRs through the guided flow

**TR Registry:** `docs/architecture/tr-registry.yaml`
- Stable requirement IDs (e.g. `TR-MOV-001`) that link GDD requirements to stories
- Never renumber existing IDs — only append new ones
- Updated by `/architecture-review` Phase 8

**Control Manifest:** `docs/architecture/control-manifest.md`
- Flat programmer rules sheet: Required / Forbidden / Guardrails per layer
- Date-stamped `Manifest Version:` in header
- Stories embed this version; `/story-done` checks for staleness

**Validation:** Run `/architecture-review` after completing a set of ADRs.

## Engine Reference (`docs/engine-reference/`)

Version-pinned engine API snapshots. **Always check here before using any
engine API** — the LLM's training data predates the pinned engine version.

Current engine: see `docs/engine-reference/godot/VERSION.md`


# FILE: docs/examples/session-design-crafting-system.md

# Example Session: Designing the Crafting System

**Context:** Solo indie dev, week 2 of project, needs to design the crafting system mentioned in the game pillars.

**Starting State:**
- Game concept and pillars defined
- Engine set up (Godot 4.6)
- Core combat system designed but not implemented yet
- Pillar 2: "Emergent Discovery Through Experimentation"

**Session Duration:** ~45 minutes
**Turns:** 12
**Outcome:** Complete crafting system GDD ready for implementation

---

## Turn 1: User Initiates Design

**User:**
> I need to design the crafting system. Pillar 2 is "Emergent Discovery Through Experimentation", so I want players to discover recipes by trying combinations.

## Turn 2: Agent Asks Clarifying Questions

**Agent (game-designer):**
> I'll help design the crafting system with discovery at its core. Before proposing mechanics, I need to understand your vision:
>
> 1. **Discovery Method**: Should recipes be pure trial-and-error, or should there be hints/clues to guide players?
> 2. **Failure Punishment**: When players try an invalid combination, what happens?
>    - Materials completely lost (harsh)
>    - Materials partially refunded (moderate)
>    - No cost to experiment (forgiving)
> 3. **Progression**: Does crafting skill improve over time? If so, what does higher skill unlock?
> 4. **Scope**: How central is crafting to the game? Core pillar feature or supporting system?
> 5. **Reference Games**: Any crafting systems you love or hate? (Minecraft, Terraria, Stardew Valley, Potion Craft?)

## Turn 3: User Provides Context

**User:**
> 1. I want hints that unlock gradually - start with pure discovery, earn hints through skill
> 2. Moderate punishment - waste materials but gain partial XP
> 3. Yes, skill unlocks hint system and improves success rates
> 4. Core feature - one of the three main loops (combat, exploration, crafting)
> 5. Love Potion Craft's deduction mechanic. Hate Minecraft wikis being mandatory.

## Turn 4: Agent Presents Options

**Agent:**
> Perfect context! Based on "emergent discovery" + "deduction over wikis" + "Potion Craft inspiration", here are three mechanical approaches:
>
> **Option A: Pure Randomized Discovery**
> - **Mechanics**: Try any 2-4 ingredient combo, roll for success based on compatibility
> - **Hint System**: None - players document discoveries manually
> - **Pros**:
>   - Maximum emergent discovery
>   - Community can share findings without breaking core loop
>   - Aligns strongly with "experimentation" pillar
> - **Cons**:
>   - High frustration for completionists
>   - Low skill expression (mostly RNG)
>   - Players may feel "wiki is required" despite your intent
> - **Aligns with Pillars**: ✅✅ Emergent Discovery, ⚠️ Meaningful Choices (randomness reduces agency)
>
> **Option B: Tag-Based Deduction System (Potion Craft-style)**
> - **Mechanics**: Each ingredient has hidden "tags" (Fire, Water, Healing, Damage, etc.)
>   - Recipes require specific tag combinations
>   - At Skill 0: No tags visible, pure experimentation
>   - At Skill 5: Can inspect items to see 1 tag
>   - At Skill 10: See 2 tags, etc.
> - **Hint System**: Tags ARE the hint system, unlocked by skill
> - **Pros**:
>   - Rewards observation and pattern recognition (skill expression!)
>   - Progressive scaffolding - accessible to all player types
>   - Creates "aha!" moments when patterns click
>   - No wiki needed - everything discoverable in-game
> - **Cons**:
>   - More complex to implement (tag system + UI)
>   - Requires careful tag design to avoid degeneracy
> - **Aligns with Pillars**: ✅✅ Emergent Discovery, ✅✅ Meaningful Choices
>
> **Option C: Ingredient Compatibility Matrix**
> - **Mechanics**: Each ingredient pairs well/poorly with others
>   - Success rate = compatibility score
>   - Skill 0: No compatibility shown, ~30% base success
>   - Higher skill: See color-coded compatibility (red/yellow/green)
> - **Hint System**: Visual compatibility indicators unlock with skill
> - **Pros**:
>   - Simple to implement and understand
>   - Clear progression arc (skill = more information)
>   - Feels fair (players understand why they failed)
> - **Cons**:
>   - Less emergent than tag system (more prescriptive)
>   - Optimal recipes more obvious once you have hints
> - **Aligns with Pillars**: ✅ Emergent Discovery, ✅ Meaningful Choices
>
> **My Recommendation: Option B (Tag-Based Deduction)**
>
> **Reasoning:**
> - It's the only option that creates TRUE emergent discovery through systems interaction
> - Players develop mastery by learning tag patterns, not memorizing recipes
> - The progressive reveal (tags unlock with skill) serves both Explorers (discovery) and Achievers (progression)
> - Potion Craft proved this works and is satisfying
> - Avoids wiki-dependency because the deduction is solvable in-game
>
> Which option resonates with your vision? Or should I explore a hybrid?

## Turn 5: User Decides with Modification

**User:**
> Option B feels perfect, but I want to add: failed attempts should give hints about which tags were WRONG, not just which were right. Like "You added Fire, but this recipe needs Water instead."

## Turn 6: Agent Incorporates Feedback and Drafts

**Agent:**
> Excellent modification! That adds a deduction game on TOP of the tag discovery. Now failed attempts aren't just "waste" - they're valuable information.
>
> Let me draft the **Overview** and **Player Fantasy** sections:
>
> ---
>
> ## Overview
>
> The crafting system uses a tag-based deduction mechanic where players experiment with ingredient combinations to discover recipes. Each ingredient has 1-3 hidden tags (Fire, Water, Earth, Air, Healing, Damage, Poison, etc.). Recipes require specific tag combinations. Failed attempts waste materials but provide feedback ("This needs Water, not Fire") that teaches players tag patterns. As crafting skill increases, players unlock the ability to inspect ingredients to see their tags directly, transforming pure experimentation into informed deductio

# FILE: docs/examples/session-story-lifecycle.md

# Example Session: Full Story Lifecycle — /story-readiness → Implement → /story-done

**Context:** Solo indie dev, mid-production sprint. The movement system GDD and architecture are complete. A story for movement's core implementation has been generated by `/create-stories`.

**Starting State:**
- `design/gdd/movement-system.md` — complete, all 8 sections
- `docs/architecture/movement-adr-001.md` — Status: Accepted
- `production/sprints/sprint-03.md` — lists STORY-MOV-001 in backlog
- `production/stories/STORY-MOV-001.md` — exists but not yet validated
- No implementation code yet

**Session Duration:** ~50 minutes
**Turns:** 13
**Outcome:** Story validated ready, implemented, verified complete with `/story-done`

---

## Phase 1: Story Readiness Check

### Turn 1: User Runs Readiness Check

**User:**
> /story-readiness production/stories/STORY-MOV-001.md

### Turn 2: Agent Validates the Story

**Agent (via /story-readiness):**
> Reading `production/stories/STORY-MOV-001.md`...
>
> **STORY-MOV-001: Implement CharacterBody2D movement with terrain modifiers**
>
> Running 4 validation checks:
>
> **1. Design Completeness**
> - GDD referenced: `design/gdd/movement-system.md` ✅
> - GDD section coverage: Detailed Rules ✅, Formulas ✅, Edge Cases ✅
> - TR-IDs embedded: TR-MOV-001 through TR-MOV-008 ✅
>
> **2. Architecture Completeness**
> - ADR referenced: `docs/architecture/movement-adr-001.md` ✅
> - ADR status: **Accepted** ✅ *(Would be BLOCKED if Proposed)*
> - Control manifest version in story: `2026-03-10` — current manifest is `2026-03-10` ✅
>
> **3. Scope Clarity**
> - Acceptance criteria: 9 items, all measurable ✅
> - Out-of-scope items listed: swimming, climbing ✅
> - Ambiguities found: **1**
>   - ⚠️ Story says "roll direction follows last input direction" but GDD says "roll in movement direction" — these conflict when player stops and immediately rolls. Clarify before pickup.
>
> **4. Definition of Done**
> - Tests required: unit tests for formula functions ✅
> - Integration signal: `on_stamina_event` must fire correctly ✅
>
> ---
> **Verdict: NEEDS WORK**
>
> One ambiguity must be resolved before implementation starts. Would you like to resolve it now so I can mark the story as ready?

### Turn 3: User Resolves the Ambiguity

**User:**
> Roll uses last movement direction. If player is standing still, roll uses facing direction instead.

### Turn 4: Agent Updates the Story

**Agent:**
> Updating the story's Detailed Rules section:
>
> > Roll direction: last movement direction. If velocity is zero at roll input, roll uses current facing direction.
>
> May I write this to `production/stories/STORY-MOV-001.md` and set Status to `ready-for-dev`?

**User:**
> Yes

**Agent writes update. Story status: `ready-for-dev`.**

> **Verdict: READY**
> Story is implementation-ready. Pick it up when you're ready to build.

---

## Phase 2: Implementation

### Turn 5: User Starts Implementation

**User:**
> Let's implement STORY-MOV-001. I'm ready to start coding.

### Turn 6: Agent Reads Story and ADR

**Agent (gameplay-programmer):**
> Reading `production/stories/STORY-MOV-001.md`, `design/gdd/movement-system.md`, and `docs/architecture/movement-adr-001.md`...
>
> **Architecture (from ADR-001):**
> - `MovementComponent.gd` — attached to player scene, not a singleton
> - Terrain modifier lookup via `TerrainLayer.get_modifier(tile_position)` helper
> - Stamina events via signal (not direct call to StaminaSystem)
>
> **My proposed file structure:**
> ```
> src/gameplay/movement/
>   movement_component.gd       # CharacterBody2D logic, state machine
>   terrain_modifier_table.gd   # Const table: terrain_type -> {speed_mod, drain_mod}
> tests/unit/
>   test_movement_formulas.gd   # Unit tests for speed/drain calculations
> ```
>
> May I proceed with this structure?

**User:**
> Yes

### Turn 7: Agent Implements and Shows Key Code

**Agent:**
> Implementing `movement_component.gd`. Key excerpt for your review before I write the file:
>
> ```gdscript
> class_name MovementComponent
> extends Node
>
> signal stamina_event(type: String, amount: float)
>
> @export var base_walk_speed: float = 120.0
> @export var run_multiplier: float = 1.7
> @export var stamina_drain_walk: float = 2.0
> @export var stamina_drain_run: float = 6.0
> @export var stamina_cost_roll: float = 15.0
>
> var _is_carrying_heavy: bool = false
>
> func _physics_process(delta: float) -> void:
>     var terrain_mod := _get_terrain_modifier()
>     var effective_speed := _calculate_speed(terrain_mod)
>     # ...
> ```
>
> All values are `@export` — none hardcoded. Is this the direction you want?

**User:**
> Looks good. Write it.

### Turn 8–9: Agent Writes Files and Tests

**Agent writes:**
- `src/gameplay/movement/movement_component.gd`
- `src/gameplay/movement/terrain_modifier_table.gd`
- `tests/unit/test_movement_formulas.gd`

**Agent:**
> Files written. Running available linting checks...
>
> No errors. Tests file created with 6 unit tests covering:
> - Walk speed formula (3 terrain types)
> - Run speed formula
> - Stamina drain calculation
> - Roll stamina cost (with and without zero-velocity edge case)
>
> Manual testing needed for: invincibility frames, slope blocking, terrain integration (requires running scene).

---

## Phase 3: Story Completion

### Turn 10: User Tests Manually and Runs /story-done

**User:**
> I've tested it in the scene — everything works. /story-done production/stories/STORY-MOV-001.md

### Turn 11: Agent Runs Completion Review

**Agent (via /story-done):**
> Reading story, GDD, ADRs...
>
> **Phase 1: Story Located** ✅ `production/stories/STORY-MOV-001.md`
>
> **Phase 2: Acceptance Criteria Verification**
>
> | # | Criterion | Verification | Status |
> |---|-----------|--------------|--------|
> | 1 | Walk speed correct on normal ground | Auto: formula unit tests pass | ✅ AUTO |
> | 2 | Run speed correct | Auto: formula unit tests pass | ✅ AUTO |
> | 3 | Run cancels at stamina 0 | Manual: user confirmed | ✅ MA

# FILE: docs/examples/reverse-document-workflow-example.md

# Reverse Documentation Workflow Example

## Scenario
Developer built a working skill tree system but never wrote a design doc.
Code exists in `src/gameplay/skills/`, but `design/gdd/` has no skill-system.md.

---

## Session Transcript

**User:**
```
I have a working skill tree system in src/gameplay/skills/ with about 1200 lines
of code. I never wrote a design doc. Can we create one from the implementation?
```

**Game-Designer (reads code, analyzes):**
```
I've analyzed your skill tree implementation. Here's what I found:

STRUCTURE:
- 3 skill trees: Combat, Survival, Tech
- 5 tiers per tree (unlock via level + prerequisites)
- Total 45 skills (15 per tree)
- Cost: skill points (1 per level, can respec for gold)

MECHANICS:
- Passive skills (stat bonuses)
- Active skills (abilities with cooldowns)
- Synergy bonuses (cross-tree unlocks at tier 4+)

IMPLEMENTATION DETAILS:
- Data-driven (JSON files in assets/data/skills/)
- Save-compatible (skill state serialized)
- UI shows locked/unlocked/available states

QUESTIONS before I draft the design doc:

1. **Design Intent:** Was the 3-tree structure meant to represent player archetypes
   (fighter/survivor/engineer) or playstyle flexibility?

2. **Respec Cost:** Respec costs gold - is this meant to:
   - Discourage frequent respecs (commitment to builds)?
   - Create a gold sink (economy balance)?
   - Or should it be free (experimentation encouraged)?

3. **Synergy System:** Cross-tree synergies appear at tier 4. Was this:
   - Intentional (reward hybrid builds late-game)?
   - Or emergent (accidentally creates hybrid meta)?

4. **Balance Philosophy:** I see some skills are clearly better (tier-5 passive
   is +50% damage). Is this:
   - Power fantasy (late-game should feel OP)?
   - Or unbalanced (needs tuning)?
```

**User:**
```
Good questions! Here's the intent:

1. Yes, the 3 trees are archetypes but I want flexibility
2. Respec should be cheap - I want experimentation
3. Synergies were intentional - hybrid builds are a feature
4. Yeah, tier 5 is meant to be powerful, but +50% might be too much
```

**Game-Designer:**
```
Perfect, that clarifies the vision. Let me draft the design doc:

[Shows draft of design/gdd/skill-system.md]

SECTIONS:
1. Overview (3-tree system, hybrid-friendly, respec-encouraged)
2. Design Pillars:
   - Archetype clarity (each tree has identity)
   - Build flexibility (no lock-in, cheap respec)
   - Synergy rewards (cross-tree combinations viable)
3. Detailed Design (tree structure, unlock rules, respec)
4. Balance Framework (tier power curve, synergy limits)
5. Edge Cases (respec during combat? max skills? cap?)
6. Dependencies (UI, save system, tutorial)
7. Acceptance Criteria (all trees viable, 10+ hybrid builds, clear tooltips)
8. Open Questions:
   - Should respec cost scale with level or stay flat?
   - Tier 5 damage bonus: tune to +30% or keep +50%?

**May I write this to design/gdd/skill-system.md?**
```

**User:**
```
Yes, write it. But let's tune tier 5 to +30% and make respec cost scale.
```

**Game-Designer:**
```
✅ Written to design/gdd/skill-system.md
✅ Marked as [REVERSE-DOCUMENTED FROM IMPLEMENTATION]
✅ Added TODO: Update tier-5 passive to +30% in assets/data/skills/combat-tree.json
✅ Added TODO: Implement scaling respec cost formula

Next steps:
- Run /balance-check to validate skill tree progression curve?
- Create ADR documenting why 3 trees instead of 5?
- Update tutorial to explain hybrid synergies?
```

---

## Key Observations

1. **Agent asked clarifying questions** - didn't just describe code
2. **Separated intent from implementation** - user corrected "accidental" imbalance
3. **Design doc captures "why"** - not just "what the code does"
4. **Identified missing pieces** - edge cases not in code
5. **Flagged follow-up work** - balance tuning, ADRs, tutorial

## Outcome

The design doc now exists and **matches reality** while also capturing the **intended vision**. Future changes will reference this doc, and new team members understand the *why* behind decisions.


# FILE: docs/examples/skill-flow-diagrams.md

# Skill Flow Diagrams

Visual maps of how skills chain together across the 7 development phases.
These show what runs before and after each skill, and what artifacts flow between them.

---

## Full Pipeline Overview (Zero to Ship)

```
PHASE 1: CONCEPT
  /start ──────────────────────────────────────────────────────► routes to A/B/C/D
  /brainstorm ──────────────────────────────────────────────────► design/gdd/game-concept.md
  /setup-engine ────────────────────────────────────────────────► CLAUDE.md + technical-preferences.md
  /design-review [game-concept.md] ────────────────────────────► concept validated
  /gate-check ─────────────────────────────────────────────────► PASS → advance to systems-design
        │
        ▼
PHASE 2: SYSTEMS DESIGN
  /map-systems ────────────────────────────────────────────────► design/gdd/systems-index.md
        │
        ▼ (for each system, in dependency order)
  /design-system [name] ──────────────────────────────────────► design/gdd/[system].md
  /design-review [system].md ─────────────────────────────────► per-GDD review comments
        │
        ▼ (after all MVP GDDs done)
  /review-all-gdds ────────────────────────────────────────────► design/gdd/gdd-cross-review-[date].md
  /gate-check ─────────────────────────────────────────────────► PASS → advance to technical-setup
        │
        ▼
PHASE 3: TECHNICAL SETUP
  /create-architecture ────────────────────────────────────────► docs/architecture/master.md
  /architecture-decision (×N) ─────────────────────────────────► docs/architecture/[adr-nnn].md
  /architecture-review ────────────────────────────────────────► review report + docs/architecture/tr-registry.yaml
  /create-control-manifest ────────────────────────────────────► docs/architecture/control-manifest.md
  /gate-check ─────────────────────────────────────────────────► PASS → advance to pre-production
        │
        ▼
PHASE 4: PRE-PRODUCTION
  [UX — before epics, so specs exist when stories are written]
  /ux-design [screen/hud/patterns] ────────────────────────────► design/ux/*.md
  /ux-review ──────────────────────────────────────────────────► UX specs approved (HARD gate for /team-ui)

  [Test infrastructure — scaffold before stories reference tests]
  /test-setup ─────────────────────────────────────────────────► test framework + CI/CD pipeline
  /test-helpers ───────────────────────────────────────────────► tests/helpers/[engine-specific].gd

  [Stories + prototype]
  /create-epics [layer] ───────────────────────────────────────► production/epics/*/EPIC.md
  /create-stories [epic-slug] ─────────────────────────────────► production/epics/*/story-*.md
  /prototype [core-mechanic] ──────────────────────────────────► prototypes/[name]/
  /playtest-report ────────────────────────────────────────────► tests/playtest/vertical-slice.md
  /sprint-plan new ────────────────────────────────────────────► production/sprints/sprint-01.md
  /gate-check ─────────────────────────────────────────────────► PASS → advance to production
        │
        ▼
PHASE 5: PRODUCTION (repeating sprint loop)
  /sprint-status ──────────────────────────────────────────────► sprint snapshot
  /story-readiness [story] ────────────────────────────────────► story validated READY
        │
        ▼ (pick up and implement)
  /dev-story [story] ──────────────────────────────────────────► routes to correct programmer agent
        │
        ▼ (during implementation, as needed)
  /code-review ────────────────────────────────────────────────► code review report
  /scope-check ────────────────────────────────────────────────► scope creep detected / clear
  /content-audit ──────────────────────────────────────────────► GDD content gaps identified
  /bug-report ─────────────────────────────────────────────────► production/qa/bugs/bug-NNN.md
  /bug-triage ─────────────────────────────────────────────────► bugs re-prioritized + assigned

  [Team skills for feature areas — spawn when working a full feature]
  /team-combat / /team-narrative / /team-ui / /team-level / /team-audio

  [QA cycle per sprint]
  /qa-plan ────────────────────────────────────────────────────► production/qa/qa-plan-sprint-NN.md
  /smoke-check ────────────────────────────────────────────────► smoke test gate (PASS/FAIL)
  /regression-suite ───────────────────────────────────────────► coverage gaps + missing regression tests
  /test-evidence-review ───────────────────────────────────────► evidence quality report
  /test-flakiness ─────────────────────────────────────────────► flaky test report
        │
        ▼
  /story-done [story] ─────────────────────────────────────────► story closed + next surfaced
  /sprint-plan [next] ─────────────────────────────────────────► next sprint
        │
        ▼ (after Production milestone)
  /milestone-review ───────────────────────────────────────────► milestone report
  /gate-check ─────────────────────────────────────────────────► PASS → advance to polish
        │
        ▼
PHASE 6: POLISH
  /perf-profile ───────────────────────────────────────────────► perf report + fixes
  /balance-check ──────────────────────────────────────────────► balance report + fixes
  /asset-audit ────────────────────────────────────────────────► asset compliance report
  /tech-debt ──────────────────────────────────────────────────► docs/tech-debt-register.md
  /soak-test ──────────────────────────────────────────────────► soak test protocol + results
  /localize ───────────────────────────────────────────────────► localization readiness report
  /team-polish ────────────────────────────────────────────────► polish sprint orchestrated
  /team-qa ────────────────────────────────────────────────────► full QA cycle sign-off
  /gate-check ─────────────────────────────────────────────────► PASS → advance to release
        │
        ▼
PHASE 7: RELEASE
  /launch-checklist ───────────────────────────────────────────► launch readiness report
  /release-checklist ───────────────────────────────

# FILE: docs/examples/session-gate-check-phase-transition.md

# Example Session: /gate-check Phase Transition — Systems Design → Technical Setup

**Context:** Solo indie dev, end of week 5. The Systems Design phase feels complete — 6 MVP GDDs written, cross-review done, engine set up. User wants to formally advance to Technical Setup.

**Starting State:**
- `production/stage.txt` — currently `systems-design`
- `design/gdd/systems-index.md` — 6 MVP systems listed, all marked `Status: GDD Complete`
- `design/gdd/` — 6 GDD files present
- `design/gdd/gdd-cross-review-2026-03-10.md` — cross-review report, verdict: CONCERNS (1 low-priority note)
- Engine configured (Godot 4.6, `/setup-engine` complete)

**Session Duration:** ~20 minutes
**Turns:** 7
**Outcome:** Gate passed, `stage.txt` updated to `technical-setup`, clear list of what comes next

---

## Turn 1: User Initiates Gate Check

**User:**
> /gate-check

## Turn 2: Agent Detects Current Phase and Runs the Check

**Agent (via /gate-check):**
> Reading `production/stage.txt` — current phase: **systems-design**
>
> Running gate: **Systems Design → Technical Setup**
>
> ---
> **Required Artifacts Checklist:**
>
> | Artifact | Requirement | Status |
> |----------|-------------|--------|
> | `design/gdd/systems-index.md` | Exists, all MVP systems listed | ✅ |
> | Per-system GDDs | All MVP systems have a GDD | ✅ (6/6) |
> | `/design-review` per GDD | Each GDD reviewed | ✅ (6/6 review comments found) |
> | Cross-GDD review report | `design/gdd/gdd-cross-review-*.md` exists | ✅ |
> | Cross-review verdict | PASS or CONCERNS (not FAIL) | ✅ CONCERNS |
> | Engine configured | `production/stage.txt` or CLAUDE.md engine entry | ✅ Godot 4.6 |
>
> ---
> **Content Scan:**
>
> Checking GDD completeness (8 required sections each)...
>
> | GDD | Missing Sections |
> |-----|-----------------|
> | movement-system.md | None ✅ |
> | stamina-system.md | None ✅ |
> | combat-system.md | None ✅ |
> | inventory-system.md | None ✅ |
> | crafting-system.md | None ✅ |
> | exploration-system.md | None ✅ |
>
> ---
> **Cross-Review Concerns (from `gdd-cross-review-2026-03-10.md`):**
>
> 1. ⚠️ LOW — Crafting and inventory both define "item stack size" independently with different defaults (crafting: 99, inventory: 64). One system should be the authority; the other should reference it. Not blocking — can resolve in ADR.
>
> ---
> **Verdict: PASS**
>
> All required artifacts present. Cross-review concern is LOW severity and can be resolved during Technical Setup via an ADR. This is a normal finding at this stage.
>
> **May I advance `production/stage.txt` to `technical-setup`?**

## Turn 3: User Confirms

**User:**
> Yes, advance it.

## Turn 4: Agent Updates Stage and Presents Next Steps

**Agent:**
> Updated `production/stage.txt` → `technical-setup`
>
> ---
> **You are now in: Technical Setup**
>
> This phase establishes the technical foundation before production coding starts. Your goal is a complete, approved architecture so that every story written in Pre-Production has clear, unambiguous technical guidance.
>
> **Required steps this phase (in order):**
>
> 1. **`/create-architecture`** — Author the master architecture document. Covers system decomposition, data flow, layer boundaries, and module responsibilities.
>
> 2. **`/architecture-decision` (one per significant technical choice)** — At minimum:
>    - Rendering approach (2D camera, viewport, etc.)
>    - Save/load strategy
>    - Audio bus architecture
>    - The "item stack size authority" issue from cross-review (crafting vs inventory)
>
> 3. **`/architecture-review`** — Validates all ADRs for completeness, dependency ordering, and GDD traceability. Produces the TR-registry.
>
> 4. **`/create-control-manifest`** — Converts Accepted ADRs into a flat programmer rules sheet. This is what implementation agents will consult during coding.
>
> 5. **`/gate-check`** — Technical Setup → Pre-Production gate. Requires: architecture doc, all ADRs Accepted, control manifest, and dependency ordering resolved.
>
> **Optional but recommended:**
> - `/tech-debt` scan if you have any prototype code you plan to carry forward
> - `/setup-engine` re-run if you haven't yet fetched Godot 4.6 API snapshots
>
> **Tip:** Start with `/architecture-decision` for the item stack size conflict. It's a quick win that closes an open question before it creates ambiguity in two ADRs later.

## Turn 5: User Asks About the Cross-Review Concern

**User:**
> What do I actually write in the ADR for the stack size conflict?

## Turn 6: Agent Advises

**Agent:**
> The ADR decision is: **which system owns the canonical `max_stack_size` value?**
>
> Two options to consider:
>
> **Option A: Inventory owns it**
> - `ItemData` resource (owned by inventory) gets `max_stack_size: int = 64`
> - Crafting system reads from `ItemData`, never sets its own value
> - Pros: inventory is the source of truth for all item properties
> - Cons: crafting team needs to know to look at inventory data
>
> **Option B: Item data resource owns it (shared resource)**
> - `ItemData.max_stack_size` is the authority for both systems
> - Both crafting and inventory import from `ItemData`
> - Pros: single source, no coupling between crafting and inventory modules
> - Cons: one more thing in the shared data layer
>
> Most studios go with B (shared resource) once they have >2 systems touching item data. But either is valid for a solo project.
>
> Run `/architecture-decision` and it will guide you through the ADR format, including the Dependencies section that links this ADR back to the two GDDs.

## Turn 7: User Wraps Up

**User:**
> Got it. I'll start with /architecture-decision for this.

**Agent:**
> Good starting point. The ADR will document the decision, the reasoning, and the GDD requirements it addresses — so when you write code months from now, the rationale is preserved.
>
> Your phase gate is logged. Run `/help` at any time during Technical Setup to see your current progress against the required checklist.

---

## What This Example 

# FILE: docs/examples/session-implement-combat-damage.md

# Example Session: Implementing Combat Damage Calculation

**Context:** Solo indie dev, week 4 of project, implementing gameplay systems.

**Starting State:**
- `design/gdd/combat-system.md` exists and reviewed
- Godot 4.6 project set up with basic scene structure
- No gameplay code written yet
- Sprint goal: "Implement core combat damage calculation"

**Session Duration:** ~30 minutes
**Turns:** 10
**Outcome:** Working damage calculator with tests, ready for integration

---

## Turn 1: User Requests Implementation

**User:**
> Implement the damage calculation system from design/gdd/combat-system.md. The formula is in section 4.

## Turn 2: Agent Reads Design and Asks Clarifying Questions

**Agent (gameplay-programmer):**
> I've read `design/gdd/combat-system.md`. The damage formula is:
>
> ```
> final_damage = base_damage * (1 + attack_stat * 0.1) * crit_multiplier * type_effectiveness * (1 - target_defense)
> ```
>
> Before implementing, I need to clarify some details that aren't specified in the doc:
>
> **Architecture Questions:**
> 1. Should `DamageCalculator` be a static utility class (no state, just calculations) or an autoload singleton?
> 2. Where should `base_damage` come from? (Weapon data? Character stats? Ability data?)
> 3. Where should `type_effectiveness` values live? (Per weapon? Per damage type? Separate data file?)
>
> **Spec Ambiguities:**
> 4. Should `attack_stat` be clamped to a range? (Prevents exponential scaling bugs)
> 5. The doc says "critical hits do 2x damage" but doesn't specify rounding. Should I `floor()`, `ceil()`, or `round()` the final damage?
> 6. What happens if `target_defense` >= 1.0? (100% mitigation or higher) Should damage go negative or clamp to 0?
>
> **Integration:**
> 7. I don't see a design doc for the Health/HP system. Should I create a minimal one, or is that coming separately?
>
> Please clarify so I can implement this correctly the first time.

## Turn 3: User Resolves Ambiguities

**User:**
> 1. Static utility - no state needed
> 2. Base damage from Weapon resource. I'll create a simple Weapon class.
> 3. Type effectiveness in a separate data file `assets/data/combat_damage.json`
> 4. Yes, clamp attack_stat to 0-100
> 5. Use `floor()` to round down to integers
> 6. Clamp damage to minimum of 1 (always do at least 1 damage, even with 100% defense)
> 7. Create a minimal health component - just current_hp, max_hp, and take_damage() method

## Turn 4: Agent Proposes Architecture

**Agent:**
> Got it! Here's my proposed architecture:
>
> **Files I'll create:**
> ```
> src/gameplay/combat/damage_calculator.gd     # Static damage formula
> src/gameplay/combat/health_component.gd      # HP tracking node component
> src/gameplay/combat/weapon.gd                # Weapon resource
> assets/data/combat_damage.json               # Type effectiveness values
> design/gdd/health-system.md                  # Minimal health doc
> tests/combat/test_damage_calculator.gd       # Unit tests
> ```
>
> **Architecture Details:**
>
> **DamageCalculator** (static class):
> ```gdscript
> class_name DamageCalculator
> extends RefCounted
>
> static func calculate_damage(
>     attacker_stats: Dictionary,
>     weapon: Weapon,
>     defender_stats: Dictionary,
>     is_crit: bool = false
> ) -> int:
>     # Implementation here
>     return floori(final_damage)
> ```
>
> **HealthComponent** (node component):
> ```gdscript
> extends Node
> class_name HealthComponent
>
> signal health_changed(old_hp: int, new_hp: int)
> signal died()
>
> @export var max_hp: int = 100
> var current_hp: int:
>     set(value):
>         # Clamp and emit signals
>
> func take_damage(amount: int) -> void:
>     current_hp -= amount
>     if current_hp <= 0:
>         died.emit()
> ```
>
> **Weapon** (resource):
> ```gdscript
> extends Resource
> class_name Weapon
>
> @export var base_damage: float
> @export var damage_type: String  # "physical", "fire", "ice", etc.
> ```
>
> **combat_damage.json**:
> ```json
> {
>   "crit_multiplier": 2.0,
>   "attack_stat_min": 0,
>   "attack_stat_max": 100,
>   "type_effectiveness": {
>     "physical": { "armored": 0.5, "flesh": 1.0, "crystal": 1.5 },
>     "fire": { "armored": 1.0, "flesh": 1.2, "crystal": 0.3 }
>   }
> }
> ```
>
> **Question:** This architecture makes `DamageCalculator` easily testable (pure function, no dependencies). The `HealthComponent` uses signals for VFX/SFX hookup. Does this match your expectations, or should I change anything before implementing?

## Turn 5: User Approves with Minor Change

**User:**
> Looks good, but change `attacker_stats` and `defender_stats` to proper typed dictionaries or classes. I don't want untyped Dictionary bags floating around.

## Turn 6: Agent Refines Architecture

**Agent:**
> Absolutely - type safety is important. I'll create a `CharacterStats` resource:
>
> ```gdscript
> extends Resource
> class_name CharacterStats
>
> @export var attack_stat: int = 0  # 0-100
> @export var defense: float = 0.0  # 0.0-1.0 (0-100% mitigation)
> @export var armor_type: String = "flesh"  # for type effectiveness lookup
> ```
>
> Then `DamageCalculator.calculate_damage()` signature becomes:
> ```gdscript
> static func calculate_damage(
>     attacker: CharacterStats,
>     weapon: Weapon,
>     defender: CharacterStats,
>     is_crit: bool = false
> ) -> int
> ```
>
> Much cleaner. May I proceed with implementation?

## Turn 7: User Approves Implementation

**User:**
> Yes, implement it.

## Turn 8: Agent Implements and Reports

**Agent:**
> Implementation complete! Here's what I created:
>
> **Files Created:**
> - ✅ `src/gameplay/combat/damage_calculator.gd` (82 lines)
> - ✅ `src/gameplay/combat/health_component.gd` (45 lines)
> - ✅ `src/gameplay/combat/weapon.gd` (12 lines)
> - ✅ `src/gameplay/combat/character_stats.gd` (16 lines)
> - ✅ `assets/data/combat_damage.json` (validated JSON)
> - ✅ `design/gdd/health-system.md` (minimal 8-section doc)
>
> **Rules Enforcement Results:**
>
> The `gameplay-code` rule automat

# FILE: docs/examples/README.md

# Collaborative Session Examples

This directory contains realistic, end-to-end session transcripts showing how the Game Studio Agent Architecture works in practice. Each example demonstrates the **collaborative workflow** where agents ask questions, present options, and wait for user approval rather than autonomously generating content.

---

## Visual Reference

**New to the system? Start here:**
[Skill Flow Diagrams](skill-flow-diagrams.md) — visual maps of all 7 phases and how skills chain together.

---

## 📚 **Available Examples**

### CORE WORKFLOW

### [Skill Flow Diagrams](skill-flow-diagrams.md)
**Type:** Visual Reference
**Complexity:** All levels

Full pipeline overview (zero to ship), plus detailed chain diagrams for:
design-system, story lifecycle, UX pipeline, and brownfield onboarding.
**Start here if you want to understand how the pieces fit together.**

---

### [Session: Authoring a GDD with /design-system](session-design-system-skill.md)
**Type:** Design (skill-driven)
**Skill:** `/design-system`
**Duration:** ~60 minutes (14 turns)
**Complexity:** Medium

**Scenario:**
Dev runs `/design-system movement` after `/map-systems` produced the systems index. The skill loads context from the game concept and dependency GDDs, runs a technical feasibility pre-check, then guides through all 8 GDD sections one at a time — drafting, approving, and writing each section to disk before moving to the next.

**Key Moments:**
- Technical feasibility pre-check flags Jolt physics default change (Godot 4.6)
- Incremental writing: each section on disk immediately after approval
- Session crash during section 5 → agent resumes from first empty section
- Dependency signals (stamina, inventory) surfaced during the Dependencies section
- Ends with explicit handoff: "run `/design-review` before the next system"

**Learn:**
- How `/design-system` is different from asking an agent to "write a GDD"
- How the section-by-section cycle prevents 30k-token context bloat
- How incremental file writing survives session crashes
- How the skill surfaces downstream dependency contracts

---

### [Session: Full Story Lifecycle](session-story-lifecycle.md)
**Type:** Full Workflow
**Skills:** `/story-readiness` → implementation → `/story-done`
**Duration:** ~50 minutes (13 turns)
**Complexity:** Medium

**Scenario:**
Dev picks up a story from the sprint backlog. `/story-readiness` catches a roll-direction ambiguity before any code is written. After implementation, `/story-done` verifies 9 acceptance criteria, identifies 2 deferred criteria (inventory not integrated yet), and closes the story with notes.

**Key Moments:**
- `/story-readiness` catches spec ambiguity in Turn 2 — resolved before implementation starts
- ADR status check: story would be BLOCKED if ADR was still Proposed
- Manifest version check: confirms story's guidance hasn't drifted from current architecture
- Deferred criteria tracked (not lost) when integration not yet possible
- `sprint-status.yaml` updated at story close, next ready story surfaced automatically

**Learn:**
- Why `/story-readiness` prevents late-implementation ambiguity
- How deferred criteria work (COMPLETE WITH NOTES vs. BLOCKED)
- How TR-ID references prevent false deviation flags
- The full loop from backlog → implemented → closed

---

### [Session: Gate Check and Phase Transition](session-gate-check-phase-transition.md)
**Type:** Phase Gate
**Skill:** `/gate-check`
**Duration:** ~20 minutes (7 turns)
**Complexity:** Low

**Scenario:**
Dev completes the Systems Design phase and runs `/gate-check` to advance. The gate finds all 6 MVP GDDs complete, cross-review passed with one low-severity concern. Gate passes, `stage.txt` updated, and the agent provides a specific ordered checklist for Technical Setup.

**Key Moments:**
- Gate validates artifact presence AND internal completeness (8 sections per GDD)
- CONCERNS ≠ FAIL: low-severity cross-review note passes the gate
- stage.txt update changes what `/help`, `/sprint-status`, and all skills see going forward
- Agent surfaces the cross-review concern as a concrete ADR to write next
- Next phase checklist is specific and ordered, not generic

**Learn:**
- What a gate check actually validates (not just "do files exist?")
- How PASS/CONCERNS/FAIL verdicts work
- Why stage.txt is the authority for phase tracking
- What changes after a phase transition

---

### [Session: UX Pipeline — /ux-design → /ux-review → /team-ui](session-ux-pipeline.md)
**Type:** UX Design Pipeline
**Skills:** `/ux-design`, `/ux-review`, `/team-ui`
**Duration:** ~90 minutes (16 turns)
**Complexity:** Medium-High

**Scenario:**
Dev designs the HUD and inventory screen. `/ux-design` reads the player journey and GDDs to ground decisions in player emotional state. `/ux-review` catches a blocking accessibility gap (no keyboard alternative to drag-drop) and an advisory colorblind issue. After fixes, `/team-ui` accepts the handoff.

**Key Moments:**
- HUD philosophy choice (diegetic vs. persistent vs. tactical) grounded in survival genre conventions
- `/ux-review` distinguishes BLOCKING (stops handoff) vs. ADVISORY (can fix in visual pass)
- Accessibility caught before implementation, not during QA
- Keyboard alternative added in one turn; review re-runs and passes
- `/team-ui` checks for a passing `/ux-review` before starting visual design

**Learn:**
- How `/ux-design` uses player journey context to ground UI decisions
- What `/ux-review` actually checks (not just "does a spec exist?")
- The difference between HUD doc (`design/ux/hud.md`) and per-screen specs
- How accessibility issues are handled at design time vs. implementation time

---

### [Session: Brownfield Onboarding with /adopt](session-adopt-brownfield.md)
**Type:** Brownfield Adoption
**Skill:** `/adopt`
**Duration:** ~30 minutes (8 turns)
**Complexity:** Low-Medium

**Scenario:**
Dev has 3 months of existing code and rough design notes but nothing in the right format. `/adopt` audits format compli

# FILE: docs/examples/session-ux-pipeline.md

# Example Session: UX Pipeline — /ux-design → /ux-review → /team-ui

**Context:** Solo indie dev, Pre-Production phase. The HUD and inventory screen are the first UI to design. The game has a player journey doc and GDDs for inventory and combat.

**Starting State:**
- `design/gdd/inventory-system.md` — complete
- `design/gdd/combat-system.md` — complete
- `design/player-journey.md` — complete (6-phase arc defined)
- No UX specs yet
- `design/ux/` directory does not exist

**Session Duration:** ~90 minutes across two sessions (HUD design, then inventory screen)
**Turns:** 16
**Outcome:** `design/ux/hud.md` and `design/ux/screens/inventory.md` created and reviewed; team-ui handed off for visual implementation

---

## Part 1: HUD Design with /ux-design

### Turn 1: User Starts HUD Design

**User:**
> /ux-design hud

### Turn 2: Agent Loads Context and Presents the Approach

**Agent (ux-designer, via /ux-design):**
> Starting HUD design. Loading context...
>
> - `design/player-journey.md` read — key states: Calm Exploration, Tension (threat detected), Crisis (low HP/stamina), Combat
> - `design/gdd/combat-system.md` — HUD needs: HP bar, stamina bar, active ability cooldowns (up to 3), damage numbers
> - `design/gdd/inventory-system.md` — HUD needs: quick slots (4 slots), active item indicator
>
> **HUD Philosophy question:** What is the player's primary attention focus during play?
>
> This determines how aggressive the HUD should be:
> - **Option A: Diegetic (low presence)** — HP shown only when damaged, stamina shown only when draining. World-first, HUD recedes unless urgent.
> - **Option B: Persistent minimal** — HP and stamina always visible, small and unobtrusive. Quick reference without mode-switching.
> - **Option C: Full tactical** — All info always visible (HP, stamina, cooldowns, map, inventory slots). Player always has full awareness.
>
> Given your survival game and "lone survivor" fantasy, A or B is most consistent with the genre.

**User:**
> B — I want it always there but minimal. The player is always managing resources.

### Turn 3: Agent Drafts HUD Philosophy Section

**Agent:**
> **HUD Philosophy draft:**
>
> > **Approach: Persistent Minimal**
> > The HUD is always visible but occupies minimal screen real estate. The player is a resource-managing survivor — denying HP/stamina visibility creates frustration, not tension. All critical stats are readable at a glance without interrupting exploration focus. Elements scale in visual weight when they become urgent (HP below 30% pulses, stamina at 0 flashes), then return to minimal state.
>
> May I write this to `design/ux/hud.md` as the Philosophy section?

**User:**
> Yes

**Agent creates `design/ux/hud.md` and writes Philosophy section.**

*(Turns 4–7 continue the section-by-section HUD authoring: Info Architecture, Zones, Element Specs, State Machine, Visual Budget, Platform Adaptation — each drafted, approved, and written to file.)*

---

**Final HUD structure after all sections:**

```
design/ux/hud.md
  - Philosophy: Persistent Minimal
  - Info Architecture: HP (top-left), Stamina (top-left below HP), Quick Slots (bottom-center),
    Ability Cooldowns (bottom-right), Damage Numbers (world-space)
  - Zones: 4 defined (top-left vitals, bottom-center interaction, bottom-right abilities, world-space)
  - Element Specs: 6 elements with dimensions, font sizes, opacity rules
  - State Machine: Calm / Tension / Crisis / Combat (4 states, transition triggers)
  - Visual Budget: Max 8% screen coverage, 3 simultaneous animations
  - Platform Adaptation: Controller (aim reticle added), Mobile (out of scope v1)
```

---

## Part 2: Inventory Screen with /ux-design

### Turn 8: User Starts Inventory Screen

**User:**
> /ux-design screen inventory

### Turn 9: Agent Scans GDD and Player Journey

**Agent:**
> Loading context for inventory screen...
>
> From `design/gdd/inventory-system.md`:
> - Grid inventory, 6×8 slots
> - Items have weight (affects movement) and stack size
> - Player can equip, drop, inspect, split stacks
>
> From `design/player-journey.md`:
> - Inventory opens frequently during Calm Exploration
> - Players should feel "organized and in control" when opening inventory
> - Anxiety moment: "I need to decide what to drop" — should be clear, not panicked
>
> **Player Need (from journey):** *I need to quickly assess what I'm carrying, decide what to keep or drop, and get back into the world.*
>
> **Key design question:** How do players navigate to inventory actions?
> - **Option A: Right-click context menu** — hover item → right-click → menu appears (Escape/common)
> - **Option B: Drag-based** — drag to drop zone to drop; drag to equipment slot to equip (Stardew Valley)
> - **Option C: Inspect panel** — click item → details panel appears on right with action buttons

**User:**
> B — drag-based. I want it tactile.

*(Turns 10–12 continue section-by-section for the inventory screen spec: Player Need, Layout Zones, States, Interaction Map, Data Requirements, Events Fired, Accessibility, Localization.)*

---

## Part 3: /ux-review

### Turn 13: User Runs Review

**User:**
> /ux-review design/ux/

### Turn 14: Agent Reviews Both Documents

**Agent (via /ux-review):**
> Reviewing all UX specs in `design/ux/`...
>
> ---
> **HUD Review (`hud.md`):**
>
> | Check | Status | Notes |
> |-------|--------|-------|
> | GDD alignment — all required elements present | ✅ | HP, stamina, quick slots, cooldowns all specced |
> | State machine coverage | ✅ | All 4 gameplay states covered |
> | Accessibility tier | ⚠️ | No colorblind mode specified for HP/stamina bars (red/yellow convention) |
> | Visual budget | ✅ | 8% screen coverage, within budget |
> | Platform notes | ✅ | Controller variant documented |
>
> **Inventory Screen Review (`screens/inventory.md`):**
>
> | Check | Status | Notes |
> |-------|--------|-------|
> | Player Need stated | ✅ | |
> | All GDD actions covered | ✅ | Equip, drop, inspect, split all in interaction map |
> | Drag

# FILE: docs/examples/session-scope-crisis-decision.md

# Example Session: Scope Crisis - Strategic Decision Making

**Context:** Solo indie dev, week 8 of project (month 2), approaching Alpha milestone.

**Crisis:**
- Alpha milestone is in 2 weeks
- Crafting system (Pillar 2) not yet implemented
- Lead programmer says full crafting will take 3 weeks
- Investor demo at Alpha - must show all pillars

**Session Duration:** ~25 minutes
**Turns:** 8
**Outcome:** Strategic scope decision with documented ADR

---

## Turn 1: User Escalates Problem to Creative Director

**User:**
> We have a problem. Alpha is in 2 weeks. The crafting system (Pillar 2 "Emergent Discovery") isn't implemented yet. Lead programmer says it'll take 3 weeks to implement fully. But the investor demo is at Alpha and they need to see both pillars (Combat + Crafting). What should I do?

## Turn 2: Creative Director Gathers Full Context

**Agent (creative-director):**
> This is a classic pillar vs. schedule conflict - exactly what I'm here to help resolve. Let me gather the full context before recommending options.
>
> First, let me review the relevant documents:
> - `production/milestones/alpha.md` (milestone definition)
> - `design/pillars.md` (what's non-negotiable)
> - `design/gdd/crafting-system.md` (what was designed)
> - `production/sprints/sprint-current.md` (current work)
>
> [Reads documents]
>
> **Context Understood:**
> - Pillar 2: "Emergent Discovery Through Experimentation" (crafting is primary expression)
> - Alpha success criteria: "All pillars demonstrated in playable form"
> - Investor demo purpose: Validate vision and secure next funding round
> - Current crafting design: Tag-based deduction system with 12 tags, ~50 recipes, progressive hint unlocking
>
> **Clarifying Questions:**
> 1. Is the Alpha date **hard** (investor won't reschedule) or **soft** (we could ask for 1 more week)?
> 2. What's the **minimum crafting** that still demonstrates Pillar 2? (One recipe? Ten recipes? Full tag system?)
> 3. What **breaks** if crafting is cut entirely from Alpha? (Does the game still make sense?)
> 4. How **critical** is this investor relationship? (Nice-to-have funding vs. make-or-break for project survival?)
> 5. What's the **team status**? (Burned out from crunch? Fresh and could push if needed?)

## Turn 3: User Provides Decision Context

**User:**
> 1. Hard date - investor flying in specifically for demo, can't reschedule
> 2. I think minimum is: discovery mechanic working (tag system) + 10 recipes. Doesn't need polish.
> 3. Without crafting, Alpha only shows combat. That's 50% of the vision - investor might think it's just another combat game
> 4. Make-or-break. This investor is our only lead. No funding = project dies.
> 5. Just me solo, I'm not burned out yet.

## Turn 4: Creative Director Frames the Decision

**Agent:**
> Thank you. Now I understand what's truly at stake. Let me frame this decision properly:
>
> **The Core Question:**
> Do we deliver full crafting and slip Alpha, deliver simplified crafting and make Alpha, or cut crafting and risk the investor not seeing our full vision?
>
> **What's Really at Stake:**
> - **Vision Integrity**: Can investor see Pillar 2 at all?
> - **Schedule Trust**: Do we keep our commitment to Alpha date?
> - **Project Survival**: No funding = no game
> - **Quality Standards**: Is "rough but working" acceptable for this demo?
>
> **Decision Criteria (in priority order for this scenario):**
> 1. **Investor Confidence** (highest - project survival depends on this)
> 2. **Pillar Representation** (high - they need to see the full vision)
> 3. **Schedule Integrity** (medium - matters, but less than funding)
> 4. **Polish Quality** (lowest - vertical slice can be rough)
>
> Now let me present three strategic options...

## Turn 5: Creative Director Presents Options with Analysis

**Agent:**
> **Option A: Implement Full Crafting System (3 weeks, slip Alpha by 1 week)**
>
> **Execution:**
> - Implement complete tag-based system with all 50 recipes
> - Full UI polish, all features from GDD
> - Miss Alpha date, reschedule investor demo (+1 week)
>
> **Pros:**
> - ✅ Pillar 2 fully represented with production quality
> - ✅ No design compromises
> - ✅ First impression is polished
>
> **Cons:**
> - ❌ Breaks investor commitment (they're flying in for the original date)
> - ❌ Signals schedule management issues ("if they slipped Alpha, will they slip release?")
> - ❌ May damage investor trust more than rough demo would
>
> **Risk: CRITICAL**
> - Investor may not reschedule (busy schedule, other opportunities)
> - Even if they do, the slip damages credibility
> - Unlikely to succeed given hard date constraint
>
> **Verdict: NOT RECOMMENDED** - The date is hard and non-negotiable
>
> ---
>
> **Option B: Simplify Crafting to Core Pillar (1.5 weeks, make Alpha)**
>
> **Execution:**
> - Implement core tag discovery mechanic ONLY
> - 10 recipes instead of 50 (enough to demonstrate the system)
> - Basic UI (functional, not polished)
> - No progressive hint unlock (all tags visible at Skill 0 for demo clarity)
> - No failed-attempt feedback system (just success/fail)
>
> **Scope: "Vertical Slice of Pillar 2"**
> - Players CAN discover recipes by combining tagged ingredients
> - Players CAN learn tag patterns and deduce new recipes
> - The SOUL of Pillar 2 is present, just unpolished
>
> **Pros:**
> - ✅ Makes Alpha deadline (schedule integrity maintained)
> - ✅ Pillar 2 demonstrated (investor sees full vision)
> - ✅ Core mechanic is playable and provable
> - ✅ Can use "Alpha → Beta improvement" as narrative ("here's rough, here's polished")
>
> **Cons:**
> - ⚠️ First impression is "rough" (but vertical slices are expected to be rough)
> - ⚠️ Investor might think "this feels small" (mitigation: present roadmap showing post-Alpha expansion)
>
> **Risk: MEDIUM**
> - Investor might not "get" the pillar from 10 recipes (mitigation: good demo script explaining the vision)
> - Might feel incomplete (mitigation: frame as "vertical slice proving the concep
