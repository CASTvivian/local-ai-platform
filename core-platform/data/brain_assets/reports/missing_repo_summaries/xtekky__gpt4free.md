# Missing Repo Summary Source: xtekky/gpt4free

- URL: https://github.com/xtekky/gpt4free
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/xtekky__gpt4free
- Clone Status: cloned
- Language: Python
- Stars: 66212
- Topics: chatbot, chatbots, chatgpt, chatgpt-4, chatgpt-api, chatgpt-free, chatgpt4, deepseek, deepseek-api, deepseek-r1, gpt, gpt-4, gpt-4o, gpt4, gpt4-api, language-model, openai, openai-api, openai-chatgpt, reverse-engineering
- Description: The official gpt4free repository | various collection of powerful language models | opus 4.6 gpt 5.3 kimi 2.5 deepseek v3.2 gemini 3

## Extracted README / Docs / Examples



# FILE: README.md

# GPT4Free (g4f)

[![PyPI](https://img.shields.io/pypi/v/g4f)](https://pypi.org/project/g4f) [![Docker Hub](https://img.shields.io/badge/docker-hlohaus789%2Fg4f-blue)](https://hub.docker.com/r/hlohaus789/g4f) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-red.svg)](https://www.gnu.org/licenses/gpl-3.0.txt) [![PyPI Downloads](https://static.pepy.tech/personalized-badge/g4f?period=total&units=INTERNATIONAL_SYSTEM&left_color=GREY&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/g4f) ![GitHub Repo stars](https://img.shields.io/github/stars/xtekky/gpt4free)

<p align="center">
  <img src="https://g4f.dev/docs/images/477107515-7f60c240-00fa-4c37-bf7f-ae5cc20906a1.png" alt="GPT4Free logo" height="200" />
</p>

<p align="center">
  <span style="background: linear-gradient(45deg, #12c2e9, #c471ed, #f64f59); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
    <strong>Created by <a href="https://github.com/xtekky">@xtekky</a>,<br> maintained by <a href="https://github.com/hlohaus">@hlohaus</a></strong>
  </span>
</p>
<p align="center">
<span>Support the project on</span>
      <a href="https://github.com/sponsors/hlohaus" target="_blank" rel="noopener noreferrer">
        GitHub Sponsors
      </a>
      ❤️
</p>
<p align="center">
Live demo & docs: https://g4f.dev | Documentation: https://g4f.dev/docs
</p>

---

GPT4Free (g4f) is a community-driven project that aggregates multiple accessible providers and interfaces to make working with modern LLMs and media-generation models easier and more flexible. GPT4Free aims to offer multi-provider support, local GUI, OpenAI-compatible REST APIs, and convenient Python and JavaScript clients — all under a community-first license.

This README is a consolidated, improved, and complete guide to installing, running, and contributing to GPT4Free.

Table of contents
- [What’s included](#whats-included)
- [Quick links](#quick-links)
- [Requirements & compatibility](#requirements--compatibility)
- [Installation](#installation)
  - [Docker (recommended)](#docker-recommended)
  - [Slim Docker image](#slim-docker-image)
  - [Windows (.exe)](#windows-exe)
  - [Python (pip / from source / partial installs)](#python-pip--from-source--partial-installs)
- [Running the app](#running-the-app)
  - [GUI (web client)](#gui-web-client)
  - [FastAPI / Interference API](#fastapi--interference-api)
  - [CLI](#cli)
  - [Optional provider login (desktop in container)](#optional-provider-login-desktop-in-container)
- [Using the Python client](#using-the-python-client)
  - [Synchronous text example](#synchronous-text-example)
  - [Image generation example](#image-generation-example)
  - [Async client example](#async-client-example)
- [Using GPT4Free.js (browser JS client)](#using-gpt4freejs-browser-js-client)
- [Providers & models (overview)](#providers--models-overview)
- [Local inference & media](#local-inference--media)
- [Configuration & customization](#configuration--customization)
- [Running on smartphone](#running-on-smartphone)
- [Interference API (OpenAI‑compatible)](#interference-api-openai-compatible)
- [Examples & common patterns](#examples--common-patterns)
- [Contributing](#contributing)
  - [How to create a new provider](#how-to-create-a-new-provider)
  - [How AI can help you write code](#how-ai-can-help-you-write-code)
- [Security, privacy & takedown policy](#security-privacy--takedown-policy)
- [Credits, contributors & attribution](#credits-contributors--attribution)
- [Powered-by highlights](#powered-by-highlights)
- [Changelog & releases](#changelog--releases)
- [Manifesto / Project principles](#manifesto--project-principles)
- [License](#license)
- [Contact & sponsorship](#contact--sponsorship)
- [Appendix: Quick commands & examples](#appendix-quick-commands--examples)

---

## What’s included
- Python client library and async client.
- Optional local web GUI.
- FastAPI-based OpenAI-compatible API (Interference API).
- Official browser JS client (g4f.dev distribution).
- Docker images (full and slim).
- Multi-provider adapters (LLMs, media providers, local inference backends).
- Tooling for image/audio/video generation and media persistence.

---

## Quick links
- Website & docs: https://g4f.dev | https://g4f.dev/docs  
- PyPI: https://pypi.org/project/g4f  
- Docker image: https://hub.docker.com/r/hlohaus789/g4f  
- Releases: https://github.com/xtekky/gpt4free/releases  
- Issues: https://github.com/xtekky/gpt4free/issues  
- Community: Telegram (https://telegram.me/g4f_channel) · Discord News (https://discord.gg/5E39JUWUFa) · Discord Support (https://discord.gg/qXA4Wf4Fsm)

---

## Requirements & compatibility
- Python 3.10+ recommended.
- Google Chrome/Chromium for providers using browser automation.
- Docker for containerized deployment.
- Works on x86_64 and arm64 (slim image supports both).
- Some provider adapters may require platform-specific tooling (Chrome/Chromium, etc.). Check provider docs for details.

---

## Installation

### Docker (recommended)
1. Install Docker: https://docs.docker.com/get-docker/
2. Create persistent directories:
   - Example (Linux/macOS):
     ```bash
     mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_media
     sudo chown -R 1200:1201 ${PWD}/har_and_cookies ${PWD}/generated_media
     ```
3. Pull image:
   ```bash
   docker pull hlohaus789/g4f
   ```
4. Run container:
   ```bash
   docker run -p 8080:8080 -p 7900:7900 \
     --shm-size="2g" \
     -v ${PWD}/har_and_cookies:/app/har_and_cookies \
     -v ${PWD}/generated_media:/app/generated_media \
     hlohaus789/g4f:latest
   ```
Notes:
- Port 8080 serves GUI/API; 7900 can expose a VNC-like desktop for provider logins (optional).
- Increase --shm-size for heavier browser automation tasks.

### Slim Docker image (x64 & arm64)
```bash
mkdir -p ${PWD}/har_and_cookies ${PWD}/generated_media
chown -R 1000:1000 ${PWD}/har_and_cookies ${PWD}/generated_media

docker run \
  -p 1337:8080 -p 8080:8080 \
  -v ${PWD}/har_and_cookies:/app/har_and_cookies \
  -v ${PWD}/generated_media:/app/generated_media \
  hlohaus789/g4f:latest-slim
```
Notes:
- The slim image can update the g4f package on startup and installs additional dependencies as needed.
- In this example, the Interference API is mapped to 1337.

### Windows Guide (.exe)

👉 Check out the Windows launcher for GPT4Free:  
🔗 [https://github.com/gpt4free/g4f.exe](https://github.com/gpt4free/g4f.exe) 🚀  

1. Download the release artifact `g4f.exe.zip` from:
   https://github.com/xtekky/gpt4free/releases/latest
2. Unzip and run `g4f.exe`.
3. Open GUI at: http://localhost:8080/chat/
4. If Windows Firewall blocks access, allow the application.

### Python Installation (pip / from source / partial installs)

Prerequisites:
- Python 3.10+ (https://www.python.org/downloads/)
- Chrome/Chromium for some providers.

Install from PyPI (recommended):
```bash
pip install -U g4f[all]
```

Partial installs
- To install only specific functionality, use optional extras groups. See docs/requirements.md in the project docs.

Install from source:
```bash
git clone https://github.com/xtekky/gpt4free.git
cd gpt4free
pip install -r requirements.txt
pip install -e .
```

Notes:
- Some features require Chrome/Chromium or other tools; follow provider-specific docs.

---

## Running the app

### GUI (web client)
- Run via Python:
```python
from g4f.gui import run_gui
run_gui()
```
- Or via CLI:
```bash
python -m g4f.cli gui --port 8080 --debug
```
- Open: http://localhost:8080/chat/

### FastAPI / Interference API
- Start FastAPI server:
```bash
python -m g4f --port 8080 --debug
```
- If using slim docker mapping, Interference API may be available at `http://localhost:1337/v1`
- Swagger UI: `http://localhost:1337/docs`

### CLI
- Start GUI server:
```bash
python -m g4f.cli gui --port 8080 --debug
```

### MCP Server
GPT4Free now includes a Model Context Protocol (MCP) server that allows AI assistants like Claude to access web search, scraping, and image generation capabilities.

**Starting the MCP server (stdio mode):**
```bash
# Using g4f command
g4f mcp

# Or using Python module
python -m g4f.mcp
```

**Starting the MCP server (HTTP mode):**
```bash
# Start HTTP server on port 8765
g4f mcp --http --port 8765

# Custom host and port
g4f mcp --http --host 127.0.0.1 --port 3000
```

HTTP mode provides:
- `POST http://localhost:8765/mcp` - JSON-RPC endpoint
- `GET http://localhost:8765/health` - Health check

**Configuring with Claude Desktop:**

Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "gpt4free": {
      "command": "python",
      "args": ["-m", "g4f.mcp"]
    }
  }
}
```

**Available MCP Tools:**
- `web_search` - Search the web using DuckDuckGo
- `web_scrape` - Extract text content from web pages  
- `image_generation` - Generate images from text prompts

For detailed MCP documentation, see [g4f/mcp/README.md](g4f/mcp/README.md)

### Optional provider login (desktop within container)
- Accessible at:
  ```
  http://localhost:7900/?autoconnect=1&resize=scale&password=secret
  ```
- Useful for logging into web-based providers to obtain cookies/HAR files.

---

## Using the Python client

Install:
```bash
pip install -U g4f[all]
```

Synchronous text example:
```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    web_search=False
)
print(response.choices[0].message.content)
```
Expected:
```
Hello! How can I assist you today?
```

Image generation example:
```python
from g4f.client import Client

client = Client()
response = client.images.generate(
    model="flux",
    prompt="a white siamese cat",
    response_format="url"
)
print(f"Generated image URL: {response.data[0].url}")
```

Async client example:
```python
from g4f.client import AsyncClient
import asyncio

async def main():
    client = AsyncClient()
    response = await client.chat.completio

# FILE: docs/arm64-build-plan.md

# Future ARM64 Build Enhancement Plan

This document outlines the plan for adding comprehensive ARM64 support to the g4f build system.

## Current Status

- **macOS ARM64**: ✅ Supported (native runners)
- **Linux ARM64**: ⏳ Requires ARM64 runners or cross-compilation
- **Windows ARM64**: ⏳ Requires ARM64 runners or cross-compilation

## Implementation Plan for ARM64 Support

### Phase 1: Linux ARM64 (Future Enhancement)
```yaml
# Add to .github/workflows/build-packages.yml
build-linux-exe:
  strategy:
    matrix:
      include:
        - architecture: x64
          runner: ubuntu-latest
          runner-arch: x86_64
        - architecture: arm64
          runner: buildjet-4vcpu-ubuntu-2204-arm  # ARM64 runners
          runner-arch: aarch64
```

### Phase 2: Windows ARM64 (Future Enhancement)  
```yaml
build-windows-exe:
  strategy:
    matrix:
      include:
        - architecture: x64
          runner: windows-latest
          runner-arch: x86_64
        - architecture: arm64  
          runner: windows-latest-arm64  # When available
          runner-arch: arm64
```

### Phase 3: Cross-compilation Support
For environments without native ARM64 runners:
- Use Docker with QEMU emulation
- Configure Nuitka for cross-compilation
- Test compatibility and performance

## Benefits of ARM64 Support

1. **Performance**: Native ARM64 binaries run faster on ARM64 hardware
2. **Compatibility**: Better support for Apple Silicon Macs and ARM64 Linux systems
3. **Future-proofing**: ARM64 adoption is increasing across all platforms

## Testing Requirements

- Verify ARM64 binaries work on actual ARM64 hardware
- Test performance compared to x64 binaries on ARM64 systems
- Ensure compatibility with all g4f features

## Notes

- This is marked as a future enhancement because it requires ARM64 runners or cross-compilation setup
- Current implementation provides a solid foundation for easy expansion
- The build matrix is designed to accommodate additional architectures

# FILE: docs/reasoning-standardization.md

# Reasoning Field Standardization

## Issue
DeepSeek uses `"reasoning_content"` field while OpenAI uses `"reasoning"` field in their chat completion streaming responses. This inconsistency caused confusion about what field name to use in the g4f Interference API.

## Decision
**Standardized on OpenAI's `"reasoning"` field format for API output while maintaining input compatibility.**

## Rationale
1. **OpenAI Compatibility**: OpenAI is the de facto standard for chat completion APIs
2. **Ecosystem Compatibility**: Most tools and libraries expect OpenAI format
3. **Consistency**: Provides a unified output format regardless of the underlying provider
4. **Backward Compatibility**: Input parsing continues to accept both formats

## Implementation

### Input Format Support (Unchanged)
The system continues to accept both input formats in `OpenaiTemplate.py`:
```python
reasoning_content = choice.get("delta", {}).get("reasoning_content", choice.get("delta", {}).get("reasoning"))
```

### Output Format Standardization (Changed)
- **Streaming Delta**: Uses `reasoning` field (OpenAI format)
- **Non-streaming Message**: Uses `reasoning` field (OpenAI format)  
- **API Responses**: Should use standard OpenAI streaming format

### Example Output Formats

#### Streaming Response (OpenAI Compatible)
```json
{
  "id": "chatcmpl-example",
  "object": "chat.completion.chunk",
  "choices": [{
    "index": 0,
    "delta": {
      "role": "assistant",
      "reasoning": "I need to think about this step by step..."
    },
    "finish_reason": null
  }]
}
```

#### Non-streaming Response
```json
{
  "choices": [{
    "message": {
      "role": "assistant",
      "content": "Here's my answer",
      "reasoning": "My reasoning process was..."
    }
  }]
}
```

## Files Changed
- `g4f/client/stubs.py`: Updated to use `reasoning` field instead of `reasoning_content`

## Testing
- Added comprehensive tests for format standardization
- Verified input compatibility with both OpenAI and DeepSeek formats
- Confirmed no regressions in existing functionality

# FILE: docs/README.md

Link to [Documentation](https://github.com/gpt4free/gpt4free.github.io)

# FILE: docs/aarch64-compatibility.md

# aarch64 (ARM64) Compatibility

This document describes the compatibility status and known issues for g4f on aarch64 (ARM64) systems.

## Issue Resolution

**Fixed in this release:** The "Illegal instruction (core dumped)" error that occurred when importing g4f on aarch64 systems has been resolved.

### Problem
Previously, g4f would crash with "Illegal instruction (core dumped)" on ARM64 systems (such as Apple Silicon Macs, Raspberry Pi, AWS Graviton instances, etc.) due to compiled dependencies with architecture-specific optimizations.

### Solution
The library now includes proper error handling for architecture-incompatible dependencies:
- Safe import mechanisms prevent crashes when compiled libraries are unavailable
- Graceful fallbacks to alternative implementations when possible
- Clear error messages when specific features require unavailable dependencies

## Compatibility Status

### ✅ Working Features
- Basic client functionality (`from g4f.client import Client`)
- CLI commands (`g4f --help`, `g4f client --help`)
- Providers that use standard HTTP libraries
- Most text generation functionality

### ⚠️ Limited Features  
Some advanced features may have reduced functionality on aarch64:
- Providers requiring `curl_cffi` will fall back to `aiohttp`
- Browser automation features may not be available
- Some performance optimizations may not be active

### 📋 Requirements
For full functionality on aarch64, ensure you have:
```bash
# Basic requirements (should work on all architectures)
pip install -r requirements-min.txt

# Full requirements (some packages may need compilation on aarch64)
pip install -r requirements.txt
```

## Testing Your Installation

You can verify your installation works correctly:

```python
# Test basic import
from g4f.client import Client
client = Client()
print("✓ g4f imported successfully")

# Test CLI
import subprocess
result = subprocess.run(['g4f', '--help'], capture_output=True)
print("✓ CLI works" if result.returncode == 0 else "✗ CLI issues")
```

## Known Issues

1. **Performance**: Some providers may have reduced performance due to fallback implementations
2. **Browser Features**: nodriver and webview functionality may not be available
3. **Image Processing**: Some image-related features may have compatibility issues

## Getting Help

If you encounter issues on aarch64:
1. First try with minimal requirements: `pip install -r requirements-min.txt`
2. Check if the issue persists with basic functionality
3. Report architecture-specific issues with your system details:
   - Architecture: `uname -m`
   - OS: `uname -a` 
   - Python version: `python --version`

# FILE: docs/build-workflow.md

# Build Workflow Documentation

This document explains the comprehensive build workflow for g4f that creates packages for multiple platforms and package managers.

## Workflow Overview

The `.github/workflows/build-packages.yml` workflow automatically builds multiple package formats when a version tag is pushed to the repository.

### Supported Package Formats

1. **PyPI Package** - Python wheel and source distribution
2. **Windows Executable** - Standalone .exe file built with Nuitka  
3. **Linux Executable** - Standalone binary for Linux systems built with Nuitka
4. **macOS Executable** - Standalone binary for macOS systems built with Nuitka (x64 and ARM64)
5. **Debian Packages** - .deb files for Ubuntu/Debian (amd64, arm64, armhf)
6. **WinGet Package** - Windows Package Manager manifest
7. **Docker Images** - Multi-architecture container images

### Triggering a Build

To trigger a build, push a version tag to the repository:

```bash
git tag v1.2.3
git push origin v1.2.3
```

The workflow will:
1. Detect the tag and extract the version
2. Build all package formats in parallel 
3. Create a GitHub release with all artifacts
4. Publish to PyPI (for releases)
5. Generate WinGet manifest for Windows Package Manager

### Manual Build Triggering

You can also manually trigger builds using the workflow_dispatch event:

1. Go to the "Actions" tab in GitHub
2. Select "Build All Packages" workflow
3. Click "Run workflow"
4. Optionally specify a version number

### Package Locations

After a successful build, packages are available:

- **GitHub Releases**: All executables and packages as release assets
  - Python packages (wheel and source distribution)
  - Standalone executables for Windows, Linux, and macOS
  - Debian packages for AMD64, ARM64, and ARMv7 architectures
  - WinGet manifest files
- **PyPI**: `pip install g4f`
- **Docker Hub**: `docker pull hlohaus789/g4f:latest`
- **WinGet**: `winget install g4f` (after manifest approval)

### Build Requirements

The workflow handles all dependencies automatically, but for local development:

- Python 3.10+
- Nuitka for executables (replaces PyInstaller)
- Docker for container builds
- dpkg-deb for Debian packages

### Customizing Builds

Key files for customization:

- `g4f_cli.py` - Entry point for executable builds
- `scripts/build-nuitka.sh` - Nuitka build script for all platforms
- `scripts/build-deb.sh` - Debian package build script
- `winget/manifests/` - WinGet package manifest templates
- `.github/workflows/build-packages.yml` - Main workflow configuration

### Version Handling

The workflow supports multiple version sources:
1. Git tags (preferred for releases)
2. Environment variable `G4F_VERSION`
3. Manual input in workflow dispatch

Version must follow [PEP 440](https://peps.python.org/pep-0440/) format for PyPI compatibility.

### Troubleshooting

Common issues and solutions:

1. **Build fails**: Check Python version compatibility and dependencies
2. **Version errors**: Ensure version follows PEP 440 format
3. **Missing artifacts**: Check if all build jobs completed successfully
4. **Docker push fails**: Verify Docker Hub credentials are set in repository secrets

### Security Notes

The workflow uses secure practices:
- Trusted action versions
- Environment isolation
- Secret management for credentials
- No hardcoded sensitive data

### Contributing

To improve the build system:
1. Test changes locally first
2. Update documentation
3. Consider backward compatibility
4. Test with multiple Python versions

# FILE: docs/config-yaml-routing.md

# Custom Model Routing with `config.yaml`

g4f supports a `config.yaml` file that lets you define **custom model routes** – named
models that are transparently forwarded to one or more real providers based on
availability, quota balance, and recent error counts.

This is similar to the [LiteLLM](https://docs.litellm.ai/) routing configuration.

---

## Quick start

1. Place a `config.yaml` file in the same directory as your `.har` / `.json`
   cookie files (the "cookies dir").
   * Default location: `~/.config/g4f/cookies/config.yaml`
   * Alternative: `./har_and_cookies/config.yaml`

2. Define your routes (see format below).

3. g4f loads the file automatically when it reads the cookie directory
   (e.g. on API server start-up, or when `read_cookie_files()` is called).

4. Request the custom model name from any client:

```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="my-gpt4",   # defined in config.yaml
    messages=[{"role": "user", "content": "Hello!"}],
)
print(response.choices[0].message.content)
```

---

## File format

```yaml
models:
  - name: "<model-name>"          # the name clients use
    providers:
      - provider: "<ProviderName>"  # g4f provider class name
        model: "<provider-model>"   # model name passed to that provider
        condition: "<expression>"   # optional – see below
      - provider: "..."             # fallback provider (no condition = always eligible)
        model: "..."
```

### Keys

| Key | Required | Description |
|-----|----------|-------------|
| `name` | ✅ | The model name used by clients. |
| `providers` | ✅ | Ordered list of provider candidates. |
| `provider` | ✅ | Provider class name (e.g. `"OpenaiAccount"`, `"PollinationsAI"`). |
| `model` | | Model name forwarded to the provider. Defaults to the route `name`. |
| `condition` | | Boolean expression controlling when this provider is eligible. |

---

## Condition expressions

The `condition` field is a boolean expression evaluated before each request.
It can reference the following variables:

### `quota` – full provider quota dict

Each provider that implements `get_quota()` returns a **provider-specific** dict.
The result is cached in memory (5 min TTL) and invalidated on 429 responses.

Access any field with **dot-notation**:

| Provider | `get_quota()` format | Example condition |
|----------|---------------------|-------------------|
| `PollinationsAI` | `{"balance": float}` | `quota.balance > 0` |
| `Yupp` | `{"credits": {"remaining": int, "total": int}}` | `quota.credits.remaining > 100` |
| `PuterJS` | raw metering JSON from the API | `quota.total_requests < 1000` |
| `GeminiCLI` | `{"buckets": [...]}` | `error_count < 3` |
| `GithubCopilot` | usage details dict | `error_count < 5` |

Missing keys resolve to `0.0` (no error raised).

### `balance` – shorthand alias

`balance` is a convenience shorthand for `quota.balance`.  It is preserved for
backward compatibility and is most useful with **PollinationsAI** which returns
`{"balance": float}`.  For other providers, prefer the explicit `quota.*` form.

### `error_count`

Number of errors recorded for this provider in the last **1 hour**.  Errors
older than 1 hour are automatically pruned.

### Operators

| Operator | Meaning |
|----------|---------|
| `>` `<` `>=` `<=` | Numeric comparison |
| `==` `!=` | Equality / inequality |
| `and` `or` `not` | Logical connectives |
| `(` `)` | Grouping |

### Examples

```yaml
# PollinationsAI – uses quota.balance shorthand
condition: "balance > 0"
condition: "balance > 0 or error_count < 3"

# Yupp – provider-specific nested field
condition: "quota.credits.remaining > 0"
condition: "quota.credits.remaining > 0 or error_count < 3"

# Any provider – error-count-only conditions work universally
condition: "error_count < 3"
condition: "error_count == 0"
```

When the condition is **absent** or evaluates to `True`, the provider is
eligible.  When it evaluates to `False` the provider is skipped and g4f
tries the next one in the list.

---

## Quota caching

Quota values are fetched via the provider's `get_quota()` method and cached in
memory for **5 minutes** (configurable via `QuotaCache.ttl`).

When a provider returns an HTTP **429 (Too Many Requests)** error the cache
entry for that provider is **immediately invalidated**, so the next routing
decision fetches a fresh quota value before deciding.

---

## Error counting

Every time a provider raises an exception the error counter for that provider
is incremented.  Errors older than **1 hour** are automatically pruned.

Reference `error_count` in a condition to avoid retrying providers that have
been failing repeatedly.

---

## Full example

```yaml
# ~/.config/g4f/cookies/config.yaml

models:
  # PollinationsAI: use quota.balance shorthand
  - name: "my-gpt4"
    providers:
      - provider: "OpenaiAccount"
        model: "gpt-4o"
        condition: "balance > 0 or error_count < 3"
      - provider: "PollinationsAI"
        model: "openai-large"

  # Yupp: provider-specific nested quota field
  - name: "yupp-chat"
    providers:
      - provider: "Yupp"
        model: "gpt-4o"
        condition: "quota.credits.remaining > 0 or error_count < 3"
      - provider: "PollinationsAI"
        model: "openai-large"

  # Universal: error-count-only condition works for any provider
  - name: "llama-fast"
    providers:
      - provider: "Groq"
        model: "llama-3.3-70b"
        condition: "error_count < 3"
      - provider: "DeepInfra"
        model: "meta-llama/Llama-3.3-70B-Instruct"
```

---

## Python API

The routing machinery is exposed in `g4f.providers.config_provider`:

```python
from g4f.providers.config_provider import (
    RouterConfig,        # load / query routes
    QuotaCache,          # inspect / invalidate quota cache
    ErrorCounter,        # inspect / reset error counters
    evaluate_condition,  # evaluate a condition string directly
)

# Reload routes from a cu
