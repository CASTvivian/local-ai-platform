# Missing Repo Summary Source: zai-org/CogVideo

- URL: https://github.com/zai-org/CogVideo
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/zai-org__CogVideo
- Clone Status: cloned
- Language: Python
- Stars: 12717
- Topics: cogvideox, image-to-video, llm, sora, text-to-video, video-generation
- Description: text and image to video generation: CogVideoX (2024) and CogVideo (ICLR 2023)

## Extracted README / Docs / Examples



# FILE: README_ja.md

# CogVideo & CogVideoX

[Read this in English](./README.md)

[中文阅读](./README_zh.md)

<div align="center">
<img src=resources/logo.svg width="50%"/>
</div>
<p align="center">
<a href="https://huggingface.co/spaces/THUDM/CogVideoX-5B" target="_blank"> 🤗 Huggingface Space</a> または <a href="https://modelscope.cn/studios/ZhipuAI/CogVideoX-5b-demo" target="_blank"> 🤖 ModelScope Space</a> で CogVideoX-5B モデルをオンラインで体験してください
</p>
<p align="center">
📚 <a href="https://arxiv.org/abs/2408.06072" target="_blank">論文</a>と<a href="https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh" target="_blank">使用ドキュメント</a>を表示します。
</p>
<p align="center">
    👋 <a href="resources/WECHAT.md" target="_blank">WeChat</a> と <a href="https://discord.gg/dCGfUsagrD" target="_blank">Discord</a> に参加
</p>
<p align="center">
📍 <a href="https://chatglm.cn/video?lang=en?fr=osm_cogvideo">清影</a> と <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9">APIプラットフォーム</a> を訪問して、より大規模な商用ビデオ生成モデルを体験.
</p>

