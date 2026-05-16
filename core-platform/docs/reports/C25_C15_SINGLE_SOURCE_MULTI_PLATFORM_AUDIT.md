# C25-C15 Single Source Multi-Platform Audit

**Audit ID**: C25-C15-SINGLE-SOURCE  
**Date**: 2026-05-16  
**Commit**: `d6008ad`  
**Branch**: main (synced with origin)  

---

## 结论：PASS WITH ISSUES ✅⚠️

**项目没有 Win/Mac 代码分叉。所有业务逻辑是单源的。**

```text
同一套 core-platform 源码 ✅
同一套 Agent Runtime       ✅
同一套 Desktop 前端         ✅
同一套 services            ✅
同一套 data policy/catalog ✅

Win/Mac 分别通过 Tauri 打包 ✅
未发现任何 Win/Mac 业务代码分叉 ✅
```

---

## 1. Git 状态

| 项 | 值 |
|---|---|
| HEAD | `d6008adbe35ef00ffb434b7c4f3ec6fea73dd672` |
| origin/main | `d6008adbe35ef00ffb434b7c4f3ec6fea73dd672` |
| 同步 | ✅ 一致 |

---

## 2. 单源核心目录

所有核心目录存在且只有一份：

| 目录 | 存在 | 文件数 |
|---|---|---|
| `apps/desktop/src` | ✅ | 18 |
| `apps/desktop/src-tauri/src` | ✅ | 2 |
| `services/agent_runtime_service` | ✅ | 123 |
| `services/model_gateway` | ✅ | 4 |
| `services/model_bootstrap_service` | ✅ | 5 |
| `services/repo_memory_service` | ✅ | 13 |
| `services/skill_store_service` | ✅ | 15 |
| `services/workflow_store_service` | ✅ | 13 |
| `data/agent_policy` | ✅ | 3 |
| `data/agent_team` | ✅ | 14 |
| `data/sandbox_policy` | ✅ | 1 |
| `data/brain_assets/manifests` | ✅ | 13 |
| `data/brain_assets/model_catalog` | ✅ | 1 |
| `data/brain_assets/video_catalog` | ✅ | 1 |

**结论：零分叉 ✅**

---

## 3. 平台差异目录（仅允许这些）

| 目录 | 存在 | 文件数 | 用途 |
|---|---|---|---|
| `scripts/windows/` | ✅ | 7 | Windows 启动/停止/状态/引导脚本 |
| `scripts/mac/` | ✅ | 2 | macOS 启动/状态脚本 |
| `.github/workflows/` | ✅ | 1 | CI 构建（仅 Windows） |

---

## 4. 疑似分叉目录扫描

**未发现任何分叉目录** ✅

扫描关键词：`windows_only`, `win_only`, `mac_only`, `macos_only`, `desktop_win`, `desktop_mac`, `agent_runtime_windows`, `agent_runtime_mac`, `services_windows`, `services_mac`

**结果：0 个匹配**

---

## 5. Tauri Resources 配置

`tauri.conf.json` resources 包含 19+ 项：

| 类型 | 包含 | 状态 |
|---|---|---|
| Windows 脚本 | `scripts/windows/*.ps1` (4个) | ✅ |
| Mac 脚本 | `scripts/mac` | ✅ |
| 嵌入式 Mac 脚本 | `resources/scripts/start_all.sh`, `stop_all.sh` | ⚠️ 旧版 |
| Services | 6 个 service 目录 | ✅ |
| Data | agent_policy, sandbox_policy, agent_team, brain_assets | ✅ |

### ⚠️ ISSUE-1: 嵌入式脚本过时

`resources/scripts/start_all.sh` 和 `stop_all.sh` 是**旧版本**：
- 硬编码路径 `/Users/mofamaomi/Documents/本地ai/core-platform`
- 只启动 4 个旧服务 (model_gateway, plugin_manager, eval_engine, agent_orchestrator)
- **没有** RUNTIME_ROOT 自动解析
- **没有** 当前 6 个核心服务 (repo_memory, skill_store, workflow_store, model_bootstrap, model_gateway, agent_runtime)

而 `scripts/mac/start_all.sh` 是**正确版本**：
- 支持 `MAOMIAI_RUNTIME_ROOT` 环境变量
- 自动搜索 services 目录
- 包含所有 6 个核心服务
- health check 等待

**建议**：删除 `resources/scripts/` 目录，tauri.conf.json 中将 `resources/scripts/start_all.sh` 和 `stop_all.sh` 改为引用 `../../../scripts/mac/start_all.sh`。或者让 Mac 启动直接使用 `../../../scripts/mac` 目录（已配置），删除 `resources/scripts` 中的重复文件。

