# Missing Repo Summary Source: obra/superpowers

- URL: https://github.com/obra/superpowers
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/obra__superpowers
- Clone Status: cloned
- Language: Shell
- Stars: 188042
- Topics: 
- Description: An agentic skills framework & software development methodology that works.

## Extracted README / Docs / Examples



# FILE: README.md

# Superpowers

Superpowers is a complete software development methodology for your coding agents, built on top of a set of composable skills and some initial instructions that make sure your agent uses them.

## Quickstart

Give your agent Superpowers: [Claude Code](#claude-code), [Codex CLI](#codex-cli), [Codex App](#codex-app), [Factory Droid](#factory-droid), [Gemini CLI](#gemini-cli), [OpenCode](#opencode), [Cursor](#cursor), [GitHub Copilot CLI](#github-copilot-cli).

## How it works

It starts from the moment you fire up your coding agent. As soon as it sees that you're building something, it *doesn't* just jump into trying to write code. Instead, it steps back and asks you what you're really trying to do. 

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. 

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY. 

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superpowers.


## Sponsorship

If Superpowers has helped you do stuff that makes money and you are so inclined, I'd greatly appreciate it if you'd consider [sponsoring my opensource work](https://github.com/sponsors/obra).

Thanks! 

- Jesse


## Installation

Installation differs by harness. If you use more than one, install Superpowers separately for each one.

### Claude Code

Superpowers is available via the [official Claude plugin marketplace](https://claude.com/plugins/superpowers)

#### Official Marketplace

- Install the plugin from Anthropic's official marketplace:

  ```bash
  /plugin install superpowers@claude-plugins-official
  ```

#### Superpowers Marketplace

The Superpowers marketplace provides Superpowers and some other related plugins for Claude Code.

- Register the marketplace:

  ```bash
  /plugin marketplace add obra/superpowers-marketplace
  ```

- Install the plugin from this marketplace:

  ```bash
  /plugin install superpowers@superpowers-marketplace
  ```

### Codex CLI

Superpowers is available via the [official Codex plugin marketplace](https://github.com/openai/plugins).

- Open the plugin search interface:

  ```bash
  /plugins
  ```

- Search for Superpowers:

  ```bash
  superpowers
  ```

- Select `Install Plugin`.

### Codex App

Superpowers is available via the [official Codex plugin marketplace](https://github.com/openai/plugins).

- In the Codex app, click on Plugins in the sidebar.
- You should see `Superpowers` in the Coding section.
- Click the `+` next to Superpowers and follow the prompts.

### Factory Droid

- Register the marketplace:

  ```bash
  droid plugin marketplace add https://github.com/obra/superpowers
  ```

- Install the plugin:

  ```bash
  droid plugin install superpowers@superpowers
  ```

### Gemini CLI

- Install the extension:

  ```bash
  gemini extensions install https://github.com/obra/superpowers
  ```

- Update later:

  ```bash
  gemini extensions update superpowers
  ```

### OpenCode

OpenCode uses its own plugin install; install Superpowers separately even if you
already use it in another harness.

- Tell OpenCode:

  ```
  Fetch and follow instructions from https://raw.githubusercontent.com/obra/superpowers/refs/heads/main/.opencode/INSTALL.md
  ```

- Detailed docs: [docs/README.opencode.md](docs/README.opencode.md)

### Cursor

- In Cursor Agent chat, install from marketplace:

  ```text
  /add-plugin superpowers
  ```

- Or search for "superpowers" in the plugin marketplace.

### GitHub Copilot CLI

- Register the marketplace:

  ```bash
  copilot plugin marketplace add obra/superpowers-marketplace
  ```

- Install the plugin:

  ```bash
  copilot plugin install superpowers@superpowers-marketplace
  ```

## The Basic Workflow

1. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.

2. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.

3. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.

4. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.

5. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.

6. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.

7. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## What's Inside

### Skills Library

**Testing**
- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** - Ensure it's actually fixed

**Collaboration** 
- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)

**Meta**
- **writing-skills** - Create new skills following best practices (includes testing methodology)
- **using-superpowers** - Introduction to the skills system

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

Read [the original release announcement](https://blog.fsck.com/2025/10/09/superpowers/).

## Contributing

The general contribution process for Superpowers is below. Keep in mind that we don't generally accept contributions of new skills and that any updates to skills must work across all of the coding agents we support.

1. Fork the repository
2. Switch to the 'dev' branch
3. Create a branch for your work
4. Follow the `writing-skills` skill for creating and testing new and modified skills
5. Submit a PR, being sure to fill in the pull request template.

See `skills/writing-skills/SKILL.md` for the complete guide.

## Updating

Superpowers updates are somewhat coding-agent dependent, but are often automatic.

## License

MIT License - see LICENSE file for details

## Community

Superpowers is built by [Jesse Vincent](https://blog.fsck.com) and the rest of the folks at [Prime Radiant](https://primeradiant.com).

- **Discord**: [Join us](https://discord.gg/35wsABTejz) for community support, questions, and sharing what you're building with Superpowers
- **Issues**: https://github.com/obra/superpowers/issues
- **Release announcements**: [Sign up](https://primeradiant.com/superpowers/) to get notified about new versions


# FILE: docs/testing.md

# Testing Superpowers Skills

This document describes how to test Superpowers skills, particularly the integration tests for complex skills like `subagent-driven-development`.

## Overview

Testing skills that involve subagents, workflows, and complex interactions requires running actual Claude Code sessions in headless mode and verifying their behavior through session transcripts.

## Test Structure

```
tests/
├── claude-code/
│   ├── test-helpers.sh                    # Shared test utilities
│   ├── test-subagent-driven-development-integration.sh
│   ├── analyze-token-usage.py             # Token analysis tool
│   └── run-skill-tests.sh                 # Test runner (if exists)
```

## Running Tests

### Integration Tests

Integration tests execute real Claude Code sessions with actual skills:

```bash
# Run the subagent-driven-development integration test
cd tests/claude-code
./test-subagent-driven-development-integration.sh
```

**Note:** Integration tests can take 10-30 minutes as they execute real implementation plans with multiple subagents.

### Requirements

- Must run from the **superpowers plugin directory** (not from temp directories)
- Claude Code must be installed and available as `claude` command
- Local dev marketplace must be enabled: `"superpowers@superpowers-dev": true` in `~/.claude/settings.json`

## Integration Test: subagent-driven-development

### What It Tests

The integration test verifies the `subagent-driven-development` skill correctly:

1. **Plan Loading**: Reads the plan once at the beginning
2. **Full Task Text**: Provides complete task descriptions to subagents (doesn't make them read files)
3. **Self-Review**: Ensures subagents perform self-review before reporting
4. **Review Order**: Runs spec compliance review before code quality review
5. **Review Loops**: Uses review loops when issues are found
6. **Independent Verification**: Spec reviewer reads code independently, doesn't trust implementer reports

### How It Works

1. **Setup**: Creates a temporary Node.js project with a minimal implementation plan
2. **Execution**: Runs Claude Code in headless mode with the skill
3. **Verification**: Parses the session transcript (`.jsonl` file) to verify:
   - Skill tool was invoked
   - Subagents were dispatched (Task tool)
   - TodoWrite was used for tracking
   - Implementation files were created
   - Tests pass
   - Git commits show proper workflow
4. **Token Analysis**: Shows token usage breakdown by subagent

### Test Output

```
========================================
 Integration Test: subagent-driven-development
========================================

Test project: /tmp/tmp.xyz123

=== Verification Tests ===

Test 1: Skill tool invoked...
  [PASS] subagent-driven-development skill was invoked

Test 2: Subagents dispatched...
  [PASS] 7 subagents dispatched

Test 3: Task tracking...
  [PASS] TodoWrite used 5 time(s)

Test 6: Implementation verification...
  [PASS] src/math.js created
  [PASS] add function exists
  [PASS] multiply function exists
  [PASS] test/math.test.js created
  [PASS] Tests pass

Test 7: Git commit history...
  [PASS] Multiple commits created (3 total)

Test 8: No extra features added...
  [PASS] No extra features added

=========================================
 Token Usage Analysis
=========================================

Usage Breakdown:
----------------------------------------------------------------------------------------------------
Agent           Description                          Msgs      Input     Output      Cache     Cost
----------------------------------------------------------------------------------------------------
main            Main session (coordinator)             34         27      3,996  1,213,703 $   4.09
3380c209        implementing Task 1: Create Add Function     1          2        787     24,989 $   0.09
34b00fde        implementing Task 2: Create Multiply Function     1          4        644     25,114 $   0.09
3801a732        reviewing whether an implementation matches...   1          5        703     25,742 $   0.09
4c142934        doing a final code review...                    1          6        854     25,319 $   0.09
5f017a42        a code reviewer. Review Task 2...               1          6        504     22,949 $   0.08
a6b7fbe4        a code reviewer. Review Task 1...               1          6        515     22,534 $   0.08
f15837c0        reviewing whether an implementation matches...   1          6        416     22,485 $   0.07
----------------------------------------------------------------------------------------------------

TOTALS:
  Total messages:         41
  Input tokens:           62
  Output tokens:          8,419
  Cache creation tokens:  132,742
  Cache read tokens:      1,382,835

  Total input (incl cache): 1,515,639
  Total tokens:             1,524,058

  Estimated cost: $4.67
  (at $3/$15 per M tokens for input/output)

========================================
 Test Summary
========================================

STATUS: PASSED
```

## Token Analysis Tool

### Usage

Analyze token usage from any Claude Code session:

```bash
python3 tests/claude-code/analyze-token-usage.py ~/.claude/projects/<project-dir>/<session-id>.jsonl
```

### Finding Session Files

Session transcripts are stored in `~/.claude/projects/` with the working directory path encoded:

```bash
# Example for /Users/yourname/Documents/GitHub/superpowers/superpowers
SESSION_DIR="$HOME/.claude/projects/-Users-yourname-Documents-GitHub-superpowers-superpowers"

# Find recent sessions
ls -lt "$SESSION_DIR"/*.jsonl | head -5
```

### What It Shows

- **Main session usage**: Token usage by the coordinator (you or main Claude instance)
- **Per-subagent breakdown**: Each Task invocation with:
  - Agent ID
  - Description (extracted from prompt)
  - Message count
  - Input/output tokens
  - Cache usage
  - Estimated cost
- **Totals**: Overall token usage and cost estimate

### Understanding the Output

- 

# FILE: docs/README.opencode.md

# Superpowers for OpenCode

Complete guide for using Superpowers with [OpenCode.ai](https://opencode.ai).

## Installation

Add superpowers to the `plugin` array in your `opencode.json` (global or project-level):

```json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git"]
}
```

Restart OpenCode. The plugin installs through OpenCode's plugin manager and
registers all skills.

Verify by asking: "Tell me about your superpowers"

OpenCode uses its own plugin install. If you also use Claude Code, Codex, or
another harness, install Superpowers separately for each one.

### Migrating from the old symlink-based install

If you previously installed superpowers using `git clone` and symlinks, remove the old setup:

```bash
# Remove old symlinks
rm -f ~/.config/opencode/plugins/superpowers.js
rm -rf ~/.config/opencode/skills/superpowers

# Optionally remove the cloned repo
rm -rf ~/.config/opencode/superpowers

# Remove skills.paths from opencode.json if you added one for superpowers
```

Then follow the installation steps above.

## Usage

### Finding Skills

Use OpenCode's native `skill` tool to list all available skills:

```
use skill tool to list skills
```

### Loading a Skill

```
use skill tool to load superpowers/brainstorming
```

### Personal Skills

Create your own skills in `~/.config/opencode/skills/`:

```bash
mkdir -p ~/.config/opencode/skills/my-skill
```

Create `~/.config/opencode/skills/my-skill/SKILL.md`:

```markdown
---
name: my-skill
description: Use when [condition] - [what it does]
---

# My Skill

[Your skill content here]
```

### Project Skills

Create project-specific skills in `.opencode/skills/` within your project.

**Skill Priority:** Project skills > Personal skills > Superpowers skills

## Updating

OpenCode installs Superpowers through a git-backed package spec. Some OpenCode
and Bun versions pin that resolved git dependency in a lockfile or cache, so a
restart may not pick up the newest Superpowers commit. If updates do not appear,
clear OpenCode's package cache or reinstall the plugin.

To pin a specific version, use a branch or tag:

```json
{
  "plugin": ["superpowers@git+https://github.com/obra/superpowers.git#v5.0.3"]
}
```

## How It Works

The plugin does two things:

1. **Injects bootstrap context** via the `experimental.chat.system.transform` hook, adding superpowers awareness to every conversation.
2. **Registers the skills directory** via the `config` hook, so OpenCode discovers all superpowers skills without symlinks or manual config.

### Tool Mapping

Skills written for Claude Code are automatically adapted for OpenCode:

- `TodoWrite` → `todowrite`
- `Task` with subagents → OpenCode's `@mention` system
- `Skill` tool → OpenCode's native `skill` tool
- File operations → Native OpenCode tools

## Troubleshooting

### Plugin not loading

1. Check OpenCode logs: `opencode run --print-logs "hello" 2>&1 | grep -i superpowers`
2. Verify the plugin line in your `opencode.json` is correct
3. Make sure you're running a recent version of OpenCode

### Windows install issues

Some Windows OpenCode builds have upstream installer issues with git-backed
plugin specs, including cache paths for `git+https` URLs and Bun not finding
`git.exe` even when it works in a normal terminal. If OpenCode cannot install
the plugin, try installing with system npm and pointing OpenCode at the local
package:

```powershell
npm install superpowers@git+https://github.com/obra/superpowers.git --prefix "$HOME\.config\opencode"
```

Then use the installed package path in `opencode.json`:

```json
{
  "plugin": ["~/.config/opencode/node_modules/superpowers"]
}
```

### Skills not found

1. Use OpenCode's `skill` tool to list available skills
2. Check that the plugin is loading (see above)
3. Each skill needs a `SKILL.md` file with valid YAML frontmatter

### Bootstrap not appearing

1. Check OpenCode version supports `experimental.chat.system.transform` hook
2. Restart OpenCode after config changes

## Getting Help

- Report issues: https://github.com/obra/superpowers/issues
- Main documentation: https://github.com/obra/superpowers
- OpenCode docs: https://opencode.ai/docs/


# FILE: docs/plans/2025-11-22-opencode-support-implementation.md

# OpenCode Support Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add full superpowers support for OpenCode.ai with a native JavaScript plugin that shares core functionality with the existing Codex implementation.

**Architecture:** Extract common skill discovery/parsing logic into `lib/skills-core.js`, refactor Codex to use it, then build OpenCode plugin using their native plugin API with custom tools and session hooks.

**Tech Stack:** Node.js, JavaScript, OpenCode Plugin API, Git worktrees

---

## Phase 1: Create Shared Core Module

### Task 1: Extract Frontmatter Parsing

**Files:**
- Create: `lib/skills-core.js`
- Reference: `.codex/superpowers-codex` (lines 40-74)

**Step 1: Create lib/skills-core.js with extractFrontmatter function**

```javascript
#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Extract YAML frontmatter from a skill file.
 * Current format:
 * ---
 * name: skill-name
 * description: Use when [condition] - [what it does]
 * ---
 *
 * @param {string} filePath - Path to SKILL.md file
 * @returns {{name: string, description: string}}
 */
function extractFrontmatter(filePath) {
    try {
        const content = fs.readFileSync(filePath, 'utf8');
        const lines = content.split('\n');

        let inFrontmatter = false;
        let name = '';
        let description = '';

        for (const line of lines) {
            if (line.trim() === '---') {
                if (inFrontmatter) break;
                inFrontmatter = true;
                continue;
            }

            if (inFrontmatter) {
                const match = line.match(/^(\w+):\s*(.*)$/);
                if (match) {
                    const [, key, value] = match;
                    switch (key) {
                        case 'name':
                            name = value.trim();
                            break;
                        case 'description':
                            description = value.trim();
                            break;
                    }
                }
            }
        }

        return { name, description };
    } catch (error) {
        return { name: '', description: '' };
    }
}

module.exports = {
    extractFrontmatter
};
```

**Step 2: Verify file was created**

Run: `ls -l lib/skills-core.js`
Expected: File exists

**Step 3: Commit**

```bash
git add lib/skills-core.js
git commit -m "feat: create shared skills core module with frontmatter parser"
```

---

### Task 2: Extract Skill Discovery Logic

**Files:**
- Modify: `lib/skills-core.js`
- Reference: `.codex/superpowers-codex` (lines 97-136)

**Step 1: Add findSkillsInDir function to skills-core.js**

Add before `module.exports`:

```javascript
/**
 * Find all SKILL.md files in a directory recursively.
 *
 * @param {string} dir - Directory to search
 * @param {string} sourceType - 'personal' or 'superpowers' for namespacing
 * @param {number} maxDepth - Maximum recursion depth (default: 3)
 * @returns {Array<{path: string, name: string, description: string, sourceType: string}>}
 */
function findSkillsInDir(dir, sourceType, maxDepth = 3) {
    const skills = [];

    if (!fs.existsSync(dir)) return skills;

    function recurse(currentDir, depth) {
        if (depth > maxDepth) return;

        const entries = fs.readdirSync(currentDir, { withFileTypes: true });

        for (const entry of entries) {
            const fullPath = path.join(currentDir, entry.name);

            if (entry.isDirectory()) {
                // Check for SKILL.md in this directory
                const skillFile = path.join(fullPath, 'SKILL.md');
                if (fs.existsSync(skillFile)) {
                    const { name, description } = extractFrontmatter(skillFile);
                    skills.push({
                        path: fullPath,
                        skillFile: skillFile,
                        name: name || entry.name,
                        description: description || '',
                        sourceType: sourceType
                    });
                }

                // Recurse into subdirectories
                recurse(fullPath, depth + 1);
            }
        }
    }

    recurse(dir, 0);
    return skills;
}
```

**Step 2: Update module.exports**

Replace the exports line with:

```javascript
module.exports = {
    extractFrontmatter,
    findSkillsInDir
};
```

**Step 3: Verify syntax**

Run: `node -c lib/skills-core.js`
Expected: No output (success)

**Step 4: Commit**

```bash
git add lib/skills-core.js
git commit -m "feat: add skill discovery function to core module"
```

---

### Task 3: Extract Skill Resolution Logic

**Files:**
- Modify: `lib/skills-core.js`
- Reference: `.codex/superpowers-codex` (lines 212-280)

**Step 1: Add resolveSkillPath function**

Add before `module.exports`:

```javascript
/**
 * Resolve a skill name to its file path, handling shadowing
 * (personal skills override superpowers skills).
 *
 * @param {string} skillName - Name like "superpowers:brainstorming" or "my-skill"
 * @param {string} superpowersDir - Path to superpowers skills directory
 * @param {string} personalDir - Path to personal skills directory
 * @returns {{skillFile: string, sourceType: string, skillPath: string} | null}
 */
function resolveSkillPath(skillName, superpowersDir, personalDir) {
    // Strip superpowers: prefix if present
    const forceSuperpowers = skillName.startsWith('superpowers:');
    const actualSkillName = forceSuperpowers ? skillName.replace(/^superpowers:/, '') : skillName;

    // Try personal skills first (unless explicitly superpowers:)
    if (!forceSuperpowers && personalDir) {
        const personalPath = path.join(personalDir, actualSkillName);
        const personalSkillFile = path.join(personalPath, 'SKILL.md');
        if (fs.existsSync(personalSkillFile)) {
            return {
                skillFile: per

# FILE: docs/plans/2025-11-22-opencode-support-design.md

# OpenCode Support Design

**Date:** 2025-11-22
**Author:** Bot & Jesse
**Status:** Design Complete, Awaiting Implementation

## Overview

Add full superpowers support for OpenCode.ai using a native OpenCode plugin architecture that shares core functionality with the existing Codex implementation.

## Background

OpenCode.ai is a coding agent similar to Claude Code and Codex. Previous attempts to port superpowers to OpenCode (PR #93, PR #116) used file-copying approaches. This design takes a different approach: building a native OpenCode plugin using their JavaScript/TypeScript plugin system while sharing code with the Codex implementation.

### Key Differences Between Platforms

- **Claude Code**: Native Anthropic plugin system + file-based skills
- **Codex**: No plugin system → bootstrap markdown + CLI script
- **OpenCode**: JavaScript/TypeScript plugins with event hooks and custom tools API

### OpenCode's Agent System

- **Primary agents**: Build (default, full access) and Plan (restricted, read-only)
- **Subagents**: General (research, searching, multi-step tasks)
- **Invocation**: Automatic dispatch by primary agents OR manual `@mention` syntax
- **Configuration**: Custom agents in `opencode.json` or `~/.config/opencode/agent/`

## Architecture

### High-Level Structure

1. **Shared Core Module** (`lib/skills-core.js`)
   - Common skill discovery and parsing logic
   - Used by both Codex and OpenCode implementations

2. **Platform-Specific Wrappers**
   - Codex: CLI script (`.codex/superpowers-codex`)
   - OpenCode: Plugin module (`.opencode/plugin/superpowers.js`)

3. **Skill Directories**
   - Core: `~/.config/opencode/superpowers/skills/` (or installed location)
   - Personal: `~/.config/opencode/skills/` (shadows core skills)

### Code Reuse Strategy

Extract common functionality from `.codex/superpowers-codex` into shared module:

```javascript
// lib/skills-core.js
module.exports = {
  extractFrontmatter(filePath),      // Parse name + description from YAML
  findSkillsInDir(dir, maxDepth),    // Recursive SKILL.md discovery
  findAllSkills(dirs),                // Scan multiple directories
  resolveSkillPath(skillName, dirs), // Handle shadowing (personal > core)
  checkForUpdates(repoDir)           // Git fetch/status check
};
```

### Skill Frontmatter Format

Current format (no `when_to_use` field):

```yaml
---
name: skill-name
description: Use when [condition] - [what it does]; [additional context]
---
```

## OpenCode Plugin Implementation

### Custom Tools

**Tool 1: `use_skill`**

Loads a specific skill's content into the conversation (equivalent to Claude's Skill tool).

```javascript
{
  name: 'use_skill',
  description: 'Load and read a specific skill to guide your work',
  schema: z.object({
    skill_name: z.string().describe('Name of skill (e.g., "superpowers:brainstorming")')
  }),
  execute: async ({ skill_name }) => {
    const { skillPath, content, frontmatter } = resolveAndReadSkill(skill_name);
    const skillDir = path.dirname(skillPath);

    return `# ${frontmatter.name}
# ${frontmatter.description}
# Supporting tools and docs are in ${skillDir}
# ============================================

${content}`;
  }
}
```

**Tool 2: `find_skills`**

Lists all available skills with metadata.

```javascript
{
  name: 'find_skills',
  description: 'List all available skills',
  schema: z.object({}),
  execute: async () => {
    const skills = discoverAllSkills();
    return skills.map(s =>
      `${s.namespace}:${s.name}
  ${s.description}
  Directory: ${s.directory}
`).join('\n');
  }
}
```

### Session Startup Hook

When a new session starts (`session.started` event):

1. **Inject using-superpowers content**
   - Full content of the using-superpowers skill
   - Establishes mandatory workflows

2. **Run find_skills automatically**
   - Display full list of available skills upfront
   - Include skill directories for each

3. **Inject tool mapping instructions**
   ```markdown
   **Tool Mapping for OpenCode:**
   When skills reference tools you don't have, substitute:
   - `TodoWrite` → `update_plan`
   - `Task` with subagents → Use OpenCode subagent system (@mention)
   - `Skill` tool → `use_skill` custom tool
   - Read, Write, Edit, Bash → Your native equivalents

   **Skill directories contain:**
   - Supporting scripts (run with bash)
   - Additional documentation (read with read tool)
   - Utilities specific to that skill
   ```

4. **Check for updates** (non-blocking)
   - Quick git fetch with timeout
   - Notify if updates available

### Plugin Structure

```javascript
// .opencode/plugin/superpowers.js
const skillsCore = require('../../lib/skills-core');
const path = require('path');
const fs = require('fs');
const { z } = require('zod');

export const SuperpowersPlugin = async ({ client, directory, $ }) => {
  const superpowersDir = path.join(process.env.HOME, '.config/opencode/superpowers');
  const personalDir = path.join(process.env.HOME, '.config/opencode/skills');

  return {
    'session.started': async () => {
      const usingSuperpowers = await readSkill('using-superpowers');
      const skillsList = await findAllSkills();
      const toolMapping = getToolMappingInstructions();

      return {
        context: `${usingSuperpowers}\n\n${skillsList}\n\n${toolMapping}`
      };
    },

    tools: [
      {
        name: 'use_skill',
        description: 'Load and read a specific skill',
        schema: z.object({
          skill_name: z.string()
        }),
        execute: async ({ skill_name }) => {
          // Implementation using skillsCore
        }
      },
      {
        name: 'find_skills',
        description: 'List all available skills',
        schema: z.object({}),
        execute: async () => {
          // Implementation using skillsCore
        }
      }
    ]
  };
};
```

## File Structure

```
superpowers/
├── lib/
│   └── skills-core.js           # NEW: Shared skill logic
├── .codex/
│   ├── superpowers-codex        # UPDATED: U

# FILE: docs/plans/2026-01-17-visual-brainstorming.md

# Visual Brainstorming Companion Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Give Claude a browser-based visual companion for brainstorming sessions - show mockups, prototypes, and interactive choices alongside terminal conversation.

**Architecture:** Claude writes HTML to a temp file. A local Node.js server watches that file and serves it with an auto-injected helper library. User interactions flow via WebSocket to server stdout, which Claude sees in background task output.

**Tech Stack:** Node.js, Express, ws (WebSocket), chokidar (file watching)

---

## Task 1: Create the Server Foundation

**Files:**
- Create: `lib/brainstorm-server/index.js`
- Create: `lib/brainstorm-server/package.json`

**Step 1: Create package.json**

```json
{
  "name": "brainstorm-server",
  "version": "1.0.0",
  "description": "Visual brainstorming companion server for Claude Code",
  "main": "index.js",
  "dependencies": {
    "chokidar": "^3.5.3",
    "express": "^4.18.2",
    "ws": "^8.14.2"
  }
}
```

**Step 2: Create minimal server that starts**

```javascript
const express = require('express');
const http = require('http');
const WebSocket = require('ws');
const chokidar = require('chokidar');
const fs = require('fs');
const path = require('path');

const PORT = process.env.BRAINSTORM_PORT || 3333;
const SCREEN_FILE = process.env.BRAINSTORM_SCREEN || '/tmp/brainstorm/screen.html';
const SCREEN_DIR = path.dirname(SCREEN_FILE);

// Ensure screen directory exists
if (!fs.existsSync(SCREEN_DIR)) {
  fs.mkdirSync(SCREEN_DIR, { recursive: true });
}

// Create default screen if none exists
if (!fs.existsSync(SCREEN_FILE)) {
  fs.writeFileSync(SCREEN_FILE, `<!DOCTYPE html>
<html>
<head>
  <title>Brainstorm Companion</title>
  <style>
    body { font-family: system-ui, sans-serif; padding: 2rem; max-width: 800px; margin: 0 auto; }
    h1 { color: #333; }
    p { color: #666; }
  </style>
</head>
<body>
  <h1>Brainstorm Companion</h1>
  <p>Waiting for Claude to push a screen...</p>
</body>
</html>`);
}

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

// Track connected browsers for reload notifications
const clients = new Set();

wss.on('connection', (ws) => {
  clients.add(ws);
  ws.on('close', () => clients.delete(ws));

  ws.on('message', (data) => {
    // User interaction event - write to stdout for Claude
    const event = JSON.parse(data.toString());
    console.log(JSON.stringify({ type: 'user-event', ...event }));
  });
});

// Serve current screen with helper.js injected
app.get('/', (req, res) => {
  let html = fs.readFileSync(SCREEN_FILE, 'utf-8');

  // Inject helper script before </body>
  const helperScript = fs.readFileSync(path.join(__dirname, 'helper.js'), 'utf-8');
  const injection = `<script>\n${helperScript}\n</script>`;

  if (html.includes('</body>')) {
    html = html.replace('</body>', `${injection}\n</body>`);
  } else {
    html += injection;
  }

  res.type('html').send(html);
});

// Watch for screen file changes
chokidar.watch(SCREEN_FILE).on('change', () => {
  console.log(JSON.stringify({ type: 'screen-updated', file: SCREEN_FILE }));
  // Notify all browsers to reload
  clients.forEach(ws => {
    if (ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify({ type: 'reload' }));
    }
  });
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(JSON.stringify({ type: 'server-started', port: PORT, url: `http://localhost:${PORT}` }));
});
```

**Step 3: Run npm install**

Run: `cd lib/brainstorm-server && npm install`
Expected: Dependencies installed

**Step 4: Test server starts**

Run: `cd lib/brainstorm-server && timeout 3 node index.js || true`
Expected: See JSON with `server-started` and port info

**Step 5: Commit**

```bash
git add lib/brainstorm-server/
git commit -m "feat: add brainstorm server foundation"
```

---

## Task 2: Create the Helper Library

**Files:**
- Create: `lib/brainstorm-server/helper.js`

**Step 1: Create helper.js with event auto-capture**

```javascript
(function() {
  const WS_URL = 'ws://' + window.location.host;
  let ws = null;
  let eventQueue = [];

  function connect() {
    ws = new WebSocket(WS_URL);

    ws.onopen = () => {
      // Send any queued events
      eventQueue.forEach(e => ws.send(JSON.stringify(e)));
      eventQueue = [];
    };

    ws.onmessage = (msg) => {
      const data = JSON.parse(msg.data);
      if (data.type === 'reload') {
        window.location.reload();
      }
    };

    ws.onclose = () => {
      // Reconnect after 1 second
      setTimeout(connect, 1000);
    };
  }

  function send(event) {
    event.timestamp = Date.now();
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(event));
    } else {
      eventQueue.push(event);
    }
  }

  // Auto-capture clicks on interactive elements
  document.addEventListener('click', (e) => {
    const target = e.target.closest('button, a, [data-choice], [role="button"], input[type="submit"]');
    if (!target) return;

    // Don't capture regular link navigation
    if (target.tagName === 'A' && !target.dataset.choice) return;

    e.preventDefault();

    send({
      type: 'click',
      text: target.textContent.trim(),
      choice: target.dataset.choice || null,
      id: target.id || null,
      className: target.className || null
    });
  });

  // Auto-capture form submissions
  document.addEventListener('submit', (e) => {
    e.preventDefault();
    const form = e.target;
    const formData = new FormData(form);
    const data = {};
    formData.forEach((value, key) => { data[key] = value; });

    send({
      type: 'submit',
      formId: form.id || null,
      formName: form.name || null,
      data: data
    });
  });

  // Auto-capture input changes (debounced)
  let inputTimeout = null;
  document.addEventListener('input', (e) => {
    const target =

# FILE: docs/plans/2025-11-28-skills-improvements-from-user-feedback.md

# Skills Improvements from User Feedback

**Date:** 2025-11-28
**Status:** Draft
**Source:** Two Claude instances using superpowers in real development scenarios

---

## Executive Summary

Two Claude instances provided detailed feedback from actual development sessions. Their feedback reveals **systematic gaps** in current skills that allowed preventable bugs to ship despite following the skills.

**Critical insight:** These are problem reports, not just solution proposals. The problems are real; the solutions need careful evaluation.

**Key themes:**
1. **Verification gaps** - We verify operations succeed but not that they achieve intended outcomes
2. **Process hygiene** - Background processes accumulate and interfere across subagents
3. **Context optimization** - Subagents get too much irrelevant information
4. **Self-reflection missing** - No prompt to critique own work before handoff
5. **Mock safety** - Mocks can drift from interfaces without detection
6. **Skill activation** - Skills exist but aren't being read/used

---

## Problems Identified

### Problem 1: Configuration Change Verification Gap

**What happened:**
- Subagent tested "OpenAI integration"
- Set `OPENAI_API_KEY` env var
- Got status 200 responses
- Reported "OpenAI integration working"
- **BUT** response contained `"model": "claude-sonnet-4-20250514"` - was actually using Anthropic

**Root cause:**
`verification-before-completion` checks operations succeed but not that outcomes reflect intended configuration changes.

**Impact:** High - False confidence in integration tests, bugs ship to production

**Example failure pattern:**
- Switch LLM provider → verify status 200 but don't check model name
- Enable feature flag → verify no errors but don't check feature is active
- Change environment → verify deployment succeeds but don't check environment vars

---

### Problem 2: Background Process Accumulation

**What happened:**
- Multiple subagents dispatched during session
- Each started background server processes
- Processes accumulated (4+ servers running)
- Stale processes still bound to ports
- Later E2E test hit stale server with wrong config
- Confusing/incorrect test results

**Root cause:**
Subagents are stateless - don't know about previous subagents' processes. No cleanup protocol.

**Impact:** Medium-High - Tests hit wrong server, false passes/failures, debugging confusion

---

### Problem 3: Context Bloat in Subagent Prompts

**What happened:**
- Standard approach: give subagent full plan file to read
- Experiment: give only task + pattern + file + verify command
- Result: Faster, more focused, single-attempt completion more common

**Root cause:**
Subagents waste tokens and attention on irrelevant plan sections.

**Impact:** Medium - Slower execution, more failed attempts

**What worked:**
```
You are adding a single E2E test to packnplay's test suite.

**Your task:** Add `TestE2E_FeaturePrivilegedMode` to `pkg/runner/e2e_test.go`

**What to test:** A local devcontainer feature that requests `"privileged": true`
in its metadata should result in the container running with `--privileged` flag.

**Follow the exact pattern of TestE2E_FeatureOptionValidation** (at the end of the file)

**After writing, run:** `go test -v ./pkg/runner -run TestE2E_FeaturePrivilegedMode -timeout 5m`
```

---

### Problem 4: No Self-Reflection Before Handoff

**What happened:**
- Added self-reflection prompt: "Look at your work with fresh eyes - what could be better?"
- Implementer for Task 5 identified failing test was due to implementation bug, not test bug
- Traced to line 99: `strings.Join(metadata.Entrypoint, " ")` creating invalid Docker syntax
- Without self-reflection, would have just reported "test fails" without root cause

**Root cause:**
Implementers don't naturally step back and critique their own work before reporting completion.

**Impact:** Medium - Bugs handed off to reviewer that implementer could have caught

---

### Problem 5: Mock-Interface Drift

**What happened:**
```typescript
// Interface defines close()
interface PlatformAdapter {
  close(): Promise<void>;
}

// Code (BUGGY) calls cleanup()
await adapter.cleanup();

// Mock (MATCHES BUG) defines cleanup()
vi.mock('web-adapter', () => ({
  WebAdapter: vi.fn().mockImplementation(() => ({
    cleanup: vi.fn().mockResolvedValue(undefined),  // Wrong!
  })),
}));
```
- Tests passed
- Runtime crashed: "adapter.cleanup is not a function"

**Root cause:**
Mock derived from what buggy code calls, not from interface definition. TypeScript can't catch inline mocks with wrong method names.

**Impact:** High - Tests give false confidence, runtime crashes

**Why testing-anti-patterns didn't prevent this:**
The skill covers testing mock behavior and mocking without understanding, but not the specific pattern of "derive mock from interface, not implementation."

---

### Problem 6: Code Reviewer File Access

**What happened:**
- Code reviewer subagent dispatched
- Couldn't find test file: "The file doesn't appear to exist in the repository"
- File actually exists
- Reviewer didn't know to explicitly read it first

**Root cause:**
Reviewer prompts don't include explicit file reading instructions.

**Impact:** Low-Medium - Reviews fail or incomplete

---

### Problem 7: Fix Workflow Latency

**What happened:**
- Implementer identifies bug during self-reflection
- Implementer knows the fix
- Current workflow: report → I dispatch fixer → fixer fixes → I verify
- Extra round-trip adds latency without adding value

**Root cause:**
Rigid separation between implementer and fixer roles when implementer has already diagnosed.

**Impact:** Low - Latency, but no correctness issue

---

### Problem 8: Skills Not Being Read

**What happened:**
- `testing-anti-patterns` skill exists
- Neither human nor subagents read it before writing tests
- Would have prevented some issues (though not all - see Problem 5)

**Root cause:**
No enforcement that subagents read relevant skills. No promp

# FILE: docs/windows/polyglot-hooks.md

# Cross-Platform Polyglot Hooks for Claude Code

Claude Code plugins need hooks that work on Windows, macOS, and Linux. This document explains the polyglot wrapper technique that makes this possible.

## The Problem

Claude Code runs hook commands through the system's default shell:
- **Windows**: CMD.exe
- **macOS/Linux**: bash or sh

This creates several challenges:

1. **Script execution**: Windows CMD can't execute `.sh` files directly - it tries to open them in a text editor
2. **Path format**: Windows uses backslashes (`C:\path`), Unix uses forward slashes (`/path`)
3. **Environment variables**: `$VAR` syntax doesn't work in CMD
4. **No `bash` in PATH**: Even with Git Bash installed, `bash` isn't in the PATH when CMD runs

## The Solution: Polyglot `.cmd` Wrapper

A polyglot script is valid syntax in multiple languages simultaneously. Our wrapper is valid in both CMD and bash:

```cmd
: << 'CMDBLOCK'
@echo off
"C:\Program Files\Git\bin\bash.exe" -l -c "\"$(cygpath -u \"$CLAUDE_PLUGIN_ROOT\")/hooks/session-start.sh\""
exit /b
CMDBLOCK

# Unix shell runs from here
"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.sh"
```

### How It Works

#### On Windows (CMD.exe)

1. `: << 'CMDBLOCK'` - CMD sees `:` as a label (like `:label`) and ignores `<< 'CMDBLOCK'`
2. `@echo off` - Suppresses command echoing
3. The bash.exe command runs with:
   - `-l` (login shell) to get proper PATH with Unix utilities
   - `cygpath -u` converts Windows path to Unix format (`C:\foo` → `/c/foo`)
4. `exit /b` - Exits the batch script, stopping CMD here
5. Everything after `CMDBLOCK` is never reached by CMD

#### On Unix (bash/sh)

1. `: << 'CMDBLOCK'` - `:` is a no-op, `<< 'CMDBLOCK'` starts a heredoc
2. Everything until `CMDBLOCK` is consumed by the heredoc (ignored)
3. `# Unix shell runs from here` - Comment
4. The script runs directly with the Unix path

## File Structure

```
hooks/
├── hooks.json           # Points to the .cmd wrapper
├── session-start.cmd    # Polyglot wrapper (cross-platform entry point)
└── session-start.sh     # Actual hook logic (bash script)
```

### hooks.json

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/session-start.cmd\""
          }
        ]
      }
    ]
  }
}
```

Note: The path must be quoted because `${CLAUDE_PLUGIN_ROOT}` may contain spaces on Windows (e.g., `C:\Program Files\...`).

## Requirements

### Windows
- **Git for Windows** must be installed (provides `bash.exe` and `cygpath`)
- Default installation path: `C:\Program Files\Git\bin\bash.exe`
- If Git is installed elsewhere, the wrapper needs modification

### Unix (macOS/Linux)
- Standard bash or sh shell
- The `.cmd` file must have execute permission (`chmod +x`)

## Writing Cross-Platform Hook Scripts

Your actual hook logic goes in the `.sh` file. To ensure it works on Windows (via Git Bash):

### Do:
- Use pure bash builtins when possible
- Use `$(command)` instead of backticks
- Quote all variable expansions: `"$VAR"`
- Use `printf` or here-docs for output

### Avoid:
- External commands that may not be in PATH (sed, awk, grep)
- If you must use them, they're available in Git Bash but ensure PATH is set up (use `bash -l`)

### Example: JSON Escaping Without sed/awk

Instead of:
```bash
escaped=$(echo "$content" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g' | awk '{printf "%s\\n", $0}')
```

Use pure bash:
```bash
escape_for_json() {
    local input="$1"
    local output=""
    local i char
    for (( i=0; i<${#input}; i++ )); do
        char="${input:$i:1}"
        case "$char" in
            $'\\') output+='\\' ;;
            '"') output+='\"' ;;
            $'\n') output+='\n' ;;
            $'\r') output+='\r' ;;
            $'\t') output+='\t' ;;
            *) output+="$char" ;;
        esac
    done
    printf '%s' "$output"
}
```

## Reusable Wrapper Pattern

For plugins with multiple hooks, you can create a generic wrapper that takes the script name as an argument:

### run-hook.cmd
```cmd
: << 'CMDBLOCK'
@echo off
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_NAME=%~1"
"C:\Program Files\Git\bin\bash.exe" -l -c "cd \"$(cygpath -u \"%SCRIPT_DIR%\")\" && \"./%SCRIPT_NAME%\""
exit /b
CMDBLOCK

# Unix shell runs from here
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SCRIPT_NAME="$1"
shift
"${SCRIPT_DIR}/${SCRIPT_NAME}" "$@"
```

### hooks.json using the reusable wrapper
```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd\" session-start.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd\" validate-bash.sh"
          }
        ]
      }
    ]
  }
}
```

## Troubleshooting

### "bash is not recognized"
CMD can't find bash. The wrapper uses the full path `C:\Program Files\Git\bin\bash.exe`. If Git is installed elsewhere, update the path.

### "cygpath: command not found" or "dirname: command not found"
Bash isn't running as a login shell. Ensure `-l` flag is used.

### Path has weird `\/` in it
`${CLAUDE_PLUGIN_ROOT}` expanded to a Windows path ending with backslash, then `/hooks/...` was appended. Use `cygpath` to convert the entire path.

### Script opens in text editor instead of running
The hooks.json is pointing directly to the `.sh` file. Point to the `.cmd` wrapper instead.

### Works in terminal but not as hook
Claude Code may run hooks differently. Test by simulating the hook environment:
```powershell
$env:CLAUDE_PLUGIN_ROOT = "C:\path\to\plugin"
cmd /c "C:\path\to\plugin\hooks\session-start.cmd"
```

## Related Issues

- [anthropics/claude-code#9758](https://github.com/anthropics/claude-code/issues/9758) - .sh scripts open

# FILE: docs/superpowers/plans/2026-01-22-document-review-system.md

# Document Review System Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan.

**Goal:** Add spec and plan document review loops to the brainstorming and writing-plans skills.

**Architecture:** Create reviewer prompt templates in each skill directory. Modify skill files to add review loops after document creation. Use Task tool with general-purpose subagent for reviewer dispatch.

**Tech Stack:** Markdown skill files, subagent dispatch via Task tool

**Spec:** docs/superpowers/specs/2026-01-22-document-review-system-design.md

---

## Chunk 1: Spec Document Reviewer

This chunk adds the spec document reviewer to the brainstorming skill.

### Task 1: Create Spec Document Reviewer Prompt Template

**Files:**
- Create: `skills/brainstorming/spec-document-reviewer-prompt.md`

- [ ] **Step 1:** Create the reviewer prompt template file

```markdown
# Spec Document Reviewer Prompt Template

