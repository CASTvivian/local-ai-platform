# Missing Repo Summary Source: nicedreamzapp/claude-code-local

- URL: https://github.com/nicedreamzapp/claude-code-local
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/nicedreamzapp__claude-code-local
- Clone Status: cloned
- Language: Python
- Stars: 2597
- Topics: abliterated, ai-privacy, airgap, ambient-computing, anthropic, apple-silicon, browser-agent, claude-code, gemma, llama, local-ai, local-llm, macos, mlx, mlx-lm, offline-ai, on-device-ai, private-ai, qwen, voice-ai
- Description: Run Claude Code 100% on-device with local AI on Apple Silicon. MLX-native Anthropic-API server, 65 tok/s Qwen 3.5 122B, Llama 3.3 70B, Gemma 4 31B. Private, offline, airgap-ready. Built for NDA / legal / healthcare workflows.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <h1 align="center">🧠⚡ Claude Code Local — The Lineup</h1>
  <p align="center">
    <strong>Three local AI brains. Four modes. One MacBook. Zero cloud.<br>Pick your fighter and run Claude Code 100% on-device.<br>📍 Now with <a href="#-new-deepseek-v4-flash-via-ds4">DeepSeek V4 Flash · 1M-token context · via Antirez's <code>ds4</code> engine</a>.</strong>
  </p>
  <p align="center">
    <a href="https://github.com/nicedreamzapp/claude-code-local/stargazers"><img src="https://img.shields.io/github/stars/nicedreamzapp/claude-code-local?style=for-the-badge&logo=github&color=f5c542&labelColor=1f2328" alt="GitHub stars"></a>
    <a href="https://github.com/nicedreamzapp/claude-code-local/network/members"><img src="https://img.shields.io/github/forks/nicedreamzapp/claude-code-local?style=for-the-badge&logo=github&color=4c9a2a&labelColor=1f2328" alt="GitHub forks"></a>
    <a href="#-the-lineup--pick-your-fighter"><img src="https://img.shields.io/badge/🥊_Lineup-3_Models-red?style=for-the-badge" alt="3 Models"></a>
    <a href="#-the-modes"><img src="https://img.shields.io/badge/🎮_Modes-4-purple?style=for-the-badge" alt="4 Modes"></a>
    <a href="#-benchmarks"><img src="https://img.shields.io/badge/⚡_Qwen_3.5-65_tok%2Fs-brightgreen?style=for-the-badge" alt="Qwen 3.5 speed"></a>
    <a href="#-benchmarks"><img src="https://img.shields.io/badge/🚀_Claude_Code_Task-17.6s_(Qwen)-blue?style=for-the-badge" alt="Claude Code task time"></a>
    <a href="#-safety--how-the-data-flows"><img src="https://img.shields.io/badge/🔒_Privacy-100%25_Local-success?style=for-the-badge" alt="100% Local"></a>
    <a href="#-hands-free-voice-mode--the-whole-loop-on-device"><img src="https://img.shields.io/badge/🎤_Voice-Hands_Free-orange?style=for-the-badge" alt="Hands-Free Voice"></a>
    <a href="#-the-complete-local-first-stack"><img src="https://img.shields.io/badge/🪴_Ambient-Computing-ff69b4?style=for-the-badge" alt="Ambient Computing"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/📜_License-MIT-yellow?style=for-the-badge" alt="MIT"></a>
    <a href="https://discord.gg/ZdSqgAxUW"><img src="https://img.shields.io/discord/1497121921580404818?label=NiceDreamzApps&logo=discord&color=5865F2&style=for-the-badge" alt="Join the NiceDreamzApps Discord"></a>
  </p>
  <p align="center">
    <em>Built by <a href="https://x.com/NiceDreamzApps">Matt Macosko</a> in Arcata, CA. Started with a chicken problem. Still figuring it out.</em>
  </p>
  <p align="center">
    <a href="#-watch-the-demo--airgap-ai">🎬 Demo</a> ·
    <a href="#-the-lineup--pick-your-fighter">🥊 Lineup</a> ·
    <a href="#-the-modes">🎮 Modes</a> ·
    <a href="#-quick-start-3-commands">🚀 Quick Start</a> ·
    <a href="#-benchmarks">📊 Benchmarks</a> ·
    <a href="#-safety--how-the-data-flows">🔒 Safety</a> ·
    <a href="#-hands-free-voice-mode--the-whole-loop-on-device">🎤 Voice</a> ·
    <a href="#-the-complete-local-first-stack">🧩 The Stack</a> ·
    <a href="#-whats-next">🛣️ Roadmap</a> ·
    <a href="#-contributing--ideas">🤝 Contribute</a>
  </p>
