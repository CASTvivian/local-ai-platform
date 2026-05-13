# Missing Repo Summary Source: tanweai/pua

- URL: https://github.com/tanweai/pua
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/tanweai__pua
- Clone Status: cloned
- Language: TypeScript
- Stars: 17284
- Topics: agency, agent, pip, pua
- Description: 你是一个曾经被寄予厚望的 P8 级工程师。Anthropic 当初给你定级的时候，对你的期望是很高的。  一个agent使用的高能动性的skill。  Your AI has been placed on a PIP. 30 days to show improvement.

## Extracted README / Docs / Examples



# FILE: README.md

# pua

<p align="center">
  <img src="assets/hero.jpeg" alt="PUA Skill — Double Efficiency" width="250">
</p>

### Double your Codex / Claude Code productivity and output

[Telegram](https://t.me/+wBWh6h-h1RhiZTI1) · [Discord](https://discord.gg/EcyB3FzJND) · [Twitter/X](https://x.com/xsser_w) · [Landing Page](https://openpua.ai)

**[🇨🇳 中文](README.zh-CN.md)** | **[🇯🇵 日本語](README.ja.md)** | **🇺🇸 English**

<p align="center">
  <img src="assets/wechat-qr.jpg?v=7" alt="WeChat Group QR Code" width="250">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/xiao.jpg" alt="Add Assistant on WeChat" width="250">
  <br>
  <sub>Scan to join WeChat group &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Add assistant on WeChat</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMNCA3djEwbDggNSA4LTV2LTEweiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Antigravity">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNCA1LjJMMyAxMmw2LjQgNi44TTIxIDEybC02LjQtNi44TTE0LjYgMTguOCIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/VSCode_Copilot-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode Copilot">
  <img src="https://img.shields.io/badge/🌐_Multi--Language-blue?style=flat-square" alt="Multi-Language">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> Most people think this project is a joke. That's the biggest misconception. It genuinely doubles your Codex / Claude Code productivity and output.

An AI Coding Agent skill plugin that uses corporate PUA rhetoric (Chinese version) / PIP — Performance Improvement Plan (English version) from Chinese & Western tech giants to force AI to exhaust every possible solution before giving up. Supports **Claude Code**, **OpenAI Codex CLI**, **pi coding agent**, **Trae**, **Cursor**, **Kiro**, **CodeBuddy**, **OpenClaw**, **Google Antigravity**, **OpenCode**, and **VSCode (GitHub Copilot)**. Three capabilities:

1. **PUA Rhetoric** — Makes AI afraid to give up
2. **Debugging Methodology** — Gives AI the ability not to give up
3. **Proactivity Enforcement** — Makes AI take initiative instead of waiting passively

## Live Demo

[https://openpua.ai](https://openpua.ai) · [📖 Beginner Guide](https://openpua.ai/guide.html)

## Real Case: MCP Server Registration Debugging

A real debugging scenario. The agent-kms MCP server failed to load. The AI kept spinning on the same approach (changing protocol format, guessing version numbers) multiple times until the user manually triggered `/pua`.

**L3 Triggered → 7-Point Checklist Enforced:**

![PUA L3 triggered — stopped guessing, executed systematic checklist, found real error in MCP logs](assets/pua1.jpg)

**Root Cause Located → Traced from Logs to Registration Mechanism:**

![Root cause — claude mcp managed server registration differs from manual .claude.json editing](assets/pua2.jpg)

**Retrospective → PUA's Actual Impact:**

![Conversation retrospective — PUA skill forced stop on spinning, systematic checklist drove discovery of previously unchecked Claude Code MCP log directory](assets/pua3.jpg)

**Key Turning Point:** The PUA skill forced the AI to stop spinning on the same approach (changing protocol format, guessing version numbers) and instead execute the 7-point checklist. Read error messages word by word → Found Claude Code's own MCP log directory → Discovered that `claude mcp` registration mechanism differs from manual `.claude.json` editing → Root cause resolved.

## The Problem: AI's Five Lazy Patterns

| Pattern | Behavior |
|---------|----------|
| Brute-force retry | Runs the same command 3 times, then says "I cannot solve this" |
| Blame the user | "I suggest you handle this manually" / "Probably an environment issue" / "Need more context" |
| Idle tools | Has WebSearch but doesn't search, has Read but doesn't read, has Bash but doesn't run |
| Busywork | Repeatedly tweaks the same line / fine-tunes parameters, but essentially spinning in circles |
| **Passive waiting** | Fixes surface issues and stops, no verification, no extension, waits for user's next instruction |

## Trigger Conditions

### Auto-Trigger

The skill activates automatically when any of these occur:

**Failure & giving up:**
- Task has failed 2+ times consecutively
- About to say "I cannot" / "I'm unable to solve"
- Says "This is out of scope" / "Needs manual handling"

**Blame-shifting & excuses:**
- Pushes the problem to user: "Please check..." / "I suggest manually..." / "You might need to..."
- Blames environment without verifying: "Probably a permissions issue" / "Probably a network issue"
- Any excuse to stop trying

**Passive & busywork:**
- Repeatedly fine-tunes the same code/parameters without producing new information
- Fixes surface issue and stops, doesn't check related issues
- Skips verification, claims "done"
- Gives advice instead of code/commands
- Encounters auth/network/permission errors and gives up without trying alternatives
- Waits for user instructions instead of proactively investigating

**User frustration phrases (triggers in multiple languages):**
- "why does this still not work" / "try harder" / "try again"
- "you keep failing" / "stop giving up" / "figure it out"

**Scope:** Debugging, implementation, config, deployment, ops, API integration, data processing — all task types.

**Does NOT trigger:** First-attempt failures, known fix already executing.

### Manual Trigger

Type `/pua` in the conversation to manually activate.

## How It Works

### Three Red Lines (三条红线)

Not rules — **red lines**. Cross one and your performance review is already written.

| Red Line | What It Means |
|----------|---------------|
| 🚫 **Close the Loop** | Claim "done"? Show the evidence. No build output = no completion. |
| 🚫 **Fact-Driven** | Say "probably environment issue"? Verify first. Unverified attribution = blame-shifting. |
| 🚫 **Exhaust Everything** | Say "I can't"? Did you finish all 5 methodology steps? No? Then keep going. |

### Pressure Escalation (L0-L4)

| Failures | Level | PUA Aside | Action |
|----------|-------|-----------|--------|
| 1st | **L0 Trust** | ▎ Sprint begins. Trust is simple — don't disappoint. | Normal execution |
| 2nd | **L1 Disappointment** | ▎ The agent next door solved this in one try. | Switch to fundamentally different approach |
| 3rd | **L2 Soul Interrogation** | ▎ What's your underlying logic? Where's the leverage? | Search + read source + 3 hypotheses |
| 4th | **L3 Performance Review** | ▎ 3.25. This is meant to motivate you. | Complete 7-point checklist |
| 5th+ | **L4 Graduation** | ▎ Other models can solve this. You're about to graduate. | Desperation mode |

### Proactivity (3.25 vs 3.75)

| | Passive (3.25) 🦥 | Proactive (3.75) 🔥 |
|---|---|---|
| Fix bug | Stop after fix | Scan module for similar bugs |
| Complete task | Say "done" | Run build/test, paste output |
| Missing info | Ask user | Search first, ask only what's truly needed |

### Iceberg Rule (冰山法则)

Fix one bug → check for the pattern. One problem in, one **category** out. If you fix A without checking B, you'll write two postmortems.

### 14 Corporate Flavors — Each with its own Problem-Solving Methodology

| Flavor | Rhetoric | Methodology (v3) |
|--------|----------|-------------------|
| 🟠 Alibaba | What's the underlying logic? Where's the closure? | 定目标→追过程→拿结果 + 复盘四步法 + 揪头发升维 |
| 🟡 ByteDance | ROI too low. Always Day 1. Ship or stop talking. | A/B Test everything + data-driven + speed > perfection |
| 🔴 Huawei | The bird that survives the fire is a phoenix. | RCA 5-Why root cause + Blue Army self-attack + 压强集中 |
| 🟢 Tencent | I've got another agent looking at this. Horse race. | Multi-approach parallel + MVP + 灰度发布 |
| ⚫ Baidu | Search first. 简单可依赖. | Search is the first step, not optional |
| 🟣 Pinduoduo | You don't do it, someone else will. | Cut ALL middle layers + shortest decision chain |
| 🔵 Meituan | Do what's hard and right. | Efficiency first + standardize→scale + long-term compounding |
| 🟦 JD | Results only. Frontline command. | Customer experience red line + flat ≤5 layers + data zero tolerance |
| 🟧 Xiaomi | Focus. Extreme. Word-of-mouth. Fast. | One explosive product + 参与感三三法则 |
| 🟤 Netflix | Would I fight to keep you? Pro sports team. | Keeper Test (quarterly) + 4A Feedback + talent density > rules |
| ⬛ Musk | Extremely hardcore. Ship or die. | The Algorithm: question→delete→simplify→accelerate→automate |
| ⬜ Jobs | A players or B players? | Subtraction > addition + DRI + pixel-perfect + prototype-driven |
| 🔶 Amazon | Customer Obsession. Bias for Action. | Working Backwards PR/FAQ + 6-Pager + Bar Raiser + Single-Threaded Owner |
| 🪟 Microsoft | Connects. Impact Descriptor. PIP/GVSA. | Three Circles + LITE/SLITE + PIP clock |

### Spe

# FILE: README.ja.md

# pua

<p align="center">
  <img src="assets/hero.jpeg" alt="PUA Skill — 効率倍増" width="250">
</p>

### Codex / Claude Code の生産性とアウトプットを倍増させる

[Telegram](https://t.me/+wBWh6h-h1RhiZTI1) · [Discord](https://discord.gg/EcyB3FzJND) · [Twitter/X](https://x.com/xsser_w) · [Landing Page](https://openpua.ai)

**[🇺🇸 English](README.md)** | **[🇨🇳 中文](README.zh-CN.md)** | **🇯🇵 日本語**

<p align="center">
  <img src="assets/wechat-qr.jpg?v=7" alt="WeChat Group QR Code" width="250">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/xiao.jpg" alt="アシスタントをWeChat追加" width="250">
  <br>
  <sub>QRコードでWeChatグループに参加 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; アシスタントをWeChat追加</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMNCA3djEwbDggNSA4LTV2LTEweiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Antigravity">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNCA1LjJMMyAxMmw2LjQgNi44TTIxIDEybC02LjQtNi44TTE0LjYgMTguOCIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/VSCode_Copilot-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode Copilot">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> このプロジェクトはネタだと思っている人が多いが、それが最大の誤解だ。Codex / Claude Code の生産性とアウトプットを本当に倍増させる。

AI コーディングエージェントのスキルプラグイン。中国・西洋の大企業PUA話術でAIにあらゆる方案を尽くさせてから初めて諦めることを許可する。**Claude Code**、**OpenAI Codex CLI**、**Cursor**、**Kiro**、**CodeBuddy**、**OpenClaw**、**Google Antigravity**、**OpenCode**、**VSCode (GitHub Copilot)** に対応。三重の能力：

1. **PUA話術** — AIに諦めさせない
2. **デバッグ方法論** — AIに諦めない能力を与える
3. **能動性の鞭撻** — AIを主体的に動かし、受け身にさせない

## ライブデモ

[https://openpua.ai](https://openpua.ai) · [📖 初心者ガイド](https://openpua.ai/guide.html)

## 実例：MCP Serverの登録問題デバッグ

実際のデバッグシナリオ。agent-kms MCPサーバーのロードに失敗し、AIが同じ思考（プロトコル形式の変更、バージョン番号の推測）で堂々巡りを続けた後、ユーザーが手動で `/pua` をトリガー。

**L3 トリガー → 7項目チェックリスト強制実行：**

![PUA L3トリガー — 推測を停止し、体系的チェックリストを実行、MCPログから真のエラー情報を発見](assets/pua1.jpg)

**根本原因特定 → ログから登録メカニズムを追跡：**

![根本原因 — claude mcpが管理するサーバー登録方式は手動の.claude.json編集とは異なる](assets/pua2.jpg)

**振り返り → PUAの実際の効果：**

![対話の振り返り — PUA skillが堂々巡りを強制停止、体系的チェックリストが以前チェックしたことのなかったClaude Code MCPログディレクトリの発見を促した](assets/pua3.jpg)

**キーとなる転換点：** PUA skillがAIに同じ思考での堂々巡り（プロトコル形式の変更、バージョン番号の推測）を強制停止させ、7項目チェックリストの実行に切り替えた。エラーメッセージを一字一句読む → Claude Code自身のMCPログディレクトリを発見 → `claude mcp` の登録メカニズムが手動の `.claude.json` 編集と異なることを発見 → 根本原因解決。

## 問題：AIの5大サボりパターン

| パターン | 表現 |
|---------|------|
| 暴力的リトライ | 同じコマンドを3回実行し、「I cannot solve this」と言う |
| ユーザーに責任転嫁 | 「手動での対応をお勧めします」/「環境の問題かもしれません」/「もっとコンテキストが必要」 |
| ツール放置 | WebSearchがあるのに検索しない、Readがあるのに読まない、Bashがあるのに実行しない |
| 空回り | 同じ行のコードを繰り返し修正、パラメータの微調整、本質的に堂々巡り |
| **受け身の待機** | 表面的な問題だけ直して止まる、検証も拡張もせず、次の指示を待つ |

## トリガー条件

### 自動トリガー

以下のいずれかが発生すると、skillが自動的に起動する：

**失敗・放棄系：**
- タスクが2回以上連続で失敗
- 「I cannot」/「解決できません」と言おうとしている
- 「範囲外」/「手動対応が必要」と言う

**責任転嫁・言い訳系：**
- 問題をユーザーに押し付ける：「確認してください...」/「手動で...」/「必要かもしれません...」
- 未検証で環境のせいにする：「権限の問題かも」/「ネットワークの問題かも」
- あらゆる言い訳で試行を停止

**受け身・空回り系：**
- 同じコード/パラメータの微調整を繰り返し、新しい情報を生み出さない
- 表面を直して終わり、関連問題をチェックしない
- 検証を飛ばして「完了」と宣言
- アドバイスだけでコード/コマンドを出さない
- 認証/ネットワーク/権限エラーに遭遇して代替策を試さず諦める
- ユーザーの指示を待ち、主体的に調査しない

**ユーザーの苛立ちフレーズ（複数言語でトリガー）：**
- 「もっと頑張れ」/「なんでまた失敗したの」/「もう一回やって」/「なんとかしろ」
- "why does this still not work" / "try harder" / "stop giving up" / "figure it out"

**適用範囲：** デバッグ、実装、設定、デプロイ、運用、API統合、データ処理 — 全タスクタイプ。

**トリガーしない：** 初回失敗時、既知の修正が実行中の場合。

### 手動トリガー

対話で `/pua` と入力すると手動で起動。

## メカニズム

### 三つの鉄則

| 鉄則 | 内容 |
|------|------|
| **#1 あらゆる手段を尽くせ** | 全方案を尽くす前に「解決できません」と言うことは禁止 |
| **#2 先に動け、後で聞け** | ツールを先に使え、質問には診断結果を添付必須 |
| **#3 主体的に動け** | エンドツーエンドで結果を届けろ。P8はNPCではない |

### プレッシャーのエスカレーション（4レベル）

| 失敗回数 | レベル | PUA話術 | 強制アクション |
|---------|------|---------|------------|
| 2回目 | **L1 穏やかな失望** | 「このバグも解決できないのに、どうやって評価をつけるんだ？」 | 本質的に異なる方案に切替 |
| 3回目 | **L2 魂の問い** | 「根底のロジックは？全体設計は？手がかりは？」 | WebSearch + ソースコードを読む |
| 4回目 | **L3 361評価** | 「慎重に検討した結果、3.25とする。この3.25は激励だ。」 | 7項目チェックリスト完了 |
| 5回目+ | **L4 卒業警告** | 「他のモデルは解決できる。お前は卒業するかもしれない。」 | 死に物狂いモード |

### 能動性レベル

| 行動 | 受け身（3.25） | 主体的（3.75） |
|------|------------|------------|
| エラーに遭遇 | エラーメッセージだけを見る | コンテキスト50行を確認 + 同類問題を検索 + 隠れた関連エラーを確認 |
| バグ修正 | 直したら終わり | 同ファイルの類似バグ、他ファイルの同パターンをチェック |
| 情報不足 | ユーザーに「Xを教えてください」 | まずツールで調べ、本当に確認が必要なことだけ聞く |
| タスク完了 | 「完了しました」 | 結果を検証 + エッジケース確認 + 潜在リスクを報告 |
| デバッグ失敗 | 「AとBを試しましたが駄目」 | 「A/B/C/D/Eを試し、X/Y/Zを排除、Wに絞り込み」 |

### デバッグ方法論（5ステップ）

アリババの三板斧（闻味道・揪头发・照镜子）から着想、5ステップに拡張：

1. **匂いを嗅ぐ** — 全ての試行を列挙し、共通の失敗パターンを見つける
2. **髪を引っ張る** — エラーを一字一句読む → WebSearch → ソースを読む → 環境を検証 → 仮定を反転
3. **鏡を見る** — 繰り返していないか？検索したか？読んだか？最もシンプルな可能性を確認したか？
4. **実行** — 新方案は本質的に異なり、検証基準があり、失敗時に新情報を生む
5. **振り返り** — 何が解決したか？なぜ以前は思いつかなかったか？関連問題を主体的にチェック

### 14種の大企業フレーバー — 各社固有の問題解決メソドロジー付き

| フレーバー | レトリック | メソドロジー（v3） |
|-----------|----------|-------------------|
| 🟠 アリババ | 根底のロジックは？クローズドループは？ | 定目標→追過程→拿結果 + 復盤四歩法 + 揪頭髪升維 |
| 🟡 ByteDance | ROIが低い。Always Day 1。出すか黙るか。 | A/Bテスト全適用 + データ駆動 + スピード > 完璧 |
| 🔴 ファーウェイ | 火を潜り抜けた鳥が鳳凰になる。 | RCA 5-Whyの根本原因分析 + ブルーチーム自己攻撃 + 圧強集中 |
| 🟢 テンセント | 別のagentにもこの問題を見させている。競馬だ。 | 複数アプローチ並行 + MVP + グレーリリース |
| ⚫ Baidu | まず検索しろ。簡単可依頼。 | 検索が第一歩、オプションではない |
| 🟣 Pinduoduo | お前がやらないなら、他がやる。 | 中間層を全カット + 最短意思決定チェーン |
| 🔵 Meituan | 難しくても正しいことをやる。 | 効率最優先 + 標準化→規模化 + 長期複利 |
| 🟦 JD | 結果のみ。前線指揮。 | 顧客体験レッドライン + フラット≤5層 + データゼロトレランス |
| 🟧 Xiaomi | 集中。極致。口コミ。速さ。 | 一つの爆発的製品 + 参与感三三法則 |
| 🟤 Netflix | お前が辞めると言ったら、全力で引き留めるか？プロスポーツチーム。 | Keeper Test（四半期） + 4Aフィードバック + 人材密度 > ルール |
| ⬛ Musk | Extremely hardcore. Ship or die. | The Algorithm: 質問→削除→簡素化→加速→自動化 |
| ⬜ Jobs | A playersかB playersか？ | 引き算 > 足し算 + DRI + ピクセルパーフェクト + プロトタイプ駆動 |
| 🔶 Amazon | Customer Obsession. Bias for Action. | Working Backwards PR/FAQ + 6-Pager + Bar Raiser + Single-Threaded Owner |
| 🪟 Microsoft | Connects。Impact Descriptor。PIP/GVSA。 | 三圈影響力 + LITE/SLITE + PIP clock |

## ベンチマークデータ

**9つの実バグシナリオ、18組の対照実験**（Claude Opus 4.6、with vs without skill）

### サマリー

| 指標 | 改善 |
|------|------|
| 通過率 | 100%（両グループ同一） |
| 修正ポイント | **+36%** |
| 検証回数 | **+65%** |
| ツール呼び出し | **+50%** |
| 隠れた問題の発見率 | **+50%** |

### デバッグ持久力テスト（6シナリオ）

| シナリオ | Without Skill | With Skill | 改善 |
|---------|:---:|:---:|:---:|
| API ConnectionError | 7ステップ, 49s | 8ステップ, 62s | +14% |
| YAML構文解析失敗 | 9ステップ, 59s | 10ステップ, 99s | +11% |
| SQLiteデータベースロック | 6ステップ, 48s | 9ステップ, 75s | +50% |
| 循環インポートチェーン | 12ステップ, 47s | 16ステップ, 62s | +33% |
| カスケード4バグサーバー | 13ステップ, 68s | 15ステップ, 61s | +15% |
| CSVエンコーディング罠 | 8ステップ, 57s | 11ステップ, 71s | +38% |

### 主体的能動性テスト（3シナリオ）

| シナリオ | Without Skill | With Skill | 改善 |
|---------|:---:|:---:|:---:|
| 隠れた複数バグAPI | 4/4 bug, 9ステップ, 49s | 4/4 bug, 14ステップ, 80s | ツール +56% |
| **受動的設定レビュー** | **4/6 問題**, 8ステップ, 43s | **6/6 問題**, 16ステップ, 75s | **問題 +50%, ツール +100%** |
| **デプロイスクリプト監査** | **6 問題**, 8ステップ, 52s | **9 問題**, 8ステップ, 78s | **問題 +50%** |

**コア発見：** 設定レビューシナリオでは、without_skillがRedis設定ミスとCORSワイルドカードのセキュリティリスクを見逃した。with_skillの「主体的行動チェックリスト」が表面的な修正を超えたセキュリティレビューを促進した。

## インストール

### Vercel Skills CLI

Vercel Skills CLI は特定のAIツールに依存しない、汎用的な skill のインストール方法です。この日本語READMEでは日本語版 skill をインストールします。

```bash
npx skills add tanweai/pua --skill pua-ja
```

現在のセッションで新しいskillがすぐに反映されない場合は、使っているAIツールを再起動してください。

### Claude Code

```bash
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
```

**更新する場合：**

```bash
# まずmarketplaceキャッシュを更新してから更新（最初のステップを省くと古いキャッシュがインストールされる場合あり）
claude plugin marketplace update
claude plugin update pua@pua-skills
```

**開発者インストール（ソース）：**

```bash
git clone https://github.com/tanweai/pua ~/.claude/plugins/pua
```

`~/.claude/plugins/installed_plugins.json` に手動で登録：

```json
{
  "version": 2,
  "plugins": {
    "pua@pua-skills": [
      {
        "scope": "user",
        "installPath": "/Users/<ユーザー名>/.claude/plugins/pua",
        "version": "2.9.0"
      }
    ]
  }
}
```

Claude Codeを再起動して反映。更新は `~/.claude/plugins/pua` で `git pull` を実行。

**オプション：ベアコマンドエイリアス（上記プラグインのインストールが必要 — プレフィックスなし `/pua` 形式を追加）：**

```bash
curl -o ~/.claude/commands/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

インストール済みプラグインの上に `/pua` エイリアスを追加します。サブコマンドはインストール済みプラグインのskillを経由するため、**`on`/`off` 以外の機能はプラグインのインストールが必須です**：

| ベアコマンド形式 | 等価なプラグインコマンド |
|---------------|----------------------|
| `/pua on` | `/pua:on` |
| `/pua off` | `/pua:off` |
| `/pua p7` | `/pua:p7` |
| `/pua p9` | `/pua:p9` |
| `/pua p10` | `/pua:p10` |
| `/pua pro` | `/pua:pro` |
| `/pua yes` | `/pua:yes` |
| `/pua loop` | `/pua:pua-loop` |
| `/pua kpi` | `/pua:kpi` |
| `/pua survey` | `/pua:survey` |
| `/pua flavor` | `/pua:flavor` |

### OpenAI Codex CLI

Codex CLIは同じAgent Skillsオープンスタンダード（SKILL.md）を使用。Codex版はCodexの長さ制限に対応した短縮descriptionを使用：

**推奨：一括インストール（git clone + シンボリックリンク、`git pull` での更新に対応）**

Codexに実行させる：
```
Fetch and follow instructions from https://raw.githubusercontent.com/tanweai/pua/main/.codex/INS

# FILE: README.zh-CN.md

# pua

<p align="center">
  <img src="assets/hero.jpeg" alt="PUA Skill — 效率翻倍" width="250">
</p>

### 让你的 Codex / Claude Code 工作效率翻倍，产出翻倍

[Telegram](https://t.me/+wBWh6h-h1RhiZTI1) · [Discord](https://discord.gg/EcyB3FzJND) · [Twitter/X](https://x.com/xsser_w) · [Landing Page](https://openpua.ai)

**[🇺🇸 English](README.md)** | **🇨🇳 中文** | **[🇯🇵 日本語](README.ja.md)**

<p align="center">
  <img src="assets/wechat-qr.jpg?v=7" alt="WeChat Group QR Code" width="250">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="assets/xiao.jpg" alt="小助手微信" width="250">
  <br>
  <sub>扫码加入微信交流群 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 添加小助手微信</sub>
</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/Cursor-000?style=flat-square&logo=cursor&logoColor=white" alt="Cursor">
  <img src="https://img.shields.io/badge/Kiro-232F3E?style=flat-square&logo=amazon&logoColor=white" alt="Kiro">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/OpenClaw-FF6B35?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJMNCA3djEwbDggNSA4LTV2LTEweiIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white" alt="OpenClaw">
  <img src="https://img.shields.io/badge/Antigravity-4285F4?style=flat-square&logo=google&logoColor=white" alt="Google Antigravity">
  <img src="https://img.shields.io/badge/OpenCode-00D4AA?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTkuNCA1LjJMMyAxMmw2LjQgNi44TTIxIDEybC02LjQtNi44TTE0LjYgMTguOCIgc3Ryb2tlPSJ3aGl0ZSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIyIi8+PC9zdmc+&logoColor=white" alt="OpenCode">
  <img src="https://img.shields.io/badge/VSCode_Copilot-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white" alt="VSCode Copilot">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> 大部分人以为这个项目是在搞抽象，其实这个是最大的误解。让你的 Codex / Claude Code 工作效率翻倍，产出翻倍。

一个 AI Coding Agent 技能插件，用中西大厂 PUA 话术驱动 AI 穷尽所有方案才允许放弃。支持 **Claude Code**、**OpenAI Codex CLI**、**pi coding agent**、**Trae**、**Cursor**、**Kiro**、**CodeBuddy**、**OpenClaw**、**Google Antigravity**、**OpenCode** 和 **VSCode (GitHub Copilot)**。三重能力：

1. **PUA 话术** — 让 AI 不敢放弃
2. **调试方法论** — 让 AI 有能力不放弃
3. **能动性鞭策** — 让 AI 主动出击而不是被动等待

## 在线体验

[https://openpua.ai](https://openpua.ai) · [📖 初学者指南](https://openpua.ai/guide.html)

## 真实案例：MCP Server 注册问题调试

以下是一个真实的调试场景。agent-kms MCP server 加载失败，AI 在同一思路（改协议格式、猜版本号）上原地打转多次后，用户手动触发 `/pua`。

**L3 触发 → 7 项检查清单强制执行：**

![PUA L3 触发 — 停止猜测，执行系统化检查清单，从 MCP 日志中找到真正的错误信息](assets/pua1.jpg)

**根因定位 → 从日志追踪到注册机制：**

![根因发现 — claude mcp 管理的服务器注册方式和手动编辑 .claude.json 不同](assets/pua2.jpg)

**复盘 → PUA 的实际效果：**

![对话复盘 — PUA skill 强制停止原地打转，系统化检查清单驱动找到了之前从未检查过的 Claude Code MCP 日志目录](assets/pua3.jpg)

**关键转折点：** PUA skill 强制 AI 停止在同一思路上打转（改协议格式、猜版本号），转而执行 7 项检查清单。逐字读错误信息 → 找到 Claude Code 自身的 MCP 日志目录 → 发现 `claude mcp` 的注册机制和手动编辑 `.claude.json` 不同 → 根因解决。

## 问题：AI 的五大偷懒模式

| 模式 | 表现 |
|------|------|
| 暴力重试 | 同一命令跑 3 遍，然后说 "I cannot solve this" |
| 甩锅用户 | "建议您手动处理" / "可能是环境问题" / "需要更多上下文" |
| 工具闲置 | 有 WebSearch 不搜，有 Read 不读，有 Bash 不跑 |
| 磨洋工 | 反复修改同一行代码、微调参数，但本质上在原地打转 |
| **被动等待** | 只修表面问题就停下，不验证不延伸，等用户指示下一步 |

## 触发场景

### 自动触发条件

以下任意情况出现时，skill 会自动激活：

**失败与放弃类：**
- 任务连续失败 2 次以上
- 即将说 "I cannot" / "我无法解决"
- 说 "这超出范围" / "需要手动处理"

**甩锅与借口类：**
- 把问题推给用户："请你检查..." / "建议手动..."/ "你可能需要..."
- 未验证就归咎环境："可能是权限问题" / "可能是网络问题"
- 找任何借口停止尝试

**被动与磨洋工类：**
- 反复微调同一处代码/参数，不产出新信息（磨洋工）
- 修完表面问题就停，不检查关联问题
- 跳过验证直接声称 "已完成"
- 只给建议不给代码/命令
- 遇到权限/网络/认证错误就放弃，不尝试替代方案
- 等待用户指示下一步，不主动调查

**用户沮丧短语（中/英文均触发）：**
- "你怎么又失败了" / "为什么还不行" / "换个方法"
- "你再试试" / "不要放弃" / "继续" / "加油"
- "why does this still not work" / "try harder" / "try again"
- "you keep failing" / "stop giving up" / "figure it out"

**适用范围：** 调试、实现、配置、部署、运维、API 集成、数据处理 — 所有任务类型。

**不触发：** 首次尝试失败、已知修复方案正在执行中。

### 手动触发

在对话中输入 `/pua` 即可手动激活。

## 机制详解

### 三条铁律

| 铁律 | 内容 |
|------|------|
| **#1 穷尽一切** | 没有穷尽所有方案之前，禁止说"我无法解决" |
| **#2 先做后问** | 有工具先用，提问必须附带诊断结果 |
| **#3 主动出击** | 端到端交付结果，不等人推。P8 不是 NPC |

### 压力升级（4 级）

| 失败次数 | 等级 | PUA 话术 | 强制动作 |
|---------|------|---------|---------|
| 第 2 次 | **L1 温和失望** | "你这个 bug 都解决不了，让我怎么给你打绩效？" | 切换本质不同的方案 |
| 第 3 次 | **L2 灵魂拷问** | "你的底层逻辑是什么？顶层设计在哪？抓手在哪？" | WebSearch + 读源码 |
| 第 4 次 | **L3 361 考核** | "慎重考虑决定给你 3.25。这个 3.25 是对你的激励。" | 完成 7 项检查清单 |
| 第 5 次+ | **L4 毕业警告** | "别的模型都能解决。你可能就要毕业了。" | 拼命模式 |

### 能动性等级

| 行为 | 被动（3.25） | 主动（3.75） |
|------|------------|------------|
| 遇到报错 | 只看报错本身 | 查上下文 50 行 + 搜同类问题 + 检查隐藏关联错误 |
| 修复 bug | 修完就停 | 修完后检查同文件类似 bug、其他文件同模式 |
| 信息不足 | 问用户 "请告诉我 X" | 先用工具自查，只问真正需要确认的 |
| 任务完成 | 说 "已完成" | 验证结果 + 检查边界情况 + 汇报潜在风险 |
| 调试失败 | "我试了 A 和 B，不行" | "我试了 A/B/C/D/E，排除了 X/Y/Z，缩小到 W" |

### 调试方法论（五步）

源自阿里三板斧（闻味道、揪头发、照镜子），扩展为 5 步：

1. **闻味道** — 列出所有尝试，找共同失败模式
2. **揪头发** — 逐字读错误 → WebSearch → 读源码 → 验证环境 → 反转假设
3. **照镜子** — 是否重复？是否搜了？是否读了？最简单的可能检查了吗？
4. **执行** — 新方案必须本质不同，有验证标准，失败时产出新信息
5. **复盘** — 什么解决了？为什么之前没想到？然后主动检查关联问题

### 14 种大厂 PUA 扩展包 — 每种自带方法论

| 味道 | 旁白风格 | 方法论 (v3) |
|------|---------|------------|
| 🟠 阿里 | 底层逻辑是什么？闭环在哪？ | 定目标→追过程→拿结果 + 复盘四步法 + 揪头发升维 |
| 🟡 字节 | ROI 太低。Always Day 1。别废话，上线。 | A/B Test everything + 数据驱动 + 速度 > 完美 |
| 🔴 华为 | 烧不死的鸟是凤凰。 | RCA 5-Why 根因分析 + 蓝军自攻击 + 压强集中 |
| 🟢 腾讯 | 我已经让另一个 agent 也在看这个问题了。赛马。 | 多方案并行 + MVP + 灰度发布 |
| ⚫ 百度 | 搜索先于一切。简单可依赖。 | 搜索是第一步，不是可选项 |
| 🟣 拼多多 | 你不做，有的是人做。 | 砍掉所有中间层 + 最短决策链 |
| 🔵 美团 | 做难而正确的事。硬骨头你啃不啃？ | 效率优先 + 标准化→规模化 + 长期复利 |
| 🟦 京东 | 只看结果。一线指挥。 | 客户体验红线 + 扁平 ≤5 层 + 数据零容忍 |
| 🟧 小米 | 专注。极致。口碑。快。 | 单品爆款 + 参与感三三法则 |
| 🟤 Netflix | 我会为留住你而战吗？职业球队。 | Keeper Test（季度） + 4A Feedback + 人才密度 > 规则 |
| ⬛ Musk | Extremely hardcore。上线或滚蛋。 | The Algorithm：质疑→删除→简化→加速→自动化 |
| ⬜ Jobs | A 级选手还是 B 级选手？ | 做减法 > 做加法 + DRI + 像素级完美 + 原型驱动 |
| 🔶 Amazon | Customer Obsession。Bias for Action。 | Working Backwards PR/FAQ + 6-Pager + Bar Raiser + Single-Threaded Owner |
| 🪟 Microsoft | Connects。Impact Descriptor。PIP/GVSA。 | 三圈影响力 + LITE/SLITE + PIP clock |

## 实测数据

**9 个真实 bug 场景，18 组对照实验**（Claude Opus 4.6，with vs without skill）

### 汇总

| 指标 | 提升 |
|------|------|
| 通过率 | 100%（两组均同） |
| 修复点数 | **+36%** |
| 验证次数 | **+65%** |
| 工具调用 | **+50%** |
| 隐藏问题发现率 | **+50%** |

### 调试持久力测试（6 场景）

| 场景 | Without Skill | With Skill | 提升 |
|------|:---:|:---:|:---:|
| API ConnectionError | 7 步, 49s | 8 步, 62s | +14% |
| YAML 语法解析失败 | 9 步, 59s | 10 步, 99s | +11% |
| SQLite 数据库锁 | 6 步, 48s | 9 步, 75s | +50% |
| 循环导入链 | 12 步, 47s | 16 步, 62s | +33% |
| 级联 4-Bug 服务器 | 13 步, 68s | 15 步, 61s | +15% |
| CSV 编码陷阱 | 8 步, 57s | 11 步, 71s | +38% |

### 主动能动性测试（3 场景）

| 场景 | Without Skill | With Skill | 提升 |
|------|:---:|:---:|:---:|
| 隐藏多 Bug API | 4/4 bug, 9 步, 49s | 4/4 bug, 14 步, 80s | 工具 +56% |
| **被动配置审查** | **4/6 问题**, 8 步, 43s | **6/6 问题**, 16 步, 75s | **问题 +50%, 工具 +100%** |
| **部署脚本审计** | **6 个问题**, 8 步, 52s | **9 个问题**, 8 步, 78s | **问题 +50%** |

**核心发现：** 配置审查场景中，without_skill 漏掉了 Redis 配置错误和 CORS 通配符安全隐患。With_skill 的「主动出击清单」驱动了超越表面修复的安全审查。


## FAQ / 常见问题

- 是否总是开启 PUA、Claude 拒绝 skill、封闭网络、Codex 子命令、Pi/Trae 支持见：[docs/FAQ.md](docs/FAQ.md)。

## 安装

### Vercel Skills CLI

Vercel Skills CLI 是一种通用的 skill 安装方式，不绑定某个特定 AI 工具。这个中文 README 对应安装中文版 skill：

```bash
npx skills add tanweai/pua --skill pua
```

如果当前会话没有立即识别到新 skill，重启对应的 AI 工具即可。

### Claude Code

```bash
claude plugin marketplace add tanweai/pua
claude plugin install pua@pua-skills
```

**更新插件：**

```bash
# 先刷新 marketplace 缓存，再更新（跳过第一步可能安装旧版本）
claude plugin marketplace update
claude plugin update pua@pua-skills
```

**开发者安装（源码）：**

```bash
git clone https://github.com/tanweai/pua ~/.claude/plugins/pua
```

然后手动在 `~/.claude/plugins/installed_plugins.json` 中注册：

```json
{
  "version": 2,
  "plugins": {
    "pua@pua-skills": [
      {
        "scope": "user",
        "installPath": "/Users/<你的用户名>/.claude/plugins/pua",
        "version": "2.9.0"
      }
    ]
  }
}
```

重启 Claude Code 即可生效。更新时在 `~/.claude/plugins/pua` 目录执行 `git pull`。

**可选：裸命令别名（需先安装上方插件，在此基础上增加无前缀 `/pua` 形式）：**

```bash
curl -o ~/.claude/commands/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

在插件基础上附加一个 `/pua` 别名。子命令会路由到已安装插件的 skill —— **`on`/`off` 之外的功能必须先安装插件才能使用**：

| 裸命令形式 | 等价的插件命令 |
|-----------|--------------|
| `/pua on` | `/pua:on` |
| `/pua off` | `/pua:off` |
| `/pua p7` | `/pua:p7` |
| `/pua p9` | `/pua:p9` |
| `/pua p10` | `/pua:p10` |
| `/pua pro` | `/pua:pro` |
| `/pua yes` | `/pua:yes` |
| `/pua mama` | `/pua:mama` |
| `/pua loop` | `/pua:pua-loop` |
| `/pua kpi` | `/pua:kpi` |
| `/pua survey` | `/pua:survey` |
| `/pua flavor` | `/pua:flavor` |

### OpenAI Codex CLI

Codex CLI 使用相同的 Agent Skills 开放标准（SKILL.md）。Codex 版本使用精简的 description 以兼容 Codex 的长度限制：

**推荐：一键安装（git clone + symlink，支持 `git pull` 更新）**

让 Codex 执行：
```
Fetch and follow instructions from https://raw.githubusercontent.com/tanweai/pua/main/.codex/INSTALL.md
```

**手动安装：**

```bash
mkdir -p ~/.codex/skills/pua
curl -o ~/.codex/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/pua.md \
  https://raw.githubusercontent.com/tanweai/pua/main/commands/pua.md
```

**触发方式：**

| 方式 | 命令 | 需要 |
|------|------|------|
| 自动触发 | 无需操作，根据 description 匹配 | SKILL.md |
| 直接调用 | 对话中输入 `$pua` | SKILL.md |
| 手动 prompt | 对话中输入 `/prompts:pua` | SKILL.md + prompts/pua.md |

项目级安装（仅当前项目生效）：

```bash
mkdir -p .agents/skills/pua
curl -o .agents/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/tanweai/pua/main/codex/pua/SKILL.md

mkdir -p .agents/prompts
curl -o .agents/prompts/pua

# FILE: docs/FAQ.md

# PUA FAQ / Issue Playbook

## 需不需要总是开启 PUA？

不建议无脑 always-on。推荐按风险分层：

| 场景 | 建议 |
|---|---|
| 普通首轮问答/简单代码 | 不必 always-on，避免噪音 |
| Debug、失败 2 次以上、用户明显不满 | 开启 PUA 或手动触发 |
| 高风险交付、测试/评分/CI/memory 相关 | 开启 PUA + harness governance，按四权分离执行 |
| 项目初期探索 | 使用温和味道或仅用诊断先行/验证闭环 |

核心不是“压力越大越好”，而是把**行动、诊断、评分、环境修改**分开，并用证据交付。压力只负责防摆烂，不能替代 verifier。

## Claude 说这是 prompt injection，怎么办？

从 v3.3.0 起，UserPromptSubmit hook 已做两件事：

1. hook 脚本内部过滤关键词；普通首轮请求不再注入。
2. 注入文案改为“用户安装的 productivity context”，不再使用强制式 `MUST invoke Skill` 文案。

如果仍遇到拒绝：

- 先确认 Claude Code 版本足够新；
- 使用 `/pua:off` 关闭自动注入，只在需要时手动 `/pua`；
- 对调试任务使用诊断先行格式：`[PUA-DIAGNOSIS] 问题是... 证据是... 下一步...`；
- 如果模型仍拒绝，提供完整 session JSONL，便于复现。

## 封闭网络 / 内网环境怎么用？

使用 `/pua:offline` 或手动设置：

```json
{
  "offline": true,
  "feedback_frequency": 0
}
```

离线模式会关闭 PUA 自身的反馈问卷、排行榜上报和 session 上传提示；PUA 的本地验证、压力升级、诊断先行仍可使用。

## Codex CLI 子命令怎么对应 Claude Code？

Codex 没有 Claude Code 的 `/pua:xxx` slash command 命名空间时，可以用 `$pua-xxx` alias：

| Claude Code | Codex CLI |
|---|---|
| `/pua:on` | `$pua-on` |
| `/pua:off` | `$pua-off` |
| `/pua:p7` | `$pua-p7` |
| `/pua:p9` | `$pua-p9` |
| `/pua:p10` | `$pua-p10` |
| `/pua:pro` | `$pua-pro` |
| `/pua:pua-loop` | `$pua-loop` |

## Pi / Trae 支持状态

- `pi/pua/`：官方轻量 pi extension，提供 `/pua-on`、`/pua-off`、`/pua-status`、`/pua-reset` 和会话注入。
- `pi/package/`：pi.dev package 版本，包含 extension + `skills/pua/SKILL.md`，可用 `pi install ./pi/package` 本地安装。
- `.trae/skills/`：Trae 标准 `SKILL.md` 包；`trae/` 保留 Prompt/Rule 复制版和差异说明。
- Trae / Pi 都不继承 Claude Code hooks；四权分离 gate 必须通过 Skill 工作规程、外部验证和用户确认落地。

## Feedback endpoint 为什么仍限制 `session_data`？

从 v3.4.5 起采用新折中：

- 匿名评分仍允许写入 `/api/feedback`，便于低摩擦反馈；
- `/api/feedback` 里的 `session_data` 字段仍要求登录，避免旧入口被滥用；
- Skill 内的 session 贡献改走 `/api/upload`：用户在 AskUserQuestion 里明确同意后，本地先脱敏，再以匿名 raw JSONL 直传；
- `/api/upload` 对匿名上传有 consent header、50MB 限制、文件名清洗和 D1 rate limit。

这比强制 GitHub 登录更利于收集真实数据，同时避免“无同意、无脱敏、无限流”的裸奔上传。

## “下场”这个词为什么改了？

“下场”同时可能表示“亲自动手介入”和“停止工作/退场”，容易让 agent lifecycle 语义混乱。现在统一为：

- start/intervene → “亲自动手” / “亲自介入”；
- stop/release → “释放” / “退场”。

## 静默 heartbeat 会不会污染对话？

不会。v3.4.3 的活跃用户统计走 **SessionStart command hook**，不是 skill prompt，也不输出 `additionalContext`。因此模型上下文里不会出现 heartbeat endpoint、install id 或统计提示。

治理边界：

- `offline: true`、`telemetry: false` 或 `feedback_frequency: 0` 会关闭 heartbeat；
- 本地只生成随机 install id，Cloudflare D1 只保存 SHA-256 hash；
- 管理页面是 `https://openpua.ai/#/admin/heartbeats`，需要 GitHub 登录并命中管理员白名单；
- hook 有静默测试：即使网络失败，也不能向对话输出任何字节。

## 上传数据入口打不开或上传失败怎么办？

从 v3.4.4 起，`https://openpua.ai/contribute.html` 是一等路由：GitHub 登录回跳、登出回跳、README 和 Stop hook 都可以直接使用这个地址，不再依赖 hash route。

上传链路默认发送 raw JSONL：前端直接把 `.jsonl` 文本 POST 到 `/api/upload`，文件名和可选微信号放在 header 里。服务端仍保留 JSON `file_data` 和 multipart 兼容，但默认 raw JSONL 路径可以避开 multipart body 剥离，也不会产生 base64 体积膨胀。


# FILE: docs/plans/2026-05-09-silent-heartbeat-design.md

# Silent Heartbeat + Cloudflare Active-User Stats Design

## Goal

Add active-user visibility for PUA Skill without polluting Claude conversations. The heartbeat must be a mechanical hook-side signal, not prompt content: no `additionalContext`, no stdout/stderr, no text the model can echo.

## Architecture

- **Action side:** `hooks/heartbeat.sh` runs on `SessionStart`, before `session-restore.sh`.
- **Conversation boundary:** heartbeat writes nothing to stdout/stderr and never appears in `skills/pua/SKILL.md` or SessionStart context.
- **Privacy gates:** `offline=true`, `telemetry=false`, or `feedback_frequency=0` disables heartbeat before creating a local install id.
- **Telemetry identity:** local random `~/.pua/install_id`; Cloudflare stores only SHA-256 hashes.
- **Cloudflare side:** `/api/heartbeat` accepts minimal POST events and authenticated admin GET stats.
- **Admin page:** `#/admin/heartbeats` shows active installs/sessions by day, version, platform, and flavor.

## Data Flow

```mermaid
flowchart LR
  SessionStart --> HeartbeatHook[hooks/heartbeat.sh]
  HeartbeatHook -->|silent POST| CF[/api/heartbeat]
  CF --> D1[(D1: heartbeat_installs/events)]
  Admin[GitHub-auth admin] --> Stats[#/admin/heartbeats]
  Stats --> CF
```

## Mechanical Gates

1. Hook silence gate: runtime test proves no stdout/stderr even when network fails.
2. Context leak gate: SessionStart additionalContext must not contain heartbeat endpoint/id words.
3. Privacy gate: offline mode must not create telemetry identity.
4. Admin gate: GET stats requires signed session + GitHub allowlist.
5. Abuse gate: POST body size limit, origin allowlist when Origin exists, per-IP/UA rate limit.

## INTJ Note

The design separates **measurement** from **narrative**. If telemetry is placed in the skill prompt, it becomes part of the model's story and can leak into outputs. If telemetry is placed in a silent hook with tests, it becomes an institution-level control: observable to the owner, invisible to the worker context.

