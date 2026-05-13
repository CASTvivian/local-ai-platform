# Missing Repo Summary Source: supermemoryai/supermemory

- URL: https://github.com/supermemoryai/supermemory
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/supermemoryai__supermemory
- Clone Status: cloned
- Language: TypeScript
- Stars: 22535
- Topics: agent-memory, ai-memory, cloudflare-kv, cloudflare-pages, cloudflare-workers, drizzle-orm, memory, postgres, remix, tailwindcss, typescript, vite
- Description: Memory engine and app that is extremely fast, scalable. The Memory API for the AI era.

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <picture>
    <source srcset="apps/web/public/logo-fullmark.svg" media="(prefers-color-scheme: dark)">
    <source srcset="apps/web/public/logo-light-fullmark.svg" media="(prefers-color-scheme: light)">
    <img src="apps/web/public/logo-fullmark.svg" alt="Supermemory" width="400" />
  </picture>
</p>

<p align="center">
  <strong>State-of-the-art memory and context engine for AI.</strong>
</p>

<p align="center">
  <a href="https://supermemory.ai/docs">Docs</a> ·
  <a href="https://supermemory.ai/docs/quickstart">Quickstart</a> ·
  <a href="https://console.supermemory.ai">Dashboard</a> ·
  <a href="https://supermemory.link/discord">Discord</a>
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/supermemory"><img src="https://img.shields.io/npm/v/supermemory?style=flat-square&color=blue" alt="npm" /></a>
  <a href="https://pypi.org/project/supermemory/"><img src="https://img.shields.io/pypi/v/supermemory?style=flat-square&color=blue" alt="pypi" /></a>
  <a href="https://supermemory.ai/docs"><img src="https://img.shields.io/badge/docs-supermemory.ai-blue?style=flat-square" alt="docs" /></a>
</p>

---

Supermemory is the memory and context layer for AI. **#1 on [LongMemEval](https://github.com/xiaowu0162/LongMemEval), [LoCoMo](https://github.com/snap-research/locomo), and [ConvoMem](https://github.com/Salesforce/ConvoMem)** — the three major benchmarks for AI memory. 

We are a research lab building the engine, plugins and tools around it.

Your AI forgets everything between conversations. Supermemory fixes that.

It automatically learns from conversations, extracts facts, builds user profiles, handles knowledge updates and contradictions, forgets expired information, and delivers the right context at the right time. Full RAG, connectors, file processing — the entire context stack, one system.

| | |
|---|---|
| 🧠 **Memory** | Extracts facts from conversations. Handles temporal changes, contradictions, and automatic forgetting. |
| 👤 **User Profiles** | Auto-maintained user context — stable facts + recent activity. One call, ~50ms. |
| 🔍 **Hybrid Search** | RAG + Memory in a single query. Knowledge base docs and personalized context together. |
| 🔌 **Connectors** | Google Drive · Gmail · Notion · OneDrive · GitHub — auto-sync with real-time webhooks. |
| 📄 **Multi-modal Extractors** | PDFs, images (OCR), videos (transcription), code (AST-aware chunking). Upload and it works. |

All of this is in our single memory structure and ontology. 

<img width="1414" height="937" alt="image" src="https://github.com/user-attachments/assets/8863b6d9-c043-4c75-b200-4f1759e7edaf" />


---

## Use Supermemory

<table>
<tr>
<td width="50%" valign="top">

<h3>🧑‍💻 I use AI tools</h3>

Build your own personal supermemory by using our app. Builds **persistent memory graph across every conversation**.

Your AI remembers your preferences, projects, past discussions — and gets smarter over time.

