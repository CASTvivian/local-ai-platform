# Missing Repo Summary Source: moyangzhan/langchain4j-aideepin

- URL: https://github.com/moyangzhan/langchain4j-aideepin
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/moyangzhan__langchain4j-aideepin
- Clone Status: cloned
- Language: Java
- Stars: 1273
- Topics: ai-agent, ai-workflow, graphrag, knowlege-base, langchain4j, mcp, rag
- Description: 基于AI的工作效率提升工具（聊天、绘画、知识库、工作流、 MCP服务市场、语音输入输出、长期记忆） | Ai-based productivity tools (Chat,Draw,RAG,Workflow,MCP marketplace, ASR,TTS, Long-term memory etc)

## Extracted README / Docs / Examples



# FILE: README.md

## Getting Started

> **[🇨🇳 中文文档](README.zh-CN.md)** | English

**LangChain4j-AIDeepin is an AI-based productivity enhancement tool.**

*It can be used to assist enterprises/teams in technical research and development, product design, HR/finance/IT information consulting, system/product consulting, customer service support, etc.*

## System Composition and Documentation

```
AIDEEPIN
  |__ Server (langchain4j-aideepin)
  |__ User Web (langchain4j-aideepin-web)
  |__ Admin Web (langchain4j-aideepin-admin)
```

👉 [Detailed Documentation](docs/en/index.md)