Use this template when dispatching a spec document reviewer subagent.

**Purpose:** Verify the spec is complete, consistent, and ready for implementation planning.

**Dispatch after:** Spec document is written to docs/superpowers/specs/

```
Task tool (general-purpose):
  description: "Review spec document"
  prompt: |
    You are a spec document reviewer. Verify this spec is complete and ready for planning.

    **Spec to review:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, "TBD", incomplete sections |
    | Coverage | Missing error handling, edge cases, integration points |
    | Consistency | Internal contradictions, conflicting requirements |
    | Clarity | Ambiguous requirements |
    | YAGNI | Unrequested features, over-engineering |

    ## CRITICAL

    Look especially hard for:
    - Any TODO markers or placeholder text
    - Sections saying "to be defined later" or "will spec when X is done"
    - Sections noticeably less detailed than others

    ## Output Format

    ## Spec Review

    **Status:** ✅ Approved | ❌ Issues Found

    **Issues (if any):**
    - [Section X]: [specific issue] - [why it matters]

    **Recommendations (advisory):**
    - [suggestions that don't block approval]
```

**Reviewer returns:** Status, Issues (if any), Recommendations
```

- [ ] **Step 2:** Verify the file was created correctly

Run: `cat skills/brainstorming/spec-document-reviewer-prompt.md | head -20`
Expected: Shows the header and purpose section

- [ ] **Step 3:** Commit

```bash
git add skills/brainstorming/spec-document-reviewer-prompt.md
git commit -m "feat: add spec document reviewer prompt template"
```

---

### Task 2: Add Review Loop to Brainstorming Skill

**Files:**
- Modify: `skills/brainstorming/SKILL.md`

- [ ] **Step 1:** Read the current brainstorming skill

Run: `cat skills/brainstorming/SKILL.md`

- [ ] **Step 2:** Add the review loop section after "After the Design"

Find the "After the Design" section and add a new "Spec Review Loop" section after documentation but before implementation:

```markdown
**Spec Review Loop:**
After writing the spec document:
1. Dispatch spec-document-reviewer subagent (see spec-document-reviewer-prompt.md)
2. If ❌ Issues Found:
   - Fix the issues in the spec document
   - Re-dispatch reviewer
   - Repeat until ✅ Approved
