# Missing Repo Summary Source: jingyaogong/minimind-o

- URL: https://github.com/jingyaogong/minimind-o
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/jingyaogong__minimind-o
- Clone Status: cloned
- Language: Python
- Stars: 1094
- Topics: artificial-intelligence, chatgpt, omni
- Description: 🎙️ 「大模型」从0训练0.1B能听能说能看的全模态Omni模型！A 0.1B Omni model trained from scratch, capable of listening, speaking, and seeing!

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">

![logo](./images/logo.png)

</div>


<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind-o)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind-o?style=social)](https://github.com/jingyaogong/minimind-o/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind-o?v=1)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind-o)](https://github.com/jingyaogong/minimind-o/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind-o/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind--O%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-o)
[![Technical Report](https://img.shields.io/badge/Technical%20Report-arXiv-red)](http://arxiv.org/abs/2605.03937)

</div>

<div align="center">
  <h3>"大道至简"</h3>
</div>

<div align="center">

中文 | [English](./README_en.md)

</div>

* 此开源项目旨在从 0 完整实现一个小规模的端到端 Omni 模型，单一权重同时支持文 / 音 / 图三模态输入与文本 / 流式语音输出。
* 其中 `minimind-3o` 仅 ~0.1B，普通个人 GPU 即可完成训练、CPU即可快速推理，是当前公开模型中规模最小的完整 Omni 实现（或之一）。
* 开源 mini 与 full 两套训练数据：mini 单卡 3090 上约 2 小时跑通完整链路，便于入门；full 与发布权重对应。
* 开源 Omni 模型的完整代码与技术报告，覆盖 Thinker–Talker 双路径、流式语音生成、实时打断、近似双工交互、音色克隆与电话模式 WebUI。
* 所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖三方框架提供的高层抽象。
* MiniMind-O 进一步延续了 [MiniMind](https://github.com/jingyaogong/minimind)（语言）与 [MiniMind-V](https://github.com/jingyaogong/minimind-v)（视觉多模态）的设计范式。

> 注："约 2 小时" 指 mini 数据集在单张 NVIDIA RTX 3090 上跑完 SFT 的实测耗时。

---

<div align="center">

[📄 MiniMind-O Technical Report](http://arxiv.org/abs/2605.03937)

https://github.com/user-attachments/assets/10cbcc5f-4e70-45cf-bdc5-d6361e40bb86

[🔗 在线体验 (Gradio)](https://modelscope.cn/studios/gongjy/MiniMind-O) &nbsp;|&nbsp; [🔗 视频介绍](https://www.bilibili.com/video/BV1V1RsBcEMX)


</div>

---

# 📌 项目介绍

继 [MiniMind](https://github.com/jingyaogong/minimind)（LLM）和 [MiniMind-V](https://github.com/jingyaogong/minimind-v)（VLM）之后，MiniMind-O 是这个系列的第三站。所谓 Omni，就是让一个模型同时具备听、看、说的多模态交互能力：接收文本、语音和视觉信号，输出文本与流式语音。

或许 GPT-4o 让人第一次感受到足够自然的流式语音交互形态，随后 Mini-Omni2、Moshi、GLM-4-Voice、Qwen3-Omni 等开源工作陆续出现。但如果目标不是直接调用这些参数庞大的现成权重，而是从 0 读懂、训练、改动一个完整 Omni 模型，开源社区仍然急缺足够轻量、链路完整的起点。要把语音真正纳入 Omni 模型，一种做法是把 ASR、LLM、TTS 串成级联链路：语音先转文字，LLM 处理后再合成语音。这条路工程上直接，但中间多了一次文本转写，延迟、语气和情绪信息都会受到影响。

MiniMind-O 尝试补上已知的空位：让语音和文本在 hidden state 层面直接连通，在主 backbone 仅 0.1B 的规模下保留端到端 Omni 链路。Talker 侧采用 MTP（Multi-Token Prediction）一次预测多层 Mimi codes，再配合 VAD 支持实时打断与近似双工交互，这是足够实用的工程路线之一。本项目的代码、模型权重、训练数据和技术报告全部完整开源，单张 RTX 3090 上约 2 小时即可跑通 mini 数据集训练。目标依旧：让每个人都能从第一行代码读起，自己动手，从 0 训练一个能听、能看、能思考、能说的模型：

![](images/omni_io_flow.png)

😊 一起感受创造的乐趣吧！

---

#### 🎉 项目包含以下内容

- 提供完整的 MiniMind-O 结构代码：Thinker、独立 Talker、audio / vision projector、Mimi codebook 接口以及 MTP audio head。
- 提供 SFT 全链路训练流程，覆盖 T2A、I2T、A2A 三类数据，支持全参数训练、音频投影层训练、视觉投影层训练与 DDP 多卡训练。
- 提供 mini 与 full 两套训练数据：mini 便于快速入门，单卡 3090 上约 2 小时可跑通；full 与发布权重对应，覆盖中文语音与图像任务。
- 提供多种内置音色、unseen 音色与任意参考音频的音色克隆能力，便于复现音色控制实验。
- 提供完整的推理与 Demo 工具，支持 CLI 推理、Web UI、流式播放、barge-in 打断和电话模式。
- 关键模块均从 0 用 PyTorch 原生实现，不依赖三方高层封装；同时兼容 `transformers` Tokenizer 与原生权重格式。
- 配套技术报告覆盖架构、训练曲线、CER / WER 评估、音色克隆相似度与跨模型对比，链接见顶部 Tech Report 区。

#### 🎉 已发布模型列表

| 模型 | 参数（主干） | Release |
|---|---|---|
| minimind-3o | ~0.1B | 2026.05.05 |
| minimind-3o-moe | ~0.3B-A0.1B | 2026.05.05 |

---

#### 👉 更新日志

<details close>
<summary> <b>🔥 2026-05-05</b> </summary>

- MiniMind-O 首次开源，发布 `minimind-3o`（115M）与 `minimind-3o-moe`（312M-A115M）
- Thinker–Talker 双路径架构，Talker 采用 MTP 预测多层 Mimi codes，支持 24 kHz 流式语音生成与 barge-in 打断
- 音频编解码器采用 Mimi（8 层 codebook，12.5 Hz，24 kHz），Talker 在 codebook 接口上使用共享主体与轻量 adapter
- 语音 / 视觉特征分别由冻结的 SenseVoice-Small 与 SigLIP2 编码，再通过两层 MLP projector 注入 MiniMind 隐空间
- 同步发布 mini 与 full 两套训练数据，mini 单卡 3090 ~2h 即可跑通整条 Thinker–Talker 链路
- 内置 5 个 voice prompt + 7 个 unseen voice prompt，提供音色克隆与电话模式 WebUI

</details>


# 📌 快速开始

<details style="color:rgb(128,128,128)">
<summary>分享本人的软硬件配置（仅供参考）</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090(24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10
* [requirements.txt](./requirements.txt)

</details>

## 第0步（必须）

### 1' 环境准备

```bash
# 克隆仓库代码
git clone --depth 1 https://github.com/jingyaogong/minimind-o
# 安装必要依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2' 下载资源

```bash
# 下载 SenseVoice-Small 语音编码器到 ./model/SenseVoiceSmall
modelscope download --model gongjy/SenseVoiceSmall --local_dir ./model/SenseVoiceSmall
# 下载 SigLIP2 视觉编码器到 ./model/siglip2-base-p32-256-ve
modelscope download --model gongjy/siglip2-base-p32-256-ve --local_dir ./model/siglip2-base-p32-256-ve
# 下载 Mimi 音频编解码器到 ./model/mimi
modelscope download --model gongjy/mimi --local_dir ./model/mimi
# 下载 CAMPPlus 说话人编码器到 ./model/campplus
modelscope download --model gongjy/campplus --local_dir ./model/campplus
# 下载 MiniMind 语言模型权重到 ./out 目录下（作为训练 Omni 的基座语言模型）
modelscope download --model gongjy/minimind-3o-pytorch llm_768.pth --local_dir ./out
```

注：也可从 [ModelScope Collection](https://modelscope.cn/collections/gongjy/MiniMind-O) 或 [HuggingFace Collection](https://huggingface.co/collections/jingyaogong/minimind-o) 选择对应内容 `git clone`（需LFS）下载，此处不再赘述。

完成后，结构应如下：

```text
minimind-o/
├── model/
│   ├── SenseVoiceSmall/
│   ├── siglip2-base-p32-256-ve/
│   ├── mimi/
│   ├── campplus/
│   └── ...
├── out/
│   └── llm_768.pth
└── ...
```

## Ⅰ 🚀 模型推理

### 1' 下载发布权重

```bash
# 下载发布权重到 ./out 目录下
modelscope download --model gongjy/minimind-3o-pytorch --local_dir ./out
```

### 2' 命令行问答

```bash
python eval_omni.py --load_from model --weight sft_omni
```

如果使用 transformers 格式模型，可先下载模型目录：

```bash
git clone https://huggingface.co/jingyaogong/minimind-3o
python eval_omni.py --load_from minimind-3o
```

### 3' 启动 WebUI（可选）

```bash
# ⚠️ 须先将 transformers 格式模型文件夹复制到 ./scripts/ 目录下，web_demo_omni 脚本会自动扫描该目录下包含权重文件的子文件夹，如不存在则报错
cp -r minimind-3o ./scripts/minimind-3o
cd scripts && python web_demo_omni.py
```

## Ⅱ 🛠️ 模型训练

<details style="color:rgb(128,128,128)">
<summary>注：提前测试Torch是否可用cuda</summary>

```python
import torch
print(torch.cuda.is_available())
```

如果不可用，请自行去[torch_stable](https://download.pytorch.org/whl/torch_stable.html)下载whl文件安装。

</details>

### 1' 下载数据

快速开始时，推荐从[数据集链接](https://huggingface.co/datasets/jingyaogong/minimind-o_dataset)只下载 `_mini` 数据集，并放到 `./dataset` 下。

### 2' 开始训练

推荐 mini 训练管线如下，默认在 `trainer/` 目录下执行，可直接 `cd trainer && bash train.sh`：

```bash
CUDA_VISIBLE_DEVICES=0 torchrun --master_port 29560 --nproc_per_node 1 train_sft_omni.py --learning_rate 5e-4 --data_path ../dataset/sft_t2a_mini.parquet --epochs 1 --batch_size 40 --use_compile 1 --from_weight llm --save_weight sft_zero --max_seq_len 512 --use_wandb --use_moe 0
CUDA_VISIBLE_DEVICES=0 torchrun --master_port 29560 --nproc_per_node 1 train_sft_omni.py --learning_rate 5e-4 --data_path ../dataset/sft_a2a_mini.parquet --epochs 1 --batch_size 40 --use_compile 0 --from_weight sft_zero --save_weight sft_zero --max_seq_len 640 --mode audio_proj --use_wandb --use_moe 0
CUDA_VISIBLE_DEVICES=0 torchrun --master_port 29560 --nproc_per_node 1 train_sft_omni.py --learning_rate 2e-5 --data_path ../dataset/sft_a2a_mini.parquet --epochs 1 --batch_size 16 --use_compile 0 --from_weight sft_zero --save_weight sft_zero --max_seq_len 768 --use_wandb --use_moe 0
```

### 3' 测试已训练模型（可选）

确保需要测试的模型 `*.pth` 文件已保存于 `./out/` 目录下。

```bash
python eval_omni.py --weight sft_omni
```

# 📌 模型细节

MiniMind-O 的基座语言模型来自孪生项目 [MiniMind](https://github.com/jingyaogong/minimind)，LLM 的结构与训练细节可移步该项目查阅。即使不了解 LLM 细节，也可直接参照上方"快速开始"流程训练一个 MiniMind-O。

## Ⅰ 架构总览

![](./images/architecture.jpg)

MiniMind-O 的主体由 Thinker 和 Talker 两条路径组成。Thinker 负责理解文本、语音和图像输入，并生成语义层面的文本回复；Talker 则在 Thinker 给出的语义条件上，通过 MTP 同步预测多层 Mimi audio codes，最后由音频解码器还原成流式语音。这样做的目的不是把 ASR、LLM、TTS 简单串起来，而是在一个统一序列里同时保留文本推理、语音输出和流式交互能力。

文本输入直接进入语言主干；语音和图像分别经过 Audio Encoder 与 Vision Encoder 提取特征，再映射到 MiniMind 的隐空间中。音色信息由 Speaker Encoder 或参考音频 codes 提供，推理时可以配合 VAD 实现边听边答、实时打断和近似双工交互。更细的 projector 结构、序列排布和训练目标在后文展开，代码层面的实现细节可直接参考 `model/model_omni.py` 与[技术报告](http://arxiv.org/abs/2605.03937)。

![](./images/input_token_layout.jpg)

图中展示了文本 token、语音特征、图像特征和音色条件在输入序列中的布局方式。

## Ⅱ Thinker 侧多模态理解

Thinker 负责统一接收文本、语音和图像信息，并生成语义层面的文本回复。文本 token 直接进入语言主干，语音和图像特征则通过对应 projector 注入到占位符位置，使不同模态最终落到同一条序列中建模。

## Ⅲ 中间层 Bridge

Thinker 向 Talker 传递的表征取自中间层，而不是 embedding 层或最后一层。embedding 层语义信息不足，最后一层又更贴近 next-token prediction 目标；中间层通常已经融合了上下文和跨模态信息，同时还没有被 LM head 过度塑形，更适合作为语音生成的条件。默认 `bridge_layer = num_hidden_layers // 2 - 1`，不同规模下也可以通过配置调整。

## Ⅳ Talker 侧语音生成

Talker 负责把 Thinker 给出的语义状态转成 8 层 Mimi codebook 序列。这里采用 MTP 形式同时预测多个 audio codebook，而不是把每层 codebook 拆成独立的长链路；为了控制 0.1B 模型中的额外参数量，音频 embedding 和输出 head 采用共享主体加轻量 codebook adapter 的形式。这样既保留不同 codebook 的分布差异，也避免为每一层 codebook 复制一整套参数。

## Ⅴ 序列格式与流式解码

![](./images/sequence_format.jpg)

MiniMind-O 将文本 token 与 8 路 audio-code stream 放在同一个训练样本中：Thinker 负责文本序列，Talker 负责音频 code 序列，语音、图像和音色条件都通过占位符或 reference codes 注入。回复开始之后才计算目标文本和目标音频的损失，因此 reference 与 conditioning 区域只提供条件，不作为重构目标。

流式生成时，模型一边产生文本 token，一边通过 MTP 和延迟调度补齐 8 层 Mimi codes。Mimi 解码器可以增量恢复 24 kHz 波形，因此语音播放不必等待完整回答结束。

## Ⅵ 音色控制

音色控制采用 in-context voice cloning 的方式完成：参考音频先被编码成 voice prompt，作为上下文条件喂给 Talker，而不是通过微调权重或改写文本 prompt 来指定音色。模型也可以同时使用 speaker embedding 提供更稳定的说话人约束；推理时更换音色只需要替换这些条件信息，Thinker prompt 与 Talker 权重保持不变。

默认 release 带有 5 个内置 voice prompt（dylan、eric、serena、uncle_fu、vivian），另保留 7 个 unseen prompt 用于评估（arthur、chelsie、cherry、ethan、jennifer、momo、moon）。

## Ⅶ 模块与参数规模

MiniMind-O 所说的 0.1B，指 Thinker、Talker 和两路 projector 组成的可训练主体；落到具体发布版本上，`minimind-3o` 约 113M，`minimind-3o-moe` 约 315M。Audio Encoder、Vision Encoder 和 Speech Codec 属于冻结的外部旁路模型，负责特征提取或音频编解码，合计约 425M 参数，不计入 active MiniMind-O 参数。

下表按发布模型统计主要模块参数，Trainable 参数按 PyTorch 模块统计，tied embedding 去重计入。

| 统计口径 | minimind-3o | minimind-3o-moe |
|---|---:|---:|
| 可训练主体 | 113.13M | 314.89M |
| 冻结外部模块 | 424.70M 

# FILE: README_en.md

<div align="center">

![logo](./images/logo.png)

</div>


<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind-o)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind-o?style=social)](https://github.com/jingyaogong/minimind-o/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind-o?v=1)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind-o)](https://github.com/jingyaogong/minimind-o/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind-o/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind--O%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-o)
[![Technical Report](https://img.shields.io/badge/Technical%20Report-arXiv-red)](http://arxiv.org/abs/2605.03937)

</div>

<div align="center">
  <h3>"Less is More"</h3>
</div>

<div align="center">

[中文](./README.md) | English

</div>

* This project implements a small end-to-end Omni model from scratch, where a single set of weights jointly handles text / audio / image inputs and produces text / streaming-speech outputs.
* `minimind-3o` has only ~0.1B parameters: it can be trained on a consumer GPU and runs quickly on CPU, making it one of the smallest fully-functional Omni implementations publicly available.
* Two training datasets are released, `mini` and `full`. `mini` runs the full pipeline in about 2 hours on a single RTX 3090 and is intended for getting started; `full` corresponds to the released weights.
* The full codebase and technical report are released, covering the Thinker–Talker dual-path architecture, streaming speech generation, real-time barge-in, near-duplex interaction, voice cloning and a phone-mode WebUI.
* All core algorithmic components are implemented from scratch in native PyTorch and do not rely on high-level abstractions from third-party frameworks.
* MiniMind-O continues the design philosophy of [MiniMind](https://github.com/jingyaogong/minimind) (language) and [MiniMind-V](https://github.com/jingyaogong/minimind-v) (vision-language).

> Note: "about 2 hours" refers to the measured time of running SFT on the mini dataset using a single NVIDIA RTX 3090.

---

<div align="center">

[📄 MiniMind-O Technical Report](http://arxiv.org/abs/2605.03937)

https://github.com/user-attachments/assets/10cbcc5f-4e70-45cf-bdc5-d6361e40bb86

[🔗 Online Demo (Gradio)](https://modelscope.cn/studios/gongjy/MiniMind-O) &nbsp;|&nbsp; [🔗 Video Intro](https://www.bilibili.com/video/BV1V1RsBcEMX)

</div>

---

# 📌 Project Introduction

After [MiniMind](https://github.com/jingyaogong/minimind) (LLM) and [MiniMind-V](https://github.com/jingyaogong/minimind-v) (VLM), MiniMind-O is the third stop in this series. By "Omni" we mean a model that can listen, see and speak at the same time: it takes text, speech and visual signals as inputs, and produces text together with streaming speech.

GPT-4o was probably the first system that made natural streaming voice interaction feel real. Since then, open-source projects such as Mini-Omni2, Moshi, GLM-4-Voice and Qwen3-Omni have gradually appeared. However, if the goal is not just to call ready-made checkpoints with billions of parameters, but to fully understand, train and modify a complete Omni model from scratch, the open-source community still lacks a sufficiently lightweight starting point with an end-to-end pipeline. A common way to bring speech into an Omni model is to chain ASR, LLM and TTS into a cascade: speech is first transcribed to text, the LLM processes it, and the answer is then synthesized back to speech. This is straightforward from an engineering perspective, but it adds an extra transcription step and noticeably hurts latency, prosody and emotional cues.

MiniMind-O attempts to fill this gap: speech and text are connected directly at the hidden-state level, while the trainable backbone remains only ~0.1B parameters and the end-to-end Omni pipeline is preserved. The Talker side adopts MTP (Multi-Token Prediction) to predict multiple Mimi codebook layers at once, and combines it with VAD to support real-time barge-in and near-duplex interaction—a practical engineering route for a tiny Omni model. The code, model weights, training data and technical report are all open-sourced. A single RTX 3090 can finish training on the mini dataset in about 2 hours. The goal remains the same: let everyone read the project from the first line of code, and train, from scratch, a model that can listen, see, think and speak:

![](images/omni_io_flow.png)

😊 Enjoy building.

---

#### 🎉 What this project provides

- A complete MiniMind-O architecture: Thinker, an independent Talker, audio / vision projectors, the Mimi codebook interface and the MTP audio head.
- A full SFT pipeline that covers T2A, I2T and A2A data, supporting full-parameter training, audio-projector-only training, vision-projector-only training, and DDP multi-GPU training.
- Two training datasets, `mini` and `full`. `mini` is meant for quick onboarding and runs the pipeline in ~2 hours on a single RTX 3090; `full` matches the released weights and covers Chinese speech and image tasks.
- Multiple built-in voice prompts, unseen voice prompts and voice cloning from arbitrary reference audio, making voice-control experiments easy to reproduce.
- A complete inference and demo toolkit: CLI, Web UI, streaming playback, barge-in interruption and a phone-mode demo.
- Key modules are written from scratch in native PyTorch without high-level third-party wrappers, while remaining compatible with `transformers` tokenizers and native weight formats.
- A companion technical report covers architecture, training curves, CER / WER evaluation, voice-cloning similarity and cross-model comparisons. See the Tech Report badge at the top.

#### 🎉 Released models

| Model | Backbone params | Release |
|---|---|---|
| minimind-3o | ~0.1B | 2026.05.05 |
| minimind-3o-moe | ~0.3B-A0.1B | 2026.05.05 |

---

#### 👉 Update Log

<details close>
<summary> <b>🔥 2026-05-05</b> </summary>

- First release of MiniMind-O: `minimind-3o` (115M) and `minimind-3o-moe` (312M-A115M).
- Thinker–Talker dual-path architecture. Talker uses MTP to predict multi-codebook Mimi codes and supports 24 kHz streaming speech generation and barge-in.
- Audio codec is Mimi (8 codebooks, 12.5 Hz, 24 kHz). Talker uses a shared backbone plus lightweight adapters at the codebook interface.
- Speech and visual features are extracted by frozen SenseVoice-Small and SigLIP2 respectively, and injected into the MiniMind hidden space through two-layer MLP projectors.
- Mini and full training datasets are released alongside; mini runs the full Thinker–Talker pipeline in ~2h on a single RTX 3090.
- 5 built-in voice prompts and 7 unseen voice prompts, with voice cloning and a phone-mode WebUI included.

</details>


# 📌 Quick Start

<details style="color:rgb(128,128,128)">
<summary>Reference hardware / software setup</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090 (24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10
* [requirements.txt](./requirements.txt)

</details>

## Step 0 (required)

### 1' Environment

```bash
# Clone the repository
git clone --depth 1 https://github.com/jingyaogong/minimind-o
# Install dependencies
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2' Download resources

```bash
# Download SenseVoice-Small audio encoder to ./model/SenseVoiceSmall
modelscope download --model gongjy/SenseVoiceSmall --local_dir ./model/SenseVoiceSmall
# Download SigLIP2 vision encoder to ./model/siglip2-base-p32-256-ve
modelscope download --model gongjy/siglip2-base-p32-256-ve --local_dir ./model/siglip2-base-p32-256-ve
# Download Mimi audio codec to ./model/mimi
modelscope download --model gongjy/mimi --local_dir ./model/mimi
# Download CAM++ speaker encoder to ./model/campplus
modelscope download --model gongjy/campplus --local_dir ./model/campplus
# Download MiniMind LLM weights to ./out (used as the language backbone for training Omni)
modelscope download --model gongjy/minimind-3o-pytorch llm_768.pth --local_dir ./out
```

You can also `git clone` the corresponding repos from the [ModelScope Collection](https://modelscope.cn/collections/gongjy/MiniMind-O) or [HuggingFace Collection](https://huggingface.co/collections/jingyaogong/minimind-o) (LFS required); details omitted here.

After downloading, the directory should look like:

```text
minimind-o/
├── model/
│   ├── SenseVoiceSmall/
│   ├── siglip2-base-p32-256-ve/
│   ├── mimi/
│   ├── campplus/
│   └── ...
├── out/
│   └── llm_768.pth
└── ...
```

## Ⅰ 🚀 Inference

### 1' Download released weights

```bash
# Download released weights to ./out
modelscope download --model gongjy/minimind-3o-pytorch --local_dir ./out
```

### 2' Command-line chat

```bash
python eval_omni.py --load_from model --weight sft_omni
```

To use the Transformers-format model, download the model directory first:

```bash
git clone https://huggingface.co/jingyaogong/minimind-3o
python eval_omni.py --load_from minimind-3o
```

### 3' Launch WebUI (optional)

```bash
# ⚠️ Copy the Transformers-format model folder into ./scripts/. The web_demo_omni script
#    automatically scans this directory for sub-folders that contain weight files; it
#    raises an error if none is found.
cp -r minimind-3o ./scripts/minimind-3o
cd scripts && python web_demo_omni.py
```

## Ⅱ 🛠️ Training

<details style="color:rgb(128,128,128)">
<summary>Verify Torch is using CUDA</summary>

```python
import torch
print(torch.cuda.is_available())
```

If unavailable, please download the matching `.whl` from [torch_stable](https://download.pytorch.org/whl/torch_stable.html) and install it manually.

</details>

### 1' Download data

For a quick start, downloading only the `
