# Missing Repo Summary Source: jingyaogong/minimind-v

- URL: https://github.com/jingyaogong/minimind-v
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/jingyaogong__minimind-v
- Clone Status: cloned
- Language: Python
- Stars: 7880
- Topics: artificial-intelligence, chatgpt, vision-language-model
- Description: 👀「大模型」2小时从0训练65M参数的视觉多模态VLM！Train a 65M-parameter VLM from scratch in just 2h! 

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">

![logo](./images/logo.png)

</div>


<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind-v)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind-v?style=social)](https://github.com/jingyaogong/minimind-v/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind-v?v=1)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind-v)](https://github.com/jingyaogong/minimind-v/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind-v/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMindV%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-v-67000833fb60b3a2e1f3597d)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/13265)

</div>


<div align="center">
  <h3>"大道至简"</h3>
</div>

<div align="center">

中文 | [English](./README_en.md)

</div>

* 此项目旨在从0开始，仅用3块钱成本 + 2小时！即可训练出65M参数的超小多模态视觉语言模型**MiniMind-V**。
* **MiniMind-V**最小版本体积仅为 GPT3 的约 $\frac{1}{2600}$，力求做到个人GPU也可快速推理甚至训练。
* **MiniMind-V**是[MiniMind](https://github.com/jingyaogong/minimind)纯语言模型的视觉能力额外拓展，同系列多模态Omni模型详见[MiniMind-O](https://github.com/jingyaogong/minimind-o)。
* 项目同时包含了VLM大模型的极简结构、数据集清洗、Pretrain、SFT等全过程代码。
* 这不仅是一个开源VLM模型的最小实现，也是入门视觉语言模型的简明教程。
* 希望此项目能为所有人提供一个抛砖引玉的示例，一起感受创造的乐趣！推动更广泛AI社区的进步！

> 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。



<div align="center">

![minimind-3v](./images/minimind-3v.gif)

[🔗🤖在线体验](https://www.modelscope.cn/studios/gongjy/MiniMind-V) | [🔗🎞️视频介绍](https://www.bilibili.com/video/BV1Sh1vYBEzY)

</div>

# 📌 项目介绍

“用乐高拼出一架飞机，远比坐在头等舱里飞行更让人兴奋！”
构建VLM范式的多模态大模型是否真的如想象中那样复杂？它的代码实现到底如何？
训练过程究竟难不难？那么现在，探索它们的答案，一起感受创造的乐趣吧！

> [!TIP]
> （截至2026-04-20）MiniMind-V 系列已完成了以下型号模型训练，最小仅需65M (0.065B)，即可具备识图和对话的能力！

| 模型 | 参数量 | Release |
|---|---|---|
| minimind-3v-moe | 200M-A65M | 2026.04.20 |
| minimind-3v | 65M | 2026.04.20 |
| MiniMind2-V | 104M | 2025.02.20 |
| MiniMind2-Small-V | 26M | 2025.02.20 |
| minimind-v-v1-small | 27M | 2024.10.04 |
| minimind-v-v1 | 109M | 2024.10.04 |

#### 👉 更新日志

<details>
<summary> <b>2026-04-20</b> </summary>

- 更新模型检查点：minimind-3v (65M) / minimind-3v-moe (200M-A65M)
- Projector 更新：添加 `LayerNorm`，去掉 reshape token 合并（P32 原生 64 token，无需下采样）
- Vision Encoder 换为 `SiglipVisionModel`（P32，固定 256×256）
- 训练数据切到 ALLaVA-4V（Pretrain 127 万 / SFT 290 万，已合并为单阶段 SFT）
- Freeze 策略更新：`freeze_llm=1` 解冻首末两层，Pretrain/SFT 默认改为 `2`/`1`；`max_seq_len` 360 → 450
- 其他 bugfix 与小调整

</details>

<details> 
<summary> <b>2026-04-01</b> </summary>

- 新增 minimind-3v (67M) 和 minimind-3v-moe (201M-A67M) 模型
- 统一使用768+8架构，支持dense和moe两种模式
- 视觉编码器从CLIP切换为SigLIP2（siglip2-base-p16-256-ve）
- 投影模块从QFormer改为MLP Projection + reshape压缩
- 数据集格式更新为parquet，混合数据源、更新tokenizer，图像占位符改为`<|image_pad|>`、新增WebUI：支持动态扫描模型目录、下拉菜单切换模型
- 模型代码重构，LLM/VLM统一适配Transformers格式
- 训练脚本支持DDP多卡、bfloat16混合精度、torch.compile加速

</details>

<details> 
<summary> <b>2025-10-24</b> </summary>

- bug修复：模型权重不对应
- 适配[「minimind-1024更新」](https://github.com/jingyaogong/minimind)
- 代码重构：训练和评估脚本规范化
- 新增完整的断点续训支持

</details>

<details>

<summary> <b>More...</b> </summary>

**2025-04-27**

- 兼容性更新
- 适配[「minimind仓库新特性」](https://github.com/jingyaogong/minimind/issues/370)
- 规范化部分代码

**2025-02-20**

- MiniMind2-V伴随MiniMind2同步更新
- 大幅减少所有冗余代码，规范代码格式
- 大幅精简模型冗余结构
- 更新数据集格式，拓展新的SFT数据集
- 比前代VLM更优秀的效果！

**2024-10-05**

- MiniMind-V如期而至，首次开源

</details>

# 📌 快速开始

<details>
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
git clone --depth 1 https://github.com/jingyaogong/minimind-v
# 安装必要依赖
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2' 下载资源

```bash
# 下载 SigLIP2 视觉编码器到 ./model/siglip2-base-p32-256-ve
modelscope download --model gongjy/siglip2-base-p32-256-ve --local_dir ./model/siglip2-base-p32-256-ve
# 下载 MiniMind 语言模型权重到 ./out 目录下（作为训练 VLM 的基座语言模型）
modelscope download --model gongjy/minimind-3v-pytorch llm_768.pth --local_dir ./out
```

注：也可从 [ModelScope Collection](https://modelscope.cn/collections/gongjy/MiniMind-V) 或 [HuggingFace Collection](https://huggingface.co/collections/jingyaogong/minimind-v-67000833fb60b3a2e1f3597d) 选择对应内容 `git clone`（需 LFS）下载，此处不再赘述。

完成后，结构应如下：

```text
minimind-v/
├── model/
│   ├── siglip2-base-p32-256-ve/
│   └── ...
├── out/
│   └── llm_768.pth
└── ...
```

## Ⅰ 🚀 模型推理

### 1' 下载发布权重

```bash
# 下载发布权重到 ./out 目录下
modelscope download --model gongjy/minimind-3v-pytorch --local_dir ./out
```

### 2' 命令行问答

```bash
# load_from='model': 加载原生PyTorch权重, load_from='其他路径': 加载transformers格式
python eval_vlm.py --load_from model --weight sft_vlm
```

如果使用 transformers 格式模型，可先下载模型目录：

```bash
git clone https://huggingface.co/jingyaogong/minimind-3v
python eval_vlm.py --load_from minimind-3v
```

### 3' 启动 WebUI（可选）

```bash
# ⚠️ 须先将 transformers 格式模型文件夹复制到 ./scripts/ 目录下，web_demo_vlm 脚本会自动扫描该目录下包含权重文件的子文件夹，如不存在则报错
cp -r minimind-3v ./scripts/minimind-3v
cd scripts && python web_demo_vlm.py
```

## Ⅱ 🛠️ 模型训练

<details style="color:rgb(128,128,128)">
<summary>注：提前测试Torch是否可用cuda</summary>

```python
import torch
print(torch.cuda.is_available())
```

如果不可用，请自行去 [torch_stable](https://download.pytorch.org/whl/torch_stable.html) 下载 whl 文件安装。

</details>

### 1' 下载数据

快速开始时，直接从[数据集链接](https://huggingface.co/datasets/jingyaogong/minimind-v_dataset)下载 `sft_i2t.parquet`，并放到 `./dataset` 下即可。

<details style="color:rgb(128,128,128)">
<summary>注：数据集须知</summary>

【注1】之前需解压50万零碎的图像文件可能非常慢。2025-12-27起，数据集格式统一为 Parquet，图文一体化存储，体积更小，无需解压，加载更快。

【注2】Parquet 是列式存储格式，支持高效压缩和快速读取。如果你对它感到陌生，可以预览数据内容，在 `dataset/` 目录下执行 `python lm_dataset.py` 可视化前5条图文对。

Pretrain 数据（可选；仅包含 caption 子集）：
```bash
wget https://hf-mirror.com/datasets/jingyaogong/minimind-v_dataset/resolve/main/pretrain_i2t.parquet -P ./dataset
```

SFT 单文件 290 万条已把 Pretrain 作为子集合并，经全局 dictionary encoding 去重后体积只比 SFT 原版多 ~10%，可覆盖所有训练阶段。因此快速复现时可以跳过 Pretrain，直接进入 SFT。

</details>

### 2' 开始训练

推荐直接执行 SFT。默认 `--freeze_llm 1`，即训练 `vision_proj` 和 LLM 首尾层，保留中间层原有语言能力：

```bash
python train_sft_vlm.py --epochs 2 --from_weight llm
```

如果希望让 Projector 先完成一轮图文对齐，再进入 SFT，可额外执行 Pretrain：

```bash
python train_pretrain_vlm.py --epochs 2 --from_weight llm
python train_sft_vlm.py --epochs 2 --from_weight pretrain_vlm
```

执行完成后，`out/` 下会生成 `sft_vlm_*.pth` 作为 SFT 权重。

<details style="color:rgb(128,128,128)">
<summary>注：训练须知</summary>

- 支持断点续训：添加`--from_resume 1`参数可从上次中断处继续训练
- 支持GPU数量变化：续训时GPU数量改变会自动转换step
- 原子性保存：使用临时文件+替换机制，防止保存过程中断导致权重损坏
- 每次保存同时生成`out/**.pth`（模型权重）和`checkpoints/**_resume.pth`（训练状态）文件

```bash
# 训练中断后，使用相同命令并添加 --from_resume 1
python train_sft_vlm.py --epochs 4 --from_resume 1
```

**参数说明：**
- `--from_weight`: 基础权重名称（llm, pretrain_vlm, none等）
- `--save_weight`: 保存权重的前缀名
- `--from_resume`: 是否续训（0=从头开始，1=从检查点继续）
- `--freeze_llm`: 冻结策略（0=全参可训，1=proj + LLM 首尾层，2=仅训 proj）。Pretrain 默认 2，SFT 默认 1
- 更多可直接参考代码

</details>

### 3' 测试已训练模型（可选）

确保需要测试的模型 `*.pth` 文件位于 `./out/` 目录下。
也可以直接去[此处](https://huggingface.co/jingyaogong/minimind-3v-pytorch)下载使用我训练的`*.pth`文件。

```bash
# 测试SFT模型（默认）
python eval_vlm.py --weight sft_vlm

# 测试Pretrain模型
python eval_vlm.py --weight pretrain_vlm
```

---

> [!TIP]
> 训练脚本均为 PyTorch 原生框架，均支持多卡加速，假设你的设备有 N (N＞1) 张显卡：

单机N卡启动训练方式 (DDP, 支持多机多卡集群)

```bash
torchrun --nproc_per_node N train_xxx.py
```

<details>
<summary>注：其它须知</summary>

<del>
单机N卡启动训练 (DeepSpeed)

```bash
deepspeed --master_port 29500 --num_gpus=N train_xxx.py
```
</del>

可根据需要开启wandb记录训练过程

```bash
# 需要登录: wandb login
torchrun --nproc_per_node N train_xxx.py --use_wandb
# and
python train_xxx.py --use_wandb
```

通过添加`--use_wandb`参数，可以记录训练过程，训练完成后，可以在wandb网站上查看训练过程。通过修改`wandb_project`
和`wandb_run_name`参数，可以指定项目名称和运行名称。

【注】：25年6月后，国内网络环境无法直连WandB，MiniMind项目默认转为使用[SwanLab](https://swanlab.cn/)作为训练可视化工具（完全兼容WandB API），即`import wandb`改为`import swanlab as wandb`即可，其他均无需改动。

</details>

# 📌 模型细节

MiniMind-V 的语言主干即孪生项目 [minimind](https://github.com/jingyaogong/minimind) 训练得到的 `llm_768.pth`，LLM 本身的结构、训练细节与实验分析不在本仓库重复，默认读者对 MiniMind LLM 已有基本了解。未接触过也不影响照着“快速开始”跑通 MiniMind-V，流程自洽。

顶部 “从 0 训练” 和 “65M” 两个简化口号在这里也需要说明。“从 0 训练” 指 VLM 本身从零构建（Projection 随机初始化、LLM 首末层微调对齐），但 LLM 主干并非从零 pretrain，而是基于 MiniMind 的语言模型权重续训而来；若要严格意义上的 “完全从零 pretrain”，请先在 MiniMind 训一版 LLM 再迁回本项目。“65M” 指可训练部分的主干规模（LLM ~64M + Projection ~1M）；视觉编码器 SigLIP2 另有 ~95M 参数全程冻结、仅作图像特征提取，因此推理时整机参数量约 160M（dense）/ 294M（MoE）。

VLM 在 LLM 基础上增加 Visual Encoder 和特征投影两个子模块，引入模态混合分支以支持多模态输入：
![LLM-structure](./images/VLM-structure.jpg)
![LLM-structure](./images/VLM-structure-moe.jpg)


<details>
<summary> 【重要】一些有趣的思考 </summary>

此处不妨展开想一想两个问题：

* 什么叫做**L**arge **L**anguage **M**odel (LLM)？
* 什么叫做多模态模型？

[这篇文章](https://www.jiqizhixin.com/articles/2024-09-15-3)完美吻合本人的想法：
大语言模型（LLM）名字虽然带有语言二字，但它们其实与语言关系不大，这只是历史问题，更确切的名字应该是自回归 Transformer
或者其他。LLM 更多是一种统计建模的通用技术，它们主要通过自回归 Transformer 来模拟 token 流，而这些 token
可以代表文本、图片、音频、动作选择、甚至是分子等任何东西。
因此，只要能将问题转化为模拟一系列离散 token 的流程，理论上都可以应用 LLM 来解决。
实际上，随着大型语言模型技术栈的日益成熟，我们可能会看到越来越多的问题被纳入这种建模范式。也就是说，问题固定在使用 LLM
进行『下一个 token 的预测』，只是每个领域中 token 的用途和含义有所不同。

[ZJU-LiXi老师](https://person.zju.edu.cn/xilics#694283)同样谈及过类似观点（原话大意如下）：
文本、视频、语音、动作等在人类看来属于「多模态」信号，但所谓的「模态」其实只是人类在信息存储方式上的一种分类概念。
就像`.txt`和`.png`文件，虽然在视觉呈现和高级表现形式上有所不同，但它们本质上并没有根本区别。
之所以出现「多模态」这个概念，仅仅是因为人类在不同的感知层面上对这些信号的分类需求。
然而，对于机器来说，无论信号来自何种「模态」，最终它们都只是以一串二进制的「单模态」数字序列来呈现。
机器并不会区分这些信号的模态来源，而只是处理和分析这些序列背后所承载的信息内容。

个人认为**G**enerative **P**retrained **T**ransformer (GPT) 比 **L**arge **L**anguage **M**odel (LLM)更为贴切，
因此本人表达上更习惯用"GPT"去代表LLM/VLM/类GPT架构的系列模型，而非为了蹭OpenAI的热度。

至此，我们可以用一句话总结GPT的所作所为：

GPT模型根据现有token预测输出下一个下下一个下下下一个token ...，直到模型输出结束符；此处的"token"其实并不需要一定是文本！

```text
> 对于LLM模型，如果需要理解"图片"，我们

# FILE: README_en.md

<div align="center">

![logo](./images/logo.png)

</div>


<div align="center">

[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind-v?style=social)](https://github.com/jingyaogong/minimind-v/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind-v?v=1)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind-v)](https://github.com/jingyaogong/minimind-v/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind-v/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMindV%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-v-67000833fb60b3a2e1f3597d)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/13265)

</div>


<div align="center">
  <h3>"The Greatest Path is the Simplest"</h3>
</div>

<div align="center">

[中文](./README.md) | English

</div>

* This project aims to train a super-small multimodal vision-language model, **MiniMind-V**, with just a cost of 3 RMB
  and 2 hours of work, starting from scratch!
* The smallest version of **MiniMind-V** is only about $\frac{1}{2600}$ the size of GPT-3, designed to enable fast
  inference and even training on personal GPUs.
* **MiniMind-V** is an extension of the visual capabilities of the [MiniMind](https://github.com/jingyaogong/minimind) pure language model; for the multimodal Omni model in the same family, see [MiniMind-O](https://github.com/jingyaogong/minimind-o).
* The project includes full code for the minimalist structure of large VLM models, dataset cleaning, Pretrain, and SFT.
* This is not only the smallest implementation of an open-source VLM model but also a concise tutorial for beginners in
  vision-language models.
* The hope is that this project can provide a useful example to inspire others and share the joy of creation, helping to
  drive progress in the wider AI community!

> Note: this project is released under the Apache 2.0 license and is completely free. The "2 hours" refer to the measured time of running `1 epoch` of SFT on a single NVIDIA 3090, and the "3 RMB" refer to the GPU rental cost for that time slot.

<div align="center">

![minimind-3v](./images/minimind-3v.gif)

[🔗🤖 Online Experience](https://www.modelscope.cn/studios/gongjy/MiniMind-V) | [🔗🎞️ Video Introduction](https://www.bilibili.com/video/BV1Sh1vYBEzY)

</div>

# 📌 Introduction

“Building a plane with Legos is much more exciting than flying in first class!”
Is it really as complex as imagined to build a VLM-based multimodal large model? How is the code implementation done?
Is the training process difficult? Now, let's explore the answers and feel the joy of creation together!

> [!TIP]
> (As of 2026-04-20) The MiniMind-V series has completed the training of the following model versions, with the smallest
> requiring only 65M (0.065B) parameters, capable of both image recognition and conversation!

| Model | Params | Release |
|---|---|---|
| minimind-3v-moe | 200M-A65M | 2026.04.20 |
| minimind-3v | 65M | 2026.04.20 |
| MiniMind2-V | 104M | 2025.02.20 |
| MiniMind2-Small-V | 26M | 2025.02.20 |
| minimind-v-v1-small | 27M | 2024.10.04 |
| minimind-v-v1 | 109M | 2024.10.04 |

### 👉**Recent Updates**

<details>
<summary> <b>2026-04-20</b> </summary>

- New checkpoints released: minimind-3v (65M) / minimind-3v-moe (200M-A65M)
- Projector: added `LayerNorm`, removed reshape token merging (P32 natively outputs 64 tokens, no downsampling needed)
- Vision Encoder switched to `SiglipVisionModel` (P32, fixed 256×256)
- Training data moved to ALLaVA-4V (Pretrain 1.27M / SFT 2.9M, merged into a single-stage SFT)
- Freeze strategy updated: `freeze_llm=1` unfreezes first + last layers; Pretrain/SFT defaults now `2`/`1`; `max_seq_len` 360 → 450
- Misc bugfixes and small tweaks

</details>

<details> 
<summary> <b>2026-04-01</b> </summary>

- Added minimind-3v (67M) and minimind-3v-moe (201M-A67M) models
- Unified 768+8 architecture, supporting both dense and moe modes
- Switched Visual Encoder from CLIP to SigLIP2 (siglip2-base-p16-256-ve)
- Replaced QFormer with MLP Projection + reshape compression
- Dataset format updated to parquet, mixed data sources, updated tokenizer with image placeholder `<|image_pad|>`, new WebUI with dynamic model directory scanning and dropdown model switching
- Model code refactored, LLM/VLM unified for Transformers format
- Training scripts support DDP multi-GPU, bfloat16 mixed precision, torch.compile acceleration

</details>

<details> 
<summary> <b>2025-10-24</b> </summary>

- Bug fix: model weights mismatch
- Adapted to ["minimind-1024 update"](https://github.com/jingyaogong/minimind)
- Code refactoring: training and evaluation scripts standardized
- Added complete checkpoint resumption support

</details>

<details>

<summary> <b>More...</b> </summary>

**2025-04-27**

- Compatibility updates
- Adapted to [MiniMind repository new features](https://github.com/jingyaogong/minimind/issues/370)
- Code normalization

**2025-02-20**

- MiniMind2-V updated alongside MiniMind2
- Significant reduction of all redundant code, standardized code format
- Major simplification of the model's redundant structure
- Updated dataset format, expanded with new SFT datasets
- Better performance than the previous VLM version!

**2024-10-05**

- MiniMind-V released on schedule, first open-source release

</details>

# 📌 Quick Start

<details>
<summary>My software and hardware setup (for reference only)</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090(24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10
* [requirements.txt](./requirements.txt)

</details>

## Step 0 (required)

### 1' Environment setup

```bash
# Clone the repository
git clone --depth 1 https://github.com/jingyaogong/minimind-v
# Install dependencies
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 2' Download resources

```bash
# Download the SigLIP2 vision encoder to ./model/siglip2-base-p32-256-ve
modelscope download --model gongjy/siglip2-base-p32-256-ve --local_dir ./model/siglip2-base-p32-256-ve
# Download the MiniMind language model weight to ./out (used as the base language model for VLM training)
modelscope download --model gongjy/minimind-3v-pytorch llm_768.pth --local_dir ./out
```

Alternatively, the same files can be selected from the [ModelScope Collection](https://modelscope.cn/collections/gongjy/MiniMind-V) or [HuggingFace Collection](https://huggingface.co/collections/jingyaogong/minimind-v-67000833fb60b3a2e1f3597d) and downloaded with `git clone` (LFS required).

The directory should look like this after the resources are ready:

```text
minimind-v/
├── model/
│   ├── siglip2-base-p32-256-ve/
│   └── ...
├── out/
│   └── llm_768.pth
└── ...
```

## Ⅰ 🚀 Model inference

### 1' Download released weights

```bash
# Download released weights to ./out
modelscope download --model gongjy/minimind-3v-pytorch --local_dir ./out
```

### 2' Command-line Q&A

```bash
# load_from='model': load native PyTorch weights, load_from='other path': load transformers format
python eval_vlm.py --load_from model --weight sft_vlm
```

If using a transformers-format model, download the model directory first:

```bash
git clone https://huggingface.co/jingyaogong/minimind-3v
python eval_vlm.py --load_from minimind-3v
```

### 3' Start WebUI (optional)

```bash
# ⚠️ The transformers-format model directory must be copied to ./scripts/ first. web_demo_vlm scans subdirectories under ./scripts/ that contain weight files and reports an error if none are found.
cp -r minimind-3v ./scripts/minimind-3v
cd scripts && python web_demo_vlm.py
```

## Ⅱ 🛠️ Model training

<details style="color:rgb(128,128,128)">
<summary>Note: test whether Torch can use CUDA</summary>

```python
import torch
print(torch.cuda.is_available())
```

If CUDA is unavailable, download the matching whl file from [torch_stable](https://download.pytorch.org/whl/torch_stable.html) and install it manually.

</details>

### 1' Download data

For a quick start, download `sft_i2t.parquet` from the [dataset link](https://huggingface.co/datasets/jingyaogong/minimind-v_dataset) and place it under `./dataset`.

<details style="color:rgb(128,128,128)">
<summary>Note: dataset details</summary>

**[Note 1]** The older dataset required extracting 500k fragmented image files, which could be very slow. Since 2025-12-27, the dataset has been unified into Parquet with image and text stored together. It is smaller, requires no decompression, and loads faster.

**[Note 2]** Parquet is a columnar storage format with efficient compression and fast reading. If it is unfamiliar, run `python lm_dataset.py` under `dataset/` to visualize the first 5 image-text pairs.

Pretrain data (optional; contains caption subset only):
```bash
wget https://hf-mirror.com/datasets/jingyaogong/minimind-v_dataset/resolve/main/pretrain_i2t.parquet -P ./dataset
```

The single `sft_i2t.parquet` file contains 2.9M rows and absorbs Pretrain as a subset. After global dictionary encoding deduplication, it is only ~10% larger than the original SFT file and is enough to cover every training stage. For quick reproduction, Pretrain can be skipped and SFT can be started directly.

</details>

### 2' Start training

SFT is the recommended starting point. By default, `--freeze_llm 1` trains `vision_proj` and the first/last LLM layers while keeping the middle layers' original language ability:

```bash
python train_sft_vlm.py --epochs 2 --from_weight llm
```

If the Projector should be aligned on image-text pairs before SFT, run Pretrain first:

```bash
python train_pretrain_vlm.py --epochs 2 --from_weight llm
python train_sft_vlm.py --epochs 2 --from_weight pretrain_vlm
```

After training, `sft_vlm_*.pth` will be written under `out/` as the SFT weight.

<details style="color:rgb(