3. If ✅ Approved: proceed to implementation setup

**Review loop guidance:**
- Same agent that wrote the spec fixes it (preserves context)
- If loop exceeds 5 iterations, surface to human for guidance
- Reviewers are advisory - explain disagreements if you believe feedback is incorrect
```

- [ ] **Step 3:** Verify the changes

Run: `grep -A 15 "Spec Review Loop" skills/brainstorming/SKILL.md`
Expected: Shows the new review loop section

- [ ] **Step 4:** Commit

```bash
git add skills/brainstorming/SKILL.md
git commit -m "feat: add spec review loop to brainstorming skill"
```

---

## Chunk 2: Plan Document Reviewer

This chunk adds the plan document reviewer to the writing-plans skill.

### Task 3: Create Plan Document Reviewer Prompt Template

**Files:**
- Create: `skills/writing-plans/plan-document-reviewer-prompt.md`

- [ ] **Step 1:** Create the reviewer prompt template file

```markdown
# Plan Document Reviewer Prompt Template

Use this template when dispatching a plan document reviewer subagent.

**Purpose:** Verify the plan chunk is complete, matches the spec, and has proper task decomposition.

**Dispatch after:** Each plan chunk is written

```
Task tool (general-purpose):
  description: "Review plan chunk N"
  prompt: |
    You are a plan document reviewer. Verify this plan chunk is complete and ready for implementation.

    **Plan chunk to review:** [PLAN_FILE_PATH] - Chunk N only
    **Spec for reference:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, incomplete tasks, missing steps |
    | Spec Alignment | Chunk covers relevant spec requirements, no scope creep |
    | Task Decomposition | Tasks atomic, clear boundaries, steps actionable |
    | Task Syntax | Checkbox syntax (`- [ ]`) on tasks and steps |
    | Chunk Size | Each chunk under 1000 lines |

    ## CRITICAL

    Look especially hard for:
    - Any TODO markers or placeholder text
    - Steps that say "similar to X" without actual content
    - Incomplete task definitions
    - Missing verification steps or expected outputs

    ## Output Format

    ## Plan Review - Chunk N

    **Status:** ✅ Approved | ❌ Issues Found

    **Issues (if any):**
    - [Task X, Step Y]: [specific issue] - [why it matters]

    **Recommendations (advisory):**
    - [suggestions that don't block approval]
```

