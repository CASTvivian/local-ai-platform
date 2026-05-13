# Missing Repo Summary Source: htdt/godogen

- URL: https://github.com/htdt/godogen
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/htdt__godogen
- Clone Status: cloned
- Language: Python
- Stars: 3163
- Topics: claude, claude-code, claude-code-skill, codex, codex-cli, codex-skill, game-development, godot, godot4, skills
- Description: Autonomous game development for Godot and Bevy with Claude Code and Codex

## Extracted README / Docs / Examples



# FILE: README.md

# Godogen: Autonomous game development for Godot and Bevy with Claude Code and Codex

[![Watch the video](https://img.youtube.com/vi/eUz19GROIpY/maxresdefault.jpg)](https://youtu.be/eUz19GROIpY)

[Watch the demos](https://youtu.be/eUz19GROIpY) · [Prompts](docs/demo_prompts.md)

Describe a game. Godogen plans it, writes the code, generates assets, runs the engine, checks screenshots, and fixes what looks wrong.

This repo is not a game. It is the source for a generator that produces games: **godogen -> game repo -> game**. You publish the skills into a fresh game repo, choosing the engine and host-agent flavor, then the agent runs inside that repo to build the actual game.

## Source layout

The source is organized along the engine axis:

- `shared/` — engine-agnostic `godogen` stages, asset-generation tooling, shared stop hook, and common game-repo instructions
- `godot/` — Godot-specific `godogen` stages, Godot capture helpers, and the `godot-api` skill
- `bevy/` — Bevy-specific `godogen` stages, Bevy capture helpers, and the `bevy-help` skill

Claude Code vs Codex is a publish-time render choice, not a separate source tree. The root [publish.sh](publish.sh) renders the right runtime layout for the chosen engine and host agent.

## What skills do

- **Godot 4 output** — real C#/.NET projects with proper scene trees, scene builders, scripts, and asset organization.
- **Godot Android export** — debug APK export remains available when the user requests an Android app.
- **Bevy output** — Rust/Bevy projects with code-first scenes, local Bevy docs lookup, deterministic capture guidance, and final proof bundles.
- **Asset generation** — Gemini creates precise references and characters; xAI Grok handles textures and simple objects; Tripo3D converts images to 3D models. Animated sprites use Grok video generation with loop detection.
- **C# / .NET 9 for Godot** — Godot output uses C#. See [why C# over GDScript](docs/gdscript-vs-csharp.md).
- **Frame-grounded self-repair** — the agent is carefully prompted to judge progress from captured screenshots, not from code that compiles, so visible defects (clipping, wrong scale, frozen motion, missing assets) drive the next iteration instead of being rationalized away.
- **Telegram proof push** — published repos install a stop hook that pushes the latest `screenshots/result/{N}/video.mp4` to Telegram when `tg-push` and the TG_* env vars are configured. No-op otherwise.
- **Runs on commodity hardware** — any machine with the relevant engine toolchain, Python, and the required API keys can run the pipeline.

## Getting started

### Prerequisites

- [Godot 4](https://godotengine.org/download/) (.NET build) on `PATH` for Godot projects
- Rust/Cargo plus local Bevy docs for Bevy projects
- Python 3 with pip
- API keys as environment variables:
  - `GOOGLE_API_KEY` — [Google AI Studio](https://aistudio.google.com/) for Gemini image generation
  - `XAI_API_KEY` — [xAI Grok](https://console.x.ai/home) for image/video generation
  - `TRIPO3D_API_KEY` — [Tripo3D](https://platform.tripo3d.ai/) for 3D generation
- System packages from [setup.md](setup.md): `vulkan-tools`, `xvfb`, `ffmpeg`, `imagemagick`, plus platform-specific extras
- Tested on Ubuntu, Debian, and macOS
- Claude Code or Codex

### Publish a game repo

Pick the engine and host agent:

```bash
./publish.sh --engine godot --agent claude --out ~/my-game  # CLAUDE.md + .claude/skills/
./publish.sh --engine godot --agent codex  --out ~/my-game  # AGENTS.md + .agents/skills/
./publish.sh --engine bevy  --agent claude --out ~/my-game
./publish.sh --engine bevy  --agent codex  --out ~/my-game
```

Pass `--force` to wipe existing contents at the target before publishing — use this when re-publishing over a previous run.

### Bevy docs setup

If you're working on Bevy generation, configure and populate a shared Bevy docs folder once after clone:

```bash
./setup_bevy_docs.sh /absolute/or/user/path/to/bevy-docs
```

The setup script links `bevy/skills/bevy-help/docs/` to that folder, creates shallow Bevy docs source checkouts for new caches, and builds local rustdoc for the current stable release. No default path is assumed. See [setup.md](setup.md) for the full workstation setup.

## Running on a server

A full generation run can take hours, so it's convenient to offload it to a server, ideally a GPU instance, since engine rendering and video capture are much faster with hardware acceleration.

- Keep the session alive across SSH drops with `tmux` or `screen`.
- Install [tg-push](https://github.com/htdt/tg-push): the stop hook auto-sends the final proof video to Telegram on completion.
- Enable remote control so you can check in and steer the run from any device — both Claude Code and Codex have official remote-control interfaces.

## Improving the skills

After a full generation session, ask the agent you used to review how the pipeline performed:

> Analyze this session. Were the instructions optimal? Flag anything that was too obvious, missing, or misleading. Did any tools pollute context with noise? Did the capture loop catch the real problems? Any tool failures or workarounds?

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

Follow progress: [@alex_erm](https://x.com/alex_erm)


# FILE: docs/gdscript-vs-csharp.md

# GDScript vs C# — Skill Instruction Comparison

## What C# eliminated

**GDScript's type inference minefield is gone.** The GDScript quirks.md had a 28-line "Type Inference Errors" section documenting `:=` footguns — `instantiate()` returns Variant, polymorphic math functions (`abs`, `clamp`, `lerp`, `min`, `max`...) return Variant, array/dict element access returns Variant. All of these silently break type inference with `:=`. This entire class of errors doesn't exist in C#.

Other GDScript-specific issues removed:
- `preload()` vs `load()` ordering trap during generation
- `await` during `--write-movie` advancing frame counter
- `@onready` timing with `init()` vs `_ready()`
- `get_path()` name collision with Node built-in
- Pass-by-value workarounds needing Array accumulators (C# has `ref`/`out` and return values)

**task-execution.md shrank 14%** — the GDScript version needed `--check-only -s` per-file pre-validation step; C# replaces it with a single `dotnet build` that catches everything at once.

## What C# added

**One major quirk: `SetScript()` disposes the C# managed wrapper.** After calling `SetScript()` on a node, the C# variable is dead (`ObjectDisposedException`). This requires a "temp parent" pattern to re-obtain root nodes. It's well-contained — 12 lines of example code — and once the pattern is in the template, it's never a problem in practice.

Other C#-specific additions:
- `.csproj` file (5 lines of boilerplate, but one more file to manage)
- `dotnet build` step in the pipeline (replaces per-file `--check-only`)
- `partial` class requirement on every Godot class
- Signal delegates must end in `EventHandler`
- C# enum names are unreliable in LLM output (training data is predominantly GDScript) — explicit `godot-api` lookup instruction added

## Code comparison: asset loading

The game logic is conceptually identical — same nodes, same hierarchy, same engine API. The difference is how much the language fights you while writing it.

```gdscript
# GDScript — three traps in four lines
var scene: PackedScene = load("res://assets/glb/car.glb")  # MUST type, or load() returns Resource
var model = scene.instantiate()                              # MUST use = not :=, Variant inference
var found = find_mesh_instance(model)                        # MUST use = not :=, recursive return
```

```csharp
// C# — just works
var scene = GD.Load<PackedScene>("res://assets/glb/car.glb");  // generic returns PackedScene
var model = scene.Instantiate();                                // type flows through
var found = FindMeshInstance(model);                            // same
```

GDScript requires remembering where `var x :=` is forbidden and where explicit typing is needed. C# generics and type inference handle this automatically. The actual game logic — physics, input, camera rigs, collision setup, node hierarchy — is 1:1 identical between the two. PascalCase instead of snake_case, `new Vector3()` instead of `Vector3()`, braces instead of indentation. No conceptual difference.

## Qualitative assessment

**GDScript complexity profile:** Death by a thousand paper cuts. The type inference system creates a steady stream of subtle errors — the LLM generates plausible code that fails silently or with cryptic messages. Every `load()`, `instantiate()`, `abs()`, array access is a potential trap. The `:=` operator is the default instinct but fails on ~15 common API patterns.

**C# complexity profile:** One sharp edge (`SetScript()` disposal), one ecosystem tax (`.csproj` + `dotnet build`), one LLM bias issue (enum names from GDScript training data). Everything else is standard typed language — the compiler catches mistakes before runtime. The type system works *with* you rather than against you.

**Bottom line:** C# is not easier or harder to write *conceptually* — it's easier to write *correctly*. The compiler catches what GDScript lets through silently. C# trades GDScript's diffuse type-system complexity (many small gotchas scattered everywhere) for a small number of well-documented, well-contained sharp edges. The instructions are 9% larger by line count but carry less cognitive load — the quirks file alone went from 100 lines to 79 despite adding the `SetScript()` pattern. The LLM generates more correct code on the first try because the type system prevents the Variant inference class of errors entirely.


# FILE: docs/PROJECT.md

# Godogen — From Prompt to Playable Game

Godogen is an autonomous development pipeline for turning a natural-language game brief into a playable Godot or Bevy project. It plans the game, generates visual direction and assets, writes code, and captures media from the running engine for visual review.

It is not a game engine, a code generator, or an asset marketplace. It is a source repo for runtime skills that are published into a fresh game repo and then executed by Claude Code or Codex.

## Source Model

The repo is organized by engine:

- `shared/` — engine-agnostic `godogen` stages, the shared `Stop` hook, and common published-repo instructions
- `godot/` — Godot-specific `godogen` stages and `godot-api`
- `bevy/` — Bevy-specific `godogen` stages and `bevy-help`

Claude Code vs Codex is selected at render time:

```bash
./publish.sh --engine godot --agent claude --out ~/game
./publish.sh --engine godot --agent codex --out ~/game
./publish.sh --engine bevy --agent claude --out ~/game
./publish.sh --engine bevy --agent codex --out ~/game
```

Publishing writes `CLAUDE.md` plus `.claude/skills/` for Claude Code, or `AGENTS.md` plus `.agents/skills/` for Codex. Codex `agents/openai.yaml` files are generated from each rendered `SKILL.md` frontmatter.

## Pipeline

The `godogen` skill orchestrates the run and loads stage-specific files only when they are needed:

1. **Visual target** — generate `reference.png` and write art direction into `ASSETS.md`.
2. **Decomposition** — write `PLAN.md`, isolating only genuinely risky features.
3. **Scaffold** — create or update the engine project shell and `STRUCTURE.md`.
4. **Asset planning and generation** — spend the user-provided budget on the assets that matter most.
5. **Task execution** — implement risk slices first, then the main build.
6. **Capture** — create a fresh `screenshots/result/{N}/` bundle with raw `frameXXX.png` files and `video.mp4`.
7. **Telegram push** — the shared stop hook pushes the latest proof video to Telegram when `tg-push` and `TG_*` env vars are configured; otherwise it no-ops.

The document protocol is deliberate. `PLAN.md`, `STRUCTURE.md`, `ASSETS.md`, and `MEMORY.md` survive context compaction and let the run resume from files instead of conversational memory.

## Engine Support

Godot output is a Godot 4 C#/.NET project. The Godot runtime skill uses scene builders for generated `.tscn` files, runtime scripts for gameplay, `godot-api` for targeted engine lookup, and a Godot capture helper for final proof bundles.

Bevy output is a Rust/Bevy project. The Bevy runtime skill uses code-first scene construction, local Bevy rustdoc/examples through `bevy-help`, and a dedicated capture path for final proof bundles.

Both engines share the same final-bundle contract: the latest numeric `screenshots/result/{N}/` folder containing `video.mp4` plus its raw `frameXXX.png` sequence.

## What Makes This Different

**Capture-first proof.** The pipeline captures actual frames from the game and assembles them into a final proof bundle, so the run is judged on what the game looks like rather than on what the code claims.

**Progressive loading.** The orchestrator reads only the stage file it needs at the moment. Support skills keep large engine references out of the main context.

**Budget-aware asset generation.** Gemini, Grok, and Tripo3D are used where they make economic sense, and generated assets are assigned back into `PLAN.md` so implementation does not lose them.

**Engine-specific expertise without agent duplication.** Godot and Bevy are different enough to keep their engine docs separate. Claude and Codex are similar enough to render from one source.

## Runtime Limitations

The current runtime does not ship audio. Godot supports debug APK export when requested; Bevy Android export is not implemented yet.


# FILE: docs/demo_prompts.md

# Demo Prompts

## CartoRally

```text
Top-down racing game with a stylized topographic map aesthetic. Terrain rendered with visible contour lines following elevation changes, spaced tighter on steep slopes and wider on flat areas. Muted earthy color palette: cream/parchment base, sage green for lowlands, tan/brown for mid-elevation, grey-white for peaks. The racing track is a bold saturated line (burnt orange or red) cutting through the terrain, with subtle road markings. Trees represented as simplified symbolic markers — small clustered circles in dark green, like map legend symbols. Mountain border walls rendered as dense contour bundles with hatch shading. Subtle paper texture overlay across the entire scene. Elevation communicated through both 3D geometry and contour line density. Clean, minimal, highly readable. Visual references: topographic hiking maps, ordnance survey maps, vintage cartography with a modern minimal twist.
Terrain is a heightmap with distinct elevation changes — rolling hills create natural ramps where the car launches into the air and lands with impact. Track conforms to the terrain surface, following contours over hills and through valleys. Car physics emphasize verticality: visible airtime on crests, shadow separation from ground during jumps, suspension compression on landing. High mountain walls enclose the scene as natural borders. Closed-loop circuit with a natural winding layout through varied elevation.
```

## Ultra Realistic Nature Scene

```text
Generate a serene riverbank nature scene combining HQ 3D models with procedural shaders.
Scene elements:
River with shader-based water (reflection, refraction, flow, edge foam)
Riverbank with shader-blended ground (grass/dirt/mud transition)
Procedural grass with wind-animated vertex shaders
One tree — modeled trunk/branches, shader-driven leaf cards with wind sway and translucency
Forest backdrop behind the river (simple tree silhouettes or billboard impostors)
Old small wooden boat (3D model, weathered look)
Fallen log on the bank (3D model)
Technical split:
Models: boat, log, tree trunk/branches, rocks
Shaders: water surface, grass, leaves, ground blending, wind animation
Visual targets: Natural lighting (directional sun + ambient), soft shadows, subtle fog/atmosphere for depth.
```

## Amsterdam Cyclist

```text
A 2D side-scrolling cyclist game, left to right, with lane switching, slow and relaxed in pace. You ride through Amsterdam on a red bike lane — 4 horizontal lanes stacked vertically: two bottom lanes for your direction, two top lanes with oncoming traffic. Tourists jump onto the bike lane from gray sidewalks (top and bottom edges) as obstacles; three caricature types: the Selfie Walker (phone up, completely oblivious), the Lost Map Reader (spinning confused, giant map unfolded), and the Tulip Hauler (struggling to see past a comically huge bouquet of tulips, drifting blindly). You dodge by switching lanes vertically; moving into oncoming lanes risks hitting approaching cyclists — the core risk/reward. Lane switching is discrete with smooth lerp, max speed caps at 25 km/h — the vibe is chill Amsterdam cruising that slowly gets chaotic.
Three-layer parallax: canal water at the bottom scrolls fastest, road/bike lanes at medium speed, townhouse facades along the top slowest. The canal is visually rich — animated dark water with ripple highlights, and varied boats drifting past: classic sloepen with passengers, houseboats with rooftop plants, tourist canal boats, an occasional rower. Boats vary in size and speed, some overlapping — pure eye candy, no interaction. Road markings (dashed center line, bike symbols, arrows) are baked into the road tile texture, not separate objects. Sidewalks have a subtle brick pattern. All sprites stay small (~250px) with bold simple shapes, thick outlines, flat filled colors — chunky and iconic, readable at a glance.
The cyclist has a pedaling animation loop. Each tourist type has a distinct animation: Selfie Walker shuffling with phone raised, Map Reader spinning in place, Tulip Hauler swaying with the bouquet bobbing. Art style: flat colored sprite illustrations, clean and cartoony. HUD shows distance and speed; game over screen with final score and restart. Controls: W/S or Up/Down to switch lanes. No coins or power-ups — just survival as tourist density gradually increases.
```

## 3D Alpine Snowboard Simulator

```text
A downhill snowboarding game set in an Alpine ski resort.
World: A long slope descending with gentle undulations. A curvy groomed track winds down the center, flanked by powder snow zones on both sides — visually distinct, and entering them heavily dampens speed. Scattered along the track are ramp-shaped kickers that launch the rider airborne when hit with speed.
Obstacles: Slow-moving skiers (simple figures) drift downhill on the track. Snowy pine trees with white snow caps line the edges and occasionally encroach onto the track. Collision with either means crash and game over with restart option.
Snowboard physics — the core feel: The rider stands sideways on a board. Left/Right input carves by tilting onto the heel edge or toe edge — lean the whole model into the turn and gradually arc the heading. Turns should feel carved with angular momentum, not instant snaps. Sharper carves scrub more speed. No input means neutral glide with gravity acceleration. Airborne means preserve momentum plus gravity.
Snow spray: Sharp carves spawn a burst of white particles fanning out from the board's outside edge, rising slightly and fading quickly. Harder carve means bigger spray. This should feel satisfying and punchy.
Camera: Third-person chase cam behind and above the rider, smooth-following with slight lag, gently swinging on turns.
Scenery: Panorama image. At the bottom of the slope, a charming Alpine village — clustered wooden chalets with snowy roofs, a small church steeple. Behind it, jagged snow-capped mountain peaks on the horizon. Clear winter blue sky wi
