# Missing Repo Summary Source: coleam00/Archon

- URL: https://github.com/coleam00/Archon
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/coleam00__Archon
- Clone Status: cloned
- Language: TypeScript
- Stars: 21341
- Topics: ai, automation, bun, claude, cli, coding-assistant, developer-tools, typescript, workflow-engine, yaml
- Description: The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="assets/logo.png" alt="Archon" width="160" />
</p>

<h1 align="center">Archon</h1>

<p align="center">
  The first open-source harness builder for AI coding. Make AI coding deterministic and repeatable.
</p>

<p align="center">
  <a href="https://trendshift.io/repositories/13964" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13964" alt="coleam00%2FArchon | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT" /></a>
  <a href="https://github.com/coleam00/Archon/actions/workflows/test.yml"><img src="https://github.com/coleam00/Archon/actions/workflows/test.yml/badge.svg" alt="CI" /></a>
  <a href="https://archon.diy"><img src="https://img.shields.io/badge/docs-archon.diy-blue" alt="Docs" /></a>
</p>

---

Archon is a workflow engine for AI coding agents. Define your development processes as YAML workflows - planning, implementation, validation, code review, PR creation - and run them reliably across all your projects.

Like what Dockerfiles did for infrastructure and GitHub Actions did for CI/CD - Archon does for AI coding workflows. Think n8n, but for software development.

## Why Archon?

When you ask an AI agent to "fix this bug", what happens depends on the model's mood. It might skip planning. It might forget to run tests. It might write a PR description that ignores your template. Every run is different.

Archon fixes this. Encode your development process as a workflow. The workflow defines the phases, validation gates, and artifacts. The AI fills in the intelligence at each step, but the structure is deterministic and owned by you.

- **Repeatable** - Same workflow, same sequence, every time. Plan, implement, validate, review, PR.
- **Isolated** - Every workflow run gets its own git worktree. Run 5 fixes in parallel with no conflicts.
- **Fire and forget** - Kick off a workflow, go do other work. Come back to a finished PR with review comments.
- **Composable** - Mix deterministic nodes (bash scripts, tests, git ops) with AI nodes (planning, code generation, review). The AI only runs where it adds value.
- **Portable** - Define workflows once in `.archon/workflows/`, commit them to your repo. They work the same from CLI, Web UI, Slack, Telegram, or GitHub.

## What It Looks Like

Here's an example of an Archon workflow that plans, implements in a loop until tests pass, gets your approval, then creates the PR:

```yaml
# .archon/workflows/build-feature.yaml
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"

  - id: implement
    depends_on: [plan]
    loop:                                      # AI loop - iterate until done
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
      fresh_context: true                      # Fresh session each iteration

  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"                   # Deterministic - no AI

  - id: review
    depends_on: [run-tests]
    prompt: "Review all changes against the plan. Fix any issues."

  - id: approve
    depends_on: [review]
    loop:                                      # Human approval gate
      prompt: "Present the changes for review. Address any feedback."
      until: APPROVED
      interactive: true                        # Pauses and waits for human input

  - id: create-pr
    depends_on: [approve]
    prompt: "Push changes and create a pull request"
```

Tell your coding agent what you want, and Archon handles the rest:

```
You: Use archon to add dark mode to the settings page

Agent: I'll run the archon-idea-to-pr workflow for this.
       → Creating isolated worktree on branch archon/task-dark-mode...
       → Planning...
       → Implementing (task 1/4)...
       → Implementing (task 2/4)...
       → Tests failing - iterating...
       → Tests passing after 2 iterations
       → Code review complete - 0 issues
       → PR ready: https://github.com/you/project/pull/47
```

## Previous Version

Looking for the original Python-based Archon (task management + RAG)? It's fully preserved on the [`archive/v1-task-management-rag`](https://github.com/coleam00/Archon/tree/archive/v1-task-management-rag) branch.

## Getting Started