---

## 6. lib.rs 平台处理审计

**结论：正确 ✅**

`lib.rs` 中的平台差异处理完全符合单源原则：

| 函数 | 处理方式 |
|---|---|
| `start_desktop_services` | `#[cfg(target_os = "windows")]` → PowerShell, `#[cfg(not)]` → Bash |
| `stop_desktop_services` | 同上 |
| `write_embedded_windows_bootstrap` | Windows only, `include_str!` 从 `scripts/windows/` 读取 |
| `run_windows_start_all_background` | `#[cfg(target_os = "windows")]` + `#[cfg(target_os = "macos")]` 分支 |
| `start_local_ai_runtime` | Windows only |
| `run_windows_bootstrap*` | Windows only, 非 Windows 返回提示信息 |

**关键**：所有业务逻辑共享，平台差异只在启动脚本调用层面。

---

## 7. Services 无分叉验证

扫描 `services/` 目录下所有 Python 文件，**未发现任何文件名包含 `windows`、`macos`、`darwin`**。

20 个 service 目录全部是平台无关的 Python 代码。

**结论：零分叉 ✅**

---

## 8. Build Outputs

| Build | Commit | 平台 | 日期 |
|---|---|---|---|
| macos-c25-latest | `d52ce18` | macOS aarch64 | 2026-05-16 |
| macos-c25-runtime-autostart | `8603bfd` | macOS aarch64 | 2026-05-16 |
| windows-c25-c12-msi-only | `edf07e9` | Windows x64 | 2026-05-15 |
| windows-c25-c13-runtime-resources | `4eb9866` | Windows x64 | 2026-05-15 |

⚠️ **ISSUE-4**: 各平台构建 commit 不同（因为构建时间不同），但这是当前手动构建的正常结果。建立统一 CI 后将解决。

---

## 9. 发现的问题

### ISSUE-1: 🟡 MEDIUM - 嵌入式脚本过时

**文件**：
- `apps/desktop/src-tauri/resources/scripts/start_all.sh` — 旧版硬编码，4 个旧服务
- `apps/desktop/src-tauri/resources/scripts/stop_all.sh` — 旧版

**影响**：如果 Tauri Mac 包使用 `resources/scripts/start_all.sh`（而非 `scripts/mac/start_all.sh`），则 Mac 安装包会启动错误的服务。

**修复**：删除 `resources/scripts/` 并更新 `tauri.conf.json`。

### ISSUE-2: 🟢 LOW - 根目录遗留脚本

**文件**：
- `scripts/start_all.sh` — 4 个旧服务
- `scripts/stop_all.sh` — 旧版
- `scripts/start_all.bat` — 引用不存在的旧服务 (real_impl, agent_team, research_real, hyperframes)
- `scripts/stop_all.bat` — 旧版
- `scripts/start_all_desktop.sh` (124行) — 另一个启动脚本
- `scripts/start_service.sh` — 单服务启动辅助
- `scripts/status_all.sh` — 旧版状态检查

**影响**：不在 Tauri 包中使用，但造成维护混乱。

**修复**：清理或标记为 deprecated。

### ISSUE-3: 🟡 MEDIUM - 无 Mac CI Workflow

**现状**：`.github/workflows/` 只有 `build-win-release.yml`，无 `build-mac-release.yml`。

**影响**：Mac 包手动构建，无法保证与 Windows 包同 commit 构建。

**修复**：添加 `build-mac-release.yml`。

### ISSUE-4: 🟢 LOW - Build Commit 不一致

**现状**：各平台 build 的 commit 不同。

**修复**：统一 CI pipeline 后自然解决。

---

## 10. 规则

以后所有开发遵守：

1. **Agent Runtime 只维护一份** — `services/agent_runtime_service`
2. **Desktop 前端只维护一份** — `apps/desktop/src`
3. **services 只维护一份** — `services/*`
4. **Win/Mac 不允许各自复制一套业务代码**
5. **平台差异只能在**：启动脚本 (`scripts/windows|mac`)、打包资源、Tauri cfg、`lib.rs` `#[cfg]` 中处理
6. **所有包都必须从同一个 git commit 构建**
7. **BUILD_INFO 必须记录 commit**
8. **Mac 和 Win 验收报告必须标明 build commit**

---

## 11. 下一步

1. **清理 ISSUE-1**：删除 `resources/scripts/` 过时文件，统一使用 `scripts/mac/`
2. **清理 ISSUE-2**：标记或删除根目录遗留脚本
3. **建立 ISSUE-3**：添加 Mac CI workflow
4. 继续做 **C25-C14-B：去掉结构性写死，改 schema-driven planner**