## 更新とニュース
- 🔥🔥 ```2025/03/24```: [CogKit](https://github.com/THUDM/CogKit) は **CogView4** および **CogVideoX** シリーズの微調整と推論のためのフレームワークです。このツールキットを活用することで、私たちのマルチモーダル生成モデルを最大限に活用できます。
-  **ニュース**: ```2025/02/28```: DDIM Inverse が `CogVideoX-5B` と `CogVideoX1.5-5B` でサポートされました。詳細は [こちら](inference/ddim_inversion.py) をご覧ください。
-  **ニュース**: ```2025/01/08```: 私たちは`diffusers`バージョンのモデルをベースにした`Lora`微調整用のコードを更新しました。より少ないVRAM（ビデオメモリ）で動作します。詳細については[こちら](finetune/README_ja.md)をご覧ください。
-  **ニュース**: ```2024/11/15```: `CogVideoX1.5` モデルのdiffusersバージョンをリリースしました。わずかなパラメータ調整で以前のコードをそのまま利用可能です。
-  **ニュース**: ```2024/11/08```: `CogVideoX1.5` モデルをリリースしました。CogVideoX1.5 は CogVideoX オープンソースモデルのアップグレードバージョンです。
CogVideoX1.5-5B シリーズモデルは、10秒 長の動画とより高い解像度をサポートしており、`CogVideoX1.5-5B-I2V` は任意の解像度での動画生成に対応しています。
SAT コードはすでに更新されており、`diffusers` バージョンは現在適応中です。
SAT バージョンのコードは [こちら](https://huggingface.co/THUDM/CogVideoX1.5-5B-SAT) からダウンロードできます。
- 🔥 **ニュース**: ```2024/10/13```: コスト削減のため、単一の4090 GPUで`CogVideoX-5B`
  を微調整できるフレームワーク [cogvideox-factory](https://github.com/a-r-r-o-w/cogvideox-factory)
  がリリースされました。複数の解像度での微調整に対応しています。ぜひご利用ください！
- 🔥**ニュース**: ```2024/10/10```:
  技術報告書を更新し、より詳細なトレーニング情報とデモを追加しました。
- 🔥 **ニュース**: ```2024/10/10```: 技術報告書を更新しました。[こちら](https://arxiv.org/pdf/2408.06072)
  をクリックしてご覧ください。さらにトレーニングの詳細とデモを追加しました。デモを見るには[こちら](https://yzy-thu.github.io/CogVideoX-demo/)
  をクリックしてください。
- 🔥**ニュース**: ```2024/10/09```: 飛書の[技術ドキュメント](https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh)
  でCogVideoXの微調整ガイドを公開しています。分配の自由度をさらに高めるため、公開されているドキュメント内のすべての例が完全に再現可能です。
- 🔥**ニュース**: ```2024/9/19```: CogVideoXシリーズの画像生成ビデオモデル **CogVideoX-5B-I2V**
  をオープンソース化しました。このモデルは、画像を背景入力として使用し、プロンプトワードと組み合わせてビデオを生成することができ、より高い制御性を提供します。これにより、CogVideoXシリーズのモデルは、テキストからビデオ生成、ビデオの継続、画像からビデオ生成の3つのタスクをサポートするようになりました。オンラインでの[体験](https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space)
  をお楽しみください。
- 🔥 **ニュース**: ```2024/9/19```:
  CogVideoXのトレーニングプロセスでビデオデータをテキスト記述に変換するために使用されるキャプションモデル [CogVLM2-Caption](https://huggingface.co/THUDM/cogvlm2-llama3-caption)
  をオープンソース化しました。ダウンロードしてご利用ください。
- 🔥 ```2024/8/27```: CogVideoXシリーズのより大きなモデル **CogVideoX-5B**
  をオープンソース化しました。モデルの推論性能を大幅に最適化し、推論のハードルを大幅に下げました。`GTX 1080TI` などの旧型GPUで
  **CogVideoX-2B** を、`RTX 3060` などのデスクトップGPUで **CogVideoX-5B**
  モデルを実行できます。依存関係を更新・インストールするために、[要件](requirements.txt)
  を厳守し、推論コードは [cli_demo](inference/cli_demo.py) を参照してください。さらに、**CogVideoX-2B** モデルのオープンソースライセンスが
  **Apache 2.0 ライセンス** に変更されました。
- 🔥 ```2024/8/6```: **CogVideoX-2B** 用の **3D Causal VAE** をオープンソース化しました。これにより、ビデオをほぼ無損失で再構築することができます。
- 🔥 ```2024/8/6```: CogVideoXシリーズのビデオ生成モデルの最初のモデル、**CogVideoX-2B** をオープンソース化しました。
- 🌱 **ソース**: ```2022/5/19```: CogVideoビデオ生成モデルをオープンソース化しました（現在、`CogVideo`
  ブランチで確認できます）。これは、トランスフォーマーに基づく初のオープンソース大規模テキスト生成ビデオモデルです。技術的な詳細については、[ICLR'23論文](https://arxiv.org/abs/2205.15868)
  をご覧ください。

**より強力なモデルが、より大きなパラメータサイズで登場予定です。お楽しみに！**

## 目次

特定のセクションにジャンプ：

- [クイックスタート](#クイックスタート)
  - [プロンプトの最適化](#プロンプトの最適化)
  - [SAT](#sat)
  - [Diffusers](#diffusers)
- [Gallery](#gallery)
  - [CogVideoX-5B](#cogvideox-5b)
  - [CogVideoX-2B](#cogvideox-2b)
- [モデル紹介](#モデル紹介)
- [友好的リンク](#友好的リンク)
- [プロジェクト構造](#プロジェクト構造)
  - [Colabでのクイックスタート](#colabでのクイックスタート)
  - [Inference](#inference)
  - [finetune](#finetune)
  - [sat](#sat-1)
  - [ツール](#ツール)
- [CogVideo(ICLR'23)](#cogvideoiclr23)
- [引用](#引用)
- [ライセンス契約](#ライセンス契約)

## クイックスタート

### プロンプトの最適化

モデルを実行する前に、[こちら](inference/convert_demo.py)
を参考にして、GLM-4（または同等の製品、例えばGPT-4）の大規模モデルを使用してどのようにモデルを最適化するかをご確認ください。これは非常に重要です。モデルは長いプロンプトでトレーニングされているため、良いプロンプトがビデオ生成の品質に直接影響を与えます。

### SAT

[sat_demo](sat/README.md) の指示に従ってください:
SATウェイトの推論コードと微調整コードが含まれています。CogVideoXモデル構造に基づいて改善することをお勧めします。革新的な研究者は、このコードを使用して迅速なスタッキングと開発を行うことができます。

### Diffusers

```
pip install -r requirements.txt
```

次に [diffusers_demo](inference/cli_demo.py) を参照してください: 推論コードの詳細な説明が含まれており、一般的なパラメータの意味についても言及しています。

量子化推論の詳細については、[diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao/) を参照してください。Diffusers
と TorchAO を使用することで、量子化推論も可能となり、メモリ効率の良い推論や、コンパイル時に場合によっては速度の向上が期待できます。A100
および H100
上でのさまざまな設定におけるメモリおよび時間のベンチマークの完全なリストは、[diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao)
に公開されています。

## Gallery

### CogVideoX-5B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/cf5953ea-96d3-48fd-9907-c4708752c714" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/fe0a78e6-b669-4800-8cf0-b5f9b5145b52" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/c182f606-8f8c-421d-b414-8487070fcfcb" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/7db2bbce-194d-434d-a605-350254b6c298" width="100%" controls autoplay loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/62b01046-8cab-44cc-bd45-4d965bb615ec" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/d78e552a-4b3f-4b81-ac3f-3898079554f6" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/30894f12-c741-44a2-9e6e-ddcacc231e5b" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/926575ca-7150-435b-a0ff-4900a963297b" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>

### CogVideoX-2B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/ea3af39a-3160-4999-90ec-2f7863c5b0e9" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/9de41efd-d4d1-4095-aeda-246dd834e91d" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/941d6661-6a8d-4a1b-b912-59606f0b2841" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/938529c4-91ae-4f60-b96b-3c3947fa63cb" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>

ギャラリーの対応するプロンプトワードを表示するには、[こちら](resources/galary_prompt.md)をクリックしてください

## モデル紹介

CogVideoXは、[清影](https://chatglm.cn/video?fr=osm_cogvideox) と同源のオープンソース版ビデオ生成モデルです。
以下の表に、提供しているビデオ生成モデルの基本情報を示します:

<table style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">モデル名</th>
    <th style="text-align: center;">CogVideoX1.5-5B (最新)</th>
    <th style="text-align: center;">CogVideoX1.5-5B-I2V (最新)</th>
    <th style="text-align: center;">CogVideoX-2B</th>
    <th style="text-align: center;">CogVideoX-5B</th>
    <th style="text-align: center;">CogVideoX-5B-I2V</th>
  </tr>
  <tr>
    <td style="text-align: center;">公開日</td>
    <th style="text-align: center;">2024年11月8日</th>
    <th style="text-align: center;">2024年11月8日</th>
    <th style="text-align: center;">2024年8月6日</th>
    <th style="text-align: center;">2024年8月27日</th>
    <th style="text-align: center;">2024年9月19日</th>
  </tr>
  <tr>
    <td style="text-align: center;">ビデオ解像度</td>
    <td colspan="1" style="text-align: center;">1360 * 768</td>
    <td colspan="1" style="text-align: center;"> Min(W, H) = 768 <br> 768 ≤ Max(W, H) ≤ 1360 <br> Max(W, H) % 16 = 0 </td>
    <td colspan="3" style="text-align: center;">720 * 480</td>
  </tr>
  <tr>
    <td style="text-align: center;">フレーム数</td>
    <td colspan="2" style="text-align: center;"><b>16N + 1</b> (N <= 10) である必要があります (デフォルト 81)</td>
    <td colspan="3" style="text-align: center;"><b>8N + 1</b> (N <= 6) である必要があります (デフォルト 49)</td>
  </tr>
  <tr>
    <td style="text-align: center;">推論精度</td>
    <td colspan="2" style="text-align: center;"><b>BF16(推奨)</b>, FP16, FP32，FP8*，INT8，INT4非対応</td>
    <td style="text-align: center;"><b>FP16*(推奨)</b>, BF16, FP32，FP8*，INT8，INT4非対応</td>
    <td colspan="2" style="text-align: center;"><b>BF16(推奨)</b>, FP16, FP32，FP8*，INT8，INT4非対応</td>
  </tr>
  <tr>
    <td style="text-align: center;">単一GPUメモリ消費量<br></td>
    <td colspan="2" style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> BF16: 76GB <br><b>diffusers BF16：10GBから*</b><br><b>diffusers INT8(torchao)：7GBから*</b></td>
    <td style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> FP16: 18GB <br><b>diffusers FP16: 4GB以上* </b><br><b>diffusers INT8(torchao): 3.6GB以上*</b></td>
    <td colspan="2" style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> BF16: 26GB <br><b>diffusers BF16 : 5GB以上* </b><br><b>diffusers INT8(torchao): 4.4GB以上* </b><

# FILE: README.md

# CogVideo & CogVideoX

[中文阅读](./README_zh.md)

[日本語で読む](./README_ja.md)

<div align="center">
<img src=resources/logo.svg width="50%"/>
</div>
<p align="center">
Experience the CogVideoX-5B model online at <a href="https://huggingface.co/spaces/THUDM/CogVideoX-5B" target="_blank"> 🤗 Huggingface Space</a> or <a href="https://modelscope.cn/studios/ZhipuAI/CogVideoX-5b-demo" target="_blank"> 🤖 ModelScope Space</a>
</p>
<p align="center">
📚 View the <a href="https://arxiv.org/abs/2408.06072" target="_blank">paper</a> and <a href="https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh" target="_blank">user guide</a>
</p>
<p align="center">
    👋 Join our <a href="resources/WECHAT.md" target="_blank">WeChat</a> and <a href="https://discord.gg/dCGfUsagrD" target="_blank">Discord</a>
</p>
<p align="center">
📍 Visit <a href="https://chatglm.cn/video?lang=en?fr=osm_cogvideo">QingYing</a> and <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9">API Platform</a> to experience larger-scale commercial video generation models.
</p>

## Project Updates

- 🔥🔥 **News**: ```2025/03/24```: We have launched [CogKit](https://github.com/THUDM/CogKit), a fine-tuning and inference framework for the **CogView4** and **CogVideoX** series. This toolkit allows you to fully explore and utilize our multimodal generation models.
- 🔥 **News**: ```2025/02/28```: DDIM Inverse is now supported in `CogVideoX-5B` and `CogVideoX1.5-5B`. Check [here](inference/ddim_inversion.py).
- 🔥 **News**: ```2025/01/08```: We have updated the code for `Lora` fine-tuning based on the `diffusers` version model, which uses less GPU memory. For more details, please see [here](finetune/README.md).
- 🔥 **News**: ```2024/11/15```: We released the `CogVideoX1.5` model in the diffusers version. Only minor parameter adjustments are needed to continue using previous code.
- 🔥 **News**: ```2024/11/08```: We have released the CogVideoX1.5 model. CogVideoX1.5 is an upgraded version of the open-source model CogVideoX.
The CogVideoX1.5-5B series supports 10-second videos with higher resolution, and CogVideoX1.5-5B-I2V supports video generation at any resolution.
The SAT code has already been updated, while the diffusers version is still under adaptation. Download the SAT version code [here](https://huggingface.co/THUDM/CogVideoX1.5-5B-SAT).
- 🔥 **News**: ```2024/10/13```: A more cost-effective fine-tuning framework for `CogVideoX-5B` that works with a single
  4090 GPU, [cogvideox-factory](https://github.com/a-r-r-o-w/cogvideox-factory), has been released. It supports
  fine-tuning with multiple resolutions. Feel free to use it!
- 🔥 **News**: ```2024/10/10```: We have updated our technical report. Please
  click [here](https://arxiv.org/pdf/2408.06072) to view it. More training details and a demo have been added. To see
  the demo, click [here](https://yzy-thu.github.io/CogVideoX-demo/).- 🔥 **News**: ```2024/10/09```: We have publicly
  released the [technical documentation](https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh) for CogVideoX
  fine-tuning on Feishu, further increasing distribution flexibility. All examples in the public documentation can be
  fully reproduced.
- 🔥 **News**: ```2024/9/19```: We have open-sourced the CogVideoX series image-to-video model **CogVideoX-5B-I2V**.
  This model can take an image as a background input and generate a video combined with prompt words, offering greater
  controllability. With this, the CogVideoX series models now support three tasks: text-to-video generation, video
  continuation, and image-to-video generation. Welcome to try it online
  at [Experience](https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space).
- 🔥 ```2024/9/19```: The Caption
  model [CogVLM2-Caption](https://huggingface.co/THUDM/cogvlm2-llama3-caption), used in the training process of
  CogVideoX to convert video data into text descriptions, has been open-sourced. Welcome to download and use it.
- 🔥 ```2024/8/27```: We have open-sourced a larger model in the CogVideoX series, **CogVideoX-5B**. We have
  significantly optimized the model's inference performance, greatly lowering the inference threshold.
  You can run **CogVideoX-2B** on older GPUs like `GTX 1080TI`, and **CogVideoX-5B** on desktop GPUs like `RTX 3060`. Please strictly
  follow the [requirements](requirements.txt) to update and install dependencies, and refer
  to [cli_demo](inference/cli_demo.py) for inference code. Additionally, the open-source license for
  the **CogVideoX-2B** model has been changed to the **Apache 2.0 License**.
- 🔥 ```2024/8/6```: We have open-sourced **3D Causal VAE**, used for **CogVideoX-2B**, which can reconstruct videos with
  almost no loss.
- 🔥 ```2024/8/6```: We have open-sourced the first model of the CogVideoX series video generation models, **CogVideoX-2B
  **.
- 🌱 **Source**: ```2022/5/19```: We have open-sourced the CogVideo video generation model (now you can see it in
  the `CogVideo` branch). This is the first open-source large Transformer-based text-to-video generation model. You can
  access the [ICLR'23 paper](https://arxiv.org/abs/2205.15868) for technical details.

## Table of Contents

Jump to a specific section:

- [Quick Start](#quick-start)
  - [Prompt Optimization](#prompt-optimization)
  - [SAT](#sat)
  - [Diffusers](#diffusers)
- [Gallery](#gallery)
  - [CogVideoX-5B](#cogvideox-5b)
  - [CogVideoX-2B](#cogvideox-2b)
- [Model Introduction](#model-introduction)
- [Friendly Links](#friendly-links)
- [Project Structure](#project-structure)
  - [Quick Start with Colab](#quick-start-with-colab)
  - [Inference](#inference)
  - [finetune](#finetune)
  - [sat](#sat-1)
  - [Tools](#tools)
- [CogVideo(ICLR'23)](#cogvideoiclr23)
- [Citation](#citation)
- [Model-License](#model-license)

## Quick Start

### Prompt Optimization

Before running the model, please refer to [this guide](inference/convert_demo.py) to see how we use large models like
GLM-4 (or other comparable products, such as GPT-4) to optimize the model. This is crucial because the model is trained
with long prompts, and a good prompt directly impacts the quality of the video generation.

### SAT

**Please make sure your Python version is between 3.10 and 3.12, inclusive of both 3.10 and 3.12.**

Follow instructions in [sat_demo](sat/README.md): Contains the inference code and fine-tuning code of SAT weights. It is
recommended to improve based on the CogVideoX model structure. Innovative researchers use this code to better perform
rapid stacking and development.

### Diffusers

**Please make sure your Python version is between 3.10 and 3.12, inclusive of both 3.10 and 3.12.**

```
pip install -r requirements.txt
```

Then follow [diffusers_demo](inference/cli_demo.py): A more detailed explanation of the inference code, mentioning the
significance of common parameters.

For more details on quantized inference, please refer
to [diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao/). With Diffusers and TorchAO, quantized inference
is also possible leading to memory-efficient inference as well as speedup in some cases when compiled. A full list of
memory and time benchmarks with various settings on A100 and H100 has been published
at [diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao).

## Gallery

### CogVideoX-5B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/cf5953ea-96d3-48fd-9907-c4708752c714" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/fe0a78e6-b669-4800-8cf0-b5f9b5145b52" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/c182f606-8f8c-421d-b414-8487070fcfcb" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/7db2bbce-194d-434d-a605-350254b6c298" width="100%" controls autoplay loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/62b01046-8cab-44cc-bd45-4d965bb615ec" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/d78e552a-4b3f-4b81-ac3f-3898079554f6" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/30894f12-c741-44a2-9e6e-ddcacc231e5b" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/926575ca-7150-435b-a0ff-4900a963297b" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>

### CogVideoX-2B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/ea3af39a-3160-4999-90ec-2f7863c5b0e9" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/9de41efd-d4d1-4095-aeda-246dd834e91d" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/941d6661-6a8d-4a1b-b912-59606f0b2841" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/938529c4-91ae-4f60-b96b-3c3947fa63cb" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>

To view the corresponding prompt words for the gallery, please click [here](resources/galary_prompt.md)

## Model Introduction

CogVideoX is an open-source version of the video generation model originating
from [QingYing](https://chatglm.cn/video?lang=en?fr=osm_cogvideo). The table below displays the list of video generation
models we currently offer, along with their foun

# FILE: README_zh.md

# CogVideo & CogVideoX

[Read this in English](./README.md)

[日本語で読む](./README_ja.md)

<div align="center">
<img src=resources/logo.svg width="50%"/>
</div>
<p align="center">
在 <a href="https://huggingface.co/spaces/THUDM/CogVideoX-5B" target="_blank"> 🤗 Huggingface Space</a> 或 <a href="https://modelscope.cn/studios/ZhipuAI/CogVideoX-5b-demo" target="_blank"> 🤖 ModelScope Space</a> 在线体验 CogVideoX-5B 模型
</p>
<p align="center">
📚 查看 <a href="https://arxiv.org/abs/2408.06072" target="_blank">论文</a> 和 <a href="https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh" target="_blank">使用文档</a>
</p>
<p align="center">
    👋 加入我们的 <a href="resources/WECHAT.md" target="_blank">微信</a> 和  <a href="https://discord.gg/dCGfUsagrD" target="_blank">Discord</a>
</p>
<p align="center">
📍 前往<a href="https://chatglm.cn/video?fr=osm_cogvideox"> 清影</a> 和 <a href="https://open.bigmodel.cn/?utm_campaign=open&_channel_track_key=OWTVNma9"> API平台</a> 体验更大规模的商业版视频生成模型。
</p>

## 项目更新

- 🔥🔥 **News**: ```2025/03/24```: 我们推出了 [CogKit](https://github.com/THUDM/CogKit) 工具，这是一个微调**CogView4**, **CogVideoX** 系列的微调和推理框架，一个工具包，玩转我们的多模态生成模型。
- 🔥 **News**: ```2025/02/28```:  DDIM Inverse 已经在`CogVideoX-5B` 和 `CogVideoX1.5 -5B` 支持，查看 [here](inference/ddim_inversion.py).
- 🔥 **News**: ```2025/01/08```: 我们更新了基于`diffusers`版本模型的`Lora`微调代码，占用显存更低，详情请见[这里](finetune/README_zh.md)。
- 🔥 **News**: ```2024/11/15```: 我们发布 `CogVideoX1.5` 模型的diffusers版本，仅需调整部分参数即可沿用之前的代码。
- 🔥 **News**: ```2024/11/08```: 我们发布 `CogVideoX1.5` 模型。CogVideoX1.5 是 CogVideoX 开源模型的升级版本。
CogVideoX1.5-5B 系列模型支持 **10秒** 长度的视频和更高的分辨率，其中 `CogVideoX1.5-5B-I2V` 支持 **任意分辨率** 的视频生成，SAT代码已经更新。`diffusers`版本还在适配中。SAT版本代码前往 [这里](https://huggingface.co/THUDM/CogVideoX1.5-5B-SAT) 下载。
- 🔥**News**: ```2024/10/13```: 成本更低，单卡4090可微调 `CogVideoX-5B`
  的微调框架[cogvideox-factory](https://github.com/a-r-r-o-w/cogvideox-factory)已经推出，多种分辨率微调，欢迎使用。
- 🔥 **News**: ```2024/10/10```: 我们更新了我们的技术报告,请点击 [这里](https://arxiv.org/pdf/2408.06072)
  查看，附上了更多的训练细节和demo，关于demo，点击[这里](https://yzy-thu.github.io/CogVideoX-demo/) 查看。
- 🔥 **News**: ```2024/10/09```: 我们在飞书[技术文档](https://zhipu-ai.feishu.cn/wiki/DHCjw1TrJiTyeukfc9RceoSRnCh")
  公开CogVideoX微调指导，以进一步增加分发自由度，公开文档中所有示例可以完全复现
- 🔥 **News**: ```2024/9/19```: 我们开源 CogVideoX 系列图生视频模型 **CogVideoX-5B-I2V**
  。该模型可以将一张图像作为背景输入，结合提示词一起生成视频，具有更强的可控性。
  至此，CogVideoX系列模型已经支持文本生成视频，视频续写，图片生成视频三种任务。欢迎前往在线[体验](https://huggingface.co/spaces/THUDM/CogVideoX-5B-Space)。
- 🔥 **News**: ```2024/9/19```: CogVideoX 训练过程中用于将视频数据转换为文本描述的 Caption
  模型 [CogVLM2-Caption](https://huggingface.co/THUDM/cogvlm2-llama3-caption)
  已经开源。欢迎前往下载并使用。
- 🔥 ```2024/8/27```:  我们开源 CogVideoX 系列更大的模型 **CogVideoX-5B**
  。我们大幅度优化了模型的推理性能，推理门槛大幅降低，您可以在 `GTX 1080TI` 等早期显卡运行 **CogVideoX-2B**，在 `RTX 3060`
  等桌面端甜品卡运行 **CogVideoX-5B** 模型。 请严格按照[要求](requirements.txt)
  更新安装依赖，推理代码请查看 [cli_demo](inference/cli_demo.py)。同时，**CogVideoX-2B** 模型开源协议已经修改为**Apache 2.0 协议**。
- 🔥 ```2024/8/6```: 我们开源 **3D Causal VAE**，用于 **CogVideoX-2B**，可以几乎无损地重构视频。
- 🔥 ```2024/8/6```: 我们开源 CogVideoX 系列视频生成模型的第一个模型, **CogVideoX-2B**。
- 🌱 **Source**: ```2022/5/19```: 我们开源了 CogVideo 视频生成模型（现在你可以在 `CogVideo` 分支中看到），这是首个开源的基于
  Transformer 的大型文本生成视频模型，您可以访问 [ICLR'23 论文](https://arxiv.org/abs/2205.15868) 查看技术细节。

## 目录

跳转到指定部分：

- [快速开始](#快速开始)
  - [提示词优化](#提示词优化)
  - [SAT](#sat)
  - [Diffusers](#diffusers)
- [视频作品](#视频作品)
  - [CogVideoX-5B](#cogvideox-5b)
  - [CogVideoX-2B](#cogvideox-2b)
- [模型介绍](#模型介绍)
- [友情链接](#友情链接)
- [完整项目代码结构](#完整项目代码结构)
  - [Colab 快速使用](#colab-快速使用)
  - [inference](#inference)
  - [finetune](#finetune)
  - [sat](#sat-1)
  - [tools](#tools)
- [CogVideo(ICLR'23)](#cogvideoiclr23)
- [引用](#引用)
- [模型协议](#模型协议)

## 快速开始

### 提示词优化

在开始运行模型之前，请参考 [这里](inference/convert_demo.py) 查看我们是怎么使用GLM-4(或者同级别的其他产品，例如GPT-4)
大模型对模型进行优化的，这很重要，
由于模型是在长提示词下训练的，一个好的提示词直接影响了视频生成的质量。

### SAT

查看sat文件夹下的 [sat_demo](sat/README.md)：包含了 SAT 权重的推理代码和微调代码，推荐基于此代码进行 CogVideoX
模型结构的改进，研究者使用该代码可以更好的进行快速的迭代和开发。

### Diffusers

```
pip install -r requirements.txt
```

查看[diffusers_demo](inference/cli_demo.py)：包含对推理代码更详细的解释，包括各种关键的参数。

欲了解更多关于量化推理的细节，请参考 [diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao/)。使用 Diffusers
和 TorchAO，量化推理也是可能的，这可以实现内存高效的推理，并且在某些情况下编译后速度有所提升。有关在 A100 和 H100
上使用各种设置的内存和时间基准测试的完整列表，已发布在 [diffusers-torchao](https://github.com/sayakpaul/diffusers-torchao)
上。

## 视频作品

### CogVideoX-5B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/cf5953ea-96d3-48fd-9907-c4708752c714" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/fe0a78e6-b669-4800-8cf0-b5f9b5145b52" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/c182f606-8f8c-421d-b414-8487070fcfcb" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/7db2bbce-194d-434d-a605-350254b6c298" width="100%" controls autoplay loop></video>
     </td>
  </tr>
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/62b01046-8cab-44cc-bd45-4d965bb615ec" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/d78e552a-4b3f-4b81-ac3f-3898079554f6" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/30894f12-c741-44a2-9e6e-ddcacc231e5b" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/926575ca-7150-435b-a0ff-4900a963297b" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>

### CogVideoX-2B

<table border="0" style="width: 100%; text-align: left; margin-top: 20px;">
  <tr>
      <td>
          <video src="https://github.com/user-attachments/assets/ea3af39a-3160-4999-90ec-2f7863c5b0e9" width="100%" controls autoplay loop></video>
      </td>
      <td>
          <video src="https://github.com/user-attachments/assets/9de41efd-d4d1-4095-aeda-246dd834e91d" width="100%" controls autoplay loop></video>
      </td>
       <td>
          <video src="https://github.com/user-attachments/assets/941d6661-6a8d-4a1b-b912-59606f0b2841" width="100%" controls autoplay loop></video>
     </td>
      <td>
          <video src="https://github.com/user-attachments/assets/938529c4-91ae-4f60-b96b-3c3947fa63cb" width="100%" controls autoplay loop></video>
     </td>
  </tr>
</table>


查看画廊的对应提示词，请点击[这里](resources/galary_prompt.md)

## 模型介绍

CogVideoX是 [清影](https://chatglm.cn/video?fr=osm_cogvideox) 同源的开源版本视频生成模型。
下表展示我们提供的视频生成模型相关基础信息:

<table  style="border-collapse: collapse; width: 100%;">
  <tr>
    <th style="text-align: center;">模型名</th>
    <th style="text-align: center;">CogVideoX1.5-5B (最新)</th>
    <th style="text-align: center;">CogVideoX1.5-5B-I2V (最新)</th>
    <th style="text-align: center;">CogVideoX-2B</th>
    <th style="text-align: center;">CogVideoX-5B</th>
    <th style="text-align: center;">CogVideoX-5B-I2V </th>
  </tr>
  <tr>
    <td style="text-align: center;">发布时间</td>
    <th style="text-align: center;">2024年11月8日</th>
    <th style="text-align: center;">2024年11月8日</th>
    <th style="text-align: center;">2024年8月6日</th>
    <th style="text-align: center;">2024年8月27日</th>
    <th style="text-align: center;">2024年9月19日</th>
  </tr>
  <tr>
    <td style="text-align: center;">视频分辨率</td>
    <td colspan="1" style="text-align: center;">1360 * 768</td>
    <td colspan="1" style="text-align: center;"> Min(W, H) = 768 <br> 768 ≤ Max(W, H) ≤ 1360 <br> Max(W, H) % 16 = 0 </td>
    <td colspan="3" style="text-align: center;">720 * 480</td>
  </tr>
  <tr>
    <td style="text-align: center;">帧数</td>
    <td colspan="2" style="text-align: center;">必须为 <b>16N + 1</b> 其中 N <= 10 (默认 81)</td>
    <td colspan="3" style="text-align: center;">必须为 <b>8N + 1</b> 其中 N <= 6 (默认 49)</td>
  </tr>
  <tr>
    <td style="text-align: center;">推理精度</td>
    <td colspan="2" style="text-align: center;"><b>BF16(推荐)</b>, FP16, FP32，FP8*，INT8，不支持INT4</td>
    <td style="text-align: center;"><b>FP16*(推荐)</b>, BF16, FP32，FP8*，INT8，不支持INT4</td>
    <td colspan="2" style="text-align: center;"><b>BF16(推荐)</b>, FP16, FP32，FP8*，INT8，不支持INT4</td>
  </tr>
  <tr>
    <td style="text-align: center;">单GPU显存消耗<br></td>
    <td colspan="2" style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> BF16: 76GB <br><b>diffusers BF16 : 10GB起* </b><br><b>diffusers INT8(torchao): 7G起* </b></td>
    <td style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> FP16: 18GB <br><b>diffusers FP16: 4GB起* </b><br><b>diffusers INT8(torchao): 3.6G起*</b></td>
    <td colspan="2" style="text-align: center;"><a href="https://github.com/THUDM/SwissArmyTransformer">SAT</a> BF16: 26GB <br><b>diffusers BF16 : 5GB起* </b><br><b>diffusers INT8(torchao): 4.4G起* </b></td>
  </tr>
  <tr>
    <td style="text-align: center;">多GPU推理显存消耗</td>
    <td colspan="2" style="text-align: center;"><b>BF16: 24GB* using diffusers</b><br></td>
    <td style="text-align: center;"><b>FP16: 10GB* using diffusers</b><br></td>
    <td colspan="2" style="text-align: center;"><b>BF16: 15GB* using diffusers</b><br></td>
  </tr>
  <tr>
    <td style="text-align: center;">推理速度<br>(Step = 50, FP/BF16)</td>
    <td colspan="2" style="text-align: center;">单卡A100: ~1000秒(5秒视频)<br>单卡H100: ~550秒(5秒视频)</td>
    <td style="text-align: center;">单卡A100: ~90秒<br>单卡H100: ~45秒</td>
    <td colspan="2" style="text-align: center;">单卡A100: ~180秒<br>单卡H100: ~90秒</td>
  </tr>
  <tr>
    <td style="text-align: center;">提示词语言</td>
    <td colspan="5" style="text-align: center;">English*</td>
  </tr>
  <tr>
    <td style="text-align: center;">提示词长度上限</td>
    <td colspan="2" style="text-align: center;">224 Tokens</td>
  
