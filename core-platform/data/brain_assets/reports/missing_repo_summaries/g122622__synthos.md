# Missing Repo Summary Source: g122622/synthos

- URL: https://github.com/g122622/synthos
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/g122622__synthos
- Clone Status: cloned
- Language: TypeScript
- Stars: 25
- Topics: llm, qq
- Description: 基于 Node.js 和 TypeScript 构建的智能聊天记录分析系统，专注于 QQ 聊天记录的全链路数据处理与 AI 总结功能，融合自然语言处理、向量模型、任务调度与 Web 前端展示，为用户提供从原始聊天记录导入、上下文理解、兴趣度分析到可视化摘要输出的一站式解决方案。

## Extracted README / Docs / Examples



# FILE: README.md

# Synthos：智能聊天记录全链路分析系统

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/g122622/synthos)

## 项目简介

Synthos 是一个基于 `Node.js` 和 `TypeScript` 构建的智能聊天记录分析系统，专注于 QQ 聊天记录的全链路数据处理与 AI 总结功能。项目采用现代化的 Monorepo 架构，融合自然语言处理、向量模型、任务调度与 Web 前端展示，为用户提供从原始聊天记录导入、上下文理解、兴趣度分析到可视化摘要输出的一站式解决方案。

无论是个人用户希望回顾重要对话，还是团队管理者需要洞察群聊趋势，Synthos 都能通过 AI 赋能，**让分散在不同群聊、不同时间的海量聊天信息变得可读、可查、可理解，将流式、易失的聊天记录沉淀为结构化、持久化的个人专属知识库**。

> ## 声明
>
> 1. Synthos 项目的启动目的是为了减轻手动阅读和管理巨量群聊信息的负担，不负责验证这些信息的完整性、准确性、时效性、合规性，不保证使用这些信息而获得的结果。对于有害信息造成的负面影响，作者亦不承担任何责任。
> 2. Synthos 通过非官方技术手段解密并解析 QQ 的本地消息数据库来获取群聊消息。在读取数据库的过程中，会全程保持只读，不会对用户数据完整性造成损坏；由于 Synthos 采用旁路方式非侵入式的获取群聊消息，因此被官方检测到并封号的风险极低。

---

## 界面展示

亮色模式：  
![亮色模式](./docs/assets/前端截图2.webp)

暗黑模式：  
![暗黑模式](./docs/assets/前端截图1.webp)

细节交互：  
![细节](./docs/assets/前端截图3.webp)

群组管理界面：  
![群组管理](./docs/assets/前端截图4.webp)

配置面板
![配置面板](./docs/assets/配置面板截图.png)

---

## 系统架构

![系统架构图](./docs/assets/Synthos架构7.drawio.png)