</p>

---

<p align="center">
  <h2 align="center">🎬 WATCH THE DEMO — AirGap AI</h2>
  <p align="center">
    <strong>A real NDA. Llama 3.3 70B. Wi-Fi physically OFF. <code>lsof</code> running live.<br>
    Watch a 70-billion-parameter model audit a confidential legal document, on-device, with the receipts on screen.</strong>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=V_J1LpNGwmY">
      <img src="https://img.youtube.com/vi/V_J1LpNGwmY/maxresdefault.jpg" width="720" alt="AirGap AI — Wi-Fi OFF NDA Demo">
    </a>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=V_J1LpNGwmY">
      <img src="https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
    </a>
    &nbsp;
    <a href="https://www.youtube.com/@nicedreamzapps">
      <img src="https://img.shields.io/badge/Subscribe-@nicedreamzapps-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Subscribe">
    </a>
  </p>
  <p align="center">
    <em>Built for lawyers, accountants, doctors, therapists, contractors — anyone handling other people's private stuff.</em>
  </p>
  <p align="center">
    <a href="https://nicedreamzwholesale.com/airgap/">
      <img src="https://img.shields.io/badge/📞_Need_this_for_your_firm%3F-Book_a_15--min_call-black?style=for-the-badge" alt="Book a call">
    </a>
  </p>
</p>

---

<p align="center">
  <h2 align="center">🏁 HEXAGON SHOOTOUT — Free AI vs $100/mo Claude Code</h2>
  <p align="center">
    <strong>Three AIs. One laptop. Same prompt. Live counters.<br>
    Watch Gemma 31B local, Llama 70B local, and Claude cloud race the same HTML physics prompt on a MacBook.</strong>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=2KeTDDodE0A">
      <img src="https://img.youtube.com/vi/2KeTDDodE0A/maxresdefault.jpg" width="720" alt="Hexagon Shootout — 3 AIs, 1 laptop, same prompt, live">
    </a>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=2KeTDDodE0A">
      <img src="https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
    </a>
    &nbsp;
    <a href="https://www.youtube.com/@nicedreamzapps">
      <img src="https://img.shields.io/badge/Subscribe-@nicedreamzapps-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Subscribe">
    </a>
  </p>
  <p align="center">
    <em>Gemma 31B: 56s · Claude cloud: 22s · Llama 70B: 2:17 — two of three ran with zero cloud calls.</em>
  </p>
</p>

---

<p align="center">
  <h3 align="center">🎤 Also on the channel — NarrateClaude (Hands-Free Ambient AI)</h3>
  <p align="center">
    <em>Speak to Claude Code, hear replies in a cloned voice — 100% on-device. 2:31.</em>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=4ETqEjjopUk">
      <img src="https://img.youtube.com/vi/4ETqEjjopUk/maxresdefault.jpg" width="540" alt="NarrateClaude Hands-Free Ambient AI Demo">
    </a>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=4ETqEjjopUk"><img src="https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch"></a>
    &nbsp;
    <a href="https://www.youtube.com/@nicedreamzapps"><img src="https://img.shields.io/badge/Subscribe-@nicedreamzapps-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Subscribe"></a>
  </p>
</p>

---

<p align="center">
  <h3 align="center">🏠 New — My Mac mini at home is the AI. I just talk to it from any browser.</h3>
  <p align="center">
    <em>Open any browser on any phone — chat with the Mac mini at home, hear it reply in your own cloned voice. 0:50.</em>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=PLbV4QtFmFY">
      <img src="https://img.youtube.com/vi/PLbV4QtFmFY/maxresdefault.jpg" width="540" alt="My Mac mini at home is the AI — browser-anywhere demo">
    </a>
  </p>
  <p align="center">
    <a href="https://www.youtube.com/watch?v=PLbV4QtFmFY"><img src="https://img.shields.io/badge/▶_Watch_on_YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch"></a>
    &nbsp;
    <a href="https://www.youtube.com/@nicedreamzapps"><img src="https://img.shields.io/badge/Subscribe-@nicedreamzapps-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Subscribe"></a>
  </p>
