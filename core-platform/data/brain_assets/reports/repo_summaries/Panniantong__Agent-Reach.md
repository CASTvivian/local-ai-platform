# Repo Summary Source: Panniantong/Agent-Reach
- URL: https://github.com/Panniantong/Agent-Reach
- Local Path: core-platform/data/brain_assets/repos/github_stars/Panniantong__Agent-Reach
- Buckets: agent, mcp, llm_runtime
- Stars: 19344
- Language: Python
- Description: Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.
- Clone Status: cloned
## Extracted README / Docs


# FILE: README.md

<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>给你的 AI Agent 一键装上互联网能力</strong>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#快速上手">快速开始</a> · <a href="docs/README_en.md">English</a> · <a href="docs/README_ja.md">日本語</a> · <a href="docs/README_ko.md">한국어</a> · <a href="#支持的平台">支持平台</a> · <a href="#设计理念">设计理念</a>
</p>

---

## 为什么需要 Agent Reach？

AI Agent 已经能帮你写代码、改文档、管项目——但你让它去网上找点东西，它就抓瞎了：

- 📺 "帮我看看这个 YouTube 教程讲了什么" → **看不了**，拿不到字幕
- 🐦 "帮我搜一下推特上大家怎么评价这个产品" → **搜不了**，Twitter API 要付费
- 📖 "去 Reddit 上看看有没有人遇到过同样的 bug" → **403 被封**，服务器 IP 被拒
- 📕 "帮我看看小红书上这个品的口碑" → **打不开**，必须登录才能看
- 📺 "B站上有个技术视频，帮我总结一下" → **连不上**，海外/服务器 IP 被屏蔽
- 🔍 "帮我在网上搜一下最新的 LLM 框架对比" → **没有好用的搜索**，要么付费要么质量差
- 🌐 "帮我看看这个网页写了啥" → **抓回来一堆 HTML 标签**，根本没法读
- 📦 "这个 GitHub 仓库是干嘛的？Issue 里说了什么？" → 能用，但认证配置很麻烦
- 📡 "帮我订阅这几个 RSS 源，有更新告诉我" → 要自己装库写代码

**这些不难实现，但是需要自己折腾配置**

每个平台都有自己的门槛——要付费的 API、要绕过的封锁、要登录的账号、要清洗的数据。你要一个一个去踩坑、装工具、调配置，光是让 Agent 能读个推特就得折腾半天。

**Agent Reach 把这件事变成一句话：**

```
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

复制给你的 Agent，几分钟后它就能读推特、搜 Reddit、看 YouTube、刷小红书了。

**已经装过了？更新也是一句话：**

```
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

> ⭐ **Star 这个项目**，我们会持续追踪各平台的变化、接入新的渠道。你不用自己盯——平台封了我们修，有新渠道我们加。

### ✅ 在你用之前，你可能想知道

| | |
|---|---|
| 💰 **完全免费** | 所有工具开源、所有 API 免费。唯一可能花钱的是服务器代理（$1/月），本地电脑不需要 |
| 🔒 **隐私安全** | Cookie 只存在你本地，不上传不外传。代码完全开源，随时可审查 |
| 🔄 **持续更新** | 底层工具（yt-dlp、twitter-cli、rdt-cli、Jina Reader 等）定期追踪更新到最新版，你不用自己盯 |
| 🤖 **兼容所有 Agent** | Claude Code、OpenClaw、Cursor、Windsurf……任何能跑命令行的 Agent 都能用 |
| 🩺 **自带诊断** | `agent-reach doctor` 一条命令告诉你哪个通、哪个不通、怎么修 |

---

## 支持的平台

| 平台 | 装好即用 | 配置后解锁 | 怎么配 |
|------|---------|-----------|-------|
| 🌐 **网页** | 阅读任意网页 | — | 无需配置 |
| 📺 **YouTube** | 字幕提取 + 视频搜索 | — | 无需配置 |
| 📡 **RSS** | 阅读任意 RSS/Atom 源 | — | 无需配置 |
| 🔍 **全网搜索** | — | 全网语义搜索 | 自动配置（MCP 接入，免费无需 Key） |
| 📦 **GitHub** | 读公开仓库 + 搜索 | 私有仓库、提 Issue/PR、Fork | 告诉 Agent「帮我登录 GitHub」 |
| 🐦 **Twitter/X** | 读单条推文 | 搜索推文、浏览时间线、发推 | 告诉 Agent「帮我配 Twitter」 |
| 📺 **B站** | 本地：字幕提取 + 搜索 | 服务器也能用 | 告诉 Agent「帮我配代理」 |
| 📖 **Reddit** | 搜索 + 读帖子和评论（通过 rdt-cli） | Cookie | 需要登录认证（`rdt login`），详见 [rdt-cli](https://github.com/public-clis/rdt-cli) |
| 📕 **小红书** | — | 阅读、搜索、发帖、评论、点赞 | 告诉 Agent「帮我配小红书」 |
| 🎵 **抖音** | — | 视频解析、无水印下载链接获取 | 告诉 Agent「帮我配抖音」 |
| 💼 **LinkedIn** | Jina Reader 读公开页面 | Profile 详情、公司页面、职位搜索 | 告诉 Agent「帮我配 LinkedIn」 |
| 💬 **微信公众号** | 搜索 + 阅读公众号文章（全文 Markdown） | — | 无需配置 |
| 📰 **微博** | 热搜、搜索内容/用户/话题、用户动态、评论 | — | 无需配置 |
| 💻 **V2EX** | 热门帖子、节点帖子、帖子详情+回复、用户信息 | — | 无需配置 |
| 📈 **雪球** | 股票行情、搜索股票、热门帖子、热门股票排行 | — | 告诉 Agent「帮我配雪球」 |
| 🎙️ **小宇宙播客** | — | 播客音频转文字（Whisper 转录，免费 Key） | 告诉 Agent「帮我配小宇宙播客」 |

> **不知道怎么配？不用查文档。** 直接告诉 Agent「帮我配 XXX」，它知道需要什么、会一步一步引导你。
>
> 🍪 需要 Cookie 的平台（Twitter、小红书等），**优先使用** Chrome 插件 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) 导出 Cookie，发给 Agent 即可配置。流程统一：浏览器登录 → Cookie-Editor 导出 → 发给 Agent。比扫码更简单可靠。
>
> 🔒 Cookie 只存在你本地，不上传不外传。代码完全开源，随时可审查。
> 💻 本地电脑不需要代理。代理只有部署在服务器上才需要（~$1/月）。

