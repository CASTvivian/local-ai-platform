# Missing Repo Summary Source: steipete/CodexBar

- URL: https://github.com/steipete/CodexBar
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/steipete__CodexBar
- Clone Status: cloned
- Language: Swift
- Stars: 12076
- Topics: ai, claude-code, codex, swift
- Description: Show usage stats for OpenAI Codex and Claude Code, without having to login.

## Extracted README / Docs / Examples



# FILE: README.md

# CodexBar 🎚️ — May your tokens never run out.

> Every AI coding limit, in your menu bar.

[![Latest release](https://img.shields.io/github/v/release/steipete/CodexBar?style=flat-square&color=0a0a0c)](https://github.com/steipete/CodexBar/releases/latest)
[![macOS 14+](https://img.shields.io/badge/macOS-14%2B-0a0a0c?style=flat-square)](https://github.com/steipete/CodexBar/releases/latest)
[![Homebrew](https://img.shields.io/badge/brew-steipete%2Ftap%2Fcodexbar-orange?style=flat-square)](https://github.com/steipete/homebrew-tap)
[![License: MIT](https://img.shields.io/badge/license-MIT-6e5aff?style=flat-square)](LICENSE)
[![Site](https://img.shields.io/badge/site-codexbar.app-16d3b4?style=flat-square)](https://codexbar.app)

<a href="https://codexbar.app"><img src="docs/social.png" alt="CodexBar — every AI coding limit in your menu bar. 29 providers." width="100%" /></a>

Tiny macOS 14+ menu bar app that keeps **AI coding-provider limits visible** and shows when each window resets. Codex, Claude, Cursor, Gemini, Copilot, z.ai, Kiro, Vertex AI, Augment, OpenRouter, Codebuff, Command Code, and many newer coding providers. One status item per provider, or Merge Icons mode with a provider switcher. No Dock icon, minimal UI, dynamic bar icons.

<img src="codexbar.png" alt="CodexBar menu popover with provider tiles, usage bars, and reset countdowns" width="520" />

## Why

- **Plan around resets.** Per-provider session, weekly, and monthly windows with countdowns to the next reset — stop guessing whether to start that long task.
- **Credits, spend, and cost scans.** Credit balances and monthly spend where the provider exposes them, plus a local cost scan over the last 30 days for Codex and Claude.
- **Live status.** Provider status polling surfaces incident badges in the menu and an indicator overlay on the bar icon.
- **Privacy-first.** Reuses existing provider sessions — OAuth, device flow, API keys, browser cookies, local files — so no passwords are stored.

## Install

### Requirements
- macOS 14+ (Sonoma)

### GitHub Releases
Download: <https://github.com/steipete/CodexBar/releases>

### Homebrew
```bash
brew install --cask steipete/tap/codexbar
```

### CLI Tarballs (macOS/Linux)
Homebrew formula (Linux today):
```bash
brew install steipete/tap/codexbar
```
Or download release tarballs from GitHub Releases:
- macOS: `CodexBarCLI-v<tag>-macos-arm64.tar.gz`, `CodexBarCLI-v<tag>-macos-x86_64.tar.gz`
- Linux: `CodexBarCLI-v<tag>-linux-aarch64.tar.gz`, `CodexBarCLI-v<tag>-linux-x86_64.tar.gz`

### First run
- Open Settings → Providers and enable what you use.
- Install/sign in to the provider sources you rely on: CLIs, browser sessions, OAuth/device flow, API keys, local app files, or provider apps depending on the provider.
- Optional: Settings → Providers → Codex → OpenAI cookies (Automatic or Manual) to add dashboard extras.

## Providers

- [Codex](docs/codex.md) — OAuth API or local Codex CLI, plus optional OpenAI web dashboard extras.
- [Claude](docs/claude.md) — OAuth API, browser cookies, or CLI PTY fallback; session and weekly usage where available.
- [Cursor](docs/cursor.md) — Browser session cookies for plan + usage + billing resets.
- [OpenCode](docs/opencode.md) — Browser cookies for workspace subscription usage.
- [OpenCode Go](docs/opencode.md) — Browser cookies for Go usage windows.
- [Alibaba Coding Plan](docs/alibaba-coding-plan.md) — Web cookies or API key for coding-plan quotas.
- [Gemini](docs/gemini.md) — OAuth-backed quota API using Gemini CLI credentials (no browser cookies).
- [Antigravity](docs/antigravity.md) — Local language server probe (experimental); no external auth.
- [Droid](docs/factory.md) — Browser cookies + WorkOS token flows for Factory usage + billing.
- [Copilot](docs/copilot.md) — GitHub device flow + Copilot internal usage API.
- [z.ai](docs/zai.md) — API token for quota + MCP windows.
- [Manus](docs/manus.md) — Browser `session_id` auth for credit balance, monthly credits, and daily refresh tracking.
- [MiniMax](docs/minimax.md) — API token, cookie header, or browser cookies for coding-plan usage.
- [Kimi](docs/kimi.md) — Auth token (JWT from `kimi-auth` cookie) for weekly quota + 5‑hour rate limit.
- [Kimi K2](docs/kimi-k2.md) — API key for credit-based usage totals.
- [Kilo](docs/kilo.md) — API token with CLI-auth fallback for Kilo Pass usage.
- [Kiro](docs/kiro.md) — CLI-based usage; monthly credits + bonus credits.
- [Vertex AI](docs/vertexai.md) — Google Cloud gcloud OAuth with token cost tracking from local Claude logs.
- [Augment](docs/augment.md) — Augment CLI or browser cookies for credits tracking and usage monitoring.
- [Amp](docs/amp.md) — Browser cookie-based authentication with Amp Free usage tracking.
- [Ollama](docs/ollama.md) — Browser cookies for Ollama Cloud usage windows.
- [JetBrains AI](docs/jetbrains.md) — Local XML-based quota from JetBrains IDE configuration; monthly credits tracking.
- [Warp](docs/warp.md) — API token for GraphQL request limits and monthly credits.
- [OpenRouter](docs/openrouter.md) — API token for credit-based usage tracking across multiple AI providers.
- Perplexity — Account usage credits from Perplexity usage data.
- [Abacus AI](docs/abacus.md) — Browser cookie auth for ChatLLM/RouteLLM compute credit tracking.
- Mistral — Browser cookies for monthly spend tracking.
- [DeepSeek](docs/deepseek.md) — API key for credit balance tracking (paid vs. granted breakdown).
- [Moonshot / Kimi API](docs/moonshot.md) — API key for Moonshot/Kimi API account balance tracking.
- [Venice](docs/venice.md) — API key for DIEM or USD balance tracking.
- [Codebuff](docs/codebuff.md) — API token (or `~/.config/manicode/credentials.json`) for credit balance + weekly rate limit.
- [Crof](docs/crof.md) — API key for dollar credit balance and request quota tracking.
- [Command Code](docs/command-code.md) — Browser cookies for monthly USD credits from Command Code billing.
- [StepFun](docs/stepfun.md) — Username + password login for Step Plan rate limits (5‑hour + weekly windows) and subscription plan name.
- Open to new providers: [provider authoring guide](docs/provider.md).

## Icon & Screenshot
The menu bar icon is a tiny usage meter. Bar meaning is provider-specific, and errors/stale data can dim the icon or
show an incident indicator.

## Features
- Multi-provider menu bar with per-provider toggles (Settings → Providers).
- Provider-specific usage meters with reset countdowns.
- Optional Codex web dashboard enrichments (code review remaining, usage breakdown, credits history).
- Local cost-usage scan for Codex + Claude (last 30 days).
- Provider status polling with incident badges in the menu and icon overlay.
- Merge Icons mode to combine providers into one status item + switcher.
- Display controls for provider icons, labels, bars, reset-time style, and highest-usage auto-selection.
- Refresh cadence presets (manual, 1m, 2m, 5m, 15m).
- Bundled CLI (`codexbar`) for scripts and CI (including `codexbar cost --provider codex`, `claude`, or `both` for local cost usage); macOS and Linux CLI builds available.
- WidgetKit widgets for supported providers.
- Optional session quota notifications and weekly-reset confetti.
- Privacy-first: on-device parsing by default; browser cookies are opt-in and reused (no passwords stored).

## Privacy note
Wondering if CodexBar scans your disk? It doesn’t crawl your filesystem; it reads a small set of known locations (browser cookies/local storage, provider config files, local JSONL logs) when the related features are enabled. Provider tokens and token-account settings live in `~/.codexbar/config.json` with restrictive file permissions. See the discussion and audit notes in [issue #12](https://github.com/steipete/CodexBar/issues/12).

## macOS permissions (why they’re needed)
- **Full Disk Access (optional)**: only required to read Safari cookies/local storage for web-based providers. If you don’t grant it, use another supported browser, manual cookies/API keys, OAuth, or CLI/local sources where that provider supports them.
- **Keychain access (prompted by macOS)**:
  - Chromium cookie import needs the browser “Safe Storage” key to decrypt cookies.
  - Claude OAuth bootstrap may read the Claude CLI Keychain item when CodexBar has no usable cached credentials.
  - CodexBar may use Keychain for browser cookie decryption, cached cookie headers, and OAuth/device-flow credentials where those sources require it.
  - **How do I prevent those keychain alerts?**
    - Open **Keychain Access.app** → login keychain → search the prompted item (for Claude OAuth, usually “Claude Code-credentials”).
    - Open the item → **Access Control** → add `CodexBar.app` under “Always allow access by these applications”.
    - Prefer adding just CodexBar (avoid “Allow all applications” unless you want it wide open).
    - Relaunch CodexBar after saving.
    - Reference screenshot: ![Keychain access control](docs/keychain-allow.png)
  - **How to do the same for the browser?**
    - Find the browser’s “Safe Storage” key (e.g., “Chrome Safe Storage”, “Brave Safe Storage”, “Microsoft Edge Safe Storage”).
    - Open the item → **Access Control** → add `CodexBar.app` under “Always allow access by these applications”.
    - This removes the prompt when CodexBar decrypts cookies for that browser.
- **Files & Folders prompts (folder/volume access)**: CodexBar launches provider CLIs and local probes for some providers. If those helpers read a project directory or external drive, macOS may ask CodexBar for that folder/volume (e.g., Desktop or an external volume). This is driven by the helper’s working directory, not background disk scanning.
- **What we do not request in the background**: no Screen Recording or Accessibility permissions; user-triggered helper actions may ask macOS for Automation permission to open Terminal. No passwords are stored (browser cookies are reused when you opt in).

## Docs
- Providers overview: [docs/providers.md](docs/provi

# FILE: docs/deepseek.md

---
summary: "DeepSeek provider data sources: API key + balance endpoint."
read_when:
  - Adding or tweaking DeepSeek balance parsing
  - Updating API key handling
  - Documenting new provider behavior
---

# DeepSeek provider

DeepSeek is API-only. Balance is reported by `GET https://api.deepseek.com/user/balance`,
so CodexBar only needs a valid API key to show your remaining credit balance.

## Data sources

1. **API key** supplied via `DEEPSEEK_API_KEY` / `DEEPSEEK_KEY`, or selected from DeepSeek token accounts in `~/.codexbar/config.json`.
2. **Balance endpoint**
   - `GET https://api.deepseek.com/user/balance`
   - Request headers: `Authorization: Bearer <api key>`, `Accept: application/json`
   - Response contains `is_available`, and a `balance_infos` array with per-currency entries
     (`total_balance`, `granted_balance`, `topped_up_balance`).

## Usage details

- The menu card shows total balance with the paid vs. granted breakdown:
  e.g. `$50.00 (Paid: $40.00 / Granted: $10.00)`.
- The API separates granted balance from topped-up balance; CodexBar labels these as granted vs. paid credit.
- When multiple currencies are present, USD is shown preferentially.
- If total balance is zero, CodexBar shows an add-credits message. If balance is nonzero but `is_available` is false, it shows "Balance unavailable for API calls".
- There is no session or weekly window — DeepSeek does not expose per-window quota via API.
- Token-account selection injects the selected key into the fetch environment; otherwise CodexBar reads `DEEPSEEK_API_KEY` / `DEEPSEEK_KEY`.

## Key files

- `Sources/CodexBarCore/Providers/DeepSeek/DeepSeekProviderDescriptor.swift` (descriptor + fetch strategy)
- `Sources/CodexBarCore/Providers/DeepSeek/DeepSeekUsageFetcher.swift` (HTTP client + JSON parser)
- `Sources/CodexBarCore/Providers/DeepSeek/DeepSeekSettingsReader.swift` (env var resolution)
- `Sources/CodexBar/Providers/DeepSeek/DeepSeekProviderImplementation.swift` (provider activation and token-account visibility)
- `Sources/CodexBarCore/TokenAccountSupportCatalog+Data.swift` (DeepSeek token-account injection)


# FILE: docs/perf-energy-issue-139-main-fix-validation-2026-02-19.md

# CodexBar Issue #139 Main Fix Validation (Post-Fix vs Pre-Fix)

Date: 2026-02-19
Workspace: /Users/michalkrsik/windsurf_project_folder/CodexBar
Branch: codex/perf-issue-139

Reference pre-fix report:
- /Users/michalkrsik/windsurf_project_folder/CodexBar/docs/perf-energy-issue-139-simulation-report-2026-02-19.md

## Implemented Main Fix

File changed:
- /Users/michalkrsik/windsurf_project_folder/CodexBar/Sources/CodexBarCore/Providers/Codex/CodexStatusProbe.swift

Behavior change:
- Primary Codex PTY probe timeout reduced from 18s to 8s.
- Retry policy changed from `retry on parseFailed OR timedOut` to `retry only on parseFailed`.
- Parse retry timeout set to 4s.
- Timed-out runs now fail fast and wait for next scheduled refresh.

## Post-Fix Validation Method

Target: main culprit path (Codex CLI failure path).

Practical simulation used:
- `CODEX_CLI_PATH` pointed to a fake codex script.
- Script behavior:
  - exits immediately for `app-server` args (forces RPC failure/fallback path),
  - otherwise busy-loops with no `/status` output (simulates heavy stuck CLI PTY behavior).
- Command run (3 times):
  - `./.build/debug/CodexBarCLI usage --provider codex --source cli --format json --pretty`
- Collected:
  - wall time (`/usr/bin/time -p`),
  - sampled child CPU every 0.5s,
  - leftover child-process count after run.

Artifacts:
- /tmp/codexbar_main_fix_validation_after

## Post-Fix Results (3 runs)

| Run | Real (s) | Avg child CPU (%) | Max child CPU (%) | Remaining child procs |
|---|---:|---:|---:|---:|
| 1 | 12.76 | 88.32 | 100.00 | 0 |
| 2 | 12.67 | 89.79 | 100.00 | 0 |
| 3 | 12.59 | 89.90 | 100.00 | 0 |
| Mean | 12.67 | 89.34 | 100.00 | 0 |

## Side-by-Side Comparison Against Stored Pre-Fix Report

Pre-fix values are from the stored report's Culprit A simulation summary.
Post-fix values are from the validation above.

| Metric | Pre-fix (stored report) | Post-fix (this validation) | Delta |
|---|---:|---:|---:|
| Failed-run duration (worst-case path) | 42.00s (code-path budget before fix) | 12.67s (measured mean) | -69.8% |
| Child CPU during failed run | 113.32% avg | 89.34% avg | -21.2% |
| Peak child CPU during failed run | 115.90% max | 100.00% max | -13.7% |
| Remaining child processes after failure | not captured in pre-fix report | 0 | improved |

Derived CPU-time exposure index (avg CPU * duration):
- Pre-fix: `113.32 * 42.00 = 4759.44`
- Post-fix: `89.34 * 12.67 = 1132.94`
- Reduction: **-76.2%**

## Conclusion

The implemented main fix materially reduces the failure-path runtime and overall CPU exposure.
The heavy CLI process can still spike CPU while active, but it now lives for a much shorter window and is cleaned up after failure.


# FILE: docs/codebuff.md

---
summary: "Codebuff provider data sources: API token, CLI credentials file, credit balance, and weekly rate limits."
read_when:
  - Debugging Codebuff credential resolution or usage parsing
  - Updating Codebuff credit balance or weekly rate-limit display
  - Adjusting Codebuff provider UI/menu behavior
---

# Codebuff

CodexBar surfaces [Codebuff](https://www.codebuff.com) credit balance and
weekly rate limits next to your other AI providers.

## Data sources

- `POST https://www.codebuff.com/api/v1/usage` — current credit usage,
  remaining balance, auto top-up state, and the next quota reset date.
- `GET  https://www.codebuff.com/api/user/subscription` — subscription tier,
  billing period end, and the weekly rate-limit window (`weeklyUsed` /
  `weeklyLimit`) when CodexBar is using the CLI credentials-file session token.

Both endpoints use a Bearer token. Codebuff credentials come from the
environment, the normal CodexBar config file, or the official CLI credentials
file; the Codebuff provider does not write a separate Keychain credential.

## Authentication

CodexBar resolves the Codebuff API token in this order:

1. `CODEBUFF_API_KEY` environment variable (takes precedence so CI overrides
   work). API-key tokens fetch credit balance only.
2. The per-provider API key stored in Settings → Providers → Codebuff (saved
   in `~/.codexbar/config.json` via the normal CodexBar config flow). API-key
   tokens fetch credit balance only.
3. `~/.config/manicode/credentials.json` — the file the official `codebuff`
   CLI (formerly `manicode`) writes after `codebuff login`. CodexBar reads
   `default.authToken`, falling back to top-level `authToken`, and uses that
   session token for both credit balance and subscription metadata.

If none of those is available, Codebuff shows the “missing token” error.

## Credit window mapping

- **Primary row** — credit balance (`usage / quota`), with the "next quota
  reset" date if provided.
- **Secondary row** — weekly rate-limit window (`weeklyUsed / weeklyLimit`)
  shown with a 7-day window.

The account panel shows the Codebuff tier (e.g. "Pro"), remaining balance,
and whether auto top-up is enabled.

## Troubleshooting

- Run `codebuff login` to refresh `~/.config/manicode/credentials.json`.
- Override the API base with `CODEBUFF_API_URL` for staging environments.
- Verify your token works manually:

  ```sh
  curl -s -X POST -H "Authorization: Bearer $CODEBUFF_API_KEY" \
    -H 'Content-Type: application/json' -d '{"fingerprintId":"codexbar-usage"}' \
    https://www.codebuff.com/api/v1/usage
  ```

## Related files

- `Sources/CodexBarCore/Providers/Codebuff/` — descriptor, fetcher, snapshot,
  settings reader, error types.
- `Sources/CodexBar/Providers/Codebuff/` — settings store bridge + macOS
  settings pane implementation.
- `Tests/CodexBarTests/CodebuffSettingsReaderTests.swift`,
  `CodebuffUsageFetcherTests.swift`, and the Codebuff extensions in
  `ProviderTokenResolverTests.swift`.


# FILE: docs/kiro.md

---
summary: "Kiro provider data sources: CLI-based usage via kiro-cli /usage command."
read_when:
  - Debugging Kiro usage parsing
  - Updating kiro-cli command behavior
  - Reviewing Kiro credit window mapping
---

# Kiro provider

Kiro uses the AWS `kiro-cli` tool to fetch usage data. No browser cookies or OAuth flow—authentication is handled by AWS Builder ID through the CLI.

## Data sources

1) **CLI command** (primary and only strategy)
   - Command: `kiro-cli chat --no-interactive "/usage"`
   - Timeout: 20 seconds (idle cutoff after ~10s of no output once the CLI starts responding).
   - Requires `kiro-cli` installed and logged in via AWS Builder ID.
   - Output is ANSI-decorated; CodexBar strips escape sequences before parsing.

## Output format (example)

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                          | KIRO FREE      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃ Monthly credits:                                                          ┃
┃ ████████████████████████████████████████████████████████ 100% (resets on 01/01) ┃
┃                              (0.00 of 50 covered in plan)                 ┃
┃ Bonus credits:                                                            ┃
┃ 0.00/100 credits used, expires in 88 days                                 ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

## Snapshot mapping

- **Primary window**: Monthly credits percentage (bar meter).
  - `usedPercent`: extracted from `███...█ X%` pattern.
  - `resetsAt`: parsed from `resets on MM/DD` (assumes current or next year).
- **Secondary window**: Bonus credits (when present).
  - Parsed from `Bonus credits: X.XX/Y credits used`.
  - Expiry from `expires in N days`.
- **Identity**:
  - `accountOrganization`: plan name (e.g., "KIRO FREE").
  - `loginMethod`: plan name (used for menu display).

## Status

Kiro does not have a dedicated status page. The "View Status" link opens the AWS Health Dashboard:
- `https://health.aws.amazon.com/health/status`

## Key files

- `Sources/CodexBarCore/Providers/Kiro/KiroProviderDescriptor.swift`
- `Sources/CodexBarCore/Providers/Kiro/KiroStatusProbe.swift`
- `Sources/CodexBar/Providers/Kiro/KiroProviderImplementation.swift`


# FILE: docs/warp.md

---
summary: "Warp provider notes: API token setup and request limit parsing."
read_when:
  - Adding or modifying the Warp provider
  - Debugging Warp API tokens or request limits
  - Adjusting Warp usage labels or reset behavior
---

# Warp Provider

The Warp provider reads credit limits from Warp's GraphQL API using an API token.

## Features

- **Monthly credits usage**: Shows credits used vs. plan limit.
- **Reset timing**: Displays the next refresh time when available.
- **Token-based auth**: Uses API key stored in Settings or env vars.

## Setup

1. Open **Settings → Providers**
2. Enable **Warp**
3. In Warp, open your profile menu → **Settings → Platform → API Keys**, then create a key.
4. Enter the created `wk-...` key in CodexBar.

Reference guide: `https://docs.warp.dev/reference/cli/api-keys`

### Environment variables (optional)

- `WARP_API_KEY`
- `WARP_TOKEN`

## How it works

- Endpoint: `https://app.warp.dev/graphql/v2?op=GetRequestLimitInfo`
- Query: `GetRequestLimitInfo`
- Fields used: `isUnlimited`, `nextRefreshTime`, `requestLimit`, `requestsUsedSinceLastRefresh` (API uses request-named fields for credits)

If `isUnlimited` is true, the UI shows “Unlimited” and a full remaining bar.

## Troubleshooting

### “Missing Warp API key”

Add a key in **Settings → Providers → Warp**, or set `WARP_API_KEY`.

### “Warp API error”

Confirm the token is valid and that your network can reach `app.warp.dev`.


# FILE: docs/KEYCHAIN_FIX.md

---
summary: "Current keychain behavior: legacy migration, Claude OAuth keychain bootstrap, and prompt mitigation."
read_when:
  - Investigating Keychain prompts
  - Auditing Claude OAuth keychain behavior
  - Comparing legacy keychain docs vs current architecture
---

# Keychain Fix: Current State

## Scope change from the original doc
The original fix (migrating legacy CodexBar keychain items to `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`) is
still in place, but the architecture has changed:

- Provider settings and manual secrets are now persisted in `~/.codexbar/config.json`.
- Legacy keychain stores are still present mainly to migrate old installs, then clear old items.
- Keychain is still used for runtime cache entries (for example `com.steipete.codexbar.cache`) and Claude OAuth
  bootstrap reads from Claude CLI keychain (`Claude Code-credentials`).

## Then vs now

| Previous statement in this doc | Current behavior |
| --- | --- |
| CodexBar stores provider credentials only in keychain | Manual/provider settings are config-file backed (`~/.codexbar/config.json`), while keychain is still used for runtime caches and Claude OAuth bootstrap fallback. |
| `ClaudeOAuthCredentials.swift` migrated CodexBar-owned Claude OAuth keychain items | Claude OAuth primary source is Claude CLI keychain service (`Claude Code-credentials`), with CodexBar cache in `com.steipete.codexbar.cache` (`oauth.claude`). |
| Migration runs in `CodexBarApp.init()` | Migration runs in `HiddenWindowView` `.task` via detached task (`KeychainMigration.migrateIfNeeded()`). |
| Post-migration prompts should be zero in all Claude paths | Legacy-store prompts are reduced; Claude OAuth bootstrap can still prompt when reading Claude CLI keychain, with cooldown + no-UI probes to prevent storms. |
| Log category is `KeychainMigration` | Category is `keychain-migration` (kebab-case). |

## Current keychain surfaces for Claude

### 1. Legacy CodexBar keychain migration (V1)
`Sources/CodexBar/KeychainMigration.swift` migrates legacy `com.steipete.CodexBar` items (for example
`claude-cookie`) to `AfterFirstUnlockThisDeviceOnly`.

- Gate key: `KeychainMigrationV1Completed`
- Runs once unless flag is reset.
- Covers legacy CodexBar-managed accounts only (not Claude CLI's own keychain service).

### 2. Claude OAuth bootstrap path
`Sources/CodexBarCore/Providers/Claude/ClaudeOAuth/ClaudeOAuthCredentials.swift`

Load order for credentials:
1. Environment override (`CODEXBAR_CLAUDE_OAUTH_TOKEN`, scopes env key).
2. In-memory cache.
3. CodexBar keychain cache (`com.steipete.codexbar.cache`, account `oauth.claude`).
4. `~/.claude/.credentials.json`.
5. Claude CLI keychain service: `Claude Code-credentials` (promptable fallback).

Prompt mitigation:
- Non-interactive keychain probes use `KeychainNoUIQuery` with `LAContext.interactionNotAllowed`.
- Pre-alert is shown only when preflight suggests interaction may be required.
- Denials are cooled down in the background via `claudeOAuthKeychainDeniedUntil`
  (`ClaudeOAuthKeychainAccessGate`). User actions (menu open / manual refresh) clear this cooldown.
- Auto-mode availability checks use non-interactive loads with prompt cooldown respected.
- Background cache-sync-on-change also performs non-interactive Claude keychain probes (`syncWithClaudeKeychainIfChanged`)
  and can update cached OAuth data when the token changes.

### Why two Claude keychain prompts can still happen on startup
When CodexBar does not have usable OAuth credentials in its own cache (`com.steipete.codexbar.cache` / `oauth.claude`),
bootstrap falls through to Claude CLI keychain reads.

Current flow can perform up to two interactive reads in one bootstrap call:
1. Interactive read of the newest discovered keychain candidate.
2. If that does not return usable data, interactive legacy service-level fallback read.

On some macOS keychain/ACL states, pressing **Allow** (session-only) for the first read does not grant enough access
for the second read shape, so macOS prompts again. Pressing **Always Allow** usually authorizes both query shapes for
the app identity and avoids the immediate second prompt.

The prompt copy differs because Security.framework is authorizing different operations:
- one path is a direct secret-data read for the key item,
- the fallback path is a key/service access query.

This is OS/keychain ACL behavior, not a `ThisDeviceOnly` migration issue.

### 3. Claude web cookie cache
`Sources/CodexBarCore/CookieHeaderCache.swift` and `Sources/CodexBarCore/KeychainCacheStore.swift`

- Browser-imported Claude session cookies are cached in keychain service `com.steipete.codexbar.cache`.
- Account key is `cookie.claude`.
- Cache writes use `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`.
- Users can clear browser-cookie cache entries from **Preferences → Debug → Caches** or with
  `codexbar cache clear --cookies`. `--provider <id>` scopes cookie clearing to one provider and includes scoped
  Codex managed-account cookie keys.

## What still uses `ThisDeviceOnly`

- Legacy store implementations (`CookieHeaderStore`, token stores, MiniMax stores) still write using
  `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`.
- Keychain cache store (`com.steipete.codexbar.cache`) also writes with `ThisDeviceOnly`.

## Disable keychain access behavior

`Advanced -> Disable Keychain access` sets `debugDisableKeychainAccess` and flips `KeychainAccessGate.isDisabled`.

Effects:
- Blocks keychain reads/writes in legacy stores.
- Disables keychain-backed cookie auto-import paths.
- Forces cookie source resolution to manual/off where applicable.

## Verification

### Check legacy migration flag
```bash
defaults read com.steipete.codexbar KeychainMigrationV1Completed
```

### Check Claude OAuth keychain cooldown
```bash
defaults read com.steipete.codexbar claudeOAuthKeychainDeniedUntil
```

### Inspect keychain-related logs
```bash
log show --predicate 'subsystem == "com.steipete.codexbar" && (category == "keychain-migr

# FILE: docs/kimi.md

---
summary: "Kimi provider notes: cookie auth, quotas, and rate-limit parsing."
read_when:
  - Adding or modifying the Kimi provider
  - Debugging Kimi cookie import or usage parsing
  - Adjusting Kimi menu labels or settings
---

# Kimi Provider

Tracks usage for [Kimi For Coding](https://www.kimi.com/code) in CodexBar.

## Features

- Displays weekly request quota (from membership tier)
- Shows current 5-hour rate limit usage
- Automatic and manual authentication methods
- Automatic refresh countdown

## Setup

Choose one of two authentication methods:

### Method 1: Automatic Browser Import (Recommended)

**No setup needed!** If you're already logged in to Kimi in Arc, Chrome, Safari, Edge, Brave, or Chromium:

1. Open CodexBar settings → Providers → Kimi
2. Set "Cookie source" to "Automatic"
3. Enable the Kimi provider toggle
4. CodexBar will automatically find your session

**Note**: Requires Full Disk Access to read browser cookies (System Settings → Privacy & Security → Full Disk Access → CodexBar).

### Method 2: Manual Token Entry

For advanced users or when automatic import fails:

1. Open CodexBar settings → Providers → Kimi
2. Set "Cookie source" to "Manual"
3. Visit `https://www.kimi.com/code/console` in your browser
4. Open Developer Tools (F12 or Cmd+Option+I)
5. Go to **Application** → **Cookies**
6. Copy the `kimi-auth` cookie value (JWT token)
7. Paste it into the "Auth Token" field in CodexBar

### Method 3: Environment Variable

Alternatively, set the `KIMI_AUTH_TOKEN` environment variable:

```bash
export KIMI_AUTH_TOKEN="jwt-token-here"
```

## Authentication Priority

When multiple sources are available, CodexBar uses this order:

1. Manual token (from Settings UI)
2. Environment variable (`KIMI_AUTH_TOKEN`)
3. Browser cookies (Arc → Chrome → Safari → Edge → Brave → Chromium)

**Note**: Browser cookie import requires Full Disk Access permission.

## API Details

**Endpoint**: `POST https://www.kimi.com/apiv2/kimi.gateway.billing.v1.BillingService/GetUsages`

**Authentication**: Bearer token (from `kimi-auth` cookie)

**Response**:
```json
{
  "usages": [{
    "scope": "FEATURE_CODING",
    "detail": {
      "limit": "2048",
      "used": "214",
      "remaining": "1834",
      "resetTime": "2026-01-09T15:23:13.716839300Z"
    },
    "limits": [{
      "window": {"duration": 300, "timeUnit": "TIME_UNIT_MINUTE"},
      "detail": {
        "limit": "200",
        "used": "139",
        "remaining": "61",
        "resetTime": "2026-01-06T13:33:02.717479433Z"
      }
    }]
  }]
}
```

## Membership Tiers

| Tier | Price | Weekly Quota |
|------|-------|--------------|
| Andante | ¥49/month | 1,024 requests |
| Moderato | ¥99/month | 2,048 requests |
| Allegretto | ¥199/month | 7,168 requests |

All tiers have a rate limit of 200 requests per 5 hours.

## Troubleshooting

### "Kimi auth token is missing"
- Ensure "Cookie source" is set correctly
- If using Automatic mode, verify you're logged in to Kimi in your browser
- Grant Full Disk Access permission if using browser cookies
- Try Manual mode and paste your token directly

### "Kimi auth token is invalid or expired"
- Your token has expired. Paste a new token from your browser
- If using Automatic mode, log in to Kimi again in your browser

### "No Kimi session cookies found"
- You're not logged in to Kimi in any supported browser
- Grant Full Disk Access to CodexBar in System Settings

### "Failed to parse Kimi usage data"
- The API response format may have changed. Please report this issue.

## Implementation

- **Core files**: `Sources/CodexBarCore/Providers/Kimi/`
- **UI files**: `Sources/CodexBar/Providers/Kimi/`
- **Login flow**: `Sources/CodexBar/KimiLoginRunner.swift`
- **Tests**: `Tests/CodexBarTests/KimiProviderTests.swift`


# FILE: docs/architecture.md

---
summary: "Architecture overview: modules, entry points, and data flow."
read_when:
  - Reviewing architecture before feature work
  - Refactoring app structure, app lifecycle, or module boundaries
---

# Architecture overview

## Modules
- `Sources/CodexBarCore`: fetch + parse (Codex RPC, PTY runner, Claude probes, OpenAI web scraping, status polling).
- `Sources/CodexBar`: state + UI (UsageStore, SettingsStore, StatusItemController, menus, icon rendering).
- `Sources/CodexBarWidget`: WidgetKit extension wired to the shared snapshot.
- `Sources/CodexBarCLI`: bundled CLI for `codexbar` usage/status output.
- `Sources/CodexBarMacros`: SwiftSyntax macros for provider registration.
- `Sources/CodexBarMacroSupport`: shared macro support used by app/core/CLI targets.
- `Sources/CodexBarClaudeWatchdog`: helper process for stable Claude CLI PTY sessions.
- `Sources/CodexBarClaudeWebProbe`: CLI helper to diagnose Claude web fetches.

## Entry points
- `CodexBarApp`: SwiftUI keepalive + Settings scene.
- `AppDelegate`: wires status controller, Sparkle updater, notifications.

## Data flow
- Background refresh → `UsageFetcher`/provider probes → `UsageStore` → menu/icon/widgets.
- Settings toggles feed `SettingsStore` → `UsageStore` refresh cadence + feature flags.

## Concurrency & platform
- Swift 6 strict concurrency enabled; prefer Sendable state and explicit MainActor hops.
- macOS 14+ targeting; avoid deprecated APIs when refactoring.

See also: `docs/providers.md`, `docs/refresh-loop.md`, `docs/ui.md`.


# FILE: docs/RELEASING.md

---
summary: "CodexBar release checklist: package, sign, notarize, appcast, and asset validation."
read_when:
  - Starting a CodexBar release
  - Updating signing/notarization or appcast steps
  - Validating release assets or Sparkle feed
---

# Release process (CodexBar)

SwiftPM-only; package/sign/notarize manually (no Xcode project). Sparkle feed is served from GitHub Releases. Checklist below merges Trimmy’s release flow with CodexBar specifics.

**Must read first:** open the master macOS release guide at `~/Projects/agent-scripts/docs/RELEASING-MAC.md` alongside this file and reconcile any differences in favor of CodexBar specifics before starting a release.

## Expectations
- When someone says “release CodexBar”, do the entire end-to-end flow: bump versions/CHANGELOG, build, sign and notarize, upload the zip to the GitHub release, generate/update the appcast with the new signature, publish the tag/release, and verify the enclosure URL responds with 200/OK and installs via Sparkle (no 404s or stale feeds).

### Release automation notes (Scripts/release.sh)
- Always forces a fresh build/notarization (no cached artifacts) before publishing.
- Fails fast if: git tree is dirty, the top changelog section is still “Unreleased” or mismatched, the target version already exists in the appcast, or the build number is not greater than the latest appcast entry.
- Sparkle key probe runs up front; appcast entry + signature verified automatically after generation.
- Release notes are extracted directly from the current changelog section and passed to the GitHub release (no manual notes flag needed).
- Sparkle appcast notes are generated as HTML from the same changelog section and embedded into the appcast entry.
- Requires tools/env on PATH: `swiftformat`, `swiftlint`, `swift`, `sign_update`, `generate_appcast`, `gh`, `python3`, `zip`, `curl`, plus `APP_STORE_CONNECT_*` and `SPARKLE_PRIVATE_KEY_FILE`.

## Prereqs
- Xcode 26+ installed at `/Applications/Xcode.app` (for ictool/iconutil and SDKs).
- Developer ID Application cert installed: `Developer ID Application: Peter Steinberger (Y5PE65HELJ)`.
- ASC API creds in env: `APP_STORE_CONNECT_API_KEY_P8`, `APP_STORE_CONNECT_KEY_ID`, `APP_STORE_CONNECT_ISSUER_ID`.
- Sparkle keys: public key already in Info.plist; private key path set via `SPARKLE_PRIVATE_KEY_FILE` when generating appcast.
- Ensure shell has release env vars loaded (usually `source ~/.profile`) before running `Scripts/release.sh`.

## Icon (glass .icon → .icns)
```
./Scripts/build_icon.sh Icon.icon CodexBar
```
Uses Xcode’s `ictool` + transparent padding + iconset → Icon.icns.

## Build, sign, notarize (universal: arm64 + x86_64)
```
./Scripts/sign-and-notarize.sh
```
What it does:
- `swift build -c release --arch arm64` and `swift build -c release --arch x86_64`
- Packages `CodexBar.app` with Info.plist and Icon.icns
- Embeds Sparkle.framework, Updater, Autoupdate, XPCs
- Codesigns **everything** with runtime + timestamp (deep) and adds rpath
- Zips to `CodexBar-<version>.zip`
- Submits to notarytool, waits, staples, validates

Gotchas fixed:
- Sparkle needs signing for framework, Autoupdate, Updater, XPCs (Downloader/Installer) or notarization fails.
- Use `--timestamp` and `--deep` when signing the app to avoid invalid signature errors.
- Avoid `unzip` — it can add AppleDouble `._*` files that break the sealed signature and trigger “app is damaged”. Use Finder or `ditto -x -k CodexBar-<ver>.zip /Applications`. If Gatekeeper complains, delete the app bundle, re-extract with `ditto`, then `spctl -a -t exec` to verify.
- Manual sanity check before uploading: `find CodexBar.app -name '._*'` should return nothing; then `spctl --assess --type execute --verbose CodexBar.app` and `codesign --verify --deep --strict --verbose CodexBar.app` should both pass on the packaged bundle.

## Appcast (Sparkle)
After notarization:
```
SPARKLE_PRIVATE_KEY_FILE=/path/to/ed25519-priv.key \
./Scripts/make_appcast.sh CodexBar-0.1.0.zip \
  https://raw.githubusercontent.com/steipete/CodexBar/main/appcast.xml
Generates HTML release notes from `CHANGELOG.md` (via `Scripts/changelog-to-html.sh`) and embeds them into the appcast entry.
```
Uploads not handled automatically—commit/publish appcast + zip to the feed location (GitHub Releases/raw URL).

## Tag & release
```
git tag v<version>
./Scripts/make_appcast.sh ...
# upload zip + appcast to Releases
# then create GitHub release (gh release create v<version> ...)
```

## Homebrew (Cask)
CodexBar ships a Homebrew **Cask** in `../homebrew-tap`. When installed via Homebrew, CodexBar disables Sparkle and the app
must be updated via `brew`.

After publishing the GitHub release, update the tap cask + CLI formula (see `docs/releasing-homebrew.md`).

## Checklist (quick)
- [ ] Read both this file and `~/Projects/agent-scripts/docs/RELEASING-MAC.md`; resolve any conflicts toward CodexBar’s specifics.
- [ ] Update versions (scripts/Info.plist, CHANGELOG, About text) — changelog top section must be finalized; release script pulls notes from it automatically.
- [ ] `swiftformat`, `swiftlint`, `swift test` (zero warnings/errors)
- [ ] `./Scripts/build_icon.sh` if icon changed
- [ ] `./Scripts/sign-and-notarize.sh`
- [ ] Generate Sparkle appcast with private key
  - Sparkle ed25519 private key path: `/Users/steipete/Library/CloudStorage/Dropbox/Backup/Sparkle/sparkle-private-key-KEEP-SECURE.txt` (primary) and `/Users/steipete/Library/CloudStorage/Dropbox/Backup/Sparkle-VibeTunnel/sparkle-private-key-KEEP-SECURE.txt` (older backup)
  - Upload the dSYM archive alongside the app zip on the GitHub release; the release script now automates this and will fail if it’s missing.
  - After publishing the release, run `Scripts/check-release-assets.sh <tag>` to confirm both the app zip and dSYM zip are present on GitHub.
  - Generate the appcast + HTML release notes: `./Scripts/make_appcast.sh CodexBar-<ver>.zip https://raw.githubusercontent.com/steipete/CodexBar/main/appcast.xml`
  - Be

# FILE: docs/providers.md

---
summary: "Provider data sources and parsing overview for every registered CodexBar provider."
read_when:
  - Adding or modifying provider fetch/parsing
  - Adjusting provider labels, toggles, or metadata
  - Reviewing data sources for providers
---

# Providers

## Fetch strategies (current)
Legend: web (browser cookies/WebView), cli (RPC/PTy or provider CLI), oauth (provider OAuth), api token, local probe, web dashboard.
Source labels (CLI/header): `openai-web`, `web`, `oauth`, `api`, `local`, `cli`, plus provider-specific CLI labels (e.g. `codex-cli`, `claude`).

Cookie-based providers expose a Cookie source picker (Automatic or Manual) in Settings → Providers.
Some browser cookie imports are cached in Keychain and reused until the session is invalid. API keys, manual cookie
headers, source selection, provider ordering, and token accounts are stored in `~/.codexbar/config.json`.

| Provider | Strategies (ordered for auto) |
| --- | --- |
| Codex | App Auto: OAuth API (`oauth`) → CLI RPC/PTy (`codex-cli`). CLI Auto: Web dashboard (`openai-web`) → CLI RPC/PTy (`codex-cli`). |
| Claude | App Auto: OAuth API (`oauth`) → CLI PTY (`claude`) → Web API (`web`). CLI Auto: Web API (`web`) → CLI PTY (`claude`). |
| Gemini | OAuth-backed API via Gemini CLI credentials (`api`). |
| Antigravity | Local LSP/HTTP probe (`local`). |
| Cursor | Web API via cookies → stored WebKit session (`web`). |
| OpenCode | Web dashboard via cookies (`web`). |
| OpenCode Go | Web dashboard via cookies (`web`); optional workspace ID. |
| Alibaba Coding Plan | Console RPC via web cookies (auto/manual) with API key fallback (`web`, `api`). |
| Droid/Factory | Web cookies → stored tokens → local storage → WorkOS cookies (`web`). |
| z.ai | API token from config/env → quota API (`api`). |
| Manus | Browser `session_id` cookie (auto/manual/env) → credits API (`web`). |
| MiniMax | Manual/browser session via Coding Plan web path (`web`), or Coding Plan API token (`api`). |
| Kimi | Auth token from `kimi-auth` cookie/manual token/env → usage API (`web`). |
| Kilo | API token from config/env → usage API (`api`); auto falls back to CLI session auth (`cli`). |
| Copilot | Device-flow/env/config token → `copilot_internal` API (`api`). |
| Kimi K2 | API key from config/env → credit endpoint (`api`). |
| Kiro | CLI command via `kiro-cli chat --no-interactive "/usage"` (`cli`). |
| Vertex AI | Google ADC OAuth (gcloud) → Cloud Monitoring quota usage (`oauth`). |
| Augment | `auggie` CLI first, then browser-cookie web fallback (`cli`, `web`). |
| JetBrains AI | Local XML quota file (`local`). |
| Amp | Web settings page via browser cookies (`web`). |
| Warp | API token (config/env) → GraphQL request limits (`api`). |
| Ollama | Web settings page via browser cookies (`web`). |
| Synthetic | API key from config/env → quota API (`api`). |
| OpenRouter | API token (config, overrides env) → credits API (`api`). |
| Perplexity | Browser cookies/manual cookie/env session token → credits API (`web`). |
| Xiaomi MiMo | Browser cookies → balance/token plan endpoints (`web`). |
| Doubao | API key from config/env → Volcengine Ark chat-completions probe (`api`). |
| Abacus AI | Browser cookies → compute points + billing API (`web`). |
| Mistral | Console billing API via Ory Kratos session cookies (`web`). |
| DeepSeek | API key from env or token accounts → balance endpoint (`api`). |
| Moonshot | API key from config/env → balance endpoint (`api`). |
| Codebuff | API token from config/env or `codebuff login` credentials → usage API (`api`). |
| Crof | API key from config/env → credit balance + requests quota API (`api`). |
| Venice | API key from config/env → DIEM/USD balance API (`api`). |
| Command Code | Web billing API via Command Code session cookies (`web`). |

## Codex
- App Auto: OAuth API first; falls back to CLI only when OAuth credentials are missing or auth/refresh is invalid.
- Web dashboard (optional, off by default): `https://chatgpt.com/codex/settings/usage` via WebView + browser cookies.
- Battery saver toggle (currently off by default): reduces routine OpenAI web refreshes but still allows explicit manual refreshes.
- CLI RPC default: `codex ... app-server` JSON-RPC (`account/read`, `account/rateLimits/read`).
- CLI PTY: manual diagnostics/parser coverage only; automatic refresh does not launch bare Codex TUI.
- Local cost usage: scans `CODEX_HOME` (or `~/.codex`) `sessions` and sibling `archived_sessions` JSONL files (last 30 days).
- Status: Statuspage.io (OpenAI).
- Details: `docs/codex.md`.

## Claude
- App Auto: OAuth API (`oauth`) → CLI PTY (`claude`) → Web API (`web`).
- CLI Auto: Web API (`web`) → CLI PTY (`claude`).
- Local cost usage: scans `CLAUDE_CONFIG_DIR` when set, otherwise `~/.config/claude/projects` and `~/.claude/projects` JSONL files (last 30 days).
- Status: Statuspage.io (Anthropic).
- Details: `docs/claude.md`.

## z.ai
- API token from `~/.codexbar/config.json` (`providers[].apiKey`) or `Z_AI_API_KEY` env var.
- Supports global and BigModel CN quota hosts; override with `Z_AI_API_HOST` or `Z_AI_QUOTA_URL`.
- Status: none yet.
- Details: `docs/zai.md`.

## Manus
- Session token via browser `session_id` cookie, manual Settings entry, `MANUS_SESSION_TOKEN`, or `MANUS_COOKIE`.
- Credits endpoint: `POST https://api.manus.im/user.v1.UserService/GetAvailableCredits`.
- Auto mode prefers cached/browser cookies before env fallback; manual mode accepts either a bare `session_id` value or a full Cookie header.
- Status: none yet.

## MiniMax
- Coding Plan API token or web session from configured/manual/browser sources.
- Supports global and China mainland hosts via provider region settings and environment overrides.
- Status: none yet.
- Details: `docs/minimax.md`.

## Kimi
- Auth token (JWT from `kimi-auth` cookie) via manual entry or `KIMI_AUTH_TOKEN` env var.
- Shows weekly quota and 5-hour rate limit (300 minutes).
- Status: none yet.
- Details: `docs/kimi.md`.

## Kilo
- API token from `~/.codexbar/config.

# FILE: docs/alibaba-coding-plan.md

---
summary: "Alibaba Coding Plan provider data sources: browser-session baseline, secondary API mode, and honest quota fallback behavior."
read_when:
  - Debugging Alibaba Coding Plan API key handling or quota parsing
  - Updating Alibaba Coding Plan endpoints or region behavior
  - Adjusting Alibaba Coding Plan provider UI/menu behavior
---

# Alibaba Coding Plan provider

Alibaba Coding Plan supports both browser-session and API-key paths, but the supported baseline is browser-session fetching from the Model Studio/Bailian console. API mode remains secondary and may still be limited by account/region behavior.

## Cookie sources (web mode)
1) Automatic browser import (Model Studio/Bailian cookies).
2) Manual cookie header from Settings.
3) Environment variable `ALIBABA_CODING_PLAN_COOKIE`.

When the RPC endpoint returns `ConsoleNeedLogin`, CodexBar treats that as a console-session requirement. In API mode it is surfaced as an explicit API-path limitation; in `auto` mode fallback remains observable through the fetch-attempt chain.

## Token sources (fallback order)
1) Config token (`~/.codexbar/config.json` -> `providers[].apiKey` for provider `alibaba`).
2) Environment variables, checked in order:
   - `ALIBABA_CODING_PLAN_API_KEY`
   - `ALIBABA_QWEN_API_KEY`
   - `DASHSCOPE_API_KEY`

## Region + endpoint behavior
- International host: `https://modelstudio.console.alibabacloud.com`
- China mainland host: `https://bailian.console.aliyun.com`
- Quota request path:
  - `POST /data/api.json?action=zeldaEasy.broadscope-bailian.codingPlan.queryCodingPlanInstanceInfoV2&product=broadscope-bailian&api=queryCodingPlanInstanceInfoV2`
- Region is selected in Preferences -> Providers -> Alibaba Coding Plan -> Gateway region.
- Auto fallback behavior:
  - If International fails with credential/host-style API errors, CodexBar retries China mainland once.

### CN API-key limitation (known)
- In some China mainland accounts/environments, the current Alibaba `/data/api.json` coding-plan endpoint can still return console-login-required responses (`ConsoleNeedLogin`) even when an API key is configured.
- In that case, API-key mode may not be functionally available for that account/endpoint, and web session mode is required.
- CodexBar now surfaces this as an API error in API mode (instead of a cookie-login-required message) so the limitation is explicit.

## Overrides
- Override host base: `ALIBABA_CODING_PLAN_HOST`
  - Example: `ALIBABA_CODING_PLAN_HOST=modelstudio.console.alibabacloud.com`
- Override full quota URL: `ALIBABA_CODING_PLAN_QUOTA_URL`
  - Example: `ALIBABA_CODING_PLAN_QUOTA_URL=https://example.com/data/api.json?action=...`

## Request headers
- `Authorization: Bearer <api_key>`
- `x-api-key: <api_key>`
- `X-DashScope-API-Key: <api_key>`
- `Content-Type: application/json`
- `Accept: application/json`

## Parsing + mapping
- Plan name (best effort):
  - `codingPlanInstanceInfos[].planName` / `instanceName` / `packageName`
- Quota windows (from `codingPlanQuotaInfo`):
  - `per5HourUsedQuota` + `per5HourTotalQuota` + `per5HourQuotaNextRefreshTime` -> primary (5-hour)
  - `perWeekUsedQuota` + `perWeekTotalQuota` + `perWeekQuotaNextRefreshTime` -> secondary (weekly)
  - `perBillMonthUsedQuota` + `perBillMonthTotalQuota` + `perBillMonthQuotaNextRefreshTime` -> tertiary (monthly)
- Each window maps to `usedPercent = used / total * 100` (bounded to valid range).
- If the payload proves the plan is active but does not expose defensible quota counters, CodexBar preserves the visible plan state without manufacturing a normal quantitative quota window.
- If neither real counters nor a defensible active-plan fallback signal exist, parsing fails explicitly instead of degrading to fake `0%` usage.

## Dashboard links
- International console: `https://modelstudio.console.alibabacloud.com/ap-southeast-1/?tab=globalset#/efm/coding_plan`
- China mainland console: `https://bailian.console.aliyun.com/cn-beijing/?tab=model#/efm/coding_plan`

## Key files
- `Sources/CodexBarCore/Providers/Alibaba/AlibabaCodingPlanProviderDescriptor.swift`
- `Sources/CodexBarCore/Providers/Alibaba/AlibabaCodingPlanUsageFetcher.swift`
- `Sources/CodexBarCore/Providers/Alibaba/AlibabaCodingPlanUsageSnapshot.swift`
- `Sources/CodexBar/Providers/Alibaba/AlibabaCodingPlanProviderImplementation.swift`


# FILE: docs/web-integration.md

---
summary: "Deprecated: OpenAI web dashboard integration is documented in docs/codex.md."
read_when:
  - Redirect: see docs/codex.md
---

# OpenAI web integration (Codex)

Moved to `docs/codex.md`.

