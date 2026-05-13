# Missing Repo Summary Source: OpenMOSS/MOSS-TTS-Nano

- URL: https://github.com/OpenMOSS/MOSS-TTS-Nano
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/OpenMOSS__MOSS-TTS-Nano
- Clone Status: cloned
- Language: Python
- Stars: 2910
- Topics: audio-tokenizer, chinese, english, multi-modality, multilingual, realtime, streaming-audio, tts, voice-clone
- Description: MOSS-TTS-Nano is an open-source multilingual tiny speech generation model from MOSI.AI and the OpenMOSS team. With only 0.1B parameters, it is designed for realtime speech generation, can run directly on CPU without a GPU, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

## Extracted README / Docs / Examples



# FILE: README.md

# MOSS-TTS-Nano

<br>

<p align="center">
  <img src="./assets/images/OpenMOSS_Logo.png" height="70" align="middle" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="./assets/images/mosi-logo.png" height="50" align="middle" />
</p>

<div align="center">
  <a href="https://clawhub.ai/luogao2333/moss-tts-voice"><img src="https://img.shields.io/badge/🦞_OpenClaw-Skills-8A2BE2" alt="OpenClaw"></a>
  <a href="https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano"><img src="https://img.shields.io/badge/Huggingface-Models-orange?logo=huggingface&amp"></a>
  <a href="https://modelscope.cn/models/openmoss/MOSS-TTS-Nano"><img src="https://img.shields.io/badge/ModelScope-Models-7B61FF?logo=modelscope&amp;logoColor=white"></a>
  <a href="https://openmoss.github.io/MOSS-TTS-Nano-Demo/"><img src="https://img.shields.io/badge/Blog-View-blue?logo=internet-explorer&amp"></a>
  <a href="https://arxiv.org/abs/2603.18090"><img src="https://img.shields.io/badge/Arxiv-2603.18090-red?logo=arxiv&amp"></a>

  <a href="https://studio.mosi.cn/experiments/moss-tts-nano"><img src="https://img.shields.io/badge/AIStudio-Try-green?logo=internet-explorer&amp"></a>
  <a href="https://studio.mosi.cn/docs/moss-tts-nano"><img src="https://img.shields.io/badge/API-Docs-00A3FF?logo=fastapi&amp"></a>
  <a href="https://x.com/Open_MOSS"><img src="https://img.shields.io/badge/Twitter-Follow-black?logo=x&amp"></a>
  <a href="https://discord.gg/Xf3aXddCjc"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp"></a>
  <a href="./assets/images/wechat.jpg"><img src="https://img.shields.io/badge/WeChat-Join-07C160?logo=wechat&amp;logoColor=white" alt="WeChat"></a>
</div>

[English](README.md) | [简体中文](README_zh.md)