</p>

---

> ## 🧩 This repo is the **BRAIN** of a 4-part local-first ambient-computing stack
>
> Brain (here) · 🎤 Ears+Mouth · 🌐 Hands · 📱 Phone. Each repo stands alone; together they take Claude Code off the keyboard and off the screen. **[Jump to the stack diagram →](#-the-complete-local-first-stack)**
>
> 🖥️ **More of my open-source software:** [**nicedreamzwholesale.com/software**](https://nicedreamzwholesale.com/software/)

---

## 🥊 The Lineup — Pick Your Fighter

We started with one model. Now we ship a **roster**. Same MLX server, same Anthropic API, swap one env var and you swap the brain — plus the brand-new `ds4` engine for DeepSeek V4 Flash slotted in via its own native Metal runtime.

| | 🟢 **Gemma 4 31B** | 🔵 **Qwen 3.5 122B** | 🐳 **DeepSeek V4 Flash** ⭐ |
|---|:---:|:---:|:---:|
| Nickname | The Quick One | The Beast | The 1M-Context Whale |
| Build | 4-bit IT abliterated | 4-bit MoE (A10B) | 2-bit asymmetric (ds4 GGUF) |
| Speed | ~15 tok/s | **65 tok/s** 🚀 | ~32 tok/s |
| Params | 31 B dense | 122 B / 10 B active | **284 B / 37 B active** |
| Context | 128 K | 256 K | **1 M tokens** |
| RAM | ~18 GB | ~75 GB | ~81 GB |
| Disk | 18 GB | 65 GB | 81 GB (+ disk KV cache) |
| Best at | Daily coding, fits 64 GB Mac | Max throughput, active sparsity | Long context, agentic loops |
| Engine | MLX Native | MLX Native | [`antirez/ds4`](https://github.com/antirez/ds4) |
| Launcher | `Gemma 4 Code.command` | `Claude Local.command` | `DeepSeek V4 Flash.app` |
| Min RAM to run | 32 GB | 96 GB | 128 GB |

> 💡 **Fun fact:** Qwen wins raw speed because it's an MoE — only 10B of 122B params activate per token. DeepSeek V4 Flash is even bigger (284B) but only ~37B active per token, *and* it ships with on-disk KV cache so a 25k-token Claude Code system prompt prefills exactly once, ever.

### 🐳 New: DeepSeek V4 Flash via `ds4`

We tested it the day Antirez (the Redis guy) shipped `ds4`. **Local DeepSeek beat cloud Claude on wall-clock time** on the same MacBook, same prompt.

<p align="center">
  <a href="https://youtu.be/7l8-s8xkpms" target="_blank">
    <img src="https://img.youtube.com/vi/7l8-s8xkpms/maxresdefault.jpg" alt="Three-way local AI comparison — DeepSeek V4 Flash vs Cloud Claude vs Gemma 4 31B" width="640">
  </a>
  <br>
  <em>▶ Watch on YouTube — DeepSeek V4 Flash vs Cloud Claude vs Gemma 4 31B<br>same prompt · three completely different auroras · one MacBook</em>
</p>

| | |
|---|---|
| 🧠 **Engine** | [`antirez/ds4`](https://github.com/antirez/ds4) — pure C + Metal kerne

# FILE: docs/BENCHMARKS.md

# Benchmarks — Claude Code Local (MLX Native Server)

## System

| | |
|---|---|
| **Machine** | MacBook Pro M5 Max |
| **Chip** | Apple M5 Max |
| **Memory** | 128 GB Unified |
| **Server** | MLX Native Anthropic Server (custom, ~800 lines Python) |
| **KV cache** | 4-bit / 8-bit quantized (MLX Metal GPU) |
| **Claude Code** | v2.1.84 |

---

## 🥊 The Lineup — Three Fighters, One Server

The same MLX server runs all three. Just swap the `MLX_MODEL` env var.

| Model | Tier | Architecture | Disk | RAM | tok/s | Best at |
|---|---|---|:---:|:---:|:---:|---|
| **Qwen 3.5 122B-A10B** | 🔵 THE BEAST | MoE 122B / 10B active, 4-bit | 65 GB | ~75 GB | **65** | Maximum throughput |
| **Llama 3.3 70B Abliterated** ⭐ | 🟠 THE WISE ONE | Dense 71B, 8-bit affine, group 64, 128K ctx | 75 GB | ~75 GB | ~7 | Hardest reasoning |
| **Gemma 4 31B Abliterated** | 🟢 THE QUICK ONE | Dense 31B, 4-bit IT | 18 GB | ~18 GB | ~15 | Daily coding, low RAM |

> ⭐ The Llama 3.3 70B build is **our own MLX-packed upload**: [`divinetribe/Llama-3.3-70B-Instruct-abliterated-8bit-mlx`](https://huggingface.co/divinetribe/Llama-3.3-70B-Instruct-abliterated-8bit-mlx). 8-bit affine quantization with group size 64, chosen to preserve quality over minimal footprint. Built on top of [huihui-ai's abliteration](https://huggingface.co/huihui-ai) of Meta's Llama 3.3 70B Instruct.

> Qwen wins raw tok/s because only 10B of its 122B params activate per token (MoE). Llama is the slowest but the smartest at 8-bit full precision. Gemma is the lightweight champion — fits on a 64 GB Mac with room to spare.

---

## Generation Speed (Qwen 3.5 122B — measured)

| Max Tokens | Output Tokens | Time | **Tokens/sec** |
|:---:|:---:|:---:|:---:|
| 100 | 100 | 2.2s | **45.0 tok/s** |
| 500 | 500 | 7.7s | **64.8 tok/s** |
| 1000 | 1000 | 15.3s | **65.4 tok/s** |

Sustained generation at 65 tok/s. Short requests are slower (45 tok/s) due to prompt-processing overhead amortized over fewer tokens.

---

## Three Generations — Our Optimization Journey

```
Generation Speed (tok/s):

  Gen 1: Ollama + proxy              ████████████████████████████████ 30
  Gen 2: llama.cpp TurboQuant        █████████████████████████████████████████ 41
  Gen 3: MLX Native (no proxy)       █████████████████████████████████████████████████████████████████ 65
```

```
Claude Code Task Time (seconds):

  Gen 1: Ollama + proxy              █████████████████████████████████████████████████████████ 133s
  Gen 2: llama.cpp TurboQuant        █████████████████████████████████████████████████████████ 133s
  Gen 3: MLX Native (no proxy)       ████████ 17.6s
```

| Generation | Stack | tok/s | Claude Code E2E | What Changed |
|:---:|---|:---:|:---:|---|
| 1 | Ollama → Proxy → Claude Code | 30 | 133s | Baseline |
| 2 | llama.cpp TurboQuant → Proxy → Claude Code | 41 | 133s | +37% speed, 4.9x KV compression |
| **3** | **MLX Server → Claude Code (direct)** | **65** | **17.6s** | **+117% speed, eliminated proxy** |

---

## vs Cloud APIs

| | **MLX Native (Local)** | Claude Sonnet (Cloud) | Claude Opus (Cloud) |
|---|:---:|:---:|:---:|
| **Generation speed** | 65 tok/s | ~80 tok/s | ~40 tok/s |
| **Claude Code task** | 17.6s | ~10s | ~15s |
| **Cost / million tokens** | **$0** | $3 / $15 | $15 / $75 |
| **Privacy** | **100% on-device** | Cloud | Cloud |
| **Works offline** | **Yes** | No | No |
| **Monthly cost** | **$0** | $20-100+ | $20-100+ |

Our local setup **beats cloud Opus on speed** (65 vs 40 tok/s) and is within striking distance of Sonnet.

---

## Why MLX Native is Faster

| Factor | Impact |
|--------|--------|
| **No proxy** | Eliminated API translation overhead — the #1 bottleneck |
| **MLX framework** | Apple's own ML framework, built for Metal GPU + unified memory |
| **Native Anthropic API** | Server speaks Claude Code's language directly |
| **Unified memory** | Zero-copy between CPU and GPU — model weights stay in place |
| **MoE efficiency (Qwen 122B)** | Only 10B of 122B params activate per token — fast on unified memory |

---

## Gemma 4 31B — Prompt Latency Fix (M4 Pro, 64 GB)

Gemma 4 is a reasoning model that produces `<|channel>thought\n…<channel|>` blocks before every response. Combined with Claude Code's verbose tool descriptions, the effective prompt was ~5 600 tokens per turn — causing ~60 s of prefill before the first output token.

Two server-side fixes cut E2E latency by ~4×:

| Fix | Mechanism | Tokens saved | Latency before | Latency after |
|---|---|:---:|:---:|:---:|
| **Tool description slimming** | Strip all text from tool definitions in code mode, keep only name + param types | ~5 400 tok | ~60 s prefill | ~2 s prefill |
| **Thinking suppression** (`MLX_SUPPRESS_THINKING=1`) | Pre-fill an empty `<\|channel>thought\n<channel\|>` block so the model skips its reasoning chain | ~300–500 tok generated | ~40 s generation | ~1 s generation |

```
Gemma 4 31B "hello" latency (M4 Pro, warm server):

  Before fixes    ████████████████████████████████████████████████████████████████████████████ ~120 s
  After fixes     ████ ~3-5 s
```

Generation speed is hardware-bound at ~13.5 tok/s on M4 Pro (memory bandwidth limit for a 17 GB model). The latency reduction comes entirely from eliminating unnecessary tokens — not from changing the model or quantization.

---

## Methodology

- All benchmarks run on a warm server (model already loaded)
- Each test run once (not averaged — these are representative single runs)
- Claude Code E2E includes full Claude Code startup, system prompt processing, and generation
- KV cache quantized via MLX's built-in `QuantizedKVCache`
- Temperature: 0.2 for tool-call reliability runs, 0.7 for raw generation runs
- Qwen 122B numbers are measured. Gemma 4 31B (~15 tok/s) and Llama 3.3 70B (~7 tok/s) are observed approximations from real-world Claude Code usage on the same M5 Max — full benchmarks pending.


# FILE: docs/MAC-BASE-SETUP.md

# Mac Base / Pro 16 GB Setup Guide

Este documento descreve as adaptacoes necessarias para rodar
`claude-code-local` em MacBooks Apple Silicon de entrada/Pro com **16 GB
de memoria unificada** - hardware abaixo do alvo original do projeto
(M Max / Ultra com 64-128 GB).

A documentacao oficial do repositorio assume Mac Max/Ultra. Em hardware
mais modesto, seis problemas reproduziveis aparecem em sequencia:

1. Tela de selecao de login do Claude Code mesmo com `ANTHROPIC_API_KEY` setado
2. Vazamento de tokens internos do modelo (`<|im_end|>`, `<|endoftext|>`, ...) na resposta
3. Respostas vazias ("(No output)") em todas as mensagens
4. Tool-calls do Qwen 2.5 nao reconhecidos pelo parser do servidor
5. Claude Code chama `api.anthropic.com` no startup mesmo com `ANTHROPIC_BASE_URL` setado (vazamento de "100% offline")
6. **Tools nunca executam:** Claude Code descarta toda resposta com `tool_use` porque o servidor responde JSON unico em vez de `text/event-stream`

Este guia explica a causa de cada um e a correcao aplicada nesta branch.

---

## 1. Bug do macOS keychain - tela de login persistente

### Sintoma

Apos rodar o launcher, voce ve a tela de selecao do Claude Code:

```
Select login method:
  1. Claude account with subscription
  2. Anthropic Console account
  3. 3rd-party platform
```

Mesmo com `ANTHROPIC_API_KEY=sk-local` exportado no ambiente.

### Causa

Bug conhecido do Claude Code 2.1.x no macOS - issues
[#25069](https://github.com/anthropics/claude-code/issues/25069) e
[#27900](https://github.com/anthropics/claude-code/issues/27900) no
repositorio oficial. A logica de verificacao do keychain do macOS roda
**antes** da leitura da variavel de ambiente, e quando o keychain esta
vazio o CLI cai no fluxo OAuth em vez de usar a env var.

A flag `--bare` que o repositorio original passa nos launchers nao
existe nas versoes recentes do CLI.

### Correcao

Combinacao de tres ajustes:

1. Setar `hasCompletedOnboarding: true` em `~/.claude.json`:
   ```bash
   python3 -c "
   import json, pathlib
   p = pathlib.Path.home() / '.claude.json'
   d = json.loads(p.read_text()) if p.exists() else {}
   d['hasCompletedOnboarding'] = True
   p.write_text(json.dumps(d, indent=2))
   "
   ```

2. Exportar `ANTHROPIC_AUTH_TOKEN` junto com `ANTHROPIC_API_KEY` (a
   presenca do auth token destrava o caminho de API key no modo
   interativo).

3. Setar `DISABLE_LOGIN_COMMAND=1` para esconder o comando `/login`
   dentro da sessao interativa.

Os launchers `Claude Chat.command` e `Claude Agentico.command` aplicam
os tres automaticamente.

---

## 2. Vazamento de tokens internos do modelo

### Sintoma

Em vez da resposta esperada, voce ve:

```
> me fale sobre typescript
<|endoftext|><|im_start|>user
<system-
```

Os tokens especiais do tokenizer aparecem no texto da resposta.

### Causa

O `clean_response` em `proxy/server.py` so tinha logica para os stop
markers do **Gemma 4** (`<turn|>`, `<|turn>`). Quando o servidor roda
qualquer outro modelo - Qwen, Llama, modelos ChatML em geral - os
markers `<|im_end|>`, `<|im_start|>`, `<|endoftext|>`, `<|eot_id|>` nao
eram tratados. O modelo sinalizava fim de turno corretamente, mas o
servidor nao truncava no marker e o texto vazava.

### Correcao

Patch em `proxy/server.py:132`:

```python
# Antes
for stop_marker in ['<turn|>', '<|turn>']:

# Depois
for stop_marker in ['<turn|>', '<|turn>', '<|im_end|>', '<|endoftext|>',
                    '<|im_start|>', '<|end_of_text|>', '<|eot_id|>']:
```

Truncamento de saida no primeiro marker encontrado, agora cobrindo
ChatML (Qwen, Mistral, varios modelos), Llama 3.x e Gemma.

---

## 3. Extended thinking quebra modelos pequenos

### Sintoma

Toda mensagem retorna "(No output)" no Claude Code, mesmo sem tools
e mesmo apos o fix de stop markers.

No log do servidor MLX:

```
[06:14:25] POST /v1/messages tools=25
[06:14:25]   Generated: 27 tokens - "O usuario esta testando o sistema..."
[06:14:25] POST /v1/messages tools=25
[06:14:25]   Generated: 6 tokens - "(No output)"
```

### Causa

O Claude Code 2.1 introduziu **extended thinking**: para cada turno,
faz duas chamadas ao modelo - a primeira pede `thinking` (cadeia de
raciocinio interna), a segunda pede `text` (resposta final).

Modelos pequenos / quantizados gastam o orcamento todo na primeira
chamada (raciocinando) e quando recebem a segunda nao tem mais o que
gerar - emitem so `<|im_end|>` direto e o texto sai vazio.

### Correcao

Forcar `--effort low` no Claude Code, que desativa o extended thinking
e faz cada turno virar uma unica chamada:

```bash
claude --model claude-sonnet-4-6 --effort low ...
```

Aplicado por padrao nos dois launchers desta branch.

---

## 4. Tool-calls do Qwen 2.5 nao reconhecidos

### Sintoma

Modo agentico nao executa nada. O modelo gera o pedido de tool, mas o
Claude Code nao executa - aparece como texto puro:

```
> use Bash to print pwd
<tools>
{"name": "Bash", "arguments": {"command": "pwd"}}
</tools>
```

### Causa

O `parse_tool_calls` em `proxy/server.py` cobria `<tool_call>...</tool_call>`
(formato Qwen 3.5 e variantes ChatML modernas) e `<|tool_call>...<tool_call|>`
(Gemma 4 nativo), mas **nao** cobria `<tools>...</tools>` - o formato que o
Qwen 2.5 Coder 14B emite naturalmente.

Sem o parser reconhecer a tag, o servidor devolvia o conteudo como bloco
de texto e o Claude Code nao tinha como executar.

### Correcao

Adicionado **Format 3.5** ao `parse_tool_calls` para reconhecer o
wrapper `<tools>...</tools>`, com suporte a payload unico (objeto JSON)
ou multiplos (array de objetos):

```python
pattern_qwen25 = r'<tools>\s*(.*?)\s*</tools>'
for match in re.finditer(pattern_qwen25, text, re.DOTALL):
    content = match.group(1).strip()
    call_data = json.loads(content)
    # aceita lista [{"name":..,"arguments":..}, ...] ou um objeto unico
```

Validado com `Bash({"command":"pwd"})` retornando `stop_reason: tool_use`.

---

## 5. Vazamento "100% offline" - Claude Code chama api.anthropic.com no startup

Esta foi a descobert

# FILE: docs/TWITTER-THREAD.md

# Twitter/X Thread — Claude Code Local

---

**Tweet 1 (Hook)**

I'm running Claude Code with THREE local AI models on my MacBook.

122B params at 65 tok/s. 70B for hardest reasoning. 31B for daily speed.

No internet. No API fees. No data leaves my machine.

Here's the lineup and how I built it:

---

**Tweet 2 (The Lineup)**

The fighters:

🔵 Qwen 3.5 122B — THE BEAST (65 tok/s, MoE A10B, 4-bit)
🟠 Llama 3.3 70B Abliterated — THE WISE ONE (~7 tok/s, 8-bit affine, 128K ctx) ⭐ I packed and uploaded this one myself: huggingface.co/divinetribe/Llama-3.3-70B-Instruct-abliterated-8bit-mlx
🟢 Gemma 4 31B Abliterated — THE QUICK ONE (~15 tok/s, 4-bit IT)

Same MLX server runs all three. Swap one env var and you swap the brain.

---

**Tweet 3 (The Problem We Solved)**

Claude Code only speaks Anthropic's API. Local models speak OpenAI's API.

Most projects bridge this with a proxy. Proxies add latency, complexity, and break things.

We deleted the proxy.

We wrote a server that speaks Anthropic API natively, with MLX inference under the hood.

Result: 7.5x faster than the proxy approach.

---

**Tweet 4 (Benchmarks)**

The numbers (Qwen 3.5 122B, measured on M5 Max 128 GB):

- 65 tokens/sec sustained generation
- 17.6 seconds for a real Claude Code coding task (down from 133s with a proxy)
- Tool-call reliability: 98/98 tests passing across 7 runs
- Beats cloud Opus on raw tok/s

---

**Tweet 5 (Privacy + Safety)**

Why this matters:

🔒 100% on-device. Nothing ever leaves your Mac.
✈️ Works on a plane. No internet, no problem.
🚫 No telemetry. No analytics. No phone-home.
📜 Every dependency audited. We yanked LiteLLM after the supply-chain scare.
💰 $0/month after hardware.

Same Claude Code experience. Zero data exposure.

---

**Tweet 6 (Modes)**

Four ways to use it:

1. **Code mode** — Claude Code with the local model (Gemma / Llama / Qwen)
2. **Browser mode** — Autonomous Brave browser agent via Chrome DevTools Protocol
3. **Narrative mode** — Every reply spoken aloud through your TTS or cloned voice
4. **Phone mode** — iMessage in, video out, full pipeline from your couch

---

**Tweet 7 (How to Set Up)**

```
git clone https://github.com/nicedreamzapp/claude-code-local
cd claude-code-local
bash setup.sh
```

Auto-detects your RAM, picks a model from the lineup, downloads it, builds the launcher.

Double-click the launcher on your Desktop. You're coding locally.

---

**Tweet 8 (Closer)**

2026 is the year AI goes fully local.

The hardware is here. The models are here. The tools are catching up.

You don't need a cloud subscription to have an AI coding partner anymore.
You don't need to ship your code to a server farm.
You don't need to pay $20-100/mo for what your laptop already runs.

Open source. Link in bio. Go build something.

---

*Suggested images/video per tweet:*
1. Hero shot — three model "fighter cards" side by side
2. Architecture diagram from README
3. Terminal showing the MLX server log on startup
4. Benchmark bar chart from BENCHMARKS.md
5. The data-flow safety diagram from README
6. Four-up screenshot of the four modes running
7. Terminal showing the 3-command setup
8. MacBook running on a plane, no wifi, Claude Code working

