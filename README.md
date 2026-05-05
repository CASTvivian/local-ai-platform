# MAOMIAI Local AI Platform

MAOMIAI Local AI Platform 是一个面向本地化部署的桌面级 AI 工作台，目标是在用户设备上完成模型调用、任务执行、文档处理、代码审查、工作流管理和结果产物管理，减少对外部云端服务的依赖。

本项目当前处于 P3.14 桌面演示包阶段，已完成 macOS / Windows 双平台桌面应用打包流程，并持续完善 Windows 下的本地运行时自启动、模型准备和离线能力检测体验。

---

## 项目定位

MAOMIAI 面向以下场景：

- 本地 AI 助手工作台
- 企业内部 AI 工具原型
- 本地模型调用与能力编排
- 文档、代码、工作流和产物统一管理
- 跨平台桌面应用演示与交付
- 私有化、本地优先、低外部依赖的 AI 平台验证

---

## 当前能力

### 1. 桌面端工作台

当前桌面端基于 Tauri 构建，界面层使用 HTML / CSS / JavaScript，系统层使用 Rust/Tauri，后端能力由 Python 服务提供。

已支持：
- 中文化桌面界面
- 新建会话
- 文件与结果入口
- 代码检查入口
- 本地模型准备入口
- 右侧检查器面板
- 服务健康状态展示
- Windows / macOS 打包

### 2. 本地 AI 能力链路

当前设计为本地优先：

```
Desktop App
  → Local Runtime Service
  → Local Model Gateway
  → Local Inference Backend
  → Local Model
```

系统会尽量在本地完成：

- 本地 AI 状态检测
- 本地后端服务启动
- 本地运行时准备
- 模型能力准备
- 模型调用
- 中文回复返回

具体模型名称不会在产品说明中直接暴露，普通用户只需要理解为：

- 标准对话能力
- 代码能力
- 文档理解能力
- 工作流执行能力

### 3. Windows 本地运行时准备

Windows 版本正在增强自动化准备能力，包括：

- 检测本地后端运行状态
- 检测运行时环境
- 准备本地 Python 后端运行环境
- 检测本地推理后端是否安装
- 引导用户安装本地推理后端
- 准备本地 AI 能力
- 下载或检查所需模型能力

当前策略是：平台自身运行时尽量自动准备，外部推理后端安装需要用户明确触发或确认。

### 4. 企业级服务模块

当前核心服务已进入企业级服务结构，包含：

- Skill Store Service (技能管理)
- Artifact Registry Service (执行结果管理)
- Code Review Gate Service (安全审查)
- Repo Memory Service (仓库学习)
- Workflow Store Service (工作流模板)
- Design System Service (设计规范)

这些服务已统一进入桌面打包路径，避免 Windows / macOS 出现不同版本。

---

## 仓库结构

```
.
├── .github/workflows/                  # GitHub Actions 构建流程
├── core-platform/
│   ├── apps/desktop/                   # 桌面应用源码与 Tauri 配置
│   ├── scripts/                        # macOS / Windows 启动脚本
│   ├── services/                       # 桌面端本地后端服务
│   └── releases/                       # 本地生成的演示包归档
├── capability-registry/                # 能力注册相关资源
├── generated/                          # 本地生成资源
├── scripts/                            # 历史脚本与辅助脚本
├── services/                           # 历史服务源码与同步来源
├── docs/                               # 项目文档与验收报告
└── README.md
```

当前桌面打包主路径为：

```
core-platform/apps/desktop
```

Windows / macOS 的桌面包均应从该路径构建。

---

## 构建说明

### macOS 本地构建

```bash
cd core-platform/apps/desktop
npm install
npm run tauri build
```

构建产物通常位于：

```
core-platform/apps/desktop/src-tauri/target/release/bundle/
```

### Windows GitHub Actions 构建

Windows 包通过 GitHub Actions 构建：

```
.github/workflows/build-win-release.yml
```

构建内容包括：

- 桌面应用
- 前端 dist
- Windows runtime scripts
- 本地后端服务
- 构建信息文件

产物包括：

- Windows setup 安装包
- MSI 安装包
- desktop executable
- BUILD_INFO.json

---

## 当前阶段状态

### P3.14 Desktop Demo Package

已完成：

- ✅ macOS 桌面演示包
- ✅ Windows 桌面演示包
- ✅ 中文化桌面界面
- ✅ 本地模型准备入口
- ✅ Windows runtime 文件打包
- ✅ 企业服务打包路径修复
- ✅ GitHub Actions Windows 构建流程
- ✅ 项目完整性验证通过

进行中：

- Windows 实机自动启动后端验证
- Windows 本地模型准备闭环验证
- 会话上下文与交互回归
- 临时覆盖层清理
- 产品级 UI 继续打磨

---

## 重要说明

本项目当前仍处于工程验证与演示包阶段，不应被视为正式生产版本。

Windows 端的本地 AI 自动准备流程需要在真实 Windows 环境中继续验证，包括运行时下载、后端启动、推理后端检测和模型能力准备。

---

## Roadmap

近期重点：

1. Windows 本地后端自启动稳定化
2. Windows 本地 AI 准备流程闭环
3. 模型下载状态与进度展示
4. 会话上下文管理
5. 桌面 UI 产品化
6. 临时运行时覆盖层清理
7. 企业级服务接口统一验收

---

## License

Internal prototype / demo package.