---

## 快速上手

> ⚠️ **OpenClaw 用户请先确认 exec 权限已开启**
>
> Agent Reach 依赖 Agent 执行 shell 命令（`pip install`、`mcporter`、`twitter` 等）。如果你的 OpenClaw 使用了默认的 `messaging` 工具配置，Agent 将无法执行命令。**安装前请先开启 exec 权限**：
>
> ```bash
> openclaw config set tools.profile "coding"
> ```
> 或在 `~/.openclaw/openclaw.json` 中设置 `"tools": { "profile": "coding" }`。
> 设置后重启 Gateway（`openclaw gateway restart`）并开启新对话即可。其他平台（Claude Code、Cursor、Windsurf 等）不受此限制。

复制这句话给你的 AI Agent（Claude Code、OpenClaw、Cursor 等）：

```
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

就这一步。Agent 会自己完成剩下的所有事情。

> 🔄 **已安装过？** 更新也是一句话：
> ```
> 帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

> 🛡️ **担心安全？** 可以用安全模式——不会自动装系统包，只告诉你需要什么：
> ```
> 帮我安装 Agent Reach（安全模式）：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> 安装时使用 --safe 参数
> ```

<details>
<summary>它会做什么？（点击展开）</summary>

1. **安装 CLI 工具** — `pip install` 装好 `agent-reach` 命令行
2. **安装系统依赖** — 自动检测并安装 Node.js、gh CLI、mcporter、twitter-cli、rdt-cli 等
3. **配置搜索引擎** — 通过 MCP 接入 Exa（免费，无需 API Key）
4. **检测环境** — 判断是本地电脑还是服务器，给出对应的配置建议
5. **注册 SKILL.md** — 在 Agent 的 skills 目录安装使用指南，以后 Agent 遇到"搜推特"、"看视频"这类需求，会自动知道该调哪个上游工具

安装完之后，`agent-reach doctor` 一条命令告诉你每个渠道的状态。
</details>

---

## 装好就能用

不需要任何配置，告诉 Agent 就行：

- "帮我看看这个链接" → `curl https://r.jina.ai/URL` 读任意网页
- "这个 GitHub 仓库是做什么的" → `gh repo view owner/repo`
- "这个视频讲了什么" → `yt-dlp --dump-json URL` 提取字幕
- "帮我看看这条推文" → `twitter tweet URL`
- "订阅这个 RSS" → `feedparser` 解析
- "搜一下 GitHub 上有什么 LLM 框架" → `gh search repos "LLM framework"`

**不需要记命令。** Agent 读了 SKILL.md 之后自己知道该调什么。

---

## 设计理念

**Agent Reach 是一个脚手架（scaffolding），不是框架。**

你给一个新 Agent 装环境的时候，总要花时间去找工具、装依赖、调配置——Twitter 用什么读？Reddit 怎么绕封？YouTube 字幕怎么提取？每次都要重新踩一遍。

Agent Reach 做的事情很简单：**帮你把这些选型和配置的活儿做完了。**

安装完成后，Agent 直接调用上游工具（twitter-cli、rdt-cli、xhs-cli、yt-dlp、mcporter、gh CLI 等），不需要经过 Agent Reach 的包装层。

### 🔌 每个渠道都是可插拔的

每个平台背后是一个独立的上游工具。**不满意？换掉就行。**

