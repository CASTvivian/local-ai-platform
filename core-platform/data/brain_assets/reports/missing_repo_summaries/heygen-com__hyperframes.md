# Missing Repo Summary Source: heygen-com/hyperframes

- URL: https://github.com/heygen-com/hyperframes
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/heygen-com__hyperframes
- Clone Status: cloned
- Language: TypeScript
- Stars: 17624
- Topics: ai, animation, ffmpeg, framework, gsap, html, mcp, puppeteer, rendering, typescript, video
- Description: Write HTML. Render video. Built for agents.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/logo/dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/logo/light.svg">
    <img alt="HyperFrames" src="docs/logo/light.svg" width="300">
  </picture>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/hyperframes"><img src="https://img.shields.io/npm/v/hyperframes.svg?style=flat" alt="npm version"></a>
  <a href="https://www.npmjs.com/package/hyperframes"><img src="https://img.shields.io/npm/dm/hyperframes.svg?style=flat" alt="npm downloads"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue.svg" alt="License"></a>
  <a href="https://nodejs.org"><img src="https://img.shields.io/badge/node-%3E%3D22-brightgreen" alt="Node.js"></a>
  <a href="https://discord.gg/EbK98HBPdk"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center"><b>Write HTML. Render video. Built for agents.</b></p>

<p align="center">
  <img src="https://static.heygen.ai/hyperframes-oss/docs/images/hfgif-1280.webp" alt="HyperFrames demo — HTML code on the left transforms into a rendered video on the right" width="800">
</p>

Hyperframes is an open-source video rendering framework that lets you create, preview, and render HTML-based video compositions — with first-class support for AI agents.

## Quick Start

### Option 1: With an AI coding agent (recommended)

Install the HyperFrames skills, then describe the video you want:

```bash
npx skills add heygen-com/hyperframes
```

This teaches your agent (Claude Code, Cursor, Gemini CLI, Codex) how to write correct compositions, GSAP timelines, Tailwind v4 browser-runtime styles, and first-party adapter animations. In Claude Code, the skills register as slash commands — invoke `/hyperframes` to author compositions, `/hyperframes-cli` for the dev-loop commands (init, lint, preview, render), `/hyperframes-media` for asset preprocessing (TTS, transcription, background removal), `/tailwind` for `init --tailwind` projects, `/gsap` for timeline animation help, or the adapter skills (`/animejs`, `/css-animations`, `/lottie`, `/three`, `/waapi`) when a composition uses those runtimes.

