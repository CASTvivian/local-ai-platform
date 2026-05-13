# Missing Repo Summary Source: ultraworkers/claw-code

- URL: https://github.com/ultraworkers/claw-code
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/ultraworkers__claw-code
- Clone Status: cloned
- Language: Rust
- Stars: 191229
- Topics: 
- Description: The repo is finally unlocked. enjoy the party! The fastest repo in history to surpass 100K stars ⭐. Join Discord: https://discord.gg/5TUQKqFWd Built in Rust using oh-my-codex.

## Extracted README / Docs / Examples



# FILE: README.md

# Claw Code

<p align="center">
  <a href="https://github.com/ultraworkers/claw-code">ultraworkers/claw-code</a>
  ·
  <a href="./USAGE.md">Usage</a>
  ·
  <a href="./rust/README.md">Rust workspace</a>
  ·
  <a href="./PARITY.md">Parity</a>
  ·
  <a href="./ROADMAP.md">Roadmap</a>
  ·
  <a href="https://discord.gg/5TUQKqFWd">UltraWorkers Discord</a>
</p>

<p align="center">
  <a href="https://star-history.com/#ultraworkers/claw-code&Date">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ultraworkers/claw-code&type=Date&theme=dark" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ultraworkers/claw-code&type=Date" />
      <img alt="Star history for ultraworkers/claw-code" src="https://api.star-history.com/svg?repos=ultraworkers/claw-code&type=Date" width="600" />
    </picture>
  </a>
</p>

<p align="center">
  <img src="assets/claw-hero.jpeg" alt="Claw Code" width="300" />
</p>

Claw Code is the public Rust implementation of the `claw` CLI agent harness.
The canonical implementation lives in [`rust/`](./rust), and the current source of truth for this repository is **ultraworkers/claw-code**.

> [!IMPORTANT]
> Start with [`USAGE.md`](./USAGE.md) for build, auth, CLI, session, and parity-harness workflows. Make `claw doctor` your first health check after building, use [`rust/README.md`](./rust/README.md) for crate-level details, read [`PARITY.md`](./PARITY.md) for the current Rust-port checkpoint, and see [`docs/container.md`](./docs/container.md) for the container-first workflow.
>
> **ACP / Zed status:** `claw-code` does not ship an ACP/Zed daemon entrypoint yet. Run `claw acp` (or `claw --acp`) for the current status instead of guessing from source layout; `claw acp serve` is currently a discoverability alias only, and real ACP support remains tracked separately in `ROADMAP.md`.

## Current repository shape

- **`rust/`** — canonical Rust workspace and the `claw` CLI binary
- **`USAGE.md`** — task-oriented usage guide for the current product surface
- **`PARITY.md`** — Rust-port parity status and migration notes
- **`ROADMAP.md`** — active roadmap and cleanup backlog
- **`PHILOSOPHY.md`** — project intent and system-design framing
- **`src/` + `tests/`** — companion Python/reference workspace and audit helpers; not the primary runtime surface

## Quick start

> [!NOTE]
> [!WARNING]
> **`cargo install claw-code` installs the wrong thing.** The `claw-code` crate on crates.io is a deprecated stub that places `claw-code-deprecated.exe` — not `claw`. Running it only prints `"claw-code has been renamed to agent-code"`. **Do not use `cargo install claw-code`.** Either build from source (this repo) or install the upstream binary:
> ```bash
> cargo install agent-code   # upstream binary — installs 'agent.exe' (Windows) / 'agent' (Unix), NOT 'agent-code'
> ```
> This repo (`ultraworkers/claw-code`) is **build-from-source only** — follow the steps below.

```bash
# 1. Clone and build
git clone https://github.com/ultraworkers/claw-code
cd claw-code/rust
cargo build --workspace

# 2. Set your API key (Anthropic API key — not a Claude subscription)
export ANTHROPIC_API_KEY="sk-ant-..."

# 3. Verify everything is wired correctly
./target/debug/claw doctor

# 4. Run a prompt
./target/debug/claw prompt "say hello"
```

> [!NOTE]
> **Windows (PowerShell):** the binary is `claw.exe`, not `claw`. Use `.\target\debug\claw.exe` or run `cargo run -- prompt "say hello"` to skip the path lookup.

### Windows setup

**PowerShell is a supported Windows path.** Use whichever shell works for you. The common onboarding issues on Windows are:

1. **Install Rust first** — download from <https://rustup.rs/> and run the installer. Close and reopen your terminal when it finishes.
2. **Verify Rust is on PATH:**
   ```powershell
   cargo --version
   ```
   If this fails, reopen your terminal or run the PATH setup from the Rust installer output, then retry.
