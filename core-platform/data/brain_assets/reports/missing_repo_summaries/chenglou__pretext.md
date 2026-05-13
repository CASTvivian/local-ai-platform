# Missing Repo Summary Source: chenglou/pretext

- URL: https://github.com/chenglou/pretext
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/chenglou__pretext
- Clone Status: cloned
- Language: TypeScript
- Stars: 46781
- Topics: 
- Description: Fast, accurate & comprehensive text measurement & layout

## Extracted README / Docs / Examples



# FILE: README.md

# Pretext

Pure JavaScript/TypeScript library for multiline text measurement & layout. Fast, accurate & supports all the languages you didn't even know about. Allows rendering to DOM, Canvas, SVG and soon, server-side.

Pretext side-steps the need for DOM measurements (e.g. `getBoundingClientRect`, `offsetHeight`), which trigger layout reflow, one of the most expensive operations in the browser. It implements its own text measurement logic, using the browsers' own font engine as ground truth (very AI-friendly iteration method).

## Installation

```sh
npm install @chenglou/pretext
```

## Demos

Clone the repo, run `bun install`, then `bun start`, and open `/demos/index` in your browser. On Windows, use `bun run start:windows`.
Alternatively, see them live at [chenglou.me/pretext](https://chenglou.me/pretext/). Some more at [somnai-dreams.github.io/pretext-demos](https://somnai-dreams.github.io/pretext-demos/)

## API

Pretext serves 2 use cases:

### 1. Measure a paragraph's height _without ever touching DOM_

```ts
import { prepare, layout } from '@chenglou/pretext'

const prepared = prepare('AGI 春天到了. بدأت الرحلة 🚀‎', '16px Inter')
const { height, lineCount } = layout(prepared, 320, 20) // pure arithmetic. No DOM layout & reflow!
```

`prepare()` does the one-time work: normalize whitespace, segment the text, apply glue rules, measure the segments with canvas, and return an opaque handle. `layout()` is the cheap hot path after that: pure arithmetic over cached widths. Do not rerun `prepare()` for the same text and configs; that'd defeat its precomputation. For example, on resize, only rerun `layout()`.

If you want textarea-like text where ordinary spaces, `\t` tabs, and `\n` hard breaks stay visible, pass `{ whiteSpace: 'pre-wrap' }` to `prepare()`:

```ts
const prepared = prepare(textareaValue, '16px Inter', { whiteSpace: 'pre-wrap' })
const { height } = layout(prepared, textareaWidth, 20)
```

Other `prepare()` options are `{ wordBreak: 'keep-all' }` for CSS-like `word-break: keep-all`, and `{ letterSpacing: n }` to match CSS `letter-spacing` (`n` is treated as a px value).

The returned height is the crucial last piece for unlocking web UIs:
- proper virtualization/occlusion without guesstimates & caching
- fancy userland layouts: masonry, JS-driven flexbox-like implementations, nudging a few layout values without CSS hacks (imagine that), etc.
- _development time_ verification (especially now with AI) that labels on e.g. buttons don't overflow to the next line, browser-free
- prevent layout shift when new text loads and you wanna re-anchor the scroll position

### 2. Lay out the paragraph lines manually yourself

Switch out `prepare` with `prepareWithSegments`, then:

- `layoutWithLines()` gives you all the lines at a fixed width:

```ts
import { prepareWithSegments, layoutWithLines } from '@chenglou/pretext'

const prepared = prepareWithSegments('AGI 春天到了. بدأت الرحلة 🚀', '18px "Helvetica Neue"')
const { lines } = layoutWithLines(prepared, 320, 26) // 320px max width, 26px line height
for (let i = 0; i < lines.length; i++) ctx.fillText(lines[i].text, 0, i * 26)
```

- `measureLineStats()` and `walkLineRanges()` give you line counts, widths and cursors without building the text strings:

```ts
import { measureLineStats, walkLineRanges } from '@chenglou/pretext'

const { lineCount, maxLineWidth } = measureLineStats(prepared, 320)
let maxW = 0
walkLineRanges(prepared, 320, line => { if (line.width > maxW) maxW = line.width })
// maxW is now the widest line — the tightest container width that still fits the text! This multiline "shrink wrap" has been missing from web
```

- `layoutNextLineRange()` lets you route text one row at a time when width changes as you go. If you want the actual string too, `materializeLineRange()` turns that one range back into a full line:

```ts
import { layoutNextLineRange, materializeLineRange, prepareWithSegments, type LayoutCursor } from '@chenglou/pretext'

const prepared = prepareWithSegments(article, BODY_FONT)
let cursor: LayoutCursor = { segmentIndex: 0, graphemeIndex: 0 }
let y = 0

// Flow text around a floated image: lines beside the image are narrower
while (true) {
  const width = y < image.bottom ? columnWidth - image.width : columnWidth
  const range = layoutNextLineRange(prepared, cursor, width)
  if (range === null) break

  const line = materializeLineRange(prepared, range)
  ctx.fillText(line.text, 0, y)
  cursor = range.end
  y += 26
}
```

This usage allows rendering to canvas, SVG, WebGL and (eventually) server-side. See the `/demos/dynamic-layout` demo for a richer example.

For hyphenation in manual layout, insert soft hyphens before `prepare()` / `prepareWithSegments()`. Pretext treats them as optional break points: unchosen soft hyphens stay invisible, while chosen breaks materialize as a trailing `-`. For mixed-language or user-generated app text, prefer conservative, locale-aware insertion over aggressive pattern hyphenation. Automatic hyphenation is not built in today.

If your manual layout needs a small helper for rich-text inline flow, code spans, mentions, chips, and browser-like boundary whitespace collapse, there is a helper at `@chenglou/pretext/rich-inline`. It stays inline-only and `white-space: normal`-only on purpose:

```ts
import { materializeRichInlineLineRange, prepareRichInline, walkRichInlineLineRanges } from '@chenglou/pretext/rich-inline'

const prepared = prepareRichInline([
  { text: 'Ship ', font: '500 17px Inter' },
  { text: '@maya', font: '700 12px Inter', break: 'never', extraWidth: 22 },
  { text: "'s rich-note", font: '500 17px Inter' },
])

walkRichInlineLineRanges(prepared, 320, range => {
  const line = materializeRichInlineLineRange(prepared, range)
  // each fragment keeps its source item index, text slice, gapBefore, and cursors
})
```

It is intentionally narrow:
- raw inline text in, including boundary spaces
- caller-owned `extraWidth` for pill chrome
- `break: 'never'` for atomic items like chips and mentions
- `white-space: normal` only
- not a nested markup tree and not a general CSS inline formatting engine

### API Glossary

Use-case 1 APIs:
```ts
prepare(text: string, font: string, options?: { whiteSpace?: 'normal' | 'pre-wrap', wordBreak?: 'normal' | 'keep-all', letterSpacing?: number }): PreparedText // one-time text analysis + measurement pass, returns an opaque value to pass to `layout()`. Make sure `font` and `letterSpacing` are synced with your CSS for the text you're measuring. `font` is the same format as what you'd use for `myCanvasContext.font = ...`, e.g. `16px Inter`; `letterSpacing` is a CSS pixel value.
layout(prepared: PreparedText, maxWidth: number, lineHeight: number): { height: number, lineCount: number } // calculates text height given a max width and lineHeight. Make sure `lineHeight` is synced with your css `line-height` declaration for the text you're measuring.
```

Use-case 2 APIs:
```ts
prepareWithSegments(text: string, font: string, options?: { whiteSpace?: 'normal' | 'pre-wrap', wordBreak?: 'normal' | 'keep-all', letterSpacing?: number }): PreparedTextWithSegments // same as `prepare()`, but returns a richer structure for manual line layout needs
layoutWithLines(prepared: PreparedTextWithSegments, maxWidth: number, lineHeight: number): { height: number, lineCount: number, lines: LayoutLine[] } // high-level api for manual layout needs. Accepts a fixed max width for all lines. Similar to `layout()`'s return, but additionally returns the lines info
walkLineRanges(prepared: PreparedTextWithSegments, maxWidth: number, onLine: (line: LayoutLineRange) => void): number // low-level api for manual layout needs. Accepts a fixed max width for all lines. Calls `onLine` once per line with its actual calculated line width and start/end cursors, without building line text strings. Very useful for certain cases where you wanna speculatively test a few width and height boundaries (e.g. binary search a nice width value by repeatedly calling walkLineRanges and checking the line count, and therefore height, is "nice" too). You can have text messages shrinkwrap and balanced text layout this way. After walkLineRanges calls, you'd call layoutWithLines once, with your satisfying max width, to get the actual lines info.
measureLineStats(prepared: PreparedTextWithSegments, maxWidth: number): { lineCount: number, maxLineWidth: number } // returns only how many lines this width produces, and how wide the widest one is. Avoids line/string allocations.
measureNaturalWidth(prepared: PreparedTextWithSegments): number // returns the widest forced line when width itself is not the thing causing wraps
layoutNextLine(prepared: PreparedTextWithSegments, start: LayoutCursor, maxWidth: number): LayoutLine | null // iterator-like api for laying out each line with a different width! Returns the LayoutLine starting from `start`, or `null` when the paragraph's exhausted. Pass the previous line's `end` cursor as the next `start`.
layoutNextLineRange(prepared: PreparedTextWithSegments, start: LayoutCursor, maxWidth: number): LayoutLineRange | null // same as layoutNextLine(), but without allocating line text strings. Useful for variable-width manual layout, occlusion, and virtualization measurements.
materializeLineRange(prepared: PreparedTextWithSegments, line: LayoutLineRange): LayoutLine // turns a LayoutLineRange from layoutNextLineRange() or walkLineRanges() into a full line with text
type LineStats = {
  lineCount: number // Number of wrapped lines, e.g. 3
  maxLineWidth: number // Widest wrapped line, e.g. 192.5
}
type LayoutLine = {
  text: string // Full text content of this line, e.g. 'hello world'
  width: number // Measured width of this line, e.g. 87.5
  start: LayoutCursor // Inclusive start cursor in prepared segments/graphemes
  end: LayoutCursor // Exclusive end cursor in prepared segments/graphemes
}
type LayoutLineRange = {
  width: number // Measured width of this line, e.g. 87.5
  start: LayoutCursor 
