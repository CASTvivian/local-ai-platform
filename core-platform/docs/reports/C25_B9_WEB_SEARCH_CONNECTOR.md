# C25-B9 Web Search Connector

## Status
Implemented.

## What Changed
- Added web search runtime.
- Added DuckDuckGo HTML and lite search parsing with Bing HTML fallback.
- Added optional top-result `browser.fetch` snapshot capture.
- Added web search persistence.
- Added web search execution audit records.
- Enabled `web.search` MCP tool.
- Enabled `web.search` capability.
- Added Agent executor integration for `web.search`.
- Added renderer output for web evidence.

## New APIs
- `POST /agent/web/search`
- `GET /agent/web/searches`

## Updated MCP Tool
- `web.search` is now enabled.

## Runtime Effect
Factual web questions can now follow this path:

```text
web.search -> browser.fetch -> snapshot -> execution audit -> answer with evidence
```

## Notes
If DuckDuckGo is blocked or returns unparsable HTML, the runtime attempts DuckDuckGo Lite and then Bing HTML before returning an error.
