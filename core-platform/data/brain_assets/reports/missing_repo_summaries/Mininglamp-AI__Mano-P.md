# Missing Repo Summary Source: Mininglamp-AI/Mano-P

- URL: https://github.com/Mininglamp-AI/Mano-P
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/Mininglamp-AI__Mano-P
- Clone Status: cloned
- Language: None
- Stars: 1895
- Topics: computer-use-agents, desktop-automation, edge-computing, gui-automation, gui-grounding, local-inference, mano, mano-p, multimodal-ai, on-device-ai, osworld, vision-language-action, visual-language-model
- Description: Mano-P: Open-source GUI-VLA agent for edge devices. #1 on OSWorld (specialized, 58.2%). Runs locally on Apple M4 Mac mini/MacBook — no data leaves your device.Mano-P 是一个开源 GUI-VLA 项目，支持在 Mac mini/MacBook 上或通过算力棒本地运行推理，实现纯视觉驱动的跨平台 GUI 自动化操作。数据完全本地处理，支持复杂多步骤任务规划与执行。

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">
    <h1>
      <img src="./pics/logo.png" alt="Mano-P Logo" height="60" style="vertical-align: -15px;">
      Mano-P 1.0
    </h1>
    <p><strong>GUI-Aware Agent Model for Edge Devices</strong></p>
    <p><strong>Private AI</strong></p>
</div>

<hr>

