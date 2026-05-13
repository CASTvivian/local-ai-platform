# Missing Repo Summary Source: punkpeye/awesome-mcp-servers

- URL: https://github.com/punkpeye/awesome-mcp-servers
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/punkpeye__awesome-mcp-servers
- Clone Status: cloned
- Language: None
- Stars: 86780
- Topics: ai, mcp
- Description: A collection of MCP servers.

## Extracted README / Docs / Examples



# FILE: README-th.md

# รายชื่อ MCP Servers ที่น่าสนใจ [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/中文文件-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/中文文档-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

รายการรวบรวม Model Context Protocol (MCP) servers ที่น่าสนใจ

* [MCP คืออะไร?](#what-is-mcp)
* [ไคลเอนต์](#clients)
* [บทแนะนำ](#tutorials)
* [การนำไปใช้งานเซิร์ฟเวอร์](#server-implementations)
* [เฟรมเวิร์ค](#frameworks)
* [ยูทิลิตี้](#utilities)
* [เคล็ดลับและเทคนิค](#tips-and-tricks)

## MCP คืออะไร?

[MCP](https://modelcontextprotocol.io/) คือโปรโตคอลเปิดที่ช่วยให้โมเดล AI สามารถโต้ตอบกับทรัพยากรทั้งในระบบและระยะไกลได้อย่างปลอดภัย ผ่านการใช้งานเซิร์ฟเวอร์มาตรฐาน รายการนี้มุ่งเน้นไปที่ MCP เซิร์ฟเวอร์ที่พร้อมใช้งานและอยู่ในช่วงทดลอง ซึ่งช่วยขยายความสามารถของ AI ผ่านการเข้าถึงไฟล์ การเชื่อมต่อฐานข้อมูล การผสานรวม API และบริการอื่นๆ ที่เกี่ยวข้องกับบริบท

## ไคลเอนต์

ดูเพิ่มเติมได้ที่ [awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) และ [glama.ai/mcp/clients](https://glama.ai/mcp/clients)

> [!TIP]
> [Glama Chat](https://glama.ai/chat) คือไคลเอนต์ AI แบบ multi-modal ที่รองรับ MCP และมี [AI gateway](https://glama.ai/gateway)

## บทแนะนำ

* [Model Context Protocol (MCP) เริ่มต้นอย่างรวดเร็ว](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [การตั้งค่า Claude Desktop App เพื่อใช้งานกับฐานข้อมูล SQLite](https://youtu.be/wxCCzo9dGj0)

## ชุมชน

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [เซิร์ฟเวอร์ Discord](https://glama.ai/mcp/discord)

## คำอธิบายสัญลักษณ์

* 🎖️ – การนำไปใช้งานอย่างเป็นทางการ
* ภาษาโปรแกรมมิ่ง
  * 🐍 – โค้ดเบส Python
  * 📇 – โค้ดเบส TypeScript
  * 🏎️ – โค้ดเบส Go
  * 🦀 – โค้ดเบส Rust
  * #️⃣ - โค้ดเบส C#
  * ☕ - โค้ดเบส Java
* ขอบเขต
  * ☁️ - บริการคลาวด์
  * 🏠 - บริการในเครื่อง
  * 📟 - ระบบฝังตัว
* ระบบปฏิบัติการ
  * 🍎 – สำหรับ macOS
  * 🪟 – สำหรับ Windows
  * 🐧 - สำหรับ Linux

> [!NOTE]
> สับสนระหว่าง Local 🏠 กับ Cloud ☁️ ?
> * ใช้ local เมื่อ MCP เซิร์ฟเวอร์สื่อสารกับซอฟต์แวร์ที่ติดตั้งในเครื่อง เช่น การควบคุมเบราว์เซอร์ Chrome
> * ใช้ network เมื่อ MCP เซิร์ฟเวอร์สื่อสารกับ API ระยะไกล เช่น API สภาพอากาศ

## การนำไปใช้งานเซิร์ฟเวอร์

> [!NOTE]
> ตอนนี้เรามี[ไดเร็กทอรี web-based](https://glama.ai/mcp/servers) ที่ซิงค์กับ repository นี้

* 🔗 - [รวบรวม](#aggregators)
* 🎨 - [ศิลปะและวัฒนธรรม](#art-and-culture)
* 🧬 - [ชีววิทยา การแพทย์ และไบโออินฟอร์เมติกส์](#bio)
* 📂 - [การทำงานอัตโนมัติของเบราว์เซอร์](#browser-automation)
* ☁️ - [แพลตฟอร์มคลาวด์](#cloud-platforms)
* 👨‍💻 - [การเรียกใช้โค้ด](#code-execution)
* 🖥️ - [คำสั่งในเทอร์มินัล](#command-line)
* 💬 - [การสื่อสาร](#communication)
* 👤 - [แพลตฟอร์มข้อมูลลูกค้า](#customer-data-platforms)
* 🗄️ - [ฐานข้อมูล](#databases)
* 📊 - [แพลตฟอร์มข้อมูล](#data-platforms)
* 🛠️ - [เครื่องมือสำหรับนักพัฒนา](#developer-tools)
* 📟 - [ระบบฝังตัว](#embedded-system)
* 📂 - [ระบบไฟล์](#file-systems)
* 💰 - [การเงินและฟินเทค](#finance--fintech)
* 🎮 - [เกม](#gaming)
* 🧠 - [ความรู้และความจำ](#knowledge--memory)
* ⚖️ - [กฎหมาย](#legal)
* 🗺️ - [บริการตำแหน่ง](#location-services)
* 🎯 - [การตลาด](#marketing)
* 📊 - [การตรวจสอบ](#monitoring)
* 🔎 - [ค้นหาและสกัดข้อมูล](#search)
* 🔒 - [ความปลอดภัย](#security)
* 🏃 - [กีฬา](#sports)
* 🎧 - [การสนับสนุนและจัดการบริการ](#support-and-service-management)
* 🌎 - [บริการแปลภาษา](#translation-services)
* 🚆 - [การเดินทางและการขนส่ง](#travel-and-transportation)
* 🔄 - [ระบบควบคุมเวอร์ชัน](#version-control)
* 🛠️ - [เครื่องมือและการผสานรวมอื่นๆ](#other-tools-and-integrations)

### 🔗 รวบรวม

เซิร์ฟเวอร์สำหรับเข้าถึงแอปและเครื่องมือจำนวนมากผ่าน MCP เซิร์ฟเวอร์เดียว

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP ที่รวมกันหลายเซิร์ฟเวอร์ MCP เป็นเซิร์ฟเวอร์เดียว
- [PipedreamHQ/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - เชื่อมต่อกับ API 2,500 รายการ พร้อมเครื่องมือสำเร็จรูป 8,000+ รายการ และจัดการเซิร์ฟเวอร์สำหรับผู้ใช้งานของคุณในแอปของคุณเอง
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - เครื่องมือพร็อกซี่สำหรับรวมเซิร์ฟเวอร์ MCP หลายตัวเข้าด้วยกันเป็นจุดเชื่อมต่อเดียว ปรับขนาดเครื่องมือ AI ของคุณด้วยการกระจายโหลดคำขอระหว่างเซิร์ฟเวอร์ MCP หลายตัว คล้ายกับวิธีที่ Nginx ทำงานสำหรับเว็บเซิร์ฟเวอร์
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP รวมข้อมูลส่วนตัวที่ครอบคลุมด้วยการรวม Steam, YouTube, Bilibili, Spotify, Reddit และแพลตฟอร์มอื่นๆ พร้อมการรับรองความถูกต้อง OAuth2 การจัดการโทเค็นอัตโนมัติ และเครื่องมือ 90+ สำหรับเข้าถึงข้อมูลเกม เพลง วิดีโอ และแพลตฟอร์มโซเชียล

### 🎨 ศิลปะและวัฒนธรรม

เข้าถึงและสำรวจคอลเลกชันงานศิลปะ มรดกทางวัฒนธรรม และฐานข้อมูลพิพิธภัณฑ์ ช่วยให้โมเดล AI สามารถค้นหาและวิเคราะห์เนื้อหาด้านศิลปะและวัฒนธรรม

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - เซิร์ฟเวอร์ MCP ในเครื่องที่สร้างภาพเคลื่อนไหวด้วย Manim
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - เพิ่ม วิเคราะห์ ค้นหา และสร้างการตัดต่อวิดีโอจากคอลเลกชันวิดีโอของคุณ
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 🏠 - เซิร์ฟเวอร์ MCP เพื่อโต้ตอบกับคลังข้อมูลอัลกุรอาน ผ่าน REST API v4 อย่างเป็นทางการ
- [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [glama](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - เซิร์ฟเวอร์ MCP สำหรับ AniList พร้อมการแนะนำตามรสนิยม การวิเคราะห์การรับชม เครื่องมือโซเชียล และการจัดการรายการแบบครบวงจร
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - การผสานรวม API พิพิธภัณฑ์ Rijksmuseum สำหรับค้นหางานศิลปะ รายละเอียด และคอลเลกชัน
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - การผสานรวม API Oorlogsbronnen (แหล่งข้อมูลสงคราม) สำหรับเข้าถึงบันทึกทางประวัติศาสตร์ ภาพถ่าย และเอกสารจากเนเธอร์แลนด์ในช่วงสงครามโลกครั้งที่ 2 (1940-1945)
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - การผสานรวมเซิร์ฟเวอร์ MCP สำหรับ DaVinci Resolve ที่ให้เครื่องมือทรงพลังสำหรับการตัดต่อวิดีโอ ปรับสี จัดการสื่อ และควบคุมโปรเจ็กต์
- [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [glama](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - เซิร์ฟเวอร์ MCP แบบโลคัลสำหรับสร้างแอสเซ็ตรูปภาพด้วย Google Gemini (Nano Banana 2 / Pro) รองรับเอาต์พุต PNG/WebP แบบโปร่งใส การปรับขนาด/ครอบภาพอย่างแม่นยำ รูปอ้างอิงได้สูงสุด 14 รูป และการอ้างอิงข้อมูลด้วย Google Search
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - เซิร์ฟเวอร์ MCP ที่ผสานรวม AniList API สำหรับข้อมูลอนิเมะและมังงะ
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - ให้บริการจัดทำแผนภูมิปาจื้อ (八字) และการวิเคราะห์ที่ครอบคลุมและแม่นยำ

### 🧬 ชีววิทยา การแพทย์ และไบโออินฟอร์เมติกส์

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - เซิร์ฟเวอร์ MCP สำหรับการวิจัยทางชีวการแพทย์ที่ให้การเข้าถึง PubMed, ClinicalTrials.gov และ MyVariant.info
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP เพื่อโต้ตอบกับ BioThings API รวมถึงยีน ความแปรปรวนทางพันธุกรรม ยา และข้อมูลอนุกรมวิธาน
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP ที่ให้เครื่องมือไบโออินฟอร์เมติกส์ที่ทรงพลังสำหรับการสืบค้นและวิเคราะห์ทางพันธุกรรม ห่อหุ้มไลบรารี `gget` ยอดนิยม
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP สำหรับฐานข้อมูลที่สามารถสืบค้นได้สำหรับการวิจัยเรื่องความชราและอายุยืนจากโครงการ OpenGenes
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - เซิร์ฟเวอร์ MCP สำหรับฐานข้อมูล SynergyAge ของปฏิสัมพันธ์ทางพันธุกรรมที่เสริมกันและต่อต้านกันในด้านอายุยืน
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - เซิร์ฟเวอร์โปรโตคอลบริบทโมเดลสำหรับ Fast Healthcare Interoperability Resources (FHIR) APIs ให้การผสานรวมที่ราบรื่นกับเซิร์ฟเวอร์ FHIR ทำให้ผู้ช่วย AI สามารถค้นหา ดึงข้อมูล สร้าง อัปเดต และวิเคราะห์ข้อมูลสุขภาพทางคลินิกด้วยการสนับสนุนการรับรองความถูกต้อง SMART-on-FHIR

### 📂 การทำงานอัตโนมัติของเบราว์เซอร์

ความสามารถในการเข้าถึงและทำงานอัตโนมัติกับเว็บ ช่วยให้สามารถค้นหา ดึงข้อมูล และประมวลผลเนื้อหาเว็บในรูปแบบที่เป็นมิตรกับ AI

- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 - เซิร์ฟเวอร์ MCP สำหรับการทำงานอัตโนมัติของเบราว์เซอร์ที่มีน้ำหนักเบา เขียนด้วย Rust และไม่มีการพึ่งพาภายนอก.
- [34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - เซิร์ฟเวอร์ MCP ที่สนับสนุนการค้นหาเนื้อหา Bilibili พร้อมตัวอย่างการผสานรวม LangChain และสคริปต์ทดสอบ
- [automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🐍 - เซิร์ฟเวอร์ MCP สำหรับการทำงานอัตโนมัติของเบราว์เซอร์โดยใช้ Playwright
- [blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🐍 - เซิร์ฟเวอร์ MCP Python ที่ใช้ Playwright สำหรับการทำงานอัตโนมัติของเบราว์เซอร์ เหมาะสำหรับ llm มากขึ้น
- [browserbase/mcp-server-browserbase](https://github.com/browserbase/mcp-server-browserbase) 🎖️ 📇 - ทำงานอัตโนมัติกับเบราว์เซอร์บนคลาวด์ (เช่น การนำทางเว็บ การดึงข้อมูล การกรอกแบบฟอร์ม และอื่นๆ)
- [brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - เซิร์ฟเวอร์ MCP Selenium สำหรับควบคุมเบราว์เซอร์ด้วยภาษาธรรมชาติใน Cursor IDE เหมาะอย่างยิ่งสำหรับการทดสอ

# FILE: README-ko.md

# Awesome MCP Servers [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

# 모델 컨텍스트 프로토콜 (MCP) 서버 엄선 목록

* [MCP란 무엇인가?](#mcp란-무엇인가)
* [클라이언트](#클라이언트)
* [튜토리얼](#튜토리얼)
* [서버 구현](#서버-구현)
* [프레임워크](#프레임워크)
* [유틸리티](#유틸리티)
* [팁과 요령](#팁과-요령)
* [스타 히스토리](#스타-히스토리)

## MCP란 무엇인가?

[MCP](https://modelcontextprotocol.io/)는 AI 모델이 표준화된 서버 구현을 통해 로컬 및 원격 리소스와 안전하게 상호 작용할 수 있도록 하는 개방형 프로토콜입니다. 이 목록은 파일 접근, 데이터베이스 연결, API 통합 및 기타 컨텍스트 서비스를 통해 AI 기능을 확장하는 프로덕션 준비 및 실험적 MCP 서버에 중점을 둡니다.

## 클라이언트

[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/) 및 [glama.ai/mcp/clients](https://glama.ai/mcp/clients)를 확인하세요.

> [!팁]
> [Glama Chat](https://glama.ai/chat)은 MCP 지원 및 [AI 게이트웨이](https://glama.ai/gateway)를 갖춘 멀티모달 AI 클라이언트입니다.

## 튜토리얼

* [모델 컨텍스트 프로토콜 (MCP) 빠른 시작](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [SQLite 데이터베이스를 사용하도록 Claude 데스크톱 앱 설정하기](https://youtu.be/wxCCzo9dGj0)

## 커뮤니티

* [r/mcp 레딧](https://www.reddit.com/r/mcp)
* [디스코드 서버](https://glama.ai/mcp/discord)

## 범례

* 🎖️ – 공식 구현
* 프로그래밍 언어
  * 🐍 – 파이썬 코드베이스
  * 📇 – 타입스크립트 코드베이스
  * 🏎️ – Go 코드베이스
  * 🦀 – Rust 코드베이스
  * #️⃣ - C# 코드베이스
  * ☕ - Java 코드베이스
* 범위
  * ☁️ - 클라우드 서비스
  * 🏠 - 로컬 서비스
* 운영체제
  * 🍎 – macOS용
  * 🪟 – Windows용
  * 🐧 - Linux용

> [!참고]
> 로컬 🏠 vs 클라우드 ☁️ 가 헷갈리시나요?
> * MCP 서버가 로컬에 설치된 소프트웨어와 통신할 때 로컬을 사용하세요 (예: Chrome 브라우저 제어).
> * MCP 서버가 원격 API와 통신할 때 네트워크(클라우드)를 사용하세요 (예: 날씨 API).

## 서버 구현

> [!참고]
> 이제 리포지토리와 동기화되는 [웹 기반 디렉토리](https://glama.ai/mcp/servers)가 있습니다.

* 🔗 - [Aggregators](#aggregators)
* 📂 - [브라우저 자동화](#browser-automation)
* 🎨 - [예술 및 문화](#art-and-culture)
* 🧬 - [생물학, 의학 및 생물정보학](#bio)
* ☁️ - [클라우드 플랫폼](#cloud-platforms)
* 🖥️ - [커맨드 라인](#command-line)
* 💬 - [커뮤니케이션](#communication)
* 👤 - [고객 데이터 플랫폼](#customer-data-platforms)
* 🗄️ - [데이터베이스](#databases)
* 📊 - [데이터 플랫폼](#data-platforms)
* 🛠️ - [개발자 도구](#developer-tools)
* 📂 - [파일 시스템](#file-systems)
* 💰 - [금융 및 핀테크](#finance--fintech)
* 🎮 - [게임](#gaming)
* 🧠 - [지식 및 메모리](#knowledge--memory)
* ⚖️ - [법률](#legal)
* 🗺️ - [위치 서비스](#location-services)
* 🎯 - [마케팅](#marketing)
* 📊 - [모니터링](#monitoring)
* 🔎 - [검색](#search)
* 🔒 - [보안](#security)
* 🏃 - [스포츠](#sports)
* 🌎 - [번역 서비스](#translation-services)
* 🚆 - [여행 및 교통](#travel-and-transportation)
* 🔄 - [버전 관리](#version-control)
* 🛠️ - [기타 도구 및 통합](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>애그리게이터

단일 MCP 서버를 통해 많은 앱과 도구에 접근하기 위한 서버입니다.

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - 여러 MCP 서버를 하나의 MCP 서버로 통합하는 통합 모델 컨텍스트 프로토콜 서버 구현.
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - 웹 API를 10초 만에 MCP 서버로 전환하고 오픈 소스 레지스트리에 추가하세요: https://open-mcp.org
- [tigranbs/mcgravity](https://github.com/krayniok/mcgravity) 📇 🏠 🪟 🐧 - 여러 MCP 서버를 단일 연결 포인트로 통합하여 프록시하는 도구로, 요청 부하를 분산하여 AI 도구를 확장합니다.
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCP는 GUI를 통해 MCP 연결을 관리하는 통합 미들웨어 MCP 서버입니다.
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - 서버 측 코드를 변경하지 않고 한 번의 클릭으로 웹 API를 MCP 서버로 변환합니다.
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - MCP를 통해 Google의 Imagen 3.0 API를 사용하는 강력한 이미지 생성 도구. 고급 사진, 예술 및 사실적인 컨트롤로 텍스트 프롬프트에서 고품질 이미지를 생성합니다.
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Steam, YouTube, Bilibili, Spotify, Reddit 등 플랫폼을 통합한 포괄적인 개인 데이터 집계 MCP 서버. OAuth2 인증, 자동 토큰 관리, 90+ 도구로 게임, 음악, 비디오, 소셜 플랫폼 데이터에 액세스.

### 📂 <a name="browser-automation"></a>브라우저 자동화

웹 콘텐츠 접근 및 자동화 기능. AI 친화적인 형식으로 웹 콘텐츠 검색, 스크래핑 및 처리를 가능하게 합니다.
- [BB-fat/browser-use-rs](https://github.com/BB-fat/browser-use-rs) 🦀 - Rust로 작성된 의존성 없는 경량 브라우저 자동화 MCP 서버.
- [@blackwhite084/playwright-plus-python-mcp](https://github.com/blackwhite084/playwright-plus-python-mcp) 🌐 - Playwright를 사용한 브라우저 자동화를 위한 MCP 파이썬 서버, llm에 더 적합
- [@executeautomation/playwright-mcp-server](https://github.com/executeautomation/mcp-playwright) 🌐⚡️ - 브라우저 자동화 및 웹 스크래핑을 위해 Playwright를 사용하는 MCP 서버
- [@automatalabs/mcp-server-playwright](https://github.com/Automata-Labs-team/MCP-Server-Playwright) 🌐 🖱️ - Playwright를 사용한 브라우저 자동화를 위한 MCP 서버
- [@brutalzinn/simple-mcp-selenium](https://github.com/brutalzinn/simple-mcp-selenium) 📇 🏠 - Cursor IDE에서 자연어로 브라우저를 제어하기 위한 MCP Selenium 서버입니다. 테스트, 자동화, 다중 사용자 시나리오에 최적화되어 있습니다.
- [@modelcontextprotocol/server-puppeteer](https://github.com/modelcontextprotocol/servers/tree/main/src/puppeteer) 📇 🏠 - 웹 스크래핑 및 상호 작용을 위한 브라우저 자동화
- [@kimtaeyoon83/mcp-server-youtube-transcript](https://github.com/kimtaeyoon83/mcp-server-youtube-transcript) 📇 ☁️ - AI 분석을 위해 YouTube 자막 및 스크립트 가져오기
- [@recursechat/mcp-server-apple-shortcuts](https://github.com/recursechat/mcp-server-apple-shortcuts) 📇 🏠 🍎 - Apple Shortcuts와의 MCP 서버 통합
- [@kimtth/mcp-aoai-web-Browse](https://github.com/kimtth/mcp-aoai-web-Browse) 🐍 🏠 - Azure OpenAI 및 Playwright를 사용하는 `최소한의` 서버/클라이언트 MCP 구현
- [@pskill9/web-search](https://github.com/pskill9/web-search) 📇 🏠 - API 키 없이 Google 검색 결과를 사용하여 무료 웹 검색을 가능하게 하는 MCP 서버
- [@co-browser/browser-use-mcp-server](https://github.com/co-browser/browser-use-mcp-server) 🌐🔮 - SSE 전송을 지원하는 MCP 서버로 패키징된 browser-use. Docker에서 Chromium을 실행하기 위한 Dockerfile + VNC 서버 포함.
- [@34892002/bilibili-mcp-js](https://github.com/34892002/bilibili-mcp-js) 📇 🏠 - Bilibili 콘텐츠 검색을 지원하는 MCP 서버. LangChain 통합 예제 및 테스트 스크립트 제공.
- [@getrupt/ashra-mcp](https://github.com/getrupt/ashra-mcp) 📇 🏠 - 모든 웹사이트에서 구조화된 데이터 추출. 프롬프트만 입력하면 JSON 획득.
- [freema/firefox-devtools-mcp](https://github.com/freema/firefox-devtools-mcp) 📇 🏠 - WebDriver BiDi를 통한 Firefox 브라우저 자동화. 테스트, 스크래핑 및 브라우저 제어 지원. 스냅샷/UID 기반 상호작용, 네트워크 모니터링, 콘솔 캡처 및 스크린샷 지원

### 🎨 <a name="art-and-culture"></a>예술 및 문화

예술 컬렉션, 문화 유산 및 박물관 데이터베이스에 접근하고 탐색합니다. AI 모델이 예술 및 문화 콘텐츠를 검색하고 분석할 수 있게 합니다.

- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 포괄적이고 정확한 사주팔자(八字) 분석과 해석 제공
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 📹🎬 - Video Jungle 컬렉션에서 비디오 편집 추가, 분석, 검색 및 생성
- [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [glama](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - 취향 기반 추천, 시청 분석, 소셜 도구 및 전체 목록 관리를 제공하는 AniList MCP 서버
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 작품 검색, 세부 정보 및 컬렉션을 위한 Rijksmuseum API 통합
- [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [glama](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - Google Gemini(Nano Banana 2 / Pro)로 이미지 에셋을 생성하는 로컬 MCP 서버. 투명 PNG/WebP 출력, 정확한 리사이즈/크롭, 최대 14개의 참조 이미지, Google Search 그라운딩을 지원합니다.
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - 애니메이션 및 만화 정보를 위한 AniList API를 통합하는 MCP 서버

### 🧬 <a name="bio"></a>생물학, 의학 및 생물정보학

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - PubMed, ClinicalTrials.gov, MyVariant.info에 대한 액세스를 제공하는 생의학 연구용 MCP 서버.
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - 유전자, 유전적 변이, 약물 및 분류학 정보를 포함한 BioThings API와 상호 작용하는 MCP 서버.
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - 인기있는 `gget` 라이브러리를 래핑하여 유전체학 쿼리 및 분석을 위한 강력한 생물정보학 도구키트를 제공하는 MCP 서버.
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - OpenGenes 프로젝트의 노화 및 수명 연구를 위한 쿼리 가능한 데이터베이스용 MCP 서버.
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - 수명에서의 상승적 및 길항적 유전적 상호작용의 SynergyAge 데이터베이스용 MCP 서버.
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - 빠른 의료 상호운용성 리소스(FHIR) API용 모델 컨텍스트 프로토콜 서버. FHIR 서버와의 원활한 통합을 제공하여 AI 어시스턴트가 SMART-on-FHIR 인증 지원을 통해 임상 의료 데이터를 검색, 검색, 생성, 업데이트 및 분석할 수 있게 합니다.

### ☁️ <a name="cloud-platforms"></a>클라우드 플랫폼

클라우드 플랫폼 서비스 통합. 클라우드 인프라 및 서비스의 관리 및 상호 작용을 가능하게 합니다.

- [mctlhq/mctl-mcp](https://github.com/mctlhq/mctl-mcp) [![mctl-mcp MCP server](https://glama.ai/mcp/servers/mctlhq/mctl-mcp/badges/score.svg)](https://glama.ai/mcp/servers/mctlhq/mctl-mcp) ☁️ - 쿠버네티스 관리 및 자동화된 GitOps를 위한 AI 네이티브 플랫폼 (30개 이상의 도구).
- [mrostamii/rancher-mcp-server](https://github.com/mrostamii/rancher-mcp-server) [glama](https://glama.ai/mcp/servers/mrostamii/rancher-mcp-server) 🏎️ ☁️/🏠 - Rancher 생태계를 위한 MCP 서버로, 멀티 클러스터 Kubernetes 운영, Harvester HCI 관리(VM, 스토리지, 네트워크), Fleet GitOps 도구를 제공합니다.
- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - fastmcp 라이브러리와 통합하여 NebulaBlock의 모든 API 기능을 도구로 제공합니다。
- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - Greenfield, IPFS, Arweave와 같은 분산 스토리지 네트워크에 AI 생성 코드를 즉시 배포할 수 있는 4EVERLAND Hosting용 MCP 서버 구현.
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 치니우안(七牛云) 제품으로 구축된 MCP는 치니우안 스토리지, 지능형 멀티미디어 서비스 등에 접근할 수 있습니다.
- [Cloudflare MCP 서버](https://github.com/cloudflare/mcp-server-cloudflare) 🎖️ 📇 ☁️ - Workers, KV, R2 및 D1을 포함한 Cloudflare 서비스와의 통합
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFS 스토리지 업로드 및 조작
- [alexei-led/aws-mcp-server](https://github.com/alexei-led/aws-mcp-server) 🐍 ☁️ - AI 어시스턴트가 AWS CLI 명령을 실행하고, 유닉스 파이프를 사용하며, 안전한 Docker 환경에서 일반적인 AWS 작업을 위한 프롬프트 템플릿을 멀티 아키텍처 지원으로 적용할 수 있게 하는 가볍지만 강력한 

# FILE: README-ja.md

# 素晴らしいMCPサーバー [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

[![English](https://img.shields.io/badge/English-Click-yellow)](README.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-點擊查看-orange)](README-zh_TW.md)
[![简体中文](https://img.shields.io/badge/简体中文-点击查看-orange)](README-zh.md)
[![日本語](https://img.shields.io/badge/日本語-クリック-青)](README-ja.md)
[![한국어](https://img.shields.io/badge/한국어-클릭-yellow)](README-ko.md)
[![Português Brasileiro](https://img.shields.io/badge/Português_Brasileiro-Clique-green)](README-pt_BR.md)
[![Discord](https://img.shields.io/discord/1312302100125843476?logo=discord&label=discord)](https://glama.ai/mcp/discord)
[![Subreddit subscribers](https://img.shields.io/reddit/subreddit-subscribers/mcp?style=flat&logo=reddit&label=subreddit)](https://www.reddit.com/r/mcp/)

素晴らしいモデルコンテキストプロトコル（MCP）サーバーの厳選リスト。

* [MCPとは何ですか？](#MCPとは何ですか？)
* [クライアント](#クライアント)
* [チュートリアル](#チュートリアル)
* [コミュニティ](#コミュニティ)
* [凡例](#凡例)
* [サーバー実装](#サーバー実装)
* [フレームワーク](#フレームワーク)
* [ヒントとコツ](#ヒントとコツ)

## MCPとは何ですか？

[MCP](https://modelcontextprotocol.io/) は、標準化されたサーバー実装を通じて、AIモデルがローカルおよびリモートリソースと安全に対話できるようにするオープンプロトコルです。このリストは、ファイルアクセス、データベース接続、API統合、その他のコンテキストサービスを通じてAIの機能を拡張する、実運用および実験的なMCPサーバーに焦点を当てています。

## クライアント

[awesome-mcp-clients](https://github.com/punkpeye/awesome-mcp-clients/)と[glama.ai/mcp/clients](https://glama.ai/mcp/clients)をチェックしてください。

> [!TIP]
> [Glama Chat](https://glama.ai/chat)はMCPサポートと[AI gateway](https://glama.ai/gateway)を備えたマルチモーダルAIクライアントです。

## チュートリアル

* [モデルコンテキストプロトコル (MCP) クイックスタート](https://glama.ai/blog/2024-11-25-model-context-protocol-quickstart)
* [SQLiteデータベースを使用するためのClaudeデスクトップアプリのセットアップ](https://youtu.be/wxCCzo9dGj0)

## コミュニティ

* [r/mcp Reddit](https://www.reddit.com/r/mcp)
* [Discordサーバー](https://glama.ai/mcp/discord)

## 凡例

* 🎖️ – 公式実装
* プログラミング言語
  * 🐍 – Pythonコードベース
  * 📇 – TypeScriptコードベース
  * 🏎️ – Goコードベース
  * 🦀 – Rustコードベース
  * #️⃣ – C#コードベース
  * ☕ – Javaコードベース
  * 🌊 – C/C++コードベース
* スコープ
  * ☁️ – クラウドサービス
  * 🏠 – ローカルサービス
  * 📟 – 組み込みシステム
* 対応OS
  * 🍎 – macOS用
  * 🪟 – Windows用
  * 🐧 – Linux用

> [!NOTE]
> ローカル 🏠 とクラウド ☁️ の違いに迷っていますか？
> * MCPサーバーがローカルにインストールされたソフトウェアと通信する場合（例：Chromeブラウザの制御）には「ローカル 🏠」を使用してください。
> * MCPサーバーがリモートAPIと通信する場合（例：天気API）には「とクラウド ☁️」を使用してください。

## サーバー実装

> [!NOTE]
> 現在、リポジトリと同期されている[ウェブのディレクトリ](https://glama.ai/mcp/servers)があります。

* 🔗 - [アグリゲーター](#aggregators)
* 🎨 - [芸術と文化](#art-and-culture)
* 🧬 - [生物学、医学、バイオインフォマティクス](#bio)
* 📂 - [ブラウザ自動化](#browser-automation)
* ☁️ - [クラウドプラットフォーム](#cloud-platforms)
* 👨‍💻 - [コード実行](#code-execution)
* 🤖 - [コーディングエージェント](#coding-agents)
* 🖥️ - [コマンドライン](#command-line)
* 💬 - [コミュニケーション](#communication)
* 👤 - [顧客データプラットフォーム](#customer-data-platforms)
* 🗄️ - [データベース](#databases)
* 📊 - [データプラットフォーム](#data-platforms)
* 🚚 - [配送](#delivery)
* 🛠️ - [開発者ツール](#developer-tools)
* 🧮 - [データサイエンスツール](#data-science-tools)
* 📟 - [組み込みシステム](#embedded-system)
* 📂 - [ファイルシステム](#file-systems)
* 💰 - [金融・フィンテック](#finance--fintech)
* 🎮 - [ゲーミング](#gaming)
* 🧠 - [知識と記憶](#knowledge--memory)
* ⚖️ - [法律](#legal)
* 🗺️ - [位置情報サービス](#location-services)
* 🎯 - [マーケティング](#marketing)
* 📊 - [監視](#monitoring)
* 🎥 - [マルチメディア処理](#multimedia-process)
* 🔎 - [検索・データ抽出](#search)
* 🔒 - [セキュリティ](#security)
* 🌐 - [ソーシャルメディア](#social-media)
* 🏃 - [スポーツ](#sports)
* 🎧 - [サポート・サービス管理](#support-and-service-management)
* 🌎 - [翻訳サービス](#translation-services)
* 🎧 - [テキスト読み上げ](#text-to-speech)
* 🚆 - [旅行と交通](#travel-and-transportation)
* 🔄 - [バージョン管理](#version-control)
* 🛠️ - [その他のツールと統合](#other-tools-and-integrations)

### 🔗 <a name="aggregators"></a>アグリゲーター

単一のMCPサーバーを通じて多くのアプリやツールにアクセスするためのサーバー。

- [1mcp/agent](https://github.com/1mcp-app/agent) 📇 ☁️ 🏠 🍎 🪟 🐧 - 複数のMCPサーバーを1つのMCPサーバーに集約する統一的なモデルコンテキストプロトコルサーバー実装。
- [OpenMCP](https://github.com/wegotdocs/open-mcp) 📇 🏠 🍎 🪟 🐧 - Web APIを10秒でMCPサーバーに変換し、オープンソースレジストリに追加する: https://open-mcp.org
- [mindsdb/mindsdb](https://github.com/mindsdb/mindsdb) - [MindsDBを単一のMCPサーバーとして](https://docs.mindsdb.com/mcp/overview)使用し、様々なプラットフォームとデータベース間でデータを接続・統合
- [glenngillen/mcpmcp-server](https://github.com/glenngillen/mcpmcp-server) ☁️ 📇 🍎 🪟 🐧 - MCPサーバーのリストを提供し、日常のワークフローを改善するために使用できるサーバーをクライアントに問い合わせることができる
- [pipedream/pipedream](https://github.com/PipedreamHQ/pipedream/tree/master/modelcontextprotocol) ☁️ 🏠 - 8,000以上の事前構築ツールで2,500のAPIに接続し、独自のアプリでユーザー向けサーバーを管理
- [VeriTeknik/pluggedin-mcp-proxy](https://github.com/VeriTeknik/pluggedin-mcp-proxy) 📇 🏠 - 複数のMCPサーバーを1つのインターフェースに統合する包括的なプロキシサーバー。サーバー間でツール、プロンプト、リソース、テンプレートの発見と管理を提供し、MCPサーバー構築時のデバッグ用プレイグラウンドも含む
- [tigranbs/mcgravity](https://github.com/tigranbs/mcgravity) 📇 🏠 - 複数のMCPサーバーを1つの統一エンドポイントに構成するためのプロキシツール。Nginxがウェブサーバーのために機能するのと同様に、複数のMCPサーバー間でリクエストの負荷分散を行うことで、AIツールをスケーリングします。
- [MetaMCP](https://github.com/metatool-ai/metatool-app) 📇 ☁️ 🏠 🍎 🪟 🐧 - MetaMCPは、GUIでMCP接続を管理する統合ミドルウェアMCPサーバーです。
- [WayStation-ai/mcp](https://github.com/waystation-ai/mcp) ☁️ 🍎 🪟 - Claude Desktopやその他のMCPホストを、お気に入りのアプリ（Notion、Slack、Monday、Airtableなど）にシームレスかつ安全に接続。90秒以下で完了
- [MCP Access Point](https://github.com/sxhxliang/mcp-access-point)  📇 ☁️ 🏠 🍎 🪟 🐧 - サーバー側のコードに変更を加えることなく、Web API を 1 回のクリックで MCP サーバーに変換します。。
- [hamflx/imagen3-mcp](https://github.com/hamflx/imagen3-mcp) 📇 🏠 🪟 🍎 🐧 - MCPを通じてGoogleのImagen 3.0 APIを使用する強力な画像生成ツール。高度な写真、芸術的、写実的なコントロールでテキストプロンプトから高品質な画像を生成します。
- [SureScaleAI/openai-gpt-image-mcp](https://github.com/SureScaleAI/openai-gpt-image-mcp) 📇 ☁️ - OpenAI GPT画像生成・編集MCPサーバー
- [YangLiangwei/PersonalizationMCP](https://github.com/YangLiangwei/PersonalizationMCP) 🐍 ☁️ 🏠 🍎 🪟 🐧 - Steam、YouTube、Bilibili、Spotify、Redditなどのプラットフォームを統合した包括的な個人データ集約MCPサーバー。OAuth2認証、自動トークン管理、90+ツールでゲーム、音楽、動画、ソーシャルプラットフォームデータにアクセス。

### 🎨 <a name="art-and-culture"></a>芸術と文化

美術コレクション、文化遺産、博物館データベースにアクセスして探索できます。AIモデルは、芸術的および文化的なコンテンツを検索および分析できます。

- [abhiemj/manim-mcp-server](https://github.com/abhiemj/manim-mcp-server) 🐍 🏠 🪟 🐧 - Manimを使ってアニメーションを生成するローカルMCPサーバー
- [burningion/video-editing-mcp](https://github.com/burningion/video-editing-mcp) 🐍 - Video Jungle Collectionから動画編集の追加、分析、検索、生成
- [cswkim/discogs-mcp-server](https://github.com/cswkim/discogs-mcp-server) 📇 ☁️ - Discogs APIと連携するMCPサーバー
- [djalal/quran-mcp-server](https://github.com/djalal/quran-mcp-server) 📇 ☁️ 公式REST API v4を通してQuran.comコーパスと連携するMCPサーバー
- [gavxm/ani-mcp](https://github.com/gavxm/ani-mcp) [glama](https://glama.ai/mcp/servers/gavxm/ani-mcp) 📇 🏠 - 好みに応じたおすすめ、視聴分析、ソーシャルツール、リスト管理機能を備えたAniList MCPサーバー
- [mikechao/metmuseum-mcp](https://github.com/mikechao/metmuseum-mcp) 📇 ☁️ - コレクション内の芸術作品を検索・表示するメトロポリタン美術館コレクションAPI統合
- [r-huijts/rijksmuseum-mcp](https://github.com/r-huijts/rijksmuseum-mcp) 📇 ☁️ - 芸術作品検索、詳細、コレクションのためのライクスミュージアムAPI統合
- [r-huijts/oorlogsbronnen-mcp](https://github.com/r-huijts/oorlogsbronnen-mcp) 📇 ☁️ - オランダの歴史的第二次大戦記録、写真、文書（1940-1945）にアクセスするためのOorlogsbronnen（War Sources）API統合
- [samuelgursky/davinci-resolve-mcp](https://github.com/samuelgursky/davinci-resolve-mcp) 🐍 - 動画編集、カラーグレーディング、メディア管理、プロジェクト制御の強力なツールを提供するDaVinci Resolve用MCPサーバー統合
- [tasopen/mcp-alphabanana](https://github.com/tasopen/mcp-alphabanana) [glama](https://glama.ai/mcp/servers/@tasopen/mcp-alphabanana) 📇 🏠 🍎 🪟 🐧 - Google Gemini（Nano Banana 2 / Pro）で画像アセットを生成するローカルMCPサーバー。透過PNG/WebP出力、正確なリサイズ/クロップ、最大14枚の参照画像、Google検索グラウンディングに対応。
- [yuna0x0/anilist-mcp](https://github.com/yuna0x0/anilist-mcp) 📇 ☁️ - アニメとマンガの情報をAniList APIと連携するMCPサーバー
- [diivi/aseprite-mcp](https://github.com/diivi/aseprite-mcp) 🐍 🏠 - Aseprite APIを使用してピクセルアートを作成するMCPサーバー
- [omni-mcp/isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp) 📇 ☁️ - NVIDIA Isaac Sim、Lab、OpenUSDなどの自然言語制御を可能にするMCPサーバーと拡張機能
- [8enSmith/mcp-open-library](https://github.com/8enSmith/mcp-open-library) 📇 ☁️ - AIアシスタントが書籍情報を検索できるOpen Library API用MCPサーバー
- [PatrickPalmer/MayaMCP](https://github.com/PatrickPalmer/MayaMCP) 🐍 🏠 - Autodesk Maya用MCPサーバー
- [cantian-ai/bazi-mcp](https://github.com/cantian-ai/bazi-mcp) 📇 🏠 ☁️ 🍎 🪟 - 包括的で正確な八字（四柱推命）の命式作成と占い情報を提供

### 🧬 <a name="bio"></a>生物学、医学、バイオインフォマティクス

- [genomoncology/biomcp](https://github.com/genomoncology/biomcp) 🐍 ☁️ - PubMed、ClinicalTrials.gov、MyVariant.infoへのアクセスを提供する生物医学研究用MCPサーバー。
- [longevity-genie/biothings-mcp](https://github.com/longevity-genie/biothings-mcp) 🐍 🏠 ☁️ - 遺伝子、遺伝的変異、薬物、分類学情報を含むBioThings APIと相互作用するMCPサーバー。
- [longevity-genie/gget-mcp](https://github.com/longevity-genie/gget-mcp) 🐍 🏠 ☁️ - 人気の`gget`ライブラリをラップした、ゲノムクエリと解析のための強力なバイオインフォマティクスツールキットを提供するMCPサーバー。
- [longevity-genie/opengenes-mcp](https://github.com/longevity-genie/opengenes-mcp) 🎖️ 🐍 🏠 ☁️ - OpenGenesプロジェクトの老化と長寿研究のためのクエリ可能なデータベース用MCPサーバー。
- [longevity-genie/synergy-age-mcp](https://github.com/longevity-genie/synergy-age-mcp) 🎖️ 🐍 🏠 ☁️ - 長寿における相乗的および拮抗的遺伝的相互作用のSynergyAgeデータベース用MCPサーバー。
- [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) 🐍 🏠 ☁️ - 高速医療相互運用性リソース（FHIR）API用モデルコンテキストプロトコルサーバー。FHIRサーバーとのシームレスな統合を提供し、AIアシスタントがSMART-on-FHIR認証サポートを使用して臨床医療データの検索、取得、作成、更新、分析を可能にします。

### ☁️ <a name="cloud-platforms"></a>クラウドプラットフォーム

クラウドプラットフォームサービスの統合。クラウドインフラストラクチャとサービスの管理と対話を可能にします。

- [Nebula-Block-Data/nebulablock-mcp-server](https://github.com/Nebula-Block-Data/nebulablock-mcp-server) 📇 🏠 - fastmcp ライブラリと統合し、NebulaBlock のすべての API 機能をツールとして提供します。
- [4everland/4everland-hosting-mcp](https://github.com/4everland/4everland-hosting-mcp) 🎖️ 📇 🏠 🍎 🐧 - Greenfield、IPFS、Arweaveなどの分散型ストレージネットワークにAI生成コードをすぐにデプロイできる4EVERLAND Hosting用MCPサーバー実装。
- [awslabs/mcp](https://github.com/awslabs/mcp) 🎖️ ☁️ - AWSサービスとリソースとのシームレスな統合のためのAWS MCPサーバー。
- [qiniu/qiniu-mcp-server](https://github.com/qiniu/qiniu-mcp-server) 🐍 ☁️ - 七牛クラウド製品に基づいて構築されたMCP、七牛クラウドストレージ、メディア処理サービスなどへのアクセスをサポート。
- [alexbakers/mcp-ipfs](https://github.com/alexbakers/mcp-ipfs) 📇 ☁️ - IPFSストレージのアップロードと操作
- [reza-gholizade/k8s-mcp-server](https://github.com/reza-gholizade/k8s-mcp-server) 🏎️ ☁️🏠 - API リソース検出、リソース管理、Pod ログ、メトリクス、イベントなど、標準化されたインターフェースを通じて Kubernetes クラスターと対話するためのツールを提供する Kubernetes モデルコンテキストプロトコル（MCP）サーバー。
- [VmLia/books-mcp-server](https://github.com/VmLia/books-mcp-server) 📇 ☁️ - 書籍クエリに使用されるMCPサーバーで、Cherry Studioなどの一般的なMCPクライアントに適用できます。
