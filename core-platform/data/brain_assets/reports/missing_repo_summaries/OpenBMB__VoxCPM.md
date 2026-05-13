# Missing Repo Summary Source: OpenBMB/VoxCPM

- URL: https://github.com/OpenBMB/VoxCPM
- Local Path: VoxCPM
- Clone Status: local_existing
- Language: Python
- Stars: 18517
- Topics: audio, deeplearning, minicpm, multilingual, python, pytorch, speech, speech-synthesis, text-to-speech, tts, tts-model, voice-cloning, voice-design, voxcpm
- Description: VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning

## Extracted README / Docs / Examples


# FILE: README.md

<h2 align="center">VoxCPM2: Tokenizer-Free TTS for Multilingual Speech Generation, Creative Voice Design, and True-to-Life Cloning</h2>

<p align="center">
  <b>English</b> | <a href="./README_zh.md">中文</a>
</p>

<p align="center">
  <a href="https://github.com/OpenBMB/VoxCPM/"><img src="https://img.shields.io/badge/Project%20Page-GitHub-blue" alt="Project Page"></a>
  <a href="https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo"><img src="https://img.shields.io/badge/Live%20Playground-Demo-orange" alt="Live Playground"></a>
  <a href="https://voxcpm.readthedocs.io/en/latest/"><img src="https://img.shields.io/badge/Docs-ReadTheDocs-8CA1AF" alt="Documentation"></a>
  <a href="https://huggingface.co/openbmb/VoxCPM2"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-VoxCPM2-yellow" alt="Hugging Face"></a>
  <a href="https://modelscope.cn/models/OpenBMB/VoxCPM2"><img src="https://img.shields.io/badge/ModelScope-VoxCPM2-purple" alt="ModelScope"></a>
  <a href="https://openbmb.github.io/voxcpm2-demopage/"><img src="https://img.shields.io/badge/DemoPage-Audio Samples-red"></a>

</p>

<div align="center">
  <img src="assets/voxcpm_logo.png" alt="VoxCPM Logo" width="35%">
  <br><br>
  <a href="https://trendshift.io/repositories/17704" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17704" alt="OpenBMB%2FVoxCPM | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<br>

<p align="center">
  👋 Join our community for discussion and support!
  <br>
  <a href="./assets/feishu-group.png" style="display:inline-block;vertical-align:middle; margin-left: 10px;">
    <img src="./assets/feishu-logo.png" width="16" height="16" style="vertical-align:middle;"> Feishu
  </a>
  &nbsp;|&nbsp;
  <a href="https://discord.gg/KZUx7tVNwz" style="display:inline-block;vertical-align:middle;">
    <img src="./assets/discord-logo.png" width="16" height="16" style="vertical-align:middle;"> Discord
  </a>
</p>

VoxCPM is a **tokenizer-free** Text-to-Speech system that directly generates continuous speech representations via an end-to-end **diffusion autoregressive architecture**, bypassing discrete tokenization to achieve highly natural and expressive synthesis.

