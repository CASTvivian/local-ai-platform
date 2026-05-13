# Missing Repo Summary Source: zai-org/Open-AutoGLM

- URL: https://github.com/zai-org/Open-AutoGLM
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/zai-org__Open-AutoGLM
- Clone Status: cloned
- Language: Python
- Stars: 25253
- Topics: agent, phone-use-agent
- Description: An Open Phone Agent Model & Framework. Unlocking the AI Phone for Everyone

## Extracted README / Docs / Examples



# FILE: README.md

# Open-AutoGLM

[Readme in English](README_en.md)

<div align="center">
<img src=resources/logo.svg width="20%"/>
</div>
<p align="center">
    👋 加入我们的 <a href="resources/WECHAT.md" target="_blank">微信</a> 社区
</p>
<p align="center">
    👋 关注智谱 AI 输入法 <a href="https://x.com/Autotyper_Agent?s=20" target="_blank">X</a> 账号
</p>
<p align="center">
    🎤 进一步在我们的产品 <a href="https://autoglm.zhipuai.cn/autotyper/" target="_blank">智谱 AI 输入法</a> 体验“用嘴发指令”
</p>
<p align="center">
    <a href="https://mp.weixin.qq.com/s/wRp22dmRVF23ySEiATiWIQ" target="_blank">AutoGLM 实战派</a> 开发者激励活动火热进行中，跑通、二创即可瓜分数万元现金奖池！成果提交 👉 <a href="https://zhipu-ai.feishu.cn/share/base/form/shrcnE3ZuPD5tlOyVJ7d5Wtir8c?from=navigation" target="_blank">入口</a>
</p>

## 懒人版快速安装