3. **Clone and build** (works in PowerShell, Git Bash, or WSL):
   ```powershell
   git clone https://github.com/ultraworkers/claw-code
   cd claw-code/rust
   cargo build --workspace
   ```
4. **Run** (PowerShell — note `.exe` and backslash):
   ```powershell
   $env:ANTHROPIC_API_KEY = "sk-ant-..."
   .\target\debug\claw.exe prompt "say hello"
   ```

**Git Bash / WSL** are optional alternatives, not requirements. If you prefer bash-style paths (`/c/Users/you/...` instead of `C:\Users\you\...`), Git Bash (ships with Git for Windows) works well. In Git Bash, the `MINGW64` prompt is expected and normal — not a broken install.

## Post-build: locate the binary and verify

After running `cargo build --workspace`, the `claw` binary is built but **not** automatically installed to your system. Here's where to find it and how to verify the build succeeded.

### Binary location

After `cargo build --workspace` in `claw-code/rust/`:

**Debug build (default, faster compile):**
- **macOS/Linux:** `rust/target/debug/claw`
- **Windows:** `rust/target/debug/claw.exe`

**Release build (optimized, slower compile):**
- **macOS/Linux:** `rust/target/release/claw`
- **Windows:** `rust/target/release/claw.exe`

If you ran `cargo build` without `--release`, the binary is in the `debug/` folder.

### Verify the build succeeded

Test the binary directly using its path:

```bash
# macOS/Linux (debug build)
./rust/target/debug/claw --help
./rust/target/debug/claw doctor

# Windows PowerShell (debug build)
.\rust\target\debug\claw.exe --help
.\rust\target\debug\claw.exe doctor
```

If these commands succeed, the build is working. `claw doctor` is your first health check — it validates your API key, model access, and tool configuration.

### Optional: Add to PATH

If you want to run `claw` from any directory without the full path, choose one of these approaches:

**Option 1: Symlink (macOS/Linux)**
```bash
ln -s $(pwd)/rust/target/debug/claw /usr/local/bin/claw
```
Then reload your shell and test:
```bash
claw --help
```

**Option 2: Use `cargo install` (all platforms)**

Build and install to Cargo's default location (`~/.cargo/bin/`, which is usually on PATH):
```bash
# From the claw-code/rust/ directory
cargo install --path . --force

# Then from anywhere
claw --help
```

**Option 3: Update shell profile (bash/zsh)**

Add this line to `~/.bashrc` or `~/.zshrc`:
```bash
export PATH="$(pwd)/rust/target/debug:$PATH"
```

Reload your shell:
```bash
source ~/.bashrc  # or source ~/.zshrc
claw --help
```

### Troubleshooting

- **"command not found: claw"** — The binary is in `rust/target/debug/claw`, but it's not on your PATH. Use the full path `./rust/target/debug/claw` or symlink/install as above.
- **"permission denied"** — On macOS/Linux, you may need `chmod +x rust/target/debug/claw` if the executable bit isn't set (rare).
- **Debug vs. release** — If the build is slow, you're in debug mode (default). Add `--release` to `cargo build` for faster runtime, but the build itself will take 5–10 minutes.

> [!NOTE]
> **Auth:** claw requires an **API key** (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, etc.) — Claude subscription login is not a supported auth path.

Run the workspace test suite after verifying the binary works:

```bash
cd rust
cargo test --workspace
```

## Documentation map

- [`USAGE.md`](./USAGE.md) — quick commands, auth, sessions, config, parity harness
- [`rust/README.md`](./rust/README.md) — crate map, CLI surface, features, workspace layout
- [`PARITY.md`](./PARITY.md) — parity status for the Rust port
- [`rust/MOCK_PARITY_HARNESS.md`](./rust/MOCK_PARITY_HARNESS.md) — deterministic mock-service harness details
- [`ROADMAP.md`](./ROADMAP.md) — active roadmap and open cleanup work
- [`PHILOSOPHY.md`](./PHILOSOPHY.md) — why the project exists and how it is operated

## Ecosystem

Claw Code is built in the open alongside the broader UltraWorkers toolchain:

