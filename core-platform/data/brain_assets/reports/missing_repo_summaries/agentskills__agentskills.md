# Missing Repo Summary Source: agentskills/agentskills

- URL: https://github.com/agentskills/agentskills
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/agentskills__agentskills
- Clone Status: cloned
- Language: Python
- Stars: 18463
- Topics: agent-skills
- Description: Specification and documentation for Agent Skills

## Extracted README / Docs / Examples



# FILE: README.md

# Agent Skills

[Agent Skills](https://agentskills.io) are a simple, open format for giving agents new capabilities and expertise.

Skills are folders of instructions, scripts, and resources that agents can discover and use to perform better at specific tasks. Write once, use everywhere.

## Getting Started

- **[Documentation](https://agentskills.io)** — Guides and tutorials
- **[Specification](https://agentskills.io/specification)** — Format details
- **[Example Skills](https://github.com/anthropics/skills)** — See what's possible
- **[Discord](https://discord.gg/MKPE9g8aUy)** — Join the discussion!

This repo contains the specification, documentation, and reference SDK. Also see a list of example skills [here](https://github.com/anthropics/skills).

## About

Agent Skills is an open format maintained by [Anthropic](https://anthropic.com) and open to contributions from the community.

## License

Code in this repository is licensed under [Apache 2.0](LICENSE). Documentation is licensed under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). See individual directories for details.


# FILE: docs/README.md

# Agent Skills Documentation

This directory contains the source code for the Agent Skills [documentation site](https://agentskills.io/), which is built using [Mintlify](https://mintlify.com).

## Development

Run the following command at the documentation root, where `docs.json` is located:

```bash
npx mint dev
```

View your local preview at `http://localhost:3000`.

## Publishing changes

Changes are deployed to production automatically after pushing to the default branch.


# FILE: docs/CLAUDE.md

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. The project defines an open format for teaching AI agents specialized workflows through SKILL.md files.

## Documentation

The Agent Skills documentation site, defined in the `docs/` directory, is built with [Mintlify](https://mintlify.com).

### Quick Start Commands

```bash
# Run local development server
npm run dev
```

Local preview available at `http://localhost:3000`

### Development Notes

- **Navigation**: Defined in `docs/docs.json` under `navigation.pages` array
- **Adding pages**: Create new `.mdx` file in `/docs`, add filename (without extension) to navigation
- **Deployment**: Automatic on push to `main` branch
- **Troubleshooting**: If page shows 404, ensure you're running `mint dev` from directory containing `docs.json`

