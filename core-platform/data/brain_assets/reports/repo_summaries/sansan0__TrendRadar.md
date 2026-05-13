# Repo Summary Source: sansan0/TrendRadar
- URL: https://github.com/sansan0/TrendRadar
- Local Path: core-platform/data/brain_assets/repos/github_stars/sansan0__TrendRadar
- Buckets: mcp, llm_runtime, ui
- Stars: 57410
- Language: Python
- Description: ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。
- Clone Status: cloned
## Extracted README / Docs


# FILE: README-MCP-FAQ-EN.md

<div align="center">

**[中文](README-MCP-FAQ.md)** | **English**

</div>

# TrendRadar MCP Tool Usage Q&A

> AI Query Guide - How to Use News Trend Analysis Tools Through Natural Conversation (v3.1.7)

---

## 📋 Tools Overview

| Category | Tool Name | Description |
|:--------:|-----------|-------------|
| **Date** | `resolve_date_range` | Parse "this week", "last 7 days" to standard dates |
| **Query** | `get_latest_news` | Get the latest batch of trending news |
| | `get_news_by_date` | Query historical news by date range |
| | `get_trending_topics` | Get trending topics statistics (auto-extract supported) |
| **RSS** | `get_latest_rss` | Get latest RSS subscription content |
| | `search_rss` | Search keywords in RSS data |
| | `get_rss_feeds_status` | View RSS feed config and data status |
| **Search** | `search_news` | Unified search (keyword/fuzzy/entity, RSS optional) |
| | `find_related_news` | Find news similar to a given title |
| **Analysis** | `analyze_topic_trend` | Topic trend analysis (hotness/lifecycle/viral/predict) |
| | `analyze_data_insights` | Data insights (platform compare/activity/co-occurrence) |
| | `analyze_sentiment` | News sentiment analysis |
| | `aggregate_news` | Cross-platform news aggregation & dedup |
| | `compare_periods` | Period comparison (week-over-week/month-over-month) |
| | `generate_summary_report` | Generate daily/weekly summary reports |
| **System** | `get_current_config` | Get current system configuration |
| | `get_system_status` | Get system running status |
| | `check_version` | Check version updates (TrendRadar + MCP Server) |
| | `trigger_crawl` | Manually trigger a crawl task |
| **Storage** | `sync_from_remote` | Pull data from remote storage to local |
| | `get_storage_status` | Get storage config and status |
| | `list_available_dates` | List available dates (local/remote) |
| **Article** | `read_article` | Read single article content (Markdown format) |
| | `read_articles_batch` | Batch read multiple articles (max 5) |
| **Notification** | `get_notification_channels` | Get all configured notification channels and their status |
| | `send_notification` | Send messages to configured notification channels (auto format conversion) |

---

## ⚙️ Default Settings Explanation (Important!)

The following optimization strategies are adopted by default, mainly to save AI token consumption:

| Default Setting | Description | How to Adjust |
| -------------- | --------------------------------------- | ------------------------------------- |
| **Result Limit** | Default returns 50 news items | Say "return top 10" or "give me 100 items" in conversation |
| **Time Range** | Default queries today's data | Say "query yesterday", "last week" or "Jan 1 to 7" |
| **URL Links** | Default no links (saves ~160 tokens/item) | Say "need links" or "include URLs" |
| **Keyword List** | Default does not use frequency_words.txt to filter news | Only used when calling "trending topics" tool |

**⚠️ Important:** The choice of AI model directly affects the tool call effectiveness. The smarter the AI, the more accurate the calls. When you remove the above restrictions, for example, from querying today to querying a week, first you need to have a week's data locally, and secondly, token consumption may multiply.

**💡 Tip:** This project provides a dedicated date parsing tool that can accurately parse natural language date expressions like "last 7 days", "this week", ensuring all AI models get consistent date ranges. See Q18 below for details.


## 💰 AI Models

