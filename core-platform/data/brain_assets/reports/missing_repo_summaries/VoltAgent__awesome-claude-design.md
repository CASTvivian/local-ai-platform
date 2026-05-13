# Missing Repo Summary Source: VoltAgent/awesome-claude-design

- URL: https://github.com/VoltAgent/awesome-claude-design
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/VoltAgent__awesome-claude-design
- Clone Status: cloned
- Language: None
- Stars: 2136
- Topics: claude-code, claude-design, design-md, design-system, figma
- Description: Awesome Claude Design: 68 ready-to-use design system inspirations in DESIGN.md format. Drop one in, scaffold a full UI in one shot.

## Extracted README / Docs / Examples



# FILE: README.md



<a href="https://github.com/VoltAgent/voltagent">
<img width="1500"  alt="claude-design" src="https://github.com/user-attachments/assets/c679bd35-ba7e-4d6f-834d-3f4b6e5a35e4" />
</a>

<br/>
<br/>


<div align="center">
    <strong>A collection of ready-to-use <code>DESIGN.md</code> files that Claude Design expands into a full UI scaffold with one drop.</strong>
    <br />
    <br />

</div>

<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![DESIGN.md Count](https://img.shields.io/badge/DESIGN.md%20count-68-10b981?style=classic)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-claude-design?label=Last%20update&style=classic)](https://github.com/VoltAgent/awesome-claude-design)
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

</div>
</div>


# Awesome Claude Design

Upload any `DESIGN.md` to Claude Design and it scaffolds a full design system (colors, type, components, preview cards, and a working UI kit) in a single shot. 

Skip the blank-page design brief, grab a design system inspiration that matches the feel you want, and let Claude Design do the scaffolding.


## What is Claude Design?

[Claude Design](https://claude.ai/design) is Anthropic's new design-focused workspace. Instead of generating one-off screens in a chat window, it holds a persistent **design system** for your project: tokens, components, and preview assets you can actually ship, not just swatches in a chat window.

You give it a starting point (an aesthetic, a vibe, or a `DESIGN.md`), and it scaffolds the system: color tokens, type scale, buttons, cards, nav, and a working UI kit. The output lands in the project's Design System review tab, organized and inspectable, so every new screen you request stays on-system.

## What is DESIGN.md?

[`DESIGN.md`](https://getdesign.md/what-is-design-md) is a single plain-text markdown file that describes a brand's visual language in a format AI agents can actually act on. The concept was first introduced by Google Stitch and built into a real, comparable collection by at 🎨[**getdesign.md**](https://getdesign.md/). 

> The core idea: keep **token, rule, and rationale in the same file**. A Figma export tells you *what* to use but skips *why*. A brand guideline PDF talks to humans ("approachable yet premium") but is too loose for an agent. `DESIGN.md` sits in the middle. Specific enough for the agent to make its next decision, and carrying the *why* so it can stay on-system when it hits a case the file never covered.

| File | Who reads it | What it defines |
|------|-------------|-----------------|
| `AGENTS.md` | Coding agents | How to build the project |
| `DESIGN.md` | Design agents (Claude Design, Stitch …) | How the project should look and feel |

Claude Design can use `DESIGN.md` as its source of truth. Hand it one, and the full starter package falls out the other side.

## How it works



1. Pick a design system inspiration from the list below, click through to its preview page to inspect the system in detail, then download its `DESIGN.md`.
2. Open [Claude Design](https://claude.ai/design). You've got **two ways** to feed it the file:

### Option A. Start from a design system

   Go to [claude.ai/design/#org](https://claude.ai/design/#org), click **Create new design system**, and on the *Set up your design system* screen, upload the `DESIGN.md` under **Add assets**.

![setup-a](https://github.com/user-attachments/assets/93846ec2-c159-4459-b434-8acb7ac5fcfe)


<br/>

### Option B. Start from a prototype
   Go to dashboard, create a new prototype, attach the `DESIGN.md` in the chat, and type: **"Create a design system from this DESIGN.md"**


<img width="848" height="480" alt="option-b" src="https://github.com/user-attachments/assets/c7e3c22c-fd3d-41a2-a6d0-1a50b40e22c9" />




Either way, Claude produces a full starter package in minutes:

- `README.md` with brand context, voice, and visual foundations
- `colors_and_type.css` with CSS variables, type scale, utility classes
- Google Fonts substitutes when the brand font is proprietary
- `preview/` cards for colors, type, spacing, components, and brand
- A working UI kit (`index.html` + components) applying the system to a real marketing page
- `SKILL.md`, a portable skill file for future projects

One markdown file → production-ready design package. No boilerplate, no manual setup.


## Collection

### AI & LLM Platforms

- [**Claude**](https://getdesign.md/claude/design-md) - Anthropic's AI assistant. Warm terracotta accent, clean editorial layout
- [**Cohere**](https://getdesign.md/cohere/design-md) - Enterprise AI platform. Vibrant gradients, data-rich dashboard aesthetic
- [**ElevenLabs**](https://getdesign.md/elevenlabs/design-md) - AI voice platform. Dark cinematic UI, audio-waveform aesthetics
- [**Minimax**](https://getdesign.md/minimax/design-md) - AI model provider. Bold dark interface with neon accents
- [**Mistral AI**](https://getdesign.md/mistral.ai/design-md) - Open-weight LLM provider. French-engineered minimalism, purple-toned
- [**Ollama**](https://getdesign.md/ollama/design-md) - Run LLMs locally. Terminal-first, monochrome simplicity
- [**OpenCode AI**](https://getdesign.md/opencode.ai/design-md) - AI coding platform. Developer-centric dark theme
- [**Replicate**](https://getdesign.md/replicate/design-md) - Run ML models via API. Clean white canvas, code-forward
- [**RunwayML**](https://getdesign.md/runwayml/design-md) - AI video generation. Cinematic dark UI, media-rich layout
- [**Together AI**](https://getdesign.md/together.ai/design-md) - Open-source AI infrastructure. Technical, blueprint-style design
- [**VoltAgent**](https://getdesign.md/voltagent/design-md) - AI agent framework. Void-black canvas, emerald accent, terminal-native
- [**xAI**](https://getdesign.md/x.ai/design-md) - Elon Musk's AI lab. Stark monochrome, futuristic minimalism

### Developer Tools & IDEs

- [**Cursor**](https://getdesign.md/cursor/design-md) - AI-first code editor. Sleek dark interface, gradient accents
- [**Expo**](https://getdesign.md/expo/design-md) - React Native platform. Dark theme, tight letter-spacing, code-centric
- [**Lovable**](https://getdesign.md/lovable/design-md) - AI full-stack builder. Playful gradients, friendly dev aesthetic
- [**Raycast**](https://getdesign.md/raycast/design-md) - Productivity launcher. Sleek dark chrome, vibrant gradient accents
- [**Superhuman**](https://getdesign.md/superhuman/design-md) - Fast email client. Premium dark UI, keyboard-first, purple glow
- [**Vercel**](https://getdesign.md/vercel/design-md) - Frontend deployment platform. Black and white precision, Geist font
- [**Warp**](https://getdesign.md/warp/design-md) - Modern terminal. Dark IDE-like interface, block-based command UI

### Backend, Database & DevOps

- [**ClickHouse**](https://getdesign.md/clickhouse/design-md) - Fast analytics database. Yellow-accented, technical documentation style
- [**Composio**](https://getdesign.md/composio/design-md) - Tool integration platform. Modern dark with colorful integration icons
- [**HashiCorp**](https://getdesign.md/hashicorp/design-md) - Infrastructure automation. Enterprise-clean, black and white
- [**MongoDB**](https://getdesign.md/mongodb/design-md) - Document database. Green leaf branding, developer documentation focus
- [**PostHog**](https://getdesign.md/posthog/design-md) - Product analytics. Playful hedgehog branding, developer-friendly dark UI
- [**Sanity**](https://getdesign.md/sanity/design-md) - Headless CMS. Red accent, content-first editorial layout
- [**Sentry**](https://getdesign.md/sentry/design-md) - Error monitoring. Dark dashboard, data-dense, pink-purple accent
- [**Supabase**](https://getdesign.md/supabase/design-md) - Open-source Firebase alternative. Dark emerald theme, code-first

### Productivity & SaaS

- [**Cal.com**](https://getdesign.md/cal/design-md) - Open-source scheduling. Clean neutral UI, developer-oriented simplicity
- [**Intercom**](https://getdesign.md/intercom/design-md) - Customer messaging. Friendly blue palette, conversational UI patterns
- [**Linear**](https://getdesign.md/linear.app/design-md) - Project management for engineers. Ultra-minimal, precise, purple accent
- [**Mintlify**](https://getdesign.md/mintlify/design-md) - Documentation platform. Clean, green-accented, reading-optimized
- [**Notion**](https://getdesign.md/notion/design-md) - All-in-one workspace. Warm minimalism, serif headings, soft surfaces
- [**Resend**](https://getdesign.md/resend/design-md) - Email API for developers. Minimal dark theme, monospace accents
- [**Zapier**](https://getdesign.md/zapier/design-md) - Automation platform. Warm orange, friendly illustration-driven

### Design & Creative Tools

- [**Airtable**](https://getdesign.md/airtable/design-md) - Spreadsheet-database hybrid. Colorful, friendly, structured data aesthetic
- [**Clay**](https://getdesign.md/clay/design-md) - Creative agency. Organic shapes, soft gradients, art-directed layout
- [**Figma**](https://getdesign.md/figma/design-md) - Collaborative design tool. Vibrant multi-color, playful yet professional
- [**Framer**](https://getdesign.md/framer/design-md) - Website builder. Bold black and blue, motion-first, design-forward
- [**Miro**](https://getdesign.md/miro/design-md) - Visual collaboration. Bright yellow accent, infinite canvas aesthetic
- [**Webflow**](https://getdesign.md/webflow/design-md) - Visual web builder. Blue-accented, polished marketing site aesthetic

### Fintech & Crypto

- [**Binance**](https://getdesign.md/binance/design-md) - Crypto exchange. Bold Binance Yellow on monochrome, trading-floor urgency
- [**Coinbase**](https://getdesign.md/coinbase/design-md) - Crypto exchange. Clean blue identity, trust-focused, institutional feel
- [**Kraken**](https://getdesign.md/kraken/design-md) - Crypto trading platfo