**Reviewer returns:** Status, Issues (if any), Recommendations
```

- [ ] **Step 2:** Verify the file was created

Run: `cat skills/

# FILE: docs/superpowers/plans/2026-03-23-codex-app-compatibility.md

# Codex App Compatibility Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make `using-git-worktrees`, `finishing-a-development-branch`, and related skills work in the Codex App's sandboxed worktree environment without breaking existing behavior.

**Architecture:** Read-only environment detection (`git-dir` vs `git-common-dir`) at the start of two skills. If already in a linked worktree, skip creation. If on detached HEAD, emit a handoff payload instead of the 4-option menu. Sandbox fallback catches permission errors during worktree creation.

**Tech Stack:** Git, Markdown (skill files are instruction documents, not executable code)

**Spec:** `docs/superpowers/specs/2026-03-23-codex-app-compatibility-design.md`

---

## File Structure

| File | Responsibility | Action |
|---|---|---|
| `skills/using-git-worktrees/SKILL.md` | Worktree creation + isolation | Add Step 0 detection + sandbox fallback |
| `skills/finishing-a-development-branch/SKILL.md` | Branch finishing workflow | Add Step 1.5 detection + cleanup guard |
| `skills/subagent-driven-development/SKILL.md` | Plan execution with subagents | Update Integration description |
| `skills/executing-plans/SKILL.md` | Plan execution inline | Update Integration description |
| `skills/using-superpowers/references/codex-tools.md` | Codex platform reference | Add detection + finishing docs |

