# Missing Repo Summary Source: marketcalls/openalgo

- URL: https://github.com/marketcalls/openalgo
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/marketcalls__openalgo
- Clone Status: cloned
- Language: Python
- Stars: 1818
- Topics: algorithmic-trading, algotrading, amibroker, chartink, flask, metatrader, openalgo, python, quantative-trading, quantitative-finance, reactjs, self-hosting, sqlite, stock-market, stocks, trade-automation, trading-bot, tradingview
- Description: Open Source Algo Trading Platform for Everyone

## Extracted README / Docs / Examples



# FILE: README.md

# OpenAlgo - Open Source Algorithmic Trading Platform

<div align="center">

[![PyPI Downloads](https://static.pepy.tech/badge/openalgo)](https://pepy.tech/projects/openalgo)
[![PyPI Downloads](https://static.pepy.tech/badge/openalgo/month)](https://pepy.tech/projects/openalgo)
[![X (formerly Twitter) Follow](https://img.shields.io/twitter/follow/openalgoHQ)](https://twitter.com/openalgoHQ)
[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UCw7eVneIEyiTApy4RtxrJsQ)](https://www.youtube.com/@openalgo)
[![Discord](https://img.shields.io/discord/1219847221055455263)](https://discord.com/invite/UPh7QPsNhP)

</div>

## What is OpenAlgo?

OpenAlgo is a free, open source, self-hosted **trading platform** — not just a broker bridge. Built on Python Flask + React 19, it gives traders a full-stack environment to **design, host, and execute strategies** across **30+ Indian brokers** through a single unified API. Whether you write Python, prefer drag-and-drop, or trade options exclusively, OpenAlgo gives you a first-class workflow without tying you to any single broker or vendor.

OpenAlgo is no longer just "an API layer in front of your broker." Today it is **four products in one self-hosted instance** — sharing one broker session, one WebSocket feed, and one database — covering the complete journey from idea → backtest → live trade.

## Four Ways to Trade with OpenAlgo

| Surface | Route | Who it's for |
| --- | --- | --- |
| **Unified Broker API** | `/api/v1/` | External platforms — TradingView, Amibroker, ChartInk, Excel, Google Sheets, Python, Java, Go, .NET, Node.js, MetaTrader, GoCharting, N8N. One API, 30+ brokers. |
| **Python Strategy Host** | `/python` | Traders who code — paste any Python script into the in-browser CodeMirror editor, schedule it on IST start/stop times, run multiple strategies in parallel with process isolation, watch real-time logs. No external server, no Docker, no cron. |
| **Flow — No-Code Strategy Builder** | `/flow` | Traders who don't code — drag-and-drop nodes for market data, indicators, conditions, order execution, and notifications. Webhook triggers for TradingView and external signals built in. JSON import/export for sharing strategies. |
| **Options Trading Suite** | `/tools` | Options traders — twelve built-in analytical tools (Strategy Builder with payoff diagrams & live Greeks, Option Chain, IV Smile, Max Pain, Vol Surface, GEX dashboard, OI Tracker, OI Profile, Straddle Chart, Straddle PnL simulator, Option Greeks history). Each one streams from your connected broker. |

Every surface above runs on the same Sandbox engine (₹1 Crore sandbox capital, exchange-aligned auto square-off) so you can sandbox-trade *any* of these flows before going live. Real-time dashboards, PnL tracker, latency monitor, Telegram alerts, and the AI / MCP server work uniformly across all four.

## Video Tutorial

[![What is OpenAlgo](https://img.youtube.com/vi/S5myMo9WUdQ/0.jpg)](https://www.youtube.com/watch?v=S5myMo9WUdQ)

## Quick Links

- **Documentation**: [docs.openalgo.in](https://docs.openalgo.in)
- **Installation Guide**: [Getting Started](https://docs.openalgo.in/installation-guidelines/getting-started)
- **Upgrade Guide**: [Upgrade Instructions](https://docs.openalgo.in/installation-guidelines/getting-started/upgrade)
- **Why OpenAlgo**: [Why Build with OpenAlgo](https://docs.openalgo.in/why-to-build-with-openalgo)


## Python Compatibility

**Supports Python 3.11, 3.12, 3.13, and 3.14**

## Supported Brokers (30+)

<details>
<summary>View All Supported Brokers</summary>

- 5paisa (Standard + XTS)
- AliceBlue
- AngelOne
- Compositedge
- Definedge
- Delta Exchange
- Dhan (Live + Sandbox)
- Firstock
- Flattrade
- Fyers
- Groww
- IBulls
- IIFL
- Iiflcapital
- Indmoney
- JainamXTS
- Kotak Neo
- Motilal Oswal
- Mstock
- Nubra
- Paytm Money
- Pocketful
- RMoney
- Samco
- Shoonya (Finvasia)
- Tradejini
- Upstox
- Wisdom Capital
- Zebu
- Zerodha

</details>

All brokers share a unified API interface, making it easy to switch between brokers without changing your code.

## Core Features

### Unified REST API Layer (`/api/v1/`)
A single, standardized API across all brokers with 30+ endpoints:
- **Order Management**: Place, modify, cancel orders, basket orders, smart orders with position sizing
- **Portfolio**: Get positions, holdings, order book, trade book, funds
- **Market Data**: Real-time quotes, historical data, market depth (Level 5), symbol search
- **Advanced**: Option Greeks calculator, margin calculator, synthetic futures, auto-split orders

### Real-Time WebSocket Streaming
- Unified WebSocket proxy server for all brokers (port 8765)
- Common WebSocket implementation using ZMQ for normalized data across brokers
- Subscribe to LTP, Quote, or Market Depth for any symbol
- ZeroMQ-based message bus for high-performance data distribution
- Automatic reconnection and failover handling

### Flow Visual Strategy Builder (`/flow`)
Build trading strategies visually without writing code:
- **Node-based editor** powered by xyflow/React Flow
- **Pre-built nodes**: Market data, indicators, conditions, order execution, notifications
- **Real-time execution** with live market data
- **Webhook triggers** for TradingView and external signals
- **Condition nodes** with `true/false` and `yes/no` edge handles, `{{var}}` interpolation with list indexing
- **JSON import/export** for sharing strategies between traders
- **Visual debugging** with execution flow highlighting

### Options & Strategy Analytics Tools (`/tools`)
A complete suite of twelve built-in analytical tools for options trading and market analysis — no external subscriptions required. Accessible from the **Tools** page in the sidebar:

| Tool | Route | What it does |
|------|-------|--------------|
| **Strategy Builder** | `/strategybuilder` | Build multi-leg option strategies with live Greeks, payoff diagrams, what-if simulators, Strategy Chart, Multi Strike OI tabs, and basket order execution |
| **Strategy Portfolio** | `/strategybuilder/portfolio` | Saved strategies across MyTrades and Simulation watchlists |
| **Option Chain** | `/optionchain` | Real-time option chain with live Greeks, OI data, and quick order placement |
| **Option Greeks** | `/ivchart` | Historical IV, Delta, Theta, Vega, and Gamma charts for ATM options |
| **OI Tracker** | `/oitracker` | Open Interest analysis with CE/PE OI bars, PCR overlay, and ATM strike marker |
| **Max Pain** | `/maxpain` | Max Pain strike calculation with visual pain distribution across strikes |
| **Straddle Chart** | `/straddle` | Dynamic ATM Straddle chart with rolling strike, Spot, and Synthetic Futures overlay |
| **Straddle PnL** | `/straddlepnl` | Simulated intraday ATM straddle P&L with automated N-point adjustments and trade log |
| **Vol Surface** | `/volsurface` | 3D Implied Volatility surface across strikes and expiries using live option chain data |
| **GEX Dashboard** | `/gex` | Gamma Exposure analysis with OI Walls, Net GEX per strike, and top gamma strikes |
| **IV Smile** | `/ivsmile` | Implied Volatility smile with Call/Put IV curves, ATM IV, and skew analysis |
| **OI Profile** | `/oiprofile` | Futures candlestick with OI butterfly and daily OI change across strikes |

All tools stream live from your connected broker via the unified WebSocket feed and work identically across every supported broker.

### API Analyzer Mode
Complete testing environment with ₹1 Crore sandbox capital:
- Test strategies with real market data without risking money
- Pre-deployment testing for strategy validation
- Supports all order types (Market, Limit, SL, SL-M)
- Realistic margin system with leverage
- Auto square-off at exchange timings
- Separate database for complete isolation

[API Analyzer Documentation](https://docs.openalgo.in/new-features/api-analyzer)

### Action Center
Order approval workflow for manual control:
- **Auto Mode**: Immediate order execution (for personal trading)
- **Semi-Auto Mode**: Manual approval required before broker execution
- Complete audit trail with IST timestamps
- Approve individual orders or bulk approve all

[Action Center Documentation](https://docs.openalgo.in/new-features/action-center)

### Python Strategy Host (`/python`)
Host and run your Python strategies directly inside OpenAlgo — no separate VM, no cron, no Docker:
- Built-in code editor powered by **CodeMirror** with Python syntax highlighting and themes
- Run multiple strategies in parallel with **full process isolation**
- Automated **IST-based scheduling** with start/stop times and per-day-of-week control
- Secure environment variable management with Fernet encryption
- Real-time logs streamed to the browser; state persists across restarts
- Built-in `Python Strategy Guide` page walks first-time users from an empty editor to a scheduled, running strategy

### ChartInk Integration
Direct webhook integration for scanner alerts:
- Supports BUY, SELL, SHORT, COVER actions
- Intraday with auto square-off and positional strategies
- Bulk symbol configuration via CSV
- Real-time strategy monitoring

### AI-Powered Trading (MCP Server)
Connect AI assistants for natural language trading:
- Compatible with Claude Desktop, Cursor, Windsurf, ChatGPT
- Execute trades using natural language commands
- Full trading capabilities: orders, positions, market data
- Local and secure integration with your OpenAlgo instance

### Telegram Bot Integration
Real-time notifications and command execution:
- Automatic order and trade alerts delivered to Telegram
- Get orderbook, positions, holdings, funds on demand
- Generate intraday and daily charts
- Interactive button-based menu
- Receive strategy alerts directly to Telegram
- Secure API key encryption

### Advanced Monitoring Tools
**Latency Monitor**: Track order execution performance and round-trip times across brokers

**Traffic Monitor**: API usage analytics, error tracking, and endpoint statistics

**PnL Tracker**: Real-time profit/los

# FILE: docs/HEALTH_MONITORING_IMPLEMENTATION.md

# Health Monitoring System - Implementation Complete

**Date**: 2026-01-30
**Status**: Ready for Integration
**Zero Latency Impact**: ✅ All metrics collected in background daemon thread

## What Has Been Built

### 1. Database Layer ✅
**File**: `database/health_db.py`

- Separate SQLite database (`db/health.db`)
- Two models:
  - `HealthMetric` - Stores FD, memory, DB, WS, thread metrics
  - `HealthAlert` - Tracks alerts with auto-resolution
- Industry-standard status values: `pass` | `warn` | `fail`
- Automatic data purging (7-day retention)

### 2. Monitoring Utilities ✅
**File**: `utils/health_monitor.py`

**Zero Latency Features**:
- Background daemon thread (does not block API/WebSocket)
- Cached metrics for instant access (<1ms)
- Sampling every 10 seconds (configurable)
- Minimal CPU overhead (<1%)
- Thread releases GIL during sleep

**Metrics Collected**:
- **File Descriptors**: Count, limit, usage%, status
- **Memory**: RSS, VMS, swap, system availability
- **Database Connections**: Per-database connection tracking
- **WebSocket Connections**: Per-broker connection & symbol counts
- **Threads**: Count, stuck thread detection

**Alert System**:
- Automatic alert creation on threshold breach
- Auto-resolution when metrics return to healthy range
- Configurable thresholds via environment variables

### 3. Flask Blueprint ✅
**File**: `blueprints/health.py`

**Industry-Standard Endpoints**:

| Endpoint | Auth | Purpose | Response Time |
|----------|------|---------|---------------|
| `GET /health` | No | Simple 200 OK for AWS ELB, K8s | <1ms (cached) |
| `GET /health/check` | No | DB connectivity + detailed status | ~10-50ms |
| `GET /health/` | Yes | Full monitoring dashboard | N/A (HTML) |
| `GET /health/api/current` | Yes | Current metrics snapshot | <5ms |
| `GET /health/api/history` | Yes | Historical metrics | ~50-200ms |
| `GET /health/api/stats` | Yes | Aggregated statistics | ~50-200ms |
| `GET /health/api/alerts` | Yes | Active alerts | <10ms |
| `POST /health/api/alerts/<id>/acknowledge` | Yes | Acknowledge alert | <5ms |
| `POST /health/api/alerts/<id>/resolve` | Yes | Resolve alert | <5ms |
| `GET /health/export` | Yes | Export to CSV | ~100-500ms |

**Follows**:
- `draft-inadarei-api-health-check-06` specification
- HTTP status codes: 200 (pass/warn), 503 (fail)
- Standard health check response format

## Integration Steps

### Step 1: Add Blueprint to app.py

```python
# Add to imports section
from blueprints.health import health_bp
from utils.health_monitor import init_health_monitoring

# Register blueprint (around line 100-150 where other blueprints are registered)
app.register_blueprint(health_bp)

# Initialize health monitoring (in init_app or after app setup)
init_health_monitoring(app)

# Add teardown handler (with other teardown handlers)
@app.teardown_appcontext
def shutdown_health_session(exception=None):
    from database.health_db import health_session
    health_session.remove()
```

### Step 2: Add Configuration to .env

```bash
# Health Monitoring Configuration
HEALTH_MONITOR_ENABLED=true
HEALTH_SAMPLE_INTERVAL=10  # seconds
HEALTH_RETENTION_DAYS=7

# File Descriptor Thresholds
HEALTH_FD_WARNING_THRESHOLD=700
HEALTH_FD_CRITICAL_THRESHOLD=900

# Memory Thresholds (MB)
HEALTH_MEMORY_WARNING_THRESHOLD=500
HEALTH_MEMORY_CRITICAL_THRESHOLD=1000

# Database Connection Thresholds
HEALTH_DB_WARNING_THRESHOLD=10
HEALTH_DB_CRITICAL_THRESHOLD=20

# WebSocket Connection Thresholds
HEALTH_WS_WARNING_THRESHOLD=10
HEALTH_WS_CRITICAL_THRESHOLD=20

# Thread Thresholds
HEALTH_THREAD_WARNING_THRESHOLD=50
HEALTH_THREAD_CRITICAL_THRESHOLD=100
```

### Step 3: Create Dashboard Template

**File**: `templates/health/dashboard.html` (or use React)

```html
<!DOCTYPE html>
<html>
<head>
    <title>System Health Monitor - OpenAlgo</title>
    <!-- Add your styles -->
</head>
<body>
    <div class="container">
        <h1>System Health Monitor</h1>

        <!-- Metric Cards -->
        <div class="metrics-cards">
            <div class="card" id="fd-card">
                <h3>File Descriptors</h3>
                <div class="metric-value" id="fd-count">-</div>
                <div class="metric-status" id="fd-status">-</div>
            </div>

            <div class="card" id="memory-card">
                <h3>Memory Usage</h3>
                <div class="metric-value" id="memory-value">-</div>
                <div class="metric-status" id="memory-status">-</div>
            </div>

            <!-- More cards for DB, WS, Threads -->
        </div>

        <!-- Alerts Panel -->
        <div class="alerts-panel">
            <h2>Active Alerts</h2>
            <div id="alerts-list"></div>
        </div>

        <!-- Charts -->
        <div class="charts">
            <canvas id="fd-chart"></canvas>
            <canvas id="memory-chart"></canvas>
        </div>

        <!-- Metrics Table -->
        <div class="metrics-table">
            <table id="metrics-table"></table>
        </div>
    </div>

    <script>
        // Auto-refresh every 10 seconds
        setInterval(async () => {
            const response = await fetch('/health/api/current');
            const data = await response.json();
            updateMetrics(data);
        }, 10000);

        function updateMetrics(data) {
            // Update metric cards
            document.getElementById('fd-count').textContent =
                `${data.fd.count} / ${data.fd.limit}`;
            document.getElementById('fd-status').textContent = data.fd.status;
            // ... update other metrics
        }
    </script>
</body>
</html>
```

### Step 4: Configure AWS ELB Health Check

**Target**: `http://your-domain.com/health`
- **Interval**: 30 seconds
- **Timeout**: 5 seconds
- **Healthy threshold**: 2 consecutive successes
- **Unhealthy threshold**: 2 consecutive failures
- **Success codes**: 200

**Response format**:
```json
{
    "status": "pass",
    "version": "1.0",
    "serviceId": "openalgo",
    "description": "O

# FILE: docs/scanner-architecture.md

# OpenAlgo Real-Time Scanner Service — Architecture & Implementation Guide

## Overview

A standalone, external scanner service that monitors 500+ symbols in real-time on any timeframe, running multiple independent scanners (RSI, EMA crossover, volume spike, custom conditions) without hitting broker API rate limits.

The service builds candles from OpenAlgo's live WebSocket tick stream, bootstraps indicator state from Historify (DuckDB) at startup, and distributes candle events to multiple scanner processes via Redis Streams.

---

## Problem Statement

Most Indian brokers restrict historical data API calls to 1-10 requests per second. Scanning 500 symbols by polling the REST API is fundamentally broken:

- 500 symbols at 10 req/sec = 50 seconds per scan cycle
- Data is stale before the scan completes
- Repeated polling wastes API quota
- Cannot scale beyond ~10 symbols in real-time

**Solution:** Eliminate the REST API from the real-time path entirely. Use the broker WebSocket (no rate limits) for live ticks, and local DuckDB (no rate limits) for historical bootstrap.

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         PRE-MARKET BOOTSTRAP                        │
│                                                                     │
│  Historify (DuckDB) — stores 1m candle history for all symbols      │
│  └── OpenAlgo API: GET /history (source="Db", interval="1m")        │
│      └── Fetch last N 1-minute candles per symbol                   │
│      └── Local database — zero rate limits, completes in seconds    │
│      └── Seeds indicator state so scanners are ready at 9:15 AM     │
└──────────────────────────────┬──────────────────────────────────────┘
                               │ indicators initialized
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         REAL-TIME TICK LAYER                        │
│                                                                     │
│  OpenAlgo WebSocket Proxy (port 8765)                               │
│  └── Authenticate with API key                                     │
│  └── Subscribe to 500+ symbols in LTP or Quote mode                │
│  └── Receive ~500-2000 ticks/second                                │
│  └── No rate limits — broker WebSocket is unlimited                 │
│                                                                     │
│  Tick Receiver Process                                              │
│  └── Single async WebSocket client                                  │
│  └── Publishes every tick to Redis Stream: ticks:raw                │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         CANDLE BUILDER                              │
│                                                                     │
│  Single Python Process                                              │
│  └── Consumes ticks from Redis Stream: ticks:raw                    │
│  └── Maintains in-memory candle state for all symbols               │
│  └── On minute boundary:                                            │
│       ├── Closes current candle                                     │
│       ├── Appends to rolling window (per symbol)                    │
│       ├── Publishes completed candle to Redis Stream: candles:1m    │
│       └── Optionally builds higher timeframes (5m, 15m)             │
│                                                                     │
│  Memory: 500 symbols x 200 candles x ~100 bytes = ~10 MB           │
└──────────────────────────────┬──────────────────────────────────────┘
                               │
              ┌────────────────┼────────────────┬──────────────┐
              ▼                ▼                ▼              ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐ ┌──────────────┐
│   Scanner #1      │ │  Scanner #2   │ │  Scanner #3   │ │  Scanner #N  │
│   RSI > 70        │ │  EMA Cross    │ │  Vol Spike    │ │  Custom      │
│                   │ │               │ │               │ │              │
│ Consumer group:   │ │ Consumer grp: │ │ Consumer grp: │ │ Consumer grp:│
│ scanner_rsi       │ │ scanner_ema   │ │ scanner_vol   │ │ scanner_N    │
│                   │ │               │ │               │ │              │
│ Reads: candles:1m │ │ candles:1m    │ │ candles:1m    │ │ candles:1m   │
│ Maintains own     │ │ Maintains own │ │ Maintains own │ │ Maintains own│
│ indicator state   │ │ indicator     │ │ indicator     │ │ indicator    │
│ per symbol        │ │ state         │ │ state         │ │ state        │
│                   │ │               │ │               │ │              │
│ Emits → alerts    │ │ Emits → alerts│ │ Emits → alerts│ │ Emits→alerts │
└─────────┬─────────┘ └──────┬────────┘ └──────┬────────┘ └──────┬──────┘
          └──────────────────┴─────────────────┴─────────────────┘
                                    │
                                    ▼
                    ┌──────────────────────────────┐
                    │       Results Aggregator      │
                    │                               │
                    │  Redis Stream: alerts          │
                    │  └── Dashboard WebSocket       │
                    │  └── Webhook notifications     │
                    │  └── OpenAlgo PlaceOrder API   │
                    │  └── Telegram / Discord bot    │
                    └──────────────────────────────┘
                                    │
                                    ▼ (at market close)
                    ┌──────────────────────────────┐
                    │     End-of-Day Persistence     │
                    │                               │
                    │  Write all 1m c

# FILE: docs/CHANGELOG.md

# Changelog

All notable changes to OpenAlgo will be documented in this file.

## [2.0.0.0] - 2026-01-22

### Major Release: Complete Frontend Rewrite & Feature Expansion

This is a major release featuring a complete rewrite of the frontend from Flask/Jinja2 templates to a modern React 19 Single Page Application (SPA). This release includes **212 commits** representing months of development work, introducing new features like Flow Visual Builder, Historify, and enhanced real-time capabilities.

---

## Highlights

- **React 19 Frontend** - Complete migration of 77 templates to modern React with TypeScript
- **Flow Visual Builder** - Node-based visual workflow builder for trading automation
- **Historify** - Historical market data management with DuckDB storage
- **Real-Time WebSocket** - Native WebSocket integration for live market data
- **Sandbox Mode** - Enhanced sandbox testing environment with sandbox capital
- **API Playground** - Bruno-style API testing with WebSocket support
- **Python Strategies** - Enhanced scheduler with real-time status and resource limits
- **Telegram Bot** - Fixed callbacks and improved status display
- **Enhanced Security** - Multiple security improvements and vulnerability fixes

---

## New Features

### React 19 Frontend Migration (77 Templates)

**Phase 1 - Foundation**
- Initialized React frontend with Vite, TypeScript, TanStack Query
- Added Flask blueprint to serve React frontend
- Pre-built frontend dist included for community use

**Phase 2 - Core Authentication & Trading**
- Login, Dashboard, Profile pages
- Orders, Positions, Holdings pages
- Order placement and management

**Phase 3 - Search & Symbol Management**
- FNO Discovery with performance optimization
- Symbol search and watchlist
- Bulk watchlist operations

**Phase 4 - Charts, WebSocket & Sandbox**
- TradingView charts integration
- WebSocket Test Console
- Sandbox/Analyzer mode interface

**Phase 5 - Platform Integrations**
- TradingView webhook page
- GoCharting integration
- Amibroker integration
- ChartInk integration

**Phase 6 - Strategy & Automation**
- Python Strategies management
- Strategy scheduler with SSE
- Strategy logs viewer

**Phase 7 - Monitoring & Administration**
- Logs, Latency Monitor, Traffic Logs
- Profile & Security settings
- Action Center for order approval
- Admin & Telegram modules

**Frontend Tech Stack**
- React 19 with TypeScript
- Vite 6 build system with code splitting
- TanStack Query v5 for server state
- shadcn/ui + Tailwind CSS 4 + DaisyUI
- Biome.js (replaced ESLint)
- Vitest unit tests + Playwright E2E tests
- Responsive mobile bottom navigation
- Accessibility testing (jest-axe)

---

### Flow Visual Builder

- **Node-based visual workflow builder** for trading strategies
- **Order Nodes**: Market Order, Limit Order, Smart Order, Basket Order
- **Options Order Node**: ATM/ITM/OTM offset resolution for F&O
- **Modify Order Node**: Live order management within workflows
- **Cancel Order Node**: Cancel single or all orders
- **Close Position Node**: Square off positions
- **WebSocket Streaming Nodes**: Real-time data within workflows
- **Telegram Alert Node**: Send notifications from workflows
- **Webhook Integration**: Trigger flows from external systems
- **Multi-leg Options Strategy**: Execute complex option strategies
- **Keyboard Shortcuts**: Efficient workflow creation
- Service integration for order execution

---

### Historify - Historical Data Management

- **DuckDB-powered storage** for historical market data
- **Multi-timeframe support**: 1m, 5m, 15m, 30m, 1h, Daily
- **Computed timeframes**: Weekly (W), Monthly (MO), Quarterly (Q), Yearly (Y)
- **Aggregation from daily data** for higher timeframes
- **Bulk export** with inline symbol selection
- **Multi-timeframe export** in single operation
- **Parquet import support** for external data sources
- **TradingView-style charts** with IST timezone
- **Styled crosshair tooltips** with IST timestamps
- **Job management**: Pause, resume, cancel operations
- **Broker badge display** and theme toggle
- **Date selector improvements** with Calendar component
- **Exchange market open time alignment** for candle boundaries

---

### Real-Time WebSocket Integration

- **Native WebSocket** for Holdings and Positions pages
- **Unified WebSocket proxy server** on port 8765
- **ZeroMQ message bus** for high-performance data distribution (port 5555)
- **Connection pooling**: MAX_SYMBOLS_PER_WEBSOCKET (1000) x MAX_WEBSOCKET_CONNECTIONS (3)
- **MultiQuotes API fallback** when WebSocket unavailable
- **Market timing awareness** for automatic data source switching
- **Real-time P&L calculation** using live LTP data
- **WebSocket templates** in Playground with Bruno-style collections
- **Multi-client subscribe/unsubscribe** support
- **Callback-based data retrieval** for Flow nodes
- **Pong message display** for manual ping testing

---

### Sandbox Mode (Sandbox Testing)

- **Isolated sandbox trading** with Rs. 1 Crore sandbox capital
- **Realistic margin system** with leverage
- **Auto square-off** at exchange timings for F&O contracts
- **Complete isolation** from live trading
- **Separate database** (sandbox.db) for sandbox trades
- **Real-time P&L** using WebSocket data
- **Session-based position filtering** for expired contracts
- **Expired F&O contract cleanup** on app startup
- **Sandbox logs** with date filter and Calendar icons
- **Wide dialog display** (98vw) for better visibility

---

### API Playground

- **Bruno-style API collection browser**
- **WebSocket testing console** with comprehensive controls
- **CodeMirror JSON editor** with syntax highlighting
- **Theme support** matching application theme
- **Manual ping/pong testing** for WebSocket connections
- **Multiple tabs** for endpoints with same path but different names
- **Nested braces handling** in body:json parsing
- **Source parameter** for History API collections

---

### Python Strategies

- **Enhanced scheduler** with mandatory sch

# FILE: docs/telegram-chart-rendering.md

# Telegram `/chart` rendering — architecture & operational notes

This document explains how the Telegram bot's `/chart` command renders Plotly
candlestick charts to PNG, why the implementation is more involved than a
one-line `fig.to_image()` call, and what operators need to know when running
openalgo on Docker, Ubuntu, Debian, RHEL/CentOS, Fedora, or Arch.

It also covers the non-obvious interaction between **Plotly's Kaleido 1.x
renderer**, **PTB's asyncio event loop**, and **gunicorn's eventlet worker** —
the triangular trap that caused `/chart` to fail in Docker and would fail
identically on a fresh bare-metal install without the workarounds described
below.

---

## 1. What the `/chart` command actually does

Defined in `services/telegram_bot_service.py` (`cmd_chart` at the bottom of the
file; helpers `_generate_intraday_chart` and `_generate_daily_chart` above it),
the command runs this pipeline:

1. Parse `symbol`, `exchange`, `chart_type`, `interval`, and `days` from the
   user's message.
2. Fetch OHLCV history via the OpenAlgo Python SDK
   (`client.history(symbol=..., exchange=..., interval=..., start_date=..., end_date=...)`).
3. Build a candlestick + volume figure with `plotly.graph_objects` and
   `plotly.subplots.make_subplots`.
4. **Convert the Plotly figure to PNG bytes** — `fig.to_image(format="png", engine="kaleido")`.
5. Send the PNG to Telegram via `reply_photo` (single chart) or `reply_media_group`
   (when `type=both` returns intraday + daily together).

Steps 1–3 are pure Python and work anywhere. **Step 4 is where everything
interesting happens**, and the rest of this document is about that step.

---

## 2. Why Chromium must be installed on the host (or in the container)

openalgo pins `kaleido==1.2.0` in `pyproject.toml`. Kaleido had a major
architectural change between v0.2.x and v1.x, and the switchover is the
single most common reason new openalgo installs see `/chart` silently fail:

| Kaleido version      | Chromium binary ships inside the wheel? | Runtime requirement |
| -------------------- | --------------------------------------- | ------------------- |
| `kaleido==0.2.1` (legacy) | **Yes** — static Chromium bundled, ~60 MB wheel | Nothing. Worked in any Docker image out of the box. |
| `kaleido==1.x` (current)  | **No** — pure Python bridge | A real Chromium/Chrome must be installed *separately* on the system, discoverable by `choreographer`. |

Under the hood, Kaleido 1.x uses the
[`choreographer`](https://pypi.org/project/choreographer/) library to drive a
headless Chromium over the Chrome DevTools Protocol. When you call
`fig.to_image(...)`, Kaleido:

1. Serializes the Plotly figure to JSON + HTML.
2. Spawns `/usr/bin/chromium` (or whatever browser `choreographer` finds) as a
   subprocess with `--headless --disable-gpu` and friends.
3. Loads the HTML, waits for Plotly.js to render, calls `Page.captureScreenshot`
   over CDP, and returns the PNG bytes.
4. Kills the subprocess.

**Every chart render launches a real headless Chromium for ~1–3 seconds.**
If Chromium isn't on the system, the subprocess spawn fails and
`fig.to_image()` raises — the generator catches it, logs
`Error generating intraday chart: ...`, and the bot replies with
`❌ Failed to generate charts for <symbol>`.

### Confirming Chromium is present

On Docker:

```bash
docker exec openalgo-web /usr/bin/chromium --version
# -> Chromium 120.0.6099.224 built on Debian 11.8, running on Debian 11.11
```

On bare metal:

```bash
which chromium || which chromium-browser
/usr/bin/chromium --version   # or /usr/bin/chromium-browser --version
```

You can also verify Kaleido's end-to-end path without touching Telegram at all:

```bash
# Docker
docker exec openalgo-web /app/.venv/bin/python -c '
import plotly.graph_objects as go
img = go.Figure(data=[go.Candlestick(
    x=[1,2], open=[100,102], high=[105,106], low=[99,101], close=[104,103]
)]).to_image(format="png", engine="kaleido")
print("PNG bytes:", len(img))
'
# -> PNG bytes: ~16000

# Bare metal
cd /path/to/openalgo
uv run python -c '... same snippet ...'
```

If that prints a byte count, Kaleido + Chromium + choreographer are healthy
and the `/chart` pipeline will work end-to-end. If it raises, the traceback
tells you exactly what's missing.

### Disk space cost

- Docker image grows by **~280 MB** when `chromium` + its runtime libs
  (`libnss3`, `libatk-bridge2.0-0`, `libcups2`, `libgbm1`, `libxkbcommon0`,
  `libgtk-3-0`, …) are installed via apt in the production stage of
  `Dockerfile`.
- Bare-metal installs see a similar ~280 MB increase depending on what's
  already on the host.

---

## 3. How each install path gets Chromium

### 3.1 Docker (`Dockerfile`)

The production stage's apt install block includes `chromium` and
`fonts-liberation`. Because `apt-get install -y --no-install-recommends
chromium` pulls every hard-dependency library automatically, you do **not**
need to list the shared libs individually — apt does the right thing. Two env
vars are also set for determinism:

```
BROWSER_PATH=/usr/bin/chromium
CHROME_BIN=/usr/bin/chromium
```

choreographer auto-discovers `/usr/bin/chromium` on `PATH` anyway, but being
explicit protects against future choreographer releases changing their
discovery logic.

Nothing in `start.sh` (the container entrypoint) needs Chromium-specific
configuration. It just runs migrations, starts the WebSocket proxy, then
execs gunicorn — all three pick up the already-installed Chromium via PATH
when the bot thread later calls `fig.to_image()`.

### 3.2 Bare-metal installers

Each of these scripts installs Chromium non-fatally — if the install fails
(e.g. the distro doesn't package it, network flake, snap not ready), the
rest of openalgo still installs and everything except `/chart` works:

| Script | Target | Block |
| --- | --- | --- |
| `install/install.sh` | General-purpose Ubuntu / Debian / Raspbian / RHEL / CentOS / Fedora / Amazon Linux / Arch | Per-distro `case` branch after main `apt-get instal

# FILE: docs/xtsapi.md

# ⚙️ How to Integrate Any XTS API-Supported Broker in OpenAlgo (5-Minute Setup)

OpenAlgo already supports XTS API through the `compositedge` plugin. Any broker using XTS (like IIFL, Nirmal Bang, Anand Rathi, Jainam, 5paisa, etc.) can be added with **zero code duplication**—just a few config updates.

---

## ✅ Minimal Changes Required

| File            | What to Change                                      |
|-----------------|-----------------------------------------------------|
| `baseurl.py`    | Update to your broker’s base domain and API paths   |
| `brlogin.py`    | Add your broker’s login redirect logic              |
| `broker.html`   | Add broker option and JS login switch               |
| `.sample.env`   | Add the new broker’s credentials                    |

> ⚡️ *No other backend or API changes are needed if the broker supports `apibinarymarketdata`.*

---

## 🧩 Step-by-Step Integration Guide

### 1. 🗂 Copy or Repurpose `compositedge`

```bash
cp -r broker/compositedge broker/<yourbroker>
```

Or reuse the same folder and override dynamically via `.env`.

---

### 2. ✏️ Edit `baseurl.py`

Update the base API endpoints:

```python
BASE_URL = "https://xts.<yourbroker>.com"

MARKET_DATA_URL = f"{BASE_URL}/apibinarymarketdata"
INTERACTIVE_URL = f"{BASE_URL}/interactive"
```

---

### 3. 🌐 Update `brlogin.py`

Add a new block similar to `compositedge`:

```python
elif broker == 'xtsalpha':
    # exact duplicate of compositedge logic with broker name replaced
    # handles session parsing and accessToken extraction
```

This ensures session redirection from XTS works correctly.

---

### 4. 🖼️ Update `broker.html`

#### A. Add broker to the dropdown:

```html
<option value="xtsalpha" {{ 'disabled' if broker_name != 'xtsalpha' }}>XTS Alpha {{ '(Disabled)' if broker_name != 'xtsalpha' }}</option>
```

#### B. Add to JavaScript login handler:

```javascript
case 'xtsalpha':
    loginUrl = 'https://xts.xtsalpha.com/interactive/thirdparty?appKey={{broker_api_key}}&returnURL={{ redirect_url }}';
    break;
```

> ✅ No need to add a broker login card section with `<a>` or `<img>`.

---

### 5. 🔐 Update `.env` or `.sample.env`

```env
# Broker Configuration
BROKER_API_KEY='YOUR_BROKER_API_KEY'
BROKER_API_SECRET='YOUR_BROKER_API_SECRET'

# Market Data Configuration (XTS only)
BROKER_API_KEY_MARKET='YOUR_BROKER_MARKET_API_KEY'
BROKER_API_SECRET_MARKET='YOUR_BROKER_MARKET_API_SECRET'

# OAuth Redirect
REDIRECT_URL='http://127.0.0.1:5000/xtsalpha/callback'

# Valid Brokers (must include new one)
VALID_BROKERS='fivepaisa,aliceblue,angel,compositedge,dhan,firstock,flattrade,fyers,icici,kotak,paytm,shoonya,upstox,zebu,zerodha,xtsalpha'
```

---

### ✅ Update Required in `.env` / `.sample.env`

To allow login for your new broker, you **must** add it to `VALID_BROKERS`.

#### Example:

**Before:**
```env
VALID_BROKERS='fivepaisa,aliceblue,angel,...'
```

**After:**
```env
VALID_BROKERS='fivepaisa,aliceblue,angel,...,xtsalpha'
```

> 🔐 This whitelist mechanism is used by `brlogin.py` or router logic to restrict unauthorized brokers.

---

## 🔁 Update Required in `brlogin.py` for New XTS Broker

You must add a block like this:

```python
elif broker == 'xtsalpha':
    try:
        if request.method == 'POST':
            if request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
                raw_data = request.get_data().decode('utf-8')
                if raw_data.startswith('session='):
                    from urllib.parse import unquote
                    session_data = unquote(raw_data[8:])
                else:
                    session_data = raw_data
            else:
                session_data = request.get_data().decode('utf-8')
        else:
            session_data = request.args.get('session')

        if not session_data:
            return jsonify({"error": "No session data received"}), 400

        try:
            if isinstance(session_data, str):
                session_data = session_data.strip()
                session_json = json.loads(session_data)
                if isinstance(session_json, str):
                    session_json = json.loads(session_json)
            else:
                session_json = session_data

        except json.JSONDecodeError as e:
            return jsonify({
                "error": f"Invalid JSON format: {str(e)}",
                "raw_data": session_data
            }), 400

        access_token = session_json.get('accessToken')
        if not access_token:
            return jsonify({"error": "No access token found"}), 400

        auth_token, feed_token, user_id, error_message = auth_function(access_token)
        forward_url = 'broker.html'

    except Exception as e:
        return jsonify({"error": f"Error processing request: {str(e)}"}), 500
```

---

## 📁 Breakdown: `broker/compositedge/` Folder Structure

```
broker/compositedge/
├── baseurl.py                  # XTS API base URLs
├── plugin.json                 # Metadata for plugin info
│
├── api/
│   ├── auth_api.py             # OAuth login + token handling
│   ├── data.py                 # Historical, quotes, LTP
│   ├── order_api.py            # Order handling (place, modify, cancel)
│   └── funds.py                # Fetch margin/funds
│
├── database/
│   └── master_contract_db.py   # Download & store broker's symbol master
│
└── mapping/
    ├── order_data.py           # OpenAlgo → XTS order translation
    └── transform_data.py       # XTS → OpenAlgo data formatting
```

---

### 📦 `plugin.json` Sample

```json
{
  "Plugin Name": "compositedge",
  "Plugin URI": "https://openalgo.in",
  "Description": "CompositedgeOpenAlgo Plugin",
  "Version": "1.0",
  "Author": "Kalaivani",
  "Author URI": "https://openalgo.in"
}
```

> 📦 Currently used for plugin metadata. Future versions may support dynamic plugin discovery.

---

## 🧪 Final Integration Checklist

- [x] Login from UI via `broker.html`
- [x] Token exchange successful
- [x] Order API: `/api/place_ord

# FILE: docs/websocket-architecture.md

# OpenAlgo Websockets and ZMQ

**How websocket data is distributed across the UI, Risk Management, and External Websockets.**

This page is written for traders first, with developer details toward the end. If you've ever wondered "why doesn't opening the option chain mess up my live algo?" or "can I capture broker tick data without breaking my GUI?" — this is the doc for you.

---

## The 30-second version

OpenAlgo connects to your broker's live market feed **once**. That single feed is then distributed locally to three different audiences:

1. **The UI** — the charts, quote panels, option chain etc. you see in the browser.
2. **Risk Management** — the Flow engine that watches your stoplosses, targets, and price triggers in real time.
3. **External Websockets** — your own Python, JavaScript, Excel, or AmiBroker scripts that connect to OpenAlgo to receive ticks.

All three see the same ticks at the same time. They don't compete with each other, and adding a second consumer does **not** double the load on your broker.

The plumbing that makes this possible is a small in-process message bus called **ZeroMQ (ZMQ)** plus a unified **Websocket Proxy** that the rest of the world talks to.

---

## Why is it built this way?

Every Indian broker imposes hard limits on websockets:

- Usually **1–2 websocket connections** per login (Flattrade and Kotak, for example, allow up to 2).
- Usually **1000–3000 symbols total** across those connections.
- Some brokers will silently drop subscriptions if you exceed the cap.

If every part of OpenAlgo opened its own websocket directly to the broker, you'd burn through that budget instantly — the GUI would fight your live algo, and your data-capture script would fight both.

So OpenAlgo runs **one connection to the broker per session**, demultiplexes it locally, and lets every consumer subscribe to whatever they need without anyone knowing about anyone else.

---

## The big picture

```
                ┌─────────────────────────────┐
                │     Your Broker's Feed       │
                └──────────────┬──────────────┘
                               │
                               ▼
                ┌─────────────────────────────┐
                │   Broker Websocket Adapter   │  (per broker, normalises ticks)
                │   wrapped in ConnectionPool   │  (manages 1..N broker WS sessions)
                └──────────────┬──────────────┘
                               │
                               ▼
                ┌─────────────────────────────┐
                │   ZeroMQ Bus  (port 5555)    │  internal "post office", loopback
                └──────────────┬──────────────┘
                               │
                               ▼
                ┌─────────────────────────────┐
                │  Websocket Proxy (port 8765) │  unified WSS endpoint, dedup + auth
                └───┬─────────────┬───────────┬┘
                    │             │           │
                    ▼             ▼           ▼
                  UI         MarketData    External
              (browser)        Service     (your scripts)
                                  │
                                  ▼
                            Flow / RMS
                          (stoploss, target,
                           price triggers)
```

The broker only ever sees one consumer (the pool). Everyone else taps in downstream.

---

## Roles: who does what

OpenAlgo's websocket layer is built from four distinct pieces. Each has one job. Understanding them separately makes the rest of this page (and most user questions) much easier.

### 1. The Broker Websocket Adapter

**Job:** speak the broker's proprietary websocket protocol and translate everything into a standard OpenAlgo tick format.

Every broker has its own websocket — different login flow, different message shape, different way of expressing market depth, different reconnect rules. The adapter (`broker/<broker_name>/streaming/<broker>_adapter.py`) is the *only* code in OpenAlgo that knows about those quirks. Once a tick has been parsed and normalised, it leaves the adapter looking the same regardless of which broker it came from.

The adapter does **not** know who's listening. It just publishes.

### 2. ConnectionPool

**Job:** make the broker's symbol cap invisible to everyone above it.

Most brokers cap a single websocket at 1000 symbols (Zerodha is 3000). If you need to subscribe to more than that, you need a *second* broker websocket. ConnectionPool handles that for you — it transparently opens a new broker connection when the first is full, and routes new subscriptions to whichever connection has space. From the outside, it looks like one big pipe. (Full details below in the **Connection pooling** section.)

### 3. The ZeroMQ Bus (port 5555, loopback)

**Job:** be the in-process post office between the broker side and the consumer side.

ZeroMQ here is the simplest possible "publish/subscribe" message bus. The broker adapter (or pool) publishes every normalised tick onto this bus, tagged with a topic like `NSE_RELIANCE_QUOTE`. Anything in the same machine that wants ticks can subscribe — but in practice, only the Websocket Proxy does.

Why bother with a bus instead of just calling Python functions directly?

- **Decoupling.** The broker side runs independently. If a downstream consumer is slow, ZeroMQ drops messages for that consumer rather than blocking the broker feed. Your live algo's stoploss watcher never blocks because a browser tab is being slow.
- **One-to-many fan-out for free.** Adding a new consumer (a tick recorder, a custom dashboard) doesn't require touching the broker adapter at all.
- **Resilience.** A crashing client doesn't bring down the broker session.

The bus is bound to `127.0.0.1` (loopback) only. It is not exposed off the machine. It is not a public, versioned API.

### 4. The Websocket Proxy (port 8765)

**Job:** be the *one* websocket endpoint the rest of the world talks to, a

# FILE: docs/broker-integration-guide.md

# New Broker Integration Guide

This guide walks through every step required to add a new broker to OpenAlgo. It covers the directory structure, authentication patterns, order/data APIs, symbol mapping, WebSocket streaming, master contract database, rate limiting, and all registration points across the codebase.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Directory Structure](#2-directory-structure)
3. [Step 1: Create plugin.json](#3-step-1-create-pluginjson)
4. [Step 2: Implement Authentication (auth_api.py)](#4-step-2-implement-authentication-auth_apipy)
5. [Step 3: Register the Broker Callback in brlogin.py](#5-step-3-register-the-broker-callback-in-brloginpy)
6. [Step 4: Implement Order API (order_api.py)](#6-step-4-implement-order-api-order_apipy)
7. [Step 5: Implement Data API (data.py)](#7-step-5-implement-data-api-datapy)
8. [Step 6: Implement Funds API (funds.py)](#8-step-6-implement-funds-api-fundspy)
9. [Step 7: Implement Symbol Mapping (mapping/)](#9-step-7-implement-symbol-mapping-mapping)
10. [Step 8: Implement Master Contract Database](#10-step-8-implement-master-contract-database)
11. [Step 9: Implement WebSocket Streaming](#11-step-9-implement-websocket-streaming)
12. [Step 10: Register the Broker Across the Codebase](#12-step-10-register-the-broker-across-the-codebase)
13. [Authentication Patterns Reference](#13-authentication-patterns-reference)
14. [Rate Limiting](#14-rate-limiting)
15. [Token Storage and Session Management](#15-token-storage-and-session-management)
16. [Base URL Configuration (XTS Brokers)](#16-base-url-configuration-xts-brokers)
17. [Environment Variable Reference](#17-environment-variable-reference)
18. [Testing Checklist](#18-testing-checklist)
19. [Reference Implementations](#19-reference-implementations)

---

## 1. Architecture Overview

When a user logs in via a broker, the following sequence occurs:

```
User clicks "Connect Broker"
  → blueprints/brlogin.py routes to /<broker>/callback
  → broker/<broker>/api/auth_api.py::authenticate_broker() is called
  → auth token is returned
  → utils/auth_utils.py::handle_auth_success() stores token in DB + session
  → broker/<broker>/database/master_contract_db.py downloads symbol data (async)
  → User is redirected to dashboard
```

All brokers are **dynamically discovered** at startup by `utils/plugin_loader.py`, which scans `broker/*/api/auth_api.py` for an `authenticate_broker` function and registers it as `{broker_name}_auth`.

---

## 2. Directory Structure

Every broker must follow this standardized layout:

```
broker/
└── your_broker/
    ├── plugin.json                    # Broker metadata (required)
    ├── api/
    │   ├── __init__.py                # Empty file
    │   ├── auth_api.py                # Authentication logic (required)
    │   ├── order_api.py               # Place/modify/cancel orders (required)
    │   ├── data.py                    # Quotes, depth, historical data (required)
    │   └── funds.py                   # Account balance and margins (required)
    ├── mapping/
    │   ├── transform_data.py          # OpenAlgo ↔ broker format mapping (required)
    │   ├── order_data.py              # Order response mapping (required)
    │   └── margin_data.py             # Margin calculation data (optional)
    ├── database/
    │   └── master_contract_db.py      # Symbol/token database (required)
    └── streaming/
        ├── __init__.py                # Empty file
        ├── your_broker_adapter.py     # WebSocket adapter for unified proxy (required)
        ├── your_broker_websocket.py   # Low-level WebSocket client (required)
        └── your_broker_mapping.py     # Stream data normalization (required)
```

**Reference implementations:** `broker/zerodha/`, `broker/dhan/`, `broker/angel/`

---

## 3. Step 1: Create plugin.json

Create `broker/your_broker/plugin.json`:

```json
{
    "Plugin Name": "your_broker",
    "Plugin URI": "https://openalgo.in",
    "Description": "YourBroker OpenAlgo Plugin",
    "Version": "1.0",
    "Author": "Your Name",
    "Author URI": "https://openalgo.in"
}
```

**Important:** The `"Plugin Name"` value must exactly match the directory name (`broker/your_broker/`).

---

## 4. Step 2: Implement Authentication (auth_api.py)

Create `broker/your_broker/api/auth_api.py` with an `authenticate_broker()` function.

The plugin loader (`utils/plugin_loader.py`) discovers this function automatically at startup:

```python
# utils/plugin_loader.py (how discovery works)
module_name = f"broker.{broker_name}.api.auth_api"
auth_module = importlib.import_module(module_name)
auth_function = getattr(auth_module, "authenticate_broker", None)
# Registered as: app.broker_auth_functions[f"{broker_name}_auth"]
```

### Return Value Signatures

Different authentication patterns return different tuples. The callback handler in `brlogin.py` must match:

| Pattern | Return Signature | Brokers |
|---------|-----------------|---------|
| **OAuth2 (simple)** | `(auth_token, error_message)` | zerodha, fyers, flattrade, upstox, kotak, groww, indmoney, dhan_sandbox |
| **TOTP/Credential** | `(auth_token, error_message)` | aliceblue, firstock, shoonya, zebu, samco |
| **TOTP + feed token** | `(auth_token, feed_token, error_message)` | angel, mstock, nubra, paytm, motilal |
| **XTS (dual-auth)** | `(auth_token, feed_token, user_id, error_message)` | iifl, ibulls, fivepaisaxts, compositedge, jainamxts, wisdom, pocketful, definedge |
| **OAuth + user_id** | `(auth_token, user_id, error_message)` | dhan |

### Example: OAuth2 Pattern (Simplest)

```python
# broker/your_broker/api/auth_api.py

import os
from utils.httpx_client import get_httpx_client

def authenticate_broker(request_token):
    """
    Exchange the OAuth request_token/auth_code for an access token.

    Args:
        request_token: The authorization code from broker's OAuth callback

    Returns:
        tuple: (access_token, error_message)
            - On success: (token

# FILE: docs/mcp-tool-reference.md

# OpenAlgo MCP — Tool Reference & Prompt Examples

Companion reference to the main MCP setup guide. Once the MCP server is wired into Claude Desktop, Cursor, Windsurf, Antigravity, or any other MCP-capable client, you can ask for these operations in plain English — the client decides which tool to call.

All **40 tools** shipped by the server are listed below with:

- What the tool does
- Key parameters (required / optional)
- Example prompts you can paste directly into Claude / Cursor / Antigravity / Windsurf

## Conventions

- **Default strategy tag**: `python mcp` — every MCP-triggered order is tagged so you can filter MCP activity in OpenAlgo logs and the Analyzer. Override by saying *"use strategy 'my scalper'"* in the prompt.
- **Product type defaults**: `MIS` for equity. Use `NRML` for F&O carry; `CNC` for delivery.
- **Exchange codes**: `NSE`, `BSE`, `NFO`, `BFO`, `CDS`, `BCD`, `MCX` + `NSE_INDEX` / `BSE_INDEX` for index values.
- **Lot size**: never hardcoded. The model will call `get_option_symbol` / `get_option_chain` / `get_symbol_info` to read the live `lotsize` from the broker master contract, then compute `quantity = lots × lotsize` for you.

---

## 📦 Order Management

### `place_order`

Place a single market / limit / stop-loss order.

| Param | Required | Notes |
|---|---|---|
| `symbol`, `quantity`, `action` | Yes | — |
| `exchange` | No | Default `NSE` |
| `price_type` | No | `MARKET`, `LIMIT`, `SL`, `SL-M`. Default `MARKET` |
| `product` | No | `CNC`, `NRML`, `MIS`. Default `MIS` |
| `strategy` | No | Default `python mcp` |
| `price`, `trigger_price`, `disclosed_quantity` | No | Use as applicable |

**Prompts:**
- *"Place a market buy for 100 shares of RELIANCE on NSE, intraday"*
- *"Buy 50 INFY at limit 1550, delivery product"*
- *"Sell 25 SBIN with a stop-loss at 765 and trigger 766"*

---

### `place_smart_order`

Auto-calculates the delta between your current position and the target `position_size`, then sends only the incremental order.

| Param | Required | Notes |
|---|---|---|
| `symbol`, `quantity`, `action`, `position_size` | Yes | `position_size` = your target net qty |
| Rest | No | Same defaults as `place_order` |

**Prompts:**
- *"Square off my TATAMOTORS intraday position to zero"*
- *"Scale my YESBANK position to 100 shares long"*

---

### `place_basket_order`

Fire multiple orders in one call. Each basket entry carries its own `symbol`, `exchange`, `action`, `quantity`, `pricetype`, `product`.

**Prompts:**
- *"Place a basket: buy 1 BHEL and sell 1 ZOMATO, both market MIS on NSE"*
- *"Build a basket of SBIN, HDFCBANK and ICICIBANK buys, 10 shares each, CNC"*

---

### `place_split_order`

Break a large order into equal chunks (helpful for low-liquidity names or to avoid freeze limits).

**Prompts:**
- *"Sell 500 YESBANK in slices of 50, market orders"*
- *"Split 1200 NIFTY lots across 100-lot chunks"*

---

### `place_options_order`

Single-leg option order using offset-based strike selection (ATM / ITM1–ITM50 / OTM1–OTM50). The server resolves the strike against the live option chain.

| Param | Required | Notes |
|---|---|---|
| `underlying`, `exchange`, `offset`, `option_type`, `action`, `quantity` | Yes | — |
| `expiry_date` | No | Optional if underlying includes expiry (e.g., `NIFTY28OCT25FUT`) |
| `price_type`, `product`, `price`, `trigger_price` | No | Same as `place_order` |

> **Lot size note**: if you don't know it, just ask — the assistant will pull `lotsize` from `get_option_symbol` first, then size the quantity correctly.

**Prompts:**
- *"Buy 1 lot NIFTY ATM CE expiring 28NOV25"*
- *"Short 2 lots BANKNIFTY OTM3 PE for next weekly expiry"*

---

### `place_options_multi_order`

Multi-leg option strategies (up to 20 legs). BUY legs are fired first for margin efficiency, then SELL legs. Supports per-leg overrides for `expiry_date`, `pricetype`, `price`, `product`, etc. — perfect for calendar / diagonal spreads.

**Prompts:**
- *"Place an iron condor on NIFTY 28NOV25 at OTM5 and OTM10 strikes, 1 lot each, NRML"*
- *"Build a long straddle on BANKNIFTY ATM for 25NOV25 expiry with limit orders at 250"*
- *"Diagonal NIFTY spread: buy ITM2 CE 30DEC25, sell OTM2 CE 25NOV25, 1 lot"*

---

### `modify_order`

Change price / quantity / type / trigger on a working order.

| Param | Required | Notes |
|---|---|---|
| `order_id`, `symbol`, `action`, `exchange`, `product`, `quantity`, `price` | Yes | `price` is mandatory per the REST spec — use current price if unchanged |
| `price_type`, `trigger_price`, `disclosed_quantity` | No | Sensible defaults |

**Prompts:**
- *"Modify order 250408001002736 — change limit price to 16.5"*
- *"Increase quantity of my open NIFTY CE buy order to 2 lots"*

---

### `cancel_order`

**Prompt:** *"Cancel order 250408001002736"*

---

### `cancel_all_orders`

**Prompts:**
- *"Cancel every pending order I have"*
- *"Kill all open orders for strategy 'nifty scalper'"*

---

## 📊 Positions & Holdings

### `close_all_positions`

Square off everything for a strategy.

**Prompt:** *"Close all my open positions now"*

---

### `get_open_position`

Query the current net quantity for a specific instrument.

**Prompts:**
- *"What's my current position in NHPC NSE MIS?"*
- *"How many NIFTY futures am I long?"*

---

### `get_position_book`

Every open position across instruments.

**Prompt:** *"Show me all open positions with unrealized P&L"*

---

### `get_holdings`

Delivery/CNC holdings with today's P&L, % move, and aggregate statistics.

**Prompts:**
- *"Show my demat holdings sorted by today's % change"*
- *"What's the total unrealized P&L on my long-term portfolio?"*

---

### `get_funds`

Cash, collateral, realized/unrealized M2M, utilized margin.

**Prompt:** *"How much free cash do I have for trading today?"*

---

## 📋 Order Tracking

### `get_order_status`

**Prompt:** *"Check status of order 250828000185002 — did it fill?"*

---

### `get_order_book`

Every order today with statistics (open / complete / cancelled / rej

# FILE: docs/HEALTH_MONITOR_REACT_FRONTEND.md

# Health Monitor React Frontend - Complete ✅

**Date**: 2026-01-30
**Status**: Ready to Use
**Route**: `/health`

## What's Built

### 1. API Client ✅
**File**: `frontend/src/api/health.ts`

TypeScript API client with full type safety:
- `getSimpleHealth()` - Simple 200 OK check
- `getDetailedHealthCheck()` - DB connectivity check
- `getCurrentMetrics()` - Current metrics snapshot
- `getMetricsHistory(hours)` - Historical metrics
- `getHealthStats(hours)` - Aggregated statistics
- `getActiveAlerts()` - Active alerts
- `acknowledgeAlert(id)` - Acknowledge alert
- `resolveAlert(id)` - Resolve alert
- `exportMetricsCSV(hours)` - Export to CSV

### 2. Health Monitor Dashboard ✅
**File**: `frontend/src/pages/HealthMonitor.tsx`

Beautiful, modern dashboard with:

**Features**:
- ✅ Real-time metric cards (FD, Memory, DB, WS, Threads)
- ✅ Status-based color coding (green/yellow/red)
- ✅ Active alerts panel with acknowledge button
- ✅ Live charts (File Descriptors & Memory) using lightweight-charts
- ✅ Statistics cards with min/max/avg
- ✅ Recent metrics table (last 20 samples)
- ✅ Auto-refresh every 10 seconds (toggle on/off)
- ✅ Manual refresh button
- ✅ Export to CSV button
- ✅ Responsive design (mobile-friendly)
- ✅ Dark mode support

**Components Used**:
- shadcn/ui Card, Badge, Button, Alert, Table
- lightweight-charts for time-series visualization
- lucide-react icons
- Sonner toast notifications

### 3. Table Component ✅
**File**: `frontend/src/components/ui/table.tsx`

shadcn/ui Table component (already existed in the project).

### 4. Routing ✅
**File**: `frontend/src/App.tsx`

Added:
- Import: `const HealthMonitor = lazy(() => import('@/pages/HealthMonitor'))`
- Route: `<Route path="/health" element={<HealthMonitor />} />`

## UI Preview

### Dashboard Layout

```
┌─────────────────────────────────────────────────────────┐
│  System Health Monitor      [Refresh] [Auto: ON] [CSV]  │
├─────────────────────────────────────────────────────────┤
│  ✅ System Status: PASS                                  │
│     Last updated: 30-01-2026 10:15:30                   │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │ 📁 File Desc │  │ 💾 Memory    │  │ 🗄️ Database  │  │
│  │  156 / 1024  │  │  245.5 MB    │  │  5 Conns     │  │
│  │  15.2% used  │  │  3.2% system │  │              │  │
│  │  🟢 PASS     │  │  🟢 PASS     │  │  🟢 PASS     │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                           │
│  ┌──────────────┐  ┌──────────────┐                     │
│  │ 🌐 WebSocket │  │ 🔧 Threads   │                     │
│  │  5 Conns     │  │  25 Threads  │                     │
│  │  3700 syms   │  │  None stuck  │                     │
│  │  🟢 PASS     │  │  🟢 PASS     │                     │
│  └──────────────┘  └──────────────┘                     │
│                                                           │
├─────────────────────────────────────────────────────────┤
│  🔴 Active Alerts (2)                                    │
│  ─────────────────────────────────────────────────────  │
│  ⚠️  FD WARN                                             │
│      File descriptor count elevated: 922/1024 (90.0%)   │
│                                      [Acknowledge]      │
│                                                           │
│  ⚠️  MEMORY WARN                                         │
│      Memory usage elevated: 876 MB                      │
│                                      [Acknowledge]      │
│                                                           │
├─────────────────────────────────────────────────────────┤
│  📊 File Descriptors (24h)    │  📊 Memory Usage (24h)  │
│  ─────────────────────────────│──────────────────────── │
│                                │                          │
│  [Line Chart with FD count]   │  [Line Chart with MB]   │
│                                │                          │
│                                │                          │
├─────────────────────────────────────────────────────────┤
│  📈 Statistics                                            │
│  ─────────────────────────────────────────────────────  │
│                                                           │
│  File Descriptor Stats │ Memory Stats │ Connection Stats│
│  Current: 156          │ Current: 245 │ DB Current: 5   │
│  Average: 148.5        │ Average: 238 │ DB Average: 4.8 │
│  Min/Max: 120 / 180    │ Min/Max: ...  │ WS Current: 5   │
│  Warnings: 3           │ Warnings: 1  │ WS Average: 4.2 │
│  Failures: 0           │ Failures: 0  │ Threads: 25     │
│                                                           │
├─────────────────────────────────────────────────────────┤
│  📋 Recent Metrics (Last 20 Samples)                     │
│  ─────────────────────────────────────────────────────  │
│                                                           │
│  Time      FDs  Memory  DB  WS  Threads  Status         │
│  10:15:30  156  245MB   5   5   25       🟢 pass        │
│  10:15:20  158  247MB   5   5   26       🟢 pass        │
│  10:15:10  155  244MB   5   5   25       🟢 pass        │
│  ...                                                      │
└─────────────────────────────────────────────────────────┘
```

## Color Coding

### Status Colors
- **🟢 PASS (Green)**: All metrics healthy
  - Border: `border-green-500`
  - Background: `bg-green-50 dark:bg-green-950`
  - Text: `text-green-600 dark:text-green-400`

- **🟡 WARN (Yellow)**: Degraded but functional
  - Border: `border-yellow-500`
  - Background: `bg-yellow-50 dark:bg-yellow-950`
  - Text: `text-yellow-600 dark:text-yellow-400`

- **🔴 FAIL (Red)**: Critical issue
  - Border: `border-red-500`
  - Background: `bg-red-50 dark:bg-red-950`
  - Text: `text-red-600 dark:text-red-400`

### Dark Mode Support
All components fully support dark

# FILE: docs/websocket-quote-feed.md

# WebSocket Quote Feed - Integration Guide

This guide demonstrates how to integrate with OpenAlgo's WebSocket quote feed for real-time market data streaming.

## Overview

OpenAlgo provides a unified WebSocket server (port 8765) that streams market data from 29 brokers in a normalized format. Clients can subscribe to LTP, Quote, or Depth modes.

## Connection Details

| Parameter | Value |
|-----------|-------|
| Host | `127.0.0.1` or your server IP |
| Port | `8765` |
| Protocol | `ws://` or `wss://` (with SSL) |
| Authentication | API key required |

## Message Protocol

### 1. Authentication

```json
// Request
{
    "action": "authenticate",
    "api_key": "your_64_char_api_key"
}

// Response
{
    "status": "authenticated",
    "message": "Connected to OpenAlgo WebSocket"
}
```

### 2. Subscribe (LTP Mode)

```json
// Request
{
    "action": "subscribe",
    "symbols": [
        {"symbol": "SBIN", "exchange": "NSE"},
        {"symbol": "RELIANCE", "exchange": "NSE"}
    ],
    "mode": "LTP"
}

// Response
{
    "status": "subscribed",
    "count": 2,
    "symbols": ["SBIN.NSE", "RELIANCE.NSE"]
}
```

### 3. Subscribe (Quote Mode)

```json
// Request
{
    "action": "subscribe",
    "symbols": [
        {"symbol": "SBIN", "exchange": "NSE"}
    ],
    "mode": "QUOTE"
}
```

### 4. Subscribe (Depth Mode)

```json
// Request
{
    "action": "subscribe",
    "symbols": [
        {"symbol": "NIFTY24JAN24000CE", "exchange": "NFO"}
    ],
    "mode": "DEPTH"
}
```

### 5. Unsubscribe

```json
// Request
{
    "action": "unsubscribe",
    "symbols": [
        {"symbol": "SBIN", "exchange": "NSE"}
    ]
}

// Response
{
    "status": "unsubscribed",
    "count": 1
}
```

## Data Formats

### LTP Data

```json
{
    "type": "market_data",
    "mode": "LTP",
    "symbol": "SBIN",
    "exchange": "NSE",
    "ltp": 625.50,
    "timestamp": "2024-01-15T10:30:00+05:30"
}
```

### Quote Data

```json
{
    "type": "market_data",
    "mode": "QUOTE",
    "symbol": "SBIN",
    "exchange": "NSE",
    "ltp": 625.50,
    "open": 620.00,
    "high": 628.00,
    "low": 618.50,
    "close": 622.00,
    "volume": 1500000,
    "change": 3.50,
    "change_percent": 0.56,
    "timestamp": "2024-01-15T10:30:00+05:30"
}
```

### Depth Data

```json
{
    "type": "market_data",
    "mode": "DEPTH",
    "symbol": "SBIN",
    "exchange": "NSE",
    "ltp": 625.50,
    "depth": {
        "buy": [
            {"price": 625.45, "quantity": 1000, "orders": 5},
            {"price": 625.40, "quantity": 2500, "orders": 8},
            {"price": 625.35, "quantity": 1800, "orders": 6},
            {"price": 625.30, "quantity": 3200, "orders": 12},
            {"price": 625.25, "quantity": 2100, "orders": 7}
        ],
        "sell": [
            {"price": 625.50, "quantity": 800, "orders": 3},
            {"price": 625.55, "quantity": 1200, "orders": 4},
            {"price": 625.60, "quantity": 1500, "orders": 5},
            {"price": 625.65, "quantity": 2000, "orders": 6},
            {"price": 625.70, "quantity": 1700, "orders": 5}
        ]
    },
    "timestamp": "2024-01-15T10:30:00+05:30"
}
```

## Python Client Example

### Basic Connection

```python
import asyncio
import websockets
import json

async def connect_quote_feed():
    uri = "ws://127.0.0.1:8765"
    api_key = "your_64_char_api_key"

    async with websockets.connect(uri) as ws:
        # Authenticate
        await ws.send(json.dumps({
            "action": "authenticate",
            "api_key": api_key
        }))
        response = await ws.recv()
        print(f"Auth: {response}")

        # Subscribe to symbols
        await ws.send(json.dumps({
            "action": "subscribe",
            "symbols": [
                {"symbol": "SBIN", "exchange": "NSE"},
                {"symbol": "RELIANCE", "exchange": "NSE"}
            ],
            "mode": "QUOTE"
        }))
        response = await ws.recv()
        print(f"Subscribe: {response}")

        # Receive market data
        while True:
            data = await ws.recv()
            tick = json.loads(data)
            print(f"{tick['symbol']}: {tick['ltp']}")

asyncio.run(connect_quote_feed())
```

### With Reconnection

```python
import asyncio
import websockets
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class QuoteFeedClient:
    def __init__(self, host="127.0.0.1", port=8765, api_key=None):
        self.uri = f"ws://{host}:{port}"
        self.api_key = api_key
        self.ws = None
        self.subscriptions = []
        self.reconnect_delay = 5

    async def connect(self):
        while True:
            try:
                self.ws = await websockets.connect(self.uri)
                logger.info("Connected to WebSocket")

                # Authenticate
                await self._authenticate()

                # Resubscribe if reconnecting
                if self.subscriptions:
                    await self._resubscribe()

                # Start receiving
                await self._receive_loop()

            except websockets.ConnectionClosed:
                logger.warning("Connection closed, reconnecting...")
                await asyncio.sleep(self.reconnect_delay)
            except Exception as e:
                logger.error(f"Error: {e}")
                await asyncio.sleep(self.reconnect_delay)

    async def _authenticate(self):
        await self.ws.send(json.dumps({
            "action": "authenticate",
            "api_key": self.api_key
        }))
        response = await self.ws.recv()
        data = json.loads(response)
        if data.get("status") != "authenticated":
            raise Exception("Authentication failed")
        logger.info("Authenticated")

    async def subscribe(self, symbols, mode="QUOTE"):
        self.subscriptions = symbols
        await self.ws.send(json.dumps({
            "action": "subscribe",
            "symbols": symbols,
            "mode": mode
        }))
        r

# FILE: docs/design/TRACKER.md

# OpenAlgo Developer Documentation Tracker

## Progress Overview

| # | Module | Status | Last Updated |
|---|--------|--------|--------------|
| 00 | Directory Structure | ✅ Complete | 2026-02-22 |
| 01 | Frontend Architecture | ✅ Complete | 2026-02-22 |
| 02 | Backend Architecture | ✅ Complete | 2026-02-22 |
| 03 | Login & Broker Login Flow | ✅ Complete | 2026-02-22 |
| 04 | Cache Architecture | ✅ Complete | 2026-01-21 |
| 05 | Security Architecture | ✅ Complete | 2026-01-21 |
| 06 | WebSockets Architecture | ✅ Complete | 2026-02-22 |
| 07 | Sandbox Architecture | ✅ Complete | 2026-02-22 |
| 08 | Historify Architecture | ✅ Complete | 2026-01-21 |
| 09 | REST API Documentation | ✅ Complete | 2026-02-22 |
| 10 | Flow Architecture | ✅ Complete | 2026-01-21 |
| 11 | Docker Configuration | ✅ Complete | 2026-01-21 |
| 12 | Ubuntu Server Installation | ✅ Complete | 2026-01-21 |
| 13 | Chartink Architecture | ✅ Complete | 2026-01-21 |
| 14 | TradingView & GoCharting | ✅ Complete | 2026-01-21 |
| 15 | Basic UI Elements & Analytics | ✅ Complete | 2026-02-22 |
| 16 | Centralized Logging | ✅ Complete | 2026-01-21 |
| 17 | Connection Pooling | ✅ Complete | 2026-01-21 |
| 18 | Database Structure | ✅ Complete | 2026-01-21 |
| 19 | PlaceOrder Call Flow | ✅ Complete | 2026-01-21 |
| 20 | Design Principles | ✅ Complete | 2026-02-22 |
| 21 | Admin Section | ✅ Complete | 2026-01-21 |
| 22 | Log Section | ✅ Complete | 2026-01-21 |
| 23 | IP Security | ✅ Complete | 2026-01-21 |
| 24 | Browser Security | ✅ Complete | 2026-01-21 |
| 25 | Latency Monitor | ✅ Complete | 2026-01-21 |
| 26 | Traffic Logs | ✅ Complete | 2026-01-21 |
| 27 | Service Layer | ✅ Complete | 2026-01-21 |
| 28 | Environment Configuration | ✅ Complete | 2026-01-21 |
| 29 | Ngrok Configuration | ✅ Complete | 2026-01-21 |
| 30 | Upgrade Procedure | ✅ Complete | 2026-01-21 |
| 31 | Utils Functionalities | ✅ Complete | 2026-01-21 |
| 32 | Master Contract Download | ✅ Complete | 2026-02-22 |
| 33 | Broker Folder Explanations | ✅ Complete | 2026-02-22 |
| 34 | App Startup | ✅ Complete | 2026-01-21 |
| 35 | Development & Testing Guide | ✅ Complete | 2026-01-21 |
| 36 | Rate Limiting Guide | ✅ Complete | 2026-01-21 |
| 37 | API Key & Playground | ✅ Complete | 2026-01-21 |
| 38 | Python Strategies Hosting | ✅ Complete | 2026-01-21 |
| 39 | Strategy Module | ✅ Complete | 2026-01-21 |
| 40 | Logout & Session Expiry | ✅ Complete | 2026-01-21 |
| 41 | MCP Architecture | ✅ Complete | 2026-02-22 |
| 42 | Action Center | ✅ Complete | 2026-01-21 |
| 43 | Telegram Bot Configuration | ✅ Complete | 2026-01-21 |
| 43b | Toast Notifications | ✅ Complete | 2026-01-21 |
| 44 | PnL Tracker | ✅ Complete | 2026-02-22 |
| 46 | Search | ✅ Complete | 2026-01-21 |
| 47 | SMTP Configuration | ✅ Complete | 2026-01-21 |
| 48 | Password Reset | ✅ Complete | 2026-01-21 |
| 49 | Themes | ✅ Complete | 2026-01-21 |
| 50 | TOTP Configuration | ✅ Complete | 2026-01-21 |
| 51 | Broker & System Config | ✅ Complete | 2026-01-21 |
| 52 | Broker Factory | ✅ Complete | 2026-02-22 |

## Status Legend
- ✅ Complete
- 🔄 In Progress
- ⏳ Pending

## Documentation Standards
- Each module has its own folder with `README.md`
- Include ASCII flow diagrams where applicable
- Add code examples for implementation details
- Keep explanations brief but comprehensive
- Target audience: Beginner to intermediate developers


# FILE: docs/design/README.md

# OpenAlgo Developer Documentation

Welcome to the OpenAlgo Developer Bible - a comprehensive guide for understanding and working with the OpenAlgo algorithmic trading platform.

## What is OpenAlgo?

OpenAlgo is a production-ready algorithmic trading platform built with Flask (backend) and React 19 (frontend). It provides a unified API layer across 29 Indian brokers, enabling seamless integration with TradingView, Amibroker, Excel, Python, and AI agents.

## Documentation Index

### Core Architecture
| Module | Description |
|--------|-------------|
| [00-Directory Structure](./00-directory-structure/) | Complete project directory map and navigation guide |
| [01-Frontend](./01-frontend/) | React 19 SPA architecture, components, state management |
| [02-Backend](./02-backend/) | Flask application structure, blueprints, services |
| [18-Database](./18-database/) | Database schema, 5-DB architecture, optimization |
| [20-Design Principles](./20-design-principles/) | Architectural patterns and coding conventions |

### Authentication & Security
| Module | Description |
|--------|-------------|
| [03-Login & Broker Flow](./03-login-broker-flow/) | User auth, OAuth2, broker integration |
| [05-Security Architecture](./05-security-architecture/) | Overall security design |
| [23-IP Security](./23-ip-security/) | IP banning and rate limiting |
| [24-Browser Security](./24-browser-security/) | CORS, CSP, CSRF protection |

### Trading Operations
| Module | Description |
|--------|-------------|
| [09-REST API](./09-rest-api/) | Complete API endpoint documentation |
| [19-PlaceOrder Flow](./19-placeorder-flow/) | Order execution pipeline |
| [15-UI Elements](./15-ui-elements/) | OrderBook, TradeBook, Positions, Holdings, Dashboard |

### Real-Time & Data
| Module | Description |
|--------|-------------|
| [06-WebSockets](./06-websockets/) | Market data streaming architecture |
| [04-Cache Architecture](./04-cache-architecture/) | Caching strategies and TTL |
| [08-Historify](./08-historify/) | Historical data management |
| [17-Connection Pooling](./17-connection-pooling/) | HTTP and WebSocket pooling |

### Strategies & Automation
| Module | Description |
|--------|-------------|
| [10-Flow Architecture](./10-flow/) | Visual workflow builder |
| [13-Chartink](./13-chartink/) | Chartink scanner integration |
| [14-TradingView & GoCharting](./14-tradingview-gocharting/) | Alert webhook setup |

### Analytics Tools
| Module | Description |
|--------|-------------|
| [15-UI Elements](./15-basic-ui/) | Trading UI and analytics tools (GEX, IV Smile, OI Profile, etc.) |

### Sandbox Trading
| Module | Description |
|--------|-------------|
| [07-Sandbox](./07-sandbox/) | Analyzer mode with sandbox capital |

### Monitoring & Logs
| Module | Description |
|--------|-------------|
| [16-Centralized Logging](./16-centralized-logging/) | Logging architecture |
| [22-Log Section](./22-log-section/) | Live and Sandbox logs UI |
| [25-Latency Monitor](./25-latency-monitor/) | API latency tracking |
| [26-Traffic Logs](./26-traffic-logs/) | HTTP traffic monitoring |

### Administration
| Module | Description |
|--------|-------------|
| [21-Admin Section](./21-admin-section/) | Admin features and controls |

### Deployment
| Module | Description |
|--------|-------------|
| [11-Docker](./11-docker/) | Docker containerization |
| [12-Ubuntu Installation](./12-ubuntu-installation/) | Server deployment guide |

## Quick Start

```bash
# Install uv package manager
pip install uv

# Configure environment
cp .sample.env .env

# Run application
uv run app.py
```

## Key Files Reference

| File | Purpose |
|------|---------|
| `app.py` | Main Flask entry point |
| `frontend/src/App.tsx` | React router configuration |
| `restx_api/__init__.py` | REST API namespace registry |
| `broker/*/plugin.json` | Broker plugin metadata |

## Progress Tracker

See [TRACKER.md](./TRACKER.md) for documentation completion status.


# FILE: examples/nodejs/readme.md

OpenAlgo Nodejs SDK Examples

# FILE: examples/go/readme.md

OpenAlgo Go SDK Examples

# FILE: examples/python/placing ATM order.py

from openalgo import api

print("🔁 OpenAlgo Python Bot is running.")

# ------------------------------------------
# Initialize API client
# ------------------------------------------
client = api(
    api_key="83ad96143dd5081d033abcfd20e9108daee5708fbea404121a762bed1e498dd0",
    host="http://127.0.0.1:5000",
)

# ------------------------------------------
# Fetch NIFTY Spot (must print immediately)
# ------------------------------------------
quote = client.quotes(symbol="NIFTY", exchange="NSE_INDEX")
print("NIFTY QUOTE:", quote)

# ------------------------------------------
# Place NIFTY ATM Option Order - 09DEC25
# ------------------------------------------
response = client.optionsorder(
    strategy="python",
    underlying="NIFTY",  # Underlying Index
    exchange="NSE_INDEX",  # Index exchange
    expiry_date="09DEC25",  # Correct expiry
    offset="OTM2",  # Auto-select ATM strike
    option_type="CE",  # CE or PE
    action="BUY",  # BUY or SELL
    quantity=75,  # 1 Lot = 75
    pricetype="MARKET",  # MARKET or LIMIT
    product="NRML",  # NRML or MIS
    splitsize=0,  # 0 = no split
)

print("ORDER RESPONSE:", response)


# FILE: examples/python/heatmap.py

import pandas as pd
import plotly.express as px
from openalgo import api

# ---------------------------------------------------
# OpenAlgo Client
# ---------------------------------------------------
client = api(
    api_key="7371cc58b9d30204e5fee1d143dc8cd926bcad90c24218201ad81735384d2752",
    host="http://127.0.0.1:5000",
)

print("🔁 OpenAlgo Python Bot is running.")

# ---------------------------------------------------
# NIFTY 50 SYMBOLS
# ---------------------------------------------------
symbols = [
    "INDIGO",
    "TRENT",
    "HINDUNILVR",
    "HCLTECH",
    "WIPRO",
    "INFY",
    "TATACONSUM",
    "TATASTEEL",
    "ITC",
    "ASIANPAINT",
    "SBILIFE",
    "LT",
    "SHRIRAMFIN",
    "BEL",
    "SBIN",
    "COALINDIA",
    "KOTAKBANK",
    "TCS",
    "SUNPHARMA",
    "MAXHEALTH",
    "NESTLEIND",
    "RELIANCE",
    "ETERNAL",
    "APOLLOHOSP",
    "ICICIBANK",
    "GRASIM",
    "ULTRACEMCO",
    "ADANIENT",
    "AXISBANK",
    "DRREDDY",
    "TECHM",
    "TMPV",
    "JIOFIN",
    "NTPC",
    "BAJFINANCE",
    "BHARTIARTL",
    "POWERGRID",
    "HINDALCO",
    "HDFCBANK",
    "TITAN",
    "HDFCLIFE",
    "MARUTI",
    "BAJAJFINSV",
    "ADANIPORTS",
    "CIPLA",
    "JSWSTEEL",
    "BAJAJ-AUTO",
    "ONGC",
    "EICHERMOT",
    "M&M",
]

# ---------------------------------------------------
# FETCH LIVE QUOTES
# ---------------------------------------------------
quote_symbols = [{"symbol": s, "exchange": "NSE"} for s in symbols]
response = client.multiquotes(symbols=quote_symbols)

rows = []

print("\n📊 Live Market Data:")
for item in response["results"]:
    symbol = item["symbol"]
    ltp = item["data"]["ltp"]
    prev_close = item["data"]["prev_close"]

    change_pct = round(((ltp - prev_close) / prev_close) * 100, 2)

    # Print immediately (rule)
    print(f"{symbol} | LTP: {ltp} | Change: {change_pct}%")

    rows.append([symbol, change_pct])

# ---------------------------------------------------
# PREPARE + SORT DATA
# ---------------------------------------------------
df = pd.DataFrame(rows, columns=["Symbol", "Change"])

# 🔥 SORT: TOP GAINERS → BOTTOM LOSERS
df = df.sort_values("Change", ascending=False).reset_index(drop=True)

# Grid: 10 columns x 5 rows
cols = 10
df["row"] = df.index // cols
df["col"] = df.index % cols

pivot_values = df.pivot(index="row", columns="col", values="Change")
pivot_labels = df.pivot(index="row", columns="col", values="Symbol")

# ---------------------------------------------------
# HEATMAP PLOT
# ---------------------------------------------------
fig = px.imshow(pivot_values, color_continuous_scale="RdYlGn", aspect="auto")

fig.update_traces(
    text=pivot_labels.values,
    texttemplate="%{text}<br>%{z:.2f}%",
    hovertemplate="Symbol: %{text}<br>Change: %{z:.2f}%",
)

fig.update_layout(
    title="🔥 NIFTY 50 Sorted Heatmap (%)",
    xaxis=dict(type="category", title=""),
    yaxis=dict(type="category", autorange="reversed", title=""),
    template="plotly_dark",
    height=600,
)


# FILE: examples/python/plotting candles.py

"""
RELIANCE 5-Minute Candlestick Chart - Last 20 Days
With Bollinger Bands (Top) and RSI (Bottom)
Author : OpenAlgo GPT
Description: Plots RELIANCE 5m candlestick chart using Plotly with category x-axis
"""

print("🔁 OpenAlgo Python Bot is running.")

from datetime import datetime

import pandas as pd
import plotly.graph_objects as go
from openalgo import api, ta
from plotly.subplots import make_subplots

# ───────────────────────── CONFIG ─────────────────────────
API_KEY = "3f75e26648a543a886c9b38332a6942e30e0710bbf0488cf432ef27745de8ae7"
API_HOST = "http://127.0.0.1:5000"

SYMBOL = "RELIANCE"
EXCHANGE = "NSE"
INTERVAL = "5m"

# Date range controls (last 20 days)
END_DATE = datetime.now().strftime("%Y-%m-%d")
START_DATE = (datetime.now() - pd.Timedelta(days=20)).strftime("%Y-%m-%d")

# ─────────────────────── INIT CLIENT ──────────────────────
client = api(api_key=API_KEY, host=API_HOST)


# ───────────────────── FETCH HISTORICAL DATA ─────────────────────
def fetch_historical_data():
    """Fetch 5m historical data for RELIANCE"""
    print(f"Fetching {SYMBOL} {INTERVAL} data from {START_DATE} to {END_DATE}...")

    response = client.history(
        symbol=SYMBOL,
        exchange=EXCHANGE,
        interval=INTERVAL,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    # Print the raw response
    print(f"History Response: {response}")

    # OpenAlgo history() returns DataFrame directly (not a dict)
    if isinstance(response, pd.DataFrame):
        df = response.copy()
    else:
        # Fallback if it returns dict
        df = pd.DataFrame(response.get("data", response))

    # Check if DataFrame is empty
    if df.empty:
        raise ValueError("No data received from API")

    # Handle index - if timestamp is already the index
    if df.index.name == "timestamp" or "timestamp" not in df.columns:
        df.index = pd.to_datetime(df.index)
    else:
        df["datetime"] = pd.to_datetime(df["timestamp"])
        df = df.set_index("datetime")

    df = df.sort_index()

    # Standardize column names to lowercase
    df.columns = df.columns.str.lower()

    # Ensure we have OHLC columns
    required_cols = ["open", "high", "low", "close"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    print(f"Fetched {len(df)} candles")
    print(f"Date range: {df.index.min()} to {df.index.max()}")

    return df


# ───────────────────── INDICATOR SETTINGS ─────────────────────
RSI_PERIOD = 20
BB_PERIOD = 15
BB_STD_DEV = 2.0


# ───────────────────── CALCULATE INDICATORS ─────────────────────
def calculate_indicators(df: pd.DataFrame):
    """Calculate RSI and Bollinger Bands using OpenAlgo ta library"""

    # RSI (20)
    df["rsi"] = ta.rsi(df["close"], period=RSI_PERIOD)

    # Bollinger Bands (15, 2)
    bb_upper, bb_middle, bb_lower = ta.bbands(df["close"], period=BB_PERIOD, std_dev=BB_STD_DEV)
    df["bb_upper"] = bb_upper
    df["bb_middle"] = 

# FILE: examples/python/ltp_example.py

"""
OpenAlgo WebSocket Feed Example
"""

import time

from openalgo import api

# Initialize feed client with explicit parameters
client = api(
    api_key="7653f710c940cdf1d757b5a7d808a60f43bc7e9c0239065435861da2869ec0fc",  # Replace with your API key
    host="http://127.0.0.1:5000",  # Replace with your API host
    ws_url="ws://127.0.0.1:8765",  # Explicit WebSocket URL (can be different from REST API host)
)

# MCX instruments for testing
instruments_list = [{"exchange": "NSE", "symbol": "TCS", "exchange": "NSE", "symbol": "INFY"}]


def on_data_received(data):
    print("LTP Update:")
    print(data)


# Connect and subscribe
client.connect()
client.subscribe_ltp(instruments_list, on_data_received=on_data_received)

# Poll LTP data a few times
for i in range(100):
    print(f"\nPoll {i + 1}:")
    print(client.get_ltp())
    time.sleep(0.5)

# Cleanup
client.unsubscribe_ltp(instruments_list)
client.disconnect()


# FILE: examples/python/emacrossover_strategy_python.py

"""
===============================================================================
                EMA CROSSOVER WITH FIXED DATETIME HANDLING
                            OpenAlgo Trading Bot
===============================================================================

Run standalone:
    export OPENALGO_API_KEY="your-api-key"
    python emacrossover_strategy_python.py

Run via OpenAlgo's /python strategy runner:
    OPENALGO_API_KEY            : injected per-strategy (PR #1247).
    OPENALGO_STRATEGY_EXCHANGE  : set from the strategy's `exchange` config
                                  (NSE / BSE / NFO / BFO / MCX / BCD / CDS / CRYPTO).
                                  Drives both this script's trading exchange and
                                  the host's calendar/holiday gating, so the two
                                  always agree (no NSE-only orders on an MCX-gated
                                  strategy).
    STRATEGY_ID / STRATEGY_NAME : injected for log/order tagging.
    HOST_SERVER / WEBSOCKET_URL : inherited from OpenAlgo's .env.
    No code changes required.
"""

import os
import threading
import time
from datetime import datetime, timedelta

import pandas as pd
from openalgo import api

# ===============================================================================
# TRADING CONFIGURATION
# ===============================================================================

# API Configuration — read from environment with sensible fallbacks.
# When launched via OpenAlgo's /python runner, these come from the platform:
#   OPENALGO_API_KEY : injected per-strategy (decrypted from DB)
#   HOST_SERVER      : inherited from OpenAlgo's .env
#   WEBSOCKET_URL    : inherited from OpenAlgo's .env
API_KEY = os.getenv("OPENALGO_API_KEY", "openalgo-apikey")
API_HOST = os.getenv("HOST_SERVER", "http://127.0.0.1:5000")
WS_URL = os.getenv("WEBSOCKET_URL", "ws://127.0.0.1:8765")

# Trade Settings
# EXCHANGE prefers OPENALGO_STRATEGY_EXCHANGE (set by /python runner from the
# strategy's config) so the script trades on whichever exchange the host is
# gating its calendar against. Falls back to EXCHANGE env var, then NSE.
SYMBOL = os.getenv("SYMBOL", "NHPC")              # Stock to trade
EXCHANGE = os.getenv(
    "OPENALGO_STRATEGY_EXCHANGE",
    os.getenv("EXCHANGE", "NSE"),
)                                                 # NSE, BSE, NFO, BFO, MCX, BCD, CDS, CRYPTO
QUANTITY = int(os.getenv("QUANTITY", "1"))        # Number of shares
PRODUCT = os.getenv("PRODUCT", "MIS")             # MIS (Intraday) or CNC (Delivery)

# Strategy Parameters
FAST_EMA_PERIOD = int(os.getenv("FAST_EMA_PERIOD", "2"))
SLOW_EMA_PERIOD = int(os.getenv("SLOW_EMA_PERIOD", "4"))
CANDLE_TIMEFRAME = os.getenv("CANDLE_TIMEFRAME", "5m")  # 1m, 5m, 15m, 30m, 1h, 1d

# Historical Data Lookback (1-30 days)
LOOKBACK_DAYS = int(os.getenv("LOOKBACK_DAYS", "3"))

# Risk Management (Rupees)
STOPLOSS = float(os.getenv("STOPLOSS", "0.1"))
TARGET = float(os.getenv("TARGET", "0.2")

# FILE: examples/python/multiquotes_example.py

from openalgo import api

# Initialize client
client = api(
    api_key="c32eb9dee6673190bb9dfab5f18ef0a96b0d76ba484cd36bc5ca5f7ebc8745bf",
    host="http://127.0.0.1:5000",
)

# Fetch multiple quotes
response = client.multiquotes(
    symbols=[
        {"symbol": "RELIANCE", "exchange": "NSE"},
        {"symbol": "TCS", "exchange": "NSE"},
        {"symbol": "INFY", "exchange": "NSE"},
    ]
)

print(response)