```
channels/
├── web.py          → Jina Reader     ← 可以换成 Firecrawl、Crawl4AI……
├── twitter.py      → twitter-cli       ← 可以换成官方 API……
├── youtube.py      → yt-dlp          ← 可以换成 YouTube API、Whisper……
├── github.py       → gh CLI          ← 可以换成 REST API、PyGithub……
├── bilibili.py     → yt-dlp          ← 可以换成 bilibili-api……
├── reddit.py       → rdt-cli         ← 搜索+阅读，需 Cookie 认证



# FILE: docs/README_ja.md

<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AIエージェントにワンクリックでインターネット全体へのアクセスを</strong>
</p>

<p align="center">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#クイックスタート">クイックスタート</a> · <a href="../README.md">中文</a> · <a href="README_en.md">English</a> · <a href="README_ko.md">한국어</a> · <a href="#対応プラットフォーム">プラットフォーム</a> · <a href="#設計思想">設計思想</a>
</p>

---

## なぜ Agent Reach？

AIエージェントはすでにインターネットにアクセスできます。しかし「ネットに繋がる」はほんの始まりに過ぎません。

最も価値のある情報は、さまざまなSNSやニッチなプラットフォームに散らばっています：Twitterの議論、Redditのフィードバック、YouTubeのチュートリアル、小紅書のレビュー、Bilibiliの動画、GitHubのアクティビティ… **これらこそ情報密度が最も高い場所です**。しかし、各プラットフォームにはそれぞれ障壁があります：

| 課題 | 現実 |
|------|------|
| Twitter API | 従量課金、中程度の利用で月額約$215 |
| Reddit | サーバーIPが403でブロックされる |
| 小紅書 | 閲覧にログインが必要 |
| Bilibili | 海外/サーバーIPをブロック |

エージェントをこれらのプラットフォームに接続するには、ツールを探し、依存関係をインストールし、設定をデバッグする必要があります — ひとつずつ。

**Agent Reach はこれを1つのコマンドにまとめます：**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

これをエージェントにコピーするだけ。数分後には、ツイートの閲覧、Redditの検索、Bilibiliの視聴が可能になります。

**すでにインストール済み？1コマンドでアップデート：**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ 始める前に知っておきたいこと

| | |
|---|---|
| 💰 **完全無料** | すべてのツールはオープンソース、すべてのAPIは無料。唯一のコストはサーバープロキシ（月額$1）の可能性のみ — ローカルPCでは不要 |
| 🔒 **プライバシー安全** | Cookieはローカルに保存。アップロードされることはありません。完全オープンソース — いつでも監査可能 |
| 🔄 **常に最新** | 上流ツール（yt-dlp、twitter-cli、rdt-cli、Jina Reader等）を定期的に追跡・更新 |
| 🤖 **あらゆるエージェントに対応** | Claude Code、OpenClaw、Cursor、Windsurf… コマンドを実行できるすべてのエージェント |
| 🩺 **組み込み診断** | `agent-reach doctor` — 1コマンドで何が動き、何が動かないか、どう修正するかを表示 |

---

## 対応プラットフォーム

| プラットフォーム | 機能 | セットアップ | 備考 |
|-----------------|------|:----------:|------|
| 🌐 **Web** | 閲覧 | 設定不要 | 任意のURL → クリーンなMarkdown（[Jina Reader](https://github.com/jina-ai/reader) ⭐9.8K） |
| 🐦 **Twitter/X** | 閲覧・検索 | 設定不要 / Cookie | 単一ツイートはすぐに閲覧可能。Cookieで検索、タイムライン、投稿が解放（[twitter-cli](https://github.com/public-clis/twitter-cli)） |
| 📕 **小紅書** | 閲覧・検索・**投稿・コメント・いいね** | Cookie | `pipx install xiaohongshu-cli` + `xhs login`（[xhs-cli](https://github.com/jackwener/xiaohongshu-cli)） |
| 🎵 **抖音** | 動画解析・ウォーターマークなしダウンロード | mcporter | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server)、ログイン不要 |
| 💼 **LinkedIn** | Jina Reader（公開ページ） | プロフィール、企業、求人検索 | エージェントに「LinkedInの設定を手伝って」と伝えてください |
| 💬 **WeChat記事** | 検索 + 閲覧 | 設定不要 | WeChat公式アカウント記事の検索+閲覧（完全Markdown）（[Exa](https://exa.ai) + [Camoufox](https://github.com/daijro/camoufox)（オプション）） |
| 📰 **Weibo** | トレンド・検索・フィード・コメント | 設定不要 | ホット検索、コンテンツ/ユーザー/トピック検索、フィード、コメント（[mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo)） |
| 💻 **V2EX** | 人気トピック・ノードトピック・トピック詳細+返信・ユーザープロフィール | 設定不要 | 公開JSON API、認証不要。技術コミュニティのコンテンツに最適 |
| 📈 **雪球（Xueqiu）** | 株価・検索・人気投稿・人気銘柄 | 設定不要 | 公開APIで自動セッションCookie、ログイン不要 |
| 🎙️ **小宇宙Podcast** | 文字起こし | 無料APIキー | Podcast音声 → Groq Whisper（無料）による完全テキスト文字起こし |
| 🔍 **Web検索** | 検索 | 自動設定 | インストール時に自動設定、無料、APIキー不要（[Exa](https://exa.ai)、[mcporter](https://github.com/nicepkg/mcporter)経由） |
| 📦 **GitHub** | 閲覧・検索 | 設定不要 | [gh CLI](https://cli.github.com) 搭載。公開リポジトリはすぐ使える。`gh auth login`でFork、Issue、PRが解放 |
| 📺 **YouTube** | 閲覧・**検索** | 設定不要 | 字幕 + 1800以上の動画サイトでの検索（[yt-dlp](https://github.com/yt-dlp/yt-dlp) ⭐148K） |
| 📺 **Bilibili** | 閲覧・**検索** | 設定不要 / プロキシ | 動画情報 + 字幕 + 検索。ローカルはそのまま動作、サーバーはプロキシが必要（[yt-dlp](https://github.com/yt-dlp/yt-dlp)） |
| 📡 **RSS** | 閲覧 | 設定不要 | 任意のRSS/Atomフィード（[feedparser](https://github.com/kurtmckee/feedparser) ⭐2.3K） |
| 📖 **Reddit** | 検索・閲覧 | Cookie | 2024年以降認証が必要 — インストール後 `rdt login` を実行（[rdt-cli](https://github.com/public-clis/rdt-cli)） |

> **セットアップレベル：** 設定不要 = インストールしてすぐ使える · 自動設定 = インストール時に処理 · mcporter = MCPサービスが必要 · Cookie = ブラウザからエクスポート · プロキシ = 月額$1

---

## クイックスタート

以下をAIエージェント（Claude Code、OpenClaw、Cursor等）にコピーしてください：

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

エージェントが自動でインストールし、環境を検出し、何が使えるかを教えてくれます。

> 🔄 **すでにインストール済み？** 1コマンドでアップデート：
> ```
> Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

<details>
<summary>手動インストール</summary>

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```
</details>

<details>
<summary>Skillとしてインストール（Claude Code / OpenClaw / Skills対応の任意のエージェント）</summary>

```bash
npx skills add Panniantong/Agent-Reach@agent-reach
```

Skillインストール後、エージェントは`agent-reach` CLIが利用可能かを自動検出し、必要に応じてインストールします。

> `agent-reach install` でインストールした場合、Skillは自動的に登録されます — 追加の手順は不要です。
</details>

---

## すぐに使える機能

設定不要 — エージェントに伝えるだけ：

- 「このリンクを読んで」→ `curl https://r.jina.ai/URL` で任意のWebページ
- 「このGitHubリポジトリは何？」→ `gh repo view owner/repo`
- 「この動画の内容は？」→ `yt-dlp --dump-json URL` で字幕取得
- 「このツイートを読んで」→ `twitter tweet URL`
- 「このRSSを購読して」→ `feedparser` でフィード解析
- 「GitHubでLLMフレームワークを検索して」→ `gh search repos "LLM framework"`

**コマンドを覚える必要はありません。** エージェントがSKILL.mdを読み、何を呼び出すべきか理解します。

---

## 必要に応じてアンロック

使わない？設定しなくてOK。すべてのステップはオプションです。

### 🍪 Cookie — 無料、2分

エージェントに「Twitterのクッキーの設定を手伝って」と伝えてください — ブラウザからのエクスポート手順を案内してくれます。ローカルPCなら自動インポートも可能です。

### 🌐 プロキシ — 月額$1、サーバーのみ

