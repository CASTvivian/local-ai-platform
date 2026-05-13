# Missing Repo Summary Source: openai/codex

- URL: https://github.com/openai/codex
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/openai__codex
- Clone Status: cloned
- Language: Rust
- Stars: 82152
- Topics: 
- Description: Lightweight coding agent that runs in your terminal

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center"><code>npm i -g @openai/codex</code><br />or <code>brew install --cask codex</code></p>
<p align="center"><strong>Codex CLI</strong> is a coding agent from OpenAI that runs locally on your computer.
<p align="center">
  <img src="https://github.com/openai/codex/blob/main/.github/codex-cli-splash.png" alt="Codex CLI splash" width="80%" />
</p>
</br>
If you want Codex in your code editor (VS Code, Cursor, Windsurf), <a href="https://developers.openai.com/codex/ide">install in your IDE.</a>
</br>If you want the desktop app experience, run <code>codex app</code> or visit <a href="https://chatgpt.com/codex?app-landing-page=true">the Codex App page</a>.
</br>If you are looking for the <em>cloud-based agent</em> from OpenAI, <strong>Codex Web</strong>, go to <a href="https://chatgpt.com/codex">chatgpt.com/codex</a>.</p>

---

## Quickstart

### Installing and running Codex CLI

Install globally with your preferred package manager:

```shell
# Install using npm
npm install -g @openai/codex
```

```shell
# Install using Homebrew
brew install --cask codex
```

Then simply run `codex` to get started.

<details>
<summary>You can also go to the <a href="https://github.com/openai/codex/releases/latest">latest GitHub Release</a> and download the appropriate binary for your platform.</summary>

Each GitHub Release contains many executables, but in practice, you likely want one of these:

- macOS
  - Apple Silicon/arm64: `codex-aarch64-apple-darwin.tar.gz`
  - x86_64 (older Mac hardware): `codex-x86_64-apple-darwin.tar.gz`
- Linux
  - x86_64: `codex-x86_64-unknown-linux-musl.tar.gz`
  - arm64: `codex-aarch64-unknown-linux-musl.tar.gz`

Each archive contains a single entry with the platform baked into the name (e.g., `codex-x86_64-unknown-linux-musl`), so you likely want to rename it to `codex` after extracting it.

</details>

### Using Codex with your ChatGPT plan

