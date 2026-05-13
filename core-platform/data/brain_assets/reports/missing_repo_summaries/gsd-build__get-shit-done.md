# Missing Repo Summary Source: gsd-build/get-shit-done

- URL: https://github.com/gsd-build/get-shit-done
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/gsd-build__get-shit-done
- Clone Status: cloned
- Language: JavaScript
- Stars: 61786
- Topics: claude-code, context-engineering, meta-prompting, spec-driven-development
- Description: A light-weight and powerful meta-prompting, context engineering and spec-driven development system for Claude Code by TÂCHES.

## Extracted README / Docs / Examples



# FILE: README.ja-JP.md

<div align="center">

# GET SHIT DONE

[English](README.md) · [Português](README.pt-BR.md) · [简体中文](README.zh-CN.md) · **日本語**

**Claude Code、OpenCode、Gemini CLI、Kilo、Codex、Copilot、Cursor、Windsurf、Antigravity、Augment、Trae、Cline向けの軽量かつ強力なメタプロンプティング、コンテキストエンジニアリング、仕様駆動開発システム。**

**コンテキストロット（Claudeがコンテキストウィンドウを消費するにつれ品質が劣化する現象）を解決します。**

[![npm version](https://img.shields.io/npm/v/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![npm downloads](https://img.shields.io/npm/dm/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![Tests](https://img.shields.io/github/actions/workflow/status/gsd-build/get-shit-done/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/gsd-build/get-shit-done/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![X (Twitter)](https://img.shields.io/badge/X-@gsd__foundation-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/gsd_foundation)
[![$GSD Token](https://img.shields.io/badge/$GSD-Dexscreener-1C1C1C?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgZmlsbD0iIzAwRkYwMCIvPjwvc3ZnPg==&logoColor=00FF00)](https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv)
[![GitHub stars](https://img.shields.io/github/stars/gsd-build/get-shit-done?style=for-the-badge&logo=github&color=181717)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<br>

```bash
npx get-shit-done-cc@latest
```

**Mac、Windows、Linuxで動作します。**

<br>

![GSD Install](assets/terminal.svg)

<br>

*「自分が何を作りたいか明確に分かっていれば、これが確実に作ってくれる。嘘じゃない。」*

*「SpecKit、OpenSpec、Taskmasterを試してきたが、これが一番良い結果を出してくれた。」*

*「Claude Codeへの最強の追加ツール。過剰な設計は一切なし。文字通り、やるべきことをやってくれる。」*

<br>

**Amazon、Google、Shopify、Webflowのエンジニアに信頼されています。**

[なぜ作ったのか](#なぜ作ったのか) · [仕組み](#仕組み) · [コマンド](#コマンド) · [なぜ効果的なのか](#なぜ効果的なのか) · [ユーザーガイド](docs/ja-JP/USER-GUIDE.md)

</div>

---

## なぜ作ったのか

私はソロ開発者です。コードは自分で書きません — Claude Codeが書きます。

仕様駆動開発ツールは他にもあります。BMAD、Spekkitなど。しかしどれも必要以上に複雑にしているように見えます（スプリントセレモニー、ストーリーポイント、ステークホルダーとの同期、振り返り、Jiraワークフローなど）。あるいは、何を作ろうとしているのかの全体像を本当には理解していません。私は50人規模のソフトウェア会社ではありません。エンタープライズごっこをしたいわけではありません。ただ、うまく動く素晴らしいものを作りたいクリエイティブな人間です。

だからGSDを作りました。複雑さはシステムの中にあり、ワークフローの中にはありません。裏側では、コンテキストエンジニアリング、XMLプロンプトフォーマッティング、サブエージェントのオーケストレーション、状態管理が動いています。あなたが目にするのは、ただ動くいくつかのコマンドだけです。

このシステムは、Claudeが仕事をし、*かつ*検証するために必要なすべてを提供します。私はこのワークフローを信頼しています。ちゃんといい仕事をしてくれます。

これがGSDです。エンタープライズごっこは一切なし。Claude Codeを使って一貫してクールなものを作るための、非常に効果的なシステムです。

— **TÂCHES**

---

バイブコーディングは評判が悪い。やりたいことを説明し、AIがコードを生成し、スケールすると崩壊する一貫性のないゴミが出来上がる。

GSDはそれを解決します。Claude Codeを信頼性の高いものにするコンテキストエンジニアリングレイヤーです。アイデアを説明し、システムに必要なすべてを抽出させ、Claude Codeに仕事をさせましょう。

---

## こんな人のために

やりたいことを説明するだけで正しく構築してほしい人 — 50人のエンジニア組織を運営しているふりをせずに。

ビルトインの品質ゲートが本当の問題を検出します：スキーマドリフト検出はマイグレーション漏れのORM変更をフラグし、セキュリティ強制は検証を脅威モデルに紐付け、スコープ削減検出はプランナーが要件を暗黙的に落とすのを防止します。

### v1.39.0 ハイライト

完全なリストは [v1.39.0 リリースノート](https://github.com/gsd-build/get-shit-done/releases/tag/v1.39.0) を参照してください。

- **`--minimal` インストールプロファイル** — エイリアス `--core-only`。メインループの6スキル（`new-project`、`discuss-phase`、`plan-phase`、`execute-phase`、`help`、`update`）のみをインストールし、`gsd-*` サブエージェントはゼロ。コールドスタート時のシステムプロンプトのオーバーヘッドを ~12kトークンから ~700トークンへ削減（≥94%減）。32K〜128Kコンテキストのローカル LLM やトークン課金 API に有効。
- **`/gsd-phase --edit`** — `ROADMAP.md` 上の既存フェーズの任意フィールドをその場で編集（番号や位置は変更されない）。`--force` で確認 diff をスキップ、`depends_on` の参照を検証し、書き込み時に `STATE.md` も更新。
- **マージ後ビルド & テストゲート** — `execute-phase` のステップ 5.6 が `workflow.build_command` の設定を自動検出し、無ければ Xcode（`.xcodeproj`）、Makefile、Justfile、Cargo、Go、Python、npm の順にフォールバック。Xcode/iOS プロジェクトでは `xcodebuild build` と `xcodebuild test` を自動実行。並列・直列両モードで動作。
- **ランタイム別レビューモデル選択** — `review.models.<cli>` で各外部レビュー CLI（codex、gemini など）が使うモデルをプランナー/実行プロファイルとは独立に指定可能。
- **ワークストリーム設定の継承** — `GSD_WORKSTREAM` が設定されている場合、ルートの `.planning/config.json` を先に読み込み、ワークストリーム設定をディープマージ（衝突時はワークストリーム側が優先）。ワークストリーム設定で明示的に `null` を指定するとルート値を上書き可能。
- **手動カナリアリリースワークフロー** — `.github/workflows/canary.yml` が `workflow_dispatch` 経由で `dev` ブランチから `{base}-canary.{N}` ビルドを `@canary` dist-tag に手動公開（`get-shit-done-cc` と `@gsd-build/sdk`）。
- **スキルの統合：86 → 59** — 4つの新しいグループ化スキル（`capture`、`phase`、`config`、`workspace`）が31のマイクロスキルを吸収。既存の親スキル6つはラップアップやサブ操作をフラグ化：`update --sync/--reapply`、`sketch --wrap-up`、`spike --wrap-up`、`map-codebase --fast/--query`、`code-review --fix`、`progress --do/--next`。機能の欠損なし。

---

## はじめに

```bash
npx get-shit-done-cc@latest
```

インストーラーが以下の選択を求めます：
1. **ランタイム** — Claude Code、OpenCode、Gemini、Kilo、Codex、Copilot、Cursor、Windsurf、Antigravity、Augment、Trae、Cline、またはすべて（インタラクティブ複数選択 — 1回のインストールセッションで複数のランタイムを選択可能）
2. **インストール先** — グローバル（全プロジェクト）またはローカル（現在のプロジェクトのみ）

確認方法：
- Claude Code / Gemini / Copilot / Antigravity: `/gsd-help`
- OpenCode / Kilo / Augment / Trae: `/gsd-help`
- Codex: `$gsd-help`
- Cline: GSDは`.clinerules`経由でインストール — `.clinerules`の存在を確認

> [!NOTE]
> Claude Code 2.1.88+とCodexはスキル（`skills/gsd-*/SKILL.md`）としてインストールされます。Clineは`.clinerules`を使用します。インストーラーがすべての形式を自動的に処理します。

> [!TIP]
> ソースベースのインストールやnpmが利用できない環境については、**[docs/manual-update.md](docs/manual-update.md)**を参照してください。

### 最新の状態を保つ

GSDは急速に進化しています。定期的にアップデートしてください：

```bash
npx get-shit-done-cc@latest
```

<details>
<summary><strong>非インタラクティブインストール（Docker、CI、スクリプト）</strong></summary>

```bash
# Claude Code
npx get-shit-done-cc --claude --global   # ~/.claude/ にインストール
npx get-shit-done-cc --claude --local    # ./.claude/ にインストール

# OpenCode
npx get-shit-done-cc --opencode --global # ~/.config/opencode/ にインストール

# Gemini CLI
npx get-shit-done-cc --gemini --global   # ~/.gemini/ にインストール

# Kilo
npx get-shit-done-cc --kilo --global     # ~/.config/kilo/ にインストール
npx get-shit-done-cc --kilo --local      # ./.kilo/ にインストール

# Codex
npx get-shit-done-cc --codex --global    # ~/.codex/ にインストール
npx get-shit-done-cc --codex --local     # ./.codex/ にインストール

# Copilot
npx get-shit-done-cc --copilot --global  # ~/.github/ にインストール
npx get-shit-done-cc --copilot --local   # ./.github/ にインストール

# Cursor CLI
npx get-shit-done-cc --cursor --global      # ~/.cursor/ にインストール
npx get-shit-done-cc --cursor --local       # ./.cursor/ にインストール

# Antigravity
npx get-shit-done-cc --antigravity --global # ~/.gemini/antigravity/ にインストール
npx get-shit-done-cc --antigravity --local  # ./.agent/ にインストール

# Augment
npx get-shit-done-cc --augment --global     # ~/.augment/ にインストール
npx get-shit-done-cc --augment --local      # ./.augment/ にインストール

# Trae
npx get-shit-done-cc --trae --global        # ~/.trae/ にインストール
npx get-shit-done-cc --trae --local         # ./.trae/ にインストール

# Cline
npx get-shit-done-cc --cline --global       # ~/.cline/ にインストール
npx get-shit-done-cc --cline --local        # ./.clinerules にインストール

# 全ランタイム
npx get-shit-done-cc --all --global      # すべてのディレクトリにインストール
```

`--global`（`-g`）または `--local`（`-l`）でインストール先の質問をスキップできます。
`--claude`、`--opencode`、`--gemini`、`--kilo`、`--codex`、`--copilot`、`--cursor`、`--windsurf`、`--antigravity`、`--augment`、`--trae`、`--cline`、または `--all` でランタイムの質問をスキップできます。

</details>

<details>
<summary><strong>開発用インストール</strong></summary>

リポジトリをクローンしてインストーラーをローカルで実行します：

```bash
git clone https://github.com/gsd-build/get-shit-done.git
cd get-shit-done
node bin/install.js --claude --local
```

コントリビュートする前に変更をテストするため、`./.claude/` にインストールされます。

</details>

### 推奨：パーミッションスキップモード

GSDは摩擦のない自動化のために設計されています。Claude Codeを以下のように実行してください：

```bash
claude --dangerously-skip-permissions
```

> [!TIP]
> これがGSDの意図された使い方です — `date` や `git commit` を50回も承認するために止まっていては目的が台無しです。

<details>
<summary><strong>代替案：詳細なパーミッション設定</strong></summary>

このフラグを使いたくない場合は、プロジェクトの `.claude/settings.json` に以下を追加してください：

```json
{
  "permissions": {
    "allow": [
      "Bash(date:*)",
      "Bash(echo:*)",
      "Bash(cat:*)",
      "Bash(ls:*)",
      "Bash(mkdir:*)",
      "Bash(wc:*)",
      "Bash(head:*)",
      "Bash(tail:*)",
      "Bash(sort:*)",
      "Bash(grep:*)",
      "Bash(tr:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git status:*)",
      "Bash(git log:*)",
      "Bash(git diff:*)",
      "Bash(git tag:*)"
    ]
  }
}
```

</details>

---

## 仕組み

> **既存のコードがある場合は？** まず `/gsd-map-codebase` を実行してください。並列エージェントが起動し、スタック、アーキテクチャ、規約、懸念点を分析します。その後 `/gsd-new-project` がコードベースを把握した状態で動作し、質問は追加する内容に焦点を当て、計画時にはパターンが自動的に読み込まれます。

### 1. プロジェクトの初期化

```
/gsd-new-project
```

1つのコマンド、1つのフロー。システムが以下を行います：

1. **質問** — アイデアを完全に理解するまで質問します（目標、制約、技術的な好み、エッジケース）
2. **リサーチ** — 並列エージェントが起動しドメインを調査します（オプションですが推奨）
3. **要件定義** — v1、v2、スコープ外を抽出します
4. **ロードマップ** — 要件に紐づくフェーズを作成します

ロードマップを承認します。これでビルドの準備が整いました。

**作成されるファイル：** `PROJECT.md`、`REQUIREMENTS.md`、`ROADMAP.md`、`STATE.md`、`.planning/research/`

---

### 2. フェーズの議論

```
/gsd-discuss-phase 1
```

**ここで実装の方向性を決めます。**

ロードマップには各フェーズにつき1〜2文しかありません。あなたが*想像する*通りに構築するには十分なコンテキストではありません。このステップでは、リサーチや計画の前にあなたの好みを記録します。

システムがフェーズを分析し、構築内容に基づいてグレーゾーンを特定します：

- **ビジュアル機能** → レイアウト、密度、インタラクション、空状態
- **API/CLI** → レスポンス形式、フラグ、エラーハンドリング、詳細度
- **コンテンツシステム** → 構造、トーン、深さ、フロー
- **整理タスク** → グルーピング基準、命名、重複、例外

選択した各領域について、あなたが満足するまで質問します。出力される `CONTEXT.md` は、次の2つのステップに直接反映されます：

1. **リサーチャーが読む** — どんなパターンを調査すべきかを把握（「ユーザーはカードレイアウトを希望」→ カードコンポーネントライブラリを調査）
2. **プランナーが読む** — どの決定が確定済みかを把握（「無限スクロールに決定」→ スクロール処理を計画に含める）

ここで深く掘り下げるほど、システムはあなたが本当に望むものを構築します。スキップすれば妥当なデフォルトが使われます。活用すれば*あなたのビジョン*が反映されます。

**作成されるファイル：** `{phase_num}-CONTEXT.md`

> **前提モード：** 質問よりもコードベース分析を優先したい場合は、`/gsd-settings` で `workflow.discuss_mode` を `assumptions` に設定してください。システムがコードを読み、何をなぜそうするかを提示し、間違っている部分だけ修正を求めます。詳しくは[ディスカスモード](docs/ja-JP/workflow-discuss-mode.md)をご覧ください。

---

### 3. フェーズの計画

```
/gsd-plan

# FILE: README.md

<div align="center">

# GET SHIT DONE

**English** · [Português](README.pt-BR.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja-JP.md) · [한국어](README.ko-KR.md)

**A light-weight meta-prompting, context engineering, and spec-driven development system for Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more.**

**Solves context rot — the quality degradation that happens as your AI fills its context window.**

[![npm version](https://img.shields.io/npm/v/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![npm downloads](https://img.shields.io/npm/dm/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![Tests](https://img.shields.io/github/actions/workflow/status/gsd-build/get-shit-done/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/gsd-build/get-shit-done/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![X (Twitter)](https://img.shields.io/badge/X-@gsd__foundation-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/gsd_foundation)
[![$GSD Token](https://img.shields.io/badge/$GSD-Dexscreener-1C1C1C?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgZmlsbD0iIzAwRkYwMCIvPjwvc3ZnPg==&logoColor=00FF00)](https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv)
[![GitHub stars](https://img.shields.io/github/stars/gsd-build/get-shit-done?style=for-the-badge&logo=github&color=181717)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<br>

```bash
npx get-shit-done-cc@latest
```

**Works on Mac, Windows, and Linux.**

<br>

![GSD Install](assets/terminal.svg)

<br>

*"If you know clearly what you want, this WILL build it for you. No bs."*

*"I've done SpecKit, OpenSpec and Taskmaster — this has produced the best results for me."*

*"By far the most powerful addition to my Claude Code. Nothing over-engineered. Literally just gets shit done."*

<br>

**Trusted by engineers at Amazon, Google, Shopify, and Webflow.**

</div>

---

> [!IMPORTANT]
> **Returning to GSD?**
>
> Run `/gsd-map-codebase` to re-index your codebase, then `/gsd-new-project` to rebuild GSD's planning context. Your code is fine — GSD just needs its context rebuilt. See the [CHANGELOG](CHANGELOG.md) for what's new.

---

## Why I Built This

I'm a solo developer. I don't write code — Claude Code does.

Other spec-driven tools exist, but they're all built for 50-person engineering orgs — sprint ceremonies, story points, stakeholder syncs, Jira workflows. I'm not that. I'm a creative person trying to build great things consistently.

So I built GSD. The complexity is in the system, not in your workflow. Behind the scenes: context engineering, XML prompt formatting, subagent orchestration, state management. What you see: a few commands that just work.

The system gives Claude everything it needs to do the work *and* verify it. I trust the workflow. It just does a good job.

— **TÂCHES**

---

## How It Works

The loop is six commands. Each one does exactly one thing.

### 1. Initialize

```bash
/gsd-new-project
```

Questions → research → requirements → roadmap. You approve it, then you're ready to build.

> **Already have code?** Run `/gsd-map-codebase` first. It analyzes your stack, architecture, and conventions so `/gsd-new-project` asks the right questions.

### 2. Discuss

```bash
/gsd-discuss-phase 1
```

Your roadmap has a sentence per phase. That's not enough to build it the way *you* imagine it. Discuss captures your decisions before anything gets planned: layouts, API shapes, error handling, data structures — whatever gray areas exist for this specific phase.

The output feeds directly into research and planning. Skip it, get reasonable defaults. Use it, get your vision.

### 3. Plan

```bash
/gsd-plan-phase 1
```

Research → plan → verify, in a loop until the plans pass. Each plan is small enough to execute in a fresh context window.

### 4. Execute

```bash
/gsd-execute-phase 1
```

Plans run in parallel waves. Each executor gets a fresh 200k-token context. Each task gets its own atomic commit. Walk away, come back to completed work with a clean git history.

Your main context window stays at 30–40%. The work happens in the subagents.

### 5. Verify

```bash
/gsd-verify-work 1
```

Walk through what was built. Anything broken gets a diagnosed fix plan — ready for immediate re-execution. You don't debug manually; you just run execute again.

### 6. Repeat → Ship

```bash
/gsd-ship 1
/gsd-complete-milestone
/gsd-new-milestone
```

Loop discuss → plan → execute → verify → ship until the milestone is done. Then archive, tag, and start the next one fresh.

---

## Getting Started

```bash
npx get-shit-done-cc@latest
```

The installer prompts for your runtime (Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, and more) and whether to install globally or locally.

```bash
claude --dangerously-skip-permissions
```

GSD is built for frictionless automation. Skip-permissions is how it's intended to run.

See **[docs/USER-GUIDE.md](docs/USER-GUIDE.md)** for the full walkthrough, non-interactive install flags for all 15 runtimes, minimal install (`--minimal`), Docker setup, and permissions configuration.

---

## Commands

The main loop:

| Command | What it does |
|---------|--------------|
| `/gsd-new-project` | Questions → research → requirements → roadmap |
| `/gsd-discuss-phase [N]` | Capture implementation decisions before planning |
| `/gsd-plan-phase [N]` | Research + plan + verify |
| `/gsd-execute-phase <N>` | Execute plans in parallel waves |
| `/gsd-verify-work [N]` | Manual acceptance testing |
| `/gsd-ship [N]` | Create PR from verified phase work |
| `/gsd-progress --next` | Auto-detect and run the next step |
| `/gsd-complete-milestone` | Archive milestone and tag release |
| `/gsd-new-milestone` | Start next version |

For ad-hoc tasks, autonomous mode, codebase analysis, forensics, and the full command surface — see **[docs/COMMANDS.md](docs/COMMANDS.md)**.

---

## Why It Works

Three things most AI-coding setups get wrong:

**1. Context bloat.** As a session grows, quality degrades. GSD keeps your main context clean by doing the heavy work in fresh subagent contexts. Researchers, planners, and executors each start fresh with exactly what they need.

**2. No shared memory.** GSD maintains structured artifacts that survive session boundaries: `PROJECT.md` (vision), `REQUIREMENTS.md` (scope), `ROADMAP.md` (where you're going), `STATE.md` (current position and decisions), `CONTEXT.md` (per-phase implementation decisions). Every new session loads these and knows exactly where things stand.

**3. No verification.** Code that "runs" isn't code that "works." GSD's verify step walks you through what was built, diagnoses failures with dedicated debug agents, and generates fix plans before you declare a phase done.

See **[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)** for how the multi-agent orchestration and context engineering work in detail.

---

## Configuration

Settings live in `.planning/config.json`. Configure during `/gsd-new-project` or update with `/gsd-settings`.

Key dials:

| Setting | What it controls |
|---------|-----------------|
| `mode` | `interactive` (confirm each step) or `yolo` (auto-approve) |
| Model profiles | `quality` / `balanced` / `budget` — controls which model each agent uses |
| `workflow.research` / `plan_check` / `verifier` | Toggle the quality agents that add tokens and time |
| `parallelization.enabled` | Run independent plans simultaneously |

For the full configuration reference — all settings, git branching strategies, per-runtime model overrides, workstream config inheritance, agent skills injection — see **[docs/CONFIGURATION.md](docs/CONFIGURATION.md)**.

---

## Documentation

| Doc | What's in it |
|-----|-------------|
| [User Guide](docs/USER-GUIDE.md) | End-to-end walkthrough, install options, all runtime flags, configuration reference |
| [Commands](docs/COMMANDS.md) | Every command with flags and examples |
| [Configuration](docs/CONFIGURATION.md) | Full config schema, model profiles, git branching |
| [Architecture](docs/ARCHITECTURE.md) | How the multi-agent orchestration works |
| [CLI Tools](docs/CLI-TOOLS.md) | `gsd-sdk query` and programmatic SDK dispatch seams |
| [Features](docs/FEATURES.md) | Complete feature index |
| [Changelog](CHANGELOG.md) | What changed in each release |

---

## Troubleshooting

**Commands not showing up?** Restart your runtime after install. GSD installs to `~/.claude/skills/gsd-*/` (Claude Code), `~/.codex/skills/gsd-*/` (Codex), or the equivalent for your runtime.

**Something broken?** Re-run the installer — it's idempotent:
```bash
npx get-shit-done-cc@latest
```

**Containers or Docker?** Set `CLAUDE_CONFIG_DIR` before installing to avoid tilde-expansion issues:
```bash
CLAUDE_CONFIG_DIR=/home/youruser/.claude npx get-shit-done-cc --global
```

Full troubleshooting and uninstall instructions in **[docs/USER-GUIDE.md](docs/USER-GUIDE.md#troubleshooting)**.

---

## Community

| Project | Platform |
|---------|----------|
| [gsd-opencode](https://github.com/rokicool/gsd-opencode) | Original OpenCode port |
| [Discord](https://discord.gg/mYgfVNfA2r) | Community support |

---

## Star History

<a href="https://star-history.com/#gsd-build/get-shit-done&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=gsd-build/get-shit-done&type=Date&theme=dark" />
   <source 

# FILE: README.pt-BR.md

<div align="center">

# GET SHIT DONE

[English](README.md) · **Português** · [简体中文](README.zh-CN.md) · [日本語](README.ja-JP.md)

**Um sistema leve e poderoso de meta-prompting, engenharia de contexto e desenvolvimento orientado a especificação para Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae e Cline.**

**Resolve context rot — a degradação de qualidade que acontece conforme o Claude enche a janela de contexto.**

[![npm version](https://img.shields.io/npm/v/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![npm downloads](https://img.shields.io/npm/dm/get-shit-done-cc?style=for-the-badge&logo=npm&logoColor=white&color=CB3837)](https://www.npmjs.com/package/get-shit-done-cc)
[![Tests](https://img.shields.io/github/actions/workflow/status/gsd-build/get-shit-done/test.yml?branch=main&style=for-the-badge&logo=github&label=Tests)](https://github.com/gsd-build/get-shit-done/actions/workflows/test.yml)
[![Discord](https://img.shields.io/badge/Discord-Join-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/mYgfVNfA2r)
[![X (Twitter)](https://img.shields.io/badge/X-@gsd__foundation-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/gsd_foundation)
[![$GSD Token](https://img.shields.io/badge/$GSD-Dexscreener-1C1C1C?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgZmlsbD0iIzAwRkYwMCIvPjwvc3ZnPg==&logoColor=00FF00)](https://dexscreener.com/solana/dwudwjvan7bzkw9zwlbyv6kspdlvhwzrqy6ebk8xzxkv)
[![GitHub stars](https://img.shields.io/github/stars/gsd-build/get-shit-done?style=for-the-badge&logo=github&color=181717)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)

<br>

```bash
npx get-shit-done-cc@latest
```

**Funciona em Mac, Windows e Linux.**

<br>

![GSD Install](assets/terminal.svg)

<br>

*"Se você sabe claramente o que quer, isso VAI construir para você. Sem enrolação."*

*"Eu já usei SpecKit, OpenSpec e Taskmaster — este me deu os melhores resultados."*

*"De longe a adição mais poderosa ao meu Claude Code. Nada superengenheirado. Simplesmente faz o trabalho."*

<br>

**Confiado por engenheiros da Amazon, Google, Shopify e Webflow.**

[Por que eu criei isso](#por-que-eu-criei-isso) · [Como funciona](#como-funciona) · [Comandos](#comandos) · [Por que funciona](#por-que-funciona) · [Guia do usuário](docs/pt-BR/USER-GUIDE.md)

</div>

---

## Por que eu criei isso

Sou desenvolvedor solo. Eu não escrevo código — o Claude Code escreve.

Existem outras ferramentas de desenvolvimento orientado por especificação. BMAD, Speckit... Mas quase todas parecem mais complexas do que o necessário (cerimônias de sprint, story points, sync com stakeholders, retrospectivas, fluxos Jira) ou não entendem de verdade o panorama do que você está construindo. Eu não sou uma empresa de software com 50 pessoas. Não quero teatro corporativo. Só quero construir coisas boas que funcionem.

Então eu criei o GSD. A complexidade fica no sistema, não no seu fluxo. Por trás: engenharia de contexto, formatação XML de prompts, orquestração de subagentes, gerenciamento de estado. O que você vê: alguns comandos que simplesmente funcionam.

O sistema dá ao Claude tudo que ele precisa para fazer o trabalho *e* validar o resultado. Eu confio no fluxo. Ele entrega.

— **TÂCHES**

---

Vibe coding ganhou má fama. Você descreve algo, a IA gera código, e sai um resultado inconsistente que quebra em escala.

O GSD corrige isso. É a camada de engenharia de contexto que torna o Claude Code confiável.

---

## Para quem é

Para quem quer descrever o que precisa e receber isso construído do jeito certo — sem fingir que está rodando uma engenharia de 50 pessoas.

Quality gates embutidos capturam problemas reais: detecção de schema drift sinaliza mudanças ORM sem migrations, segurança ancora verificação a modelos de ameaça, e detecção de redução de escopo impede o planner de descartar requisitos silenciosamente.

### Destaques v1.39.0

Lista completa nas [notas de release v1.39.0](https://github.com/gsd-build/get-shit-done/releases/tag/v1.39.0).

- **Perfil de instalação `--minimal`** — alias `--core-only`. Instala apenas os 6 skills do loop principal (`new-project`, `discuss-phase`, `plan-phase`, `execute-phase`, `help`, `update`) e nenhum subagente `gsd-*`. Reduz o overhead do system prompt no cold-start de ~12k para ~700 tokens (≥94% de redução). Útil para LLMs locais com contexto de 32K–128K e APIs cobradas por token.
- **`/gsd-phase --edit`** — edita qualquer campo de uma fase existente em `ROADMAP.md` no lugar, sem alterar o número ou a posição. `--force` pula o diff de confirmação; referências em `depends_on` são validadas e o `STATE.md` é atualizado na escrita.
- **Build & test gate pós-merge** — o passo 5.6 de `execute-phase` agora detecta automaticamente o comando de build em `workflow.build_command`, com fallback para Xcode (`.xcodeproj`), Makefile, Justfile, Cargo, Go, Python ou npm. Projetos Xcode/iOS rodam `xcodebuild build` e `xcodebuild test` automaticamente. Funciona em modo paralelo e serial.
- **Modelo de review por runtime** — `review.models.<cli>` permite que cada CLI externa de review (codex, gemini, etc.) escolha seu próprio modelo, independente do perfil de planner/executor.
- **Herança de configuração de workstream** — quando `GSD_WORKSTREAM` está definido, o `.planning/config.json` raiz é carregado primeiro e merge-deep com o config da workstream (workstream vence em conflito). Um `null` explícito no config da workstream sobrescreve corretamente o valor raiz.
- **Workflow manual de canary release** — `.github/workflows/canary.yml` publica builds `{base}-canary.{N}` de `get-shit-done-cc` e `@gsd-build/sdk` na dist-tag `@canary` a partir de `dev`, sob demanda via `workflow_dispatch`.
- **Consolidação de skills: 86 → 59** — 4 novos skills agrupados (`capture`, `phase`, `config`, `workspace`) absorvem 31 micro-skills. 6 skills pais existentes absorvem wrap-up e sub-operações como flags: `update --sync/--reapply`, `sketch --wrap-up`, `spike --wrap-up`, `map-codebase --fast/--query`, `code-review --fix`, `progress --do/--next`. Sem perda funcional.

---

## Primeiros passos

```bash
npx get-shit-done-cc@latest
```

O instalador pede:
1. **Runtime** — Claude Code, OpenCode, Gemini, Kilo, Codex, Copilot, Cursor, Windsurf, Antigravity, Augment, Trae, Cline, ou todos
2. **Local** — Global (todos os projetos) ou local (apenas projeto atual)

Verifique com:
- Claude Code / Gemini / Copilot / Antigravity: `/gsd-help`
- OpenCode / Kilo / Augment / Trae: `/gsd-help`
- Codex: `$gsd-help`
- Cline: GSD instala via `.clinerules` — verifique se `.clinerules` existe

> [!NOTE]
> Claude Code 2.1.88+ e Codex instalam como skills (`skills/gsd-*/SKILL.md`). Cline usa `.clinerules`. O instalador lida com todos os formatos automaticamente.

> [!TIP]
> Para instalação a partir do código-fonte ou ambientes sem npm, consulte **[docs/manual-update.md](docs/manual-update.md)**.

### Mantendo atualizado

```bash
npx get-shit-done-cc@latest
```

<details>
<summary><strong>Instalação não interativa (Docker, CI, Scripts)</strong></summary>

```bash
# Claude Code
npx get-shit-done-cc --claude --global
npx get-shit-done-cc --claude --local

# OpenCode
npx get-shit-done-cc --opencode --global

# Gemini CLI
npx get-shit-done-cc --gemini --global

# Kilo
npx get-shit-done-cc --kilo --global
npx get-shit-done-cc --kilo --local

# Codex
npx get-shit-done-cc --codex --global
npx get-shit-done-cc --codex --local

# Copilot
npx get-shit-done-cc --copilot --global
npx get-shit-done-cc --copilot --local

# Cursor
npx get-shit-done-cc --cursor --global
npx get-shit-done-cc --cursor --local

# Antigravity
npx get-shit-done-cc --antigravity --global
npx get-shit-done-cc --antigravity --local

# Augment
npx get-shit-done-cc --augment --global     # Install to ~/.augment/
npx get-shit-done-cc --augment --local      # Install to ./.augment/

# Trae
npx get-shit-done-cc --trae --global        # Install to ~/.trae/
npx get-shit-done-cc --trae --local         # Install to ./.trae/

# Cline
npx get-shit-done-cc --cline --global       # Install to ~/.cline/
npx get-shit-done-cc --cline --local        # Install to ./.clinerules

# Todos
npx get-shit-done-cc --all --global
```

Use `--global` (`-g`) ou `--local` (`-l`) para pular a pergunta de local.
Use `--claude`, `--opencode`, `--gemini`, `--kilo`, `--codex`, `--copilot`, `--cursor`, `--windsurf`, `--antigravity`, `--augment`, `--trae`, `--cline` ou `--all` para pular a pergunta de runtime.

</details>

### Recomendado: modo sem permissões

```bash
claude --dangerously-skip-permissions
```

> [!TIP]
> Esse é o modo pensado para o GSD: aprovar `date` e `git commit` 50 vezes mata a produtividade.

---

## Como funciona

> **Já tem código?** Rode `/gsd-map-codebase` primeiro para analisar stack, arquitetura, convenções e riscos.

### 1. Inicializar projeto

```
/gsd-new-project
```

O sistema:
1. **Pergunta** até entender seu objetivo
2. **Pesquisa** o domínio com agentes em paralelo
3. **Extrai requisitos** (v1, v2 e fora de escopo)
4. **Monta roadmap** por fases

**Cria:** `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `.planning/research/`

### 2. Discutir fase

```
/gsd-discuss-phase 1
```

Captura suas preferências de implementação antes do planejamento.

**Cria:** `{phase_num}-CONTEXT.md`

### 3. Planejar fase

```
/gsd-plan-phase 1
```

1. Pesquisa abordagens
2. Cria 2-3 planos atômicos em XML
3. Verifica contra os requisitos

**Cria:** `{phase_num}-RESEARCH.md`, `{phase_num}-{N}-PLAN.md`

### 4. Executar fase

```
/gsd-execute-phase 1
```

1. Executa planos em ondas
2. Contexto novo por plano
3. Commit atômic

# FILE: docs/RELEASE-v1.39.0-rc.7.md

# v1.39.0-rc.7 Release Notes

Pre-release candidate. Published to npm under the `next` tag.

```bash
npx get-shit-done-cc@next
```

---

## What's in this release

rc.7 is the first RC in the 1.39.0 train that rolls in the post-rc.5 fixes from
`main`. rc.6 was content-identical to rc.5 (`release/1.39.0` was bumped without
first being merged with `main` — see [#2856](https://github.com/gsd-build/get-shit-done/issues/2856)).
rc.7 syncs the release branch with `main` so all of the work below actually
reaches the registry.

### Added

- **Manual canary release workflow** — `.github/workflows/canary.yml` publishes
  `{base}-canary.{N}` builds of `get-shit-done-cc` under the `canary` dist-tag on
  demand via `workflow_dispatch` (manual trigger only). Optional `dry_run` boolean.
  ([#2828](https://github.com/gsd-build/get-shit-done/issues/2828))

### Fixed

- **`extractCurrentMilestone` no longer truncates ROADMAP.md at heading-like lines
  inside fenced code blocks** — the milestone-end search now scans line-by-line while
  tracking ` ``` ` / `~~~` fence state, so a line like `# Ops runbook (v1.0 compat)`
  inside a code block no longer acts as a milestone boundary.
  ([#2787](https://github.com/gsd-build/get-shit-done/issues/2787))
- **`audit-uat` parser reads `human_verification:` from frontmatter array** — the
  previous body-only regex was too strict and missed valid UAT items declared in
  YAML frontmatter, surfacing false-positive open gaps at every milestone-completion
  audit. ([#2788](https://github.com/gsd-build/get-shit-done/issues/2788))
- **Skill description anti-patterns trimmed; ≤ 100-char budget enforced** — three
  anti-patterns eliminated across `commands/gsd/*.md`: flag documentation already in
  `argument-hint:`, `Triggers:` keyword-stuffing lists, and numbered enumeration. New
  CI lint gate `npm run lint:descriptions` fails if any description exceeds 100
  chars. ([#2789](https://github.com/gsd-build/get-shit-done/issues/2789))
- **`gsd-sdk` binary collision with `@gsd-build/sdk` resolved** — workstream-aware
  query registry now respects the `GSD_WORKSTREAM` env var; `gsd-tools` bin alias
  added. ([#2791](https://github.com/gsd-build/get-shit-done/issues/2791))
- **`OpenCode` agents embed `model_profile_overrides.opencode.<tier>`** — per-tier
  model overrides set via `/gsd-settings-advanced` are now propagated into generated
  agent files. ([#2794](https://github.com/gsd-build/get-shit-done/issues/2794))
- **`roadmap update-plan-progress` accepts `--phase` flag form** — SDK arg-parsing
  regression in v0.1.0 silently dropped `--phase`/`--name`/`--plans` flags, causing
  STATE.md corruption. ([#2796](https://github.com/gsd-build/get-shit-done/issues/2796))
- **`context_window` added to `VALID_CONFIG_KEYS` allowlist** —
  `/gsd-settings-advanced` could not set `context_window` because the key was missing
  from the allowlist used by `config-set` validation.
  ([#2798](https://github.com/gsd-build/get-shit-done/issues/2798))
- **`gsd-tools init` dispatches `ingest-docs` handler** — `/gsd-ingest-docs` was
  broken in v1.38.5 because the workflow called the new tool but no `ingest-docs`
  init handler was registered. ([#2801](https://github.com/gsd-build/get-shit-done/issues/2801))
- **`config-get` honors `--default <value>` flag** — fallback for missing keys
  ported from CJS into the SDK. ([#2803](https://github.com/gsd-build/get-shit-done/issues/2803))
- **`find-phase` returns `null` for archived phases** — when the current-milestone
  phase had no directory yet, `init.plan-phase` / `init.execute-phase` returned the
  archived prior-milestone directory instead of `null`, causing wrong-phase work.
  ([#2805](https://github.com/gsd-build/get-shit-done/issues/2805))
- **SKILL.md frontmatter `name:` migrated to hyphen form** — files that still used
  the deprecated colon form (`gsd:cmd`) caused autocomplete to suggest `/gsd:command`.
  ([#2808](https://github.com/gsd-build/get-shit-done/issues/2808))
- **`gsd-sdk` resolvable in local-mode installs** — the previous `isLocal`
  short-circuit returned before the PATH probe + self-link could run. When
  `sdk/dist/cli.js` is present, local installs now run the same probe-and-link flow
  as global installs. ([#2829](https://github.com/gsd-build/get-shit-done/issues/2829))
- **OpenCode `@file` references use absolute paths on all platforms** — OpenCode
  does not shell-expand `$HOME` in `@file` references on any platform; the
  Windows-only guard from #2376 left macOS/Linux producing literal `@$HOME/...`
  strings. Guard now applies unconditionally for OpenCode.
  ([#2831](https://github.com/gsd-build/get-shit-done/issues/2831))
- **`gsd-sdk auto` detects Codex runtime correctly** — `auto` mode ignored
  `runtime: codex` and routed through `@anthropic-ai/claude-agent-sdk`, producing
  the `[FAILED] $0.00 0.1s` symptom on autonomous runs. New `runtime-gate` raises a
  clear error for non-Claude runtimes; `resolveModel()` honours `GSD_RUNTIME` env
  precedence and never injects a Claude profile id under non-Claude runtimes.
  ([#2832](https://github.com/gsd-build/get-shit-done/issues/2832))
- **CR-INTEGRATION tests aligned with hyphen-form skill names** — tests now parse
  `Skill(skill="...")` invocations structurally and reject the legacy colon form.
  ([#2835](https://github.com/gsd-build/get-shit-done/issues/2835))
- **`audit-open` quick-task scanner accepts `${quick_id}-SUMMARY.md`** — the
  bare-`SUMMARY.md` check produced false-positive `status: missing` for every
  documented quick task. UAT terminal-status enum also adds `resolved` (matches
  `execute-phase.md`'s post-gap-closure terminal).
  ([#2836](https://github.com/gsd-build/get-shit-done/issues/2836))
- **`quick.md` / `execute-phase.md` SUMMARY rescue handles gitignored `.planning/`** —
  rescue blocks used `git ls-files --exclude-standard`, silently no-op'ing when
  `.planning/` was excluded; the worktree was then deleted with the SUMMARY.
  Replaced with filesystem-le

# FILE: docs/RELEASE-v1.41.0.md

# v1.41.0 Release Notes

Stable release. Published to npm under the `latest` tag.

```bash
npx get-shit-done-cc@latest
```

---

## What's in this release

1.41.0 is a quality and infrastructure release. The headline additions are **per-phase-type model selection** and **dynamic routing** — two new config blocks that give you granular cost control without learning the agent taxonomy. The release also ships the **MVP mode SDK resolution layer** (three canonical query verbs replacing per-workflow bash duplication), the **optional update banner** for non-statusline users, and the **issue-driven orchestration guide**. Underneath that, 25+ correctness fixes cover Homebrew node path stability, planner directive fidelity, secure-phase retroactive audit, cross-runtime installs, and statusline parsing.

### Added

- **Per-phase-type model selection (`models` block)** — express "Opus for planning,
  Sonnet for the rest" in two config lines without learning the agent taxonomy. Six
  named slots (`planning` / `discuss` / `research` / `execution` / `verification` /
  `completion`) accept tier aliases (`opus` / `sonnet` / `haiku` / `inherit`). Fully
  backward compatible.
  ([#3023](https://github.com/gsd-build/get-shit-done/pull/3030))

- **Dynamic routing with failure-tier escalation (`dynamic_routing` block)** — start
  cheap, escalate only when the orchestrator detects a soft failure (inconclusive
  verification, plan-check FLAG). Disabled by default; composes with `model_overrides`
  and `models.<phase_type>` via the same precedence chain.
  ([#3024](https://github.com/gsd-build/get-shit-done/pull/3031))

- **Optional update banner for non-GSD statusline users** — when the installer detects
  no GSD statusline, it offers an opt-in `SessionStart` hook that surfaces update
  availability via the existing `~/.cache/gsd/gsd-update-check.json` cache. Silent when
  up-to-date; removed cleanly by `--uninstall`.
  ([#2795](https://github.com/gsd-build/get-shit-done/pull/2795))

- **Issue-driven orchestration guide** — new
  [`docs/issue-driven-orchestration.md`](issue-driven-orchestration.md) recipe that maps
  tracker issues (GitHub / Linear / Jira) onto existing GSD primitives: workspace →
  discuss → plan → execute → verify → review → ship.
  ([#2840](https://github.com/gsd-build/get-shit-done/pull/2840))

### Changed

- **MVP mode SDK resolution layer — three canonical query verbs** — three new verbs
  centralize the MVP-mode predicates previously duplicated across workflows:
  `gsd-sdk query phase.mvp-mode <N>` (precedence resolver), `task.is-behavior-adding`
  (Behavior-Adding Task predicate), and `user-story.validate` (User Story regex). All
  consuming workflows now call the verb instead of inlining 4–8 bash lines each. Also
  fixes a silent SDK bug where `roadmap.get-phase --pick mode` returned `null` for
  phases with `**Mode:** mvp` set.
  ([#3178](https://github.com/gsd-build/get-shit-done/pull/3178))

- **`/gsd-graphify status` surfaces commit-based staleness** — reads `built_at_commit`
  from graphify v0.7+ graphs, compares against `git HEAD`, and adds four new fields
  (`built_at_commit`, `current_commit`, `commits_behind`, `commit_stale`). Pre-v0.7
  graphs return `commit_stale: null` and fall back to the existing mtime-based signal.
  ([#3170](https://github.com/gsd-build/get-shit-done/issues/3170))

- **MVP concept index and domain glossary** — seven MVP-related terms added to
  `CONTEXT.md`; new `references/mvp-concepts.md` indexes the six MVP reference files.
  No behavior change.
  ([#3176](https://github.com/gsd-build/get-shit-done/pull/3176))

### Fixed

- **Stable node path on Homebrew** — `resolveNodeRunner()` now maps versioned Cellar
  paths to the stable Homebrew symlinks. Prevents `dyld: Library not loaded` errors
  after `brew upgrade node`.
  ([#3181](https://github.com/gsd-build/get-shit-done/issues/3181))

- **Milestone-archive layout support** — `validate consistency`, `validate health`, and
  `find-phase` now scan `.planning/milestones/v*-phases/` in addition to the flat
  `.planning/phases/` layout, eliminating spurious W006 warnings.
  ([#3164](https://github.com/gsd-build/get-shit-done/issues/3164))

- **`/gsd-graphify build` runs inline instead of spawning a sub-agent** — the
  post-extraction clustering phase was SIGTERM'd when the sub-agent exited, leaving no
  `graph.json` / `graph.html` / `GRAPH_REPORT.md` artifacts.
  ([#3166](https://github.com/gsd-build/get-shit-done/issues/3166))

- **Planner directive language restored** — 10 `CRITICAL`/`MANDATORY`/`MUST` emphasis
  markers were silently removed from `gsd-planner.md` in v1.38.4, weakening planner
  adherence to user decisions and requirement coverage. All restored.
  ([#3138](https://github.com/gsd-build/get-shit-done/issues/3087))

- **`secure-phase` retroactive-STRIDE mode for legacy phases** — phases with no
  `<threat_model>` blocks no longer rubber-stamp a clean `SECURITY.md`; the auditor
  now builds a register from implementation files before verifying mitigations.
  ([#3142](https://github.com/gsd-build/get-shit-done/issues/3120))

- **Global skills resolution now uses the correct runtime home directory** —
  `buildAgentSkillsBlock()` hardcoded `~/.claude/skills` for all runtimes. The new
  `runtime-homes.cjs` module maps all 15 supported runtimes to their canonical skills
  directory.
  ([#3126](https://github.com/gsd-build/get-shit-done/issues/3126))

- **`state.begin-phase` is now idempotent** — wave-resume calls no longer overwrite
  `Current Plan`, `stopped_at`, or `Last Activity Description` with stale values from
  the last `plan-phase` run.
  ([#3127](https://github.com/gsd-build/get-shit-done/issues/3127))

- **`gsd-validate-commit.sh` hook catches all git commit forms** — the previous bash
  regex missed `git -C /path commit`, `GIT_AUTHOR_NAME=x git commit`, and
  `/usr/bin/git commit`. New `hooks/lib/git-cmd.js` token-walk classifier handles all
  forms correctly.
  ([#3141](https://githu

# FILE: docs/RELEASE-v1.40.0-rc.1.md

# v1.40.0-rc.1 Release Notes

Pre-release candidate. Published to npm under the `next` tag.

```bash
npx get-shit-done-cc@next
```

---

## What's in this release

rc.1 opens the 1.40.0 train. The headline change is the **skill-surface
consolidation** ([#2790](https://github.com/gsd-build/get-shit-done/issues/2790))
and the new **two-stage hierarchical namespace routing** that sits on top of it
([#2792](https://github.com/gsd-build/get-shit-done/issues/2792)) — together
they drop the cold-start system-prompt overhead from ~2,150 tokens (86 flat skills)
to ~120 tokens (6 namespace routers). The release also adds the read-side of the
phase-lifecycle status-line, hardens multi-runtime installs, and clears a backlog of
correctness fixes for Gemini, Copilot, Codex, and the canary publish workflow.

### Added

- **Six namespace meta-skills with keyword-tag descriptions** — replace the flat
  86-skill listing with a two-stage hierarchical routing layer. The model sees 6
  namespace routers (`gsd:workflow`, `gsd:project`, `gsd:review`, `gsd:context`,
  `gsd:manage`, `gsd:ideate`) instead of 86 entries; selects a namespace, then routes
  to the sub-skill. Existing sub-skills are unchanged and still invocable directly.
  ([#2792](https://github.com/gsd-build/get-shit-done/issues/2792))

- **`/gsd-health --context` utilization guard** — context-window quality guard with
  two thresholds: 60 % warns ("consider `/gsd-thread`"), 70 % is critical ("reasoning
  quality may degrade"). Also exposed as `gsd-tools validate context`.
  ([#2792](https://github.com/gsd-build/get-shit-done/issues/2792))

- **Phase-lifecycle status-line — read-side** — `parseStateMd()` now reads four new
  STATE.md frontmatter fields: `active_phase`, `next_action`, `next_phases`, and
  `progress`. `formatGsdState()` gains scenes for in-flight, idle, and progress
  display. Write-side wiring follows in a later RC.
  ([#2833](https://github.com/gsd-build/get-shit-done/issues/2833))

- **`--minimal` install flag** (alias `--core-only`) — writes only the six core
  skills needed for the main workflow loop; no `gsd-*` subagents. Drops cold-start
  overhead from ~12k tokens to ~700. Useful for local LLMs with 32K–128K context.
  ([#2762](https://github.com/gsd-build/get-shit-done/issues/2762))

### Changed

- **Skill surface consolidated 86 → 59 `commands/gsd/*.md` entries** — four new
  grouped skills replace clusters of micro-skills (`capture`, `phase`, `config`,
  `workspace`); six existing parents absorb wrap-up and sub-operations as flags
  (`update --sync/--reapply`, `sketch --wrap-up`, `spike --wrap-up`,
  `map-codebase --fast/--query`, `code-review --fix`, `progress --do/--next`).
  Zero functional loss — 31 micro-skills deleted, all behavior preserved via flags.
  ([#2790](https://github.com/gsd-build/get-shit-done/issues/2790))

- **Canary release workflow now publishes from `dev` branch only** — aligns with
  the branch→dist-tag policy (`dev` → `@canary`, `main` → `@next`/`@latest`).
  `workflow_dispatch` on `main` now completes build/test/dry-run validation but
  skips publish and tag.
  ([#2868](https://github.com/gsd-build/get-shit-done/issues/2868))

- **PRs missing `Closes #NNN` are auto-closed** — the `Issue link required`
  workflow now auto-closes any PR opened without a closing keyword, posting a
  comment that points to the contribution guide.
  ([#2872](https://github.com/gsd-build/get-shit-done/issues/2872))

### Fixed

- **Gemini slash commands now namespaced as `/gsd:<cmd>` instead of `/gsd-<cmd>`** —
  Gemini CLI namespaces commands under `gsd:` so `/gsd-plan-phase` was unexecutable.
  The install path now converts every body-text reference via a roster-checked regex,
  consistently rewriting command files, agent bodies, and banners.
  ([#2768](https://github.com/gsd-build/get-shit-done/issues/2768),
  [#2783](https://github.com/gsd-build/get-shit-done/issues/2783))

- **GSD slash-command namespace drift cleaned up across docs, workflows, and
  autocomplete** — remaining stale `/gsd:<cmd>` references now use canonical
  `/gsd-<cmd>`; `scripts/fix-slash-commands.cjs` rewrites retired colon syntax.
  ([#2858](https://github.com/gsd-build/get-shit-done/pull/2858))

- **`SKILL.md` description quoted for Copilot / Antigravity / Trae / CodeBuddy** —
  descriptions starting with a YAML 1.2 flow indicator crashed gh-copilot's strict
  YAML loader. Six emission sites now wrap descriptions in `yamlQuote(...)`.
  ([#2876](https://github.com/gsd-build/get-shit-done/issues/2876))

- **`gsd-tools` invocations use the absolute installed path** — bare `gsd-tools …`
  calls inside skill bodies relied on PATH resolution not guaranteed in every runtime;
  replaced with the absolute path emitted at install time.
  ([#2851](https://github.com/gsd-build/get-shit-done/issues/2851))

- **Codex installer preserves trailing newline when stripping legacy hooks** — the
  legacy-hook strip ran against files with no terminating newline at EOF, breaking
  downstream parsers.
  ([#2866](https://github.com/gsd-build/get-shit-done/issues/2866))

---

## What was in rc.7

[`RELEASE-v1.39.0-rc.7.md`](RELEASE-v1.39.0-rc.7.md) — first 1.39.0 RC to roll in
post-rc.5 fixes from `main`. Includes the `extractCurrentMilestone` fenced-code-block
fix ([#2787](https://github.com/gsd-build/get-shit-done/issues/2787)), `audit-uat`
frontmatter parse fix ([#2788](https://github.com/gsd-build/get-shit-done/issues/2788)),
skill description budget + lint gate ([#2789](https://github.com/gsd-build/get-shit-done/issues/2789)),
`gsd-sdk` workstream + binary-collision fixes ([#2791](https://github.com/gsd-build/get-shit-done/issues/2791)),
and nine additional correctness fixes across OpenCode, Codex, and Gemini runtimes.

---

## Installing the pre-release

```bash
# npm
npm install -g get-shit-done-cc@next

# npx (one-shot)
npx get-shit-done-cc@next
```

To pin to this exact RC:

```bash
npm install -g get-shit-done-cc@1.40.0-rc.1
```

---

## What's next

- Soak 

# FILE: docs/ARCHITECTURE.md

# GSD Architecture

> System architecture for contributors and advanced users. For user-facing documentation, see [Feature Reference](FEATURES.md) or [User Guide](USER-GUIDE.md).

---

## Table of Contents

- [System Overview](#system-overview)
- [Design Principles](#design-principles)
- [Component Architecture](#component-architecture)
- [Agent Model](#agent-model)
- [Data Flow](#data-flow)
- [File System Layout](#file-system-layout)
- [Installer Architecture](#installer-architecture)
- [Hook System](#hook-system)
- [CLI Tools Layer](#cli-tools-layer)
- [Runtime Abstraction](#runtime-abstraction)

---

## System Overview

GSD is a **meta-prompting framework** that sits between the user and AI coding agents (Claude Code, Gemini CLI, OpenCode, Kilo, Codex, Copilot, Antigravity, Trae, Cline, Augment Code). It provides:

1. **Context engineering** — Structured artifacts that give the AI everything it needs per task
2. **Multi-agent orchestration** — Thin orchestrators that spawn specialized agents with fresh context windows
3. **Spec-driven development** — Requirements → research → plans → execution → verification pipeline
4. **State management** — Persistent project memory across sessions and context resets

```
┌──────────────────────────────────────────────────────┐
│                      USER                            │
│            /gsd-command [args]                        │
└─────────────────────┬────────────────────────────────┘
                      │
┌─────────────────────▼────────────────────────────────┐
│              COMMAND LAYER                            │
│   commands/gsd/*.md — Prompt-based command files      │
│   (Claude Code custom commands / Codex skills)        │
└─────────────────────┬────────────────────────────────┘
                      │
┌─────────────────────▼────────────────────────────────┐
│              WORKFLOW LAYER                           │
│   get-shit-done/workflows/*.md — Orchestration logic  │
│   (Reads references, spawns agents, manages state)    │
└──────┬──────────────┬─────────────────┬──────────────┘
       │              │                 │
┌──────▼──────┐ ┌─────▼─────┐ ┌────────▼───────┐
│  AGENT      │ │  AGENT    │ │  AGENT         │
│  (fresh     │ │  (fresh   │ │  (fresh        │
│   context)  │ │   context)│ │   context)     │
└──────┬──────┘ └─────┬─────┘ └────────┬───────┘
       │              │                 │
┌──────▼──────────────▼─────────────────▼──────────────┐
│              CLI TOOLS LAYER                          │
│   gsd-sdk query (sdk/src/query) + gsd-tools.cjs       │
│   Programmatic SDK bridge: GSDTools/query-runtime-bridge.ts │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────▼───────────────────────────────┐
│              FILE SYSTEM (.planning/)                 │
│   PROJECT.md | REQUIREMENTS.md | ROADMAP.md          │
│   STATE.md | config.json | phases/ | research/       │
└──────────────────────────────────────────────────────┘
```

---

## Design Principles

### 1. Fresh Context Per Agent

Every agent spawned by an orchestrator gets a clean context window (up to 200K tokens). This eliminates context rot — the quality degradation that happens as an AI fills its context window with accumulated conversation.

### 2. Thin Orchestrators

Workflow files (`get-shit-done/workflows/*.md`) never do heavy lifting. They:

- Load context via `gsd-sdk query init.<workflow>` (or legacy `gsd-tools.cjs init <workflow>`)
- Spawn specialized agents with focused prompts
- Collect results and route to the next step
- Update state between steps

### 3. File-Based State

All state lives in `.planning/` as human-readable Markdown and JSON. No database, no server, no external dependencies. This means:

- State survives context resets (`/clear`)
- State is inspectable by both humans and agents
- State can be committed to git for team visibility

### 4. Absent = Enabled

Workflow feature flags follow the **absent = enabled** pattern. If a key is missing from `config.json`, it defaults to `true`. Users explicitly disable features; they don't need to enable defaults.

### 5. Defense in Depth

Multiple layers prevent common failure modes:

- Plans are verified before execution (plan-checker agent)
- Execution produces atomic commits per task
- Post-execution verification checks against phase goals
- UAT provides human verification as final gate

---

## Component Architecture

### Commands (`commands/gsd/*.md`)

User-facing entry points. Each file contains YAML frontmatter (name, description, allowed-tools) and a prompt body that bootstraps the workflow. Commands are installed as:

- **Claude Code:** Custom slash commands (hyphen form, `/gsd-command-name`)
- **OpenCode / Kilo:** Slash commands (hyphen form, `/gsd-command-name`)
- **Codex:** Skills (`$gsd-command-name`)
- **Copilot:** Slash commands (hyphen form, `/gsd-command-name`)
- **Gemini CLI:** Slash commands under the `gsd:` namespace (colon form, `/gsd:command-name`) — Gemini namespaces all custom commands under their plugin id, so the install path rewrites every body-text reference to colon form
- **Antigravity:** Skills

**Total commands:** see [`docs/INVENTORY.md`](INVENTORY.md#commands) for the authoritative count and full roster.

#### Two-stage hierarchical routing (v1.40, [#2792](https://github.com/gsd-build/get-shit-done/issues/2792))

To keep the eager skill-listing token cost low, v1.40 introduces six namespace **meta-skills** (`gsd-workflow`, `gsd-project`, `gsd-quality`, `gsd-context`, `gsd-manage`, `gsd-ideate` — sourced from `commands/gsd/ns-*.md`, but the invocable `name:` is the bare form shown here) layered above the concrete sub-skills. The model sees 6 namespace routers (~120 tokens) instead of a flat 86-skill listing (~2,150 tokens), selects a namespace, then routes to the concrete sub-skill via a routing table embedded in the namespace router's body. Namespace skills are **additive** — every concrete co

# FILE: docs/RELEASE-v1.39.0-rc.6.md

# v1.39.0-rc.6 Release Notes

Pre-release candidate. Published to npm under the `next` tag.

```bash
npx get-shit-done-cc@next
```

---

## What's in this release

**rc.6 is a republish of rc.5.** No new fixes were rolled in — `release/1.39.0`
was bumped from `1.39.0-rc.5` to `1.39.0-rc.6` without first being merged with
`main`, so the branch contents at the time of tag are byte-for-byte equivalent
to rc.5 plus the version-bump commit.

```bash
$ git log v1.39.0-rc.5..v1.39.0-rc.6 --pretty='%h %s'
388118d8 chore: bump to 1.39.0-rc.6
```

If you are already on `1.39.0-rc.5`, there is nothing new to install in rc.6.
The expected next step is an rc.7 cut that first merges `main` into
`release/1.39.0` so the eight fixes that landed after rc.5 reach the registry.

---

## What was in rc.5

### Fixed

**Codex hooks migrator correctness hardening** (#2809)

Five edge-cases in the `[[hooks.<Event>]]` → `[[hooks.<Event>.hooks]]` two-level
nested schema migration path, discovered across five rounds of code review:

| Finding | Fix |
|---------|-----|
| `parseHooksBody` used a bare regex (`/^([\w.]+)\s*=/`) that silently dropped hyphenated keys such as `status-message` and any quoted TOML key | Replaced with `parseTomlKey()`, the existing full TOML key parser |
| `buildNestedBlock` unconditionally emitted `[[hooks.TYPE.hooks]]` even when no handler fields were present, producing an entry with `type = "command"` but no `command` | Added guard: matcher-only / handler-field-free sections emit only the event-entry block |
| `legacyMapSections` filter used `section.path.startsWith('hooks.')` without checking the segment count, so three-segment tables like `[hooks.SessionStart.hooks]` were misclassified as event entries and re-emitted as bogus nested events | Now uses `section.segments.length === 2` (same fix previously applied to `staleNamespacedAotSections`) |
| No regression test for quoted event names containing dots — `[[hooks."before.tool"]]` has a 2-segment path but 3 dot-parts, and a `split('.')` check would misclassify it | Regression test added; quoted-dot names are correctly treated as a single two-segment namespace |
| Handler command path assertion in install tests used a regex (`/gsd-check-update\.js/`) rather than the exact absolute path | Strengthened to `assert.strictEqual` with `path.join(codexHome, 'hooks', 'gsd-check-update.js')` |

---

## What was in rc.4

### Added

**`--minimal` install flag** (alias `--core-only`) (#2762)

Writes only the six core skills needed to run the main workflow loop:
`new-project`, `discuss-phase`, `plan-phase`, `execute-phase`, `help`, `update`.
No `gsd-*` subagents are installed.

| Mode | Cold-start system-prompt overhead |
|------|-----------------------------------|
| full (default) | ~12k tokens |
| minimal | ~700 tokens |

Useful for local LLMs with 32K–128K context windows. Sonnet 4.6 / Opus 4.7 users
don't need it — the full surface is the right default for cloud models.

The install manifest records `mode: "minimal" | "full"`. Run `gsd update` without
`--minimal` at any time to expand to the full skill set.

### Fixed (rc.4)

**Codex install no longer corrupts `~/.codex/config.toml`** (#2760)

The installer now:

- Strips legacy `[agents]` (single-bracket) and `[[agents]]` (sequence) blocks
  unconditionally — both are invalid in the current Codex TOML schema, regardless of
  whether a GSD marker is present.
- Emits the GSD-managed hook in the shape the user's config already uses:
  `[[hooks.<Event>]]` namespaced AoT if any existing hook uses that form, otherwise
  top-level `[[hooks]]`.
- Migrates any legacy `[hooks.<Event>]` (map format) to `[[hooks.<Event>]]` (array
  format) during write.
- Writes atomically via a temp file + `renameSync` — no partial writes.
- Validates the post-write bytes with a strict TOML parser that rejects duplicate
  keys, repeated table headers, trailing bytes after values, and unsupported value
  types.
- On any pre-write or write-time failure, restores the pre-install snapshot and aborts
  with a clear error instead of warn-and-continue.

---

## Installing the pre-release

```bash
# npm
npm install -g get-shit-done-cc@next

# npx (one-shot)
npx get-shit-done-cc@next
```

To pin to this exact RC:

```bash
npm install -g get-shit-done-cc@1.39.0-rc.6
```

---

## What's next

- **rc.7** — cut from `release/1.39.0` after merging `main` into the release branch,
  so the eight fixes that landed after rc.5 (#2828, #2829, #2831, #2832, #2835,
  #2836, #2838, #2839) actually reach the registry.
- Run `finalize` on the release workflow to promote `1.39.0` to `latest` once an RC
  with the full main-branch contents is stable.


# FILE: docs/gsd-sdk-query-migration-blurb.md

# GSD SDK query migration (summary blurb)

Copy-paste friendly for Discord and GitHub comments.

---

**@gsd-build/sdk** replaces the untyped, monolithic `gsd-tools.cjs` subprocess with a typed, tested, registry-based query system and **`gsd-sdk query`**, giving GSD structured results, classified errors (`GSDError` with `ErrorClassification`), and golden-verified parity with the old CLI. That gives the framework one stable contract instead of a fragile, very large CLI that every workflow had to spawn and parse by hand.

**What users can expect**

- Same GSD commands and workflows they already use.
- Snappier runs (less Node startup on chained tool calls).
- Fewer mysterious mid-workflow failures and safer upgrades, because behavior is covered by tests and a single stable contract.
- Stronger predictability: outputs and failure modes are consistent and explicit.

**Cost and tokens**

The SDK does not automatically reduce LLM tokens per model call. Savings show up indirectly: fewer ambiguous tool results and fewer retry or recovery loops, which often lowers real-world session cost and wall time.

**Agents then vs now**

Agents always followed workflow instructions. What improved is the surface those steps run on. Before, workflows effectively said to shell out to `gsd-tools.cjs` and interpret stdout or JSON with brittle assumptions. Now they point at **`gsd-sdk query`** and typed handlers that return the shapes prompts expect, with clearer error reasons when something must stop or be fixed, so instruction following holds end to end with less thrash from bad parses or silent output drift.


# FILE: docs/json-errors.md

# JSON Error Mode — `gsd-tools` Structured Errors

## Overview

`gsd-tools` supports a **JSON error mode** that emits all errors as structured
JSON objects on stderr instead of free-form text.  This is the recommended
surface for tests and tooling that need to assert on error types without
grepping raw text (see `CONTRIBUTING.md` — "Prohibited: Raw Text Matching on
Test Outputs").

## Activating

Either flag or env var activates the mode:

```bash
# Flag (preferred in test code):
node gsd-tools.cjs --json-errors <command> [args]

# Env var (preferred for shell wrappers and CI):
GSD_JSON_ERRORS=1 node gsd-tools.cjs <command> [args]
```

## Wire format

On any error, exactly one JSON line is written to **stderr** and the process
exits with code 1:

```json
{ "ok": false, "reason": "<error_code>", "message": "<human text>" }
```

Fields:

| Field     | Type    | Description |
|-----------|---------|-------------|
| `ok`      | `false` | Always `false` for error objects. |
| `reason`  | string  | Typed reason code from the taxonomy below. |
| `message` | string  | Human-readable description (may change; do not assert on it). |

## Error code taxonomy

Codes are frozen constants in `get-shit-done/bin/lib/core.cjs` under
`ERROR_REASON`.  Tests must assert on `reason` values (stable), not `message`
text (unstable).

### Dispatch errors (gsd-tools routing layer)

| Code | When emitted |
|------|-------------|
| `sdk_unknown_command` | Unknown top-level command (`gsd-tools bogus-cmd`) |
| `sdk_unknown_command` | Unknown dotted command (`gsd-tools foo.bar` where `foo` is not a known command) |
| `sdk_unknown_command` | Unknown subcommand within a domain (e.g. `gsd-tools intel bogus-sub`) |
| `sdk_missing_arg` | Required argument omitted by an SDK-level guard |
| `sdk_fail_fast` | SDK fail-fast policy triggered |

### Usage / flag errors

| Code | When emitted |
|------|-------------|
| `usage` | `--pick` flag used without a following value |
| `usage` | Version flag (`--version`, `-v`) which gsd-tools never accepts |
| `usage` | Top-level no-args invocation (usage text) |

### Config errors (`config-get`, `config-set`, `config-ensure-section`)

| Code | When emitted |
|------|-------------|
| `config_key_not_found` | `config-get` for a key that is absent from the config file |
| `config_no_file` | Config operation when `.planning/config.json` does not exist |
| `config_parse_failed` | Config file exists but is not valid JSON |
| `config_invalid_key` | `config-set` for a key outside the allowed whitelist |

### Phase / workflow errors

| Code | When emitted |
|------|-------------|
| `phase_not_found` | Phase directory lookup returns no match |
| `summary_no_planning` | Summary operation when no `.planning/` directory exists |

### Graphify errors

| Code | When emitted |
|------|-------------|
| `graphify_no_graph` | Graphify query or diff when no graph has been built |
| `graphify_invalid_query` | Graphify query with a malformed query string |

### Hook / security errors

| Code | When emitted |
|------|-------------|
| `hooks_opt_out` | Hooks are disabled via opt-out config |
| `security_scan_failed` | Security scan produced a finding that blocks the operation |

### Fallback

| Code | When emitted |
|------|-------------|
| `unknown` | All other errors without a specific reason code assigned |

## Writing tests

Always parse stderr with `JSON.parse` and assert on typed fields.  Never use
`.includes()`, `.match()`, or regex on the raw error string.

```js
// CORRECT: parse then assert on typed field
const result = runGsdTools(['--json-errors', 'bogus-command'], tmpDir);
assert.strictEqual(result.success, false);
const err = JSON.parse(result.error);
assert.strictEqual(err.ok, false);
assert.strictEqual(err.reason, 'sdk_unknown_command');

// WRONG: text matching (banned by lint-no-source-grep policy)
// assert.ok(result.error.includes('Unknown command'));
```

## Adding a new error code

1. Add the constant to `ERROR_REASON` in
   `get-shit-done/bin/lib/core.cjs` (snake\_case, prefixed by subsystem).
2. Pass it as the second argument to `error()` at the call site.
3. Add a row to this document.
4. Add a test asserting the new `reason` code via `JSON.parse`.


# FILE: docs/context-monitor.md

# Context Window Monitor

A post-tool hook (`PostToolUse` for Claude Code, `AfterTool` for Gemini CLI) that warns the agent when context window usage is high.

## Problem

The statusline shows context usage to the **user**, but the **agent** has no awareness of context limits. When context runs low, the agent continues working until it hits the wall — potentially mid-task with no state saved.

## How It Works

1. The statusline hook writes context metrics to `/tmp/claude-ctx-{session_id}.json`
2. After each tool use, the context monitor reads these metrics
3. When remaining context drops below thresholds, it injects a warning as `additionalContext`
4. The agent receives the warning in its conversation and can act accordingly

## Thresholds

| Level | Remaining | Agent Behavior |
|-------|-----------|----------------|
| Normal | > 35% | No warning |
| WARNING | <= 35% | Wrap up current task, avoid starting new complex work |
| CRITICAL | <= 25% | Stop immediately, save state (`/gsd-pause-work`) |

## Debounce

To avoid spamming the agent with repeated warnings:
- First warning always fires immediately
- Subsequent warnings require 5 tool uses between them
- Severity escalation (WARNING -> CRITICAL) bypasses debounce

## Architecture

```
Statusline Hook (gsd-statusline.js)
    | writes
    v
/tmp/claude-ctx-{session_id}.json
    ^ reads
    |
Context Monitor (gsd-context-monitor.js, PostToolUse/AfterTool)
    | injects
    v
additionalContext -> Agent sees warning
```

The bridge file is a simple JSON object:

```json
{
  "session_id": "abc123",
  "remaining_percentage": 28.5,
  "used_pct": 71,
  "timestamp": 1708200000
}
```

## Integration with GSD

GSD's `/gsd-pause-work` command saves execution state. The WARNING message suggests using it. The CRITICAL message instructs immediate state save.

## Setup

Both hooks are automatically registered during `npx get-shit-done-cc` installation:

- **Statusline** (writes bridge file): Registered as `statusLine` in settings.json
- **Context Monitor** (reads bridge file): Registered as `PostToolUse` hook in settings.json (`AfterTool` for Gemini)

Manual registration should use the absolute Node executable path that ran the installer. On Windows PowerShell, prefix the command with `&` when that executable path is quoted.

Manual registration in `~/.claude/settings.json` (Claude Code):

```json
{
  "statusLine": {
    "type": "command",
    "command": "\"/usr/local/bin/node\" \"/Users/me/.claude/hooks/gsd-statusline.js\""
  },
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"/usr/local/bin/node\" \"/Users/me/.claude/hooks/gsd-context-monitor.js\""
          }
        ]
      }
    ]
  }
}
```

For Gemini CLI (`~/.gemini/settings.json`), use `AfterTool` instead of `PostToolUse`:

```json
{
  "hooks": {
    "AfterTool": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "& \"C:/Program Files/nodejs/node.exe\" \"C:/Users/me/.gemini/hooks/gsd-context-monitor.js\""
          }
        ]
      }
    ]
  }
}
```

## Safety

- The hook wraps everything in try/catch and exits silently on error
- It never blocks tool execution — a broken monitor should not break the agent's workflow
- Stale metrics (older than 60s) are ignored
- Missing bridge files are handled gracefully (subagents, fresh sessions)


# FILE: docs/COMMANDS.md

# GSD Command Reference

> Command syntax, flags, options, and examples for stable commands. For feature details, see [Feature Reference](FEATURES.md). For workflow walkthroughs, see [User Guide](USER-GUIDE.md).

---

## Command Syntax

- **Claude Code / Copilot / OpenCode / Kilo:** `/gsd-command-name [args]` (hyphen form)
- **Gemini CLI:** `/gsd:command-name [args]` (colon form — Gemini namespaces commands under `gsd:`)
- **Codex:** `$gsd-command-name [args]`

The hyphen and colon forms are *runtime-specific spellings of the same command*. Whichever runtime you're on, the installer writes the correct form into your runtime's command directory.

---

## Namespace Meta-Skills

Six namespace routers ship as the first-stage entry points in v1.40. They keep the eager skill-listing token cost low (~120 tokens for 6 routers vs ~2,150 for a flat 86-skill listing) while the full surface remains directly invocable. The model selects a namespace, then routes to the concrete sub-skill. See [#2792](https://github.com/gsd-build/get-shit-done/issues/2792).

| Command | Routes to |
|---------|-----------|
| `/gsd-workflow` | Phase pipeline — discuss / plan / execute / verify / phase / progress |
| `/gsd-project` | Project lifecycle — milestones, audits, summary |
| `/gsd-quality` | Quality gates — code review, debug, audit, security, eval, ui |
| `/gsd-context` | Codebase intelligence — map, graphify, docs, learnings |
| `/gsd-manage` | Management — config, workspace, workstreams, thread, update, ship, inbox |
| `/gsd-ideate` | Exploration & capture — explore, sketch, spike, spec, capture |

The namespace skills are **additive** — every existing concrete command (e.g. `/gsd-plan-phase`, `/gsd-code-review --fix`) is still invocable directly.

---

## Core Workflow Commands

### `/gsd-new-project`

Initialize a new project with deep context gathering.

| Flag | Description |
|------|-------------|
| `--auto @file.md` | Auto-extract from document, skip interactive questions |

**Prerequisites:** No existing `.planning/PROJECT.md`
**Produces:** `PROJECT.md`, `REQUIREMENTS.md`, `ROADMAP.md`, `STATE.md`, `config.json`, `research/`, `CLAUDE.md`

```bash
/gsd-new-project                    # Interactive mode
/gsd-new-project --auto @prd.md     # Auto-extract from PRD
```

---

### `/gsd-workspace`

Manage GSD workspaces — create, list, or remove isolated workspace environments with repo copies and independent `.planning/` directories.

| Flag | Description |
|------|-------------|
| `--new` | Create a new workspace (use with `--name`, `--repos`, etc.) |
| `--list` | List active GSD workspaces and their status |
| `--remove <name>` | Remove a workspace and clean up git worktrees |
| `--name <name>` | Workspace name (used with `--new`) |
| `--repos repo1,repo2` | Comma-separated repo paths or names (used with `--new`) |
| `--path /target` | Target directory (default: `~/gsd-workspaces/<name>`) |
| `--strategy worktree\|clone` | Copy strategy (default: `worktree`) |
| `--branch <name>` | Branch to checkout (default: `workspace/<name>`) |
| `--auto` | Skip interactive questions |

**Use cases:**
- Multi-repo: work on a subset of repos with isolated GSD state
- Feature isolation: `--repos .` creates a worktree of the current repo

**Produces:** `WORKSPACE.md`, `.planning/`, repo copies (worktrees or clones)

```bash
/gsd-workspace --new --name feature-b --repos hr-ui,ZeymoAPI
/gsd-workspace --new --name feature-b --repos . --strategy worktree  # Same-repo isolation
/gsd-workspace --list
/gsd-workspace --remove feature-b
```

---

### `/gsd-discuss-phase`

Gather phase context through adaptive questioning before planning.

| Argument | Required | Description |
|----------|----------|-------------|
| `N` | No | Phase number (defaults to current phase) |

| Flag | Description |
|------|-------------|
| `--all` | Skip area selection — discuss all gray areas interactively (no auto-advance) |
| `--auto` | Auto-select recommended defaults for all questions |
| `--batch` | Group questions for batch intake instead of one-by-one |
| `--analyze` | Add trade-off analysis during discussion |
| `--power` | File-based bulk question answering from a prepared answers file |
| `--assumptions` | Surface Claude's implementation assumptions about the phase without an interactive session |

**Prerequisites:** `.planning/ROADMAP.md` exists
**Produces:** `{phase}-CONTEXT.md`, `{phase}-DISCUSSION-LOG.md` (audit trail)

```bash
/gsd-discuss-phase 1                # Interactive discussion for phase 1
/gsd-discuss-phase 1 --all          # Discuss all gray areas without selection step
/gsd-discuss-phase 3 --auto         # Auto-select defaults for phase 3
/gsd-discuss-phase --batch          # Batch mode for current phase
/gsd-discuss-phase 2 --analyze      # Discussion with trade-off analysis
/gsd-discuss-phase 1 --power        # Bulk answers from file
/gsd-discuss-phase 3 --assumptions  # Surface Claude's assumptions before planning
```

---

### `/gsd-ui-phase`

Generate UI design contract for frontend phases.

| Argument | Required | Description |
|----------|----------|-------------|
| `N` | No | Phase number (defaults to current phase) |

**Prerequisites:** `.planning/ROADMAP.md` exists, phase has frontend/UI work
**Produces:** `{phase}-UI-SPEC.md`

```bash
/gsd-ui-phase 2                     # Design contract for phase 2
```

---

### `/gsd-plan-phase`

Research, plan, and verify a phase.

| Argument | Required | Description |
|----------|----------|-------------|
| `N` | No | Phase number (defaults to next unplanned phase) |

| Flag | Description |
|------|-------------|
| `--auto` | Skip interactive confirmations |
| `--research` | Force re-research even if RESEARCH.md exists |
| `--skip-research` | Skip domain research step |
| `--research-phase <N>` | Research-only mode: spawn researcher for phase `<N>`, write RESEARCH.md, exit before planner. Replaces the deleted `gsd-research-phase` standalone command (#3042). |
| `--view` | Researc

# FILE: docs/contributor-standards.md

# Contributor Standards

Standards for working with `CONTEXT.md`, `docs/adr/`, and AI-agent-assisted contributions.

These apply to every PR — fix, enhancement, or feature. They are part of the merge contract, not optional background reading.

**Standards hierarchy** (canonical, in order):

1. `CONTEXT.md` — domain language and module naming
2. `docs/adr/` — accepted architectural decisions
3. Approved issue scope

---

## CONTEXT.md

### What it is

`CONTEXT.md` is the single source of truth for domain vocabulary. It defines:

- **Domain terms** — canonical Module names, seam vocabulary, and Interface names (e.g. Dispatch Policy Module, Command Contract Validation Module, Planning Workspace Module)
- **Recurring PR mistakes** — CodeRabbit findings that recur; covers tests, shell guards, changesets, docs
- **Workflow learnings** — patterns distilled from triage + PR cycles

### Format

`CONTEXT.md` is written as flat named sections under `## Domain terms` (for Modules/seams) and `##` sections for recurring rules. Machine-oriented predicates use `KEY.SUBKEY=value` flat format in code blocks under `## AI Ops Memory`.

Adding a new Module or seam:

- Add a `### <Module Name>` entry under `## Domain terms`.
- Write one paragraph. State what the Module owns. Be concrete — list the Interface names and policy boundaries it covers.
- Do not add synonyms; pick one name and use it everywhere.

Extending an existing predicate:

- Add a `KEY.SUBKEY=value` line inside the relevant `## AI Ops Memory` block.
- Do not create a new top-level section for a variation on an existing concept.

When to add a new predicate vs extend an existing one:

- New predicate: the concept has a distinct identity, distinct owner, and is not covered by any existing section.
- Extend existing: the new fact qualifies, constrains, or amends an already-named Module. Add it as a sub-entry or amendment paragraph.

### Contributor requirements

- Read `CONTEXT.md` in full before naming anything (modules, interfaces, seams, tests, PRs).
- Use `CONTEXT.md` vocabulary consistently in code comments, tests, issue/PR text, and docs.
- Do not invent synonyms. If you need a concept that is not in the glossary, note it explicitly in the issue or PR rather than using ad-hoc language.
- Do not rewrite `CONTEXT.md` as part of drive-by cleanup; propose focused updates tied to the approved issue scope.
- `CONTEXT.md` is maintainer-owned. Contributors can propose additions via issue discussion, but final wording is the maintainer's call.

### Example (correct)

A PR that adds a new query adapter should use the term **Native Dispatch Adapter Module** (from `CONTEXT.md`), not "native adapter," "query native handler," or any other variant.

---

## ADRs

### What they are

`docs/adr/` contains Architecture Decision Records. Each ADR is a concise record of one accepted decision: the problem, the decision, and the consequences. Accepted ADRs are the current standard.

Currently accepted ADRs:

| File | Decision |
|------|----------|
| `0001-dispatch-policy-module.md` | Dispatch Policy Module as the single seam for query execution outcomes |
| `0002-command-contract-validation-module.md` | Command Contract Validation Module / command contract centralization |
| `0003-model-catalog-module.md` | Model Catalog Module as the single source of truth for agent profiles and runtime tier defaults |
| `0004-worktree-workstream-seam-module.md` | Planning Workspace Module as single seam for worktree and workstream state |
| `0005-sdk-architecture-seam-map.md` | SDK Architecture seam map for query/runtime surfaces |
| `0006-planning-path-projection-module.md` | Planning Path Projection Module for SDK query handlers |
| `0007-sdk-package-seam-module.md` | SDK Package Seam Module owns SDK-to-get-shit-done-cc compatibility |

### When an ADR is required

An ADR is required when a decision:

- Introduces or removes a Module seam that other code will depend on.
- Changes the policy contract of an existing accepted ADR.
- Establishes a new architectural invariant (naming convention, test contract, CI enforcement).

An ADR is optional (a comment in the relevant issue or PR is sufficient) when:

- The change is a bugfix that lands squarely within an existing accepted decision.
- The change is a docs or test improvement with no architectural surface.

### Naming conventions

`NNNN-<short-slug>.md` — four-digit zero-padded sequence number, followed by a kebab-case slug that names the Module or decision. Example: `0003-model-catalog-module.md`.

### Required sections

Every ADR must open with:

```md
# <Title>

- **Status:** Accepted | Proposed | Deprecated
- **Date:** YYYY-MM-DD
```

Body: one-paragraph decision summary, then `## Decision` (specifics), then `## Consequences` (behavioral changes downstream callers can rely on).

Amendments are appended as `## Amendment (YYYY-MM-DD): <topic>` sections — the original body is never rewritten.

### Status block format

```md
- **Status:** Accepted
- **Date:** 2026-05-09
```

Status values: `Proposed` (under discussion), `Accepted` (current standard), `Deprecated` (superseded — include a forward reference to the replacement).

### Cross-reference style

Reference sibling ADRs by filename, not by title prose: `see \`0001-dispatch-policy-module.md\``. This survives title edits.

### ADR README index

`docs/adr/` does not currently maintain a separate `README.md` index. The canonical index is the table in this document (above). If an ADR is added, update this table in the same PR.

### Governance

- ADR creation and final wording is **maintainer-owned**. Contributors must not open ADR files as part of a contribution PR.
- Contributors can — and should — give input on proposed ADR direction in the linked issue discussion.
- Once an ADR is `Accepted`, reopening the decision must be explicit (a dedicated issue with rationale), not implied by a drive-by PR change.
- If your PR intentionally revisits an accepted ADR decision, call it o

# FILE: docs/INVENTORY.md

# GSD Shipped Surface Inventory

> Authoritative roster of every shipped GSD surface: commands, agents, workflows, references, CLI modules, and hooks. Where the broad docs (AGENTS.md, COMMANDS.md, ARCHITECTURE.md, CLI-TOOLS.md) diverge from the filesystem, treat this file and the repository tree itself as the source of truth.

## How To Use This File

- Counts here are derived from the filesystem at the v1.36.0 pin and may drift between releases. For live counts, run `ls commands/gsd/*.md | wc -l`, `ls agents/gsd-*.md | wc -l`, etc. against the checkout.
- This file enumerates every shipped surface across all six families (agents, commands, workflows, references, CLI modules, hooks). Broad docs may render narrative or curated subsets; when they disagree with the filesystem, this file and the directory listings are authoritative.
- New surfaces added after v1.36.0 should land here first, then propagate to the broad docs. The drift-control tests in `tests/inventory-counts.test.cjs`, `tests/commands-doc-parity.test.cjs`, `tests/agents-doc-parity.test.cjs`, `tests/cli-modules-doc-parity.test.cjs`, `tests/hooks-doc-parity.test.cjs`, `tests/architecture-counts.test.cjs`, and `tests/command-count-sync.test.cjs` anchor the counts and roster contents against the filesystem.

---

## Agents (33 shipped)

Full roster at `agents/gsd-*.md`. The "Primary doc" column flags whether [`docs/AGENTS.md`](AGENTS.md) carries a full role card (*primary*), a short stub in the "Advanced and Specialized Agents" section (*advanced stub*), or no coverage (*inventory only*).

| Agent | Role (one line) | Spawned by | Primary doc |
|-------|-----------------|------------|-------------|
| gsd-project-researcher | Researches domain ecosystem before roadmap creation (stack, features, architecture, pitfalls). | `/gsd-new-project`, `/gsd-new-milestone` | primary |
| gsd-phase-researcher | Researches implementation approach for a specific phase before planning. | `/gsd-plan-phase` | primary |
| gsd-ui-researcher | Produces UI design contracts for frontend phases. | `/gsd-ui-phase` | primary |
| gsd-assumptions-analyzer | Produces evidence-backed assumptions for discuss-phase (assumptions mode). | `discuss-phase-assumptions` workflow | primary |
| gsd-advisor-researcher | Researches a single gray-area decision during discuss-phase advisor mode. | `discuss-phase` workflow (advisor mode) | primary |
| gsd-research-synthesizer | Combines parallel researcher outputs into a unified SUMMARY.md. | `/gsd-new-project` | primary |
| gsd-planner | Creates executable phase plans with task breakdown and goal-backward verification. | `/gsd-plan-phase`, `/gsd-quick` | primary |
| gsd-roadmapper | Creates project roadmaps with phase breakdown and requirement mapping. | `/gsd-new-project` | primary |
| gsd-executor | Executes GSD plans with atomic commits and deviation handling. | `/gsd-execute-phase`, `/gsd-quick` | primary |
| gsd-plan-checker | Verifies plans will achieve phase goals (8 verification dimensions). | `/gsd-plan-phase` (verification loop) | primary |
| gsd-integration-checker | Verifies cross-phase integration and end-to-end flows. | `/gsd-audit-milestone` | primary |
| gsd-ui-checker | Validates UI-SPEC.md design contracts against quality dimensions. | `/gsd-ui-phase` (validation loop) | primary |
| gsd-verifier | Verifies phase goal achievement through goal-backward analysis. | `/gsd-execute-phase` | primary |
| gsd-nyquist-auditor | Fills Nyquist validation gaps by generating tests. | `/gsd-validate-phase` | primary |
| gsd-ui-auditor | Retroactive 6-pillar visual audit of implemented frontend code. | `/gsd-ui-review` | primary |
| gsd-codebase-mapper | Explores codebase and writes structured analysis documents. | `/gsd-map-codebase` | primary |
| gsd-debugger | Investigates bugs using scientific method with persistent state. | `/gsd-debug`, `/gsd-verify-work` | primary |
| gsd-user-profiler | Scores developer behavior across 8 dimensions. | `/gsd-profile-user` | primary |
| gsd-doc-writer | Writes and updates project documentation. | `/gsd-docs-update` | primary |
| gsd-doc-verifier | Verifies factual claims in generated documentation. | `/gsd-docs-update` | primary |
| gsd-security-auditor | Verifies threat mitigations from PLAN.md threat model. | `/gsd-secure-phase` | primary |
| gsd-pattern-mapper | Maps new files to closest existing analogs; writes PATTERNS.md for the planner. | `/gsd-plan-phase` (between research and planning) | advanced stub |
| gsd-debug-session-manager | Runs the full `/gsd-debug` checkpoint-and-continuation loop in isolated context so main stays lean. | `/gsd-debug` | advanced stub |
| gsd-code-reviewer | Reviews source files for bugs, security issues, and code-quality problems; produces REVIEW.md. | `/gsd-code-review` | advanced stub |
| gsd-code-fixer | Applies fixes to REVIEW.md findings with atomic per-fix commits; produces REVIEW-FIX.md. | `/gsd-code-review --fix` | advanced stub |
| gsd-ai-researcher | Researches a chosen AI framework's official docs into implementation-ready guidance (AI-SPEC.md §3–§4b). | `/gsd-ai-integration-phase` | advanced stub |
| gsd-domain-researcher | Surfaces domain-expert evaluation criteria and failure modes for an AI system (AI-SPEC.md §1b). | `/gsd-ai-integration-phase` | advanced stub |
| gsd-eval-planner | Designs structured evaluation strategy for an AI phase (AI-SPEC.md §5–§7). | `/gsd-ai-integration-phase` | advanced stub |
| gsd-eval-auditor | Retroactive audit of an AI phase's evaluation coverage; produces EVAL-REVIEW.md (COVERED/PARTIAL/MISSING). | `/gsd-eval-review` | advanced stub |
| gsd-framework-selector | ≤6-question interactive decision matrix that scores and recommends an AI/LLM framework. | `/gsd-ai-integration-phase` | advanced stub |
| gsd-intel-updater | Writes structured intel files (`.planning/intel/*.json`) used as a queryable codebase knowledge base. | `/gsd-map-codebase --query` | advanced stub |
| gsd-doc-classifier | Classifies a si

# FILE: docs/installer-migrations.md

# Installer Migration Architecture

This document defines the migration layer for GSD installs and upgrades.
It is for contributors who need to retire files, move install surfaces,
rewrite runtime config, or preserve user data while changing how GSD is
installed.

After reading this document, a contributor should be able to add a new
installer migration without guessing which files are safe to remove or how
to protect local user changes.

## Problem

The installer already handles several upgrade behaviors:

- replacing GSD-managed command, skill, agent, hook, and engine files
- backing up locally modified managed files before replacement
- preserving known user-owned artifacts
- cleaning old hook files and hook registrations
- rewriting runtime-specific configuration formats
- rolling back some failed Codex installs

Those behaviors are currently distributed across install branches. That
works for isolated fixes, but it makes feature retirement risky. A future
change can remove a file from the package while leaving stale installed
copies behind, or delete a user-created file because it happens to live
inside a GSD-managed directory.

The migration layer exists to make upgrade behavior explicit, reviewed, and
repeatable.

## Design Goals

1. Protect user data by default.
2. Remove stale GSD-managed files when a feature is retired.
3. Make destructive actions visible before they run.
4. Record what happened so future installs do not re-run the same migration.
5. Give each runtime the same safety model, even when the concrete files differ.
6. Keep migration authoring small enough that contributors use it instead of
   adding another one-off cleanup block.

## Non-Goals

- This is not a general package manager.
- This is not a database migration system.
- This does not automatically infer every historical install layout.
- This does not remove arbitrary user files.
- This does not replace the existing install transforms in one step.

## Terms

**Managed file**

A file that GSD installed and recorded in the install manifest. Managed files
can be replaced automatically when unchanged. If changed locally, they must be
backed up or merged.

**User-owned file**

A file created or maintained by a user workflow or by the user directly. These
files must never be removed just because they sit under a GSD directory.

**Unknown file**

A file found under an install root that is not in the manifest and is not
classified as user-owned. Unknown files are preserved unless a migration
explicitly classifies them with evidence.

**Migration**

A versioned change set that can inspect the current install, produce a plan,
and apply that plan after safety checks pass.

**Plan**

A list of proposed filesystem and config actions. A plan is safe to show to a
user. It describes what will happen and why, without mutating disk.

**Journal**

A per-run record of applied actions and rollback data. It exists so failed
installs can restore the pre-run state where possible.

## State Files

The migration layer uses the existing file manifest and adds one install-state
record.

### File Manifest

The existing manifest remains the ownership baseline. It records the installed
GSD version, install mode, and hashes for distribution-owned files.

The invariant is strict:

- distribution-owned files are manifest-tracked
- user-owned files are preserved and omitted from manifest hashes
- a path cannot be both

### Install State

The installer writes an install-state file next to the manifest.

Required fields:

```json
{
  "schema": 1,
  "runtime": "codex",
  "scope": "global",
  "installed_version": "1.50.0",
  "install_mode": "full",
  "applied_migrations": [
    {
      "id": "2026-05-11-codex-hooks-layout",
      "package_version": "1.50.0",
      "checksum": "sha256:...",
      "applied_at": "2026-05-11T00:00:00.000Z"
    }
  ]
}
```

The checksum is calculated from the migration definition. If an applied
migration's checksum changes, the installer must warn and refuse to silently
re-run it. Fix-forward migrations should use a new migration id.

## Migration Record

Each migration exports a plain record plus pure planning logic.

Required fields:

```js
module.exports = {
  id: '2026-05-11-runtime-layout-example',
  title: 'Move legacy commands into runtime skills',
  description: 'Move legacy runtime command files into the generated skill layout.',
  introducedIn: '1.50.0',
  runtimes: ['claude', 'codex', 'gemini'],
  scopes: ['global', 'local'],
  destructive: true,
  plan(ctx) {
    return [];
  }
};
```

The Installer Migration Authoring Guard Module rejects records that omit `id`,
`title`, `description`, `introducedIn`, `scopes`, `destructive`, or `plan`.
`runtimes` remains optional only for migrations intentionally shared by every
runtime, but scope must always be explicit so an author cannot accidentally
broaden local/global behavior.

The `plan(ctx)` function receives an install context with runtime, scope,
target directory, previous manifest, install state, package manifest, and
filesystem helpers. It returns actions. It must not mutate disk.

Migrations may use helper predicates such as:

- `isManaged(relPath)`
- `isUserOwned(relPath)`
- `hashMatchesManifest(relPath)`
- `exists(relPath)`
- `readJson(relPath)`
- `readToml(relPath)`

## Action Types

Migrations produce a small set of action types. The executor owns mutation,
backup, rollback, and reporting.

### remove-managed

Remove a path only when it is known to be GSD-managed and unchanged from the
previous manifest, or when the migration provides a purpose-built detector for
an old GSD-owned shape.

Authoring guardrail: every `remove-managed` action must include
`ownershipEvidence` explaining the manifest entry, generated marker, or
purpose-built detector that proves GSD ownership.

Use for retired hooks, old generated agents, deprecated command files, and
stale runtime-specific generated artifacts.

### backup-and-remove

Back up a managed path before removal be
