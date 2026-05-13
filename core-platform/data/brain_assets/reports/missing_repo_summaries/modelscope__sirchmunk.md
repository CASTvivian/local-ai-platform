# Missing Repo Summary Source: modelscope/sirchmunk

- URL: https://github.com/modelscope/sirchmunk
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/modelscope__sirchmunk
- Clone Status: cloned
- Language: Python
- Stars: 1100
- Topics: 
- Description: 🐿️ Sirchmunk:  Raw data to self-evolving intelligence, real-time.

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">

<img src="web/public/logo-v2.png" alt="Sirchmunk Logo" width="250" style="border-radius: 15px;">

# Sirchmunk: Raw data to self-evolving intelligence, real-time. 
<a href="https://trendshift.io/repositories/22808" target="_blank"><img src="https://trendshift.io/api/badge/repositories/22808" alt="modelscope%2Fsirchmunk | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-3.4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![DuckDB](https://img.shields.io/badge/DuckDB-OLAP-FFF000?style=flat-square&logo=duckdb&logoColor=black)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)
[![ripgrep-all](https://img.shields.io/badge/ripgrep--all-Search-E67E22?style=flat-square&logo=rust&logoColor=white)](https://github.com/phiresky/ripgrep-all)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=flat-square&logo=openai&logoColor=white)](https://github.com/openai/openai-python)
[![Kreuzberg](https://img.shields.io/badge/Kreuzberg-Text_Extraction-4CAF50?style=flat-square)](https://github.com/kreuzberg-dev/kreuzberg)
[![MCP](https://img.shields.io/badge/MCP-Python_SDK-8B5CF6?style=flat-square&logo=python&logoColor=white)](https://github.com/modelcontextprotocol/python-sdk)

📖 **[Documentation](https://modelscope.github.io/sirchmunk-web/)**

[**Quick Start**](#-quick-start) · [**Key Features**](#-key-features) · [**MCP Server**](#-mcp-server) · [**Web UI**](#️-web-ui) · [**Docker**](#-docker-deployment) · [**How it Works**](#️-how-it-works) · [**FAQ**](#-faq)

</div>

<div align="center">

🔍 **Agentic Search** &nbsp;•&nbsp; 🧠 **Knowledge Clustering** &nbsp;•&nbsp; 📊 **Monte Carlo Evidence Sampling**<br>
⚡ **Indexless Retrieval** &nbsp;•&nbsp; 🔄 **Self-Evolving Knowledge Base** &nbsp;•&nbsp; 💬 **Real-time Chat**

</div>

<br>

[English](README.md) | [中文](README_zh.md)


---

## 🌰 Why “Sirchmunk”？

Intelligence pipelines built upon vector-based retrieval can be _rigid and brittle_. They rely on static vector embeddings that are **expensive to compute, blind to real-time changes, and detached from the raw context**. We introduce **Sirchmunk** to usher in a more agile paradigm, where data is no longer treated as a snapshot, and insights can evolve together with the data.

---

## ✨ Key Features

### 1. EmbeddingDB-Free: Data in its Purest Form

**Sirchmunk** works directly with **raw data** -- bypassing the heavy overhead of squeezing your rich files into fixed-dimensional vectors.

* **Instant Search:** Eliminating complex pre-processing pipelines in hours long indexing; just drop your files and search immediately.
* **Full Fidelity:** Zero information loss —- stay true to your data without vector approximation.

### 2. Self-Evolving: A Living Index

Data is a stream, not a snapshot.  **Sirchmunk** is **dynamic by design**, while vector DB can become obsolete the moment your data changes.

* **Context-Aware:** Evolves in real-time with your data context.
* **LLM-Powered Autonomy:** Designed for Agents that perceive data as it lives, utilizing **token-efficient** reasoning that triggers LLM inference only when necessary to maximize intelligence while minimizing cost.

### 3. Intelligence at Scale: Real-Time & Massive

**Sirchmunk** bridges massive local repositories and the web with **high-scale throughput** and **real-time awareness**. <br/>
It serves as a unified intelligent hub for AI agents, delivering deep insights across vast datasets at the speed of thought.



> For more technical details, refer to the [Sirchmunk blog](https://modelscope.github.io/sirchmunk-web/blog)


---

### Traditional RAG vs. Sirchmunk

<div style="display: flex; justify-content: center; width: 100%;">
  <table style="width: 100%; max-width: 900px; border-collapse: separate; border-spacing: 0; overflow: hidden; border-radius: 12px; font-family: sans-serif; border: 1px solid rgba(128, 128, 128, 0.2); margin: 0 auto;">
    <colgroup>
      <col style="width: 25%;">
      <col style="width: 30%;">
      <col style="width: 45%;">
    </colgroup>
    <thead>
      <tr style="background-color: rgba(128, 128, 128, 0.05);">
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(128, 128, 128, 0.2); font-size: 1.3em;">Dimension</th>
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(128, 128, 128, 0.2); font-size: 1.3em; opacity: 0.7;">Traditional RAG</th>
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(58, 134, 255, 0.5); color: #3a86ff; font-weight: 800; font-size: 1.3em;">✨Sirchmunk</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">💰 Setup Cost</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">High Overhead <br/> (VectorDB, GraphDB, Complex Document Parser...)</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ Zero Infrastructure <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">Direct-to-data retrieval without vector silos</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">🕒 Data Freshness</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">Stale (Batch Re-indexing)</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ Instant &amp; Dynamic <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">Self-evolving index that reflects live changes</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">📈 Scalability</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">Linear Cost Growth</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ Extremely low RAM/CPU consumption <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">Native Elastic Support, efficiently handles large-scale datasets</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">🎯 Accuracy</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">Approximate Vector Matches</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ Deterministic &amp; Contextual <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">Hybrid logic ensuring semantic precision</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600;">⚙️ Workflow</td>
        <td style="padding: 16px; opacity: 0.6;">Complex ETL Pipelines</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef;">
          ✅ Drop-and-Search <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">Zero-config integration for rapid deployment</small>
        </td>
      </tr>
    </tbody>
  </table>
</div>

---


## Demonstration


<div align="center">
  <video controls autoplay muted loop playsinline width="100%" src="https://github.com/user-attachments/assets/704dbc0a-3df6-436a-b7f7-fb1edefbfb8c"></video>
  <p style="font-size: 1.1em; font-weight: 600; margin-top: 8px; color: #00bcd4;">
    Access files directly to start chatting
  </p>
</div>

---


|  WeChat Group  |  DingTalk Group  |
|:--------------:|:----------------:|
|  <img src="assets/pic/wechat.jpg" width="200" height="200">  |  <img src="assets/pic/dingtalk.png" width="200" height="200">  |

---


## 🎉 News

* 🚀 **Apr 13, 2026**: Sirchmunk v0.0.7
  - **C/S deployment hardening**: Strict `allowed_paths` enforcement with symlink detection for remote mode; per-IP rate limiting and JSON Lines audit logging; local mode remains unrestricted for backward compatibility.
  - **Remote file upload**: Three-mode upload UI (Select Files / Select Folder / drag-and-drop); server-side pre-upload duplicate detection with skip/overwrite options; manifest-based storage accounting.
  - **Server file browser**: `FileBrowser` defaults to server `data/` directory; manual path input validated against `allowed_paths`; permission-aware error messages for remote access control.
  - **Init alignment**: `sirchmunk init` generates `.env` fully aligned with `config/env.example`, covering all C/S deployment variables.
* 🚀 **Mar 31, 2026**: Sirchmunk v0.0.6post3
  - **Docker multi-arch**: Native `linux/amd64` and `linux/arm64` images via Docker Buildx; CI builds both architectures automatically.
  - **FAST mode**: File-level deduplication and dynamic score pruning in `_fast_find_best_file`; scope-aware knowledge cluster reuse.
* 🚀 **Mar 20, 2026**: Sirchmunk v0.0.6post1
  - **🐿️x🦞OpenClaw skill**: Sirchmunk is now available as an [OpenClaw](https://openclaw.org/) skill on [ClawHub](https://clawhub.ai/wangxingjun778/sirchmunk) — any OpenClaw-compatible agent can s

# FILE: README_zh.md

<div align="center">

<img src="web/public/logo-v2.png" alt="Sirchmunk 标志" width="250" style="border-radius: 15px;">

# Sirchmunk：无需向量数据库和预索引的自进化搜索引擎

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100%2B-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-000000?style=flat-square&logo=next.js&logoColor=white)](https://nextjs.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind-3.4-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)](https://tailwindcss.com/)
[![DuckDB](https://img.shields.io/badge/DuckDB-OLAP-FFF000?style=flat-square&logo=duckdb&logoColor=black)](https://duckdb.org/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue?style=flat-square)](LICENSE)
[![ripgrep-all](https://img.shields.io/badge/ripgrep--all-Search-E67E22?style=flat-square&logo=rust&logoColor=white)](https://github.com/phiresky/ripgrep-all)
[![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=flat-square&logo=openai&logoColor=white)](https://github.com/openai/openai-python)
[![Kreuzberg](https://img.shields.io/badge/Kreuzberg-Text_Extraction-4CAF50?style=flat-square)](https://github.com/kreuzberg-dev/kreuzberg)
[![MCP](https://img.shields.io/badge/MCP-Python_SDK-8B5CF6?style=flat-square&logo=python&logoColor=white)](https://github.com/modelcontextprotocol/python-sdk)

📖 **[官方文档](https://modelscope.github.io/sirchmunk-web/zh/)** 

[**快速开始**](#-快速开始) · [**核心特性**](#-核心特性) · [**MCP 服务器**](#-mcp-服务器) · [**Web UI**](#️-web-ui) · [**Docker 部署**](#-docker-部署) · [**工作原理**](#️-工作原理) · [**FAQ**](#-faq)


</div>

<div align="center">

🔍 **智能体搜索** &nbsp;•&nbsp; 🧠 **知识聚类** &nbsp;•&nbsp; 📊 **蒙特卡洛证据采样**<br>
⚡ **无索引检索** &nbsp;•&nbsp; 🔄 **自进化知识库** &nbsp;•&nbsp; 💬 **实时对话**

</div>

<br>

[English](README.md) | [中文](README_zh.md)

---

## 🌰 为什么选择 “Sirchmunk”？

基于向量检索的智能流水线往往 _僵硬且脆弱_。它们依赖静态向量嵌入，**计算成本高、对实时变化不敏感，并且脱离原始上下文**。我们引入 **Sirchmunk**，开启更敏捷的范式：数据不再是静态的快照和分块，而是直接从原始数据中洞见所查。

---

## ✨ 核心特性

### 1. 无需向量数据库和预索引：直接面向原始数据形态

**Sirchmunk** 直接处理 **原始数据** —— 无需将大量而繁杂的文件压缩为固定维度向量，或是构建为图数据库。

* **即开即用搜索：** 不再需要复杂、耗时的预处理与索引；直接添加文件即可检索。
* **全量保真：** 零信息损失，避免向量近似带来的偏差。

### 2. 自进化：实时动态索引

数据是流动的，而非静态快照。**Sirchmunk** 天然具备动态特性。相比之下，向量数据库可能在数据变化的瞬间就过时。

* **上下文感知：** 随数据上下文实时演化。
* **LLM 自主驱动：** 面向智能体设计，通过精心设计的上下文检索技术，仅在必要时触发LLM推理，提高Token使用效率，兼顾智能与成本。

### 3. 规模化：实时与海量数据支持
**Sirchmunk** 具备 **高吞吐** 与 **实时感知** 的特性，能够高效处理本地大型数据集和文件系统。


> 更多技术细节，参考 [Sirchmunk blog](https://modelscope.github.io/sirchmunk-web/zh/blog/).


---

### 传统 RAG vs. Sirchmunk

<div style="display: flex; justify-content: center; width: 100%;">
  <table style="width: 100%; max-width: 900px; border-collapse: separate; border-spacing: 0; overflow: hidden; border-radius: 12px; font-family: sans-serif; border: 1px solid rgba(128, 128, 128, 0.2); margin: 0 auto;">
    <colgroup>
      <col style="width: 25%;">
      <col style="width: 30%;">
      <col style="width: 45%;">
    </colgroup>
    <thead>
      <tr style="background-color: rgba(128, 128, 128, 0.05);">
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(128, 128, 128, 0.2); font-size: 1.3em;">维度</th>
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(128, 128, 128, 0.2); font-size: 1.3em; opacity: 0.7;">传统 RAG</th>
        <th style="text-align: left; padding: 16px; border-bottom: 2px solid rgba(58, 134, 255, 0.5); color: #3a86ff; font-weight: 800; font-size: 1.3em;">✨Sirchmunk</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">💰 搭建成本</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">高开销 <br/>（VectorDB、GraphDB、复杂文档解析器...）</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ 零基础设施 <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">直接面向数据检索，无向量孤岛</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">🕒 数据新鲜度</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">滞后（批量重建索引）</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ 即时 &amp; 动态 <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">自进化索引反映实时变化</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">📈 可扩展性</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">线性成本增长</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ 极低 RAM/CPU 占用 <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">原生弹性支持，高效处理大规模数据集</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">🎯 准确性</td>
        <td style="padding: 16px; opacity: 0.6; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">近似向量匹配</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef; border-bottom: 1px solid rgba(128, 128, 128, 0.1);">
          ✅ 确定性 &amp; 上下文相关 <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">混合逻辑确保语义精度</small>
        </td>
      </tr>
      <tr>
        <td style="padding: 16px; font-weight: 600;">⚙️ 工作流</td>
        <td style="padding: 16px; opacity: 0.6;">复杂 ETL 流水线</td>
        <td style="padding: 16px; background-color: rgba(58, 134, 255, 0.08); color: #4895ef;">
          ✅ 直接检索 <br/>
          <small style="opacity: 0.8; font-size: 0.85em;">零配置集成，快速部署</small>
        </td>
      </tr>
    </tbody>
  </table>
</div>

---


## 演示


<div align="center">
  <video controls autoplay muted loop playsinline width="100%" src="https://github.com/user-attachments/assets/704dbc0a-3df6-436a-b7f7-fb1edefbfb8c"></video>
  <p style="font-size: 1.1em; font-weight: 600; margin-top: 8px; color: #00bcd4;">
    直接访问文件或文件夹即可开始对话
  </p>
</div>

---


|  微信群  |  钉钉群  |
|:--------:|:--------:|
|  <img src="assets/pic/wechat.jpg" width="200" height="200">  |  <img src="assets/pic/dingtalk.png" width="200" height="200">  |

---


## 🎉 News

* 🚀 **2026年4月13日**: Sirchmunk v0.0.7
  - **C/S 部署加固**：远程模式下严格的 `allowed_paths` 路径约束与符号链接检测；按 IP 速率限制与 JSON Lines 审计日志；本地模式保持向后兼容。
  - **远程文件上传**：三种上传模式（选择文件 / 选择文件夹 / 拖拽上传）；服务端上传前重复检测，支持跳过/覆盖；基于 manifest 的存储统计。
  - **服务端文件浏览**：`FileBrowser` 默认打开服务端 `data/` 目录；手动路径输入校验 `allowed_paths`；远程访问的权限感知错误提示。
  - **Init 对齐**：`sirchmunk init` 生成与 `config/env.example` 完全对齐的 `.env`，覆盖所有 C/S 部署变量。
* 🚀 **2026年3月31日**: Sirchmunk v0.0.6post3
  - **Docker 多架构支持**：通过 Docker Buildx 原生构建 `linux/amd64` 和 `linux/arm64` 镜像；CI 自动构建双架构。
  - **FAST 模式优化**：`_fast_find_best_file` 新增文件级去重与动态分数剪枝；知识集群复用增加搜索范围感知。
* 🚀 **2026年3月20日**: Sirchmunk v0.0.6post1
  - **🐿️x🦞OpenClaw 技能**：Sirchmunk 已发布为 [OpenClaw](https://openclaw.org/) 技能，上架 [ClawHub](https://clawhub.ai/wangxingjun778/sirchmunk) — 任何兼容 OpenClaw 的 AI Agent均可通过自然语言搜索本地文件。详见 [openclaw-recipe](recipes/openclaw_skills/README.md)。
  - **Search API**：新增 SSE 流式端点（`POST /api/v1/search/stream`），支持实时日志输出；通过 `SIRCHMUNK_MAX_CONCURRENT_SEARCHES` 控制并发；`paths` 参数同时支持字符串和数组，且为可选（回退到 `SIRCHMUNK_SEARCH_PATHS`）。
  - **依赖修复**：`sirchmunk serve` 不再要求安装 `sirchmunk[web]` — `uvicorn` 已纳入核心依赖；`psutil` 改为可选。

* 🚀 **2026年3月12日**: Sirchmunk v0.0.6
  - **多轮对话**：上下文管理与 LLM 查询重写；配置项 `CHAT_HISTORY_MAX_TURNS` / `CHAT_HISTORY_MAX_TOKENS`；搜索默认 token 预算 128K
  - **文档摘要与跨语言检索**：摘要流水线（分块/合并/重排）、跨语言关键词提取、聊天历史相关性过滤
  - **Docker**：支持 `SIRCHMUNK_SEARCH_PATHS` 环境变量；更新 entrypoint；文档处理依赖
  - **OpenAI 客户端**：`_ProviderProfile` 多提供商管理；按 `base_url` 自动检测；统一流式处理；支持 `thinking_content`

<details>
<summary><b>历史版本（v0.0.2 – v0.0.5）</b></summary>

* 🚀 **2026.3.5**: **Sirchmunk v0.0.5 发布**
  - **破坏性变更**：统一搜索 API：重构 search() 接口的返回类型，引入 SearchContext 对象并简化返回参数控制，API 调用更简洁。
  - **高可用 RAG 对话**：引入重试机制与细粒度异常处理，大幅提升了 RAG 聊天在复杂网络环境下的稳定性。
  - **稳定 MCP 集成**：修复 mcp run 初始化问题，确保 MCP 协议服务器在各环境下均能顺畅启动。
  - **PyPI 安装修复**：解决了标准 pip 安装后的 Web 源码定位问题，确保 Web UI 即装即用。

* 🚀 **2026.2.27**: **Sirchmunk v0.0.4 发布**
  - **Docker 部署支持**：提供预构建 Docker 镜像，支持容器化一键部署。
  - **FAST 检索模式**：新增默认贪心搜索模式，采用两级关键词级联与上下文窗口采样策略，仅需 2 次 LLM 调用（2-5s vs 10-30s），大幅提升检索速度。
  - **简化部署链路**：精简命令行与 Web 端的部署和配置流程，降低上手门槛。
  - **Windows 兼容性修复**：修复 Windows 环境下的兼容性问题。

* 🚀 **2026.2.12**: **Sirchmunk v0.0.3 发布：核心搜索算法与 MCP 集成双升级**

  - **MCP 增强**：深度优化 Model Context Protocol 集成及配置文档。
  - **搜索精细化**：搜索工具支持 Glob 模式过滤，默认自动排除缓存与日志文件。
  - **算法文档**：新增“蒙特卡洛证据采样”与“自进化知识簇”核心原理深度解析。
  - **架构稳定性**：重构搜索管线（AgenticSearch.search），引入 SHA256 确定性 ID 确保知识簇一致性。


* 🚀 **2026.2.5**: 发布 **v0.0.2** — MCP 支持、CLI 命令行 & 知识持久化！
  - **MCP 集成**：完整支持 [Model Context Protocol](https://modelcontextprotocol.io)，与 Claude Desktop 和 Cursor IDE 无缝协作。
  - **CLI 命令行**：全新 `sirchmunk` 命令行工具，支持 `init`、`serve`、`search`、`web` 和 `mcp` 命令。
  - **KnowledgeCluster 持久化**：基于 DuckDB 存储，支持 Parquet 导出，高效管理知识聚类。
  - **知识复用**：基于语义相似度的知识聚类检索，通过 embedding 向量加速搜索。

* 🎉🎉 2026.1.22: **Sirchmunk** 初始版本 v0.0.1 现已发布！

</details>

---


## 🚀 快速开始

### 前置条件

- **Python** 3.10+
- **LLM API Key**（OpenAI 兼容 Endpoint，本地或远程）
- **Node.js** 18+（可选，用于 Web 界面）

### 安装

```bash
# 创建虚拟环境（推荐）
conda create -n sirchmunk python=3.13 -y && conda activate sirchmunk 

pip install sirchmunk

# 或使用 UV：
uv pip install sirchmunk

# 或从源码安装：
git clone https://github.com/modelscope/sirchmunk.git && cd sirchmunk
pip install -e .
```

### Python SDK 使用

```python
import asyncio

from sirchmunk import AgenticSear
