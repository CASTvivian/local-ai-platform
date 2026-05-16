# C25-C14-B3.5 Fixed Logic Detail Audit

## 结论

B3 把关键词路由从主 planner 移除后，这次审计检查的是**更深层结构性固定判断**。

**核心发现：planner.py 主入口确实干净了，但系统仍有 4 个 FAIL 级结构性硬编码和 8 个 WARN 级固定逻辑。**

## finding_count

`1196`（含大量正则匹配噪音，重点看结构性判定）

## Structural Verdicts（20 项深度检查）

| ID | Verdict | 说明 |
|----|---------|------|
| S1 | ~~FAIL~~ → **PASS** | planner.py 主入口干净，无关键词路由（` in query` 误匹配变量赋值，非意图路由） |
| S2 | **WARN** | schema_planner 使用词法评分 fallback，kind bias (safe+0.05, model.generate+0.12, restricted-0.10) 是结构性固定判断 |
| S3 | **WARN** | schema_planner._schema_only_default_plan 含固定 tool name: `["repo_memory.search", "capability.match", "web.search", "model.generate"]` |
| S4 | **PASS** | executor.py 只执行 plan.tools，无用户意图推断 |
| S5 | **WARN** | executor.py 含固定 tool dispatch table: `["time.now", "time.date_math", "weather.query", "web.search", "capability.match", "repo_memory.search", "catalog.search", "skill_store.list", "workflow_store.list", "capability.status", "model.generate"]`。新增 tool 需手动加分支 |
| S6 | **FAIL** | capability/registry.py `match_capabilities()` 含固定中文关键词评分: 代码/编程/bug → code, 推理/分析/判断 → reasoning, 仓/项目/mcp/知识库 → memory, 视频/comfyui → video, 网页/抓取 → browser |
| S7 | **WARN** | renderer.py 含 intent 分支渲染: `["time_now", "date_math", "weather", "restricted_action", "web_fact", "project_knowledge", "project_architecture_services", "project_architecture_capabilities", "project_architecture_summary", "capability_status", "local_chat"]`，新增 intent 需同步改 renderer |
| S8 | **FAIL** | desktop router `inferViewFromText()` 含中文关键词路由: 新对话→chat, 本地模型/模型→models, 文件/结果/产物→artifacts, 代码→code-review, 设置→settings |
| S9 | **WARN** | desktop router 含固定测试消息: "你好，请用一句话介绍你自己", "今天是几月几号，现在几点", "我们现在有哪些 Agent 和 MCP 相关仓库资产" |
| S10 | **WARN** | model_gateway 含固定 `PROFILE_MODEL_MAP` (standard→qwen2.5:7b, light→qwen2.5:1.5b, code→qwen2.5-coder:7b, reasoning→deepseek-r1:7b, english→llama3.1:8b, small→llama3.2:3b, embed→nomic-embed-text, embed_multi→bge-m3) |
| S11 | **WARN** | model_gateway 含固定 `OLLAMA_URL=http://127.0.0.1:11434/api/generate` |
| S12 | **PASS** | renderer.py 无硬编码 `demo_kernel`（capability_status 在 executor 中） |
| S13 | **ACCEPTED** | scripts 含固定端口（启动脚本必须指定端口，可接受） |
| S14 | **WARN** | mac start_all.sh 含开发者绝对路径 fallback: `/Users/mofamaomi/Documents/本地ai/core-platform` |
| S15 | **WARN** | bootstrap_runtime.ps1 `Get-Model-For-Profile` 含固定 profile→model 映射 |
| S16 | **WARN** | windows-click-model-setup.js `MODEL_CATALOG` 含固定模型目录 |
| S17 | **ACCEPTED** | hardcode_guard.json allowed_files 含 legacy_rule_planner.py，共 7 个允许文件 |
| S18 | **FAIL** | executor.py `capability.status` 分支返回硬编码状态列表 (demo_kernel, enabled:[...], pending:[...]) |
| S19 | **WARN** | validator.py 含 intent 分支幻觉阻断: weather, web_fact, project_knowledge/catalog_knowledge。需和 planner intent 同步 |
| S20 | **CONFIG_REVIEW** | planner_tool_schema.json 含 planner_hints 配置: 全部 10 个 tool。是 schema 配置化提示，可接受但需策略审计 |

## 4 个 FAIL 级结构性硬编码

### S6: capability/registry.py 中文关键词评分 ⛔
```python
# registry.py:235-249 — 固定中文关键词→能力映射
if any(keyword in normalized_query for keyword in ["代码", "编程", "bug", "报错", "开发"]):
    if "code" in capability.tags: score += 30
if any(keyword in normalized_query for keyword in ["推理", "分析", "判断", "策略"]):
    if "reasoning" in capability.tags: score += 30
if any(keyword in normalized_query for keyword in ["仓", "项目", "mcp", "rag", "agent", "知识库"]):
    if "memory" in capability.tags or "repo" in capability.tags: score += 35
```
**问题**：和 legacy _keyword_plan 同性质，只是从 planner 移到了 registry。新场景/新语言无法覆盖。

