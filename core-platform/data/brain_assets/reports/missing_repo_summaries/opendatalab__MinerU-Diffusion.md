# Missing Repo Summary Source: opendatalab/MinerU-Diffusion

- URL: https://github.com/opendatalab/MinerU-Diffusion
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/opendatalab__MinerU-Diffusion
- Clone Status: cloned
- Language: Python
- Stars: 590
- Topics: ai4science, diffusion, dlm, document-analysis, extract-data, layout-analysis, llada, ocr, parser, pdf, pdf-converter, pdf-extractor-llm, pdf-extractor-pretrain, pdf-extractor-rag, pdf-parser, python
- Description: A diffusion-based framework for document OCR that replaces autoregressive decoding with block-level parallel diffusion decoding. 

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="assets/banner.png" alt="MinerU-Diffusion" width="100%">
</p>

# MinerU-Diffusion: Rethinking Document OCR as Inverse Rendering via Diffusion Decoding

<p align="center">
  <img src="https://img.shields.io/badge/✨_Diffusion_Decoding-darkgreen?style=for-the-badge" alt="Diffusion Decoding" />
  <img src="https://img.shields.io/badge/⚡_Fast_Inference-yellow?style=for-the-badge" alt="Fast Inference" />
  <img src="https://img.shields.io/badge/🧩_Block--wise_Parallel-blue?style=for-the-badge" alt="Block-wise Parallel" />
  <img src="https://img.shields.io/badge/📄_Robust_OCR-red?style=for-the-badge" alt="Robust OCR" />
  <img src="https://img.shields.io/badge/🏗️_Layout_Aware-orange?style=for-the-badge" alt="Layout Aware" />
  <img src="https://img.shields.io/badge/🚀_SGLang_Ready-purple?style=for-the-badge" alt="SGLang Ready" />
  <img src="https://img.shields.io/badge/🤗_2.5B_Model-brightgreen?style=for-the-badge" alt="2.5B Model" />
  <br><br>
  <a href="https://arxiv.org/pdf/2603.22458"><img src="https://img.shields.io/badge/📄_Tech_Report-red?style=flat-square" alt="Tech Report" /></a>
  <a href="https://huggingface.co/opendatalab/MinerU-Diffusion-V1-0320-2.5B"><img src="https://img.shields.io/badge/🤗_Model-HuggingFace-yellow?style=flat-square" alt="Model" /></a>
  <a href="https://modelscope.cn/models/OpenDataLab/MinerU-Diffusion-V1-0320-2.5B"><img src="https://img.shields.io/badge/Model_on_ModelScope-purple?logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIzIiBoZWlnaHQ9IjIwMCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCiA8Zz4KICA8dGl0bGU+TGF5ZXIgMTwvdGl0bGU+CiAgPHBhdGggaWQ9InN2Z18xNCIgZmlsbD0iIzYyNGFmZiIgZD0ibTAsODkuODRsMjUuNjUsMGwwLDI1LjY0OTk5bC0yNS42NSwwbDAsLTI1LjY0OTk5eiIvPgogIDxwYXRoIGlkPSJzdmdfMTUiIGZpbGw9IiM2MjRhZmYiIGQ9Im05OS4xNCwxMTUuNDlsMjUuNjUsMGwwLDI1LjY1bC0yNS42NSwwbDAsLTI1LjY1eiIvPgogIDxwYXRoIGlkPSJzdmdfMTYiIGZpbGw9IiM2MjRhZmYiIGQ9Im0xNzYuMDksMTQxLjE0bC0yNS42NDk5OSwwbDAsMjIuMTlsNDcuODQsMGwwLC00Ny44NGwtMjIuMTksMGwwLDI1LjY1eiIvPgogIDxwYXRoIGlkPSJzdmdfMTciIGZpbGw9IiMzNmNmZDEiIGQ9Im0xMjQuNzksODkuODRsMjUuNjUsMGwwLDI1LjY0OTk5bC0yNS42NSwwbDAsLTI1LjY0OTk5eiIvPgogIDxwYXRoIGlkPSJzdmdfMTgiIGZpbGw9IiMzNmNmZDEiIGQ9Im0wLDY0LjE5bDI1LjY1LDBsMCwyNS42NWwtMjUuNjUsMGwwLC0yNS42NXoiLz4KICA8cGF0aCBpZD0ic3ZnXzE5IiBmaWxsPSIjNjI0YWZmIiBkPSJtMTk4LjI4LDg5Ljg0bDI1LjY0OTk5LDBsMCwyNS42NDk5OWwtMjUuNjQ5OTksMGwwLC0yNS42NDk5OXoiLz4KICA8cGF0aCBpZD0ic3ZnXzIwIiBmaWxsPSIjMzZjZmQxIiBkPSJtMTk4LjI4LDY0LjE5bDI1LjY0OTk5LDBsMCwyNS42NWwtMjUuNjQ5OTksMGwwLC0yNS42NXoiLz4KICA8cGF0aCBpZD0ic3ZnXzIxIiBmaWxsPSIjNjI0YWZmIiBkPSJtMTUwLjQ0LDQybDAsMjIuMTlsMjUuNjQ5OTksMGwwLDI1LjY1bDIyLjE5LDBsMCwtNDcuODRsLTQ3Ljg0LDB6Ii8+CiAgPHBhdGggaWQ9InN2Z18yMiIgZmlsbD0iIzM2Y2ZkMSIgZD0ibTczLjQ5LDg5Ljg0bDI1LjY1LDBsMCwyNS42NDk5OWwtMjUuNjUsMGwwLC0yNS42NDk5OXoiLz4KICA8cGF0aCBpZD0ic3ZnXzIzIiBmaWxsPSIjNjI0YWZmIiBkPSJtNDcuODQsNjQuMTlsMjUuNjUsMGwwLC0yMi4xOWwtNDcuODQsMGwwLDQ3Ljg0bDIyLjE5LDBsMCwtMjUuNjV6Ii8+CiAgPHBhdGggaWQ9InN2Z18yNCIgZmlsbD0iIzYyNGFmZiIgZD0ibTQ3Ljg0LDExNS40OWwtMjIuMTksMGwwLDQ3Ljg0bDQ3Ljg0LDBsMCwtMjIuMTlsLTI1LjY1LDBsMCwtMjUuNjV6Ii8+CiA8L2c+Cjwvc3ZnPg==&labelColor=white&style=flat-square" alt="Model on ModelScope" /></a>
  <a href="https://huggingface.co/spaces/opendatalab/MinerU-Diffusion-V1-0320-2.5B"><img src="https://img.shields.io/badge/🤗_Demo-HuggingFace-yellow?style=flat-square" alt="Demo on Hugging Face" /></a>
  <a href="https://github.com/sgl-project/sglang"><img src="https://img.shields.io/badge/SGLang-Supported-purple?style=flat-square" alt="SGLang Supported" /></a>
  <a href="https://github.com/GeeeekExplorer/nano-vllm"><img src="https://img.shields.io/badge/Nano--DVLM-Adapted-yellow?style=flat-square" alt="Nano-DVLM Adapted" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="License MIT" /></a>