你可以使用Claude Code，配置 [GLM Coding Plan](https://bigmodel.cn/glm-coding) 后，输入以下提示词，快速部署本项目。

```
访问文档，为我安装 AutoGLM
https://raw.githubusercontent.com/zai-org/Open-AutoGLM/refs/heads/main/README.md
```

## 项目介绍

Phone Agent 是一个基于 AutoGLM 构建的手机端智能助理框架，它能够以多模态方式理解手机屏幕内容，并通过自动化操作帮助用户完成任务。系统通过
ADB(Android Debug Bridge)来控制设备，以视觉语言模型进行屏幕感知，再结合智能规划能力生成并执行操作流程。用户只需用自然语言描述需求，如“打开小红书搜索美食”，Phone
Agent 即可自动解析意图、理解当前界面、规划下一步动作并完成整个流程。系统还内置敏感操作确认机制，并支持在登录或验证码场景下进行人工接管。同时，它提供远程
ADB 调试能力，可通过 WiFi 或网络连接设备，实现灵活的远程控制与开发。

> ⚠️
> 本项目仅供研究和学习使用。严禁用于非法获取信息、干扰系统或任何违法活动。请仔细审阅 [使用条款](resources/privacy_policy.txt)。

## 与其他自动化工具集成

### Midscene.js

[Midscene.js](https://midscenejs.com/zh/index.html) 是一款由视觉模型驱动的开源 UI 自动化 SDK，支持通过 JavaScript 或 Yaml 格式的流程语法，实现多平台的自动化。

目前 Midscene.js 已完成对 AutoGLM 模型的适配，你可以通过 [Midscene.js 接入指南](https://midscenejs.com/zh/model-common-config.html#auto-glm) 快速体验 AutoGLM 在 iOS 和 Android 设备上的自动化效果。

## 模型下载地址

| Model                         | Download Links                                                                                                                                                         |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoGLM-Phone-9B              | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B)                           |
| AutoGLM-Phone-9B-Multilingual | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B-Multilingual) |

其中，`AutoGLM-Phone-9B` 是针对中文手机应用优化的模型，而 `AutoGLM-Phone-9B-Multilingual` 支持英语场景，适用于包含英文等其他语言内容的应用。

## Android 环境准备

### 1. Python 环境

建议使用 Python 3.10 及以上版本。

### 2. 手机调试命令行工具

根据你的设备类型选择相应的工具：

#### 对于 Android 设备 - 使用 ADB

1. 下载官方 ADB [安装包](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)，并解压到自定义路径
2. 配置环境变量

- MacOS 配置方法：在 `Terminal` 或者任何命令行工具里

  ```bash
  # 假设解压后的目录为 ~/Downloads/platform-tools。如果不是请自行调整命令。
  export PATH=${PATH}:~/Downloads/platform-tools
  ```

- Windows 配置方法：可参考 [第三方教程](https://blog.csdn.net/x2584179909/article/details/108319973) 进行配置。

#### 对于鸿蒙设备 (HarmonyOS NEXT版本以上) - 使用 HDC

1. 下载 HDC 工具：
   - 从 [HarmonyOS SDK](https://developer.huawei.com/consumer/cn/download/) 下载
2. 配置环境变量

- MacOS/Linux 配置方法：

  ```bash
  # 假设解压后的目录为 ~/Downloads/harmonyos-sdk/toolchains。请根据实际路径调整。
  export PATH=${PATH}:~/Downloads/harmonyos-sdk/toolchains
  ```

- Windows 配置方法：将 HDC 工具所在目录添加到系统 PATH 环境变量

### 3. Android 7.0+ 或 HarmonyOS 设备，并启用 `开发者模式` 和 `USB 调试`

1. 开发者模式启用：通常启用方法是，找到 `设置-关于手机-版本号` 然后连续快速点击 10
   次左右，直到弹出弹窗显示“开发者模式已启用”。不同手机会有些许差别，如果找不到，可以上网搜索一下教程。
2. USB 调试启用：启用开发者模式之后，会出现 `设置-开发者选项-USB 调试`，勾选启用
3. 部分机型在设置开发者选项以后, 可能需要重启设备才能生效. 可以测试一下: 将手机用USB数据线连接到电脑后, `adb devices`
   查看是否有设备信息, 如果没有说明连接失败.

**请务必仔细检查相关权限**

![权限](resources/screenshot-20251209-181423.png)

### 4. 安装 ADB Keyboard(仅 Android 设备需要，用于文本输入)

**注意：鸿蒙设备使用原生输入方法，无需安装 ADB Keyboard。**

如果你使用的是 Android 设备：

下载 [安装包](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk) 并在对应的安卓设备中进行安装。
注意，安装完成后还需要到 `设置-输入法` 或者 `设置-键盘列表` 中启用 `ADB Keyboard` 才能生效(或使用命令`adb shell ime enable com.android.adbkeyboard/.AdbIME`[How-to-use](https://github.com/senzhk/ADBKeyBoard/blob/master/README.md#how-to-use))

## iPhone 环境准备

如果你使用的是 iPhone 设备，请参考专门的 iOS 配置文档：

📱 [iOS 环境配置指南](docs/ios_setup/ios_setup.md)

该文档详细介绍了如何配置 WebDriverAgent 和 iPhone 设备，以便在 iOS 上使用 AutoGLM。

## 部署准备工作

### 1. 安装依赖

```bash
pip install -r requirements.txt 
pip install -e .
```

### 2. 配置 ADB 或 HDC

#### 对于 Android 设备

确认 **USB数据线具有数据传输功能**, 而不是仅有充电功能

确保已安装 ADB 并使用 **USB数据线** 连接设备：

```bash
# 检查已连接的设备
adb devices

# 输出结果应显示你的设备，如：
# List of devices attached
# emulator-5554   device
```

#### 对于鸿蒙设备

确认 **USB数据线具有数据传输功能**, 而不是仅有充电功能

确保已安装 HDC 并使用 **USB数据线** 连接设备：

```bash
# 检查已连接的设备
hdc list targets

# 输出结果应显示你的设备，如：
# 7001005458323933328a01bce01c2500
```

### 3. 启动模型服务

你可以选择自行部署模型服务，或使用第三方模型服务商。

#### 选项 A: 使用第三方模型服务

如果你不想自行部署模型，可以使用以下已部署我们模型的第三方服务：

**1. 智谱 BigModel**

- 文档: https://docs.bigmodel.cn/cn/api/introduction
- `--base-url`: `https://open.bigmodel.cn/api/paas/v4`
- `--model`: `autoglm-phone`
- `--apikey`: 在智谱平台申请你的 API Key

**2. ModelScope(魔搭社区)**

- 文档: https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B
- `--base-url`: `https://api-inference.modelscope.cn/v1`
- `--model`: `ZhipuAI/AutoGLM-Phone-9B`
- `--apikey`: 在 ModelScope 平台申请你的 API Key

使用第三方服务的示例：

```bash
# 使用智谱 BigModel
python main.py --base-url https://open.bigmodel.cn/api/paas/v4 --model "autoglm-phone" --apikey "your-bigmodel-api-key" "打开美团搜索附近的火锅店"

# 使用 ModelScope
python main.py --base-url https://api-inference.modelscope.cn/v1 --model "ZhipuAI/AutoGLM-Phone-9B" --apikey "your-modelscope-api-key" "打开美团搜索附近的火锅店"
```

#### 选项 B: 自行部署模型

如果你希望在本地或自己的服务器上部署模型：

1. 按照 `requirements.txt` 中 `For Model Deployment` 章节自行安装推理引擎框架。

对于SGLang， 除了使用pip安装，你也可以使用官方docker:
>
> ```shell
> docker pull lmsysorg/sglang:v0.5.6.post1
> ```
>
> 进入容器，执行
>
> ```
> pip install nvidia-cudnn-cu12==9.16.0.29
> ```

对于 vLLM，除了使用pip 安装，你也可以使用官方docker:
>
> ```shell
> docker pull vllm/vllm-openai:v0.12.0
> ```
>
> 进入容器，执行
>
> ```
> pip install -U transformers --pre
> ```

**注意**: 上述步骤出现的关于 transformers 的依赖冲突可以忽略。

1. 在对应容器或者实体机中(非容器安装)下载模型，通过 SGlang / vLLM 启动，得到 OpenAI 格式服务。这里提供一个 vLLM部署方案，请严格遵循我们提供的启动参数:

- vLLM:

```shell
python3 -m vllm.entrypoints.openai.api_server \
 --served-model-name autoglm-phone-9b \
 --allowed-local-media-path /   \
 --mm-encoder-tp-mode data \
 --mm_processor_cache_type shm \
 --mm_processor_kwargs "{\"max_pixels\":5000000}" \
 --max-model-len 25480  \
 --chat-template-content-format string \
 --limit-mm-per-prompt "{\"image\":10}" \
 --model zai-org/AutoGLM-Phone-9B \
 --port 8000
```

- SGLang:

```shell
python3 -m sglang.launch_server --model-path  zai-org/AutoGLM-Phone-9B \
        --served-model-name autoglm-phone-9b  \
        --context-length 25480  \
        --mm-enable-dp-encoder   \
        --mm-process-config '{"image":{"max_pixels":5000000}}'  \
        --port 8000
```

- 该模型结构与 `GLM-4.1V-9B-Thinking` 相同, 关于模型部署的详细内容，你也以查看 [GLM-V](https://github.com/zai-org/GLM-V)
  获取模型部署和使用指南。

- 运行成功后，将可以通过 `http://localhost:8000/v1` 访问模型服务。 如果您在远程服务器部署模型, 使用该服务器的IP访问模型.

### 4. 检查模型部署

模型服务启动后，可以使用检查脚本验证部署是否成功：

```bash
python scripts/check_deployment_cn.py --base-url http://你的IP:你的端口/v1 --model 模型名称
```

脚本将发送测试请求并展示模型的推理结果，你可以根据输出判断模型部署是否正常工作。

基于给定的任务, 预期输出如下。**如果思维链长度很短, 或者出现了乱码, 很可能是模型部署失败**, 请仔细检查文档要求的配置和依赖。

```
<think>用户想要比较这个洗发水在京东和淘宝上的价格，然后选择最便宜的平台下单。当前在小红书app上，显示的是一个关于LUMMI MOOD洗发水的帖子。

我需要：
1. 先启动京东app，搜索这个洗发水
2. 查看京东的价格
3. 再启动淘宝app，搜索这个洗发水
4. 查看淘宝的价格
5. 比较价格后，选择最便宜的京东或淘宝下单

首先，我需要从当前的小红书界面退出，然后启动京东app。</think>
<answer>do(action="Launch", app="京东")
```

**参数说明：**
- `--base-url`: 模型服务地址(根据实际部署地址修改)
- `--model`: 模型名称
- `--messages-file`: 可选，指定自定义测试消息文件(默认使用 `scripts/sample_messages.json`)

## 使用 AutoGLM

### 命令行

根据你部署的模型, 设置 `--base-url` 和 `--model` 参数, 设置 `--device-type` 指定是安卓设备或鸿蒙设备 (默认值 adb 表示安卓设备, hdc 表示鸿蒙设备). 例如:

```bash
# Android 设备 - 交互模式
python main.py --base-url http://localhost:8000/v1 --model "autoglm-phone-9b"

# Android 设备 - 指定任务
python main.py --base-url http://localhost:8000/v1 "打开美团搜索附近的火锅店"

# 鸿蒙设备 - 交互模式
python main.py --device-type hdc --base-url http://localhost:8000/v1 --model "autoglm-phone-9b"

# 鸿蒙设备 - 指定任务
python main.py --device-type hdc --base-url http://localhost:8000/v1 "打开美团搜索附近的火锅店"

# 使用 API Key 进行认证
python main.py --apikey sk-xxxxx

# 使用英文 system prompt
python main.py --lang en --base-url http://localhost:8000/v1 "Open Chrome browser"

# 列出支持的应用（Android）
python main.py --list-apps

# 列出支持的应用（鸿蒙）
python main.py --device-type hdc --list-apps
```

### Python API

```python
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig

# Configure model
model_config = ModelConfig(
    base_url="http://localhost:8000/v1",
    model_name="autoglm-phone-9b",
)

# 创建 Agent
agent = PhoneAgent(model_config=model_config)

# 执行任务
result = agent.run("打开淘宝搜索无线耳机")
print(result)
```

## 远程调试

Phone Agent 支持通过 WiFi/网络进行远程 ADB/HDC 调试，无需 USB 连接即可控制设备。

### 配置远程调试

#### 在手机端开启无线调试

##### Android 设备

确保手机和电脑在同一个WiFi中，如图所示

![开启无线调试](resources/setting.png)

##### 鸿蒙设备

确保手机和电脑在同一个WiFi中：
1. 进入 `设置 > 系统和更新 > 开发者选项`
2. 开启 `USB 调试` 和 `无线调试`
3. 记录显示的 IP 地址和端口号

#### 在电脑端使用标准 ADB/HDC 命令

```bash
# Android 设备 - 通过 WiFi 连接, 改成手机显示的 IP 地址和端口
adb connect 192.168.1.100:5555

# 验证连接
adb devices
# 应显示：192.168.1.100:5555    device

# 鸿蒙设备 - 通过 WiFi 连接
hdc tconn 192.168.1.100:5555

# 验证连接
hdc list targets
# 应显示：192.168.1.100:5555
```

### 设备管理命令

#### Android 设备（ADB）

```bash
# 列出所有已连接设备
adb devices

# 连接远程设备
adb connect 192.168.1.100:5555

# 断开指定设备
adb disconnect 192.168.1.100:5555

# 指定设备执行任务
python main.py --device-id 192.168.1.100:5555 --base-url http://localhost:8000/v1 --model "autoglm-phone-9b" "打开抖音刷视频"
```

#### 鸿蒙设备（HDC）

```bash
# 列出所有已连接设备
hdc list targets

# 连接远程设备
hdc tconn 192.168.1.100:5555

# 断开指定设备
hdc tdisconn 192.168.1.100:5555

# 指定设备执行任务
python main.py --device-type hdc --device-id 192.168.1.100:5555 --base-url http://lo

# FILE: README_coding_agent.md

# Open-AutoGLM Quick Start for Coding Agent

<div align="center">
<img src=resources/logo.svg width="20%"/>
</div>

> **本文专为 AI 助手（如 Claude Code）阅读，用于自动化部署 Open-AutoGLM。**
>
> **This document is designed for AI assistants (such as Claude Code) to automate the deployment of Open-AutoGLM.**
>
> 如果你是人类读者，可以跳过本文，按照 README.md 文档操作即可。
>
> If you are a human reader, you can skip this document and follow the README.md instructions instead.

---

## Table of Contents / 目录

- [English](#english)
- [中文](#中文)

---

# English

## Prerequisites

### 1. Python Environment

Python 3.10 or higher is required.

### 2. ADB (Android Debug Bridge)

1. Download the official ADB [installation package](https://developer.android.com/tools/releases/platform-tools)
2. Extract and configure environment variables:

**macOS:**

```bash
# Assuming extracted to ~/Downloads/platform-tools
export PATH=${PATH}:~/Downloads/platform-tools
```

**Windows:** Add the extracted folder path to your system PATH. Refer to [this tutorial](https://blog.csdn.net/x2584179909/article/details/108319973) if needed.

### 3. Android Device Setup

Requirements:
- Android 7.0+ device or emulator
- Developer Mode enabled
- USB Debugging enabled

**Enable Developer Mode:**
1. Go to `Settings > About Phone > Build Number`
2. Tap rapidly about 10 times until "Developer mode enabled" appears

**Enable USB Debugging:**
1. Go to `Settings > Developer Options > USB Debugging`
2. Enable the toggle
3. Some devices may require a restart

**Important permissions to check:**

![Permissions](resources/screenshot-20251210-120416.png)

### 4. Install ADB Keyboard

Download and install [ADB Keyboard APK](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk) on your device.

After installation, enable it in `Settings > Input Method` or `Settings > Keyboard List`.

---

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Install package
pip install -e .
```

---

## ADB Configuration

**Ensure your USB cable supports data transfer (not charging only).**

### Verify Connection

```bash
# Check connected devices
adb devices

# Expected output:
# List of devices attached
# emulator-5554   device
```

### Remote Debugging (WiFi)

Ensure your phone and computer are on the same WiFi network.

![Enable Wireless Debugging](resources/screenshot-20251210-120630.png)

```bash
# Connect via WiFi (replace with your phone's IP and port)
adb connect 192.168.1.100:5555

# Verify connection
adb devices
```

### Device Management

```bash
# List all devices
adb devices

# Connect remote device
adb connect <ip>:<port>

# Disconnect device
adb disconnect <ip>:<port>
```

---

## Usage

### Command Line

```bash
# Interactive mode
python main.py --base-url <MODEL_API_URL> --model <MODEL_NAME>

# Execute specific task
python main.py --base-url <MODEL_API_URL> "Open Chrome browser"

# Use API key authentication
python main.py --apikey sk-xxxxx

# English system prompt
python main.py --lang en --base-url <MODEL_API_URL> "Open Chrome browser"

# List supported apps
python main.py --list-apps

# Specify device
python main.py --device-id 192.168.1.100:5555 --base-url <MODEL_API_URL> "Open TikTok"
```

### Python API

```python
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig

# Configure model
model_config = ModelConfig(
    base_url="<MODEL_API_URL>",
    model_name="<MODEL_NAME>",
)

# Create Agent
agent = PhoneAgent(model_config=model_config)

# Execute task
result = agent.run("Open eBay and search for wireless earbuds")
print(result)
```

---

## Environment Variables

| Variable                  | Description               | Default                      |
|---------------------------|---------------------------|------------------------------|
| `PHONE_AGENT_BASE_URL`    | Model API URL             | `http://localhost:8000/v1`   |
| `PHONE_AGENT_MODEL`       | Model name                | `autoglm-phone-9b`           |
| `PHONE_AGENT_API_KEY`     | API key                   | `EMPTY`                      |
| `PHONE_AGENT_MAX_STEPS`   | Max steps per task        | `100`                        |
| `PHONE_AGENT_DEVICE_ID`   | ADB device ID             | (auto-detect)                |
| `PHONE_AGENT_LANG`        | Language (`cn`/`en`)      | `cn`                         |

---

## Troubleshooting

### Device Not Found

```bash
adb kill-server
adb start-server
adb devices
```

Check:
1. USB debugging enabled
2. USB cable supports data transfer
3. Authorization popup approved on phone
4. Try different USB port/cable

### Can Open Apps but Cannot Tap

Enable both in `Settings > Developer Options`:
- **USB Debugging**
- **USB Debugging (Security Settings)**

### Text Input Not Working

1. Ensure ADB Keyboard is installed
2. Enable in `Settings > System > Language & Input > Virtual Keyboard`

### Windows Encoding Issues

Add environment variable before running:

```bash
PYTHONIOENCODING=utf-8 python main.py ...
```

---

# 中文

## 环境要求

### 1. Python 环境

需要 Python 3.10 及以上版本。

### 2. ADB (Android Debug Bridge)

1. 下载官方 ADB [安装包](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)
2. 解压并配置环境变量：

**macOS:**

```bash
# 假设解压到 ~/Downloads/platform-tools
export PATH=${PATH}:~/Downloads/platform-tools
```

**Windows:** 将解压后的文件夹路径添加到系统 PATH。可参考[此教程](https://blog.csdn.net/x2584179909/article/details/108319973)。

### 3. 安卓设备配置

要求：
- Android 7.0+ 设备或模拟器
- 开发者模式已启用
- USB 调试已启用

**启用开发者模式：**
1. 进入 `设置 > 关于手机 > 版本号`
2. 连续快速点击约 10 次，直到提示"开发者模式已启用"

**启用 USB 调试：**
1. 进入 `设置 > 开发者选项 > USB 调试`
2. 开启开关
3. 部分设备可能需要重启

**请务必检查以下权限：**

![权限](resources/screenshot-20251209-181423.png)

### 4. 安装 ADB Keyboard

在设备上下载并安装 [ADB Keyboard APK](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk)。

安装后，在 `设置 > 输入法` 或 `设置 > 键盘列表` 中启用。

---

## 安装

```bash
# 安装依赖
pip install -r requirements.txt

# 安装包
pip install -e .
```

---

## ADB 配置

**请确保 USB 数据线支持数据传输（而非仅充电）。**

### 验证连接

```bash
# 检查已连接设备
adb devices

# 预期输出：
# List of devices attached
# emulator-5554   device
```

### 远程调试（WiFi）

确保手机和电脑在同一 WiFi 网络中。

![开启无线调试](resources/setting.png)

```bash
# 通过 WiFi 连接（替换为手机显示的 IP 和端口）
adb connect 192.168.1.100:5555

# 验证连接
adb devices
```

### 设备管理

```bash
# 列出所有设备
adb devices

# 连接远程设备
adb connect <ip>:<port>

# 断开设备
adb disconnect <ip>:<port>
```

---

## 使用方法

### 命令行

```bash
# 交互模式
python main.py --base-url <模型API地址> --model <模型名称>

# 执行指定任务
python main.py --base-url <模型API地址> "打开美团搜索附近的火锅店"

# 使用 API Key 认证
python main.py --apikey sk-xxxxx

# 使用英文系统提示词
python main.py --lang en --base-url <模型API地址> "Open Chrome browser"

# 列出支持的应用
python main.py --list-apps

# 指定设备
python main.py --device-id 192.168.1.100:5555 --base-url <模型API地址> "打开抖音刷视频"
```

### Python API

```python
from phone_agent import PhoneAgent
from phone_agent.model import ModelConfig

# 配置模型
model_config = ModelConfig(
    base_url="<模型API地址>",
    model_name="<模型名称>",
)

# 创建 Agent
agent = PhoneAgent(model_config=model_config)

# 执行任务
result = agent.run("打开淘宝搜索无线耳机")
print(result)
```

---

## 环境变量

| 变量                        | 描述               | 默认值                        |
|---------------------------|------------------|----------------------------|
| `PHONE_AGENT_BASE_URL`    | 模型 API 地址        | `http://localhost:8000/v1` |
| `PHONE_AGENT_MODEL`       | 模型名称             | `autoglm-phone-9b`         |
| `PHONE_AGENT_API_KEY`     | API Key          | `EMPTY`                    |
| `PHONE_AGENT_MAX_STEPS`   | 每个任务最大步数         | `100`                      |
| `PHONE_AGENT_DEVICE_ID`   | ADB 设备 ID        | (自动检测)                     |
| `PHONE_AGENT_LANG`        | 语言 (`cn`/`en`)   | `cn`                       |

---

## 常见问题

### 设备未找到

```bash
adb kill-server
adb start-server
adb devices
```

检查：
1. USB 调试是否已开启
2. 数据线是否支持数据传输
3. 手机上的授权弹窗是否已点击「允许」
4. 尝试更换 USB 接口或数据线

### 能打开应用但无法点击

在 `设置 > 开发者选项` 中同时启用：
- **USB 调试**
- **USB 调试（安全设置）**

### 文本输入不工作

1. 确保已安装 ADB Keyboard
2. 在 `设置 > 系统 > 语言和输入法 > 虚拟键盘` 中启用

### Windows 编码异常

运行代码前添加环境变量：

```bash
PYTHONIOENCODING=utf-8 python main.py ...
```

---

## License

This project is for research and learning purposes only. See [Terms of Use](resources/privacy_policy.txt) / [使用条款](resources/privacy_policy.txt).


# FILE: README_en.md

# Open-AutoGLM

[中文阅读.](./README.md)

<div align="center">
<img src=resources/logo.svg width="20%"/>
</div>
<p align="center">
    👋 Join our<a href="resources/WECHAT.md" target="_blank"> Wechat</a> or <a href="https://discord.gg/HvT5BaPg3H" target="_blank">Discord</a> community.
</p>
<p align="center">
    👋 Follow AutoGLM Autotyper <a href="https://x.com/Autotyper_Agent?s=20" target="_blank">X</a> account
</p>

## Quick Start

You can use Claude Code with [GLM Coding Plan](https://z.ai/subscribe) and enter the following prompt to quickly deploy this project:

```
Access the documentation and install AutoGLM for me
https://raw.githubusercontent.com/zai-org/Open-AutoGLM/refs/heads/main/README_en.md
```

## Project Introduction

Phone Agent is a mobile intelligent assistant framework built on AutoGLM. It understands phone screen content in a multimodal manner and helps users complete tasks through automated operations. The system controls devices via ADB (Android Debug Bridge), perceives screens using vision-language models, and generates and executes operation workflows through intelligent planning. Users simply describe their needs in natural language, such as "Open eBay and search for wireless earphones." and Phone Agent will automatically parse the intent, understand the current interface, plan the next action, and complete the entire workflow. The system also includes a sensitive operation confirmation mechanism and supports manual takeover during login or verification code scenarios. Additionally, it provides remote ADB debugging capabilities, allowing device connection via WiFi or network for flexible remote control and development.

> ⚠️ This project is for research and learning purposes only. It is strictly prohibited to use for illegal information acquisition, system interference, or any illegal activities. Please carefully review the [Terms of Use](resources/privacy_policy_en.txt).

## Integration with Other Automation Tools

### Midscene.js

[Midscene.js](https://midscenejs.com/en/index.html) is an open-source, vision-model-driven UI automation SDK that supports JavaScript or YAML flow syntax for cross-platform automation.

Midscene.js already supports AutoGLM; see the [Midscene.js integration guide](https://midscenejs.com/model-common-config.html#auto-glm) to quickly try AutoGLM automation on both iOS and Android devices.

## Model Download Links

| Model             | Download Links                                                                                                                                             |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoGLM-Phone-9B  | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B)               |
| AutoGLM-Phone-9B-Multilingual | [🤗 Hugging Face](https://huggingface.co/zai-org/AutoGLM-Phone-9B-Multilingual)<br>[🤖 ModelScope](https://modelscope.cn/models/ZhipuAI/AutoGLM-Phone-9B-Multilingual) |

`AutoGLM-Phone-9B` is optimized for Chinese mobile applications, while `AutoGLM-Phone-9B-Multilingual` supports English scenarios and is suitable for applications containing English or other language content.

## Environment Setup

### 1. Python Environment

Python 3.10 or higher is recommended.

### 2. Device Debug Tools

Choose the appropriate tool based on your device type:

#### For Android Devices - Using ADB

1. Download the official ADB [installation package](https://developer.android.com/tools/releases/platform-tools) and extract it to a custom path
2. Configure environment variables

- MacOS configuration: In `Terminal` or any command line tool

  ```bash
  # Assuming the extracted directory is ~/Downloads/platform-tools. Adjust the command if different.
  export PATH=${PATH}:~/Downloads/platform-tools
  ```

- Windows configuration: Refer to [third-party tutorials](https://blog.csdn.net/x2584179909/article/details/108319973) for configuration.

#### For HarmonyOS Devices - Using HDC

1. Download HDC tool:
   - From [HarmonyOS SDK](https://developer.huawei.com/consumer/en/download/)
2. Configure environment variables

- MacOS/Linux configuration:

  ```bash
  # Assuming the extracted directory is ~/Downloads/harmonyos-sdk/toolchains. Adjust according to actual path.
  export PATH=${PATH}:~/Downloads/harmonyos-sdk/toolchains
  ```

- Windows configuration: Add the HDC tool directory to the system PATH environment variable

### 3. Android 7.0+ or HarmonyOS Device with `Developer Mode` and `USB Debugging` Enabled

1. Enable Developer Mode: The typical method is to find `Settings > About Phone > Build Number` and tap it rapidly about 10 times until a popup shows "Developer mode has been enabled." This may vary slightly between phones; search online for tutorials if you can't find it.
2. Enable USB Debugging: After enabling Developer Mode, go to `Settings > Developer Options > USB Debugging` and enable it
3. Some devices may require a restart after setting developer options for them to take effect. You can test by connecting your phone to your computer via USB cable and running `adb devices` to see if device information appears. If not, the connection has failed.

**Please carefully check the relevant permissions**

![Permissions](resources/screenshot-20251210-120416.png)

### 4. Install ADB Keyboard (Required for Android Devices Only, for Text Input)

**Note: HarmonyOS devices use native input methods and do not require ADB Keyboard.**

If you are using an Android device:

Download the [installation package](https://github.com/senzhk/ADBKeyBoard/blob/master/ADBKeyboard.apk) and install it on the corresponding Android device.
Note: After installation, you need to enable `ADB Keyboard` in `Settings > Input Method` or `Settings > Keyboard List` for it to work.(or use command `adb shell ime enable com.android.adbkeyboard/.AdbIME`[How-to-use](https://github.com/senzhk/ADBKeyBoard/blob/master/README.md#how-to-use))

## Deployment Preparation

### 1. Install Dependencies

```bash
pip install -r requirements.txt 
pip install -e .
```

### 2. Configure ADB or HDC

#### For Android Devices

Make sure your **USB cable supports data transfer**, not just charging.

Ensure ADB is installed and connect the device via **USB cable**:

```bash
# Check connected devices
adb devices

# Output should show your device, e.g.:
# List of devices attached
# emulator-5554   device
```

#### For HarmonyOS Devices

Make sure your **USB cable supports data transfer**, not just charging.

Ensure HDC is installed and connect the device via **USB cable**:

```bash
# Check connected devices
hdc list targets

# Output should show your device, e.g.:
# 7001005458323933328a01bce01c2500
```

### 3. Start Model Service

You can choose to deploy the model service yourself or use a third-party model service provider.

#### Option A: Use Third-Party Model Services

If you don't want to deploy the model yourself, you can use the following third-party services that have already deployed our model:

**1. z.ai**

- Documentation: https://docs.z.ai/api-reference/introduction
- `--base-url`: `https://api.z.ai/api/paas/v4`
- `--model`: `autoglm-phone-multilingual`
- `--apikey`: Apply for your own API key on the z.ai platform

**2. Novita AI**

- Documentation: https://novita.ai/models/model-detail/zai-org-autoglm-phone-9b-multilingual
- `--base-url`: `https://api.novita.ai/openai`
- `--model`: `zai-org/autoglm-phone-9b-multilingual`
- `--apikey`: Apply for your own API key on the Novita AI platform

**3. Parasail**

- Documentation: https://www.saas.parasail.io/serverless?name=auto-glm-9b-multilingual
- `--base-url`: `https://api.parasail.io/v1`
- `--model`: `parasail-auto-glm-9b-multilingual`
- `--apikey`: Apply for your own API key on the Parasail platform

Example usage with third-party services:

```bash
# Using z.ai
python main.py --base-url https://api.z.ai/api/paas/v4 --model "autoglm-phone-multilingual" --apikey "your-z-ai-api-key" "Open Chrome browser"

# Using Novita AI
python main.py --base-url https://api.novita.ai/openai --model "zai-org/autoglm-phone-9b-multilingual" --apikey "your-novita-api-key" "Open Chrome browser"

# Using Parasail
python main.py --base-url https://api.parasail.io/v1 --model "parasail-auto-glm-9b-multilingual" --apikey "your-parasail-api-key" "Open Chrome browser"
```

#### Option B: Deploy Model Yourself

If you prefer to deploy the model locally or on your own server:

1. Download the model and install the inference engine framework according to the `For Model Deployment` section in `requirements.txt`.
2. Start via SGlang / vLLM to get an OpenAI-format service. Here's a vLLM deployment solution; please strictly follow the startup parameters we provide:

- vLLM:

```shell
python3 -m vllm.entrypoints.openai.api_server \
 --served-model-name autoglm-phone-9b-multilingual \
 --allowed-local-media-path /   \
 --mm-encoder-tp-mode data \
 --mm_processor_cache_type shm \
 --mm_processor_kwargs "{\"max_pixels\":5000000}" \
 --max-model-len 25480  \
 --chat-template-content-format string \
 --limit-mm-per-prompt "{\"image\":10}" \
 --model zai-org/AutoGLM-Phone-9B-Multilingual \
 --port 8000
```

- This model has the same architecture as `GLM-4.1V-9B-Thinking`. For detailed information about model deployment, you can also check [GLM-V](https://github.com/zai-org/GLM-V) for model deployment and usage guides.

- After successful startup, the model service will be accessible at `http://localhost:8000/v1`. If you deploy the model on a remote server, access it using that server's IP address.

### 4. Check Model Deployment

After starting the model service, you can use the following command to verify the deployment:

```bash
python scripts/check_deployment_en.py --base-url http://localhost:8000/v1 --model autoglm-phone-9b-multilingual
```

If using a th

# FILE: docs/ios_setup/ios_setup.md

# iOS 环境配置指南

本文档介绍如何为 Open-AutoGLM 配置 iOS 设备环境。

## 环境要求

- macOS 操作系统
- Xcode（最新版本，在App store中下载）
- 苹果开发者账号（免费账号即可，无需付费）
- iOS 设备（iPhone/iPad）
- USB 数据线或同一 WiFi 网络


## WebDriverAgent 配置

WebDriverAgent 是 iOS 自动化的核心组件，需要在 iOS 设备上运行。

### 1. 克隆 WebDriverAgent

```bash
git clone https://github.com/appium/WebDriverAgent.git
cd WebDriverAgent
```

直接点击`WebDriverAgent.xcodeproj`即可使用Xcode打开。

### 2. 设置 Signing & Capabilities

1. 在 Xcode 中选中 `WebDriverAgent`，出现General、Signing&Capabilities等选项。
2. 进入 `Signing & Capabilities` 选项卡
3.   勾选 `Automatically manage signing`。在Team中选择自己的开发者账号
4. 将 Bundle ID 改为唯一标识符，例如：`com.yourname.WebDriverAgentRunner`
![设置签名1](resources/ios0_WebDriverAgent0.png)

5. TARGETS中，建议将WebDriverAgentLib、WebDriverAgentRunner、IntegrationApp的`Signing & Capabilities` 都按照相同方式设置。
![设置签名1](resources/ios0_WebDriverAgent1.png)

### 3. 测试XCode的GUI模式和UI自动化设置

建议先测试GUI模式能否成功安装WebDriverAgent，再进行后续步骤。
Mac和iPhone有USB和WiFi两种连接方式，建议通过USB方式，成功率更高。

#### 通过 WiFi 连接

需要满足以下条件：
1.  通过USB连接。在Finder中选中连接的IPhone，在“通用”中勾选"在 WiFi 中显示这台 iPhone"
2. Mac 与 iPhone 处于同一 WiFi 网络之下

#### 具体步骤
1. 从项目 Target 选择 `WebDriverAgentRunner`
2. 选择你的设备

![选择设备](resources/select-your-iphone-device.png)

3. 长按"▶️"运行按钮，选择 "Test" 后开始编译并部署到你的 iPhone 上

![开始测试](resources/start-wda-testing.png)

部署成功的标志：1. XCode没有报错。2. 你可以在iPhone上找到名为WebDriverAgentRunner的App

#### 设备信任配置

首次运行时，需要在 iPhone 上完成以下设置，然后重新编译和部署：

1. **输入解锁密码**
2. **信任开发者应用**
   - 进入：设置 → 通用 → VPN与设备管理
   - 在“开发者 App”中选择对应开发者
   - 点击信任“XXX”

   ![信任设备](resources/trust-dev-app.jpg)

3. **启用 UI 自动化**
   - 进入：设置 → 开发者
   - 打开 UI 自动化设置

   ![启用UI自动化](resources/enable-ui-automation.jpg)

### 4. XCode命令行模式部署

1.安装libimobiledevice，用于与 iPhone / iPad 建立连接与通信。

```
brew install libimobiledevice
# 设备检查
idevice_id -ln
```
2.使用xcodebuild安装WebAgent。命令行也需要进行“设备信任配置”，参考GUI模式下的方法。

```
cd WebDriverAgent

xcodebuild -project WebDriverAgent.xcodeproj \
           -scheme WebDriverAgentRunner \
           -destination 'platform=iOS,name=YOUR_PHONE_NAME' \
           test
```
这里，YOUR_PHONE_NAME可以在xcode的GUI中看到。
WebDriverAgent 成功运行后，会在 Xcode 控制台输出类似以下信息：

```
ServerURLHere->http://[设备IP]:8100<-ServerURLHere
```

同时，观察到手机上安装好了WebDriverAgentRunner，屏幕显示Automation Running字样。
其中，**http://[设备IP]:8100**为WiFi所需的WDA_URL。

## 使用 AutoGLM

以上配置完成后，先打开一个新终端，在后台建立端口映射（使用WiFi连接则不需要）：

```bash
 iproxy 8100 8100
```

之后，打开一个新终端，通过以下命令使用AutoGLM（WiFi则使用上述获得的WDA_URL）：

```bash
python ios.py --base-url "YOUR_BASE_URL" \
    --model  "autoglm-phone" \
    --api-key "YOUR_API_KEY" \
    --wda-url http://localhost:8100 \
    "TASK"
```

## 参考资源

- [WebDriverAgent 官方仓库](https://github.com/appium/WebDriverAgent)
- [PR141](https://github.com/zai-org/Open-AutoGLM/pull/141)
- [Gekowa提供的ios方案](https://github.com/gekowa/Open-AutoGLM/tree/ios-support)

---

如有其他问题，请参考主项目 README 或提交 Issue。


# FILE: examples/basic_usage.py

#!/usr/bin/env python3
"""
Phone Agent Usage Examples / Phone Agent 使用示例

Demonstrates how to use Phone Agent for phone automation tasks via Python API.
演示如何通过 Python API 使用 Phone Agent 进行手机自动化任务。
"""

from phone_agent import PhoneAgent
from phone_agent.agent import AgentConfig
from phone_agent.config import get_messages
from phone_agent.model import ModelConfig


def example_basic_task(lang: str = "cn"):
    """Basic task example / 基础任务示例"""
    msgs = get_messages(lang)

    # Configure model endpoint
    model_config = ModelConfig(
        base_url="http://localhost:8000/v1",
        model_name="autoglm-phone-9b",
        temperature=0.1,
    )

    # Configure Agent behavior
    agent_config = AgentConfig(
        max_steps=50,
        verbose=True,
        lang=lang,
    )

    # Create Agent
    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    # Execute task
    result = agent.run("打开小红书搜索美食攻略")
    print(f"{msgs['task_result']}: {result}")


def example_with_callbacks(lang: str = "cn"):
    """Task example with callbacks / 带回调的任务示例"""
    msgs = get_messages(lang)

    def my_confirmation(message: str) -> bool:
        """Sensitive operation confirmation callback / 敏感操作确认回调"""
        print(f"\n[{msgs['confirmation_required']}] {message}")
        response = input(f"{msgs['continue_prompt']}: ")
        return response.lower() in ("yes", "y", "是")

    def my_takeover(message: str) -> None:
        """Manual takeover callback / 人工接管回调"""
        print(f"\n[{msgs['manual_operation_required']}] {message}")
        print(msgs["manual_operation_hint"])
        input(f"{msgs['press_enter_when_done']}: ")

    # Create Agent with custom callbacks
    agent_config = AgentConfig(lang=lang)
    agent = PhoneAgent(
        agent_config=agent_config,
        confirmation_callback=my_confirmation,
        takeover_callback=my_takeover,
    )

    # Execute task that may require confirmation
    result = agent.run("打开淘宝搜索无线耳机并加入购物车")
    print(f"{msgs['task_result']}: {result}")


def example_step_by_step(lang: str = "cn"):
    """Step-by-step execution example (for debugging) / 单步执行示例（用于调试）"""
    msgs = get_messages(lang)

    agent_config = AgentConfig(lang=lang)
    agent = PhoneAgent(agent_config=agent_config)

    # Initialize task
    result = agent.step("打开美团搜索附近的火锅店")
    print(f"{msgs['step']} 1: {result.action}")

    # Continue if not finished
    while not result.finished and agent.step_count < 10:
        result = agent.step()
        print(f"{msgs['step']} {agent.step_count}: {result.action}")
        print(f"  {msgs['thinking']}: {result.thinking[:100]}...")

    print(f"\n{msgs['final_result']}: {result.message}")


def example_multiple_tasks(lang: str = "cn"):
    """Batch task example / 批量任务示例"""
    msgs = get_messages(lang)

    agent_config = AgentConfig(lang=lang)
    agent = PhoneAgent(agent_config=agent_config)

    tasks = [
        "打开高德地图查看实时路况",
        "打开大众点评搜索附近的咖啡店",
 

# FILE: examples/demo_thinking.py

#!/usr/bin/env python3
"""
Thinking Output Demo / 演示 thinking 输出的示例

This script demonstrates how the Agent outputs both thinking process and actions in verbose mode.
这个脚本展示了在 verbose 模式下，Agent 会同时输出思考过程和执行动作。
"""

from phone_agent import PhoneAgent
from phone_agent.agent import AgentConfig
from phone_agent.config import get_messages
from phone_agent.model import ModelConfig


def main(lang: str = "cn"):
    msgs = get_messages(lang)

    print("=" * 60)
    print("Phone Agent - Thinking Demo")
    print("=" * 60)

    # Configure model
    model_config = ModelConfig(
        base_url="http://localhost:8000/v1",
        model_name="autoglm-phone-9b",
        temperature=0.1,
    )

    # Configure Agent (verbose=True enables detailed output)
    agent_config = AgentConfig(
        max_steps=10,
        verbose=True,
        lang=lang,
    )

    # Create Agent
    agent = PhoneAgent(
        model_config=model_config,
        agent_config=agent_config,
    )

    # Execute task
    print(f"\n📱 {msgs['starting_task']}...\n")
    result = agent.run("打开小红书搜索美食攻略")

    print("\n" + "=" * 60)
    print(f"📊 {msgs['final_result']}: {result}")
    print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Phone Agent Thinking Demo")
    parser.add_argument(
        "--lang",
        type=str,
        default="cn",
        choices=["cn", "en"],
        help="Language for UI messages (cn=Chinese, en=English)",
    )
    args = parser.parse_args()

    main(lang=args.lang)