Below I use the **[SiliconFlow](https://cloud.siliconflow.cn)** platform as an example, which has many large models to choose from. During the development and testing of this project, I used this platform for many functional tests and validations.

### 📊 Registration Method Comparison

| Registration Method | Direct Registration Without Referral | Registration With Referral Link |
|:-------:|:-------:|:-----------------:|
| Registration Link | [siliconflow.cn](https://cloud.siliconflow.cn) | [Referral Link](https://cloud.siliconflow.cn/i/fqnyVaIU) |
| Free Quota | 0 tokens | **20 million tokens** (≈$2) |
| Extra Benefits | ❌ | ✅ Referrer also gets 20 million tokens |

> 💡 **Tip**: The above gift quota should allow for **200+ queries**


### 🚀 Quick Start

#### 1️⃣ Register and Get API Key

1. Complete registration using the link above
2. Visit [API Key Management Page](https://cloud.siliconflow.cn/me/account/ak)
3. Click "Create New API Key"
4. Copy the generated key (please keep it safe)

#### 2️⃣ Configure in Cherry Studio

1. Open **Cherry Studio**
2. Go to "Model Service" settings
3. Find "SiliconFlow"
4. Paste the copied key into the **[API Key]** input box
5. Ensure the checkbox in the top right corner shows **green** when enabled ✅

---

### ✨ Configuration Complete!

Now you can start using this project and enjoy stable and fast AI services!

After testing one query, please immediately check the [SiliconFlow Billing](https://cloud.siliconflow.cn/me/bills) to see the consumption and have an estimate in mind.


---

## Basic Queries

### Q1: How to view the latest news?

**You can ask like this:**

- "Show me the latest news"
- "Query today's trending news"
- "Get the latest 10 news from Zhihu and Weibo"
- "View latest news, need links included"

**Tool return behavior:**

- Tool returns the latest 50 news items from all platforms
- Does not include URL links by default (saves tokens)

**AI display behavior (Important):**

- ⚠️ **AI usually auto-summarizes**, only showing partial news (like TOP 10-20 items)
- ✅ If you want to see all 50 items, need to explicitly request: "show all news" or "list all 50 items completely"
- 💡 This is the AI model's natural behavior, not a tool limitation

**Can be adjusted:**

- Specify platform: like "only Zhihu"
- Adjust quantity: like "return top 20"
- Include links: like "need links"
- **Request full display**: like "show all, don't summarize"

---

### Q2: How to quer


# FILE: README.md

<div align="center" id="trendradar">

<a href="https://github.com/sansan0/TrendRadar" title="TrendRadar">
  <img src="/_image/banner.webp" alt="TrendRadar Banner" width="80%">
</a>

最快<strong>30秒</strong>部署的热点助手 —— 告别无效刷屏，只看真正关心的新闻资讯

<a href="https://trendshift.io/repositories/14726" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14726" alt="sansan0%2FTrendRadar | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>


[![GitHub Stars](https://img.shields.io/github/stars/sansan0/TrendRadar?style=flat-square&logo=github&color=yellow)](https://github.com/sansan0/TrendRadar/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/sansan0/TrendRadar?style=flat-square&logo=github&color=blue)](https://github.com/sansan0/TrendRadar/network/members)
[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg?style=flat-square)](LICENSE)
[![Version](https://img.shields.io/badge/version-v6.6.2-blue.svg)](https://github.com/sansan0/TrendRadar)
[![MCP](https://img.shields.io/badge/MCP-v4.0.2-green.svg)](https://github.com/sansan0/TrendRadar)
[![RSS](https://img.shields.io/badge/RSS-订阅源支持-orange.svg?style=flat-square&logo=rss&logoColor=white)](https://github.com/sansan0/TrendRadar)
[![AI翻译](https://img.shields.io/badge/AI-多语言推送-purple.svg?style=flat-square)](https://github.com/sansan0/TrendRadar)

[![企业微信通知](https://img.shields.io/badge/企业微信-通知-00D4AA?style=flat-square)](https://work.weixin.qq.com/)
[![个人微信通知](https://img.shields.io/badge/个人微信-通知-00D4AA?style=flat-square)](https://weixin.qq.com/)
[![Telegram通知](https://img.shields.io/badge/Telegram-通知-00D4AA?style=flat-square)](https://telegram.org/)
[![dingtalk通知](https://img.shields.io/badge/钉钉-通知-00D4AA?style=flat-square)](#)
[![飞书通知](https://img.shields.io/badge/飞书-通知-00D4AA?style=flat-square)](https://www.feishu.cn/)
[![邮件通知](https://img.shields.io/badge/Email-通知-00D4AA?style=flat-square)](#)
[![ntfy通知](https://img.shields.io/badge/ntfy-通知-00D4AA?style=flat-square)](https://github.com/binwiederhier/ntfy)
[![Bark通知](https://img.shields.io/badge/Bark-通知-00D4AA?style=flat-square)](https://github.com/Finb/Bark)
[![Slack通知](https://img.shields.io/badge/Slack-通知-00D4AA?style=flat-square)](https://slack.com/)
[![通用Webhook](https://img.shields.io/badge/通用-Webhook-607D8B?style=flat-square&logo=webhook&logoColor=white)](#)


[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-自动化-2088FF?style=flat-square&logo=github-actions&logoColor=white)](https://github.com/sansan0/TrendRadar)
[![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-部署-4285F4?style=flat-square&logo=github&logoColor=white)](https://sansan0.github.io/TrendRadar)
[![Docker](https://img.shields.io/badge/Docker-部署-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/wantcat/trendradar)
[![MCP Support](https://img.shields.io/badge/MCP-AI分析支持-FF6B6B?style=flat-square&logo=ai&logoColor=white)](https://modelcontextprotocol.io/)
[![AI分析推送](https://img.shields.io/badge/AI-分析推送-FF6B6B?style=flat-square&logo=openai&logoColor=white)](#)
[![AI智能筛选](https://img.shields.io/badge/AI-智能筛选新闻-9B59B6?style=flat-square&logo=openai&logoColor=white)](#)

</div>

<div align="center">

**中文** | **[English](README-EN.md)**

</div>

> 本项目以轻量，易部署为目标

<br>

## 📑 快速导航

> 💡 **点击下方链接**可快速跳转到对应章节。部署推荐从「**快速开始**」入手，需要详细自定义请看「**配置详解**」

<div align="center">

|   |   |   |
|:---:|:---:|:---:|
| [🚀 **快速开始**](#-快速开始) | [AI 智能分析](#-ai-智能分析) | [⚙️ **配置详解**](#配置详解) |
| [Docker部署](#6-docker-部署) | [MCP客户端](#-mcp-客户端) | [📝 **更新日志**](#-更新日志) |
| [🎯 **核心功能**](#-核心功能) | [☕ **支持项目**](#-支持项目) | [📚 **项目相关**](#-项目相关) |

</div>

<br>

- 感谢**为项目点 star** 的观众们，**fork** 你所欲也，**star** 我所欲也，两者得兼😍是对开源精神最好的支持

<details>
<summary>👉 点击展开：<strong>致谢名单</strong> (天使轮荣誉榜 🔥73+🔥 位)</summary>

### 早期支持者致谢

> 💡 **特别说明**：
>
> 1. **关于名单**：下方表格记录了项目起步阶段（天使轮）的支持者。因早期人工统计繁琐，**难免存在疏漏或记录不全的情况，如有遗漏，实非本意，万望海涵**。
> 2. **未来规划**：为了将有限的精力回归代码与功能迭代，**即日起不再人工维护此名单**。
>
> 无论名字是否上榜，你们的每一份支持都是 TrendRadar 能够走到今天的基石。🙏

### 基础设施支持

感谢 **GitHub** 免费提供的基础设施，这是本项目得以**一键 fork**便捷运行的最大前提。

### 数据支持

本项目使用 [newsnow](https://github.com/ourongxing/newsnow) 项目的 API 获取多平台数据，特别感谢作者提供的服务。

经联系，作者表示无需担心服务器压力，但这是基于他的善意和信任。请大家：
- **前往 [newsnow 项目](https://github.com/ourongxing/newsnow) 点 star 支持**
- Docker 部署时，请合理控制推送频率，勿竭泽而渔

### 推广助力

> 感谢以下平台和个人的推荐(按时间排列)

- [小众软件](https://mp.weixin.qq.com/s/fvutkJ_NPUelSW9OGK39aA) - 开源软件推荐平台
- [LinuxDo 社区](https://linux.do/) - 技术爱好者的聚集地
- [阮一峰周刊](https://github.com/ruanyf/weekly) - 技术圈有影响力的周刊

### 观众支持

> 感谢**给予资金支持**的朋友们，你们的慷慨已化身为键盘旁的零食饮料，陪伴着项目的每一次迭代。
>
> **关于"一元点赞"的回归**：
> 随着 v5.0.0 版本的发布，项目迈入了一个新的阶段。为了支持日益增长的 API 成本和咖啡因消耗，"一元点赞"通道现已重新开启。你的每一份心意，都将转化为代码世界里的 Token 和动力。🚀 [前往支持](#-支持项目)

|           点赞人            |  金额  |  日期  |             备注             |
| :-------------------------: | :----: | :----: | :-----------------------: |
|           D*5          |  1.8 * 3 | 2025.11.24  |    | 
|           *鬼          |  1 | 2025.11.17  |    | 
|           *超          |  10 | 2025.11.17  |    | 
|           R*w          |  10 | 2025.11.17  | 这 agent 做的牛逼啊,兄弟    | 
|           J*o          |  1 | 2025.11.17  | 感谢开源,祝大佬事业有成    | 
|           *晨          |  8.88  | 2025.11.16  | 项目不错,研究学习中    | 
|           *海          |  1  | 2025.11.15  |    | 
|           *德          |  1.99  | 2025.11.15  |    | 
|           *疏          |  8.8  | 2025.11.14  |  感谢开源，项目很棒，支持一下   | 
|           M*e          |  10  | 2025.11.14  |  开源不易，大佬辛苦了   | 
|           **柯          |  1  | 2025.11.14  |     | 
|           *云          |  88  | 2025.11.13  |    好项目，感谢开源  | 
|           *W          |  6  | 2025.11.13  |      | 
|           *凯          |  1  | 2025.11.13  |      | 
|           对*.          |  1  | 2025.11.13  |    Thanks for your TrendRadar  | 
|           s*y          |  1  | 2025.11.13  |      | 
|           **翔          |  10  | 2025.11.13  |   好项目，相见恨晚，感谢开源！     | 
|           *韦          |  9.9  | 2025.11.13  |   TrendRadar超赞，请老师喝咖啡~     | 
|           h*p          |


# FILE: README-MCP-FAQ.md

<div align="center">

**中文** | **[English](README-MCP-FAQ-EN.md)**

</div>

# TrendRadar MCP 工具使用问答

> AI 提问指南 - 如何通过自然对话使用新闻热点分析工具（v3.1.7）

---

## 📋 工具一览

| 分类 | 工具名称 | 功能简介 |
|:----:|---------|---------|
| **日期** | `resolve_date_range` | 解析"本周"、"最近7天"等自然语言为标准日期 |
| **查询** | `get_latest_news` | 获取最新一批爬取的热榜新闻 |
| | `get_news_by_date` | 按日期范围查询历史新闻 |
| | `get_trending_topics` | 获取热点话题统计（支持自动提取） |
| **RSS** | `get_latest_rss` | 获取最新 RSS 订阅内容 |
| | `search_rss` | 在 RSS 数据中搜索关键词 |
| | `get_rss_feeds_status` | 查看 RSS 源配置和数据状态 |
| **搜索** | `search_news` | 统一搜索（关键词/模糊/实体，可含RSS） |
| | `find_related_news` | 查找与指定标题相似的新闻 |
| **分析** | `analyze_topic_trend` | 话题趋势分析（热度/生命周期/爆火/预测） |
| | `analyze_data_insights` | 数据洞察（平台对比/活跃度/关键词共现） |
| | `analyze_sentiment` | 新闻情感倾向分析 |
| | `aggregate_news` | 跨平台新闻聚合去重 |
| | `compare_periods` | 时期对比分析（周环比/月环比） |
| | `generate_summary_report` | 生成每日/每周摘要报告 |
| **系统** | `get_current_config` | 获取当前系统配置 |
| | `get_system_status` | 获取系统运行状态 |
| | `check_version` | 检查版本更新（TrendRadar + MCP Server） |
| | `trigger_crawl` | 手动触发一次爬取任务 |
| **存储** | `sync_from_remote` | 从远程存储拉取数据到本地 |
| | `get_storage_status` | 获取存储配置和状态 |
| | `list_available_dates` | 列出本地/远程可用的日期 |
| **文章** | `read_article` | 读取单篇文章内容（Markdown 格式） |
| | `read_articles_batch` | 批量读取多篇文章（最多 5 篇） |
| **通知** | `get_notification_channels` | 获取所有已配置的通知渠道及其状态 |
| | `send_notification` | 向已配置的通知渠道发送消息（自动格式转换） |

---

## ⚙️ 默认设置说明（重要！）

默认采用以下优化策略，主要是为了节约 AI token 消耗：

| 默认设置       | 说明                                    | 如何调整                              |
| -------------- | --------------------------------------- | ------------------------------------- |
| **限制条数**   | 默认返回 50 条新闻                      | 对话中说"返回前 10 条"或"给我 100 条" |
| **时间范围**   | 默认查询今天的数据                      | 说"查询昨天"、"最近一周"或"1月1日到7日" |
| **URL 链接**   | 默认不返回链接（节省约 160 tokens/条）  | 说"需要链接"或"包含 URL"              |
| **关键词列表** | 默认不使用 frequency_words.txt 过滤新闻 | 只有调用"趋势话题"工具时才使用        |

**⚠️ 重要：** AI 模型的选择直接影响工具调用效果，AI 越智能，调用越准确。当你解除上面的限制，比如从今天的查询，放宽到一周的查询，首先你要在本地有一周的数据，其次，token 消耗量可能会倍增。

**💡 提示：** 本项目提供了专门的日期解析工具，可以准确解析"最近7天"、"本周"等自然语言日期表达式，确保所有 AI 模型获得一致的日期范围。详见下方 Q18。


## 💰 AI 模型

下面我以 **[硅基流动](https://cloud.siliconflow.cn)** 平台作为例子，里面有很多大模型可选择。在开发和测试本项目的过程中，我使用本平台进行了许多的功能测试和验证。

### 📊 注册方式对比

| 注册方式 | 无邀请链接直接注册 | 含有邀请链接注册  |
|:-------:|:-------:|:-----------------:|
| 注册链接 | [siliconflow.cn](https://cloud.siliconflow.cn) | [邀请链接](https://cloud.siliconflow.cn/i/fqnyVaIU) |
| 免费额度 | 0 tokens | **2000万 tokens** (≈14元) |
| 额外福利 | ❌ | ✅ 邀请者也获得2000万tokens |

> 💡 **提示**：上面的赠送额度，应该可以询问 **200次以上**


### 🚀 快速开始

#### 1️⃣ 注册并获取 API 密钥

1. 使用上方链接完成注册
2. 访问 [API 密钥管理页面](https://cloud.siliconflow.cn/me/account/ak)
3. 点击「新建 API 密钥」
4. 复制生成的密钥（请妥善保管）

#### 2️⃣ 在 Cherry Studio 中配置

1. 打开 **Cherry Studio**
2. 进入「模型服务」设置
3. 找到「硅基流动」
4. 将复制的密钥粘贴到 **[API密钥]** 输入框
5. 确保右上角勾选框打开后显示为 **绿色** ✅

---

### ✨ 配置完成！

现在你可以开始使用本项目，享受稳定快速的 AI 服务了！

在你测试一次询问后，请立刻去 [硅基流动账单](https://cloud.siliconflow.cn/me/bills) 查询这一次的消耗量，心底有个估算。


---

## 基础查询

### Q1: 如何查看最新的新闻？

**你可以这样问：**

- "给我看看最新的新闻"
- "查询今天的热点新闻"
- "获取知乎和微博的最新 10 条新闻"
- "查看最新新闻，需要包含链接"

**工具返回行为：**

- 工具会返回所有平台的最新 50 条新闻
- 默认不包含 URL 链接（节省 token）

**AI 展示行为（重要）：**

- ⚠️ **AI 通常会自动总结**，只展示部分新闻（如 TOP 10-20 条）
- ✅ 如果你想看全部 50 条，需要明确要求："展示所有新闻"或"完整列出所有 50 条"
- 💡 这是 AI 模型的自然行为，不是工具的限制

**可以调整：**

- 指定平台：如"只看知乎的"
- 调整数量：如"返回前 20 条"
- 包含链接：如"需要链接"
- **要求完整展示**：如"展示全部，不要总结"

---

### Q2: 如何查询特定日期的新闻？

**你可以这样问：**

- "查询昨天的新闻"
- "看看 3 天前知乎的新闻"
- "2025-10-10 的新闻有哪些"
- "上周一的新闻"
- "给我看看最新新闻"（自动查询今天）

**支持的日期格式：**

- 相对日期：今天、昨天、前天、3 天前
- 星期：上周一、本周三、last monday
- 绝对日期：2025-10-10、10 月 10 日

**工具返回行为：**

- 不指定日期时自动查询今天（节省 token）
- 工具会返回所有平台的 50 条新闻
- 默认不包含 URL 链接

**AI 展示行为（重要）：**

- ⚠️ **AI 通常会自动总结**，只展示部分新闻（如 TOP 10-20 条）
- ✅ 如果你想看全部，需要明确要求："展示所有新闻，不要总结"

---

### Q3: 如何查看热点话题统计？

**你可以这样问：**

- "我关注的词今天出现了多少次"（使用预设关注词）
- "自动分析今天新闻里有哪些热门话题"（自动提取）
- "看看新闻里最热门的词是什么"（自动提取）

**两种提取模式：**

| 模式 | 说明 | 示例问法 |
|------|------|---------|
| **预设关注词** | 统计你预先设定的关注词（基于配置文件，默认） | "我的关注词出现了多少次" |
| **自动提取** | 自动从新闻标题提取高频词（无需预设） | "自动分析热门话题" |

---

## RSS 订阅查询

### Q4.1: 如何查看最新的 RSS 订阅内容？

**你可以这样问：**

- "查看最新的 RSS 订阅内容"
- "获取 Hacker News 的最新文章"
- "查看所有 RSS 源的最新 20 条"
- "获取 RSS 订阅，需要包含摘要"
- "看看最近一周的 RSS 内容"（支持多日查询）
- "获取 Hacker News 最近 7 天的文章"

**工具返回行为：**

- 默认返回今天的 RSS 条目（最多 50 条）
- 支持 `days` 参数获取多日数据（1-30天）
- 默认不包含摘要（节省 token）
- 按发布时间倒序排列
- 跨日期自动去重（按 URL）

**AI 展示行为（重要）：**

- ⚠️ **AI 通常会自动总结**，只展示部分条目
- ✅ 如果你想看全部，需要明确要求："展示所有 RSS 内容"

**可以调整：**

- 指定 RSS 源：如"只看 Hacker News"
- 指定天数：如"最近 7 天"、"最近一周"
- 调整数量：如"返回前 20 条"
- 包含摘要：如"需要摘要"

---

### Q4.2: 如何搜索 RSS 订阅中的内容？

**你可以这样问：**

- "在 RSS 中搜索'AI'相关的文章"
- "搜索最近 7 天 RSS 中关于'机器学习'的内容"
- "在 Hacker News 中搜索'Python'"

**工具返回行为：**

- 使用关键词搜索 RSS 条目的标题
- 默认搜索最近 7 天的数据
- 工具会返回最多 50 条结果

**可以调整：**

- 指定 RSS 源：如"只搜索 Hacker News"
- 调整天数：如"搜索最近 14 天"
- 包含摘要：如"需要摘要"

---

### Q4.3: 如何查看 RSS 源的状态？

**你可以这样问：**

- "查看 RSS 源状态"
- "RSS 抓取了多少数据"
- "哪些 RSS 源有数据"

**返回信息：**

| 字段 | 说明 |
|------|------|
| **可用日期** | 有 RSS 数据的日期列表 |
| **总日期数** | 总共有多少天的数据 |
| **今日各源统计** | 今日各 RSS 源的数据统计 |
| **生成时间** | 状态生成时间 |

---

## 搜索检索

### Q4: 如何搜索包含特定关键词的新闻？

**你可以这样问：**

- "搜索包含'人工智能'的新闻"
- "查找关于'特斯拉降价'的报道"
- "搜索马斯克相关的新闻，返回前 20 条"
- "查找最近7天关于'iPhone 16'的新闻"
- "查找2025年1月1日到7日'特斯拉'的相关新闻"
- "查找'iPhone 16 发布'这条新闻的链接"

**工具返回行为：**

- 使用关键词模式搜索
- 默认搜索今天的数据
- AI会自动将"最近7天"、"上周"等相对时间转换为具体日期范围
- 工具会返回最多 50 条结果
- 默认不包含 URL 链接

**AI 展示行为（重要）：**

- ⚠️ **AI 通常会自动总结**，只展示部分搜索结果
- ✅ 如果你想看全部，需要明确要求："展示所有搜索结果"

**可以调整：**

- 指定时间范围：
  - 相对方式："搜索最近一周的"（AI 自动计算日期）
  - 绝对日期："搜索2025年1月1日到7日的"
- 指定平台：如"只搜索知乎"
- 调整排序：如"按权重排序"
- 包含链接：如"需要链接"

---

### Q4.4: 如何同时搜索热榜和 RSS 内容？

**你可以这样问：**

- "搜索'AI'相关内容，包括 RSS"
- "查找'人工智能'的新闻，同时搜索 RSS 订阅"
- "搜索'特斯拉'，热榜和 RSS 都要"

**工具返回行为：**

- 热榜结果和 RSS 结果**分开展示**
- 热榜按排名/相关度排序，RSS 按发布时间排序
- RSS 结果不影响热榜的排名展示
- 默认返回热榜 50 条 + RSS 20 条

**可以调整：**

- RSS 数量：如"RSS 返回 10 条"
- 只搜索热榜：不说"包括 RSS"（默认行为）
- 只搜索 RSS：说"只在 RSS 中搜索"

---

### Q5: 如何查找相关新闻？

**你可以这样问：**

- "找出和'特斯拉降价'相似的新闻"（今天）
- "查找昨天与'人工智能突破'相关的新闻"（历史）
- "搜索上周关于'ChatGPT
