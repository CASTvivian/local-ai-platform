# MAOMIAI Desktop Demo Guide

## 演示目标

本演示包展示 MAOMIAI 本地 AI 工作台当前阶段能力：

- 全中文桌面 UI
- 本地模型 qwen2.5:7b 调用
- 服务健康面板
- 技能商店
- 文档处理入口
- 工作流管理
- 产物中心
- 代码审查
- 仓库记忆
- 设计系统
- 模型设置入口
- 多会话聊天管理（初版）

## 当前产物

### macOS App

**路径**: `apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app`

**DMG**: `apps/desktop/src-tauri/target/release/bundle/dmg/Local AI Platform_0.1.0_aarch64.dmg`

---

## 启动顺序

### 1. 启动后端服务

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/desktop/start_desktop_services.sh
```

### 2. 检查服务状态

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/desktop/status_desktop_services.sh
```

### 3. 启动桌面 App

```bash
open "/Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app"
```

---

## 停止服务

```bash
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/desktop/stop_desktop_services.sh
```

---

## 核心服务

| 端口 | 服务 | 状态 |
|------|------|------|
| 18080 | Model Gateway | 已接入 |
| 18093 | Auto Router | 已接入 |
| 18104 | Runtime Execution | 已接入 |
| 18110 | Policy Engine | 已接入 |
| 18111 | Trace Observability | 已接入 |
| 18112 | Eval Gateway | 已接入 |
| 18120 | Document Ingestion | 部分硬化 |
| 18121 | Skill Store | enterprise |
| 18123 | Artifact Registry | enterprise |
| 18124 | Code Review Gate | enterprise |
| 18125 | Repo Memory | enterprise |
| 18126 | Workflow Store | enterprise |
| 18127 | Design System | enterprise |

---

## 模型链路

```
Desktop App
  -> 18080 Model Gateway
  -> 11434 Ollama
  -> qwen2.5:7b
```

已验证 qwen2.5:7b 能返回中文自然语言回复。

---

## 演示路径建议

### 1. 打开 App
点击 Dock 或 Finder 中的 "Local AI Platform"

### 2. 查看右侧服务健康面板
确认所有服务健康状态

### 3. 在输入框输入测试

**输入**: `你好，请用一句中文介绍你自己`

### 4. 验证本地模型回复

期望看到本地 AI 返回类似：
```
我叫Qwen，是来自阿里云的AI助手。
```

### 5. 点击左侧各页面

- 技能商店：查看技能列表
- 工作流：查看工作流列表
- 产物中心：查看产物列表
- 代码审查：输入危险命令 diff 测试
- 仓库记忆：查看仓库列表
- 设计系统：查看设计系统列表
- 模型设置：展示 P4 模型入口

---

## 已知问题

### 1. 会话上下文需要回归测试

当前已实现 `chat-session-manager.js`：

* 多会话
* localStorage 持久化
* 最近 16 条消息上下文
* model_gateway 调用

但还未完成完整人工验收。

### 2. 部分页面仍使用 Runtime Stable Override

为了保证演示稳定，当前加入了运行时覆盖层：

- `desktop-runtime-stable.js`
- `desktop-chat-stable.js`
- `chat-session-manager.js`

后续应逐步回收临时覆盖层，将逻辑沉淀回正式页面模块。

### 3. 18120 Document Ingestion 仍为部分硬化

后续需要继续接入：

* MinerU
* Docling
* PDF parser
* 文件上传链路
* 文档解析质量评估

---

## 当前阶段结论

当前版本适合做内部演示和技术路线展示，**不建议作为最终生产版本交付**。