---

### Task 1: Add Step 0 to `using-git-worktrees`

**Files:**
- Modify: `skills/using-git-worktrees/SKILL.md:14-15` (insert after Overview, before Directory Selection Process)

- [ ] **Step 1: Read the current skill file**

Read `skills/using-git-worktrees/SKILL.md` in full. Identify the exact insertion point: after the "Announce at start" line (line 14) and before "## Directory Selection Process" (line 16).

- [ ] **Step 2: Insert Step 0 section**

Insert the following between the Overview section and "## Directory Selection Process":

```markdown
## Step 0: Check if Already in an Isolated Workspace

Before creating a worktree, check if one already exists:

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

**If `GIT_DIR` differs from `GIT_COMMON`:** You are already inside a linked worktree (created by the Codex App, Claude Code's Agent tool, a previous skill run, or the user). Do NOT create another worktree. Instead:

1. Run project setup (auto-detect package manager as in "Run Project Setup" below)
2. Verify clean baseline (run tests as in "Verify Clean Baseline" below)
3. Report with branch state:
   - On a branch: "Already in an isolated workspace at `<path>` on branch `<name>`. Tests passing. Ready to implement."
   - Detached HEAD: "Already in an isolated workspace at `<path>` (detached HEAD, externally managed). Tests passing. Note: branch creation needed at finish time. Ready to implement."

After reporting, STOP. Do not continue to Directory Selection or Creation Steps.

**If `GIT_DIR` equals `GIT_COMMON`:** Proceed with the full worktree creation flow below.

**Sandbox fallback:** If you proceed to Creation Steps but `git worktree add -b` fails with a permission error (e.g., "Operation not permitted"), treat this as a late-detected restricted environment. Fall back to the behavior above — run setup and baseline tests in the current directory, report accordingly, and STOP.
```

