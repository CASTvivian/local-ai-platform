# C26-R1 Skill Rebuild Grading

## Goal

Grade 147 default skills for own builtin skill rebuild.

## Grades

| Grade | Meaning |
|-------|---------|
| `rebuild_core` | Must be rebuilt into our own builtin module |
| `reference` | Useful implementation/design reference |
| `knowledge_only` | Keep as knowledge only |
| `defer` | Postpone |
| `exclude` | Do not integrate |

## Results

| Grade | Count |
|-------|-------|
| rebuild_core | 83 |
| reference | 29 |
| knowledge_only | 2 |
| defer | 13 |
| exclude | 20 |

### Module Distribution

| Module | Count |
|--------|-------|
| agent_runtime | 96 |
| knowledge | 33 |
| mcp_tools | 5 |
| browser_agent | 5 |
| workflow | 4 |
| memory | 3 |
| code_agent | 1 |

### Top 10 rebuild_core

1. **Everything Claude Code** (score: 134) — agent_runtime + mcp_tool + memory + local_model, 180K stars
2. **Graphify** (score: 130) — agent_runtime + code_agent + browser_agent + memory, 47K stars
3. **Hyperframes** (score: 128) — agent_runtime + mcp_tool + code_agent + browser_agent, 17K stars
4. **Deer Flow** (score: 126) — agent_runtime + mcp_tool + memory + workflow, 67K stars
5. **Easy Vibe** (score: 124) — agent_runtime + code_agent + mcp_tool + workflow, 10K stars
6. **Autoclip** (score: 122) — agent_runtime + mcp_tool + browser_agent, 5K stars
7. **AutoGPT** (score: 120) — agent_runtime + mcp_tool + local_model, 184K stars
8. **Andrej Karpathy Skills** (score: 120) — agent_runtime + code_agent + local_model, 127K stars
9. **Anthropic Cybersecurity Skills** (score: 119) — agent_runtime + mcp_tool + code_agent + security, 6K stars
10. **Gstack** (score: 118) — agent_runtime + mcp_tool + code_agent, 94K stars

## Output

- `data/skill_brain/skill_rebuild_grading.json` — full grading data (147 items)
- `data/agent_core_audit/c26/skill_brain/c26_r1_skill_rebuild_grading.json` — audit summary

## Next

**C26-R2**: Select 10-20 rebuild_core skills and map into `our_builtin_skills.json`, each with module design.
