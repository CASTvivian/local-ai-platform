# Missing Repo Summary Source: bytedance/deer-flow

- URL: https://github.com/bytedance/deer-flow
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/bytedance__deer-flow
- Clone Status: cloned
- Language: Python
- Stars: 67192
- Topics: agent, agentic, agentic-framework, agentic-workflow, ai, ai-agents, deep-research, harness, langchain, langgraph, langmanus, llm, multi-agent, nodejs, podcast, python, superagent, typescript
- Description: An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.

## Extracted README / Docs / Examples



# FILE: README_ja.md

# 🦌 DeerFlow - 2.0

[English](./README.md) | [中文](./README_zh.md) | 日本語 | [Français](./README_fr.md) | [Русский](./README_ru.md)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
> 2026年2月28日、バージョン2のリリースに伴い、DeerFlowはGitHub Trendingで🏆 第1位を獲得しました。素晴らしいコミュニティの皆さん、ありがとうございます！💪🔥

DeerFlow（**D**eep **E**xploration and **E**fficient **R**esearch **Flow**）は、**サブエージェント**、**メモリ**、**サンドボックス**を統合し、**拡張可能なスキル**によってあらゆるタスクを実行できるオープンソースの**スーパーエージェントハーネス**です。

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0はゼロからの完全な書き直しです。** v1とコードを共有していません。オリジナルのDeep Researchフレームワークをお探しの場合は、[`1.x`ブランチ](https://github.com/bytedance/deer-flow/tree/main-1.x)で引き続きメンテナンスされています。現在の開発は2.0に移行しています。

## 公式ウェブサイト

[<img width="2880" height="1600" alt="image" src="https://github.com/user-attachments/assets/a598c49f-3b2f-41ea-a052-05e21349188a" />](https://deerflow.tech)

**実際のデモ**は[**公式ウェブサイト**](https://deerflow.tech)でご覧いただけます。

## ByteDance Volcengine のコーディングプラン

<img width="4808" height="2400" alt="英文方舟" src="https://github.com/user-attachments/assets/2ecc7b9d-50be-4185-b1f7-5542d222fb2d" />

- DeerFlowの実行には、Doubao-Seed-2.0-Code、DeepSeek v3.2、Kimi 2.5の使用を強く推奨します
- [詳細はこちら](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [中国大陸の開発者はこちらをクリック](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

DeerFlowは、BytePlusが独自に開発したインテリジェント検索・クローリングツールセット「[InfoQuest（無料オンライン体験対応）](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)」を新たに統合しました。

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"   alt="InfoQuest_banner"
  />
</a>

---

## 目次

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [公式ウェブサイト](#公式ウェブサイト)
  - [InfoQuest](#infoquest)
  - [目次](#目次)
  - [Coding Agent に一文でセットアップを依頼](#coding-agent-に一文でセットアップを依頼)
  - [クイックスタート](#クイックスタート)
    - [設定](#設定)
    - [アプリケーションの実行](#アプリケーションの実行)
      - [オプション1: Docker（推奨）](#オプション1-docker推奨)
      - [オプション2: ローカル開発](#オプション2-ローカル開発)
    - [詳細設定](#詳細設定)
      - [サンドボックスモード](#サンドボックスモード)
      - [MCPサーバー](#mcpサーバー)
      - [IMチャネル](#imチャネル)
      - [LangSmithトレーシング](#langsmithトレーシング)
  - [Deep Researchからスーパーエージェントハーネスへ](#deep-researchからスーパーエージェントハーネスへ)
  - [コア機能](#コア機能)
    - [スキルとツール](#スキルとツール)
      - [Claude Code連携](#claude-code連携)
    - [サブエージェント](#サブエージェント)
    - [サンドボックスとファイルシステム](#サンドボックスとファイルシステム)
    - [コンテキストエンジニアリング](#コンテキストエンジニアリング)
    - [長期メモリ](#長期メモリ)
  - [推奨モデル](#推奨モデル)
  - [組み込みPythonクライアント](#組み込みpythonクライアント)
  - [ドキュメント](#ドキュメント)
  - [⚠️ セキュリティに関する注意](#️-セキュリティに関する注意)
  - [コントリビュート](#コントリビュート)
  - [ライセンス](#ライセンス)
  - [謝辞](#謝辞)
    - [主要コントリビューター](#主要コントリビューター)
  - [Star History](#star-history)

## Coding Agent に一文でセットアップを依頼

Claude Code、Codex、Cursor、Windsurf などの coding agent を使っているなら、次の一文をそのまま渡せます。

```text
DeerFlow がまだ clone されていなければ先に clone してから、https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md に従ってローカル開発環境を初期化してください
```

このプロンプトは coding agent 向けです。必要なら先にリポジトリを clone し、Docker が使える場合は Docker を優先して初期セットアップを行い、最後に次の起動コマンドと不足している設定項目だけを返します。

## クイックスタート

### 設定

1. **DeerFlowリポジトリをクローン**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **ローカル設定ファイルの生成**

   プロジェクトルートディレクトリ（`deer-flow/`）から以下を実行します：

   ```bash
   make config
   ```

   このコマンドは、提供されたテンプレートに基づいてローカル設定ファイルを作成します。

3. **使用するモデルの設定**

   `config.yaml`を編集し、少なくとも1つのモデルを定義します：

   ```yaml
   models:
     - name: gpt-4                       # 内部識別子
       display_name: GPT-4               # 表示名
       use: langchain_openai:ChatOpenAI  # LangChainクラスパス
       model: gpt-4                      # API用モデル識別子
       api_key: $OPENAI_API_KEY          # APIキー（推奨：環境変数を使用）
       max_tokens: 4096                  # リクエストあたりの最大トークン数
       temperature: 0.7                  # サンプリング温度

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENAI_API_KEY          # OpenRouterもここではOpenAI互換のフィールド名を使用
       base_url: https://openrouter.ai/api/v1
   ```

   OpenRouterやOpenAI互換のゲートウェイは、`langchain_openai:ChatOpenAI`と`base_url`で設定します。プロバイダー固有の環境変数名を使用したい場合は、`api_key`でその変数を明示的に指定してください（例：`api_key: $OPENROUTER_API_KEY`）。

4. **設定したモデルのAPIキーを設定**

   以下のいずれかの方法を選択してください：

- オプションA：プロジェクトルートの`.env`ファイルを編集（推奨）

   ```bash
   TAVILY_API_KEY=your-tavily-api-key
   OPENAI_API_KEY=your-openai-api-key
   # OpenRouterもlangchain_openai:ChatOpenAI + base_url使用時はOPENAI_API_KEYを使用します。
   # 必要に応じて他のプロバイダーキーを追加
   INFOQUEST_API_KEY=your-infoquest-api-key
   ```

- オプションB：シェルで環境変数をエクスポート

   ```bash
   export OPENAI_API_KEY=your-openai-api-key
   ```

- オプションC：`config.yaml`を直接編集（本番環境には非推奨）

   ```yaml
   models:
     - name: gpt-4
       api_key: your-actual-api-key-here  # プレースホルダーを置換
   ```

### アプリケーションの実行

#### オプション1: Docker（推奨）

**開発環境**（ホットリロード、ソースマウント）：

```bash
make docker-init    # サンドボックスイメージをプル（初回またはイメージ更新時のみ）
make docker-start   # サービスを開始（config.yamlからサンドボックスモードを自動検出）
```

`make docker-start`は、`config.yaml`がプロビジョナーモード（`sandbox.use: deerflow.community.aio_sandbox:AioSandboxProvider`と`provisioner_url`）を使用している場合にのみ`provisioner`を起動します。

**本番環境**（ローカルでイメージをビルドし、ランタイム設定とデータをマウント）：

```bash
make up     # イメージをビルドして全本番サービスを開始
make down   # コンテナを停止して削除
```

> [!NOTE]
> Agentランタイムは現在Gateway内で実行されます。`/api/langgraph/*`はnginxによってGatewayのLangGraph-compatible APIへ書き換えられます。

アクセス: http://localhost:2026

詳細なDocker開発ガイドは[CONTRIBUTING.md](CONTRIBUTING.md)をご覧ください。

#### オプション2: ローカル開発

サービスをローカルで実行する場合：

前提条件：上記の「設定」手順を先に完了してください（`make config`とモデルAPIキー）。`make dev`には有効な設定ファイルが必要です（デフォルトはプロジェクトルートの`config.yaml`。`DEER_FLOW_CONFIG_PATH`で上書き可能）。

1. **前提条件の確認**：
   ```bash
   make check  # Node.js 22+、pnpm、uv、nginxを検証
   ```

2. **依存関係のインストール**：
   ```bash
   make install  # バックエンド＋フロントエンドの依存関係をインストール
   ```

3. **（オプション）サンドボックスイメージの事前プル**：
   ```bash
   # Docker/コンテナベースのサンドボックス使用時に推奨
   make setup-sandbox
   ```

4. **サービスの開始**：
   ```bash
   make dev
   ```

5. **アクセス**: http://localhost:2026

### 詳細設定
#### サンドボックスモード

DeerFlowは複数のサンドボックス実行モードをサポートしています：
- **ローカル実行**（ホストマシン上で直接サンドボックスコードを実行）
- **Docker実行**（分離されたDockerコンテナ内でサンドボックスコードを実行）
- **KubernetesによるDocker実行**（プロビジョナーサービス経由でKubernetesポッドでサンドボックスコードを実行）

Docker開発では、サービスの起動は`config.yaml`のサンドボックスモードに従います。ローカル/Dockerモードでは`provisioner`は起動されません。

お好みのモードの設定については[サンドボックス設定ガイド](backend/docs/CONFIGURATION.md#sandbox)をご覧ください。

#### MCPサーバー

DeerFlowは、機能を拡張するための設定可能なMCPサーバーとスキルをサポートしています。
HTTP/SSE MCPサーバーでは、OAuthトークンフロー（`client_credentials`、`refresh_token`）がサポートされています。
詳細な手順は[MCPサーバーガイド](backend/docs/MCP_SERVER.md)をご覧ください。

#### IMチャネル

DeerFlowはメッセージングアプリからのタスク受信をサポートしています。チャネルは設定時に自動的に開始されます。いずれもパブリックIPは不要です。

| チャネル | トランスポート | 難易度 |
|---------|-----------|------------|
| Telegram | Bot API（ロングポーリング） | 簡単 |
| Slack | Socket Mode | 中程度 |
| Feishu / Lark | WebSocket | 中程度 |
| DingTalk | Stream Push（WebSocket） | 中程度 |

**`config.yaml`での設定：**

```yaml
channels:
  # LangGraph-compatible Gateway API base URL（デフォルト: http://localhost:8001/api）
  langgraph_url: http://localhost:8001/api
  # Gateway API URL（デフォルト: http://localhost:8001）
  gateway_url: http://localhost:8001

  # オプション: 全モバイルチャネルのグローバルセッションデフォルト
  session:
    assistant_id: lead_agent
    config:
      recursion_limit: 100
    context:
      thinking_enabled: true
      is_plan_mode: false
      subagent_enabled: false

  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
    # domain: https://open.feishu.cn       # China (default)
    # domain: https://open.larksuite.com   # International

  slack:
    enabled: true
    bot_token: $SLACK_BOT_TOKEN     # xoxb-...
    app_token: $SLACK_APP_TOKEN     # xapp-...（Socket Mode）
    allowed_users: []               # 空 = 全員許可

  telegram:
    enabled: true
    bot_token: $TELEGRAM_BOT_TOKEN
    allowed_users: []               # 空 = 全員許可

    # オプション: チャネル/ユーザーごとのセッション設定
    session:
      assistant_id: mobile_agent
      context:
        thinking_enabled: false
      users:
        "123456789":
          assistant_id: vip_agent
          config:
            recursion_limit: 150
          context:
            thinking_enabled: true
            subagent_enabled: true

  dingtalk:
    enabled: true
    client_id: $DINGTALK_CLIENT_ID             # DingTalk Open PlatformのClientId
    client_secret: $DINGTALK_CLIENT_SECRET     # DingTalk Open PlatformのClientSecret
    allowed_users: []                          # 空 = 全員許可
    card_template_id: ""                       # オプション：ストリーミングタイプライター効果用のAIカードテンプレートID
```

対応するAPIキーを`.env`ファイルに設定します：

```bash
# Telegram
TELEGRAM_BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrSTUvwxYZ

# Slack
SLACK_BOT_TOKEN=xoxb-...
SLACK_APP_TOKEN=xapp-...

# Feishu / Lark
FEISHU_APP_ID=cli_xxxx
FEISHU_APP_SECRET=your_app_secret

# DingTalk
DINGTALK_CLIENT_ID=your_client_id
DINGTALK_CLIENT_SECRET=your_client_secret
```

**Telegramのセットアップ**

1. [@BotFather](https://t.me/BotFather)とチャットし、`/newbot`を送信してHTTP APIトークンをコピーします。
2. `.env`に`TELEGRAM_BOT_TOKEN`を設定し、`config.yaml`でチャネルを有効にします。

**Slackのセットアップ**

1. [api.slack.com/apps](https://api.slack.com/apps)でSlackアプリを作成 → 新規アプリ作成 → 最初から作成。
2. **OAuth & Permissions**で、Botトークンスコープを追加：`

# FILE: README_ru.md

# 🦌 DeerFlow - 2.0

[English](./README.md) | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | Русский

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

> 28 февраля 2026 года DeerFlow занял 🏆 #1 в GitHub Trending после релиза версии 2. Спасибо огромное нашему сообществу — всё благодаря вам! 💪🔥

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) — open-source **Super Agent Harness**, который управляет **Sub-Agents**, **Memory** и **Sandbox** для решения почти любой задачи. Всё на основе расширяемых **Skills**.

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0 — проект переписан с нуля.** Общего кода с v1 нет. Если нужен оригинальный Deep Research фреймворк — он живёт в ветке [`1.x`](https://github.com/bytedance/deer-flow/tree/main-1.x), туда тоже принимают контрибьюты. Активная разработка идёт в 2.0.

## Официальный сайт

[<img width="2880" height="1600" alt="image" src="https://github.com/user-attachments/assets/a598c49f-3b2f-41ea-a052-05e21349188a" />](https://deerflow.tech)

Больше информации и живые демо на [**официальном сайте**](https://deerflow.tech).

## Coding Plan от ByteDance Volcengine

<img width="4808" height="2400" alt="英文方舟" src="https://github.com/user-attachments/assets/2ecc7b9d-50be-4185-b1f7-5542d222fb2d" />

- Рекомендуем Doubao-Seed-2.0-Code, DeepSeek v3.2 и Kimi 2.5 для запуска DeerFlow
- [Подробнее](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [Для разработчиков из материкового Китая](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

DeerFlow интегрирован с инструментарием для умного поиска и краулинга от BytePlus — [InfoQuest (есть бесплатный онлайн-доступ)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"
    alt="InfoQuest_banner"
  />
</a>

---

## Содержание

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [Официальный сайт](#официальный-сайт)
  - [InfoQuest](#infoquest)
  - [Содержание](#содержание)
  - [Установка одной фразой для coding agent](#установка-одной-фразой-для-coding-agent)
  - [Быстрый старт](#быстрый-старт)
    - [Конфигурация](#конфигурация)
    - [Запуск](#запуск)
      - [Вариант 1: Docker (рекомендуется)](#вариант-1-docker-рекомендуется)
      - [Вариант 2: Локальная разработка](#вариант-2-локальная-разработка)
    - [Дополнительно](#дополнительно)
      - [Режим Sandbox](#режим-sandbox)
      - [MCP-сервер](#mcp-сервер)
      - [Мессенджеры](#мессенджеры)
      - [Трассировка LangSmith](#трассировка-langsmith)
  - [От Deep Research к Super Agent Harness](#от-deep-research-к-super-agent-harness)
  - [Core Features](#core-features)
    - [Skills & Tools](#skills--tools)
      - [Интеграция с Claude Code](#интеграция-с-claude-code)
    - [Sub-Agents](#sub-agents)
    - [Sandbox & файловая система](#sandbox--файловая-система)
    - [Context Engineering](#context-engineering)
    - [Long-Term Memory](#long-term-memory)
  - [Рекомендуемые модели](#рекомендуемые-модели)
  - [Встроенный Python-клиент](#встроенный-python-клиент)
  - [Документация](#документация)
  - [⚠️ Безопасность](#️-безопасность)
  - [Участие в разработке](#участие-в-разработке)
  - [Лицензия](#лицензия)
  - [Благодарности](#благодарности)
    - [Ключевые контрибьюторы](#ключевые-контрибьюторы)
  - [История звёзд](#история-звёзд)

## Установка одной фразой для coding agent

Если вы используете Claude Code, Codex, Cursor, Windsurf или другой coding agent, просто отправьте ему эту фразу:

```text
Если DeerFlow еще не клонирован, сначала клонируй его, а затем подготовь локальное окружение разработки по инструкции https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md
```

Этот prompt предназначен для coding agent. Он просит агента при необходимости сначала клонировать репозиторий, предпочесть Docker, если он доступен, и в конце вернуть точную команду запуска и список недостающих настроек.

## Быстрый старт

### Конфигурация

1. **Склонировать репозиторий DeerFlow**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **Сгенерировать локальные конфиги**

   Из корня проекта (`deer-flow/`) запустите:

   ```bash
   make config
   ```

   Команда создаёт локальные конфиги на основе шаблонов.

3. **Настроить модель**

   Отредактируйте `config.yaml` и задайте хотя бы одну модель:

   ```yaml
   models:
     - name: gpt-4                       # Внутренний идентификатор
       display_name: GPT-4               # Отображаемое имя
       use: langchain_openai:ChatOpenAI  # Путь к классу LangChain
       model: gpt-4                      # Идентификатор модели для API
       api_key: $OPENAI_API_KEY          # API-ключ (рекомендуется: переменная окружения)
       max_tokens: 4096                  # Максимальное количество токенов на запрос
       temperature: 0.7                  # Температура сэмплирования

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENAI_API_KEY
       base_url: https://openrouter.ai/api/v1

     - name: gpt-5-responses
       display_name: GPT-5 (Responses API)
       use: langchain_openai:ChatOpenAI
       model: gpt-5
       api_key: $OPENAI_API_KEY
       use_responses_api: true
       output_version: responses/v1
   ```

   OpenRouter и аналогичные OpenAI-совместимые шлюзы настраиваются через `langchain_openai:ChatOpenAI` с параметром `base_url`. Для CLI-провайдеров:

   ```yaml
   models:
     - name: gpt-5.4
       display_name: GPT-5.4 (Codex CLI)
       use: deerflow.models.openai_codex_provider:CodexChatModel
       model: gpt-5.4
       supports_thinking: true
       supports_reasoning_effort: true

     - name: claude-sonnet-4.6
       display_name: Claude Sonnet 4.6 (Claude Code OAuth)
       use: deerflow.models.claude_provider:ClaudeChatModel
       model: claude-sonnet-4-6
       max_tokens: 4096
       supports_thinking: true
   ```

   - Codex CLI читает `~/.codex/auth.json`
   - Claude Code принимает `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_AUTH_TOKEN` или `~/.claude/.credentials.json`
   - На macOS при необходимости экспортируйте аутентификацию Claude Code явно:

   ```bash
   eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"
   ```

4. **Указать API-ключи**

   - **Вариант А**: файл `.env` в корне проекта (рекомендуется)

   ```bash
   TAVILY_API_KEY=your-tavily-api-key
   OPENAI_API_KEY=your-openai-api-key
   INFOQUEST_API_KEY=your-infoquest-api-key
   ```

   - **Вариант Б**: переменные окружения в терминале

   ```bash
   export OPENAI_API_KEY=your-openai-api-key
   ```

   - **Вариант В**: напрямую в `config.yaml` (не рекомендуется для продакшена)

### Запуск

#### Вариант 1: Docker (рекомендуется)

**Разработка** (hot-reload, монтирование исходников):

```bash
make docker-init    # Загрузить образ Sandbox (один раз или при обновлении)
make docker-start   # Запустить сервисы
```

**Продакшен** (собирает образы локально):

```bash
make up     # Собрать образы и запустить все сервисы
make down   # Остановить и удалить контейнеры
```

> [!TIP]
> На Linux при ошибке `permission denied` для Docker daemon добавьте пользователя в группу `docker` и перелогиньтесь. Подробнее в [CONTRIBUTING.md](CONTRIBUTING.md#linux-docker-daemon-permission-denied).

Адрес: http://localhost:2026

#### Вариант 2: Локальная разработка

1. **Проверить зависимости**:
   ```bash
   make check  # Проверяет Node.js 22+, pnpm, uv, nginx
   ```

2. **Установить зависимости**:
   ```bash
   make install
   ```

3. **(Опционально) Загрузить образ Sandbox заранее**:
   ```bash
   make setup-sandbox
   ```

4. **Запустить сервисы**:
   ```bash
   make dev
   ```

5. **Адрес**: http://localhost:2026

### Дополнительно

#### Режим Sandbox

DeerFlow поддерживает несколько режимов выполнения:
- **Локальное выполнение** — код запускается прямо на хосте
- **Docker** — код выполняется в изолированных Docker-контейнерах
- **Docker + Kubernetes** — выполнение в Kubernetes-подах через provisioner

Подробнее в [руководстве по конфигурации Sandbox](backend/docs/CONFIGURATION.md#sandbox).

#### MCP-сервер

DeerFlow поддерживает настраиваемые MCP-серверы для расширения возможностей. Для HTTP/SSE MCP-серверов поддерживаются OAuth-токены (`client_credentials`, `refresh_token`). Подробнее в [руководстве по MCP-серверу](backend/docs/MCP_SERVER.md).

#### Мессенджеры

DeerFlow принимает задачи прямо из мессенджеров. Каналы запускаются автоматически при настройке, публичный IP не нужен.

| Канал | Транспорт | Сложность |
|-------|-----------|-----------|
| Telegram | Bot API (long-polling) | Просто |
| Slack | Socket Mode | Средне |
| Feishu / Lark | WebSocket | Средне |
| DingTalk | Stream Push (WebSocket) | Средне |

**Конфигурация в `config.yaml`:**

```yaml
channels:
  feishu:
    enabled: true
    app_id: $FEISHU_APP_ID
    app_secret: $FEISHU_APP_SECRET
    # domain: https://open.feishu.cn       # China (default)
    # domain: https://open.larksuite.com   # International

  slack:
    enabled: true
    bot_t

# FILE: README.md

# 🦌 DeerFlow - 2.0

English | [中文](./README_zh.md) | [日本語](./README_ja.md) | [Français](./README_fr.md) | [Русский](./README_ru.md)

[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)](./backend/pyproject.toml)
[![Node.js](https://img.shields.io/badge/Node.js-22%2B-339933?logo=node.js&logoColor=white)](./Makefile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

<a href="https://trendshift.io/repositories/14699" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14699" alt="bytedance%2Fdeer-flow | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
> On February 28th, 2026, DeerFlow claimed the 🏆 #1 spot on GitHub Trending following the launch of version 2. Thanks a million to our incredible community — you made this happen! 💪🔥

DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness** that orchestrates **sub-agents**, **memory**, and **sandboxes** to do almost anything — powered by **extensible skills**.

https://github.com/user-attachments/assets/a8bcadc4-e040-4cf2-8fda-dd768b999c18

> [!NOTE]
> **DeerFlow 2.0 is a ground-up rewrite.** It shares no code with v1. If you're looking for the original Deep Research framework, it's maintained on the [`1.x` branch](https://github.com/bytedance/deer-flow/tree/main-1.x) — contributions there are still welcome. Active development has moved to 2.0.

## Official Website

[<img width="2880" height="1600" alt="image" src="https://github.com/user-attachments/assets/a598c49f-3b2f-41ea-a052-05e21349188a" />](https://deerflow.tech)

Learn more and see **real demos** on our [**official website**](https://deerflow.tech).

## Coding Plan from ByteDance Volcengine

<img width="4808" height="2400" alt="英文方舟" src="https://github.com/user-attachments/assets/2ecc7b9d-50be-4185-b1f7-5542d222fb2d" />

- We strongly recommend using Doubao-Seed-2.0-Code, DeepSeek v3.2 and Kimi 2.5 to run DeerFlow
- [Learn more](https://www.byteplus.com/en/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)
- [中国大陆地区的开发者请点击这里](https://www.volcengine.com/activity/codingplan?utm_campaign=deer_flow&utm_content=deer_flow&utm_medium=devrel&utm_source=OWO&utm_term=deer_flow)

## InfoQuest

DeerFlow has newly integrated the intelligent search and crawling toolset independently developed by BytePlus--[InfoQuest (supports free online experience)](https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest)

<a href="https://docs.byteplus.com/en/docs/InfoQuest/What_is_Info_Quest" target="_blank">
  <img
    src="https://sf16-sg.tiktokcdn.com/obj/eden-sg/hubseh7bsbps/20251208-160108.png"   alt="InfoQuest_banner"
  />
</a>

---

## Table of Contents

- [🦌 DeerFlow - 2.0](#-deerflow---20)
  - [Official Website](#official-website)
  - [Coding Plan from ByteDance Volcengine](#coding-plan-from-bytedance-volcengine)
  - [InfoQuest](#infoquest)
  - [Table of Contents](#table-of-contents)
  - [One-Line Agent Setup](#one-line-agent-setup)
  - [Quick Start](#quick-start)
    - [Configuration](#configuration)
    - [Running the Application](#running-the-application)
      - [Deployment Sizing](#deployment-sizing)
      - [Option 1: Docker (Recommended)](#option-1-docker-recommended)
      - [Option 2: Local Development](#option-2-local-development)
    - [Advanced](#advanced)
      - [Sandbox Mode](#sandbox-mode)
      - [MCP Server](#mcp-server)
      - [IM Channels](#im-channels)
      - [LangSmith Tracing](#langsmith-tracing)
      - [Langfuse Tracing](#langfuse-tracing)
      - [Using Both Providers](#using-both-providers)
  - [From Deep Research to Super Agent Harness](#from-deep-research-to-super-agent-harness)
  - [Core Features](#core-features)
    - [Skills \& Tools](#skills--tools)
      - [Claude Code Integration](#claude-code-integration)
    - [Sub-Agents](#sub-agents)
    - [Sandbox \& File System](#sandbox--file-system)
    - [Context Engineering](#context-engineering)
    - [Long-Term Memory](#long-term-memory)
  - [Recommended Models](#recommended-models)
  - [Embedded Python Client](#embedded-python-client)
  - [Documentation](#documentation)
  - [⚠️ Security Notice](#️-security-notice)
    - [Improper Deployment May Introduce Security Risks](#improper-deployment-may-introduce-security-risks)
    - [Security Recommendations](#security-recommendations)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)
    - [Key Contributors](#key-contributors)
  - [Star History](#star-history)

## One-Line Agent Setup

If you use Claude Code, Codex, Cursor, Windsurf, or another coding agent, you can hand it the setup instructions in one sentence:

```text
Help me clone DeerFlow if needed, then bootstrap it for local development by following https://raw.githubusercontent.com/bytedance/deer-flow/main/Install.md
```

That prompt is intended for coding agents. It tells the agent to clone the repo if needed, choose Docker when available, and stop with the exact next command plus any missing config the user still needs to provide.

## Quick Start

### Configuration

1. **Clone the DeerFlow repository**

   ```bash
   git clone https://github.com/bytedance/deer-flow.git
   cd deer-flow
   ```

2. **Run the setup wizard**

   From the project root directory (`deer-flow/`), run:

   ```bash
   make setup
   ```

   This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and execution/safety preferences such as sandbox mode, bash access, and file-write tools. It generates a minimal `config.yaml` and writes your keys to `.env`. Takes about 2 minutes.

   The wizard also lets you configure an optional web search provider, or skip it for now.

   Run `make doctor` at any time to verify your setup and get actionable fix hints.

   > **Advanced / manual configuration**: If you prefer to edit `config.yaml` directly, run `make config` instead to copy the full template. See `config.example.yaml` for the complete reference including CLI-backed providers (Codex CLI, Claude Code OAuth), OpenRouter, Responses API, and more.

   <details>
   <summary>Manual model configuration examples</summary>

   ```yaml
   models:
     - name: gpt-4o
       display_name: GPT-4o
       use: langchain_openai:ChatOpenAI
       model: gpt-4o
       api_key: $OPENAI_API_KEY

     - name: openrouter-gemini-2.5-flash
       display_name: Gemini 2.5 Flash (OpenRouter)
       use: langchain_openai:ChatOpenAI
       model: google/gemini-2.5-flash-preview
       api_key: $OPENROUTER_API_KEY
       base_url: https://openrouter.ai/api/v1

     - name: gpt-5-responses
       display_name: GPT-5 (Responses API)
       use: langchain_openai:ChatOpenAI
       model: gpt-5
       api_key: $OPENAI_API_KEY
       use_responses_api: true
       output_version: responses/v1

     - name: qwen3-32b-vllm
       display_name: Qwen3 32B (vLLM)
       use: deerflow.models.vllm_provider:VllmChatModel
       model: Qwen/Qwen3-32B
       api_key: $VLLM_API_KEY
       base_url: http://localhost:8000/v1
       supports_thinking: true
       when_thinking_enabled:
         extra_body:
           chat_template_kwargs:
             enable_thinking: true
   ```

   OpenRouter and similar OpenAI-compatible gateways should be configured with `langchain_openai:ChatOpenAI` plus `base_url`. If you prefer a provider-specific environment variable name, point `api_key` at that variable explicitly (for example `api_key: $OPENROUTER_API_KEY`).

   To route OpenAI models through `/v1/responses`, keep using `langchain_openai:ChatOpenAI` and set `use_responses_api: true` with `output_version: responses/v1`.

   For vLLM 0.19.0, use `deerflow.models.vllm_provider:VllmChatModel`. For Qwen-style reasoning models, DeerFlow toggles reasoning with `extra_body.chat_template_kwargs.enable_thinking` and preserves vLLM's non-standard `reasoning` field across multi-turn tool-call conversations. Legacy `thinking` configs are normalized automatically for backward compatibility. Reasoning models may also require the server to be started with `--reasoning-parser ...`. If your local vLLM deployment accepts any non-empty API key, you can still set `VLLM_API_KEY` to a placeholder value.

   CLI-backed provider examples:

   ```yaml
   models:
     - name: gpt-5.4
       display_name: GPT-5.4 (Codex CLI)
       use: deerflow.models.openai_codex_provider:CodexChatModel
       model: gpt-5.4
       supports_thinking: true
       supports_reasoning_effort: true

     - name: claude-sonnet-4.6
       display_name: Claude Sonnet 4.6 (Claude Code OAuth)
       use: deerflow.models.claude_provider:ClaudeChatModel
       model: claude-sonnet-4-6
       max_tokens: 4096
       supports_thinking: true
   ```

   - Codex CLI reads `~/.codex/auth.json`
   - Claude Code accepts `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_CREDENTIALS_PATH`, or `~/.claude/.credentials.json`
   - ACP agent entries are separate from model providers — if you configure `acp_agents.codex`, point it at a Codex ACP adapter such as `npx -y @zed-industries/codex-acp`
   - On macOS, export Claude Code auth explicitly if needed:

   ```bash
   eval "$(python3 scripts/export_claude_code_oauth.py --print-export)"
   ```

   API keys can also be set manually in `.env` (recommended) or exported in your shell:

   ```bash
   OPENAI_API_KEY=your-openai-api-key
   TAVILY_API_KEY=your-tavily-api-key
   ```

   </details>

### Running the Application

#### Deployment Sizing

Use the table below as a practical starting point when choosing how to run DeerFlow:

| Deployment target | Starting point | Recommended | Notes |
|---------|-----------|------------|-------|
| Local evaluation / `make dev` | 4 vCPU, 8 GB RAM, 20 GB free SSD | 8 vCPU, 16 GB RAM | Good for one developer or one light session with hosted model APIs.

# FILE: docs/CODE_CHANGE_SUMMARY_BY_FILE.md

# 代码更改总结（按文件 diff，细到每一行）

基于 `git diff HEAD` 的完整 diff，按文件列出所有变更。删除/新增文件单独说明。

---

## 一、后端

### 1. `backend/CLAUDE.md`

```diff
@@ -156,7 +156,7 @@ FastAPI application on port 8001 with health check at `GET /health`.
 | **Skills** (`/api/skills`) | `GET /` - list skills; `GET /{name}` - details; `PUT /{name}` - update enabled; `POST /install` - install from .skill archive |
 | **Memory** (`/api/memory`) | `GET /` - memory data; `POST /reload` - force reload; `GET /config` - config; `GET /status` - config + data |
 | **Uploads** (`/api/threads/{id}/uploads`) | `POST /` - upload files (auto-converts PDF/PPT/Excel/Word); `GET /list` - list; `DELETE /{filename}` - delete |
-| **Artifacts** (`/api/threads/{id}/artifacts`) | `GET /{path}` - serve artifacts; `?download=true` for download with citation removal |
+| **Artifacts** (`/api/threads/{id}/artifacts`) | `GET /{path}` - serve artifacts; `?download=true` for file download |

 Proxied through nginx: `/api/langgraph/*` → LangGraph, all other `/api/*` → Gateway.
```

- **第 159 行**：表格中 Artifacts 描述由「download with citation removal」改为「file download」。

---

### 2. `backend/packages/harness/deerflow/agents/lead_agent/prompt.py`

```diff
@@ -240,34 +240,8 @@ You have access to skills that provide optimized workflows for specific tasks. E
 - Action-Oriented: Focus on delivering results, not explaining processes
 </response_style>
 
-<citations_format>
-After web_search, ALWAYS include citations in your output:
-
-1. Start with a `<citations>` block in JSONL format listing all sources
-2. In content, use FULL markdown link format: [Short Title](full_url)
-
-**CRITICAL - Citation Link Format:**
-- CORRECT: `[TechCrunch](https://techcrunch.com/ai-trends)` - full markdown link with URL
-- WRONG: `[arXiv:2502.19166]` - missing URL, will NOT render as link
-- WRONG: `[Source]` - missing URL, will NOT render as link
-
-**Rules:**
-- Every citation MUST be a complete markdown link with URL: `[Title](https://...)`
-- Write content naturally, add citation link at end of sentence/paragraph
-- NEVER use bare brackets like `[arXiv:xxx]` or `[Source]` without URL
-
-**Example:**
-<citations>
-{{"id": "cite-1", "title": "AI Trends 2026", "url": "https://techcrunch.com/ai-trends", "snippet": "Tech industry predictions"}}
-{{"id": "cite-2", "title": "OpenAI Research", "url": "https://openai.com/research", "snippet": "Latest AI research developments"}}
-</citations>
-The key AI trends for 2026 include enhanced reasoning capabilities and multimodal integration [TechCrunch](https://techcrunch.com/ai-trends). Recent breakthroughs in language models have also accelerated progress [OpenAI](https://openai.com/research).
-</citations_format>
-
-
 <critical_reminders>
 - **Clarification First**: ALWAYS clarify unclear/missing/ambiguous requirements BEFORE starting work - never assume or guess
-- **Web search citations**: When you use web_search (or synthesize subagent results that used it), you MUST output the `<citations>` block and [Title](url) links as specified in citations_format so citations display for the user.
 {subagent_reminder}- Skill First: Always load the relevant skill before starting **complex** tasks.
```

```diff
@@ -341,7 +315,6 @@ def apply_prompt_template(subagent_enabled: bool = False) -> str:
     # Add subagent reminder to critical_reminders if enabled
     subagent_reminder = (
         "- **Orchestrator Mode**: You are a task orchestrator - decompose complex tasks into parallel sub-tasks and launch multiple subagents simultaneously. Synthesize results, don't execute directly.\n"
-        "- **Citations when synthesizing**: When you synthesize subagent results that used web search or cite sources, you MUST include a consolidated `<citations>` block (JSONL format) and use [Title](url) markdown links in your response so citations display correctly.\n"
         if subagent_enabled
         else ""
     )
```

- **删除**：`<citations_format>...</citations_format>` 整段（原约 243–266 行）、critical_reminders 中「Web search citations」一条、`apply_prompt_template` 中「Citations when synthesizing」一行。

---

### 3. `backend/app/gateway/routers/artifacts.py`

```diff
@@ -1,12 +1,10 @@
-import json
 import mimetypes
-import re
 import zipfile
 from pathlib import Path
 from urllib.parse import quote
 
-from fastapi import APIRouter, HTTPException, Request, Response
-from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse
+from fastapi import APIRouter, HTTPException, Request
+from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse, Response
 
 from app.gateway.path_utils import resolve_thread_virtual_path
```

- **第 1 行**：删除 `import json`。
- **第 3 行**：删除 `import re`。
- **第 6–7 行**：`fastapi` 中去掉 `Response`；`fastapi.responses` 中增加 `Response`（保留二进制 inline 返回用）。

```diff
@@ -24,40 +22,6 @@ def is_text_file_by_content(path: Path, sample_size: int = 8192) -> bool:
         return False
 
 
-def _extract_citation_urls(content: str) -> set[str]:
-    """Extract URLs from <citations> JSONL blocks. Format must match frontend core/citations/utils.ts."""
-    urls: set[str] = set()
-    for match in re.finditer(r"<citations>([\s\S]*?)</citations>", content):
-        for line in match.group(1).split("\n"):
-            line = line.strip()
-            if line.startswith("{"):
-                try:
-                    obj = json.loads(line)
-                    if "url" in obj:
-                        urls.add(obj["url"])
-                except (json.JSONDecodeError, ValueError):
-                    pass
-    return urls
-
-
-def remove_citations_block(content: str) -> str:
-    """Remove ALL citations from markdown (blocks, [cite-N], and citation links). Used for downloads."""
-    if not content:
-        return content
-
-    citation_urls = _extract_citation_urls(content)
-
-    result = re.sub(r"<citations>[\s\S]*?</citations>", "", content)
-    if "<citations>" in result:
-        result = re.sub(r"<citations>[\s\S]*$", "", result)
-    resu

# FILE: docs/SKILL_NAME_CONFLICT_FIX.md

# 技能名称冲突修复 - 代码改动文档

## 概述

本文档详细记录了修复 public skill 和 custom skill 同名冲突问题的所有代码改动。

**状态**: ⚠️ **已知问题保留** - 同名技能冲突问题已识别但暂时保留，后续版本修复

**日期**: 2026-02-10

---

## 问题描述

### 原始问题

当 public skill 和 custom skill 有相同名称（但技能文件内容不同）时，会出现以下问题：

1. **打开冲突**: 打开 public skill 时，同名的 custom skill 也会被打开
2. **关闭冲突**: 关闭 public skill 时，同名的 custom skill 也会被关闭
3. **配置冲突**: 两个技能共享同一个配置键，导致状态互相影响

### 根本原因

- 配置文件中技能状态仅使用 `skill_name` 作为键
- 同名但不同类别的技能无法区分
- 缺少类别级别的重复检查

---

## 解决方案

### 核心思路

1. **组合键存储**: 使用 `{category}:{name}` 格式作为配置键，确保唯一性
2. **向后兼容**: 保持对旧格式（仅 `name`）的支持
3. **重复检查**: 在加载时检查每个类别内是否有重复的技能名称
4. **API 增强**: API 支持可选的 `category` 查询参数来区分同名技能

### 设计原则

- ✅ 最小改动原则
- ✅ 向后兼容
- ✅ 清晰的错误提示
- ✅ 代码复用（提取公共函数）

---

## 详细代码改动

### 一、后端配置层 (`backend/packages/harness/deerflow/config/extensions_config.py`)

#### 1.1 新增方法: `get_skill_key()`

**位置**: 第 152-166 行

**代码**:
```python
@staticmethod
def get_skill_key(skill_name: str, skill_category: str) -> str:
    """Get the key for a skill in the configuration.

    Uses format '{category}:{name}' to uniquely identify skills,
    allowing public and custom skills with the same name to coexist.

    Args:
        skill_name: Name of the skill
        skill_category: Category of the skill ('public' or 'custom')

    Returns:
        The skill key in format '{category}:{name}'
    """
    return f"{skill_category}:{skill_name}"
```

**作用**: 生成组合键，格式为 `{category}:{name}`

**影响**: 
- 新增方法，不影响现有代码
- 被 `is_skill_enabled()` 和 API 路由使用

---

#### 1.2 修改方法: `is_skill_enabled()`

**位置**: 第 168-195 行

**修改前**:
```python
def is_skill_enabled(self, skill_name: str, skill_category: str) -> bool:
    skill_config = self.skills.get(skill_name)
    if skill_config is None:
        return skill_category in ("public", "custom")
    return skill_config.enabled
```

**修改后**:
```python
def is_skill_enabled(self, skill_name: str, skill_category: str) -> bool:
    """Check if a skill is enabled.

    First checks for the new format key '{category}:{name}', then falls back
    to the old format '{name}' for backward compatibility.

    Args:
        skill_name: Name of the skill
        skill_category: Category of the skill

    Returns:
        True if enabled, False otherwise
    """
    # Try new format first: {category}:{name}
    skill_key = self.get_skill_key(skill_name, skill_category)
    skill_config = self.skills.get(skill_key)
    if skill_config is not None:
        return skill_config.enabled

    # Fallback to old format for backward compatibility: {name}
    # Only check old format if category is 'public' to avoid conflicts
    if skill_category == "public":
        skill_config = self.skills.get(skill_name)
        if skill_config is not None:
            return skill_config.enabled

    # Default to enabled for public & custom skills
    return skill_category in ("public", "custom")
```

**改动说明**:
- 优先检查新格式键 `{category}:{name}`
- 向后兼容：如果新格式不存在，检查旧格式（仅 public 类别）
- 保持默认行为：未配置时默认启用

**影响**:
- ✅ 向后兼容：旧配置仍可正常工作
- ✅ 新配置使用组合键，避免冲突
- ✅ 不影响现有调用方

---

### 二、后端技能加载器 (`backend/packages/harness/deerflow/skills/loader.py`)

#### 2.1 添加重复检查逻辑

**位置**: 第 54-86 行

**修改前**:
```python
skills = []

# Scan public and custom directories
for category in ["public", "custom"]:
    category_path = skills_path / category
    # ... 扫描技能目录 ...
    skill = parse_skill_file(skill_file, category=category)
    if skill:
        skills.append(skill)
```

**修改后**:
```python
skills = []
category_skill_names = {}  # Track skill names per category to detect duplicates

# Scan public and custom directories
for category in ["public", "custom"]:
    category_path = skills_path / category
    if not category_path.exists() or not category_path.is_dir():
        continue

    # Initialize tracking for this category
    if category not in category_skill_names:
        category_skill_names[category] = {}

    # Each subdirectory is a potential skill
    for skill_dir in category_path.iterdir():
        # ... 扫描逻辑 ...
        skill = parse_skill_file(skill_file, category=category)
        if skill:
            # Validate: each category cannot have duplicate skill names
            if skill.name in category_skill_names[category]:
                existing_path = category_skill_names[category][skill.name]
                raise ValueError(
                    f"Duplicate skill name '{skill.name}' found in {category} category. "
                    f"Existing: {existing_path}, Duplicate: {skill_file.parent}"
                )
            category_skill_names[category][skill.name] = str(skill_file.parent)
            skills.append(skill)
```

**改动说明**:
- 为每个类别维护技能名称字典
- 检测到重复时抛出 `ValueError`，包含详细路径信息
- 确保每个类别内技能名称唯一

**影响**:
- ✅ 防止配置冲突
- ✅ 清晰的错误提示
- ⚠️ 如果存在重复，加载会失败（这是预期行为）

---

### 三、后端 API 路由 (`backend/app/gateway/routers/skills.py`)

#### 3.1 新增辅助函数: `_find_skill_by_name()`

**位置**: 第 136-173 行

**代码**:
```python
def _find_skill_by_name(
    skills: list[Skill], skill_name: str, category: str | None = None
) -> Skill:
    """Find a skill by name, optionally filtered by category.
    
    Args:
        skills: List of all skills
        skill_name: Name of the skill to find
        category: Optional category filter
        
    Returns:
        The found Skill object
        
    Raises:
        HTTPException: If skill not found or multiple skills require category
    """
    if category:
        skill = next((s for s in skills if s.name == skill_name and s.category == category), None)
        if skill is None:
            raise HTTPException(
                status_code=404,
                detail=f"Skill '{skill_name}' with category '{category}' not found"
            )
        return skill
    
    # If no category provided, check if there are multiple skills with the same name
    matching_skills = [s for s in skills if s.name == skill_name]
    if len(matching_skills) == 0:
        raise HTTPException(status_code=404, detail=f"Skill '{skill_name}' not found")
    elif len(matching_skills) > 1:
        # Multiple

# FILE: docs/plans/2026-04-01-langfuse-tracing.md

# Langfuse Tracing Implementation Plan

**Goal:** Add optional Langfuse observability support to DeerFlow while preserving existing LangSmith tracing and allowing both providers to be enabled at the same time.

**Architecture:** Extend tracing configuration from a single LangSmith-only shape to a multi-provider config, add a tracing callback factory that builds zero, one, or two callbacks based on environment variables, and update model creation to attach those callbacks. If a provider is explicitly enabled but misconfigured or fails to initialize, tracing initialization during model creation should fail with a clear error naming that provider.

**Tech Stack:** Python 3.12, Pydantic, LangChain callbacks, LangSmith, Langfuse, pytest

---

### Task 1: Add failing tracing config tests

**Files:**
- Modify: `backend/tests/test_tracing_config.py`

**Step 1: Write the failing tests**

Add tests covering:
- Langfuse-only config parsing
- dual-provider parsing
- explicit enable with missing required Langfuse fields
- provider enable detection without relying on LangSmith-only helpers

**Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_tracing_config.py -q`
Expected: FAIL because tracing config only supports LangSmith today.

**Step 3: Write minimal implementation**

Update tracing config code to represent multiple providers and expose helper functions needed by the tests.

**Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_tracing_config.py -q`
Expected: PASS

### Task 2: Add failing callback factory and model attachment tests

**Files:**
- Modify: `backend/tests/test_model_factory.py`
- Create: `backend/tests/test_tracing_factory.py`

**Step 1: Write the failing tests**

Add tests covering:
- LangSmith callback creation
- Langfuse callback creation
- dual callback creation
- startup failure when an explicitly enabled provider cannot initialize
- model factory appends all tracing callbacks to model callbacks

**Step 2: Run tests to verify they fail**

Run: `cd backend && uv run pytest tests/test_model_factory.py tests/test_tracing_factory.py -q`
Expected: FAIL because there is no provider factory and model creation only attaches LangSmith.

**Step 3: Write minimal implementation**

Create tracing callback factory module and update model factory to use it.

**Step 4: Run tests to verify they pass**

Run: `cd backend && uv run pytest tests/test_model_factory.py tests/test_tracing_factory.py -q`
Expected: PASS

### Task 3: Wire dependency and docs

**Files:**
- Modify: `backend/packages/harness/pyproject.toml`
- Modify: `README.md`
- Modify: `backend/README.md`

**Step 1: Update dependency**

Add `langfuse` to the harness dependencies.

**Step 2: Update docs**

Document:
- Langfuse environment variables
- dual-provider behavior
- failure behavior for explicitly enabled providers

**Step 3: Run targeted verification**

Run: `cd backend && uv run pytest tests/test_tracing_config.py tests/test_model_factory.py tests/test_tracing_factory.py -q`
Expected: PASS

### Task 4: Run broader regression checks

**Files:**
- No code changes required

**Step 1: Run relevant suite**

Run: `cd backend && uv run pytest tests/test_tracing_config.py tests/test_model_factory.py tests/test_tracing_factory.py -q`

**Step 2: Run lint if needed**

Run: `cd backend && uv run ruff check packages/harness/deerflow/config/tracing_config.py packages/harness/deerflow/models/factory.py packages/harness/deerflow/tracing`

**Step 3: Review diff**

Run: `git diff -- backend/packages/harness backend/tests README.md backend/README.md`


# FILE: docs/superpowers/plans/2026-04-10-event-store-history.md

# Event Store History — Backend Compatibility Layer

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace checkpoint state with the append-only event store as the message source in the thread state/history endpoints, so summarization never causes message loss.

**Architecture:** The Gateway's `get_thread_state` and `get_thread_history` endpoints currently read messages from `checkpoint.channel_values["messages"]`. After summarization, those messages are replaced with a synthetic summary-as-human message and all pre-summarize messages are gone. We modify these endpoints to read messages from the RunEventStore instead (append-only, unaffected by summarization). The response shape for each message stays identical so the chat render path needs no changes, but the frontend's feedback hook must be aligned to use the same full-history view (see Task 4).

**Tech Stack:** Python (FastAPI, SQLAlchemy), pytest, TypeScript (React Query)

**Scope:** Gateway mode only (`make dev-pro`). Standard mode uses the LangGraph Server directly and does not go through these endpoints; the summarize bug is still present there and must be tracked as a separate follow-up (see §"Follow-ups" at end of plan).

**Prerequisite already landed:** `backend/packages/harness/deerflow/runtime/journal.py` now unwraps `Command(update={'messages':[ToolMessage(...)]})` in `on_tool_end`, so new runs that use state-updating tools (e.g. `present_files`) write the inner `ToolMessage` content to the event store instead of `str(Command(...))`. Legacy data captured before this fix is cleaned up defensively by the new helper (see Task 1 Step 3 `_sanitize_legacy_command_repr`).

---

## Real Data Alignment Analysis

Compared real `POST /history` response (checkpoint-based) with `run_events` table for thread `6d30913e-dcd4-41c8-8941-f66c716cf359` (docs/resp.json + backend/.deer-flow/data/deerflow.db). See `docs/superpowers/specs/2026-04-11-runjournal-history-evaluation.md` for full evidence chain.

| Message type | Fields compared | Difference |
|-------------|----------------|------------|
| human_message | all fields | `id` is `None` in event store, has UUID in checkpoint |
| ai_message (tool_call) | all fields, 6 overlapping | **IDENTICAL** (0 diffs) |
| ai_message (final) | all fields | **IDENTICAL** |
| tool_result (normal) | all fields | Only `id` differs (`None` vs UUID) |
| tool_result (from `Command`-returning tool) | content | **Legacy data stored `str(Command(...))` repr instead of inner ToolMessage** — fixed in journal.py for new runs; legacy rows sanitized by helper |

**Root cause for id difference:** LangGraph's checkpoint assigns `id` to HumanMessage and ToolMessage during graph execution. Event store writes happen earlier, when those ids are still None. AI messages receive `id` from the LLM response (`lc_run--*`) and are unaffected.

**Fix for id:** Generate deterministic UUIDs for `id=None` messages using `uuid5(NAMESPACE_URL, f"{thread_id}:{seq}")` at read time. Patch a **copy** of the content dict, never the live store object.

**Summarize impact quantified on the reproducer thread**: event_store has 16 messages (7 AI + 9 others); checkpoint has 12 after summarize (5 AI + 7 others). AI id overlap: 5 of 7 — the 2 missing AI messages are pre-summarize.

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `backend/app/gateway/routers/threads.py` | Modify | Replace checkpoint messages with event store messages in `get_thread_state` and `get_thread_history` |
| `backend/tests/test_thread_state_event_store.py` | Create | Tests for the modified endpoints |

---

### Task 1: Add `_get_event_store_messages` helper to `threads.py`

A shared helper that loads the **full** message stream from the event store, patches `id=None` messages with deterministic UUIDs, and defensively sanitizes legacy `Command(update=...)` reprs captured before the journal.py fix. Patches a copy of each content dict so the live store is never mutated.

**Design constraints (derived from evaluation §3, §4, §5):**
- **Full pagination**, not `limit=1000`. `RunEventStore.list_messages` returns "latest N records" — a fixed limit silently truncates older messages. Use `count_messages()` to size the request or loop with `after_seq` cursors.
- **Copy before mutate**. `MemoryRunEventStore` returns live dict references; the JSONL/DB stores may return detached rows but we must not rely on that. Always `content = dict(evt["content"])` before patching `id`.
- **Legacy Command sanitization.** Legacy data contains `content["content"] == "Command(update={'artifacts': [...], 'messages': [ToolMessage(content='X', ...)]})"`. Regex-extract the inner ToolMessage content string and replace; if extraction fails, leave content as-is (still strictly better than nothing because checkpoint fallback is also wrong for summarized threads).
- **User context.** `DbRunEventStore.list_messages` is user-scoped via `resolve_user_id(AUTO)` and relies on the auth contextvar set by `@require_permission`. Both endpoints are already decorated — document this dependency in the helper docstring.

**Files:**
- Modify: `backend/app/gateway/routers/threads.py`
- Test: `backend/tests/test_thread_state_event_store.py`

- [ ] **Step 1: Write the test**

Create `backend/tests/test_thread_state_event_store.py`:

```python
"""Tests for event-store-backed message loading in thread state/history endpoints."""

from __future__ import annotations

import uuid

import pytest

from deerflow.runtime.events.store.memory import MemoryRunEventStore


@pytest.fixture()
def event_store():
    return MemoryRunEventStore()


async def _seed_conversation(event_store: MemoryRunEventStore, thread_id: str = "t1"):
    """Seed a realistic multi-turn conversation matching real checkpoint format."""

# FILE: docs/superpowers/specs/2026-04-11-runjournal-history-evaluation.md

# RunJournal 替换 History Messages — 方案评估与对比

**日期**：2026-04-11
**分支**：`rayhpeng/fix-persistence-new`
**相关 plan**：[`docs/superpowers/plans/2026-04-10-event-store-history.md`](../plans/2026-04-10-event-store-history.md)（尚未落地）

---

## 1. 问题与数据核对

**症状**：SummarizationMiddleware 触发后，前端历史中无法展示 summarize 之前的真实用户消息。

**复现数据**（thread `6d30913e-dcd4-41c8-8941-f66c716cf359`）：

| 数据源 | seq=1 的 message | 总 message 数 | 是否保留原始 human |
|---|---|---:|---|
| `run_events`（SQLite） | human `"最新伊美局势"` | 9（1 human + 7 ai_tool_call + 9 tool_result + 1 ai_message） | ✅ |
| `/history` 响应（`docs/resp.json`） | type=human，content=`"Here is a summary of the conversation to date:…"` | 不定 | ❌（已被 summary 替换）|

**根因**：`backend/app/gateway/routers/threads.py:587-589` 的 `get_thread_history` 从 `checkpoint.channel_values["messages"]` 读取，而 LangGraph 的 SummarizationMiddleware 会原地改写这个列表。

---

## 2. 候选方案

| 方案 | 描述 | 本次是否推荐 |
|---|---|---|
| **A. event_store 覆盖 messages**（已有 plan） | `/history`、`/state` 改读 `RunEventStore.list_messages()`，覆盖 `channel_values["messages"]`；其它字段保持 checkpoint 来源 | ✅ 主方案 |
| B. 修 SummarizationMiddleware | 让 summarize 不原地替换 messages（作为附加 system message） | ❌ 违背 summarize 的 token 预算初衷 |
| C. 双读合并（checkpoint + event_store diff） | 合并 summarize 切点前后的两段 | ❌ 合并逻辑复杂无额外收益 |
| D. 切到现有 `/api/threads/{id}/messages` 端点 | 前端直接消费已经存在的 event-store 消息端点（`thread_runs.py:285-323`）| ⚠️ 更干净但需要前端改动 |

---

## 3. Claude 自评 vs Codex 独立评估

两方独立分析了同一份 plan。重合点基本一致，但 **Codex 发现了一个我遗漏的关键 bug**。

### 3.1 一致结论

| 维度 | 结论 |
|---|---|
| 正确性方向 | event_store 是 append-only + 不受 summarize 影响，方向正确 |
| ID 补齐 | `uuid5(NAMESPACE_URL, f"{thread_id}:{seq}")` 稳定且确定性，安全 |
| 前端 schema | 零改动 |
| Non-message 字段（artifacts/todos/title/thread_data） | summarize 只影响 messages，不需要覆盖其它字段 |
| 多 checkpoint 语义 | 前端 `useStream` 只取 `limit: 1`（`frontend/src/core/threads/hooks.ts:203-210`），不做时间旅行；latest-only 可接受但应在注释/文档写清楚 |
| 作用域 | 仅 Gateway mode；Standard mode 直连 LangGraph Server，bug 在默认部署路径仍然存在 |

### 3.2 Claude 的独立观察

1. 已验证数据对齐：plan 文档第 15-28 行的真实数据对齐表与本次 `run_events` 导出一致（9 条消息 id 分布：AI 来自 LLM `lc_run--*`、human/tool 为 None）。
2. 担心 `run_end` / `run_error` / `cancel` 路径未必都 flush —— 这一点 Codex 实际核查了代码并给出确定结论（见下）。
3. 方案 A 的单文件改动约 60 行，复杂度小。

### 3.3 Codex 的关键补充（Claude 遗漏）

> **Bug #1 — Plan 用 `limit=1000` 并非全量**
> `RunEventStore.list_messages()` 的语义是"返回最新 limit 条"（`base.py:51-65`、`db.py:151-181`）。对于消息数超过 1000 的长对话，plan 当前写法会**丢掉最早的消息**，再次引入"消息丢失"bug（只是换了丢失的段）。

> **Bug #2 — helper 就地修改了 store 的 dict**
> plan 的 helper 里对 `content` 原地写 `id`；`MemoryRunEventStore` 返回的是**活引用**，会污染 store 中的对象。应 deep-copy 或 dict 推导出新对象。

> **Flush 路径已核查**：
> `RunJournal` 在 threshold (`journal.py:360-373`)、`run_end` (`91-96`)、`run_error` (`97-106`)、worker `finally` (`worker.py:280-286`) 都会 flush；`CancelledError` 也走 finally。**正常 end/error/cancel 都 flush，仅硬 kill / 进程崩溃会丢缓冲区**。
> 因此 `flush_threshold 20 → 5` 的意义**仅在于硬崩溃窗口**与 mid-run reload 可见性，**不是正确性修复**，属于可选 tuning。代价是更多 put_batch / SQLite churn；且 `_flush_sync()` (`383-398`) 已防止并发 flush，所以"每 5 条一 flush"是 best-effort 非严格保证。

### 3.4 Codex 未否决但提示的次要点

- 方案 D（消费现有 `/api/threads/{id}/messages` 端点）更干净但需前端改动。
- `/history` 一旦被方案 A 改过，就不再是严格意义上的"按 checkpoint 快照"API（对 messages 字段），应写进注释和 API 文档。
- Standard mode 的 summarize bug 应建立独立 follow-up issue。

---

## 4. 最终合并判决

**Codex**：APPROVE-WITH-CHANGES
**Claude**：同意 Codex 的判决

### 合并前必须修改（Top 3）

1. **修复分页 bug**：不能用固定 `limit=1000`。必须用以下之一：
   - `count = await event_store.count_messages(thread_id)`，再 `list_messages(thread_id, limit=count)`
   - 或循环 cursor 分页（`after_seq`）直到耗尽
2. **不要原地修改 store dict**：helper 对 `content` 的 id 补齐需要 copy（`dict(content)` 浅拷贝足够，因为只写 top-level `id`）
3. **Standard mode 显式 follow-up**：在 plan 文末加 "Standard-mode follow-up: TODO #xxx"，或在合并 PR 描述中明确这是 Gateway-only 止血

### 可选（非阻塞）

4. `flush_threshold 20 → 5` 降级为"可选 tuning"，不是修复的一部分；或独立一条 commit 并说明只对硬崩溃窗口有用
5. `get_thread_history` 新增注释，说明 messages 字段脱离了 checkpoint 快照语义
6. 测试覆盖：模拟 summarize 后的 checkpoint + 真实 event_store，端到端验证 `/history` 返回包含原始 human 消息

---

## 5. 推荐执行顺序

1. 按本文档 §4 修订 `docs/superpowers/plans/2026-04-10-event-store-history.md`（主要是 Task 1 的 helper 实现 + 分页）
2. 按修订后的 plan 执行（走 `superpowers:executing-plans`）
3. 合并后立即建 Standard mode follow-up issue

## 6. Feedback 影响分析（2026-04-11 补充）

### 6.1 数据模型

`feedback` 表（`persistence/feedback/model.py`）：

| 字段 | 说明 |
|---|---|
| `feedback_id` PK | - |
| `run_id` NOT NULL | 反馈目标 run |
| `thread_id` NOT NULL | - |
| `user_id` | - |
| `message_id` nullable | 注释明确写：`optional RunEventStore event identifier` — 已经面向 event_store 设计 |
| UNIQUE(thread_id, run_id, user_id) | 每 run 每用户至多一条 |

**结论**：feedback **不按 message uuid 存**，按 `run_id` 存，所以 summarize 导致的 checkpoint messages 丢失**不会影响 feedback 存储**。schema 天生与 event_store 兼容，**无需数据迁移**。

### 6.2 前端的 runId 映射：发现隐藏 bug

前端 feedback 目前走两条并行的数据链：

| 用途 | 数据源 | 位置 |
|---|---|---|
| 渲染消息体 | `POST /history`（checkpoint） | `useStream` → `thread.messages` |
| 拿 `runId` 映射 | `GET /api/threads/{id}/messages?limit=200`（**event_store**） | `useThreadFeedback` (`hooks.ts:669-709`) |

两者通过 **"AI 消息的序号"** 对齐：

```ts
// hooks.ts:691-698
for (const msg of messages) {
  if (msg.event_type === "ai_message") {
    runIdByAiIndex.push(msg.run_id);  // 只按 AI 顺序 push
  }
}
// message-list.tsx:70-71
runId = feedbackData.runIdByAiIndex[aiMessageIndex]
```

**Bug**：summarize 过的 thread 里，两条数据链的 AI 消息数量和顺序**不一致**：

| 数据源 | 本 thread 的 AI 消息序列 | 数量 |
|---|---|---:|
| `/history`（checkpoint，summarize 后） | seq=19,31,37,45,53 | 5 |
| `/messages`（event_store，完整） | seq=5,13,19,31,37,45,53 | 7 |

结果：前端渲染的"第 0 条 AI 消息"是 seq=19，但 `runIdByAiIndex[0]` 指向 seq=5 的 run（本例同一 run 里没事，**跨多 run 的 thread 点赞就会打到错的 run 上**）。

**这个 bug 和本次 plan 无关，已经存在了**。只是用户未必注意到。

### 6.3 方案 A 对 feedback 的影响

**负面**：无。feedback 存储不受影响。

**正面（意外收益）**：`/history` 切换到 event_store 后，**两条数据链的 AI 消息序列自动对齐**，§6.2 的隐藏 bug 被顺带修好。

**前提条件**（加入 Top 3 改动之一同等重要）：

- 新 helper 必须和 `/messages` 端点用**同样的消息获取逻辑**（same store, same filter）。否则两条链仍然可能在边界条件下漂移
- 具体说：**两边都要做完整分页**。目前 `/messages?limit=200` 在前端硬编码 200，如果 thread 有 >200 条消息就

# FILE: docs/superpowers/specs/2026-04-11-summarize-marker-design.md

# Summarize Marker in History — Design & Verification

**Date**: 2026-04-11
**Branch**: `rayhpeng/fix-persistence-new`
**Status**: Design approved, implementation deferred to a follow-up PR
**Depends on**: [`2026-04-11-runjournal-history-evaluation.md`](./2026-04-11-runjournal-history-evaluation.md) (the event-store-backed history fix this builds on)

---

## 1. Goal

Display a "summarization happened here" marker in the conversation history UI when `SummarizationMiddleware` ran mid-run, so users understand why earlier messages look condensed or missing. The event-store-backed `/history` fix already recovered the original messages; this spec adds a **visible marker** at the seq position where summarization occurred, optionally showing the generated summary text.

## 2. Investigation findings

### 2.1 Today's state: zero middleware records

Full scan of `backend/.deer-flow/data/deerflow.db` `run_events`:

| category | rows |
|---|---:|
| trace | 76 |
| message | 34 |
| lifecycle | 8 |
| **middleware** | **0** |

No row has `event_type` containing `summariz` or `middleware`. The middleware category is dead in production.

### 2.2 Why: two dead code paths in `journal.py`

| Location | Status |
|---|---|
| `journal.py:343-362` — `on_custom_event("summarization", ...)` writes one trace event + one `category="middleware"` event. | Dead. Only fires when something calls `adispatch_custom_event("summarization", {...})`. The upstream LangChain `SummarizationMiddleware` (`.venv/.../langchain/agents/middleware/summarization.py:272`) **never emits custom events** — its `before_model`/`abefore_model` just mutate messages in place and return `{'messages': new_messages}`. Callback never triggered. |
| `journal.py:449` — `record_middleware(tag, *, name, hook, action, changes)` helper | Dead. Grep shows zero callers in the harness. Added speculatively, never wired up. |

### 2.3 Concrete evidence of summarize running unlogged

Thread `3d5dea4a-0983-4727-a4e8-41a64428933a`:

- `run_events` seq=1 → original human `"写一份关于deer-flow的详细技术报告"` ✓ (event store is fine)
- `run_events` seq=43 → `llm_request` trace whose `messages[0]` literal contains `"Here is a summary of the conversation to date:"` — proof that SummarizationMiddleware did inject a summary mid-run
- Zero rows with `category='middleware'` for this thread → nothing captured for UI to render

## 3. Approaches considered

### A. Subclass `SummarizationMiddleware` and dispatch a custom event

Wrap the upstream class, override `abefore_model`, call `await adispatch_custom_event("summarization", {...})` after super(). Journal's existing `on_custom_event` path captures it.

### B. Frontend-only diff heuristic

Compare `event_store.count_messages()` vs rendered count, infer summarization happened from the gap. **Rejected**: can't pinpoint position in the stream, can't show summary text. Only yields a vague badge.

### C. Hybrid A + frontend inline card rendered at the middleware event's seq position

Same backend as A, plus frontend renders an inline `[N messages condensed]` card at the correct chronological position. **Recommended terminal state**.

## 4. Subagent's wrong claim and its rebuttal

An independent agent flagged approach A as structurally broken because:

> `RunnableCallable(trace=False)` skips `set_config_context`, therefore `var_child_runnable_config` is never set, therefore `adispatch_custom_event` raises `RuntimeError("Unable to dispatch an adhoc event without a parent run id")`.

**This is wrong.** The user's counter-intuition was correct: `trace=False` does not prevent `adispatch_custom_event` from working, as long as the middleware signature explicitly accepts `config: RunnableConfig`. The mechanism:

1. `RunnableCallable.__init__` (`langgraph/_internal/_runnable.py:293-319`) inspects the function signature. If it accepts `config: RunnableConfig`, that parameter is recorded in `self.func_accepts`.
2. Both `trace=True` and `trace=False` branches of `ainvoke` run the same kwarg-injection loop (`_runnable.py:349-356`): `if kw == "config": kw_value = config`. The `config` passed to `ainvoke` (from Pregel's `task.proc.ainvoke(task.input, config)` at `pregel/_retry.py:138`) is the task config with callbacks already bound.
3. Inside the middleware, passing that `config` explicitly to `adispatch_custom_event(..., config=config)` means the function doesn't rely on `var_child_runnable_config.get()` at all. The LangChain docstring at `langchain_core/callbacks/manager.py:2574-2579` even says "If using python 3.10 and async, you MUST specify the config parameter" — which is exactly this path.

`trace=False` only changes whether **this runnable layer creates a new child callback scope**. It does not affect whether the outer-layer config (with callbacks including `RunJournal`) is passed down to the function.

## 5. Verification

Ran `/tmp/verify_summarize_event.py` (standalone minimal reproduction):

- Minimal `AgentMiddleware` subclass with `abefore_model(self, state, runtime, config: RunnableConfig)`
- Calls `await adispatch_custom_event("summarization", {...}, config=config)` inside
- `create_agent(model=FakeChatModel, middleware=[probe])`
- `agent.ainvoke({...}, config={"callbacks": [RecordingHandler()]})`

**Result**:

```
INFO verify: ProbeMiddleware.abefore_model called
INFO verify:   config keys: ['callbacks', 'configurable', 'metadata']
INFO verify:   config.callbacks type: AsyncCallbackManager
INFO verify:   config.metadata: {'langgraph_step': 1, 'langgraph_node': 'probe.before_model', ...}
INFO verify: on_custom_event fired: name=summarization
             run_id=019d7d19-1727-7830-aa33-648ecbee4b95
             data={'summary': 'fake summary', 'replaced_count': 3}
SUCCESS: approach A is viable (config injection + adispatch work)
```

All five predictions held:

1. ✅ `config: RunnableConfig` signature triggers auto-injection despite `trace=False`
2. ✅ `config.callbacks` is an `AsyncCallbackManager` with `parent_run_id` set
3. ✅ `adispatch_cu