RedditとBilibiliはサーバーIPをブロックします。プロキシを取得し（[Webshare](https://webshare.io) 推奨、月額$1）、アドレスをエージェントに伝えてください。

> ローカルPCではプロキシは不要です。Reddit検索はプロキシなしでもrdt-cliで無料で動作します。

---

## 一目でわかるステータス

```
$ agent-reach doctor

👁️  Agent Reach ステータス
========================================

✅ 利用可能:
  ✅ GitHubリポジトリとコード — 公開リポジトリの閲覧・検索可能
  ✅ Twitter/Xツイート — 閲覧可能。Cookieで検索・投稿が解放
  ✅ YouTube動画字幕 — yt-


# FILE: docs/troubleshooting.md

# 常见问题排查

## 雪球 / Xueqiu: API 返回 400

**症状：** `agent-reach doctor` 显示雪球 ⚠️，报 `HTTP Error 400`

**原因：** 雪球 API 需要登录 Cookie，无法通过匿名访问获取。

**解决方案：** 在 Chrome 里登录 xueqiu.com，然后运行：

```bash
agent-reach configure --from-browser chrome
```

再次运行 `agent-reach doctor` 确认恢复 ✅。Cookie 过期后重新运行即可。

---

## Twitter/X: twitter-cli 连接失败

**症状：** `twitter search` 或其他命令返回错误

**原因：** twitter-cli 需要 AUTH_TOKEN 和 CT0 环境变量才能访问 Twitter API。如果你的网络环境需要代理才能访问 x.com，需要配置代理。

**解决方案：**

### 方案 1：设置环境变量代理

```bash
export HTTP_PROXY="http://user:pass@host:port"
export HTTPS_PROXY="http://user:pass@host:port"
twitter search "test" -n 1
```

### 方案 2：使用全局代理工具

让代理工具接管所有网络流量，这样 twitter-cli 的请求也会走代理：

```bash
# macOS — ClashX / Surge 开启"增强模式"
# Linux — proxychains 或 tun2socks
proxychains twitter search "test" -n 1
```

### 方案 3：不用 twitter-cli，用 Exa 搜索替代

twitter-cli 不可用时，可以直接用 Exa 搜索 Twitter 内容：

```bash
mcporter call 'exa.web_search_exa(query: "site:x.com 搜索词", numResults: 5)'
```

### 方案 4：检查认证

```bash
twitter check
```

> 如果返回 "Missing credentials"，需要设置 AUTH_TOKEN 和 CT0 环境变量。
>
> **Fallback：** 如果你已经安装了 bird CLI（`npm install -g @steipete/bird`），它也能正常工作。Agent Reach 会自动检测已安装的工具。



# FILE: docs/install.md

# Agent Reach — Installation Guide

## For Humans

Copy this to your AI Agent:

```
帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

> 🛡️ **Security-conscious?** Use safe mode — it won't auto-install system packages:
> ```
> 帮我安装 Agent Reach（安全模式）：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
> 安装时使用 --safe 参数
> ```

---

## For AI Agents

### Goal

Install Agent Reach and all upstream tools so your user's agent has full internet access. After installation, you'll use the upstream tools directly (twitter-cli, rdt-cli, xhs-cli, yt-dlp, mcporter, gh CLI, etc.) — Agent Reach is just the installer and health checker.

### ⚠️ Boundaries

When fixing issues, stay within these limits:

- **DO NOT** run commands with `sudo` unless the user explicitly approved
- **DO NOT** modify system files outside `~/.agent-reach/`
- **DO NOT** install packages not listed in this guide
- **DO NOT** disable firewalls, security settings, or system protections
- **DO NOT** clone repos, create files, or run commands inside the agent workspace / working directory
- If something requires elevated permissions, **tell the user** what's needed and let them decide

### 📁 Directory Rules

All Agent Reach files go in dedicated directories — **never in the agent workspace**:

| Purpose | Directory | Example |
|---------|-----------|---------|
| Config & tokens | `~/.agent-reach/` | `~/.agent-reach/config.json` |
| Upstream tool repos | `~/.agent-reach/tools/` | `~/.agent-reach/tools/douyin-mcp-server/` |
| Temporary files | `/tmp/` | `/tmp/yt-dlp-output/` |
| Skills | `~/.openclaw/skills/agent-reach/` | SKILL.md |

**Why?** If you clone repos or create files in the workspace, it pollutes the user's project directory and can break their agent over time. Keep the workspace clean.

### Step 1: Install the basics

```bash
# 推荐：pipx（最省心）
pipx install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto

# 如果你的 Python 来自 Homebrew / 遇到 PEP 668（externally-managed-environment）
# 用虚拟环境安装：
python3 -m venv ~/.agent-reach-venv
source ~/.agent-reach-venv/bin/activate
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```

This installs core infrastructure (gh CLI, Node.js, mcporter, Exa search, yt-dlp config) and activates these zero-config channels:

- Web (Jina Reader), YouTube, GitHub, RSS, Exa Search, V2EX, Bilibili (basic)

> 💡 **macOS / Homebrew Python 提示 `externally-managed-environment`？**
> 这是 PEP 668 保护，不是 Agent Reach 本身的问题。优先用 `pipx install ...`，或先创建 `venv` 再安装。

**Safe mode / Dry run:**

```bash
agent-reach install --env=auto --safe      # Check only, no auto-install
agent-reach install --env=auto --dry-run   # Preview what would be done
```

### Step 2: Ask the user which optional channels they want

After installing the basics, **ask the user** which additional channels they need. Present this list:

> 基础渠道装好了！你现在可以让我搜网页、看 YouTube、读 GitHub 等。
>
> 还有这些可选渠道，你需要哪些？
>
> - 🐦 **Twitter/X** — 搜推文、看时间线（需要登录 Cookie）
> - 📰 **微博** — 热搜、搜索、用户动态
> - 💬 **微信公众号** — 搜索和阅读公众号文章
> - 📈 **雪球** — 股票行情、热门帖子（需要登录 Cookie）
> - 🎙️ **小宇宙播客** — 音频转文字（需要免费 Groq Key）
> - 📕 **小红书** — 阅读、搜索、发帖（需要登录）
> - 📖 **Reddit** — 搜索和阅读帖子
> - 📺 **B站完整版** — 热门、排行、搜索
> - 🎵 **抖音** — 视频解析
> - 💼 **LinkedIn** — Profile、职位搜索
>
> 告诉我你要哪些，比如"帮我装微博和 Twitter"。或者说"全部装"。

Based on the user's choice, run:

```bash
agent-reach install --env=auto --channels=twitter,weibo   # Example: user chose Twitter + Weibo
agent-reach install --env=auto --channels=all              # User wants everything
```

Supported channel names: `twitter`, `weibo`, `wechat`, `xiaoyuzhou`, `xueqiu`, `xiaohongshu`, `reddit`, `bilibili`, `douyin`, `linkedin`, `all`

### Step 3: Fix what's broken

Run `agent-reach doctor` and check the output.

Try to get as many channels to ✅ as possible. If something failed during install or shows as ❌/⚠️ in doctor, diagnose the problem and try to fix it — but stay within the boundaries above. If a fix requires elevated permissions or system changes, ask the user first.

Only ask the user when you genuinely need their input (credentials, permissions, etc.).

### Step 3: Configure things that need user input

Some channels need credentials only the user can provide. Based on the doctor output, ask for what's missing:

> 🔒 **Security tip:** For platforms that need cookies (Twitter, XiaoHongShu), we recommend using a **dedicated/secondary account** rather than your main account. Cookie-based auth carries two risks:
> 1. **Account ban** — platforms may detect non-browser API calls and restrict or ban the account
> 2. **Credential exposure** — cookies grant full account access; using a secondary account limits the blast radius if credentials are ever compromised

> 🍪 **Cookie 导入（所有需要登录的平台通用）：**
>
> 所有需要 Cookie 的平台（Twitter、小红书、雪球等），**优先使用 Cookie-Editor 导入**，这是最简单最可靠的方式：
> 1. 用户在自己的浏览器上登录对应平台
> 2. 安装 [Cookie-Editor](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) Chrome 插件
> 3. 点击插件 → Export → Header String
> 4. 把导出的字符串发给 Agent
>
> **本地电脑用户**也可以用 `agent-reach configure --from-browser chrome` 一键自动提取（支持 Twitter + 小红书 + 雪球）。

**Twitter search & posting:**
> "To unlock Twitter search, I need your Twitter cookies. Install the Cookie-Editor Chrome extension, go to x.com/twitter.com, click the extension → Export → Header String, and paste it to me."

```bash
agent-reach configure twitter-cookies "PASTED_STRING"
```

> **代理说明（中国大陆等需要翻墙的网络环境）：**
>
> twitter-cli 和 rdt-cli 使用 Python，在需要代理的网络环境下可通过环境变量配置代理。
>
> **你（Agent）需要做的：**
> 1. 确认用户配了代理：`agent-reach configure proxy http://user:pass@ip:port`
> 2. 设置环境变量：`export HTTP_PROXY="..." HTTPS_PROXY="..."`
> 3. Agent Reach 会自动处理剩下的，不需要用户做额外操作
>
> 如果用户报告 "fetch failed"，参考 [troubleshooting.md](troubleshooting.md)

**Reddit & Bilibili full access (server users):**
> "Reddit and Bilibili block server IPs. To unlock full access, I need a resid


# FILE: docs/cookie-export.md

# Cookie Export Guide — For Server Users

Your Agent is on a server and can't access your browser directly.
Here's how to export cookies from your local computer — **fastest method first**.

## Method 1: Cookie-Editor Extension (Recommended — 30 seconds per site)

1. Install **Cookie-Editor** for Chrome: https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm
   (Also available for Firefox, Edge)

2. Go to the website (e.g. https://x.com) and make sure you're logged in

3. Click the Cookie-Editor icon in your toolbar

4. Click **Export** → **Header String**

5. Paste the result to your Agent

That's it! Your Agent will run:
```bash
agent-reach configure twitter-cookies <your_pasted_string>
```

### Sites to export:

| Site | URL to visit | What to tell Agent |
|------|-------------|-------------------|
| Twitter/X | https://x.com | "Here are my Twitter cookies: [paste]" |
| XiaoHongShu | https://www.xiaohongshu.com | "Here are my XHS cookies: [paste]" |
| Bilibili | https://www.bilibili.com | "Here are my Bilibili cookies: [paste]" |

## Method 2: Manual (No extension needed)

1. Open the site in Chrome, make sure you're logged in
2. Press **F12** (or right-click → Inspect)
3. Click the **Network** tab
4. Refresh the page (F5)
5. Click any request in the list
6. In the right panel, scroll to **Request Headers**
7. Find the line starting with `Cookie:`
8. Copy the entire value after `Cookie: `
9. Paste to your Agent



# FILE: docs/README_ko.md

<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>AI 에이전트가 인터넷 전체에 접근할 수 있도록 한 번에 설정해 드립니다</strong>
</p>

<p align="center">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#빠른-시작">빠른 시작</a> · 한국어 · <a href="../README.md">中文</a> · <a href="README_en.md">English</a> · <a href="README_ja.md">日本語</a> · <a href="#지원-플랫폼">지원 플랫폼</a> · <a href="#설계-철학">설계 철학</a>
</p>

---

## Agent Reach가 필요한 이유

AI 에이전트는 이미 인터넷에 접근할 수 있습니다 — 하지만 "인터넷에 접속할 수 있다"는 것은 시작에 불과합니다.

가장 가치 있는 정보는 소셜 미디어와 특화된 플랫폼에 분포되어 있습니다: Twitter 토론, Reddit 피드백, YouTube 튜토리얼, XiaoHongShu 리뷰, Bilibili 비디오, GitHub 활동... **여기가 정보 밀도가 가장 높은 곳**이지만, 각 플랫폼은 고유한 진입장벽이 있습니다:

| 문제점 | 현실 |
|------------|---------|
| Twitter API | 유료 사용, 중간 정도 사용량 ~월 $215 |
| Reddit | 서버 IP가 403 오류 발생 |
| XiaoHongShu | 둘러보기 위해 로그인 필요 |
| Bilibili | 해외/서버 IP 차단 |

에이전트를 이 플랫폼에 연결하려면 도구를 찾고, 의존성을 설치하고, 설정을 디버깅해야 합니다 — 하나씩 직접.

**Agent Reach는 이를 하나의 명령으로 바꿉니다:**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

이 명령을 에이전트에 복사해서 붙여넣으세요. 몇 분 뒤에는 트윗을 읽고, Reddit을 검색하고, Bilibili를 볼 수 있게 됩니다.

**이미 설치하셨나요? 한 번에 업데이트하세요:**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ 시작하기 전에 알면 좋은 것들

| | |
|---|---|
| 💰 **완전 무료** | 모든 도구는 오픈 소스, 모든 API는 무료입니다. 유일한 비용은 서버 프록시(월 $1)일 수 있습니다 — 로컬 컴퓨터에서는 불필요 |
| 🔒 **프라이버시 안전** | Cookie는 로컬에 유지됩니다. 업로드되지 않습니다. 완전 오픈 소스 — 언제든지 감사 가능 |
| 🔄 **최신 상태 유지** | 업스트림 도구(yt-dlp, twitter-cli, rdt-cli, Jina Reader 등)를 추적하고 정기적으로 업데이트 |
| 🤖 **모든 에이전트와 호환** | Claude Code, OpenClaw, Cursor, Windsurf... 명령을 실행할 수 있는 모든 에이전트 |
| 🩺 **내장 진단 도구** | `agent-reach doctor` — 하나의 명령으로 작동 항목, 작동하지 않는 항목, 수정 방법 표시 |

---

## 지원 플랫폼

| 플랫폼 | 기능 | 설정 | 참고 |
|----------|-------------|:-----:|-------|
| 🌐 **Web** | 읽기 | 없음 | 모든 URL → 깨끗한 Markdown ([Jina Reader](https://github.com/jina-ai/reader) ⭐9.8K) |
| 🐦 **Twitter/X** | 읽기 · 검색 | Cookie | Cookie로 검색, 타임라인, 트윗 읽기, 아티클 읽기 가능 ([twitter-cli](https://github.com/public-clis/twitter-cli)) |
| 📕 **XiaoHongShu** | 읽기 · 검색 · **게시글 작성 · 댓글 · 좋아요** | Cookie | `pipx install xiaohongshu-cli` + `xhs login` ([xhs-cli](https://github.com/jackwener/xiaohongshu-cli)) |
| 🎵 **Douyin** | 비디오 파싱 · 워터마크 없는 다운로드 | mcporter | [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server) 통해, 로그인 불필요 |
| 💼 **LinkedIn** | Jina Reader (공개 페이지) | Cookie | 전체 프로필, 회사, 채용 공고 검색 가능. 에이전트에 "LinkedIn 설정 도와줘"라고 말하세요 |
| 💬 **WeChat Articles** | 검색 + 읽기 | 없음 | Exa를 통한 WeChat 공식 계정 게시글 검색 + 읽기 (설정 없음) + 선택적 [Camoufox](https://github.com/daijro/camoufox) |
| 📰 **Weibo** | 인기 · 검색 · 피드 · 댓글 | 없음 | 핫 검색, 콘텐츠/사용자/주제 검색, 피드, 댓글 ([mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo)) |
| 💻 **V2EX** | 인기 주제 · 노드 주제 · 주제 상세 + 답글 · 사용자 프로필 | 없음 | 공개 JSON API, 인증 없음. 기술 커뮤니티 콘텐츠에 적합 |
| 📈 **Xueqiu (雪球)** | 주식 시세 · 검색 · 인기 글 · 인기 종목 | 브라우저 Cookie | 에이전트에 "Xueqiu 설정 도와줘"라고 말하세요 |
| 🎙️ **Xiaoyuzhou Podcast** | 음성 변환 | 무료 API key | Groq Whisper를 통한 팟캐스트 오디오 → 전체 텍스트 변환 (무료) |
| 🔍 **Web Search** | 검색 | 자동 설정 | 설치 시 자동 설정, 무료, API key 불필요 ([Exa](https://exa.ai) via [mcporter](https://github.com/nicepkg/mcporter)) |
| 📦 **GitHub** | 읽기 · 검색 | 없음 | [gh CLI](https://cli.github.com) 기반. 공개 저장소는 즉시 사용 가능. `gh auth login`으로 Fork, Issue, PR 기능 활성화 |
| 📺 **YouTube** | 읽기 · **검색** | 없음 | 자막 + 1800+ 비디오 사이트 검색 ([yt-dlp](https://github.com/yt-dlp/yt-dlp) ⭐148K) |
| 📺 **Bilibili** | 읽기 · **검색** | 없음 / 프록시 | 비디오 정보 + 자막 + 검색. 로컬은 바로 작동, 서버는 프록시 필요 ([yt-dlp](https://github.com/yt-dlp/yt-dlp)) |
| 📡 **RSS** | 읽기 | 없음 | 모든 RSS/Atom 피드 ([feedparser](https://github.com/kurtmckee/feedparser) ⭐2.3K) |
| 📖 **Reddit** | 검색 · 읽기 | Cookie | 2024년부터 인증 필요 — 설치 후 `rdt login` 실행 ([rdt-cli](https://github.com/public-clis/rdt-cli)) |

> **설정 단계:** 없음 = 설치 후 바로 사용 · 자동 = 설치 시 처리 · mcporter = MCP 서비스 필요 · Cookie = 브라우저에서 내보내기 · 프록시 = 월 $1

---

## 빠른 시작

이 명령을 AI 에이전트(Claude Code, OpenClaw, Cursor 등)에 입력하세요:

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

에이전트가 자동으로 설치하고, 환경을 감지하고, 준비된 항목을 알려줍니다.

> 🔄 **이미 설치하셨나요?** 한 번에 업데이트:
> ```
> Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

<details>
<summary>수동 설치</summary>

```bash
pip install https://github.com/Panniantong/agent-reach/archive/main.zip
agent-reach install --env=auto
```
</details>

<details>
<summary>Skill로 설치 (Claude Code / OpenClaw / Skill을 지원하는 모든 에이전트)</summary>

```bash
npx skills add Panniantong/Agent-Reach@agent-reach
```

Skill이 설치된 후, 에이전트는 `agent-reach` CLI 사용 가능 여부를 자동 감지하고 필요한 경우 설치합니다.

> `agent-reach install`을 통해 설치하면 Skill이 자동으로 등록됩니다 — 추가 단계 불필요.
</details>

---

## 별도 설정 없이 바로 사용

별도의 설정이 필요 없습니다. 에이전트에게 요청하기만 하면 됩니다:

- "이 링크 읽어줘" → 모든 웹 페이지에 대해 `curl https://r.jina.ai/URL`
- "이 GitHub 저장소는 무엇인가요?" → `gh repo view owner/repo`
- "이 비디오는 무엇을 다루나요?" → 자막을 위해 `yt-dlp --dump-json URL`
- "이 트윗 읽어줘" → `twitter tweet URL`
- "이 RSS 구독해줘" → 피드 파싱을 위해 `feedparser`
- "GitHub에서 LLM 프레임워크 검색" → `gh search repos "LLM framework"`

**기억할 명령이 없습니다.** 에이전트가 SKILL.md를 읽고 무엇을 호출할지 알고 있습니다.

---

## 필요할 때 설정

사용하지 않나요? 설정하지 마세요. 모든 단계는 선택 사항입니다.

### 🍪 Cookies — 무료, 2분

에이전트에 "Twitter 쿠키 설정 도와줘"라고 말하세요 — 브라우저에서 내보내는 과정을 안내해 줍니다. 로컬 컴퓨터는 자동으로 가져올 수 있습니다.

### 🌐 Proxy — 월 $1, 서버 전용

Bilibili은 서버 IP를 차단합니다. 프록시를 가져오세요([Webshare](https://webshare.io) 추천, 월 $1)하고 주소를 에이전트에 보내세요.

> Reddit은 이제 프록시 없이 rdt-cli를 통해 무료로 작동합니다. 로컬 컴퓨터는 Bilibili에도 프록시가 필요 없습니다.

---

## 한눈에 보는 상태

```
$ agent-reach doctor

👁️  Agent Rea


# FILE: docs/README_en.md

<h1 align="center">👁️ Agent Reach</h1>

<p align="center">
  <strong>Give your AI Agent one-click access to the entire internet</strong>
</p>

<p align="center">
  <a href="../LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.10+-green.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+"></a>
  <a href="https://github.com/Panniantong/agent-reach/stargazers"><img src="https://img.shields.io/github/stars/Panniantong/agent-reach?style=for-the-badge" alt="GitHub Stars"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> · <a href="../README.md">中文</a> · <a href="README_ja.md">日本語</a> · <a href="README_ko.md">한국어</a> · <a href="#supported-platforms">Platforms</a> · <a href="#design-philosophy">Philosophy</a>
</p>

---

## Why Agent Reach?

AI Agents can already access the internet — but "can go online" is barely the start.

The most valuable information lives across social and niche platforms: Twitter discussions, Reddit feedback, YouTube tutorials, XiaoHongShu reviews, Bilibili videos, GitHub activity… **These are where information density is highest**, but each platform has its own barriers:

| Pain Point | Reality |
|------------|---------|
| Twitter API | Pay-per-use, moderate usage ~$215/month |
| Reddit | Server IPs get 403'd |
| XiaoHongShu | Login required to browse |
| Bilibili | Blocks overseas/server IPs |

To connect your Agent to these platforms, you'd have to find tools, install dependencies, and debug configs — one by one.

**Agent Reach turns this into one command:**

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Copy that to your Agent. A few minutes later, it can read tweets, search Reddit, and watch Bilibili.

**Already installed? Update in one command:**

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

### ✅ Before you start, you might want to know

| | |
|---|---|
| 💰 **Completely free** | All tools are open source, all APIs are free. The only possible cost is a server proxy ($1/month) — local computers don't need one |
| 🔒 **Privacy safe** | Cookies stay local. Never uploaded. Fully open source — audit anytime |
| 🔄 **Kept up to date** | Upstream tools (yt-dlp, twitter-cli, rdt-cli, Jina Reader, etc.) are tracked and updated regularly |
| 🤖 **Works with any Agent** | Claude Code, OpenClaw, Cursor, Windsurf… any Agent that can run commands |
| 🩺 **Built-in diagnostics** | `agent-reach doctor` — one command shows what works, what doesn't, and how to fix it |

---

## Supported Platforms

| Platform | Capabilities | Setup | Notes |
|----------|-------------|:-----:|-------|
| 🌐 **Web** | Read | Zero config | Any URL → clean Markdown ([Jina Reader](https://github.com/jina-ai/reader) ⭐9.8K) |
| 🐦 **Twitter/X** | Read · Search | Cookie | Cookie unlocks search, timeline, tweet reading, articles ([twitter-cli](https://github.com/public-clis/twitter-cli)) |
| 📕 **XiaoHongShu** | Read · Search · **Post · Comment · Like** | Cookie | `pipx install xiaohongshu-cli` + `xhs login` ([xhs-cli](https://github.com/jackwener/xiaohongshu-cli)) |
| 🎵 **Douyin** | Video parsing · Watermark-free download | mcporter | Via [douyin-mcp-server](https://github.com/yzfly/douyin-mcp-server), no login needed |
| 💼 **LinkedIn** | Jina Reader (public pages) | Full profiles, companies, job search | Tell your Agent "help me set up LinkedIn" |
| 💬 **WeChat Articles** | Search + Read | Zero config | Search + read WeChat Official Account articles via Exa (zero config) + optional [Camoufox](https://github.com/daijro/camoufox) |
| 📰 **Weibo** | Trending · Search · Feeds · Comments | Zero config | Hot search, content/user/topic search, feeds, comments ([mcp-server-weibo](https://github.com/Panniantong/mcp-server-weibo)) |
| 💻 **V2EX** | Hot topics · Node topics · Topic detail + replies · User profile | Zero config | Public JSON API, no auth required. Great for tech community content |
| 📈 **Xueqiu (雪球)** | Stock quotes · Search · Hot posts · Hot stocks | Browser cookie | Tell your Agent "help me set up Xueqiu" |
| 🎙️ **Xiaoyuzhou Podcast** | Transcription | Free API key | Podcast audio → full text transcript via Groq Whisper (free) |
| 🔍 **Web Search** | Search | Auto-configured | Auto-configured during install, free, no API key ([Exa](https://exa.ai) via [mcporter](https://github.com/nicepkg/mcporter)) |
| 📦 **GitHub** | Read · Search | Zero config | [gh CLI](https://cli.github.com) powered. Public repos work immediately. `gh auth login` unlocks Fork, Issue, PR |
| 📺 **YouTube** | Read · **Search** | Zero config | Subtitles + search across 1800+ video sites ([yt-dlp](https://github.com/yt-dlp/yt-dlp) ⭐148K) |
| 📺 **Bilibili** | Read · **Search** | Zero config / Proxy | Video info + subtitles + search. Local works directly, servers need a proxy ([yt-dlp](https://github.com/yt-dlp/yt-dlp)) |
| 📡 **RSS** | Read | Zero config | Any RSS/Atom feed ([feedparser](https://github.com/kurtmckee/feedparser) ⭐2.3K) |
| 📖 **Reddit** | Search · Read | Cookie | Requires auth since 2024 — `rdt login` after install ([rdt-cli](https://github.com/public-clis/rdt-cli)) |

> **Setup levels:** Zero config = install and go · Auto-configured = handled during install · mcporter = needs MCP service · Cookie = export from browser · Proxy = $1/month

---

## Quick Start

Copy this to your AI Agent (Claude Code, OpenClaw, Cursor, etc.):

```
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

The Agent auto-installs, detects your environment, and tells you what's ready.

> 🔄 **Already installed?** Update in one command:
> ```
> Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
> ```

<details>
<summary>Manual install</summary>

```bash
pip 


# FILE: docs/update.md

# Agent Reach — Update Guide

## For Humans

Copy this to your AI Agent:

```
帮我更新 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

Or in English:

```
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

---

## For AI Agents

### ⚠️ Workspace Rules

**Never create files, clone repos, or run commands in the agent workspace.** Use `/tmp/` for temporary work and `~/.agent-reach/` for persistent data.

### Goal

Update Agent Reach to the latest version, install any new upstream tools, migrate from deprecated tools, and verify everything works. The user should not need to do anything manually.

### Step 1: Check current version

```bash
agent-reach check-update
```

If it says "已是最新版本", skip to Step 5 (verify). Otherwise continue.

### Step 2: Update Agent Reach package

```bash
pip install --upgrade https://github.com/Panniantong/agent-reach/archive/main.zip
```

### Step 3: Install / migrate upstream tools

Run these commands to ensure all upstream CLI tools are installed. Skip any that are already installed.

```bash
# === Required tools (core functionality) ===

# Twitter/X — twitter-cli (replaces deprecated bird CLI)
which twitter >/dev/null 2>&1 || pipx install twitter-cli 2>/dev/null || uv tool install twitter-cli 2>/dev/null

# Reddit — rdt-cli (replaces Exa-based approach)
which rdt >/dev/null 2>&1 || pipx install rdt-cli 2>/dev/null || uv tool install rdt-cli 2>/dev/null

# XiaoHongShu — xhs-cli (replaces Docker MCP)
which xhs >/dev/null 2>&1 || pipx install xiaohongshu-cli 2>/dev/null || uv tool install xiaohongshu-cli 2>/dev/null

# === Optional enhancements ===

# Bilibili — bili-cli (adds hot/rank/search on top of yt-dlp)
which bili >/dev/null 2>&1 || pipx install bilibili-cli 2>/dev/null || uv tool install bilibili-cli 2>/dev/null

# mcporter + Exa (for WeChat, web search)
which mcporter >/dev/null 2>&1 || npm install -g mcporter 2>/dev/null

# yt-dlp (YouTube + Bilibili video)
which yt-dlp >/dev/null 2>&1 || pip install yt-dlp 2>/dev/null

# gh CLI (GitHub)
which gh >/dev/null 2>&1 || echo "GitHub CLI not installed — see https://cli.github.com"
```

### Step 4: Coexistence (DO NOT uninstall old tools)

**IMPORTANT: Never uninstall any existing tools the user already has installed.** Old tools (bird, browser_cookie3, miku_ai, etc.) may still be working on the user's machine even if their upstream repos are archived or deleted. Agent Reach supports both old and new tools as fallback. Only install new tools alongside existing ones.

### Step 5: Verify

```bash
agent-reach version
agent-reach doctor
```

Check the doctor output:
- All channels should show ✅ or ⚠️ (with clear instructions)
- If any channel that was working before now shows ❌, investigate:
  - Twitter: needs `twitter-cli` + browser cookies (run `xhs login` pattern)
  - Reddit: needs `rdt-cli` (should be installed in Step 3)
  - XiaoHongShu: needs `xhs-cli` + login (run `xhs login`)
  - WeChat: should work via Exa (zero config)

### Step 6: Update SKILL.md (if installed)

```bash
agent-reach install --skill-only 2>/dev/null || python3 -c "
import importlib.resources, os
try:
    skill_pkg = importlib.resources.files('agent_reach').joinpath('skill')
except Exception:
    from pathlib import Path
    skill_pkg = Path(os.path.dirname(os.path.abspath(__file__))).parent / 'agent_reach' / 'skill'

skill_md = skill_pkg.joinpath('SKILL.md').read_text(encoding='utf-8')
refs_pkg = skill_pkg.joinpath('references')

for base in [os.path.expanduser('~/.openclaw/skills/agent-reach'),
             os.path.expanduser('~/.claude/skills/agent-reach'),
             os.path.expanduser('~/.agents/skills/agent-reach')]:
    if os.path.isdir(base):
        with open(os.path.join(base, 'SKILL.md'), 'w', encoding='utf-8') as f:
            f.write(skill_md)
        refs_dir = os.path.join(base, 'references')
        os.makedirs(refs_dir, exist_ok=True)
        for ref in refs_pkg.iterdir():
            name = ref.name if hasattr(ref, 'name') else str(ref).split('/')[-1]
            if name.endswith('.md'):
                with open(os.path.join(refs_dir, name), 'w', encoding='utf-8') as f:
                    f.write(ref.read_text(encoding='utf-8'))
        print(f'✅ Updated skill: {base}')
"
```

### Step 7: Report to user

Tell the user:
1. What version they're now on (`agent-reach version`)
2. How many channels are available (count ✅ in doctor output)
3. Any channels that need their action (e.g., `xhs login` for XiaoHongShu, browser cookies for Twitter)
4. What changed in this update (major: Twitter/Reddit/XiaoHongShu upstream tools migrated for better stability)

Done.



# FILE: docs/dependency-locking.md

# Dependency Locking Guide

Agent Reach uses `constraints.txt` as a reproducible dependency baseline.

## Why

- Keep local/CI dependency graph stable
- Reduce "works on my machine" drift
- Make regression results easier to compare

## Install with constraints

```bash
pip install -c constraints.txt -e .[dev]
```

## Update workflow

1. Update `pyproject.toml` dependency ranges as needed.
2. Validate against latest compatible versions locally.
3. Update pinned versions in `constraints.txt`.
4. Run validation:

```bash
pytest -q
ruff check agent_reach tests
mypy agent_reach
```

5. Open PR with dependency and validation notes.

