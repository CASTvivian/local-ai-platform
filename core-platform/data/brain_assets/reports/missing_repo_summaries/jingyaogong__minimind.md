# Missing Repo Summary Source: jingyaogong/minimind

- URL: https://github.com/jingyaogong/minimind
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/jingyaogong__minimind
- Clone Status: cloned
- Language: Python
- Stars: 49610
- Topics: artificial-intelligence, large-language-model
- Description: 🧠「大模型」2小时完全从0训练64M的小参数LLM！Train a 64M-parameter LLM from scratch in just 2h!

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">

![logo](./images/logo.png)

</div>

<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)](https://github.com/jingyaogong/minimind/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind)](https://github.com/jingyaogong/minimind/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/12586)

</div>

<div align="center">
  <h3>"大道至简"</h3>
</div>

<div align="center">

中文 | [English](./README_en.md)

</div>

* 此开源项目旨在完全从 0 开始，仅用 3 块钱成本与 2 小时训练时间，即可训练出规模约为 64M 的超小语言模型 MiniMind。
* MiniMind 系列极其轻量，主线最小版本体积约为 GPT-3 的 $\frac{1}{2700}$，力求让普通个人 GPU 也能快速完成训练与复现。
* 项目同时开源了大模型的极简结构与完整训练链路，覆盖 MoE、数据清洗、预训练（Pretrain）、监督微调（SFT）、LoRA、RLHF（DPO）、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等全过程代码。
* MiniMind 同时拓展了视觉模态模型 [MiniMind-V](https://github.com/jingyaogong/minimind-v)、多模态 Omni 模型 [MiniMind-O](https://github.com/jingyaogong/minimind-o)、扩散语言模型（MiniMind-dLM）、线性模型（MiniMind-Linear），详见 [Discussion](https://github.com/jingyaogong/minimind/discussions)。
* 项目所有核心算法代码均从 0 使用 PyTorch 原生实现，不依赖第三方库提供的高层抽象接口。
* 这不仅是一个大语言模型全阶段开源复现项目，也是一套面向 LLM 入门与实践的教程。
* 希望此项目能为更多人提供一个可复现、可理解、可扩展的起点，一起感受创造的乐趣，并推动更广泛 AI 社区的进步。

> 注：本项目基于 Apache 2.0 协议开源，完全免费。“2 小时” 指 SFT 阶段在单张 NVIDIA 3090 上跑完 `1 epoch` 的实测耗时，“3 块钱” 指对应时段的 GPU 租用成本。

---

<div align="center">

![minimind-3](./images/minimind-3.gif)

[🔗 在线体验](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗 视频介绍](https://www.bilibili.com/video/BV12dHPeqE72)


<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://huggingface.co/collections/jingyaogong/minimind" style="text-decoration: none;">
          <img src="./images/with_huggingface.png" alt="Hugging Face Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.modelscope.cn/profile/gongjy" style="text-decoration: none;">
          <img src="./images/with_modelscope.png" alt="ModelScope Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
    </tr>
  </table>
</div>


</div>

---

# 📌 项目介绍

大语言模型（Large Language Model, LLM）的出现，引发了全球范围内对 AI 的空前关注。无论是 ChatGPT、DeepSeek 还是 Qwen，都以惊艳的效果让人真切感受到这场技术浪潮的冲击力。然而，动辄数百亿参数的模型规模，使得它们对个人设备而言不仅难以训练，甚至连部署都显得遥不可及。打开大模型的“黑盒子”，真正去理解其内部运作机制，本应是一件令人心潮澎湃的事。遗憾的是，绝大多数探索最终都止步于使用 LoRA 等技术对现有大模型做少量微调，学习一些新指令或特定任务。这更像是在教牛顿如何使用 21 世纪的智能手机——虽然有趣，却偏离了理解物理本质的初衷。

与此同时，第三方的大模型框架与工具库，如 `transformers` / `trl` / `peft` 等，往往只暴露出高度抽象的接口。只需短短十几行代码，就可以完成“加载模型 + 加载数据集 + 推理 + 强化学习”的全流程训练。这种高效封装固然便利，却也在一定程度上把开发者与底层实现隔离开来，削弱了深入理解 LLM 核心代码的机会。我认为 “用乐高自己拼出一架飞机，远比坐在头等舱里飞行更让人兴奋”，然而更现实的问题是，互联网上充斥着大量付费课程和营销内容，用漏洞百出、一知半解的讲解包装所谓的 AI 教程。正因如此，本项目的初衷就是尽可能降低 LLM 的学习门槛，让每个人都能从理解每一行代码开始，从 0 开始亲手训练一个极小的语言模型。是的，从**零开始训练**，而不是仅仅停留在**推理**层面。最低只需不到 3 块钱的服务器成本，就能亲身体验从 0 到 1 构建一个语言模型的全过程。

😊 一起感受创造的乐趣吧！

---

#### 🎉 本项目包含以下内容

- 提供完整的 MiniMind-LLM 结构代码（Dense + MoE），当前主线结构对齐 `Qwen3 / Qwen3-MoE` 生态。
- 提供 Tokenizer 与分词器训练代码，支持 `<tool_call>`、`<tool_response>`、`<think>` 等模板标记。
- 覆盖 Pretrain、SFT、LoRA、RLHF-DPO、RLAIF（PPO / GRPO / CISPO）、Tool Use、Agentic RL、自适应思考与模型蒸馏等完整训练流程。
- 提供全阶段开源数据，覆盖收集、蒸馏、清洗与去重后的高质量数据集。
- 关键训练算法与核心模块均从 0 实现，不依赖第三方框架封装。
- 兼容 `transformers`、`trl`、`peft` 等主流框架，以及 `llama.cpp`、`vllm`、`ollama` 等常用推理引擎与 `Llama-Factory` 等训练框架。
- 支持单机单卡与单机多卡（DDP、DeepSpeed）训练，支持 wandb / swanlab 可视化与动态启停训练。
- 支持在 C-Eval、C-MMLU、OpenBookQA 等第三方测评集上进行评测，并支持通过 YaRN 实现 RoPE 长文本外推。
- 提供兼容 OpenAI API 协议的极简服务端，便于接入 FastGPT、Open-WebUI 等第三方 Chat UI，并支持 `reasoning_content`、`tool_calls`、`open_thinking`。
- 提供基于 Streamlit 的极简聊天 WebUI，支持思考展示、工具选择与多轮 Tool Call。
- 包含实验性拓展：离散扩散语言模型（[dLM](https://github.com/jingyaogong/minimind/discussions/618)）与线性注意力模型（[Linear Attention](https://github.com/jingyaogong/minimind/discussions/704)），均可基于主线 AR 模型进行续训。

#### 🎉 已发布模型列表

| 模型 | 参数量 | Release |
|------|--------|---------|
| minimind-3 | 64M | 2026.04.01 |
| minimind-3-moe | 198M-A64M | 2026.04.01 |
| minimind2-small | 26M | 2025.04.26 |
| minimind2-moe | 145M | 2025.04.26 |
| minimind2 | 104M | 2025.04.26 |
| minimind-v1-small | 26M | 2024.08.28 |
| minimind-v1-moe | 4×26M | 2024.09.17 |
| minimind-v1 | 108M | 2024.09.01 |


---

#### 📝 更新日志

<details> 
<summary> <b>🔥 2026-04-01</b> </summary>

 - 发布 `minimind-3` / `minimind-3-moe`：结构、Tokenizer、训练链路、推理接口与默认配置全面更新
- 结构主线对齐 `Qwen3 / Qwen3-MoE` 生态：Dense 约 `64M`，MoE 约 `198M-A64M`，并移除了 shared expert 设计
- 默认训练数据切换为 `pretrain_t2t(_mini).jsonl`、`sft_t2t(_mini).jsonl`、`rlaif.jsonl`、`agent_rl.jsonl` 与 `agent_rl_math.jsonl`
- 移除独立 `train_reason.py`；思考能力统一由 `chat_template + <think>` 与 `open_thinking` 自适应开关控制
- `toolcall` 能力已混入 `sft_t2t / sft_t2t_mini` 主线数据，默认 `full_sft` 即具备基础 Tool Call 能力；同时新增 `scripts/chat_api.py` 等推理示例
- 新增原生 `Agentic RL` 训练脚本 `train_agent.py`，支持多轮 Tool-Use 场景下的 `GRPO / CISPO`
- RLAIF / Agentic RL 训练流程完成 `rollout engine` 解耦，支持更灵活地切换生成后端
- `serve_openai_api.py` 与 `web_demo.py` 新增 `reasoning_content` / `tool_calls` / `open_thinking` 支持
- Tokenizer 基于 `BPE + ByteLevel` 更新，并新增工具调用与思考标记，预留 buffer token 便于后续扩展
- 新增 LoRA 权重合并导出流程，可通过 `scripts/convert_model.py` 将基础模型与 LoRA 权重合并为新的完整模型权重
- 结构图资源更新，README 大面积更新

</details>

<details> 
<summary> <b>2025-10-24</b> </summary>

- 🔥 新增RLAIF训练算法：PPO、GRPO、SPO（从0原生实现）
- 新增断点续训功能：支持训练自动恢复、跨GPU数量恢复、wandb记录连续性
- 新增RLAIF数据集：rlaif-mini.jsonl（从SFT数据随机采样1万条）；简化DPO数据集，加入中文数据
- 新增YaRN算法：支持RoPE长文本外推，提升长序列处理能力
- Adaptive Thinking：Reason模型可选是否启用思考链
- chat_template全面支持Tool Calling和Reasoning标签（`<tool_call>`、`<think>`等）
- 新增RLAIF完整章节、训练曲线对比、算法原理折叠说明
- [SwanLab](https://swanlab.cn/)替代WandB（国内访问友好，API完全兼容）
- 规范化所有代码 & 修复一些已知bugs

</details>

<details> 
<summary> <b>2025-04-26</b> </summary>

- 重要更新
- 如有兼容性需要，可访问[🔗旧仓库内容🔗](https://github.com/jingyaogong/minimind/tree/7da201a944a90ed49daef8a0265c959288dff83a)。
- MiniMind模型参数完全改名，对齐Transformers库模型（统一命名）。
- generate方式重构，继承自GenerationMixin类。
- 🔥支持llama.cpp、vllm、ollama等热门三方生态。
- 规范代码和目录结构。
- 改动词表`<s></s>`->`<|im_start|><|im_end|>`

```text
为兼容第三方推理框架llama.cpp、vllm，本次更新需付出一些可观代价。
本次更新不再支持「直接」加载25-04-26以前的旧模型进行推理。
由于Llama位置编码方式与minimind存在区别，导致映射Llama模型后QK值存在差异
minimind2系列旧模型均经过权重映射+（微调训练）QKVO线性层校准恢复而来。
本次更新后将放弃对`minimind-v1`全系列的维护，并在仓库中下线。
```

</details>

<details>
<summary> <b>More...</b> </summary>

**2025-02-09**
- 迎来发布以来重大更新，Release minimind2 Series。
- 代码几乎全部重构，使用更简洁明了的统一结构。
  如有旧代码的兼容性需要，可访问[🔗旧仓库内容🔗](https://github.com/jingyaogong/minimind/tree/6e9cd28ef9b34a0a10afbdf6f59e65cb6e628efb)。
- 免去数据预处理步骤。统一数据集格式，更换为`jsonl`格式杜绝数据集下载混乱的问题。
- minimind2系列效果相比MiniMind-V1显著提升。
- 小问题：{kv-cache写法更标准、MoE的负载均衡loss被考虑等等}
- 提供模型迁移到私有数据集的训练方案（医疗模型、自我认知样例）。
- 精简预训练数据集，并大幅提升预训练数据质量，大幅缩短个人快速训练所需时间，单卡3090即可2小时复现！
- 更新：LoRA微调脱离peft包装，从0实现LoRA过程；DPO算法从0使用PyTorch原生实现；模型白盒蒸馏原生实现。
- minimind2-DeepSeek-R1系列蒸馏模型诞生！
- minimind2具备一定的英文能力！
- 更新minimind2与第三方模型的基于更多大模型榜单测试性能的结果。

**2024-10-05**
- 为MiniMind拓展了多模态能力之---视觉
- 移步孪生项目[minimind-v](https://github.com/jingyaogong/minimind-v)查看详情！

**2024-09-27**
- 09-27更新pretrain数据集的预处理方式，为了保证文本完整性，放弃预处理成.bin训练的形式（轻微牺牲训练速度）。
- 目前pretrain预处理后的文件命名为：pretrain_data.csv。
- 删除了一些冗余的代码。

**2024-09-17**
- 更新minimind-v1-moe模型
- 为了防止歧义，不再使用mistral_tokenizer分词，全部采用自定义的minimind_tokenizer作为分词器。

**2024-09-01**
- 更新minimind-v1 (108M)模型，采用minimind_tokenizer，预训练轮次3 + SFT轮次10，更充分训练，性能更强。
- 项目已部署至ModelScope创空间，可以在此网站上体验：
- [🔗ModelScope在线体验🔗](https://www.modelscope.cn/studios/gongjy/minimind)

**2024-08-27**
- 项目首次开源

</details>

---

# 📌 快速开始

<details>
<summary>本人的软硬件配置（供参考）</summary>

* CPU: Intel(R) Core(TM) i9-10980XE CPU @ 3.00GHz
* RAM: 128 GB
* GPU: NVIDIA GeForce RTX 3090 (24GB) * 8
* Ubuntu==20.04
* CUDA==12.2
* Python==3.10.16
* [requirements.txt](./requirements.txt)

</details>

## 第0步

```bash
# 克隆仓库、安装依赖
git clone --depth 1 https://github.com/jingyaogong/minimind
cd minimind && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple
```

## Ⅰ 🚀 模型推理

### 1' 下载模型

在项目根目录：
```bash
# 方式1
modelscope download --model gongjy/minimind-3 --local_dir ./minimind-3
# 方式2
git clone https://huggingface.co/jingyaogong/minimind-3
```

### 2' CLI 推理

```bash
# 方式1：使用 Transformers 格式模型
python eval_llm.py --load_from ./minimind-3
# 方式2：基于 PyTorch 模型（确保./out目录下有对应权重）
python eval_llm.py --load_from ./model --weight full_sft
```

### 3'（可选）WebUI

```bash
# 可能需要`python>=3.10`，安装 `pip install streamlit`
# ⚠️ 须先将 transformers 格式模型文件夹复制到 ./scripts/ 目录下（例如：cp -r minimind-3 ./scripts/minimind-3），web_demo 脚本会自动扫描该目录下包含权重文件的子文件夹，如不存在则报错
cd scripts && streamlit run web_demo.py
```

### 4'（可选）第三方推理框架

```bash
# ollama
ollama run jingyaogong/minimind-3
# vllm
vllm serve /path/to/model --served-model-name "minimind"
```

## Ⅱ 🛠️ 模型训练

<details>
<summary>注：提前确认 Torch 的可用后端</summary>

```python
import torch
print(torch.cuda.is_available())
```

若你计划使用 CUDA 训练，建议先确认当前环境是否已正确识别 GPU。  
若 `cuda` 不可用，也仍可根据自身设备选择 `CPU` 或 `MPS` 运行，但训练速度与兼容性会有非常大的差异。  
如需安装或更换 PyTorch 版本，可参考 [torch_stable](https://download.pytorch.org/whl/torch_stable.html) 与[链接](https://blog.csdn.net/weixin_45456738/article/details/141029610?ops_request_misc=&request_id=&biz_id=102&utm_term=%E5%AE%89%E8%A3%85torch&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-2-141029610.nonecase&spm=1018.2226.3001.4187)

</details>

### 1' 下载数据

从下文提供的[数据集下载链接](https://www.modelscope.cn/datasets/gongjy/minimind_dataset/files) 下载所需数据文件，并放入 `./dataset` 目录

> 当前默认仅需下载 `pretrain_t2t_mini.jsonl` 与 `sft_t2t_mini.jsonl`，即可较快复现 `MiniMind Zero` 对话模型。
如有更多需求，下文提供多种搭配方案，可根据自身任务目标与 GPU 资源灵活选择。

### 2' 开始训练

<details>
<summary>💡 检查点

# FILE: README_en.md

<div align="center">

![logo](./images/logo.png)

</div>

<div align="center">

![visitors](https://visitor-badge.laobi.icu/badge?page_id=jingyaogong/minimind)
[![GitHub Repo stars](https://img.shields.io/github/stars/jingyaogong/minimind?style=social)](https://github.com/jingyaogong/minimind/stargazers)
[![GitHub Code License](https://img.shields.io/github/license/jingyaogong/minimind)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/jingyaogong/minimind)](https://github.com/jingyaogong/minimind/commits/master)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/jingyaogong/minimind/pulls)
[![Collection](https://img.shields.io/badge/🤗-MiniMind%20%20Collection-blue)](https://huggingface.co/collections/jingyaogong/minimind-66caf8d999f5c7fa64f399e5)

</div>

<div align="center">

![GitHub Trend](https://trendshift.io/api/badge/repositories/12586)

</div>

<div align="center">
  <h3>"The Great Way is Simple"</h3>
</div>

<div align="center">

[中文](./README.md) | English

</div>

* This open-source project aims to train MiniMind, an ultra-small language model with about 64M parameters, entirely from scratch with only about RMB 3 in cost and 2 hours of training time.
* The MiniMind series is intentionally lightweight. The smallest model on the main branch is about $\frac{1}{2700}$ the size of GPT-3, making full training and reproduction feasible even on ordinary personal GPUs.
* The project provides a minimalist model architecture and an end-to-end LLM training pipeline, covering MoE, data cleaning, pretraining, Supervised Fine-Tuning (SFT), LoRA, RLHF (DPO), RLAIF (PPO / GRPO / CISPO), Tool Use, Agentic RL, Adaptive Thinking, and Model Distillation.
* MiniMind has also been extended to a vision model [MiniMind-V](https://github.com/jingyaogong/minimind-v), a multimodal Omni model [MiniMind-O](https://github.com/jingyaogong/minimind-o), a diffusion language model (MiniMind-dLM), and a linear attention model (MiniMind-Linear). See [Discussion](https://github.com/jingyaogong/minimind/discussions) for details.
* All core algorithms are implemented directly in native PyTorch, without relying on high-level abstractions from third-party libraries.
* MiniMind is both an end-to-end open-source reproduction of the LLM training pipeline and a hands-on tutorial for learning how LLMs are built.
* We hope this project can provide a reproducible, understandable, and extensible starting point for more people, share the joy of creation, and help move the broader AI community forward.

> Note: This project is released under the Apache 2.0 license and is completely free. "2 hours" refers to the measured time for running `1 epoch` of the SFT stage on a single NVIDIA 3090, while "RMB 3" refers to the corresponding GPU rental cost.

---

<div align="center">

![minimind-3](./images/minimind-3.gif)

[🔗 Online Demo](https://www.modelscope.cn/studios/gongjy/MiniMind) | [🔗 Video Introduction](https://www.bilibili.com/video/BV12dHPeqE72)


<div align="center">
  <table>
    <tr>
      <td align="center">
        <a href="https://huggingface.co/collections/jingyaogong/minimind" style="text-decoration: none;">
          <img src="./images/with_huggingface.png" alt="Hugging Face Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
      <td align="center">
        <a href="https://www.modelscope.cn/profile/gongjy" style="text-decoration: none;">
          <img src="./images/with_modelscope.png" alt="ModelScope Logo" style="vertical-align: middle; width: auto; max-width: 100%;" />
        </a>
      </td>
    </tr>
  </table>
</div>


</div>

---

# 📌 Project Introduction

The emergence of Large Language Models (LLMs) has drawn unprecedented global attention to AI. ChatGPT, DeepSeek, Qwen, and many other models have impressed people with their remarkable performance, making the impact of this technological wave feel very real. However, models with tens or hundreds of billions of parameters are not only difficult to train on personal devices, but often out of reach even for deployment. Opening the "black box" of large models and truly understanding how they work internally should have been an exciting thing. Unfortunately, most explorations eventually stop at applying techniques such as LoRA to fine-tune existing large models on a few new instructions or specific tasks. This is more like teaching Newton how to use a 21st-century smartphone — interesting, but not quite the original goal of understanding the essence of physics.

At the same time, third-party LLM frameworks and toolkits such as `transformers` / `trl` / `peft` often expose only highly abstract interfaces. With just a dozen lines of code, one can complete the entire pipeline of "load model + load dataset + inference + reinforcement learning" training. This kind of efficient encapsulation is convenient, but it also separates developers from the underlying implementation to some extent, reducing the opportunity to deeply understand the core code of LLMs. I believe that "building an airplane from Lego bricks yourself is far more exciting than flying in first class". A more practical problem is that the internet is also filled with paid courses and marketing content, where so-called AI tutorials are wrapped in flawed and half-understood explanations. For this reason, the original intention of this project is to lower the learning barrier of LLMs as much as possible, so that everyone can start from understanding every line of code and train a tiny language model by hand from scratch. Yes, **training from scratch**, not merely staying at the **inference** level. With a server cost of less than RMB 3, you can personally experience the full process of building a language model from 0 to 1.

😊 Let's share the joy of creation together!

---

#### 🎉 This Project Includes the Following

- Provides the full MiniMind-LLM architecture implementation (Dense + MoE), aligned with the `Qwen3 / Qwen3-MoE` ecosystem.
- Provides the tokenizer and tokenizer training code, supporting template tokens such as `<tool_call>`, `<tool_response>`, `<think>`, etc.
- Covers end-to-end training pipelines including pretraining, SFT, LoRA, RLHF-DPO, RLAIF (PPO / GRPO / CISPO), Tool Use, Agentic RL, Adaptive Thinking, and Model Distillation.
- Provides open-source data for all stages, covering collected, distilled, cleaned, and deduplicated high-quality datasets.
- Key training algorithms and core modules are all implemented from scratch, without relying on third-party framework wrappers.
- Compatible with mainstream frameworks such as `transformers`, `trl`, `peft`, as well as commonly used inference engines like `llama.cpp`, `vllm`, `ollama`, and training frameworks like `Llama-Factory`.
- Supports single-node single-GPU and single-node multi-GPU training (DDP, DeepSpeed), wandb / swanlab visualization, and dynamic training pause/resume.
- Supports evaluation on third-party benchmark suites such as C-Eval, C-MMLU, OpenBookQA, etc., and supports RoPE long context extrapolation through YaRN.
- Provides a lightweight OpenAI-compatible API server for integration with third-party Chat UIs such as FastGPT and Open-WebUI, with support for `reasoning_content`, `tool_calls`, and `open_thinking`.
- Provides a minimalist chat WebUI based on Streamlit, supporting thinking display, tool selection, and multi-turn Tool Call.
- Includes experimental extensions: diffusion language model ([dLM](https://github.com/jingyaogong/minimind/discussions/618)) and linear attention model ([Linear Attention](https://github.com/jingyaogong/minimind/discussions/704)), both of which can be further trained from the main autoregressive model.

#### 🎉 Released Model List

| Model | Parameters | Release |
|------|--------|---------|
| minimind-3 | 64M | 2026.04.01 |
| minimind-3-moe | 198M-A64M | 2026.04.01 |
| minimind2-small | 26M | 2025.04.26 |
| minimind2-moe | 145M | 2025.04.26 |
| minimind2 | 104M | 2025.04.26 |
| minimind-v1-small | 26M | 2024.08.28 |
| minimind-v1-moe | 4×26M | 2024.09.17 |
| minimind-v1 | 108M | 2024.09.01 |

---

#### 📝 Changelog

<details> 
<summary> <b>🔥 2026-04-01</b> </summary>

 - Released `minimind-3` / `minimind-3-moe`: comprehensive updates to structure, Tokenizer, training pipeline, inference interface, and default configuration
- Main branch structure aligned with `Qwen3 / Qwen3-MoE` ecosystem: Dense approximately `64M`, MoE approximately `198M-A64M`, and removed shared expert design
- Default training data switched to `pretrain_t2t(_mini).jsonl`, `sft_t2t(_mini).jsonl`, `rlaif.jsonl`, `agent_rl.jsonl`, and `agent_rl_math.jsonl`
- Removed standalone `train_reason.py`; thinking capability is now unified through `chat_template + <think>` and `open_thinking` adaptive switch control
- `toolcall` capability has been merged into `sft_t2t / sft_t2t_mini` main branch data, default `full_sft` already has basic Tool Call capability; also added inference examples such as `scripts/chat_api.py`
- Added native `Agentic RL` training script `train_agent.py`, supporting `GRPO / CISPO` in multi-turn Tool-Use scenarios
- RLAIF / Agentic RL training pipeline completed `rollout engine` decoupling, supporting more flexible switching of generation backends
- `serve_openai_api.py` and `web_demo.py` added `reasoning_content` / `tool_calls` / `open_thinking` support
- Tokenizer updated based on `BPE + ByteLevel`, with new tool call and thinking tokens, reserved buffer tokens for future extension
- Added LoRA weight merging and export pipeline, can merge base model and LoRA weights into new complete model weights via `scripts/convert_model.py`
- Structure diagram resources updated, README extensively updated

</details>

<details> 
<summary> <b>2025-10-24</b> </summary>

- 🔥 Added RLAIF training algorithms: PPO, GRPO, SPO (natively implemented from scratch)
- Added checkpoint resume functionality: supports automatic training recovery, cr