Run `codex` and select **Sign in with ChatGPT**. We recommend signing into your ChatGPT account to use Codex as part of your Plus, Pro, Business, Edu, or Enterprise plan. [Learn more about what's included in your ChatGPT plan](https://help.openai.com/en/articles/11369540-codex-in-chatgpt).

You can also use Codex with an API key, but this requires [additional setup](https://developers.openai.com/codex/auth#sign-in-with-an-api-key).

## Docs

- [**Codex Documentation**](https://developers.openai.com/codex)
- [**Contributing**](./docs/contributing.md)
- [**Installing & building**](./docs/install.md)
- [**Open source fund**](./docs/open-source-fund.md)

This repository is licensed under the [Apache-2.0 License](LICENSE).


# FILE: docs/authentication.md

# Authentication

For information about Codex CLI authentication, see [this documentation](https://developers.openai.com/codex/auth).


# FILE: docs/license.md

## License

This repository is licensed under the [Apache-2.0 License](../LICENSE).


# FILE: docs/agents_md.md

# AGENTS.md

For information about AGENTS.md, see [this documentation](https://developers.openai.com/codex/guides/agents-md).

## Hierarchical agents message

When the `child_agents_md` feature flag is enabled (via `[features]` in `config.toml`), Codex appends additional guidance about AGENTS.md scope and precedence to the user instructions message and emits that message even when no AGENTS.md is present.


# FILE: docs/sandbox.md

## Sandbox & approvals

For information about Codex sandboxing and approvals, see [this documentation](https://developers.openai.com/codex/security).


# FILE: docs/open-source-fund.md

## Codex open source fund

We're excited to launch a **$1 million initiative** supporting open source projects that use Codex CLI and other OpenAI models.

- Grants are awarded up to **$25,000** API credits.
- Applications are reviewed **on a rolling basis**.

**Interested? [Apply here](https://openai.com/form/codex-open-source-fund/).**


# FILE: docs/install.md

## Installing & building

### System requirements

| Requirement                 | Details                                                         |
| --------------------------- | --------------------------------------------------------------- |
| Operating systems           | macOS 12+, Ubuntu 20.04+/Debian 10+, or Windows 11 **via WSL2** |
| Git (optional, recommended) | 2.23+ for built-in PR helpers                                   |
| RAM                         | 4-GB minimum (8-GB recommended)                                 |

### DotSlash

The GitHub Release also contains a [DotSlash](https://dotslash-cli.com/) file for the Codex CLI named `codex`. Using a DotSlash file makes it possible to make a lightweight commit to source control to ensure all contributors use the same version of an executable, regardless of what platform they use for development.

### Build from source

```bash
# Clone the repository and navigate to the root of the Cargo workspace.
git clone https://github.com/openai/codex.git
cd codex/codex-rs

# Install the Rust toolchain, if necessary.
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
source "$HOME/.cargo/env"
rustup component add rustfmt
rustup component add clippy
# Install helper tools used by the workspace justfile:
cargo install --locked just
# Optional: install nextest for the `just test` helper
cargo install --locked cargo-nextest

# Build Codex.
cargo build

# Launch the TUI with a sample prompt.
cargo run --bin codex -- "explain this codebase to me"

# After making changes, use the root justfile helpers (they default to codex-rs):
just fmt
just fix -p <crate-you-touched>

# Run the relevant tests (project-specific is fastest), for example:
cargo test -p codex-tui
# If you have cargo-nextest installed, `just test` runs the test suite via nextest:
just test
# Avoid `--all-features` for routine local runs because it increases build
# time and `target/` disk usage by compiling additional feature combinations.
# If you specifically want full feature coverage, use:
cargo test --all-features
```

## Tracing / verbose logging

Codex is written in Rust, so it honors the `RUST_LOG` environment variable to configure its logging behavior.

The TUI defaults to `RUST_LOG=codex_core=info,codex_tui=info,codex_rmcp_client=info` and log messages are written to `~/.codex/log/codex-tui.log` by default. For a single run, you can override the log directory with `-c log_dir=...` (for example, `-c log_dir=./.codex-log`).

```bash
tail -F ~/.codex/log/codex-tui.log
```

By comparison, the non-interactive mode (`codex exec`) defaults to `RUST_LOG=error`, but messages are printed inline, so there is no need to monitor a separate file.

See the Rust documentation on [`RUST_LOG`](https://docs.rs/env_logger/latest/env_logger/#enabling-logging) for more information on the configuration options.


# FILE: docs/example-config.md

# Sample configuration

For a sample configuration file, see [this documentation](https://developers.openai.com/codex/config-sample).


# FILE: docs/execpolicy.md

# Execution policy

For an overview of execution policy rules, see [this documentation](https://developers.openai.com/codex/exec-policy).


# FILE: docs/getting-started.md

# Getting started with Codex CLI

For an overview of Codex CLI features, see [this documentation](https://developers.openai.com/codex/cli/features#running-in-interactive-mode).


# FILE: docs/config.md

# Configuration

For basic configuration instructions, see [this documentation](https://developers.openai.com/codex/config-basic).

For advanced configuration instructions, see [this documentation](https://developers.openai.com/codex/config-advanced).

For a full configuration reference, see [this documentation](https://developers.openai.com/codex/config-reference).

## Lifecycle hooks

Admins can set top-level `allow_managed_hooks_only = true` in
`requirements.toml` to ignore user, project, and session hook configs while
still allowing managed hooks from requirements and managed config layers. This
setting is only supported in `requirements.toml`; putting it in `config.toml`
does not enable managed-hooks-only mode.


# FILE: docs/skills.md

# Skills

For information about skills, refer to [this documentation](https://developers.openai.com/codex/skills).


# FILE: docs/CLA.md

# Individual Contributor License Agreement (v1.0, OpenAI)

_Based on the Apache Software Foundation Individual CLA v 2.2._

By commenting **“I have read the CLA Document and I hereby sign the CLA”**
on a Pull Request, **you (“Contributor”) agree to the following terms** for any
past and future “Contributions” submitted to the **OpenAI Codex CLI project
(the “Project”)**.

---

## 1. Definitions

- **“Contribution”** – any original work of authorship submitted to the Project
  (code, documentation, designs, etc.).
- **“You” / “Your”** – the individual (or legal entity) posting the acceptance
  comment.

## 2. Copyright License

You grant **OpenAI, Inc.** and all recipients of software distributed by the
Project a perpetual, worldwide, non‑exclusive, royalty‑free, irrevocable
license to reproduce, prepare derivative works of, publicly display, publicly
perform, sublicense, and distribute Your Contributions and derivative works.

## 3. Patent License

You grant **OpenAI, Inc.** and all recipients of the Project a perpetual,
worldwide, non‑exclusive, royalty‑free, irrevocable (except as below) patent
license to make, have made, use, sell, offer to sell, import, and otherwise
transfer Your Contributions alone or in combination with the Project.

If any entity brings patent litigation alleging that the Project or a
Contribution infringes a patent, the patent licenses granted by You to that
entity under this CLA terminate.

## 4. Representations

1. You are legally entitled to grant the licenses above.
2. Each Contribution is either Your original creation or You have authority to
   submit it under this CLA.
3. Your Contributions are provided **“AS IS”** without warranties of any kind.
4. You will notify the Project if any statement above becomes inaccurate.

## 5. Miscellany

This Agreement is governed by the laws of the **State of California**, USA,
excluding its conflict‑of‑laws rules. If any provision is held unenforceable,
the remaining provisions remain in force.

