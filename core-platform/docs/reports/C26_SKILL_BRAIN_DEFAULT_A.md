# C26 Skill Brain Default A

## Goal
Turn local brain assets, GitHub stars, and repository memory into default skills that are available at agent startup, not just on-demand search.

## Implemented

### Generator Script
`scripts/build/generate_default_skills.py`

Scans three data sources:
1. `data/brain_assets/manifests/brain_asset_index.json` — 147 indexed repos
2. `data/github_stars/CASTvivian_starred_repos.json` — all starred repos (overlaps with #1)
3. `data/repo_memory/brain_asset_seed.json` — cross-reference enrichment

### Generated Output
`data/skill_brain/default_skills.json`

Each skill includes:
- **id** — normalized skill identifier
- **title** — human-readable name
- **source_path** — local filesystem path
- **source_type** — brain_asset | github_star | repo_memory
- **source_repo** — GitHub full_name
- **html_url** — GitHub URL
- **enabled_by_default** — true (all skills active by default)
- **tags** — skill categories (mapped from buckets + original tags)
- **buckets** — original brain asset buckets
- **original_tags** — GitHub/brain-asset tags (up to 15)
- **description** — repo description
- **language** — primary language
- **stars** — GitHub stars
- **tools** — default tools [repo_memory.search, capability.match, model.generate]
- **risk** — safe
- **created_at** — generation timestamp

### Classification Logic
Word-boundary matching with fallback tag-set matching:
- **agent_runtime** (96) — agents, autonomous, planner, executor, harness, agentic
- **local_model** (56) — llm, ollama, qwen, embedding, inference, transformer
- **prompt_framework** (52) — prompt-engineering, skill-framework, claude-code, codex-cli
- **ui_component** (42) — react, vue, tauri, desktop, design-system, component-lib
- **workflow** (34) — workflow, automation, pipeline, orchestration, langgraph
- **code_agent** (31) — coding-agent, code-generation, copilot, ide, code-review
- **mcp_tool** (31) — mcp, tool-server, stdio-transport
- **memory** (25) — memory, rag, vector-db, knowledge-graph
- **browser_agent** (11) — browser-automation, playwright, headless-browser
- **security** (5) — sandbox, cybersecurity, vulnerability
- **evaluation** (4) — eval, benchmark, metric
- **general_skill** (38) — no specific category matched

### Audit
`data/agent_core_audit/c26/skill_brain/c26_skill_brain_default_audit.json`

### Top 5 by Stars
| # | Skill | Stars | Tags |
|---|-------|-------|------|
| 1 | public-apis | 434K | general_skill |
| 2 | OpenClaw | 371K | general_skill, workflow |
| 3 | Claw Code | 191K | agent_runtime, prompt_framework |
| 4 | Superpowers | 188K | agent_runtime, code_agent, prompt_framework, ui_component |
| 5 | AutoGPT | 184K | agent_runtime, local_model, mcp_tool |

### Language Distribution
- Python: 57, TypeScript: 26, JavaScript: 13, Java: 11, HTML: 9, Shell: 6, Rust: 3

## Validation
- [x] Generator script runs successfully
- [x] 147 skills generated
- [x] Tag classification uses word-boundary matching (no false positives)
- [x] Hardcode guard passes
- [x] Audit file generated
- [x] Skills sorted by stars (descending)

## Meaning
This is the first step toward making collected repositories become default platform skills. The generated `default_skills.json` is a machine-readable catalog that can be consumed by:
- Capability registry (C26-B)
- Desktop skill store UI (C26-C)
- Schema planner (C26-D)
- Repo memory auto-update (C26-E)

## Next
- **C26-B**: Load `default_skills.json` into capability registry, expose via `capability.match`
- **C26-C**: Desktop skill store page shows default skills
- **C26-D**: Planner uses skill tags during plan generation
- **C26-E**: Repo memory auto-updates skills when new repos are added