**[→ Jump to User setup](#give-your-ai-memory)**

</td>
<td width="50%" valign="top">

<h3>🔧 I'm building AI products</h3>

Add memory, RAG, user profiles, and connectors to your agents and apps with **a single API**.

No vector DB config. No embedding pipelines. No chunking strategies.

**[→ Jump to developer quickstart](#build-with-supermemory-api)**

</td>
</tr>
</table>

---

## Give your AI memory

The Supermemory App, browser extension, plugins and MCP server gives any compatible AI assistant persistent memory. One install, and your AI remembers you.

### The app

You can use supermemory without any code, by using our consumer-facing app for free.

Start at https://app.supermemory.ai

<img width="1705" height="1030" alt="image" src="https://github.com/user-attachments/assets/5b43af30-b998-4585-8de6-f3e9a26d894a" />

It also comes with an agent embedded inside, which we call Nova.

### Supermemory Plugins

Supermemory comes built with Plugins for Claude Code, OpenCode, OpenClaw, and Hermes.

<img width="844" height="484" alt="image" src="https://github.com/user-attachments/assets/ecb879a2-8652-495d-9228-f305a97ba603" />

These plugins are implementations of the supermemory API, and they are open source! 

You can find them here: 

- Openclaw plugin: https://github.com/supermemoryai/openclaw-supermemory
- Claude code plugin: https://github.com/supermemoryai/claude-supermemory
- OpenCode plugin: https://github.com/supermemoryai/opencode-supermemory
- Hermes agent (Supermemory memory provider): https://github.com/NousResearch/hermes-agent

### MCP - Quick install

```bash
npx -y install-mcp@latest https://mcp.supermemory.ai/mcp --client claude --oauth=yes
```

Replace `claude` with your client: `cursor`, `windsurf`, `vscode`, etc.

Read more about our MCP here - https://supermemory.ai/docs/supermemory-mcp/mcp

### What your AI gets

| Tool | What it does |
|---|---|
| `memory` | Save or forget information. Your AI calls this automatically when you share something worth remembering. |
| `recall` | Search memories by query. Returns relevant memories + your user profile summary. |
| `context` | Injects your full profile (preferences, recent activity) into the conversation at start. In Cursor and Claude Code, just type `/context`. |

### How it works

Once installed, Supermemory runs in the background:

1. **You talk to your AI normally.** Share preferences, mention projects, discuss problems.
2. **Supermemory extracts and stores the important stuff.** Facts, preferences, project context — not noise.
3. **Next conversation, your AI already knows you.** It recalls what you're working on, how you like things, what you discussed before.

Memory is scoped with **projects** (container tags) so you can separate work and personal context, or organize by client, repo, or anything else.

### Supported clients

**Claude Desktop** · **Cursor** · **Windsurf** · **VS Code** · **Claude Code** · **OpenCode** · **OpenClaw** · **Hermes**

The MCP server is open source — [view the source](https://supermemory.ai/docs/supermemory-mcp/mcp).

### Manual configuration

Add this to your MCP client config:

```json
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp"
    }
  }
}
```

Or use an API key instead of OAuth:

```json
{
  "mcpServers": {
    "supermemory": {
      "url": "https://mcp.supermemory.ai/mcp",
      "headers": {
        "Authorization": "Bearer sm_your_api_key_here"
      }
    }
  }
}
```

---

## Build with Supermemory (API)

If you're building AI agents or apps, Supermemory gives you the entire context stack through one API — memory, RAG, user profiles, connectors, and file processing.

### Install

```bash
npm install supermemory    # or: pip install supermemory
```

### Quickstart

```typescript
import Supermemory from "supermemory";

const client = new Supermemory();

// Store a conversation
await client.add({
  content: "User loves TypeScript and prefers functional patterns",
  containerTag: "user_123",
});

// Get user profile + relevant memories in one call
const { profile, searchResults } = await client.profile({
  containerTag: "user_123",
  q: "What programming style does the user prefer?",
});

// profile.static  → ["Loves TypeScript", "Prefers functional patterns"]
// profile.dynamic → ["Working on API integration"]
// searchResults   → Relevant memories ranked by similarity
```

```python
from supermemory import Supermemory

client = Supermemory()

client.add(
    content="User loves TypeScript and prefers functional patterns",
    container_tag="user_123"
)

result = client.profile(container_tag="user_123", q="programming style")

print(result.profile.static)   # Long-term facts
print(result.profile.dynamic)  # Recent context
```

Supermemory automatically extracts memories, builds user profiles, and returns relevant context. No embedding pipelines, no vector DB config, no chunking strategies.

### Framework integrations

Drop-in wrappers for every major AI framework:

```typescript
// Vercel AI SDK
import { withSupermemory } from "@supermemory/tools/ai-sdk";
const model = withSupermemory(openai("gpt-4o"), { containerTag: "user_123", customId: "conv-1" });

// Mastra
import { withSupermemory } from "@supermemory/tools/mastra";
const agent = new Agent(withSupermemory(config, "user-123", { mode: "full" }));
```

**Vercel AI SDK** · **LangChain** · **LangGraph** · **OpenAI Agents SDK** · **Mastra** · **Agno** · **Claude Memory Tool** · **n8n**

### Search modes

```typescript
// Hybrid (default) — RAG + Memory in one query
const results = await client.search.memories({
  q: "how do I deploy?",
  containerTag: "user_123",
  searchMode: "hybrid",
});
// Returns deployment docs (RAG) + user's deploy preferences (Memory)

// Memories only
const results = await client.search.memories({
  q: "user preferences",
  containerTag: "user_123",
  searchMode: "memories",
});
```

### User profiles

Traditional memory relies on search — you need to know what to ask for. Supermemory automatically maintains a profile for every user:

```typescript
const { profile } = await client.profile({ containerTag: "user_123" });

// profile.static  → ["Senior engineer at Acme", "Prefers dark mode", "Uses Vim"]
// profile.dynamic → ["Working on auth migration", "Debugging rate limits"]
```

One call. ~50ms. Inject into your system prompt and your agent instantly knows who it's talking to.

### Connectors

Auto-sync external data into your knowledge base:

**Google Drive** · **Gmail** · **Notion** · **OneDrive** · **GitHub** · **Web Crawler**

Real-time webhooks. Documents automatically processed, chunked, and searchable.

### API at a glance

| Method | Purpose |
|---|---|
| `client.add()` | Store content — text, conversations, URLs, HTML |
| `client.profile()` | User profile + optional search in one call |
| `client.search.memories()` | Hybrid search across memories and documents |
| `client.search.documents()` | Document search with metadata filters |
| `client.documents.uploadFile()` | Upload