### S8: desktop router 中文关键词路由 ⛔
```javascript
// windows-demo-stable-router.js:663-671
function inferViewFromText(text) {
  if (value.includes("新对话") || value.includes("新建会话")) return "chat";
  if (value.includes("本地模型") || value.includes("模型")) return "models";
  if (value.includes("文件") || value.includes("结果") || value.includes("产物")) return "artifacts";
  if (value.includes("代码")) return "code-review";
  if (value.includes("设置")) return "settings";
}
```
**问题**：前端也有中文关键词路由，和后端 planner 无关，但仍是固定逻辑。

### S18: executor.py capability.status 硬编码状态 ⛔
```python
# executor.py:141-164 — 固定能力状态列表
elif tool == "capability.status":
    return ToolResult(tool="capability.status", ok=True, data={
        "status": "demo_kernel",
        "enabled": ["desktop_app", "local_model_runtime", "model_download", ...],
        "pending": ["web_search", "weather_tool", "mcp_gateway", ...],
    })
```
**问题**：能力状态应该从 capability registry 动态读取，不应硬编码。

### S1 误报说明
S1 标记 FAIL 是因为 ` in query` 匹配到 `query = (text or "").strip()` 变量赋值行，实际 planner.py 主入口无关键词路由逻辑，修正为 PASS。

## 8 个 WARN 级固定逻辑

1. **S2**: schema_planner kind bias (safe+0.05, model.generate+0.12, restricted-0.10)
2. **S3**: schema_planner 固定 tool name 检查
3. **S5**: executor.py 固定 tool dispatch if/elif 链
4. **S7**: renderer.py intent→template 分支链
5. **S9**: desktop router 固定测试消息
6. **S10+S11**: model_gateway 固定 PROFILE_MODEL_MAP 和 OLLAMA_URL
7. **S14+S15+S16**: scripts/JS 固定端口/路径/profile 映射
8. **S19**: validator.py intent 分支幻觉阻断

## risk_summary

| Risk | Count | 说明 |
|------|-------|------|
| critical | 123 | planner.py/executor.py 正则噪音（大部分是合法代码） |
| high | 241 | registry/router 关键词匹配 |
| medium | 588 | model_gateway/config/JS |
| low | 60 | scripts 固定端口 |
| config_review | 82 | JSON 配置文件 |
| accepted_legacy | 63 | legacy_rule_planner.py |
| ui_copy_review | 39 | 前端中文文案 |

## top 10 文件

| Count | File |
|-------|------|
| 232 | scripts/windows/bootstrap_runtime.ps1 |
| 141 | apps/desktop/src/js/windows-click-model-setup.js |
| 133 | apps/desktop/src/js/windows-demo-stable-router.js |
| 91 | data/agent_policy/planner_tool_schema.json |
| 75 | services/agent_runtime_service/app/renderer.py |
| 72 | services/agent_runtime_service/app/planning/schema_planner.py |
| 63 | services/agent_runtime_service/app/planner.py |
| 63 | services/agent_runtime_service/app/planning/legacy_rule_planner.py |
| 63 | services/agent_runtime_service/app/capability/registry.py |
| 60 | services/agent_runtime_service/app/executor.py |

## 关键判定

| 检查项 | 结果 |
|--------|------|
| planner.py 是否干净 | ✅ PASS（主入口无关键词路由） |
| schema_planner 还剩什么 | ⚠️ 词法评分 fallback + kind bias + 固定 tool name |
| executor 是否干净 | ⚠️ 无意图推断，但有固定 tool dispatch table + capability.status 硬编码 |
| capability registry | ❌ 中文关键词评分（代码/推理/仓/视频/网页） |
| desktop router | ❌ 中文关键词路由 + 固定测试消息 |
| model_gateway | ⚠️ 固定 PROFILE_MODEL_MAP + OLLAMA_URL |
| scripts | ✅ ACCEPTED（固定端口/路径可接受） |
| hardcode_guard | ✅ ACCEPTED（allowlist 合理） |

## 下一步优先级

| Priority | ID | Action |
|----------|----|--------|
| 🔴 P0 | B4 | planner model structured JSON output，model_gateway 健康时默认让模型根据 schema 产 plan |
| 🔴 P0 | B11 | 重构 capability/registry.py 关键词评分→schema-driven matching（消除 S6 FAIL） |
| 🟡 P1 | B6 | 清理 desktop router 中文关键词路由 + 固定测试消息（消除 S8/S9） |
| 🟡 P1 | B12 | 移除 executor.py capability.status 硬编码，改为动态读取（消除 S18） |
| 🟡 P1 | B9 | 重构 executor.py tool dispatch if/elif→registry pattern（S5） |
| 🟡 P1 | B10 | 重构 renderer.py intent 分支→data-driven template rendering（S7） |
| 🟢 P2 | B5 | planner_hints/request_shapes 策略化，标注哪些是 schema hint，哪些禁止写死（S20） |
| 🟢 P2 | B7 | 集中配置 ports/models/profiles/providers（S10/S11/S15/S16） |
| 🟢 P3 | B8 | CI fail gate，critical structural hardcode 不允许进入主 runtime |
