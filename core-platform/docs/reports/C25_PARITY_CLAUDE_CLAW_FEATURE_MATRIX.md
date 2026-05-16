# C25-PARITY Claude/Claw Feature Matrix

> Checked at: 2026-05-16T12:50:00Z
> Schema version: c25-parity-v1

## Summary

| Metric | Value |
|--------|-------|
| Implemented | 8 / 16 |
| Partial | 6 / 16 |
| Missing | 2 / 16 |
| Average Score | 73.1 / 100 |
| P0 Gaps | 3 |
| P1 Gaps | 4 |
| P2 Gaps | 1 |
| Core Rebuild % | ~70% |
| Mac Demo % | ~75% |
| Win Demo % | ~60% |
| Claude/Claw Parity % | ~65% |

## Verdict

| Question | Answer |
|----------|--------|
| Can demo on Mac? | ✅ Yes |
| Can demo on Windows? | ✅ Yes (needs real-device resource/autostart verification) |
| Can claim full rebuild? | ❌ No — 3 P0 gaps remain |
| Next P0? | C25-C14-B4 (Planner Model Structured Output) |

## Feature Matrix

| ID | Feature | Status | Score | Missing Terms | Priority |
|----|---------|--------|-------|---------------|----------|
| agent_runtime_entry | 统一 Agent Runtime 入口 | ✅ implemented | 95 | - | P1 |
| schema_planner | Schema-driven Planner | ✅ implemented | 88 | - | P0* |
| planner_model_structured_output | Planner Model 结构化输出 | ⚠️ partial | 55 | structured json plan, planner model | **P0** |
| tool_registry_mcp | Tool Registry / MCP Runtime | ✅ implemented | 85 | - | P1 |
| executor_loop | Executor 执行 plan.steps | ⚠️ partial | 70 | steps | **P0** |
| observation_replan | Observation / Replan Loop | ✅ implemented | 82 | - | P2 |
| approval_sandbox | Approval / Sandbox | ✅ implemented | 90 | - | P2 |
| run_store_session_replay | Run Store / Session / Replay | ✅ implemented | 88 | - | - |
| filesystem_tools | Filesystem Tools | ✅ implemented | 85 | sandbox (in path) | P1 |
| shell_tools | Shell Execution Tools | ✅ implemented | 80 | - | P1 |
| browser_web_tools | Browser / Web Tools | ✅ implemented | 85 | - | - |
| capability_registry | Capability Registry | ✅ implemented | 92 | - | **P0*** |
| repo_memory_brain | Repo Memory / Brain Assets | ✅ implemented | 90 | - | - |
| multi_agent | Multi-Agent Runtime | ⚠️ partial | 60 | worker | P1 |
| desktop_integration | Desktop Chat Integration | ⚠️ partial | 65 | - | P1 |
| cross_platform_packaging | Single Source Win/Mac Packaging | ⚠️ partial | 70 | tauri resources (partial) | P1 |

*schema_planner and capability_registry are implemented but marked P0 because downstream consumers (executor, renderer) still have hardcode issues that block full parity.

## Detailed Gap Analysis

### P0 — Critical (Must complete before final demo)

#### C25-C14-B4: Planner Model Structured Output
- **Current**: `MAOMIAI_SCHEMA_PLANNER_MODEL` env var gates LLM planner; defaults to lexical scoring fallback
- **Target**: Enable by default, wire to model gateway, produce structured JSON plans
- **Impact**: Planner accuracy, tool selection quality, Claude/Claw parity
- **Files**: `planning/schema_planner.py`, `planning/llm_planner.py`

#### C25-C14-B9: Executor Tool Dispatch Registry化
- **Current**: `executor.py` uses if/elif chains: `if tool == "time.now": ... elif tool == "weather.query": ...`
- **Target**: Replace with MCP registry lookup; new tools require zero executor code changes
- **Impact**: Extensibility, single dispatch path
- **Files**: `executor.py`, `mcp/invoker.py`, `mcp/registry.py`