**VoxCPM2** is the latest major release — a **2B** parameter model trained on **over 2 million hours** of multilingual speech data, now supporting **30 languages**, **Voice Design**, **Controllable Voice Cloning**, and **48kHz** studio-quality audio output. Built on a [MiniCPM-4](https://github.com/OpenBMB/MiniCPM) backbone.

### ✨ Highlights

- 🌍 **30-Language Multilingual** — Input text in any of the 30 supported languages and synthesize directly, no language tag needed
- 🎨 **Voice Design** — Create a brand-new voice from a natural-language description alone (gender, age, tone, emotion, pace …), no reference audio required
- 🎛️ **Controllable Cloning** — Clone any voice from a short reference clip, with optional style guidance to steer emotion, pace, and expression while preserving the original timbre
- 🎙️ **Ultimate Cloning** — Reproduce every vocal nuance: provide both reference audio and its transcript, and the model continues seamlessly from the reference, faithfully preserving every vocal detail — timbre, rhythm, emotion, and style (same as VoxCPM1.5)
- 🔊 **48kHz High-Quality Audio** — Accepts 16kHz reference audio and directly outputs 48kHz studio-quality audio via AudioVAE V2's asymmetric encode/decode design, with built-in super-resolution — no external upsampler needed
- 🧠 **Context-Aware Synthesis** — Automatically infers appropriate prosody and expressiveness from text content
- ⚡ **Real-Time Streaming** — RTF as low as ~0.3 on NVIDIA RTX 4090, and ~0.13  accelerated by [Nano-VLLM](https://github.com/a710128/nanovllm-voxcpm)
- 📜 **Fully Open-Source & Commercial-Ready** — Weights and code released under the [Apache-2.0](LICENSE) license, free for commercial use


<summary><b>🌍 Supported Languages (30)</b></summary>
<br>
Arabic, Burmese, Chinese, Danish, Dutch, English, Finnish, French, German, Greek, Hebrew, Hindi, Indonesian, Italian, Japanese, Khmer, Korean, Lao, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swahili, Swedish, Tagalog, Thai, Turkish, Vietnamese

Chinese Dialect: 四川话, 粤语, 吴语, 东北话, 河南话, 陕西话, 山东话, 天津话, 闽南话


### News

* **[2026.04]** 🔥 We release **VoxCPM2** — 2B, 30 languages, Voice Design & Controllable Voice Cloning, 48kHz audio output! [Weights](https://huggingface.co/openbmb/VoxCPM2) | [Docs](https://voxcpm.readthedocs.io/en/latest/) | [Playground](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo)
* **[2025.12]** 🎉 Open-source **VoxCPM1.5** [weights](https://huggingface.co/openbmb/VoxCPM1.5) with SFT & LoRA fine-tuning. (**🏆 #1 GitHub Trending**)
* **[2025.09]** 🔥 Release VoxCPM [Technical Report](https://arxiv.org/abs/2509.24650).
* **[2025.09]** 🎉 Open-source **VoxCPM-0.5B** [weights](https://huggingface.co/openbmb/VoxCPM-0.5B) (**🏆 #1 HuggingFace Trending**)

---

## Contents

- [Quick Start](#-quick-start)
  - [Installation](#installation)
  - [Python API](#python-api)
  - [CLI Usage](#cli-usage)
  - [Web Demo](#web-demo)
  - [Production Deployment](#-production-deployment-nano-vllm)
- [Models & Versions](#-models--versions)
- [Performance](#-performance)
- [Fine-tuning](#%EF%B8%8F-fine-tuning)
- [Documentation](#-documentation)
- [Ecosystem & Community](#-ecosystem--community)
- [Risks and Limitations](#%EF%B8%8F-risks-and-limitations)
- [Citation](#-citation)

---

## 🚀 Quick Start

### Installation

```sh
pip install voxcpm
```

> **Requirements:** Python ≥ 3.10 (<3.13), PyTorch ≥ 2.5.0, CUDA ≥ 12.0. See [Quick Start Docs](https://voxcpm.readthedocs.io/en/latest/quickstart.html) for details.

### Python API

#### 🗣️ Text-to-Speech

```python
from voxcpm import VoxCPM
import soundfile as sf

model = VoxCPM.from_pretrained(
  "openbmb/VoxCPM2",
  load_denoiser=False,
)

wav = model.generate(
    text="VoxCPM2 is the current recommended release


# FILE: README_zh.md

<h2 align="center">VoxCPM2：基于连续表征的多语言语音合成、创意音色设计与高保真声音克隆</h2>

<p align="center">
  <a href="./README.md">English</a> | <b>中文</b>
</p>

<p align="center">
  <a href="https://github.com/OpenBMB/VoxCPM/"><img src="https://img.shields.io/badge/Project%20Page-GitHub-blue" alt="Project Page"></a>
  <a href="https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo"><img src="https://img.shields.io/badge/Live%20Playground-Demo-orange" alt="Live Playground"></a>
  <a href="https://voxcpm.readthedocs.io/zh-cn/latest/"><img src="https://img.shields.io/badge/Docs-ReadTheDocs-8CA1AF" alt="Documentation"></a>
  <a href="https://huggingface.co/openbmb/VoxCPM2"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-VoxCPM2-yellow" alt="Hugging Face"></a>
  <a href="https://modelscope.cn/models/OpenBMB/VoxCPM2"><img src="https://img.shields.io/badge/ModelScope-VoxCPM2-purple" alt="ModelScope"></a>
  <a href="https://openbmb.github.io/voxcpm2-demopage/"><img src="https://img.shields.io/badge/DemoPage-Audio Samples-red"></a>

</p>

<div align="center">
  <img src="assets/voxcpm_logo.png" alt="VoxCPM Logo" width="35%">
  <br><br>
  <a href="https://trendshift.io/repositories/17704" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17704" alt="OpenBMB%2FVoxCPM | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

<br>

<p align="center">
  👋 欢迎加入社区，参与讨论与交流！
  <br>
  <a href="./assets/feishu-group.png" style="display:inline-block;vertical-align:middle; margin-left: 10px;">
    <img src="./assets/feishu-logo.png" width="16" height="16" style="vertical-align:middle;"> 飞书群
  </a>
  &nbsp;|&nbsp;
  <a href="https://discord.gg/KZUx7tVNwz" style="display:inline-block;vertical-align:middle;">
    <img src="./assets/discord-logo.png" width="16" height="16" style="vertical-align:middle;"> Discord
  </a>
</p>

VoxCPM 是一个**无离散音频分词器**（Tokenizer-Free）的语音合成系统，通过端到端的**扩散自回归架构**直接生成连续语音表征，绕过对音频的离散编码步骤，实现高度自然且富有表现力的语音合成。

**VoxCPM2** 是最新的版本 — 基于 [MiniCPM-4](https://github.com/OpenBMB/MiniCPM) 基座构建，总计 **20亿** 参数，在超过 **200万小时** 的多语种音频数据上训练，支持 **30种全球语言+9种中文方言**、**音色设计**、**可控声音克隆**，原生输出 **48kHz** 高质量音频。

### ✨ 核心特性

- 🌍 **30种语言语音合成** — 直接输入原始文本即可合成（支持语言详见下文），无需额外语言标签
- 🎨 **音色设计** — 用自然语言描述（性别、年龄、音色、情绪、语速……）凭空创建全新音色，无需参考音频
- 🎛️ **可控声音克隆** — 从参考音频片段克隆任意声音，可叠加风格指令控制情绪、语速和表现力，同时保持原始音色
- 🎙️ **极致克隆** — 提供参考音频及其文本内容，模型接着参考音频进行无缝续写，从而精准还原声音细节特征（与 VoxCPM1.5 一致）
- 🔊 **48kHz 高质量音频** — 输入 16kHz 参考音频，通过 AudioVAE V2 的非对称编解码设计直接输出 48kHz 高质量音频，内置超分能力
- 🧠 **语境感知合成** — 根据文本内容自动推断合适的韵律和表现力
- ⚡ **实时流式合成** — 在 NVIDIA RTX 4090 上 RTF 低至 ~0.3，通过 [Nano-VLLM](https://github.com/a710128/nanovllm-voxcpm) 加速后可达 ~0.13
- 📜 **完全开源，商用就绪** — 权重和代码基于 [Apache-2.0](LICENSE) 协议发布，免费商用

<summary><b>🌍 支持的语言（30种）</b></summary>
<br>
阿拉伯语、缅甸语、中文、丹麦语、荷兰语、英语、芬兰语、法语、德语、希腊语、希伯来语、印地语、印尼语、意大利语、日语、高棉语、韩语、老挝语、马来语、挪威语、波兰语、葡萄牙语、俄语、西班牙语、斯瓦希里语、瑞典语、菲律宾语、泰语、土耳其语、越南语

中国方言：四川话、粤语、吴语、东北话、河南话、陕西话、山东话、天津话、闽南话


### 最新动态

* **[2026.04]** 🔥 发布 **VoxCPM2** — 20亿参数，30种语言，音色设计与可控声音克隆，48kHz 音频输出！[模型权重](https://huggingface.co/openbmb/VoxCPM2) | [使用文档](https://voxcpm.readthedocs.io/zh-cn/latest/) | [在线体验](https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo) | [官网体验](https://voxcpm.modelbest.cn/) (适用国内访问)
* **[2025.12]** 🎉 开源 **VoxCPM1.5** [模型权重](https://huggingface.co/openbmb/VoxCPM1.5)，支持 SFT 和 LoRA 微调。(**🏆 GitHub Trending #1**)
* **[2025.09]** 🔥 发布 VoxCPM [技术报告](https://arxiv.org/abs/2509.24650)。
* **[2025.09]** 🎉 开源 **VoxCPM-0.5B** [模型权重](https://huggingface.co/openbmb/VoxCPM-0.5B) (**🏆 HuggingFace Trending #1**)

---

## 目录

- [快速开始](#-快速开始)
  - [安装](#安装)
  - [Python API](#python-api)
  - [命令行使用](#命令行使用)
  - [Web Demo](#web-demo)
  - [生产部署](#-生产部署nano-vllm)
- [模型与版本](#-模型与版本)
- [性能评测](#-性能评测)
- [微调](#%EF%B8%8F-微调)
- [文档](#-文档)
- [生态与社区](#-生态与社区)
- [风险与局限性](#%EF%B8%8F-风险与局限性)
- [引用](#-引用)

---

## 🚀 快速开始

### 安装

```sh
pip install voxcpm
```

> **环境要求：** Python ≥ 3.10 (<3.13)，PyTorch ≥ 2.5.0，CUDA ≥ 12.0。详见 [快速开始文档](https://voxcpm.readthedocs.io/zh-cn/latest/quickstart.html)。

### Python API

#### 🗣️ 文本转语音

```python
from voxcpm import VoxCPM
import soundfile as sf

model = VoxCPM.from_pretrained(
  "openbmb/VoxCPM2",
  load_denoiser=False,
)

wav = model.generate(
    text="VoxCPM2 是目前推荐使用的多语言语音合成版本。",
    cfg_value=2.0,
    inference_timesteps=10,
)
sf.write("demo.wav", wav, model.tts_model.sample_rate)
print("已保存: demo.wav")
```

如果你希望先从 ModelScope 下载模型到本地（适用于国内网络访问），可以使用：

```bash
pip install modelscope
```

```python
from modelscope import snapshot_download
snapshot_download("OpenBMB/VoxCPM2", local_dir='./pretrained_models/VoxCPM2') # 指定模型保存的本地路径

from voxcpm import VoxCPM
import soundfile as sf
model = VoxCPM.from_pretrained('./pretrained_models/VoxCPM2', load_denoiser=False)

wav = model.generate(
    text="VoxCPM2 是目前推荐使用的多语言语音合成版本。",
    cfg_value=2.0,
    inference_timesteps=10,
)
sf.write("demo.wav", wav, model.tts_model.sample_rate)
```

#### 🎨 音色设计

用自然语言描述创建全新音色，无需参考音频。**格式：** 在 `text` 开头用括号写入音色描述（如 `"(音色描述)要合成的文本。"`）：

```python
wav = model.generate(
    text="(年轻女性，声音温柔甜美)你好，欢迎使用VoxCPM2！",
    cfg_value=2.0,
    inference_timesteps=10,
)
sf.write("voice_design.wav", wav, model.tts_model.sample_rate)
```

#### 🎛️ 可控声音克隆

上传一段参考音频，模型克隆其音色，同时可以使用控制指令调节语速、情绪或风格。

```python
wav = model.generate(
    text="这是VoxCPM2生成的克隆语音。",
    reference_wav_path="path/to/voice.wav",
)
sf.write("clone.wav", wav, model.tts_model.sample_rate)

wav = model.generate(
    text="(稍快一点，欢快的语气)这是带风格控制的克隆语音。",
    reference_wav_path="path/to/voice.wav",
    cfg_value=2.0,
    inference_timesteps=10,
)
sf.write("controllable_clone.wav", wav, model.tts_model.sample_rate)
```

#### 🎙️ 极致克隆

提供参考音频及其精确文本转录，实现基于音频续写的高保真克隆。为获得最高克隆相似度，可将同一音频同时传给 `reference_wav_path` 和 `prompt_wav_path`：

```python
wav = model.generate(
    text="这是使用VoxCPM2的极致克隆演示。",
    prompt_wav_path="path/to/voice.wav",
    prompt_text="参考音频的文本转录。",
    reference_wav_path="path/to/voice.wav",  # 可选，提升相似度
)
sf.write("hifi_clone.wav", wav, model.tts_model.sample_rate)
```

<details>
<
