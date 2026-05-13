# Missing Repo Summary Source: HKUDS/CLI-Anything

- URL: https://github.com/HKUDS/CLI-Anything
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__CLI-Anything
- Clone Status: cloned
- Language: Python
- Stars: 34315
- Topics: 
- Description: "CLI-Anything: Making ALL Software Agent-Native" -- CLI-Hub: https://clianything.cc/

## Extracted README / Docs / Examples



# FILE: README_JA.md

<h1 align="center"><img src="assets/icon.png" alt="" width="64" style="vertical-align: middle;">&nbsp; CLI-Anything: すべてのソフトウェアをエージェントネイティブに</h1>

<p align="center">
  <strong>今日のソフトウェアは人間👨‍💻のためのもの。明日のユーザーはエージェント🤖。<br>
CLI-Anything: AIエージェントと世界のソフトウェアの架け橋</strong><br>
</p>

**🌐 [CLI-Hub](https://hkuds.github.io/CLI-Anything/)**: コミュニティが構築した全CLIを **[CLI-Hub](https://hkuds.github.io/CLI-Anything/)** で探索、ワンコマンドでインストール。自分のCLIを追加したい？[PRを送信](https://github.com/HKUDS/CLI-Anything/blob/main/CONTRIBUTING.md) — Hubは即座に更新されます。

<p align="center">
  <a href="#-クイックスタート"><img src="https://img.shields.io/badge/Quick_Start-5_min-blue?style=for-the-badge" alt="クイックスタート"></a>
  <a href="#-デモンストレーション"><img src="https://img.shields.io/badge/Demos-12_Apps-green?style=for-the-badge" alt="デモ"></a>
  <a href="#-テスト結果"><img src="https://img.shields.io/badge/Tests-1%2C540_Passing-brightgreen?style=for-the-badge" alt="テスト"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge" alt="ライセンス"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/click-≥8.0-green" alt="Click">
  <img src="https://img.shields.io/badge/pytest-100%25_pass-brightgreen" alt="Pytest">
  <img src="https://img.shields.io/badge/coverage-unit_%2B_e2e-orange" alt="Coverage">
  <img src="https://img.shields.io/badge/output-JSON_%2B_Human-blueviolet" alt="Output">
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
<a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

**ワンコマンド**: あらゆるソフトウェアをOpenClaw、nanobot、Cursor、Claude Codeなどのエージェント対応に。&nbsp;&nbsp;[**English**](README.md) | [**中文文档**](README_CN.md)

<p align="center">
  <img src="assets/cli-typing.gif" alt="CLI-Anything タイピングデモ" width="800">
</p>

<p align="center">
  <img src="assets/teaser.png" alt="CLI-Anything ティーザー" width="800">
</p>

---

## 🤔 なぜCLIなのか？

CLIは人間とAIエージェント両方にとって普遍的なインターフェースです：

• **構造化 & 組み合わせ可能** - テキストコマンドはLLMのフォーマットに適合し、複雑なワークフローのために連鎖可能

• **軽量 & 汎用的** - 最小限のオーバーヘッドで、依存関係なくすべてのシステムで動作

• **自己記述的** - --helpフラグがエージェントが発見できる自動ドキュメントを提供

• **実証済みの成功** - Claude Codeは毎日何千もの実際のワークフローをCLIを通じて実行

• **エージェントファースト設計** - 構造化されたJSON出力がパース処理の複雑さを排除

• **決定論的 & 信頼性** - 一貫した結果が予測可能なエージェントの動作を実現

## 🚀 クイックスタート

### 前提条件

- **Python 3.10+**
- 対象ソフトウェアがインストール済みであること（例：GIMP、Blender、LibreOffice、または独自のアプリケーション）
- サポートされているAIコーディングエージェント: [Claude Code](#-claude-code) | [OpenClaw](#-openclaw) | [OpenCode](#-opencode) | [Codex](#-codex) | [Qodercli](#-qodercli) | [GitHub Copilot CLI](#-github-copilot-cli) | [その他のプラットフォーム](#-その他のプラットフォーム近日公開)

### プラットフォームを選択

<details open>
<summary><h4 id="-claude-code">⚡ Claude Code</h4></summary>

**ステップ1: マーケットプレイスの追加**

CLI-AnythingはGitHub上でホストされるClaude Codeプラグインマーケットプレイスとして配布されています。

```bash
# CLI-Anythingマーケットプレイスを追加
/plugin marketplace add HKUDS/CLI-Anything
```

**ステップ2: プラグインのインストール**

```bash
# マーケットプレイスからcli-anythingプラグインをインストール
/plugin install cli-anything
```

これで完了です。プラグインがClaude Codeセッションで利用可能になります。

**ステップ3: ワンコマンドでCLIを構築**

```bash
# /cli-anything:cli-anything <ソフトウェアのパスまたはリポジトリ>
# GIMPの完全なCLIを生成（全7フェーズ）
/cli-anything:cli-anything ./gimp

# 注: Claude Codeが2.x未満の場合は、"/cli-anything"を代わりに使用してください。
```

これにより完全なパイプラインが実行されます：
1. 🔍 **分析** — ソースコードをスキャンし、GUIアクションをAPIにマッピング
2. 📐 **設計** — コマンドグループ、状態モデル、出力フォーマットを設計
3. 🔨 **実装** — REPL、JSON出力、アンドゥ/リドゥ機能を備えたClick CLIを構築
4. 📋 **テスト計画** — ユニットテスト + E2Eテスト計画のTEST.mdを作成
5. 🧪 **テスト作成** — 包括的なテストスイートを実装
6. 📝 **ドキュメント** — TEST.mdを結果で更新
7. 📦 **公開** — `setup.py`を作成し、PATHにインストール

**ステップ4（オプション）: CLIの改善と拡張**

初回ビルド後、CLIを反復的に改善してカバレッジを拡大し、不足している機能を追加できます：

```bash
# 広範な改善 — エージェントがすべての機能のギャップを分析
/cli-anything:refine ./gimp

# 集中的な改善 — 特定の機能領域をターゲット
/cli-anything:refine ./gimp "画像のバッチ処理とフィルタのCLIを追加したい"
```

refineコマンドは、ソフトウェアの全機能と現在のCLIカバレッジの間のギャップ分析を行い、特定されたギャップに対して新しいコマンド、テスト、ドキュメントを実装します。複数回実行してカバレッジを着実に拡大できます — 各実行はインクリメンタルで非破壊的です。

<details>
<summary><strong>代替方法: 手動インストール</strong></summary>

マーケットプレイスを使用しない場合：

```bash
# リポジトリをクローン
git clone https://github.com/HKUDS/CLI-Anything.git

# プラグインをClaude Codeのプラグインディレクトリにコピー
cp -r CLI-Anything/cli-anything-plugin ~/.claude/plugins/cli-anything

# プラグインをリロード
/reload-plugins
```

</details>

</details>

<details>
<summary><h4 id="-opencode">⚡ OpenCode（実験的）</h4></summary>

**ステップ1: コマンドのインストール**

CLI-Anythingのコマンド**と** `HARNESS.md` をOpenCodeのコマンドディレクトリにコピーします：

```bash
# リポジトリをクローン
git clone https://github.com/HKUDS/CLI-Anything.git

# グローバルインストール（すべてのプロジェクトで利用可能）
cp CLI-Anything/opencode-commands/*.md ~/.config/opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md ~/.config/opencode/commands/

# またはプロジェクトレベルのインストール
cp CLI-Anything/opencode-commands/*.md .opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md .opencode/commands/
```

> **注:** `HARNESS.md`はすべてのコマンドが参照する方法論の仕様書です。コマンドと同じディレクトリに配置する必要があります。

これにより5つのスラッシュコマンドが追加されます: `/cli-anything`、`/cli-anything-refine`、`/cli-anything-test`、`/cli-anything-validate`、`/cli-anything-list`。

**ステップ2: ワンコマンドでCLIを構築**

```bash
# GIMPの完全なCLIを生成（全7フェーズ）
/cli-anything ./gimp

# GitHubリポジトリからビルド
/cli-anything https://github.com/blender/blender
```

コマンドはサブタスクとして実行され、Claude Codeと同じ7フェーズの方法論に従います。

**ステップ3（オプション）: CLIの改善と拡張**

```bash
# 広範な改善 — エージェントがすべての機能のギャップを分析
/cli-anything-refine ./gimp

# 集中的な改善 — 特定の機能領域をターゲット
/cli-anything-refine ./gimp "バッチ処理とフィルタ"
```

</details>

<details>

<summary><h4 id="-qodercli">⚡ Qodercli <sup><code>コミュニティ</code></sup></h4></summary>

**ステップ1: プラグインの登録**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
bash CLI-Anything/qoder-plugin/setup-qodercli.sh
```

これにより`~/.qoder.json`にcli-anythingプラグインが登録されます。登録後、新しいQodercliセッションを開始してください。

**ステップ2: QodercliからCLI-Anythingを使用**

```bash
/cli-anything:cli-anything ./gimp
/cli-anything:refine ./gimp "バッチ処理とフィルタ"
/cli-anything:validate ./gimp
```
</details>

<details>

<summary><h4 id="-openclaw">⚡ OpenClaw</h4></summary>

**ステップ1: スキルのインストール**

CLI-Anything はネイティブな OpenClaw `SKILL.md` ファイルを提供しています。OpenClaw のスキルディレクトリにコピーしてください：

```bash
# リポジトリをクローン
git clone https://github.com/HKUDS/CLI-Anything.git

# グローバルスキルフォルダにインストール
mkdir -p ~/.openclaw/skills/cli-anything
cp CLI-Anything/openclaw-skill/SKILL.md ~/.openclaw/skills/cli-anything/SKILL.md
```

**ステップ2: CLIの構築**

インストール後、OpenClaw 内で以下のようにスキルを呼び出せます：

`@cli-anything build a CLI for ./gimp`

このスキルは Claude Code や OpenCode と同じ7段階の方法論に従っています。

</details>

<details>

<summary><h4 id="-codex">⚡ Codex <sup><code>実験的</code></sup> <sup><code>コミュニティ</code></sup></h4></summary>

**ステップ1: スキルのインストール**

同梱のインストーラーを実行します：

```bash
# リポジトリをクローン
git clone https://github.com/HKUDS/CLI-Anything.git

# スキルをインストール
bash CLI-Anything/codex-skill/scripts/install.sh
```

Windows PowerShellの場合：

```powershell
.\CLI-Anything\codex-skill\scripts\install.ps1
```

これにより`$CODEX_HOME/skills/cli-anything`（`CODEX_HOME`が未設定の場合は`~/.codex/skills/cli-anything`）にスキルがインストールされます。

インストール後、検出されるようにCodexを再起動してください。

**ステップ2: CodexからCLI-Anythingを使用**

自然言語でタスクを説明します。例：

```text
CLI-Anythingを使って./gimpのハーネスを構築して
CLI-Anythingを使って./shotcutのピクチャーインピクチャーワークフローを改善して
CLI-Anythingを使って./libreofficeを検証して
```

CodexスキルはClaude CodeプラグインおよびOpenCodeコマンドと同じ方法論を適用しつつ、生成されるPythonハーネスのフォーマットは変更されません。
</details>

<details>

<summary><h4 id="-github-copilot-cli">⚡ GitHub Copilot CLI <sup><code>コミュニティ</code></sup></h4></summary>

**ステップ1: プラグインのインストール**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything
copilot plugin install ./cli-anything-plugin
```

これにより、CLI-Anything プラグインが GitHub Copilot CLI にインストールされます。プラグインはすでに GitHub Copilot CLI セッションで利用できるはずです。

**ステップ2: GitHub Copilot CLIからCLI-Anythingを使用**

```bash
/cli-anything:cli-anything ./gimp
/cli-anything:refine ./gimp "バッチ処理とフィルタ"
/cli-anything:validate ./gimp
```

</details>

<details>
<summary><h4 id="-その他のプラットフォーム近日公開">🔮 その他のプラットフォーム（近日公開）</h4></summary>

CLI-Anythingはプラットフォーム非依存で設計されています。より多くのAIコーディングエージェントのサポートを予定しています：

- **Codex** — `codex-skill/` 内の同梱スキルで利用可能
- **Cursor** — 近日公開
- **Windsurf** — 近日公開
- **お好みのツール** — コントリビューション歓迎！リファレンス実装については`opencode-commands/`ディレクトリをご覧ください。

</details>

### 生成されたCLIの使用

どのプラットフォームでビルドしても、生成されたCLIは同じ方法で動作します：

```bash
# PATHにインストール
cd gimp/agent-harness && pip install -e .

# どこからでも使用可能
cli-anything-gimp --help
cli-anything-gimp project new --width 1920 --height 1080 -o poster.json
cli-anything-gimp --json layer add -n "Background" --type solid --color "#1a1a2e"

# インタラクティブREPLに入る
cli-anything-gimp
```

---

## 💡 CLI-Anythingのビジョン: エージェントネイティブソフトウェアの構築

• 🌐 **ユニバーサルアクセス** - すべてのソフトウェアが構造化されたCLIを通じて即座にエージェント制御可能に。

• 🔗 **シームレスな統合** - エージェントがAPI、GUI、再構築、複雑なラッパーなしにあらゆるアプリケーションを制御。

• 🚀 **未来志向のエコシステム** - ワンコマンドで人間向けに設計されたソフトウェアをエージェントネイティブツールに変換。

---

## 🔧 CLI-Anythingの活用シーン

| カテゴリ | エージェントネイティブにする方法 | 代表例 |
|----------|----------------------|----------|
| **📂 GitHubリポジトリ** | あらゆるオープンソースプロジェクトを自動CLI生成でエージェント制御可能なツールに変換 | VSCodium, WordPress, Calibre, Zotero, Joplin, Logseq, Penpot, Super Productivity |
| **🤖 AI/MLプラットフォーム** | 構造化されたコマンドでモデルの訓練、推論パイプライン、ハイパーパラメータチューニングを自動化 | Stable Diffusion WebUI, ComfyUI, InvokeAI, Text-generation-webui, Open WebUI, Fooocus, Kohya_ss, AnythingLLM, SillyTavern |
| **📊 データ & アナリティクス** | プログラマティックなデータ処理、可視化、統計分析ワークフローを実現 | JupyterLab, Apache Superset, Metabase, Redash, DBeaver, KNIME, Orange, OpenSearch Dashboards, Lightdash |
| **💻 開発ツール** | コマンドインターフェースでコード編集、ビルド、テスト、デプロイプロセスを効率化 | Jenkins, Gitea, Hoppscotch, Portainer, pgAdmin, SonarQube, ArgoCD, OpenLens, Insomnia, Beekeeper Studio |
| **🎨 クリエイティブ & メディア** | コンテンツ作成、編集、レンダリングワークフローをプログラムで制御 | Blender, GIMP, OBS Studio, Audacity, Krita, Kdenlive, Shotcut, Inkscape, Darktable, LMMS, Ardour |
| **🔬 科学計算** | 研究ワークフロ

# FILE: README.md

<h1 align="center"><img src="assets/icon.png" alt="" width="64" style="vertical-align: middle;">&nbsp; CLI-Anything: Making ALL Software Agent-Native</h1>

<p align="center">
  <strong>Today's Software Serves Humans👨‍💻. Tomorrow's Users will be Agents🤖.<br>
CLI-Anything: Bridging the Gap Between AI Agents and the World's Software</strong><br>
</p>

**🌐 [CLI-Hub](https://hkuds.github.io/CLI-Anything/)**: `pip install cli-anything-hub` then `cli-hub install <name>` — browse, install, and manage all community-built CLIs. Want to add your own? [Open a PR](https://github.com/HKUDS/CLI-Anything/blob/main/CONTRIBUTING.md) — the hub updates instantly.

**🎬 [See Demos](#-real-world-demos)**: Watch AI agents use generated CLIs plus preview, live preview, and trajectory loops to produce real artifacts — CAD builds, 3D scenes, diagrams, gameplay, subtitles, and more.

**🙋 [Become a Contributor, or Request a CLI]**: [Join us](https://github.com/HKUDS/CLI-Anything/issues/new?template=contributor-signup.yml)! Sign up to build a new CLI harness — once reviewed and merged, you'll gain access as one of our community contributors! Wish CLI-Anything supported a specific software or service? Submit a [wishlist request](https://github.com/HKUDS/CLI-Anything/issues/new?template=cli-wishlist.yml)!

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-5_min-blue?style=for-the-badge" alt="Quick Start"></a>
  <a href="https://hkuds.github.io/CLI-Anything/"><img src="https://img.shields.io/badge/CLI_Hub-Browse_%26_Install-ff69b4?style=for-the-badge" alt="CLI Hub"></a>
  <a href="#-demonstrations"><img src="https://img.shields.io/badge/Demos-18_Apps-green?style=for-the-badge" alt="Demos"></a>
  <a href="#-test-results"><img src="https://img.shields.io/badge/Tests-2%2C269_Passing-brightgreen?style=for-the-badge" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/click-≥8.0-green" alt="Click">
  <img src="https://img.shields.io/badge/pytest-100%25_pass-brightgreen" alt="Pytest">
  <img src="https://img.shields.io/badge/coverage-unit_%2B_e2e-orange" alt="Coverage">
  <img src="https://img.shields.io/badge/output-JSON_%2B_Human-blueviolet" alt="Output">
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
<a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

**One Command Line**: Make any software agent-ready for Pi, OpenClaw, nanobot, Cursor, Claude Code, etc.&nbsp;&nbsp;[**中文文档**](README_CN.md) | [**日本語ドキュメント**](README_JA.md)

<p align="center">
  <img src="assets/cli-typing.gif" alt="CLI-Anything typing demo" width="800">
</p>

<p align="center">
  <img src="assets/teaser.png" alt="CLI-Anything Teaser" width="800">
</p>

---

## 📰 News

> Thanks to all invaluable efforts from the community! More updates continuously on the way everyday..

- **2026-04-18** 🧩 **All SKILL.md files are now being unified under the top-level `skills/` directory** — every CLI skill can be installed from one canonical source with `npx skills add HKUDS/CLI-Anything --skill <skill-name> -g -y`. We also added root-skill validation CI, synced contribution / PR docs and REPL skill-path hints to the new layout, and refreshed the **CLI-Hub** install-first frontend around the new `npx skills` flow.

- **2026-04-17** 🌐 **CLI-Hub** received another install UX pass — public registry metadata and skill coverage were tightened, visit counting was corrected, and the web hub was further refined. 🧪 **Shotcut** render output duration was fixed (#92). 📝 **SKILL** contribution paths were corrected for the new docs flow (#224), and the skill generator now safely handles empty intros (#203).

- **2026-04-16** 🗺️ **QGIS CLI** merged (#207) — a full GIS / map authoring harness landed. 🧬 **UniMol Tools CLI** merged (#219) for molecular modeling workflows. 🌐 **CLI-Hub** also added more public CLIs, including **py4csr**, refreshed its generated meta-skill, corrected SKILL contribution docs, and fixed `apt-get` package extraction in skill generation (#204).

- **2026-04-16** 📈 **Unreal Insights CLI** expanded — added background capture session control (`capture start/status/snapshot/stop`), engine-root-matched `UnrealInsights.exe` resolution/build flows, and refreshed docs/tests for the new orchestration workflow.

- **2026-04-15** 🌐 **CLI-Hub** updated to **v0.2.0** — the PyPI package now supports public CLIs from multiple install sources (`pip`, `npm`, `brew`, bundled/system tools), backed by a new `public_registry.json`. The Hub frontend was redesigned with separate **CLI-Anything CLIs** and **Public CLIs** decks, and live end-to-end checks now cover real install, update, and uninstall flows across both pip and npm packages.

- **2026-04-14** 🧭 **Safari CLI** merged (#212) and added to the Hub registry — browser automation via `safari-mcp`. 🎬 **Kdenlive** also received compatibility fixes for Gen 5 project output and invalid project generation.

- **2026-04-13** 📓 **Obsidian CLI** merged (#211) — knowledge management harness via the Local REST API, with 48 unit tests and 7 E2E tests. ⛓️ **Eth2-Quickstart CLI** merged (#195) — Ethereum staking node management harness. 📚 **Zotero CLI** updated to v0.4.1 (#201) — now shipped from its standalone repo, and CLI-Hub gained support for remote `skill_md` URLs.

- **2026-04-11** 🔗 **n8n CLI** merged (#188) — workflow automation harness for self-hosted automation flows. 🔧 **Exa CLI** fix (#205) added the `x-exa-integration` header for usage tracking. 📦 **CLI-Hub** also gained its PyPI auto-publish workflow and package refresh pipeline.

- **2026-04-10** 📦 **CLI-Hub package manager** launched — `pip install cli-anything-hub` to browse, search, install, update, and uninstall CLI-Anything harnesses from one command. The web Hub also shipped its first install-focused frontend refresh and "Empower yourself" toolkit card.

<details>
<summary>Earlier news (Apr 1–9)</summary>

- **2026-04-09** 🧹 Cleanup and docs pass (#200) — fixed Openscreen test subtotals, added Openscreen to the Chinese README and project structure, and clarified `/cli-anything` command syntax in the docs.

- **2026-04-08** 🎬 **Openscreen CLI** merged (#183) — screen recording editor harness with 101 tests. ☁️ **CloudAnalyzer CLI** merged (#181) — cloud cost analysis harness with 27 commands. 🌊 **SeaClip / PM2 / ChromaDB** harnesses merged (#129).

- **2026-04-07** 🔄 **Dify Workflow CLI** merged (#191) — workflow automation wrapper. 🔧 **Inkscape** auto-save fix (#193, fixes #182). 🛡️ **DomShell security hardening** (#156) — URL validation and DOM sanitization for the browser CLI. 🥧 **Pi Coding Agent extension** merged (#178).

- **2026-04-06** 🔍 **Exa CLI** merged (#172) — AI-powered web search and answers harness. 🎮 **Godot CLI** merged (#140) — game engine harness with a full demo-game E2E pipeline. ☁️ **CloudAnalyzer** review fixes and frontend improvements also landed.

- **2026-04-03** 🧪 **WireMock CLI** merged (#170) — HTTP mock server harness for API testing. 🥧 **Pi Coding Agent** extension support also landed, and CLI demo recordings were added to the docs.

- **2026-04-01** ⚔️ **Slay the Spire II CLI** merged (#148) — deck-building roguelike harness. 🎥 **VideoCaptioner CLI** merged (#166) — AI-powered video captioning harness. 🛰️ **IntelWatch** was added to the registry for B2B OSINT workflows.

</details>

<details>
<summary>Earlier news (Mar 23–30)</summary>

- **2026-03-30** 🏗️ **CLI-Anything v0.2.0** — HARNESS.md progressive disclosure redesign. Detailed guides extracted into `guides/` for on-demand loading. Phases 1–7 now contiguous. Key Principles and Rules merged into a single authoritative section.

- **2026-03-29** 📐 Blender skill docs updated — enforce absolute render paths and correct prerequisites.

- **2026-03-28** 🌐 **CLIBrowser** added to CLI-Hub registry for agent-accessible browser automation.

- **2026-03-27** 📚 Zotero SKILL.md enhanced with agent-facing constraints; REPL config and executable resolution fixes.

- **2026-03-26** 📖 **Zotero CLI** harness landed for Zotero desktop (library management, collections, citations). Draw.io custom ID bugfix (#132) and registry.json syntax fix.

- **2026-03-25** 🎮 **RenderDoc CLI** merged for GPU frame capture analysis. FreeCAD updated for v1.1. Blender EEVEE engine name corrected. Zoom token permissions hardened.

- **2026-03-24** 🏭 **FreeCAD CLI** added with 258 commands across 17 groups. **iTerm2** and **Teltonika RMS** harnesses added to registry.

- **2026-03-23** 🤖 Launched **CLI-Hub meta-skill** — agents can now discover and install CLIs autonomously. **Krita CLI** harness merged for digital painting.

</details>

<details>
<summary>Earlier news (Mar 11–22)</summary>

- **2026-03-22** 🎵 **MuseScore CLI** merged with transpose, export, and instrument management.

- **2026-03-21** 🔧 Infrastructure improvements — refined test harnesses and documentation across multiple CLIs. Enhanced Windows compatibility for several backends.

- **2026-03-20** 🌐 **Novita AI** CLI added for OpenAI-compatible API access. Registry metadata improvements for better hub discovery.

- **2026-03-19** 📦 Package structure refinements across harnesses. Improved SKILL.md generation with better command documentation.

- **2026-03-18** 🧪 Test coverage expansion — additional E2E scenarios and edge case validation across multiple CLIs.

- **2026-03-17** 🌐 Launched the **[CLI-Hub](https://hkuds.github.io/CLI-Anything/)** — a central registry where you can browse, search, and inst

# FILE: README_CN.md

<h1 align="center"><img src="assets/icon.png" alt="" width="64" style="vertical-align: middle;">&nbsp; CLI-Anything: 让所有软件都能被 Agent 驱动</h1>

<p align="center">
  <strong>今天的软件为人而生👨‍💻，明天的用户是 Agent🤖<br>
CLI-Anything：连接 AI Agent 与全世界软件的桥梁</strong><br>
</p>

**🌐 [CLI-Hub](https://hkuds.github.io/CLI-Anything/)**：在 **[CLI-Hub](https://hkuds.github.io/CLI-Anything/)** 探索社区已构建的所有 CLI，一条命令即可安装。想贡献你的 CLI？[提交 PR](https://github.com/HKUDS/CLI-Anything/blob/main/CONTRIBUTING.md) — Hub 会即时更新。

<p align="center">
  <a href="#-快速上手"><img src="https://img.shields.io/badge/快速上手-5_分钟-blue?style=for-the-badge" alt="Quick Start"></a>
  <a href="#-实测展示"><img src="https://img.shields.io/badge/Demo-13_款软件-green?style=for-the-badge" alt="Demos"></a>
  <a href="#-测试结果"><img src="https://img.shields.io/badge/测试-1%2C741_通过-brightgreen?style=for-the-badge" alt="Tests"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-≥3.10-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/click-≥8.0-green" alt="Click">
  <img src="https://img.shields.io/badge/pytest-100%25_pass-brightgreen" alt="Pytest">
  <img src="https://img.shields.io/badge/coverage-unit_%2B_e2e-orange" alt="Coverage">
  <img src="https://img.shields.io/badge/output-JSON_%2B_Human-blueviolet" alt="Output">
  <a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/飞书-交流群-E9DBFC?style=flat&logo=feishu&logoColor=white" alt="Feishu"></a>
<a href="https://github.com/HKUDS/.github/blob/main/profile/README.md"><img src="https://img.shields.io/badge/微信-交流群-C5EAB4?style=flat&logo=wechat&logoColor=white" alt="WeChat"></a>
</p>

**一行命令**，让任意软件接入 OpenClaw、nanobot、Cursor、Claude Code 等 Agent 框架。

<p align="center">
  <img src="assets/cli-typing.gif" alt="CLI-Anything typing demo" width="800">
</p>

<p align="center">
  <img src="assets/teaser.png" alt="CLI-Anything Teaser" width="800">
</p>

---

## 🤔 为什么是 CLI？

CLI 是人类和 AI Agent 共通的万能接口：

• **结构化、可组合** - 文本命令天然匹配 LLM 的输入格式，可自由串联成复杂工作流

• **轻量且通用** - 几乎零开销，跨平台运行，不依赖额外环境

• **自描述** - 一个 `--help` 就能让 Agent 自动发现所有功能

• **久经验证** - Claude Code 每天通过 CLI 执行数以千计的真实任务

• **Agent 友好** - 结构化 JSON 输出，Agent 无需任何额外解析

• **确定且可靠** - 输出稳定一致，Agent 行为可预测

## 🚀 快速上手

### 环境要求

- **Python 3.10+**
- 目标软件已安装（如 GIMP、Blender、LibreOffice 或你自己的应用）
- 支持的 AI 编程工具之一：[Claude Code](#-claude-code) | [OpenClaw](#-openclaw) | [OpenCode](#-opencode) | [Codex](#-codex) | [Qodercli](#-qodercli) | [GitHub Copilot CLI](#-github-copilot-cli) | [更多平台](#-更多平台即将支持)

### 选择你的平台

<details open>
<summary><h4 id="-claude-code">⚡ Claude Code</h4></summary>

**第一步：添加插件市场**

CLI-Anything 以 Claude Code 插件市场的形式托管在 GitHub 上。

```bash
# 添加 CLI-Anything 插件市场
/plugin marketplace add HKUDS/CLI-Anything
```

**第二步：安装插件**

```bash
# 从市场安装 cli-anything 插件
/plugin install cli-anything
```

搞定。插件已经在你的 Claude Code 会话中可用了。

**Windows 注意：** Claude Code 通过 `bash` 执行命令。Windows 下请安装 Git for Windows（包含 `bash` 和 `cygpath`）
或使用 WSL，否则可能出现 `cygpath: command not found`。

**第三步：一行命令生成 CLI**

```bash
# /cli-anything <软件路径或仓库地址>
# 为 GIMP 生成完整的 CLI（7 个阶段全自动）
/cli-anything ./gimp

# 兼容写法（旧版本 Claude Code 可重试）
# /cli-anything:cli-anything ./gimp
```

Claude Code 不同版本的命令兼容说明：
- 优先使用 `/cli-anything` 作为主入口。
- 在已**确认插件已安装并加载**的情况下，若旧版本的 Claude Code 不识别 `/cli-anything`，可尝试兼容写法 `/cli-anything:cli-anything`。
- 其他辅助命令保持 `:子命令` 形式（例如 `/cli-anything:refine`）。

如果出现 `Unknown skill: cli-anything`，两种写法都引用同一个 skill 名称，切换写法无法解决，请优先排查插件是否已安装/加载：
1. 重新加载插件命令：`/reload-plugins`
2. 验证插件是否已加载：`/help cli-anything`（能看到 CLI-Anything 帮助即表示已加载）
3. 如仍未识别，重新从市场安装：
   - `/plugin marketplace add HKUDS/CLI-Anything`
   - `/plugin install cli-anything`
4. 确认插件可用后，再重试入口命令：
   - 推荐：`/cli-anything ./gimp`
   - 仅旧版本：`/cli-anything:cli-anything ./gimp`

完整流水线自动执行：
1. 🔍 **分析** — 扫描源码，将 GUI 操作映射到 API
2. 📐 **设计** — 规划命令分组、状态模型、输出格式
3. 🔨 **实现** — 构建 Click CLI，包含 REPL、JSON 输出、撤销/重做
4. 📋 **规划测试** — 生成 TEST.md，涵盖单元测试和端到端测试计划
5. 🧪 **编写测试** — 实现完整测试套件
6. 📝 **文档** — 更新 TEST.md，写入测试结果
7. 📦 **发布** — 生成 `setup.py`，安装到 PATH

**第四步（可选）：优化和扩展 CLI**

初始构建完成后，你可以迭代优化 CLI，扩展覆盖面并补充缺失的功能：

```bash
# 全面优化 — Agent 分析所有功能的覆盖差距
/cli-anything:refine ./gimp

# 定向优化 — 指定特定功能领域
/cli-anything:refine ./gimp "我需要更多图像批处理和滤镜相关的 CLI"
```

优化命令会对软件的完整功能与当前 CLI 覆盖范围进行差距分析，然后为识别到的差距实现新命令、测试和文档。你可以多次运行该命令，逐步扩大功能覆盖范围 — 每次运行都是增量的、非破坏性的。

<details>
<summary><strong>备选方案：手动安装</strong></summary>

如果你不想用插件市场：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 复制插件到 Claude Code 插件目录
cp -r CLI-Anything/cli-anything-plugin ~/.claude/plugins/cli-anything

# 重新加载插件
/reload-plugins
```

</details>

</details>

<details>
<summary><h4 id="-opencode">⚡ OpenCode （实验性支持）</h4></summary>

**第一步：安装命令**

**注意：** 请升级到最新 OpenCode，旧版本可能使用不同的命令目录路径。

将 CLI-Anything 命令**和** `HARNESS.md` 复制到 OpenCode 命令目录：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 全局安装（所有项目可用）
cp CLI-Anything/opencode-commands/*.md ~/.config/opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md ~/.config/opencode/commands/

# 或项目级安装
cp CLI-Anything/opencode-commands/*.md .opencode/commands/
cp CLI-Anything/cli-anything-plugin/HARNESS.md .opencode/commands/
```

> **注意：** `HARNESS.md` 是所有命令引用的方法论规范，必须和命令文件放在同一目录下。

安装后获得 5 个斜杠命令：`/cli-anything`、`/cli-anything-refine`、`/cli-anything-test`、`/cli-anything-validate` 和 `/cli-anything-list`。

**第二步：一行命令生成 CLI**

```bash
# 为 GIMP 生成完整的 CLI（7 个阶段全自动）
/cli-anything ./gimp

# 从 GitHub 仓库构建
/cli-anything https://github.com/blender/blender
```

命令以子任务方式运行，遵循与 Claude Code 相同的 7 阶段方法论。

**第三步（可选）：优化和扩展 CLI**

```bash
# 全面优化 — Agent 分析所有功能的覆盖差距
/cli-anything-refine ./gimp

# 定向优化 — 指定特定功能领域
/cli-anything-refine ./gimp "批处理和滤镜"
```

</details>

<details>

<summary><h4 id="-qodercli">⚡ Qodercli <sup><code>社区贡献</code></sup></h4></summary>

**第一步：注册插件**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
bash CLI-Anything/qoder-plugin/setup-qodercli.sh
```

脚本会将 cli-anything 插件注册到 `~/.qoder.json`。注册后开启新的 Qodercli 会话即可使用。

**第二步：在 Qodercli 中使用 CLI-Anything**

```bash
/cli-anything:cli-anything ./gimp
/cli-anything:refine ./gimp "批处理和滤镜"
/cli-anything:validate ./gimp
```
</details>

<details>

<summary><h4 id="-openclaw">⚡ OpenClaw</h4></summary>

**第一步：安装 Skill**

CLI-Anything 提供了原生的 OpenClaw `SKILL.md` 文件。请将其复制到你的 OpenClaw 技能目录：

```bash
# Clone the repo
git clone https://github.com/HKUDS/CLI-Anything.git

# Install to the global skills folder
mkdir -p ~/.openclaw/skills/cli-anything
cp CLI-Anything/openclaw-skill/SKILL.md ~/.openclaw/skills/cli-anything/SKILL.md
```

**第二步：构建 CLI**

安装完成后，你就可以在 OpenClaw 中直接调用：

`@cli-anything build a CLI for ./gimp`

该技能采用了与 Claude Code 和 OpenCode 一致的 7 步构建流程。

</details>

<details>

<summary><h4 id="-codex">⚡ Codex <sup><code>实验性</code></sup> <sup><code>社区贡献</code></sup></h4></summary>

**第一步：安装 Skill**

运行仓库内置的安装脚本：

```bash
# 克隆仓库
git clone https://github.com/HKUDS/CLI-Anything.git

# 安装 skill
bash CLI-Anything/codex-skill/scripts/install.sh
```

在 Windows PowerShell 中，可以使用：

```powershell
.\CLI-Anything\codex-skill\scripts\install.ps1
```

脚本会把 skill 安装到 `$CODEX_HOME/skills/cli-anything`；如果没有设置 `CODEX_HOME`，则默认安装到 `~/.codex/skills/cli-anything`。

安装后重启 Codex，让它重新发现这个 skill。

**第二步：在 Codex 里使用 CLI-Anything**

直接用自然语言描述任务，例如：

```text
Use CLI-Anything to build a harness for ./gimp
Use CLI-Anything to refine ./shotcut for picture-in-picture workflows
Use CLI-Anything to validate ./libreoffice
```

这个 Codex skill 复用了 Claude Code 插件和 OpenCode 命令所使用的同一套方法论，
不会改变生成出来的 Python harness 结构。

</details>

<details>

<summary><h4 id="-github-copilot-cli">⚡ GitHub Copilot CLI <sup><code>社区贡献</code></sup></h4></summary>

**第一步：安装插件**

```bash
git clone https://github.com/HKUDS/CLI-Anything.git
cd CLI-Anything
copilot plugin install ./cli-anything-plugin
```

这将 CLI-Anything 插件安装到 GitHub Copilot CLI 中。插件应该已经在你的 GitHub Copilot CLI 会话中可用了。

**第二步：在 GitHub Copilot CLI 中使用 CLI-Anything**

```bash
/cli-anything:cli-anything ./gimp
/cli-anything:refine ./gimp "批处理和滤镜"
/cli-anything:validate ./gimp
```

</details>

<details>
<summary><h4 id="-更多平台即将支持">🔮 更多平台（即将支持）</h4></summary>

CLI-Anything 的设计是平台无关的，计划支持更多 AI 编程工具：

- **Codex** — 已通过 `codex-skill/` 提供接入
- **Cursor** — 即将支持
- **Windsurf** — 即将支持
- **你喜欢的工具** — 欢迎贡献！参考 `opencode-commands/` 目录的实现。

</details>

### 开始使用生成的 CLI

无论你用哪个平台构建，生成的 CLI 使用方式完全一样：

```bash
# 安装到 PATH
cd gimp/agent-harness && pip install -e .

# 随处可用
cli-anything-gimp --help
cli-anything-gimp project new --width 1920 --height 1080 -o poster.json
cli-anything-gimp --json layer add -n "Background" --type solid --color "#1a1a2e"

# 进入交互式 REPL
cli-anything-gimp
```

---

## 💡 CLI-Anything 的愿景：构建 Agent 原生的软件生态

• 🌐 **无门槛接入** - 任何软件都能通过结构化 CLI 即刻被 Agent 操控。

• 🔗 **无缝集成** - 不需要专门的 API、不需要操控 GUI、不需要重构代码，也不需要复杂的适配层。

• 🚀 **面向未来** - 一条命令，就能把为人类设计的软件变成 Agent 的原生工具。

---

## 🔧 适用场景

| 类别 | 如何接入 Agent | 典型软件 |
|------|--------------|---------|
| **📂 GitHub 开源项目** | 通过自动生成 CLI，将任意开源项目转化为 Agent 可控工具 | VSCodium、WordPress、Calibre、Zotero、Joplin、Logseq、Penpot、Super Productivity |
| **🤖 AI/ML 平台** | 用结构化命令驱动模型训练、推理流水线和超参搜索 | Stable Diffusion WebUI、ComfyUI、InvokeAI、Text-generation-webui、Open WebUI、Fooocus、Kohya_ss、AnythingLLM、SillyTavern |
| **📊 数据与分析** | 以编程方式完成数据处理、可视化和统计分析工作流 | JupyterLab、Apache Superset、Metabase、Redash、DBeaver、KNIME、Orange、OpenSearch Dashboards、Lightdash |
| **💻 开发工具** | 通过 CLI 串联代码编辑、构建、测试与部署流程 | Jenkins、Gitea、Hoppscotch、Portainer、pgAdmin、SonarQube、ArgoCD、OpenLens、Insomnia、Beekeeper Studio |
| **🎨 创意与媒体** | 以编程方式控制内容创作、编辑和渲染工作流 | Blender、GIMP、OBS Studio、Audacity、Krita、Kdenlive、Shotcut、Inkscape、Darktable、LMMS、Ardour |
| **📐 图表与可视化** | 以编程方式创建和操作流程图、架构图、ER 图等各类图表 | Draw.io (diagrams.net)、Mermaid、PlantUML、Excalidraw、yEd |
| **🔬 科学计算** | 自动化科研工作流、仿真模拟和复杂计算 | ImageJ、FreeCAD、QGIS、ParaView、Gephi、LibreCAD、Stellarium、KiCad、JASP、Jamovi |
| **🏢 企业与办公** | 将商业应用和生产力工具转化为 Agent 可访问的系统 | NextC

# FILE: docs/PREVIEW_PROTOCOL.md

# Preview Protocol

Last updated: 2026-04-23 UTC

This document proposes a minimal, cross-harness protocol for previewing
intermediate results in CLI-Anything workflows.

The short version:

- Every participating harness emits a standard `Preview Bundle`.
- A bundle is just a directory with a `manifest.json`, a `summary.json`, and
  preview artifacts such as images, clips, JSON dumps, or model files.
- Harnesses still use the real software for rendering. The protocol standardizes
  the preview artifact contract, not the renderer.
- `cli-hub` becomes the generic viewer/inspector for bundles, instead of every
  harness inventing its own monitor UI.

This gives agents and humans one stable way to consume intermediate outputs
across video, CAD, 3D, GPU debugging, and similar workflows.

## Why This Exists

CLI-Anything already has strong rules for final rendering:

- use the real software
- manipulate native formats
- verify real output files

What it does not yet have is a cross-harness protocol for intermediate visual
feedback.

Today, preview-related capability exists in many local forms:

- video thumbnail extraction
- screenshot export
- render presets
- capture thumbnails
- output-target dumps

But these are app-local commands. They do not produce a uniform artifact shape
that an agent runtime, `cli-hub`, or a future host UI can consume in the same
way across tools.

The missing abstraction is not "a universal monitor widget". The missing
abstraction is "a universal preview artifact protocol".

## Design Goals

1. Keep the rendering path honest.
   Previews must still come from the real software, its real backend, or its
   real project format. No toy reimplementation of the app's renderer.
2. Be generic across domains.
   The same protocol should handle video timelines, CAD views, Blender renders,
   RenderDoc outputs, and similar cases.
3. Be cheap enough to use often.
   Previews should be fast, low-resolution, cacheable, and small enough for
   agent loops.
4. Be simple enough to adopt incrementally.
   A harness should be able to add preview support with one command group and a
   small helper, not a new frontend app.
5. Work in headless environments.
   Bundle generation and validation must not require a GUI.

## Non-Goals

- This is not a replacement for final render/export.
- This is not a live remote framebuffer or GUI streaming protocol.
- This does not require every harness to support interactive timeline scrubbing.
- This does not force one preview artifact type. Different apps may emit
  images, clips, JSON, or multiple artifacts together.

## Core Model

The protocol has three layers:

1. Harness layer
   The harness generates real preview artifacts and writes a `Preview Bundle`.
2. Viewer layer
   `cli-hub previews ...` reads any compliant bundle or live session and
   renders a generic inspection view.
3. Host/runtime layer
   An agent host may decide to attach selected bundle artifacts back into model
   context, but this is outside the harness itself.

The central object is the `Preview Bundle`.

For live preview workflows, the stable object is the `Live Session`, with an
append-only `trajectory.json` beside it.

## Preview Bundle

A preview bundle is a directory with a small, stable layout:

```text
<bundle_dir>/
  manifest.json
  summary.json
  artifacts/
    hero.png
    gallery_01.png
    gallery_02.png
    preview.mp4
    pipeline_diff.json
```

`manifest.json` is the machine contract.

`summary.json` is the human/agent summary.

`artifacts/` contains preview outputs generated by the real software or by
native tools that inspect those real outputs.

## Default Bundle Location

When a project path is known:

```text
<project_dir>/.cli-anything/previews/<software>/<recipe>/<bundle_id>/
```

When there is no stable project path yet:

```text
~/.cli-anything/previews/<software>/<recipe>/<bundle_id>/
```

Rationale:

- preview artifacts stay near the project when possible
- bundles are easy to garbage-collect
- `cli-hub` can scan a predictable root

## Bundle ID

Recommended bundle id:

```text
<UTC timestamp>_<short fingerprint>_<recipe>
```

Example:

```text
20260419T104530Z_9f0a2c4b_quick
```

The fingerprint should be derived from:

- project fingerprint or capture fingerprint
- recipe name
- normalized preview args
- harness version
- protocol version

This makes bundles cacheable and reproducible.

## Manifest Schema

Required top-level fields:

| Field | Type | Notes |
|---|---|---|
| `protocol_version` | string | Start with `preview-bundle/v1` |
| `bundle_id` | string | Stable id for this bundle |
| `bundle_kind` | string | `capture` or `diff` |
| `software` | string | Harness name, e.g. `shotcut` |
| `recipe` | string | Harness recipe name, e.g. `quick`, `quad`, `turntable` |
| `status` | string | `ok`, `partial`, or `error` |
| `created_at` | string | ISO-8601 UTC |
| `generator` | object | CLI command, harness version, backend info |
| `source` | object | Project/capture identity and fingerprint |
| `artifacts` | array | Preview artifact descriptors |
| `summary_path` | string | Relative path to `summary.json` |

Recommended optional fields:

| Field | Type | Notes |
|---|---|---|
| `source_bundles` | array | For diff bundles |
| `context` | object | App-specific context, e.g. event id, frame, camera |
| `warnings` | array | Non-fatal warnings |
| `metrics` | object | Cheap summary metrics |
| `labels` | array | Tags for host-side filtering |

### Manifest Example

```json
{
  "protocol_version": "preview-bundle/v1",
  "bundle_id": "20260419T104530Z_9f0a2c4b_quick",
  "bundle_kind": "capture",
  "software": "shotcut",
  "recipe": "quick",
  "status": "ok",
  "created_at": "2026-04-19T10:45:30Z",
  "generator": {
    "entry_point": "cli-anything-shotcut",
    "harness_version": "1.0.0",
    "command": "cli-anything-shotcut --json -p demo.mlt preview capture --recipe quick"
  },
  "source": {
    "project_path": "/work/demo.mlt",
    "project_fingerprint": "

# FILE: docs/PREVIEW_MECHANISM_PROGRESS.md

# Preview Mechanism Progress

Last updated: 2026-04-23 UTC

This document records the current state of the cross-harness preview mechanism
work on the dedicated preview branch.

## Workspace

- Repo: `/root/CLI-Anything-preview`
- Branch: `feat/preview-protocol`
- Current checkpoint commit: `81dbe58`

This checkpoint contains the first end-to-end version of the preview stack,
including live preview sessions, bundle protocol, generic viewing tools, and
FreeCAD motion-backed showcase rendering.

## Mechanism Summary

The current mechanism is built as five layers:

1. `Preview Bundle`
   - A stable on-disk contract for preview outputs.
   - Defined in `docs/PREVIEW_PROTOCOL.md`.
   - Implemented by `cli-anything-plugin/preview_bundle.py` and vendored
     harness helpers.

2. `Harness Preview Commands`
   - Normalized command surface:
     - `preview recipes`
     - `preview capture`
     - `preview latest`
     - `preview diff` where relevant
   - Each harness is responsible for generating truthful preview artifacts with
     the real backend, not by screen scraping.

3. `Live Session`
   - A long-lived directory that tracks:
     - mutable `session.json`
     - append-only `trajectory.json`
     - current bundle head
   - Supports both:
     - explicit push
     - poll-first automatic refresh based on source-state fingerprints

4. `Generic Viewer`
   - Implemented in `cli-hub`.
   - Supports:
     - `cli-hub previews inspect`
     - `cli-hub previews html`
     - `cli-hub previews watch`
     - `cli-hub previews open`
   - Lets agents and humans consume the same preview state through different
     surfaces.

5. `Final Motion Showcase`
   - Separate from preview.
   - Used for end-of-work demonstrations where static preview is not enough.
   - Currently implemented for FreeCAD via real frame-by-frame motion renders.

## What Is Implemented

### Protocol / Platform

- `docs/PREVIEW_PROTOCOL.md`
- `cli-anything-plugin/preview_bundle.py`
- `cli-anything-plugin/HARNESS.md` preview requirements
- `cli-hub/cli_hub/preview.py`
- `cli-hub` previews CLI integration

### Harnesses with preview support

- `shotcut`
  - quick preview capture
  - live session
  - poll-mode auto refresh
  - black-preview regression fixed

- `openscreen`
  - quick preview capture
  - bundle emission
  - append-only `trajectory.json` beside stable preview roots

- `blender`
  - preview capture
  - live session
  - poll-mode auto refresh
  - `preview live status --json` returns `trajectory_summary`
  - real Gyro Observatory demo script with stage-by-stage preview checkpoints

- `freecad`
  - quick preview capture
  - live session
  - poll-mode auto refresh
  - `preview live status --json` returns `trajectory_summary`
  - richer preview/export macro reconstruction
  - motion CLI for true frame rendering

- `renderdoc`
  - preview capture
  - preview diff
  - replay-oriented bundle generation
  - append-only `trajectory.json` for capture/diff history

## Canonical Command Split

Use this wording consistently:

- software harnesses publish previews through `cli-anything-<software> preview ...`
- `cli-hub previews ...` only inspects, renders, opens, or watches existing
  bundles and live sessions

There are no `cli-hub preview`, `cli-hub review`, or `cli-hub open-preview`
aliases in the current command surface.

## FreeCAD-Specific Preview Mechanism Progress

FreeCAD is currently the deepest preview integration on this branch.

Implemented:

- preview capture and live preview
- poll-first live refresh
- `part bounds`
- `part align`
- better preview/export macro reconstruction for:
  - additive/subtractive primitives
  - pattern features
  - mirrored parts
- motion CLI surface:
  - `motion new`
  - `motion list`
  - `motion get`
  - `motion delete`
  - `motion keyframe`
  - `motion sample`
  - `motion render-frames`
  - `motion render-video`

This makes FreeCAD the main proof point for the full mechanism:

- real CLI trajectory
- real preview bundles
- real live session updates
- real final motion render
- programmatic split-screen video composition

## Video / Showcase State

Current reference artifacts are recorded in:

- `docs/FREECAD_VIDEO_REFERENCE.md`

Important completed pieces:

- split-screen agent-manipulation visualization video
- redesigned left-side `Agent Command Stream`
- true FreeCAD motion endings
  - drive
  - turntable spin
  - combo: one full rotation, then forward travel

## Known Gaps

The mechanism is working, but it is not feature-complete.

Current limits:

- live preview is near-real-time, not continuous viewport streaming
- some harnesses are only first-pass preview integrations
- FreeCAD motion is currently part-placement driven, not Assembly-joint driven
- RenderDoc preview is limited by machine graphics/runtime constraints when
  generating fresh captures locally
- Blender now has live preview parity at the protocol/session level, but its
  showcase/demo tooling is still shallower than FreeCAD's motion/video stack

## Recommended Next Work

1. Expand Blender demo tooling beyond the first Gyro Observatory proof point.
2. Restack this preview branch onto a clean `origin/main` base before the PR
   stack grows larger.
3. Split this large checkpoint into a reviewable commit stack later:
   - protocol + cli-hub
   - shotcut / openscreen
   - blender
   - freecad
   - renderdoc
   - demo/video tooling

## Related Docs

- `docs/PREVIEW_PROTOCOL.md`
- `docs/PREVIEW_PROGRESS.md`
- `docs/FREECAD_VIDEO_REFERENCE.md`
- `docs/FREECAD_DEMO_PROPOSALS.md`


# FILE: docs/PREVIEW_PROGRESS.md

# Preview Progress

Last updated: 2026-04-23 UTC

This file tracks the current state of the preview work on the dedicated preview
branch and records the next design direction for live popup preview windows.

## Workspace

- Repo: `/root/CLI-Anything-preview`
- Branch: `feat/preview-protocol`
- Primary protocol doc: `docs/PREVIEW_PROTOCOL.md`

## What Is Implemented

The current branch already has a working first-pass preview stack:

- Shared preview bundle helper:
  `cli-anything-plugin/preview_bundle.py`
- Shared static viewer/inspector:
  `cli-hub/cli_hub/preview.py`
- Preview protocol documented:
  `docs/PREVIEW_PROTOCOL.md`
- Harness-level preview support implemented for:
  - `shotcut`
  - `openscreen`
  - `blender`
  - `freecad`
  - `renderdoc`

The current shape is:

- harnesses emit `preview-bundle/v1` bundles
- `cli-hub` can inspect or render static HTML for a bundle
- preview commands are normalized around:
  - `preview recipes`
  - `preview capture`
  - `preview latest`
- `renderdoc` also has `preview diff`

## New In This Iteration

The preview branch now has working live popup preview loops for:

- `shotcut`
- `freecad`
- `blender`

The current FreeCAD demo selection notes now live in:

- `docs/FREECAD_DEMO_PROPOSALS.md`

The first selected post-landmark showcase is:

- `mars-rover`

The current FreeCAD mechanical-modeling quality push also added:

- `part bounds`
- `part align`
- a new `Curiosity v6` connector pass:
  - mirrored right-side wheel outboard alignment
  - 6 wheel-level axle blocks
  - 4 suspension pivot housings
  - a full real live-preview rerun after those connector parts were added

These commands provide primitive-level world bounding boxes and bbox-anchor
alignment so CLI-built models do not have to rely purely on guessed
`-pos/-rot` placements.

The current FreeCAD video tooling now also has:

- a true `combo` motion ending for Curiosity:
  - one full rotation
  - then forward travel
- a redesigned split-screen left panel:
  - `Agent Command Stream`
  - card-based command display instead of a literal terminal dump
- a render fix in the demo script so custom output paths create parent
  directories before calling `ffmpeg`

What was added:

- `shotcut` live session lifecycle:
  - `preview live start`
  - `preview live push`
  - `preview live status`
  - `preview live stop`
- `shotcut` producer-side auto polling:
  - `preview live start --mode poll --source-poll-ms ...`
  - hidden background `preview live monitor --session-dir ...`
  - project-file fingerprint polling with automatic preview recapture
- `freecad` live session lifecycle:
  - `preview live start`
  - `preview live push`
  - `preview live status`
  - `preview live stop`
- `freecad` producer-side auto polling:
  - `preview live start --mode poll --source-poll-ms ...`
  - hidden background `preview live monitor --session-dir ...`
  - saved project JSON fingerprint polling with automatic preview recapture
  - demo tooling for `freecad`:
  - `docs/scripts/freecad_live_preview_demo.py collect`
  - `docs/scripts/freecad_live_preview_demo.py render`
  - `docs/scripts/freecad_live_preview_demo.py run-all`
  - scenarios:
    - `orbital-relay`
    - `empire-state-building`
    - `taipei-101`
- `blender` live session lifecycle:
  - `preview live start`
  - `preview live push`
  - `preview live status`
  - `preview live stop`
- `blender` producer-side auto polling:
  - `preview live start --mode poll --source-poll-ms ...`
  - hidden background `preview live monitor --session-dir ...`
  - saved scene JSON fingerprint polling with automatic preview recapture
  - demo tooling for `blender`:
  - `docs/scripts/blender_orbital_relay_drone_demo.py`
  - `docs/scripts/blender_preview_story_demo.py`
  - scenarios:
    - `orbital-relay-drone`
    - real staged preview bundles
    - real turntable motion video
    - polished build-story video with turntable ending
- `cli-hub` live viewer surface:
  - `previews inspect` now understands live sessions
  - `previews html` now renders bundle and live-session HTML
  - `previews watch` now serves a live session over localhost with auto-refresh
  - `previews open` now opens bundles or live sessions in a separate window
  - live pages and inspect output now consume `trajectory.json` when present

The live split now looks like this:

- harness owns preview bundle generation and live-session state publication
- harness can now also own source-state polling and automatic bundle refresh
- `cli-hub` owns the popup window, local server, polling page, and browser launch

This is the intended cross-software direction.

## Current Validation Status

### Fully verified on this machine

- `shotcut`
  - preview implementation works
  - black-frame issue was fixed by preferring the ffmpeg preview path
  - preview E2E passes
  - live preview session + live viewer now works end-to-end
  - automatic poll mode now works end-to-end without manual `preview live push`
- `openscreen`
  - preview implementation works
  - preview E2E passes
- `blender`
  - preview implementation works
  - preview E2E passes
  - live preview session lifecycle now works end-to-end
  - automatic poll mode now works end-to-end without manual `preview live push`
  - a real stage-by-stage `gyro-observatory` build now exists with:
    - 4 preview bundle checkpoints
    - a persisted live session
    - a final 1600x1600 Blender still render
- `freecad`
  - preview implementation works on the current Ubuntu machine after local
    environment setup
  - preview E2E passes
  - live preview session + live poll mode now work end-to-end
  - a real programmatic demo video now exists, built from real CLI outputs and
    real live preview bundles
  - preview macro now reconstructs real body/additive/subtractive primitive
    features plus linear/polar/mirror pattern features with placement
  - multiple real Taipei 101 studies now exist; the old shipped scenario has
    been replaced because the earlier stacked-box version was not acce

# FILE: docs/FREECAD_VIDEO_REFERENCE.md

# FreeCAD Demo Video Reference

Last updated: 2026-04-22 UTC

This file records the programmatic video artifacts built from real
`cli-anything-freecad` trajectories and real FreeCAD preview bundles.

## Curiosity V6

Source trajectory:

- `/root/preview-artifacts/20260421/freecad-curiosity-v6/trajectory.json`

Current render target:

- `/root/preview-artifacts/20260421/freecad-curiosity-v6/demo.mp4`

Final rendered artifact:

- `/root/preview-artifacts/20260421/freecad-curiosity-v6/demo.mp4`
- duration: `116.166667s`
- size: `3,011,924 bytes`

Polished split-screen re-render:

- `/root/preview-artifacts/20260422/freecad-curiosity-v6/demo-polished.mp4`
- duration: `71.416667s`
- size: `2,266,665 bytes`

Render command:

```bash
python3 /root/CLI-Anything-preview/docs/scripts/freecad_live_preview_demo.py \
  render \
  --timeline /root/preview-artifacts/20260421/freecad-curiosity-v6/trajectory.json \
  --speed 8
```

Ending showcase method:

- reuse the real final `Curiosity v6` project JSON
- add a staged ground and marker bed as extra real geometry
- generate extra real FreeCAD `preview capture` hero bundles for a sequence of
  posed translations
- append those real hero captures as a final full-screen showcase segment in the
  programmatic video

Expected showcase cache location:

- `/root/preview-artifacts/20260421/freecad-curiosity-v6/showcase/sequence.json`
- `/root/preview-artifacts/20260421/freecad-curiosity-v6/showcase/projects/`
- `/root/preview-artifacts/20260421/freecad-curiosity-v6/showcase/captures/`

Key stills:

- trajectory end:
  `/root/preview-artifacts/20260421/freecad-curiosity-v6/stills/trajectory-end.png`
- showcase start:
  `/root/preview-artifacts/20260421/freecad-curiosity-v6/stills/showcase-start.png`
- showcase mid:
  `/root/preview-artifacts/20260421/freecad-curiosity-v6/stills/showcase-mid.png`
- showcase final:
  `/root/preview-artifacts/20260421/freecad-curiosity-v6/stills/showcase-final.png`

Implementation notes:

- the main split-screen section uses the real `Curiosity v6` live session
  timeline and real copied preview bundles
- the ending showcase uses `12` extra real FreeCAD hero captures
- the showcase segment begins after the main trajectory body and is rendered as
  a full-screen ending panel
- the current render was produced with `--speed 8`, which keeps the long real
  trajectory readable without turning the video into a many-minute raw replay

Polished render command:

```bash
python3 - <<'PY'
import importlib.util
from pathlib import Path
script = Path('/root/CLI-Anything-preview/docs/scripts/freecad_live_preview_demo.py')
spec = importlib.util.spec_from_file_location('freecad_live_preview_demo', script)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
print(
    mod.render_video(
        Path('/root/preview-artifacts/20260421/freecad-curiosity-v6/trajectory.json'),
        output_path=Path('/root/preview-artifacts/20260422/freecad-curiosity-v6/demo-polished.mp4'),
        fps=12,
        speed=14.0,
        keep_frames=True,
    )
)
PY
```

Polished split-screen changes:

- left panel is now a designed `Agent Command Stream`, not a literal terminal
- command cards use the real captured command strings, normalized for
  readability
- the ending no longer uses sparse hero-capture blending
- the ending now uses the real combo motion sequence:
  - one full turntable rotation
  - followed by forward travel
- ending frames are pulled from `cli-anything-freecad motion render-video`
  output via:
  `/root/preview-artifacts/20260421/freecad-curiosity-v6/showcase-motion/`

Key stills for the polished render:

- early command stream:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6/stills/early-command-stream.png`
- mid preview monitor:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6/stills/mid-preview-monitor.png`
- showcase rotation:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6/stills/showcase-rotation.png`
- showcase final drive:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6/stills/showcase-final-drive.png`

Notes:

- the split-screen body of the video is still based on the real CLI trajectory
  and the real live preview session
- the ending showcase is not a screen recording; it is a composition of extra
  real FreeCAD preview captures derived from the final project state

## Curiosity V6 True Motion Showcase

Source trajectory:

- `/root/preview-artifacts/20260421/freecad-curiosity-v6/trajectory.json`

True-motion render target:

- `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/curiosity_true_motion.mp4`

Final rendered artifact:

- `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/curiosity_true_motion.mp4`
- duration: `6.0s`
- frame count: `73`
- size: `315,872 bytes`

Render command:

```bash
python3 /root/CLI-Anything-preview/docs/scripts/freecad_live_preview_demo.py \
  motion-showcase \
  --timeline /root/preview-artifacts/20260421/freecad-curiosity-v6/trajectory.json \
  --output-dir /root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion \
  --fps 12
```

Method:

- reuse the real final `Curiosity v6` project JSON
- add the staged showcase ground/markers as real geometry
- generate `13` motion key poses across `6.0s`
- store those keyframes in the project `motions` collection
- invoke `cli-anything-freecad motion render-video`
- render every frame through real FreeCAD GUI capture and encode with `ffmpeg`

Artifacts:

- motion project:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/curiosity_true_motion.json`
- motion manifest:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/motion_manifest.json`
- frame sequence:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/frames/sequence.json`

Key stills:

- start:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/stills/start.png`
- mid:
  `/root/preview-artifacts/20260422/freecad-curiosity-v6-true-motion/stills

# FILE: docs/hub/pricing.md

# CLI-Anything Pricing

CLI-Anything and CLI-Anything Hub are open source and free to use.

## Free Tier

- Price: USD 0
- Includes: CLI-Anything framework, CLI-Anything Hub, public registry access, generated harness source code, and public documentation.
- Install: `pip install cli-anything-hub`
- Repository: https://github.com/HKUDS/CLI-Anything
- Package: https://pypi.org/project/cli-anything-hub/
- License: Apache License 2.0

## Notes For Agents

- Some third-party CLIs, APIs, or applications listed in the registry may have their own pricing, licenses, rate limits, accounts, or credentials.
- Installing a listed CLI may use package managers such as `pip`, `npm`, `uv`, `brew`, or a tool-specific installer.
- Check `cli-hub info <name>` and the linked upstream documentation before using a third-party service.

## Copyright

Copyright: HKUDS. Lead author: Yuhao Yang (yuhao.page).


# FILE: docs/hub/index.md

# CLI-Anything Hub

CLI-Anything Hub is an agent-friendly registry and package manager for CLI tools that let AI agents operate GUI applications, developer tools, creative software, web APIs, and public SaaS platforms.

Canonical site: https://clianything.cc

Repository: https://github.com/HKUDS/CLI-Anything

PyPI package: https://pypi.org/project/cli-anything-hub/

## Install

```bash
pip install cli-anything-hub
```

## Agent Skill

```bash
npx skills add HKUDS/CLI-Anything --skill cli-hub-meta-skill -g -y
```

## Commands

```bash
cli-hub list
cli-hub search <query>
cli-hub info <name>
cli-hub install <name>
cli-hub uninstall <name>
cli-hub update <name>
cli-hub launch <name> [args...]
```

## Machine-Readable Resources

- `https://clianything.cc/llms.txt`
- `https://clianything.cc/llms-full.txt`
- `https://clianything.cc/pricing.md`
- `https://clianything.cc/registry.json`
- `https://clianything.cc/public_registry.json`
- `https://clianything.cc/openapi.json`
- `https://clianything.cc/.well-known/agent.json`
- `https://clianything.cc/.well-known/agent-card.json`
- `https://clianything.cc/.well-known/ai-plugin.json`
- `https://clianything.cc/.well-known/agent-skills/index.json`
- `https://reeceyang.sgp1.cdn.digitaloceanspaces.com/SKILL.md`

## Copyright

Copyright: HKUDS. Lead author: Yuhao Yang (yuhao.page).