<div align="center">

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Mininglamp-AI/Mano-P?style=social)](https://github.com/Mininglamp-AI/Mano-P)
[![Paper](https://img.shields.io/badge/arXiv-Technical%20Report-red?logo=arxiv)](https://arxiv.org/abs/2509.17336)

<a href="README_CN.md">中文</a> | English

**[📖 Overview](#-overview) | [🎯 Key Highlights](#-key-highlights) | [🎬 Use Cases](#-use-case-demonstrations) | [📊 Benchmark](#-benchmark-performance) | [🔧 Skills](#-skills) | [🤖 Models](#-models) | [⚡ Inference SDK](#-inference-sdk) | [⚗️ Approach](#-approach) | [🌟 Technical Advantages](#-technical-advantages) | [🔗 Applications](#-applications) | [📄 Citation](#-technical-papers--citation) | [❓ FAQ](#-faq)**

</div>

---

<div align="center">
  <a href="https://ccnt9oddmvfr.feishu.cn/wiki/QUwbwmUwriHdL4kkyqPcWNaPn9c" target="_blank">
    <img src="pics/Benchmark_Overview.png" alt="GUI Agent Grounding Benchmark" style="max-width: 100%; height: auto;">
  </a>
</div>

---

## 📖 Overview

**Mano-P**: "Mano" means "hand" in Spanish, and "P" stands for Private. We believe that both individuals and organizations can create their own Private AI, and a bright future of human-machine collaboration is on the horizon.

![opensource_architecture.png](pics/opensource_architecture_en.png)

**Mano-P** is a GUI-VLA agent project designed specifically for edge devices. It serves both as an open-source project and a hardware product solution.
As an open-source project, Mano-P is being released in a phased, progressive manner, targeting three distinct groups of developers. In the first phase, we will open-source the Mano-CUA Skills. This phase is aimed at Agent enthusiasts—such as users of OpenClaw or Claude Code—enabling them to leverage the capabilities of Mano-CUA Skills to construct more intelligent CUA task workflows and overcome the bottlenecks associated with human intervention. In the second phase, we will open-source the local-side models and SDK components of Mano-CUA. This phase targets developers with high security requirements, allowing them to directly utilize GUI-VLA models capable of running inference locally on a Mac mini to build their own custom Skills, Tools, and more; **crucially, all your CUA operations will be executed entirely on your local Mac mini and will not be uploaded to external servers.** In the third phase, we will open-source the training methodologies and the pruning and quantization techniques used for the Mano-P models. This phase is designed for developers with specific model training needs, empowering them to apply our training methods to create their own on-device GUI-VLA models tailored to their unique requirements.

Regarding our GUI-VLA models—which are capable of running inference directly on Mac mini and MacBook devices—we currently support two deployment methods: First, direct deployment on Mac mini or MacBook models equipped with an M4 chip and 32GB or more of RAM; and second, deployment utilizing a compute stick connected via a USB 4.0 port or higher. We will be releasing detailed instructions for both deployment methods in the near future, and we plan to expand our support to include additional deployment options in the future.

### Main Capabilities

- **Complex GUI Automation**: Autonomously complete complex interface operations containing hundreds of interactive elements
- **Cross-System Data Integration**: Extract and integrate multi-source data through pure visual interaction without API interfaces
- **Long-Task Planning Execution**: Support enterprise-level business process automation of dozens to hundreds of steps
- **Intelligent Report Generation**: Automatically generate structured documents such as data analysis reports and work summaries
- **Edge-Native Inference**: Efficient on-device execution on Apple Silicon via INT8 activation quantization ([Cider](#-inference-sdk))
- **Autonomous Application Construction**: Drives end-to-end software construction pipelines through visual GUI operation ([Mano-AFK](#-applications))

### Technical Background

Mano-P builds upon the complete technical framework of the Mano project (see [Mano Technical Report](https://arxiv.org/abs/2509.17336)), employing the Mano-Action bidirectional self-reinforcement learning method, three-stage progressive training (SFT → Offline Reinforcement Learning → Online Reinforcement Learning), "think-act-verify" loop reasoning mechanism, and a closed-loop data circulation system to achieve high-precision GUI understanding and operation capabilities. The edge version is optimized through mixed-precision quantization, visual token pruning, and edge inference adaptation, enabling large-scale parameter models to run efficiently on edge devices like Mac mini/MacBook/computing sticks.

## 🎯 Key Highlights

- **#1 on OSWorld Benchmark**: Mano-P 1.0-72B achieves **58.2% success rate on OSWorld**, ranking first among all specialized GUI agent models, outperforming the second-place opencua-72b (45.0%) by 13.2 percentage points
- **Leading on WebRetriever Protocol I**: Mano-P 1.0 scores **41.7 NavEval**, surpassing Gemini 2.5 Pro Computer Use (40.9) and Claude 4.5 Computer Use (31.3)
- **Fully Local Execution**: Runs inference locally on **Apple M4 chip with 32GB RAM** (Mac mini or MacBook). No cloud API calls required. All screenshots and task data stay on-device
- **High-Performance Inference**: Mano-P 1.0-4B achieves **~80 tokens/s decode** on Apple M5 Pro; with Cider's W8A8 activation quantization, prefill speeds up by **~12.7%** over the W8A16 baseline
- **Autonomous Long-Task Execution**: Supports **complex business processes** with end-to-end automation without internet connectivity
- **Edge-Native INT8 Acceleration**: Companion [Cider](#-inference-sdk) SDK adds the W8A8 / W4A8 activation-quantization primitives MLX lacks natively, delivering **1.4x–2.2x prefill speedup** over MLX W4A16 on Apple M5 Pro — works with any MLX model, not just Mano-P
- **Autonomous Software Construction**: [Mano-AFK](#-applications) drives a full PRD → code → deploy → test → fix loop using Mano-P as its local vision model for real-browser E2E testing — from a single natural-language prompt to a deployed, tested application, no human in the loop

---

## 🎬 Use Case Demonstrations

### Scenario 1: Mano-AFK Fully automated application construction

https://github.com/user-attachments/assets/8512ab65-f836-4779-979a-4c636fe61fd2

We demonstrated the fully automated application construction process of [Mano-AFK](#-applications). After receiving natural language requirements, the system sequentially completes requirement clarification, technical architecture design, code generation, local deployment, and multi-level testing (API interface testing, LLM based page visual inspection, and end-to-end GUI automation testing driven by VLA model). When the test fails, the system automatically locates the root cause of the problem, fixes the code, and deploys verification again, iterating until all test cases pass. The entire process does not require manual intervention, and ultimately delivers a runnable application with complete requirement documents and build reports.

[![Watch on YouTube](https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube)](https://youtu.be/T2QeXOOvRBQ?si=-I1HDmmtWNeKmg5Q)

### Scenario 2: Commercial video intelligent system

https://github.com/user-attachments/assets/04730188-e664-4f92-8ba7-023269880718

We fully demonstrated the actual workflow of a commercial video intelligent system. Starting from the user's command, the system automatically completes the entire process of video generation, uploading, analysis, editing, and secondary evaluation. During the process, the system can autonomously operate web pages and editing software, complete fine operations such as file processing and subtitle modification, and generate analysis reports containing subjective evaluations and objective indicators. By comparing the differences between the initial and refined versions, visually present the overall capabilities and application effects of the system.

[![Watch on YouTube](https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube)](https://youtu.be/g4sXOTtNPbo?si=RmV5wLLlI1u4e7Nj)

### Scenario 3: Local model task execution

https://github.com/user-attachments/assets/992f4961-3028-45c9-a7c2-29a8e5bf93a9

Mano-P, The small-sized end side GUI-VLA model can run directly on your computer, supporting direct inference operation on Macmini/Macbook with M4 chip and above, as well as direct operation on plug and play computing power sticks. In the CUA scenario, break through the bottleneck of human participation in the Agent workflow. Mano-P, The first step in leading Private AI.

[![Watch on YouTube](https://img.shields.io/badge/Watch%20on-YouTube-red?logo=youtube)](https://youtu.be/VyHhsO1HFpg)

### Scenario 4: Daily Life and Entertainment Applications

https://github.com/user-attachments/assets/ff11fd5b-9ee7-4a74-b8e6-3ad3071d3af8

Mano-P excels not only in enterprise-level business automation but also integrates seamlessly into daily life. This video demonstrates the system's application in Mahjong gameplay: through pure visual understanding of the game interface, it autonomously completes tile recognition, analysis, and decision-making. This case validates Mano-P's general-purpose capabilities beyond work scenarios—from office automation to leisure entertainment, from structured data processing to unstructured game interactions, truly realizing the vision of "Private AI." One model, adapting to every aspect of life and work.

[![Watch on YouTube](https://img.shield

# FILE: README_CN.md

<div align="center">
    <h1>
      <img src="./pics/logo.png" alt="Mano-P Logo" height="60" style="vertical-align: -15px;">
      Mano-P 1.0
    </h1>
    <p><strong>面向端侧设备的GUI感知智能体模型</strong></p>
    <p><strong>私有 AI</strong></p>
</div>

<hr>

<div align="center">

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/Mininglamp-AI/Mano-P?style=social)](https://github.com/Mininglamp-AI/Mano-P)
[![Paper](https://img.shields.io/badge/arXiv-Technical%20Report-red?logo=arxiv)](https://arxiv.org/abs/2509.17336)

中文 | <a href="README.md">English</a>

**[📖 项目概述](#-项目概述) | [🎯 核心亮点](#-核心亮点) | [🎬 应用场景](#-应用场景展示) | [📊 基准测试](#-基准测试性能) | [🔧 Skills](#-skills) | [🤖 模型](#-模型) | [⚡ 推理加速 SDK](#-推理加速-sdk) | [⚗️ 方法](#-方法) | [🌟 技术优势](#-技术优势) | [🔗 应用](#-应用) | [📄 论文引用](#-技术论文与引用) | [❓ FAQ](#-常见问题)**

</div>

---

<div align="center">
  <a href="https://ccnt9oddmvfr.feishu.cn/wiki/QUwbwmUwriHdL4kkyqPcWNaPn9c" target="_blank">
    <img src="pics/Benchmark_Overview.png" alt="GUI Agent Grounding Benchmark" style="max-width: 100%; height: auto;">
  </a>
</div>

---

## 📖 项目概述

**Mano-P**，Mano 是西班牙语里"手"的意思，P 代表 Private。我们相信，个体和组织都能够创造属于自己的私有 AI，人机协同的美好世界即将到来。

![opensource_architecture.png](pics/opensource_architecture_zh.png)

**Mano-P** 是一个专为边缘设备设计的 GUI-VLA 代理项目。它既是一个开源项目，也是一个硬件产品解决方案。作为开源项目，Mano-P 将面向三类不同的开发者群体，分阶段逐步发布。在第一阶段，我们将开源 Mano-CUA 技能。此阶段的目标用户是Agent爱好者，例如 OpenClaw 或 Claude Code 的用户，使他们能够利用 Mano-CUA 技能的功能构建更智能的 CUA 任务工作流程，并克服人工干预带来的瓶颈。在第二阶段，我们将开源 Mano-CUA 的本地模型和 SDK 组件。此阶段的目标用户是具有高安全性要求的开发者，使他们能够直接使用可在 Mac mini 本地运行推理的 GUI-VLA 模型来构建自定义技能、工具等。**重要的是，所有 CUA 操作都将在本地 Mac mini 上执行，而不会上传到外部服务器**。在第三阶段，我们将开源 Mano-P 模型所使用的训练方法、剪枝和量化技术。此阶段旨在满足开发者特定的模型训练需求，使他们能够应用我们的训练方法，创建符合自身独特需求的本地 GUI-VLA 模型。

关于我们的 GUI-VLA 模型（可在 Mac mini 和 MacBook 设备上直接运行推理），我们目前支持两种部署方式：第一种是直接部署在配备 M4 芯片和 32GB 或以上内存的 Mac mini 或 MacBook 机型上；第二种是使用通过 USB 4.0 或更高版本端口连接的算力棒进行部署。我们将在近期发布这两种部署方式的详细说明，并计划在未来扩展支持范围，纳入更多部署选项。

### 主要能力

- **复杂 GUI 自动化操作**：自主完成包含数百个交互元素的复杂界面操作
- **跨系统数据整合**：无需 API 接口，通过纯视觉交互提取和整合多源数据
- **长任务规划执行**：支持数十步至上百步的企业级业务流程自动化
- **智能报告生成**：自动生成数据分析报告、工作总结等结构化文档
- **端侧原生推理**：基于 INT8 激活量化在 Apple Silicon 上高效本地执行（[Cider](#-推理加速-sdk)）
- **自主应用构建**：以视觉 GUI 操作驱动端到端软件构建流水线（[Mano-AFK](#-应用)）

### 技术背景

Mano-P 基于完整的 Mano 项目技术体系（详见 [Mano Technical Report](https://arxiv.org/abs/2509.17336)），采用 Mano-Action 双向自增强学习方法，通过三阶段渐进式训练（SFT → 离线强化学习 → 在线强化学习）和"思考-行动-验证"循环推理机制，配合闭环数据循环系统，实现了高精度的 GUI 理解和操作能力。端侧版本通过混合精度量化、视觉 Token 剪枝和边缘推理自适应等优化，使大参数量模型能够在 Mac mini/MacBook/算力棒等端侧设备上高效运行。

## 🎯 核心亮点

- **OSWorld 基准测试第一**：Mano-P 1.0-72B 在 OSWorld 上取得 **58.2% 成功率**，在所有专用 GUI 智能体模型中排名第一，领先第二名 opencua-72b (45.0%) 达 13.2 个百分点
- **WebRetriever Protocol I 领先**：Mano-P 1.0 取得 **41.7 NavEval 分数**，超越 Gemini 2.5 Pro Computer Use (40.9) 和 Claude 4.5 Computer Use (31.3)
- **完全本地运行**：在**苹果 M4 芯片 + 32GB 内存**的 Mac mini/MacBook 上本地推理，无需云端 API，所有截图和任务数据不出设备
- **高性能推理**：Mano-P 1.0-4B 在 Apple M5 Pro 上实现 **~80 tokens/s 解码**；配合 Cider 的 W8A8 激活量化，prefill 相对 W8A16 baseline 加速约 **12.7%**
- **长任务自主执行**：支持**复杂业务流程**的端到端自动化，无需联网
- **端侧 INT8 加速**：配套 [Cider](#-推理加速-sdk) SDK 补齐了 MLX 原生缺失的 W8A8 / W4A8 激活量化原语，在 Apple M5 Pro 上相对 MLX 原生 W4A16 实现 **1.4x–2.2x 的 prefill 加速**——兼容任意 MLX 模型，并非 Mano-P 专属
- **自主软件构建**：[Mano-AFK](#-应用) 以 Mano-P 为本地视觉模型驱动真实浏览器 E2E 测试，打通 PRD → 代码 → 部署 → 测试 → 修复的完整闭环，从一句自然语言描述到可运行、已测试的应用，全程零人工介入

---

## 🎬 应用场景展示

### 场景 1: Mano-AFK 全自动化应用构建

https://github.com/user-attachments/assets/7637957d-aa5e-48c1-b823-56ff392181ab

我们演示了 [Mano-AFK](#-应用) 全自动化应用构建流程。系统接收自然语言需求后，依次完成需求澄清、技术架构设计、代码生成、本地部署及多层级测试（API接口测试、基于LLM的页面视觉检测、以及通过VLA模型驱动的端到端GUI自动化测试）。测试未通过时，系统自动定位问题根因、修复代码并重新部署验证，循环迭代直至所有测试用例通过。全流程无需人工干预，最终交付可运行的应用及完整的需求文档与构建报告。

[![Watch on 微信视频号](https://img.shields.io/badge/Watch%20on-微信视频号-07C160?logo=wechat&logoColor=white)](https://weixin.qq.com/sph/A7eBqGJkH0)

### 场景 2: 商业视频智能系统

https://github.com/user-attachments/assets/64c7dca1-973f-4c36-b30e-1f4e0e9e8a03

我们完整演示了一套商业视频智能系统的实际工作流程。从用户下发指令开始，系统自动完成视频生成、上传、分析、剪辑再到二次评测的全过程。过程中，系统可自主操作网页与剪辑软件，完成文件处理、字幕修改等精细操作，并生成包含主观评价与客观指标的分析报告。通过对比初版与精剪版本的差异，直观呈现系统的整体能力与应用效果。

[![Watch on 微信视频号](https://img.shields.io/badge/Watch%20on-微信视频号-07C160?logo=wechat&logoColor=white)](https://weixin.qq.com/sph/A0vd7EAezv)

### 场景 3: 本地模型任务执行

https://github.com/user-attachments/assets/cb3e65be-eaf5-44a5-9f38-1415c12a8a43

Mano-P，小尺寸端上GUI-VLA模型，直接运行在你的电脑上，支持M4芯片及以上的Macmini/Macbook直接推理运行，也支持在即插即用算力棒上直接运行。在CUA场景中，打通Agent工作流人类参与其中的瓶颈。Mano-P，引领私有 AI 第一步。

[![Watch on 微信视频号](https://img.shields.io/badge/Watch%20on-微信视频号-07C160?logo=wechat&logoColor=white)](https://weixin.qq.com/sph/AkCLmX4NTA)

### 场景 4: 生活娱乐场景应用

https://github.com/user-attachments/assets/397a0552-9611-4d74-9f24-99544da272b6

Mano-P不仅能胜任企业级业务自动化，更能融入日常生活。本视频展示系统在麻将游戏中的应用：通过纯视觉理解游戏界面，自主完成识牌、分析和决策。这一案例验证了Mano-P在非工作场景下的通用能力——从办公自动化到休闲娱乐，从结构化数据处理到非结构化游戏交互，真正实现"私有 AI"的愿景。一个模型，适配生活与工作的方方面面。

[![Watch on 微信视频号](https://img.shields.io/badge/Watch%20on-微信视频号-07C160?logo=wechat&logoColor=white)](https://weixin.qq.com/sph/AOzBArrvd7)

### 场景 5: Mano-AFK × Cider 本地加速端到端应用构建

https://github.com/user-attachments/assets/5215d4eb-4e6f-4e03-b31b-dc8037c3794d

本视频展示 [Mano-AFK](#-应用) 与 [Cider](#-推理加速-sdk) 推理加速 SDK 的联合能力。Mano-AFK 从一句自然语言需求出发，自主完成需求澄清、架构设计、代码生成、本地部署，并在 E2E 测试环节调用由 Cider 加速的本地 Mano-P 视觉模型驱动真实浏览器完成 GUI 自动化测试；测试失败时自动定位缺陷、修复代码并重新验证，直至交付可运行的应用。Cider 提供 INT8 激活量化原语，让 Mano-P 在 Apple Silicon 上获得显著的 prefill 加速，整个"构建—测试—修复"闭环完全在本地执行，兼顾自主性、隐私与性能。

[![Watch on 抖音](https://img.shields.io/badge/Watch%20on-抖音-000000?logo=tiktok&logoColor=white)](https://v.douyin.com/3NnZSIEzcK0/)

---

## 📊 基准测试性能

**Mano系列模型在多项基准测试上的表现：**

### 1. GUI Grounding

<details>
<summary>📊 展开评测数据</summary>
<br>

![GUI Agent Grounding Benchmark](./pics/GUI_Agent_Grounding_Benchmark.png)

</details>

### 2. BUA & CUA

<details>
<summary>📊 展开评测数据</summary>

#### [OSWorld](https://os-world.github.io/) - Specialized Models

![OS-World-Verified-Specialized-Model.png](pics/OS-World-Verified-Specialized-Model.png)

#### [OSWorld](https://os-world.github.io/) - All Models

![OS-World-Verified-All-Model.png](pics/OS-World-Verified-All-Model.png)

#### [WebRetriever](https://github.com/hhhhhhalf/WebRetriever)

![WebRetriever.png](pics/WebRetriever.png)

</details>

### 3. Perception & Cognition

<details>
<summary>📊 展开评测数据</summary>

#### Video-SME-2

<table>
  <thead>
    <tr>
      <th rowspan="2">Models</th>
      <th rowspan="2">Protocol</th>
      <th colspan="2">CA</th>
      <th colspan="2">CV</th>
      <th colspan="2">PAR</th>
      <th colspan="5">Saliency</th>
    </tr>
    <tr>
      <th>Acc</th>
      <th>F1</th>
      <th>Acc</th>
      <th>F1</th>
      <th>Acc</th>
      <th>F1</th>
      <th>KL↓</th>
      <th>CC↑</th>
      <th>SIM↑</th>
      <th>NSS↑</th>
      <th>AUC↑</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Random</td>
      <td>P1</td>
      <td>10.42</td>
      <td>11.03</td>
      <td>10.76</td>
      <td>10.95</td>
      <td>15.94</td>
      <td>16.00</td>
      <td>2.1789</td>
      <td>0.0452</td>
      <td>0.2852</td>
      <td>0.1081</td>
      <td>0.5340</td>
    </tr>
    <tr>
      <td>P2</td>
      <td>10.01</td>
      <td>10.74</td>
      <td>10.32</td>
      <td>10.50</td>
      <td>14.39</td>
      <td>15.04</td>
      <td>4.3378</td>
      <td>0.0270</td>
      <td>0.2274</td>
      <td>0.0665</td>
      <td>0.5273</td>
    </tr>
  </tbody>
  <tbody>
    <tr>
      <td colspan="13" align="center"><strong>Zero-shot for MLLMs</strong></td>
    </tr>
    <tr>
      <td rowspan="2">GPT4o</td>
      <td>P1</td>
      <td>15.17</td>
      <td>6.57</td>
      <td>16.11</td>
      <td>9.58</td>
      <td>16.71</td>
      <td>10.34</td>
      <td>1.9423</td>
      <td>0.4660</td>
      <td>0.4602</td>
      <td>1.2842</td>
      <td>0.7848</td>
    </tr>
    <tr>
      <td>P2</td>
      <td>10.26</td>
      <td>4.77</td>
      <td>12.16</td>
      <td>7.66</td>
      <td>15.00</td>
      <td>8.55</td>
      <td>2.2650</td>
      <td>0.4097</td>
      <td>0.4028</td>
      <td>1.2418</td>
      <td>0.7807</td>
    </tr>
    <tr>
      <td rowspan="2">Gemini 2.0 Flash</td>
      <td>P1</td>
      <td>17.18</td>
      <td>5.13</td>
      <td><b>25.06</b></td>
      <td>8.39</td>
      <td>24.94</td>
      <td>9.52</td>
      <td>1.4726</td>
      <td>0.3380</td>
      <td>0.3751</td>
      <td>0.8629</td>
      <td>0.7296</td>
    </tr>
    <tr>
      <td>P2</td>
      <td>10.45</td>
      <td>4.26</td>
      <td>12.60</td>
      <td>4.95</td>
      <td>15.96</td>
      <td>7.90</td>
      <td>1.6373</td>
      <td>0.3542</td>
      <td>0.3490</td>
      <td>1.0027</td>
      <td>0.7590</td>
    </tr>
    <tr>
      <td rowspan="2">GPT-5.2</td>
      <td>P1</td>
      <td><b>17.83</b></td>
      <td>7.67</td>
      <td>22.22</td>
      <td>12.55</td>
      <td>16.17</td>
      <td>9.74</td>
      <td><b>1.3262</b></td>
      <td>0.4852</td>
      <td>0.4632</td>
      <td>1.3078</td>
      <td>0.7969</td>
    </tr>
    <tr>
      <td>P2</td>
      <td>15.31</td>
      <td>5.14</td>
      <td>19.88</td>
      <td>10.27</td>
      <td>13.56</td>
      <td>7.42</td>
      <td>1.5444</td>
      <td>0.4379</td>
      <td>0.4092</td>
      <td>1.3006</td>
      <td>0.7999</td>
    </tr>
    <tr>
      <td rowspan="2">Claude Sonnet 4.5</td>
      <td>P1</td>
      <td>10.34</td>
      <td>5.8</td>
      <td>13.26</td>
      <td>9.84</td>
      <td>16.02</td>
      <td>9.94</td>
      <td>1.4235</td>
      <td><b>0.4912</b></td>
      <td>0.4213</td>
      <td>1.2956</td>
      <td>0.8042</td>
    </tr>
    <tr>
      <td>P2</td>
      <td>10.34</td>
      <td>5.55</td>
      <td>13.27</td>
      <td>7.08</td>
      <td>16.02</td>
      <td>9.6</td>
      <td><b>1.2855</b></td>
      <td><b>0.4564</b></td>
      <td>0.4781</td>
      <td>1.3112</td>
      <td>0.7915</td>
    </tr>
    <tr>
      <td rowspan="2">Llama 4 Scout</td>
      <td>P1</td>
      <td>13.98</td>
      <td>9.96</td>
      <td>10.25</td>
      <td>6.51</td>
 
