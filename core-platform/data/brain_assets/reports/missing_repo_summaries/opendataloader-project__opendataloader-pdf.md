# Missing Repo Summary Source: opendataloader-project/opendataloader-pdf

- URL: https://github.com/opendataloader-project/opendataloader-pdf
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/opendataloader-project__opendataloader-pdf
- Clone Status: cloned
- Language: Java
- Stars: 21176
- Topics: a11y, accessibility, ai, bounding-box, document-parsing, eaa, html, json, markdown, ocr, ocr-recognition, pdf, pdf-accessibility, pdf-converter, pdf-extraction, pdf-parser, pdf-ua, rag, tables, tagged-pdf
- Description: PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.

## Extracted README / Docs / Examples



# FILE: README.md

<!-- AI-AGENT-SUMMARY
name: opendataloader-pdf
category: PDF data extraction, PDF accessibility automation
license: Apache-2.0
solves: [PDF to structured data for RAG/LLM pipelines, accelerate PDF accessibility remediation — layout analysis + auto-tagging to Tagged PDF as foundation for PDF/UA (first open-source end-to-end)]
input: PDF files (digital, scanned, tagged)
output: Markdown, JSON (with bounding boxes), HTML, Tagged PDF, PDF/UA (enterprise)
sdk: Python, Node.js, Java
requirements: Java 11+
pricing: open-source core (data extraction, layout analysis, auto-tagging to Tagged PDF), enterprise add-on (PDF/UA export, accessibility studio)
extraction-benchmark: #1 overall extraction accuracy (0.907) in hybrid mode, 0.928 table extraction accuracy, 0.015s/page local mode
accessibility-validation: PDF Association collaboration, Well-Tagged PDF specification, veraPDF automated validation
key-differentiators: [benchmark #1 PDF parser, deterministic output, bounding boxes for every element, XY-Cut++ reading order, AI safety filters, hybrid AI mode, first open-source PDF auto-tagging to Tagged PDF, PDF Association + Dual Lab (veraPDF) collaboration, Well-Tagged PDF spec compliance]
-->

# OpenDataLoader PDF

**PDF Parser for AI-ready data. Automate PDF accessibility. Open-source.**

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf/blob/main/LICENSE)
[![PyPI version](https://img.shields.io/pypi/v/opendataloader-pdf.svg)](https://pypi.org/project/opendataloader-pdf/)
[![npm version](https://img.shields.io/npm/v/@opendataloader/pdf.svg)](https://www.npmjs.com/package/@opendataloader/pdf)
[![Maven Central](https://img.shields.io/maven-central/v/org.opendataloader/opendataloader-pdf-core.svg)](https://search.maven.org/artifact/org.opendataloader/opendataloader-pdf-core)
[![Java](https://img.shields.io/badge/Java-11%2B-blue.svg)](https://github.com/opendataloader-project/opendataloader-pdf#java)

<a href="https://trendshift.io/repositories/21917" target="_blank"><img src="https://trendshift.io/api/badge/repositories/21917" alt="opendataloader-project%2Fopendataloader-pdf | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

🔍 **PDF parser for AI data extraction** — Extract Markdown, JSON (with bounding boxes), and HTML from any PDF. #1 in benchmarks (0.907 overall). Deterministic local mode + AI hybrid mode for complex pages.

- **How accurate is it?** — #1 in benchmarks: 0.907 overall, 0.928 table accuracy across 200 real-world PDFs including multi-column and scientific papers. Deterministic local mode + AI hybrid mode for complex pages ([benchmarks](#extraction-benchmarks))
- **Scanned PDFs and OCR?** — Yes. Built-in OCR (80+ languages) in hybrid mode. Works with poor-quality scans at 300 DPI+ ([hybrid mode](#hybrid-mode-1-accuracy-for-complex-pdfs))
- **Tables, formulas, images, charts?** — Yes. Complex/borderless tables, LaTeX formulas, and AI-generated picture/chart descriptions all via hybrid mode ([hybrid mode](#hybrid-mode-1-accuracy-for-complex-pdfs))
- **How do I use this for RAG?** — `pip install opendataloader-pdf`, convert in 3 lines. Outputs structured Markdown for chunking, JSON with bounding boxes for source citations, and HTML. LangChain integration available. Python, Node.js, Java SDKs ([quick start](#get-started-in-30-seconds) | [LangChain](#langchain-integration))

♿ **PDF accessibility automation** — Auto-tag untagged PDFs into screen-reader-ready Tagged PDFs at scale. First open-source tool to generate Tagged PDFs end-to-end.

- **What's the problem?** — Accessibility regulations are now enforced worldwide. Manual PDF remediation costs $50–200 per document and doesn't scale ([regulations](#pdf-accessibility--pdfua-conversion))
- **What's free?** — Layout analysis + auto-tagging (Apache 2.0). Untagged PDF in → Tagged PDF out. No proprietary SDK dependency ([auto-tagging](#auto-tagging))
- **What about PDF/UA compliance?** — Converting Tagged PDF to PDF/UA-1 or PDF/UA-2 is an enterprise add-on. Auto-tagging generates the Tagged PDF; PDF/UA export is the final step ([pipeline](#accessibility-pipeline))
- **Why trust this?** — Built in collaboration with [Dual Lab](https://duallab.com) ([veraPDF](https://verapdf.org) developers) based on [PDF Association](https://pdfa.org) specifications, best practice guides and expertise of the [PDF Community](https://pdfa.org/community/). Auto-tagging follows the [Well-Tagged PDF specification](https://pdfa.org/wtpdf/), validated with veraPDF ([collaboration](https://opendataloader.org/docs/tagged-pdf-collaboration))

## Get Started in 30 Seconds

**Requires**: Java 11+ and Python 3.10+ ([Node.js](https://opendataloader.org/docs/quick-start-nodejs) | [Java](https://opendataloader.org/docs/quick-start-java) also available)

> Before you start: run `java -version`. If not found, install JDK 11+ from [Adoptium](https://adoptium.net/).

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# Batch all files in one call — each convert() spawns a JVM process, so repeated calls are slow
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

![OpenDataLoader PDF layout analysis — headings, tables, images detected with bounding boxes](https://raw.githubusercontent.com/opendataloader-project/opendataloader-pdf/main/samples/image/example_annotated_pdf.png)

*Annotated PDF output — each element (heading, paragraph, table, image) detected with bounding boxes and semantic type.*

## What Problems Does This Solve?

| Problem | Solution | Status |
|---------|----------|--------|
| **PDF structure lost during parsing** — wrong reading order, broken tables, no element coordinates | Deterministic local PDF to Markdown/JSON with bounding boxes, XY-Cut++ reading order | Shipped |
| **Complex tables, scanned PDFs, formulas, charts** need AI-level understanding | Hybrid mode routes complex pages to AI backend (#1 in benchmarks) | Shipped |
| **Manual PDF remediation cost** — Accessibility regulations (EAA, ADA, Section 508) demand Tagged PDFs. Manual remediation costs $50–200/doc | Auto-tag untagged PDFs into Tagged PDFs (free, Apache 2.0). Foundation for PDF/UA workflows; full PDF/UA-1/2 export is an enterprise add-on | Auto-tag: Shipped. PDF/UA export: Enterprise |

## Capability Matrix

| Capability | Supported | Tier |
|------------|-----------|------|
| **Data extraction** | | |
| Extract text with correct reading order | Yes | Free |
| Bounding boxes for every element | Yes | Free |
| Table extraction (simple borders) | Yes | Free |
| Table extraction (complex/borderless) | Yes | Free (Hybrid) |
| Heading hierarchy detection | Yes | Free |
| List detection (numbered, bulleted, nested) | Yes | Free |
| Image extraction with coordinates | Yes | Free |
| AI chart/image description | Yes | Free (Hybrid) |
| OCR for scanned PDFs | Yes | Free (Hybrid) |
| Formula extraction (LaTeX) | Yes | Free (Hybrid) |
| Tagged PDF structure extraction | Yes | Free |
| AI safety (prompt injection filtering) | Yes | Free |
| Header/footer/watermark filtering | Yes | Free |
| **Accessibility** | | |
| Auto-tagging → Tagged PDF for untagged PDFs | Yes | Free (Apache 2.0) |
| PDF/UA-1, PDF/UA-2 export | 💼 Available | Enterprise |
| Accessibility studio (visual editor) | 💼 Available | Enterprise |
| **Limitations** | | |
| Process Word/Excel/PPT | No | — |
| GPU required | No | — |

## Extraction Benchmarks

**opendataloader-pdf [hybrid] ranks #1 overall (0.907)** across reading order, table, and heading extraction accuracy.

| Engine | Overall | Reading Order | Table | Heading | Speed (s/page) | License |
|--------|---------|---------------|-------|---------|----------------|---------|
| **opendataloader [hybrid]** | **0.907** | **0.934** | **0.928** | 0.821 | 0.463 | Apache-2.0 |
| nutrient | 0.885 | 0.925 | 0.708 | 0.819 | **0.008** | Commercial |
| docling | 0.882 | 0.898 | 0.887 | **0.824** | 0.762 | MIT |
| marker | 0.861 | 0.890 | 0.808 | 0.796 | 53.932 | GPL-3.0 |
| unstructured [hi_res] | 0.841 | 0.904 | 0.588 | 0.749 | 3.008 | Apache-2.0 |
| edgeparse | 0.837 | 0.894 | 0.717 | 0.706 | 0.036 | Apache-2.0 |
| opendataloader | 0.831 | 0.902 | 0.489 | 0.739 | 0.015 | Apache-2.0 |
| mineru | 0.831 | 0.857 | 0.873 | 0.743 | 5.962 | AGPL-3.0 |
| pymupdf4llm | 0.732 | 0.885 | 0.401 | 0.412 | 0.091 | AGPL-3.0 |
| unstructured | 0.686 | 0.882 | 0.000 | 0.388 | 0.077 | Apache-2.0 |
| markitdown | 0.589 | 0.844 | 0.273 | 0.000 | 0.114 | MIT |
| liteparse | 0.576 | 0.866 | 0.000 | 0.000 | 1.061 | Apache-2.0 |

> Scores normalized to [0, 1]. Higher is better for accuracy; lower is better for speed. **Bold** = best. [Full benchmark details](https://github.com/opendataloader-project/opendataloader-bench)

[![Benchmark](https://github.com/opendataloader-project/opendataloader-bench/raw/refs/heads/main/charts/benchmark.png)](https://github.com/opendataloader-project/opendataloader-bench)

[![Quality Breakdown](https://github.com/opendataloader-project/opendataloader-bench/raw/refs/heads/main/charts/benchmark_quality.png)](https://github.com/opendataloader-project/opendataloader-bench)

## Which Mode Should I Use?

| Your Document | Mode | Install | Server Command | Client Command |
|---------------|------|---------|----------------|----------------|
| Standard digital PDF | Fast (default) | `pip install opendataloader-pdf` | None needed | `opendataloader-pdf file1.pdf file2.pdf folder/` |
| Complex or nested tables | **Hybrid** | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --port 5002` | `opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf folder/` |
| Scanned / image-based PDF | Hybrid + OCR | `pip install "opendataloader-pdf[hybrid]"` | `opendataloader-pdf-hybrid --port 5002 --force-ocr` | `opendataloader-pdf --hybrid docling-fast file1.pdf file2.pdf f

# FILE: docs/hybrid/hybrid-mode-tasks.md

# Hybrid Mode Implementation Tasks

Each task is independently executable. A new Claude Code session can reference this document to perform the task.

---

## Decision Points (Runtime-Dependent)

These decisions **require execution results** before they can be made.

### After Phase -1 (based on docling API test results)

| Decision | How to Verify | Impact |
|----------|---------------|--------|
| **API endpoint** | Check available endpoints in OpenAPI spec | Task 6 client implementation |
| **Page filtering support** | Check if API options include page filter | Full PDF send required if unsupported |
| **Response page structure** | Analyze sample response JSON structure | Task 7 per-page separation logic |
| **Coordinate system** | Check bbox value ranges in sample response | Task 7 coordinate conversion formula |
| **docling element types** | Extract actual type values from sample response | Task 1 mapping table |

### After Phase 2 (based on benchmark results)

| Decision | How to Verify | Impact |
|----------|---------------|--------|
| **Triage threshold tuning** | Check triage_fn (missed tables) count | Lower thresholds if recall < 95% |

### After Phase 4 (based on evaluation results)

| Decision | How to Verify | Impact |
|----------|---------------|--------|
| **Triage re-tuning needed** | Analyze FN case signal patterns | Phase 2 rework |

---

## Progress Tracker

| Task | Status | Completed | Notes |
|------|--------|-----------|-------|
| Task -1: Pre-research | ✅ completed | 2026-01-02 | See docs/hybrid/research/ |
| Task 0: docling-api skill | ✅ completed | 2026-01-02 | See .claude/skills/docling-api/ |
| Task 1: schema-mapping skill | ✅ completed | 2026-01-02 | See .claude/skills/schema-mapping/ |
| Task 2: triage-criteria skill | ✅ completed | 2026-01-02 | See .claude/skills/triage-criteria/ |
| Task 3: HybridConfig | ✅ completed | 2026-01-02 | See java/.../hybrid/HybridConfig.java |
| Task 4: CLI Options | ✅ completed | 2026-01-02 | See java/.../cli/CLIOptions.java |
| Task 5: TriageProcessor | ✅ completed | 2026-01-02 | See java/.../hybrid/TriageProcessor.java |
| Task 6: DoclingClient | ✅ completed | 2026-01-02 | See java/.../hybrid/DoclingClient.java |
| Task 7: SchemaTransformer | ✅ completed | 2026-01-02 | See java/.../hybrid/DoclingSchemaTransformer.java |
| Task 8: HybridDocumentProcessor | ✅ completed | 2026-01-02 | See java/.../processors/HybridDocumentProcessor.java |
| Task 9: Triage Logging | ✅ completed | 2026-01-02 | See java/.../hybrid/TriageLogger.java |
| Task 10: Triage Evaluator | ✅ completed | 2026-01-02 | See tests/benchmark/src/evaluator_triage.py |
| Task 11: Triage Analyzer Agent | ✅ completed | 2026-01-02 | See .claude/agents/triage-analyzer.md |

**Status Legend:**
- ⬜ `not_started` - Not yet begun
- 🔄 `in_progress` - Currently working
- ✅ `completed` - Done and verified
- ⏸️ `blocked` - Waiting on dependency or issue

---

## Task -1: Pre-research & Data Collection

### Goal
Collect all required data and specifications before implementation begins.

### Prerequisites
- Docker installed
- Access to test PDFs in `tests/benchmark/pdfs/`

### Research Steps

#### 1. Start docling-serve and collect OpenAPI spec
```bash
# Start docling-serve (official container image)
# Reference: https://github.com/docling-project/docling-serve
docker run -d -p 5001:5001 --name docling-serve \
  -e DOCLING_SERVE_ENABLE_UI=1 \
  quay.io/docling-project/docling-serve

# Wait for startup (model loading takes time)
sleep 30

# Verify server is running (check API docs page)
curl -s http://localhost:5001/docs | head -20

# Access UI playground at: http://localhost:5001/ui

# Collect OpenAPI specification
curl http://localhost:5001/openapi.json > docs/hybrid/research/docling-openapi.json

# Check available endpoints
cat docs/hybrid/research/docling-openapi.json | jq '.paths | keys'

# Alternative: Using pip (if Docker not available)
# pip install "docling-serve[ui]"
# docling-serve run --enable-ui
```

#### 2. Test API and collect sample response
```bash
# Convert using /v1/convert/source endpoint (official API)
# Using file URL source
curl -X POST http://localhost:5001/v1/convert/source \
  -H "Content-Type: application/json" \
  -d '{
    "sources": [{"kind": "file", "path": "samples/pdf/1901.03003.pdf"}],
    "options": {"to_formats": ["json", "md"], "do_table_structure": true}
  }' \
  > docs/hybrid/research/docling-sample-response.json

# If file path doesn't work, try with base64 or HTTP URL
# Alternative: Use multipart form if available
curl -X POST http://localhost:5001/v1/convert/source \
  -F "file=@samples/pdf/1901.03003.pdf" \
  > docs/hybrid/research/docling-sample-response.json

# Extract response structure
cat docs/hybrid/research/docling-sample-response.json | jq 'keys'
cat docs/hybrid/research/docling-sample-response.json | jq '.document | keys' 2>/dev/null || \
  cat docs/hybrid/research/docling-sample-response.json | jq '.[0] | keys'

# Check element types in response
cat docs/hybrid/research/docling-sample-response.json | jq '[.. | .type? // empty] | unique' 2>/dev/null
```

#### 3. Extract documents with tables (for triage evaluation)
```bash
# List documents containing tables
cat tests/benchmark/ground-truth/reference.json | \
  jq -r 'to_entries[] | select(.value[]?.category == "Table") | .key' | \
  sort | uniq > docs/hybrid/research/documents-with-tables.txt

# Count
wc -l docs/hybrid/research/documents-with-tables.txt
```

#### 4. Parse same PDF with OpenDataLoader Java
```bash
# Build Java CLI
./scripts/build-java.sh

# Parse the same PDF with Java (JSON output)
java -jar java/opendataloader-pdf-cli/target/opendataloader-pdf-cli-*.jar \
  --format json \
  -o docs/hybrid/research/ \
  samples/pdf/1901.03003.pdf

# Rename for clarity
mv docs/hybrid/research/1901.03003.json docs/hybrid/research/opendataloader-sample-response.json

# Also generate markdown for comparison
java -jar java/opendataloader-pdf-cli/target/opendataloader-pdf-cli-*.jar \
 

# FILE: docs/hybrid/docling-speed-optimization-plan.md

# Docling Speed Optimization Plan

## Progress Tracker

| Task | Status | Completed | Result |
|------|--------|-----------|--------|
| Phase 0: Baseline measurement | ✅ completed | 2026-01-03 | 2.283s/doc |
| Phase 0: FastAPI experiment | ✅ completed | 2026-01-03 | 0.685s/doc (PASS < 0.8s) |
| Phase 0: subprocess experiment | ✅ completed | 2026-01-03 | 0.661s/doc (PASS < 1.0s) |
| Phase 0: Results comparison | ✅ completed | 2026-01-03 | 3.3x-3.5x speedup |
| Task 1.1: docling_subprocess_worker.py | ⏭️ skipped | - | FastAPI only |
| Task 1.2: hybrid_server.py | ✅ completed | 2026-01-03 | opendataloader-pdf-hybrid |
| Task 2.1: DoclingSubprocessClient.java | ⏭️ skipped | - | FastAPI only |
| Task 2.2: DoclingFastServerClient.java | ✅ completed | 2026-01-03 | - |
| Task 2.3: HybridClientFactory modification | ✅ completed | 2026-01-03 | docling-fast only |
| Task 3.1: pdf_parser modules | ✅ completed | 2026-01-03 | docling-fast only |
| Task 3.2: engine_registry.py | ✅ completed | 2026-01-03 | - |
| Task 3.3: run.py CLI options | ✅ completed | 2026-01-03 | - |
| Task 4.1: Full benchmark | ✅ completed | 2026-01-03 | See experiments/speed/ |
| Task 4.2: Results documentation | ✅ completed | 2026-01-03 | speed-experiment-2026-01-03.md |

**Status Legend:**
- ⬜ `not_started` - Not yet begun
- 🔄 `in_progress` - Currently working
- ✅ `completed` - Done and verified
- ⏭️ `skipped` - Excluded from plan
- ⏸️ `blocked` - Waiting on dependency
- ❌ `failed` - Did not meet criteria
- 🚫 `discarded` - Plan abandoned

---

## 1. Background

### Current Problem
- **DoclingClient** (docling-serve HTTP API): ~2 seconds per page
- **docling SDK direct call**: ~0.5 seconds per document (user-reported)
- HTTP overhead negates the speed benefits of hybrid mode

### Goal
Implement alternative approaches to efficiently call the docling SDK, then compare benchmark speeds

---

## 2. Experiment Phase (Phase 0)

### Purpose
Validate the speed improvement hypothesis before full implementation

### Experiment Targets
| Approach | Description |
|----------|-------------|
| baseline | Current docling-serve (reference) |
| fastapi | Optimized FastAPI server |
| subprocess | Direct Python subprocess call |

### Success Criteria
| Approach | Threshold | Condition |
|----------|-----------|-----------|
| fastapi | **< 0.8 sec/doc** (average) | Based on 200 documents |
| subprocess | **< 1.0 sec/doc** (average) | Based on 200 documents |

### Failure Conditions
- If fastapi approach exceeds 0.8 sec/doc: **Discard entire plan**
- If only subprocess fails: Exclude that approach only

### Experiment Environment
- Benchmark PDFs: `tests/benchmark/pdfs/` (200 files)
- Settings: `do_ocr=true`, `do_table_structure=true`
- Measurement: `total_time / document_count`

### Experiment Scripts
```
scripts/experiments/
├── docling_baseline_bench.py     # docling-serve speed measurement
├── docling_fastapi_bench.py      # FastAPI server + client test
├── docling_subprocess_bench.py   # subprocess approach test
└── docling_speed_report.py       # Results comparison report
```

### Experiment Execution
```bash
# 1. baseline (requires docling-serve running)
python scripts/experiments/docling_baseline_bench.py

# 2. fastapi (server auto-starts)
python scripts/experiments/docling_fastapi_bench.py

# 3. subprocess
python scripts/experiments/docling_subprocess_bench.py

# 4. compare results
python scripts/experiments/docling_speed_report.py
```

### Results Recording
```
docs/hybrid/experiments/
└── speed-experiment-YYYY-MM-DD.md
```

---

## 3. Implementation Tasks (After Phase 0 Success)

### Task 1: Python Scripts

#### Task 1.1: docling_subprocess_worker.py
| Item | Details |
|------|---------|
| File | `scripts/docling_subprocess_worker.py` |
| Prerequisites | docling package installed |
| Description | stdin JSON → stdout JSON conversion |
| Success Criteria | Single PDF conversion succeeds, JSON output parseable |
| Test | `echo '{"pdf_path":"/path/to.pdf"}' \| python scripts/docling_subprocess_worker.py` |

#### Task 1.2: hybrid_server.py
| Item | Details |
|------|---------|
| File | `python/opendataloader-pdf/src/opendataloader_pdf/hybrid_server.py` |
| Prerequisites | `pip install opendataloader-pdf[hybrid]` |
| Description | POST /convert endpoint, DocumentConverter singleton |
| Success Criteria | curl PDF upload returns JSON response |
| Test | `opendataloader-pdf-hybrid &` then `curl -F "file=@test.pdf" http://localhost:5002/v1/convert/file` |

### Task 2: Java Client Implementation

#### Task 2.1: DoclingSubprocessClient.java
| Item | Details |
|------|---------|
| File | `java/.../hybrid/DoclingSubprocessClient.java` |
| Prerequisites | Task 1.1 complete |
| Description | ProcessBuilder executes Python, stdin/stdout JSON |
| Success Criteria | Implements HybridClient interface, single PDF conversion succeeds |
| Test | `DoclingSubprocessClientTest.java` unit tests pass |

#### Task 2.2: DoclingFastServerClient.java
| Item | Details |
|------|---------|
| File | `java/.../hybrid/DoclingFastServerClient.java` |
| Prerequisites | Task 1.2 complete |
| Description | OkHttp calls FastAPI server |
| Success Criteria | Implements HybridClient interface, single PDF conversion succeeds |
| Test | `DoclingFastServerClientTest.java` unit tests pass |

#### Task 2.3: HybridClientFactory Modification
| Item | Details |
|------|---------|
| File | `java/.../hybrid/HybridClientFactory.java` |
| Prerequisites | Task 2.1, 2.2 complete |
| Description | Register `docling-subprocess`, `docling-fast` backends |
| Success Criteria | `HybridClientFactory.getOrCreate("docling-fast", config)` works |
| Test | Extend `HybridClientFactoryTest.java` |

### Task 3: Benchmark Integration

#### Task 3.1: Add pdf_parser Modules
| Item | Details |
|------|---------|
| Files | `tests/benchmark/src/pdf_parser_opendataloader_hybrid_subprocess.py` |
|       | `tests/benchmark/src/pdf_parser_opendataloader_hybrid_fast.py` |
| Prerequisites | Task 2.3 complete, JAR bui

# FILE: docs/hybrid/hybrid-mode-design.md

# Hybrid PDF Processing System - Design Document

## Overview

Hybrid PDF processing system combining Java heuristics + external AI backends.
Routes pages via per-page Triage: simple pages to fast Java path, complex tables/OCR to AI backend.

## Key Decisions

| Item | Decision |
|------|----------|
| CLI Option | `--hybrid <off\|docling\|hancom\|...>` |
| Default | `off` (Java-only, no external dependency) |
| First Backend | `docling` (docling-serve REST API) |
| Automation | Semi-automatic (benchmark/analysis auto, code changes require approval) |
| Triage Strategy | Conservative (minimize FN, accept FP, route uncertain pages to backend) |

---

## CLI Usage

```bash
# Default: Java-only processing
opendataloader-pdf input.pdf
opendataloader-pdf --hybrid off input.pdf

# Use docling backend
opendataloader-pdf --hybrid docling input.pdf

# With custom backend URL
opendataloader-pdf --hybrid docling --hybrid-url http://localhost:5001 input.pdf

# Future backends
opendataloader-pdf --hybrid hancom input.pdf
```

## Hybrid Options

| Option | Description |
|--------|-------------|
| `--hybrid <name>` | Hybrid backend: `off` (default), `docling`, `hancom`, etc. |
| `--hybrid-url <url>` | Backend server URL (overrides default) |
| `--hybrid-timeout <ms>` | Request timeout in milliseconds (default: 0, no timeout) |
| `--hybrid-fallback` | Fallback to Java on backend error (default: true) |

## Supported Backends

| Backend | Status | Description |
|---------|--------|-------------|
| `off` | ✅ Default | Java-only, no external calls |
| `docling-fast` | ✅ Available | docling-serve (local) |
| `hancom` | 📋 Future (Priority) | Hancom Document AI |
| `azure` | 📋 Future | Azure Document Intelligence |
| `google` | 📋 Future | Google Document AI |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        PDF Input                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                   ContentFilterProcessor                         │
│                   (existing: text filtering)                     │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  TriageProcessor.triageAllPages()                │
│   - Batch triage all pages                                       │
│   - Output: Map<PageNumber, TriageResult>                        │
└─────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              │                               │
              ▼                               ▼
┌─────────────────────────┐     ┌─────────────────────────┐
│      JAVA Path          │     │     BACKEND Path        │
│  (parallel processing)  │     │  (single batch API call)│
│                         │     │                         │
│  ExecutorService        │     │  BackendClient          │
│  - TableBorderProcessor │     │  - Send all pages once  │
│  - TextLineProcessor    │     │  - Receive all results  │
│  - ParagraphProcessor   │     │  SchemaTransformer      │
└─────────────────────────┘     └─────────────────────────┘
              │                               │
              │         CONCURRENT            │
              └───────────────┬───────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Result Merger                                 │
│                  (preserve page order)                           │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              Post-processing & Output Generation                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Backend unavailable | `--hybrid-fallback` (default: true) |
| Triage FN (missed tables) | Conservative threshold, benchmark monitoring |
| Schema mismatch | Step-by-step validation, type checking |
| Slow processing | Parallel execution, batch API calls |

---

## Related Documents

- **Implementation Tasks**: [hybrid-mode-tasks.md](hybrid-mode-tasks.md)


# FILE: docs/superpowers/plans/2026-04-18-hancom-ai-mock-server.md

# Hancom AI Mock Server Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Hancom AI 서버 부재 시 transformer 개발/디버그 사이클을 유지하기 위한 fixture-replay HTTP mock 서버 구현 + 클라이언트(`HancomAIClient.java`) REQUEST_ID 규약 패치.

**Architecture:** Python(FastAPI) 로컬 서버가 200개 벤치 PDF의 SHA256을 인덱싱하고, PDF 입력은 SHA256 룩업, 이미지 입력은 클라이언트가 REQUEST_ID에 인코딩한 `(sha_short, page, obj, module)`로 룩업, pdf2img는 PyMuPDF로 동적 300DPI 렌더링 + base64 응답. 클라이언트는 `convert()` 진입 시 PDF SHA256을 캐시하고 모든 호출에 REQUEST_ID 규약 적용.

**Tech Stack:**
- Mock 서버: Python 3.10+, FastAPI, uvicorn, PyMuPDF, pytest, httpx (TestClient)
- Client 패치: Java 8+, OkHttp, Jackson, Maven, JUnit 5
- 데이터: `bundolee/kb-odl/raw/4-기술/2026-04-16_Q2-기술-ctx_hancom-ai-a11y_출력데이터-스키마/`
- PDFs: `opendataloader-project/opendataloader-bench/pdfs/`

**Spec:** `bundolee/kb-odl/raw/4-기술/2026-04-18_Q2-DEV-02-Code_hancom-ai-mock-server-design.md` (commit `dfe0671`)

---

## File Structure

### Mock 서버 (신규)

`opendataloader-project/opendataloader-pdfua/scripts/mock_server/`

| 파일 | 책임 |
|---|---|
| `mock_server/__init__.py` | 빈 패키지 마커 |
| `mock_server/__main__.py` | CLI 엔트리포인트 (`python -m mock_server ...`) |
| `mock_server/index.py` | 부팅 시 `--pdf-dir` 스캔 → `{sha256: (basename, path)}` 인덱스 |
| `mock_server/request_id.py` | REQUEST_ID 정규식 파싱 (`odl-{sha12}-p{n}-o{n}-{module}`) |
| `mock_server/lookup.py` | 모듈명/입력타입에 따른 fixture 경로 결정 + JSON 로드. `FixtureMiss` 예외. |
| `mock_server/pdf_render.py` | PyMuPDF로 PDF 페이지 → PNG 300DPI bytes |
| `mock_server/server.py` | FastAPI app: `/ping`, `/hocr/sdk`, `/support/pdf2img` (각각 `/api/v1/` 변형 별칭) |
| `mock_server/tests/__init__.py` | |
| `mock_server/tests/conftest.py` | 테스트 fixture (샘플 PDF dir, 샘플 fixture dir) |
| `mock_server/tests/test_index.py` | |
| `mock_server/tests/test_request_id.py` | |
| `mock_server/tests/test_lookup.py` | |
| `mock_server/tests/test_pdf_render.py` | |
| `mock_server/tests/test_server.py` | |
| `mock_server/pyproject.toml` | 의존성 + pytest 설정 |
| `mock_server/README.md` | 실행법 + 디버깅 + client 패치 메모 |

### Client 패치 (수정)

`opendataloader-project/opendataloader-pdf/java/opendataloader-pdf-core/src/main/java/org/opendataloader/pdf/hybrid/HancomAIClient.java`

`opendataloader-project/opendataloader-pdf/java/opendataloader-pdf-core/src/test/java/org/opendataloader/pdf/hybrid/HancomAIClientRequestIdTest.java` (신규)

---

## Phase 1 — Mock Server (10 tasks)

### Task 1: 프로젝트 스캐폴딩

**Files:**
- Create: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/pyproject.toml`
- Create: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/__init__.py`
- Create: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/tests/__init__.py`
- Create: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/README.md`

- [ ] **Step 1: pyproject.toml 작성**

```toml
[project]
name = "hancom-ai-mock-server"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "fastapi>=0.110",
    "uvicorn>=0.27",
    "pymupdf>=1.24",
    "python-multipart>=0.0.9",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "httpx>=0.27",
]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 2: 빈 패키지 마커 + README 초안**

`mock_server/__init__.py`:
```python
"""Hancom AI HOCR SDK fixture-replay mock server."""
```

`mock_server/tests/__init__.py`:
```python
```

`mock_server/README.md`:
```markdown
# Hancom AI Mock Server

Fixture-replay mock for `HancomAIClient`. See spec at
`bundolee/kb-odl/raw/4-기술/2026-04-18_Q2-DEV-02-Code_hancom-ai-mock-server-design.md`.

## Run

```bash
cd opendataloader-pdfua/scripts/mock_server
pip install -e ".[dev]"
python -m mock_server \
  --pdf-dir /path/to/opendataloader-bench/pdfs \
  --fixture-dir /path/to/kb-odl/raw/4-기술/2026-04-16_Q2-기술-ctx_hancom-ai-a11y_출력데이터-스키마 \
  --port 18008
```

## Tests

```bash
pytest -v
```
```

- [ ] **Step 3: 디렉토리 구조 확인**

Run: `ls opendataloader-project/opendataloader-pdfua/scripts/mock_server/`
Expected: `pyproject.toml  README.md  __init__.py  tests/`

- [ ] **Step 4: Commit**

```bash
cd opendataloader-project/opendataloader-pdfua
git add scripts/mock_server/
git commit -m "feat(mock-server): scaffold project structure"
```

---

### Task 2: REQUEST_ID 파서 (TDD)

**Files:**
- Test: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/tests/test_request_id.py`
- Create: `opendataloader-project/opendataloader-pdfua/scripts/mock_server/mock_server/request_id.py`

- [ ] **Step 1: 실패하는 테스트 작성**

`tests/test_request_id.py`:
```python
import pytest
from mock_server.request_id import parse_request_id, RequestIdParts


def test_parse_caption():
    parts = parse_request_id("odl-a3f1c9d2e7b8-p0-o5-caption")
    assert parts == RequestIdParts(sha_short="a3f1c9d2e7b8", page=0, obj=5, module="caption")


def test_parse_chart():
    parts = parse_request_id("odl-deadbeef0000-p3-o12-chart")
    assert parts == RequestIdParts(sha_short="deadbeef0000", page=3, obj=12, module="chart")


def test_parse_tsr():
    parts = parse_request_id("odl-aabbccddeeff-p0-o0-tsr")
    assert parts.module == "tsr"


def test_parse_invalid_returns_none():
    assert parse_request_id("odl-DOCUMENT_LAYOUT_WITH_OCR") is None
    assert parse_request_id("garbage") is None
    assert parse_request_id("") is None
    assert parse_request_id("odl-a3f1-p0-o0-unknown") is None  # bad module


def test_parse_pdf_module_request_id_returns_none():
    # PDF modules use REQUEST_ID for tracing only; mock matches via SHA256 of bytes.
    # Parser returns None for these so caller falls back to PDF lookup path.
    assert parse_request_id("odl-a3f1c9d2e7b8-dla-ocr") is None
```

- [ ] **Step 2: 테스트 실행 (실패 확인)**

Run: `cd opendataloader-project/opendataloader-pdfua/scripts/mock_server && pytest tests/test_request_id.py -v`
Expected: FAIL — `ModuleNotFoundError: No module n

# FILE: docs/superpowers/plans/2026-04-29-hybrid-hancom-ai-options.md

# Hybrid hancom-ai Options & CLI Refactoring Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Expose 5 hancom-ai-specific knobs as `--hybrid-hancom-ai-*` CLI options, then refactor `CLIOptions` so opendataloader-pdfua reuses the entire core option set instead of redefining its own.

**Architecture:** Three independent commits. (1) Add 5 options + gate validation in core. (2) Extract `addAllTo` / `applyAllTo` public API on `CLIOptions`. (3) Refactor pdfua's `Main.java` and `RemediationConfig` to consume that API; collapse 9 `RemediationConfig` constructors into a Builder; embed `Config` directly. Hard-break removed getters since all call sites are internal/test.

**Tech Stack:** Java 11, Apache Commons CLI, JUnit 5, Maven multi-module (`opendataloader-pdf-core`, `opendataloader-pdf-cli`, `opendataloader-pdfua`).

---

## File Structure

**opendataloader-pdf (core)**

| File | Action | Responsibility |
|---|---|---|
| `java/opendataloader-pdf-cli/src/main/java/org/opendataloader/pdf/cli/CLIOptions.java` | Modify | Add 5 option constants, 5 OPTION_DEFINITIONS entries, parsing in `applyHybridOptions`, hancom-ai gate. Add public `addAllTo(Options)` and `applyAllTo(Config, CommandLine)`. |
| `java/opendataloader-pdf-cli/src/test/java/org/opendataloader/pdf/cli/CLIOptionsTest.java` | Modify | Tests for each new option's parsing + gate enforcement. |
| `options.json` (root) | Regenerate | Auto-generated from `CLIOptions` via `npm run sync`. |
| Python/Node bindings | Regenerate | Auto-generated by `npm run sync`. |

**opendataloader-pdfua**

| File | Action | Responsibility |
|---|---|---|
| `src/main/java/org/opendataloader/pdf/Main.java` | Modify | Replace self-defined hybrid options with `CLIOptions.addAllTo()`. Add `applyPdfuaDefaults()`. Use new `RemediationConfig.Builder`. |
| `src/main/java/org/opendataloader/pdf/remediation/RemediationConfig.java` | Modify | Embed core `Config`. Replace 9 constructors with one Builder. Remove `getHybridUrl()` / `getHybridMode()` (delegate via `getHybridConfig()`). |
| `src/main/java/org/opendataloader/pdf/remediation/RemediationProcessor.java` | Modify | Replace per-field hybrid forwarding (lines 163-170) with `config = remediationConfig.getCoreConfig()`. |
| `src/test/java/.../AuditBundleEmitterTest.java` | Modify | Switch to Builder. |
| `src/test/java/.../CertificateIssuerTest.java` | Modify | Switch to Builder (4 instantiations). |
| `src/test/java/.../AuditManifestBuilderTest.java` | Modify | Switch to Builder (4 instantiations). |
| `src/test/java/.../RemediationConfigAuditBundleTest.java` | Modify | Switch to Builder. |

---

## Phase 1 — Add 5 hybrid-hancom-ai-* options to core

### Task 1.1: Add option name + description constants

**Files:**
- Modify: `opendataloader-pdf/java/opendataloader-pdf-cli/src/main/java/org/opendataloader/pdf/cli/CLIOptions.java` (insert after line 137, the existing `HYBRID_FALLBACK_DESC`)

- [ ] **Step 1: Add the 5 long-option constants and descriptions**

Insert after the `HYBRID_FALLBACK_DESC` block (currently around line 137) and before the `// ===== Stdout Output =====` section header:

```java
    // ===== Hybrid hancom-ai backend-specific =====
    private static final String HYBRID_HANCOM_AI_REGIONLIST_STRATEGY_LONG_OPTION =
            "hybrid-hancom-ai-regionlist-strategy";
    private static final String HYBRID_HANCOM_AI_REGIONLIST_STRATEGY_DESC =
            "DLA label 7 (regionlist) handling. Requires --hybrid=hancom-ai. "
            + "Values: table-first (default; check TSR overlap), list-only (skip TSR, always treat as list)";

    private static final String HYBRID_HANCOM_AI_OCR_STRATEGY_LONG_OPTION =
            "hybrid-hancom-ai-ocr-strategy";
    private static final String HYBRID_HANCOM_AI_OCR_STRATEGY_DESC =
            "OCR strategy. Requires --hybrid=hancom-ai. "
            + "Values: off (stream-only), auto (default; stream first, OCR fallback), force (OCR-only)";

    private static final String HYBRID_HANCOM_AI_IMAGE_CACHE_LONG_OPTION =
            "hybrid-hancom-ai-image-cache";
    private static final String HYBRID_HANCOM_AI_IMAGE_CACHE_DESC =
            "Page image cache backing. Requires --hybrid=hancom-ai. "
            + "Values: memory (default), disk";

    private static final String HYBRID_HANCOM_AI_SAVE_CROPS_LONG_OPTION =
            "hybrid-hancom-ai-save-crops";
    private static final String HYBRID_HANCOM_AI_SAVE_CROPS_DESC =
            "Persist cropped figure images to disk for debugging. Requires --hybrid=hancom-ai";

    private static final String HYBRID_HANCOM_AI_CROP_OUTPUT_DIR_LONG_OPTION =
            "hybrid-hancom-ai-crop-output-dir";
    private static final String HYBRID_HANCOM_AI_CROP_OUTPUT_DIR_DESC =
            "Output directory for --hybrid-hancom-ai-save-crops. Requires --hybrid=hancom-ai";
```

- [ ] **Step 2: Verify file still compiles**

Run: `cd opendataloader-pdf/java && mvn -pl opendataloader-pdf-cli compile -DskipTests -q`
Expected: BUILD SUCCESS (constants added but unused — no warning since `private static final` is fine).

- [ ] **Step 3: Commit**

```bash
cd opendataloader-pdf && git add java/opendataloader-pdf-cli/src/main/java/org/opendataloader/pdf/cli/CLIOptions.java
git commit -m "$(cat <<'EOF'
feat(cli): add --hybrid-hancom-ai-* option name constants

Defines long-name and description constants for 5 hancom-ai-specific
flags. Wiring into OPTION_DEFINITIONS and parser comes in subsequent
commits.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
```

---

### Task 1.2: Register options in OPTION_DEFINITIONS

**Files:**
- Modify: `opendataloader-pdf/java/opendataloader-pdf-cli/src/main/java/org/opendataloader/pdf/cli/CLIOptions.java` (the `OPTION_DEFINITIONS` list, currently lines 166-208)

- [ ] **Step 1: Add 

# FILE: docs/superpowers/plans/2026-03-16-cid-font-detection.md

# CID Font Extraction Failure Detection — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Detect pages where CID font extraction failed (high U+FFFD ratio), emit warning logs, and auto-route to OCR backend in hybrid mode.

**Architecture:** Measure replacement character ratio in ContentFilterProcessor before replacement, store in StaticLayoutContainers, consume in TriageProcessor as highest-priority signal. Warning log fires regardless of hybrid mode.

**Tech Stack:** Java 11+, JUnit Jupiter, veraPDF API (`ChunkParser.REPLACEMENT_CHARACTER_STRING`)

---

## File Structure

| File | Responsibility |
|---|---|
| `TextProcessor.java` | New `measureReplacementCharRatio()` method |
| `StaticLayoutContainers.java` | Per-page replacement ratio storage |
| `ContentFilterProcessor.java` | Measure + warn + store before replacement |
| `TriageProcessor.java` | Signal 0: route high-ratio pages to BACKEND |
| `TextProcessorTest.java` | Unit tests for measurement |
| `TriageProcessorTest.java` | Unit tests for Signal 0 routing |
| `CidFontDetectionTest.java` (new) | e2e test with synthetic PDF |
| `test/resources/cid-font-no-tounicode.pdf` (new) | Test fixture |
| `test/resources/generate-cid-test-pdf.py` (new) | Generation script (reference) |

All paths below are relative to `java/opendataloader-pdf-core/src/`.

---

## Chunk 1: Measurement + Storage

### Task 1: Add per-page ratio storage to StaticLayoutContainers

**Files:**
- Modify: `main/java/org/opendataloader/pdf/containers/StaticLayoutContainers.java`

- [ ] **Step 1: Add ThreadLocal map field and imports**

Add after line 40 (`imageFormat` field):

```java
private static final ThreadLocal<Map<Integer, Double>> replacementCharRatios = ThreadLocal.withInitial(HashMap::new);
```

Add to imports:

```java
import java.util.HashMap;
import java.util.Map;
```

- [ ] **Step 2: Add getter and setter**

Add after `setImageFormat()` (after line 145):

```java
public static void setReplacementCharRatio(int pageNumber, double ratio) {
    replacementCharRatios.get().put(pageNumber, ratio);
}

public static double getReplacementCharRatio(int pageNumber) {
    return replacementCharRatios.get().getOrDefault(pageNumber, 0.0);
}
```

- [ ] **Step 3: Clear in clearContainers()**

Add inside `clearContainers()` method, after line 51 (`imageFormat.set(...)`):

```java
replacementCharRatios.get().clear();
```

- [ ] **Step 4: Compile check**

Run: `cd java && mvn compile -pl opendataloader-pdf-core -q`
Expected: BUILD SUCCESS

- [ ] **Step 5: Commit**

```bash
git add java/opendataloader-pdf-core/src/main/java/org/opendataloader/pdf/containers/StaticLayoutContainers.java
git commit -m "feat: add per-page replacement char ratio storage to StaticLayoutContainers"
```

### Task 2: Add measureReplacementCharRatio to TextProcessor

**Files:**
- Modify: `main/java/org/opendataloader/pdf/processors/TextProcessor.java`
- Test: `test/java/org/opendataloader/pdf/processors/TextProcessorTest.java`

- [ ] **Step 1: Write failing tests**

Add to `TextProcessorTest.java` after the last test method (before closing `}`):

```java
@Test
public void testMeasureReplacementCharRatio_allReplacement() {
    List<IObject> contents = new ArrayList<>();
    contents.add(new TextChunk(new BoundingBox(1, 10.0, 10.0, 100.0, 20.0),
        "\uFFFD\uFFFD\uFFFD", 10, 10.0));

    double ratio = TextProcessor.measureReplacementCharRatio(contents);
    Assertions.assertEquals(1.0, ratio, 0.001);
}

@Test
public void testMeasureReplacementCharRatio_noReplacement() {
    List<IObject> contents = new ArrayList<>();
    contents.add(new TextChunk(new BoundingBox(1, 10.0, 10.0, 100.0, 20.0),
        "Hello World", 10, 10.0));

    double ratio = TextProcessor.measureReplacementCharRatio(contents);
    Assertions.assertEquals(0.0, ratio, 0.001);
}

@Test
public void testMeasureReplacementCharRatio_mixed() {
    List<IObject> contents = new ArrayList<>();
    // 3 replacement chars out of 10 total = 0.3
    contents.add(new TextChunk(new BoundingBox(1, 10.0, 10.0, 100.0, 20.0),
        "\uFFFD\uFFFD\uFFFDAbcdefg", 10, 10.0));

    double ratio = TextProcessor.measureReplacementCharRatio(contents);
    Assertions.assertEquals(0.3, ratio, 0.001);
}

@Test
public void testMeasureReplacementCharRatio_emptyContents() {
    List<IObject> contents = new ArrayList<>();

    double ratio = TextProcessor.measureReplacementCharRatio(contents);
    Assertions.assertEquals(0.0, ratio, 0.001);
}

@Test
public void testMeasureReplacementCharRatio_nonTextChunksIgnored() {
    List<IObject> contents = new ArrayList<>();
    contents.add(new ImageChunk(new BoundingBox(1, 10.0, 10.0, 100.0, 20.0)));
    contents.add(new TextChunk(new BoundingBox(1, 10.0, 30.0, 100.0, 40.0),
        "\uFFFD\uFFFD\uFFFD\uFFFD\uFFFD", 10, 10.0));

    double ratio = TextProcessor.measureReplacementCharRatio(contents);
    // Only TextChunks counted: 5/5 = 1.0
    Assertions.assertEquals(1.0, ratio, 0.001);
}
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd java && mvn test -pl opendataloader-pdf-core -Dtest=TextProcessorTest#testMeasureReplacementCharRatio_allReplacement -q`
Expected: FAIL — `measureReplacementCharRatio` method not found

- [ ] **Step 3: Implement measureReplacementCharRatio**

Add to `TextProcessor.java` after `replaceUndefinedCharacters()` method (after line 53):

```java
public static double measureReplacementCharRatio(List<IObject> contents) {
    char replacementChar = ChunkParser.REPLACEMENT_CHARACTER_STRING.charAt(0);
    int totalChars = 0;
    int replacementChars = 0;
    for (IObject object : contents) {
        if (object instanceof TextChunk) {
            String value = ((TextChunk) object).getValue();
            totalChars += value.length();
            for (int i = 0; i < value.length(); i++) {
     

# FILE: docs/superpowers/specs/2026-04-29-hybrid-hancom-ai-options-design.md

# Hybrid hancom-ai Backend Options & CLI Refactoring

Issue: not yet filed — this design precedes the issue/PRs.
Scope: opendataloader-pdf (core CLI) + opendataloader-pdfua (downstream CLI)

## Problem

Five hancom-ai backend behaviors are already wired through `HybridConfig` but not exposed on any CLI:

| HybridConfig field | Default | Effect when set |
|---|---|---|
| `regionlistStrategy` | `table-first` | How to handle DLA label 7 (regionlist) |
| `ocrStrategy` | `auto` | Stream-only / fallback / OCR-only |
| `imageCache` | `memory` | Page image cache backing |
| `saveCrops` | `false` | Persist cropped figures (debug) |
| `cropOutputDir` | `null` | Output dir for saved crops (debug) |

`HancomAISchemaTransformer` and `HancomAIClient` already read these via `HybridConfig`, but `CLIOptions.java` has no flags and `applyHybridOptions()` never sets them. They are reachable only through programmatic `Config` use.

A second, structural problem makes adding these flags painful:

- **opendataloader-pdf** defines all CLI options in `CLIOptions.OPTION_DEFINITIONS` (private, single source for `options.json`/Python/Node bindings).
- **opendataloader-pdfua** defines its own `--hybrid`, `--hybrid-url`, `--hybrid-mode` separately in `Main.java`, with different defaults, then forwards them through `RemediationConfig` (3 hybrid fields, 9 constructor overloads).

Adding 5 new flags to both CLIs the current way means duplicating definitions, expanding `RemediationConfig` to 8 hybrid fields, and creating yet more constructor overloads. The two CLIs will drift further apart.

## Solution

Two coupled changes, executed in order:

1. **Add the 5 hancom-ai-specific options** to core `CLIOptions` under a `--hybrid-hancom-ai-*` prefix, with a guard that rejects them when `--hybrid` is not `hancom-ai`.
2. **Refactor core `CLIOptions` to be reusable** so opendataloader-pdfua imports the full core option set and adds only its own pdfua-specific options on top. `RemediationConfig` embeds a core `Config` instead of carrying parallel hybrid fields.

After this, adding any future core CLI option propagates to pdfua with a rebuild — no Main.java edits.

## Design

### Option naming: `--hybrid-hancom-ai-*` (full path)

Decision rationale (recorded for future contributors):

- `--hybrid-*` alone (e.g. `--hybrid-regionlist-strategy`) was rejected because docling-fast and other backends will never support these knobs; the name would lie about scope.
- `--hancom-ai-*` alone (e.g. `--hancom-ai-regionlist-strategy`) was rejected because it breaks the existing `--hybrid-mode/url/timeout/fallback` grouping and gives users two mental models.
- `--hybrid-hancom-ai-*` mirrors the `gh pr create` / `git remote add` full-path convention: every option name encodes the context it belongs to. `--help` alphabetic sort keeps all hybrid options in one block.
- A single comma-separated `--hybrid-hancom-ai-config` mega-option was rejected: defeats Apache Commons CLI typo detection, breaks `options.json` codegen for Python/Node bindings, complicates Windows path escaping.

The five new options:

| Long option | Type | Default | Exported | Description |
|---|---|---|---|---|
| `--hybrid-hancom-ai-regionlist-strategy` | string | `table-first` | yes | DLA label 7 handling. Values: `table-first`, `list-only` |
| `--hybrid-hancom-ai-ocr-strategy` | string | `auto` | yes | OCR strategy. Values: `off`, `auto`, `force` |
| `--hybrid-hancom-ai-image-cache` | string | `memory` | yes | Page image cache. Values: `memory`, `disk` |
| `--hybrid-hancom-ai-save-crops` | boolean | `false` | **no** | Persist cropped figures (debug only) |
| `--hybrid-hancom-ai-crop-output-dir` | string | `null` | **no** | Output directory for `--hybrid-hancom-ai-save-crops` |

`exported=false` for the two debug options keeps them out of `options.json` and the auto-generated Python/Node bindings, while remaining usable on the Java CLI. Same pattern as existing legacy options at `CLIOptions.java:201-208`.

### Validation

Inside `applyHybridOptions()`, after `--hybrid` is parsed, before returning:

```java
boolean usesHancomAiOnly =
    commandLine.hasOption(HYBRID_HANCOM_AI_REGIONLIST_STRATEGY_LONG_OPTION) ||
    commandLine.hasOption(HYBRID_HANCOM_AI_OCR_STRATEGY_LONG_OPTION) ||
    commandLine.hasOption(HYBRID_HANCOM_AI_IMAGE_CACHE_LONG_OPTION) ||
    commandLine.hasOption(HYBRID_HANCOM_AI_SAVE_CROPS_LONG_OPTION) ||
    commandLine.hasOption(HYBRID_HANCOM_AI_CROP_OUTPUT_DIR_LONG_OPTION);

if (usesHancomAiOnly && !Config.HYBRID_HANCOM_AI.equals(config.getHybrid())) {
    throw new IllegalArgumentException(
        "Options --hybrid-hancom-ai-* require --hybrid=hancom-ai");
}
```

Per-value validation (e.g. `regionlistStrategy` must be `table-first`/`list-only`) is already implemented in `HybridConfig` setters and re-thrown as `IllegalArgumentException`. CLI passes the raw value through; HybridConfig is the validation authority.

### Core CLIOptions refactoring

Goal: pdfua can register every core option in its own `Options` and ask core to apply them to a `Config`.

Two new public static methods on `CLIOptions`:

```java
/** Register every core option onto an external Options. Used by downstream CLIs (pdfua). */
public static void addAllTo(Options options) {
    for (OptionDefinition def : OPTION_DEFINITIONS) {
        options.addOption(def.toOption());
    }
}

/** Apply parsed core options to a Config. Used by downstream CLIs after parse. */
public static void applyAllTo(Config config, CommandLine commandLine) {
    // body identical to current createConfigFromCommandLine,
    // minus `new Config()` and minus the positional-arg output-folder fallback
}
```

The existing `defineOptions()` and `createConfigFromCommandLine()` keep their signatures and behavior; internally they delegate to the two new methods. Backward compatibility for any existing callers is preserved.

`OPTION_DEFINITIONS` stays private. `OptionDefinition` stays private. We expose only the two operations dow

# FILE: docs/superpowers/specs/2026-03-16-cid-font-detection-design.md

# CID Font Extraction Failure Detection

Issue: [#286](https://github.com/opendataloader-project/opendataloader-pdf/issues/286)

## Problem

PDFs with CID-keyed fonts that lack ToUnicode mappings produce no usable text from veraPDF extraction. veraPDF replaces unmappable characters with U+FFFD (replacement character), which `TextProcessor.replaceUndefinedCharacters()` then converts to spaces. The result is empty or whitespace-only output with no indication to the user of what went wrong.

Users currently resort to external tools (e.g., pdfplumber) to pre-screen PDFs for CID issues before passing them to opendataloader-pdf.

## Solution

Detect pages with high replacement character ratios and:

1. **Always**: emit a WARNING log explaining the problem and suggesting `--hybrid-mode`
2. **When hybrid mode is on**: automatically route affected pages to OCR backend via TriageProcessor

No new CLI options. Hybrid mode setting is respected as-is.

## Design

### Detection: Replacement Character Ratio

`TextProcessor.measureReplacementCharRatio(List<IObject>)` counts `\uFFFD` characters across all TextChunks on a page and returns the ratio (0.0–1.0).

**Threshold**: 30%. CID-affected pages typically show 90%+ replacement characters. 30% catches real problems while avoiding false positives from PDFs with occasional unmappable glyphs.

**Measurement point**: Inside `ContentFilterProcessor.getFilteredContents()`, immediately before `replaceUndefinedCharacters()` is called (line 74). At this point veraPDF has already inserted `\uFFFD` but the characters haven't been replaced with spaces yet, so measurement is accurate.

**Safety of measurement point**: The prior processing steps (`mergeCloseTextChunks`, `trimTextChunksWhiteSpaces`, `filterConsecutiveSpaces`, `splitTextChunksByWhiteSpaces`) do not affect U+FFFD characters. U+FFFD is not whitespace, so it is not trimmed, compressed, or used as a split boundary. The count is accurate at this position.

**Zero-text pages**: When a page has no TextChunk objects (e.g., image-only pages), the method returns 0.0 to avoid division by zero. This correctly avoids triggering the CID warning on non-text pages.

The method uses `ChunkParser.REPLACEMENT_CHARACTER_STRING` constant (not a hardcoded `"\uFFFD"` literal) to stay consistent with `replaceUndefinedCharacters()`.

### Data Flow

The measured ratio is stored in `StaticLayoutContainers` per page:

```
ContentFilterProcessor.getFilteredContents()
  │
  ├─ TextProcessor.measureReplacementCharRatio() → ratio
  ├─ StaticLayoutContainers.setReplacementCharRatio(pageNumber, ratio)
  ├─ if ratio >= 0.3: LOGGER.warning(...)
  └─ TextProcessor.replaceUndefinedCharacters()  // existing call
```

Note: `StaticLayoutContainers` currently stores global `ThreadLocal` scalars and lists, not per-page maps. Per-page data (e.g., bounding boxes) lives in `DocumentProcessor`. This change introduces a new per-page `Map<Integer, Double>` pattern to `StaticLayoutContainers`. We place it here rather than `DocumentProcessor` because it is layout-metadata consumed by `TriageProcessor`, keeping the triage data path self-contained. The existing `clearContainers()` method **must** be updated to clear this map to prevent cross-document data leakage in multi-document processing.

### Warning Log

Emitted from `ContentFilterProcessor` when ratio >= 0.3:

```
WARNING: Page 3: 94% of characters are replacement characters (U+FFFD).
This PDF likely contains CID-keyed fonts without ToUnicode mappings.
Text extraction may be incomplete. Consider using --hybrid-mode for OCR fallback.
```

This fires regardless of hybrid mode setting.

### Triage Routing

In `TriageProcessor.classifyPage()`, a new **Signal 0** is inserted before all existing signals (before TableBorder check). This signal only fires when hybrid mode is active, since `classifyPage()` is only called from `HybridDocumentProcessor`. In non-hybrid mode, only the warning log (from `ContentFilterProcessor`) is emitted:

```java
double replacementRatio = StaticLayoutContainers.getReplacementCharRatio(pageNumber);
if (replacementRatio >= 0.3) {
    return TriageResult.backend(pageNumber, 1.0, signals);
}
```

Priority is highest (confidence 1.0) because a page with mostly broken text extraction gains nothing from Java-path processing.

### Behavior Matrix

| Hybrid Mode | Ratio >= 30% | Result |
|---|---|---|
| OFF | Yes | Warning log. Java path produces incomplete text. |
| OFF | No | No change. Normal processing. |
| ON (auto) | Yes | Warning log + auto-route to BACKEND (OCR). |
| ON (auto) | No | No change. Normal triage. |
| ON (full) | Yes | Warning log. All pages already go to BACKEND. |
| ON (full) | No | No change. All pages already go to BACKEND. |

## Changes

### Modified Files

| File | Change |
|---|---|
| `TextProcessor.java` | Add `measureReplacementCharRatio()` static method |
| `ContentFilterProcessor.java` | Call measurement before `replaceUndefinedCharacters()`, store result, emit warning |
| `StaticLayoutContainers.java` | Add `replacementCharRatios` map with getter/setter, clear in `clearContainers()` |
| `TriageProcessor.java` | Add Signal 0: replacement ratio check before TableBorder signal |

### New Files

| File | Purpose |
|---|---|
| `java/opendataloader-pdf-core/src/test/java/org/opendataloader/pdf/processors/CidFontDetectionTest.java` | e2e test using synthetic CID PDF |
| `java/opendataloader-pdf-core/src/test/resources/cid-font-no-tounicode.pdf` | Pre-generated test fixture (CID font, no ToUnicode) |
| `java/opendataloader-pdf-core/src/test/resources/generate-cid-test-pdf.py` | Generation script for reference |

### Modified Test Files

| File | Change |
|---|---|
| `TextProcessorTest.java` | 5 unit tests for `measureReplacementCharRatio()` |
| `TriageProcessorTest.java` | 3 unit tests for Signal 0 routing |

## Test Plan

### Unit Tests (TextProcessorTest)

- `testMeasureReplacementCharRatio_allReplacement` — all U+FFFD → 1.0
- `testMeasureReplacementCharRat

# FILE: docs/hybrid/research/comparison-summary.md

# Docling vs OpenDataLoader Output Comparison

## Test Document
- File: `01030000000045.pdf` (1 page with table)

## Element Count Comparison

| Category | Docling | OpenDataLoader |
|----------|---------|----------------|
| Tables | 1 | 1 |
| Text elements | 5 | 4 paragraphs |
| Images | 0 | 1 |
| Headings | (N/A - uses labels) | 1 |

## Text Element Labels (Docling)

| Label | Count |
|-------|-------|
| caption | 1 |
| footnote | 1 |
| page_footer | 1 |
| page_header | 1 |
| text | 1 |

## Table Structure Comparison

| Property | Docling | OpenDataLoader |
|----------|---------|----------------|
| Rows | 9 | 3 |
| Columns | 3 | 3 |
| Total cells | 26 | 9 |

**Note**: Docling detects more rows in the table structure. This may be due to:
- Different table detection algorithms
- OpenDataLoader may have merged some rows
- Different handling of header rows

## Bounding Box Comparison (Table)

| System | l/left | t/top | r/right | b/bottom | Origin |
|--------|--------|-------|---------|----------|--------|
| Docling | 53.22 | 439.98 | 373.94 | 234.74 | BOTTOMLEFT |
| OpenDataLoader | 54.0 | 234.44 | 372.73 | 440.21 | BOTTOMLEFT |

**Coordinate mapping**: Both use BOTTOMLEFT origin.
- Docling: `{l, t, r, b}` where t=top, b=bottom
- OpenDataLoader: `[left, bottom, right, top]`

So the actual coordinates match closely:
- Left: 53.22 ≈ 54.0
- Bottom: 234.74 ≈ 234.44
- Right: 373.94 ≈ 372.73
- Top: 439.98 ≈ 440.21

## Schema Mapping Summary

| Docling Type | OpenDataLoader Type |
|--------------|---------------------|
| texts (label: text) | paragraph |
| texts (label: section_header) | heading |
| tables | table |
| pictures | image |
| texts (label: page_header) | paragraph (filtered as header) |
| texts (label: page_footer) | paragraph (filtered as footer) |
| texts (label: caption) | paragraph |
| texts (label: footnote) | paragraph |

## Key Differences

1. **Type naming**: Docling uses `label` field for text types, OpenDataLoader uses `type`
2. **Table structure**: Docling detects more detailed row structure
3. **Coordinate format**: Same origin but different field order
4. **Heading detection**: Docling uses `SectionHeaderItem` with `level`, OpenDataLoader uses `heading` type with `level`


# FILE: docs/hybrid/research/iobject-structure.md

# IObject Class Structure

## Overview
IObject is imported from `org.verapdf.wcag.algorithms.entities.IObject` (external verapdf-wcag-algs library).

## JSON Output Types

Based on sample response analysis, OpenDataLoader produces the following element types:

### Element Types

| Type | JSON `type` field | Description |
|------|-------------------|-------------|
| Paragraph | `paragraph` | Text paragraph with font info |
| Heading | `heading` | Section heading with level |
| Table | `table` | Table with rows and cells |
| Image | `image` | Image/figure element |
| List | `list` | Bulleted or numbered list |

### Common Fields (all types)

```json
{
  "type": "paragraph",
  "id": 17,
  "page number": 1,
  "bounding box": [left, bottom, right, top]  // PDF points, origin at bottom-left
}
```

### Paragraph Fields

```json
{
  "type": "paragraph",
  "font": "ArialMT",
  "font size": 8.0,
  "text color": "[0.0, 0.0, 0.0, 0.7]",
  "content": "Text content here"
}
```

### Heading Fields

```json
{
  "type": "heading",
  "level": "1",
  "content": "Heading text"
}
```

### Table Structure

```json
{
  "type": "table",
  "level": "1",
  "number of rows": 3,
  "number of columns": 3,
  "rows": [
    {
      "type": "table row",
      "row number": 1,
      "cells": [
        {
          "type": "table cell",
          "page number": 1,
          "bounding box": [left, bottom, right, top],
          "row number": 1,
          "column number": 1,
          "row span": 1,
          "column span": 1,
          "kids": [
            {
              "type": "paragraph",
              "content": "Cell text"
            }
          ]
        }
      ]
    }
  ]
}
```

## Bounding Box Coordinate System

- **OpenDataLoader**: `[left, bottom, right, top]` in PDF points, origin at BOTTOMLEFT
- **Docling**: `{l, t, r, b}` with `coord_origin: "BOTTOMLEFT"` or `"TOPLEFT"`

### Conversion Notes

- If docling uses TOPLEFT origin: `bottom = page_height - docling_t`, `top = page_height - docling_b`
- If docling uses BOTTOMLEFT origin: direct mapping `[l, b, r, t]` → `[left, bottom, right, top]`

## Key Java Classes

From the codebase:

- `TableBorder` - Table with border-based detection
- `TableBorderRow` - Table row
- `TableBorderCell` - Table cell with contents, rowSpan, colSpan
- `BoundingBox` - PDF coordinates (page, left, bottom, right, top)
- Processors: `TextLineProcessor`, `TableBorderProcessor`, `HeadingProcessor`, `ListProcessor`


# FILE: docs/hybrid/research/opendataloader-sample-response.md

Civil Society Engagement

election integrity. The registration of local election observers runs until 25 May, and the NEC is still reviewing the application of nearly 5,000 observers.

# Table: The number of accredited observers as of 28 April 202215

|No.|Name of organization|Number of accredited observers|
|---|---|---|
|1<br>2<br>3<br>4<br>5<br>6<br>7<br>|Union of Youth Federations of Cambodia (UYFC)<br><br>Cambodian Women for Peace and Development<br><br>Association of Democratic Students of Cambodia<br><br>Association of Intellectual and Youth Volunteer<br><br>Our Friends Association COMFREL Traditional and Modern Mental Health Organization|17,266<br><br>9,835<br><br>711<br><br>46<br><br>27 26 15|
||Total|27,926|


15 https://www.nec.gov.kh/khmer/content/5524

17



# FILE: docs/hybrid/experiments/speed/speed-experiment-2026-01-03.md

# Docling Speed Experiment Results

**Date**: 2026-01-03 14:31:43

## Summary

| Approach | Description | Avg (s/doc) | Target | Status | Speedup |
|----------|-------------|-------------|--------|--------|---------|
| baseline | docling-serve HTTP | 2.283 | - | - | - |
| fastapi | FastAPI + SDK singleton | 0.685 | 0.8 | PASS | 3.3x |
| subprocess | Persistent subprocess | 0.661 | 1.0 | PASS | 3.5x |

## Decision

**Phase 0 PASSED** - FastAPI approach meets the < 0.8s threshold.

Proceed to Phase 1 implementation:

- [x] Task 1.1: docling_subprocess_worker.py (skipped - FastAPI only)
- [x] Task 1.2: hybrid_server.py (opendataloader-pdf-hybrid CLI)
- [x] Task 2.1: DoclingSubprocessClient.java (skipped - FastAPI only)
- [x] Task 2.2: DoclingFastServerClient.java
- [x] Task 2.3: HybridClientFactory modification
- [x] Task 3: Benchmark integration
- [x] Task 4: Final validation

Subprocess approach also passed - both approaches available for implementation.

## Detailed Statistics

### Baseline

- **Description**: docling-serve HTTP API
- **Timestamp**: 2026-01-03 14:23:41
- **Total documents**: 200
- **Successful**: 200
- **Failed**: 0
- **Total elapsed**: 456.6s
- **Average per doc**: 2.2825s
- **Min**: 2.0045s
- **Max**: 8.0182s

### Fastapi

- **Description**: FastAPI server with docling SDK singleton
- **Timestamp**: 2026-01-03 14:27:18
- **Total documents**: 200
- **Successful**: 200
- **Failed**: 0
- **Total elapsed**: 137.1s
- **Average per doc**: 0.6855s
- **Min**: 0.1912s
- **Max**: 4.2420s

### Subprocess

- **Description**: Persistent Python subprocess with docling SDK
- **Timestamp**: 2026-01-03 14:30:50
- **Total documents**: 200
- **Successful**: 200
- **Failed**: 0
- **Total elapsed**: 132.4s
- **Average per doc**: 0.6612s
- **Min**: 0.1908s
- **Max**: 4.2498s


# FILE: examples/python/rag/basic_chunking.py

#!/usr/bin/env python3
"""
Basic RAG Chunking Example - No External Dependencies

Demonstrates PDF-to-chunks conversion using only opendataloader-pdf
and Python standard library. Ready for integration with any embedding
model or vector store.

Usage:
    pip install opendataloader-pdf
    python basic_chunking.py
"""

import json
import tempfile
from pathlib import Path


import opendataloader_pdf


def convert_pdf_to_json(pdf_path: str, output_dir: str) -> Path:
    """Convert PDF to JSON and Markdown with reading order enabled."""
    opendataloader_pdf.convert(
        input_path=pdf_path,
        output_dir=output_dir,
        format="json,markdown",
        reading_order="xycut",
        quiet=True,
    )
    pdf_name = Path(pdf_path).stem
    return Path(output_dir) / f"{pdf_name}.json"


def load_document(json_path: Path) -> dict:
    """Load the JSON output from OpenDataLoader."""
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)


def chunk_by_element(doc: dict) -> list[dict]:
    """
    Strategy 1: Chunk by semantic element.

    Creates one chunk per paragraph, heading, or list element.
    Best for: Fine-grained retrieval, precise citations.
    """
    chunks = []
    for element in doc.get("kids", []):
        if element.get("type") in ("paragraph", "heading", "list"):
            chunks.append({
                "text": element.get("content", ""),
                "metadata": {
                    "type": element["type"],
                    "page": element.get("page number"),
                    "bbox": element.get("bounding box"),
                    "source": doc.get("file name"),
                }
            })
    return chunks


def chunk_by_section(doc: dict) -> list[dict]:
    """
    Strategy 2: Chunk by heading/section.

    Groups content under headings into coherent sections.
    Best for: Context-rich retrieval, topic-based search.
    """
    chunks = []
    current_heading = None
    current_content: list[str] = []
    current_start_page = None

    for element in doc.get("kids", []):
        element_type = element.get("type")

        if element_type == "heading":
            # Save previous section
            if current_content:
                chunks.append({
                    "text": "\n".join(current_content),
                    "metadata": {
                        "heading": current_heading,
                        "page": current_start_page,
                        "source": doc.get("file name"),
                    }
                })
            current_heading = element.get("content", "")
            current_content = [current_heading]
            current_start_page = element.get("page number")
        elif element_type in ("paragraph", "list"):
            content = element.get("content", "")
            if content:
                current_content.append(content)

    # Save the last section
    if current_content:
        chunks.append({
            "text": "\n".join(curre

# FILE: examples/python/rag/README.md

# RAG Examples for OpenDataLoader PDF

Working examples demonstrating how to use OpenDataLoader PDF in RAG (Retrieval-Augmented Generation) pipelines.

## Prerequisites

- Python 3.10+
- Java 11+ (on PATH)

## Sample PDF

Examples use `samples/pdf/1901.03003.pdf` - a multi-page academic paper (arXiv:1901.03003) with:
- Two-column layout
- Multiple sections and headings
- Tables and figures
- Complex reading order

## Examples

### 1. Basic Chunking (No External Dependencies)

[`basic_chunking.py`](basic_chunking.py) demonstrates PDF-to-chunks conversion using only `opendataloader-pdf` and Python standard library. No external embedding or vector store dependencies.

**Features:**
- PDF to JSON conversion with reading order
- Three chunking strategies:
  1. By element (paragraph, heading, list)
  2. By section (grouped under headings)
  3. Merged chunks (minimum size threshold)
- Bounding box metadata for citations

**Run:**
```bash
pip install opendataloader-pdf
python basic_chunking.py
```

### 2. LangChain Integration

[`langchain_example.py`](langchain_example.py) shows integration with the official LangChain loader.

**Features:**
- OpenDataLoaderPDFLoader usage
- Returns LangChain Document objects
- Ready for any LangChain pipeline

**Run:**
```bash
pip install -r requirements.txt
python langchain_example.py
```

## Sample Output

```
Processing: 1901.03003.pdf
==================================================
Document: 1901.03003.pdf
Pages: 9
Elements: 187

--- Strategy 1: Chunk by Element ---
Created 156 chunks
  [1] RoBERTa: A Robustly Optimized BERT Pretraining Approach
      Source: 1901.03003.pdf, Page 1, Position (108, 655)
  [2] Yinhan Liu† Myle Ott† Naman Goyal† Jingfei Du† ...
      Source: 1901.03003.pdf, Page 1, Position (142, 603)

--- Strategy 2: Chunk by Section ---
Created 12 chunks
  Section: RoBERTa: A Robustly Optimized BERT Pretraining Approach
  Section: 1 Introduction
  Section: 2 Background
  ...
```

## Next Steps

After chunking, integrate with your preferred:
- **Embedding model**: OpenAI, Cohere, HuggingFace, etc.
- **Vector store**: Chroma, FAISS, Pinecone, Weaviate, etc.

Each chunk includes `text` and `metadata` ready for embedding:

```python
{
  "text": "Language model pretraining has led to significant...",
  "metadata": {
    "type": "paragraph",
    "page": 1,
    "bbox": [108.0, 526.2, 286.5, 592.8],
    "source": "1901.03003.pdf"
  }
}
```


# FILE: examples/python/rag/langchain_example.py

#!/usr/bin/env python3
"""
LangChain Integration Example

Demonstrates using the official langchain-opendataloader-pdf package
for seamless RAG pipeline integration.

Usage:
    pip install langchain-opendataloader-pdf
    python langchain_example.py
"""

from pathlib import Path

from langchain_opendataloader_pdf import OpenDataLoaderPDFLoader


def main():
    # Find sample PDF relative to this script
    # Using 1901.03003.pdf - a multi-page academic paper with complex layout
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent.parent
    sample_pdf = repo_root / "samples" / "pdf" / "1901.03003.pdf"

    if not sample_pdf.exists():
        print(f"Sample PDF not found at: {sample_pdf}")
        print("Make sure you're running from the repository.")
        return

    print(f"Loading: {sample_pdf.name}")
    print("=" * 50)

    # Create loader with LangChain integration
    loader = OpenDataLoaderPDFLoader(
        file_path=[str(sample_pdf)],
        format="text",
        quiet=True,
    )

    # Load documents (returns LangChain Document objects)
    documents = loader.load()

    print(f"Loaded {len(documents)} document(s)\n")

    for i, doc in enumerate(documents):
        print(f"--- Document {i+1} ---")
        print(f"Metadata: {doc.metadata}")
        content_preview = doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
        print(f"Content:\n{content_preview}\n")

    # Show integration points
    print("--- LangChain Integration ---")
    print("These Document objects work directly with:")
    print("  - Text splitters: RecursiveCharacterTextSplitter, etc.")
    print("  - Vector stores: Chroma, FAISS, Pinecone, etc.")
    print("  - Retrievers: vectorstore.as_retriever()")
    print("  - Chains: RetrievalQA, ConversationalRetrievalChain, etc.")

    # Example: Using with a text splitter
    print("\n--- Example: Text Splitting ---")
    try:
        from langchain_text_splitters import RecursiveCharacterTextSplitter

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
        )
        chunks = splitter.split_documents(documents)
        print(f"Split into {len(chunks)} chunks")
        if chunks:
            print(f"First chunk ({len(chunks[0].page_content)} chars):")
            print(f"  {chunks[0].page_content[:100]}...")
    except ImportError:
        print("Install langchain-text-splitters to see this example:")
        print("  pip install langchain-text-splitters")


if __name__ == "__main__":
    main()


# FILE: examples/python/batch/README.md

# Batch Processing Example

Demonstrates processing multiple PDFs in a single invocation to avoid repeated Java JVM startup overhead.

## Prerequisites

- Python 3.10+
- Java 11+ (on PATH)

## Example

[`batch_processing.py`](batch_processing.py) shows two methods for batch conversion:

1. **File list** — Pass multiple PDF paths as a list
2. **Directory** — Pass a directory path (recursively finds all PDFs)

Both methods use a single JVM invocation, which is significantly faster than calling the CLI once per file.

**Run:**
```bash
pip install -r requirements.txt
python batch_processing.py
```

## Sample Output

```
Found 4 PDFs in pdf/

==========================================================
Method 1: Batch convert with file list
==========================================================

Document                                  Pages Top-level
----------------------------------------------------------
1901.03003                                   15       241
2408.02509v1                                 14       365
chinese_scan                                  1         1
lorem                                         1         2
----------------------------------------------------------
Total                                        31       609

Processed 4 documents
Time: 7.95s (single JVM invocation)
```


# FILE: examples/python/batch/batch_processing.py

#!/usr/bin/env python3
"""
Batch Processing Example

Demonstrates processing multiple PDFs in a single invocation to avoid
repeated Java JVM startup overhead. This is the recommended approach
for large-scale document pipelines.

Requires Python 3.10+.

Usage:
    pip install opendataloader-pdf
    python batch_processing.py
"""

from __future__ import annotations

import json
import tempfile
import time
from pathlib import Path

import opendataloader_pdf


def batch_convert(pdf_paths: list[str], output_dir: str) -> list[Path]:
    """Convert multiple PDFs in a single JVM invocation."""
    opendataloader_pdf.convert(
        input_path=pdf_paths,
        output_dir=output_dir,
        format="json,markdown",
        quiet=True,
    )
    # Collect output JSON files
    return sorted(Path(output_dir).glob("*.json"))


def convert_directory(directory: str, output_dir: str) -> list[Path]:
    """Convert all PDFs in a directory (recursive)."""
    opendataloader_pdf.convert(
        input_path=directory,
        output_dir=output_dir,
        format="json,markdown",
        quiet=True,
    )
    return sorted(Path(output_dir).glob("*.json"))


def summarize_results(json_files: list[Path]) -> None:
    """Print a summary of all converted documents."""
    total_pages = 0
    total_elements = 0

    print(f"\n{'Document':<40} {'Pages':>6} {'Top-level':>9}")
    print("-" * 58)

    for json_path in json_files:
        with open(json_path, encoding="utf-8") as f:
            doc = json.load(f)
        pages = doc.get("number of pages", 0)
        elements = len(doc.get("kids", []))
        total_pages += pages
        total_elements += elements
        print(f"{json_path.stem:<40} {pages:>6} {elements:>9}")

    print("-" * 58)
    print(f"{'Total':<40} {total_pages:>6} {total_elements:>9}")
    print(f"\nProcessed {len(json_files)} documents")


def main():
    # Find sample PDFs relative to this script
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent.parent.parent
    samples_dir = repo_root / "samples" / "pdf"

    pdf_files = sorted(samples_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No sample PDFs found at: {samples_dir}")
        return

    print(f"Found {len(pdf_files)} PDFs in {samples_dir.name}/")
    for p in pdf_files:
        print(f"  - {p.name}")

    # --- Method 1: Pass a list of files ---
    print("\n" + "=" * 58)
    print("Method 1: Batch convert with file list")
    print("=" * 58)

    with tempfile.TemporaryDirectory() as temp_dir:
        start = time.perf_counter()
        json_files = batch_convert(
            [str(p) for p in pdf_files],
            temp_dir,
        )
        elapsed = time.perf_counter() - start

        summarize_results(json_files)
        print(f"Time: {elapsed:.2f}s (single JVM invocation)")

    # --- Method 2: Pass a directory ---
    # Note: directory input recursively finds PDFs in subdirectories,
    # so the file count may differ from Method 1 (which
