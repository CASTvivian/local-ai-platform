# Repo Summary Source: JuliusBrussee/caveman
- URL: https://github.com/JuliusBrussee/caveman
- Local Path: core-platform/data/brain_assets/repos/github_stars/JuliusBrussee__caveman
- Buckets: agent, llm_runtime
- Stars: 59037
- Language: JavaScript
- Description: 🪨 why use many token when few token do trick — Claude Code skill that cuts 65% of tokens by talking like caveman
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

<p align="center">
  <img src="https://em-content.zobj.net/source/apple/391/rock_1faa8.png" width="120" />
</p>

<h1 align="center">caveman</h1>

<p align="center">
  <strong>why use many token when few do trick</strong>
</p>

<p align="center">
  <a href="https://github.com/JuliusBrussee/caveman/stargazers"><img src="https://img.shields.io/github/stars/JuliusBrussee/caveman?style=flat&color=yellow" alt="Stars"></a>
  <a href="https://github.com/JuliusBrussee/caveman/commits/main"><img src="https://img.shields.io/github/last-commit/JuliusBrussee/caveman?style=flat" alt="Last Commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/JuliusBrussee/caveman?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="#before--after">Before/After</a> •
  <a href="#install">Install</a> •
  <a href="#what-you-get">What You Get</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="./INSTALL.md">Full install guide</a>
</p>

---

