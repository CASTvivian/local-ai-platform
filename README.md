# MAOMIAI Local AI Platform

MAOMIAI Local AI Platform 是一个面向本地化部署的桌面级 AI 工作台。项目目标是在用户设备或企业内网环境中完成 AI 对话、文档处理、代码检查、任务编排和结果管理，减少对外部云服务的依赖。

当前版本处于桌面演示包和本地运行时验证阶段，已支持 Windows / macOS 桌面打包、本地后端服务、模型能力准备入口和多模块工作台界面。

---

## 项目定位

MAOMIAI 面向以下场景：

- 本地 AI 助手工作台
- 企业内部 AI 原型系统
- 私有化 AI 能力验证
- 本地模型与本地后端服务编排
- 文档、代码、工作流、产物统一管理
- Windows / macOS 双平台桌面演示交付
- 低外部依赖、本地优先的 AI 平台方案验证

---

## 当前已具备的能力

### 1. 桌面工作台

- 中文化桌面界面
- 新对话入口
- 文件与结果管理入口
- 代码检查入口
- 本地模型入口
- 设置入口
- 右侧检查器和服务状态面板
- Windows / macOS 桌面包构建流程

### 2. 本地模型能力准备

本地模型页面已经按"能力商店"方式设计，用户无需打开终端，也不需要手动输入命令。

当前规划能力包括：

- 标准对话能力
- 轻量快速能力
- 代码能力
- 推理分析能力
- 英文通用能力
- 小型通用能力
- 文档向量能力
- 多语言文档向量能力

软件目标流程：

```text
选择能力
  → 自动检测本地推理后端
  → 自动启动本地推理服务
  → 自动下载对应能力
  → 自动验证
  → 自动接入对话
```

### 3. 本地后端服务

当前本地后端采用多服务结构，包含：

* 模型网关服务 (Model Gateway)
* 模型准备服务 (Model Bootstrap Service)
* 技能管理服务 (Skill Store Service)
* 产物注册服务 (Artifact Registry Service)
* 代码检查服务 (Code Review Gate Service)
* 仓库记忆服务 (Repo Memory Service)
* 工作流服务 (Workflow Store Service)
* 设计系统服务 (Design System Service)

### 4. 企业级服务结构

以下模块已进入企业级服务结构：

* Skill Store Service (18121)
* Artifact Registry Service (18123)
* Code Review Gate Service (18124)
* Repo Memory Service (18125)
* Workflow Store Service (18126)
* Design System Service (18127)

---

## 技术结构

```
Desktop UI
  → Tauri Desktop Shell
  → Local Runtime Scripts
  → Python Backend Services
  → Local Inference Backend
  → Local Model Capabilities
```

界面层使用 Web 技术实现，桌面壳由 Tauri 提供，后端能力由本地 Python 服务提供。该模式可以同时兼顾桌面分发、跨平台界面和本地服务编排。

---

## 仓库结构

```
.
├── .github/workflows/          # GitHub Actions 构建流程
├── core-platform/
│   ├── apps/desktop/           # 桌面应用源码与 Tauri 配置
│   ├── scripts/                # 本地运行时脚本
│   ├── services/               # 本地后端服务
│   └── releases/               # 本地演示包和交付包
├── docs/                       # 项目文档与验收报告
├── capability-registry/        # 能力注册相关资源
├── generated/                  # 本地生成资源
└── README.md
```

当前桌面打包主路径为：

```
core-platform/apps/desktop
```

---

## 构建说明

### macOS 本地构建

```bash
cd core-platform/apps/desktop
npm install
npm run tauri build
```

### Windows 构建

Windows 包通过 GitHub Actions 构建：

```
.github/workflows/build-win-release.yml
```

构建产物包括：

* Windows 安装器
* MSI 安装包
* 桌面可执行文件
* 构建信息文件

---

## 当前阶段状态

### P3.14 Desktop Demo Package

已完成：

* macOS 桌面演示包
* Windows 桌面演示包
* 本地模型准备入口
* 本地模型能力商店 UI
* Windows runtime 文件打包
* 企业服务打包路径修复
* Windows 导航稳定化处理
* GitHub Actions Windows 构建流程

进行中：

* Windows 实机本地后端自动启动验证
* Windows 模型能力一键下载闭环
* 下载进度和状态反馈优化
* 会话上下文管理
* 演示级 UI 继续打磨
* 临时运行时覆盖层清理

---

## Roadmap

### 近期重点

1. Windows 后端自启动稳定化
2. 本地模型一键下载和启用闭环
3. 模型下载进度展示
4. 本地服务健康状态可视化
5. 会话上下文记忆
6. 文档能力与知识库能力接入
7. 企业级服务接口统一验收
8. 对外演示包和安装流程产品化

---

## 说明

本项目当前属于内部原型和演示包阶段，不应直接视为生产版本。Windows 本地运行时、模型下载和后端服务自启动仍在持续验证中。
