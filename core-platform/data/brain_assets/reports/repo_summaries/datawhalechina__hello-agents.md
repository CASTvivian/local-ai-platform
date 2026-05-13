# Repo Summary Source: datawhalechina/hello-agents
- URL: https://github.com/datawhalechina/hello-agents
- Local Path: core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents
- Buckets: agent, rag, llm_runtime
- Stars: 48290
- Language: Python
- Description: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

<div align="right">
  <a href="./README_EN.md">English</a> | 中文
</div>

<div align='center'>
  <img src="./docs/images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 《从零开始构建智能体》</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>从基础理论到实际应用，全面掌握智能体系统的设计与实现</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-Chinese-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/在线阅读-Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

---

## 🎯 项目介绍

&emsp;&emsp;如果说 2024 年是"百模大战"的元年，那么 2025 年无疑开启了"Agent 元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。然而，当前系统性、重实践的教程却极度匮乏。为此，我们发起了 Hello-Agents 项目，希望能为社区提供一本从零开始、理论与实战并重的智能体系统构建指南。

&emsp;&emsp;Hello-Agents 是 Datawhale 社区的<strong>系统性智能体学习教程</strong>。如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM 作为数据处理的后端；另一派则是 AI 原生的 Agent，即真正以 AI 驱动的 Agent。本教程旨在带领大家深入理解并构建后者——真正的 AI Native Agent。教程将带领你穿透框架表象，从智能体的核心原理出发，深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。我们相信，最好的学习方式就是动手实践。希望这本教程能成为你探索智能体世界的起点，能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。

## 📚 快速开始