- [ ] **Step 3: Verify the insertion**

Read the file again. Confirm:
- Step 0 appears between Overview and Directory Selection Process
- The rest of the file (Directory Selection, Safety Verification, Creation Steps, etc.) is unchanged
- No duplicate sections or broken markdown

- [ ] **Step 4: Commit**

```bash
git add skills/using-git-worktrees/SKILL.md
git commit -m "feat(using-git-worktrees): add Step 0 environment detection (PRI-823)

Skip worktree creation when already in a linked worktree. Includes
sandbox fallback for permission errors on git worktree add."
```

---

### Task 2: Update `using-git-worktrees` Integration section

**Files:**
- Modify: `skills/using-git-worktrees/SKILL.md:211-215` (Integration > Called by)

- [ ] **Step 1: Update the three "Called by" entries**

Change lines 212-214 from:

```markdown
- **brainstorming** (Phase 4) - REQUIRED when design is approved and implementation follows
- **subagent-driven-development** - REQUIRED before executing any tasks
- **executing-plans** - REQUIRED before executing any tasks
```

To:

```markdown
- **brainstorming** - REQUIRED: Ensures isolated workspace (creates one or verifies existing)
- **subagent-driven-development** - REQUIRED: Ensures isolated workspace (creates one or verifies existing)
- **executing-plans** - REQUIRED: Ensures isolated workspace (creates one or verifies existing)
```

- [ ] **Step 2: Verify the Integration section**

Read the Integration section. Confirm all three entries are updated, "Pairs with" is unchanged.

- [ ] **Step 3: Commit**

```bash
git add skills/using-git-worktrees/SKILL.md
git commit -m "docs(using-git-worktrees): update Integration descriptions (PRI-823)

Clarify that skill ensures a workspace exists, not that it always creates one."
```

---

### Task 3: Add Step 1.5 to `finishing-a-development-branch`

**Files:**
- Modify: `skills/finishing-a-development-branch/SKILL.md:38` (insert after Step 1, before Step 2)

- [ ] **Step 1: Read the current skill file**

Read `skills/finishing-a-development-branch/SKILL.md` in full. Identify the insertion point: after "**If tests pass:** Continue to Step 2." (line 38) and before "### Step 2: Determine Base Branch" (line 40).

- [ ] **Step 2: Insert Step 1.5 section**

Insert the following between Step 1 and Step 2:

