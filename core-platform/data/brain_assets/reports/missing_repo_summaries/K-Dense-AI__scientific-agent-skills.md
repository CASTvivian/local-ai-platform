# Missing Repo Summary Source: K-Dense-AI/scientific-agent-skills

- URL: https://github.com/K-Dense-AI/scientific-agent-skills
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/K-Dense-AI__scientific-agent-skills
- Clone Status: cloned
- Language: Python
- Stars: 20767
- Topics: agent-skills, ai-scientist, bioinformatics, chemoinformatics, claude, claude-skills, claudecode, clinical-research, computational-biology, data-analysis, drug-discovery, genomics, materials-science, metabolomics, proteomics, scientific-computing, scientific-visualization
- Description: A set of ready to use Agent Skills for research, science, engineering, analysis, finance and writing.

## Extracted README / Docs / Examples



# FILE: README.md

# Scientific Agent Skills

> **🔔 Claude Scientific Skills is now Scientific Agent Skills.** Same skills, broader compatibility — now works with any AI agent that supports the open [Agent Skills](https://agentskills.io/) standard, not just Claude.

> **New: [K-Dense BYOK](https://github.com/K-Dense-AI/k-dense-byok)** — A free, open-source AI co-scientist that runs on your desktop, powered by Scientific Agent Skills. Bring your own API keys, pick from 40+ models, and get a full research workspace with web search, file handling, 100+ scientific databases, and access to all 135 skills in this repo. Your data stays on your computer, and you can optionally scale to cloud compute via [Modal](https://modal.com/) for heavy workloads. [Get started here.](https://github.com/K-Dense-AI/k-dense-byok)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Skills](https://img.shields.io/badge/Skills-135-brightgreen.svg)](#whats-included)
[![Databases](https://img.shields.io/badge/Databases-100%2B-orange.svg)](#whats-included)
[![Agent Skills](https://img.shields.io/badge/Standard-Agent_Skills-blueviolet.svg)](https://agentskills.io/)
[![Works with](https://img.shields.io/badge/Works_with-Cursor_|_Claude_Code_|_Codex-blue.svg)](#getting-started)
[![X](https://img.shields.io/badge/Follow_on_X-%40k__dense__ai-000000?logo=x)](https://x.com/k_dense_ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-K--Dense_Inc.-0A66C2?logo=linkedin)](https://www.linkedin.com/company/k-dense-inc)
[![YouTube](https://img.shields.io/badge/YouTube-K--Dense_Inc.-FF0000?logo=youtube)](https://www.youtube.com/@K-Dense-Inc)

A comprehensive collection of **135 ready-to-use scientific and research skills** (covering cancer genomics, drug-target binding, molecular dynamics, RNA velocity, geospatial science, time series forecasting, scientific ML resource discovery via Hugging Science, 78+ scientific databases, and more) for any AI agent that supports the open [Agent Skills](https://agentskills.io/) standard, created by [K-Dense](https://k-dense.ai). Works with **Cursor, Claude Code, Codex, and more**. Transform your AI agent into a research assistant capable of executing complex multi-step scientific workflows across biology, chemistry, medicine, and beyond.

---

These skills enable your AI agent to seamlessly work with specialized scientific libraries, databases, and tools across multiple scientific domains. While the agent can use any Python package or API on its own, these explicitly defined skills provide curated documentation and examples that make it significantly stronger and more reliable for the workflows below:
- 🧬 Bioinformatics & Genomics - Sequence analysis, single-cell RNA-seq, gene regulatory networks, variant annotation, phylogenetic analysis
- 🧪 Cheminformatics & Drug Discovery - Molecular property prediction, virtual screening, ADMET analysis, molecular docking, lead optimization
- 🔬 Proteomics & Mass Spectrometry - LC-MS/MS processing, peptide identification, spectral matching, protein quantification
- 🏥 Clinical Research & Precision Medicine - Clinical trials, pharmacogenomics, variant interpretation, drug safety, clinical decision support, treatment planning
- 🧠 Healthcare AI & Clinical ML - EHR analysis, physiological signal processing, medical imaging, clinical prediction models
- 🖼️ Medical Imaging & Digital Pathology - DICOM processing, whole slide image analysis, computational pathology, radiology workflows
- 🤖 Machine Learning & AI - Deep learning, reinforcement learning, time series analysis, model interpretability, Bayesian methods
- 🔮 Materials Science & Chemistry - Crystal structure analysis, phase diagrams, metabolic modeling, computational chemistry
- 🌌 Physics & Astronomy - Astronomical data analysis, coordinate transformations, cosmological calculations, symbolic mathematics, physics computations
- ⚙️ Engineering & Simulation - Discrete-event simulation, multi-objective optimization, metabolic engineering, systems modeling, process optimization
- 📊 Data Analysis & Visualization - Statistical analysis, network analysis, time series, publication-quality figures, large-scale data processing, EDA
- 🌍 Geospatial Science & Remote Sensing - Satellite imagery processing, GIS analysis, spatial statistics, terrain analysis, machine learning for Earth observation
- 🧪 Laboratory Automation - Liquid handling protocols, lab equipment control, workflow automation, LIMS integration
- 📚 Scientific Communication - Literature review, peer review, scientific writing, document processing, posters, slides, schematics, citation management
- 🔬 Multi-omics & Systems Biology - Multi-modal data integration, pathway analysis, network biology, systems-level insights
- 🧬 Protein Engineering & Design - Protein language models, structure prediction, sequence design, function annotation
- 🎓 Research Methodology - Hypothesis generation, scientific brainstorming, critical thinking, grant writing, scholar evaluation

**Transform your AI coding agent into an 'AI Scientist' on your desktop!**

> ⭐ **If you find this repository useful**, please consider giving it a star! It helps others discover these tools and encourages us to continue maintaining and expanding this collection.

> 🎬 **New to Scientific Agent Skills?** Watch our [Getting Started with Scientific Agent Skills](https://youtu.be/ZxbnDaD_FVg) video for a quick walkthrough.

---

## 📦 What's Included

This repository provides **135 scientific and research skills** organized into the following categories:

- **100+ Scientific & Financial Databases** - A unified database-lookup skill provides direct access to 78 public databases (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov, FRED, USPTO, and more), plus dedicated skills for DepMap, Imaging Data Commons, PrimeKG, U.S. Treasury Fiscal Data, and Hugging Science (curated catalog of scientific datasets, models, and demos across 17 scientific domains on Hugging Face). Multi-database packages like BioServices (~40 bioinformatics services), BioPython (38 NCBI sub-databases via Entrez), and gget (20+ genomics databases) add further coverage
- **70+ Optimized Python Package Skills** - Explicitly defined skills for RDKit, Scanpy, PyTorch Lightning, scikit-learn, BioPython, pyzotero, BioServices, PennyLane, Qiskit, OpenMM, MDAnalysis, scVelo, TimesFM, and others — with curated documentation, examples, and best practices. Note: the agent can write code using *any* Python package, not just these; these skills simply provide stronger, more reliable performance for the packages listed
- **9 Scientific Integration Skills** - Explicitly defined skills for Benchling, DNAnexus, LatchBio, OMERO, Protocols.io, Open Notebook, and more. Again, the agent is not limited to these — any API or platform reachable from Python is fair game; these skills are the optimized, pre-documented paths
- **30+ Analysis & Communication Tools** - Literature review, scientific writing, peer review, document processing, posters, slides, schematics, infographics, Mermaid diagrams, and more
- **10+ Research & Clinical Tools** - Hypothesis generation, grant writing, clinical decision support, treatment plans, regulatory compliance, scenario analysis

Each skill includes:
- ✅ Comprehensive documentation (`SKILL.md`)
- ✅ Practical code examples
- ✅ Use cases and best practices
- ✅ Integration guides
- ✅ Reference materials

---

## 📋 Table of Contents

- [What's Included](#whats-included)
- [Why Use This?](#why-use-this)
- [Getting Started](#getting-started)
- [Security Disclaimer](#-security-disclaimer)
- [Support Open Source](#-support-the-open-source-community)
- [Prerequisites](#prerequisites)
- [Quick Examples](#quick-examples)
- [Use Cases](#use-cases)
- [Available Skills](#available-skills)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Support](#support)
- [Citation](#citation)
- [License](#license)

---

## 🚀 Why Use This?

### ⚡ **Accelerate Your Research**
- **Save Days of Work** - Skip API documentation research and integration setup
- **Production-Ready Code** - Tested, validated examples following scientific best practices
- **Multi-Step Workflows** - Execute complex pipelines with a single prompt

### 🎯 **Comprehensive Coverage**
- **135 Skills** - Extensive coverage across all major scientific domains
- **100+ Databases** - Unified access to 78+ databases via database-lookup, plus dedicated data access skills and multi-database packages like BioServices, BioPython, and gget
- **70+ Optimized Python Package Skills** - RDKit, Scanpy, PyTorch Lightning, scikit-learn, BioServices, PennyLane, Qiskit, OpenMM, scVelo, TimesFM, and others (the agent can use any Python package; these are the pre-documented, higher-performing paths)

### 🔧 **Easy Integration**
- **Simple Setup** - Copy skills to your skills directory and start working
- **Automatic Discovery** - Your agent automatically finds and uses relevant skills
- **Well Documented** - Each skill includes examples, use cases, and best practices

### 🌟 **Maintained & Supported**
- **Regular Updates** - Continuously maintained and expanded by K-Dense team
- **Community Driven** - Open source with active community contributions
- **Enterprise Ready** - Commercial support available for advanced needs

---

## 🎯 Getting Started

### Option 1: npx (all platforms)

Install Scientific Agent Skills with a single command:

```bash
npx skills add K-Dense-AI/scientific-agent-skills
```

This is the official standard approach for installing Agent Skills across **all platforms**, including **Claude Code**, **Claude Cowork**, **Codex**, **Gemini CLI**, **Cursor**, and any other agent that supports the open [Agent Skills](https://agentskills.io/) standard.

### Option 2: GitHub CLI (`gh skill`)

If you use the [GitHub CLI](https://cli.github.com/) (v2.90.0+), you can install skills with [`gh skill`](https://github.blog/changelog/2026-04-16-manage-agent-skills-with-githu

# FILE: docs/examples.md

# Real-World Scientific Examples

This document provides comprehensive, practical examples demonstrating how to combine Scientific Agent Skills to solve real scientific problems across multiple domains.

---

## 📋 Table of Contents

1. [Drug Discovery & Medicinal Chemistry](#drug-discovery--medicinal-chemistry)
2. [Cancer Genomics & Precision Medicine](#cancer-genomics--precision-medicine)
3. [Single-Cell Transcriptomics](#single-cell-transcriptomics)
4. [Protein Structure & Function](#protein-structure--function)
5. [Chemical Safety & Toxicology](#chemical-safety--toxicology)
6. [Clinical Trial Analysis](#clinical-trial-analysis)
7. [Metabolomics & Systems Biology](#metabolomics--systems-biology)
8. [Materials Science & Chemistry](#materials-science--chemistry)
9. [Digital Pathology](#digital-pathology)
10. [Lab Automation & Protocol Design](#lab-automation--protocol-design)
11. [Agricultural Genomics](#agricultural-genomics)
12. [Neuroscience & Brain Imaging](#neuroscience--brain-imaging)
13. [Environmental Microbiology](#environmental-microbiology)
14. [Infectious Disease Research](#infectious-disease-research)
15. [Multi-Omics Integration](#multi-omics-integration)
16. [Computational Chemistry & Synthesis](#computational-chemistry--synthesis)
17. [Clinical Research & Real-World Evidence](#clinical-research--real-world-evidence)
18. [Experimental Physics & Data Analysis](#experimental-physics--data-analysis)
19. [Chemical Engineering & Process Optimization](#chemical-engineering--process-optimization)
20. [Scientific Illustration & Visual Communication](#scientific-illustration--visual-communication)
21. [Quantum Computing for Chemistry](#quantum-computing-for-chemistry)
22. [Research Grant Writing](#research-grant-writing)
23. [Flow Cytometry & Immunophenotyping](#flow-cytometry--immunophenotyping)

---

## Drug Discovery & Medicinal Chemistry

### Example 1: Discovery of Novel EGFR Inhibitors for Lung Cancer

**Objective**: Identify novel small molecule inhibitors of EGFR with improved properties compared to existing drugs.

**Skills Used**:
- `database-lookup` - Query ChEMBL, PubChem, COSMIC, AlphaFold DB
- `paper-lookup` - Search PubMed for literature
- `rdkit` - Analyze molecular properties
- `datamol` - Generate analogs
- `medchem` - Medicinal chemistry filters
- `molfeat` - Molecular featurization
- `diffdock` - Molecular docking
- `deepchem` - Property prediction
- `torchdrug` - Graph neural networks for molecules
- `scientific-visualization` - Create figures
- `clinical-reports` - Generate PDF reports

**Workflow**:

```bash
# Always use available 'skills' when possible. Keep the output organized.

Step 1: Query ChEMBL for known EGFR inhibitors with high potency
- Search for compounds targeting EGFR (CHEMBL203)
- Filter: IC50 < 50 nM, pChEMBL value > 7
- Extract SMILES strings and activity data
- Export to DataFrame for analysis

Step 2: Analyze structure-activity relationships
- Load compounds into RDKit
- Calculate molecular descriptors (MW, LogP, TPSA, HBD, HBA)
- Generate Morgan fingerprints (radius=2, 2048 bits)
- Perform hierarchical clustering to identify scaffolds
- Visualize top scaffolds with activity annotations

Step 3: Identify resistance mutations from COSMIC
- Query COSMIC for EGFR mutations in lung cancer
- Focus on gatekeeper mutations (T790M, C797S)
- Extract mutation frequencies and clinical significance
- Cross-reference with literature in PubMed

Step 4: Retrieve EGFR structure from AlphaFold
- Download AlphaFold prediction for EGFR kinase domain
- Alternatively, use experimental structure from PDB (if available)
- Prepare structure for docking (add hydrogens, optimize)

Step 5: Generate novel analogs using datamol
- Select top 5 scaffolds from ChEMBL analysis
- Use scaffold decoration to generate 100 analogs per scaffold
- Apply Lipinski's Rule of Five filtering
- Ensure synthetic accessibility (SA score < 4)
- Check for PAINS and unwanted substructures

Step 6: Predict properties with DeepChem
- Train graph convolutional model on ChEMBL EGFR data
- Predict pIC50 for generated analogs
- Predict ADMET properties (solubility, permeability, hERG)
- Rank candidates by predicted potency and drug-likeness

Step 7: Virtual screening with DiffDock
- Perform molecular docking on top 50 candidates
- Dock into wild-type EGFR and T790M mutant
- Calculate binding energies and interaction patterns
- Identify compounds with favorable binding to both forms

Step 8: Search PubChem for commercial availability
- Query PubChem for top 10 candidates by InChI key
- Check supplier information and purchasing options
- Identify close analogs if exact matches unavailable

Step 9: Literature validation with PubMed
- Search for any prior art on top scaffolds
- Query: "[scaffold_name] AND EGFR AND inhibitor"
- Summarize relevant findings and potential liabilities

Step 10: Create comprehensive report
- Generate 2D structure visualizations of top hits
- Create scatter plots: MW vs LogP, TPSA vs potency
- Produce binding pose figures for top 3 compounds
- Generate table comparing properties to approved drugs (gefitinib, erlotinib)
- Write scientific summary with methodology, results, and recommendations
- Export to PDF with proper citations

Expected Output: 
- Ranked list of 10-20 novel EGFR inhibitor candidates
- Predicted activity and ADMET properties
- Docking poses and binding analysis
- Comprehensive scientific report with publication-quality figures
```

---

### Example 2: Drug Repurposing for Rare Diseases

**Objective**: Identify FDA-approved drugs that could be repurposed for treating a rare metabolic disorder.

**Skills Used**:
- `database-lookup` - Query DrugBank, Open Targets, STRING, KEGG, Reactome, ClinicalTrials.gov, FDA
- `paper-lookup` - Search OpenAlex, bioRxiv, PubMed
- `networkx` - Network analysis
- `bioservices` - Biological database queries
- `literature-review` - Systematic review

**Workflow**:

```bash
Step 1: Define disease pathway
- Query KEGG and Reactom

# FILE: docs/open-source-sponsors.md

# Support the Open Source Projects We Depend On

Scientific Agent Skills is built on the shoulders of giants. The 135 skills in this repository leverage dozens of incredible open source projects created and maintained by dedicated developers and research communities around the world.

**If you find value in these skills, please consider supporting the underlying open source projects that make them possible.**

---

## How to Support Open Source

1. **Star repositories** on GitHub - It's free and helps projects gain visibility
2. **Sponsor maintainers** directly through GitHub Sponsors, Open Collective, or project-specific donation pages
3. **Contribute** code, documentation, or bug reports
4. **Cite** projects in your publications
5. **Share** projects with colleagues

---

## Featured Projects by Domain

### Bioinformatics & Genomics

| Project | Description | Links |
|---------|-------------|-------|
| **Biopython** | Computational molecular biology toolkit | [GitHub](https://github.com/biopython/biopython) - [Donate](https://numfocus.org/donate-to-biopython) |
| **Scanpy** | Single-cell analysis in Python | [GitHub](https://github.com/scverse/scanpy) - [scverse](https://scverse.org/) |
| **AnnData** | Annotated data matrices for single-cell | [GitHub](https://github.com/scverse/anndata) |
| **scvi-tools** | Deep learning for single-cell omics | [GitHub](https://github.com/scverse/scvi-tools) |
| **Arboreto** | Gene regulatory network inference | [GitHub](https://github.com/aertslab/arboreto) |
| **pysam** | SAM/BAM/VCF file interface | [GitHub](https://github.com/pysam-developers/pysam) |
| **scikit-bio** | Bioinformatics library | [GitHub](https://github.com/scikit-bio/scikit-bio) |
| **gget** | Gene and transcript info retrieval | [GitHub](https://github.com/pachterlab/gget) |
| **deepTools** | Tools for deep-sequencing data | [GitHub](https://github.com/deeptools/deepTools) |
| **ETE Toolkit** | Phylogenetic tree analysis | [GitHub](https://github.com/etetoolkit/ete) |

### Cheminformatics & Drug Discovery

| Project | Description | Links |
|---------|-------------|-------|
| **RDKit** | Cheminformatics toolkit | [GitHub](https://github.com/rdkit/rdkit) - [Donate](https://github.com/sponsors/rdkit) |
| **Datamol** | Molecular manipulation made easy | [GitHub](https://github.com/datamol-io/datamol) |
| **DeepChem** | Deep learning for chemistry | [GitHub](https://github.com/deepchem/deepchem) |
| **TorchDrug** | Drug discovery with PyTorch | [GitHub](https://github.com/DeepGraphLearning/torchdrug) |
| **molfeat** | Molecular featurization | [GitHub](https://github.com/datamol-io/molfeat) |
| **MedChem** | Medicinal chemistry filters | [GitHub](https://github.com/datamol-io/medchem) |
| **PyTDC** | Therapeutics Data Commons | [GitHub](https://github.com/mims-harvard/TDC) |

### Proteomics & Mass Spectrometry

| Project | Description | Links |
|---------|-------------|-------|
| **matchms** | Mass spectrometry data processing | [GitHub](https://github.com/matchms/matchms) |
| **pyOpenMS** | Mass spectrometry toolkit | [GitHub](https://github.com/OpenMS/OpenMS) |

### Machine Learning & AI

| Project | Description | Links |
|---------|-------------|-------|
| **PyTorch Lightning** | Deep learning framework | [GitHub](https://github.com/Lightning-AI/pytorch-lightning) - [Sponsor](https://github.com/sponsors/Lightning-AI) |
| **Transformers** | State-of-the-art NLP | [GitHub](https://github.com/huggingface/transformers) |
| **scikit-learn** | Machine learning in Python | [GitHub](https://github.com/scikit-learn/scikit-learn) - [Donate](https://numfocus.org/donate-to-scikit-learn) |
| **PyTorch Geometric** | Geometric deep learning | [GitHub](https://github.com/pyg-team/pytorch_geometric) |
| **PyMC** | Probabilistic programming | [GitHub](https://github.com/pymc-devs/pymc) - [Donate](https://numfocus.org/donate-to-pymc) |
| **SHAP** | Model interpretability | [GitHub](https://github.com/shap/shap) |
| **Stable Baselines3** | Reinforcement learning | [GitHub](https://github.com/DLR-RM/stable-baselines3) |
| **scikit-survival** | Survival analysis | [GitHub](https://github.com/sebp/scikit-survival) |
| **aeon** | Time series ML toolkit | [GitHub](https://github.com/aeon-toolkit/aeon) |
| **PyMOO** | Multi-objective optimization | [GitHub](https://github.com/anyoptimization/pymoo) |
| **UMAP** | Dimensionality reduction | [GitHub](https://github.com/lmcinnes/umap) |

### Data Science & Visualization

| Project | Description | Links |
|---------|-------------|-------|
| **Matplotlib** | Plotting library | [GitHub](https://github.com/matplotlib/matplotlib) - [Donate](https://numfocus.org/donate-to-matplotlib) |
| **Seaborn** | Statistical visualization | [GitHub](https://github.com/mwaskom/seaborn) |
| **Plotly** | Interactive visualizations | [GitHub](https://github.com/plotly/plotly.py) |
| **NetworkX** | Network analysis | [GitHub](https://github.com/networkx/networkx) - [Donate](https://numfocus.org/donate-to-networkx) |
| **SymPy** | Symbolic mathematics | [GitHub](https://github.com/sympy/sympy) - [Donate](https://numfocus.org/donate-to-sympy) |
| **statsmodels** | Statistical modeling | [GitHub](https://github.com/statsmodels/statsmodels) |
| **GeoPandas** | Geospatial data in Python | [GitHub](https://github.com/geopandas/geopandas) |
| **Polars** | Fast DataFrame library | [GitHub](https://github.com/pola-rs/polars) |
| **Dask** | Parallel computing | [GitHub](https://github.com/dask/dask) - [Donate](https://numfocus.org/donate-to-dask) |
| **Vaex** | Out-of-core DataFrames | [GitHub](https://github.com/vaexio/vaex) |

### Medical Imaging & Digital Pathology

| Project | Description | Links |
|---------|-------------|-------|
| **pydicom** | DICOM file handling | [GitHub](https://github.com/pydicom/pydicom) |
| **histolab** | Digital pathology preprocessing | [GitHub](https://github.com/histolab/histolab) |
| **PathML** | Pathology ML toolkit | [GitHub](https://github.com/Dana-Farber

# FILE: docs/scientific-skills.md

# Scientific Skills

## Scientific Databases & Data Access

- **Database Lookup** - Search 78 public scientific, biomedical, materials science, and economic databases via their REST APIs and return structured JSON results. Covers physics/astronomy (NASA, NIST, SDSS, SIMBAD, Exoplanet Archive), earth/environment (USGS, NOAA, EPA, OpenWeatherMap), chemistry/drugs (PubChem, ChEMBL, DrugBank, FDA, KEGG, DailyMed, ZINC, BindingDB), materials science (Materials Project, COD), biology/genomics (Reactome, BRENDA, UniProt, STRING, Ensembl, NCBI Gene, GEO, GTEx, PDB, AlphaFold, InterPro, ChEBI, BioGRID, Gene Ontology, QuickGO, NCBI Protein/Taxonomy, dbSNP, SRA, ENA, gnomAD, UCSC Genome, ENCODE, JASPAR, MouseMine, PRIDE, LINCS L1000, Human Protein Atlas, Human Cell Atlas, RummaGEO, Metabolomics Workbench, EMDB, Addgene), disease/clinical (COSMIC, Open Targets, ClinPGx, ClinicalTrials.gov, OMIM, ClinVar, GDC/TCGA, cBioPortal, DisGeNET, GWAS Catalog, Monarch, HPO), regulatory (FDA, USPTO, SEC EDGAR), economics/finance (FRED, BEA, BLS, Federal Reserve, World Bank, ECB, US Treasury, Alpha Vantage, Data Commons), and demographics (US Census, Eurostat, WHO). Use this skill whenever the user wants to look up compounds, drugs, proteins, genes, pathways, enzymes, gene expression, variants, clinical trials, patents, SEC filings, economic indicators, crystal structures, astronomical objects, earthquakes, weather, or any data from a public database API
- **DepMap** - Query the Cancer Dependency Map (DepMap) for cancer cell line gene dependency scores (CRISPR Chronos), drug sensitivity data, and gene effect profiles. Use for identifying cancer-specific vulnerabilities, synthetic lethal interactions, and validating oncology drug targets
- **Imaging Data Commons** - Query and download public cancer imaging data from NCI Imaging Data Commons using idc-index. Use for accessing large-scale radiology (CT, MR, PET) and pathology datasets for AI training or research. No authentication required. Query by metadata, visualize in browser, check licenses
- **PrimeKG** - Query the Precision Medicine Knowledge Graph (PrimeKG) for multiscale biological data including genes, drugs, diseases, phenotypes, and more. Integrates 20+ biomedical resources into a single knowledge graph for drug repurposing, disease mechanism exploration, and target identification
- **U.S. Treasury Fiscal Data** - Free, open REST API from the U.S. Department of the Treasury providing 54 datasets and 182 data tables covering federal fiscal data. No API key required. Access national debt (Debt to the Penny back to 1993, Historical Debt back to 1790), Daily Treasury Statements (TGA balances, deposits/withdrawals), Monthly Treasury Statements (federal budget receipts and outlays), Treasury securities auctions data (bills, notes, bonds, TIPS, FRNs since 1979), average interest rates on Treasury securities, Treasury reporting exchange rates (quarterly for 170+ currencies), I Bond and savings bond rates, TIPS/CPI data, and more. Supports filtering, sorting, pagination, and CSV/XML/JSON output formats
- **Hugging Science** - Curated, LLM-friendly catalog of scientific datasets, models, blog posts, and interactive Spaces hosted on Hugging Face, spanning 17 scientific domains (astronomy, benchmark, biology, biotechnology, chemistry, climate, conservation, earth-science, ecology, energy, engineering, genomics, materials-science, mathematics, medicine, physics, scientific-reasoning). Discovery happens via huggingscience.co (with `llms.txt`, `llms-full.txt`, and per-topic markdown files designed for agent consumption); usage goes through standard Hugging Face APIs. Includes a bundled `fetch_catalog.py` script for filtered access by topic, type (datasets/models/blogs/spaces), or free-text search, plus reference guides for loading datasets via the `datasets` library (with streaming for billion-token corpora), running models via `transformers` or the Inference API/Providers (handling `trust_remote_code` requirements for custom architectures like Evo-2), and calling Spaces via `gradio_client` (with a worked BoltzGen example for protein binder design). Authenticates gated resources via `HF_TOKEN` from `.env`. Use cases: discovering the right dataset/model for a scientific ML task without trawling the broader Hub, fine-tuning on curated scientific data, citing methodology blogs from dataset/model authors, running interactive scientific demos (binder design, theorem proving, weather modeling) without local GPU setup, and bridging from "I need a model for protein/genome/molecule/climate/materials/astronomy" to working code

## Scientific Integrations

### Laboratory Information Management Systems (LIMS) & R&D Platforms
- **Benchling Integration** - Toolkit for integrating with Benchling's R&D platform, providing programmatic access to laboratory data management including registry entities (DNA sequences, proteins), inventory systems (samples, containers, locations), electronic lab notebooks (entries, protocols), workflows (tasks, automation), and data exports using Python SDK and REST API

### Cloud Platforms for Genomics & Biomedical Data
- **DNAnexus Integration** - Comprehensive toolkit for working with the DNAnexus cloud platform for genomics and biomedical data analysis. Covers building and deploying apps/applets (Python/Bash), managing data objects (files, records, databases), running analyses and workflows, using the dxpy Python SDK, and configuring app metadata and dependencies (dxapp.json setup, system packages, Docker, assets). Enables processing of FASTQ/BAM/VCF files, bioinformatics pipelines, job execution, workflow orchestration, and platform operations including project management and permissions

### Laboratory Automation
- **Opentrons Integration** - Toolkit for creating, editing, and debugging Opentrons Python Protocol API v2 protocols for laboratory automation using Flex and OT-2 robots. Enables automated liquid handling, pipetting workflows, hardware mod
