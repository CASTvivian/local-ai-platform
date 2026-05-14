# C25-B8 Browser Runtime Boundary

## Status
Implemented.

## What Changed
- Added read-only browser fetch runtime.
- Added SSRF protection for localhost, private, link-local, multicast and unspecified IPs.
- Limited fetches to public `http` and `https` URLs.
- Added browser snapshot persistence.
- Added execution audit records for browser fetch attempts.
- Added `browser.fetch` MCP tool.
- Added `browser.fetch` capability.
- Added browser snapshot APIs.

## New APIs
- `POST /agent/browser/fetch`
- `GET /agent/browser/snapshots`
- `GET /agent/browser/snapshot/{snapshot_id}`

## New MCP Tool
- `browser.fetch`

## Runtime Effect
Agent Runtime can now fetch public webpages into local snapshots without controlling the user's browser.

```text
browser.fetch -> SSRF guard -> snapshot -> execution audit
```

## Safety Notes
- `localhost`, loopback, private, link-local and multicast network targets are blocked.
- Browser runtime is read-only.
- Full browser control remains out of scope for this step.
