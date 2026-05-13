# Missing Repo Summary Source: datawhalechina/hello-agents

- URL: https://github.com/datawhalechina/hello-agents
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents
- Clone Status: cloned
- Language: Python
- Stars: 48290
- Topics: agent, llm, rag, tutorial
- Description: 📚 《从零开始构建智能体》——从零开始的智能体原理与实践教程

## Extracted README / Docs / Examples



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
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [00-共创毕业设计](https://github.com/datawhalechina/hello-agents/blob/main/Co-creation-projects)                                             | 社区共创毕业设计项目      |
| [01-Agent面试题总结](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-面试问题总结.md)                          | Agent 岗位相关面试问题    |
| [01-Agent面试题答案](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-参考答案.md)                              | 相关面试问题答案          |
| [02-上下文工程内容补充](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra02-上下文工程补充知识.md)                 | 上下文工程内容扩展        |
| [03-Dify智能体创建保姆级教程](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra03-Dify智能体创建保姆级操作流程.md) | Dify智能体创建保姆级教程  |
| [04-Hello-agents课程常见问题](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra04-DatawhaleFAQ.md)                 | Datawhale课程常见问题     |
| [05-Agent Skills与MCP对比解读](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra05-AgentSkills解读.md)             | Agent Skills与MCP技术对比 |
| [06-GUI Agent科普与实战](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra06-GUIAgent科普与实战.md)                | GUI Agent科普与多场景实战 |
| [07-环境配置](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra07-环境配置.md)                | 环境配置 |
| [08-如何写出好的Skill](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra08-如何写出好的Skill.md) | Skill 写作最佳实践 |
| [09-Agent应用开发实践踩坑与经验分享](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra09-Agent应用开发实践踩坑与经验分享.md) | Code Agent 应用开发踩坑与经验总结 |
| [10-Agent Self-Evolution智能体自进化](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra10-Agent自进化.md) | Agent 自进化四类闭环与代表项目 |

### PDF 版本下载

&emsp;&emsp;*<strong>本 Hello-Agents PDF 教程完全开源免费。为防止各类营销号加水印后贩卖给多智能体系统初学者，我们特地在 PDF 文件中预先添加了不影响阅读的 Datawhale 开源标志水印，敬请谅解～</strong>*

> *Hello-Agents PDF : https://github.com/datawhalechina/hello-agents/releases/latest/*  
> *Hello-Agents PDF 国内下载地址 : https://www.datawhale.cn/learn/summary/239* 

## 💡 如何学习

&emsp;&emsp;欢迎你，未来的智能系统构建者！在开启这段激动人心的旅程之前，请允许我们给你一些清晰的指引。

&emsp;&emsp;本项目内容兼顾理论与实战，旨在帮助你系统性地掌握从单个智能体到多智能体系统的设计与开发全流程。因此，尤其适合有一定编程基础的 <strong>AI 开发者、软件工程师、在校学生</strong> 以及对前沿 AI 技术抱有浓厚兴趣的 <strong>自学者</strong>。在学习本项目之前，我们希望你具备基础的 Python 编程能力，并对大语言模型有基本的概念性了解（例如，知道如何通过 API 调用一个 LLM）。项目的重点是应用与构建，因此你无需具备深厚的算法或模型训练背景。

&emsp;&emsp;项目分为五大部分，每一部分都是通往下一阶段的坚实阶梯：

- <strong>第一部分：智能体与语言模型基础</strong>（第一章～第三章），我们将从智能体的定义、类型与发展历史讲起，为你梳理"智能体"这一概念的来龙去脉。随后，我们会快速巩固大语言模型的核心知识，为你的实践之旅打下坚实的理论地基。

- <strong>第二部分：构建你的大语言模型智能体</strong>（第四章～第七章），这是你动手实践的起点。你将亲手实现 ReAct 等经典范式，体验 Coze 等低代码平台的便捷，并掌握 Langgraph 等主流框架的应用。最终，我们还会带你从零开始构建一个属于自己的智能体框架，让你兼具“用轮子”与“造轮子”的能力。

- <strong>第三部分：高级知识扩展</strong>（第八章～第十二章），在这一部分，你的智能体将“学会”思考与协作。我们将使用第二部分的自研框架，深入探索记忆与检索、上下文工程、Agent 训练等核心技术，并学习多智能体间的通信协议。最终，你将掌握评估智能体系统性能的专业方法。

- <strong>第四部分：综合案例进阶</strong>（第十三章～第十五章），这里是理论与实践的交汇点。你将把所学融会贯通，亲手打造智能旅行助手、自动化深度研究智能体，乃至一个模拟社会动态的赛博小镇，在真实有趣的项目中淬炼你的构建能力。

- <strong>第五部分：毕业设计及未来展望</strong>（第十六章），在旅程的终点，你将迎来一个毕业设计，构建一个完整的、属于你自己的多智能体应用，全面检验你的学习成果。我们还将与你一同展望智能体的未来，探索激动人心的前沿方向。


&emsp;&emsp;智能体是一个飞速发展且极度依赖实践的领域。为了获得最佳的学习效果，我们在项目的`code`文件夹内提供了配套的全部代码，强烈建议你<strong>将理论与实践相结合</strong>。请务必亲手运行、调试甚至修改项目里提供的每一份代码。欢迎你随时关注 Datawhale 以及其他 Agent 相关社区，当遇到问题时，你可以随时在本项目的 issue 区提问。

&emsp;&emsp;现在，准备好进入智能体的奇妙世界了吗？让我们即刻启程！

## 下一步规划

- 视频课程陆续放出（将会更加细致，实践课带领大家从设计思路到实施，授人以鱼也授人以渔）
- HelloAgents框架已经更新V1.0.0版本，将会继续完善，增加更多好用，轻量化的工具和特性，兼容学习版本。
- 感谢大家助力4W Star! 现在提供调查问卷，供大家填写自己需要学习的智能体内容。后续作品《从零开始训练智能体》，帮助每一个学习者掌握从零到一训练自定义场景智能体模型的能力。
<div align='center'>
    <img src="./读者反馈问卷.png" alt="读者反馈问卷" width="30%">
    <p>扫描二维码填写反馈意见，助力新项目共同成长</p>
</div>

## 🤝 如何贡献

我们是一个开放的开源社区，欢迎任何形式的贡献！

- 🐛 <strong>报告 Bug</strong> - 发现内容或代码问题，请提交 Issue
- 💡 <strong>提出建议</strong> - 对项目有好想法，欢迎发起讨论
- 📝 <strong>完善内容</strong> - 帮助改进教程，提交你的 Pull Request
- ✍️ <strong>分享实践</strong> - 在"社区贡献精选"中分享你的学习笔记和项目

## 🙏 致谢

### 核心贡献者


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
| [Chapter 4: Classic Agent Paradigm Construction](./docs/chapter4/Chapter4-Building-Classic-Agent-Paradigms.md)        | Hands-on implementation of ReAct, Plan-and-Solve, Reflection               | ✅      |
| [Chapter 5: Low-Code Platform Agent Development](./docs/chapter5/Chapter5-Building-Agents-with-Low-Code-Platforms.md) | Understanding Coze, Dify, n8n and other low-code agent platforms           | ✅      |
| [Chapter 6: Framework Development Practice](./docs/chapter6/Chapter6-Framework-Development-Practice.md)               | AutoGen, AgentScope, LangGraph and other mainstream framework applications | ✅      |
| [Chapter 7: Building Your Agent Framework](./docs/chapter7/Chapter7-Building-Your-Agent-Framework.md)                 | Building an agent framework from scratch                                   | ✅      |
| **Part 3: Advanced Knowledge Extension**                                                                              |                                                                            |        |
| [Chapter 8: Memory and Retrieval](./docs/chapter8/Chapter8-Memory-and-Retrieval.md)                                   | Memory systems, RAG, storage                                               | ✅      |
| [Chapter 9: Context Engineering](./docs/chapter9/Chapter9-Context-Engineering.md)                                     | "Contextual understanding" for continuous interaction                      | ✅      |
| [Chapter 10: Agent Communication Protocols](./docs/chapter10/Chapter10-Agent-Communication-Protocols.md)              | MCP, A2A, ANP and other protocol analysis                                  | ✅      |
| [Chapter 11: Agentic-RL](./docs/chapter11/Chapter11-Agentic-RL.md)                                                    | Practical LLM training from SFT to GRPO                                    | ✅      |
| [Chapter 12: Agent Performance Evaluation](./docs/chapter12/Chapter12-Agent-Performance-Evaluation.md)                | Core metrics, benchmarks, and evaluation frameworks                        | ✅      |
| **Part 4: Comprehensive Case Studies**                                                                                |                                                                            |        |
| [Chapter 13: Intelligent Travel Assistant](./docs/chapter13/Chapter13-Intelligent-Travel-Assistant.md)                | Real-world applications of MCP and multi-agent collaboration               | ✅      |
| [Chapter 14: Automated Deep Research Agent](./docs/chapter14/Chapter14-Automated-Deep-Research-Agent.md)              | DeepResearch Agent reproduction and analysis                               | ✅      |
| [Chapter 15: Building a Cyber Town](./docs/chapter15/Chapter15-Building-Cyber-Town.md)                                | Combining agents with games, simulating social dynamics                    | ✅      |
| **Part 5: Capstone Project and Future Outlook**                                                                       |                                                                            |        |
| [Chapter 16: Capstone Project](./docs/chapter16/Chapter16-Graduation-Project.md)                                      | Build your own complete multi-agent application                            | ✅      |

### Community Contributions

&emsp;&emsp;We welcome everyone to contribute their unique insights and practical summaries from learning Hello-Agents or Agent-related technologies to the community selection in the form of PRs. If the content is independent of the main text, you can also submit it to Extra-Chapter! **Looking forward to your first contribution!**

| Community Selection                                                                                                                                            | Content Summary                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [00-Co-creation Capstone Projects](https://github.com/datawhalechi

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

# FILE: docs/chapter6/第六章 框架开发实践.md

# 第六章 框架开发实践

在第四章中，我们通过编写原生代码，实现了 ReAct、Plan-and-Solve 和 Reflection 这几种智能体的核心工作流。这个过程让我们对智能体的内在执行逻辑有了理解。随后，在第五章，我们切换到“使用者”的视角，体验了低代码平台带来的便捷与高效。

本章的目标，就是探讨如何利用业界主流的一些<strong>智能体框架</strong>，来高效、规范地构建可靠的智能体应用。我们将首先概览当前市面上主流的智能体框架，然后并对几个具有代表性的框架，通过一个完整的实战案例，来体验框架驱动的开发模式。

## 6.1 从手动实现到框架开发

从编写一次性的脚本到使用一个成熟的框架，是软件工程领域一次重要的思维跃迁。我们在第四章中编写的代码，其主要目的是为了教学和理解。它们能很好地完成特定任务，但如果要用它们来构建多个、不同类型且逻辑复杂的智能体应用，很快就会遇到瓶颈。

一个框架的本质，是提供一套经过验证的“规范”。它将所有智能体共有的、重复性的工作（如主循环、状态管理、工具调用、日志记录等）进行抽象和封装，让我们在构建新的智能体时，能够专注于其独特的业务逻辑，而非通用的底层实现。

### 6.1.1 为何需要智能体框架

在我们开始实战之前，首先需要明确为什么要使用框架。相比于直接编写独立的智能体脚本，使用框架的价值主要体现在以下几个方面：

1. <strong>提升代码复用与开发效率</strong>：这是最直接的价值。一个好的框架会提供一个通用的 `Agent` 基类或执行器，它封装了智能体运行的核心循环（Agent Loop）。无论是 ReAct 还是 Plan-and-Solve，都可以基于框架提供的标准组件快速搭建，从而避免重复劳动。
2. <strong>实现核心组件的解耦与可扩展性</strong>：一个健壮的智能体系统应该由多个松散耦合的模块组成。框架的设计会强制我们分离不同的关注点：
   - <strong>模型层 (Model Layer)</strong>：负责与大语言模型交互，可以轻松替换不同的模型（OpenAI, Anthropic, 本地模型）。
   - <strong>工具层 (Tool Layer)</strong>：提供标准化的工具定义、注册和执行接口，添加新工具不会影响其他代码。
   - <strong>记忆层 (Memory Layer)</strong>：处理短期和长期记忆，可以根据需求切换不同的记忆策略（如滑动窗口、摘要记忆）。 这种模块化的设计使得整个系统极具可扩展性，更换或升级任何一个组件都变得简单。
3. <strong>标准化复杂的状态管理</strong>：我们在 `ReflectionAgent` 中实现的 `Memory` 类只是一个简单的开始。在真实的、长时运行的智能体应用中，状态管理是一个巨大的挑战，它需要处理上下文窗口限制、历史信息持久化、多轮对话状态跟踪等问题。一个框架可以提供一套强大而通用的状态管理机制，开发者无需每次都重新处理这些复杂问题。
4. <strong>简化可观测性与调试过程</strong>：当智能体的行为变得复杂时，理解其决策过程变得至关重要。一个精心设计的框架可以内置强大的可观测性能力。例如，通过引入事件回调机制（Callbacks），我们可以在智能体生命周期的关键节点（如 `on_llm_start`, `on_tool_end`, `on_agent_finish`）自动触发日志记录或数据上报，从而轻松地追踪和调试智能体的完整运行轨迹。这远比在代码中手动添加 `print` 语句要高效和系统化。

因此，从手动实现走向框架开发，不仅是代码组织方式的改变，更是构建复杂、可靠、可维护的智能体应用的必由之路。

### 6.1.2 主流框架的选型与对比

智能体框架的生态正在以前所未有的速度发展。如果说 LangChain 和 LlamaIndex 定义了第一代通用 LLM 应用框架的范式，那么新一代的框架则更加专注于解决特定领域的深层挑战，尤其是<strong>多智能体协作 (Multi-Agent Collaboration)</strong> 和 <strong>复杂工作流控制 (Complex Workflow Control)</strong>。

在本章的后续实战中，我们将聚焦于四个在这些前沿领域极具代表性的框架：AutoGen、AgentScope、CAMEL 和 LangGraph。它们的设计理念各不相同，分别代表了实现复杂智能体系统的不同技术路径，如表6.1所示。

<div align="center">
  <p>表 6.1 四种智能体框架对比</p>
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/6-figures/01.png" alt="" width="90%"/>
</div>


- <strong>AutoGen</strong>：AutoGen 的核心思想是通过对话实现协作<sup>[1]</sup>。它将多智能体系统抽象为一个由多个“可对话”智能体组成的群聊。开发者可以定义不同角色（如 `Coder`, `ProductManager`, `Tester`），并设定它们之间的交互规则（例如，`Coder` 写完代码后由 `Tester` 自动接管）。任务的解决过程，就是这些智能体在群聊中通过自动化消息传递，不断对话、协作、迭代直至最终目标达成的过程。
- <strong>AgentScope</strong>：AgentScope 是一个专为多智能体应用设计的、功能全面的开发平台<sup>[2]</sup>。它的核心特点是<strong>易用性</strong>和<strong>工程化</strong>。它提供了一套非常友好的编程接口，让开发者可以轻松定义智能体、构建通信网络，并管理整个应用的生命周期。其内置的<strong>消息传递机制</strong>和对分布式部署的支持，使其非常适合构建和运维复杂、大规模的多智能体系统。
- <strong>CAMEL</strong>：CAMEL 提供了一种新颖的、名为<strong>角色扮演 (Role-Playing)</strong> 的协作方法<sup>[3]</sup>。其核心理念是，我们只需要为两个智能体（例如，`AI研究员` 和 `Python程序员`）设定好各自的角色和共同的任务目标，它们就能在“<strong>初始提示 (Inception Prompting)</strong>”的引导下，自主地进行多轮对话，相互启发、相互配合，共同完成任务。它极大地降低了设计多智能体对话流程的复杂度。
- <strong>LangGraph</strong>：作为 LangChain 生态的扩展，LangGraph 另辟蹊径，将智能体的执行流程建模为<strong>图 (Graph)</strong><sup>[4]</sup>。在传统的链式结构中，信息只能单向流动。而 LangGraph 将每一步操作（如调用LLM、执行工具）定义为图中的一个<strong>节点 (Node)</strong>，并用<strong>边 (Edge)</strong> 来定义节点之间的跳转逻辑。这种设计天然支持<strong>循环 (Cycles)</strong>，使得实现如 Reflection 这样的迭代、修正、自我反思的复杂工作流变得异常简单和直观。

在接下来的小节中，我们将对这四个框架，分别通过一个完整的实战案例，来深入体验框架驱动的开发模式。<strong>请注意</strong>，所有演示的项目源文件会放在`code`文件夹下，正文内只讲解原理部分。

## 6.2 框架一：AutoGen

正如前文所述，AutoGen 的设计哲学根植于"以对话驱动协作"。它巧妙地将复杂的任务解决流程，映射为不同角色的智能体之间的一系列自动化对话。基于这一核心理念，AutoGen 框架持续演进。我们将以 `0.7.4` 版本为例，因为它是截止目前为止最新版本，代表了一次重要的架构重构，从类继承设计转向了更灵活的组合式架构。为了深入理解并应用这一框架，我们首先需要讲解其最核心的构成要素与底层的对话交互机制。

### 6.2.1 AutoGen 的核心机制

`0.7.4` 版本的发布是 AutoGen 发展的一个重要节点，它标志着框架在底层设计上的一次根本性革新。这次更新并非简单的功能叠加，而是对整体架构的重新思考，旨在提升框架的模块化、并发性能和开发者体验。

<div align="center">
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/6-figures/02.png" alt="" width="90%"/>
  <p>图 6.1 AutoGen架构图</p>
</div>

（1）框架结构的演进

如图6.1所示，新架构最显著的变化是引入了清晰的分层和异步优先的设计理念。

- <strong>分层设计：</strong> 框架被拆分为两个核心模块：
  - `autogen-core`：作为框架的底层基础，封装了与语言模型交互、消息传递等核心功能。它的存在保证了框架的稳定性和未来扩展性。
  - `autogen-agentchat`：构建于 `core` 之上，提供了用于开发对话式智能体应用的高级接口，简化了多智能体应用的开发流程。 这种分层策略使得各组件职责明确，降低了系统的耦合度。
- <strong>异步优先：</strong> 新架构全面转向异步编程 (`async/await`)。在多智能体协作场景中，网络请求（如调用 LLM API）是主要耗时操作。异步模式允许系统在等待一个智能体响应时处理其他任务，从而避免了线程阻塞，显著提升了并发处理能力和系统资源的利用效率。

（2）核心智能体组件

智能体是执行任务的基本单元。在 `0.7.4` 版本中，智能体的设计更加专注和模块化。

- <strong>AssistantAgent (助理智能体)：</strong> 这是任务的主要解决者，其核心是封装了一个大型语言模型（LLM）。它的职责是根据对话历史生成富有逻辑和知识的回复，例如提出计划、撰写文章或编写代码。通过不同的系统消息（System Message），我们可以为其赋予不同的“专家”角色。
- <strong>UserProxyAgent (用户代理智能体)：</strong> 这是 AutoGen 中功能独特的组件。它扮演着双重角色：既是人类用户的“代言人”，负责发起任务和传达意图；又是一个可靠的“执行器”，可以配置为执行代码或调用工具，并将结果反馈给其他智能体。这种设计清晰地区分了“思考”（由 `AssistantAgent` 完成）与“行动”。

（3）从 GroupChatManager 到 Team

当任务需要多个智能体协作时，就需要一个机制来协调对话流程。在早期版本中，`GroupChatManager` 承担了这一职责。而在新架构中，引入了更灵活的 `Team` 或群聊概念，例如 `RoundRobinGroupChat`。

- <strong>轮询群聊 (RoundRobinGroupChat)：</strong> 这是一种明确的、顺序化的对话协调机制。它会让参与的智能体按照预定义的顺序依次发言。这种模式非常适用于流程固定的任务，例如一个典型的软件开发流程：产品经理先提出需求，然后工程师编写代码，最后由代码审查员进行检查。
- <strong>工作流：</strong>
  1. 首先，创建一个 `RoundRobinGroupChat` 实例，并将所有参与协作的智能体（如产品经理、工程师等）加入其中。
  2. 当一个任务开始时，群聊会按照预设的顺序，依次激活相应的智能体。
  3. 被选中的智能体根据当前的对话上下文进行响应。
  4. 群聊将新的回复加入对话历史，并激活下一个智能体。
  5. 这个过程会持续进行，直到达到最大对话轮次或满足预设的终止条件。

通过这种方式，AutoGen 将复杂的协作关系，简化为一个流程清晰、易于管理的自动化“圆桌会议”。开发者只需定义好每个团队成员的角色和发言顺序，剩下的协作流程便可由群聊机制自主驱动。

在下一节中，我们将通过构建一个模拟软件开发团队的实例，来亲身体验如何在新架构下定义不同角色的智能体，并将它们组织在一个由 `RoundRobinGroupChat` 协调的群聊中，以协作完成一个真实的编程任务。

### 6.2.2 软件开发团队

在理解了 AutoGen 的核心组件与对话机制后，本节将通过一个完整的实战案例来具体展示如何应用这些新特性。我们将构建一个模拟的软件开发团队，该团队由多个具有不同专业技能的智能体组成，它们将协作完成一个真实的软件开发任务。

（1）业务目标

我们的目标是开发一个功能明确的 Web 应用：<strong>实时显示比特币当前价格</strong>。这个任务虽小，却完整地覆盖了软件开发的典型环节：从需求分析、技术选型、编码实现到代码审查和最终测试。这使其成为检验 AutoGen 自动化协作流程的理想场景。

（2）智能体团队角色

为了模拟真实的软件开发流程，我们设计了四个职责分明的智能体角色：

- <strong>ProductManager (产品经理):</strong> 负责将用户的模糊需求转化为清晰、可执行的开发计划。
- <strong>Engineer (工程师):</strong> 依据开发计划，负责编写具体的应用程序代码。
- <strong>CodeReviewer (代码审查员):</strong> 负责审查工程师提交的代码，确保其质量、可读性和健壮性。
- <strong>UserProxy (用户代理):</strong> 代表最终用户，发起初始任务，并负责执行和验证最终交付的代码。

这种角色划分是多智能体系统设计中的关键一步，它将一个复杂任

# FILE: docs/chapter6/Chapter6-Framework-Development-Practice.md

# Chapter 6 Framework Development Practice

In Chapter 4, we implemented the core workflows of several agents such as ReAct, Plan-and-Solve, and Reflection by writing native code. This process gave us an understanding of the internal execution logic of agents. Subsequently, in Chapter 5, we switched to the "user" perspective and experienced the convenience and efficiency brought by low-code platforms.

The goal of this chapter is to explore how to use some mainstream **agent frameworks** in the industry to efficiently and standardly build reliable agent applications. We will first overview the current mainstream agent frameworks on the market, and then experience the framework-driven development model through a complete practical case for several representative frameworks.

## 6.1 From Manual Implementation to Framework Development

Moving from writing one-time scripts to using a mature framework is an important mental leap in the field of software engineering. The code we wrote in Chapter 4 was primarily for teaching and understanding purposes. They can complete specific tasks well, but if we want to use them to build multiple, different types of agents with complex logic, we will soon encounter bottlenecks.

The essence of a framework is to provide a set of validated "specifications." It abstracts and encapsulates all the repetitive work common to all agents (such as main loops, state management, tool invocation, logging, etc.), allowing us to focus on their unique business logic when building new agents, rather than general underlying implementations.

### 6.1.1 Why Agent Frameworks Are Needed

Before we start the practical work, we first need to clarify why we should use frameworks. Compared to directly writing independent agent scripts, the value of using frameworks is mainly reflected in the following aspects:

1. **Improve Code Reuse and Development Efficiency**: This is the most direct value. A good framework will provide a general `Agent` base class or executor that encapsulates the core loop of agent operation (Agent Loop). Whether it's ReAct or Plan-and-Solve, they can be quickly built based on standard components provided by the framework, thus avoiding repetitive work.
2. **Achieve Decoupling and Extensibility of Core Components**: A robust agent system should consist of multiple loosely coupled modules. The framework's design will force us to separate different concerns:
   - **Model Layer**: Responsible for interacting with large language models, can easily replace different models (OpenAI, Anthropic, local models).
   - **Tool Layer**: Provides standardized tool definition, registration, and execution interfaces; adding new tools will not affect other code.
   - **Memory Layer**: Handles short-term and long-term memory, can switch different memory strategies according to needs (such as sliding window, summary memory). This modular design makes the entire system highly extensible, making it simple to replace or upgrade any component.
3. **Standardize Complex State Management**: The `Memory` class we implemented in `ReflectionAgent` is just a simple start. In real, long-running agent applications, state management is a huge challenge that needs to handle context window limitations, historical information persistence, multi-turn conversation state tracking, and other issues. A framework can provide a powerful and general state management mechanism, so developers don't have to deal with these complex issues every time.
4. **Simplify Observability and Debugging Process**: When agent behavior becomes complex, understanding its decision-making process becomes crucial. A well-designed framework can have built-in powerful observability capabilities. For example, by introducing an event callback mechanism (Callbacks), we can automatically trigger logging or data reporting at key nodes in the agent lifecycle (such as `on_llm_start`, `on_tool_end`, `on_agent_finish`), making it easy to track and debug the complete running trajectory of the agent. This is far more efficient and systematic than manually adding `print` statements in code.

Therefore, moving from manual implementation to framework development is not only a change in code organization, but also the necessary path to building complex, reliable, and maintainable agent applications.

### 6.1.2 Selection and Comparison of Mainstream Frameworks

The ecosystem of agent frameworks is developing at an unprecedented speed. If LangChain and LlamaIndex defined the paradigm of the first generation of general LLM application frameworks, then the new generation of frameworks is more focused on solving deep challenges in specific domains, especially **Multi-Agent Collaboration** and **Complex Workflow Control**.

In the subsequent practical work of this chapter, we will focus on four frameworks that are highly representative in these cutting-edge fields: AutoGen, AgentScope, CAMEL, and LangGraph. Their design philosophies are different, representing different technical paths for implementing complex agent systems, as shown in Table 6.1.

<div align="center">
  <p>Table 6.1 Comparison of Four Agent Frameworks</p>
  <img src="https://raw.githubusercontent.com/datawhalechina/Hello-Agents/main/docs/images/6-figures/01.png" alt="" width="90%"/>
</div>


- **AutoGen**: The core idea of AutoGen is to achieve collaboration through conversation<sup>[1]</sup>. It abstracts multi-agent systems as a group chat composed of multiple "conversable" agents. Developers can define different roles (such as `Coder`, `ProductManager`, `Tester`) and set interaction rules between them (for example, after `Coder` finishes writing code, `Tester` automatically takes over). The task-solving process is the process where these agents continuously converse, collaborate, and iterate in the group chat through automated message passing until the final goal is achieved.
- **AgentScope**: AgentScope is a fully functional development platform designed specifically for mult
