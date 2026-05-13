# Missing Repo Summary Source: NanmiCoder/MediaCrawler

- URL: https://github.com/NanmiCoder/MediaCrawler
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/NanmiCoder__MediaCrawler
- Clone Status: cloned
- Language: Python
- Stars: 49499
- Topics: 
- Description: 小红书笔记 | 评论爬虫、抖音视频 | 评论爬虫、快手视频 | 评论爬虫、B 站视频 ｜ 评论爬虫、微博帖子 ｜ 评论爬虫、百度贴吧帖子 ｜ 百度贴吧评论回复爬虫  | 知乎问答文章｜评论爬虫

## Extracted README / Docs / Examples



# FILE: README.md

# 🔥 MediaCrawler - 自媒体平台爬虫 🕷️

<div align="center">

<a href="https://trendshift.io/repositories/8291" target="_blank">
  <img src="https://trendshift.io/api/badge/repositories/8291" alt="NanmiCoder%2FMediaCrawler | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
</a>

[![GitHub Stars](https://img.shields.io/github/stars/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/pulls)
[![License](https://img.shields.io/github/license/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/blob/main/LICENSE)
[![中文](https://img.shields.io/badge/🇨🇳_中文-当前-blue)](README.md)
[![English](https://img.shields.io/badge/🇺🇸_English-Available-green)](README_en.md)
[![Español](https://img.shields.io/badge/🇪🇸_Español-Available-green)](README_es.md)
</div>



> **免责声明：**
> 
> 大家请以学习为目的使用本仓库⚠️⚠️⚠️⚠️，[爬虫违法违规的案件](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)  <br>
>
>本仓库的所有内容仅供学习和参考之用，禁止用于商业用途。任何人或组织不得将本仓库的内容用于非法用途或侵犯他人合法权益。本仓库所涉及的爬虫技术仅用于学习和研究，不得用于对其他平台进行大规模爬虫或其他非法行为。对于因使用本仓库内容而引起的任何法律责任，本仓库不承担任何责任。使用本仓库的内容即表示您同意本免责声明的所有条款和条件。
>
> 点击查看更为详细的免责声明。[点击跳转](#disclaimer)




## 📖 项目简介

一个功能强大的**多平台自媒体数据采集工具**，支持小红书、抖音、快手、B站、微博、贴吧、知乎等主流平台的公开信息抓取。

### 🔧 技术原理

- **核心技术**：基于 [Playwright](https://playwright.dev/) 浏览器自动化框架登录保存登录态
- **无需JS逆向**：利用保留登录态的浏览器上下文环境，通过 JS 表达式获取签名参数
- **优势特点**：无需逆向复杂的加密算法，大幅降低技术门槛


## ✨ 功能特性
| 平台   | 关键词搜索 | 指定帖子ID爬取 | 二级评论 | 指定创作者主页 | 登录态缓存 | IP代理池 | 生成评论词云图 |
| ------ | ---------- | -------------- | -------- | -------------- | ---------- | -------- | -------------- |
| 小红书 | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| 抖音   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| 快手   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| B 站   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| 微博   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| 贴吧   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| 知乎   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |



<strong>MediaCrawlerPro 重磅发布！开源不易，欢迎订阅支持</strong>

> 专注于学习成熟项目的架构设计，不仅仅是爬虫技术，Pro 版本的代码设计思路同样值得深入学习！

[MediaCrawlerPro](https://github.com/MediaCrawlerPro) 相较于开源版本的核心优势：

#### 🎯 核心功能升级
- ✅ **自媒体内容拆解Agent**（新增功能）
- ✅ **断点续爬功能**（重点特性）
- ✅ **多账号 + IP代理池支持**（重点特性）
- ✅ **去除 Playwright 依赖**，使用更简单
- ✅ **完整 Linux 环境支持**

#### 🏗️ 架构设计优化
- ✅ **代码重构优化**，更易读易维护（解耦 JS 签名逻辑）
- ✅ **企业级代码质量**，适合构建大型爬虫项目
- ✅ **完美架构设计**，高扩展性，源码学习价值更大

#### 🎁 额外功能
- ✅ **自媒体视频下载器桌面端**（适合学习全栈开发）
- ✅ **多平台首页信息流推荐**（HomeFeed）
- ✅ **AI Agent Skill 支持**（[OpenClaw](https://openclaw.ai/) 🦞 / Claude Code / Cursor 一键安装，让 Agent 自动爬取数据）
- [ ] **基于评论分析AI Agent正在开发中 🚀🚀**

点击查看：[MediaCrawlerPro 项目主页](https://github.com/MediaCrawlerPro) 更多介绍



## 🚀 快速开始

> 💡 **如果这个项目对您有帮助，请给个 ⭐ Star 支持一下！**

## 📋 前置依赖

### 🚀 uv 安装（推荐）

在进行下一步操作之前，请确保电脑上已经安装了 uv：

- **安装地址**：[uv 官方安装指南](https://docs.astral.sh/uv/getting-started/installation)
- **验证安装**：终端输入命令 `uv --version`，如果正常显示版本号，证明已经安装成功
- **推荐理由**：uv 是目前最强的 Python 包管理工具，速度快、依赖解析准确

### 🟢 Node.js 安装

项目依赖 Node.js，请前往官网下载安装：

- **下载地址**：https://nodejs.org/en/download/
- **版本要求**：>= 16.0.0

### 📦 Python 包安装

```shell
# 进入项目目录
cd MediaCrawler

# 使用 uv sync 命令来保证 python 版本和相关依赖包的一致性
uv sync
```

### 🌐 浏览器驱动安装（可选）

> 如果使用默认的 CDP 模式（连接已有 Chrome 浏览器），**无需安装浏览器驱动**。仅在使用标准 Playwright 模式时需要安装。

```shell
# 仅在标准 Playwright 模式下需要安装浏览器驱动
uv run playwright install
```

### 🌍 Chrome 浏览器配置（推荐）

项目默认使用 CDP 模式连接用户已有的 Chrome 浏览器，可以复用浏览器已有的登录状态、Cookie、扩展等，**大幅降低平台风控检测风险**。

使用前需要：

1. **安装最新版 Chrome 浏览器**（版本 >= 144），[下载地址](https://www.google.com/chrome/)
2. **开启远程调试功能**：在 Chrome 地址栏输入 `chrome://inspect/#remote-debugging`，勾选 **"Allow remote debugging for this browser instance"**
3. 页面显示 `Server running at: 127.0.0.1:9222` 表示已就绪

> 💡 **提示**：运行爬虫后，Chrome 浏览器会弹出确认对话框，点击"接受"即可。程序会等待用户确认，60秒内操作完成即可。
>
> 如果不想使用 CDP 模式，可以在 `config/base_config.py` 中设置 `ENABLE_CDP_MODE = False` 切换为标准 Playwright 模式。

## 🚀 运行爬虫程序

```shell
# 在 config/base_config.py 查看配置项目功能，写的有中文注释

# 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
uv run main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例，执行下面的命令查看
uv run main.py --help
```

<details>
<summary>🖥️ <strong>WebUI 可视化操作界面</strong></summary>

MediaCrawler 提供了基于 Web 的可视化操作界面，无需命令行也能轻松使用爬虫功能。

#### 启动 WebUI 服务

```shell
# 启动 API 服务器（默认端口 8080）
uv run uvicorn api.main:app --port 8080 --reload

# 或者使用模块方式启动
uv run python -m api.main
```

启动成功后，访问 `http://localhost:8080` 即可打开 WebUI 界面。

#### WebUI 功能特性

- 可视化配置爬虫参数（平台、登录方式、爬取类型等）
- 实时查看爬虫运行状态和日志
- 数据预览和导出

#### 界面预览

<img src="docs/static/images/img_8.png" alt="WebUI 界面预览">

</details>

<details>
<summary>🔗 <strong>使用 Python 原生 venv 管理环境（不推荐）</strong></summary>

#### 创建并激活 Python 虚拟环境

> 如果是爬取抖音和知乎，需要提前安装 nodejs 环境，版本大于等于：`16` 即可

```shell
# 进入项目根目录
cd MediaCrawler

# 创建虚拟环境
# 我的 python 版本是：3.11 requirements.txt 中的库是基于这个版本的
# 如果是其他 python 版本，可能 requirements.txt 中的库不兼容，需自行解决
python -m venv venv

# macOS & Linux 激活虚拟环境
source venv/bin/activate

# Windows 激活虚拟环境
venv\Scripts\activate
```

#### 安装依赖库

```shell
pip install -r requirements.txt
```

#### 安装 playwright 浏览器驱动

```shell
playwright install
```

#### 运行爬虫程序（原生环境）

```shell
# 项目默认是没有开启评论爬取模式，如需评论请在 config/base_config.py 中的 ENABLE_GET_COMMENTS 变量修改
# 一些其他支持项，也可以在 config/base_config.py 查看功能，写的有中文注释

# 从配置文件中读取关键词搜索相关的帖子并爬取帖子信息与评论
python main.py --platform xhs --lt qrcode --type search

# 从配置文件中读取指定的帖子ID列表获取指定帖子的信息与评论信息
python main.py --platform xhs --lt qrcode --type detail

# 打开对应APP扫二维码登录

# 其他平台爬虫使用示例，执行下面的命令查看
python main.py --help
```

</details>


## 💾 数据保存

MediaCrawler 支持多种数据存储方式，包括 CSV、JSON、JSONL、Excel、SQLite 和 MySQL 数据库。

📖 **详细使用说明请查看：[数据存储指南](docs/data_storage_guide.md)**


[🚀 MediaCrawlerPro 重磅发布 🚀！更多的功能，更好的架构设计！开源不易，欢迎订阅支持！](https://github.com/MediaCrawlerPro)


## 💬 交流群组
- **微信交流群**：[点击加入](https://nanmicoder.github.io/MediaCrawler/%E5%BE%AE%E4%BF%A1%E4%BA%A4%E6%B5%81%E7%BE%A4.html)
- **B站账号**：[关注我](https://space.bilibili.com/434377496)，分享AI与爬虫技术知识


## 💰 赞助商展示

<a href="https://tikhub.io/?utm_source=github.com/NanmiCoder/MediaCrawler&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad">
<img width="500" src="docs/static/images/tikhub_banner_zh.png">
<br>
TikHub.io 提供 900+ 高稳定性数据接口，覆盖 TK、DY、XHS、Y2B、Ins、X 等 14+ 海内外主流平台，支持用户、内容、商品、评论等多维度公开数据 API，并配套 4000 万+ 已清洗结构化数据集，使用邀请码 <code>cfzyejV9</code> 注册并充值，即可额外获得 $2 赠送额度。
</a>

<br>
<br>

<a href="https://legionproxy.io/?utm_source=github&utm_campaign=mediacrawler">
<img width="420" src="docs/static/images/legionproxy_banner.jpg" alt="LegionProxy residential proxy sponsor banner">
<br>
LegionProxy 专为账号注册与自动化场景提供住宅代理网络，覆盖 74M+ 真实住宅 IP、195+ 国家，支持 HTTP/3 高速连接，价格 $0.60/GB 起。
</a>

---

## 🤝 成为赞助者

成为赞助者，可以将您的产品展示在这里，每天获得大量曝光！

**联系方式**：
- 微信：`relakkes`
- 邮箱：`relakkes@gmail.com`
---

## ☕ 请作者喝杯咖啡

如果这个项目对您有帮助，欢迎打赏支持，您的每一份支持都是我持续更新的动力 ❤️

<table>
<tr>
<td align="center" width="33%">
<img src="docs/static/images/wechat_pay.jpeg" width="250" alt="微信赞赏"><br>
<b>微信赞赏</b>
</td>
<td align="center" width="33%">
<img src="docs/static/images/zfb_pay.png" width="250" alt="支付宝"><br>
<b>支付宝</b>
</td>
<td align="center" width="33%">
<a href="https://buymeacoffee.com/relakkes" target="_blank">
<img src="docs/static/images/bmc_button.png" width="250" alt="Buy Me a Coffee">
</a><br>
<b>Buy Me a Coffee</b>
</td>
</tr>
</table>

---

## 📚 其他
- **常见问题**：[MediaCrawler 完整文档](https://nanmicoder.github.io/MediaCrawler/)
- **爬虫入门教程**：[CrawlerTutorial 免费教程](https://github.com/NanmiCoder/CrawlerTutorial)
- **新闻爬虫开源项目**：[NewsCrawlerCollection](https://github.com/NanmiCoder/NewsCrawlerCollection)


## ⭐ Star 趋势图

如果这个项目对您有帮助，请给个 ⭐ Star 支持一下，让更多的人看到 MediaCrawler！

[![Star History Chart](https://api.star-history.com/svg?repos=NanmiCoder/MediaCrawler&type=Date)](https://star-history.com/#NanmiCoder/MediaCrawler&Date)


## 📚 参考

- **小红书签名仓库**：[Cloxl 的 xhs 签名仓库](https://github.com/Cloxl/xhshow)
- **小红书客户端**：[ReaJason 的 xhs 仓库](https://github.com/ReaJason/xhs)
- **短信转发**：[SmsForwarder 参考仓库](https://github.com/pppscn/SmsForwarder)
- **内网穿透工具**：[ngrok 官方文档](https://ngrok.com/docs/)


# 免责声明
<div id="disclaimer"> 

## 1. 项目目的与性质
本项目（以下简称“本项目”）是作为一个技术研究与学习工具而创建的，旨在探索和学习网络数据采集技术。本项目专注于自媒体平台的数据爬取技术研究，旨在提供给学习者和研究者作为技术交流之用。

## 2. 法律合规性声明
本项目开发者（以下简称“开发者”）郑重提醒用户在下载、安装和使用本项目时，严格遵守中华人民共和国相关法律法规，包括但不限于《中华人民共和国网络安全法》、《中华人民共和国反间谍法》等所有适用的国家法律和政策。用户应自行承担一切因使用本项目而可能引起的法律责任。

## 3. 使用目的限制
本项目严禁用于任何非法目的或非学习、非研究的商业行为。本项目不得用于任何形式的非法侵入他人计算机系统，不得用于任何侵犯他人知识产权或其他合法权益的行为。用户应保证其使用本项目的目的纯属个人学习和技术研究，不得用于任何形式的非法活动。

## 4. 免责声明
开发者已尽最大努力确保本项目的正当性及安全性，但不对用户使用本项目可能引起的任何形式的直接或间接损失承担责任。包括但不限于由于使用本项目而导致的任何数据丢失、设备损坏、法律诉讼等。

## 5. 知识产权声明
本项目的知识产权归开发者所有。本项目受到著作权法和国际著作权条约以及其他知识产权法律和条约的保护。用户在遵守本声明及相关法律法规的前提下，可以下载和使用本项目。

## 6. 最终解释权
关于本项目的最终解释权归开发者所有。开发者保留随时更改或更新本免责声明的权利，恕不另行通知。
</div>


# FILE: README_es.md

# 🔥 MediaCrawler - Rastreador de Plataformas de Redes Sociales 🕷️

<div align="center">

<a href="https://trendshift.io/repositories/8291" target="_blank">
  <img src="https://trendshift.io/api/badge/repositories/8291" alt="NanmiCoder%2FMediaCrawler | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
</a>

[![GitHub Stars](https://img.shields.io/github/stars/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/pulls)
[![License](https://img.shields.io/github/license/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/blob/main/LICENSE)
[![中文](https://img.shields.io/badge/🇨🇳_中文-Available-blue)](README.md)
[![English](https://img.shields.io/badge/🇺🇸_English-Available-green)](README_en.md)
[![Español](https://img.shields.io/badge/🇪🇸_Español-Current-green)](README_es.md)

</div>

> **Descargo de responsabilidad:**
> 
> Por favor, utilice este repositorio únicamente con fines de aprendizaje ⚠️⚠️⚠️⚠️, [Casos ilegales de web scraping](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)  <br>
>
>Todo el contenido de este repositorio es únicamente para fines de aprendizaje y referencia, y está prohibido el uso comercial. Ninguna persona u organización puede usar el contenido de este repositorio para propósitos ilegales o infringir los derechos e intereses legítimos de otros. La tecnología de web scraping involucrada en este repositorio es solo para aprendizaje e investigación, y no puede ser utilizada para rastreo a gran escala de otras plataformas u otras actividades ilegales. Este repositorio no asume ninguna responsabilidad legal por cualquier responsabilidad legal que surja del uso del contenido de este repositorio. Al usar el contenido de este repositorio, usted acepta todos los términos y condiciones de este descargo de responsabilidad.
>
> Haga clic para ver un descargo de responsabilidad más detallado. [Haga clic para saltar](#disclaimer)

## 📖 Introducción del Proyecto

Una poderosa **herramienta de recolección de datos de redes sociales multiplataforma** que soporta el rastreo de información pública de plataformas principales incluyendo Xiaohongshu, Douyin, Kuaishou, Bilibili, Weibo, Tieba, Zhihu, y más.

### 🔧 Principios Técnicos

- **Tecnología Central**: Basado en el framework de automatización de navegador [Playwright](https://playwright.dev/) para login y mantenimiento del estado de login
- **No Requiere Ingeniería Inversa de JS**: Utiliza el entorno de contexto del navegador con estado de login preservado para obtener parámetros de firma a través de expresiones JS
- **Ventajas**: No necesita hacer ingeniería inversa de algoritmos de encriptación complejos, reduciendo significativamente la barrera técnica

## ✨ Características
| Plataforma | Búsqueda por Palabras Clave | Rastreo de ID de Publicación Específica | Comentarios Secundarios | Página de Inicio de Creador Específico | Caché de Estado de Login | Pool de Proxy IP | Generar Nube de Palabras de Comentarios |
| ------ | ---------- | -------------- | -------- | -------------- | ---------- | -------- | -------------- |
| Xiaohongshu | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Douyin   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Kuaishou   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Bilibili   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Weibo   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Tieba   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Zhihu   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |


<strong>¡Lanzamiento Mayor de MediaCrawlerPro! ¡El código abierto no es fácil, bienvenido a suscribirse y apoyar!</strong>

> Enfócate en aprender el diseño arquitectónico de proyectos maduros, no solo tecnología de rastreo. ¡La filosofía de diseño de código de la versión Pro también vale la pena estudiar en profundidad!

[MediaCrawlerPro](https://github.com/MediaCrawlerPro) ventajas principales sobre la versión de código abierto:

#### 🎯 Actualizaciones de Características Principales
- ✅ **Agente de Deconstrucción de Contenido** (Nueva función)
- ✅ **Funcionalidad de reanudación de rastreo** (Característica clave)
- ✅ **Soporte de múltiples cuentas + pool de proxy IP** (Característica clave)
- ✅ **Eliminar dependencia de Playwright**, más fácil de usar
- ✅ **Soporte completo de entorno Linux**

#### 🏗️ Optimización de Diseño Arquitectónico
- ✅ **Optimización de refactorización de código**, más legible y mantenible (lógica de firma JS desacoplada)
- ✅ **Calidad de código de nivel empresarial**, adecuado para construir proyectos de rastreo a gran escala
- ✅ **Diseño arquitectónico perfecto**, alta escalabilidad, mayor valor de aprendizaje del código fuente

#### 🎁 Características Adicionales
- ✅ **Aplicación de escritorio descargadora de videos de redes sociales** (adecuada para aprender desarrollo full-stack)
- ✅ **Recomendaciones de feed de página de inicio multiplataforma** (HomeFeed)
- [ ] **Agente AI basado en análisis de comentarios está en desarrollo 🚀🚀**

Haga clic para ver: [Página de Inicio del Proyecto MediaCrawlerPro](https://github.com/MediaCrawlerPro) para más información

## 🚀 Inicio Rápido

> 💡 **¡El código abierto no es fácil, si este proyecto te ayuda, por favor da una ⭐ Estrella para apoyar!**

## 📋 Prerrequisitos

### 🚀 Instalación de uv (Recomendado)

Antes de proceder con los siguientes pasos, por favor asegúrese de que uv esté instalado en su computadora:

- **Guía de Instalación**: [Guía Oficial de Instalación de uv](https://docs.astral.sh/uv/getting-started/installation)
- **Verificar Instalación**: Ingrese el comando `uv --version` en la terminal. Si el número de versión se muestra normalmente, la instalación fue exitosa
- **Razón de Recomendación**: uv es actualmente la herramienta de gestión de paquetes Python más poderosa, con velocidad rápida y resolución de dependencias precisa

### 🟢 Instalación de Node.js

El proyecto depende de Node.js, por favor descargue e instale desde el sitio web oficial:

- **Enlace de Descarga**: https://nodejs.org/en/download/
- **Requisito de Versión**: >= 16.0.0

### 📦 Instalación de Paquetes Python

```shell
# Entrar al directorio del proyecto
cd MediaCrawler

# Usar el comando uv sync para asegurar la consistencia de la versión de python y paquetes de dependencias relacionados
uv sync
```

### 🌐 Instalación de Controlador de Navegador

```shell
# Instalar controlador de navegador
uv run playwright install
```

> **💡 Consejo**: MediaCrawler ahora soporta usar playwright para conectarse a su navegador Chrome local, resolviendo algunos problemas causados por Webdriver.
>
> Actualmente, `xhs` y `dy` están disponibles usando el modo CDP para conectarse a navegadores locales. Si es necesario, verifique los elementos de configuración en `config/base_config.py`.

## 🚀 Ejecutar Programa Rastreador

```shell
# El proyecto no habilita el modo de rastreo de comentarios por defecto. Si necesita comentarios, por favor modifique la variable ENABLE_GET_COMMENTS en config/base_config.py
# Otras opciones soportadas también pueden verse en config/base_config.py con comentarios en chino

# Leer palabras clave del archivo de configuración para buscar publicaciones relacionadas y rastrear información de publicaciones y comentarios
uv run main.py --platform xhs --lt qrcode --type search

# Leer lista de ID de publicaciones específicas del archivo de configuración para obtener información e información de comentarios de publicaciones específicas
uv run main.py --platform xhs --lt qrcode --type detail

# Abrir la APP correspondiente para escanear código QR para login

# Para ejemplos de uso de rastreador de otras plataformas, ejecute el siguiente comando para ver
uv run main.py --help
```

## Soporte WebUI

<details>
<summary>🖥️ <strong>Interfaz de Operación Visual WebUI</strong></summary>

MediaCrawler proporciona una interfaz de operación visual basada en web, permitiéndole usar fácilmente las funciones del rastreador sin línea de comandos.

#### Iniciar Servicio WebUI

```shell
# Iniciar servidor API (puerto predeterminado 8080)
uv run uvicorn api.main:app --port 8080 --reload

# O iniciar usando método de módulo
uv run python -m api.main
```

Después de iniciar exitosamente, visite `http://localhost:8080` para abrir la interfaz WebUI.

#### Características de WebUI

- Configuración visual de parámetros del rastreador (plataforma, método de login, tipo de rastreo, etc.)
- Vista en tiempo real del estado de ejecución del rastreador y logs
- Vista previa y exportación de datos

#### Vista Previa de la Interfaz

<img src="docs/static/images/img_8.png" alt="Vista Previa de Interfaz WebUI">

</details>

<details>
<summary>🔗 <strong>Usando gestión de entorno venv nativo de Python (No recomendado)</strong></summary>

#### Crear y activar entorno virtual de Python

> Si rastrea Douyin y Zhihu, necesita instalar el entorno nodejs con anticipación, versión mayor o igual a: `16`

```shell
# Entrar al directorio raíz del proyecto
cd MediaCrawler

# Crear entorno virtual
# Mi versión de python es: 3.9.6, las librerías en requirements.txt están basadas en esta versión
# Si usa otras versiones de python, las librerías en requireme

# FILE: README_en.md

# 🔥 MediaCrawler - Social Media Platform Crawler 🕷️

<div align="center">

<a href="https://trendshift.io/repositories/8291" target="_blank">
  <img src="https://trendshift.io/api/badge/repositories/8291" alt="NanmiCoder%2FMediaCrawler | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
</a>

[![GitHub Stars](https://img.shields.io/github/stars/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/NanmiCoder/MediaCrawler?style=social)](https://github.com/NanmiCoder/MediaCrawler/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/pulls)
[![License](https://img.shields.io/github/license/NanmiCoder/MediaCrawler)](https://github.com/NanmiCoder/MediaCrawler/blob/main/LICENSE)
[![中文](https://img.shields.io/badge/🇨🇳_中文-Available-blue)](README.md)
[![English](https://img.shields.io/badge/🇺🇸_English-Current-green)](README_en.md)
[![Español](https://img.shields.io/badge/🇪🇸_Español-Available-green)](README_es.md)

</div>

> **Disclaimer:**
> 
> Please use this repository for learning purposes only ⚠️⚠️⚠️⚠️, [Web scraping illegal cases](https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China)  <br>
>
>All content in this repository is for learning and reference purposes only, and commercial use is prohibited. No person or organization may use the content of this repository for illegal purposes or infringe upon the legitimate rights and interests of others. The web scraping technology involved in this repository is only for learning and research, and may not be used for large-scale crawling of other platforms or other illegal activities. This repository assumes no legal responsibility for any legal liability arising from the use of the content of this repository. By using the content of this repository, you agree to all terms and conditions of this disclaimer.
>
> Click to view a more detailed disclaimer. [Click to jump](#disclaimer)

## 📖 Project Introduction

A powerful **multi-platform social media data collection tool** that supports crawling public information from mainstream platforms including Xiaohongshu, Douyin, Kuaishou, Bilibili, Weibo, Tieba, Zhihu, and more.

### 🔧 Technical Principles

- **Core Technology**: Based on [Playwright](https://playwright.dev/) browser automation framework for login and maintaining login state
- **No JS Reverse Engineering Required**: Uses browser context environment with preserved login state to obtain signature parameters through JS expressions
- **Advantages**: No need to reverse complex encryption algorithms, significantly lowering the technical barrier

## ✨ Features
| Platform | Keyword Search | Specific Post ID Crawling | Secondary Comments | Specific Creator Homepage | Login State Cache | IP Proxy Pool | Generate Comment Word Cloud |
| ------ | ---------- | -------------- | -------- | -------------- | ---------- | -------- | -------------- |
| Xiaohongshu | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Douyin   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Kuaishou   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Bilibili   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Weibo   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Tieba   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |
| Zhihu   | ✅          | ✅              | ✅        | ✅              | ✅          | ✅        | ✅              |


<strong>MediaCrawlerPro Major Release! Open source is not easy, welcome to subscribe and support!</strong>

> Focus on learning mature project architectural design, not just crawling technology. The code design philosophy of the Pro version is equally worth in-depth study!

[MediaCrawlerPro](https://github.com/MediaCrawlerPro) core advantages over the open-source version:

#### 🎯 Core Feature Upgrades
- ✅ **Content Deconstruction Agent** (New feature)
- ✅ **Resume crawling functionality** (Key feature)
- ✅ **Multi-account + IP proxy pool support** (Key feature)
- ✅ **Remove Playwright dependency**, easier to use
- ✅ **Complete Linux environment support**

#### 🏗️ Architectural Design Optimization
- ✅ **Code refactoring optimization**, more readable and maintainable (decoupled JS signature logic)
- ✅ **Enterprise-level code quality**, suitable for building large-scale crawler projects
- ✅ **Perfect architectural design**, high scalability, greater source code learning value

#### 🎁 Additional Features
- ✅ **Social media video downloader desktop app** (suitable for learning full-stack development)
- ✅ **Multi-platform homepage feed recommendations** (HomeFeed)
- [ ] **AI Agent based on comment analysis is under development 🚀🚀**

Click to view: [MediaCrawlerPro Project Homepage](https://github.com/MediaCrawlerPro) for more information

## 🚀 Quick Start

> 💡 **Open source is not easy, if this project helps you, please give a ⭐ Star to support!**

## 📋 Prerequisites

### 🚀 uv Installation (Recommended)

Before proceeding with the next steps, please ensure that uv is installed on your computer:

- **Installation Guide**: [uv Official Installation Guide](https://docs.astral.sh/uv/getting-started/installation)
- **Verify Installation**: Enter the command `uv --version` in the terminal. If the version number is displayed normally, the installation was successful
- **Recommendation Reason**: uv is currently the most powerful Python package management tool, with fast speed and accurate dependency resolution

### 🟢 Node.js Installation

The project depends on Node.js, please download and install from the official website:

- **Download Link**: https://nodejs.org/en/download/
- **Version Requirement**: >= 16.0.0

### 📦 Python Package Installation

```shell
# Enter project directory
cd MediaCrawler

# Use uv sync command to ensure consistency of python version and related dependency packages
uv sync
```

### 🌐 Browser Driver Installation

```shell
# Install browser driver
uv run playwright install
```

> **💡 Tip**: MediaCrawler now supports using playwright to connect to your local Chrome browser, solving some issues caused by Webdriver.
>
> Currently, `xhs` and `dy` are available using CDP mode to connect to local browsers. If needed, check the configuration items in `config/base_config.py`.

## 🚀 Run Crawler Program

```shell
# The project does not enable comment crawling mode by default. If you need comments, please modify the ENABLE_GET_COMMENTS variable in config/base_config.py
# Other supported options can also be viewed in config/base_config.py with Chinese comments

# Read keywords from configuration file to search related posts and crawl post information and comments
uv run main.py --platform xhs --lt qrcode --type search

# Read specified post ID list from configuration file to get information and comment information of specified posts
uv run main.py --platform xhs --lt qrcode --type detail

# Open corresponding APP to scan QR code for login

# For other platform crawler usage examples, execute the following command to view
uv run main.py --help
```

## WebUI Support

<details>
<summary>🖥️ <strong>WebUI Visual Operation Interface</strong></summary>

MediaCrawler provides a web-based visual operation interface, allowing you to easily use crawler features without command line.

#### Start WebUI Service

```shell
# Start API server (default port 8080)
uv run uvicorn api.main:app --port 8080 --reload

# Or start using module method
uv run python -m api.main
```

After successful startup, visit `http://localhost:8080` to open the WebUI interface.

#### WebUI Features

- Visualize crawler parameter configuration (platform, login method, crawling type, etc.)
- Real-time view of crawler running status and logs
- Data preview and export

#### Interface Preview

<img src="docs/static/images/img_8.png" alt="WebUI Interface Preview">

</details>

<details>
<summary>🔗 <strong>Using Python native venv environment management (Not recommended)</strong></summary>

#### Create and activate Python virtual environment

> If crawling Douyin and Zhihu, you need to install nodejs environment in advance, version greater than or equal to: `16`

```shell
# Enter project root directory
cd MediaCrawler

# Create virtual environment
# My python version is: 3.9.6, the libraries in requirements.txt are based on this version
# If using other python versions, the libraries in requirements.txt may not be compatible, please resolve on your own
python -m venv venv

# macOS & Linux activate virtual environment
source venv/bin/activate

# Windows activate virtual environment
venv\Scripts\activate
```

#### Install dependency libraries

```shell
pip install -r requirements.txt
```

#### Install playwright browser driver

```shell
playwright install
```

#### Run crawler program (native environment)

```shell
# The project does not enable comment crawling mode by default. If you need comments, please modify the ENABLE_GET_COMMENTS variable in config/base_config.py
# Other supported options can also be viewed in config/base_config.py with Chinese comments

# Read keywords from configuration file to search related posts and crawl post information and comments
python main.py --platform xhs --lt qrcode --type search

# Read specified post ID list from configuration file to get information and comment information of specified posts
python main.py --platform xhs --lt qrcode --type detail

# Open corresponding APP to scan QR code for login

# For other platfor

# FILE: docs/项目代码结构.md

# 项目代码结构

```
MediaCrawler
├── base
│   └── base_crawler.py         # 项目的抽象基类
├── cache
│   ├── abs_cache.py            # 缓存抽象基类
│   ├── cache_factory.py        # 缓存工厂
│   ├── local_cache.py          # 本地缓存实现
│   └── redis_cache.py          # Redis缓存实现
├── cmd_arg
│   └── arg.py                  # 命令行参数定义
├── config
│   ├── base_config.py          # 基础配置
│   ├── db_config.py            # 数据库配置
│   └── ...                     # 各平台配置文件
├── constant
│   └── ...                     # 各平台常量定义
├── database
│   ├── db.py                   # 数据库ORM，封装增删改查
│   ├── db_session.py           # 数据库会话管理
│   └── models.py               # 数据库模型定义
├── docs
│   └── ...                     # 项目文档
├── libs
│   ├── douyin.js               # 抖音Sign函数
│   ├── stealth.min.js          # 去除浏览器自动化特征的JS
│   └── zhihu.js                # 知乎Sign函数
├── media_platform
│   ├── bilibili                # B站采集实现
│   ├── douyin                  # 抖音采集实现
│   ├── kuaishou                # 快手采集实现
│   ├── tieba                   # 百度贴吧采集实现
│   ├── weibo                   # 微博采集实现
│   ├── xhs                     # 小红书采集实现
│   └── zhihu                   # 知乎采集实现
├── model
│   ├── m_baidu_tieba.py        # 百度贴吧数据模型
│   ├── m_douyin.py             # 抖音数据模型
│   ├── m_kuaishou.py           # 快手数据模型
│   ├── m_weibo.py              # 微博数据模型
│   ├── m_xiaohongshu.py        # 小红书数据模型
│   └── m_zhihu.py              # 知乎数据模型
├── proxy
│   ├── base_proxy.py           # 代理基类
│   ├── providers               # 代理提供商实现
│   ├── proxy_ip_pool.py        # 代理IP池
│   └── types.py                # 代理类型定义
├── store
│   ├── bilibili                # B站数据存储实现
│   ├── douyin                  # 抖音数据存储实现
│   ├── kuaishou                # 快手数据存储实现
│   ├── tieba                   # 贴吧数据存储实现
│   ├── weibo                   # 微博数据存储实现
│   ├── xhs                     # 小红书数据存储实现
│   └── zhihu                   # 知乎数据存储实现
├── test
│   ├── test_db_sync.py         # 数据库同步测试
│   ├── test_proxy_ip_pool.py   # 代理IP池测试
│   └── ...                     # 其他测试用例
├── tools
│   ├── browser_launcher.py     # 浏览器启动器
│   ├── cdp_browser.py          # CDP浏览器控制
│   ├── crawler_util.py         # 爬虫工具函数
│   ├── utils.py                # 通用工具函数
│   └── ...
├── main.py                     # 程序入口, 支持 --init_db 参数来初始化数据库
├── recv_sms.py                 # 短信转发HTTP SERVER接口
└── var.py                      # 全局上下文变量定义
```

# FILE: docs/词云图使用配置.md

# 关于词云图相关操作

## 1.如何正确调用词云图
> ps:保存格式为json或jsonl文件时，才会生成词云图。其他存储方式添加词云图将在近期添加。

需要修改的配置项（./config/base_config.py）：

```python
# 数据保存类型选项配置,支持多种类型：csv、db、json、jsonl等
#此处需要为json或jsonl格式保存，原因如上
SAVE_DATA_OPTION = "jsonl"  # csv or db or json or jsonl
```

```python
# 是否开启爬评论模式, 默认不开启爬评论
#此处为True，需要爬取评论才可以生成评论的词云图。
ENABLE_GET_COMMENTS = True
```

```python
#词云相关
#是否开启生成评论词云图
#打开词云图功能
ENABLE_GET_WORDCLOUD = True
```

```python
# 添加自定义词语及其分组
#添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    '零几': '年份',  # 将“零几”识别为一个整体
    '高频词': '专业术语'  # 示例自定义词
}
```

```python
#停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"
```

```python
#中文字体文件路径
FONT_PATH= "./docs/STZHONGS.TTF"
```

**相关解释**

- 自定义词组的添加，`xx:yy` 中`xx`为自定义词语，`yy`为`xx`分配词语的组别。`yy`可以随便给任意值。

- 如果需要添加禁用词，请在./docs/hit_stopwords.txt添加禁用词(保证格式正确，一个词语一行)
- `FONT_PATH`为生成词云图中中文字体的格式，默认为宋体。可以自行添加字体文件，修改路径。

## 2.生成词云图的位置

![image-20240627204928601](https://rosyrain.oss-cn-hangzhou.aliyuncs.com/img2/202406272049662.png)

如图，在data文件下的`words文件夹`下，其中json为词频统计文件，png为词云图。原本的评论内容在`jsonl文件夹`（或`json文件夹`）下。

# FILE: docs/data_storage_guide.md

# 数据保存指南 / Data Storage Guide


### 💾 数据保存

MediaCrawler 支持多种数据存储方式，您可以根据需求选择最适合的方案：

#### 存储方式

- **CSV 文件**：支持保存到 CSV 中（`data/` 目录下）
- **JSON 文件**：支持保存到 JSON 中（`data/` 目录下）
- **JSONL 文件**：支持保存到 JSONL 中（`data/` 目录下）— 默认格式，每行一个 JSON 对象，追加写入性能好
- **Excel 文件**：支持保存到格式化的 Excel 文件（`data/` 目录下）✨ 新功能
  - 多工作表支持（内容、评论、创作者）
  - 专业格式化（标题样式、自动列宽、边框）
  - 易于分析和分享
- **数据库存储**
  - 使用参数 `--init_db` 进行数据库初始化（使用`--init_db`时不需要携带其他optional）
  - **SQLite 数据库**：轻量级数据库，无需服务器，适合个人使用（推荐）
    1. 初始化：`--init_db sqlite`
    2. 数据存储：`--save_data_option sqlite`
  - **MySQL 数据库**：支持关系型数据库 MySQL 中保存（需要提前创建数据库）
    1. 初始化：`--init_db mysql`
    2. 数据存储：`--save_data_option db`（db 参数为兼容历史更新保留）
  - **PostgreSQL 数据库**：支持高级关系型数据库 PostgreSQL 中保存（推荐生产环境使用）
    1. 初始化：`--init_db postgres`
    2. 数据存储：`--save_data_option postgres`

#### 使用示例

```shell
# 使用 Excel 存储数据（推荐用于数据分析）✨ 新功能
uv run main.py --platform xhs --lt qrcode --type search --save_data_option excel

# 初始化 SQLite 数据库
uv run main.py --init_db sqlite
# 使用 SQLite 存储数据
uv run main.py --platform xhs --lt qrcode --type search --save_data_option sqlite
```

```shell
# 初始化 MySQL 数据库
uv run main.py --init_db mysql
# 使用 MySQL 存储数据（为适配历史更新，db参数进行沿用）
uv run main.py --platform xhs --lt qrcode --type search --save_data_option db
```

```shell
# 初始化 PostgreSQL 数据库
uv run main.py --init_db postgres
# 使用 PostgreSQL 存储数据
uv run main.py --platform xhs --lt qrcode --type search --save_data_option postgres
```

```shell
# 使用 CSV 存储数据
uv run main.py --platform xhs --lt qrcode --type search --save_data_option csv

# 使用 JSON 存储数据
uv run main.py --platform xhs --lt qrcode --type search --save_data_option json

# 使用 JSONL 存储数据（默认格式，无需指定）
uv run main.py --platform xhs --lt qrcode --type search --save_data_option jsonl
```

#### 详细文档

- **Excel 导出详细指南**：查看 [Excel 导出指南](excel_export_guide.md)
- **数据库配置**：参考 [常见问题](常见问题.md)

---


# FILE: docs/mediacrawlerpro订阅.md

# 订阅MediaCrawlerPro版本源码访问权限

## 获取Pro版本的访问权限
> MediaCrawler开源超过一年了，相信该仓库帮过不少朋友低门槛的学习和了解爬虫。维护真的耗费了大量精力和人力 <br>
> 
> 所以Pro版本不会开源，可以订阅Pro版本让我更加有动力去更新。<br>
> 
> 如果感兴趣可以加我微信，订阅Pro版本访问权限哦，有门槛💰。<br>
> 
> 仅针对想学习Pro版本源码实现的用户，如果是公司或者商业化盈利性质的就不要加我了，谢谢🙏
> 
> 代码设计拓展性强，可以自己扩展更多的爬虫平台，更多的数据存储方式，相信对你架构这种爬虫代码有所帮助。
> 
> 
> **MediaCrawlerPro项目主页地址**
> [MediaCrawlerPro Github主页地址](https://github.com/MediaCrawlerPro)



扫描下方我的个人微信，备注：pro版本（如果图片展示不出来，可以直接添加我的微信号：relakkes）

![relakkes_weichat.JPG](static/images/relakkes_weichat.jpg)


##  Pro版本诞生的背景
[MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)这个项目开源至今获得了大量的关注，同时也暴露出来了一系列问题，比如：
- 能否支持多账号？
- 能否在linux部署？
- 能否去掉playwright的依赖？
- 有没有更简单的部署方法？
- 有没有针对新手上门槛更低的方法？

诸如上面的此类问题，想要在原有项目上去动刀，无疑是增加了复杂度，可能导致后续的维护更加困难。
出于可持续维护、简便易用、部署简单等目的，对MediaCrawler进行彻底重构。

## 项目介绍
### [MediaCrawler](https://github.com/NanmiCoder/MediaCrawler)的Pro版本python实现
**小红书爬虫**，**抖音爬虫**， **快手爬虫**， **B站爬虫**， **微博爬虫**，**百度贴吧**，**知乎爬虫**...。

支持多种平台的爬虫，支持多种数据的爬取，支持多种数据的存储，最重要的**完美支持多账号+IP代理池，让你的爬虫更加稳定**。
相较于MediaCrawler，Pro版本最大的变化：
- 去掉了playwright的依赖，不再将Playwright集成到爬虫主干中，依赖过重。
- 增加了Docker，Docker-compose的方式部署，让部署更加简单。
- 多账号+IP代理池的支持，让爬虫更加稳定。
- 新增签名服务，解耦签名逻辑，让爬虫更加灵活。


# FILE: docs/捐赠名单.md

## 捐赠MediaCrawler开源项目
> 捐赠时请务必备注您的昵称，我会在捐赠名单中表达对您的感谢

## 赞赏二维码

<table align="center">
  <tr>
    <td align="center">
      <h3>微信赞赏</h3>
      <img src="./static/images/wechat_pay.jpeg" alt="微信赞赏二维码" width="200"/>
    </td>
    <td align="center">
      <h3>支付宝赞赏</h3>
      <img src="./static/images/zfb_pay.png" alt="支付宝赞赏二维码" width="200"/>
    </td>
  </tr>
</table>

# MediaCrawler捐赠名单

> 再次感谢下面的捐赠者们对MediaCrawler的鼎力支持，是你们的支持让MediaCrawler的更新有了动力。

PS：如果打赏时请备注捐赠者，如有遗漏请联系我添加（有时候消息多可能会漏掉，十分抱歉）

| 捐赠者      | 捐赠金额 | 捐赠日期   |
| ----------- | -------- | ---------- |
| RichardYU   | 99 元    | 2025-06-19 |
| Z.FB        | 20 元    | 2025-04-10 |
| 若成        | 20 元    | 2025-04-01 |
| Puple_twirl | 20 元    | 2025-03-30 |
| N--F        | 20 元    | 2025-03-13 |
| 财*         | 20 元    | 2025-03-06 |
| 布莱**      | 1 元     | 2025-01-27 |
| xldmilktea  | 20 元    | 2025-01-25 |
| ChenWenLon  | 20 元    | 2025-01-07 |
| steam       | 20 元    | 2024-12-20 |
| mike        | 20 元    | 2024-12-17 |
| thechnolog  | 5 元     | 2024-11-05 |
| yinzhou     | 100 元   | 2024-10-21 |
| Tnk_se      | 50 元    | 2024-10-21 |
| 望、7       | 66 元    | 2024-09-26 |
| 凌凌7       | 200 元   | 2024-09-19 |
| yutao       | 20 元    | 2024-09-19 |
| Urtb*       | 100 元   | 2024-09-07 |
| Tornado     | 66 元    | 2024-09-04 |
| srhedbj     | 50 元    | 2024-08-20 |
| *嘉         | 20 元    | 2024-08-15 |
| *良         | 50 元    | 2024-08-13 |
| *皓         | 50 元    | 2024-03-18 |
| *刚         | 50 元    | 2024-03-18 |
| *乐         | 20 元    | 2024-03-17 |
| *木         | 20 元    | 2024-03-17 |
| *诚         | 20 元    | 2024-03-17 |
| Strem Gamer | 20 元    | 2024-03-16 |
| *鑫         | 20 元    | 2024-03-14 |
| Yuzu        | 20 元    | 2024-03-07 |
| **宁        | 100 元   | 2024-03-03 |
| **媛        | 20 元    | 2024-03-03 |
| Scarlett    | 20 元    | 2024-02-16 |
| Asun        | 20 元    | 2024-01-30 |
| 何*         | 100 元   | 2024-01-21 |
| allen       | 20 元    | 2024-01-10 |
| llllll      | 20 元    | 2024-01-07 |
| 邝*元       | 20 元    | 2023-12-29 |
| 50chen      | 50 元    | 2023-12-22 |
| xiongot     | 20 元    | 2023-12-17 |
| atom.hu     | 20 元    | 2023-12-16 |
| 一呆        | 20 元    | 2023-12-01 |
| 坠落        | 50 元    | 2023-11-08 |




# FILE: docs/原生环境管理文档.md

# 本地原生环境管理

## 推荐方案：使用 uv 管理依赖

### 1. 前置依赖
- 安装 [uv](https://docs.astral.sh/uv/getting-started/installation)，并使用 `uv --version` 验证。
- Python 版本建议使用 **3.11**（当前依赖基于该版本构建）。
- 安装 Node.js（抖音、知乎等平台需要），版本需 `>= 16.0.0`。

### 2. 同步 Python 依赖
```shell
# 进入项目根目录
cd MediaCrawler

# 使用 uv 保证 Python 版本和依赖一致性
uv sync
```

### 3. 安装 Playwright 浏览器驱动
```shell
uv run playwright install
```
> 项目已支持使用 Playwright 连接本地 Chrome。如需使用 CDP 方式，可在 `config/base_config.py` 中调整 `xhs` 和 `dy` 的相关配置。

### 4. 运行爬虫程序
```shell
# 项目默认未开启评论爬取，如需评论请在 config/base_config.py 中修改 ENABLE_GET_COMMENTS
# 其他功能开关也可在 config/base_config.py 查看，均有中文注释

# 从配置中读取关键词搜索并爬取帖子与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置中读取指定帖子ID列表并爬取帖子与评论
uv run main.py --platform xhs --lt qrcode --type detail

# 其他平台示例
uv run main.py --help
```

## 备选方案：Python 原生 venv（不推荐）

### 创建并激活虚拟环境
> 如果爬取抖音或知乎，需要提前安装 Node.js，版本 `>= 16`。
```shell
# 进入项目根目录
cd MediaCrawler

# 创建虚拟环境（示例 Python 版本：3.11，requirements 基于该版本）
python -m venv venv

# macOS & Linux 激活虚拟环境
source venv/bin/activate

# Windows 激活虚拟环境
venv\Scripts\activate
```

### 安装依赖与驱动
```shell
pip install -r requirements.txt
playwright install
```

### 运行爬虫程序（venv 环境）
```shell
# 从配置中读取关键词搜索并爬取帖子与评论
python main.py --platform xhs --lt qrcode --type search

# 从配置中读取指定帖子ID列表并爬取帖子与评论
python main.py --platform xhs --lt qrcode --type detail

# 更多示例
python main.py --help
```


# FILE: docs/常见问题.md

# 常见程序运行出错问题

## 缺少node环境导致的问题
Q: 爬取抖音和知乎报错: `execjs._exceptions.ProgramError: SyntaxError: 缺少 ';'` <br>
A: 该错误为缺少 nodejs 环境，这个错误可以通过安装 nodejs 环境来解决，版本大于等：`v16` <br>

Q: 使用Cookie爬取抖音报错: execjs._exceptions.ProgramError: TypeError: Cannot read property 'JS_MD5_NO_COMMON_JS' of null
A: windows电脑去网站下载`https://nodejs.org/en/blog/release/v16.8.0` Windows 64-bit Installer 版本，一直下一步即可。

## xhs登录出现滑块一直验证不通过问题

Q: 小红书扫码登录成功后，浏览器一直在验证滑块，无法登录？<br>
A: 小红书平台风控非常严格，**强烈建议使用 CDP 模式连接自己的真实浏览器**（默认配置），不要使用无痕浏览器或标准 Playwright 模式。连接真实浏览器可以复用已有的 Cookie、登录状态和浏览历史，大幅降低被风控检测的概率。如果仍然出现滑块问题，可以尝试删除项目目录下的`brower_data`文件夹，重新走登录流程。<br>

## 如何指定关键词
Q: 可以指定关键词爬取吗？<br>
A: 在config/base_config.py 中 KEYWORDS 参数用于控制需要爬取的关键词 <br>

## 如何指定帖子
Q: 可以指定帖子爬取吗？<br>
A：在config/base_config.py 中 XHS_SPECIFIED_ID_LIST 参数用于控制需要指定爬取的帖子ID列表 <br>

## 爬取失效
Q: 刚开始能爬取数据，过一段时间就是失效了？<br>
A：出现这种情况多半是由于你的账号触发了平台风控机制了，❗️❗️请勿大规模对平台进行爬虫，影响平台。<br>

## 如何更换另一个账号
Q: 如何更换登录账号？<br>
A：删除项目根目录下的 brower_data/ 文件夹即可 <br>

## playwright超时问题
Q: 报错 `playwright._impl._api_types.TimeoutError: Timeout 30000ms exceeded.`<br>
A: 出现这种情况检查下开梯子没有<br>

## 如果配置playwright浏览器驱动过滑块验证
Q: 小红书扫码登录成功后如何手动验证?
A: 打开 config/base_config.py 文件, 找到 HEADLESS 配置项, 将其设置为 False, 此时重启项目, 在浏览器中手动通过验证码<br>

## 词云图生成
Q: 如何配置词云图的生成?
A: 打开 config/base_config.py 文件, 找到`ENABLE_GET_WORDCLOUD` 以及`ENABLE_GET_COMMENTS` 两个配置项，将其都设为True即可使用该功能。<br>

## 词云图添加禁用词和自定义词组
Q: 如何给词云图添加禁用词和自定义词组？
A: 打开 `docs/hit_stopwords.txt` 输入禁用词(注意一个词语一行)。打开 config/base_config.py 文件找到 `CUSTOM_WORDS `按格式添加自定义词组即可。<br>

## CDP 连接已有浏览器相关问题

Q: 运行爬虫后提示无法连接到浏览器，报错 `Cannot connect to existing browser on port 9222`？<br>
A: 请检查以下几点：<br>
1. 确保 Chrome 浏览器已经打开并正在运行<br>
2. 在 Chrome 地址栏输入 `chrome://inspect/#remote-debugging`，确保已勾选 **"Allow remote debugging for this browser instance"**<br>
3. 页面上应显示 `Server running at: 127.0.0.1:9222`，如果没有显示说明远程调试未成功开启<br>
4. 确保 Chrome 版本 >= 144，低版本不支持此功能，在地址栏输入 `chrome://version` 查看版本号<br>

Q: 运行爬虫后浏览器弹出了确认对话框，需要怎么操作？<br>
A: 这是正常行为。Chrome 连接已有浏览器时会弹出确认对话框，点击"接受"即可。程序会等待用户确认，默认超时时间为60秒，在此期间点击确认即可。<br>

Q: 不想连接已有浏览器，想让程序自动启动一个新的浏览器怎么办？<br>
A: 在 `config/base_config.py` 中设置 `CDP_CONNECT_EXISTING = False`，程序会自动检测并启动一个新的 Chrome/Edge 浏览器实例。<br>

Q: 为什么推荐连接已有浏览器而不是启动新浏览器？<br>
A: 连接已有浏览器可以直接复用你浏览器中真实的 Cookie、登录状态、扩展插件和浏览历史，平台很难区分这是自动化操作还是真实用户行为，**大幅降低被平台风控检测的风险**。而启动新浏览器是一个"干净"的环境，更容易被平台识别为爬虫。<br>


# FILE: docs/index.md

# MediaCrawler使用方法

## 项目文档

- [项目架构文档](项目架构文档.md) - 系统架构、模块设计、数据流向（含 Mermaid 图表）

## 推荐：使用 uv 管理依赖

### 1. 前置依赖
- 安装 [uv](https://docs.astral.sh/uv/getting-started/installation)，并用 `uv --version` 验证。
- Python 版本建议使用 **3.11**（当前依赖基于该版本构建）。
- 安装 Node.js（抖音、知乎等平台需要），版本需 `>= 16.0.0`。

### 2. 同步 Python 依赖
```shell
# 进入项目根目录
cd MediaCrawler

# 使用 uv 保证 Python 版本和依赖一致性
uv sync
```

### 3. 安装 Playwright 浏览器驱动
```shell
uv run playwright install
```
> 项目已支持使用 Playwright 连接本地 Chrome。如需使用 CDP 方式，可在 `config/base_config.py` 中调整 `xhs` 和 `dy` 的相关配置。

### 4. 运行爬虫程序
```shell
# 项目默认未开启评论爬取，如需评论请在 config/base_config.py 中修改 ENABLE_GET_COMMENTS
# 其他功能开关也可在 config/base_config.py 查看，均有中文注释

# 从配置中读取关键词搜索并爬取帖子与评论
uv run main.py --platform xhs --lt qrcode --type search

# 从配置中读取指定帖子ID列表并爬取帖子与评论
uv run main.py --platform xhs --lt qrcode --type detail

# 使用 SQLite 数据库存储数据（推荐个人用户使用）
uv run main.py --platform xhs --lt qrcode --type search --save_data_option sqlite

# 使用 MySQL 数据库存储数据
uv run main.py --platform xhs --lt qrcode --type search --save_data_option db

# 其他平台示例
uv run main.py --help
```

## 备选：Python 原生 venv（不推荐）
> 如果爬取抖音或知乎，需要提前安装 Node.js，版本 `>= 16`。
```shell
# 进入项目根目录
cd MediaCrawler

# 创建虚拟环境（示例 Python 版本：3.11，requirements 基于该版本）
python -m venv venv

# macOS & Linux 激活虚拟环境
source venv/bin/activate

# Windows 激活虚拟环境
venv\Scripts\activate
```
```shell
# 安装依赖与驱动
pip install -r requirements.txt
playwright install
```
```shell
# 运行爬虫程序（venv 环境）
python main.py --platform xhs --lt qrcode --type search
python main.py --platform xhs --lt qrcode --type detail
python main.py --platform xhs --lt qrcode --type search --save_data_option sqlite
python main.py --platform xhs --lt qrcode --type search --save_data_option db
python main.py --help
```

## 💾 数据存储

支持多种数据存储方式：
- **CSV 文件**: 支持保存至 CSV (位于 `data/` 目录下)
- **JSON 文件**: 支持保存至 JSON (位于 `data/` 目录下)
- **数据库存储**
  - 使用 `--init_db` 参数进行数据库初始化 (使用 `--init_db` 时，无需其他可选参数)
  - **SQLite 数据库**: 轻量级数据库，无需服务器，适合个人使用 (推荐)
    1. 初始化: `--init_db sqlite`
    2. 数据存储: `--save_data_option sqlite`
  - **MySQL 数据库**: 支持保存至关系型数据库 MySQL (需提前创建数据库)
    1. 初始化: `--init_db mysql`
    2. 数据存储: `--save_data_option db` (db 参数为兼容历史更新保留)

## 免责声明
> **免责声明：**
> 
> 大家请以学习为目的使用本仓库，爬虫违法违规的案件：https://github.com/HiddenStrawberry/Crawler_Illegal_Cases_In_China  <br>
>
>本项目的所有内容仅供学习和参考之用，禁止用于商业用途。任何人或组织不得将本仓库的内容用于非法用途或侵犯他人合法权益。本仓库所涉及的爬虫技术仅用于学习和研究，不得用于对其他平台进行大规模爬虫或其他非法行为。对于因使用本仓库内容而引起的任何法律责任，本仓库不承担任何责任。使用本仓库的内容即表示您同意本免责声明的所有条款和条件。


# FILE: docs/作者介绍.md

# 关于作者
> 大家都叫我阿江，网名：程序员阿江-Relakkes，目前是一名独立开发者，专注于 AI Agent 和爬虫相关的开发工作，All in AI。

- [Github万星开源自媒体爬虫仓库MediaCrawler作者](https://github.com/NanmiCoder/MediaCrawler)
- 全栈程序员，熟悉Python、Golang、JavaScript，工作中主要用Golang。
- 曾经主导并参与过百万级爬虫采集系统架构设计与编码
- 爬虫是一种技术兴趣爱好，参与爬虫有一种对抗的感觉，越难越兴奋。
- 目前专注于 AI Agent 领域，积极探索 AI 技术的应用与创新
- 如果你有 AI Agent 相关的项目需要合作，欢迎联系我，我有很多时间可以投入
 
## 微信联系方式
![relakkes_weichat.JPG](static/images/relakkes_weichat.jpg)

## B站主页地址
https://space.bilibili.com/434377496

## 抖音主页地址
https://www.douyin.com/user/MS4wLjABAAAATJPY7LAlaa5X-c8uNdWkvz0jUGgpw4eeXIwu_8BhvqE?previous_page=app_code_link

## 小红书主页地址
https://www.xiaohongshu.com/user/profile/5f58bd990000000001003753?xhsshare=CopyLink&appuid=5f58bd990000000001003753&apptime=1724737153

# FILE: docs/知识付费介绍.md

# 知识付费介绍

## MediaCrawlerPro项目源码订阅服务
[mediacrawlerpro订阅文档说明](mediacrawlerpro订阅.md)

## MediaCrawler源码剖析视频课程
[mediacrawler源码课程介绍](https://relakkes.feishu.cn/wiki/JUgBwdhIeiSbAwkFCLkciHdAnhh)



# FILE: docs/快代理使用文档.md

## 快代理使用文档（支持个人和企业用户）

## 准备代理 IP 信息
点击 <a href="https://www.kuaidaili.com/?ref=ldwkjqipvz6c">快代理</a> 官网注册并实名认证（国内使用代理 IP 必须要实名，懂的都懂）

## 获取 IP 代理的密钥信息
从 <a href="https://www.kuaidaili.com/?ref=ldwkjqipvz6c">快代理</a> 官网获取免费试用，如下图所示
![img.png](static/images/img.png)

注意：选择私密代理
![img_1.png](static/images/img_1.png)

选择开通试用
![img_2.png](static/images/img_2.png)

初始化一个快代理的示例，如下代码所示，需要4个参数

```python
# 文件地址： proxy/providers/kuai_daili_proxy.py
# -*- coding: utf-8 -*-
def new_kuai_daili_proxy() -> KuaiDaiLiProxy:
    """
    构造快代理HTTP实例
    Returns:

    """
    return KuaiDaiLiProxy(
        kdl_secret_id=os.getenv("kdl_secret_id", "你的快代理secert_id"),
        kdl_signature=os.getenv("kdl_signature", "你的快代理签名"),
        kdl_user_name=os.getenv("kdl_user_name", "你的快代理用户名"),
        kdl_user_pwd=os.getenv("kdl_user_pwd", "你的快代理密码"),
    )

```
在试用的订单中可以看到这四个参数，如下图所示

`kdl_user_name`、`kdl_user_pwd`
![img_3.png](static/images/img_3.png)

`kdl_secret_id`、`kdl_signature`
![img_4.png](static/images/img_4.png)


# FILE: docs/代理使用.md

# 代理 IP 使用说明
> 还是得跟大家再次强调下，不要对一些自媒体平台进行大规模爬虫或其他非法行为，要踩缝纫机的哦🤣

## 简易的流程图

![代理 IP 使用流程图](static/images/代理IP%20流程图.drawio.png)


## 选择一个代理IP提供商

### 快代理
[快代理使用文档](快代理使用文档.md)

### 豌豆HTTP文档查看
[豌豆HTTP使用文档](豌豆HTTP使用文档.md)
