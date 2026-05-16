# C26-R2 Fusion Own Builtin Modules

## Goal

Do not convert 83 rebuild_core repos into 83 separate skills. Instead:

```
83 rebuild_core reference repos
→ fused into 12 own builtin modules
→ each module references multiple sources
→ runtime implementation is owned code
```

## Output

| File | Purpose |
|------|---------|
| `data/skill_brain/our_builtin_skill_modules.json` | 12 fusion modules with source references |
| `data/skill_brain/fusion_policy.json` | Long-term asset fusion policy |
| `scripts/build/generate_builtin_fusion_modules.py` | Module generation script |
| `scripts/build/fuse_skill_references.py` | Future asset fusion script |
| `data/skill_brain/skill_reference_fusion_result.json` | Fusion result for 147 default skills |

## Module Distribution

| Module | Refs | Title |
|--------|------|-------|
| builtin.code_agent_core | 26 | 代码智能体核心模块 |
| builtin.memory_rag_core | 17 | 记忆与 RAG 检索模块 |
| builtin.mcp_tool_hub | 12 | MCP 工具协议模块 |
| builtin.browser_operator | 9 | 浏览器自动化模块 |
| builtin.local_model_runtime | 9 | 本地模型运行模块 |
| builtin.workflow_orchestrator | 3 | 工作流编排模块 |
| builtin.eval_benchmark | 3 | 评估与基准模块 |
| builtin.agent_runtime_core | 2 | 通用 Agent Runtime 模块 |
| builtin.prompt_skill_engine | 1 | Prompt 技能引擎模块 |
| builtin.security_sandbox | 1 | 安全沙箱与策略模块 |
| builtin.ui_desktop_operator | 0 | 桌面 UI 操作模块 (reserved) |
| builtin.artifact_report_engine | 0 | 产物与报告生成模块 (reserved) |

## Fusion Policy (5 Rules)

1. **reference_only** — External assets are reference only
2. **fusion_first** — Fuse before creating new skills
3. **no_one_repo_one_skill** — No one-repo-one-skill default
4. **manual_review_required** — Manual review before enablement
5. **owned_runtime_only** — Owned runtime only

## Asset Lifecycle

```
discovered → classified → matched_to_builtin_module → merged_as_reference → manual_reviewed → implemented_as_owned_module → enabled
```

## Design

Each module:
- merges similar external repos by specialist-tag-first scoring
- keeps references as design sources only
- has no runtime dependency on external repo
- defines own module implementation plan
- has acceptance criteria

## Validation

- py_compile: PASS
- hardcode guard: PASS
- rebuild_core_count: 83
- assigned_reference_count: 83
- module_count: 12
- fusion_policy rule_count: 5
- fuse_skill_references: 42 assignable, 22 new candidates

## Next

C26-R3:
- Expose builtin.* fusion modules in capability registry.
- Prioritize builtin modules over external skill.*.
