# Missing Repo Summary Source: ageerle/ruoyi-ai

- URL: https://github.com/ageerle/ruoyi-ai
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/ageerle__ruoyi-ai
- Clone Status: cloned
- Language: Java
- Stars: 5247
- Topics: agent, ai, knowledge, mcp, rag
- Description: 面向企业级市场的一站式AI应用开发框架，支持多厂商大模型统一接入与管理，具备安全可控的企业知识库与高精度检索优化能力，提供可视化流程编排、自主决策智能体与多智能体协同调度，兼容主流 Agent Skill 协议，帮助企业与开发者零门槛快速构建安全、高效、可落地的AI智能体应用与行业解决方案。

## Extracted README / Docs / Examples



# FILE: README.md

# RuoYi AI

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<p align="center">
  <a href="https://trendshift.io/repositories/13209">
    <img src="https://trendshift.io/api/badge/repositories/13209" alt="GitHub Trending">
  </a>
</p>

<img src="docs/image/logo.png" alt="RuoYi AI Logo" width="120" height="120">

### 企业级AI助手平台

*开箱即用的全栈AI平台，支持多智能体协同、Supervisor模式编排、多种决策模式、RAG技术和流程编排能力*

**[English](README_EN.md)** | **[📖 使用文档](https://doc.pandarobot.chat)** |
**[🚀 在线体验](https://web.pandarobot.chat)** | **[🐛 问题反馈](https://github.com/ageerle/ruoyi-ai/issues)** | **[💡 功能建议](https://github.com/ageerle/ruoyi-ai/issues)**

</div>


## ✨ 核心亮点

|     模块     | 现有能力 
|:----------:|---
|  **模型管理**  | 多模型接入(OpenAI/DeepSeek/通义/智谱/MiniMax)、多模态理解、Coze/DIFY/FastGPT平台集成
|  **知识管理**  | 本地RAG + 向量库(Milvus/Weaviate/Qdrant)  + 文档解析
|  **工具管理**  | Mcp协议集成、Skills能力 + 可扩展工具生态                             
|  **流程编排**  | 可视化工作流设计器、节点拖拽编排、SSE流式执行,目前已经支持模型调用,邮件发送,人工审核等节点  
|  **多智能体**  | 基于Langchain4j的Agent框架、Supervisor模式编排,支持多种决策模型          

## 🚀 快速体验

### 在线演示

|   平台   | 地址 | 账号 |
|:------:|---|---|
|  用户端   | [web.pandarobot.chat](https://web.pandarobot.chat) | admin / admin123 |
| 管理后台 | [admin.pandarobot.chat](https://admin.pandarobot.chat) | admin / admin123 |

### 项目源码

| 项目模块     | GitHub 仓库                                             | Gitee 仓库                                             | GitCode 仓库                                             |
|----------|-------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------|
| 🔧 后端服务  | [ruoyi-ai](https://github.com/ageerle/ruoyi-ai)       | [ruoyi-ai](https://gitee.com/ageerle/ruoyi-ai)       | [ruoyi-ai](https://gitcode.com/ageerle/ruoyi-ai)       |
| 🎨 用户前端  | [ruoyi-web](https://github.com/ageerle/ruoyi-web)     | [ruoyi-web](https://gitee.com/ageerle/ruoyi-web)     | [ruoyi-web](https://gitcode.com/ageerle/ruoyi-web)     |
| 🛠️ 管理后台 | [ruoyi-admin](https://github.com/ageerle/ruoyi-admin) | [ruoyi-admin](https://gitee.com/ageerle/ruoyi-admin) | [ruoyi-admin](https://gitcode.com/ageerle/ruoyi-admin) |

### 合作项目
| 项目名称           | GitHub 仓库                                             | Gitee 仓库                                             
|----------------|-------------------------------------------------------|------------------------------------------------------|
| element-plus-x | [element-plus-x](https://github.com/element-plus-x/Element-Plus-X)       | [element-plus-x](https://gitee.com/he-jiayue/element-plus-x)       | 

## 🛠️ 技术架构

### 核心框架
- **后端架构**：Spring Boot 3.5.8 + Langchain4j
- **数据存储**：MySQL 8.0 + Redis + 向量数据库（Milvus/Weaviate/Qdrant）
- **前端技术**：Vue 3 + Vben Admin + element-plus-x
- **安全认证**：Sa-Token + JWT 双重保障


- **文档处理**：PDF、Word、Excel 解析，图像智能分析
- **实时通信**：WebSocket 实时通信，SSE 流式响应
- **系统监控**：完善的日志体系、性能监控、服务健康检查

## 使用web coding急速部署
####  在线体验： https://monkeycode-ai.com/?ic=019d9e9f-edc3-7a4b-8987-11b028751a1e

<table>
<tr>
<td align="center" style="padding: 20px;">
<img src="docs/image/01.png" alt="web code" width="660" height="400"><br>
</td>
</tr>
<tr>
<td align="center" style="padding: 20px;">
<img src="docs/image/02.png" alt="web code" width="660" height="400"><br>
</td>
</tr>
<tr>
<td align="center" style="padding: 20px;">
<img src="docs/image/03.png" alt="web code" width="660" height="400"><br>
</td>
</tr>
</table>

#### 等待10分钟左右即可完成

## 🐳 Docker 部署

本项目提供两种 Docker 部署方式：

### 方式一：一键启动所有服务（推荐）

使用 `docker-compose-all.yaml` 可以一键启动所有服务（包括后端、管理端、用户端及依赖服务）：

```bash
# 克隆仓库
git clone https://github.com/ageerle/ruoyi-ai.git
cd ruoyi-ai

# 启动所有服务（从镜像仓库拉取预构建镜像）
docker-compose -f docker-compose-all.yaml up -d

# 查看服务状态
docker-compose -f docker-compose-all.yaml ps

# 访问服务
# 管理端: http://localhost:25666 (admin / admin123)
# 用户端: http://localhost:25137
# 后端API: http://localhost:26039
```

### 方式二：分步部署（源码编译）

如果您需要从源码构建后端服务，请按照以下步骤操作：

#### 第一步：部署后端服务

```bash
# 进入后端项目目录
cd ruoyi-ai

# 启动后端服务（源码编译构建）
docker-compose up -d --build

# 等待后端服务启动完成
docker-compose logs -f backend
```

#### 第二步：部署管理端

```bash
# 进入管理端项目目录
cd ruoyi-admin

# 构建并启动管理端
docker-compose up -d --build

# 访问管理端
# 地址: http://localhost:5666
```

#### 第三步：部署用户端（可选）

```bash
# 进入用户端项目目录
cd ruoyi-web

# 构建并启动用户端
docker-compose up -d --build

# 访问用户端
# 地址: http://localhost:5137
```

### 服务端口说明

| 服务 | 一键启动端口 | 分步部署端口 | 说明 |
|------|-------------|-------------|------|
| 管理端 | 25666 | 5666 | 管理后台访问地址 |
| 用户端 | 25137 | 5137 | 用户前端访问地址 |
| 后端服务 | 26039 | 6039 | 后端 API 服务 |
| MySQL | 23306 | 23306 | 数据库服务 |
| Redis | 26379 | 6379 | 缓存服务 |
| Weaviate | 28080 | 28080 | 向量数据库 |
| MinIO API | 29000 | 9000 | 对象存储 API |
| MinIO Console | 29090 | 9090 | 对象存储控制台 |

### 镜像仓库

所有镜像托管在阿里云容器镜像服务：

```
crpi-31mraxd99y2gqdgr.cn-beijing.personal.cr.aliyuncs.com/ruoyi_ai
```

可用镜像：
- `mysql:v3` - MySQL 数据库（包含初始化 SQL）
- `redis:6.2` - Redis 缓存
- `weaviate:1.30.0` - 向量数据库
- `minio:latest` - 对象存储
- `ruoyi-ai-backend:latest` - 后端服务
- `ruoyi-ai-admin:latest` - 管理端前端
- `ruoyi-ai-web:latest` - 用户端前端

### 常用命令

```bash
# 停止所有服务
docker-compose -f docker-compose-all.yaml down

# 查看服务日志
docker-compose -f docker-compose-all.yaml logs -f [服务名]

# 重启某个服务
docker-compose -f docker-compose-all.yaml restart [服务名]
```

## 📚 使用文档

想要深入了解安装部署、功能配置和二次开发？

**👉 [完整使用文档](https://doc.pandarobot.chat)**

## 🤝 参与贡献

我们热烈欢迎社区贡献！无论您是资深开发者还是初学者，都可以为项目贡献力量 💪

### 贡献方式

1. **Fork** 项目到您的账户
2. **创建分支** (`git checkout -b feature/新功能名称`)
3. **提交代码** (`git commit -m '添加某某功能'`)
4. **推送分支** (`git push origin feature/新功能名称`)
5. **发起 Pull Request**

> 💡 **小贴士**：建议将 PR 提交到 GitHub，我们会自动同步到其他代码托管平台

## 📄 开源协议

本项目采用 **MIT 开源协议**，详情请查看 [LICENSE](LICENSE) 文件。

## 🙏 特别鸣谢

感谢以下优秀的开源项目为本项目提供支持：
- [Spring AI Alibaba Copilot](https://github.com/spring-ai-alibaba/copilot) - 基于spring-ai-alibaba
  的智能编码助手
- [Langchain4j](https://github.com/langchain4j/langchain4j) - 强大的 Java LLM 开发框架
- [RuoYi-Vue-Plus](https://gitee.com/dromara/RuoYi-Vue-Plus) - 成熟的企业级快速开发框架
- [Vben Admin](https://github.com/vbenjs/vue-vben-admin) - 现代化的 Vue 后台管理模板

## 🌐 生态伙伴

- [PPIO 派欧云](https://ppinfra.com/user/register?invited_by=P8QTUY&utm_source=github_ruoyi-ai) - 提供高性价比的 GPU
  算力和模型 API 服务
- [优云智算](https://www.compshare.cn/?ytag=GPU_YY-gh_ruoyi) - 万卡RTX40系GPU+海内外主流模型API服务，秒级响应，按量计费，新客免费用。

## 💬 社区交流

<div align="center">

<table>
<tr>
<td align="center">
<img src="docs/image/wx.png" alt="微信二维码" width="200" height="200"><br>
<strong>扫码添加作者微信</strong><br>
<em>邀请进群学习</em>
</td>
<td align="center">
<img src="docs/image/qq.png" alt="QQ群二维码" width="200" height="200"><br>
<strong>QQ技术交流群</strong><br>
<em>技术讨论</em>
</td>

</tr>
</table>

</div>

---
<div align="center">

**[⭐ 点个Star支持一下](https://github.com/ageerle/ruoyi-ai)** • **[ Fork 开始贡献](https://github.com/ageerle/ruoyi-ai/fork)** • **[📚 English](README_EN.md)** • **[📖 查看完整文档](https://doc.pandarobot.chat)**

*用 ❤️ 打造，由 RuoYi AI 开源社区维护*

</div>

<!-- Badge Links -->

[contributors-shield]: https://img.shields.io/github/contributors/ageerle/ruoyi-ai.svg?style=flat-square

[contributors-url]: https://github.com/ageerle/ruoyi-ai/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/ageerle/ruoyi-ai.svg?style=flat-square

[forks-url]: https://github.com/ageerle/ruoyi-ai/network/members

[stars-shield]: https://img.shields.io/github/stars/ageerle/ruoyi-ai.svg?style=flat-square

[stars-url]: https://github.com/ageerle/ruoyi-ai/stargazers

[issues-shield]: https://img.shields.io/github/issues/ageerle/ruoyi-ai.svg?style=flat-square

[issues-url]: https://github.com/ageerle/ruoyi-ai/issues

[license-shield]: https://img.shields.io/github/license/ageerle/ruoyi-ai.svg?style=flat-square

[license-url]: https://github.com/ageerle/ruoyi-ai/blob/main/LICENSE


# FILE: README_EN.md


# RuoYi AI

<div align="center">

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<p align="center">
  <a href="https://trendshift.io/repositories/13209">
    <img src="https://trendshift.io/api/badge/repositories/13209" alt="GitHub Trending">
  </a>
</p>

<img src="docs/image/logo.png" alt="RuoYi AI Logo" width="120" height="120">

### Enterprise-Grade AI Assistant Platform

*An out-of-the-box full-stack AI platform supporting multi-agent collaboration, Supervisor mode orchestration, and multiple decision models, with advanced RAG technology and visual workflow orchestration capabilities*

**[中文](README.md)** | **[📖 Documentation](https://doc.pandarobot.chat)** |
**[🚀 Live Demo](https://web.pandarobot.chat)** | **[🐛 Report Issues](https://github.com/ageerle/ruoyi-ai/issues)** | **[💡 Feature Requests](https://github.com/ageerle/ruoyi-ai/issues)**

</div>




## ✨ Core Features

| Module | Current Capabilities |
|:---:|---|
| **Model Management** | Multi-model integration (OpenAI/DeepSeek/Tongyi/Zhipu/MiniMax), multi-modal understanding, Coze/DIFY/FastGPT platform integration |
| **Knowledge Base** | Local RAG + Vector DB (Milvus/Weaviate/Qdrant) + Document parsing |
| **Tool Management** | MCP protocol integration, Skills capability + Extensible tool ecosystem |
| **Workflow Orchestration** | Visual workflow designer, drag-and-drop node orchestration, SSE streaming execution, currently supports model calls, email sending, manual review nodes |
| **Multi-Agent** | Agent framework based on Langchain4j, Supervisor mode orchestration, supports multiple decision models |

## 🚀 Quick Start

### Live Demo

|   Platform   | URL | Account |
|:------:|---|---|
|  User Frontend   | [web.pandarobot.chat](https://web.pandarobot.chat) | admin / admin123 |
| Admin Panel | [admin.pandarobot.chat](https://admin.pandarobot.chat) | admin / admin123 |

### Project Repositories

| Module     | GitHub Repository                                             | Gitee Repository                                             | GitCode Repository                                             |
|----------|-------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------|
| 🔧 Backend  | [ruoyi-ai](https://github.com/ageerle/ruoyi-ai)       | [ruoyi-ai](https://gitee.com/ageerle/ruoyi-ai)       | [ruoyi-ai](https://gitcode.com/ageerle/ruoyi-ai)       |
| 🎨 User Frontend  | [ruoyi-web](https://github.com/ageerle/ruoyi-web)     | [ruoyi-web](https://gitee.com/ageerle/ruoyi-web)     | [ruoyi-web](https://gitcode.com/ageerle/ruoyi-web)     |
| 🛠️ Admin Panel | [ruoyi-admin](https://github.com/ageerle/ruoyi-admin) | [ruoyi-admin](https://gitee.com/ageerle/ruoyi-admin) | [ruoyi-admin](https://gitcode.com/ageerle/ruoyi-admin) |

### Partner Projects
| Project Name           | GitHub Repository                                             | Gitee Repository |
|----------------|-------------------------------------------------------|------------------------------------------------------|
| element-plus-x | [element-plus-x](https://github.com/element-plus-x/Element-Plus-X)       | [element-plus-x](https://gitee.com/he-jiayue/element-plus-x)       |

## 🛠️ Technical Architecture

### Core Framework
- **Backend**: Spring Boot 3.5.8 + Langchain4j
- **Data Storage**: MySQL 8.0 + Redis + Vector Databases (Milvus/Weaviate/Qdrant)
- **Frontend**: Vue 3 + Vben Admin + element-plus-x
- **Security**: Sa-Token + JWT dual-layer security


- **Document Processing**: PDF, Word, Excel parsing, intelligent image analysis
- **Real-time Communication**: WebSocket real-time communication, SSE streaming response
- **System Monitoring**: Comprehensive logging system, performance monitoring, service health checks

## 🐳 Docker Deployment

This project provides two Docker deployment methods:

### Method 1: One-click Start All Services (Recommended)

Use `docker-compose-all.yaml` to start all services at once (including backend, admin panel, user frontend, and dependencies):

```bash
# Clone the repository
git clone https://github.com/ageerle/ruoyi-ai.git
cd ruoyi-ai

# Start all services (pull pre-built images from registry)
docker-compose -f docker-compose-all.yaml up -d

# Check service status
docker-compose -f docker-compose-all.yaml ps

# Access services
# Admin Panel: http://localhost:25666 (admin / admin123)
# User Frontend: http://localhost:25137
# Backend API: http://localhost:26039
```

### Method 2: Step-by-step Deployment (Source Build)

If you need to build backend services from source, follow these steps:

#### Step 1: Deploy Backend Service

```bash
# Enter backend project directory
cd ruoyi-ai

# Start backend service (build from source)
docker-compose up -d --build

# Wait for backend service to start
docker-compose logs -f backend
```

#### Step 2: Deploy Admin Panel

```bash
# Enter admin panel project directory
cd ruoyi-admin

# Build and start admin panel
docker-compose up -d --build

# Access admin panel
# URL: http://localhost:5666
```

#### Step 3: Deploy User Frontend (Optional)

```bash
# Enter user frontend project directory
cd ruoyi-web

# Build and start user frontend
docker-compose up -d --build

# Access user frontend
# URL: http://localhost:5137
```

### Service Ports

| Service | One-click Port | Step-by-step Port | Description |
|------|-------------|-------------|------|
| Admin Panel | 25666 | 5666 | Admin backend access |
| User Frontend | 25137 | 5137 | User frontend access |
| Backend Service | 26039 | 6039 | Backend API service |
| MySQL | 23306 | 23306 | Database service |
| Redis | 26379 | 6379 | Cache service |
| Weaviate | 28080 | 28080 | Vector database |
| MinIO API | 29000 | 9000 | Object storage API |
| MinIO Console | 29090 | 9090 | Object storage console |

### Image Registry

All images are hosted on Alibaba Cloud Container Registry:

```
crpi-31mraxd99y2gqdgr.cn-beijing.personal.cr.aliyuncs.com/ruoyi_ai
```

Available images:
- `mysql:v3` - MySQL database (includes initialization SQL)
- `redis:6.2` - Redis cache
- `weaviate:1.30.0` - Vector database
- `minio:latest` - Object storage
- `ruoyi-ai-backend:latest` - Backend service
- `ruoyi-ai-admin:latest` - Admin frontend
- `ruoyi-ai-web:latest` - User frontend

### Common Commands

```bash
# Stop all services
docker-compose -f docker-compose-all.yaml down

# View service logs
docker-compose -f docker-compose-all.yaml logs -f [service-name]

# Restart a service
docker-compose -f docker-compose-all.yaml restart [service-name]
```

## 📚 Documentation

Want to learn more about installation, deployment, configuration, and secondary development?

**👉 [Complete Documentation](https://doc.pandarobot.chat)**

## 🤝 Contributing

We warmly welcome community contributions! Whether you are a seasoned developer or just getting started, you can contribute to the project 💪

### How to Contribute

1. **Fork** the project to your account
2. **Create a branch** (`git checkout -b feature/new-feature-name`)
3. **Commit your changes** (`git commit -m 'Add new feature'`)
4. **Push to the branch** (`git push origin feature/new-feature-name`)
5. **Create a Pull Request**

> 💡 **Tip**: We recommend submitting PRs to GitHub, we will automatically sync to other code hosting platforms

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Thanks to the following excellent open-source projects for their support:
- [Spring AI Alibaba Copilot](https://github.com/spring-ai-alibaba/copilot) - Intelligent coding assistant based on spring-ai-alibaba
- [Langchain4j](https://github.com/langchain4j/langchain4j) - Powerful Java LLM development framework
- [RuoYi-Vue-Plus](https://gitee.com/dromara/RuoYi-Vue-Plus) - Mature enterprise-level rapid development framework
- [Vben Admin](https://github.com/vbenjs/vue-vben-admin) - Modern Vue admin template

## 🌐 Ecosystem Partners

- [PPIO Cloud](https://ppinfra.com/user/register?invited_by=P8QTUY&utm_source=github_ruoyi-ai) - Provides cost-effective GPU computing and model API services
- [Youyun Intelligent Computing](https://www.compshare.cn/?ytag=GPU_YY-gh_ruoyi) - Thousands of RTX40 series GPUs + mainstream models API services, second-level response, pay-per-use, free for new customers.


## 💬 Community Chat

<div align="center">

**[📱 Join Telegram Group](
https://t.me/+LqooQAc5HxRmYmE1)**

</div>

---

<div align="center">

**[⭐ Star to Support](https://github.com/ageerle/ruoyi-ai)** • **[Fork to Contribute](https://github.com/ageerle/ruoyi-ai/fork)** • **[📚 中文](README.md)** • **[📖 Complete Documentation](https://doc.pandarobot.chat)**

*Built with ❤️, maintained by the RuoYi AI open-source community*

</div>

<!-- Badge Links -->

[contributors-shield]: https://img.shields.io/github/contributors/ageerle/ruoyi-ai.svg?style=flat-square

[contributors-url]: https://github.com/ageerle/ruoyi-ai/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/ageerle/ruoyi-ai.svg?style=flat-square

[forks-url]: https://github.com/ageerle/ruoyi-ai/network/members

[stars-shield]: https://img.shields.io/github/stars/ageerle/ruoyi-ai.svg?style=flat-square

[stars-url]: https://github.com/ageerle/ruoyi-ai/stargazers

[issues-shield]: https://img.shields.io/github/issues/ageerle/ruoyi-ai.svg?style=flat-square

[issues-url]: https://github.com/ageerle/ruoyi-ai/issues

[license-shield]: https://img.shields.io/github/license/ageerle/ruoyi-ai.svg?style=flat-square

[license-url]: https://github.com/ageerle/ruoyi-ai/blob/main/LICENSE