Deepwiki: [https://deepwiki.com/g122622/synthos](https://deepwiki.com/g122622/synthos)

---

## 核心功能特性

- **智能预处理**：自动分组、上下文拼接、引用消息追踪
- **AI 摘要生成**：基于 云端/本地 模型生成高质量对话摘要
- **兴趣度指数**：用户可设置关键词偏好，系统为每个话题打分排序（支持负向反馈）
- **历史记录自动拉取**：支持增量同步与历史回溯
- **日报自动生成**：每日汇总高价值讨论内容
- **多群组管理**：灵活配置不同群组的分析策略

### Agent 对话（流式）

- WebUI 对外提供 Agent 问答能力，并支持 **REST SSE（`POST /api/agent/ask/stream`）** 全流式输出。
- 事件协议为稳定业务事件：`token` / `tool_call` / `tool_result` / `done` / `error`（用于前端展示 token 与工具调用过程）。
- 单实例并发保护：同一 `conversationId` 不允许并发双发（冲突时返回 HTTP `409`）。

接口细节（请求参数、事件格式、time-travel 接口等）见：[docs/接口文档/API文档.md](./docs/接口文档/API文档.md)

> **TODO愿望单**  
>
> - [TODO] 转发聊天记录跟随  
> - ✅ 已完成 引用聊天记录跟随  
> - [TODO] 主动拉取历史聊天记录（⚠️目前技术实现遇到困难）
> - ✅ 每天生成日报
> - ✅ 简单易用的设置面板
> - ✅ 已完成 将兴趣度打分后端模型迁移至ollama的bge-m3，以利用GPU加速
> - ✅ 支持在打分或者rag向量生成时，自动将群昵称替换为类似"用户1"这样的昵称，避免抽象昵称影响模型理解
> - ✅ 已完成 用户输入rag问题后，先让llm生成查询计划（Multi-Query），然后再查向量数据库，并对结果去重
> - ✅ 构建rag问答上下文时，插入当前日期和每个话题的日期，以提高模型回答的准确性
> - ✅ RAG前端问答页面支持 1. 解析话题，并在鼠标hover后自动展示话题详情浮层 2. 渲染markdown 3. 支持全文复制
> - ✅ RAG支持记忆历史会话
> - ✅ 已完成 init() 防重入
> - [TODO] 支持根据nickname反查qq号，进而展示头像
> - [TODO] 支持按照群友发言数量排名（可按照群、时间段等筛选）、分析根据每个群友的发言内容生成群友画像
> - [TODO] 预处理支持对图片进行ocr和vllm识别
> - ✅ 生成摘要、回答等场景的上下文补充背景知识（使用关键词检索来召回）
> - [TODO] 上下文中间件支持补充链接查询结果
> - [TODO] 上下文中间件支持过滤违禁词
> - ✅ 后端子项目可以监听代码变动，进行HMR
> - [TODO] 支持可视化任务编排
> - [TODO] 支持进行关键词or语义实时监听群内消息，并快速发邮件通知
> - ✅ 支持监控各个模块的CPU和内存占用、支持监控存储空间占用。将这些数据持久化，并可通过前端看到趋势图，以及通过健康检测接口看到实时值。
> - ✅ 已完成 兴趣度指数：用户给出自己的兴趣偏好（关键词标签组），系统根据用户的兴趣偏好为每个话题打分，排序后推荐给用户。（用户也可以标记不喜欢的话题，此时话题得分为负数）
> - ✅ 已完成 向量嵌入与语义检索：基于 Ollama + bge-m3 生成话题向量嵌入，支持 RAG 语义搜索

---

## 技术架构

### 核心技术栈

- **🧑‍💻语言**：纯 TypeScript + Node
- **🎯项目管理**：Pnpm + Monorepo
- **🐳容器化/部署（WIP）**：Docker Compose + Nginx（前端静态托管 & /api 反代）
- **💬RPC库**：tRPC
- **💉依赖注入框架**：TSyringe
- **🕗任务调度与编排框架**：Agenda
- **📚数据库**：MongoDB（任务调度） + SQLite（聊天记录 & ai生成数据存储） + LevelDB（KV元数据存储） + sqlite-vec（向量索引存储）
- **📦向量数据库**：基于 better-sqlite3 + sqlite-vec 的轻量级向量存储方案
- **🤖LLM框架**：Langchain，支持任意云端 LLM or 本地的 Ollama
- **🧪测试框架**：Vitest  
- **🌏Web 后端框架**：Express
- **⚛️Web 前端框架**：React + ECharts + HeroUI + Tailwind CSS

### 模块划分

| 模块 | 职责 |
|------|------|
| `data-provider` | 从 QQ 等 IM 平台获取原始聊天记录 |
| `preprocessing` | 清洗、分组、上下文拼接、引用解析 |
| `ai-model` | 文本向量化、主题提取、摘要生成、兴趣度计算、向量嵌入存储与检索（RAG） |
| `orchestrator` | Pipeline 调度器，按顺序串联执行各数据处理任务（ProvideData → Preprocess → AISummarize → GenerateEmbedding → InterestScore） |
| `webui-backend` | 提供 RESTful API，支持群组管理、消息查询、结果获取 |
| `common` | 共享类型定义、配置管理、数据库工具、日志系统 |

---

## 快速开始

> ⚠️ **推荐硬件配置**  
>
> - 由于需运行 Ollama 服务（选配），加上 MongoDB、Node 进程和 SQLite 实例，**建议内存 ≥16GB**。
> - 中端 CPU
> - 【选配】支持 CUDA 的 GPU（如果 llm 和嵌入模型都使用云端服务，则无需本地 GPU）
> - 10G以上剩余硬盘空间。

![硬件要求](./docs/assets/hardware.png)

### 1. 环境准备

#### 安装 MongoDB

项目依赖 Agenda 进行任务调度，需提前安装 [MongoDB 社区版](https://www.mongodb.com/try/download/community) 并确保服务正在运行。

#### 安装 Ollama 并下载 bge-m3 模型（用于 RAG 向量检索）

项目使用 Ollama 部署 `bge-m3` 模型生成 1024 维嵌入向量，用于话题的语义检索。

1. **安装 Ollama**：访问 [Ollama 官网](https://ollama.ai/) 下载并安装

2. **拉取 bge-m3 模型**：

```bash
ollama pull bge-m3
```

1. **确保 Ollama 服务运行**：默认监听 `http://localhost:11434`

> 💡 **提示**：Ollama 服务会在系统启动时自动运行。如需手动启动，执行 `ollama serve`。

#### 准备配置文件

在项目根目录创建 `synthos_config.json`，格式请参考 [`./common/config/@types/GlobalConfig.ts`](.\common\config\@types\GlobalConfig.ts)。  
QQ 数据库密钥配置方法详见：[https://docs.aaqwq.top/](https://docs.aaqwq.top/)

附：**向量嵌入相关配置示例**（配置文件中的 `ai.embedding` 和 `ai.rpc` 部分）：

```json
{
  "ai": {
    "embedding": {
      "ollamaBaseURL": "http://localhost:11434",
      "model": "bge-m3",
      "batchSize": 10,
      "vectorDBPath": "./data/vectors.db",
      "dimension": 1024
    },
    "rpc": {
      "port": 7979
    }
  },
  "orchestrator": {
    "pipelineIntervalInMinutes": 60
  }
}
```

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `ollamaBaseURL` | Ollama 服务地址 | `http://localhost:11434` |
| `model` | 嵌入模型名称 | `bge-m3` |
| `batchSize` | 批量生成向量的大小 | `10` |
| `vectorDBPath` | 向量数据库存储路径 | - |
| `dimension` | 向量维度（需与模型匹配） | `1024` |
| `rpc.port` | RAG RPC 服务端口 | `7979` |

> 💡 **运维建议**：数据无价，项目运行中产生的 SQLite、LevelDB 数据库以及向量数据库建议定期执行"3-2-1"备份策略（3份副本、2种介质、1份异地），防止数据丢失。
>
### 2. 启动项目

#### 方式一：使用新的 HMR 开发模式（推荐）⚡

所有后端子项目现已支持**热重载（HMR）**功能，代码修改后会自动重新编译并重启服务，无需手动操作。

```bash
# 1. 安装monorepo依赖
pnpm i # 这不仅会安装根目录下的依赖，还会自动安装所有子项目的依赖

# 2. 启动所有服务（含前后端，支持热重载）
pnpm dev:all

# 或者，仅启动后端服务（不含前端）
pnpm dev:backend

# 或者，仅启动配置面板（轻量级模式）
pnpm dev:config

# 或者，启动完整服务 + 公网转发
pnpm dev:forwarder
```

---

## Docker 部署（WIP，暂不推荐）

该方案将 `orchestrator` / `preprocessing` / `ai-model` / `webui-backend` / `webui-frontend` / `MongoDB` 容器化，
`data-provider` 仍在宿主机运行（因为其依赖本机 QQNT 数据库与 VFS DLL）。

### 1) 启动容器

```bash
docker compose up -d --build
```

可选启用 Ollama：

```bash
docker compose --profile ollama up -d --build
```

### 2) 在宿主机启动 data-provider（连接容器 Mongo）

> 注意：`docker-compose.yml` 中提供了一个 `host-only` profile 下的 `data-provider` 占位服务，仅用于提示该组件需在宿主机运行，并不会真正容器化该进程。

```bash
set SYNTHOS_MONGODB_URL=mongodb://localhost:27017/synthos
pnpm --filter data-provider dev
```

PowerShell：

```powershell
$env:SYNTHOS_MONGODB_URL="mongodb://localhost:27017/synthos"
pnpm --filter data-provider dev
```

### 3) 访问 WebUI

- 前端（nginx）：http://localhost:8080
- 后端健康检查：http://localhost:3002/health
- AI RPC（tRPC HTTP/WS）：http://localhost:7979 （WS 同端口）

> 配置文件默认挂载为 `docker/config/synthos_config.json`（容器内路径：`/config/synthos_config.json`）。
> 如需自定义，可直接修改该文件，或使用 `synthos_config_override.json` 进行覆盖。
> 建议把敏感信息（如 `apiKey`/`dbKey`）放到 `synthos_config_override.json`（已被 gitignore），避免误提交。

**可用的启动脚本：**

| 命令 | 说明 | 包含的服务 |
|------|------|-----------|
| `pnpm dev:all` | 完整开发环境（推荐） | orchestrator, preprocessing, ai-model, data-provider, webui-backend, webui-frontend |
| `pnpm dev:backend` | 仅后端服务 | orchestrator, preprocessing, ai-model, data-provider, webui-backend |
| `pnpm dev:webui` | WebUI 开发模式 | ai-model, webui-backend, webui-frontend |
| `pnpm dev:config` | 配置面板模式 | webui-backend (配置模式), webui-frontend |
| `pnpm dev:forwarder` | 完整服务 + 公网转发 | 所有服务 + webui-forwarder |

**热重载特性：**

- ✅ **自动检测变化**：监听 `src/` 和 `common/` 目录的 `.ts` 和 `.json` 文件
- ✅ **快速重载**：修改代码后 2-5 秒内自动重新编译和重启
- ✅ **前端 HMR**：前端使用 Vite，支持极速的模块热替换（通常 < 1 秒）
- ✅ **并行启动**：所有服务并行启动，无需等待

#### 方式二：使用原有的启动脚本（兼容模式）

如果需要使用原有的串行启动方式（兼容性更好，但不支持热重载）：

```bash
# 启动所有服务（串行启动，间隔 3 秒）
npm run dev

# 或者，仅启动配置面板（轻量级模式）
npm run config
```

服务启动后，可通过以下方式验证：

- WebUI 后端：`http://localhost:3002`
- 健康检查接口：`GET /health`
- 配置面板：`http://localhost:5173/config`（仅启动配置面板时）

测试环境启用mock： `VITE_MOCK_ENABLED=true pnpm dev`

---

## API 与前端开发

- **API 文档**：详见 [`applications/webui-backend/docs/API文档.md`](.\applications\webui-backend\docs\API文档.md)
- **前端开发指引**：详见 [`applications/webui-backend/docs/前端开发指引文档.md`](.\applications\webui-backend\docs/前端开发指引文档.md)

核心接口包括：

- `GET /api/group-details`：获取群组列表
- `GET /api/chat-messages-by-group-id`：按群组查询消息
- `GET /api/ai-digest-result-by-topic-id`：获取 AI 摘要结果
- `GET /api/is-session-summarized`：检查会话是否已总结

---


# FILE: docs/HMR热重载实现文档.md

# Synthos 热重载（开发期自动重启）实现文档

## 概述

本文档记录 Synthos 后端各子项目在开发环境下实现“改代码自动重启”的方案。

- 目标：修改 `src/` 或 `common/` 后，自动触发构建并重启对应服务
- 范围：后端子项目（ai-model, webui-backend, data-provider, preprocessing, orchestrator, webui-forwarder）
- 说明：这里更准确地说是“热重载/自动重启（hot-reload）”，不是浏览器层面的 HMR

实施日期：2026年1月17日

---

## 技术方案

### 方案选择

我们尝试过两类方案，最终采用统一的 runner 脚本：

1. **tsx watch（初次尝试，已弃用）**
   - 问题：与项目中大量使用的装饰器（如 tsyringe 的 parameter decorators）存在兼容性限制

2. **nodemon + 原有构建流程（中期尝试，已弃用）**
   - nodemon 相关的 `dev.js` / `nodemon.json` / `start*.js` 等文件已从仓库移除

3. **scripts/devRunner.cjs（最终采用）** ✅
   - 使用 `chokidar` 监听文件变化
   - 变化后执行现有构建流程，再重启 Node 进程
   - 统一封装 Windows 下的进程树结束、端口占用清理等细节

### 架构设计

```
开发者修改代码
   │
   ▼
chokidar 监听变化 (src + common)
   │
   ▼
执行构建流程
  1) pnpm -s run build
  2) node ../../scripts/redirectRequire.js
  3) node ../../scripts/fixESMExtensions.mjs
   │
   ▼
停止旧进程 /（可选）释放端口
   │
   ▼
启动新进程 (node <entry>)
```

---

## 使用方式

### 1) 安装依赖

根工作区需要：

```bash
pnpm add -Dw chokidar concurrently
```

> 注：`nodemon` / `tsx` 不再作为本方案的必要依赖。

### 2) 子项目 dev 脚本

每个后端子项目的 `package.json` 将 `dev` 指向统一 runner，例如（示意）：

```json
{
  "scripts": {
    "dev": "node ../../scripts/devRunner.cjs --name ai-model --entry dist/index.js --kill-port 7979"
  }
}
```

其中：

- `--name`：用于日志标识
- `--entry`：构建产物入口（通常是 `dist/index.js`）
- `--kill-port`：可选；在 Windows 上常见的端口占用问题可通过它在重启前释放端口

更完整参数请直接查看 [scripts/devRunner.cjs](scripts/devRunner.cjs)。

### 3) Workspace 一键启动

根 `package.json` 提供并行启动命令（依赖 `concurrently`）：

- `pnpm dev:backend`：启动后端相关服务
- `pnpm dev:all`：启动后端 + 前端
- `pnpm dev:config`：启动配置面板相关
- `pnpm dev:forwarder`：启动带 forwarder 的组合

### 4) 启动前命令（可选）

你可以在启动上述“一次启动多个子项目”的命令之前，先执行一个自定义命令（会开独立子进程执行，**不等待其执行完成**）。

在 `synthos_config.json` 增加：

```json
{
   "preStartCommand": {
      "enabled": true,
      "command": "<你的命令字符串>",
      "silent": true,
      "detached": false
   }
}
```

说明：

- `command`：交给系统 shell 解析执行，适合写一整串命令
- `silent`：是否静默（不输出 stdout/stderr）
- `detached`：是否以 detached 方式运行（父进程退出后仍继续运行）

---

## 故障排查

### 问题 1：修改后没有触发重启

- 确认变更文件在监听范围内（通常为子项目 `src/` 以及 `common/`）
- 查看 devRunner 的输出日志，确认 watcher 是否启动成功

### 问题 2：构建失败后无法恢复

- 先修复编译错误
- 观察下一次文件变更是否触发重新构建
- 必要时手动 Ctrl+C 停止后重启 `pnpm dev`

### 问题 3：端口被占用（EADDRINUSE）

- 给对应服务的 dev 脚本加上 `--kill-port <port>`（例如 `3002` / `7979`）
- 或手动排查端口占用后结束进程

---

## 总结

- 当前有效方案为统一的 [scripts/devRunner.cjs](scripts/devRunner.cjs)
- 历史上的 nodemon/tsx 方案已弃用，并且相关脚手架文件已清理
- 后端开发体验：改代码 → 自动构建 → 自动重启


# FILE: docs/接口文档/前端开发指引文档.md

﻿# 前端开发指引（已按源码更新）

> 面向 WebUI 前端：以当前后端实现为准完成接入与页面开发。

## 1. 本地联调

- WebUI Backend 默认：`http://localhost:3002`
- 建议：前端开发服务器配置代理 `/api -> http://localhost:3002/api`，并把 `/health` 也代理过去。

## 2. 通用调用约定

### 2.1 请求

- POST 请求统一 JSON：`Content-Type: application/json`
- 时间戳统一毫秒（UNIX ms）。

### 2.2 响应与错误

- 大多数接口：`{ success: true, data }` / `{ success: false, message }`
- 配置接口有少量分支使用 `{ success: false, error }`；建议统一做：

```ts
const errMsg = resp.message ?? resp.error ?? "未知错误";
```

- 系统监控接口是例外：直接返回对象/数组，不包 `success`。

### 2.3 参数小坑

- `GET /api/chat-messages-by-group-id` 的 `timeStart/timeEnd` 来自 query string，后端会 `parseInt`，请传字符串数字。

## 3. 页面/模块与接口映射（建议）

### 3.1 群组与聊天记录浏览

- 群组列表/群详情：`GET /api/group-details`

- 聊天消息列表（按群 + 时间范围）：
  - `GET /api/chat-messages-by-group-id?groupId=...&timeStart=...&timeEnd=...`
  - 返回包含 raw 字段 + `sessionId` + `preProcessedContent`（若已预处理）。

- 会话选择（按群 + 时间范围拉取 sessionId）：
  - `POST /api/session-ids-by-group-ids-and-time-range`
  - 渲染会话的时间范围：`POST /api/session-time-durations`

- 消息趋势（当前 24h + 昨日 24h）：`POST /api/message-hourly-stats`

### 3.2 主题/摘要结果

- 获取单个 topic 摘要：`GET /api/ai-digest-result-by-topic-id?topicId=...`
- 按会话批量获取摘要：`POST /api/ai-digest-results-by-session-ids`
- 判断会话是否已摘要：`GET /api/is-session-summarized?sessionId=...`

### 3.3 话题状态（收藏/已读）

- 收藏/取消收藏：
  - `POST /api/topic/favorite/mark`
  - `POST /api/topic/favorite/remove`

- 批量查询收藏状态（列表渲染前置）：`POST /api/topic/favorite/status`

- 已读/取消已读：
  - `POST /api/topic/read/mark`
  - `POST /api/topic/read/unmark`

- 批量查询已读状态：`POST /api/topic/read/status`

### 3.4 兴趣度评分

- 批量获取 topic 兴趣度：`POST /api/interest-score-results`

### 3.5 搜索与 RAG 问答

- 语义搜索：`POST /api/search`
- RAG 问答：`POST /api/ask`（返回 `answer + references`）

#### 3.5.1 WebUI 侧问答历史（本地持久化）

如果需要问答历史在 WebUI 内可回看：

- 列表分页：`POST /api/rag/session/list`（limit/offset）
- 详情：`POST /api/rag/session/detail`
- 删除：`POST /api/rag/session/delete`
- 改标题：`POST /api/rag/session/update-title`
- 清空：`POST /api/rag/session/clear-all`

说明：会话创建不再由前端显式调用接口完成；WebUI-Backend 会在 tRPC `askStream` 流式结束后自动落库，并在 `done` chunk 中返回 `sessionId`。

### 3.6 日报中心

- 列表分页：`POST /api/reports`（page/pageSize，可选 type）
- 单条详情：`GET /api/report/:reportId`
- 最近日报：`POST /api/reports/recent`
- 按日期/时间范围：
  - `POST /api/reports/by-date`
  - `POST /api/reports/by-time-range`

- 已读状态：
  - `POST /api/report/read/mark`
  - `POST /api/report/read/unmark`
  - `POST /api/report/read/status`

- 运维/手动触发：
  - 生成：`POST /api/reports/generate`
  - 邮件发送：`POST /api/report/send-email`

### 3.7 系统监控

- 最新：`GET /api/system/monitor/latest`（建议 1s~3s 轮询）
- 历史：`GET /api/system/monitor/history`（用于折线图）

注意：该模块接口返回 **不含** `success` 包裹。

### 3.8 日志查看（System Monitor / Logs）

- 日志分页查询（每次建议 100 条，按时间从新到旧）：`POST /api/logs/query`

请求示例：

```json
{
  "limit": 100,
  "before": 1737619200000,
  "startTime": 1737532800000,
  "endTime": 1737619200000,
  "levels": ["info", "warning", "error"]
}
```

说明：

- `before` 为时间戳 cursor（UNIX ms），用于向上翻加载更旧日志；后端会返回 `nextBefore` 供下一次请求继续使用。
- 日志文件目录来自 `synthos_config.json` 的 `logger.logDirectory`（不是仓库内的 `logs/` 目录）。

### 3.9 Agent 对话

- 发起问答：`POST /api/agent/ask`
- 会话列表分页：`POST /api/agent/conversations`（beforeUpdatedAt + limit）
- 会话消息分页：`POST /api/agent/conversations/:id/messages`（beforeTimestamp + limit）

说明：消息返回中的 `toolsUsed/tokenUsage` 后端已从 DB JSON 字符串解析为对象/数组，前端可直接展示。

## 4. 配置面板（Config Panel）

后端提供配置 CRUD + 校验接口（正常模式也可用）：

- Schema：`GET /api/config/schema`（适合动态表单渲染/前端校验提示）
- 当前合并配置：`GET /api/config/current`
- 基础配置：`GET/POST /api/config/base`
- Override 配置：`GET/POST /api/config/override`
- 校验：`POST /api/config/validate`（支持 partial 校验）

注意：保存 override 后端会提示需要手动重启服务以使配置生效，前端建议在保存成功后明确提示用户。

## 5. 调试建议

- 先打 `/health` 验证后端是否启动。
- 遇到失败响应，统一把 `message/error` 打到控制台，便于快速定位。


# FILE: docs/接口文档/API文档.md

# WebUI Backend API 文档（已按源码重写）

## 1. 服务信息

- 默认本地地址：`http://localhost:3002`
- 端口来源：
    - 正常模式：取配置 `webUI_Backend.port`
    - 配置面板模式：取环境变量 `CONFIG_PANEL_PORT`（默认 3002）

## 2. 通用约定

### 2.1 Content-Type

- 除 GET 查询参数外，所有 POST 请求都使用 JSON：`Content-Type: application/json`

### 2.2 时间戳

- 全部使用 **UNIX 毫秒时间戳**。
- 对于 POST JSON body：请直接传 number。
- `GET /api/chat-messages-by-group-id` 的 `timeStart/timeEnd` 来自 query string，只能是字符串；请传“字符串形式的数字”，后端会 `parseInt`。

### 2.3 通用响应格式（大多数接口）

成功：

```json
{ "success": true, "data": {} }
```

部分“成功但无数据”的接口使用 `message`：

```json
{ "success": true, "message": "..." }
```

失败（全局错误处理中间件）：

```json
{ "success": false, "message": "错误描述" }
```

### 2.4 例外：系统监控接口不包裹 success

- `GET /api/system/monitor/latest`：直接返回 `SystemStats` 或 `{}`
- `GET /api/system/monitor/history`：直接返回 `SystemStats[]`

### 2.5 例外：配置接口的部分错误字段为 error

`ConfigController` 中部分分支直接返回：

```json
{ "success": false, "error": "..." }
```

或：

```json
{ "success": false, "error": "配置验证失败", "details": ["..."] }
```

前端应同时兼容 `message` 与 `error`。

---

## 3. 健康检查

### GET /health

响应：

```json
{
  "success": true,
  "message": "WebUI后端服务运行正常",
  "timestamp": "2026-01-19T00:00:00.000Z"
}
```

---

## 4. 群组

### GET /api/group-details

说明：返回当前配置中的 `groupConfigs`（结构由配置决定）。

响应：

```json
{ "success": true, "data": { "<groupId>": { "IM": "QQ" } } }
```

---

## 5. 聊天消息

### GET /api/chat-messages-by-group-id

Query：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 群组ID |
| timeStart | string | 是 | 起始时间戳（毫秒，字符串） |
| timeEnd | string | 是 | 结束时间戳（毫秒，字符串） |

响应 `data`：`ProcessedChatMessageWithRawMessage[]`

```ts
type ProcessedChatMessageWithRawMessage = {
  msgId: string;
  messageContent: string;
  groupId: string;
  timestamp: number;
  senderId: string;
  senderGroupNickname: string;
  senderNickname: string;
  quotedMsgId?: string;
  quotedMsgContent?: string;
  sessionId: string;
  preProcessedContent?: string;
}[];
```

### POST /api/session-ids-by-group-ids-and-time-range

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupIds | string[] | 是 | 群组ID数组 |
| timeStart | number \| string | 是 | 起始时间戳（毫秒） |
| timeEnd | number \| string | 是 | 结束时间戳（毫秒） |

响应 `data`：

```ts
{ groupId: string; sessionIds: string[] }[]
```

### POST /api/session-time-durations

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionIds | string[] | 是 | 会话ID数组 |

响应 `data`：

```ts
{ sessionId: string; timeStart?: number; timeEnd?: number }[]
```

### POST /api/message-hourly-stats

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupIds | string[] | 是 | 群组ID数组 |

响应 `data`：

---

### POST /api/chat-messages-fts-search

说明：聊天消息“全文检索（FTS）”查询接口。该接口查询的是独立的 FTS 数据库文件（由 db-cli 手动构建索引）。

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 搜索文本（纯文本，不暴露 FTS 语法） |
| groupIds | string[] | 否 | 群组过滤；不传则全库 |
| timeStart | number | 否 | 起始时间戳（毫秒） |
| timeEnd | number | 否 | 结束时间戳（毫秒） |
| page | number | 是 | 从 1 开始 |
| pageSize | number | 是 | 1~100 |

响应 `data`：

```ts
{
  groups: {
    groupId: string;
    count: number; // 该群组命中总数
    hits: {
      msgId: string;
      timestamp: number;
      snippet: string; // 片段（高亮由前端完成）
    }[];
  }[];
  total: number; // 全库命中总数（groupIds/time 过滤后）
  page: number;
  pageSize: number;
}
```

备注：群组之间按命中数降序，群内默认按相关性（FTS bm25）优先、再按时间。

### POST /api/chat-messages-fts-context

说明：根据命中消息获取前后 N 条上下文（用于点击命中后展开）。

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| groupId | string | 是 | 群组ID |
| msgId | string | 是 | 目标消息ID |
| before | number | 否 | 取前 N 条，默认 20，0~200 |
| after | number | 否 | 取后 N 条，默认 20，0~200 |

响应 `data`：`ProcessedChatMessageWithRawMessage[]`

```ts
{
  data: Record<string, { current: number[]; previous: number[] }>;
  timestamps: { current: number[]; previous: number[] };
  totalCounts: { current: number; previous: number };
}
```

---

## 6. AI 摘要

### GET /api/ai-digest-result-by-topic-id

Query：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| topicId | string | 是 | 主题ID |

响应 `data`：

```ts
{
  topicId: string;
  sessionId: string;
  topic: string;
  contributors: string;
  detail: string;
  modelName: string;
  updateTime: number;
}
```

### POST /api/ai-digest-results-by-session-ids

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionIds | string[] | 是 | 会话ID数组 |

响应 `data`：

```ts
{ sessionId: string; result: AIDigestResult[] }[]
```

### GET /api/is-session-summarized

Query：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sessionId | string | 是 | 会话ID |

响应：

```json
{ "success": true, "data": { "isSummarized": true } }
```

---

## 7. 杂项

### GET /api/qq-avatar

Query：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| qqNumber | string | 是 | QQ 号码 |

响应：

```json
{ "success": true, "data": { "avatarBase64": "..." } }
```

---

## 8. 兴趣度评分

### POST /api/interest-score-results

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| topicIds | string[] | 是 | 主题ID数组 |

响应 `data`：

```ts
{ topicId: string; score: unknown }[]
```

---

## 9. 话题状态（收藏 / 已读）

### POST /api/topic/favorite/mark

Body：`{ "topicId": string }`

响应：`{ "success": true, "message": "话题已标记为收藏" }`

### POST /api/topic/favorite/remove

Body：`{ "topicId": string }`

响应：`{ "success": true, "message": "话题已从收藏中移除" }`

### POST /api/topic/favorite/status

Body：`{ "topicIds": string[] }`

响应：

```json
{ "success": true, "data": { "favoriteStatus": { "<topicId>": true } } }
```

### POST /api/topic/read/mark

Body：`{ "topicId": string }`

响应：`{ "success": true, "message": "话题已标记为已读" }`

### POST /api/topic/read/unmark

Body：`{ "topicId": string }`

响应：`{ "success": true, "message": "话题已读状态已清除" }`

### POST /api/topic/read/status

Body：`{ "topicIds": string[] }`

响应：

```json
{ "success": true, "data": { "readStatus": { "<topicId>": false } } }
```

---

## 10. 搜索与问答

### POST /api/search

Body：

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| query | string | 是 | 搜索文本 |
| limit | number | 否 | 默认 10 |

响应 `data`：

```ts
{
  topicId

# FILE: docs/迭代历程/日报.md

# 基本思路

功能：
个人用户回顾自己关注的群聊
其实是半日报（定时任务，中午、晚上各推送过去半天的群聊消息）
还可以再来个周报、月报
不需要支持分享

内容：
基于已有的 AIDigestResult（话题摘要），挑选高价值话题汇总成日报。实现细节是：先去掉兴趣度为负数的话题，然后提取出标题喂给llm；除了标题外，也可以选择一些具体内容喂给llm
希望日报是unity的，即不需要按群组分类展示，平等对待这些信息
日报中需要包含数据统计（如话题总数、最活跃群组、最活跃时段等）
统计数据在日报中的呈现位置：在开头（先看统计，再看综述和话题）

UI：
web端展示（日报需要存储在数据库中，以便历史查阅，可追溯历史日报） + 邮件推送

---

# 实现状态: ✅ 已完成

## 新增/修改的文件清单

### common 模块
- `common/config/@types/GlobalConfig.ts` - 新增 `ReportConfigSchema` 配置
- `common/database/constants/InitialSQL.ts` - 新增 `createReportTableSQL` 建表语句
- `common/database/ReportDbAccessService.ts` - 新增日报数据库管理器
- `common/contracts/report/index.ts` - 新增日报类型定义
- `common/scheduler/@types/Tasks.ts` - 新增 `GenerateReport` 任务类型

### ai-model 模块
- `ai-model/src/tasks/GenerateReport.ts` - 新增日报生成任务
- `ai-model/src/context/prompts/ReportPromptStore.ts` - 新增日报 Prompt 模板
- `ai-model/src/index.ts` - 注册日报生成任务

### webui-backend 模块
- `webui-backend/src/services/EmailService.ts` - 新增邮件发送服务
- `webui-backend/src/services/ReportService.ts` - 新增日报业务服务
- `webui-backend/src/controllers/ReportController.ts` - 新增日报控制器
- `webui-backend/src/schemas/index.ts` - 新增日报参数校验 Schema
- `webui-backend/src/di/tokens.ts` - 新增日报相关 Token
- `webui-backend/src/di/container.ts` - 注册日报相关依赖
- `webui-backend/src/routers/apiRouter.ts` - 新增日报 API 路由
- `webui-backend/src/lifecycle/dbInitialization.ts` - 初始化 ReportDbAccessService
- `webui-backend/src/index.ts` - 注册 ReportDbAccessService
- `webui-backend/package.json` - 新增 nodemailer 依赖

### orchestrator 模块
- `orchestrator/src/index.ts` - 新增日报定时任务调度

### webui-frontend 模块
- `webui-frontend/src/api/reportApi.ts` - 新增日报 API 调用
- `webui-frontend/src/pages/reports/reports.tsx` - 新增日报页面
- `webui-frontend/src/pages/reports/components/ReportCard.tsx` - 新增日报卡片组件
- `webui-frontend/src/pages/reports/components/ReportDetailModal.tsx` - 新增日报详情弹窗
- `webui-frontend/src/App.tsx` - 新增日报路由
- `webui-frontend/src/config/site.ts` - 新增日报导航

---

# 细节

### 1. 功能定义
| 维度 | 说明 |
|------|------|
| **报告类型** | 半日报、周报、月报 |
| **定时触发** | 中午、晚上各推送一次半日报 |
| **内容来源** | 基于 `AIDigestResult`，过滤掉兴趣度 < 0 的话题 |
| **LLM处理** | 提取话题标题（及部分正文 detail字段）喂给 LLM 生成综述 |
| **内容风格** | Unity（统一展示，不按群组分类） |
| **统计数据** | 话题总数、最活跃群组、最活跃时段等 |

### 2. 技术实现
| 模块 | 实现方式 |
|------|----------|
| **存储** | 新增数据库表存储日报/周报/月报 |
| **调度** | 使用现有 Agenda 框架，新增定时任务 |
| **前端** | 新增"日报"页面，支持历史查阅 |
| **邮件** | 需要新增邮件发送基建（项目中暂无） |

---

## ❓ 需要进一步明确的问题

### 一、关于定时触发的时间点

1. **"中午"和"晚上"的具体时间是？**
   - 默认：中午 12:00、晚上 18:00
   - 但也是可配置的（在 GlobalConfig 中配置）

2. **半日报覆盖的时间范围按照"中午"和"晚上"的具体时间来分割**

### 二、关于 LLM 生成综述

3. **LLM 生成的内容格式是什么？**
   - 纯文本综述（如"今天群里主要讨论了 xxx，其中关于 yyy 的讨论较为激烈..."）

4. **喂给 LLM 的内容上限是多少？**
   - 如果某个时段有 100 个话题，只取 Top N
   - Top N 的排序依据是兴趣度评分
   - N 的值可配置

5. **LLM 调用失败时的兜底策略是什么？**
   - 重试 N 次后放弃（不生成综述，只展示原始话题列表）
   - N 可配置

如果某个时段没有任何话题（或过滤后为空），则生成一个"本时段暂无热门话题"的空日报，并将isEmpty置为true

### 三、关于数据统计

6. **"最活跃群组"的定义是什么？**
   话题数量最多的群

7. **"最活跃时段"的粒度是什么？**
   按小时（如 14:00-15:00）

### 四、关于邮件推送

8. **邮件推送的收件人是谁？**
   在配置文件中配置固定邮箱（数组）

9. **邮件内容和 Web 端展示的内容一致**

10. **邮件发送方式？**
    - 使用 SMTP（需配置邮箱账号密码）

邮件的标题格式：[Synthos 半日报] 2024-01-15 上午

邮件发送失败: 重试 N 次,记录日志(n可配置)

### 五、关于周报/月报

11. **周报/月报的触发时机是？**
    - 周报：默认每周一早上（可配置）
    - 月报：默认每月1号早上（可配置）

12. **周报/月报的生成逻辑是？**
    - 汇总该周期内的所有半日报 + 辅以独立查询该周期的原始话题数据重新生成

### 六、关于 Web 端展示

13. **日报页面的交互设计？**
    - 需要日历视图方便选择历史日期
    - 支持按周/月切换视图

14. **日报中的话题是否可点击跳转到详情？**
    - 类似现有的 `latest-topics` 页面中的 `TopicCard`

# 技术细节

## 日报存储的格式：

```ts
interface Report {
  reportId: string;                      // 主键
  type: 'half-daily' | 'weekly' | 'monthly';  // 报告类型
  timeStart: number;               // 统计周期开始时间 毫秒级时间戳
  timeEnd: number;                 // 统计周期结束时间 毫秒级时间戳

  isEmpty: boolean; // 没有任何话题（或过滤后为空）
  
  // LLM 生成的综述
  summary: string;                 // 综述文本
  summaryGeneratedAt: Date;        // 综述生成时间
  summaryStatus: 'success' | 'failed' | 'pending';  // 生成状态
  model: string; // 生成综述时的模型名
  
  // 统计数据
  statistics: {
    topicCount: number;            // 话题总数
    mostActiveGroups: string[];       // 最活跃群组（取三个）
    mostActiveHour: number;        // 最活跃时段（小时）
  };
  // 关联的话题 ID 列表（用于点击跳转）
  topicIds: string[];
  
  createdAt: number;
  updatedAt: number;
}
```


# FILE: docs/迭代历程/Agent问答.md

RAG问答新增agent能力，可调用的工具如下：

- RAG搜索
- SQL查询（查之前先返回一次数量）
- Web搜索

目前已升级为 REST SSE（`POST /api/agent/ask/stream`）实现全流式，并定义稳定的业务事件协议：

- `token`：模型输出的增量文本
- `tool_call`：工具调用（用于审阅展示）
- `tool_result`：工具结果（任意 JSON，用于审阅展示）
- `done`：一次问答结束（含落库后的 `messageId` 等摘要信息）
- `error`：错误


# FILE: docs/迭代历程/系统状态监控面板.md



> 一个深色主题的本地存储管理界面，用于 ChatLab 聊天 AI 应用。整体风格简洁现代，采用圆角卡片、柔和阴影和清晰的排版。  
> 
> **顶部标题区**：  
>
> - 主标题：“本地存储管理”（白色加粗字体）  
> - 副标题：“管理 ChatLab 在本地存储的数据文件”（浅灰色小字）  
> - 右上角显示总占用空间：“总占用：306 B”，并附带一个刷新图标（↻）  
>
> **三个主要功能卡片**（垂直排列，每张卡片有图标、标题、说明、状态和操作按钮）：  
>
> 1. **聊天记录数据库**  
>    - 图标：绿色圆形图标  
>    - 说明：“导入的聊天记录分析数据”  
>    - 状态：“0 文件 | 0 B”  
>    - 操作按钮：“打开” + 文件夹图标  
>
> 2. **AI 对话数据库**  
>    - 图标：紫色圆形图标  
>    - 说明：“AI 对话历史和配置文件”  
>    - 状态：“0 文件 | 0 B”  
>    - 操作按钮：“打开” + 文件夹图标  
>
> 3. **日志文件**  
>    - 图标：蓝色文档图标  
>    - 说明：“软件的运行日志，包含导入、AI、错误等日志”  
>    - 状态：“1 文件 | 306 B”  
>    - 操作按钮：“清理”（带垃圾桶图标）+ “打开”（带文件夹图标）  
>
> **注意事项警告区**：  
>
> - 橙色背景警示框，左侧有黄色感叹号三角图标  
> - 标题：“注意事项”  
> - 内容：  
>   • 日志文件主要用于排查 BUG，可以安全清理  
>   • 所有文件清理后无法恢复，请谨慎操作  

> **整体视觉风格**：  
>
> - 背景色：深灰（#121212 或类似）  
> - 卡片背景：稍亮的深灰（如 #1e1e1e），带轻微圆角和内边距  
> - 文字颜色：白色（主标题）、浅灰（说明文字）、橙色（警告）、绿色/紫色/蓝色（对应图标）  
> - 图标风格：线性或面性简约图标，与文字对齐  

上述文字是其他项目中的。你需要仿照上述设计风格，参考common\services\config\schemas\GlobalConfig.ts中涉及的数据库和日志存储路径，统计存储大小，并增加支持监控各个模块的CPU和内存占用、支持监控存储空间占用。将这些数据每秒采样一次，滚动存入内存（保存最近5min的数据），并可通过前端看到趋势图和实时值。


# FILE: docs/迭代历程/嵌入模型数据清洗.md

【背景】

export interface AIDigestResult {
    topicId: string; // 主题id
    sessionId: string; // 摘要所属会话id
    topic: string; // 摘要主题
    contributors: string; // 群聊中的话题参与者
    detail: string; // 摘要详情正文部分
}

一个典型的摘要结果如下：

{
    topicId: 1ZeM7KVnSsvJXpcn
    sessionId: IoCN7JPSLoxDNBzq
    topic: 蓝桥杯竞赛是否仍可作为保研加分项
    contributors: ["2023-scau-奇华","23-xmu-五周目","23-fwu-Cody","22-xdu-thu-残心","23-shnu-yuan","24-fwu-mo","22-yxu-slow","22-图书馆求导被开除-好想进组😭😭😭","22-bjtu-白菜","23 yzu"]
    detail: 2023-scau-奇华询问“蓝桥杯还能加保研分吗”，引发多人群回“看自己学校的保研条例”。22-xdu-thu-残心补充“很多学校都不加”，22-yxu-slow推测“换主办方今年估计都不加了”。22-图书馆求导被开除-好想进组😭😭😭指出部分学校“按历史惯例执行，改条例没那么快”，22-bjtu-白菜认为“学校可能都没关注”这一变动。讨论未达成统一结论，但共识是政策高度依赖各校具体规定，建议学生查阅本校最新文件而非依赖往届经验。
}

本项目需要将大量的AIDigestResult作为文档片段，喂给嵌入模型生成向量表示。

现希望rag向量生成前，自动将detail中的群昵称替换为类似“用户1”这样的昵称，避免昵称影响模型生成向量的精准度。


# FILE: docs/迭代历程/可视化编排.md

# 需求背景： 现在已有的这个 orchestrator 到底在“编排”什么？

### 1.1 固定写死的 5 步串行 Pipeline

`orchestrator` 定义了一个 `RunPipeline` 任务，然后在里面按顺序触发 5 个任务，并且每一步都“等上一部完成才继续”。

```13:160:/synthos/applications/orchestrator/src/index.ts
/**
 * Pipeline 执行顺序（严格串行）:
 * 1. ProvideData - 获取原始数据
 * 2. Preprocess - 预处理数据
 * 3. AISummarize - AI 摘要生成
 * 4. GenerateEmbedding - 生成向量嵌入
 * 5. InterestScore - 计算兴趣度评分
 */
// ...
const provideDataSuccess = await scheduleAndWaitForJob(TaskHandlerTypes.ProvideData, { /*...*/ }, POLL_INTERVAL, TASK_TIMEOUT);
// ...
const preprocessSuccess = await scheduleAndWaitForJob(TaskHandlerTypes.Preprocess, { /*...*/ }, POLL_INTERVAL, TASK_TIMEOUT);
// ...
```

### 1.2 “等待完成”的机制：不是 DAG 引擎，而是轮询 Mongo(Agenda jobs)

它用 `scheduleAndWaitForJob()`：先 `agendaInstance.now()` 立刻塞一个 job，然后轮询这个 jobId 的状态，直到 `lastFinishedAt` 或 `failedAt`。

```178:192:/synthos/common/scheduler/jobUtils.ts
export async function scheduleAndWaitForJob<T extends TaskHandlerTypes>(
    taskName: T,
    data: TaskParamsMap[T],
    pollIntervalMs: number,
    timeoutMs: number
): Promise<boolean> {
    LOGGER.info(`调度任务 [${taskName}]`);
    const job = await agendaInstance.now(taskName, data);
    return waitForJobCompletionByIdV3(job.attrs._id.toString(), pollIntervalMs, timeoutMs);
}
```

### 1.3 任务处理器分布在其它 apps 进程

- `ProvideData` 在 `applications/data-provider/src/index.ts` 里 `agendaInstance.define(...)`
- `Preprocess` 在 `applications/preprocessing/src/index.ts`
- `AISummarize/GenerateEmbedding/InterestScore/GenerateReport` 在 `applications/ai-model/src/tasks/*`

也就是说：**orchestrator 只是发号施令**；各任务由其它 Node 进程作为 worker 执行（共享同一个 MongoDB 的 `synthos_jobs` 集合）。

### 1.4 报告调度是独立子调度器

`orchestrator` 里还有 `setupReportScheduler()`：按 cron 配置定时 `agendaInstance.now(GenerateReport, ...)`。

```60:203:/synthos/applications/orchestrator/src/schedulers/reportScheduler.ts
await agendaInstance.every(cronExpression, `HalfDailyReport_${timeStr}`, {}, { skipImmediate: true });
// ...
agendaInstance.define(`HalfDailyReport_${timeStr}`, async () => {
  await agendaInstance.now(TaskHandlerTypes.GenerateReport, { reportType: "half-daily", timeStart, timeEnd });
});
```

# 需求概述

现在是“固定脚本串行调用”。我们要的“拖拽编排”本质需要两块能力：

1) **可视化建模**：拖拽节点、连线、配置节点参数（这是 UI / 模型）
2) **运行时执行器**：把图（DAG/流程）解释成一次次 job 调度，并处理：
   - 节点依赖（前置完成才运行）
   - 分支/并行/汇聚
   - 重试、超时、失败策略、跳过策略
   - 运行历史、可观测性
   - 支持**分支/并行/汇聚/条件判断**
   - 支持看到当前执行状态，运行到哪一步了

  现有代码可能已经包含部分上述逻辑（如检查网络连接、重试等），但是很分散且不好治理。

我们现在已有的只有：Agenda（定时/队列） + 一个“脚本式顺序控制”。

流程里节点类型需要覆盖现有 `TaskHandlerTypes`（ProvideData/Preprocess/...），也希望未来能“自定义脚本节点/HTTP 节点/循环”等。需要把各个任务执行期间的logger输出全部展示到前端页面。这需要：WebSocket 推送：后端实时推送日志行;关联流程执行 ID：每次 Pipeline 运行有唯一标识，日志带上这个 ID

我们希望流程定义存在哪里？继续沿用配置体系（`synthos_config_override.json`），好处是简单、可备份。

我们希望“编排 UI”集成到现有 `webui-frontend` 里（一个新页面）

# 具体实现

我打算使用 https://reactflow.dev/examples/overview 这个库。

需要订一个详细的、完备的流程编排契约！

可能涉及到applications\orchestrator和applications\webui-backend的tRPC通信

因为上述需求比较复杂，因此我想引入成熟的工作流和流程编排引擎。有没有什么强大的推荐？

请你先充分探索这个项目（并联网阅读https://reactflow.dev文档），然后和我讨论，以帮助我细化需求和技术细节。不要修改任何文件和代码！

尝试进行需求排期（因为一次肯定做不完这些东西！）


# FILE: docs/迭代历程/配置服务DI化改造.md

本次改造中的几个难点：

## 1. CommonDBService 的特殊设计挑战

问题：CommonDBService 原本在构造函数中接收 initialSQL 参数，而每个 DbAccessService（如 AgcDbAccessService、ImDbAccessService 等）都需要传入不同的建表 SQL。这与标准的 DI 单例模式冲突。

解决方案：将 initialSQL 从构造函数参数改为 init(initialSQL?) 方法参数，使 CommonDBService 可以被 DI 容器管理（每次 resolve 返回新实例），同时保持灵活性。

*// 改造前*

constructor(initialSQL?: string) { ... }

async init(): Promise<void> { ... }

*// 改造后*

public constructor(@inject(COMMON_TOKENS.ConfigManagerService) private configManagerService: IConfigManagerService) { ... }

public async init(initialSQL?: string): Promise<void> { ... }

## 2. TypeScript 装饰器配置缺失

问题：common/tsconfig.json 原本没有启用 experimentalDecorators 和 emitDecoratorMetadata，导致添加 @injectable() 和 @inject() 装饰器后编译报错：error TS1206: Decorators are not valid here。

解决方案：更新 common/tsconfig.json，添加装饰器相关配置：

{

  "experimentalDecorators": true,

  "emitDecoratorMetadata": true

}

## 3. 单例与非单例的权衡

问题：不同类型的服务需要不同的生命周期管理：

- ConfigManagerService、EmailService、TextGenerator 应该是单例（整个应用共享一个实例）

- CommonDBService、QQProvider、AccumulativeSplitter 应该是非单例（每次需要新实例，因为有独立的生命周期 init/dispose）

解决方案：使用不同的注册方式：

*// 单例*

container.registerSingleton(TOKEN, Class);

*// 或*

container.registerInstance(TOKEN, instance);

*// 非单例（每次 resolve 返回新实例）*

container.register(TOKEN, { useClass: Class });

## 4. 测试文件的适配

问题：单元测试和集成测试中直接 new QQProvider() 创建实例，改造后构造函数需要 configManagerService 参数，导致测试编译失败。

解决方案：

- 在测试开始前注册 DI 容器（registerConfigManagerService(), registerQQProvider()）

- 将 new QQProvider() 改为 getQQProvider()

## 5. 循环依赖的潜在风险

问题：PooledTextGenerator 和 GenerateReport 内部直接 new TextGenerator()，但 TextGenerator 改造后需要从 DI 获取。如果在 DI 容器完全初始化之前调用 getTextGenerator()，会导致运行时错误。

解决方案：确保 DI 注册顺序正确，registerTextGenerator() 必须在任何使用 getTextGenerator() 的代码之前调用。在 ai-model/src/index.ts 中明确了初始化顺序。

## 6. 默认单例导出的废弃

问题：EmailService 原本导出了一个默认单例实例 export default instance，改造后由于构造函数需要参数，无法直接 new EmailService() 创建默认实例。

解决方案：删除默认单例导出，统一通过 DI 容器管理：

*// 删除这些*

const instance = new EmailService();

export default instance;

*// 改为只导出类*

export { EmailService };

------

总体来说，最核心的挑战是平衡依赖注入的统一性与各类特殊需求（如 CommonDBService 的动态 SQL、非单例的生命周期管理等）。通过合理调整 API 设计（如将参数从构造函数移到 init 方法）和使用正确的 DI 注册方式，成功实现了改造目标。

# FILE: docs/迭代历程/数据库增量备份.md

# 需求概述

实现一个数据库中间层（位于PromisifiedSQLite下），拦截所有可能更改数据库数据&结构&元数据的SQL语句，将其转为压缩后的日志储存起来，后期恢复的时候只要重放一遍日志即可。

压缩使用gzip压缩，得到.tar.gz文件，每12小时生成一次，并存储在指定目录下。文件名字以`2023-06-15_00:00:00-12:00:00.tar.gz`的格式命名。


# FILE: docs/迭代历程/配置面板.md

【背景】

目前common/config/ConfigManagerService.ts负责从本地json文件加载配置。

希望引入一个用户友好的可视化配置面板，要求如下：

1. 在apps/webui-frontend/src/pages下新增配置页面，并更新相应的其他文件
2. 根目录package.json新增 npm run config命令，拉起配置面板（可以参考现有脚本scripts/launchAll.cjs的写法）新增一个launchConfigPanel脚本
3. 配置页面要求仅启动webui-frontend + webui-backend两个子项目即可完全可用
4. 前端需要对表单有效性进行实时验证，用户输入配置的类型由common/config/@types/GlobalConfig.ts决定。目前方案是：使用 Zod 定义配置 schema
5. 配置页面的表单粒度是：完整的可视化表单，每个配置项都有对应的输入控件

关于表单 UI 设计：单页长表单，通过锚点+侧边栏导航
ai.models 和 groupConfigs 是 Record<string, T> 类型（动态 key-value），需要支持添加/删除 key
ai.pinnedModels、ai.interestScore.UserInterestsPositiveKeywords 等是字符串数组，需要支持动态增删数组元素
前端在配置面板模式下需要隐藏其他导航项（只显示配置页面）
ai.models.*.apiKey、dataProviders.QQ.dbKey 等是敏感信息，需要特殊处理（如：密码输入框、部分遮蔽显示）
配置页面的路由路径：/config

# FILE: docs/迭代历程/监控兴趣话题并监听.md

## 背景

目前已经有“兴趣度打分”系统（位于applications\ai-model\src\tasks\InterestScore.ts），但是这个打分系统基于对话题 + 预先设定的关键词 计算语义嵌入向量相似度，得到浮点数并进行rank。这存在识别不够智能准确、且无法发邮件的问题。

## 需求

保持已有“兴趣度打分”任务相关代码不变的情况下，新开一个任务，并append到ai-model最后执行。

用户给定一个string[]（通过配置管理服务获取（这个配置项还没有，可以放在ai.interestScore下），里面最好是句子，便于ai思考） + topics（也是string[]），借助LLM进行兴趣度评价，LLM只给出boolean[]，每一项代表topics中指定下标的topic是否用户感兴趣，如果为true，则对应话题需要邮件通知用户（在applications\ai-model\src\services\email下新增一个InterestEmailService服务）。

为了减小llm调用量，需要成batch喂给llm，batchSize也从配置拿（这个配置项还没有，可以放在ai.interestScore下）

