# MAOMIAI Local AI Platform

MAOMIAI Local AI Platform 是一套面向本地化部署的 AI 工作台与智能体平台。项目目标是在用户自己的电脑、私有服务器或企业内网环境中，提供任务路由、模型调用、文档处理、工作流编排、代码审查、产物管理、仓库记忆、设计系统和桌面端操作台等能力。

当前版本已经完成 **P3.14 跨平台演示包封口**，可用于内部演示、客户沟通和后续迭代验证。

---

## 当前阶段状态

| 模块 | 状态 |
|---|---|
| macOS Desktop App | ✅ 已打包 |
| macOS DMG | ✅ 已生成 |
| Windows GitHub Actions 打包 | ✅ 已生成安装包 artifact |
| 本地模型调用链路 | ✅ 已接通 |
| 模型网关 | ✅ 已接通 |
| 本地推理后端 | ✅ 已接通 |
| 全中文桌面 UI | ✅ 已完成 |
| 服务健康面板 | ✅ 已完成 |
| Demo 启停脚本 | ✅ 已完成 |
| 会话上下文管理 | ⚠️ 已实现，待完整回归 |
| 页面交互清理 | ⚠️ D7 阶段继续修复 |

> 说明：公开文档不暴露具体模型名称和内部模型配置，仅描述本地模型能力与部署链路。

---

## 产品定位

MAOMIAI Local AI Platform 不是单一聊天机器人，而是一个本地 AI 工作台底座。它面向以下使用场景：

- 本地大模型调用与统一网关
- 多服务协同的本地 Agent 工作台
- 代码生成、代码审查与安全门禁
- 文档处理、知识沉淀与后续检索增强
- 工作流模板管理和执行入口
- 执行产物、报告、文件、补丁和构建结果管理
- 仓库级修复历史与知识记忆
- 设计系统与 UI 规范管理
- macOS / Windows 桌面端演示与交付

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
  -> Model Gateway
  -> Local Inference Runtime
  -> Local Model Response
```

当前已验证桌面端可以通过本地模型网关获得中文自然语言回复。公开说明中不写具体模型名，具体模型选择与部署方式由本地环境配置决定。

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

| 服务 | 说明 |
|---|---|
| Model Gateway | 本地模型统一网关 |
| Auto Router | 任务路由与能力选择 |
| Runtime Execution | 运行时执行与沙箱入口 |
| Policy Engine | 策略评估与权限控制 |
| Trace Observability | 追踪、审计和可观测性 |
| Eval Gateway | 评测任务入口 |
| Document Ingestion | 文档处理与摄取入口 |
| Skill Store | 技能安装与启用管理 |
| Artifact Registry | 产物注册与查询 |
| Code Review Gate | 代码审查与安全检测 |
| Repo Memory | 仓库记忆与修复历史 |
| Workflow Store | 工作流模板管理 |
| Design System | 设计规范与 UI 约束管理 |

---

## 跨平台演示包

### macOS

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

### Windows

Windows 通过 GitHub Actions 打包：

```text
.github/workflows/build-win-release.yml
```

构建完成后下载 artifact：

```text
local-ai-platform-win
```

当前已验证 Windows artifact 可包含：

```text
Local AI Platform_0.1.0_x64-setup.exe
Local AI Platform_0.1.0_x64_en-US.msi
desktop_lib.exe
```

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

## GitHub Actions

当前仓库包含 Windows 桌面打包工作流：

```text
Actions -> build-win-release
```

构建逻辑：

1. Checkout 仓库
2. 安装 Node 与 Rust 环境
3. 安装桌面端依赖
4. 构建前端静态资源
5. 执行 Tauri Windows 打包
6. 收集 Windows 安装包与可执行文件
7. 上传 GitHub Actions artifact

说明：当前以 artifact 上传作为主要交付方式，不依赖 GitHub Release 发布权限。

---

## 当前已知问题

当前版本是演示版本，不是最终生产封口。

待 D7 阶段继续处理：

1. 会话上下文完整回归
2. 新建会话 / 会话隔离 / 本地持久化细节修复
3. 页面交互完整回归
4. 移除临时 runtime override 层
5. 页面模块正式化
6. 文档处理服务完整硬化
7. 模型下载 / 注册 / 校验链路

---

## 当前阶段结论

```text
P3.14 Demo Package Freeze ✅
macOS Demo Package ✅
Windows Demo Package ✅
D7 Interaction Regression Pending ⚠️
```