> **Most users should start with the [Full Setup](#full-setup-5-minutes)** - it walks you through credentials, installs the Archon skill into your projects, and gives you the web dashboard.
>
> **Already have Claude Code and just want the CLI?** Jump to the [Quick Install](#quick-install-30-seconds).

### Full Setup (5 minutes)

Clone the repo and use the guided setup wizard. This configures credentials, platform integrations, and copies the Archon skill into your target projects.

<details>
<summary><b>Prerequisites</b> - Bun, Claude Code, and the GitHub CLI</summary>

**Bun** - [bun.sh](https://bun.sh)

```bash
# macOS/Linux
curl -fsSL https://bun.sh/install | bash

# Windows (PowerShell)
irm bun.sh/install.ps1 | iex
```

**GitHub CLI** - [cli.github.com](https://cli.github.com/)

```bash
# macOS
brew install gh

# Windows (via winget)
winget install GitHub.cli

# Linux (Debian/Ubuntu)
sudo apt install gh
```

**Claude Code** - [claude.ai/code](https://claude.ai/code)

```bash
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex
```

</details>

```bash
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```

Then say: **"Set up Archon"**

The setup wizard walks you through everything: CLI installation, authentication, platform selection, and copies the Archon skill to your target repo.

### Quick Install (30 seconds)

Already have Claude Code set up? Install the standalone CLI binary and skip the wizard.

**macOS / Linux**
```bash
curl -fsSL https://archon.diy/install | bash
```

**Windows (PowerShell)**
```powershell
irm https://archon.diy/install.ps1 | iex
```

**Homebrew**
```bash
brew install coleam00/archon/archon
```

> **Compiled binaries need a `CLAUDE_BIN_PATH`.** The quick-install binaries
> don't bundle Claude Code. Install it separately, then point Archon at it:
>
> ```bash
> # macOS / Linux / WSL
> curl -fsSL https://claude.ai/install.sh | bash
> export CLAUDE_BIN_PATH="$HOME/.local/bin/claude"
>
> # Windows (PowerShell)
> irm https://claude.ai/install.ps1 | iex
> $env:CLAUDE_BIN_PATH = "$env:USERPROFILE\.local\bin\claude.exe"
> ```
>
> Or set `assistants.claude.claudeBinaryPath` in `~/.archon/config.yaml`.
> The Docker image ships Claude Code pre-installed. See [AI Assistants → Binary path configuration](https://archon.diy/docs/getting-started/ai-assistants/#binary-path-configuration-compiled-binaries-only) for details.

### Start Using Archon

Once you've completed either setup path, go to your project and start working:

```bash
cd /path/to/your/project
claude
```

```
Use archon to fix issue #42
```

```
What archon workflows do I have? When would I use each one?
```

The coding agent handles workflow selection, branch naming, and worktree isolation for you. Projects are registered automatically the first time they're used.

> **Important:** Always run Claude Code from your target repo, not from the Archon repo. The setup wizard copies the Archon skill into your project so it works from there.

## Web UI

Archon includes a web dashboard for chatting with your coding agent, running workflows, and monitoring activity. Binary installs: run `archon serve` to download and start the web UI in one step. From source: ask your coding agent to run the frontend from the Archon repo, or run `bun run dev` from the repo root yourself.

Register a project by clicking **+** next to "Project" in the chat sidebar - enter a GitHub URL or local path. Then start a conversation, invoke workflows, and watch progress in real time.

**Key pages:**
- **Chat** - Conversation interface with real-time streaming and tool call visualization
- **Dashboard** - Mission Control for monitoring running workflows, with filterable history by project, status, and date
- **Workflow Builder** - Visual drag-and-drop editor for creating DAG workflows with loop nodes
- **Workflow Execution** - Step-by-step progress view for any running or completed workflow

**Monitoring hub:** The sidebar shows conversations from **all platforms** - not just the web. Workflows kicked off from the CLI, messages from Slack or Telegram, GitHub issue interactions - everything appears in one place.

See the [Web UI Guide](https://archon.diy/adapters/web/) for full documentation.

## What Can You Automate?

Archon ships with workflows for common development tasks:

| Workflow | What it does |
|----------|-------------|
| `archon-assist` | General Q&A, debugging, exploration - full Claude Code agent with all tools |
| `archon-fix-github-issue` | Classify issue → investigate/plan → implement → validate → PR → smart review → self-fix |
| `archon-idea-to-pr` | Feature idea → plan → implement → validate → PR → 5 parallel reviews → self-fix |
| `archon-plan-to-pr` | Execute existing plan → implement → validate → PR → review → self-fix |
| `archon-issue-review-full` | Comprehensive fix + full multi-agent review pipeline for GitHub issues |
| `archon-smart-pr-review` | Classify PR complexity → run targeted review agents → synthesize findings |
| `archon-comprehensive-pr-review` | Multi-agent PR review (5 parallel reviewers) with automatic fixes |
| `archon-create-issue` | Classify problem → gather context → investigate → create GitHub issue |
| `archon-validate-pr` | Thorough PR validation testing both main and feature branches |
| `archon-resolve-conflicts` | Detect merge conflicts → analyze both sides → resolve → validate → commit |
| `archon-feature-development` | Implement feature from plan → validate → create PR |
| `archon-architect` | Archite
