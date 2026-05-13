# Missing Repo Summary Source: Significant-Gravitas/AutoGPT

- URL: https://github.com/Significant-Gravitas/AutoGPT
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT
- Clone Status: cloned
- Language: Python
- Stars: 184250
- Topics: agentic-ai, agents, ai, artificial-intelligence, autonomous-agents, claude, gpt, llama-api, llm, openai, python
- Description: AutoGPT is the vision of accessible AI for everyone, to use and to build on. Our mission is to provide the tools, so that you can focus on what matters.

## Extracted README / Docs / Examples



# FILE: README.md

# AutoGPT: Build, Deploy, and Run AI Agents

[![Discord Follow](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fdiscord.com%2Fapi%2Finvites%2Fautogpt%3Fwith_counts%3Dtrue&query=%24.approximate_member_count&label=total%20members&logo=discord&logoColor=white&color=7289da)](https://discord.gg/autogpt) &ensp;
[![Twitter Follow](https://img.shields.io/twitter/follow/Auto_GPT?style=social)](https://twitter.com/Auto_GPT) &ensp;

<!-- Keep these links. Translations will automatically update with the README. -->
[Deutsch](https://zdoc.app/de/Significant-Gravitas/AutoGPT) | 
[Español](https://zdoc.app/es/Significant-Gravitas/AutoGPT) | 
[français](https://zdoc.app/fr/Significant-Gravitas/AutoGPT) | 
[日本語](https://zdoc.app/ja/Significant-Gravitas/AutoGPT) | 
[한국어](https://zdoc.app/ko/Significant-Gravitas/AutoGPT) | 
[Português](https://zdoc.app/pt/Significant-Gravitas/AutoGPT) | 
[Русский](https://zdoc.app/ru/Significant-Gravitas/AutoGPT) | 
[中文](https://zdoc.app/zh/Significant-Gravitas/AutoGPT)

**AutoGPT** is a powerful platform that allows you to create, deploy, and manage continuous AI agents that automate complex workflows. 

## Hosting Options 
   - Download to self-host (Free!)
   - [Join the Waitlist](https://bit.ly/3ZDijAI) for the cloud-hosted beta (Closed Beta - Public release Coming Soon!)

## How to Self-Host the AutoGPT Platform
> [!NOTE]
> Setting up and hosting the AutoGPT Platform yourself is a technical process. 
> If you'd rather something that just works, we recommend [joining the waitlist](https://bit.ly/3ZDijAI) for the cloud-hosted beta.

### System Requirements

Before proceeding with the installation, ensure your system meets the following requirements:

#### Hardware Requirements
- CPU: 4+ cores recommended
- RAM: Minimum 8GB, 16GB recommended
- Storage: At least 10GB of free space

#### Software Requirements
- Operating Systems:
  - Linux (Ubuntu 20.04 or newer recommended)
  - macOS (10.15 or newer)
  - Windows 10/11 with WSL2
- Required Software (with minimum versions):
  - Docker Engine (20.10.0 or newer)
  - Docker Compose (2.0.0 or newer)
  - Git (2.30 or newer)
  - Node.js (16.x or newer)
  - npm (8.x or newer)
  - VSCode (1.60 or newer) or any modern code editor

#### Network Requirements
- Stable internet connection
- Access to required ports (will be configured in Docker)
- Ability to make outbound HTTPS connections

### Updated Setup Instructions:
We've moved to a fully maintained and regularly updated documentation site.

👉 [Follow the official self-hosting guide here](https://agpt.co/docs/platform/getting-started/getting-started)


This tutorial assumes you have Docker, VSCode, git and npm installed.

---

#### ⚡ Quick Setup with One-Line Script (Recommended for Local Hosting)

Skip the manual steps and get started in minutes using our automatic setup script.

For macOS/Linux:
```
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
```

For Windows (PowerShell):
```
powershell -c "iwr https://setup.agpt.co/install.bat -o install.bat; ./install.bat"
```

This will install dependencies, configure Docker, and launch your local instance — all in one go.

### 🧱 AutoGPT Frontend

The AutoGPT frontend is where users interact with our powerful AI automation platform. It offers multiple ways to engage with and leverage our AI agents. This is the interface where you'll bring your AI automation ideas to life:

   **Agent Builder:** For those who want to customize, our intuitive, low-code interface allows you to design and configure your own AI agents. 
   
   **Workflow Management:** Build, modify, and optimize your automation workflows with ease. You build your agent by connecting blocks, where each block performs a single action.
   
   **Deployment Controls:** Manage the lifecycle of your agents, from testing to production.
   
   **Ready-to-Use Agents:** Don't want to build? Simply select from our library of pre-configured agents and put them to work immediately.
   
   **Agent Interaction:** Whether you've built your own or are using pre-configured agents, easily run and interact with them through our user-friendly interface.

   **Monitoring and Analytics:** Keep track of your agents' performance and gain insights to continually improve your automation processes.

[Read this guide](https://docs.agpt.co/platform/new_blocks/) to learn how to build your own custom blocks.

### 💽 AutoGPT Server

The AutoGPT Server is the powerhouse of our platform This is where your agents run. Once deployed, agents can be triggered by external sources and can operate continuously. It contains all the essential components that make AutoGPT run smoothly.

   **Source Code:** The core logic that drives our agents and automation processes.
   
   **Infrastructure:** Robust systems that ensure reliable and scalable performance.
   
   **Marketplace:** A comprehensive marketplace where you can find and deploy a wide range of pre-built agents.

### 🐙 Example Agents

Here are two examples of what you can do with AutoGPT:

1. **Generate Viral Videos from Trending Topics**
   - This agent reads topics on Reddit.
   - It identifies trending topics.
   - It then automatically creates a short-form video based on the content. 

2. **Identify Top Quotes from Videos for Social Media**
   - This agent subscribes to your YouTube channel.
   - When you post a new video, it transcribes it.
   - It uses AI to identify the most impactful quotes to generate a summary.
   - Then, it writes a post to automatically publish to your social media. 

These examples show just a glimpse of what you can achieve with AutoGPT! You can create customized workflows to build agents for any use case.

---

### **License Overview:**

🛡️ **Polyform Shield License:**
All code and content within the `autogpt_platform` folder is licensed under the Polyform Shield License. This new project is our in-developlemt platform for building, deploying and managing agents.</br>_[Read more about this effort](https://agpt.co/blog/introducing-the-autogpt-platform)_

🦉 **MIT License:**
All other portions of the AutoGPT repository (i.e., everything outside the `autogpt_platform` folder) are licensed under the MIT License. This includes the original stand-alone AutoGPT Agent, along with projects such as [Forge](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/forge), [agbenchmark](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/benchmark) and the [AutoGPT Classic GUI](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/frontend).</br>We also publish additional work under the MIT Licence in other repositories, such as [GravitasML](https://github.com/Significant-Gravitas/gravitasml) which is developed for and used in the AutoGPT Platform. See also our MIT Licenced [Code Ability](https://github.com/Significant-Gravitas/AutoGPT-Code-Ability) project.

---
### Mission
Our mission is to provide the tools, so that you can focus on what matters:

- 🏗️ **Building** - Lay the foundation for something amazing.
- 🧪 **Testing** - Fine-tune your agent to perfection.
- 🤝 **Delegating** - Let AI work for you, and have your ideas come to life.

Be part of the revolution! **AutoGPT** is here to stay, at the forefront of AI innovation.

**📖 [Documentation](https://docs.agpt.co)**
&ensp;|&ensp;
**🚀 [Contributing](CONTRIBUTING.md)**

---
## 🤖 AutoGPT Classic
> Below is information about the classic version of AutoGPT.

**🛠️ [Build your own Agent - Quickstart](classic/FORGE-QUICKSTART.md)**

### 🏗️ Forge

**Forge your own agent!** &ndash; Forge is a ready-to-go toolkit to build your own agent application. It handles most of the boilerplate code, letting you channel all your creativity into the things that set *your* agent apart. All tutorials are located [here](https://medium.com/@aiedge/autogpt-forge-e3de53cc58ec). Components from [`forge`](/classic/forge/) can also be used individually to speed up development and reduce boilerplate in your agent project.

🚀 [**Getting Started with Forge**](https://github.com/Significant-Gravitas/AutoGPT/blob/master/classic/forge/tutorials/001_getting_started.md) &ndash;
This guide will walk you through the process of creating your own agent and using the benchmark and user interface.

📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/forge) about Forge

### 🎯 Benchmark

**Measure your agent's performance!** The `agbenchmark` can be used with any agent that supports the agent protocol, and the integration with the project's [CLI] makes it even easier to use with AutoGPT and forge-based agents. The benchmark offers a stringent testing environment. Our framework allows for autonomous, objective performance evaluations, ensuring your agents are primed for real-world action.

<!-- TODO: insert visual demonstrating the benchmark -->

📦 [`agbenchmark`](https://pypi.org/project/agbenchmark/) on Pypi
&ensp;|&ensp;
📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/benchmark) about the Benchmark

### 💻 UI

**Makes agents easy to use!** The `frontend` gives you a user-friendly interface to control and monitor your agents. It connects to agents through the [agent protocol](#-agent-protocol), ensuring compatibility with many agents from both inside and outside of our ecosystem.

<!-- TODO: insert screenshot of front end -->

The frontend works out-of-the-box with all agents in the repo. Just use the [CLI] to run your agent of choice!

📘 [Learn More](https://github.com/Significant-Gravitas/AutoGPT/tree/master/classic/frontend) about the Frontend

### ⌨️ CLI

[CLI]: #-cli

To make it as easy as possible to use all of the tools offered by the repository, a CLI is included at the root of the repo:

```shell
$ ./run
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  agent      Commands to create, start and stop agents
  benchmark  Commands to start the benchmark an

# FILE: docs/AGENTS.md

# Documentation Guidelines

## Block Documentation Manual Sections

When updating manual sections (`<!-- MANUAL: ... -->`) in block documentation files (e.g., `docs/integrations/basic.md`), follow these formats:

### How It Works Section

Provide a technical explanation of how the block functions:
- Describe the processing logic in 1-2 paragraphs
- Mention any validation, error handling, or edge cases
- Use code examples with backticks when helpful (e.g., `[[1, 2], [3, 4]]` becomes `[1, 2, 3, 4]`)

Example:
```markdown
<!-- MANUAL: how_it_works -->
The block iterates through each list in the input and extends a result list with all elements from each one. It processes lists in order, so `[[1, 2], [3, 4]]` becomes `[1, 2, 3, 4]`.

The block includes validation to ensure each item is actually a list. If a non-list value is encountered, the block outputs an error message instead of proceeding.
<!-- END MANUAL -->
```

### Use Case Section

Provide 3 practical use cases in this format:
- **Bold Heading**: Short one-sentence description

Example:
```markdown
<!-- MANUAL: use_case -->
**Paginated API Merging**: Combine results from multiple API pages into a single list for batch processing or display.

**Parallel Task Aggregation**: Merge outputs from parallel workflow branches that each produce a list of results.

**Multi-Source Data Collection**: Combine data collected from different sources (like multiple RSS feeds or API endpoints) into one unified list.
<!-- END MANUAL -->
```

### Style Guidelines

- Keep descriptions concise and action-oriented
- Focus on practical, real-world scenarios
- Use consistent terminology with other blocks
- Avoid overly technical jargon unless necessary


# FILE: docs/CLAUDE.md

@AGENTS.md


# FILE: docs/home/SUMMARY.md

# Table of contents

* [Developer Platform](README.md)


# FILE: docs/home/README.md

---
description: Welcome to your team’s developer platform
cover: .gitbook/assets/Banner_image.png
coverY: 56.53835084561286
layout:
  width: wide
  cover:
    visible: true
    size: full
  title:
    visible: false
  description:
    visible: false
  tableOfContents:
    visible: false
  outline:
    visible: false
  pagination:
    visible: false
  metadata:
    visible: true
---

# Developer Platform

<h2 align="center">AutoGPT Documentation</h2>

<p align="center">Create innovative agents that amplify human potential</p>



<table data-view="cards"><thead><tr><th></th><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th><th data-hidden data-card-cover data-type="image">Cover image</th></tr></thead><tbody><tr><td><h4><i class="fa-leaf">:leaf:</i></h4></td><td><strong>AutoGPT Platform</strong></td><td>Get started with the developer platform in 5 minutes.</td><td><a href="https://app.gitbook.com/o/ouZP6hgdu8LtbWil2Hvb/s/iMDOYkb9SC1mijdHzvKF/">AutoGPT Platform</a></td><td><a href=".gitbook/assets/AGPT_Platform.png">AGPT_Platform.png</a></td></tr><tr><td><h4><i class="fa-server">:server:</i></h4></td><td><strong>Integrations</strong></td><td>Learn more about hosting the developer platform.</td><td><a href="https://app.gitbook.com/o/ouZP6hgdu8LtbWil2Hvb/s/InwWrtMw9tc0NCzvPVK4/">Integrations</a></td><td><a href=".gitbook/assets/Integrations.png">Integrations.png</a></td></tr><tr><td><h4><i class="fa-terminal">:terminal:</i></h4></td><td><strong>Contribute</strong></td><td>Browse, test, and implement APIs.</td><td><a href="https://app.gitbook.com/s/x9A8W5T9IXYWENaFbHqO/">Contributing to the Docs</a></td><td><a href=".gitbook/assets/Contribute.png">Contribute.png</a></td></tr></tbody></table>

{% columns %}
{% column valign="middle" %}
<p align="center"><a href="https://github.com/Significant-Gravitas/AutoGPT/blob/master/LICENSE">AutoGPT License on GitHub</a></p>
{% endcolumn %}

{% column %}
<p align="center"><a href="https://app.gitbook.com/s/dDGesk9atyMLUMMo4QuI/autogpt-classic/introduction">AutoGPT Classic (Local Installation)</a></p>
{% endcolumn %}
{% endcolumns %}

***



<h2 align="center">Join a community of 65,000+ developers</h2>

<p align="center">Join our Discord community or create your first PR in just a few steps.</p>

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th><th></th><th data-hidden data-card-cover data-type="files"></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><h4><i class="fa-discord">:discord:</i></h4></td><td><strong>Discord community</strong></td><td>Join our Discord community to post questions, get help, and share resources with our growing community of over 55,000 members.</td><td><a href="https://www.gitbook.com/" class="button secondary">Join Discord</a></td><td></td><td><a href="https://discord.com/invite/autogpt">https://discord.com/invite/autogpt</a></td></tr><tr><td><h4><i class="fa-github">:github:</i></h4></td><td><strong>GitHub</strong></td><td>Our product is 100% open source and built by developers just like you. Head to our GitHub repository to learn how to submit your first PR.</td><td><a href="https://www.gitbook.com/" class="button secondary">Submit a PR</a></td><td></td><td><a href="https://github.com/Significant-Gravitas/AutoGPT">https://github.com/Significant-Gravitas/AutoGPT</a></td></tr></tbody></table>


# FILE: docs/platform/submit-agent-to-marketplace.md

# **How to Submit an Agent to the AutoGPT Marketplace**

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/o42HPN7SihU?si=lGeNFN-xIDSFqaQN" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

## **Prerequisites**
* A completed agent built using the AutoGPT Builder
* Your agent must be saved before submission

## **Submission Steps**
1. **Access the Submission Form**
    * Navigate to the marketplace
    * Click the "Submit Agent" button
2. **Select Your Agent**
    * Use the dropdown menu to select your completed agent
3. **Fill Out Required Information**
    * Add a detailed description of your agent
    * Enter the author name
    * Add at least one keyword to help users find your agent
    * Select the most relevant category for your agent
4. **Review Terms**
    * Read and agree to the marketplace terms
5. **Submit for Review**
    * Click the "Submit" button to complete your submission

## **After Submission**
* Your agent will enter a "pending" state
* The AutoGPT team will review your submission
* If approved, your agent will appear in the marketplace as a new listing


## **Tips for a Successful Submission**
* Provide a clear, detailed description of what your agent does
* Choose relevant keywords that accurately describe your agent's functionality
* Ensure your agent is fully tested and working as intended before submission
* Select the most appropriate category to help users find your agent

# FILE: docs/platform/agent-blocks.md

# **How to Create an AI Agent as a Block in AutoGPT**

## **Overview**

This guide explains how to create a reusable agent block that can be used as a component in other agents.

<center><iframe width="560" height="315" src="https://www.youtube.com/embed/G5t5wbfomNE?si=dek4KKAPmx8DVOxm" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center>

## **What Are Agent Blocks?**

Agent blocks are pre-configured, reusable AI workflows that can be used as components within larger automation systems. Think of them as "smart building blocks" - each agent block is itself a complete workflow that can:

- Accept specific inputs
- Process data using AI and traditional automation
- Produce defined outputs
- Be easily reused in different contexts

The power of agent blocks lies in their modularity. Once you create an agent with a specific capability (like translating text or analyzing sentiment), you can reuse it as a single block in other workflows. This means you can:

- Combine multiple agent blocks to create more complex automations
- Reuse proven workflows without rebuilding them
- Share agent blocks with other users
- Create hierarchical systems where specialized agents work together

For example, a content creation workflow might combine several agent blocks:

- A research agent block that gathers information
- A writing agent block that creates the initial draft
- An editing agent block that polishes the content
- A formatting agent block that prepares the final output

## **Creating the Base Agent**

### **Required Components**

1. Input Block
2. AI Text Generator Block
3. Output Block

### **Step-by-Step Setup**

1. **Add and Configure Blocks**
    * Add an Input Block
    * Add an AI Text Generator Block
    * Add an Output Block
2. **Connect Components**
    * Connect Input's result to AI Text Generator's Prompt
    * Connect AI Text Generator's response to Output's value
3. **Name the Components**
    * Name the Input Block: "question"
    * Name the Output Block: "answer"
4. **Save the Agent**
    * Choose a descriptive name (e.g., "Weather Agent")
    * Click Save



## **Converting to a Block**

1. **Access the Block Menu**
    * Go to the Builder interface
    * Click the Blocks menu
    * Click the agent tag or search the name of your agent
2. **Using the Agent Block**
    * Click on the agent block to add to your workflow
    * Save the new agent with a descriptive name (e.g., "Weather Agent")

## **Testing the Agent Block**

1. **Run the Agent**
    * Enter a test question (e.g., "How far is the Earth from the Moon?")
    * Click Run
2. **View Results**
    * Option 1: Check "Agent Outputs" section*
    * Option 2: Click "View More" for detailed results

*Note: if there is no output block then the "Agent Outputs" button will show up blank. You can see the output under view more or at bottom of the block.

## **Advanced Usage**

* You can make more complex agents by combining multiple agent blocks
* Chain different agents together for more sophisticated workflows

## **Note**

This is a basic example that can be expanded upon to create more complex agent blocks with additional functionality.

# FILE: docs/platform/installer.md

# AutoGPT Platform Installer

The AutoGPT Platform provides easy-to-use installers to help you quickly set up the platform on your system. This page covers how to use the installer scripts for both Linux/macOS and Windows.

## What the Installer Does

The installer scripts will:

1. Check for required prerequisites (Git, Docker, npm)
2. Clone the AutoGPT repository
3. Set up the backend services using Docker
4. Set up the frontend application
5. Start both the backend and frontend services

## Prerequisites

Before running the installer, make sure you have the following installed:

- **Git**: For cloning the repository
- **Docker**: For running the backend services
- **Node.js and npm**: For the frontend application

## Quick One-Liner Installation

For convenience, you can use the following one-liner commands to install AutoGPT Platform:

### Linux/macOS

```bash
curl -fsSL https://setup.agpt.co/install.sh -o install.sh && bash install.sh
```

### Windows

```powershell
powershell -c "iwr https://setup.agpt.co/install.bat -o install.bat; ./install.bat"
```

## Manual Installation

If you prefer, you can manually download and run the installer scripts:

- **Linux/macOS:** `setup-autogpt.sh`
- **Windows:** `setup-autogpt.bat`

These scripts are located in the `autogpt_platform/installer/` directory.

## After Installation

Once the installation is complete:
- The backend services will be running in Docker containers
- The frontend application will be available at http://localhost:3000

## Stopping the Services

To stop the services, press Ctrl+C in the terminal where the frontend is running, then run:

```bash
cd AutoGPT/autogpt_platform
docker compose down
```

## Troubleshooting

If you encounter any issues during installation:

1. Make sure all prerequisites are correctly installed
2. Check that Docker is running
3. Ensure you have a stable internet connection
4. Verify you have sufficient permissions to create directories and run Docker 

# FILE: docs/platform/advanced_setup.md

# Advanced Setup

The advanced steps below are intended for people with sysadmin experience. If you are not comfortable with these steps, please refer to the [basic setup guide](../platform/getting-started.md).

## Introduction

For the advanced setup, first follow the [basic setup guide](../platform/getting-started.md) to get the server up and running. Once you have the server running, you can follow the steps below to configure the server for your specific needs.

## Configuration

### Setting config via environment variables

The server uses environment variables to store configs. You can set these environment variables in a `.env` file in the root of the project. The `.env` file should look like this:

```bash
# .env
KEY1=value1
KEY2=value2
```

The server will automatically load the `.env` file when it starts. You can also set the environment variables directly in your shell. Refer to your operating system's documentation on how to set environment variables in the current session.

The valid options are listed in `.env.default` in the root of the builder and server directories. You can copy the `.env.default` file to `.env` and modify the values as needed.

```bash
# Copy the .env.default file to .env
cp .env.default .env
```

### Secrets directory

The secret directory is located at `./secrets`. You can store any secrets you need in this directory. The server will automatically load the secrets when it starts.

An example for a secret called `my_secret` would look like this:

```bash
# ./secrets/my_secret
my_secret_value
```

This is useful when running on docker so you can copy the secrets into the container without exposing them in the Dockerfile.

## Database selection


### PostgreSQL

We use a Supabase PostgreSQL as the database. You will swap the commands you use to generate and run prisma to the following

```bash
poetry run prisma generate --schema postgres/schema.prisma
```

This will generate the Prisma client for PostgreSQL. You will also need to run the PostgreSQL database in a separate container. You can use the `docker-compose.yml` file in the `rnd` directory to run the PostgreSQL database.

```bash
cd autogpt_platform/
docker compose up -d --build
```

You can then run the migrations from the `backend` directory.

```bash
cd ../backend
prisma migrate dev --schema postgres/schema.prisma
```

## AutoGPT Agent Server Advanced set up

This guide walks you through a dockerized set up, with an external DB (postgres)

### Setup

We use the Poetry to manage the dependencies. To set up the project, follow these steps inside this directory:

0. Install Poetry
    ```sh
    pip install poetry
    ```
    
1. Configure Poetry to use .venv in your project directory
    ```sh
    poetry config virtualenvs.in-project true
    ```

2. Enter the poetry shell

   ```sh
   poetry shell
   ```

3. Install dependencies

   ```sh
   poetry install
   ```

4. Copy .env.default to .env

   ```sh
   cp .env.default .env
   ```

5. Generate the Prisma client

   ```sh
   poetry run prisma generate
   ```

   > In case Prisma generates the client for the global Python installation instead of the virtual environment, the current mitigation is to just uninstall the global Prisma package:
   >
   > ```sh
   > pip uninstall prisma
   > ```
   >
   > Then run the generation again. The path _should_ look something like this:  
   > `<some path>/pypoetry/virtualenvs/backend-TQIRSwR6-py3.12/bin/prisma`

6. Run the postgres database from the /rnd folder

   ```sh
   cd autogpt_platform/
   docker compose up -d
   ```

7. Run the migrations (from the backend folder)

   ```sh
   cd ../backend
   prisma migrate deploy
   ```

### Running The Server

#### Starting the server directly

Run the following command:

```sh
poetry run app
```


# FILE: docs/platform/d_id.md

# Find available voices for D-ID

1. **ElevenLabs**
   - Select any voice from the voice list: https://api.elevenlabs.io/v1/voices
   - Copy the voice_id
   - Use it as a string in the voice_id field in the CreateTalkingAvatarClip Block

2. **Microsoft Azure Voices**
    - Select any voice from the voice gallery: https://speech.microsoft.com/portal/voicegallery
    - Click on the "Sample code" tab on the right
    - Copy the voice name, for example: config.SpeechSynthesisVoiceName ="en-GB-AbbiNeural"
    - Use this string en-GB-AbbiNeural in the voice_id field in the CreateTalkingAvatarClip Block

3. **Amazon Polly Voices**
    - Select any voice from the voice list: https://docs.aws.amazon.com/polly/latest/dg/available-voices.html
    - Copy the voice name / ID
    - Use it as string in the voice_id field in the CreateTalkingAvatarClip Block

# FILE: docs/platform/SUMMARY.md

# Table of contents

* [What is the AutoGPT Platform?](what-is-autogpt-platform.md)

## Getting Started

* [Setting Up Auto-GPT (Local Host)](getting-started.md)
* [AutoGPT Platform Installer](installer.md)
* [Edit an Agent](edit-agent.md)
* [Delete an Agent](delete-agent.md)
* [Download & Import an Agent](download-agent-from-marketplace-local.md)
* [Create a Basic Agent](create-basic-agent.md)
* [Submit an Agent to the Marketplace](submit-agent-to-marketplace.md)

## Advanced Setup

* [Advanced Setup](advanced_setup.md)

## Building Blocks

* [Agent Blocks Overview](agent-blocks.md)
* [Build your own Blocks](new_blocks.md)
* [Block SDK Guide](block-sdk-guide.md)

## Using AI Services

* [Using Google Gemini](gemini.md)
* [Using Ollama](ollama.md)
* [Using AI/ML API](aimlapi.md)
* [Using D-ID](d_id.md)

## API & Integrations

* [API Introduction](integrating/api-guide.md)
* [OAuth & SSO](integrating/oauth-guide.md)


# FILE: docs/platform/block-sdk-guide.md

# Block Creation with SDK

This guide explains how to create new blocks for the AutoGPT Platform using the SDK pattern with advanced features.

## Overview

Blocks are reusable components that perform specific tasks in AutoGPT workflows. They can integrate with external services, process data, or perform any programmatic operation.

## Basic Structure

### 1. Create Provider Configuration

First, create a `_config.py` file to configure your provider using the `ProviderBuilder`:

!!! note "Simple API key provider"
    ```python
    from backend.sdk import BlockCostType, ProviderBuilder

    my_provider = (
        ProviderBuilder("my_provider")
        .with_api_key("MY_PROVIDER_API_KEY", "My Provider API Key")
        .with_base_cost(1, BlockCostType.RUN)
        .build()
    )
    ```

For OAuth providers:

!!! note "OAuth provider configuration"
    ```python
    from backend.sdk import BlockCostType, ProviderBuilder
    from ._oauth import MyProviderOAuthHandler

    my_provider = (
        ProviderBuilder("my_provider")
        .with_oauth(
            MyProviderOAuthHandler,
            scopes=["read", "write"],
            client_id_env_var="MY_PROVIDER_CLIENT_ID",
            client_secret_env_var="MY_PROVIDER_CLIENT_SECRET",
        )
        .with_base_cost(1, BlockCostType.RUN)
        .build()
    )
    ```

### 2. Create the Block Class

Create your block file (e.g., `my_block.py`):

```python
import uuid
from backend.sdk import (
    APIKeyCredentials,
    Block,
    BlockCategory,
    BlockOutput,
    BlockSchema,
    BlockSchemaInput,
    BlockSchemaOutput,
    CredentialsMetaInput,
    SchemaField,
)
from ._config import my_provider


class MyBlock(Block):
    class Input(BlockSchemaInput):
        credentials: CredentialsMetaInput = my_provider.credentials_field(
            description="API credentials for My Provider"
        )
        query: str = SchemaField(description="The query to process")
        limit: int = SchemaField(
            description="Number of results",
            default=10,
            ge=1,
            le=100,
        )
        advanced_option: str = SchemaField(
            description="Advanced setting",
            default="",
            advanced=True,
        )

    class Output(BlockSchemaOutput):
        results: list = SchemaField(description="List of results")
        count: int = SchemaField(description="Total count")

    def __init__(self):
        super().__init__(
            id=str(uuid.uuid4()),
            description="Brief description of what this block does",
            categories={BlockCategory.SEARCH},
            input_schema=self.Input,
            output_schema=self.Output,
        )

    async def run(
        self,
        input_data: Input,
        *,
        credentials: APIKeyCredentials,
        **kwargs
    ) -> BlockOutput:
        try:
            results = await self.process_data(
                input_data.query,
                input_data.limit,
                credentials
            )

            yield "results", results
            yield "count", len(results)

        except Exception as e:
            yield "error", str(e)

    async def process_data(self, query, limit, credentials):
        pass
```

!!! note "Input Schema Fields"
    - **`credentials`**: Use `my_provider.credentials_field()` to add provider authentication
    - **`query`**: Simple string field with description
    - **`limit`**: Integer field with validation constraints (`ge=1`, `le=100`)
    - **`advanced_option`**: Marked with `advanced=True` to hide from basic UI

!!! note "Output Schema Fields"
    - **`results`**: List of results from the block
    - **`count`**: Total count of results
    - The `error` output pin is already defined on `BlockSchemaOutput`

!!! note "Block Initialization"
    - **`id`**: Generate a unique ID using `uuid.uuid4()`
    - **`description`**: Brief description of what the block does
    - **`categories`**: Choose from `BlockCategory` enum (e.g., SEARCH, AI, PRODUCTIVITY)
    - **`input_schema` / `output_schema`**: Assign the Input and Output classes

!!! note "Run Method"
    - Implement your block logic in `process_data()` helper method
    - Use `credentials.api_key.get_secret_value()` to access the API key
    - Use `yield` to output results

## Key Components Explained

### Provider Configuration

The `ProviderBuilder` allows you to:
- **`.with_api_key()`**: Add API key authentication
- **`.with_oauth()`**: Add OAuth authentication
- **`.with_base_cost()`**: Set resource costs for the block
- **`.with_webhook_manager()`**: Add webhook support
- **`.with_user_password()`**: Add username/password auth

### Block Schema

- **Input/Output classes**: Define the data structure using `BlockSchema`
- **SchemaField**: Define individual fields with validation
- **CredentialsMetaInput**: Special field for handling credentials

### Block Implementation

1. **Unique ID**: Generate using `uuid.uuid4()`
2. **Categories**: Choose from `BlockCategory` enum (e.g., SEARCH, AI, PRODUCTIVITY)
3. **async run()**: Main execution method that yields outputs
4. **Error handling**: Error output pin is already defined on BlockSchemaOutput

## Advanced Features

### Testing

Add test configuration to your block:

!!! note "Test Configuration"
    ```python
    def __init__(self):
        super().__init__(
            # ... other config ...
            test_input={
                "query": "test query",
                "limit": 5,
                "credentials": {
                    "provider": "my_provider",
                    "id": str(uuid.uuid4()),
                    "type": "api_key"
                }
            },
            test_output=[
                ("results", ["result1", "result2"]),
                ("count", 2)
            ],
            test_mock={
                "process_data": lambda *args, **kwargs: ["result1", "result2"]
            }
        )
    ```

### OAuth Support

Create an OAuth handler in `_oaut

# FILE: docs/platform/ollama.md

# Running Ollama with AutoGPT

> **Important**: Ollama integration is only available when self-hosting the AutoGPT platform. It cannot be used with the cloud-hosted version.

Follow these steps to set up and run Ollama with the AutoGPT platform.

## Prerequisites

1. Make sure you have gone through and completed the [AutoGPT Setup](/platform/getting-started) steps, if not please do so before continuing with this guide.
2. Before starting, ensure you have [Ollama installed](https://ollama.com/download) on your machine.

## Setup Steps

### 1. Launch Ollama

To properly set up Ollama for network access, choose one of these methods:

**Method A: Using Ollama Desktop App (Recommended)**

1. Open the Ollama desktop application
2. Go to **Settings** and toggle **"Expose Ollama to the network"**
   ![Expose Ollama to Network](../imgs/ollama/Ollama-Expose-Network.png)
3. Click on the model name field in the "New Chat" window
4. Search for "llama3.2" (or your preferred model)
   ![Select llama3.2 model](../imgs/ollama/Ollama-Select-llama3.2.png)
5. Click on it to start the download and load the model to be used

??? note "Method B: Using Docker (Alternative)"

    If you prefer to run Ollama via Docker instead of the desktop app, you can use the official [Ollama Docker image](https://hub.docker.com/r/ollama/ollama):

    1. **Start Ollama container** (choose based on your hardware):

       **CPU only:**
       ```bash
       docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
       ```

       **With NVIDIA GPU** (requires [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)):
       ```bash
       docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
       ```

       **With AMD GPU:**
       ```bash
       docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm
       ```

       **Download your desired model:**
       ```bash
       docker exec -it ollama ollama run llama3.2
       ```

    !!! note
        The Docker method automatically exposes Ollama on `0.0.0.0:11434`, making it accessible to AutoGPT. More models can be found on the [Ollama library](https://ollama.com/library).

??? warning "Method C: Using Ollama Via Command Line (Legacy)"

    For users still using the traditional CLI approach or older Ollama installations:

    1. **Set the host environment variable:**

       **Windows (Command Prompt):**
       ```cmd
       set OLLAMA_HOST=0.0.0.0:11434
       ```
       
       **Linux/macOS (Terminal):**
       ```bash
       export OLLAMA_HOST=0.0.0.0:11434
       ```

    2. **Start the Ollama server:**
       ```bash
       ollama serve
       ```

    3. **Open a new terminal/command window** and download your desired model:
       ```bash
       ollama pull llama3.2
       ```

    !!! note
        This will download the [llama3.2](https://ollama.com/library/llama3.2) model. Keep the terminal with `ollama serve` running in the background throughout your session.

### 2. Start the AutoGPT Platform

Navigate to the autogpt_platform directory and start all services:

```bash
cd autogpt_platform
docker compose up -d --build
```

This command starts both the backend and frontend services. Once running, visit [http://localhost:3000](http://localhost:3000) to access the platform. After registering/logging in, navigate to the build page at [http://localhost:3000/build](http://localhost:3000/build).

### 3. Using Ollama with AutoGPT

Now that both Ollama and the AutoGPT platform are running, we can use Ollama with AutoGPT:

1. Add an AI Text Generator block to your workspace (it can work with any AI LLM block but for this example will be using the AI Text Generator block):
   ![Add AI Text Generator Block](../imgs/ollama/Select-AI-block.png)

2. **Configure the API Key field**: Enter any value (e.g., "dummy" or "not-needed") since Ollama doesn't require authentication.

3. In the "LLM Model" dropdown, select "llama3.2" (This is the model we downloaded earlier)
   ![Select Ollama Model](../imgs/ollama/Ollama-Select-Llama32.png)

   > **Compatible Models**: The following Ollama models are available in AutoGPT by default:
   > - `llama3.2` (Recommended for most use cases)
   > - `llama3` 
   > - `llama3.1:405b`
   > - `dolphin-mistral:latest`
   > 
   > **Note**: To use other models, follow the "Add Custom Models" step above.

4. **Set your local IP address** in the "Ollama Host" field:

   **To find your local IP address:**

   **Windows (Command Prompt):**
   ```cmd
   ipconfig
   ```

   **Linux/macOS (Terminal):**
   ```bash
   ip addr show
   ```
   or
   ```bash
   ifconfig
   ```

   Look for your IPv4 address (e.g., `192.168.0.39`), then enter it with port `11434` in the "Ollama Host" field:
   ```
   192.168.0.39:11434
   ```

   ![Ollama Remote Host](../imgs/ollama/Ollama-Remote-Host.png)

   > **Important**: Since AutoGPT runs in Docker containers, you must use your host machine's IP address instead of `localhost` or `127.0.0.1`. Docker containers cannot reach `localhost` on the host machine.

5. Add prompts to your AI block, save the graph, and run it:
   ![Add Prompt](../imgs/ollama/Ollama-Add-Prompts.png)

That's it! You've successfully setup the AutoGPT platform and made a LLM call to Ollama.
![Ollama Output](../imgs/ollama/Ollama-Output.png)

### Using Ollama on a Remote Server with AutoGPT

For running Ollama on a remote server, simply make sure the Ollama server is running and is accessible from other devices on your network/remotely through the port 11434. 

**To find your local IP address of the system running Ollama:**

**Windows (Command Prompt):**
```cmd
ipconfig
```

**Linux/macOS (Terminal):**
```bash
ip addr show
```
or
```bash
ifconfig
```

Look for your IPv4 address (e.g., `192.168.0.39`).

Then you can use the same steps above but you need to add the Ollama ser
