# Missing Repo Summary Source: Yeachan-Heo/oh-my-codex

- URL: https://github.com/Yeachan-Heo/oh-my-codex
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/Yeachan-Heo__oh-my-codex
- Clone Status: cloned
- Language: TypeScript
- Stars: 28395
- Topics: 
- Description: OmX - Oh My codeX: Your codex is not alone. Add hooks, agent teams, HUDs, and so much more.

## Extracted README / Docs / Examples



# FILE: README.md

# oh-my-codex (OMX)

<p align="center">
  <img src="https://yeachan-heo.github.io/oh-my-codex-website/omx-character-nobg.png" alt="oh-my-codex character" width="280">
  <br>
  <em>Start Codex stronger, then let OMX add better prompts, workflows, and runtime help when the work grows.</em>
</p>

[![npm version](https://img.shields.io/npm/v/oh-my-codex)](https://www.npmjs.com/package/oh-my-codex)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Node.js](https://img.shields.io/badge/node-%3E%3D20-brightgreen)](https://nodejs.org)
[![Discord](https://img.shields.io/discord/1452487457085063218?color=5865F2&logo=discord&logoColor=white&label=Discord)](https://discord.gg/PUwSMR9XNk)

**Website:** https://yeachan-heo.github.io/oh-my-codex-website/

**Docs:** [Getting Started](./docs/getting-started.html) · [Agents](./docs/agents.html) · [Skills](./docs/skills.html) · [Integrations](./docs/integrations.html) · [Demo](./DEMO.md) · [OpenClaw guide](./docs/openclaw-integration.md)

**Community:** [Discord](https://discord.gg/PUwSMR9XNk) — shared OMX/community server for oh-my-codex and related tooling.

OMX is a workflow layer for [OpenAI Codex CLI](https://github.com/openai/codex).

<table>
<tr>
<td><strong>🚨 CAUTION — RECOMMENDED DEFAULT ONLY: macOS or Linux with Codex CLI.</strong><br><br><strong>OMX is primarily designed and actively tuned for that path.</strong><br><strong>Native Windows and Codex App are not the default experience, may break or behave inconsistently, and currently receive less support.</strong></td>
</tr>
</table>

It keeps Codex as the execution engine and makes it easier to:
- start a stronger Codex session by default
- run one consistent workflow from clarification to completion
- invoke the canonical skills with `$deep-interview`, `$ralplan`, `$team`, and `$ralph`
- keep project guidance, plans, logs, and state in `.omx/`

## Core Maintainers

| Role | Name | GitHub |
| --- | --- | --- |
| Creator & Lead | Yeachan Heo | [@Yeachan-Heo](https://github.com/Yeachan-Heo) |
| Maintainer | HaD0Yun | [@HaD0Yun](https://github.com/HaD0Yun) |

## Ambassadors

| Name | GitHub |
| --- | --- |
| Sigrid Jin | [@sigridjineth](https://github.com/sigridjineth) |

## Top Collaborators

| Name | GitHub |
| --- | --- |
| HaD0Yun | [@HaD0Yun](https://github.com/HaD0Yun) |
| Junho Yeo | [@junhoyeo](https://github.com/junhoyeo) |
| JiHongKim98 | [@JiHongKim98](https://github.com/JiHongKim98) |
| Lor | [@gobylor](https://github.com/gobylor) |
| HyunjunJeon | [@HyunjunJeon](https://github.com/HyunjunJeon) |

## Recommended default flow

If you want the default OMX experience, start here:

```bash
npm install -g @openai/codex oh-my-codex
omx --madmax --high
```

On a real `oh-my-codex` version bump, the global npm install now prints an explicit reminder instead of launching `omx setup` automatically. When you're ready, run `omx setup` manually or use `omx update` to check npm and then run the same setup refresh path.

**Codex plugin install note:** this repo also ships an official Codex plugin layout at `plugins/oh-my-codex` with marketplace metadata in `.agents/plugins/marketplace.json`. That plugin bundles the mirrored skill surface plus plugin-scoped companion metadata for optional MCP compatibility servers and apps, disabled by default. Native/runtime hooks still stay on the setup/runtime side rather than the installable plugin manifest. It is still **not** a replacement for `npm install -g oh-my-codex` plus `omx setup`: legacy setup mode installs native agents and prompts, while plugin setup mode relies on plugin discovery for bundled skills and archives/removes legacy OMX-managed prompts/native-agent TOMLs so stale role files cannot shadow plugin behavior.

Then work normally inside Codex:

```text
$deep-interview "clarify the authentication change"
$ralplan "approve the auth plan and review tradeoffs"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
$ultragoal "turn this launch into durable Codex goals"
```

That is the main path.
Before you treat the runtime as ready, run the quick-start smoke test below: `omx doctor` verifies the install shape, while `omx exec` proves the active Codex runtime can actually authenticate and complete a model call from the current environment.
Start OMX strongly, clarify first when needed, approve the plan, then choose `$team` for coordinated parallel execution or `$ralph` for the persistent completion loop.

## What OMX is for

Use OMX if you already like Codex and want a better day-to-day runtime around it:
- a standard workflow built around `$deep-interview`, `$ralplan`, `$team`, and `$ralph`
- durable multi-goal handoffs with `$ultragoal` and `.omx/ultragoal` artifacts when a launch needs sequential Codex goals
- specialist roles and supporting skills when the task needs them
- project guidance through scoped `AGENTS.md`
- durable state under `.omx/` for plans, logs, memory, and mode tracking

If you want plain Codex with no extra workflow layer, you probably do not need OMX.

## Quick start

### Requirements

- Node.js 20+
- Codex CLI installed: `npm install -g @openai/codex`
- Codex auth configured and visible in the same shell/profile that will run OMX
- `tmux` on macOS/Linux if you want the recommended durable team runtime
- `psmux` on native Windows only if you intentionally want the less-supported Windows team path

### A good first session

After install, check both boundaries:

```bash
omx doctor
codex login status
omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"
```

`omx doctor` catches missing OMX files, hooks, and runtime prerequisites. The real smoke test catches auth, profile, and provider/base-URL problems that only appear when Codex performs an actual request.

Launch OMX the recommended way:

```bash
omx --madmax --high
```

On macOS/Linux interactive terminals with `tmux` available, this starts the
leader in OMX-managed detached tmux by default so the HUD/runtime panes can be
created and recovered.

If you want a one-off launch with no OMX tmux/HUD management, use `--direct`:

```bash
omx --direct --yolo
```

For a persistent shell/profile preference, set an environment policy:

```bash
OMX_LAUNCH_POLICY=direct omx --yolo
```

Return to the auto/default behavior with:

```bash
unset OMX_LAUNCH_POLICY
```

CLI policy flags win over the environment, and the last CLI policy flag before
`--` wins:

```bash
OMX_LAUNCH_POLICY=direct omx --tmux --yolo
```

Use `OMX_LAUNCH_POLICY=direct|tmux|detached-tmux|auto`. This iteration only
adds CLI and environment controls; it intentionally does not add a config-file
setting. If you run `--direct` from inside an existing tmux pane, OMX will not
create HUD splits, enable mouse mode, or wrap extended-key handling, but the
process still runs inside that already-open terminal pane.

Then try the canonical workflow:

```text
$deep-interview "clarify the authentication change"
$ralplan "approve the safest implementation path"
$ralph "carry the approved plan to completion"
$team 3:executor "execute the approved plan in parallel"
```

Use `$team` when the approved plan needs coordinated parallel work, or `$ralph` when one persistent owner should keep pushing to completion.

## A simple mental model

OMX does **not** replace Codex.

It adds a better working layer around it:
- **Codex** does the actual agent work
- **OMX role keywords** make useful roles reusable
- **OMX skills** make common workflows reusable
- **`.omx/`** stores plans, logs, memory, and runtime state

Most users should think of OMX as **better task routing + better workflow + better runtime**, not as a command surface to operate manually all day.

## Start here if you are new

1. Install or update OMX with `npm install -g @openai/codex oh-my-codex`
2. After install or real OMX version bumps, run `omx setup` yourself when you're ready, or use `omx update` when you also want npm to check for and install the latest build before refreshing setup
3. Run `omx doctor`
4. Run a real execution smoke test: `codex login status` and `omx exec --skip-git-repo-check -C . "Reply with exactly OMX-EXEC-OK"`
5. Launch with `omx --madmax --high`
6. Use `$deep-interview "..."` when the request or boundaries are still unclear
7. Use `$ralplan "..."` to approve the plan and review tradeoffs
8. Choose `$team` for coordinated parallel execution or `$ralph` for persistent completion loops

## Recommended workflow

1. `$deep-interview` — clarify scope when the request or boundaries are still vague.
2. `$ralplan` — turn that clarified scope into an approved architecture and implementation plan.
3. `$team` or `$ralph` — use `$team` for coordinated parallel execution, or `$ralph` when you want a persistent completion loop with one owner.

## Common in-session surfaces

| Surface | Use it for |
| --- | --- |
| `$deep-interview "..."` | clarifying intent, boundaries, and non-goals |
| `$ralplan "..."` | approving the implementation plan and tradeoffs |
| `$ralph "..."` | persistent completion and verification loops |
| `$team "..."` | coordinated parallel execution when the work is big enough |
| `/skills` | browsing installed skills and supporting helpers |

## Advanced / operator surfaces

These are useful, but they are not the main onboarding path.

### Team runtime

Use the team runtime when you specifically need durable tmux/worktree coordination, not as the default way to begin using OMX. In Codex App or plain outside-tmux sessions, treat `omx team` as a tmux-runtime shell surface rather than a directly available in-app workflow; launch OMX CLI from shell first if you actually want team execution.

```bash
omx team 3:executor "fix the failing tests with verification"
omx team status <team-name>
omx team resume <team-name>
omx team shutdown <team-name>
```

### Setup, doctor, and HUD

These are operator/support surfaces:
- Codex plugin marketplace install/dis

# FILE: docs/hooks-extension.md

# Hooks Extension (Custom Plugins)

OMX supports an additive hooks extension point for user plugins under `.omx/hooks/*.mjs`.

The official packaged Codex plugin at `plugins/oh-my-codex` also ships plugin-scoped
companion metadata files (`.mcp.json`, `.app.json`) so the plugin bundle describes those
surfaces from inside the plugin root. Native/runtime hooks are intentionally separate:
they stay on the runtime/config side (`.codex/hooks.json` plus `.omx/hooks/*.mjs`) rather
than inside the installable plugin manifest.

Native Codex hook ownership is documented separately in
[Codex native hook mapping](./codex-native-hooks.md). In short:

- `.codex/hooks.json` = native Codex hook registrations installed by `omx setup`
- `.omx/hooks/*.mjs` = OMX plugin hooks dispatched by runtime/native events
- `omx tmux-hook` / notify-hook / derived watcher = tmux/runtime fallback surfaces

`omx setup` treats `.codex/hooks.json` as a shared-ownership file: it refreshes only the OMX-managed
wrapper entries that invoke `dist/scripts/codex-native-hook.js` and preserves user hook entries in the
same file. `omx uninstall` removes only those OMX-managed wrappers and leaves `.codex/hooks.json` in
place when user hooks remain.

> Compatibility guarantee: `omx tmux-hook` remains fully supported and unchanged.
> The new `omx hooks` command group is additive and does **not** replace tmux-hook workflows.

## Quick start

```bash
omx hooks init
omx hooks status
omx hooks validate
omx hooks test
```

This creates a scaffold plugin at:

- `.omx/hooks/sample-plugin.mjs`

## Enablement model

Plugins are **enabled by default**.

Disable plugin dispatch explicitly:

```bash
export OMX_HOOK_PLUGINS=0
```

Optional timeout tuning (default: 1500ms):

```bash
export OMX_HOOK_PLUGIN_TIMEOUT_MS=1500
```

## Native event pipeline (v1)

Native/derived plugin events come from two places:

1. Existing lifecycle/notify paths
2. Native Codex hook entrypoint dispatch (`dist/scripts/codex-native-hook.js`)

Current event vocabulary exposed to OMX plugins:

- `session-start`
- `keyword-detector`
- `pre-tool-use`
- `post-tool-use`
- `stop`
- `session-end`
- `turn-complete`
- `session-idle`

OMX keeps this existing event vocabulary rather than exposing raw Codex hook names directly.
That lets native Codex hooks and fallback/derived paths feed one shared plugin/runtime surface.

For clawhip-oriented operational routing, see [Clawhip Event Contract](./clawhip-event-contract.md).

Envelope fields include:

- `schema_version: "1"`
- `event`
- `timestamp`
- `source` (`native` or `derived`)
- `context`
- optional IDs: `session_id`, `thread_id`, `turn_id`, `mode`

## Derived signals (opt-in)

Best-effort derived events are gated and disabled by default.

```bash
export OMX_HOOK_DERIVED_SIGNALS=1
```

Derived signals include:

- `needs-input`
- `pre-tool-use`
- `post-tool-use`

Derived events are labeled with:

- `source: "derived"`
- `confidence`
- parser-specific context hints

## Team-safety behavior

In team-worker sessions (`OMX_TEAM_WORKER` set), plugin side effects are skipped by default.
This keeps the lead session as the canonical side-effect emitter and avoids duplicate sends.

## Plugin contract

Each plugin must export:

```js
export async function onHookEvent(event, sdk) {
  // handle event
}
```

SDK surface includes:

- `sdk.tmux.sendKeys(...)`
- `sdk.log.info|warn|error(...)`
- `sdk.state.read|write|delete|all(...)` (plugin namespace scoped)
- `sdk.omx.session.read()`
- `sdk.omx.hud.read()`
- `sdk.omx.notifyFallback.read()`
- `sdk.omx.updateCheck.read()`

`sdk.omx` is intentionally narrow and read-only in pass one. These helpers read the
repo-root `.omx/state/*.json` runtime files for the current workspace.

Compatibility notes:

- `omx tmux-hook` remains a CLI/runtime workflow, not `sdk.omx.tmuxHook.*`
- pass one does not add `sdk.omx.tmuxHook.*`; tmux plugin behavior stays on `sdk.tmux.sendKeys(...)`
- pass one does not add generic `sdk.omx.readJson(...)`, `sdk.omx.list()`, or `sdk.omx.exists()`
- pass one does not add `sdk.pluginState`; keep using `sdk.state`

## Logs

Plugin dispatch and plugin logs are written to:

- `.omx/logs/hooks-YYYY-MM-DD.jsonl`


# FILE: docs/release-notes-0.15.0.md

# Release notes — 0.15.0

## Summary

`0.15.0` prepares a minor release for the current `dev` train: first-party plugin delivery, Codex App compatibility, Visual Ralph, setup install-mode selection, native agent/model routing, hook/runtime hardening, Windows/tmux question reliability, CI hang protection, Rust compatibility, and release readiness collateral.

Range note: `v0.14.4` exists off the current `dev` ancestry and is not a valid reachable base for this candidate. Release comparison and readiness evidence therefore use `v0.14.3` as the verified reachable base, while keeping `0.14.4` release notes/readiness files as historical collateral.

## Highlights

- First-party Codex plugin packaging is now part of the release surface, including `plugins/oh-my-codex`, plugin descriptors, marketplace metadata, package layout tests, and mirror synchronization checks.
- Codex App compatibility paths avoid tmux-only runtime assumptions and preserve plugin-prefixed skill routing.
- Visual Ralph is available as a first-class workflow skill with routing, generated docs, and regression coverage.
- Setup can preserve plugin-vs-legacy install mode, report cleanup/backups clearly, and keep hooks/runtime assets aligned without overwriting local choices.
- **Launch behavior is explicit by default and operator-controllable:** the default launch path remains detached-tmux; use `omx --direct` or `OMX_LAUNCH_POLICY=direct` (or `=tmux`/`=detached-tmux`) to force the desired launch mode.
- Native agent and model-routing contracts are enforced across definitions, generated model tables, setup refresh paths, and runtime guidance.
- Hook/runtime hardening covers Stop-hook parseability, notification fallback watchers, derived watchers, stale tmux sockets, team worker identity, and CI silence protection.
- Windows/tmux question handling and Rust 1.73-compatible explore harness behavior are covered by targeted tests.

## Compatibility

- No user migration is required for existing legacy skill installs.
- Plugin-mode installs should use the bundled first-party plugin after the release owner publishes the package/release.
- Existing model overrides retain their semantics; generated defaults continue to prefer `gpt-5.5`, `gpt-5.4-mini`, and `gpt-5.3-codex-spark` for their respective lanes.
- No release tag or npm publication is performed as part of this preparation step.

## Verification

Release verification evidence is recorded in `docs/qa/release-readiness-0.15.0.md`.


# FILE: docs/release-notes-0.14.1.md

# Release notes — 0.14.1

## Summary

`0.14.1` is a patch release after `0.14.0` focused on reliability follow-through for the new interactive orchestration surfaces: deep-interview question enforcement, `omx question` tmux rendering, update/setup refresh behavior, stop/lifecycle normalization, and a smaller round of guidance/CI hardening.

## Highlights

- **Pending deep-interview question obligations now block Stop correctly** — even when the mode already marked itself inactive, OMX still treats the pending structured question as a blocking obligation.
- **Question panes are more resilient across tmux environments** — non-POSIX shells, missing panes, and detached-session startup failures now fail closed instead of silently leaving a dead question UI behind.
- **Setup refresh is easier to recover** — explicit `omx update` can refresh setup state even when the installed version is already current, and advisory update-state write failures no longer block the refresh path.
- **Lifecycle compatibility code is centralized** — terminal lifecycle helpers now reuse the shared runtime run-outcome contract instead of carrying a parallel normalization implementation.
- **Review/explore guidance stays aligned with current defaults** — the code-review skill is stronger, and lightweight fallback lanes remain intentionally lean.

## Fixed

- Deep-interview Stop gating around pending question obligations.
- Question renderer/session liveness and answer-submission reliability in tmux/Codex panes.
- Postinstall/setup refresh rooting and explicit-update stale-setup retry behavior.
- Stale Ralph / skill-active / ultrawork Stop leakage across sessions.
- Release metadata and lockfile synchronization to `0.14.1`.

## Verification evidence

Release verification evidence is recorded in `docs/qa/release-readiness-0.14.1.md`.

- `npm test` ✅
- `cargo test -p omx-explore-harness -p omx-sparkshell` ✅
- `npm pack --dry-run` ✅

## Remaining risk

- This is a local release-readiness pass rather than a full CI matrix rerun.
- The most valuable post-release observation surface remains real multi-session tmux/operator behavior around `omx question`, Stop gating, and upgraded-install setup refresh flows.


# FILE: docs/release-notes-0.8.6.md

# oh-my-codex v0.8.6

Released: 2026-03-07

4 non-merge commits from `main..dev`.
Contributor: [@Yeachan-Heo](https://github.com/Yeachan-Heo).

## Highlights

### Event-aware team waiting and runtime coordination

OMX team orchestration can now wait on canonical team events in addition to terminal completion.

This release adds:
- additive `wake_on=event` / `after_event_id` support to `omx_run_team_wait`
- shared event reading, normalization, and cursor helpers in the team state layer
- canonical event typing across contracts, runtime state, and API interop
- `omx team await <team-name>` CLI support
- runtime emission of `worker_state_changed` while preserving legacy `worker_idle` compatibility
- stronger visibility into notify-fallback watcher dispatch/drain progress and deferred leader state

PR: [#609](https://github.com/Yeachan-Heo/oh-my-codex/pull/609)

### GPT-5.4 prompt-guidance rollout and expansion

OMX's prompt and workflow surfaces were updated in two passes to better reflect OpenAI's GPT-5.4 prompt-guidance patterns.

Core-surface pass ([#611](https://github.com/Yeachan-Heo/oh-my-codex/pull/611), addresses [#608](https://github.com/Yeachan-Heo/oh-my-codex/issues/608)):
- root `AGENTS.md`
- `templates/AGENTS.md`
- `prompts/executor.md`
- `prompts/planner.md`
- `prompts/verifier.md`
- generated `developer_instructions` text in `src/config/generator.ts`
- focused regression coverage for prompt-contract expectations

Expansion pass ([#612](https://github.com/Yeachan-Heo/oh-my-codex/pull/612), follow-up to [#611](https://github.com/Yeachan-Heo/oh-my-codex/pull/611)):
- the broader agent prompt catalog (`analyst`, `architect`, `debugger`, `researcher`, `security-reviewer`, `writer`, and many more)
- execution-heavy skills including `analyze`, `autopilot`, `build-fix`, `code-review`, `plan`, `ralph`, `ralplan`, `security-review`, `team`, and `ultraqa`
- additional regression coverage for prompt catalogs, scenario examples, wave-two guidance, and skill guidance contracts

Behavioral emphasis now more explicitly covers:
- compact, information-dense output by default
- automatic follow-through on clear, low-risk, reversible next steps
- localized handling of mid-task user overrides
- continued tool usage when correctness depends on retrieval, diagnostics, or verification
- scenario-style examples that reinforce the intended execution contract across prompts and skills

## Bug fixes

### team-ops gateway contract restoration

A post-merge follow-up restored the intended public export surface for the `team-ops` gateway after the event-aware wait changes landed.

Fix: remove the accidental `teamEventLogPath` re-export so the strict `team-ops` module contract test remains stable.

PR: [#610](https://github.com/Yeachan-Heo/oh-my-codex/pull/610)

## Compare stats

- Commit window: **4 non-merge commits** (`2026-03-07`)
- Diff snapshot (`main...dev`): **69 files changed, +1,745 / -71**

## Full commit log (v0.8.5..v0.8.6)

```
9d3e2a2 fix(team): harden leader follow-up and event-aware waiting (#609)
c13290a fix(team): keep team-ops gateway contract stable (#610)
9d4b1ea feat: apply GPT-5.4 prompt-guidance patterns
76e3918 feat: expand GPT-5.4 prompt guidance across prompts and skills
```


# FILE: docs/release-notes-0.11.8.md

# Release notes — 0.11.8

## Summary

`0.11.8` is a hotfix release after `0.11.7` that disables all nudges while deep-interview state is active and hardens duplicate fresh-leader nudge prevention.

## Included fixes

- deep-interview state suppresses leader nudges, worker-idle nudges, Ralph continue-steers, and auto-nudges
- fallback watcher leader nudges remain stale-only instead of reacting to fresh mailbox activity
- notify-hook regression coverage now proves the same fresh mailbox message is not re-nudged on repeated runs
- release metadata is bumped to `0.11.8` across Node and Cargo packages

## Verification evidence

### Targeted regression suite

- `npm run build` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-hook-auto-nudge.test.js` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-hook-team-leader-nudge.test.js` ✅
- `node --test --test-reporter=spec dist/hooks/__tests__/notify-fallback-watcher.test.js` ✅

## Remaining risk

- The coverage is targeted at notify-hook and fallback-watcher nudge paths; broader runtime behavior still relies on the full suite and live tmux workflows.
- Future nudge entrypoints should reuse the same deep-interview suppression check to preserve this hotfix contract.


# FILE: docs/migration-mainline-post-v0.4.4.md

# Migration Guide: post-v0.4.4 mainline changes

This guide covers migration from **v0.4.4** to the current mainline changes merged after it (including PR #137 and follow-up fixes).

## Who is affected

You are affected if you:

- invoke removed prompts or skills from old notes/scripts,
- depend on pre-consolidation catalog names,
- use `omx setup` and need predictable install scope behavior,
- run `omx team`/tmux workflows and want the latest reliability fixes,
- use notifier output and need verbosity control.

## What changed (high level)

- Catalog consolidation for prompts/skills and cleanup of deprecated entries.
- `omx setup` now supports scope-aware install modes (`user`, `project`). Legacy `project-local` values are auto-migrated.
- Spark worker routing added for team workers (`--spark`, `--madmax-spark`).
- Notifier verbosity controls added.
- tmux runtime hardening updates landed, including post-review pane capture/input hardening.
- Stale references to removed `scientist`/`pipeline` were cleaned up.

## Removed prompts and skills

### Removed prompts

- `deep-executor`
- `scientist`

### Removed skills

- `deepinit`
- `learn-about-omx`
- `learner`
- `pipeline`
- `project-session-manager`
- `psm`
- `release`
- `ultrapilot`
- `writer-memory`

## Mapping old references to current ones

Use these replacements in docs, scripts, and personal shortcuts.

| Old reference | Use now | Notes |
|---|---|---|
| `/prompts:deep-executor` | `/prompts:executor` | `deep-executor` was a deprecated alias to executor behavior. |
| `/prompts:scientist` | `/prompts:researcher` | Use researcher for research-focused workflows in current catalog. |
| `$pipeline` | `$team` (or explicit `/prompts:*` sequencing) | Team is the default orchestrator pipeline surface. |
| `$ultrapilot` | `$team` | Use team-based parallel orchestration. |
| `$psm` / `$project-session-manager` | No in-repo replacement | Remove from automation or maintain out-of-tree tooling. |
| `$release` | No in-repo replacement | Use your project release process directly. |
| `$deepinit` | `omx agents-init [path]` | Lightweight CLI successor for AGENTS.md bootstrap only; immediate child directories only, unmanaged files preserved unless `--force`. |
| `$learn-about-omx` / `$learner` / `$writer-memory` | No in-repo replacement | Remove stale references from workflows/docs. |

## Verification checklist after upgrade

Run this checklist after pulling latest mainline:

- [ ] Confirm removed references are gone from local notes/scripts:
  ```bash
  rg -n "deep-executor|scientist|pipeline|project-session-manager|\bpsm\b|ultrapilot|learn-about-omx|writer-memory|learner|deepinit|\brelease\b" README.md docs scripts .omx -S
  ```
- [ ] Confirm current prompt catalog no longer contains removed prompts:
  ```bash
  ls prompts
  ```
- [ ] Confirm current skill catalog no longer contains removed skills:
  ```bash
  ls skills
  ```
- [ ] Validate setup scope options are available:
  ```bash
  omx help | rg -e "--scope|project"
  ```
- [ ] Validate team/tmux health checks:
  ```bash
  omx doctor --team
  ```
- [ ] If using spark worker routing, verify flags are available:
  ```bash
  omx --help | rg "spark|madmax-spark"
  ```

## Related docs

- Release notes: [CHANGELOG.md](../CHANGELOG.md)
- Main overview: [README.md](../README.md)


# FILE: docs/adapt.md

# `omx adapt`

`omx adapt <target>` is the OMX-owned surface for persistent external-agent adaptation.

Shared foundation behavior:

- CLI scaffold for `probe`, `status`, `init`, `envelope`, and `doctor`
- shared capability reporting with explicit ownership (`omx-owned`, `shared-contract`, `target-observed`)
- adapter-owned paths under `.omx/adapters/<target>/...`
- shared envelope/status/doctor/init behavior that does not touch `.omx/state/...`

OpenClaw follow-on behavior:

- `omx adapt openclaw probe` observes existing local OpenClaw config/env/gateway evidence
- `omx adapt openclaw status` synthesizes local adapter status from env gates, config source, hook mappings, and command-gateway opt-in
- `omx adapt openclaw envelope` includes lifecycle bridge metadata for the existing OMX to OpenClaw event mapping
- `omx adapt openclaw init --write` still writes only under `.omx/adapters/openclaw/...`

Current targets:

- `openclaw`
- `hermes`

Hermes follow-on behavior in this worktree:

- `probe` inspects external Hermes ACP, gateway, and session-store evidence
- `status` synthesizes `unavailable` / `installed` / `degraded` / `running` from observable Hermes files only
- `envelope` includes Hermes bootstrap metadata for ACP commands, lifecycle bridge guidance, and status commands
- `init --write` still writes only under `.omx/adapters/hermes/...`; Hermes runtime files remain read-only inputs

Examples:

```bash
omx adapt openclaw probe
omx adapt hermes status --json
omx adapt openclaw init --write
omx adapt hermes envelope --json
```

Foundation constraints:

- thin adapter surface only, not a bidirectional control plane
- no direct writes to `.omx/state/...`
- no direct writes to external runtime internals
- target capability reporting stays asymmetric; OMX reports what it owns, what is shared, and what is only target-observed
- OpenClaw status is local evidence only; it does not claim downstream runtime acknowledgement or execution
- command-gateway readiness still requires `OMX_OPENCLAW_COMMAND=1`

Hermes-specific evidence discovery uses `HERMES_HOME` plus an overrideable Hermes source root (`OMX_ADAPT_HERMES_ROOT`) so OMX can inspect an external runtime without vendoring or mutating it.


# FILE: docs/release-notes-0.16.3.md

# Release notes — 0.16.3

`0.16.3` is a post-`0.16.2` reliability release for Codex native-hook setup, Team/Ralph runtime state boundaries, approved handoff context, planning context-pack guidance, and release-review blocker fixes discovered before promotion.

## Highlights

- **Codex native-hook setup is aligned with the supported feature flag** — generated setup/runtime config now emits and migrates to `[features].hooks = true`, removes stale legacy `codex_hooks = true` aliases inside the features table, preserves user-owned hook state, and keeps project runtime `CODEX_HOME` hook trust pointed at the mirrored runtime `hooks.json`.
- **User-owned notification hooks are safer across setup/uninstall** — project setup with `notifyCommand: false` preserves non-OMX `notify` commands, managed notify detection no longer relies on basename-only matches, uninstall keeps user hook enablement intact, and Windows/global install hook commands avoid unsafe self-updates.
- **Team, planning, and approved handoffs are more durable** — approved handoff context is surfaced to workers, ready context-pack role references are exposed, symbolic Team launch signatures survive planning, role-agnostic approved hints are preserved, and Team startup-evidence tests now isolate local state roots from global OMX state.
- **Ralph/autoresearch/native compact hooks avoid stale or malformed lifecycle behavior** — stale Ralph sessions no longer auto-resume, blocked autoresearch Stop reconciliation is explicit, and PreCompact/PostCompact native hook output remains valid JSON.

## Fixes and compatibility notes

- Project-scope release review fixed hook trust placement and runtime mirror dedupe regressions from the `0.16.2` train.
- Notify-hook managed-CWD detection no longer treats bare stale `.omx/state` or `.omx/logs` directories as OMX-owned.
- Planning artifact reads and Team runtime state roots now prefer repository-local `.omx` paths unless an explicit Team state root is configured.
- The release keeps legacy cleanup/migration coverage for older unsupported hook aliases without documenting them as current setup guidance.

## Merged PR inventory

- [#2186](https://github.com/Yeachan-Heo/oh-my-codex/pull/2186) — fix: surface Codex startup exits
- [#2190](https://github.com/Yeachan-Heo/oh-my-codex/pull/2190) — Fix runtime hook mirror dedupe and hooks feature flag
- [#2191](https://github.com/Yeachan-Heo/oh-my-codex/pull/2191) — Fix Windows Codex hook command generation
- [#2196](https://github.com/Yeachan-Heo/oh-my-codex/pull/2196) — Fix notify setup scope handling
- [#2200](https://github.com/Yeachan-Heo/oh-my-codex/pull/2200) — fix: preserve user hook enablement on uninstall
- [#2199](https://github.com/Yeachan-Heo/oh-my-codex/pull/2199) — fix: dedupe managed hook trust state
- [#2201](https://github.com/Yeachan-Heo/oh-my-codex/pull/2201) — Fix hooks.json trust state placement
- [#2202](https://github.com/Yeachan-Heo/oh-my-codex/pull/2202) — fix(planning): preserve team launch signatures
- [#2203](https://github.com/Yeachan-Heo/oh-my-codex/pull/2203) — fix(team): preserve role-agnostic approved hints
- [#2204](https://github.com/Yeachan-Heo/oh-my-codex/pull/2204) — feat(planning): expose ready context-pack role refs
- [#2207](https://github.com/Yeachan-Heo/oh-my-codex/pull/2207) — Fix PostCompact native hook JSON output
- [#2208](https://github.com/Yeachan-Heo/oh-my-codex/pull/2208) — feat(team): add approved handoff context section
- [#2212](https://github.com/Yeachan-Heo/oh-my-codex/pull/2212) — Defer startup self-updates on Windows/global installs
- [#2213](https://github.com/Yeachan-Heo/oh-my-codex/pull/2213) — Fix autoresearch Stop reconciliation for blocked verdicts
- [#2216](https://github.com/Yeachan-Heo/oh-my-codex/pull/2216) — fix: migrate Codex hooks feature flag
- [#2217](https://github.com/Yeachan-Heo/oh-my-codex/pull/2217) — Fix PreCompact native hook JSON output
- [#2220](https://github.com/Yeachan-Heo/oh-my-codex/pull/2220) — Prevent stale Ralph sessions from auto-resuming
- Release-review fixes — exact supported hook feature flag generation, project notify preservation, runtime hook trust remapping, Team startup-evidence state-root isolation, and notify guard tightening.

## Validation

- Local release-review gates: `npm run build`, `npm run lint`, `npm run check:no-unused`, targeted setup/config/uninstall/hook/Team Node tests, and `git diff --check`.
- Release collateral generated from the `v0.16.2...v0.16.3` compare range and verified with `generate-release-body.js` before tagging.
- GitHub CI and publication evidence are recorded in `docs/qa/release-readiness-0.16.3.md`.

**Full Changelog**: [`v0.16.2...v0.16.3`](https://github.com/Yeachan-Heo/oh-my-codex/compare/v0.16.2...v0.16.3)


# FILE: docs/release-notes-0.8.2.md

# oh-my-codex v0.8.2

Released: **2026-03-06**

This is a **targeted patch release** focused on team-provider expansion, safer defaults, setup hygiene, and correctness fixes across setup, keyword handling, and OpenClaw hook templating.

---

## TL;DR

- `$team` / team runtime can now launch **Gemini CLI workers** alongside Codex and Claude (`#576`, `#579`, related issue `#573`).
- Default frontier-model fallback is now routed through **`DEFAULT_FRONTIER_MODEL`** instead of hardcoded model strings (`#583`).
- Setup/install is stricter about shipping only the right skills, now ships **`configure-notifications`** canonically, and cleans stale legacy skill dirs on `--force` (`#575`, `#580`, `#584`, closes `#574`).
- `omx setup` now skips the deprecated **`[tui]`** config section for Codex CLI `>= 0.107.0` (`#572`, fixes `#564`).
- Fixed two additional patch-level bugs: unresolved OpenClaw placeholders (`#581`, closes `#578`) and keyword detection ordering/`/prompts` guarding (`#582`).

---

## What changed

### 1) Team mode: Gemini CLI worker support

OMX team mode now supports **Gemini** as a worker CLI provider in addition to Codex and Claude.

Included in this update:
- Gemini worker launch support in runtime/session resolution
- mixed CLI maps with Codex / Claude / Gemini workers
- `--model` passthrough support for Gemini workers
- expanded runtime and tmux-session coverage for Gemini worker behavior

**Why this matters:**
- more flexibility for mixed-provider teams
- easier experimentation with provider-specific worker roles
- better parity across the team orchestration surface

### 2) Model fallback defaults are now centralized

Hardcoded default frontier-model fallback references were replaced with `DEFAULT_FRONTIER_MODEL`.

Current behavior from this release:
- default frontier fallback now resolves through a single constant
- that constant is currently set to **`gpt-5.5`**
- low-complexity spark default remains **`gpt-5.3-codex-spark`**

**Why this matters:**
- fewer hidden fallback mismatches
- easier future model updates
- cleaner test and config semantics

### 3) Setup/install behavior is cleaner and safer

Setup now respects the catalog manifest and current Codex compatibility more strictly:
- installs only `active` / `internal` skills
- canonically ships `configure-notifications`
- skips deprecated / merged / alias entries
- removes stale shipped / legacy notification skill directories during `--force` cleanup
- skips writing the deprecated `[tui]` section when Codex CLI is `>= 0.107.0`

**Why this matters:**
- cleaner installs and upgrades
- fewer stale shipped assets after upgrades
- fewer setup/config issues on newer Codex CLI versions
- lower chance of confusing doctor/setup results

### 4) Patch fixes

Two additional correctness fixes landed in this release:

- **OpenClaw template safety:** unresolved placeholders in hook instruction templates now fall back safely instead of leaking literal placeholders into instructions (`#581`, closes `#578`).
- **Keyword detection hardening:** explicit multi-skill order is preserved left-to-right, missing keyword aliases were restored, and direct `/prompts:<name>` invocations are protected from unintended implicit keyword activation (`#582`).

---

## Related PRs and issues

### Merged PRs in this release
- #584 — fix(setup): canonicalize `configure-notifications` skill
- #583 — feat: use `DEFAULT_FRONTIER_MODEL` for default model fallback
- #582 — fix(keyword): explicit multi-skill order + `/prompts` guard hardening
- #581 — fix(openclaw): prevent unresolved placeholder leakage in hook instruction templates
- #580 — fix(setup): skip non-installable skills and cleanup stale shipped dirs
- #579 — feat(team): add Gemini CLI worker support
- #576 — feat(team): add Gemini CLI worker support (`#573`)
- #575 — fix: setup skips deprecated/merged/alias catalog skills
- #572 — fix(setup): skip `[tui]` section for Codex >= `0.107.0`
- #571 — docs: improve OpenClaw gateway configuration examples

### Related issues tagged in this release
- #564 — setup/config breakage caused by deprecated `[tui]` generation on newer Codex CLI versions
- #573 — feat(team): add Gemini CLI worker support to OMX team mode
- #574 — setup should skip non-installable catalog skills and clean stale shipped dirs
- #578 — unresolved placeholder leakage in OpenClaw hook instruction templates

---

## Scope and commit window

Release scope was prepared from non-merge commits in:
- `v0.8.1..main`

Snapshot at preparation time:
- **15 non-merge commits** (`2026-03-05` to `2026-03-06`)
- **70 files changed** (`+2,300 / -243`)

---

## Verification summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.2.md`.

Release gates for the final `main` release candidate:
- `npm run build`
- `npm test`
- `npm run check:no-unused`
- CLI smoke checks (`--help`, `version`, `status`, `doctor`, `setup --dry-run`, `cancel`)

---

Thanks for using **oh-my-codex**. If anything regresses, please open an issue with reproduction steps, logs, and your CLI/runtime details.


# FILE: docs/release-notes-0.16.2.md

# Release notes — 0.16.2

`0.16.2` is a post-`0.16.1` release-train correction and workflow hardening release. It ships the major `$ultragoal` aggregate-goal amendments, commit-shared wiki/compaction support, state isolation fixes, and the Codex native-hook setup corrections found during release review.

## Highlights

- **`$ultragoal` now defaults to aggregate Codex goals** — new plans use one aggregate Codex objective while OMX tracks per-story `G001`/`G002` checkpoints. Existing/no-mode plans keep legacy per-story behavior, and explicit `--codex-goal-mode per-story` remains supported. Planning, ralplan, deep-interview, plugin-skill mirrors, help text, and docs now point users toward `$ultragoal` as the default goal-mode follow-up. ([#2188](https://github.com/Yeachan-Heo/oh-my-codex/pull/2188))
- **Project wiki pages are now commit-shared** — canonical wiki storage moved to repository-root `omx_wiki/`, with legacy `.omx/wiki/` retained as a read-only fallback. Native `PreCompact`/`PostCompact` hooks now preserve and promote durable compaction findings into the shared wiki surface. ([#2180](https://github.com/Yeachan-Heo/oh-my-codex/pull/2180))
- **Stateful workflows are isolated by OMX session** — session-scoped workflow state no longer inherits or autocompletes from root/global state, and explicit `all_sessions` cleanup remains the global reset path. ([#2193](https://github.com/Yeachan-Heo/oh-my-codex/pull/2193))

## Codex native hooks and setup

- Added Codex-compatible trust-state generation for setup-owned `codex-native-hook.js` wrappers so generated hooks can be trusted without manual `/hooks` review, while user hook entries and user-owned hook state remain preserved. ([#2194](https://github.com/Yeachan-Heo/oh-my-codex/pull/2194))
- Updated the hook feature-flag migration so generated setup config uses the Codex CLI 0.130 lifecycle-hook flag, `[features].codex_hooks = true`.
- Migrates unsupported `[features].hooks = true` entries back to `codex_hooks` during setup, while retaining legacy cleanup detection for older configs.

## Merged PR inventory

- [#2174](https://github.com/Yeachan-Heo/oh-my-codex/pull/2174) — fix: use supported Codex hooks feature flag
- [#2188](https://github.com/Yeachan-Heo/oh-my-codex/pull/2188) — Default ultragoal to aggregate Codex goals
- [#2180](https://github.com/Yeachan-Heo/oh-my-codex/pull/2180) — Make OMX wiki commit-shared and add compact hooks
- [#2194](https://github.com/Yeachan-Heo/oh-my-codex/pull/2194) — Trust setup-owned Codex hooks during setup
- [#2193](https://github.com/Yeachan-Heo/oh-my-codex/pull/2193) — Fix stateful workflow session isolation

## Validation

- Local release-review gates: `npm run build`, `npm run check:no-unused`, targeted setup/config/uninstall/hook Node tests, `npm run verify:native-agents`, `npm run verify:plugin-bundle`, catalog-doc check, and `cargo test`.
- Changed-area PR gates included targeted `$ultragoal`, wiki/MCP/storage, state/session, native-hook, setup, lint, no-unused, and plugin-bundle checks.
- GitHub CI passed on `dev` and `main`; the tag release workflow passed native builds, release-asset publishing, smoke verification, packed global install smoke, and npm publish.

**Full Changelog**: [`v0.16.1...v0.16.2`](https://github.com/Yeachan-Heo/oh-my-codex/compare/v0.16.1...v0.16.2)


# FILE: docs/release-notes-0.8.3.md

# oh-my-codex v0.8.3

Released: **2026-03-06**

This is a **focused hotfix release** for the Gemini team-worker path shipped in the `0.8.2` dev release line.

---

## TL;DR

- Fixes Gemini worker startup in team prompt mode by launching workers with `--approval-mode yolo -i "<initial inbox prompt>"` instead of depending on stdin for the first instruction (`#585`).
- Prevents non-Gemini default models such as `gpt-5.3-codex-spark` from being passed through to Gemini workers unless the configured model is explicitly a Gemini model (`#585`).
- Adds targeted runtime and tmux-session regression coverage for the Gemini prompt-launch path (`#585`).
- Includes a small test-only hardening for the notify-fallback watcher so full-suite release validation remains stable under load.

---

## What changed

### 1) Gemini prompt-mode workers now start with an explicit initial prompt

Gemini workers launched through OMX team prompt mode are now started with an explicit initial instruction:

- `--approval-mode yolo`
- `-i "Read and follow the instructions in .../inbox.md"`

**Why this matters:**
- removes dependence on stdin-delivered bootstrap text for Gemini startup
- aligns worker bootstrap with Gemini CLI expectations in prompt mode
- fixes the broken worker bring-up path reported in the hotfix PR

### 2) Non-Gemini default model passthrough is filtered for Gemini workers

Gemini workers no longer inherit non-Gemini default models by accident.

Current behavior from this release:
- explicit Gemini models still pass through
- non-Gemini defaults are omitted for Gemini workers
- mixed-provider team configs avoid invalid startup argument combinations

**Why this matters:**
- prevents invalid provider/model pairings during worker launch
- preserves cleaner mixed-provider CLI interoperability
- reduces surprising failures in prompt-mode and mapped-worker setups

### 3) Regression coverage was expanded for the hotfix path

This release adds focused tests covering:
- prompt-mode Gemini startup argument construction
- runtime startup behavior for prompt-launched Gemini workers
- translation behavior when default models are non-Gemini

### 4) Full-suite verification was stabilized

Release validation also hardened a flaky watcher test so the full suite reliably waits for watcher readiness before asserting streaming EOF-tail behavior.

**Why this matters:**
- keeps release verification deterministic under heavy suite load
- preserves the intended watcher behavior instead of relying on fixed sleeps
- does not change shipped Gemini runtime behavior

---

## Related PRs and issues

### Merged PRs in this release
- #585 — fix(team): seed gemini workers with prompt-interactive launch

### Scope note
- Functional release scope is centered on PR `#585`, the Gemini worker startup hotfix after the `0.8.2` dev release line.
- Release validation also includes a small test-only stabilization in `src/hooks/__tests__/notify-fallback-watcher.test.ts` so the full suite remains reliable under load.
- Final tracked change set for the release branch: `package.json`, `package-lock.json`, `CHANGELOG.md`, and the watcher test hardening.

---

## Verification summary

Release verification evidence is recorded in `docs/qa/release-readiness-0.8.3.md`.

Planned release gates:
- `npm run build`
- `npm test`
- `npm run check:no-unused`
- CLI smoke checks (`--help`, `version`, `status`, `doctor`, `setup --dry-run`, `cancel`)
- Gemini-targeted regression checks from PR `#585`

---

Thanks for using **oh-my-codex**. If anything regresses, please open an issue with reproduction steps, logs, and your CLI/runtime details.


# FILE: docs/release-notes-0.14.4.md

# Release notes — 0.14.4

## Summary

`0.14.4` is a patch release after `0.14.3` that promotes the default frontier lane from `gpt-5.4` to `gpt-5.5` while intentionally preserving the exact `gpt-5.4-mini` standard/mini seam and the `gpt-5.3-codex-spark` spark lane.

## Highlights

- Runtime defaults, Codex agent defaults, and `omx explore` fallback behavior now resolve the frontier lane to `gpt-5.5`. Setup and setup and executor worker reasoning defaults now use medium instead of high.
- Setup/config seeding docs and regression coverage now describe `gpt-5.5` with the existing `model_context_window = 250000` and `model_auto_compact_token_limit = 200000` recommendations.
- Exact-match `gpt-5.4-mini` behavior remains unchanged.
- Spark defaults remain on `gpt-5.3-codex-spark`.
- Release/package metadata is aligned for the `0.14.4` cut.

## Compatibility

- No user migration is required.
- Existing `gpt-5.4-mini` and `gpt-5.3-codex-spark` overrides keep their current semantics.
- Fresh/default frontier-managed config paths now prefer `gpt-5.5`.

## Verification

- `npm run build` ✅
- Targeted Node suites for model/default changes ✅
- `npm run lint`, `npm run check:no-unused`, and `cargo test --workspace` passed earlier on this branch ✅
- Full `npm test` was intentionally not rerun after the final fast-path executor reasoning tweak.

Release verification evidence is recorded in `docs/qa/release-readiness-0.14.4.md`.

