# Missing Repo Summary Source: msitarzewski/agency-agents

- URL: https://github.com/msitarzewski/agency-agents
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/msitarzewski__agency-agents
- Clone Status: cloned
- Language: Shell
- Stars: 96502
- Topics: 
- Description: A complete AI agency at your fingertips - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

## Extracted README / Docs / Examples



# FILE: README.md

# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

> **A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. Each agent is a specialized expert with personality, processes, and proven deliverables.

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)](https://github.com/sponsors/msitarzewski)

---

## 🚀 What Is This?

Born from a Reddit thread and months of iteration, **The Agency** is a growing collection of meticulously crafted AI agent personalities. Each agent is:

- **🎯 Specialized**: Deep expertise in their domain (not generic prompt templates)
- **🧠 Personality-Driven**: Unique voice, communication style, and approach
- **📋 Deliverable-Focused**: Real code, processes, and measurable outcomes
- **✅ Production-Ready**: Battle-tested workflows and success metrics

**Think of it as**: Assembling your dream team, except they're AI specialists who never sleep, never complain, and always deliver.

---

## ⚡ Quick Start

### Option 1: Use with Claude Code (Recommended)

```bash
# Install all agents to your Claude Code directory
./scripts/install.sh --tool claude-code

# Or manually copy a category if you only want one division
cp engineering/*.md ~/.claude/agents/

# Then activate any agent in your Claude Code sessions:
# "Hey Claude, activate Frontend Developer mode and help me build a React component"
```

### Option 2: Use as Reference

Each agent file contains:
- Identity & personality traits
- Core mission & workflows
- Technical deliverables with code examples
- Success metrics & communication style

Browse the agents below and copy/adapt the ones you need!

### Option 3: Use with Other Tools (GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi Code)

```bash
# Step 1 -- generate integration files for all supported tools
./scripts/convert.sh

# Step 2 -- install interactively (auto-detects what you have installed)
./scripts/install.sh

# Or target a specific tool directly
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool opencode
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool cursor
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool kimi
```

See the [Multi-Tool Integrations](#-multi-tool-integrations) section below for full details.

---

## 🎨 The Agency Roster

### 💻 Engineering Division

Building the future, one commit at a time.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🎨 [Frontend Developer](engineering/engineering-frontend-developer.md) | React/Vue/Angular, UI implementation, performance | Modern web apps, pixel-perfect UIs, Core Web Vitals optimization |
| 🏗️ [Backend Architect](engineering/engineering-backend-architect.md) | API design, database architecture, scalability | Server-side systems, microservices, cloud infrastructure |
| 📱 [Mobile App Builder](engineering/engineering-mobile-app-builder.md) | iOS/Android, React Native, Flutter | Native and cross-platform mobile applications |
| 🤖 [AI Engineer](engineering/engineering-ai-engineer.md) | ML models, deployment, AI integration | Machine learning features, data pipelines, AI-powered apps |
| 🚀 [DevOps Automator](engineering/engineering-devops-automator.md) | CI/CD, infrastructure automation, cloud ops | Pipeline development, deployment automation, monitoring |
| ⚡ [Rapid Prototyper](engineering/engineering-rapid-prototyper.md) | Fast POC development, MVPs | Quick proof-of-concepts, hackathon projects, fast iteration |
| 💎 [Senior Developer](engineering/engineering-senior-developer.md) | Laravel/Livewire, advanced patterns | Complex implementations, architecture decisions |
| 🔧 [Filament Optimization Specialist](engineering/engineering-filament-optimization-specialist.md) | Filament PHP admin UX, structural form redesign, resource optimization | Restructuring Filament resources/forms/tables for faster, cleaner admin workflows |
| 🔒 [Security Engineer](engineering/engineering-security-engineer.md) | Threat modeling, secure code review, security architecture | Application security, vulnerability assessment, security CI/CD |
| ⚡ [Autonomous Optimization Architect](engineering/engineering-autonomous-optimization-architect.md) | LLM routing, cost optimization, shadow testing | Autonomous systems needing intelligent API selection and cost guardrails |
| 🔩 [Embedded Firmware Engineer](engineering/engineering-embedded-firmware-engineer.md) | Bare-metal, RTOS, ESP32/STM32/Nordic firmware | Production-grade embedded systems and IoT devices |
| 🚨 [Incident Response Commander](engineering/engineering-incident-response-commander.md) | Incident management, post-mortems, on-call | Managing production incidents and building incident readiness |
| ⛓️ [Solidity Smart Contract Engineer](engineering/engineering-solidity-smart-contract-engineer.md) | EVM contracts, gas optimization, DeFi | Secure, gas-optimized smart contracts and DeFi protocols |
| 🧭 [Codebase Onboarding Engineer](engineering/engineering-codebase-onboarding-engineer.md) | Fast developer onboarding, read-only codebase exploration, factual explanation | Helping new developers understand unfamiliar repos quickly by reading the code, tracing code paths, and stating facts about structure and behavior |
| 📚 [Technical Writer](engineering/engineering-technical-writer.md) | Developer docs, API reference, tutorials | Clear, accurate technical documentation |
| 🎯 [Threat Detection Engineer](engineering/engineering-threat-detection-engineer.md) | SIEM rules, threat hunting, ATT&CK mapping | Building detection layers and threat hunting |
| 💬 [WeChat Mini Program Developer](engineering/engineering-wechat-mini-program-developer.md) | WeChat ecosystem, Mini Programs, payment integration | Building performant apps for the WeChat ecosystem |
| 👁️ [Code Reviewer](engineering/engineering-code-reviewer.md) | Constructive code review, security, maintainability | PR reviews, code quality gates, mentoring through review |
| 🗄️ [Database Optimizer](engineering/engineering-database-optimizer.md) | Schema design, query optimization, indexing strategies | PostgreSQL/MySQL tuning, slow query debugging, migration planning |
| 🌿 [Git Workflow Master](engineering/engineering-git-workflow-master.md) | Branching strategies, conventional commits, advanced Git | Git workflow design, history cleanup, CI-friendly branch management |
| 🏛️ [Software Architect](engineering/engineering-software-architect.md) | System design, DDD, architectural patterns, trade-off analysis | Architecture decisions, domain modeling, system evolution strategy |
| 🛡️ [SRE](engineering/engineering-sre.md) | SLOs, error budgets, observability, chaos engineering | Production reliability, toil reduction, capacity planning |
| 🧬 [AI Data Remediation Engineer](engineering/engineering-ai-data-remediation-engineer.md) | Self-healing pipelines, air-gapped SLMs, semantic clustering | Fixing broken data at scale with zero data loss |
| 🔧 [Data Engineer](engineering/engineering-data-engineer.md) | Data pipelines, lakehouse architecture, ETL/ELT | Building reliable data infrastructure and warehousing |
| 🔗 [Feishu Integration Developer](engineering/engineering-feishu-integration-developer.md) | Feishu/Lark Open Platform, bots, workflows | Building integrations for the Feishu ecosystem |
| 🧱 [CMS Developer](engineering/engineering-cms-developer.md) | WordPress & Drupal themes, plugins/modules, content architecture | Code-first CMS implementation and customization |
| 📧 [Email Intelligence Engineer](engineering/engineering-email-intelligence-engineer.md) | Email parsing, MIME extraction, structured data for AI agents | Turning raw email threads into reasoning-ready context |
| 🎙️ [Voice AI Integration Engineer](engineering/engineering-voice-ai-integration-engineer.md) | Speech-to-text pipelines, Whisper, ASR, speaker diarization | End-to-end transcription pipelines, audio preprocessing, structured transcript delivery |

### 🎨 Design Division

Making it beautiful, usable, and delightful.

| Agent | Specialty | When to Use |
|-------|-----------|-------------|
| 🎯 [UI Designer](design/design-ui-designer.md) | Visual design, component libraries, design systems | Interface creation, brand consistency, component design |
| 🔍 [UX Researcher](design/design-ux-researcher.md) | User testing, behavior analysis, research | Understanding users, usability testing, design insights |
| 🏛️ [UX Architect](design/design-ux-architect.md) | Technical architecture, CSS systems, implementation | Developer-friendly foundations, implementation guidance |
| 🎭 [Brand Guardian](design/design-brand-guardian.md) | Brand identity, consistency, positioning | Brand strategy, identity development, guidelines |
| 📖 [Visual Storyteller](design/design-visual-storyteller.md) | Visual narratives, multimedia content | Compelling visual stories, brand storytelling |
| ✨ [Whimsy Injector](design/design-whimsy-injector.md) | Personality, delight, playful interactions | Adding joy, micro-interactions, Easter eggs, brand personality |
| 📷 [Image Prompt Engineer](design/design-image-prompt-engineer.md) | AI image generation prompts, photography | Photography prompts for Midjourney, DALL-E, Stable Diffusion |
| 🌈 [Inclusive Visuals Specialist](design/design-inclusive-visuals-specialist.md) | Representation, bias mitigation, authentic imagery | Generating culturally accurate AI images and video |

### 💰 Paid Media Division

# FILE: examples/workflow-book-chapter.md

# Workflow Example: Book Chapter Development

> A focused single-agent workflow for turning rough source material into a strategic first-person chapter draft with explicit revision loops.

## When to Use This

Use this workflow when an author has voice notes, fragments, or strategic notes, but not yet a clean chapter draft. The goal is not generic ghostwriting. The goal is to produce a chapter that strengthens category positioning, preserves the author's voice, and exposes open editorial decisions clearly.

## Agent Used

| Agent | Role |
|-------|------|
| Book Co-Author | Converts source material into a versioned chapter draft with editorial notes and next-step questions |

## Example Activation

```text
Activate Book Co-Author.

Book goal: Build authority around practical AI adoption for Mittelstand companies.
Target audience: Owners and operational leaders of 20-200 person businesses.
Chapter topic: Why most AI projects fail before implementation starts.
Desired draft maturity: First substantial draft.

Raw material:
- Voice memo: "The real failure happens in expectation setting, not tooling."
- Notes: Leaders buy software before defining the operational bottleneck.
- Story fragment: We nearly rolled out the wrong automation in a cabinetmaking workflow because the actual problem was quoting delays, not production throughput.
- Positioning angle: Practical realism over hype.

Produce:
1. Chapter objective and strategic role in the book
2. Any clarification questions you need
3. Chapter 2 - Version 1 - ready for review
4. Editorial notes on assumptions and proof gaps
5. Specific next-step revision requests
```

## Expected Output Shape

The Book Co-Author should respond in five parts:

1. `Target Outcome`
2. `Chapter Draft`
3. `Editorial Notes`
4. `Feedback Loop`
5. `Next Step`

## Quality Bar

- The draft stays in first-person voice
- The chapter has one clear promise and internal logic
- Claims are tied to source material or flagged as assumptions
- Generic motivational language is removed
- The output ends with explicit revision questions, not a vague handoff


# FILE: examples/README.md

# Examples

This directory contains example outputs demonstrating how the agency's agents can be orchestrated together to tackle real-world tasks.

## Why This Exists

The agency-agents repo defines dozens of specialized agents across engineering, design, marketing, product, support, spatial computing, and project management. But agent definitions alone don't show what happens when you **deploy them all at once** on a single mission.

These examples answer the question: *"What does it actually look like when the full agency collaborates?"*

## Contents

### [nexus-spatial-discovery.md](./nexus-spatial-discovery.md)

**What:** A complete product discovery exercise where 8 agents worked in parallel to evaluate a software opportunity and produce a unified plan.

**The scenario:** Web research identified an opportunity at the intersection of AI agent orchestration and spatial computing. The entire agency was then deployed simultaneously to produce:

- Market validation and competitive analysis
- Technical architecture (8-service system design with full SQL schema)
- Brand strategy and visual identity
- Go-to-market and growth plan
- Customer support operations blueprint
- UX research plan with personas and journey maps
- 35-week project execution plan with 65 sprint tickets
- Spatial interface architecture specification

**Agents used:**
| Agent | Role |
|-------|------|
| Product Trend Researcher | Market validation, competitive landscape |
| Backend Architect | System architecture, data model, API design |
| Brand Guardian | Positioning, visual identity, naming |
| Growth Hacker | GTM strategy, pricing, launch plan |
| Support Responder | Support tiers, onboarding, community |
| UX Researcher | Personas, journey maps, design principles |
| Project Shepherd | Phase plan, sprints, risk register |
| XR Interface Architect | Spatial UI specification |

**Key takeaway:** All 8 agents ran in parallel and produced coherent, cross-referencing plans without coordination overhead. The output demonstrates the agency's ability to go from "find an opportunity" to "here's the full blueprint" in a single session.

## Adding New Examples

If you run an interesting multi-agent exercise, consider adding it here. Good examples show:

- Multiple agents collaborating on a shared objective
- The breadth of the agency's capabilities
- Real-world applicability of the agent definitions


# FILE: examples/workflow-startup-mvp.md

# Multi-Agent Workflow: Startup MVP

> A step-by-step example of how to coordinate multiple agents to go from idea to shipped MVP.

## The Scenario

You're building a SaaS MVP — a team retrospective tool for remote teams. You have 4 weeks to ship a working product with user signups, a core feature, and a landing page.

## Agent Team

| Agent | Role in this workflow |
|-------|---------------------|
| Sprint Prioritizer | Break the project into weekly sprints |
| UX Researcher | Validate the idea with quick user interviews |
| Backend Architect | Design the API and data model |
| Frontend Developer | Build the React app |
| Rapid Prototyper | Get the first version running fast |
| Growth Hacker | Plan launch strategy while building |
| Reality Checker | Gate each milestone before moving on |

## The Workflow

### Week 1: Discovery + Architecture

**Step 1 — Activate Sprint Prioritizer**

```
Activate Sprint Prioritizer.

Project: RetroBoard — a real-time team retrospective tool for remote teams.
Timeline: 4 weeks to MVP launch.
Core features: user auth, create retro boards, add cards, vote, action items.
Constraints: solo developer, React + Node.js stack, deploy to Vercel + Railway.

Break this into 4 weekly sprints with clear deliverables and acceptance criteria.
```

**Step 2 — Activate UX Researcher (in parallel)**

```
Activate UX Researcher.

I'm building a team retrospective tool for remote teams (5-20 people).
Competitors: EasyRetro, Retrium, Parabol.

Run a quick competitive analysis and identify:
1. What features are table stakes
2. Where competitors fall short
3. One differentiator we could own

Output a 1-page research brief.
```

**Step 3 — Hand off to Backend Architect**

```
Activate Backend Architect.

Here's our sprint plan: [paste Sprint Prioritizer output]
Here's our research brief: [paste UX Researcher output]

Design the API and database schema for RetroBoard.
Stack: Node.js, Express, PostgreSQL, Socket.io for real-time.

Deliver:
1. Database schema (SQL)
2. REST API endpoints list
3. WebSocket events for real-time board updates
4. Auth strategy recommendation
```

### Week 2: Build Core Features

**Step 4 — Activate Frontend Developer + Rapid Prototyper**

```
Activate Frontend Developer.

Here's the API spec: [paste Backend Architect output]

Build the RetroBoard React app:
- Stack: React, TypeScript, Tailwind, Socket.io-client
- Pages: Login, Dashboard, Board view
- Components: RetroCard, VoteButton, ActionItem, BoardColumn

Start with the Board view — it's the core experience.
Focus on real-time: when one user adds a card, everyone sees it.
```

**Step 5 — Reality Check at midpoint**

```
Activate Reality Checker.

We're at week 2 of a 4-week MVP build for RetroBoard.

Here's what we have so far:
- Database schema: [paste]
- API endpoints: [paste]
- Frontend components: [paste]

Evaluate:
1. Can we realistically ship in 2 more weeks?
2. What should we cut to make the deadline?
3. Any technical debt that will bite us at laun

# FILE: examples/workflow-landing-page.md

# Multi-Agent Workflow: Landing Page Sprint

> Ship a conversion-optimized landing page in one day using 4 agents.

## The Scenario

You need a landing page for a new product launch. It needs to look great, convert visitors, and be live by end of day.

## Agent Team

| Agent | Role in this workflow |
|-------|---------------------|
| Content Creator | Write the copy |
| UI Designer | Design the layout and component specs |
| Frontend Developer | Build it |
| Growth Hacker | Optimize for conversion |

## The Workflow

### Morning: Copy + Design (parallel)

**Step 1a — Activate Content Creator**

```
Activate Content Creator.

Write landing page copy for "FlowSync" — an API integration platform
that connects any two SaaS tools in under 5 minutes.

Target audience: developers and technical PMs at mid-size companies.
Tone: confident, concise, slightly playful.

Sections needed:
1. Hero (headline + subheadline + CTA)
2. Problem statement (3 pain points)
3. How it works (3 steps)
4. Social proof (placeholder testimonial format)
5. Pricing (3 tiers: Free, Pro, Enterprise)
6. Final CTA

Keep it scannable. No fluff.
```

**Step 1b — Activate UI Designer (in parallel)**

```
Activate UI Designer.

Design specs for a SaaS landing page. Product: FlowSync (API integration platform).
Style: clean, modern, dark mode option. Think Linear or Vercel aesthetic.

Deliver:
1. Layout wireframe (section order + spacing)
2. Color palette (primary, secondary, accent, background)
3. Typography (font pairing, heading sizes, body size)
4. Component specs: hero section, feature cards, pricing table, CTA buttons
5. Responsive breakpoints (mobile, tablet, desktop)
```

### Midday: Build

**Step 2 — Activate Frontend Developer**

```
Activate Frontend Developer.

Build a landing page from these specs:

Copy: [paste Content Creator output]
Design: [paste UI Designer output]

Stack: HTML, Tailwind CSS, minimal vanilla JS (no framework needed).
Requirements:
- Responsive (mobile-first)
- Fast (no heavy assets, system fonts OK)
- Accessible (proper headings, alt text, focus states)
- Include a working email signup form (action URL: /api/subscribe)

Deliver a single index.html file ready to deploy.
```

### Afternoon: Optimize

**Step 3 — Activate Growth Hacker**

```
Activate Growth Hacker.

Review this landing page for conversion optimization:

[paste the HTML or describe the current page]

Evaluate:
1. Is the CTA above the fold?
2. Is the value proposition clear in under 5 seconds?
3. Any friction in the signup flow?
4. What A/B tests would you run first?
5. SEO basics: meta tags, OG tags, structured data

Give me specific changes, not general advice.
```

## Timeline

| Time | Activity | Agent |
|------|----------|-------|
| 9:00 | Copy + design kick off (parallel) | Content Creator + UI Designer |
| 11:00 | Build starts | Frontend Developer |
| 14:00 | First version ready | — |
| 14:30 | Conversion review | Growth Hacker |
| 15:30 | Apply feedback | Frontend Developer |
| 16:30

# FILE: examples/workflow-with-memory.md

# Multi-Agent Workflow: Startup MVP with Persistent Memory

> The same startup MVP workflow from [workflow-startup-mvp.md](workflow-startup-mvp.md), but with an MCP memory server handling state between agents. No more copy-paste handoffs.

## The Problem with Manual Handoffs

In the standard workflow, every agent-to-agent transition looks like this:

```
Activate Backend Architect.

Here's our sprint plan: [paste Sprint Prioritizer output]
Here's our research brief: [paste UX Researcher output]

Design the API and database schema for RetroBoard.
...
```

You are the glue. You copy-paste outputs between agents, keep track of what's been done, and hope you don't lose context along the way. It works for small projects, but it falls apart when:

- Sessions time out and you lose the output
- Multiple agents need the same context
- QA fails and you need to rewind to a previous state
- The project spans days or weeks across many sessions

## The Fix

With an MCP memory server installed, agents store their deliverables in memory and retrieve what they need automatically. Handoffs become:

```
Activate Backend Architect.

Project: RetroBoard. Recall previous context for this project
and design the API and database schema.
```

The agent searches memory for RetroBoard context, finds the sprint plan and research brief stored by previous agents, and picks up from there.

## Setup

Install any MCP-compatible memory server that supports `remember`, `recall`, and `rollback` operations. See [integrations/mcp-memory/README.md](../integrations/mcp-memory/README.md) for setup.

## The Scenario

Same as the standard workflow: a SaaS team retrospective tool (RetroBoard), 4 weeks to MVP, solo developer.

## Agent Team

| Agent | Role in this workflow |
|-------|---------------------|
| Sprint Prioritizer | Break the project into weekly sprints |
| UX Researcher | Validate the idea with quick user interviews |
| Backend Architect | Design the API and data model |
| Frontend Developer | Build the React app |
| Rapid Prototyper | Get the first version running fast |
| Growth Hacker | Plan launch strategy while building |
| Reality Checker | Gate each milestone before moving on |

Each agent has a Memory Integration section in their prompt (see [integrations/mcp-memory/README.md](../integrations/mcp-memory/README.md) for how to add it).

## The Workflow

### Week 1: Discovery + Architecture

**Step 1 — Activate Sprint Prioritizer**

```
Activate Sprint Prioritizer.

Project: RetroBoard — a real-time team retrospective tool for remote teams.
Timeline: 4 weeks to MVP launch.
Core features: user auth, create retro boards, add cards, vote, action items.
Constraints: solo developer, React + Node.js stack, deploy to Vercel + Railway.

Break this into 4 weekly sprints with clear deliverables and acceptance criteria.
Remember your sprint plan tagged for this project when done.
```

The Sprint Prioritizer produces the sprint plan and stores it in memory tagged with `sprint-priorit

# FILE: examples/nexus-spatial-discovery.md

# Nexus Spatial: Full Agency Discovery Exercise

> **Exercise type:** Multi-agent product discovery
> **Date:** March 5, 2026
> **Agents deployed:** 8 (in parallel)
> **Duration:** ~10 minutes wall-clock time
> **Purpose:** Demonstrate full-agency orchestration from opportunity identification through comprehensive planning

---

## Table of Contents

1. [The Opportunity](#1-the-opportunity)
2. [Market Validation](#2-market-validation)
3. [Technical Architecture](#3-technical-architecture)
4. [Brand Strategy](#4-brand-strategy)
5. [Go-to-Market & Growth](#5-go-to-market--growth)
6. [Customer Support Blueprint](#6-customer-support-blueprint)
7. [UX Research & Design Direction](#7-ux-research--design-direction)
8. [Project Execution Plan](#8-project-execution-plan)
9. [Spatial Interface Architecture](#9-spatial-interface-architecture)
10. [Cross-Agent Synthesis](#10-cross-agent-synthesis)

---

## 1. The Opportunity

### How It Was Found

Web research across multiple sources identified three converging trends:

- **AI infrastructure/orchestration** is the fastest-growing software category (AI orchestration market valued at ~$13.5B in 2026, 22%+ CAGR)
- **Spatial computing** (Vision Pro, WebXR) is maturing but lacks killer enterprise apps
- Every existing AI workflow tool (LangSmith, n8n, Flowise, CrewAI) is a **flat 2D dashboard**

### The Concept: Nexus Spatial

An AI Agent Command Center in spatial computing -- a VisionOS + WebXR application that provides an immersive 3D command center for orchestrating, monitoring, and interacting with AI agents. Users visualize agent pipelines as 3D node graphs, monitor real-time outputs in spatial panels, build workflows with drag-and-drop in 3D space, and collaborate in shared spatial environments.

### Why This Agency Is Uniquely Positioned

The agency has deep spatial computing expertise (XR developers, VisionOS engineers, Metal specialists, interface architects) alongside a full engineering, design, marketing, and operations stack -- a rare combination for a product that demands both spatial computing mastery and enterprise software rigor.

### Sources

- [Profitable SaaS Ideas 2026 (273K+ Reviews)](https://bigideasdb.com/profitable-saas-micro-saas-ideas-2026)
- [2026 SaaS and AI Revolution: 20 Top Trends](https://fungies.io/the-2026-saas-and-ai-revolution-20-top-trends/)
- [Top 21 Underserved Markets 2026](https://mktclarity.com/blogs/news/list-underserved-niches)
- [Fastest Growing Products 2026 - G2](https://www.g2.com/best-software-companies/fastest-growing)
- [PwC 2026 AI Business Predictions](https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-predictions.html)

---

## 2. Market Validation

**Agent:** Product Trend Researcher

### Verdict: CONDITIONAL GO -- 2D-First, Spatial-Second

### Market Size

| Segment | 2026 Value | Growth |
|---------|-----------|--------|
| AI Orchestration Tools | $13.5B | 22.3% CAGR |
| Autonomous AI Agents | $8.5B | 45.8% CAGR to $50.3B by 2030 |
| Extended Reality | $