</p>

<div align="center">
  <a href="https://huggingface.co/papers/2603.22458">
    <img src="assets/huggingface_paper_gold_day.svg"/>
  </a>
</div>

<p align="center">
  <video src="https://github.com/user-attachments/assets/bf3e73a1-6d24-48b5-9dbe-94efee3993e0" controls width="200" align="center"></video>
</p>



## 📰 News

- **[2026/3/24]** 🔥 We release **MinerU-Diffusion-V1** — a 2.5B diffusion-based framework for document OCR that
replaces autoregressive decoding with block-level parallel diffusion decoding.

## 🎯 Roadmap

Our long-term goal is to **build efficient and reliable 2.5B diffusion-based decoding for document OCR**. 

- ✅ **Release MinerU-Diffusion-V1:** A 2.5B diffusion-based framework for document OCR that replaces autoregressive decoding with block-level parallel diffusion decoding.
- ✅ Support [SGLang](https://github.com/sgl-project/sglang) to accommodate diffusion computation.
- ✅ Complete the [Nano-vLLM](https://github.com/GeeeekExplorer/nano-vllm) adaptation used by our `nano_dvlm` engine for single-GPU inference.
- ✅ Complete the Gradio-based interactive demo implementation.
- ⬜ Release MinerU-Diffusion-V2: More Small, More Faster, More Elegant, More Powerful!
- ⬜ Release Training Code

---

## 💡 TL;DR

> **MinerU-Diffusion** reframes document OCR as an inverse rendering problem and replaces slow, error-prone autoregressive decoding with parallel diffusion decoding.

By introducing block-wise diffusion, uncertainty-driven curriculum learning, it achieves up to 3.2× faster decoding while improving robustness and reducing reliance on language priors.

<p align="center">
  <img src="assets/decode.png" alt="Diffusion Decoding" width="700">
</p>

<p align="center">
  <em>Diffusion decoding progressively reconstructs structured text from masked tokens under visual conditioning: black tokens are confirmed, red tokens are being updated, and yellow tokens remain masked, enabling parallel generation with global consistency, in contrast to autoregressive left-to-right decoding.</em>
</p>

<p align="center">
  <img src="assets/train.png"  alt="Overview"  width="600">
</p>

<p align="center">
  <em>Training of MinerU-Diffusion. Left: the target token sequence is randomly masked to form a partially observed input, and the model predicts only the masked positions under visual and prompt conditioning. Right: the structured block-attention mask used during training, where tokens attend bidirectionally within each block and causally to all preceding blocks, enabling parallel diffusion refinement within blocks while preserving coarse autoregressive structure across blocks.</em>
</p>

## 📈 Performance

<p align="center">
  <img src="assets/performance_tradeoff.jpeg" alt="Performance Trade-off" width="775">
</p>

MinerU-Diffusion provides a flexible accuracy-throughput trade-off through threshold control. Compared with MinerU2.5, it achieves up to **3.26x** TPS, while also offering practical operating points such as **2.12x speedup with 99.9% relative accuracy** and **3.01x speedup with 98.8% relative accuracy**.

## 🗂️ Repository Layout

```text
MinerU-Diffusion/
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
├── assets/
│   ├── banner.png
│   ├── decode.png
│   ├── homepage-demo.mp4
│   ├── image.png
│   ├── performance_tradeoff.jpeg
│   └── train.png
├── docs/
│   ├── MinerU-Diffusion-V1.pdf
│   ├── gradio/
│   │   ├── .gitignore
│   │   ├── app.py
│   │   ├── diffusion_hf.py
│   │   ├── mineru_hf.py
│   │   ├── runtime_paths.example.json
│   │   └── speed_compare/
│   └── sglang/
│       ├── README.md
│       ├── mineru_request.py
│       ├── run_infer.sh
│       └── run_server.sh
├── engines/
│   ├── __init__.py
│   ├── hf/
│   │   ├── __init__.py
│   │   └── runner.py
│   ├── nano_dvlm/
│   │   ├── .gitignore
│   │   ├── LICENSE
│   │   ├── __init__.py
│   │   ├── nanovllm/
│   │   ├── bench.py
│   │   ├── example.py
│   │   ├── llm_outputs/
│   │   └── pyproject.toml
│   └── sglang/
│       └── __init__.py
├── mineru_diffusion/
│   ├── __init__.py
│   ├── configuration_mineru_diffusion.py
│   ├── modeling_mineru_diffusion.py
│   ├── processing_mineru_diffusion.py
│   └── utils/
│       ├── __init__.py
│       └── bbox.py
├── requirements.txt
├── scripts/
│   ├── run_end2end.py
│   ├── run_end2end.sh
│   ├── run_inference.py
│   ├── run_inference.sh
│   └── run_sglang_server.sh
```

## 🌐 Online Experience

### Official online web application
The official web application provides a more complete product experience, including a polished interface and richer features. Login is required.

### Gradio-based online demo
A lightweight Gradio WebUI for trying the core parsing workflow. No login is required.

- [![HuggingFace](https://img.shields.io/badge/Demo_on_HuggingFace-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAF8AAABYCAMAAACkl9t/AAAAk1BMVEVHcEz/nQv/nQv/nQr/nQv/nQr/nQv/nQv/nQr/wRf/txT/pg7/yRr/rBD/zRz/ngv/oAz/zhz/nwv/txT/ngv/0B3+zBz/nQv/0h7/wxn/vRb/thXkuiT/rxH/pxD/ogzcqyf/nQvTlSz/czCxky7/SjifdjT/Mj3+Mj3wMj15aTnDNz+DSD9RTUBsP0FRO0Q6O0WyIxEIAAAAGHRSTlMADB8zSWF3krDDw8TJ1NbX5efv8ff9/fxKDJ9uAAAGKklEQVR42u2Z63qjOAyGC4RwCOfB2JAGqrSb2WnTw/1f3UaWcSGYNKTdf/P+mOkTrE+yJBulvfvLT2A5ruenaVHyIks33npl/6C4s/ZLAM45SOi/1FtZPyFur1OYofBX3w7d54Bxm+E8db+nDr12ttmESZ4zludJEG5S7TO72YPlKZFyE+YCYUJTBZsMiNS5Sd7NlDmKM2Eg2JQg8awbglfqgbhArjxkS7dgp2RH6hc9AMLdZYUtZN5DJr4molC8BfKrEkPKEnEVjLbgW1fLy77ZVOJagoIcLIl+IxaQZGjiX597HopF5CkaXVMDO9Pyix3AFV3kw4lQLCbHuMovz8FallbcQIJ5Ta0vks9RnolbCK84BtjKRS5uA43hYoZcOBGIG2Epbv6CvFVQ8m8loh66WNySsnN7htL58LNp+NXT8/PhXiBXPMjLSxtwp8W9f/1AngRierBkA+kk/IpUSOeKByzn8y3kAAAfh//0oXgV4roHm/kz4E2z//zRc3/lgwBzbM2mJxQEa5pqgX7d1L0htrhx7LKxOZlKbwcAWyEOWqYSI8YPtgDQVjpB5nvaHaSnBaQSD6hweDi8PosxD6/PT09YY3xQA7LTCTKfYX+QHpA0GCcqmEHvr/cyfKQTEuwgbs2kPxJEB0iNjfJcCTPyocx+A0griHSmADiC91oNGVwJ69RudYe65vJmoqfpul0lrqXadW0jFKH5BKwAeCq+Den7s+3zfRJzA61/Uj/9H/VzLKTx9jFPPdXeeP+L7WEvDLAKAIoF8bPTKT0+TM7W8ePj3Rz/Yn3kOAp2f1Kf0Weony7pn/cPydvhQYV+eFOfmOu7VB/ViPe34/EN3RFHY/yRuT8ddCtMPH/McBAT5s+vRde/gf2c/sPsjLK+m5IBQF5tO+h2tTlBGnP6693JdsvofjOPnnEHkh2TnV/X1fBl9S5zrwuwF8NFrAVJVwCAPTe8gaJlomqlp0pv4Pjn98tJ/t/fL++6unpR1YGC2n/KCoa0tTLoKiEeUPDl94nj+5/Tv3/eT5vBQ60X1S0oZr+IWRR8Ldhu7AlLj

# FILE: docs/sglang/README.md

# MinerU-Diffusion SGLang Notes

This directory contains the original SGLang prototype and related notes for running MinerU-Diffusion with an OpenAI-compatible SGLang server.

For normal use, prefer the unified repository-level entrypoints:

- `scripts/run_sglang_server.sh`
- `scripts/run_inference.sh` with `ENGINE=sglang`

This document keeps the lower-level SGLang notes in one place for debugging, validation, and reproduction.

## Environment

When running inside an SGLang checkout, make sure the runtime environment is set correctly:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install -e "python[all]"
```

## Recommended Server Commands

Recommended launch command:

```bash
PYTHONPATH=python CUDA_VISIBLE_DEVICES=0 sglang serve \
  --model-path <MODEL_PATH> \
  --host 127.0.0.1 \
  --port 31000 \
  --tp-size 1 \
  --dllm-algorithm LowConfidence \
  --mem-fraction-static 0.72 \
  --cuda-graph-max-bs 160
```

If you want a more conservative setup, you can disable CUDA graph:

```bash
PYTHONPATH=python CUDA_VISIBLE_DEVICES=0 sglang serve \
  --model-path <MODEL_PATH> \
  --host 127.0.0.1 \
  --port 31000 \
  --tp-size 1 \
  --dllm-algorithm LowConfidence \
  --disable-cuda-graph \
  --attention-backend triton \
  --sampling-backend pytorch
```

## Request Examples

The examples below use:

- `<BASE_URL>` for the server address, for example `http://127.0.0.1:31000`
- `<MODEL_PATH>` for the model directory
- `<IMAGE_PATH>` for the input image

### Formula Recognition

```bash
python - <<'PY'
import base64, json, pathlib, urllib.request

base_url = "<BASE_URL>/v1/chat/completions"
model = "<MODEL_PATH>"
img_path = pathlib.Path("<IMAGE_PATH>")
img_b64 = base64.b64encode(img_path.read_bytes()).decode("utf-8")

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Formula Recognition:"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
            ],
        }
    ],
    "max_tokens": 128,
}

req = urllib.request.Request(
    base_url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=120) as resp:
    print(resp.read().decode("utf-8"))
PY
```

### Table Recognition

```bash
python - <<'PY'
import base64, json, pathlib, urllib.request

base_url = "<BASE_URL>/v1/chat/completions"
model = "<MODEL_PATH>"
img_path = pathlib.Path("<IMAGE_PATH>")
img_b64 = base64.b64encode(img_path.read_bytes()).decode("utf-8")

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Table Recognition:"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
            ],
        }
    ],
    "max_tokens": 1024,
}

req = urllib.request.Request(
    base_url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=300) as resp:
    print(resp.read().decode("utf-8"))
PY
```

If the tokenizer is configured correctly, table outputs should preserve structure tokens such as `<fcel>` and `<nl>`.

### Layout Analysis

```bash
python - <<'PY'
import base64, json, pathlib, urllib.request

base_url = "<BASE_URL>/v1/chat/completions"
model = "<MODEL_PATH>"
img_path = pathlib.Path("<IMAGE_PATH>")
img_b64 = base64.b64encode(img_path.read_bytes()).decode("utf-8")

payload = {
    "model": model,
    "messages": [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Layout Analysis:"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}},
            ],
        }
    ],
    "max_tokens": 1024,
}

req = urllib.request.Request(
    base_url,
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req, timeout=300) as resp:
    print(resp.read().decode("utf-8"))
PY
```

## HF Baseline Comparison

If you have an HF-based demo script, you can compare the outputs with the same image and the same prompt type.

Generic example:

```bash
python <HF_DEMO_SCRIPT> \
  --model-path <MODEL_PATH> \
  --image-path <IMAGE_PATH> \
  --prompt-type table
```

## Recommended Runtime Settings

For a single-GPU setup with correctness as the priority, the recommended settings are:

```bash
--tp-size 1
--dllm-algorithm LowConfidence
--mem-fraction-static 0.72
--cuda-graph-max-bs 160
```

## Prototype Files in This Directory

The following files are preserved from the original standalone prototype:

- `run_server.sh`: starts an SGLang server with hard-coded local paths
- `mineru_request.py`: sends a single test request to the OpenAI-compatible endpoint
- `run_infer.sh`: runs `mineru_request.py`

These files are mainly useful for reproducing the original experiment or debugging low-level SGLang behavior.