Backend source repository: [github](https://github.com/moyangzhan/langchain4j-aideepin)

Frontend projects:

- User Web: langchain4j-aideepin-web
  - [github](https://github.com/moyangzhan/langchain4j-aideepin-web)
- Admin Web: langchain4j-aideepin-admin
  - [github](https://github.com/moyangzhan/langchain4j-aideepin-admin)

## Demo URL

[http://www.aideepin.com](http://www.aideepin.com/)

## Features

### AI Chat

Multi-conversation support with different AI roles. Each conversation can be configured with a specific system prompt, model, and parameters. Supports streaming output with real-time token display.

### Image Generation

Generate images from text prompts using models like GPT-Image-2 and DashScope's Wanx. Supports text-to-image, image editing, image variation, and background generation.

### Knowledge Base (RAG)

Build knowledge bases from uploaded documents (PDF, Word, PPT, Excel, etc.) and use them to enhance AI responses with retrieval-augmented generation.

- **Vector Search**: Embed documents into vector space using models like `all-minilm-l6-v2` or `bge-small-zh-v1.5`, then retrieve relevant chunks via similarity search
- **Graph Search**: Extract entities and relationships from documents to build knowledge graphs using Apache AGE or Neo4j, enabling structured knowledge retrieval

### AI Workflow

Visual workflow editor for building complex AI pipelines. Supports conditional branching, parallel execution, and various node types including LLM calls, knowledge base queries, code execution, and human feedback loops.

### MCP Service Marketplace

Discover and integrate MCP (Model Context Protocol) servers to extend AI capabilities with external tools and data sources. Supports SSE and stdio transport types.

### ASR & TTS

Full voice interaction support with flexible input/output combinations:

- Text question → Text response
- Text question → Voice response
- Voice question → Text response
- Voice question → Voice response

### Long-term Memory

Automatically extracts and stores key information from conversations as user memories, allowing the AI to personalize responses based on historical context.

### Storage

- Local file storage
- Alibaba Cloud OSS integration

## Integrated Platform Features

| Model Platform | Chat | Image Generation | Background Generation | Image Recognition | Text-to-Speech | Speech Recognition |
|:---------------|:----:|:----------------:|:---------------------:|:-----------------:|:--------------:|:------------------:|
| OpenAI         |  ✓   |        ✓         |                       |                   |                |                    |
| Dashscope      |  ✓   |        ✓         |           ✓           |         ✓         |       ✓        |         ✓          |
| SiliconFlow    |  ✓   |        ✓         |                       |         ✓         |       ✓        |         ✓          |
| Ollama         |  ✓   |                  |                       |                   |                |                    |
| DeepSeek       |  ✓   |                  |                       |                   |                |                    |

## Tech Stack

This repository is for the backend service.

Backend:

- JDK 17
- Spring Boot 3.5.14
- [langchain4j](https://github.com/langchain4j/langchain4j) (Java version of LangChain)
- [langgraph4j](https://github.com/bsorrentino/langgraph4j)
- PostgreSQL
  - [pgvector](https://github.com/pgvector/pgvector) extension (vector database)
  - [Apache AGE](https://github.com/apache/age) extension (graph database)
- [neo4j](https://neo4j.com/deployment-center/) (alternative to pgvector + Apache AGE)

Frontend:

- Vue 3
- Vite
- TypeScript
- pnpm
- Pinia
- Naive UI

## How to Deploy

### Initialization

**a. Initialize the database**

1. Create the database `aideepin`
2. Execute `db_migration/all_ddl.sql` to create tables
3. Execute `db_migration/all_dml.sql` to insert base data
4. Execute `db_migration/all_dml_en.sql` (English) or `db_migration/all_dml_cn.sql` (Chinese) to insert display data
5. Enable and configure the model platform (also referred to as model provider) or use the [admin web](https://github.com/moyangzhan/langchain4j-aideepin-admin) to configure via the interface

Configure model platforms:

```sql
-- DeepSeek
UPDATE adi_model_platform SET api_key = 'my_deepseek_secret_key' WHERE name = 'deepseek';

-- OpenAI
UPDATE adi_model_platform SET api_key = 'my_openai_secret_key' WHERE name = 'openai';

-- Dashscope
UPDATE adi_model_platform SET api_key = 'my_dashcope_api_key' WHERE name = 'dashscope';

-- Siliconflow
UPDATE adi_model_platform SET api_key = 'my_siliconflow_api_key' WHERE name = 'siliconflow_setting';

-- Ollama
UPDATE adi_model_platform SET base_url = 'my_ollama_base_url' WHERE name = 'ollama';
```

Enable models or add new models:

```sql
-- Enable models
UPDATE adi_ai_model SET is_enable = true WHERE name = 'deepseek-v4-flash';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'gpt-3.5-turbo';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'gpt-image-2';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'qwen-turbo';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'THUDM/GLM-Z1-9B-0414';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'tinydolphin';

-- Add new model
INSERT INTO adi_ai_model (name, type, platform, is_enable) VALUES ('vicuna', 'text', 'ollama', true);
```

Configure search engine (Google):

```sql
UPDATE adi_sys_config SET value = '{"url":"https://www.googleapis.com/customsearch/v1","key":"my key from cloud.google.com","cx":"my cx from programmablesearchengine.google.com"}' WHERE name = 'google_setting';
```

**b. Modify the configuration file**

Copy the example config and rename it:

```bash
cp adi-bootstrap/src/main/resources/application-dev.yml.example adi-bootstrap/src/main/resources/application-dev.yml
```

Then modify the following entries:

- PostgreSQL: `application-[dev|prod].yml` → `spring.datasource`
- Redis: `application-[dev|prod].yml` → `spring.data.redis`
- Mail: `application.yml` → `spring.mail`

### Build and Run

```bash
cd langchain4j-aideepin
mvn clean package -Dmaven.test.skip=true
```

Start with JAR:

```bash
cd adi-bootstrap/target
nohup java -jar -Xms768m -Xmx1024m -XX:+HeapDumpOnOutOfMemoryError \
  adi-bootstrap-0.0.1-SNAPSHOT.jar --spring.profiles.active=[dev|prod] \
  /dev/null 2>&1 &
```

Start with Docker:

```bash
cd adi-bootstrap
docker build . -t aideepin:0.0.1
docker run -d \
  --name=aideepin \
  -p 8888:9999 \
  -e APP_PROFILE=[dev|prod] \
  -v="/data/aideepin/logs:/data/logs" \
  aideepin:0.0.1
```

## Contributing Guidelines

All forms of contributions are welcome, including but not limited to:

- Submitting Bug Reports
- Proposing New Features
- Improving Documentation
- Submitting Code (PR)

Code Submission Process:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/xxx`)
3. Commit changes (`git commit -m 'feat: xxx'`)
4. Push the branch (`git push origin feature/xxx`)
5. Submit a Pull Request

## ⭐ Support the Project

If you find LangChain4j-AIDeepin useful, please consider:

- Starring the repository on GitHub
- Recommending it to others
- Sharing your experience

## ❤️ Thanks to

**Contributors**

<a href="https://github.com/moyangzhan/langchain4j-aideepin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=moyangzhan/langchain4j-aideepin" />
</a>

<br/>

## Recommended Projects

[Mango Finder](https://github.com/moyangzhan/mango-finder) — A local-first desktop app for semantic search across documents, images, and audio files using natural language, with cross-device search support. It helps you find information based on what you remember, not file names or folder structures.


# FILE: README.zh-CN.md

## Getting Started

> 中文文档 | **[🇬🇧 English](README.md)**

**LangChain4j-AIDeepin（得应AI） 是基于 AI 的工作效率提升工具。**

*可用于辅助企业/团队进行技术研发、产品设计、人事/财务/IT信息咨询、系统/商品咨询、客服话术支撑等工作*

## 系统组成及文档

```
AIDEEPIN
  |__ 服务端 (langchain4j-aideepin)
  |__ 用户端 WEB (langchain4j-aideepin-web)
  |__ 管理端 WEB (langchain4j-aideepin-admin)
```

👉 [详细文档](docs/cn/index.md)

后端服务代码地址：[github](https://github.com/moyangzhan/langchain4j-aideepin) | [gitee](https://gitee.com/moyangzhan/langchain4j-aideepin)

前端项目：

- 用户端 WEB：langchain4j-aideepin-web
  - [github](https://github.com/moyangzhan/langchain4j-aideepin-web) | [gitee](https://gitee.com/moyangzhan/langchain4j-aideepin-web)
- 管理端 WEB：langchain4j-aideepin-admin
  - [github](https://github.com/moyangzhan/langchain4j-aideepin-admin) | [gitee](https://gitee.com/moyangzhan/langchain4j-aideepin-admin)

## 体验网址

[http://www.aideepin.com](http://www.aideepin.com/)

## 功能点

### AI 对话

多会话（多角色）支持，每个会话可配置系统提示词、模型和参数，支持流式输出。

### 图片生成

支持 GPT-Image-2、灵积万相等模型，提供文生图、图片编辑、图片变体、背景生成等功能。

### 知识库（RAG）

上传文档（PDF、Word、PPT、Excel 等）构建知识库，通过检索增强生成提升 AI 回复质量。

- **向量搜索**：使用 `all-minilm-l6-v2`、`bge-small-zh-v1.5` 等模型进行文档向量化，通过相似度搜索检索相关内容
- **图搜索**：从文档中提取实体和关系构建知识图谱（Apache AGE 或 Neo4j），实现结构化知识检索

### AI 工作流

可视化工作流编辑器，支持条件分支、并行执行，以及 LLM 调用、知识库查询、代码执行、人工反馈等多种节点类型。

### MCP 服务市场

发现和集成 MCP（Model Context Protocol）服务，扩展 AI 的外部工具和数据源能力，支持 SSE 和 stdio 传输类型。

### ASR & TTS

支持灵活的语音输入输出组合：

- 文字提问 → 文字回复
- 文字提问 → 语音回复
- 语音提问 → 文字回复
- 语音提问 → 语音回复

AI 音色可选。

### 长期记忆

自动从对话中提取和存储关键信息作为用户记忆，使 AI 能够基于历史上下文进行个性化回复。

### 存储

- 本地存储
- 阿里云 OSS

## 已集成的模型平台功能

| 模型平台   | 对话 | 文生图 | 背景生成 | 图像识别 | 语音合成 | 语音识别 |
|:---------|:----:|:-----:|:-------:|:-------:|:-------:|:-------:|
| OpenAI   |  ✓   |   ✓   |         |         |         |         |
| 灵积      |  ✓   |   ✓   |    ✓    |    ✓    |    ✓    |    ✓    |
| 硅基流动   |  ✓   |   ✓   |         |    ✓    |    ✓    |    ✓    |
| Ollama   |  ✓   |       |         |         |         |         |
| DeepSeek |  ✓   |       |         |         |         |         |

## 技术栈

该仓库为后端服务。

后端：

- JDK 17
- Spring Boot 3.5.14
- [langchain4j](https://github.com/langchain4j/langchain4j)（Java 版 LangChain）
- [langgraph4j](https://github.com/bsorrentino/langgraph4j)
- PostgreSQL
  - [pgvector](https://github.com/pgvector/pgvector) 扩展（向量数据库）
  - [Apache AGE](https://github.com/apache/age) 扩展（图数据库）
- [neo4j](https://neo4j.com/deployment-center/)（pgvector + Apache AGE 的替代方案）

前端：

- Vue 3
- Vite
- TypeScript
- pnpm
- Pinia
- Naive UI

## 如何部署

### 初始化

**a. 初始化数据库**

1. 创建数据库 `aideepin`
2. 执行 `db_migration/all_ddl.sql` 创建表结构
3. 执行 `db_migration/all_dml.sql` 插入基础数据
4. 执行 `db_migration/all_dml_cn.sql`（中文）或 `db_migration/all_dml_en.sql`（英文）插入展示数据
5. 配置并启用模型平台（至少启用一个，可参考上方表格选择），或使用[管理端](https://github.com/moyangzhan/langchain4j-aideepin-admin)在界面上配置

配置模型平台：

```sql
-- DeepSeek
UPDATE adi_model_platform SET api_key = 'my_deepseek_secret_key' WHERE name = 'deepseek';

-- OpenAI
UPDATE adi_model_platform SET api_key = 'my_openai_secret_key' WHERE name = 'openai';

-- 灵积
UPDATE adi_model_platform SET api_key = 'my_dashcope_api_key' WHERE name = 'dashscope';

-- 硅基流动
UPDATE adi_model_platform SET api_key = 'my_siliconflow_api_key' WHERE name = 'siliconflow_setting';

-- Ollama
UPDATE adi_model_platform SET base_url = 'my_ollama_base_url' WHERE name = 'ollama';
```

启用模型或新增模型：

```sql
-- 启用模型
UPDATE adi_ai_model SET is_enable = true WHERE name = 'deepseek-v4-flash';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'gpt-3.5-turbo';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'gpt-image-2';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'qwen-turbo';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'THUDM/GLM-Z1-9B-0414';
UPDATE adi_ai_model SET is_enable = true WHERE name = 'tinydolphin';

-- 新增模型
INSERT INTO adi_ai_model (name, type, platform, is_enable) VALUES ('vicuna', 'text', 'ollama', true);
```

配置搜索引擎（Google）：

```sql
UPDATE adi_sys_config SET value = '{"url":"https://www.googleapis.com/customsearch/v1","key":"my key from cloud.google.com","cx":"my cx from programmablesearchengine.google.com"}' WHERE name = 'google_setting';
```

**b. 修改配置文件**

复制示例配置并重命名：

```bash
cp adi-bootstrap/src/main/resources/application-dev.yml.example adi-bootstrap/src/main/resources/application-dev.yml
```

然后修改以下配置项：

- PostgreSQL：`application-[dev|prod].yml` → `spring.datasource`
- Redis：`application-[dev|prod].yml` → `spring.data.redis`
- 邮箱：`application.yml` → `spring.mail`
- 向量数据库（默认 pgvector）：`application-[dev|prod].yml` → `adi.vector-database=[pgvector|neo4j]`
- 图数据库（默认 Apache AGE）：`application-[dev|prod].yml` → `adi.graph-database=[apache-age|neo4j]`

### 编译及运行

```bash
cd langchain4j-aideepin
mvn clean package -Dmaven.test.skip=true
```

JAR 包启动：

```bash
cd adi-bootstrap/target
nohup java -jar -Xms768m -Xmx1024m -XX:+HeapDumpOnOutOfMemoryError \
  adi-bootstrap-0.0.1-SNAPSHOT.jar --spring.profiles.active=[dev|prod] \
  /dev/null 2>&1 &
```

Docker 启动：

```bash
cd adi-bootstrap
docker build . -t aideepin:0.0.1
docker run -d \
  --name=aideepin \
  -p 8888:9999 \
  -e APP_PROFILE=[dev|prod] \
  -v="/data/aideepin/logs:/data/logs" \
  aideepin:0.0.1
```

## 贡献指南

欢迎任何形式的贡献，包括但不限于：

- 提交 Bug 报告
- 提出功能建议
- 改进文档
- 提交代码（PR）

代码提交流程：

1. Fork 本仓库
2. 创建特性分支（`git checkout -b feature/xxx`）
3. 提交更改（`git commit -m 'feat: xxx'`）
4. 推送分支（`git push origin feature/xxx`）
5. 提交 Pull Request

## 截图

**AI 对话：**

![AI聊天](image/README/1691583184761.png)

**AI 画图：**

![AI画图](image/README/draw_001.png "AI绘图")

**知识库：**

![知识库](image/README/kbidx.png)

**向量化：**

![向量化](image/README/kb03.png)

**知识图谱：**

![知识图谱](image/README/kb_graph_01.png)

**工作流：**

![工作流](image/README/workflow.png)

## ⭐ 支持项目

如果 LangChain4j-AIDeepin 对您有帮助，欢迎：

- 给仓库点个 Star
- 推荐给身边的人
- 分享您的使用体验

## ❤️ 感谢

**Contributors**

<a href="https://github.com/moyangzhan/langchain4j-aideepin/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=moyangzhan/langchain4j-aideepin" />
</a>

<br/>

## 推荐项目

[Mango Finder](https://github.com/moyangzhan/mango-finder) — 一款用自然语言搜索本地文件的桌面应用，支持文档、图片、音频的语义搜索及跨设备搜索功能。帮助您根据记忆中的内容查找信息，而不需要记住文件名或文件夹结构。


# FILE: docs/cn/capability-tts.md

# 语音合成（TTS）能力接入

## 是否需要写代码？

**始终需要**。TTS 接口没有行业统一的 API 标准，各厂商使用不同的私有 API 格式，因此无论平台是否兼容 OpenAI 对话接口，都需要编写 Service 类。

> **注意**：TTS 服务由系统全局配置指定，用户不能自行切换。同一时间系统只有一个 TTS 服务处于激活状态。系统通过 `adi_sys_config` 表中 `name = 'tts_setting'` 的记录指定激活的 TTS 服务，其 `value` 为 JSON 格式：
>
> ```json
> {"synthesizer_side": "server", "model_name": "新平台的模型名称", "platform": "newai"}
> ```
>
> 可通过管理后台修改此配置，也可以直接更新数据库：
>
> ```sql
> UPDATE adi_sys_config SET value = '{"synthesizer_side":"server","model_name":"newai-tts-v1","platform":"newai"}' WHERE name = 'tts_setting';
> ```

## 前置步骤：注册平台名称常量

在 `AdiConstant.ModelPlatform` 中添加新平台名称常量：

**文件**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    // ... 现有常量 ...
    public static final String NEWAI = "newai";
}
```

## 步骤 1：Service 开发

**继承关系**: `CommonModelService` → `AbstractTtsModelService` → 你的 Service

基类 `AbstractTtsModelService` 很薄（约 30 行），仅定义了三个抽象方法的契约和代理设置，因此大部分逻辑需要子类自行实现。

**必须实现的抽象方法**：

| 方法 | 说明 |
|------|------|
| `start(String jobId, String voice, Consumer<ByteBuffer> onProcess, Consumer<String> onComplete, Consumer<String> onError)` | 初始化 TTS 任务，设置音色和回调 |
| `processByStream(String jobId, String partText)` | 流式接收文本片段并发送给 TTS 引擎 |
| `complete(String jobId)` | 完成所有文本输入，等待音频生成完成 |

### 复杂度说明

TTS 是所有能力中实现复杂度最高的。需要处理音频流、WAV 文件头生成、临时文件管理等底层细节：

- **流式 API 模式**（参考 `DashScopeTtsService`，约 215 行）：使用 SDK 实时接收音频帧，处理 PCM 数据并转 WAV 格式，涉及音频缓冲区操作和回调机制
- **REST API 模式**（参考 `SiliconflowTtsService`，约 154 行）：先积累文本，完成后一次性发送请求，再处理流式音频响应并写入文件

## 步骤 2：注册到 AiModelInitializer

**文件**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

在 `initTtsModelServiceList()` 方法中添加：

```java
private synchronized void initTtsModelServiceList(Map<String, ModelPlatform> nameToPlatform) {
    // ... 现有平台 ...

    // 新增
    initTtsModelService(AdiConstant.ModelPlatform.NEWAI,
        model -> new NewAiTtsService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI)));
}
```


# FILE: docs/cn/capability-asr.md

# 语音识别（ASR）能力接入

## 是否需要写代码？

**始终需要**。ASR 接口没有行业统一的 API 标准，各厂商使用不同的私有 API 格式，因此无论平台是否兼容 OpenAI 对话接口，都需要编写 Service 类。

> **注意**：ASR 服务由系统全局配置指定，用户不能自行切换。同一时间系统只有一个 ASR 服务处于激活状态。系统通过 `adi_sys_config` 表中 `name = 'asr_setting'` 的记录指定激活的 ASR 服务，其 `value` 为 JSON 格式：
>
> ```json
> {"model_name": "新平台的模型名称", "platform": "newai", "max_record_duration": 60, "max_file_size": 10485760}
> ```
>
> 可通过管理后台修改此配置，也可以直接更新数据库：
>
> ```sql
> UPDATE adi_sys_config SET value = '{"model_name":"newai-asr-v1","platform":"newai","max_record_duration":60,"max_file_size":10485760}' WHERE name = 'asr_setting';
> ```

## 前置步骤：注册平台名称常量

在 `AdiConstant.ModelPlatform` 中添加新平台名称常量：

**文件**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    // ... 现有常量 ...
    public static final String NEWAI = "newai";
}
```

## 步骤 1：Service 开发

**继承关系**: `CommonModelService` → `AbstractAsrModelService` → 你的 Service

基类 `AbstractAsrModelService` 很薄（约 20 行），仅定义了 `audioToText` 抽象方法和代理设置，因此大部分逻辑需要子类自行实现。

**必须实现的抽象方法**：

| 方法 | 返回值 | 说明 |
|------|--------|------|
| `audioToText(String urlOrPath)` | String | 接收音频文件 URL 或本地路径，返回识别的文本 |

### 复杂度说明

实现复杂度中等，需要处理文件上传（本地文件或远程 URL）、HTTP 请求、响应解析等：

- **异步 API 模式**（参考 `DashScopeAsrService`，约 76 行）：使用 SDK 提交异步任务，轮询等待结果，仅支持远程 URL
- **同步上传模式**（参考 `SiliconflowAsrService`，约 90 行）：使用 multipart/form-data 上传音频文件，同步返回结果，支持本地文件和远程 URL

## 步骤 2：注册到 AiModelInitializer

**文件**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

在 `initAsrModelServiceList()` 方法中添加：

```java
private synchronized void initAsrModelServiceList(Map<String, ModelPlatform> nameToPlatform) {
    // ... 现有平台 ...

    // 新增
    initAsrModelService(AdiConstant.ModelPlatform.NEWAI,
        model -> new NewAiAsrService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI)));
}
```


# FILE: docs/cn/architecture.md

# 系统架构

## 1. 系统概述

AIDeepIn 是一个 AI 辅助平台，通过对话、知识库、工作流、图像生成等能力，帮助企业和团队提升工作效率。

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              用户层                                          │
├──────────────────────────┬──────────────────────────────────────────────────┤
│   langchain4j-aideepin-web    │         langchain4j-aideepin-admin          │
│      (用户端 Vue3)             │             (管理端 Vue3)                    │
│   • AI对话/绘图               │         • 用户管理                           │
│   • 知识库问答                │         • 模型配置                           │
│   • 工作流使用                │         • 系统配置                           │
└──────────────────────────┴──────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         API网关层 (Spring Boot)                              │
├──────────────────────────┬──────────────────────────────────────────────────┤
│        adi-chat               │              adi-admin                       │
│     (用户端API接口)            │           (管理端API接口)                     │
└──────────────────────────┴──────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           核心业务层 (adi-common)                            │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────────────┤
│   对话服务    │   RAG服务     │  工作流引擎   │   绘图服务    │    MCP服务      │
├──────────────┴──────────────┴──────────────┴──────────────┴─────────────────┤
│                         大模型服务层 (languagemodel)                         │
├─────────────┬─────────────┬─────────────┬─────────────┬────────────────────┤
│   OpenAI    │  DeepSeek   │  阿里灵积    │  硅基流动    │     Ollama         │
└─────────────┴─────────────┴─────────────┴─────────────┴────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            数据存储层                                        │
├─────────────────────┬─────────────────────┬─────────────────────────────────┤
│   PostgreSQL        │       Redis         │       Neo4j (可选)              │
│   (pgvector+AGE)    │      (缓存)          │       (图数据库)                │
└─────────────────────┴─────────────────────┴─────────────────────────────────┘
```

## 2. 业务模块

### 2.1 智能对话

系统的核心模块，支持与 AI 进行多轮对话。

**对话流程**：

```
用户输入（文本/语音/图片）
    ↓
预处理（语音转文本、配额校验）
    ↓
上下文增强（短期/长期记忆 + 关联知识库 → RAG 检索 / 关联 MCP → 工具调用）
    ↓
LLM 生成回答（流式输出）
    ↓
后处理（TTS 语音合成、Token 计费、保存历史）
```

**核心能力**：
- 多模型切换：用户可在对话中选择不同的 AI 模型
- 多轮记忆：短期记忆（当前会话上下文）+ 长期记忆（跨会话的关键信息）
- 多模态输入：文本、图片、语音
- TTS 语音合成：将 AI 回答转为语音输出
- RAG 增强回答：关联知识库后，AI 基于检索到的内容生成回答
- MCP 工具调用：对话中可调用外部工具（如搜索引擎、数据库查询等）
- 多回答对比：同一问题可生成多个 AI 回答供用户选择

### 2.2 知识库（RAG）

将文档导入知识库后，AI 对话可基于知识库内容生成更准确的回答。

**RAG 架构**：

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  文档上传   │ -> │  文档解析   │ -> │  文本分块   │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  向量存储   │ <- │  Embedding  │ <- │  文本块     │
└─────────────┘    └─────────────┘    └─────────────┘
       │
       ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  用户提问   │ -> │  相似检索   │ -> │  上下文构建 │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │  LLM生成    │
                                      └─────────────┘
```

**文档处理流程**：

```
上传文档（PDF/Word/TXT 等）
    ↓
解析文档内容，拆分为片段
    ↓
索引（可选向量索引或图谱索引或两者）
    ↓
用户提问
    ↓
检索相关片段（向量相似度搜索 / 图谱关系查询）
    ↓
将检索结果注入 LLM Prompt，生成回答
```

**索引类型**：
- **向量索引**：将文本转为向量，通过语义相似度检索。使用 pgvector 存储
- **图谱索引**：从文档中提取实体和关系，构建知识图谱。使用 Apache AGE 存储
- **混合检索**：同时使用向量和图谱检索，综合排序

**知识库配置**：
- 公开/私有：公开知识库可被其他用户使用
- 检索参数：最大召回数量、最低相似度阈值
- 切片参数：文档分段大小、重叠长度

### 2.3 工作流

通过可视化编排多个处理节点，构建自动化的 AI 处理流程。

**节点类型**：

| 节点 | 作用 |
|------|------|
| 开始节点 | 工作流入口，接收用户输入 |
| 分类节点 | 对输入进行意图分类，决定后续分支 |
| 知识检索节点 | 搜索关联的知识库 |
| LLM 回答节点 | 调用 AI 模型生成回答 |
| HTTP 请求节点 | 调用外部 API |
| 模板节点 | 按模板生成结构化输出 |
| 条件判断节点 | 根据条件选择不同分支 |
| 关键词提取节点 | 从文本中提取关键词 |
| FAQ 提取节点 | 从文本中提取问答对 |
| 人工反馈节点 | 暂停等待人工确认 |
| 图像生成节点 | 生成图片 |
| 邮件发送节点 | 发送邮件 |

**工作流与对话的关系**：用户在对话中可调用工作流，工作流内部可以检索知识库和调用 MCP 工具。

### 2.4 MCP（模型上下文协议）

MCP 是一种标准化的外部工具接入协议，允许 AI 在对话中调用外部服务。

**支持的传输方式**：
- SSE（Server-Sent Events）
- Stdio（标准输入输出）
- Docker 容器
- 远程服务
- WASM（WebAssembly）

**使用方式**：
- 管理员配置 MCP 服务及其参数
- 用户在对话中启用 MCP 服务
- AI 根据需要自动调用 MCP 工具

### 2.5 图像生成

通过文本描述生成图片：

```
用户输入描述 → 选择图像模型 → 生成图片 → 保存到图库
```

- 支持多个图像生成平台（OpenAI、DashScope、SiliconFlow 等）
- 生成的图片可设为公开（带水印）或私有
- 支持点赞、评论

## 3. 模块间关系

```
                              ┌──────────┐
                              │  用户端   │
                              └────┬─────┘
                                   │ HTTP / SSE
                              ┌────▼─────┐
                              │  服务端   │
                              └────┬─────┘
                                   │
     ┌─────────┬─────────┬─────────┼─────────┬─────────┐
     │         │         │         │         │         │
┌────▼───┐┌───▼────┐┌───▼────┐┌──▼────┐┌───▼─────┐
│智能对话 ││ 文生图  ││ 工作流 ││ 知识库  ││   MCP   │
└────┬───┘└───┬────┘└──┬────┘└───┬────┘└───┬─────┘
     │        │         │        │         │         │
     └────────┴────┬────┴────────┴────┬────┘         │
                   │                  │              │
              ┌────▼────┐        ┌────▼────┐   ┌────▼────┐
              │LLM 服务 │        │R

# FILE: docs/cn/capability-chat.md

# 对话 / 图像识别能力接入

对话（`text`）和图像识别（`vision`）使用同一套 LLM 基础设施，共享同一套接入逻辑。

## 是否需要写代码？

| 平台兼容 OpenAI API | 平台不兼容 OpenAI API |
|:------------------:|:-------------------:|
| 不需要 | **需要** |

- **兼容 OpenAI API 的平台**：只需在 `adi_model_platform` 中将 `is_openai_api_compatible` 设为 `true`，系统启动时通过 `OpenAiCompatibleLLMService` 自动加载，**零代码**。
- **不兼容的平台**：需要编写 Service 类，见下文。

## 前置步骤：注册平台名称常量

在 `AdiConstant.ModelPlatform` 中添加新平台名称常量：

**文件**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    public static final String DEEPSEEK = "deepseek";
    public static final String OPENAI = "openai";
    public static final String DASHSCOPE = "dashscope";
    public static final String OLLAMA = "ollama";
    public static final String SILICONFLOW = "siliconflow";
    // 新增
    public static final String NEWAI = "newai";
}
```

## 步骤 1：Service 开发

**继承关系**: `CommonModelService` → `AbstractLLMService` → 你的 Service

**必须实现的抽象方法**：

| 方法 | 返回值 | 说明 |
|------|--------|------|
| `isEnabled()` | boolean | 检查服务是否可用（通常检查 API Key 是否配置） |
| `doBuildChatModel(ChatModelBuilderProperties)` | ChatModel | 构建同步对话模型 |
| `buildStreamingChatModel(ChatModelBuilderProperties)` | StreamingChatModel | 构建流式对话模型 |
| `parseError(Object)` | LLMException | 解析 API 错误信息 |
| `getTokenEstimator()` | TokenCountEstimator | Token 估算器（可返回 null） |

**可选覆盖的方法**：

| 方法 | 说明 |
|------|------|
| `checkBeforeChat(SseAskParams)` | 聊天前校验（如 DashScope 检查 base URL） |
| `doCreateChatRequestParameters(ChatRequestParameters, Map)` | 自定义请求参数（如开启深度思考、联网搜索） |

### 复杂度说明

基类 `AbstractLLMService`（约 600 行）已实现完整的对话流程（流式输出、工具调用、记忆管理、Token 统计、TTS 集成等），子类的实际工作量取决于目标平台：

- **langchain4j 已内置的平台**（如 Ollama）：直接使用对应的 `OllamaChatModel`，实现很简单（参考 `OllamaLLMService`，约 53 行）
- **有特殊参数的平台**：除了构建 Model，还需要覆盖 `doCreateChatRequestParameters()` 处理平台特有的参数（参考 `DashScopeLLMService` 约 131 行，处理深度思考、联网搜索等）

### 示例（参考 DashScopeLLMService）

非兼容平台需要使用平台方提供的 SDK 构建 Model：

```java
public class NewAiLLMService extends AbstractLLMService {
    @Override
    protected ChatModel doBuildChatModel(ChatModelBuilderProperties properties) {
        return NewAiSdkChatModel.builder()
                .baseUrl(platform.getBaseUrl())
                .apiKey(platform.getApiKey())
                .modelName(aiModel.getName())
                .temperature(properties.getTemperature().floatValue())
                .build();
    }
    // ... 其他方法类似
}
```

## 步骤 2：注册到 AiModelInitializer

**文件**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

在 `initLLMServiceList()` 方法中添加：

```java
private synchronized void initLLMServiceList(Map<String, ModelPlatform> nameToPlatform, String modelType) {
    // ... 现有平台 ...

    // 新增
    initLLMService(AdiConstant.ModelPlatform.NEWAI, modelType,
        model -> new NewAiLLMService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI))
            .setProxyAddress(proxyAddress));
}
```


# FILE: docs/cn/index.md

# AIDeepIn 技术开发文档

## 系统架构

- [系统架构](architecture.md)

## 模型平台

> 模型平台在其他项目中有时也称为"模型提供商"（Model Provider）。

- [新模型平台接入指南](model-platform-integration.md)


# FILE: docs/cn/capability-image.md

# 文生图能力接入

## 是否需要写代码？

**始终需要**。文生图接口没有行业统一的 API 标准，各厂商使用不同的私有 API 格式，因此无论平台是否兼容 OpenAI 对话接口，都需要编写 Service 类。

## 前置步骤：注册平台名称常量

在 `AdiConstant.ModelPlatform` 中添加新平台名称常量：

**文件**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    // ... 现有常量 ...
    public static final String NEWAI = "newai";
}
```

## 步骤 1：Service 开发

**继承关系**: `CommonModelService` → `AbstractImageModelService` → 你的 Service

基类 `AbstractImageModelService` 已实现完整的图片生成流程（调用模型、处理 URL/Base64 响应、保存文件），子类只需构建 `ImageModel` 实例并处理错误。

**必须实现的抽象方法**：

| 方法 | 返回值 | 说明 |
|------|--------|------|
| `isEnabled()` | boolean | 检查服务是否可用 |
| `buildImageModel(User, Draw)` | ImageModel | 构建图片生成模型 |
| `parseError(Object)` | LLMException | 解析 API 错误 |

### 复杂度说明

实际开发复杂度取决于目标平台 API 的差异程度：

- **langchain4j 已内置的平台**（如 OpenAI）：直接使用 `OpenAiImageModel`，实现非常简单（参考 `OpenAiImageService`，约 22 行）
- **需要自定义适配的平台**：需要编写自定义的 `ImageModel` 实现来对接平台 API，再在 Service 中使用（参考 `DashScopeWanxService`，约 74 行，需处理背景生成等特殊模式）

## 步骤 2：注册到 AiModelInitializer

**文件**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

在 `initImageModelServiceList()` 方法中添加：

```java
private synchronized void initImageModelServiceList(Map<String, ModelPlatform> nameToPlatform) {
    // ... 现有平台 ...

    // 新增
    initImageModelService(AdiConstant.ModelPlatform.NEWAI,
        model -> new NewAiImageService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI)));
}
```

## 步骤 3：前端适配（用户端）

**文件**: `langchain4j-aideepin-web/src/views/draw/`

前端按平台划分了独立的生成组件，需要为新平台创建对应的组件。

### 前端组件结构

```
src/views/draw/components/
  ├── gpt-image/
  │   └── GptImageEditor.vue    — OpenAI 图像编辑器
  ├── wanx/
  │   ├── index.vue              — DashScope 万相入口
  │   ├── GenerateImage.vue      — 图片生成
  │   └── GenerateBackground.vue — 背景生成
  ├── siliconflow/
  │   ├── index.vue              — SiliconFlow 入口
  │   └── GenerateImage.vue      — 图片生成
  ├── CommonDraws.vue            — 通用绘图操作
  ├── Header.vue                 — 页面头（含模型选择器）
  └── SearchInput.vue            — 提示词输入框
```

### 需要开发的内容

1. **创建平台组件目录**：在 `src/views/draw/components/` 下新建 `newai/` 目录，创建 `index.vue` 和 `GenerateImage.vue`

2. **实现生成组件**：参考现有组件（如 `siliconflow/GenerateImage.vue`），实现以下逻辑：
   - 调用 `api.imageGenerate()` 接口，传入 `modelName`、`prompt`、`size`、`number` 等参数
   - 调用 `checkProcess(uuid)` 轮询生成结果
   - 将结果推入 `drawStore`

3. **注册平台组件**：在 `src/views/draw/index.vue` 中引入新组件，根据选中的图像模型平台动态渲染对应组件

### 各平台参数差异

| 参数 | OpenAI | DashScope 万相 | SiliconFlow |
|------|--------|---------------|-------------|
| 图片尺寸 | auto/1024x1024/1024x1536/1536x1024 | 固定选项 | 从模型 `properties.image_sizes` 动态读取 |
| 图片质量 | auto/low/medium/high | — | — |
| 生成数量 | 1 | 1 | 1-4 |
| 随机种子 | — | -1（随机） | -1（随机） |
| 负向提示词 | — | — | — |

### 图像模型数据要求

前端通过 `appStore.selectedImageModel` 获取当前选中的图像模型信息，该数据来源于 `adi_ai_model` 表。如果新平台需要前端动态读取配置（如 SiliconFlow 从 `properties.image_sizes` 读取尺寸选项），需要在 `adi_ai_model.properties` 中配置对应字段。


# FILE: docs/cn/model-platform-integration.md

# 新模型平台接入指南

## 1. 概述

AIDeepIn 使用 **策略模式 + 工厂模式 + 上下文模式** 管理多个模型平台。系统当前支持以下能力类型：

| 类型 | 常量值 | 说明 | 接入文档 |
|------|--------|------|---------|
| 对话 | `text` | 文本对话（Chat Completions） | [对话接入](capability-chat.md) |
| 图像识别 | `vision` | 多模态对话（支持图片输入） | [对话接入](capability-chat.md) |
| 文生图 | `image` | 文本生成图片 | [文生图接入](capability-image.md) |
| 语音合成 | `tts` | 文本转语音 | [TTS 接入](capability-tts.md) |
| 语音识别 | `asr` | 语音转文本 | [ASR 接入](capability-asr.md) |

> **注意**：对话（text）和图像识别（vision）使用同一套 LLM 基础设施（`AbstractLLMService`），共享同一套接入逻辑。

接入新平台分两部分：
1. **第一部分：数据库配置（必须）** — 见下文第 2 节
2. **第二部分：代码开发（按需）** — 根据需要启用的能力，阅读对应的能力接入文档

> **快速接入**：如果新平台兼容 OpenAI API 且只需要使用对话（text）或图像识别（vision）功能，只需完成数据库配置即可，无需编写任何代码。系统会通过 `OpenAiCompatibleLLMService` 自动加载该平台的对话模型。

---

## 2. 数据库配置（必须）

### 2.1 模型平台表（adi_model_platform）

该表存储平台级别的配置信息（API 地址、密钥等）。

```sql
INSERT INTO adi_model_platform (name, title, base_url, api_key, remark, is_proxy_enable, is_openai_api_compatible)
VALUES ('newai', 'NewAI', 'https://api.newai.com/v1', 'your-api-key', 'NewAI model platform', false, true);
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | varchar(45) | 平台唯一标识，如 `openai`、`dashscope`、`ollama`。**必须与代码中 `AdiConstant.ModelPlatform` 的常量值一致** |
| `title` | varchar(45) | 显示名称，如 `OpenAI`、`DeepSeek` |
| `base_url` | varchar(250) | API 请求基础地址，如 `https://api.openai.com/v1` |
| `api_key` | varchar(100) | API 密钥 |
| `secret_key` | varchar(100) | 已废弃，仅做兼容保留 |
| `remark` | varchar(1000) | 备注说明 |
| `is_proxy_enable` | boolean | 是否通过代理访问（代理配置在 `application.yml` 的 `adi.proxy` 中） |
| `is_openai_api_compatible` | boolean | **关键字段**：是否兼容 OpenAI API 格式。设为 `true` 后，对话(text/vision)类型模型将自动使用 `OpenAiCompatibleLLMService` 加载，无需编写代码 |

### 2.2 AI 模型表（adi_ai_model）

该表存储平台下的具体模型信息。**每个能力类型对应一条记录**。

```sql
-- 对话模型
INSERT INTO adi_ai_model (name, title, type, platform, context_window, max_input_tokens, max_output_tokens,
    input_types, response_format_types, is_free, is_enable, properties)
VALUES ('newai-chat-v1', 'NewAI Chat V1', 'text', 'newai', 128000, 120000, 8000,
    'text', 'text,json_object', false, true, '{}');

-- 图像识别模型
INSERT INTO adi_ai_model (name, title, type, platform, context_window, max_input_tokens, max_output_tokens,
    input_types, response_format_types, is_free, is_enable, properties)
VALUES ('newai-vision-v1', 'NewAI Vision V1', 'vision', 'newai', 128000, 120000, 8000,
    'text,image', 'text', false, true, '{}');

-- 文生图模型
INSERT INTO adi_ai_model (name, title, type, platform, context_window, max_input_tokens, max_output_tokens,
    input_types, response_format_types, is_free, is_enable, properties)
VALUES ('newai-image-v1', 'NewAI Image V1', 'image', 'newai', 0, 0, 0,
    'text', 'text', false, true, '{}');

-- TTS 模型
INSERT INTO adi_ai_model (name, title, type, platform, context_window, max_input_tokens, max_output_tokens,
    input_types, response_format_types, is_free, is_enable, properties)
VALUES ('newai-tts-v1', 'NewAI TTS V1', 'tts', 'newai', 0, 0, 0,
    'text', 'text', false, true, '{"voices":["alloy","echo","fable"]}');

-- ASR 模型
INSERT INTO adi_ai_model (name, title, type, platform, context_window, max_input_tokens, max_output_tokens,
    input_types, response_format_types, is_free, is_enable, properties)
VALUES ('newai-asr-v1', 'NewAI ASR V1', 'asr', 'newai', 0, 0, 0,
    'audio', 'text', false, true, '{}');
```

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | varchar(45) | 模型名称，**必须与模型平台方指定的模型名称完全一致**（传给 API 的参数） |
| `title` | varchar(45) | 显示名称 |
| `type` | varchar(45) | 模型类型：`text`、`image`、`vision`、`embedding`、`rerank`、`tts`、`asr` |
| `platform` | varchar(45) | 对应 `adi_model_platform.name` |
| `context_window` | int | 上下文窗口大小（token 数） |
| `max_input_tokens` | int | 最大输入 token 数 |
| `max_output_tokens` | int | 最大输出 token 数 |
| `input_types` | varchar(100) | 支持的输入类型：`text`、`image`、`audio`、`video`，多值用逗号分隔 |
| `response_format_types` | varchar(200) | 支持的输出格式：`text`、`json_object`，多值用逗号分隔 |
| `properties` | jsonb | 模型特有属性，如 TTS 模型的音色列表 `{"voices":["v1","v2"]}` |
| `setting` | varchar(500) | 模型配置，JSON 格式 |
| `is_free` | boolean | 是否免费 |
| `is_enable` | boolean | 是否启用 |
| `is_reasoner` | boolean | 是否为推理模型（如 deepseek-r1） |
| `is_thinking_closable` | boolean | 思考过程是否可关闭（如 Qwen3 可关闭，deepseek-r1 不可关闭） |
| `is_support_web_search` | boolean | 是否支持联网搜索 |

### 2.3 通过 Admin API 操作

除了直接执行 SQL，也可以通过管理后台 API 操作：

- `POST /admin/model-platform/add` — 添加平台
- `POST /admin/model-platform/edit` — 编辑平台
- `POST /admin/model/addOne` — 添加模型
- `POST /admin/model/edit` — 编辑模型

---

## 3. 调试与验证

### 查看启动日志

服务启动时会打印模型加载日志：

```
add openai api compatible llm model,model: AiModel(name=newai-chat-v1, ...)
add llm model,model: AiModel(name=newai-chat-v1, ...)
add image model,model: AiModel(name=newai-image-v1, ...)
add tts model,model: AiModel(name=newai-tts-v1, ...)
add asr model,model: AiModel(name=newai-asr-v1, ...)
```

如果看到 `{platform} service is disabled`，说明该平台下没有已启用的模型或 API Key 未配置。

### 常见问题

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| 平台未被加载 | `adi_model_platform` 中 `is_deleted = true` | 确认记录未被软删除 |
| 模型未被加载 | `adi_ai_model` 中 `is_enable = false` | 将 `is_enable` 设为 `true` |
| 对话模型不生效但 `is_openai_api_compatible = true` | `api_key` 为空 | 配置有效的 API Key |
| 非 OpenAI 兼容平台模型不生效 | 未在 `AiModelInitializer` 中注册 | 按对应能力接入文档添加注册代码 |
| 代理不生效 | 平台 `is_proxy_enable = false` 或全局代理未开启 | 检查 `adi_model_platform.is_proxy_enable` 和 `application.yml` 中的 `adi.proxy.enable` |

---

## 4. 源码文件索引

| 文件路径 | 作用 |
|---------|------|
| `adi-common/.../entity/ModelPlatform.java` | 模型平台实体 |
| `adi-common/.../entity/AiModel.java` | AI 模型实体 |
| `adi-common/.../cosntant/AdiConstant.java` | 平台名称常量（`ModelPlatform` 内部类）+ 模型类型常量（`ModelType` 内部类） |
| `adi-common/.../languagemodel/CommonModelService.java` | 所有 Service 的基类（持有 AiModel 和 ModelPlatform 引用） |
| `adi-common/.../languagemodel/AbstractLLMService.java` | 对话服务抽象基类 |
| `adi-common/.../languagemodel/AbstractImageModelService.java` | 文生图抽象基类 |
| `adi-common/.../languagemodel/AbstractTtsModelService.java` | TTS 抽象基类 |
| 

# FILE: docs/en/capability-tts.md

# Text-to-Speech (TTS) Capability Integration

## Is Code Required?

**Always required**. The TTS API has no industry-standard format. Each vendor uses different proprietary API formats, so regardless of whether the platform is OpenAI-compatible for chat, you need to write a Service class.

> **Note**: The TTS service is specified by system-level configuration; users cannot switch between providers. Only one TTS service is active at a time. The system determines the active TTS service via the `adi_sys_config` table record where `name = 'tts_setting'`. The `value` is in JSON format:
>
> ```json
> {"synthesizer_side": "server", "model_name": "new-model-name", "platform": "newai"}
> ```
>
> You can change this via the admin backend, or update the database directly:
>
> ```sql
> UPDATE adi_sys_config SET value = '{"synthesizer_side":"server","model_name":"newai-tts-v1","platform":"newai"}' WHERE name = 'tts_setting';
> ```

## Prerequisite: Register Platform Name Constant

Add a new platform name constant in `AdiConstant.ModelPlatform`:

**File**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    // ... existing constants ...
    public static final String NEWAI = "newai";
}
```

## Step 1: Service Development

**Inheritance**: `CommonModelService` → `AbstractTtsModelService` → Your Service

The base class `AbstractTtsModelService` is thin (~30 lines), defining only the contract for three abstract methods and proxy settings, so most of the logic must be implemented by subclasses.

**Required abstract methods**:

| Method | Description |
|--------|-------------|
| `start(String jobId, String voice, Consumer<ByteBuffer> onProcess, Consumer<String> onComplete, Consumer<String> onError)` | Initialize TTS task, set voice and callbacks |
| `processByStream(String jobId, String partText)` | Receive streaming text fragments and send to TTS engine |
| `complete(String jobId)` | Finish all text input and wait for audio generation to complete |

### Complexity Notes

TTS has the highest implementation complexity among all capabilities. It requires handling audio streams, WAV header generation, temporary file management, and other low-level details:

- **Streaming API mode** (see `DashScopeTtsService`, ~215 lines): Uses SDK to receive audio frames in real-time, processes PCM data and converts to WAV format, involves audio buffer operations and callback mechanisms
- **REST API mode** (see `SiliconflowTtsService`, ~154 lines): Accumulates text first, sends a single request on completion, then processes streaming audio response and writes to file

## Step 2: Register in AiModelInitializer

**File**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

Add in the `initTtsModelServiceList()` method:

```java
private synchronized void initTtsModelServiceList(Map<String, ModelPlatform> nameToPlatform) {
    // ... existing platforms ...

    // Add new
    initTtsModelService(AdiConstant.ModelPlatform.NEWAI,
        model -> new NewAiTtsService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI)));
}
```


# FILE: docs/en/capability-asr.md

# Speech-to-Text (ASR) Capability Integration

## Is Code Required?

**Always required**. The ASR API has no industry-standard format. Each vendor uses different proprietary API formats, so regardless of whether the platform is OpenAI-compatible for chat, you need to write a Service class.

> **Note**: The ASR service is specified by system-level configuration; users cannot switch between providers. Only one ASR service is active at a time. The system determines the active ASR service via the `adi_sys_config` table record where `name = 'asr_setting'`. The `value` is in JSON format:
>
> ```json
> {"model_name": "new-model-name", "platform": "newai", "max_record_duration": 60, "max_file_size": 10485760}
> ```
>
> You can change this via the admin backend, or update the database directly:
>
> ```sql
> UPDATE adi_sys_config SET value = '{"model_name":"newai-asr-v1","platform":"newai","max_record_duration":60,"max_file_size":10485760}' WHERE name = 'asr_setting';
> ```

## Prerequisite: Register Platform Name Constant

Add a new platform name constant in `AdiConstant.ModelPlatform`:

**File**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    // ... existing constants ...
    public static final String NEWAI = "newai";
}
```

## Step 1: Service Development

**Inheritance**: `CommonModelService` → `AbstractAsrModelService` → Your Service

The base class `AbstractAsrModelService` is thin (~20 lines), defining only the `audioToText` abstract method and proxy settings, so most of the logic must be implemented by subclasses.

**Required abstract methods**:

| Method | Return Type | Description |
|--------|-------------|-------------|
| `audioToText(String urlOrPath)` | String | Receive an audio file URL or local path, return recognized text |

### Complexity Notes

Implementation complexity is moderate. It requires handling file uploads (local or remote URLs), HTTP requests, response parsing, etc.:

- **Async API mode** (see `DashScopeAsrService`, ~76 lines): Uses SDK to submit an async task, polls for results. Supports remote URLs only
- **Sync upload mode** (see `SiliconflowAsrService`, ~90 lines): Uses multipart/form-data to upload audio files, returns results synchronously. Supports both local files and remote URLs

## Step 2: Register in AiModelInitializer

**File**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

Add in the `initAsrModelServiceList()` method:

```java
private synchronized void initAsrModelServiceList(Map<String, ModelPlatform> nameToPlatform) {
    // ... existing platforms ...

    // Add new
    initAsrModelService(AdiConstant.ModelPlatform.NEWAI,
        model -> new NewAiAsrService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI)));
}
```


# FILE: docs/en/architecture.md

# System Architecture

## 1. System Overview

AIDeepIn is an AI-powered productivity platform that helps enterprises and teams improve work efficiency through capabilities such as chat, knowledge bases, workflows, and image generation.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            User Layer                                       │
├──────────────────────────┬──────────────────────────────────────────────────┤
│   langchain4j-aideepin-web    │         langchain4j-aideepin-admin          │
│      (User Frontend Vue3)     │         (Admin Frontend Vue3)               │
│   • AI Chat / Drawing         │         • User Management                   │
│   • Knowledge Base Q&A        │         • Model Configuration               │
│   • Workflow Usage            │         • System Settings                   │
└──────────────────────────┴──────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      API Gateway Layer (Spring Boot)                        │
├──────────────────────────┬──────────────────────────────────────────────────┤
│        adi-chat               │              adi-admin                       │
│     (User API endpoints)      │         (Admin API endpoints)                │
└──────────────────────────┴──────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Core Business Layer (adi-common)                       │
├──────────────┬──────────────┬──────────────┬──────────────┬─────────────────┤
│  Chat Service │  RAG Service │  Workflow    │ Image Gen    │  MCP Service    │
│               │              │  Engine      │ Service      │                 │
├──────────────┴──────────────┴──────────────┴──────────────┴─────────────────┤
│                    Model Service Layer (languagemodel)                      │
├─────────────┬─────────────┬─────────────┬─────────────┬────────────────────┤
│   OpenAI    │  DeepSeek   │  DashScope  │ SiliconFlow │     Ollama         │
└─────────────┴─────────────┴─────────────┴─────────────┴────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         Data Storage Layer                                   │
├─────────────────────┬─────────────────────┬─────────────────────────────────┤
│   PostgreSQL        │       Redis         │       Neo4j (optional)          │
│   (pgvector+AGE)    │      (cache)         │       (graph database)         │
└─────────────────────┴─────────────────────┴─────────────────────────────────┘
```

## 2. Business Modules

### 2.1 Smart Chat

The core module of the system, supporting multi-turn conversations with AI.

**Chat Flow**:

```
User input (text/voice/image)
    ↓
Pre-processing (voice-to-text, quota validation)
    ↓
Context enhancement (short-term/long-term memory + linked knowledge base → RAG retrieval / linked MCP → tool calls)
    ↓
LLM generates answer (streaming output)
    ↓
Post-processing (TTS synthesis, token billing, save history)
```

**Core Capabilities**:
- Multi-model switching: Users can select different AI models in a conversation
- Multi-turn memory: Short-term memory (current session context) + Long-term memory (key information across sessions)
- Multimodal input: Text, images, voice
- TTS synthesis: Convert AI responses to speech output
- RAG-enhanced responses: When linked to a knowledge base, AI generates answers based on retrieved content
- MCP tool calling: External tools can be invoked during conversations (e.g. search engines, database queries)
- Multi-answer comparison: Multiple AI responses can be generated for the same question

### 2.2 Knowledge Base (RAG)

After importing documents into a knowledge base, AI chat can generate more accurate answers based on the knowledge base content.

**RAG Architecture**:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Document  │ -> │   Document  │ -> │  Text       │
│   Upload    │    │   Parsing   │    │  Chunking   │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Vector    │ <- │  Embedding  │ <- │  Text       │
│   Storage   │    │             │    │  Chunks     │
└─────────────┘    └─────────────┘    └─────────────┘
       │
       ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   User      │ -> │  Similarity │ -> │   Context   │
│   Question  │    │  Search     │    │  Building   │
└─────────────┘    └─────────────┘    └─────────────┘
                                             │
                                             ▼
                                      ┌─────────────┐
                                      │  LLM        │
                                      │  Generation │
                                      └─────────────┘
```

**Document Processing Flow**:

```
Upload documents (PDF/Word/TXT etc.)
    ↓
Parse document content, split into segments
    ↓
Index (optional: vector index, graph index, or both)
    ↓
User asks a question
    ↓
Retrieve relevant segments (vector similarity search / graph relationship query)
    ↓
Inject retrieved results into LLM prompt, generate answer
```

**Index Types**:
- **Vector Index**: Converts text to vectors and retrieves via semantic similarity. Stored in pgvector
- **Graph Index**: Extracts entities and relationships from documents to build a knowledge graph. Stored in Apache AGE
- **Hybrid Retrieval**: Uses both vector and graph retrieval with combin

# FILE: docs/en/capability-chat.md

# Chat / Vision Capability Integration

Chat (`text`) and Vision (`vision`) share the same LLM infrastructure and use the same integration logic.

## Is Code Required?

| Platform Compatible with OpenAI API | Platform Not Compatible |
|:----------------------------------:|:-----------------------:|
| No | **Yes** |

- **OpenAI API compatible platforms**: Simply set `is_openai_api_compatible` to `true` in `adi_model_platform`. The system will automatically load it via `OpenAiCompatibleLLMService` on startup — **zero code**.
- **Non-compatible platforms**: You need to write a Service class. See below.

## Prerequisite: Register Platform Name Constant

Add a new platform name constant in `AdiConstant.ModelPlatform`:

**File**: `adi-common/src/main/java/com/moyz/adi/common/cosntant/AdiConstant.java`

```java
public static class ModelPlatform {
    public static final String DEEPSEEK = "deepseek";
    public static final String OPENAI = "openai";
    public static final String DASHSCOPE = "dashscope";
    public static final String OLLAMA = "ollama";
    public static final String SILICONFLOW = "siliconflow";
    // Add new
    public static final String NEWAI = "newai";
}
```

## Step 1: Service Development

**Inheritance**: `CommonModelService` → `AbstractLLMService` → Your Service

**Required abstract methods**:

| Method | Return Type | Description |
|--------|-------------|-------------|
| `isEnabled()` | boolean | Check if the service is available (typically checks if API Key is configured) |
| `doBuildChatModel(ChatModelBuilderProperties)` | ChatModel | Build a synchronous chat model |
| `buildStreamingChatModel(ChatModelBuilderProperties)` | StreamingChatModel | Build a streaming chat model |
| `parseError(Object)` | LLMException | Parse API error information |
| `getTokenEstimator()` | TokenCountEstimator | Token estimator (can return null) |

**Optional methods to override**:

| Method | Description |
|--------|-------------|
| `checkBeforeChat(SseAskParams)` | Pre-chat validation (e.g. DashScope checks base URL) |
| `doCreateChatRequestParameters(ChatRequestParameters, Map)` | Customize request parameters (e.g. enable deep thinking, web search) |

### Complexity Notes

The base class `AbstractLLMService` (~600 lines) implements the complete chat flow (streaming output, tool calling, memory management, token statistics, TTS integration, etc.). The actual effort depends on the target platform:

- **Platforms already supported by langchain4j** (e.g. Ollama): Use the corresponding `OllamaChatModel` directly — very simple (see `OllamaLLMService`, ~53 lines)
- **Platforms with special parameters**: In addition to building the Model, you also need to override `doCreateChatRequestParameters()` to handle platform-specific parameters (see `DashScopeLLMService`, ~131 lines, handling deep thinking, web search, etc.)

### Example (reference DashScopeLLMService)

Non-compatible platforms need to use the platform provider's SDK to build the Model:

```java
public class NewAiLLMService extends AbstractLLMService {
    @Override
    protected ChatModel doBuildChatModel(ChatModelBuilderProperties properties) {
        return NewAiSdkChatModel.builder()
                .baseUrl(platform.getBaseUrl())
                .apiKey(platform.getApiKey())
                .modelName(aiModel.getName())
                .temperature(properties.getTemperature().floatValue())
                .build();
    }
    // ... other methods similar
}
```

## Step 2: Register in AiModelInitializer

**File**: `adi-common/src/main/java/com/moyz/adi/common/service/AiModelInitializer.java`

Add in the `initLLMServiceList()` method:

```java
private synchronized void initLLMServiceList(Map<String, ModelPlatform> nameToPlatform, String modelType) {
    // ... existing platforms ...

    // Add new
    initLLMService(AdiConstant.ModelPlatform.NEWAI, modelType,
        model -> new NewAiLLMService(model, nameToPlatform.get(AdiConstant.ModelPlatform.NEWAI))
            .setProxyAddress(proxyAddress));
}
```


# FILE: docs/en/index.md

# AIDeepIn Technical Documentation

## System Architecture

- [System Architecture](architecture.md)

## Model Platform

> "Model Platform" is sometimes referred to as "Model Provider" in other projects.

- [New Model Platform Integration Guide](model-platform-integration.md)

