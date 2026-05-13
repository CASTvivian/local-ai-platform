# Missing Repo Summary Source: nikmcfly/MiroFish-Offline

- URL: https://github.com/nikmcfly/MiroFish-Offline
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/nikmcfly__MiroFish-Offline
- Clone Status: cloned
- Language: Python
- Stars: 2154
- Topics: ai, multi-agent, neo4j, offline, ollama, open-source, prediction, simulation, swarm-intelligence, vue
- Description: Offline multi-agent simulation & prediction engine. English fork of MiroFish with Neo4j + Ollama local stack.

## Extracted README / Docs / Examples



# FILE: README.md

<div align="center">

<img src="./static/image/mirofish-offline-banner.png" alt="MiroFish Offline" width="100%"/>

# MiroFish-Offline

**Fully local fork of [MiroFish](https://github.com/666ghj/MiroFish) — no cloud APIs required. English UI.**

*A multi-agent swarm intelligence engine that simulates public opinion, market sentiment, and social dynamics. Entirely on your hardware.*

[![GitHub Stars](https://img.shields.io/github/stars/nikmcfly/MiroFish-Offline?style=flat-square&color=DAA520)](https://github.com/nikmcfly/MiroFish-Offline/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/nikmcfly/MiroFish-Offline?style=flat-square)](https://github.com/nikmcfly/MiroFish-Offline/network)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-blue?style=flat-square)](./LICENSE)

</div>

## What is this?

MiroFish is a multi-agent simulation engine: upload any document (press release, policy draft, financial report), and it generates hundreds of AI agents with unique personalities that simulate the public reaction on social media. Posts, arguments, opinion shifts — hour by hour.

The [original MiroFish](https://github.com/666ghj/MiroFish) was built for the Chinese market (Chinese UI, Zep Cloud for knowledge graphs, DashScope API). This fork makes it **fully local and fully English**:

| Original MiroFish | MiroFish-Offline |
|---|---|
| Chinese UI | **English UI** (1,000+ strings translated) |
| Zep Cloud (graph memory) | **Neo4j Community Edition 5.15** |
| DashScope / OpenAI API (LLM) | **Ollama** (qwen2.5, llama3, etc.) |
| Zep Cloud embeddings | **nomic-embed-text** via Ollama |
| Cloud API keys required | **Zero cloud dependencies** |

## Workflow

1. **Graph Build** — Extracts entities (people, companies, events) and relationships from your document. Builds a knowledge graph with individual and group memory via Neo4j.
2. **Env Setup** — Generates hundreds of agent personas, each with unique personality, opinion bias, reaction speed, influence level, and memory of past events.
3. **Simulation** — Agents interact on simulated social platforms: posting, replying, arguing, shifting opinions. The system tracks sentiment evolution, topic propagation, and influence dynamics in real time.
4. **Report** — A ReportAgent analyzes the post-simulation environment, interviews a focus group of agents, searches the knowledge graph for evidence, and generates a structured analysis.
5. **Interaction** — Chat with any agent from the simulated world. Ask them why they posted what they posted. Full memory and personality persists.

## Screenshot

<div align="center">
<img src="./static/image/mirofish-offline-screenshot.jpg" alt="MiroFish Offline — English UI" width="100%"/>
</div>

## Quick Start

### Prerequisites

- Docker & Docker Compose (recommended), **or**
- Python 3.11+, Node.js 18+, Neo4j 5.15+, Ollama

### Option A: Docker (easiest)

```bash
git clone https://github.com/nikmcfly/MiroFish-Offline.git
cd MiroFish-Offline
cp .env.example .env

# Start all services (Neo4j, Ollama, MiroFish)
docker compose up -d

# Pull the required models into Ollama
docker exec mirofish-ollama ollama pull qwen2.5:32b
docker exec mirofish-ollama ollama pull nomic-embed-text
```

Open `http://localhost:3000` — that's it.

### Option B: Manual

**1. Start Neo4j**

```bash
docker run -d --name neo4j \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/mirofish \
  neo4j:5.15-community
```

**2. Start Ollama & pull models**

```bash
ollama serve &
ollama pull qwen2.5:32b      # LLM (or qwen2.5:14b for less VRAM)
ollama pull nomic-embed-text  # Embeddings (768d)
```

**3. Configure & run backend**

```bash
cp .env.example .env
# Edit .env if your Neo4j/Ollama are on non-default ports

cd backend
pip install -r requirements.txt
python run.py
```

**4. Run frontend**

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:3000`.

## Configuration

All settings are in `.env` (copy from `.env.example`):

```bash
# LLM — points to local Ollama (OpenAI-compatible API)
LLM_API_KEY=ollama
LLM_BASE_URL=http://localhost:11434/v1
LLM_MODEL_NAME=qwen2.5:32b

# Neo4j
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=mirofish

# Embeddings
EMBEDDING_MODEL=nomic-embed-text
EMBEDDING_BASE_URL=http://localhost:11434
```

Works with any OpenAI-compatible API — swap Ollama for Claude, GPT, or any other provider by changing `LLM_BASE_URL` and `LLM_API_KEY`.

## Architecture

This fork introduces a clean abstraction layer between the application and the graph database:

```
┌─────────────────────────────────────────┐
│              Flask API                   │
│  graph.py  simulation.py  report.py     │
└──────────────┬──────────────────────────┘
               │ app.extensions['neo4j_storage']
┌──────────────▼──────────────────────────┐
│           Service Layer                  │
│  EntityReader  GraphToolsService         │
│  GraphMemoryUpdater  ReportAgent         │
└──────────────┬──────────────────────────┘
               │ storage: GraphStorage
┌──────────────▼──────────────────────────┐
│         GraphStorage (abstract)          │
│              │                            │
│    ┌─────────▼─────────┐                │
│    │   Neo4jStorage     │                │
│    │  ┌───────────────┐ │                │
│    │  │ EmbeddingService│ ← Ollama       │
│    │  │ NERExtractor   │ ← Ollama LLM   │
│    │  │ SearchService  │ ← Hybrid search │
│    │  └───────────────┘ │                │
│    └───────────────────┘                │
└─────────────────────────────────────────┘
               │
        ┌──────▼──────┐
        │  Neo4j CE   │
        │  5.15       │
        └─────────────┘
```

**Key design decisions:**

- `GraphStorage` is an abstract interface — swap Neo4j for any other graph DB by implementing one class
- Dependency injection via Flask `app.extensions` — no global singletons
- Hybrid search: 0.7 × vector similarity + 0.3 × BM25 keyword search
- Synchronous NER/RE extraction via local LLM (replaces Zep's async episodes)
- All original dataclasses and LLM tools (InsightForge, Panorama, Agent Interviews) preserved

## Hardware Requirements

| Component | Minimum | Recommended |
|---|---|---|
| RAM | 16 GB | 32 GB |
| VRAM (GPU) | 10 GB (14b model) | 24 GB (32b model) |
| Disk | 20 GB | 50 GB |
| CPU | 4 cores | 8+ cores |

CPU-only mode works but is significantly slower for LLM inference. For lighter setups, use `qwen2.5:14b` or `qwen2.5:7b`.

## Use Cases

- **PR crisis testing** — simulate the public reaction to a press release before publishing
- **Trading signal generation** — feed financial news and observe simulated market sentiment
- **Policy impact analysis** — test draft regulations against simulated public response
- **Creative experiments** — someone fed it a classical Chinese novel with a lost ending; the agents wrote a narratively consistent conclusion

## License

AGPL-3.0 — same as the original MiroFish project. See [LICENSE](./LICENSE).

## Credits & Attribution

This is a modified fork of [MiroFish](https://github.com/666ghj/MiroFish) by [666ghj](https://github.com/666ghj), originally supported by [Shanda Group](https://www.shanda.com/). The simulation engine is powered by [OASIS](https://github.com/camel-ai/oasis) from the CAMEL-AI team.

**Modifications in this fork:**
- Backend migrated from Zep Cloud to local Neo4j CE 5.15 + Ollama
- Entire frontend translated from Chinese to English (20 files, 1,000+ strings)
- All Zep references replaced with Neo4j across the UI
- Rebranded to MiroFish Offline


# FILE: docs/progress.md

# MiroFish-Offline Migration Progress

## Overview
Migration from Zep Cloud + DashScope (Alibaba Qwen API) to local Neo4j CE + Ollama.

## PHASE 0 — Scaffolding (COMPLETE)
- **TASK-001**: Created `LLMClient` abstraction (`backend/app/llm/client.py`) — Ollama-backed, sync, supports chat + embedding
- **TASK-002**: Created `NERExtractor` (`backend/app/llm/ner_extractor.py`) — local NER/RE via LLM, ontology-guided
- **TASK-003**: Created `EmbeddingService` (`backend/app/llm/embedding.py`) — nomic-embed-text via Ollama, 768d vectors

## PHASE 1 — Storage Layer (COMPLETE)
- **TASK-004**: Created `GraphStorage` abstract interface (`backend/app/storage/graph_storage.py`)
- **TASK-005**: Created `Neo4jStorage` implementation (`backend/app/storage/neo4j_storage.py`) — full CRUD, hybrid search (0.7*vector + 0.3*BM25), vector indexes, fulltext indexes
- **TASK-006**: Created `backend/app/storage/__init__.py` with exports
- **TASK-007**: Config updates for Neo4j + Ollama connection params

## PHASE 2 — Service Layer Rewrite (COMPLETE)
- **TASK-008**: Rewrote `graph_builder.py` — uses `GraphStorage` instead of Zep client
- **TASK-009**: Created `entity_reader.py` (replaces `zep_entity_reader.py`) — `EntityReader(storage: GraphStorage)`, optimized `get_entity_with_context()` with O(1) node lookup
- **TASK-010**: Marked `zep_paging.py` for deletion (only used by old zep files)
- **TASK-011**: Created `graph_tools.py` (replaces `zep_tools.py`, ~900 lines) — `GraphToolsService(storage, llm_client)`, all 7 dataclasses preserved, LLM tools (insight_forge, panorama, interviews) intact
- **TASK-012**: Adapted `report_agent.py` — `ZepToolsService` → `GraphToolsService`, DI constructor
- **TASK-013**: Created `graph_memory_updater.py` (replaces `zep_graph_memory_updater.py`) — `GraphMemoryUpdater(graph_id, storage)`, adapted `simulation_runner.py`
- **TASK-014**: Adapted `oasis_profile_generator.py` — removed `zep_cloud` import, `_search_graph_for_entity()` rewrite
- **TASK-014b**: Adapted `simulation_manager.py`, `simulation_config_generator.py`, `services/__init__.py`, `api/report.py`, `api/simulation.py` — all Zep references replaced with GraphStorage DI via `current_app.extensions`

## PHASE 3 — Flask DI + App Factory (COMPLETE)
- **TASK-015**: Wired `Neo4jStorage` singleton in `create_app()` → `app.extensions['neo4j_storage']`. Updated all API endpoints (`graph.py`, `simulation.py`, `report.py`) to use injected storage. Removed all `ZEP_API_KEY` guards. Added teardown hook to close Neo4j driver.

## PHASE 4 — End-to-End Test (COMPLETE)
- **TASK-016**: Verified full import chain — all storage, service, and API modules import successfully. Flask app factory creates without crash (graceful fallback when Neo4j/Ollama unavailable).

## PHASE 5 — CAMEL-AI + Ollama (COMPLETE — already compatible)
- **TASK-017**: Verified simulation scripts already use `ModelPlatformType.OPENAI` with `OPENAI_API_BASE_URL` mapped from `LLM_BASE_URL`. No DashScope references remain. Ollama's OpenAI-compatible API works out of the box.

## PHASE 6 — Cleanup (COMPLETE)
- **TASK-018**: Deleted 4 dead `zep_*.py` files, deprecated `generate_python_code()` in ontology_generator, fixed Zep docstrings in graph.py, added `requests` to requirements.txt

## PHASE 7 — Publish (TODO)
- **TASK-019**: Rename to MiroFish-Offline, add AGPL-3.0 license, publish to GitHub

## Files Created (New)
| File | Replaces | Status |
|------|----------|--------|
| `backend/app/llm/client.py` | DashScope API calls | Done |
| `backend/app/llm/ner_extractor.py` | Zep Cloud NER | Done |
| `backend/app/llm/embedding.py` | Zep Cloud embeddings | Done |
| `backend/app/storage/graph_storage.py` | Zep Cloud SDK interface | Done |
| `backend/app/storage/neo4j_storage.py` | Zep Cloud backend | Done |
| `backend/app/services/entity_reader.py` | `zep_entity_reader.py` | Done |
| `backend/app/services/graph_tools.py` | `zep_tools.py` | Done |
| `backend/app/services/graph_memory_updater.py` | `zep_graph_memory_updater.py` | Done |

## Files Modified
| File | Changes | Status |
|------|---------|--------|
| `backend/app/services/graph_builder.py` | Uses GraphStorage | Done |
| `backend/app/services/report_agent.py` | GraphToolsService DI | Done |
| `backend/app/services/simulation_runner.py` | GraphMemoryManager DI | Done |
| `backend/app/services/oasis_profile_generator.py` | GraphStorage DI | Done |
| `backend/app/services/simulation_manager.py` | EntityReader DI | Done |
| `backend/app/services/simulation_config_generator.py` | Import fix | Done |
| `backend/app/services/__init__.py` | All new exports | Done |
| `backend/app/api/report.py` | GraphToolsService DI, TODO cleaned | Done |
| `backend/app/api/simulation.py` | EntityReader DI, ZEP guards removed | Done |
| `backend/app/__init__.py` | Neo4jStorage singleton init + teardown | Done |

## Files Deleted (PHASE 6 — DONE)
- ~~`backend/app/services/zep_entity_reader.py`~~ — deleted
- ~~`backend/app/services/zep_tools.py`~~ — deleted
- ~~`backend/app/services/zep_graph_memory_updater.py`~~ — deleted
- ~~`backend/app/utils/zep_paging.py`~~ — deleted