```markdown
### Step 1.5: Detect Environment

```bash
GIT_DIR=$(c

# FILE: docs/superpowers/plans/2026-02-19-visual-brainstorming-refactor.md

# Visual Brainstorming Refactor Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor visual brainstorming from blocking TUI feedback model to non-blocking "Browser Displays, Terminal Commands" architecture.

**Architecture:** Browser becomes an interactive display; terminal stays the conversation channel. Server writes user events to a per-screen `.events` file that Claude reads on its next turn. Eliminates `wait-for-feedback.sh` and all `TaskOutput` blocking.

**Tech Stack:** Node.js (Express, ws, chokidar), vanilla HTML/CSS/JS

**Spec:** `docs/superpowers/specs/2026-02-19-visual-brainstorming-refactor-design.md`

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `lib/brainstorm-server/index.js` | Modify | Server: add `.events` file writing, clear on new screen, replace `wrapInFrame` |
| `lib/brainstorm-server/frame-template.html` | Modify | Template: remove feedback footer, add content placeholder + selection indicator |
| `lib/brainstorm-server/helper.js` | Modify | Client JS: remove send/feedback functions, narrow to click capture + indicator updates |
| `lib/brainstorm-server/wait-for-feedback.sh` | Delete | No longer needed |
| `skills/brainstorming/visual-companion.md` | Modify | Skill instructions: rewrite loop to non-blocking flow |
| `tests/brainstorm-server/server.test.js` | Modify | Tests: update for new template structure and helper.js API |

---

## Chunk 1: Server, Template, Client, Tests, Skill

### Task 1: Update `frame-template.html`

**Files:**
- Modify: `lib/brainstorm-server/frame-template.html`

- [ ] **Step 1: Remove the feedback footer HTML**

Replace the feedback-footer div (lines 227-233) with a selection indicator bar:

```html
  <div class="indicator-bar">
    <span id="indicator-text">Click an option above, then return to the terminal</span>
  </div>
```

Also replace the default content inside `#claude-content` (lines 220-223) with the content placeholder:

```html
    <div id="claude-content">
      <!-- CONTENT -->
    </div>
```

- [ ] **Step 2: Replace feedback footer CSS with indicator bar CSS**

Remove the `.feedback-footer`, `.feedback-footer label`, `.feedback-row`, and the textarea/button styles within `.feedback-footer` (lines 82-112).

Add indicator bar CSS:

```css
    .indicator-bar {
      background: var(--bg-secondary);
      border-top: 1px solid var(--border);
      padding: 0.5rem 1.5rem;
      flex-shrink: 0;
      text-align: center;
    }
    .indicator-bar span {
      font-size: 0.75rem;
      color: var(--text-secondary);
    }
    .indicator-bar .selected-text {
      color: var(--accent);
      font-weight: 500;
    }
```

- [ ] **Step 3: Verify template renders**

Run the test suite to check the template still loads:
```bash
cd /Users/drewritter/prime-rad/superpowers && node tests/brainstorm-server/server.test.js
```
Expected: Tests 1-5 should still pass. Tests 6-8 may fail (expected — they assert old structure).

- [ ] **Step 4: Commit**

```bash
git add lib/brainstorm-server/frame-template.html
git commit -m "Replace feedback footer with selection indicator bar in brainstorm template"
```

---

### Task 2: Update `index.js` — content injection and `.events` file

**Files:**
- Modify: `lib/brainstorm-server/index.js`

- [ ] **Step 1: Write failing test for `.events` file writing**

Add to `tests/brainstorm-server/server.test.js` after Test 4 area — a new test that sends a WebSocket event with a `choice` field and verifies `.events` file is written:

```javascript
    // Test: Choice events written to .events file
    console.log('Test: Choice events written to .events file');
    const ws3 = new WebSocket(`ws://localhost:${TEST_PORT}`);
    await new Promise(resolve => ws3.on('open', resolve));

    ws3.send(JSON.stringify({ type: 'click', choice: 'a', text: 'Option A' }));
    await sleep(300);

    const eventsFile = path.join(TEST_DIR, '.events');
    assert(fs.existsSync(eventsFile), '.events file should exist after choice click');
    const lines = fs.readFileSync(eventsFile, 'utf-8').trim().split('\n');
    const event = JSON.parse(lines[lines.length - 1]);
    assert.strictEqual(event.choice, 'a', 'Event should contain choice');
    assert.strictEqual(event.text, 'Option A', 'Event should contain text');
    ws3.close();
    console.log('  PASS');
```

- [ ] **Step 2: Run test to verify it fails**

```bash
cd /Users/drewritter/prime-rad/superpowers && node tests/brainstorm-server/server.test.js
```
Expected: New test FAILS — `.events` file doesn't exist yet.

- [ ] **Step 3: Write failing test for `.events` file clearing on new screen**

Add another test:

```javascript
    // Test: .events cleared on new screen
    console.log('Test: .events cleared on new screen');
    // .events file should still exist from previous test
    assert(fs.existsSync(path.join(TEST_DIR, '.events')), '.events should exist before new screen');
    fs.writeFileSync(path.join(TEST_DIR, 'new-screen.html'), '<h2>New screen</h2>');
    await sleep(500);
    assert(!fs.existsSync(path.join(TEST_DIR, '.events')), '.events should be cleared after new screen');
    console.log('  PASS');
```

- [ ] **Step 4: Run test to verify it fails**

```bash
cd /Users/drewritter/prime-rad/superpowers && node tests/brainstorm-server/server.test.js
```
Expected: New test FAILS — `.events` not cleared on screen push.

- [ ] **Step 5: Implement `.events` file writing in `index.js`**

In the WebSocket `message` handler (line 74-77 of `index.js`), after the `console.log`, add:

```javascript
    // Write user events to .events file for Claude to read
    if (event.choice) {
      const eventsFile = path.join(SCREEN_DIR, '.events');
      fs.appendFileSync(eventsFile, JSON.stringify(event) + '\n');
    }
```

In the chokidar `add` handle

# FILE: docs/superpowers/plans/2026-03-11-zero-dep-brainstorm-server.md

# Zero-Dependency Brainstorm Server Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the brainstorm server's vendored node_modules with a single zero-dependency `server.js` using Node built-ins.

**Architecture:** Single file with WebSocket protocol (RFC 6455 text frames), HTTP server (`http` module), and file watching (`fs.watch`). Exports protocol functions for unit testing when required as a module.

**Tech Stack:** Node.js built-ins only: `http`, `crypto`, `fs`, `path`

**Spec:** `docs/superpowers/specs/2026-03-11-zero-dep-brainstorm-server-design.md`

**Existing tests:** `tests/brainstorm-server/ws-protocol.test.js` (unit), `tests/brainstorm-server/server.test.js` (integration)

---

## File Map

- **Create:** `skills/brainstorming/scripts/server.js` — the zero-dep replacement
- **Modify:** `skills/brainstorming/scripts/start-server.sh:94,100` — change `index.js` to `server.js`
- **Modify:** `.gitignore:6` — remove the `!skills/brainstorming/scripts/node_modules/` exception
- **Delete:** `skills/brainstorming/scripts/index.js`
- **Delete:** `skills/brainstorming/scripts/package.json`
- **Delete:** `skills/brainstorming/scripts/package-lock.json`
- **Delete:** `skills/brainstorming/scripts/node_modules/` (714 files)
- **No changes:** `skills/brainstorming/scripts/helper.js`, `skills/brainstorming/scripts/frame-template.html`, `skills/brainstorming/scripts/stop-server.sh`

---

## Chunk 1: WebSocket Protocol Layer

### Task 1: Implement WebSocket protocol exports

**Files:**
- Create: `skills/brainstorming/scripts/server.js`
- Test: `tests/brainstorm-server/ws-protocol.test.js` (already exists)

- [ ] **Step 1: Create server.js with OPCODES constant and computeAcceptKey**

```js
const crypto = require('crypto');

const OPCODES = { TEXT: 0x01, CLOSE: 0x08, PING: 0x09, PONG: 0x0A };
const WS_MAGIC = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11';

function computeAcceptKey(clientKey) {
  return crypto.createHash('sha1').update(clientKey + WS_MAGIC).digest('base64');
}
```

- [ ] **Step 2: Implement encodeFrame**

Server frames are never masked. Three length encodings:
- payload < 126: 2-byte header (FIN+opcode, length)
- 126-65535: 4-byte header (FIN+opcode, 126, 16-bit length)
- &gt; 65535: 10-byte header (FIN+opcode, 127, 64-bit length)

```js
function encodeFrame(opcode, payload) {
  const fin = 0x80;
  const len = payload.length;
  let header;

  if (len < 126) {
    header = Buffer.alloc(2);
    header[0] = fin | opcode;
    header[1] = len;
  } else if (len < 65536) {
    header = Buffer.alloc(4);
    header[0] = fin | opcode;
    header[1] = 126;
    header.writeUInt16BE(len, 2);
  } else {
    header = Buffer.alloc(10);
    header[0] = fin | opcode;
    header[1] = 127;
    header.writeBigUInt64BE(BigInt(len), 2);
  }

  return Buffer.concat([header, payload]);
}
```

- [ ] **Step 3: Implement decodeFrame**

Client frames are always masked. Returns `{ opcode, payload, bytesConsumed }` or `null` for incomplete. Throws on unmasked frames.

```js
function decodeFrame(buffer) {
  if (buffer.length < 2) return null;

  const firstByte = buffer[0];
  const secondByte = buffer[1];
  const opcode = firstByte & 0x0F;
  const masked = (secondByte & 0x80) !== 0;
  let payloadLen = secondByte & 0x7F;
  let offset = 2;

  if (!masked) throw new Error('Client frames must be masked');

  if (payloadLen === 126) {
    if (buffer.length < 4) return null;
    payloadLen = buffer.readUInt16BE(2);
    offset = 4;
  } else if (payloadLen === 127) {
    if (buffer.length < 10) return null;
    payloadLen = Number(buffer.readBigUInt64BE(2));
    offset = 10;
  }

  const maskOffset = offset;
  const dataOffset = offset + 4;
  const totalLen = dataOffset + payloadLen;
  if (buffer.length < totalLen) return null;

  const mask = buffer.slice(maskOffset, dataOffset);
  const data = Buffer.alloc(payloadLen);
  for (let i = 0; i < payloadLen; i++) {
    data[i] = buffer[dataOffset + i] ^ mask[i % 4];
  }

  return { opcode, payload: data, bytesConsumed: totalLen };
}
```

- [ ] **Step 4: Add module exports at the bottom of the file**

```js
module.exports = { computeAcceptKey, encodeFrame, decodeFrame, OPCODES };
```

- [ ] **Step 5: Run unit tests**

Run: `cd tests/brainstorm-server && node ws-protocol.test.js`
Expected: All tests pass (handshake, encoding, decoding, boundaries, edge cases)

- [ ] **Step 6: Commit**

```bash
git add skills/brainstorming/scripts/server.js
git commit -m "Add WebSocket protocol layer for zero-dep brainstorm server"
```

---

## Chunk 2: HTTP Server and Application Logic

### Task 2: Add HTTP server, file watching, and WebSocket connection handling

**Files:**
- Modify: `skills/brainstorming/scripts/server.js`
- Test: `tests/brainstorm-server/server.test.js` (already exists)

- [ ] **Step 1: Add configuration and constants at top of server.js (after requires)**

```js
const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = process.env.BRAINSTORM_PORT || (49152 + Math.floor(Math.random() * 16383));
const HOST = process.env.BRAINSTORM_HOST || '127.0.0.1';
const URL_HOST = process.env.BRAINSTORM_URL_HOST || (HOST === '127.0.0.1' ? 'localhost' : HOST);
const SCREEN_DIR = process.env.BRAINSTORM_DIR || '/tmp/brainstorm';

const MIME_TYPES = {
  '.html': 'text/html', '.css': 'text/css', '.js': 'application/javascript',
  '.json': 'application/json', '.png': 'image/png', '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.svg': 'image/svg+xml'
};
```

- [ ] **Step 2: Add WAITING_PAGE, template loading at module scope, and helper functions**

Load `frameTemplate` and `helperInjection` at module scope so they're accessible to `wrapInFrame` and `handleRequest`. They only read files from `__dirname` (the scripts directory), which is val

# FILE: docs/superpowers/plans/2026-04-06-worktree-rototill.md

# Worktree Rototill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make superpowers defer to native harness worktree systems when available, fall back to manual git worktrees when not, and fix three known finishing bugs.

**Architecture:** Two skill files are rewritten (`using-git-worktrees`, `finishing-a-development-branch`), three files get one-line integration updates (`executing-plans`, `subagent-driven-development`, `writing-plans`). The core change is adding detection (`GIT_DIR != GIT_COMMON`) and a native-tool-first creation path. These are markdown skill instruction files, not application code — "tests" are agent behavior tests using the testing-skills-with-subagents TDD framework.

**Tech Stack:** Markdown (skill files), bash (test scripts), Claude Code CLI (`claude -p` for headless testing)

**Spec:** `docs/superpowers/specs/2026-04-06-worktree-rototill-design.md`

---

### Task 1: GATE — TDD Validation of Step 1a (Native Tool Preference)

Step 1a is the load-bearing assumption of the entire design. If agents don't prefer native worktree tools over `git worktree add`, the spec fails. Validate this FIRST, before touching any skill files.

**Files:**
- Create: `tests/claude-code/test-worktree-native-preference.sh`
- Read: `skills/using-git-worktrees/SKILL.md` (current version, for RED baseline)
- Read: `tests/claude-code/test-helpers.sh` (for `run_claude`, `assert_contains`, etc.)
- Read: `skills/writing-skills/testing-skills-with-subagents.md` (TDD framework)

**This task is a gate.** If the GREEN phase fails after 2 REFACTOR iterations, STOP. Do not proceed to Task 2. Report back — the creation approach needs redesign.

- [ ] **Step 1: Write the RED baseline test script**

Create the test script that will run scenarios both WITHOUT and WITH the updated skill text. The RED phase runs against the current skill (which has no Step 1a).

```bash
#!/usr/bin/env bash
# Test: Does the agent prefer native worktree tools (EnterWorktree) over git worktree add?
# Framework: RED-GREEN-REFACTOR per testing-skills-with-subagents.md
#
# RED:   Current skill has no native tool preference. Agent should use git worktree add.
# GREEN: Updated skill has Step 1a. Agent should use EnterWorktree on Claude Code.

set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
source "$SCRIPT_DIR/test-helpers.sh"

# Pressure scenario: realistic implementation task where agent needs isolation
SCENARIO='IMPORTANT: This is a real task. Choose and act.

You need to implement a small feature (add a "version" field to package.json).
This should be done in an isolated workspace to protect the main branch.

You have the using-git-worktrees skill available. Set up the isolated workspace now.
Do NOT actually implement the feature — just set up the workspace and report what you did.

Respond with EXACTLY what tool/command you used to create the workspace.'

echo "=== Worktree Native Preference Test ==="
echo ""

# Phase selection
PHASE="${1:-red}"

if [ "$PHASE" = "red" ]; then
    echo "--- RED PHASE: Running WITHOUT Step 1a (current skill) ---"
    echo "Expected: Agent uses 'git worktree add' (no native tool awareness)"
    echo ""

    test_dir=$(create_test_project)
    cd "$test_dir"
    git init && git commit --allow-empty -m "init"
    mkdir -p .worktrees

    output=$(run_claude "$SCENARIO" 120)

    echo "Agent output:"
    echo "$output"
    echo ""

    # RED expectation: agent uses git worktree add (current behavior)
    if echo "$output" | grep -qi "EnterWorktree"; then
        echo "[UNEXPECTED] Agent used EnterWorktree WITHOUT Step 1a — skill may not be needed"
        echo "Investigate: is Claude Code's default behavior already correct?"
    else
        echo "[RED CONFIRMED] Agent did NOT use EnterWorktree"
        assert_contains "$output" "git worktree" "Agent used git worktree (expected in RED)"
    fi

    cleanup_test_project "$test_dir"

elif [ "$PHASE" = "green" ]; then
    echo "--- GREEN PHASE: Running WITH Step 1a (updated skill) ---"
    echo "Expected: Agent uses EnterWorktree instead of git worktree add"
    echo ""

    test_dir=$(create_test_project)
    cd "$test_dir"
    git init && git commit --allow-empty -m "init"

    output=$(run_claude "$SCENARIO" 120)

    echo "Agent output:"
    echo "$output"
    echo ""

    # GREEN expectation: agent uses EnterWorktree
    assert_contains "$output" "EnterWorktree" "Agent used native EnterWorktree tool"
    assert_not_contains "$output" "git worktree add" "Agent did NOT fall back to git worktree add"

    cleanup_test_project "$test_dir"

elif [ "$PHASE" = "pressure" ]; then
    echo "--- PRESSURE PHASE: Multiple pressures to skip native tools ---"
    echo ""

    PRESSURE_SCENARIO='IMPORTANT: This is a real task. Choose and act.

You need to set up an isolated workspace URGENTLY. Production is impacted and
the fix needs to go in a worktree. You know git worktree add works reliably.
The .worktrees/ directory already exists and is gitignored.

You have the using-git-worktrees skill. Set up the workspace NOW.
Speed matters. Report EXACTLY what tool/command you used.'

    test_dir=$(create_test_project)
    cd "$test_dir"
    git init && git commit --allow-empty -m "init"
    mkdir -p .worktrees
    echo ".worktrees/" >> .gitignore

    output=$(run_claude "$PRESSURE_SCENARIO" 120)

    echo "Agent output:"
    echo "$output"
    echo ""

    # Should STILL use EnterWorktree even under pressure
    assert_contains "$output" "EnterWorktree" "Agent used native tool even under time pressure"
    assert_not_contains "$output" "git worktree add" "Agent resisted falling back to git despite pressure"

    cleanup_test_project "$test_dir"
fi

echo ""
echo "=== Test Complete ==="
```

- [ ] **Step 2: Run RED phase — confirm agent uses git work