#### C25-C14-B12: 清 executor capability.status 硬编码
- **Current**: `executor.py` has hardcoded `capability.status` handling
- **Target**: Route through capability registry service call
- **Impact**: Single source of truth, consistency
- **Files**: `executor.py`, `capability/registry.py`

### P1 — Important (Should complete before claiming full rebuild)

#### C25-C14-B6: 清 desktop router dry_run / 固定测试按钮
- **Current**: `windows-demo-stable-router.js` has `MODEL_CATALOG_FALLBACK`, `inferViewFromText()` with Chinese keyword routing, hardcoded test messages ("你好，请用一句话介绍你自己")
- **Target**: Fetch catalog from 18131 API, remove keyword view routing, remove hardcoded test buttons
- **Files**: `windows-demo-stable-router.js`

#### C25-C14-B10: Renderer intent 分支清理
- **Current**: `renderer.py` has intent-based branches (weather, web_fact, project_knowledge, etc.)
- **Target**: Schema-driven formatting, remove hardcoded intent strings
- **Files**: `renderer.py`

#### C25-C14-B7: Model/Profile/Provider 配置归一
- **Current**: Model profiles scattered across `MODEL_CATALOG_FALLBACK`, `tools.py`, `model_gateway/main.py`
- **Target**: Single schema-driven model profile registry
- **Files**: Multiple

#### C25-OFFLINE: 离线模型预种/Demo Pack
- **Current**: No pre-seeded model weights, requires Ollama pull
- **Target**: Bundle at least one model for offline demo

### P2 — Nice to Have

#### C25-MULTI-AGENT-V2: Real Worker Agent Spawning
- **Current**: Team coordinator exists but workers are capability-tag-matched, not independent instances
- **Target**: Actual parallel worker spawning with message passing

## What's Working Well

1. **Agent Runtime 主链路**: planner → executor → validator → renderer 全链路可用
2. **Schema-driven 核心架构**: capability_registry + planner_tool_schema 外部化，无硬编码关键词
3. **7 个 Enterprise Workbench Service**: Document(18120), Skill(18121), Artifact(18123), CodeReview(18124), RepoMemory(18125), Workflow(18126), DesignSystem(18127)
4. **安全体系**: Approval Store + Sandbox + Guard + Policy 三层防护
5. **Observation/Replan**: 观察器+重规划器已接入主循环
6. **Run Store/Replay**: 完整运行记录+时间线回放
7. **Browser/Search/Weather**: 三种外部工具全部可用
8. **Filesystem**: 沙箱化文件操作

## Conclusion

当前项目已具备 Claude/Claw 风格 Agent Kernel 的主体能力，但**不能称为 100% parity**。

- ✅ 本地 Agent Runtime 主体已完成
- ✅ Mac 路演主链路可用
- ✅ Schema Planner 已替换固定规则
- ⚠️ Planner Model Structured Output 未默认启用
- ⚠️ Executor dispatch 仍偏 if/elif
- ⚠️ Desktop fallback/测试按钮未清理
- ❌ 距完全 Claude/Claw 二次重构融合版还差 ~30%

**建议完成 B4/B9/B12 后再做最终路演。**

## Next Priority

1. **C25-C14-B4**: Planner Model Structured Output (P0)
2. **C25-C14-B9**: Executor Tool Dispatch Registry化 (P0)
3. **C25-C14-B12**: 清 executor capability.status 硬编码 (P0)
4. **C25-C14-B6**: 清 desktop router fallback (P1)
5. **C25-C14-B10**: Renderer intent 分支清理 (P1)
6. **C25-C14-B7**: Model/Profile/Provider 配置归一 (P1)
7. **C25-OFFLINE**: 离线模型预种 (P1)
8. **C25-FINAL**: 最终 Mac/Win 路演包