MOSS-TTS-Nano is an open-source **multilingual tiny speech generation model** from [MOSI.AI](https://mosi.cn/#hero) and the [OpenMOSS team](https://www.open-moss.com/). With only **0.1B parameters**, it is designed for **realtime speech generation**, can run directly on **CPU without a GPU**, and keeps the deployment stack simple enough for local demos, web serving, and lightweight product integration.

## MOSS-TTS 2.0 Feedback Collection

MOSS-TTS 2.0 is coming soon. To better optimize model capabilities and product experience, we are collecting feedback and suggestions from TTS users. Please take 2-3 minutes to fill out the [requirements collection form](https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef). Feature requests of any kind are welcome.

<p align="center">
  <a href="https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef">
    <img src="./assets/images/moss_tts_2_requirements_gathering.jpg" width="360" alt="MOSS-TTS 2.0 requirements collection QR code" />
  </a>
</p>

[demo_video.mp4](https://github.com/user-attachments/assets/25aca215-0bd7-4d0c-be95-8d1f6737aec8)

## News

* 2026.5.6: **MOSS-TTS**, **MOSS-TTS-Nano**, and **MOSS-Audio-Tokenizer** now support [**mlx-audio**](https://github.com/Blaizzy/mlx-audio). Visit the [mlx-audio GitHub repository](https://github.com/Blaizzy/mlx-audio) for details.
* 2026.4.29: MOSS-TTS 2.0 is coming soon! We are collecting TTS feedback, suggestions, and feature requests via the [requirements collection form](https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef).
* 2026.4.27: We added updated evaluation results for [**MOSS-Audio-Tokenizer-Nano**](#moss-audio-tokenizer-nano), including reconstruction quality comparisons on speech, audio, and music benchmarks.
* 2026.4.17: We are excited to release a more efficient and fully standalone [**ONNX CPU Version**](#onnx-cpu-version), backed by the Hugging Face repositories [**MOSS-TTS-Nano-100M-ONNX**](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano-100M-ONNX) and [**MOSS-Audio-Tokenizer-Nano-ONNX**](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX). It preserves the full voice cloning workflow while removing the PyTorch dependency during inference. In our tests, it delivers nearly **2x** the processing efficiency of the original version, and runs smoothly on a **single CPU core** on a **MacBook Air M4**. Built on top of this ONNX CPU version, we have also updated [**MOSS-TTS-Nano-Reader**](https://github.com/OpenMOSS/MOSS-TTS-Nano-Reader), which can now run the model directly inside the browser as an extension, without requiring a separate local inference service.
* 2026.4.16: We release the **MOSS-TTS-Nano finetuning code**. See [./finetuning/README.md](./finetuning/README.md) for training and usage details.
* 2026.4.14: We release [**MOSS-TTS-Nano-Reader**](https://github.com/OpenMOSS/MOSS-TTS-Nano-Reader), a local browser reading application built on top of **MOSS-TTS-Nano**.
* 2026.4.10: We release **MOSS-TTS-Nano**. A demo Space is available at [OpenMOSS-Team/MOSS-TTS-Nano](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS-Nano). You can also view the demo and more details at [openmoss.github.io/MOSS-TTS-Nano-Demo/](https://openmoss.github.io/MOSS-TTS-Nano-Demo/).

## Demo

- Online Demo: [https://openmoss.github.io/MOSS-TTS-Nano-Demo/](https://openmoss.github.io/MOSS-TTS-Nano-Demo/)
- Hugging Face Space: [OpenMOSS-Team/MOSS-TTS-Nano](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS-Nano)

## Contents

- [News](#news)
- [Demo](#demo)
- [Introduction](#introduction)
  - [Main Features](#main-features)
- [Supported Languages](#supported-languages)
- [Quickstart](#quickstart)
  - [Environment Setup](#environment-setup)
  - [Voice Clone with `infer.py`](#voice-clone-with-inferpy)
  - [Local Web Demo with `app.py`](#local-web-demo-with-apppy)
  - [ONNX CPU Inference](#onnx-cpu-version)
  - [Export TTS-only ONNX Weights](#export-tts-only-onnx-weights)
  - [CLI Command: `moss-tts-nano generate`](#cli-command-moss-tts-nano-generate)
  - [CLI Command: `moss-tts-nano serve`](#cli-command-moss-tts-nano-serve)
  - [Finetuning](#finetuning)
- [MOSS-Audio-Tokenizer-Nano](#moss-audio-tokenizer-nano)
- [MOSS-TTS Family](#moss-tts)
- [License](#license)
- [Citation](#citation)
- [Star History](#star-history)

## Introduction

<p align="center">
  <img src="./assets/images/concept.png" alt="MOSS-TTS-Nano concept" width="85%" />
</p>

MOSS-TTS-Nano focuses on the part of TTS deployment that matters most in practice: **small footprint**, **low latency**, **good enough quality for realtime products**, and **simple local setup**. It uses a pure autoregressive **Audio Tokenizer + LLM** pipeline and keeps the inference workflow friendly for both terminal users and web-demo users.

### Main Features

- **Tiny model size**: only **0.1B parameters**
- **Native audio format**: **48 kHz**, **2-channel** output
- **Multilingual**: supports **Chinese, English, and more**
- **Pure autoregressive architecture**: built on **Audio Tokenizer + LLM**
- **Streaming inference**: low realtime latency and fast first audio
- **CPU friendly**: streaming generation can run on a **4-core CPU**
- **Long-text capable**: supports long input with automatic chunked voice cloning
- **Open-source deployment**: direct `python infer.py`, `python app.py`, and packaged CLI support

<p align="center">
  <img src="./assets/images/arch_moss_tts_nano.png" alt="MOSS-TTS-Nano architecture" width="80%" />
  <br />
  Architecture of MOSS-TTS-Nano
</p>

## Supported Languages

MOSS-TTS-Nano currently supports **20 languages**:

| Language | Code | Flag | Language | Code | Flag | Language | Code | Flag |
|---|---|---|---|---|---|---|---|---|
| Chinese | zh | 🇨🇳 | English | en | 🇺🇸 | German | de | 🇩🇪 |
| Spanish | es | 🇪🇸 | French | fr | 🇫🇷 | Japanese | ja | 🇯🇵 |
| Italian | it | 🇮🇹 | Hungarian | hu | 🇭🇺 | Korean | ko | 🇰🇷 |
| Russian | ru | 🇷🇺 | Persian (Farsi) | fa | 🇮🇷 | Arabic | ar | 🇸🇦 |
| Polish | pl | 🇵🇱 | Portuguese | pt | 🇵🇹 | Czech | cs | 🇨🇿 |
| Danish | da | 🇩🇰 | Swedish | sv | 🇸🇪 | Greek | el | 🇬🇷 |
| Turkish | tr | 🇹🇷 |  |  |  |  |  |  |

## Quickstart

### Environment Setup

We recommend a clean Python environment first, then installing the project in editable mode so the `moss-tts-nano` command becomes available locally.
The examples below intentionally keep arguments minimal and rely on the repository defaults.
By default, the code loads `OpenMOSS-Team/MOSS-TTS-Nano` and `OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano`.

#### Using Conda

```bash
conda create -n moss-tts-nano python=3.12 -y
conda activate moss-tts-nano

git clone https://github.com/OpenMOSS/MOSS-TTS-Nano.git
cd MOSS-TTS-Nano

pip install -r requirements.txt
pip install -e .
```

If `WeTextProcessing` or `pynini` fails to install from `requirements.txt`, install `pynini` first in the same environment, then install `WeTextProcessing`, remove `WeTextProcessing` from `requirements.txt`, and finally rerun `pip install -r requirements.txt`.

With Conda, we recommend:

```bash
conda install -c conda-forge pynini=2.1.6.post1 -y
pip install git+https://github.com/WhizZest/WeTextProcessing.git
pip install -r requirements.txt
```

If you are not using Conda, make sure you download a `pynini` wheel that matches your Python version and platform before installing `WeTextProcessing`. For a community-tested example, see [Issue #6](https://github.com/OpenMOSS/MOSS-TTS-Nano/issues/6).

### Voice Clone with `infer.py`

This repository keeps the direct Python entrypoint for local inference. The example below uses **voice clone mode**, which is the main recommended workflow for MOSS-TTS-Nano.

```bash
python infer.py \
  --prompt-audio-path assets/audio/zh_1.wav \
  --text "欢迎关注模思智能、上海创智学院与复旦大学自然语言处理实验室。"
```

This writes audio to `generated_audio/infer_output.wav` by default.

### Local Web Demo with `app.py`

You can launch the local FastAPI demo for browser-based testing:

```bash
python app.py
```

Then open `http://127.0.0.1:18083` in your browser.

<a id="onnx-cpu-version"></a>

### ONNX CPU Inference

We now strongly recommend trying the **ONNX CPU version** first for lightweight local deployment and CPU inference.

This version is designed to be

# FILE: README_zh.md

# MOSS-TTS-Nano

<br>

<p align="center">
  <img src="./assets/images/OpenMOSS_Logo.png" height="70" align="middle" />
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="./assets/images/mosi-logo.png" height="50" align="middle" />
</p>

<div align="center">
  <a href="https://clawhub.ai/luogao2333/moss-tts-voice"><img src="https://img.shields.io/badge/🦞_OpenClaw-Skills-8A2BE2" alt="OpenClaw"></a>
  <a href="https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano"><img src="https://img.shields.io/badge/Huggingface-Models-orange?logo=huggingface&amp"></a>
  <a href="https://modelscope.cn/collections/OpenMOSS-Team/MOSS-TTS-Nano"><img src="https://img.shields.io/badge/ModelScope-Models-7B61FF?logo=modelscope&amp;logoColor=white"></a>
  <a href="https://openmoss.github.io/MOSS-TTS-Nano-Demo/"><img src="https://img.shields.io/badge/Blog-View-blue?logo=internet-explorer&amp"></a>
  <a href="https://arxiv.org/abs/2603.18090"><img src="https://img.shields.io/badge/Arxiv-2603.18090-red?logo=arxiv&amp"></a>
  <a href="https://studio.mosi.cn/experiments/moss-tts-nano"><img src="https://img.shields.io/badge/AIStudio-Try-green?logo=internet-explorer&amp"></a>
  <a href="https://studio.mosi.cn/docs/moss-tts-nano"><img src="https://img.shields.io/badge/API-Docs-00A3FF?logo=fastapi&amp"></a>
  <a href="https://x.com/Open_MOSS"><img src="https://img.shields.io/badge/Twitter-Follow-black?logo=x&amp"></a>
  <a href="https://discord.gg/Xf3aXddCjc"><img src="https://img.shields.io/badge/Discord-Join-5865F2?logo=discord&amp"></a>
  <a href="./assets/images/wechat.jpg"><img src="https://img.shields.io/badge/WeChat-Join-07C160?logo=wechat&amp;logoColor=white" alt="WeChat"></a>
</div>

[English](README.md) | [简体中文](README_zh.md)

MOSS-TTS-Nano 是来自 [MOSI.AI](https://mosi.cn/#hero) 和 [OpenMOSS 团队](https://www.open-moss.com/) 的开源**多语言微型语音生成模型**。仅包含 **0.1B 参数**，专为**实时语音生成**设计，可直接在 **CPU 上运行（无需 GPU）**，并保持部署栈足够简单，适用于本地演示、网络服务和轻量级产品集成。

## MOSS-TTS 2.0 需求收集

MOSS-TTS 2.0 即将到来。为了更好地优化模型能力和产品体验，我们想收集大家在使用 TTS 过程中的反馈与建议。希望大家能够花 2-3 分钟填写[需求收集表](https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef)，欢迎各种意义上的需求说明，包括许愿！

<p align="center">
  <a href="https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef">
    <img src="./assets/images/moss_tts_2_requirements_gathering.jpg" width="360" alt="MOSS-TTS 2.0 需求收集二维码" />
  </a>
</p>

[demo_video.mp4](https://github.com/user-attachments/assets/25aca215-0bd7-4d0c-be95-8d1f6737aec8)

## 新闻

* 2026.5.6：**MOSS-TTS**、**MOSS-TTS-Nano** 和 **MOSS-Audio-Tokenizer** 现已支持 [**mlx-audio**](https://github.com/Blaizzy/mlx-audio)，详情请访问 [mlx-audio GitHub 仓库](https://github.com/Blaizzy/mlx-audio)。
* 2026.4.29：MOSS-TTS 2.0 即将到来！我们正在通过[需求收集表](https://acnc6zeentra.feishu.cn/share/base/form/shrcnyAe1LwqKWjCSuW4wiZ2Hef)收集大家在使用 TTS 过程中的反馈、建议与功能需求。
* 2026.4.27：我们新增了 [**MOSS-Audio-Tokenizer-Nano**](#moss-audio-tokenizer-nano) 的最新评测结果，包括在语音、音频和音乐基准上的重建质量对比。
* 2026.4.17：我们很高兴发布更加高效且可独立运行的 [**ONNX CPU 版本**](#onnx-cpu-version)，对应 Hugging Face 仓库 [**MOSS-TTS-Nano-100M-ONNX**](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano-100M-ONNX) 与 [**MOSS-Audio-Tokenizer-Nano-ONNX**](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX)。该版本在推理阶段不再依赖 PyTorch，完整保留音色克隆工作流；根据我们的实测，其处理效率较原版接近翻倍，并且在 **MacBook Air M4** 上仅使用 **1 核 CPU** 即可流畅运行。基于这一 ONNX CPU 版本，我们也同步更新了 [**MOSS-TTS-Nano-Reader**](https://github.com/OpenMOSS/MOSS-TTS-Nano-Reader)，现在可以直接以浏览器插件的形式在浏览器内运行本模型，无需再在本地单独部署推理服务。
* 2026.4.16：我们发布了 **MOSS-TTS-Nano 微调代码**。训练和使用说明见 [./finetuning/README_zh.md](./finetuning/README_zh.md)。
* 2026.4.14：我们发布了 [**MOSS-TTS-Nano-Reader**](https://github.com/OpenMOSS/MOSS-TTS-Nano-Reader)，这是一个基于 **MOSS-TTS-Nano** 的本地浏览器网页朗读应用。
* 2026.4.10：我们发布了 **MOSS-TTS-Nano**。演示 Space 已在 [OpenMOSS-Team/MOSS-TTS-Nano](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS-Nano) 上线，也可以通过 [openmoss.github.io/MOSS-TTS-Nano-Demo/](https://openmoss.github.io/MOSS-TTS-Nano-Demo/) 查看 demo 和更多细节。

## 演示

- 在线演示：[https://openmoss.github.io/MOSS-TTS-Nano-Demo/](https://openmoss.github.io/MOSS-TTS-Nano-Demo/)
- Hugging Face Space：[OpenMOSS-Team/MOSS-TTS-Nano](https://huggingface.co/spaces/OpenMOSS-Team/MOSS-TTS-Nano)

## 目录

- [新闻](#新闻)
- [演示](#演示)
- [介绍](#介绍)
  - [主要特性](#主要特性)
- [支持的语言](#支持的语言)
- [快速开始](#快速开始)
  - [环境配置](#环境配置)
  - [使用 `infer.py` 进行语音克隆](#使用-inferpy-进行语音克隆)
  - [使用 `app.py` 启动本地-web-演示](#使用-apppy-启动本地-web-演示)
  - [ONNX CPU 版本](#onnx-cpu-version)
  - [导出仅 TTS 的 ONNX 权重](#导出仅-tts-的-onnx-权重)
  - [CLI 命令：`moss-tts-nano generate`](#cli-命令-moss-tts-nano-generate)
  - [CLI 命令：`moss-tts-nano serve`](#cli-命令-moss-tts-nano-serve)
  - [微调](#微调)
- [MOSS-Audio-Tokenizer-Nano](#moss-audio-tokenizer-nano)
- [MOSS-TTS 家族](#moss-tts)
- [许可证](#许可证)
- [引用](#引用)
- [Star 历史](#star-历史)

## 介绍

<p align="center">
  <img src="./assets/images/concept.png" alt="MOSS-TTS-Nano concept" width="85%" />
</p>

MOSS-TTS-Nano 专注于 TTS 部署中最重要的部分：**小体积**、**低延迟**、**足够好的实时产品质量** 和 **简单的本地配置**。它使用纯自回归 **Audio Tokenizer + LLM** 管道，并保持推理工作流对终端用户和网络演示用户都友好。

### 主要特性

- **超小模型尺寸**：仅 **0.1B 参数**
- **原生音频格式**：**48 kHz**、**2 声道**输出
- **多语言支持**：支持 **中文、英文等多种语言**
- **纯自回归架构**：基于 **Audio Tokenizer + LLM**
- **流式推理**：低实时延迟和快速首字节音频
- **CPU 友好**：流式生成可在 **4 核 CPU** 上运行
- **长文本支持**：支持长输入，具有自动分块语音克隆
- **开源部署**：支持直接 `python infer.py`、`python app.py` 和打包 CLI

<p align="center">
  <img src="./assets/images/arch_moss_tts_nano.png" alt="MOSS-TTS-Nano architecture" width="80%" />
  <br />
  MOSS-TTS-Nano 架构图
</p>

## 支持的语言

MOSS-TTS-Nano 目前支持 **20 种语言**：

| 语言 | 代码 | 旗帜 | 语言 | 代码 | 旗帜 | 语言 | 代码 | 旗帜 |
|---|---|---|---|---|---|---|---|---|
| 中文 | zh | 🇨🇳 | 英文 | en | 🇺🇸 | 德语 | de | 🇩🇪 |
| 西班牙语 | es | 🇪🇸 | 法语 | fr | 🇫🇷 | 日语 | ja | 🇯🇵 |
| 意大利语 | it | 🇮🇹 | 匈牙利语 | hu | 🇭🇺 | 韩语 | ko | 🇰🇷 |
| 俄语 | ru | 🇷🇺 | 波斯语 (Farsi) | fa | 🇮🇷 | 阿拉伯语 | ar | 🇸🇦 |
| 波兰语 | pl | 🇵🇱 | 葡萄牙语 | pt | 🇵🇹 | 捷克语 | cs | 🇨🇿 |
| 丹麦语 | da | 🇩🇰 | 瑞典语 | sv | 🇸🇪 | 希腊语 | el | 🇬🇷 |
| 土耳其语 | tr | 🇹🇷 |  |  |  |  |  |  |

## 快速开始

### 环境配置

我们建议先创建一个干净的 Python 环境，然后以可编辑模式安装项目，使得 `moss-tts-nano` 命令在本地可用。下面的示例故意保持参数最少，依赖仓库默认设置。默认情况下，代码加载 `OpenMOSS-Team/MOSS-TTS-Nano` 和 `OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano`。

#### 使用 Conda

```bash
conda create -n moss-tts-nano python=3.12 -y
conda activate moss-tts-nano

git clone https://github.com/OpenMOSS/MOSS-TTS-Nano.git
cd MOSS-TTS-Nano

pip install -r requirements.txt
pip install -e .
```

如果 `WeTextProcessing` 或 `pynini` 无法从 `requirements.txt` 安装，请先在同一环境中安装 `pynini`，再安装 `WeTextProcessing`，然后从 `requirements.txt` 中移除 `WeTextProcessing`，最后重新执行 `pip install -r requirements.txt`。

推荐优先使用 Conda：

```bash
conda install -c conda-forge pynini=2.1.6.post1 -y
pip install git+https://github.com/WhizZest/WeTextProcessing.git
pip install -r requirements.txt
```

如果不使用 Conda，请先准备与当前 Python 版本和平台匹配的 `pynini` wheel，再安装 `WeTextProcessing`。可参考 [Issue #6](https://github.com/OpenMOSS/MOSS-TTS-Nano/issues/6) 中给出的安装示例。

### 使用 `infer.py` 进行语音克隆

本仓库保留了直接 Python 入口点用于本地推理。下面的示例使用 **语音克隆模式**，这是 MOSS-TTS-Nano 的主要推荐工作流。

```bash
python infer.py \
  --prompt-audio-path assets/audio/zh_1.wav \
  --text "欢迎关注模思智能、上海创智学院与复旦大学自然语言处理实验室。"
```

默认情况下，这会将音频写入 `generated_audio/infer_output.wav`。

### 使用 `app.py` 启动本地 Web 演示

您可以启动本地 FastAPI 演示进行基于浏览器的测试：

```bash
python app.py
```

然后在浏览器中打开 `http://127.0.0.1:18083`。

<a id="onnx-cpu-version"></a>

## ONNX CPU 版本

我们现在十分推荐优先尝试 **ONNX CPU 版本**，尤其适合轻量本地部署和纯 CPU 推理场景。

这一版本在保留 MOSS-TTS-Nano 核心体验的同时，更适合直接部署：

- **推理阶段不依赖 PyTorch**：直接基于 ONNX Runtime CPU 运行。
- **可独立运行、部署更轻量**：适合本地 demo、服务化和轻量集成。
- **完整保留语音克隆能力**：支持直接参考音频输入、内置音色和 `Realtime Streaming Decode`。
- **速度更快**：根据我们的实测，处理效率较原版**接近翻倍**。
- **单核可用性更强**：在 **MacBook Air M4** 上，仅使用 **1 核 CPU** 即可流畅运行。

对应的 ONNX 入口包括 `infer_onnx.py`、`app_onnx.py`，以及带 `--backend onnx` 的打包 CLI。

默认情况下，基于 ONNX Runtime CPU 运行，如果要切换到 GPU，需要安装 `onnxruntime-gpu`，然后可以通过 `--execution-provider cuda` 显式切到 CUDA。

如果要准备 CUDA ONNX Runtime 环境，请把 CPU 版 ONNX Runtime wheel 替换成 GPU 版：

```bash
pip uninstall -y onnxruntime
pip install "onnxruntime-gpu>=1.20.0"
```

如果不传 `--model-dir`，程序会默认检查 `./models`。当该目录下缺少模型时，会在首次运行时自动从下面两个 Hugging Face 仓库下载：

- [OpenMOSS-Team/MOSS-TTS-Nano-100M-ONNX](https://huggingface.co/OpenMOSS-Team/MOSS-TTS-Nano-100M-ONNX)
- [OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-Nano-ONNX)

默认下载后的目录结构为：

- `models/MOSS-TTS-Nano-100M-ONNX`
- `models/MOSS-Audio-Tokenizer-Nano-ONNX`

命令行示例：

```bash
python infer_onnx.py \
  --prompt-audio-path assets/audio/zh_1.wav \
  --text "欢迎使用 ONNX Runtime CPU 版本。"
```

如果你已经有本地导出的 ONNX 目录，也可以显式传入：

```bash
python infer_onnx.py \
  --model-dir /path/to/models \
  --prompt-audio-path assets/audio/zh_1.wav \
  --text "欢迎使用 ONNX Runtime CPU 版本。"
```

如果要使用 CUDA 推理：

```bash
python infer_onnx.py \
  --execution-provider cuda \
  --prompt-audio-path assets/audio/zh_1.wav \
  --text "欢迎使用 ONNX Runtime CUDA 版本。"
```

CUDA 推理需要安装 `onnxruntime-gpu`。

本地 Web Demo：

```bash
python app_onnx.py
```

如果要用 CUDA 启动 ONNX Web Demo：

```bash
python app_onnx.py \
  --execution-provider cuda
```

然后在浏览器中打开 `http://127.0.0.1:18083`。

首次启动如果本地没有 ONNX 权重，会先自动下载。

### 导出仅 TTS 的 ONNX 权重

如果重新训练了 `MOSS-TTS-Nano`，那么需要重导 TTS 侧 ONNX 权重。[`onnx/`](./onnx) 目录下的导出脚本接收本地 Hugging Face 格式的 `MOSS-TTS-Nano` checkpoint，并输出一套仅包含 TTS 侧文件的 ONNX 模型目录。

示例：

```bash
python onnx/export_hf_to_tts_onnx.py \
  --checkpoint-path /path/to/MOSS-TTS-Nano \
  --output-dir /path/to/MOSS-TTS-Nano-100M-ONNX
```

输出目录包含：

- `moss_tts_prefill.onnx`
- `moss_tts_decode_step.onnx`
- `moss_tts_local_decoder.onnx`
- `moss_tts_local_cached_step.onnx`
- `moss_tts_local_fixed_sampled_frame.onnx`
- `moss_tts_global_shared.data`
- `moss_tts_local_shared.data`
- `tts_browser_onnx_meta.json`
- `tokenizer.model`

这个脚本面向 ONNX 部署链路。只要 `MOSS-Audio-Tokenizer-Nano` 没变，原先基于它生成的 prompt audio codes 不需要重新生成。

### CLI 命令：`moss-tts-nano generate`

安装后 `pip install -e .`，您可以直接调用打包的 CLI：

```bash
moss-tts-nano generate \
  --prompt-speech assets/audio/zh_1.wav \
  --text "欢迎关注模思智能、上海创智学院与复旦大学自然语言处理实验室。"
```

如果要切到 ONNX CPU 后端，只需加上 `--backend 