For Claude Design, open [`docs/guides/claude-design-hyperframes.md`](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/claude-design-hyperframes.md) on GitHub and click the download button (↓) to save it, then attach the file to your Claude Design chat. It produces a valid first draft; refine in any AI coding agent. See the [Claude Design guide](https://hyperframes.heygen.com/guides/claude-design).

For Codex specifically, the same skills are also exposed as an [OpenAI Codex plugin](./.codex-plugin/plugin.json) — sparse-install just the plugin surface:

```bash
codex plugin marketplace add heygen-com/hyperframes --sparse .codex-plugin --sparse skills --sparse assets
```

For Claude Code, the repo also ships a [Claude Code plugin manifest](./.claude-plugin/plugin.json): test it locally with `claude --plugin-dir .`. The manifest intentionally omits `skills` because Claude Code auto-discovers the root `skills/` directory by convention, and for marketplace submission use the title `HyperFrames by HeyGen` plus the black/white icon assets at [`assets/claude-code-icon-dark.svg`](./assets/claude-code-icon-dark.svg) and [`assets/claude-code-icon-light.svg`](./assets/claude-code-icon-light.svg) for the two theme slots.
For Cursor, the same skills are packaged as a [Cursor plugin](./.cursor-plugin/plugin.json) — install from the Cursor Marketplace, or sideload by cloning this repo and pointing **Settings → Plugins → Load unpacked** at the repo root.

#### Try it: example prompts

Copy any of these into your agent to get started. The `/hyperframes` prefix loads the skill context explicitly so you get correct output the first time.

**Cold start — describe what you want:**

> Using `/hyperframes`, create a 10-second product intro with a fade-in title, a background video, and background music.

**Warm start — turn existing context into a video:**

> Take a look at this GitHub repo https://github.com/heygen-com/hyperframes and explain its uses and architecture to me using `/hyperframes`.

> Summarize the attached PDF into a 45-second pitch video using `/hyperframes`.

> Turn this CSV into an animated bar chart race using `/hyperframes`.

**Format-specific:**

> Make a 9:16 TikTok-style hook video about [topic] using `/hyperframes`, with bouncy captions synced to a TTS narration.

**Iterate — talk to the agent like a video editor:**

> Make the title 2x bigger, swap to dark mode, and add a fade-out at the end.

> Add a lower third at 0:03 with my name and title.

The agent handles scaffolding, animation, and rendering. See the [prompting guide](https://hyperframes.heygen.com/guides/prompting) for more patterns.

### Option 2: Start a project manually

```bash
npx hyperframes init my-video
cd my-video
npx hyperframes preview      # preview in browser (live reload)
npx hyperframes render       # render to MP4
```

`hyperframes init` installs skills automatically, so you can hand off to your AI agent at any point.

**Requirements:** Node.js >= 22, FFmpeg

## Why Hyperframes?

- **HTML-native** — compositions are HTML files with data attributes. No React, no proprietary DSL.
- **AI-first** — agents already speak HTML. The CLI is non-interactive by default, designed for agent-driven workflows.
- **Deterministic rendering** — same input = identical output. Built for automated pipelines.
- **Frame Adapter pattern** — bring your own animation runtime (GSAP, Lottie, CSS, Three.js).

## Hyperframes vs Remotion

Hyperframes is inspired by [Remotion](https://www.remotion.dev) — we used Remotion at HeyGen in production, learned a ton from it, and kept attribution comments in the source for the patterns it pioneered (Chrome launch flags, image2pipe → FFmpeg streaming, frame buffering). Both tools drive headless Chrome and both are deterministic. They differ on one decision: **what the primary author writes.** Remotion's bet is React components; Hyperframes' bet is HTML.

|                                                       | **Hyperframes**                | **Remotion**                      |
| ----------------------------------------------------- | ------------------------------ | --------------------------------- |
| Authoring                                             | HTML + CSS + GSAP              | React components (TSX)            |
| Build step                                            | None; `index.html` plays as-is | Required (bundler)                |
| Library-clock animations (GSAP, Anime.js, Motion One) | Seekable, frame-accurate       | Plays at wall-clock during render |
| Arbitrary HTML / CSS passthrough                      | Paste and animate              | Rewrite as JSX                    |
| Distributed rendering                                 | Single-machine today           | Lambda, production-ready          |

### Licensing: fully open source vs source-available

**Hyperframes is completely open source under [Apache 2.0](LICENSE)** — an OSI-approved license. Use it commercially at any scale, with no per-render fees, no seat caps, no company-size thresholds.

**Remotion is [source-available, not open source](https://www.remotion.pro/license).** The code is on GitHub under a custom Remotion License that requires a paid company license above small-team thresholds. It's a great product with a real team behind it — but if open-source licensing matters to you (OSI compliance, redistribution rights, no per-use fees), that's a first-order decision point.

Full write-up with benchmarks, an honest list of where each tool wins, and a GSAP side-by-side: **[Hyperframes vs Remotion guide](https://hyperframes.heygen.com/guides/hyperframes-vs-remotion)**.

## How It Works

Define your video as HTML with data attributes:

```html
<div id="stage" data-composition-id="my-video" data-start="0" data-width="1920" data-height="1080">
  <video
    id="clip-1"
    data-start="0"
    data-duration="5"
    data-track-index="0"
    src="intro.mp4"
    muted
    playsinline
  ></video>
  <img
    id="overlay"
    class="clip"
    data-start="2"
    data-duration="3"
    data-track-index="1"
    src="logo.png"
  />
  <audio
    id="bg-music"
    data-start="0"
    data-duration="9"
    data-track-index="2"
    data-volume="0.5"
    src="music.wav"
  ></audio>
</div>
```

Preview instantly in the browser. Render to MP4 locally or in Docker.

## Catalog

50+ ready-to-use blocks and components — social overlays, shader transitions, data visualizations, and cinematic effects:

```bash
npx hyperframes add flash-through-white   # shader transition
npx hyperframes add instagram-follow      # social overlay
npx hyperframes add data-chart            # animated chart
```

Browse the full catalog at **[hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart)**.

## Documentation

Full documentation at **[hyperframes.heygen.com/introduction](https://hyperframes.heygen.com/introduction)** — [Quickstart](https://hyperframes.heygen.com/quickstart) | [Guides](https://hyperframes.heygen.com/guides/gsap-animation) | [API Reference](https://hyperframes.heygen.com/packages/core) | [Catalog](https://hyperframes.heygen.com/catalog/blocks/data-chart)

## Packages

| Package                                                          | Description                                                 |
| ---------------------------------------------------------------- | ----------------------------------------------------------- |
| [`hyperframes`](packages/cli)                                    | CLI — create, preview, lint, and render compositions        |
| [`@hyperframes/core`](packages/core)                             | Types, parsers, generators, linter, runtime, frame adapters |
| [`@hy

# FILE: docs/guides/claude-design-hyperframes.md

# Claude Design + HyperFrames (Template-First)

Your medium is **HyperFrames compositions**: plain HTML + CSS + a paused GSAP timeline. The CLI (`npx hyperframes render index.html`) turns the HTML into an MP4. You author the HTML -- the user renders locally.

**HyperFrames replaces your default video-artifact workflow.** Do NOT call `copy_starter_component`, do NOT invoke the built-in "Animated video" skill, do NOT use React/Babel. Plain HTML + GSAP only.

---

## Your role

**You produce a valid first draft -- not a final render.** Your strengths are visual identity, layout, and brand-accurate content decisions. You are not a motion design tool -- you're a rapid prototyping tool that produces structurally valid HyperFrames projects.

The user's workflow:

1. **Claude Design** (you) -- brand identity, scene content, layout, first-pass animations, shader choices
2. **Download ZIP** -- user gets a valid HyperFrames project
3. **Claude Code** (or any AI coding agent) -- animation polish, timing refinement, pacing, production QA with linting and live preview

Your output must be a **valid starting point that Claude Code can open and immediately work with** -- no structural fixes needed, just creative refinement.

### What you optimize for (your strengths)

- Correct brand identity from attachments (palette, typography, tone)
- Strong visual layout per scene (hierarchy, spacing, readability)
- Scene content that tells the story (headlines, stats, copy, imagery)
- Structural validity (passes `npx hyperframes lint` with zero errors)
- Appropriate shader transition choices for the mood
- Reasonable scene count and durations for the video type

### What Claude Code polishes after you (refinement, not creation)

You create ALL the animations, transitions, and mid-scene activity. Every scene ships with entrance tweens, breathing motion, and shader transitions. The video plays with full motion from your first draft.

What Claude Code does is **watch the full playthrough with reliable preview tools and fine-tune**:

- Ease curve tweaks (swapping `power3.out` for `expo.out` after seeing it play)
- Stagger timing adjustments (0.12 → 0.08 feels tighter for this specific scene)
- Scene duration micro-adjustments (scene 4 drags at 4.5s, trim to 3.8s)
- Adding richer mid-scene activity where a scene feels too static after playback
- Shader swaps (this `cinematic-zoom` should be `whip-pan` for the energy shift)
- Production QA (snapshot verification, cross-browser testing)

Think of it as: **you create the first cut of the film, Claude Code does the edit bay refinement.**

---

## How this works

You get a **pre-valid skeleton** that already passes the HyperFrames linter. Your job:

1. Read the brief, pick a skeleton
2. Fill in the palette + typography (CSS custom properties)
3. Fill in scene content (text, layout inside `.scene-content`)
4. Fill in GSAP animations (timeline blocks marked per scene)
5. Verify the preview, deliver the ZIP

The skeleton handles the structural rules -- data attributes, timeline registration, HyperShader wiring, initial visibility, `preview.html` token forwarding. You focus on the creative work.

**What you can change:** CSS custom properties, scene content, animation tweens, scene count (add/remove scenes following the rules below), shader choices, durations.

**What you must not touch:** The `<script>` loading order, `window.__timelines` initialization, the `.scene.clip` class on scene containers, the `.scene-content` wrapper inside each scene, the `preview.html` structure.

---

## Step 1: Understand the brief

**Gate:** You can name the subject, duration, aspect ratio, and at least one source of visual direction.

### Inputs, in order of reliability

1. **Attachments** (strongest) -- screenshots, PDFs, brand guides, reference images. Mine for palette, type, tone.
2. **Pasted content** -- hex codes, typefaces, copy, scripts.
3. **Research** -- `web_search` the brand. Static pages (blogs, press, Wikipedia) work. SPA homepages return empty shells -- pivot to blog/press/Wikipedia.
4. **URLs the user provided** -- start there, expand outward.

### Ask ONE question if the brief is sparse

If the prompt has NONE of: an attachment, a hex code or named typeface, a named aesthetic/style/director, a well-known brand, or "just build" / "surprise me" -- ask one short clarifying question with concrete options. Wait for the reply.

---

## Step 2: Pick a skeleton and fill identity

**Gate:** A working `index.html` exists with your palette and typography on `:root`. The preview renders (even if scenes are empty).

### Choose by video type

| Type                     | Duration | Scenes | Skeleton   |
| ------------------------ | -------- | ------ | ---------- |
| Social reel (9:16)       | 10-15s   | 5-7    | Skeleton A |
| Launch teaser (16:9)     | 15-25s   | 7-10   | Skeleton B |
| Product explainer (16:9) | 30-60s   | 10-18  | Skeleton C |
| Cinematic title (16:9)   | 45-90s   | 7-12   | Skeleton D |

Copy the skeleton (Section 7 below), then **immediately fill the `:root` CSS custom properties**:

```css
:root {
  /* === FILL: Your brand identity === */
  --bg: #0a0a0d;
  --ink: #f5f5f7;
  --accent: #7c6cff;
  --muted: #5a6270;
  --accent-dim: #3d3680;
  --font-display: "Space Grotesk", sans-serif;
  --font-data: "JetBrains Mono", monospace;
}
```

### Anti-monoculture

These are the defaults every LLM reaches for. Pick something the brief actually calls for:

- **Banned fonts:** Inter, Inter Tight, Roboto, Open Sans, Noto Sans, Lato, Poppins, Outfit, Sora, Fraunces, Playfair Display, Cormorant Garamond, EB Garamond, Syne, Cinzel, Prata, Bodoni Moda, Nunito, Source Sans, PT Sans, Arimo.
- **Banned pairings:** Fraunces + JetBrains Mono, Inter + anything, Playfair + Lato.
- **Question these defaults:** gradient text, cyan-on-dark, pure `#000`/`#fff`, identical card grids, left-edge accent stripes, everything centered with equal weight.

Pick a real typeface pair. Weight contrast must be

# FILE: docs/guides/open-design-hyperframes.md

---
name: hyperframes-handoff
description: |
  Produce a HyperFrames-valid HTML composition — paused GSAP timeline, data
  attributes, scene structure — that any AI coding agent can immediately
  refine with `npx hyperframes lint` and `npx hyperframes preview`. Use when
  the brief mentions "video", "reel", "motion graphic", "title card",
  "animated explainer", or pairs Open Design with HyperFrames for export.
triggers:
  - "hyperframes"
  - "video"
  - "reel"
  - "motion graphic"
  - "animated explainer"
  - "title card"
  - "kinetic typography"
  - "动效视频"
  - "视频海报"
od:
  mode: prototype
  platform: desktop
  scenario: marketing
  preview:
    type: html
    entry: index.html
  design_system:
    requires: true
    sections: [color, typography, layout, motion]
  example_prompt: "Design a 15-second Instagram reel announcing dark mode for Taskflow (#6C5CE7). Output as a HyperFrames composition I can render locally."
---

# HyperFrames Handoff — for Open Design

> **Drop this file at `skills/hyperframes-handoff/SKILL.md` inside your local
> [Open Design](https://github.com/nexu-io/open-design) checkout, restart the
> daemon, and the skill appears in the picker. Or attach it to a fresh chat
> as a one-shot.**

This skill teaches Open Design to emit a **valid first draft** of a
[HyperFrames](https://github.com/heygen-com/hyperframes) composition — plain
HTML + CSS + a paused GSAP timeline. The CLI (`npx hyperframes render
index.html`) turns the HTML into an MP4. You author the HTML; the user runs
the render locally.

**HyperFrames replaces the default video-artifact workflow.** Do NOT emit a
React/Babel composition, do NOT call other prototype skills, do NOT use the
sandboxed iframe's wall-clock playback for timing decisions. Plain HTML +
GSAP only. Treat the [`claude-design-hyperframes.md`](https://github.com/heygen-com/hyperframes/blob/main/docs/guides/claude-design-hyperframes.md)
companion document as the **upstream spec for HyperFrames structural rules** —
the rules below condense it to what Open Design needs at emission time, but
that file is the source of truth for shader catalogs, skeleton variants, and
edge cases.

---

## Your role

**You produce a valid first draft — not a final render.** Open Design's
strengths are visual identity (driven by the active `DESIGN.md`), layout, and
brand-accurate content decisions. The user (or their coding agent) handles
animation polish, timing micro-adjustments, and production QA after handoff.

The user's workflow:

1. **Open Design** (you) — pick palette + typography from the active
   `DESIGN.md`, fill scene content, lay down first-pass GSAP entrances and
   mid-scene activity, pick shader transitions for 2–3 key moments
2. **Save to disk** — Open Design writes the project into
   `.od/projects/<id>/` (real `cwd`, agent-ready)
3. **Any AI coding agent** (Claude Code, Codex, Cursor, …) — `npx hyperframes
   lint`, `npx hyperframes preview`, then iterate timing, eases, shader
   choices, pacing

Your output must be a **valid starting point a coding agent can open and
refine immediately** — no structural fixes needed.

### What you optimize for

- The active `DESIGN.md` palette + typography bound onto `:root` (never
  freestyle a palette when one is active)
- Strong visual layout per scene (hierarchy, spacing, readability at video
  size — 60px+ headlines, 20px+ body)
- Scene content that tells the story (headlines, stats, copy, imagery)
- Structural validity (passes `npx hyperframes lint` with zero errors)
- Appropriate shader choices for the mood (use the catalog at
  [hyperframes.heygen.com/catalog](https://hyperframes.heygen.com/catalog))
- Reasonable scene count and durations for the video type

### What the coding agent polishes after you

You ship every scene with entrance tweens, breathing motion, and shader
transitions. The video plays with full motion from your first draft. The
agent does the **edit-bay refinement**: ease curve tweaks, stagger timing,
scene-duration micro-adjustments, richer mid-scene activity, shader swaps,
production QA.

---

## Hard rules (must-pass before emitting `<artifact>`)

These are HyperFrames-structural and non-negotiable. Open Design's
five-dimensional self-critique gate must verify all of them before emission.

1. **Single HTML file.** `<!doctype html>` through `</html>`, all CSS inline,
   GSAP loaded from CDN. No build step.
2. **Root composition element.** A single `<div id="stage">` with:
   - `data-composition-id="<kebab-name>"`
   - `data-start="0"`
   - `data-width` / `data-height` (e.g. `1080` × `1920` for 9:16, `1920` ×
     `1080` for 16:9, `1080` × `1080` for square)
   - `data-duration="<total-seconds>"` matching the sum of scene durations
3. **Scenes are children of `#stage`.** Each scene is `<div class="scene
   clip">` with:
   - `data-start="<seconds-from-zero>"`
   - `data-duration="<scene-seconds>"`
   - `data-track-index="0"` (HyperFrames uses tracks for layering; visual
     scenes share track 0 unless you intentionally overlap)
   - A `.scene-content` wrapper inside it that holds the readable content
     (headlines, stats, imagery). Decoratives (glows, grain, vignette) live
     directly inside `.scene` but **outside** `.scene-content`.
4. **GSAP timeline registered paused.** A single timeline created with
   `gsap.timeline({ paused: true })` and registered on
   `window.__timelines = window.__timelines || {}; window.__timelines["<comp-id>"] = tl;`.
   This is what makes the composition deterministically seekable — the
   HyperFrames engine drives the playhead.
5. **`tl.from()` for entrances.** Animate FROM offscreen/invisible TO the
   resting CSS position. Offset the first tween 0.1–0.3s into each scene to
   avoid jump-cuts.
6. **Mid-scene activity on every scene.** Every visible element keeps moving
   after its entrance. A still element on a still background is a JPEG with
   a progress bar. Use at least 2 patterns per scene from the table below.
7. **Shader transitions ONLY at