- [clawhip](https://github.com/Yeachan-Heo/clawhip)
- [oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent)
- [oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode)
- [oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex)
- [UltraWorkers Discord](https://discord.gg/5TUQKqFWd)

## Ownership / affiliation disclaimer

- This repository does **not** claim ownership of the original Claude Code source material.
- This repository is **not affiliated with, endorsed by, or maintained by Anthropic**.


# FILE: docs/container.md

# Container-first claw-code workflows

This repo already had **container detection** in the Rust runtime before this document was added:

- `rust/crates/runtime/src/sandbox.rs` detects Docker/Podman/container markers such as `/.dockerenv`, `/run/.containerenv`, matching env vars, and `/proc/1/cgroup` hints.
- `rust/crates/rusty-claude-cli/src/main.rs` exposes that state through the `claw sandbox` / `cargo run -p rusty-claude-cli -- sandbox` report.
- `.github/workflows/rust-ci.yml` runs on `ubuntu-latest`, but it does **not** define a Docker or Podman container job.
- Before this change, the repo did **not** have a checked-in `Dockerfile`, `Containerfile`, or `.devcontainer/` config.

This document adds a small checked-in `Containerfile` so Docker and Podman users have one canonical container workflow.

## What the checked-in container image is for

The root [`../Containerfile`](../Containerfile) gives you a reusable Rust build/test shell with the extra packages this workspace commonly needs (`git`, `pkg-config`, `libssl-dev`, certificates).

It does **not** copy the repository into the image. Instead, the recommended flow is to bind-mount your checkout into `/workspace` so edits stay on the host.

## Build the image

From the repository root:

### Docker

```bash
docker build -t claw-code-dev -f Containerfile .
```

### Podman

```bash
podman build -t claw-code-dev -f Containerfile .
```

## Run `cargo test --workspace` in the container

These commands mount the repo, keep Cargo build artifacts out of the working tree, and run from the Rust workspace at `rust/`.

### Docker

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev \
  cargo test --workspace
```

### Podman

```bash
podman run --rm -it \
  -v "$PWD":/workspace:Z \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev \
  cargo test --workspace
```

If you want a fully clean rebuild, add `cargo clean &&` before `cargo test --workspace`.

## Open a shell in the container

### Docker

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev
```

### Podman

```bash
podman run --rm -it \
  -v "$PWD":/workspace:Z \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev
```

Inside the shell:

```bash
cargo build --workspace
cargo test --workspace
cargo run -p rusty-claude-cli -- --help
cargo run -p rusty-claude-cli -- sandbox
```

The `sandbox` command is a useful sanity check: inside Docker or Podman it should report `In container true` and list the markers the runtime detected.

## Bind-mount this repo and another repo at the same time

If you want to run `claw` against a second checkout while keeping `claw-code` itself mounted read-write:

### Docker

```bash
docker run --rm -it \
  -v "$PWD":/workspace \
  -v "$HOME/src/other-repo":/repo \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev
```

### Podman

```bash
podman run --rm -it \
  -v "$PWD":/workspace:Z \
  -v "$HOME/src/other-repo":/repo:Z \
  -e CARGO_TARGET_DIR=/tmp/claw-target \
  -w /workspace/rust \
  claw-code-dev
```

Then, for example:

```bash
cargo run -p rusty-claude-cli -- prompt "summarize /repo"
```

## Notes

- Docker and Podman use the same checked-in `Containerfile`.
- The `:Z` suffix in the Podman examples is for SELinux relabeling; keep it on Fedora/RHEL-class hosts.
- Running with `CARGO_TARGET_DIR=/tmp/claw-target` avoids leaving container-owned `target/` artifacts in your bind-mounted checkout.
- For non-container local development, keep using [`../USAGE.md`](../USAGE.md) and [`../rust/README.md`](../rust/README.md).


# FILE: docs/MODEL_COMPATIBILITY.md

# Model Compatibility Guide

This document describes model-specific handling in the OpenAI-compatible provider. When adding new models or providers, review this guide to ensure proper compatibility.

## Table of Contents

- [Overview](#overview)
- [Model-Specific Handling](#model-specific-handling)
  - [Kimi Models (is_error Exclusion)](#kimi-models-is_error-exclusion)
  - [Reasoning Models (Tuning Parameter Stripping)](#reasoning-models-tuning-parameter-stripping)
  - [GPT-5 (max_completion_tokens)](#gpt-5-max_completion_tokens)
  - [Qwen Models (DashScope Routing)](#qwen-models-dashscope-routing)
- [Implementation Details](#implementation-details)
- [Adding New Models](#adding-new-models)
- [Testing](#testing)

## Overview

The `openai_compat.rs` provider translates Claude Code's internal message format to OpenAI-compatible chat completion requests. Different models have varying requirements for:

- Tool result message fields (`is_error`)
- Sampling parameters (temperature, top_p, etc.)
- Token limit fields (`max_tokens` vs `max_completion_tokens`)
- Base URL routing

## Model-Specific Handling

### Kimi Models (is_error Exclusion)

**Affected models:** `kimi-k2.5`, `kimi-k1.5`, `kimi-moonshot`, and any model with `kimi` in the name (case-insensitive)

**Behavior:** The `is_error` field is **excluded** from tool result messages.

**Rationale:** Kimi models (via Moonshot AI and DashScope) reject the `is_error` field with a 400 Bad Request error:
```json
{
  "error": {
    "type": "invalid_request_error",
    "message": "Unknown field: is_error"
  }
}
```

**Detection:**
```rust
fn model_rejects_is_error_field(model: &str) -> bool {
    let lowered = model.to_ascii_lowercase();
    let canonical = lowered.rsplit('/').next().unwrap_or(lowered.as_str());
    canonical.starts_with("kimi-")
}
```

**Testing:** See `model_rejects_is_error_field_detects_kimi_models` and related tests in `openai_compat.rs`.

---

### Reasoning Models (Tuning Parameter Stripping)

**Affected models:**
- OpenAI: `o1`, `o1-*`, `o3`, `o3-*`, `o4`, `o4-*`
- xAI: `grok-3-mini`
- Alibaba DashScope: `qwen-qwq-*`, `qwq-*`, `qwen3-*-thinking`

**Behavior:** The following tuning parameters are **stripped** from requests:
- `temperature`
- `top_p`
- `frequency_penalty`
- `presence_penalty`

**Rationale:** Reasoning/chain-of-thought models use fixed sampling strategies and reject these parameters with 400 errors.

**Exception:** `reasoning_effort` is included for compatible models when explicitly set.

**Detection:**
```rust
fn is_reasoning_model(model: &str) -> bool {
    let canonical = model.to_ascii_lowercase()
        .rsplit('/')
        .next()
        .unwrap_or(model);
    canonical.starts_with("o1")
        || canonical.starts_with("o3")
        || canonical.starts_with("o4")
        || canonical == "grok-3-mini"
        || canonical.starts_with("qwen-qwq")
        || canonical.starts_with("qwq")
        || (canonical.starts_with("qwen3") && canonical.contains("-thinking"))
}
```

**Testing:** See `reasoning_model_strips_tuning_params`, `grok_3_mini_is_reasoning_model`, and `qwen_reasoning_variants_are_detected` tests.

---

### GPT-5 (max_completion_tokens)

**Affected models:** All models starting with `gpt-5`

**Behavior:** Uses `max_completion_tokens` instead of `max_tokens` in the request payload.

**Rationale:** GPT-5 models require the `max_completion_tokens` field. Legacy `max_tokens` causes request validation failures:
```json
{
  "error": {
    "message": "Unknown field: max_tokens"
  }
}
```

**Implementation:**
```rust
let max_tokens_key = if wire_model.starts_with("gpt-5") {
    "max_completion_tokens"
} else {
    "max_tokens"
};
```

**Testing:** See `gpt5_uses_max_completion_tokens_not_max_tokens` and `non_gpt5_uses_max_tokens` tests.

---

### Qwen Models (DashScope Routing)

**Affected models:** All models with `qwen` prefix

**Behavior:** Routed to DashScope (`https://dashscope.aliyuncs.com/compatible-mode/v1`) rather than default providers.

**Rationale:** Qwen models are hosted by Alibaba Cloud's DashScope service, not OpenAI or Anthropic.

**Configuration:**
```rust
pub const DEFAULT_DASHSCOPE_BASE_URL: &str = "https://dashscope.aliyuncs.com/compatible-mode/v1";
```

**Authentication:** Uses `DASHSCOPE_API_KEY` environment variable.

**Note:** Some Qwen models are also reasoning models (see [Reasoning Models](#reasoning-models-tuning-parameter-stripping) above) and receive both treatments.

## Implementation Details

### File Location
All model-specific logic is in:
```
rust/crates/api/src/providers/openai_compat.rs
```

### Key Functions

| Function | Purpose |
|----------|---------|
| `model_rejects_is_error_field()` | Detects models that don't support `is_error` in tool results |
| `is_reasoning_model()` | Detects reasoning models that need tuning param stripping |
| `translate_message()` | Converts internal messages to OpenAI format (applies `is_error` logic) |
| `build_chat_completion_request()` | Constructs full request payload (applies all model-specific logic) |

### Provider Prefix Handling

All model detection functions strip provider prefixes (e.g., `dashscope/kimi-k2.5` → `kimi-k2.5`) before matching:

```rust
let canonical = model.to_ascii_lowercase()
    .rsplit('/')
    .next()
    .unwrap_or(model);
```

This ensures consistent detection regardless of whether models are referenced with or without provider prefixes.

## Adding New Models

When adding support for new models:

1. **Check if the model is a reasoning model**
   - Does it reject temperature/top_p parameters?
   - Add to `is_reasoning_model()` detection

2. **Check tool result compatibility**
   - Does it reject the `is_error` field?
   - Add to `model_rejects_is_error_field()` detection

3. **Check token limit field**
   - Does it require `max_completion_tokens` instead of `max_tokens`?
   - Update the `max_tokens_key` logic

4. **Add tests**
   - Unit test for detection function
   - Integration test in `build_chat
