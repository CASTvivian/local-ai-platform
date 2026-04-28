# MAOMIAI Local AI Platform

MAOMIAI Local AI Platform 是一套本地运行的 AI 工作台与智能体平台，目标是在本地电脑或私有服务器上完成任务路由、模型调用、文档处理、工作流、代码审查、产物管理、仓库记忆、设计系统和模型设置等能力。

当前版本已经完成 **P3.14 跨平台演示包封口**，可用于内部演示和后续迭代验证。

---

## 当前阶段状态

| 模块 | 状态 |
|---|---|
| macOS Desktop App | ✅ 已打包 |
| macOS DMG | ✅ 已生成 |
| Windows GitHub Actions 打包 | ✅ 已生成 artifact |
| 本地模型 qwen2.5:7b | ✅ 已接通 |
| Model Gateway 18080 | ✅ 已接通 |
| Ollama 11434 | ✅ 已接通 |
| 全中文桌面 UI | ✅ 已完成 |
| 服务健康面板 | ✅ 已完成 |
| Demo 启停脚本 | ✅ 已完成 |
| 会话上下文管理 | ⚠️ 已实现，待完整回归 |
| 页面交互清理 | ⚠️ D7 阶段继续修复 |

---

## 仓库结构

```text
.
├── .github/workflows/                 # GitHub Actions，含 Windows 打包
├── core-platform/                      # 本地 AI 平台主工程
│   ├── apps/desktop/                   # Tauri 桌面端
│   ├── services/                       # 后端服务
│   ├── scripts/                        # 启停 / 验收 / 打包脚本
│   ├── manifests/                      # 模型与设备配置
│   ├── docs/                           # 报告与演示文档
│   └── releases/                       # 本地打包产物
├── generated/                          # 生成产物目录
├── scripts/                            # 仓库级辅助脚本
└── README.md
```

---

## 核心能力

### 1. 本地模型链路

```text
Desktop App
  -> Model Gateway :18080
  -> Ollama :11434
  -> qwen2.5:7b
```

已验证 `qwen2.5:7b` 可以返回中文自然语言回复。

### 2. 桌面工作台

当前桌面端包含：

- 新建会话
- 启动中心
- 大脑状态
- 技能商店
- 文档处理
- 工作流
- 产物中心
- 代码审查
- 仓库记忆
- 设计系统
- 模型设置
- 服务健康检查
- 右侧 Inspector 面板

### 3. 核心服务

| 端口 | 服务 | 说明 |
|---|---|---|
| 18080 | Model Gateway | 本地模型网关 |
| 18093 | Auto Router | 任务路由 |
| 18104 | Runtime Execution | 运行时执行 |
| 18110 | Policy Engine | 策略权限 |
| 18111 | Trace Observability | 追踪审计 |
| 18112 | Eval Gateway | 评测网关 |
| 18120 | Document Ingestion | 文档处理 |
| 18121 | Skill Store | 技能商店 |
| 18123 | Artifact Registry | 产物中心 |
| 18124 | Code Review Gate | 代码审查 |
| 18125 | Repo Memory | 仓库记忆 |
| 18126 | Workflow Store | 工作流 |
| 18127 | Design System | 设计系统 |

---

## 本地启动

### 启动 Demo

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/demo/run_desktop_demo.sh
```

### 停止 Demo

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/demo/stop_desktop_demo.sh
```

### 只启动后端服务

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/desktop/start_desktop_services.sh
```

### 查看服务状态

```bash
bash scripts/desktop/status_desktop_services.sh
```

---

## macOS 打包产物

当前 macOS 演示包已完成：

```text
core-platform/releases/maomiai-desktop-demo/
core-platform/releases/maomiai-desktop-demo.tar.gz
```

包含：

- `Local AI Platform.app`
- `Local AI Platform_0.1.0_aarch64.dmg`
- 启动 / 停止脚本
- Demo Guide
- 验收报告
- Package Manifest

---

## Windows 打包

Windows 打包通过 GitHub Actions 执行：

```text
.github/workflows/build-win-release.yml
```

进入 GitHub：

```text
Actions -> build-win-release
```

构建完成后下载 artifact：

```text
local-ai-platform-win
```

已验证 Windows artifact 可包含：

```text
Local AI Platform_0.1.0_x64-setup.exe
Local AI Platform_0.1.0_x64_en-US.msi
desktop_lib.exe
```

---

## 当前已知问题

当前版本是演示版本，不是最终生产封口。

待 D7 阶段继续处理：

1. 会话上下文完整回归
2. 新建会话 / 会话隔离 / localStorage 持久化细节修复
3. 页面交互完整回归
4. 移除临时 runtime override 层
5. 页面模块正式化
6. 18120 文档处理完整硬化
7. P4 模型下载 / 注册 / 校验链路

---

## 当前阶段结论

```text
P3.14 Demo Package Freeze ✅
macOS Demo Package ✅
Windows Demo Package ✅
D7 Interaction Regression Pending ⚠️
```
