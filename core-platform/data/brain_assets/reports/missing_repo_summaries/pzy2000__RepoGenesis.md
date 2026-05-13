# Missing Repo Summary Source: pzy2000/RepoGenesis

- URL: https://github.com/pzy2000/RepoGenesis
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/pzy2000__RepoGenesis
- Clone Status: cloned
- Language: Python
- Stars: 96
- Topics: 
- Description: 1st Multilingual Benchmark for Repository-Level E2E Microservice Generation

## Extracted README / Docs / Examples



# FILE: README.md

# RepoGenesis: Benchmarking End-to-End Microservice Generation from Readme to Repository 🚀

[//]: # ([![Project]&#40;http://img.shields.io/badge/Project-SER-E3E4C8.svg&#41;]&#40;https://microsoft.github.io/DKI_LLM/ser/ser_index.html&#41;)

[![Paper](http://img.shields.io/badge/Paper-arxiv.2601.13943-99D4C8.svg)](https://arxiv.org/abs/2601.13943)
[![Website](http://img.shields.io/badge/Website-RepoGenesis-99D4C8.svg)](https://microsoft.github.io/DKI_LLM/RepoGenesis/RepoGenesis_index.html)
[![Leaderboard](https://img.shields.io/badge/Leaderboard-RepoGenesis-99D4C8.svg)](http://23.83.232.182:4090/)

## News 🔥
- April, 2026: our paper was accepted by *ACL 2026 (Main)* with a **Top 15%** of accepted papers.
- Feb, 2026: We released the [Leaderboard](http://23.83.232.182:4090/)! You can now check the latest evaluation results of different agents and IDEs.

This repository contains the code and data for RepoGenesis, the first multilingual benchmark for repository-level end-to-end web microservice generation. RepoGenesis assesses LLMs' capability in generating complete web microservice repositories from natural language requirements.

Refer to [the official github repo](https://github.com/microsoft/DKI_LLM/tree/main/RepoGenesis) for up-to-date information.


## Table of Contents

- [Overview](#overview)
- [Evaluation Metrics](#evaluation-metrics)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Evaluation Workflow](#evaluation-workflow)
  - [Step 1 — Generate Repositories](#step-1--generate-repositories)
  - [Step 2 — Docker-based Evaluation (Recommended)](#step-2--docker-based-evaluation-recommended)
  - [Step 3 — Legacy Script Evaluation](#step-3--legacy-script-evaluation)
  - [Step 4 — Aggregate and Reproduce Paper Results](#step-4--aggregate-and-reproduce-paper-results)
- [Development](#development)

## Overview ⭐

<div align="center">
  <img width="90%" src="docs/RepoGenesis.png">
</div>

RepoGenesis is the first benchmark for evaluating repository-level microservice generation from natural language requirements. Unlike existing benchmarks that focus on function-level or class-level code generation, RepoGenesis challenges LLMs to generate repositories from scratch.

**Key Features:**
- **11 frameworks** including Django, FastAPI, Javalin, Spring Boot, and more
- **18 application domains** covering authentication, content management, ***gaming***, file management, and more
- **Multi-dimensional metrics**: Pass@1 for functional correctness, API Coverage (AC) for implementation completeness, and Deployment Success Rate (DSR) for deployability
- **Docker-based isolated evaluation** via `eval_harness` — reproducible, hermetic, no conda required
- **Support for multiple agents**: MetaGPT <img src="docs/metagpt.png" height="16">, DeepCode <img src="docs/DeepCode.png" height="16">, Qwen-Agent <img src="docs/qwen-color.png" height="16">, MS-Agent <img src="docs/modelscope-color.png" height="16">, and commercial IDEs like Cursor <img src="docs/cursor.png" height="16"> and Copilot <img src="docs/githubcopilot.png" height="16">

## Installation

### Prerequisites

| Requirement | Version | Purpose |
|---|---|---|
| Python | 3.10+ | Orchestrator scripts |
| Docker | 20.10+ | Isolated evaluation (recommended) |
| Java JDK | 17+ | Java repo evaluation (legacy scripts) |
| Conda | Any | Isolated test envs (legacy scripts only) |
| Git | Any | Repository management |

### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Configure API Keys

```bash
export OPENAI_API_KEY="your-api-key"
export OPENAI_BASE_URL="your-base-url"   # optional, for custom endpoints
```

### Install Agent Frameworks (Optional)

Only needed if you want to run generation with a specific agent framework:

```bash
# MetaGPT
git clone https://github.com/FoundationAgents/MetaGPT.git && cd MetaGPT && pip install -e .

# DeepCode
git clone https://github.com/HKUDS/DeepCode.git && cd DeepCode && pip install -e .

# Qwen-Agent
git clone https://github.com/QwenLM/Qwen-Agent.git && cd Qwen-Agent && pip install -e .

# MS-Agent
git clone https://github.com/modelscope/ms-agent.git && cd ms-agent && pip install -e .
```

---

## Quick Start

The fastest path to evaluate a set of generated repos end-to-end:

```bash
# 1. Generate repos (example: MetaGPT on Blog)
python gen_and_eval.py \
    --agent metagpt \
    --repo_root ./my_generated_repos \
    --repo_name Blog \
    --llm_model gpt-4o \
    --llm_api_key $OPENAI_API_KEY

# 2. Evaluate with Docker harness (all 3 metrics, 30 verified repos)
python -m eval_harness.run_evaluation \
    --predictions_dir ./my_generated_repos \
    --output_dir ./eval_results

# 3. View the results
cat eval_results/report.json
```

---

## Evaluation Workflow

The evaluation pipeline consists of four stages. Stages 1–2 are the recommended path. Stage 3 (legacy scripts) is kept for reproducing earlier paper results.

```
┌─────────────────┐     ┌──────────────────────┐     ┌─────────────────────┐
│  1. Generation  │────▶│  2. Docker Harness   │────▶│  4. Report / Paper  │
│  (agent + LLM)  │     │  (DSR + Pass@1 + AC) │     │  Results            │
└─────────────────┘     └──────────────────────┘     └─────────────────────┘
                                   │
                          ┌────────┴────────┐
                          │  3. Legacy eval │
                          │  (optional)     │
                          └─────────────────┘
```

### Step 1 — Generate Repositories

#### For Python Repositories

```bash
# MetaGPT
python gen_and_eval.py \
    --agent metagpt \
    --repo_root repo \
    --repo_name <repository-name> \
    --llm_model gpt-4o \
    --llm_api_key $OPENAI_API_KEY
```

#### For Java Repositories (the same args with Python)

```bash
python gen_and_eval_Java.py \
    --agent <agent-name> \
    --repo_root repo_java \
    --repo_name <java-repository-name> \
    --llm_model gpt-4o \
    --llm_api_key $OPENAI_API_KEY
```
After generation, your `--repo_root` will contain one subdirectory per repo, each with the generated source code. This directory is then passed to the evaluation harness as `--predictions_dir`.

---

### Step 2 — Docker-based Evaluation (Recommended)

The `eval_harness` package provides a hermetic, Docker-based evaluation pipeline that computes all three metrics (DSR, Pass@1, AC) in a single command. Each repo is evaluated in its own container — no conda environments, no port conflicts, no dependency pollution between repos.

#### How it Works

```
predictions_dir/
└── <repo_name>/          ← agent-generated source code
    ├── start.sh
    ├── requirements.txt  (Python) or pom.xml (Java)
    └── ...

          │
          ▼ eval_harness
          
1. AC computed via static analysis (no Docker needed)
2. Docker image built:
   ├── Base image: python:3.10-slim or maven:3.9-eclipse-temurin-17
   ├── Generated repo copied in
   └── Golden oracle tests injected (overwrite any agent-generated tests)
3. Container runs entrypoint.sh:
   ├── Phase 1 — DSR: install deps → start server → health check
   │   └── Emits >>>>> DSR_START ... >>>>> DSR_END markers
   └── Phase 2 — Pass@1: run pytest (Python) or mvn test (Java)
       └── Emits >>>>> TEST_START ... >>>>> TEST_END markers
4. Container logs parsed → DSR + Pass@1 graded
5. Image removed; intermediate result saved for crash recovery
6. Final JSON report + summary table printed
```

#### Run the Full Evaluation

```bash
python -m eval_harness.run_evaluation \
    --predictions_dir ./generated \
    --output_dir ./eval_results
```

#### Common Options

| Flag | Default | Description |
|---|---|---|
| `--predictions_dir` | *(required)* | Directory of generated repos (one subdir per repo) |
| `--output_dir` | `eval_results/` | Where to write `report.json` and intermediate results |
| `--repo_names Blog flask` | all found | Evaluate only specific repos |
| `--lang python` | all | Filter to `python` or `java` repos only |
| `--skip_docker` | off | Compute AC only, skip Docker (no DSR/Pass@1) |
| `--resume` | off | Resume from a previously interrupted run |
| `--keep_images` | off | Do not remove Docker images after evaluation |
| `--no_cache` | off | Build Docker images with `--no-cache` |
| `--verbose` / `-v` | off | Stream container logs + DEBUG logging |
| `--log_file eval.log` | none | Also write logs to a file |
| `--model_name gpt-4o` | none | Record model name in report metadata |
| `--agent_name metagpt` | none | Record agent name in report metadata |
| `--cleanup` | — | Remove all eval containers/images and exit |
| `--timeout` | 900 | Per-container timeout in seconds |

#### Example: Evaluate a Single Repo with Verbose Output

```bash
python -m eval_harness.run_evaluation \
    --predictions_dir ./generated \
    --repo_names Blog \
    --output_dir ./eval_results \
    --verbose \
    --model_name gpt-4o \
    --agent_name metagpt
```

#### Example: AC-only Evaluation (No Docker Required)

```bash
python -m eval_harness.run_evaluation \
    --predictions_dir ./generated \
    --skip_docker \
    --output_dir ./eval_results
```

#### Example: Resume an Interrupted Run

Intermediate results are saved after each repo under `eval_results/intermediate/<repo_name>.json`. If the run crashes, resume it:

```bash
python -m eval_harness.run_evaluation \
    --predictions_dir ./generated \
    --output_dir ./eval_results \
    --resume
```

#### Output Format

The final report is written to `eval_results/report.json`:

```jsonc
{
  "metadata": {
    "timestamp": "2026-02-25T12:00:00",
    "harness_version": "1.0.0",
    "model_name": "gpt-4o",
    "agent_name": "metagpt",
    "total_elapsed_seconds": 1234.5,
    "predictions_dir": "./generated"
  },
  "summary": {
    "total_repos": 30,
    "python_repos": 22,
    "java_repos": 8,
    "avg_pass_at_1": 0.4123,
    "avg_api_coverage": 0.7654,
    "deployment_success_rate": 0.6000,
    "pass_at_1_by_lang": { "python": 0.4500, "java": 0.3200 },
    "ac_by_lang":        