A [Claude Code](https://docs.anthropic.com/en/docs/claude-code) skill/plugin (also Codex, Gemini, Cursor, Windsurf, Cline, Copilot, 30+ more) that makes agent talk like caveman — cuts **~75% of output tokens**, keeps full technical accuracy. Brain still big. Mouth small.

## Before / After

<table>
<tr>
<td width="50%">

### 🗣️ Normal Claude (69 tokens)

> "The reason your React component is re-rendering is likely because you're creating a new object reference on each render cycle. When you pass an inline object as a prop, React's shallow comparison sees it as a different object every time, which triggers a re-render. I'd recommend using useMemo to memoize the object."

</td>
<td width="50%">

### 🪨 Caveman Claude (19 tokens)

> "New object ref each render. Inline object prop = new ref = re-render. Wrap in `useMemo`."

</td>
</tr>
<tr>
<td>

### 🗣️ Normal Claude

> "Sure! I'd be happy to help you with that. The issue you're experiencing is most likely caused by your authentication middleware not properly validating the token expiry. Let me take a look and suggest a fix."

</td>
<td>

### 🪨 Caveman Claude

> "Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:"

</td>
</tr>
</table>

**Same fix. 75% less word. Brain still big.**

```
┌─────────────────────────────────────┐
│  TOKENS SAVED          ████████ 75% │
│  TECHNICAL ACCURACY    ████████ 100%│
│  SPEED INCREASE        ████████ ~3x │
│  VIBES                 ████████ OOG │
└─────────────────────────────────────┘
```

Pick your level of grunt — `lite` (drop filler), `full` (default caveman), `ultra` (telegraphic), or `wenyan` (classical Chinese, even shorter). One command switch. Cost go down forever.

## Install

One line. Find every agent. Install for each.

```bash
# macOS / Linux / WSL / Git Bash
curl -fsSL https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.sh | bash

# Windows (PowerShell 5.1+)
irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex
```

~30 seconds. Needs Node ≥18. Skip agent you no have. Safe to re-run.

**Trigger:** type `/caveman` or say "talk like caveman". Stop with "normal mode".

One agent only, manual command, or any of 30+ other agents → [**INSTALL.md**](./INSTALL.md).
Install break? Open agent, say *"Read CLAUDE.md and INSTALL.md, install caveman for me."* Agent fix own brain.

## What You Get

| Skill | What |
|---|---|
| `/caveman [lite\|full\|ultra\|wenyan]` | Compress every reply. Levels stick until session end. |
| `/caveman-commit` | Conventional Commit messages, ≤50 char subject. Why over what. |
| `/caveman-review` | One-line PR comments: `L42: 🔴 bug: user null. Add guard.` |
| `/caveman-stats` | Real session token usage + lifetime savings + USD. Tweetable line via `--share`. |
| `/caveman-compress <file>` | Rewrite memory file (e.g. `CLAUDE.md`) into caveman-speak. Cuts ~46% input tokens every session. Code/URLs/paths byte-preserved. |
| `caveman-shrink` | MCP middleware. Wraps any MCP server, compresses tool descriptions. [npm](https://www.npmjs.com/package/caveman-shrink). |
| `cavecrew-*` | Caveman subagents (investigator/builder/reviewer). ~60% fewer tokens than vanilla, main context lasts longer. |

**Statusline badge** — Claude Code shows `[CAVEMAN] ⛏ 12.4k` (lifetime tokens saved). Updates every `/caveman-stats` run. Set `CAVEMAN_STATUSLINE_SAVINGS=0` to silence.

Auto-activate every session: Claude Code, Codex, Gemini (built-in). Cursor / Windsurf / Cline / Copilot get always-on rule files via `--with-init`. Other agents trigger with `/caveman` per session. Full feature matrix in [INSTALL.md](./INSTALL.md#what-you-get).

## Benchmarks

Real token counts from the Claude API. Average **65% output reduction** across 10 prompts (range 22-87%).

<!-- BENCHMARK-TABLE-START -->
| Task | Normal | Caveman | Saved |
|------|-------:|--------:|------:|
| Explain React re-render bug | 1180 | 159 | 87% |
| Fix auth middleware token expiry | 704 | 121 | 83% |
| Set up PostgreSQL connection pool | 2347 | 380 | 84% |
| Explain git rebase vs merge | 702 | 292 | 58% |
| Refactor callback to async/await | 387 | 301 | 22% |
| Architecture: microservices vs monolith | 446 | 310 | 30% |
| Review PR for security issues | 678 | 398 | 41% |
| Docker multi-stage build | 1042 | 290 | 72% |
| Debug PostgreSQL race condition | 1200 | 232 | 81% |
| Implement React error boundary | 3454 | 456 | 87% |
| **Average** | **1214** | **294** | **65%** |
<!-- BENCHMARK-TABLE-END -->

Raw data and reproduction script: [`benchmarks/`](./benchmarks/). Three-arm eval harness (baseline / terse / skill) lives in [`evals/`](./evals/) — caveman compared against `Answer concisely.` not against verbose default, so the delta is honest.

**caveman-compress receipts** (real memory files):

| File | Original | Compressed | Saved |
|---|---:|---:|---:|
| `claude-md-preferences.md` | 706 | 285 | **59.6%** |
| `project-notes.md` | 1145 | 535 | **53.3%** |
| `claude-md-project.md` | 1122 | 636 | **43.3%** |
| `todo-list.md` | 627 | 3


# FILE: docs/install-windows.md

# Windows install fallback

If `irm https://raw.githubusercontent.com/JuliusBrussee/caveman/main/install.ps1 | iex` fails on Windows (issues #249, #199, #72), set up plugin-skill activation by hand. This does **not** install the standalone hooks or the statusline — for those, run the unified Node installer afterwards: `npx -y github:JuliusBrussee/caveman -- --only claude` (or `node bin/install.js --only claude` from a clone).

```powershell
$ClaudeDir = if ($env:CLAUDE_CONFIG_DIR) { $env:CLAUDE_CONFIG_DIR } else { Join-Path $HOME ".claude" }
$PluginSkillDir = Join-Path $ClaudeDir ".agents\plugins\caveman\skills\caveman"
$MarketplaceDir = Join-Path $ClaudeDir ".agents\plugins"
$MarketplaceFile = Join-Path $MarketplaceDir "marketplace.json"

# Copy SKILL.md into the plugin path (run from a clone of the repo)
New-Item -ItemType Directory -Path $PluginSkillDir -Force | Out-Null
Copy-Item ".\skills\caveman\SKILL.md" "$PluginSkillDir\SKILL.md" -Force

# Create or update marketplace.json with the caveman entry
New-Item -ItemType Directory -Path $MarketplaceDir -Force | Out-Null
if (Test-Path $MarketplaceFile) {
  $marketplace = Get-Content $MarketplaceFile -Raw | ConvertFrom-Json
} else {
  $marketplace = [pscustomobject]@{}
}
if (-not ($marketplace.PSObject.Properties.Name -contains "plugins")) {
  $marketplace | Add-Member -NotePropertyName plugins -NotePropertyValue ([pscustomobject]@{})
}
$plugins = [ordered]@{}
foreach ($p in $marketplace.plugins.PSObject.Properties) { $plugins[$p.Name] = $p.Value }
$plugins["caveman"] = [ordered]@{ name = "caveman"; source = "JuliusBrussee/caveman"; version = "main" }
$marketplace.plugins = [pscustomobject]$plugins
$marketplace | ConvertTo-Json -Depth 10 | Set-Content -Path $MarketplaceFile -Encoding UTF8
```

Verify: `Test-Path "$PluginSkillDir\SKILL.md"` should print `True`. Restart Claude Code, then run `/caveman` to confirm the skill loads.

## Codex on Windows

1. Enable symlinks first: `git config --global core.symlinks true` (requires Developer Mode or admin).
2. Clone repo → Open VS Code → Codex Settings → Plugins → find "Caveman" under the local marketplace → Install → Reload Window.
3. Codex hooks are currently disabled on Windows, so use `$caveman` to start the mode manually each session.

## `npx skills` symlink fallback

`npx skills` uses symlinks by default. If symlinks fail, add `--copy`:

```powershell
npx skills add JuliusBrussee/caveman --copy
```

## Want it always on (any agent)?

Paste this into the agent's system prompt or rules file:

```
Terse like caveman. Technical substance exact. Only fluff die.
Drop: articles, filler (just/really/basically), pleasantries, hedging.
Fragments OK. Short synonyms. Code unchanged.
Pattern: [thing] [action] [reason]. [next step].
ACTIVE EVERY RESPONSE. No revert after many turns. No filler drift.
Code/commits/PRs: normal. Off: "stop caveman" / "normal mode".
```

