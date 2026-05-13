# Missing Repo Summary Source: OpenDCAI/DataFlex

- URL: https://github.com/OpenDCAI/DataFlex
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/OpenDCAI__DataFlex
- Clone Status: cloned
- Language: Python
- Stars: 617
- Topics: data, data-mixture, data-model-interaction, data-reweighting, data-science, data-selection, model-training
- Description: DataFlex is a data-centric training framework that enhances model performance by either selecting the most influential samples, optimizing their weights, or adjusting their mixing ratios.

## Extracted README / Docs / Examples



# FILE: README.md


# DataFlex

<p align="center">
 Data Select · Mix · Reweight — Right in the LLM Training Loop
  <img src="https://github.com/user-attachments/assets/12b542ed-3cd9-43a9-acf0-8ebcfe564ecd" width="90%">
</p>
<div align="center">

[![Documents](https://img.shields.io/badge/Documents-Click_here-brightgreen?logo=read-the-docs)](https://OpenDCAI.github.io/DataFlex-Doc/)
[![](https://img.shields.io/github/license/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/blob/main/LICENSE)
[![](https://img.shields.io/github/stars/OpenDCAI/DataFlex?style=social)](https://github.com/OpenDCAI/DataFlex)
[![](https://img.shields.io/github/contributors/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/graphs/contributors)
[![](https://img.shields.io/github/repo-size/OpenDCAI/DataFlex?color=green)](https://github.com/OpenDCAI/DataFlex)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/OpenDCAI/DataFlex)

<!-- [![](https://img.shields.io/github/last-commit/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/commits/main/) -->
<!--[![](https://img.shields.io/github/issues-raw/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/issues) -->

🎉 If you like our project, please give us a star ⭐ on GitHub for the latest update.

[简体中文](./README-zh.md) | English

</div>

## 📰 1. News
- [2026-04-04] 🎉 Our [technical report](https://huggingface.co/papers/2603.26164) ranked #1 on the Hugging Face Daily Papers leaderboard for that day.
- [2026-03-17] We now support gradient computation under DeepSpeed ZeRO-3, enabling training and analysis of larger-scale models.
- [2025-12-23] 🎉 We’re excited to announce the first Data-Centric Training System DataFlex, is now released! Stay tuned for future updates.


## 🔍 2. Overview
<img src="https://github.com/user-attachments/assets/093bfc8e-f450-4048-ad22-456edfdc00d9">

**DataFlex** is an advanced dynamic training framework built on top of [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).  
It intelligently schedules training data during optimization and integrates several difficult-to-reproduce repositories into a unified framework. The system provides reproducible implementations of **Data Selection**, **Data Mixture**, and **Data Reweighting**, thereby improving both experimental reproducibility and final model performance.

DataFlex integrates seamlessly with LLaMA-Factory, offering researchers and developers more flexible and powerful training control. For goals and design philosophy, please refer to [DataFlex-Doc](https://opendcai.github.io/DataFlex-Doc/).
We summarize repositories related to Data Selection, Data Mixture, and Data Reweighting.
❌ indicates that no official repository is available;
✅ indicates that an official repository is available;
⚠️ indicates that an official repository exists but contains issues.

- **Data Selection**: Dynamically selects training samples according to a given strategy (e.g., focus on “hard” samples). The data selection algorithms are summarized as follows:

<div align="center">

| Method | Category | Requires Model-in-the-Loop? | Official Repo |
|:------:|:--------:|:---------------------------:|:-------------:|
| **LESS** | Gradient-Based | ✅ Yes | ⚠️[official code](https://github.com/princeton-nlp/LESS) |
| **NICE** | Gradient-Based | ✅ Yes | ⚠️[official code](https://github.com/JTWang2000/NICE) |
| **Loss** | Loss-Based | ✅ Yes | ❌ |
| **Delta Loss** | Loss-Based | ✅ Yes | ❌ |
| **NEAR** | Data Distribution-Based | ❌ No | ❌ |
| **TSDS** | Data Distribution-Based | ❌ No | ✅[official code](https://github.com/ZifanL/TSDS) |
| **Static** | No Selection | ❌ No | ❌ |
| **Random** | Random Sampling | ❌ No | ❌ |

</div>


- **Data Mixture**: Dynamically adjusts the ratio of data from different domains during training. The data mixture algorithms are summarized as follows:

<div align="center">

| Method | Category | Requires Model-in-the-Loop? | Official Repo |
|:------:|:--------:|:---------------------------:|:-------------:|
| **DOREMI** | Offline Mixture | ✅ Yes | ⚠️[official code](https://github.com/sangmichaelxie/doremi) |
| **ODM** | Online Mixture | ✅ Yes | ⚠️[official code](https://github.com/alon-albalak/online-data-mixing) |

</div>

- **Data Reweighting**: Dynamically adjusts sample weights during backpropagation to emphasize data preferred by the model. The data reweighting algorithms are summarized as follows:

<div align="center">

| Method | Category | Requires Model-in-the-Loop? | Official Repo |
|:------:|:--------:|:---------------------------:|:-------------:|
| **Loss Reweighting** | Loss-Based | ✅ Yes | ❌ |

</div>

- **Full compatibility with LLaMA-Factory**, drop-in replacement.  

## 📌 3. Quick Start

Please use the following commands for environment setup and installation👇

```bash
pip install dataflex
```

Or install from source for development:

```bash
git clone https://github.com/OpenDCAI/DataFlex.git
cd DataFlex
pip install -e .
```

> **Note:** Python 3.11+ is recommended. The core dependencies (including `llamafactory`) will be installed automatically. If you are using Python 3.10, you need to install a compatible version of `llamafactory` manually.

The launch command is similar to [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).
Below is an example using [LESS](https://arxiv.org/abs/2402.04333) :

```bash
dataflex-cli train examples/train_lora/selectors/less.yaml
```

Unlike vanilla LLaMA-Factory, your `.yaml` config file must also include **DataFlex-specific parameters**. For details, please refer to [DataFlex-Doc](https://opendcai.github.io/DataFlex-Doc/).

## 📖 Skills

- [How to Use DataFlex](skills/how_to_use.md) — Installation, CLI commands, YAML configuration, training modes, and supported algorithms.
- [How to Add a New Algorithm](skills/how_to_add_algorithm.md) — Architecture overview, registry system, base class interfaces, and step-by-step guide for adding selectors/mixers/weighters.

## 📚 4. Experimental Results
Using DataFlex can improve performance over the default LLaMA-Factory training.

### Data Selector & Reweightor Results
We use a subset of [Open-Hermes-2.5](https://huggingface.co/datasets/OpenDCAI/DataFlex-selector-openhermes-10w) as the training dataset. The data selection algorithms and data reweighting algorithm outperform the random selector baseline on the [MMLU benchmark](https://huggingface.co/datasets/OpenDCAI/dataflex-selector-MMLUSubset-test) subset relevant to the training dataset. For the Less and Nice algorithm, we set the validation set as the [MMLU-Validation-Set](https://huggingface.co/datasets/OpenDCAI/dataflex-selector-MMLUSubset-valid-cot), using a GPT-5-generated trajectory.

<p align="center">
  <img src="https://github.com/user-attachments/assets/817c7dd7-79cf-4c70-b683-32b5b4c1722b" width="49%">
  <img src="https://github.com/user-attachments/assets/ed5495db-1c5c-4dfd-a0cd-a941000ab33d" width="49%">
</p>

### Data Mixture Results
We use subsets of [SlimPajama-627B](https://huggingface.co/datasets/cerebras/SlimPajama-627B) for data mixture. The data mixture algorithms outperform the baseline (default data mixture) on MMLU accuracy while also achieving lower perplexity across different data domains.

<div align="center">

<table>
  <thead>
    <tr>
      <th rowspan="2">Method</th>
      <th colspan="1">Acc ↑</th>
      <th colspan="8">Perplexity (PPL) ↓</th>
    </tr>
    <tr>
      <th>MMLU</th>
      <th>ALL</th>
      <th>CC</th>
      <th>C4</th>
      <th>SE</th>
      <th>Wiki</th>
      <th>GitHub</th>
      <th>ArXiv</th>
      <th>Book</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="10"><b>Slim-Pajama-6B</b></td>
    </tr>
    <tr>
      <td>Baseline</td>
      <td>25.27</td>
      <td>4.217</td>
      <td>4.278</td>
      <td>4.532</td>
      <td>3.402</td>
      <td><b>3.546</b></td>
      <td><b>2.640</b></td>
      <td>3.508</td>
      <td>4.778</td>
    </tr>
    <tr>
      <td>DoReMi</td>
      <td>25.84</td>
      <td><b>4.134</b></td>
      <td><b>4.108</b></td>
      <td><b>4.358</b></td>
      <td>3.788</td>
      <td>3.997</td>
      <td>3.420</td>
      <td>3.413</td>
      <td>4.661</td>
    </tr>
    <tr>
      <td>ODM</td>
      <td><b>26.04</b></td>
      <td>4.244</td>
      <td>4.326</td>
      <td>4.555</td>
      <td><b>3.243</b></td>
      <td>3.699</td>
      <td>2.704</td>
      <td><b>2.904</b></td>
      <td><b>4.613</b></td>
    </tr>
    <tr>
      <td colspan="10"><b>Slim-Pajama-30B</b></td>
    </tr>
    <tr>
      <td>Baseline</td>
      <td>25.51</td>
      <td>3.584</td>
      <td>3.723</td>
      <td>3.505</td>
      <td>2.850</td>
      <td>3.215</td>
      <td>3.163</td>
      <td>4.540</td>
      <td>5.329</td>
    </tr>
    <tr>
      <td>DoReMi</td>
      <td><b>25.97</b></td>
      <td>3.562</td>
      <td>3.731</td>
      <td><b>3.503</b></td>
      <td>2.706</td>
      <td>2.985</td>
      <td>2.973</td>
      <td>4.441</td>
      <td>5.214</td>
    </tr>
    <tr>
      <td>ODM</td>
      <td>25.63</td>
      <td><b>3.429</b></td>
      <td><b>3.598</b></td>
      <td>3.519</td>
      <td><b>2.382</b></td>
      <td><b>2.713</b></td>
      <td><b>2.255</b></td>
      <td><b>3.487</b></td>
      <td><b>4.746</b></td>
    </tr>
  </tbody>
</table>

</div>

## 🧩 5. Ecosystem
DataFlex focuses on data scheduling during training. For a complete pipeline starting from raw data, it pairs well with [DataFlow](https://github.com/OpenDCAI/DataFlow):
<div align="center">
  <img src="https://github.com/user-attachments/assets/7459da1b-86ec-40cc-873b-c54f10f8c291" width="90%">
</div>

[DataFlow](https://github.com/OpenDCAI/DataFlow) converts raw files into LLM training data through composable operator pipelines — document parsing, knowledge cleaning, QA / CoT synthesis, and training format conversion. The output JSON can be fed directly into DataFlex.
The two projects are independent with no code dependency, connected only by standard data formats. DataFlex accepts training da

# FILE: README-zh.md


# DataFlex
<p align="center">
 Data Select · Mix · Reweight — Right in the LLM Training Loop
  <img src="https://github.com/user-attachments/assets/12b542ed-3cd9-43a9-acf0-8ebcfe564ecd" width="90%">
</p>

<div align="center">

[![Documents](https://img.shields.io/badge/官方文档-单击此处-brightgreen?logo=read-the-docs)](https://OpenDCAI.github.io/DataFlex-Doc/)
[![](https://img.shields.io/github/license/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/blob/main/LICENSE)
[![](https://img.shields.io/github/stars/OpenDCAI/DataFlex?style=social)](https://github.com/OpenDCAI/DataFlex)
[![](https://img.shields.io/github/contributors/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/graphs/contributors)
[![](https://img.shields.io/github/repo-size/OpenDCAI/DataFlex?color=green)](https://github.com/OpenDCAI/DataFlex)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/OpenDCAI/DataFlex)

<!-- [![](https://img.shields.io/github/last-commit/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/commits/main/) -->
<!--[![](https://img.shields.io/github/issues-raw/OpenDCAI/DataFlex)](https://github.com/OpenDCAI/DataFlex/issues) -->

🎉 如果你认可我们的项目，欢迎在 GitHub 上点个 ⭐ Star，关注项目最新进展。

简体中文 | [English](./README.md)

</div>

## 📰 1. 新闻
* [2026-04-04] 🎉 我们的[技术报告](https://huggingface.co/papers/2603.26164)在 Hugging Face Daily Papers 当日榜单中排名第一。
* [2026-03-17] 我们现已支持在 DeepSpeed ZeRO-3 下进行梯度计算，从而支持更大规模模型的训练与分析。
* [2025-12-23] 🎉 我们很高兴地宣布首个 **数据中心训练系统 DataFlex** 正式发布！敬请期待后续更新。

## 🔍 2. 概述

<img src="https://github.com/user-attachments/assets/1fdb62e4-1143-4866-afd2-c1067ad25ae8">

**DataFlex** 是一个构建在 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 之上的高级动态训练框架。
它能够在训练过程中智能地调度数据，支持 **动态样本选择**、**领域比例调整** 以及 **动态加权**，旨在同时提升训练效率与最终模型性能。

DataFlex 与 LLaMA-Factory 无缝集成，为研究人员和开发者提供更灵活、更强大的训练控制能力。关于目标与设计理念，请参考 [DataFlex-Doc](https://opendcai.github.io/DataFlex-Doc/)。

我们汇总了与数据选择、数据混合和数据重加权相关的仓库。
❌ 表示没有官方仓库；
✅ 表示有官方仓库；
⚠️ 表示有官方仓库但存在问题。

- **Dynamic Select Trainer（动态数据选择训练器）**：  
  根据给定策略在训练过程中**动态选择训练样本**（例如，优先关注“困难样本”）。支持的数据选择算法总结如下：
<div align="center">
  
  | 方法 | 类别 | 是否需要模型参与 | 官方仓库 |
  |:----:|:----:|:-------------------------------------:|:-------------:|
  | **LESS** | 基于梯度 | ✅ 是 | ⚠️[official code](https://github.com/princeton-nlp/LESS) |
  | **NICE** | 基于梯度 | ✅ 是 | ⚠️[official code](https://github.com/JTWang2000/NICE) |
  | **Loss** | 基于损失 | ✅ 是 | ❌ |
  | **Delta Loss** | 基于损失 | ✅ 是 | ❌ |
  | **NEAR** | 基于数据分布 | ❌ 否 | ❌ |
  | **TSDS** | 基于数据分布 | ❌ 否 | ✅[official code](https://github.com/ZifanL/TSDS) |
  | **Static** | 无数据选择 | ❌ 否 | ❌ |
  | **Random** | 随机采样 | ❌ 否 | ❌ |
  
</div>

- **Dynamic Mix Trainer（动态数据混合训练器）**：  
  在训练过程中**动态调整来自不同数据域的数据比例**。支持的数据混合算法总结如下：
<div align="center">
  
  | 方法 | 类别 | 是否需要模型参与 | 官方仓库 |
  |:----:|:----:|:-------------------------------------:|:-------------:|
  | **DOREMI** | 离线混合 | ✅ 是 | ⚠️[official code](https://github.com/sangmichaelxie/doremi) |
  | **ODM** | 在线混合 | ✅ 是 | ⚠️[official code](https://github.com/alon-albalak/online-data-mixing) |
</div>

- **Dynamic Weight Trainer（动态样本加权训练器）**：  
  在反向传播过程中**动态调整样本权重**，以强调模型更偏好的数据。支持的数据重加权算法总结如下：
  
<div align="center">
  
  | 方法 | 类别 | 是否需要模型参与 | 官方仓库 |
  |:----:|:----:|:-------------------------------------:|:-------------:|
  | **Loss Reweighting** | 基于损失 | ✅ 是 | ❌ |
</div>
* **与 LLaMA-Factory 完全兼容**，可作为即插即用的替代方案。

## 📌 3. 快速开始

请使用以下命令进行环境配置与安装👇

```bash
pip install dataflex
```

或者从源码安装（适用于开发）：

```bash
git clone https://github.com/OpenDCAI/DataFlex.git
cd DataFlex
pip install -e .

# 在 Python 3.10 环境中，请安装 v0.9.3 以确保兼容性
pip install llamafactory==0.9.3

# 在 Python 3.11+ 环境中，推荐安装最新的 v0.9.4
pip install llamafactory==0.9.4
```

启动命令与 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 类似。
下面给出一个使用 [LESS](https://arxiv.org/abs/2402.04333) 的示例：

```bash
dataflex-cli train examples/train_lora/selectors/less.yaml
```

与原生 LLaMA-Factory 不同的是，你的 `.yaml` 配置文件中还必须包含 **DataFlex 特有的参数**，具体请参考 [DataFlex-Doc](https://opendcai.github.io/DataFlex-Doc/)。

## 📖 Skills

- [如何使用 DataFlex](skills/how_to_use.md) — 安装、CLI 命令、YAML 配置、训练模式、已支持算法一览。
- [如何添加新算法](skills/how_to_add_algorithm.md) — 架构概览、Registry 机制、基类接口、添加 Selector/Mixer/Weighter 的完整步骤。

## 📚 4. 实验结果
使用 DataFlex 可以在默认 LLaMA-Factory 训练的基础上提升模型性能。

### 数据选择与加权实验结果
我们使用 Open-Hermes-2.5 的一个子集作为训练数据集。实验结果表明，相较于随机选择（random selector）基线，所采用的数据选择算法和数据重加权算法在与训练数据集相关的 MMLU 基准测试子集上均取得了更优的性能。对于 LESS 和 NICE 算法，我们将 MMLU-Validation-Set 作为验证集，并使用由 GPT-5 生成的推理轨迹（trajectory）进行验证。

<p align="center">
  <img src="https://github.com/user-attachments/assets/817c7dd7-79cf-4c70-b683-32b5b4c1722b" width="49%">
  <img src="https://github.com/user-attachments/assets/ed5495db-1c5c-4dfd-a0cd-a941000ab33d" width="49%">
</p>

### 数据配比实验结果
我们使用 [SlimPajama-627B](https://huggingface.co/datasets/cerebras/SlimPajama-627B) 的子集进行数据配比实验。数据配比算法在 MMLU 准确率上超过了基线方法，同时在不同数据域上也取得了更低的困惑度（PPL）。

<div align="center">

<table>
  <thead>
    <tr>
      <th rowspan="2">方法</th>
      <th colspan="1">Acc ↑</th>
      <th colspan="8">Perplexity (PPL) ↓</th>
    </tr>
    <tr>
      <th>MMLU</th>
      <th>ALL</th>
      <th>CC</th>
      <th>C4</th>
      <th>SE</th>
      <th>Wiki</th>
      <th>GitHub</th>
      <th>ArXiv</th>
      <th>Book</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td colspan="10"><b>Slim-Pajama-6B</b></td>
    </tr>
    <tr>
      <td>Baseline</td>
      <td>25.27</td>
      <td>4.217</td>
      <td>4.278</td>
      <td>4.532</td>
      <td>3.402</td>
      <td><b>3.546</b></td>
      <td><b>2.640</b></td>
      <td>3.508</td>
      <td>4.778</td>
    </tr>
    <tr>
      <td>DoReMi</td>
      <td>25.84</td>
      <td><b>4.134</b></td>
      <td><b>4.108</b></td>
      <td><b>4.358</b></td>
      <td>3.788</td>
      <td>3.997</td>
      <td>3.420</td>
      <td>3.413</td>
      <td>4.661</td>
    </tr>
    <tr>
      <td>ODM</td>
      <td><b>26.04</b></td>
      <td>4.244</td>
      <td>4.326</td>
      <td>4.555</td>
      <td><b>3.243</b></td>
      <td>3.699</td>
      <td>2.704</td>
      <td><b>2.904</b></td>
      <td><b>4.613</b></td>
    </tr>
    <tr>
      <td colspan="10"><b>Slim-Pajama-30B</b></td>
    </tr>
    <tr>
      <td>Baseline</td>
      <td>25.51</td>
      <td>3.584</td>
      <td>3.723</td>
      <td>3.505</td>
      <td>2.850</td>
      <td>3.215</td>
      <td>3.163</td>
      <td>4.540</td>
      <td>5.329</td>
    </tr>
    <tr>
      <td>DoReMi</td>
      <td><b>25.97</b></td>
      <td>3.562</td>
      <td>3.731</td>
      <td><b>3.503</b></td>
      <td>2.706</td>
      <td>2.985</td>
      <td>2.973</td>
      <td>4.441</td>
      <td>5.214</td>
    </tr>
    <tr>
      <td>ODM</td>
      <td>25.63</td>
      <td><b>3.429</b></td>
      <td><b>3.598</b></td>
      <td>3.519</td>
      <td><b>2.382</b></td>
      <td><b>2.713</b></td>
      <td><b>2.255</b></td>
      <td><b>3.487</b></td>
      <td><b>4.746</b></td>
    </tr>
  </tbody>
</table>

</div>

## 🧩 5. 生态系统

DataFlex 主要聚焦于训练过程中的数据调度。若希望构建一条从原始数据出发的完整流水线，它可以与 [DataFlow](https://github.com/OpenDCAI/DataFlow) 配合使用：

<div align="center">
  <img src="https://github.com/user-attachments/assets/7459da1b-86ec-40cc-873b-c54f10f8c291" width="90%">
</div>

[DataFlow](https://github.com/OpenDCAI/DataFlow) 通过可组合的算子工作流，将原始文件转换为适用于大语言模型训练的数据，包括文档解析、知识清洗、问答 / CoT 合成，以及训练格式转换等步骤。其输出的 JSON 数据可直接输入 DataFlex 进行训练。

这两个项目彼此独立，不存在代码层面的依赖关系，仅通过标准化的数据格式进行衔接。DataFlex 可以接收来自任意来源的训练数据，包括 DataFlow、人工标注、HuggingFace 数据集，或用户自定义的数据处理脚本。

## 🤝 6. 致谢

我们感谢 [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) 提供了高效且易用的大模型微调框架，极大地促进了我们在训练与实验中的快速迭代。
感谢中关村学院提供的 API 和 GPU 支持。
同时也感谢所有开源社区的贡献者——正是你们的努力共同推动了 DataFlex 的发展。

## 📜 7. 引用

如果您在研究中使用了 DataFlex，欢迎引用我们的项目。
```bibtex
@article{liang2026dataflex,
  title={DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language Models},
  author={Liang, Hao and Zhao, Zhengyang and Qiang, Meiyi and Chen, Mingrui and Ma, Lu and Yu, Rongyi and Feng, Hengyi and Sun, Shixuan and Meng, Zimo and Ma, Xiaochen and others},
  journal={arXiv preprint arXiv:2603.26164},
  year={2026}
}

@article{liang2026towards,
  title={Towards Next-Generation LLM Training: From the Data-Centric Perspective},
  author={Liang, Hao and Zhao, Zhengyang and Han, Zhaoyang and Qiang, Meiyi and Ma, Xiaochen and Zeng, Bohan and Cai, Qifeng and Li, Zhiyu and Tang, Linpeng and Zhang, Wentao and others},
  journal={arXiv preprint arXiv:2603.14712},
  year={2026}
}
```

## 🤝 8. 社区与支持

我们欢迎贡献新的 trainers 和 selectors！
在提交 PR 之前，请确保代码风格与现有代码保持一致。

我们也欢迎你加入 [DataFlex](https://github.com/OpenDCAI/DataFlex) 与 [DataFlow](https://github.com/OpenDCAI/DataFlow) 开源社区，提出问题、分享想法，并与其他开发者协作！

•	📮 [GitHub Issues](../../issues)：报告 Bug 或提出新功能建议

•	🔧 [GitHub Pull Requests](../../pulls)：贡献代码改进

•	💬 加入我们的社区群组，与我们及其他贡献者交流！

<div align="center">
  <img src="https://github.com/user-attachments/assets/3a5704ac-08ac-4396-8145-8e051db5969d" width="70%">
</div>


# FILE: examples/README.md

We provide diverse examples about fine-tuning LLMs.

Make sure to execute these commands in the `LLaMA-Factory` directory.

## Table of Contents

- [LoRA Fine-Tuning](#lora-fine-tuning)
- [QLoRA Fine-Tuning](#qlora-fine-tuning)
- [Full-Parameter Fine-Tuning](#full-parameter-fine-tuning)
- [Merging LoRA Adapters and Quantization](#merging-lora-adapters-and-quantization)
- [Inferring LoRA Fine-Tuned Models](#inferring-lora-fine-tuned-models)
- [Extras](#extras)

Use `CUDA_VISIBLE_DEVICES` (GPU) or `ASCEND_RT_VISIBLE_DEVICES` (NPU) to choose computing devices.

By default, LLaMA-Factory uses all visible computing devices.

Basic usage:

```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

Advanced usage:

```bash
CUDA_VISIBLE_DEVICES=0,1 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml \
    learning_rate=1e-5 \
    logging_steps=1
```

```bash
bash examples/train_lora/llama3_lora_sft.sh
```

## Examples

### LoRA Fine-Tuning

#### (Continuous) Pre-Training

```bash
llamafactory-cli train examples/train_lora/llama3_lora_pretrain.yaml
```

#### Supervised Fine-Tuning

```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

#### Multimodal Supervised Fine-Tuning

```bash
llamafactory-cli train examples/train_lora/qwen2_5vl_lora_sft.yaml
```

#### DPO/ORPO/SimPO Training

```bash
llamafactory-cli train examples/train_lora/llama3_lora_dpo.yaml
```

#### Multimodal DPO/ORPO/SimPO Training

```bash
llamafactory-cli train examples/train_lora/qwen2_5vl_lora_dpo.yaml
```

#### Reward Modeling

```bash
llamafactory-cli train examples/train_lora/llama3_lora_reward.yaml
```

#### PPO Training

```bash
llamafactory-cli train examples/train_lora/llama3_lora_ppo.yaml
```

#### KTO Training

```bash
llamafactory-cli train examples/train_lora/llama3_lora_kto.yaml
```

#### Preprocess Dataset

It is useful for large dataset, use `tokenized_path` in config to load the preprocessed dataset.

```bash
llamafactory-cli train examples/train_lora/llama3_preprocess.yaml
```

#### Evaluating on MMLU/CMMLU/C-Eval Benchmarks

```bash
llamafactory-cli eval examples/train_lora/llama3_lora_eval.yaml
```

#### Supervised Fine-Tuning on Multiple Nodes

```bash
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=0 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=1 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

#### Supervised Fine-Tuning with DeepSpeed ZeRO-3 (Weight Sharding)

```bash
FORCE_TORCHRUN=1 llamafactory-cli train examples/train_lora/llama3_lora_sft_ds3.yaml
```

#### Supervised Fine-Tuning with Ray on 4 GPUs

```bash
USE_RAY=1 llamafactory-cli train examples/train_lora/llama3_lora_sft_ray.yaml
```

### QLoRA Fine-Tuning

#### Supervised Fine-Tuning with 4/8-bit Bitsandbytes/HQQ/EETQ Quantization (Recommended)

```bash
llamafactory-cli train examples/train_qlora/llama3_lora_s

# FILE: examples/README_zh.md

我们提供了多样化的大模型微调示例脚本。

请确保在 `LLaMA-Factory` 目录下执行下述命令。

## 目录

- [LoRA 微调](#lora-微调)
- [QLoRA 微调](#qlora-微调)
- [全参数微调](#全参数微调)
- [合并 LoRA 适配器与模型量化](#合并-lora-适配器与模型量化)
- [推理 LoRA 模型](#推理-lora-模型)
- [杂项](#杂项)

使用 `CUDA_VISIBLE_DEVICES`（GPU）或 `ASCEND_RT_VISIBLE_DEVICES`（NPU）选择计算设备。

LLaMA-Factory 默认使用所有可见的计算设备。

基础用法：

```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

高级用法：

```bash
CUDA_VISIBLE_DEVICES=0,1 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml \
    learning_rate=1e-5 \
    logging_steps=1
```

```bash
bash examples/train_lora/llama3_lora_sft.sh
```

## 示例

### LoRA 微调

#### （增量）预训练

```bash
llamafactory-cli train examples/train_lora/llama3_lora_pretrain.yaml
```

#### 指令监督微调

```bash
llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

#### 多模态指令监督微调

```bash
llamafactory-cli train examples/train_lora/qwen2_5vl_lora_sft.yaml
```

#### DPO/ORPO/SimPO 训练

```bash
llamafactory-cli train examples/train_lora/llama3_lora_dpo.yaml
```

#### 多模态 DPO/ORPO/SimPO 训练

```bash
llamafactory-cli train examples/train_lora/qwen2_5vl_lora_dpo.yaml
```

#### 奖励模型训练

```bash
llamafactory-cli train examples/train_lora/llama3_lora_reward.yaml
```

#### PPO 训练

```bash
llamafactory-cli train examples/train_lora/llama3_lora_ppo.yaml
```

#### KTO 训练

```bash
llamafactory-cli train examples/train_lora/llama3_lora_kto.yaml
```

#### 预处理数据集

对于大数据集有帮助，在配置中使用 `tokenized_path` 以加载预处理后的数据集。

```bash
llamafactory-cli train examples/train_lora/llama3_preprocess.yaml
```

#### 在 MMLU/CMMLU/C-Eval 上评估

```bash
llamafactory-cli eval examples/train_lora/llama3_lora_eval.yaml
```

#### 多机指令监督微调

```bash
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=0 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
FORCE_TORCHRUN=1 NNODES=2 NODE_RANK=1 MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 llamafactory-cli train examples/train_lora/llama3_lora_sft.yaml
```

### 支持弹性和容错的多机指令监督微调

要启动一个支持弹性节点和容错的多机指令微调，在每个节点上执行以下命令。弹性节点数量范围为 `MIN_NNODES:MAX_NNODES`，每个节点最多允许因为错误重启 `MAX_RESTARTS` 次。`RDZV_ID` 应设置为一个唯一的作业 ID（由参与该作业的所有节点共享）。更多新可以参考官方文档 [torchrun](https://docs.pytorch.org/docs/stable/elastic/run.html)。

```bash
FORCE_TORCHRUN=1 MIN_NNODES=1 MAX_NNODES=3 MAX_RESTARTS=3 RDZV_ID=llamafactory MASTER_ADDR=192.168.0.1 MASTER_PORT=29500 llamafactory-cli train examples/train_full/llama3_full_sft.yaml
```

#### 使用 DeepSpeed ZeRO-3 平均分配显存

```bash
FORCE_TORCHRUN=1 llamafactory-cli train examples/train_lora/llama3_lora_sft_ds3.yaml
```

#### 使用 Ray 在 4 张 GPU 上微调

```bash
USE_RAY=1 llamafactory-cli train examples/train_lora/llama3_lora_sft_ray.yaml
```

### QLoRA 微调

#### 基于 4/8 比特 Bitsandbytes/HQQ/EETQ 量化进行指令监督微调（推荐）

```bash
llamafactory-cli train examples/train_qlora/llama3_lora_sft_otfq.yaml
```

#### 在 NPU 上基于 4 比特 Bitsandbytes 量化进行指令监督微调

```bash
llamafactory-cli train examples/train_qlora/llama3_lora_sft_bnb_npu.yaml
```

#### 基于 4/8 比特 GPTQ 量化进行指令监督微调

```bash
llamafactory-cli train examples/trai

# FILE: examples/deepspeed/ds_z3_config.json

{
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "zero_allow_untested_optimizer": true,
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 3,
    "overlap_comm": false,
    "contiguous_gradients": true,
    "sub_group_size": 1e9,
    "reduce_bucket_size": "auto",
    "stage3_prefetch_bucket_size": "auto",
    "stage3_param_persistence_threshold": "auto",
    "stage3_max_live_parameters": 1e9,
    "stage3_max_reuse_distance": 1e9,
    "stage3_gather_16bit_weights_on_model_save": true
  }
}


# FILE: examples/deepspeed/ds_z0_config.json

{
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "zero_allow_untested_optimizer": true,
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 0,
    "allgather_partitions": true,
    "allgather_bucket_size": 5e8,
    "overlap_comm": false,
    "reduce_scatter": true,
    "reduce_bucket_size": 5e8,
    "contiguous_gradients": true,
    "round_robin_gradients": true
  }
}


# FILE: examples/deepspeed/ds_z3_offload_config.json

{
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "zero_allow_untested_optimizer": true,
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": {
      "device": "cpu",
      "pin_memory": true
    },
    "offload_param": {
      "device": "cpu",
      "pin_memory": true
    },
    "overlap_comm": false,
    "contiguous_gradients": true,
    "sub_group_size": 1e9,
    "reduce_bucket_size": "auto",
    "stage3_prefetch_bucket_size": "auto",
    "stage3_param_persistence_threshold": "auto",
    "stage3_max_live_parameters": 1e9,
    "stage3_max_reuse_distance": 1e9,
    "stage3_gather_16bit_weights_on_model_save": true
  }
}


# FILE: examples/deepspeed/ds_z2_offload_config.json

{
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "zero_allow_untested_optimizer": true,
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 2,
    "offload_optimizer": {
      "device": "cpu",
      "pin_memory": true
    },
    "allgather_partitions": true,
    "allgather_bucket_size": 5e8,
    "overlap_comm": false,
    "reduce_scatter": true,
    "reduce_bucket_size": 5e8,
    "contiguous_gradients": true,
    "round_robin_gradients": true
  }
}


# FILE: examples/deepspeed/ds_z2_config.json

{
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto",
  "gradient_accumulation_steps": "auto",
  "gradient_clipping": "auto",
  "zero_allow_untested_optimizer": true,
  "fp16": {
    "enabled": "auto",
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  "bf16": {
    "enabled": "auto"
  },
  "zero_optimization": {
    "stage": 2,
    "allgather_partitions": true,
    "allgather_bucket_size": 5e8,
    "overlap_comm": false,
    "reduce_scatter": true,
    "reduce_bucket_size": 5e8,
    "contiguous_gradients": true,
    "round_robin_gradients": true
  }
}


# FILE: examples/accelerate/fsdp_config_offload.yaml

compute_environment: LOCAL_MACHINE
debug: false
distributed_type: FSDP
downcast_bf16: 'no'
fsdp_config:
  fsdp_auto_wrap_policy: TRANSFORMER_BASED_WRAP
  fsdp_backward_prefetch: BACKWARD_PRE
  fsdp_forward_prefetch: false
  fsdp_cpu_ram_efficient_loading: true
  fsdp_offload_params: true  # offload may affect training speed
  fsdp_sharding_strategy: FULL_SHARD
  fsdp_state_dict_type: FULL_STATE_DICT
  fsdp_sync_module_states: true
  fsdp_use_orig_params: true
machine_rank: 0
main_training_function: main
mixed_precision: bf16  # or fp16
num_machines: 1  # the number of nodes
num_processes: 2  # the number of GPUs in all nodes
rdzv_backend: static
same_network: true
tpu_env: []
tpu_use_cluster: false
tpu_use_sudo: false
use_cpu: false