### 在线阅读
**[🌐 国外访问](https://datawhalechina.github.io/hello-agents/)** | **[🚀 国内加速](https://hello-agents.datawhale.cc)** - 无需下载，随时随地学习

### 本地阅读
如果您希望在本地阅读或贡献内容，请参考下方的学习指南。

### ✨ 你将收获什么？

- 📖 <strong>Datawhale 开源免费</strong> 完全免费学习本项目所有内容，与社区共同成长
- 🔍 <strong>理解核心原理</strong> 深入理解智能体的概念、历史与经典范式
- 🏗️ <strong>亲手实现</strong> 掌握热门低代码平台和智能体代码框架的使用
- 🛠️ <strong>自研框架 [HelloAgents](https://github.com/jjyaoao/helloagents)</strong> 基于 Openai 原生 API 从零构建一个自己的智能体框架
- ⚙️ <strong>掌握高级技能</strong> 一步步实现上下文工程、Memory、协议、评估等系统性技术
- 🤝 <strong>模型训练</strong> 掌握 Agentic RL，从 SFT 到 GRPO 的全流程实战训练 LLM
- 🚀 <strong>驱动真实案例</strong> 实战开发智能旅行助手、赛博小镇等综合项目
- 📖 <strong>求职面试</strong> 学习智能体求职相关面试问题

## 📖 内容导航

| 章节                                                                                        | 关键内容                                      | 状态 |
| ------------------------------------------------------------------------------------------- | --------------------------------------------- | ---- |
| [前言](./docs/前言.md)                                                                      | 项目的缘起、背景及读者建议                    | ✅    |
| <strong>第一部分：智能体与语言模型基础</strong>                                             |                                               |      |
| [第一章 初识智能体](./docs/chapter1/第一章%20初识智能体.md)                                 | 智能体定义、类型、范式与应用                  | ✅    |
| [第二章 智能体发展史](./docs/chapter2/第二章%20智能体发展史.md)                             | 从符号主义到 LLM 驱动的智能体演进             | ✅    |
| [第三章 大语言模型基础](./docs/chapter3/第三章%20大语言模型基础.md)                         | Transformer、提示、主流 LLM 及其局限          | ✅    |
| <strong>第二部分：构建你的大语言模型智能体</strong>                                         |                                               |      |
| [第四章 智能体经典范式构建](./docs/chapter4/第四章%20智能体经典范式构建.md)                 | 手把手实现 ReAct、Plan-and-Solve、Reflection  | ✅    |
| [第五章 基于低代码平台的智能体搭建](./docs/chapter5/第五章%20基于低代码平台的智能体搭建.md) | 了解 Coze、Dify、n8n 等低代码智能体平台使用   | ✅    |
| [第六章 框架开发实践](./docs/chapter6/第六章%20框架开发实践.md)                             | AutoGen、AgentScope、LangGraph 等主流框架应用 | ✅    |
| [第七章 构建你的Agent框架](./docs/chapter7/第七章%20构建你的Agent框架.md)                   | 从 0 开始构建智能体框架                       | ✅    |
| <strong>第三部分：高级知识扩展</strong>                                                     |                                               |      |
| [第八章 记忆与检索](./docs/chapter8/第八章%20记忆与检索.md)                                 | 记忆系统，RAG，存储                           | ✅    |
| [第九章 上下文工程](./docs/chapter9/第九章%20上下文工程.md)                                 | 持续交互的"情境理解"                          | ✅    |
| [第十章 智能体通信协议](./docs/chapter10/第十章%20智能体通信协议.md)                        | MCP、A2A、ANP 等协议解析                      | ✅    |
| [第十一章 Agentic-RL](./docs/chapter11/第十一章%20Agentic-RL.md)                            | 从 SFT 到 GRPO 的 LLM 训练实战                | ✅    |
| [第十二章 智能体性能评估](./docs/chapter12/第十二章%20智能体性能评估.md)                    | 核心指标、基准测试与评估框架                  | ✅    |
| <strong>第四部分：综合案例进阶</strong>                                                     |                                               |      |
| [第十三章 智能旅行助手](./docs/chapter13/第十三章%20智能旅行助手.md)                        | MCP 与多智能体协作的真实世界应用              | ✅    |
| [第十四章 自动化深度研究智能体](./docs/chapter14/第十四章%20自动化深度研究智能体.md)        | DeepResearch Agent 复现与解析                 | ✅    |
| [第十五章 构建赛博小镇](./docs/chapter15/第十五章%20构建赛博小镇.md)                        | Agent 与游戏的结合，模拟社会动态              | ✅    |
| <strong>第五部分：毕业设计及未来展望</strong>                                               |                                               |      |
| [第十六章 毕业设计](./docs/chapter16/第十六章%20毕业设计.md)                                | 构建属于你的完整多智能体应用                  | ✅    |

### 社区贡献精选 (Community Blog)

&emsp;&emsp;欢迎大家将在学习 Hello-Agents 或 Agent 相关技术中的独到见解、实践总结，以 PR 的形式贡献到社区精选。如果是独立于正文的内容，也可以投稿至 Extra-Chapter！<strong>期待你的第一次贡献！</strong>

| 社区精选                                                                                                                                      | 内容总结                  |
| --------------------------------------------------------------------------------------------------------------------------------------------


# FILE: README_EN.md

<div align="right">
  English | <a href="./README.md">中文</a>
</div>

<div align='center'>
  <img src="./docs/images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 "Building Agent Systems from Scratch"</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>From foundational theory to practical applications, master the design and implementation of agent systems</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-English-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

---

## 🎯 Project Introduction

&emsp;&emsp;If 2024 was the year of the "Battle of a Hundred Models," then 2025 has undoubtedly ushered in the "Year of Agents." The focus of technology is shifting from training larger foundation models to building smarter agent applications. However, systematic, practice-oriented tutorials are extremely scarce. For this reason, we launched the Hello-Agents project, hoping to provide the community with a comprehensive guide to building agent systems from scratch, balancing theory and practice.

&emsp;&emsp;Hello-Agents is a **systematic agent learning tutorial** from the Datawhale community. Today, agent development is mainly divided into two schools: one is software engineering-oriented agents like Dify, Coze, and n8n, which are essentially process-driven software development with LLMs serving as data processing backends; the other is AI-native agents, truly AI-driven agents. This tutorial aims to lead you to deeply understand and build the latter—truly AI Native Agents. The tutorial will guide you through the surface of frameworks, starting from the core principles of agents, delving into their core architecture, understanding their classic paradigms, and ultimately building your own multi-agent applications. We believe that the best way to learn is through hands-on practice. We hope this tutorial can be your starting point for exploring the world of agents, transforming you from a "user" of large language models to a "builder" of agent systems.

## 📚 Quick Start

### Online Reading
**[🌐 International Access](https://datawhalechina.github.io/hello-agents/)** | **[🚀 Domestic Acceleration](https://hello-agents.datawhale.cc)** - No download required, learn anytime, anywhere

### Local Reading
If you wish to read locally or contribute content, please refer to the learning guide below.

### ✨ What Will You Gain?

- 📖 **Datawhale Open Source & Free** - Learn all project content completely free, grow with the community
- 🔍 **Understand Core Principles** - Deeply understand agent concepts, history, and classic paradigms
- 🏗️ **Hands-on Implementation** - Master popular low-code platforms and agent code frameworks
- 🛠️ **Self-developed Framework [HelloAgents](https://github.com/jjyaoao/helloagents)** - Build your own agent framework from scratch based on OpenAI native API
- ⚙️ **Master Advanced Skills** - Step-by-step implementation of context engineering, Memory, protocols, evaluation, and other systematic technologies
- 🤝 **Model Training** - Master Agentic RL, from SFT to GRPO full-process practical LLM training
- 🚀 **Drive Real Cases** - Practical development of intelligent travel assistants, cyber towns, and other comprehensive projects
- 📖 **Job Interviews** - Learn agent-related interview questions for job hunting

## 📖 Content Navigation

| Chapter                                                                                                               | Key Content                                                                | Status |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------ |
| [Preface](./docs/Preface.md)                                                                                          | Project origin, background, and reader suggestions                         | ✅      |
| **Part 1: Agent and Language Model Fundamentals**                                                                     |                                                                            |        |
| [Chapter 1: Introduction to Agents](./docs/chapter1/Chapter1-Introduction-to-Agents.md)                               | Agent definition, types, paradigms, and applications                       | ✅      |
| [Chapter 2: History of Agents](./docs/chapter2/Chapter2-History-of-Agents.md)                                         | Evolution from symbolism to LLM-driven agents                              | ✅      |
| [Chapter 3: Large Language Model Fundamentals](./docs/chapter3/Chapter3-Fundamentals-of-Large-Language-Models.md)     | Transformer, prompts, mainstream LLMs and their limitations                | ✅      |
| **Part 2: Building Your LLM Agent**                                                                                   |                                                                            |        |
| [Chapter 4: Classic Agent Paradigm Construction](./docs/chapter4/Chapter4-Building-Classic-Agent-Paradigms.md)        | Hands-on implementation of ReAct, Plan-and-Solve, Refl


# FILE: docs/前言.md

# 前言
自 2022 年底以来，以 ChatGPT 为代表的大语言模型（Large Language Model, LLM）如同一场技术海啸，彻底改变了我们与人工智能交互的方式。LLM 强大的自然语言理解和生成能力，让我们看到了通往通用人工智能（AGI）的曙光。然而，当最初的惊艳沉淀下来，开发者们开始探索下一个前沿：如何让 AI 不仅仅是一个“有问必答”的工具，而是成为一个能自主规划、调用工具、解决复杂问题的“行动者”？

答案，就是 智能体（Agent）。

如果说 2024 年是“百模大战”的元年，那么 2025 年无疑开启了“Agent 元年”。我们看到，技术的焦点正从训练更大、更强的基础模型，转向如何构建更聪明、更高效的智能体应用。单个智能体已经能胜任特定领域的任务，而由多个智能体分工、协作、甚至辩论，共同完成一个宏大目标的多智能体系统（Multi-Agent System, MAS），则被视为释放 LLM 全部潜能、解决真实世界复杂问题的关键钥匙。

然而，当前的生态中存在一个明显的断层：一方面是层出不穷的 Agent 框架和应用，令人眼花缭乱；另一方面，却是系统性知识的极度匮乏。大多数教程聚焦于某个特定框架的 API 调用，学习者往往“知其然，而不知其所以然”，在面对复杂需求时，依然感到力不从心。我们缺少一本能够穿透框架表象，从第一性原理出发，系统讲解智能体设计、构建与协作的实战指南。

鉴于此，我们发起了 Hello-Agents 项目，希望能为社区提供一本从零开始、理论与实战并重的智能体系统构建指南。我们不仅会带你领略智能体领域最前沿的技术，更会引导你深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。

我们相信，最好的学习方式就是动手实践。希望这本教程能成为你探索智能体世界的起点，能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。

## 写给读者的建议

欢迎你，未来的智能系统构建者！在开启这段激动人心的旅程之前，请允许我们给你一些小小的建议。

在阅读项目之前，我们希望你：

- 具备基础的 Python 编程能力。

- 对大语言模型有基本的概念性了解（例如，知道如何获取 LLM 的 API）。

- 请放心，你无需具备深厚的算法或模型训练背景，项目的重点是应用与构建。

本项目分为五部分，覆盖基础到实战，循序渐进，层层相扣：

第一部分（基础篇）： 我们将为你铺垫人工智能与 LLM 的核心知识，让你对智能体的诞生背景有宏观的认识。

第二部分（单体篇）： 这是你动手实践的开始。我们将带你从零开始，构建一个功能完备的单体智能，深入理解其内部的“心智”结构。

第三部分（高级篇）： 在这里，你的智能体将“学会”思考、拥有记忆和工具，并掌握智能体之间的通信协议，最终完成评估的闭环。

第四部分（实战篇）： 这是项目的核心价值所在。你将通过一系列精心设计的综合案例，将所学知识融会贯通，在实战中淬炼真金。

第五部分（展望篇）： 旅程的终点是新的起点。你将亲手打造属于你的“毕业作品”，为你的学习之旅画上一个圆满的句号。

纸上得来终觉浅，绝知此事要躬行。为了获得最佳的学习效果，我们在项目的`code`文件夹内提供了配套的全部代码，强烈建议你将理论与实践相结合。请务必亲手运行、调试甚至修改项目里提供的每一份代码。我们鼓励你举一反三，将所学技术应用到自己感兴趣的真实场景中，这才是学习的最终目的。

最后，作为一个开源项目，我们热忱欢迎你的参与和贡献。当你遇到问题时，可以在我们的社区中提问；当你有了新的想法或发现时，也欢迎你随时加入到项目的共建中来。

感谢你选择阅读 Hello-agents，祝你学习愉快，探索无限！



# FILE: docs/README.md

<div align="right">
  <a href="./README_EN.md">English</a> | 中文
</div>
<div align='center'>
  <img src="./images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 《从零开始构建智能体》</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>从基础理论到实际应用，全面掌握智能体系统的设计与实现</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-Chinese-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/在线阅读-Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>


---

## 🎯 项目介绍

&emsp;&emsp;如果说 2024 年是"百模大战"的元年，那么 2025 年无疑开启了"Agent 元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。然而，当前系统性、重实践的教程却极度匮乏。为此，我们发起了 Hello-Agents 项目，希望能为社区提供一本从零开始、理论与实战并重的智能体系统构建指南。

&emsp;&emsp;Hello-Agents 是 Datawhale 社区的<strong>系统性智能体学习教程</strong>。如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM 作为数据处理的后端；另一派则是 AI 原生的 Agent，即真正以 AI 驱动的 Agent。本教程旨在带领大家深入理解并构建后者——真正的 AI Native Agent。教程将带领你穿透框架表象，从智能体的核心原理出发，深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。我们相信，最好的学习方式就是动手实践。希望这本教程能成为你探索智能体世界的起点，能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。

## 🌐 在线阅读

**[🌐 国外访问](https://datawhalechina.github.io/hello-agents/)** | **[🚀 国内加速](https://hello-agents.datawhale.cc)**

### ✨ 你将收获什么？

- 📖 <strong>Datawhale 开源免费</strong> 完全免费学习本项目所有内容，与社区共同成长
- 🔍 <strong>理解核心原理</strong> 深入理解智能体的概念、历史与经典范式
- 🏗️ <strong>亲手实现</strong> 掌握热门低代码平台和智能体代码框架的使用
- 🛠️ <strong>自研框架[HelloAgents](https://github.com/jjyaoao/helloagents)</strong> 基于 Openai 原生 API 从零构建一个自己的智能体框架
- ⚙️ <strong>掌握高级技能</strong> 一步步实现上下文工程、Memory、协议、评估等系统性技术
- 🤝 <strong>模型训练</strong> 掌握 Agentic RL，从 SFT 到 GRPO 的全流程实战训练 LLM
- 🚀 <strong>驱动真实案例</strong> 实战开发智能旅行助手、赛博小镇等综合项目
- 📖 <strong>求职面试</strong> 学习智能体求职相关面试问题

## 📖 内容导航

| 章节                                                                                   | 关键内容                                      | 状态 |
| -------------------------------------------------------------------------------------- | --------------------------------------------- | ---- |
| [前言](./前言.md)                                                                      | 项目的缘起、背景及读者建议                    | ✅    |
| <strong>第一部分：智能体与语言模型基础</strong>                                        |                                               |      |
| [第一章 初识智能体](./chapter1/第一章%20初识智能体.md)                                 | 智能体定义、类型、范式与应用                  | ✅    |
| [第二章 智能体发展史](./chapter2/第二章%20智能体发展史.md)                             | 从符号主义到 LLM 驱动的智能体演进             | ✅    |
| [第三章 大语言模型基础](./chapter3/第三章%20大语言模型基础.md)                         | Transformer、提示、主流 LLM 及其局限          | ✅    |
| <strong>第二部分：构建你的大语言模型智能体</strong>                                    |                                               |      |
| [第四章 智能体经典范式构建](./chapter4/第四章%20智能体经典范式构建.md)                 | 手把手实现 ReAct、Plan-and-Solve、Reflection  | ✅    |
| [第五章 基于低代码平台的智能体搭建](./chapter5/第五章%20基于低代码平台的智能体搭建.md) | 了解 Coze、Dify、n8n 等低代码智能体平台使用   | ✅    |
| [第六章 框架开发实践](./chapter6/第六章%20框架开发实践.md)                             | AutoGen、AgentScope、LangGraph 等主流框架应用 | ✅    |
| [第七章 构建你的Agent框架](./chapter7/第七章%20构建你的Agent框架.md)                   | 从 0 开始构建智能体框架                       | ✅    |
| <strong>第三部分：高级知识扩展</strong>                                                |                                               |      |
| [第八章 记忆与检索](./chapter8/第八章%20记忆与检索.md)                                 | 记忆系统，RAG，存储                           | ✅    |
| [第九章 上下文工程](./chapter9/第九章%20上下文工程.md)                                 | 持续交互的"情境理解"                          | ✅    |
| [第十章 智能体通信协议](./chapter10/第十章%20智能体通信协议.md)                        | MCP、A2A、ANP 等协议解析                      | ✅    |
| [第十一章 Agentic-RL](./chapter11/第十一章%20Agentic-RL.md)                            | 从 SFT 到 GRPO 的 LLM 训练实战                | ✅    |
| [第十二章 智能体性能评估](./chapter12/第十二章%20智能体性能评估.md)                    | 核心指标、基准测试与评估框架                  | ✅    |
| <strong>第四部分：综合案例进阶</strong>                                                |                                               |      |
| [第十三章 智能旅行助手](./chapter13/第十三章%20智能旅行助手.md)                        | MCP 与多智能体协作的真实世界应用              | ✅    |
| [第十四章 自动化深度研究智能体](./chapter14/第十四章%20自动化深度研究智能体.md)        | DeepResearch Agent 复现与解析                 | ✅    |
| [第十五章 构建赛博小镇](./chapter15/第十五章%20构建赛博小镇.md)                        | Agent 与游戏的结合，模拟社会动态              | ✅    |
| <strong>第五部分：毕业设计及未来展望</strong>                                          |                                               |      |
| [第十六章 毕业设计](./chapter16/第十六章%20毕业设计.md)                                | 构建属于你的完整多智能体应用                  | ✅    |

### 社区贡献精选 (Community Blog)

&emsp;&emsp;欢迎大家将在学习 Hello-Agents 或 Agent 相关技术中的独到见解、实践总结，以 PR 的形式贡献到社区精选。如果是独立于正文的内容，也可以投稿至 Extra-Chapter！<strong>期待你的第一次贡献！</strong>

| 社区精选                                                                                                                                      | 内容总结                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [00-共创毕业设计](https://github.com/datawhalechina/hello-agents/blob/main/Co-creation-projects)                                             | 社区共创毕业设计项目      


# FILE: docs/README_EN.md

<div align='center'>
  <img src="./images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 "Building Agent Systems from Scratch"</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>From fundamental theory to practical applications, comprehensively master the design and implementation of agent systems</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-English-blue?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/Online%20Reading-在线阅读-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

---

## 🎯 Project Introduction

&emsp;&emsp;If 2024 was the inaugural year of the "battle of a hundred models," then 2025 has undoubtedly ushered in the "Year of Agents." The technological focus is shifting from training larger foundation models to building smarter agent applications. However, systematic, practice-oriented tutorials are extremely scarce. For this reason, we launched the Hello-Agents project, hoping to provide the community with a guide for building agent systems from scratch, balancing theory and practice.

&emsp;&emsp;Hello-Agents is a **systematic agent learning tutorial** from the Datawhale community. Currently, Agent construction is mainly divided into two schools: one is software engineering-type Agents like Dify, Coze, and n8n, which are essentially process-driven software development with LLMs serving as data processing backends; the other is AI-native Agents, truly AI-driven Agents. This tutorial aims to lead you to deeply understand and build the latter—true AI Native Agents. The tutorial will guide you to penetrate framework appearances, start from the core principles of agents, delve into their core architecture, understand their classic paradigms, and ultimately build your own multi-agent applications with your own hands. We believe that the best way to learn is through hands-on practice. We hope this tutorial can become your starting point for exploring the world of agents, enabling you to transform from a "user" of large language models to a "builder" of agent systems.

## 🌐 Online Reading

**[🌐 International Access](https://datawhalechina.github.io/hello-agents/)** | **[🚀 Domestic Acceleration](https://hello-agents.datawhale.cc)**

### ✨ What Will You Gain?

- 📖 **Datawhale Open Source Free** - Learn all content of this project completely free, grow together with the community
- 🔍 **Understand Core Principles** - Deeply understand the concepts, history, and classic paradigms of agents
- 🏗️ **Hands-on Implementation** - Master the use of popular low-code platforms and agent code frameworks
- 🛠️ **Self-developed Framework [HelloAgents](https://github.com/jjyaoao/helloagents)** - Build your own agent framework from scratch based on OpenAI native API
- ⚙️ **Master Advanced Skills** - Step by step implement systematic technologies such as context engineering, Memory, protocols, and evaluation
- 🤝 **Model Training** - Master Agentic RL, from SFT to GRPO full-process practical training of LLMs
- 🚀 **Drive Real Cases** - Practical development of comprehensive projects such as intelligent travel assistants and cyber towns
- 📖 **Job Interviews** - Learn agent-related interview questions for job hunting

## 📖 Content Navigation

| Chapter                                                                                                                 | Key Content                                                                 | Status |
| ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------ |
| [Preface](./Preface.md)                                                                                                 | Project origin, background, and reader suggestions                          | ✅      |
| **Part One: Agent and Language Model Fundamentals**                                                                     |                                                                             |        |
| [Chapter 1: Introduction to Agents](./chapter1/Chapter1-Introduction-to-Agents.md)                                      | Agent definition, types, paradigms, and applications                        | ✅      |
| [Chapter 2: History of Agents](./chapter2/Chapter2-History-of-Agents.md)                                                | Evolution from symbolism to LLM-driven agents                               | ✅      |
| [Chapter 3: Large Language Model Fundamentals](./chapter3/Chapter3-Fundamentals-of-Large-Language-Models.md)            | Transformer, prompts, mainstream LLMs and their limitations                 | ✅      |
| **Part Two: Building Your Large Language Model Agent**                                                                  |                                                                             |        |
| [Chapter 4: Building Classic Agent Paradigms](./chapter4/Chapter4-Building-Classic-Agent-Paradigms.md)                  | Hands-on implementation of ReAct, Plan-and-Solve, Reflection                | ✅      |
| [Chapter 5: Agent Building Based on Low-Code Platforms](./chapter5/Chapter5-Building-Agents-with-Low-Code-Platforms.md) | Und


# FILE: docs/_sidebar.md

- [Hello-Agents](./README.md)
  - [前言](./前言.md)
  
- <strong>第一部分：智能体与语言模型基础</strong>
  - [第一章 初识智能体](./chapter1/第一章%20初识智能体.md)
  - [第二章 智能体发展史](./chapter2/第二章%20智能体发展史.md)
  - [第三章 大语言模型基础](./chapter3/第三章%20大语言模型基础.md)

- <strong>第二部分：构建你的大语言模型智能体</strong>
  - [第四章 智能体经典范式构建](./chapter4/第四章%20智能体经典范式构建.md)
  - [第五章 基于低代码平台的智能体搭建](./chapter5/第五章%20基于低代码平台的智能体搭建.md)
  - [第六章 框架开发实践](./chapter6/第六章%20框架开发实践.md)
  - [第七章 构建你的Agent框架](./chapter7/第七章%20构建你的Agent框架.md)

- <strong>第三部分：高级知识扩展</strong>
  - [第八章 记忆与检索](./chapter8/第八章%20记忆与检索.md)
  - [第九章 上下文工程](./chapter9/第九章%20上下文工程.md)
  - [第十章 智能体通信协议](./chapter10/第十章%20智能体通信协议.md)
  - [第十一章 Agentic-RL](./chapter11/第十一章%20Agentic-RL.md)
  - [第十二章 智能体性能评估](./chapter12/第十二章%20智能体性能评估.md)

- <strong>第四部分：综合案例进阶</strong>
  - [第十三章 智能旅行助手](./chapter13/第十三章%20智能旅行助手.md)
  - [第十四章 自动化深度研究智能体](./chapter14/第十四章%20自动化深度研究智能体.md)
  - [第十五章 构建赛博小镇](./chapter15/第十五章%20构建赛博小镇.md)

- <strong>第五部分：毕业设计及未来展望</strong>
  - [第十六章 毕业设计](./chapter16/第十六章%20毕业设计.md)



# FILE: docs/Preface.md

# Preface

Since the end of 2022, Large Language Models (LLMs) represented by ChatGPT have swept across the world like a technological tsunami, completely transforming how we interact with artificial intelligence. The powerful natural language understanding and generation capabilities of LLMs have shown us a glimpse of the path toward Artificial General Intelligence (AGI). However, as the initial amazement settled, developers began exploring the next frontier: how to make AI not just a "question-answering" tool, but an "actor" capable of autonomous planning, tool invocation, and solving complex problems?

The answer is **Agents**.

If 2024 was the inaugural year of the "battle of a hundred models," then 2025 has undoubtedly ushered in the "Year of Agents." We see that the technological focus is shifting from training larger and more powerful foundation models to building smarter and more efficient agent applications. Individual agents can already handle tasks in specific domains, while Multi-Agent Systems (MAS), where multiple agents collaborate through division of labor, cooperation, and even debate to accomplish grand goals, are viewed as the key to unlocking the full potential of LLMs and solving complex real-world problems.

However, there is an obvious gap in the current ecosystem: on one hand, there is a dizzying array of Agent frameworks and applications emerging continuously; on the other hand, there is an extreme scarcity of systematic knowledge. Most tutorials focus on API calls for specific frameworks, leaving learners "knowing how but not knowing why," still feeling powerless when facing complex requirements. We lack a practical guide that can penetrate framework appearances, start from first principles, and systematically explain agent design, construction, and collaboration.

In view of this, we launched the Hello-Agents project, hoping to provide the community with a guide for building agent systems from scratch, balancing theory and practice. We will not only lead you to appreciate the most cutting-edge technologies in the agent field but also guide you to delve into their core architecture, understand their classic paradigms, and ultimately build your own multi-agent applications with your own hands.

We believe that the best way to learn is through hands-on practice. We hope this tutorial can become your starting point for exploring the world of agents, enabling you to transform from a "user" of large language models to a "builder" of agent systems.

## Suggestions for Readers

Welcome, future intelligent system builder! Before embarking on this exciting journey, please allow us to give you some small suggestions.

Before reading this project, we hope you:

- Have basic Python programming skills.

- Have a basic conceptual understanding of large language models (for example, know how to obtain LLM APIs).

- Rest assured, you don't need a deep background in algorithms or model training; the project focuses on application and construction.

This project is divided into five parts, covering basics to practice, progressing step by step, layer by layer:

**Part One (Fundamentals)**: We will lay the foundation of core knowledge about artificial intelligence and LLMs, giving you a macro understanding of the background of agent emergence.

**Part Two (Single Agent)**: This is where your hands-on practice begins. We will guide you to build a fully functional single agent from scratch, deeply understanding its internal "mental" structure.

**Part Three (Advanced)**: Here, your agent will "learn" to think, possess memory and tools, and master communication protocols between agents, ultimately completing the evaluation closed loop.

**Part Four (Practice)**: This is where the core value of the project lies. You will integrate all learned knowledge through a series of carefully designed comprehensive cases, tempering true gold in practice.

**Part Five (Outlook)**: The end of the journey is a new beginning. You will personally create your "graduation project," drawing a perfect conclusion to your learning journey.

"What is learned on paper is superficial; to truly understand, one must practice." To achieve the best learning effect, we provide all supporting code in the project's `code` folder. We strongly recommend combining theory with practice. Please be sure to personally run, debug, and even modify every piece of code provided in the project. We encourage you to apply what you've learned to real scenarios that interest you—this is the ultimate purpose of learning.

Finally, as an open-source project, we warmly welcome your participation and contribution. When you encounter problems, you can ask questions in our community; when you have new ideas or discoveries, you are also welcome to join the project's co-construction at any time.

Thank you for choosing to read Hello-Agents. We wish you happy learning and unlimited exploration!




# FILE: docs/_sidebar_en.md

- [Hello-Agents](/en/README_EN.md)
  - [Preface](./Preface.md)

- <strong>Part I: Fundamentals of Agents and Language Models</strong>
  - [Chapter 1 Introduction to Agents](/en/chapter1/Chapter1-Introduction-to-Agents.md)
  - [Chapter 2 History of Agents](/en/chapter2/Chapter2-History-of-Agents.md)
  - [Chapter 3 Fundamentals of Large Language Models](/en/chapter3/Chapter3-Fundamentals-of-Large-Language-Models.md)

- <strong>Part II: Building Your Large Language Model Agent</strong>
  - [Chapter 4 Building Classic Agent Paradigms](/en/chapter4/Chapter4-Building-Classic-Agent-Paradigms.md)
  - [Chapter 5 Building Agents with Low-Code Platforms](/en/chapter5/Chapter5-Building-Agents-with-Low-Code-Platforms.md)
  - [Chapter 6 Framework Development Practice](/en/chapter6/Chapter6-Framework-Development-Practice.md)
  - [Chapter 7 Building Your Agent Framework](/en/chapter7/Chapter7-Building-Your-Agent-Framework.md)

- <strong>Part III: Advanced Knowledge Extension</strong>
  - [Chapter 8 Memory and Retrieval](/en/chapter8/Chapter8-Memory-and-Retrieval.md)
  - [Chapter 9 Context Engineering](/en/chapter9/Chapter9-Context-Engineering.md)
  - [Chapter 10 Agent Communication Protocols](/en/chapter10/Chapter10-Agent-Communication-Protocols.md)
  - [Chapter 11 Agentic-RL](/en/chapter11/Chapter11-Agentic-RL.md)
  - [Chapter 12 Agent Performance Evaluation](/en/chapter12/Chapter12-Agent-Performance-Evaluation.md)

- <strong>Part IV: Comprehensive Case Studies</strong>
  - [Chapter 13 Intelligent Travel Assistant](/en/chapter13/Chapter13-Intelligent-Travel-Assistant.md)
  - [Chapter 14 Automated Deep Research Agent](/en/chapter14/Chapter14-Automated-Deep-Research-Agent.md)
  - [Chapter 15 Building Cyber Town](/en/chapter15/Chapter15-Building-Cyber-Town.md)

- <strong>Part V: Graduation Project and Future Outlook</strong>
  - [Chapter 16 Graduation Project](/en/chapter16/Chapter16-Graduation-Project.md)




# FILE: docs/chapter8/Chapter8-Memory-and-Retrieval.md

# Chapter 8 Memory and Retrieval

In previous chapters, we built the basic architecture of the HelloAgents framework, implementing various agent paradigms and tool systems. However, our framework still lacks a critical capability: **memory**. If an agent cannot remember previous interactions or learn from historical experiences, its performance will be greatly limited in continuous conversations or complex tasks.

This chapter will add two core capabilities to HelloAgents based on the framework built in Chapter 7: **Memory System** and **Retrieval-Augmented Generation (RAG)**. We will adopt a "framework extension + knowledge popularization" approach, deeply understanding the theoretical foundations of Memory and RAG during the construction process, and ultimately implementing an agent system with complete memory and knowledge retrieval capabilities.


## 8.1 From Cognitive Science to Agent Memory

### 8.1.1 Inspiration from Human Memory Systems

Before building an agent's memory system, let's first understand from a cognitive science perspective how humans process and store information. Human memory is a multi-level cognitive system that not only stores information but also classifies and organizes information based on importance, time, and context. Cognitive psychology provides a classic theoretical framework for understanding the structure and processes of memory<sup>[1]</sup>, as shown in Figure 8.1.

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/8-figures/8-1.png" alt="Human Memory System Structure" width="85%"/>
  <p>Figure 8.1 Hierarchical Structure of Human Memory System</p>
</div>

According to cognitive psychology research, human memory can be divided into the following levels:

1. **Sensory Memory**: Very short duration (0.5-3 seconds), huge capacity, responsible for temporarily storing all information received by the senses
2. **Working Memory**: Short duration (15-30 seconds), limited capacity (7±2 items), responsible for information processing in current tasks
3. **Long-term Memory**: Long duration (can last a lifetime), almost unlimited capacity, further divided into:
   - **Procedural Memory**: Skills and habits (such as riding a bicycle)
   - **Declarative Memory**: Knowledge that can be expressed in language, further divided into:
     - **Semantic Memory**: General knowledge and concepts (such as "Paris is the capital of France")
     - **Episodic Memory**: Personal experiences and events (such as "yesterday's meeting content")

### 8.1.2 Why Agents Need Memory and RAG

Drawing on the design of human memory systems, we can understand why agents also need similar memory capabilities. An important characteristic of human intelligence is the ability to remember past experiences, learn from them, and apply these experiences to new situations. Similarly, a truly intelligent agent also needs memory capabilities. For LLM-based agents, they typically face two fundamental limitations: **forgetting of conversation state** and **limitations of built-in knowledge**.

(1) Limitation 1: Conversation Forgetting Due to Statelessness

Current large language models, although powerful, are designed to be **stateless**. This means that each user request (or API call) is an independent, unrelated computation. The model itself does not automatically "remember" the content of the previous conversation. This brings several problems:

1. **Context Loss**: In long conversations, important early information may be lost due to context window limitations
2. **Lack of Personalization**: The agent cannot remember user preferences, habits, or specific needs
3. **Limited Learning Ability**: Cannot learn and improve from past successes or failures
4. **Consistency Issues**: May provide contradictory answers in multi-turn conversations

Let's understand this problem through a specific example:

```python
# How to use Agent from Chapter 7
from hello_agents import SimpleAgent, HelloAgentsLLM

agent = SimpleAgent(name="Learning Assistant", llm=HelloAgentsLLM())

# First conversation
response1 = agent.run("My name is Zhang San, I'm learning Python and have mastered basic syntax")
print(response1)  # "Great! Python basic syntax is an important foundation for programming..."
 
# Second conversation (new session)
response2 = agent.run("Do you remember my learning progress?")
print(response2)  # "Sorry, I don't know your learning progress..."
```

To solve this problem, our framework needs to introduce a memory system.

(2) Limitation 2: Limitations of Model's Built-in Knowledge

Besides forgetting conversation history, another core limitation of LLMs is that their knowledge is **static and limited**. This knowledge comes entirely from their training data, bringing a series of problems:

1. **Knowledge Timeliness**: Large models have a training data cutoff date and cannot access the latest information
2. **Domain-Specific Knowledge**: General models may lack sufficient depth in specific domains
3. **Factual Accuracy**: Reduce model hallucinations through retrieval verification
4. **Explainability**: Provide information sources to enhance answer credibility

To overcome this limitation, RAG technology emerged. Its core idea is to retrieve the most relevant information from an external knowledge base (such as documents, databases, APIs) before the model generates an answer, and provide this information as context to the model.

### 8.1.3 Memory and RAG System Architecture Design

Based on the framework foundation established in Chapter 7 and inspiration from cognitive science, we designed a layered memory and RAG system architecture, as shown in Figure 8.2. This architecture not only draws on the hierarchical structure of human memory systems but also fully considers the scalability of engineering implementation. In implementation, we design memory and RAG as two independent tools: `memory_tool` is responsible for storing and maintaining interaction


# FILE: docs/chapter8/第八章 记忆与检索.md

# 第八章 记忆与检索

在前面的章节中，我们构建了HelloAgents框架的基础架构，实现了多种智能体范式和工具系统。不过，我们的框架还缺少一个关键能力：<strong>记忆</strong>。如果智能体无法记住之前的交互内容，也无法从历史经验中学习，那么在连续对话或复杂任务中，其表现将受到极大限制。

本章将在第七章构建的框架基础上，为HelloAgents增加两个核心能力：<strong>记忆系统（Memory System）</strong>和<strong>检索增强生成（Retrieval-Augmented Generation, RAG）</strong>。我们将采用"框架扩展 + 知识科普"的方式，在构建过程中深入理解Memory和RAG的理论基础，最终实现一个具有完整记忆和知识检索能力的智能体系统。


## 8.1 从认知科学到智能体记忆

### 8.1.1 人类记忆系统的启发

在构建智能体的记忆系统之前，让我们先从认知科学的角度理解人类是如何处理和存储信息的。人类记忆是一个多层级的认知系统，它不仅能存储信息，还能根据重要性、时间和上下文对信息进行分类和整理。认知心理学为理解记忆的结构和过程提供了经典的理论框架<sup>[1]</sup>，如图8.1所示。

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/8-figures/8-1.png" alt="人类记忆系统结构图" width="85%"/>
  <p>图 8.1 人类记忆系统的层次结构</p>
</div>

根据认知心理学的研究，人类记忆可以分为以下几个层次：

1. <strong>感觉记忆（Sensory Memory）</strong>：持续时间极短（0.5-3秒），容量巨大，负责暂时保存感官接收到的所有信息
2. <strong>工作记忆（Working Memory）</strong>：持续时间短（15-30秒），容量有限（7±2个项目），负责当前任务的信息处理
3. <strong>长期记忆（Long-term Memory）</strong>：持续时间长（可达终生），容量几乎无限，进一步分为：
   - <strong>程序性记忆</strong>：技能和习惯（如骑自行车）
   - <strong>陈述性记忆</strong>：可以用语言表达的知识，又分为：
     - <strong>语义记忆</strong>：一般知识和概念（如"巴黎是法国首都"）
     - <strong>情景记忆</strong>：个人经历和事件（如"昨天的会议内容"）

### 8.1.2 为何智能体需要记忆与RAG

借鉴人类记忆系统的设计，我们可以理解为什么智能体也需要类似的记忆能力。人类智能的一个重要特征就是能够记住过去的经历，从中学习，并将这些经验应用到新的情况中。同样，一个真正智能的智能体也需要具备记忆能力。对于基于LLM的智能体而言，通常面临两个根本性局限：<strong>对话状态的遗忘</strong>和<strong>内置知识的局限</strong>。

（1）局限一：无状态导致的对话遗忘

当前的大语言模型虽然强大，但设计上是<strong>无状态的</strong>。这意味着，每一次用户请求（或API调用）都是一次独立的、无关联的计算。模型本身不会自动“记住”上一次对话的内容。这带来了几个问题：

1. <strong>上下文丢失</strong>：在长对话中，早期的重要信息可能会因为上下文窗口限制而丢失
2. <strong>个性化缺失</strong>：Agent无法记住用户的偏好、习惯或特定需求
3. <strong>学习能力受限</strong>：无法从过往的成功或失败经验中学习改进
4. <strong>一致性问题</strong>：在多轮对话中可能出现前后矛盾的回答

让我们通过一个具体例子来理解这个问题：

```python
# 第七章的Agent使用方式
from hello_agents import SimpleAgent, HelloAgentsLLM

agent = SimpleAgent(name="学习助手", llm=HelloAgentsLLM())

# 第一次对话
response1 = agent.run("我叫张三，正在学习Python，目前掌握了基础语法")
print(response1)  # "很好！Python基础语法是编程的重要基础..."
 
# 第二次对话（新的会话）
response2 = agent.run("你还记得我的学习进度吗？")
print(response2)  # "抱歉，我不知道您的学习进度..."
```

要解决这个问题，我们的框架需要引入记忆系统。

（2）局限二：模型内置知识的局限性

除了遗忘对话历史，LLM 的另一个核心局限在于其知识是<strong>静态的、有限的</strong>。这些知识完全来自于它的训练数据，并因此带来一系列问题：

1. <strong>知识时效性</strong>：大模型的训练数据有时间截止点，无法获取最新信息
2. <strong>专业领域知识</strong>：通用模型在特定领域的深度知识可能不足
3. <strong>事实准确性</strong>：通过检索验证，减少模型的幻觉问题
4. <strong>可解释性</strong>：提供信息来源，增强回答的可信度

为了克服这一局限，RAG技术应运而生。它的核心思想是在模型生成回答之前，先从一个外部知识库（如文档、数据库、API）中检索出最相关的信息，并将这些信息作为上下文一同提供给模型。

### 8.1.3 记忆与RAG系统架构设计

基于第七章建立的框架基础和认知科学的启发，我们设计了一个分层的记忆与RAG系统架构，如图8.2所示。这个架构不仅借鉴了人类记忆系统的层次结构，还充分考虑了工程实现的可扩展性。在实现上，我们将记忆和RAG设计为两个独立的工具：`memory_tool`负责存储和维护对话过程中的交互信息，`rag_tool`则负责从用户提供的知识库中检索相关信息作为上下文，并可将重要的检索结果自动存储到记忆系统中。
<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/8-figures/8-2.png" alt="HelloAgents记忆与RAG系统架构图" width="95%"/>
  <p>图 8.2 HelloAgents记忆与RAG系统整体架构</p>
</div>

记忆系统采用了四层架构设计：

```
HelloAgents记忆系统
├── 基础设施层 (Infrastructure Layer)
│   ├── MemoryManager - 记忆管理器（统一调度和协调）
│   ├── MemoryItem - 记忆数据结构（标准化记忆项）
│   ├── MemoryConfig - 配置管理（系统参数设置）
│   └── BaseMemory - 记忆基类（通用接口定义）
├── 记忆类型层 (Memory Types Layer)
│   ├── WorkingMemory - 工作记忆（临时信息，TTL管理）
│   ├── EpisodicMemory - 情景记忆（具体事件，时间序列）
│   ├── SemanticMemory - 语义记忆（抽象知识，图谱关系）
│   └── PerceptualMemory - 感知记忆（多模态数据）
├── 存储后端层 (Storage Backend Layer)
│   ├── QdrantVectorStore - 向量存储（高性能语义检索）
│   ├── Neo4jGraphStore - 图存储（知识图谱管理）
│   └── SQLiteDocumentStore - 文档存储（结构化持久化）
└── 嵌入服务层 (Embedding Service Layer)
    ├── DashScopeEmbedding - 通义千问嵌入（云端API）
    ├── LocalTransformerEmbedding - 本地嵌入（离线部署）
    └── TFIDFEmbedding - TFIDF嵌入（轻量级兜底）
```

RAG系统专注于外部知识的获取和利用：

```
HelloAgents RAG系统
├── 文档处理层 (Document Processing Layer)
│   ├── DocumentProcessor - 文档处理器（多格式解析）
│   ├── Document - 文档对象（元数据管理）
│   └── Pipeline - RAG管道（端到端处理）
├── 嵌入表示层 (Embedding Layer)
│   └── 统一嵌入接口 - 复用记忆系统的嵌入服务
├── 向量存储层 (Vector Storage Layer)
│   └── QdrantVectorStore - 向量数据库（命名空间隔离）
└── 智能问答层 (Intelligent Q&A Layer)
    ├── 多策略检索 - 向量检索 + MQE + HyDE
    ├── 上下文构建 - 智能片段合并与截断
    └── LLM增强生成 - 基于上下文的准确问答
```

### 8.1.4 本章学习目标与快速体验

让我们先看看第八章的核心学习内容：

```
hello-agents/
├── hello_agents/
│   ├── memory/                   # 记忆系统模块
│   │   ├── base.py               # 基础数据结构（MemoryItem, MemoryConfig, BaseMemory）
│   │   ├── manager.py            # 记忆管理器（统一协调调度）
│   │   ├── embedding.py          # 统一嵌入服务（DashScope/Local/TFIDF）
│   │   ├── types/                # 记忆类型实现
│   │   │   ├── working.py        # 工作记忆（TTL管理，纯内存）
│   │   │   ├── episodic.py       # 情景记忆（事件序列，SQLite+Qdrant）
│   │   │   ├── semantic.py       # 语义记忆（知识图谱，Qdrant+Neo4j）
│   │   │   └── perceptual.py     # 感知记忆（多模态，SQLite+Qdrant）
│   │   ├── storage/              # 存储后端实现
│   │   │   ├── qdrant_store.py   # Qdrant向量存储（高性能向量检索）
│   │   │   ├── neo4j_store.py    # Neo4j图存储（知识图谱管理）
│   │   │   └── document_store.py # SQLite文档存储（结构化持久化）
│   │   └── rag/                  # RAG系统
│   │       ├── pipeline.py       # RAG管道（端到端处理）
│   │       └── document.py       # 文档处理器（多格式解析）
│   └── tools/builtin/            # 扩展内置工具
│       ├── memory_tool.py        # 记忆工具（Agent记忆能力）
│       └── rag_tool.py           # RAG工具（智能问答能力）
└──
```

<strong>快速开始：安装HelloAgents框架</strong>

为了让读者能够快速体验本章的完整功能，我们提供了可直接安装的Python包。你可以通过以下命令安装本章对应的版本：

```bash
# 0.2.0版本若遇到模型不可用，查看issue#320或切换0.2.9版本进行测试
pip install "hello-agents[all]==0.2.0"
python -m spacy download zh_core_web_sm
python -m spacy download en_core_web_sm
```

除此之外，还需要在`.env`配置图数据库，向量数据库，LLM以及Embedding方案的API。在教程中向量数据库采用Qdrant，图数据库采用Neo4J，Embedding首选百炼平台，若没有API可切换为本地部署模型方案。

```bash
# ================================
# Qdrant 向量数据库配置 - 获取API密钥：https://cloud.qdrant.io/
# ================================
# 使用Qdrant云服务 (推荐)
QDRANT_URL=https://your-cluster.qdrant.tech:6333
QDRANT_API_KEY=your_qdrant_api_key_here

# 或使用本地Qdrant (需要Docker)
# QDRANT_URL=http://localhost:6333
# QDRANT_API_KEY=

# Qdrant集合配置
QDRANT_COLLECTION=hello_agents_vectors
QDRANT_VECTOR_SIZE=384
QDRANT_DISTANCE=cosine
QDRANT_


# FILE: docs/chapter1/Chapter1-Introduction-to-Agents.md

# Chapter 1: Introduction to Agents

Welcome to the world of agents! In today's era where the wave of artificial intelligence is sweeping across the globe, **Agents** have become one of the core concepts driving technological transformation and application innovation. Whether your aspiration is to become a researcher or engineer in the AI field, or you hope to deeply understand the cutting edge of technology as an observer, mastering the essence of agents will be an indispensable part of your knowledge system.

Therefore, in this chapter, let's return to the fundamentals and explore several questions together: What is an agent? What are its main types? How does it interact with the world we live in? Through these discussions, we hope to lay a solid foundation for your future learning and exploration.

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-0.png" alt="Figure description" width="90%"/>
  <p>Figure 1.1 Basic interaction loop between agent and environment</p>
</div>

## 1.1 What is an Agent?

When exploring any complex concept, it's best to start with a concise definition. In the field of artificial intelligence, an agent is defined as any entity that can perceive its **Environment** through **Sensors**, and **autonomously** take **Actions** through **Actuators** to achieve specific goals.

This definition contains four fundamental elements of an agent's existence. The environment is the external world in which the agent operates. For an autonomous vehicle, the environment is the dynamically changing road traffic; for a trading algorithm, the environment is the ever-changing financial market. The agent is not isolated from the environment—it continuously perceives the environmental state through its sensors. Cameras, microphones, radar, or data streams returned by various **Application Programming Interfaces (APIs)** are all extensions of its perceptual capabilities.

After acquiring information, the agent needs to take actions to influence the environment, changing its state through actuators. Actuators can be physical devices (such as robotic arms or steering wheels) or virtual tools (such as executing code or calling a service).

However, what truly endows an agent with "intelligence" is its **Autonomy**. An agent is not merely a program that passively responds to external stimuli or strictly executes preset instructions; it can make independent decisions based on its perceptions and internal state to achieve its design goals. This closed loop from perception to action forms the foundation of all agent behavior, as shown in Figure 1.1.

### 1.1.1 Agents from a Traditional Perspective

Before the current wave of **Large Language Models (LLMs)**, pioneers in artificial intelligence had already spent decades exploring and building the concept of "agents." These paradigms, which we now call "traditional agents," are not a single static concept but have undergone a clear evolutionary path from simple to complex, from passive reaction to active learning.

The starting point of this evolution is the structurally simplest **Simple Reflex Agent**. Their decision-making core consists of "condition-action" rules explicitly designed by engineers, as shown in Figure 1.2. A classic automatic thermostat works this way: if the sensor perceives that the room temperature is higher than the set value, it activates the cooling system.

This type of agent relies entirely on current perceptual input and has no memory or predictive capability. It's like a digitized instinct—reliable and efficient, but therefore unable to handle complex tasks that require understanding context. Its limitations raise a key question: What should an agent do if the current state of the environment is insufficient as the sole basis for decision-making?

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-1.png" alt="Figure description" width="90%"/>
  <p>Figure 1.2 Decision logic diagram of a simple reflex agent</p>
</div>

To answer this question, researchers introduced the concept of "state" and developed **Model-Based Reflex Agents**. This type of agent has an internal **World Model** used to track and understand aspects of the environment that cannot be directly perceived. It attempts to answer: "What is the world like now?" For example, an autonomous vehicle driving through a tunnel, even if its camera temporarily cannot perceive the vehicle ahead, its internal model will still maintain a judgment about that vehicle's existence, speed, and estimated position. This internal model gives the agent a primitive form of "memory," making its decisions no longer solely dependent on instantaneous perception but based on a more coherent and complete understanding of the world state.

However, merely understanding the world is not enough—an agent needs clear goals. This led to the development of **Goal-Based Agents**. Unlike the previous two types, their behavior is no longer passively reacting to the environment but actively and proactively selecting actions that can lead to a specific future state. The question this type of agent needs to answer is: "What should I do to achieve my goal?" A classic example is a GPS navigation system: your goal is to reach the office, and the agent will plan an optimal route using search algorithms (such as A*) based on map data (world model). The core capability of this type of agent is reflected in its consideration and planning for the future.

Going further, real-world goals are often not singular. We not only want to reach the office but also want the shortest time, the most fuel-efficient route, and to avoid congestion. When multiple goals need to be balanced, **Utility-Based Agents** emerge. They assign a utility value to every possible world state, representing the level of satisfaction. The agent's core goal is no lon


# FILE: docs/chapter1/第一章 初识智能体.md

# 第一章 初识智能体

欢迎来到智能体的世界！在人工智能浪潮席卷全球的今天，<strong>智能体（Agent）</strong>已成为驱动技术变革与应用创新的核心概念之一。无论你的志向是成为 AI 领域的研究者、工程师，还是希望深刻理解技术前沿的观察者，掌握智能体的本质，都将是你知识体系中不可或缺的一环。

因此，在本章，让我们回到原点，一起探讨几个问题：智能体是什么？它有哪些主要的类型？它又是如何与我们所处的世界进行交互的？通过这些讨论，希望能为你未来的学习和探索打下坚实的基础。

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-0.png" alt="图片描述" width="90%"/>
  <p>图 1.1 智能体与环境的基本交互循环</p>
</div>

## 1.1 什么是智能体？

在探索任何一个复杂概念时，我们最好从一个简洁的定义开始。在人工智能领域，智能体被定义为任何能够通过<strong>传感器（Sensors）</strong>感知其所处<strong>环境（Environment）</strong>，并<strong>自主</strong>地通过<strong>执行器（Actuators）</strong>采取<strong>行动（Action）</strong>以达成特定目标的实体。

这个定义包含了智能体存在的四个基本要素。环境是智能体所处的外部世界。对于自动驾驶汽车，环境是动态变化的道路交通；对于一个交易算法，环境则是瞬息万变的金融市场。智能体并非与环境隔离，它通过其传感器持续地感知环境状态。摄像头、麦克风、雷达或各类<strong>应用程序编程接口（Application Programming Interface, API）</strong>返回的数据流，都是其感知能力的延伸。

获取信息后，智能体需要采取行动来对环境施加影响，它通过执行器来改变环境的状态。执行器可以是物理设备（如机械臂、方向盘）或虚拟工具（如执行一段代码、调用一个服务）。

然而，真正赋予智能体"智能"的，是其<strong>自主性（Autonomy）</strong>。智能体并非只是被动响应外部刺激或严格执行预设指令的程序，它能够基于其感知和内部状态进行独立决策，以达成其设计目标。这种从感知到行动的闭环，构成了所有智能体行为的基础，如图 1.1 所示。


### 1.1.1 传统视角下的智能体

在当前<strong>大语言模型（Large Language Model, LLM）</strong>的热潮出现之前，人工智能的先驱们已经对“智能体”这一概念进行了数十年的探索与构建。这些如今我们称之为“传统智能体”的范式，并非单一的静态概念，而是经历了一条从简单到复杂、从被动反应到主动学习的清晰演进路线。

这个演进的起点，是那些结构最简单的<strong>反射智能体（Simple Reflex Agent）</strong>。它们的决策核心由工程师明确设计的“条件-动作”规则构成，如图 1.2 所示。经典的自动恒温器便是如此：若传感器感知的室温高于设定值，则启动制冷系统。

这种智能体完全依赖于当前的感知输入，不具备记忆或预测能力。它像一种数字化的本能，可靠且高效，但也因此无法应对需要理解上下文的复杂任务。它的局限性引出了一个关键问题：如果环境的当前状态不足以作为决策的全部依据，智能体该怎么办？

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-1.png" alt="图片描述" width="90%"/>
  <p>图 1.2 简单反射智能体的决策逻辑示意图</p>
</div>

为了回答这个问题，研究者们引入了“状态”的概念，发展出<strong>基于模型的反射智能体（Model-Based Reflex Agent）</strong>。这类智能体拥有一个内部的<strong>世界模型（World Model）</strong>，用于追踪和理解环境中那些无法被直接感知的方面。它试图回答：“世界现在是什么样子的？”。例如，一辆在隧道中行驶的自动驾驶汽车，即便摄像头暂时无法感知到前方的车辆，它的内部模型依然会维持对那辆车存在、速度和预估位置的判断。这个内部模型让智能体拥有了初级的“记忆”，使其决策不再仅仅依赖于瞬时感知，而是基于一个更连贯、更完整的世界状态理解。

然而，仅仅理解世界还不够，智能体需要有明确的目标。这促进了<strong>基于目标的智能体（Goal-Based Agent）</strong>的发展。与前两者不同，它的行为不再是被动地对环境做出反应，而是主动地、有预见性地选择能够导向某个特定未来状态的行动。这类智能体需要回答的问题是：“我应该做什么才能达成目标？”。经典的例子是 GPS 导航系统：你的目标是到达公司，智能体会基于地图数据（世界模型），通过搜索算法（如 A*算法）来规划（Planning）出一条最优路径。这类智能体的核心能力体现在了对未来的考量与规划上。

更进一步，现实世界的目标往往不是单一的。我们不仅希望到达公司，还希望时间最短、路程最省油并且避开拥堵。当多个目标需要权衡时，<strong>基于效用的智能体（Utility-Based Agent）</strong>便随之出现。它为每一个可能的世界状态都赋予一个效用值，这个值代表了满意度的高低。智能体的核心目标不再是简单地达成某个特定状态，而是最大化期望效用。它需要回答一个更复杂的问题：“哪种行为能为我带来最满意的结果？”。这种架构让智能体学会在相互冲突的目标之间进行权衡，使其决策更接近人类的理性选择。

至此，我们讨论的智能体虽然功能日益复杂，但其核心决策逻辑，无论是规则、模型还是效用函数，依然依赖于人类设计师的先验知识。如果智能体能不依赖预设，而是通过与环境的互动自主学习呢？

这便是<strong>学习型智能体（Learning Agent）</strong>的核心思想，而<strong>强化学习（Reinforcement Learning, RL）</strong>是实现这一思想最具代表性的路径。一个学习型智能体包含一个性能元件（即我们前面讨论的各类智能体）和一个学习元件。学习元件通过观察性能元件在环境中的行动所带来的结果来不断修正性能元件的决策策略。

想象一个学习下棋的 AI。它开始时可能只是随机落子，当它最终赢下一局时，系统会给予它一个正向的奖励。通过大量的自我对弈，学习元件会逐渐发现哪些棋路更有可能导向最终的胜利。AlphaGo Zero 是这一理念的一个里程碑式的成就。它在围棋这一复杂博弈中，通过强化学习发现了许多超越人类既有知识的有效策略。

从简单的恒温器，到拥有内部模型的汽车，再到能够规划路线的导航、懂得权衡利弊的决策者，最终到可以通过经验自我进化的学习者。这条演进之路，展示了传统人工智能在构建机器智能的道路上所经历的发展脉络。它们为我们今天理解更前沿的智能体范式，打下了坚实而必要的基础。

### 1.1.2 大语言模型驱动的新范式

以<strong>GPT（Generative Pre-trained Transformer）</strong>为代表的大语言模型的出现，正在显著改变智能体的构建方法与能力边界。由大语言模型驱动的 LLM 智能体，其核心决策机制与传统智能体存在本质区别，从而赋予了其一系列全新的特性。

这种转变，可以从两者在核心引擎、知识来源、交互方式等多个维度的对比中清晰地看出，如表 1.1 所示。简而言之，传统智能体的能力源于工程师的显式编程与知识构建，其行为模式是确定且有边界的；而 LLM 智能体则通过在海量数据上的预训练，获得了隐式的世界模型与强大的涌现能力，使其能够以更灵活、更通用的方式应对复杂任务。

<div align="center">
  <p>表 1.1 传统智能体与 LLM 驱动智能体的核心对比</p>
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-2.png" alt="图片描述" width="90%"/>
</div>

这种差异使得 LLM 智能体可以直接处理高层级、模糊且充满上下文信息的自然语言指令。让我们以一个“智能旅行助手”为例来说明。

在 LLM 智能体出现之前，规划旅行通常意味着用户需要在多个专用应用（如天气、地图、预订网站）之间手动切换，并由用户自己扮演信息整合与决策的角色。而一个 LLM 智能体则能将这个流程整合起来。当接收到“规划一次厦门之旅”这样的模糊指令时，它的工作方式体现了以下几点：

- <strong>规划与推理</strong>：智能体首先会将这个高层级目标分解为一系列逻辑子任务，例如：`[确认出行偏好] -> [查询目的地信息] -> [制定行程草案] -> [预订票务住宿]`。这是一个内在的、由模型驱动的规划过程。
- <strong>工具使用</strong>：在执行规划时，智能体识别到信息缺口，会主动调用外部工具来补全。例如，它会调用天气查询接口获取实时天气，并基于“预报有雨”这一信息，在后续规划中倾向于推荐室内活动。
- <strong>动态修正</strong>：在交互过程中，智能体会将用户的反馈（如“这家酒店超出预算”）视为新的约束，并据此调整后续的行动，重新搜索并推荐符合新要求的选项。整个“<strong>查天气 → 调行程 → 订酒店</strong>”的流程，展现了其根据上下文动态修正自身行为的能力。

总而言之，我们正从开发专用自动化工具转向构建能自主解决问题的系统。核心不再是编写代码，而是引导一个通用的“大脑”去规划、行动和学习。

### 1.1.3 智能体的类型

继上文回顾智能体的演进后，本节将从三个互补的维度对智能体进行分类。

（1）<strong>基于内部决策架构的分类</strong>

第一种分类维度是依据智能体内部决策架构的复杂程度，这个视角在《Artificial Intelligence: A Modern Approach》中系统性地提出<sup>[1]</sup>。正如 1.1.1 节所述，传统智能体的演进路径本身就构成了最经典的分类阶梯，它涵盖了从简单的<strong>反应式</strong>智能体，到引入内部模型的<strong>模型式</strong>智能体，再到更具前瞻性的<strong>基于目标</strong>和<strong>基于效用</strong>的智能体。此外，<strong>学习能力</strong>则是一种可赋予上述所有类型的元能力，使其能通过经验自我改进。

（2）<strong>基于时间与反应性的分类</strong>

除了内部架构的复杂性，还可以从智能体处理决策的时间维度进行分类。这个视角关注智能体是在接收到信息后立即行动，还是会经过深思熟虑的规划再行动。这揭示了智能体设计中一个核心权衡：追求速度的<strong>反应性（Reactivity）</strong>与追求最优解的<strong>规划性（Deliberation）</strong>之间的平衡，如图 1.3 所示。

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/1-figures/1757242319667-3.png" alt="图片描述" width="90%"/>
  <p>图 1.3 智能体决策时间与质量关系图</p>
</div>

- <strong>反应式智能体 (Reactive Agents)</strong>

这类智能体对环境刺激做出近乎即时的响应，决策延迟极低。它们通常遵循从感知到行动的直接映射，不进行或只进行极少的未来规划。上文的<strong>简单反应式</strong>和<strong>基于模型</strong>的智能体都属于此类别。

其核心优势在于<strong>速度快、计算开销低</strong>，这在需要快速决策的动态环境中至关重要。例如，车辆的安全气囊系统必须在碰撞发生的毫秒内做出反应，任何延迟都可能导致严重后果；同样，高频交易机器人也必须依赖反应式决策来捕捉稍纵即逝的市场机会。然而，这种速度的代价是“短视”，由于缺乏长远规划，反应式智能体容易陷入局部最优，难以完成需要多步骤协调的复杂任务。

- <strong>规划式智能体(Deliberative Agents)</strong>

与反应式智能体相对，规划式（或称审议式）智能体在行动前会进行复杂的思考和规划。它们不会立即对感知做出反应，而是会先利用其内部的世界模型，系统地探索未来的各种可能性，评估不同行动序列的后果，以期找到一条能够达成目标的最佳路径 。<strong>基于目标</strong>和<strong>基于效用</strong>的智能体是典型的规划式智能体。

可以将其决策过程类比为一位棋手。他不会只看眼前的一步，而是会预想对手可能的应对，并规划出后续几步甚至十几步的棋路。这种深思熟虑的能力使其能够处理复杂的、需要长远眼光的任务，例如制定一份商业计划或规划一次长途旅行。它们的优势在于决策的战略性和远见。然而，这种优势的另一面是高昂的时间和计算成本。在瞬息万变的环境中，当规划式智能体还在深思熟虑时，采取行动的最佳时机可能早已过去。

- <strong>混合式智能体(Hybrid Agents)</strong>

现实世界的复杂任务，往往既需要即时反应，也需要长远规划。例如，我们之前提到的智能旅行助手，既要能根据用户的即时反馈（如
