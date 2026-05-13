# Missing Repo Summary Source: kzhrknt/awesome-design-md-jp

- URL: https://github.com/kzhrknt/awesome-design-md-jp
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/kzhrknt__awesome-design-md-jp
- Clone Status: cloned
- Language: HTML
- Stars: 663
- Topics: 
- Description: 日本語UIをAIエージェントに正しくつくらせるためのDESIGN.md集。Japanese DESIGN.md collection for AI agents — extending Google Stitch format with CJK typography.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="designmd-jp.jpg" alt="Awesome Design MD JP" width="100%">
</p>

# Awesome Design MD JP

> A curated collection of `DESIGN.md` files for Japanese web services — enabling AI agents to generate accurate Japanese UI with proper typography, font stacks, and typographic rules.

**[日本語](#日本語) | [English](#english)**

---

## 日本語

### DESIGN.md とは

[DESIGN.md](https://stitch.withgoogle.com/docs/design-md/overview/) は Google Stitch が提唱するフォーマットで、AIエージェントが一貫したUIを生成するためのデザイン仕様書です。プレーンテキストのMarkdownで記述し、コードベースに `AGENTS.md`（作り方）と並べて `DESIGN.md`（見た目と雰囲気）として配置します。

### なぜ日本語版が必要か

既存の [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) は欧米の55以上のサービスをカバーしていますが、**日本語タイポグラフィの仕様は完全に欠落しています**。日本語UIには根本的に異なるタイポグラフィ仕様が必要です：

- **和文フォントのフォールバックチェーン**（和文 → 欧文 → generic）
- **広い行間**（line-height 1.5〜2.0、欧文の1.4〜1.5とは異なる）
- **日本語の字間**（本文に0.04〜0.1em程度）
- **禁則処理**（句読点や括弧の行頭・行末ルール）
- **OpenType機能**（`palt`, `kern` によるプロポーショナル組版）
- **混植ルール**（和文と欧文の組み合わせ規則）

これらの仕様がなければ、AIエージェントは間違ったフォント、詰まった行間、壊れた句読点処理の日本語UIを生成してしまいます。

### プレビュー

各 DESIGN.md のデザイントークンを可視化したショーケースページ（`preview.html`）を同梱しています。

<p align="center">
  <a href="https://kzhrknt.github.io/awesome-design-md-jp/gallery.html">Gallery (182 sites)</a>
</p>

<table>
<tr>
<td align="center"><strong>Apple</strong><br><img src="design-md/apple/preview-screenshot.png" width="120"></td>
<td align="center"><strong>MUJI</strong><br><img src="design-md/muji/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Mercari</strong><br><img src="design-md/mercari/preview-screenshot.png" width="120"></td>
<td align="center"><strong>STUDIO</strong><br><img src="design-md/studio/preview-screenshot.png" width="120"></td>
<td align="center"><strong>SmartHR</strong><br><img src="design-md/smarthr/preview-screenshot.png" width="120"></td>
<td align="center"><strong>freee</strong><br><img src="design-md/freee/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>note</strong><br><img src="design-md/note/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Novasell</strong><br><img src="design-md/novasell/preview-screenshot.png" width="120"></td>
<td align="center"><strong>WIRED</strong><br><img src="design-md/wired/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Toyota</strong><br><img src="design-md/toyota/preview-screenshot.png" width="120"></td>
<td align="center"><strong>LINE</strong><br><img src="design-md/line/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Cookpad</strong><br><img src="design-md/cookpad/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>MF</strong><br><img src="design-md/moneyforward/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Cybozu</strong><br><img src="design-md/cybozu/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Qiita</strong><br><img src="design-md/qiita/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Rakuten</strong><br><img src="design-md/rakuten/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Tabelog</strong><br><img src="design-md/tabelog/preview-screenshot.png" width="120"></td>
<td align="center"><strong>pixiv</strong><br><img src="design-md/pixiv/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>Zenn</strong><br><img src="design-md/zenn/preview-screenshot.png" width="120"></td>
<td align="center"><strong>connpass</strong><br><img src="design-md/connpass/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Sansan</strong><br><img src="design-md/sansan/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Notion</strong><br><img src="design-md/notion/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ABEMA</strong><br><img src="design-md/abema/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Droga5</strong><br><img src="design-md/droga5/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>三菱地所</strong><br><img src="design-md/mec/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Nintendo</strong><br><img src="design-md/nintendo/preview-screenshot.png" width="120"></td>
<td align="center"><strong>UNIQLO</strong><br><img src="design-md/uniqlo/preview-screenshot.png" width="120"></td>
<td align="center"><strong>星野リゾート</strong><br><img src="design-md/hoshinoresorts/preview-screenshot.png" width="120"></td>
<td align="center"><strong>デジタル庁</strong><br><img src="design-md/digital-go/preview-screenshot.png" width="120"></td>
<td align="center"><strong>PayPay</strong><br><img src="design-md/paypay/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>日経電子版</strong><br><img src="design-md/nikkei/preview-screenshot.png" width="120"></td>
<td align="center"><strong>MOSH</strong><br><img src="design-md/mosh/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Shiseido</strong><br><img src="design-md/shiseido/preview-screenshot.png" width="120"></td>
<td align="center"><strong>STORES</strong><br><img src="design-md/stores/preview-screenshot.png" width="120"></td>
<td align="center"><strong>一休.com</strong><br><img src="design-md/ikyu/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Wantedly</strong><br><img src="design-md/wantedly/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>Snow Peak</strong><br><img src="design-md/snowpeak/preview-screenshot.png" width="120"></td>
<td align="center"><strong>JINS</strong><br><img src="design-md/jins/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ヤマハ</strong><br><img src="design-md/yamaha/preview-screenshot.png" width="120"></td>
<td align="center"><strong>BAKE</strong><br><img src="design-md/bake/preview-screenshot.png" width="120"></td>
<td align="center"><strong>nendo</strong><br><img src="design-md/nendo/preview-screenshot.png" width="120"></td>
<td align="center"><strong>BEAMS</strong><br><img src="design-md/beams/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>サンリオ</strong><br><img src="design-md/sanrio/preview-screenshot.png" width="120"></td>
<td align="center"><strong>吉田カバン</strong><br><img src="design-md/yoshidakaban/preview-screenshot.png" width="120"></td>
<td align="center"><strong>中川政七商店</strong><br><img src="design-md/nakagawa/preview-screenshot.png" width="120"></td>
<td align="center"><strong>POLA</strong><br><img src="design-md/pola/preview-screenshot.png" width="120"></td>
<td align="center"><strong>D&amp;DEPARTMENT</strong><br><img src="design-md/ddepartment/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Takram</strong><br><img src="design-md/takram/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>KOKUYO</strong><br><img src="design-md/kokuyo/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Gマーク</strong><br><img src="design-md/g-mark/preview-screenshot.png" width="120"></td>
<td align="center"><strong>teamLab</strong><br><img src="design-md/teamlab/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ISSEY MIYAKE</strong><br><img src="design-md/isseymiyake/preview-screenshot.png" width="120"></td>
<td align="center"><strong>SOU・SOU</strong><br><img src="design-md/sousou/preview-screenshot.png" width="120"></td>
<td align="center"><strong>PARCO</strong><br><img src="design-md/parco/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>とらや</strong><br><img src="design-md/toraya/preview-screenshot.png" width="120"></td>
<td align="center"><strong>IDÉE</strong><br><img src="design-md/idee/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Mazda</strong><br><img src="design-md/mazda/preview-screenshot.png" width="120"></td>
<td align="center"><strong>BRUTUS</strong><br><img src="design-md/brutus/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ACTUS</strong><br><img src="design-md/actus/preview-screenshot.png" width="120"></td>
<td align="center"><strong>KINTO</strong><br><img src="design-md/kinto/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>21_21 DS</strong><br><img src="design-md/2121designsight/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Pen Online</strong><br><img src="design-md/penonline/preview-screenshot.png" width="120"></td>
<td align="center"><strong>LEXUS</strong><br><img src="design-md/lexus/preview-screenshot.png" width="120"></td>
<td align="center"><strong>マルニ木工</strong><br><img src="design-md/maruni/preview-screenshot.png" width="120"></td>
<td align="center"><strong>POPEYE</strong><br><img src="design-md/popeye/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ミナ ペルホネン</strong><br><img src="design-md/mina-perhonen/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>NDC</strong><br><img src="design-md/ndc/preview-screenshot.png" width="120"></td>
<td align="center"><strong>代官山 蔦屋書店</strong><br><img src="design-md/daikanyama-tsite/preview-screenshot.png" width="120"></td>
<td align="center"><strong>BALMUDA</strong><br><img src="design-md/balmuda/preview-screenshot.png" width="120"></td>
<td align="center"><strong>ほぼ日</strong><br><img src="design-md/hobonichi/preview-screenshot.png" width="120"></td>
<td align="center"><strong>±0</strong><br><img src="design-md/plusminuszero/preview-screenshot.png" width="120"></td>
<td align="center"><strong>サントリー</strong><br><img src="design-md/suntory/preview-screenshot.png" width="120"></td>
</tr>
<tr>
<td align="center"><strong>GINZA SIX</strong><br><img src="design-md/ginza6/preview-screenshot.png" width="120"></td>
<td align="center"><strong>東京ミッドタウン</strong><br><img src="design-md/tokyo-midtown/preview-screenshot.png" width="120"></td>
<td align="center"><strong>Casa BRUTUS</strong><br
