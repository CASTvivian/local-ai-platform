# Missing Repo Summary Source: mukul975/Anthropic-Cybersecurity-Skills

- URL: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/mukul975__Anthropic-Cybersecurity-Skills
- Clone Status: cloned
- Language: Python
- Stars: 6246
- Topics: ai-agents, claude-code, cloud-security, cybersecurity, devsecops, ethical-hacking, incident-response, infosec, llm, malware-analysis, mcp, mitre-attack, nist-csf, osint, penetration-testing, red-team, security, security-automation, threat-hunting, threat-intelligence
- Description: 754 structured cybersecurity skills for AI agents · Mapped to 5 frameworks: MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND & NIST AI RMF · agentskills.io standard · Works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI & 20+ platforms · 26 security domains · Apache 2.0

## Extracted README / Docs / Examples



# FILE: README.md

<p align="center">
  <img src="assets/banner.png" alt="Anthropic Cybersecurity Skills" width="100%">
</p>

<div align="center">

#  Anthropic Cybersecurity Skills

### The largest open-source cybersecurity skills library for AI agents

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=flat-square)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-754-brightgreen?style=flat-square)](#whats-inside--26-security-domains)
[![Frameworks](https://img.shields.io/badge/frameworks-5-orange?style=flat-square)](#five-frameworks-one-skill-library)
[![Domains](https://img.shields.io/badge/domains-26-9cf?style=flat-square)](#whats-inside--26-security-domains)
[![Platforms](https://img.shields.io/badge/platforms-26%2B-blueviolet?style=flat-square)](#compatible-platforms)
[![GitHub stars](https://img.shields.io/github/stars/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/mukul975/Anthropic-Cybersecurity-Skills?style=flat-square)](https://github.com/mukul975/Anthropic-Cybersecurity-Skills/commits/main)
[![agentskills.io](https://img.shields.io/badge/standard-agentskills.io-ff6600?style=flat-square)](https://agentskills.io)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)
[![Playground](https://img.shields.io/badge/Playground-Casky.ai-blue)](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)
[![Hermes Agent](https://img.shields.io/badge/Hermes_Agent-compatible-blueviolet?style=flat)](https://github.com/NousResearch/hermes-agent)


**754 production-grade cybersecurity skills · 26 security domains · 5 framework mappings · 26+ AI platforms**

[Get Started](#quick-start) · [What's Inside](#whats-inside--26-security-domains) · [Frameworks](#five-frameworks-one-skill-library) · [Platforms](#compatible-platforms) · [Contributing](#contributing)

</div>

---

> ⚠️ **Community Project** — This is an independent, community-created project. Not affiliated with Anthropic PBC. 

## Give any AI agent the security skills of a senior analyst

A junior analyst knows which Volatility3 plugin to run on a suspicious memory dump, which Sigma rules catch Kerberoasting, and how to scope a cloud breach across three providers. **Your AI agent doesn't — unless you give it these skills.**

This repo contains **754 structured cybersecurity skills** spanning **26 security domains**, each following the [agentskills.io](https://agentskills.io) open standard.  Every skill is mapped to **five industry frameworks** — MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, MITRE D3FEND, and NIST AI RMF  — making this the only open-source skills library with unified cross-framework coverage.  Clone it, point your agent at it, and your next security investigation gets expert-level guidance in seconds.

## Five frameworks, one skill library

No other open-source skills library maps every skill to all five frameworks.  One skill, five compliance checkboxes. 

| Framework | Version | Scope in this repo | What it maps |
|---|---|---|---|
| [MITRE ATT&CK](https://attack.mitre.org) | v18 | 14 tactics · 200+ techniques | Adversary behaviors and TTPs |
| [NIST CSF 2.0](https://www.nist.gov/cyberframework) | 2.0 | 6 functions · 22 categories | Organizational security posture |
| [MITRE ATLAS](https://atlas.mitre.org) | v5.4 | 16 tactics · 84 techniques | AI/ML adversarial threats |
| [MITRE D3FEND](https://d3fend.mitre.org) | v1.3 | 7 categories · 267 techniques | Defensive countermeasures |
| [NIST AI RMF](https://airc.nist.gov/AI_RMF) | 1.0 | 4 functions · 72 subcategories | AI risk management |

**Example — a single skill maps across all five:**

| Skill | ATT&CK | NIST CSF | ATLAS | D3FEND | AI RMF |
|---|---|---|---|---|---|
| `analyzing-network-traffic-of-malware` | T1071 | DE.CM | AML.T0047 | D3-NTA | MEASURE-2.6 |

## Quick start

```bash
# Option 1: npx (recommended)
npx skills add mukul975/Anthropic-Cybersecurity-Skills

# Option 2: Git clone
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills.git
cd Anthropic-Cybersecurity-Skills
```

Works immediately with Claude Code, GitHub Copilot, OpenAI Codex CLI, Cursor, Gemini CLI, and any [agentskills.io](https://agentskills.io)-compatible platform. 
## 🚀 Try it on the Playground

Experience Casky.ai hands-on — no setup required.

**[→ Launch Playground on Casky.ai](https://casky.ai/?utm_source=github&utm_medium=readme&utm_campaign=cohort_launch#waitlist)**

The playground lets you:
- Run live cybersecurity skill exercises against real targets
- See AI agents execute structured skills in real time
- Explore MITRE ATT&CK mapped workflows interactively
- Test threat hunting, DFIR, and penetration testing scenarios

No installation. No configuration. Just open and start.
## Why this exists

The cybersecurity workforce gap hit **4.8 million unfilled roles** globally in 2024 (ISC2). AI agents can help close that gap — but only if they have structured domain knowledge to work from. Today's agents can write code and search the web, but they lack the practitioner playbooks that turn a generic LLM into a capable security analyst.

Existing security tool repos give you wordlists, payloads, or exploit code. None of them give an AI agent the structured decision-making workflow a senior analyst follows: when to use each technique, what prerequisites to check, how to execute step-by-step, and how to verify results. That is the gap this project fills.

**Anthropic Cybersecurity Skills** is not a collection of scripts or checklists. It is an **AI-native knowledge base** built from the ground up for the agentskills.io standard  — YAML frontmatter for sub-second discovery, structured Markdown for step-by-step execution, and reference files for deep technical context.  Every skill encodes real practitioner workflows, not generated summaries. 

## What's inside — 26 security domains

| Domain | Skills | Key capabilities |
|---|---|---|
| Cloud Security | 60 | AWS, Azure, GCP hardening · CSPM · cloud forensics |
| Threat Hunting | 55 | Hypothesis-driven hunts · LOTL detection · behavioral analytics |
| Threat Intelligence | 50 | STIX/TAXII · MISP · feed integration · actor profiling |
| Web Application Security | 42 | OWASP Top 10 · SQLi · XSS · SSRF · deserialization |
| Network Security | 40 | IDS/IPS · firewall rules · VLAN segmentation · traffic analysis |
| Malware Analysis | 39 | Static/dynamic analysis · reverse engineering · sandboxing |
| Digital Forensics | 37 | Disk imaging · memory forensics · timeline reconstruction |
| Security Operations | 36 | SIEM correlation · log analysis · alert triage |
| Identity & Access Management | 35 | IAM policies · PAM · zero trust identity · Okta · SailPoint |
| SOC Operations | 33 | Playbooks · escalation workflows · metrics · tabletop exercises |
| Container Security | 30 | K8s RBAC · image scanning · Falco · container forensics |
| OT/ICS Security | 28 | Modbus · DNP3 · IEC 62443 · historian defense · SCADA |
| API Security | 28 | GraphQL · REST · OWASP API Top 10 · WAF bypass |
| Vulnerability Management | 25 | Nessus · scanning workflows · patch prioritization · CVSS |
| Incident Response | 25 | Breach containment · ransomware response · IR playbooks |
| Red Teaming | 24 | Full-scope engagements · AD attacks · phishing simulation |
| Penetration Testing | 23 | Network · web · cloud · mobile · wireless pentesting |
| Endpoint Security | 17 | EDR · LOTL detection · fileless malware · persistence hunting |
| DevSecOps | 17 | CI/CD security · code signing · Terraform auditing |
| Phishing Defense | 16 | Email authentication · BEC detection · phishing IR |
| Cryptography | 14 | TLS · Ed25519 · certificate transparency · key management |
| Zero Trust Architecture | 13 | BeyondCorp · CISA maturity model · microsegmentation |
| Mobile Security | 12 | Android/iOS analysis · mobile pentesting · MDM forensics |
| Ransomware Defense | 7 | Precursor detection · response · recovery · encryption analysis |
| Compliance & Governance | 5 | CIS benchmarks · SOC 2 · regulatory frameworks |
| Deception Technology | 2 | Honeytokens · breach detection canaries |

## How AI agents use these skills

Each skill costs **~30 tokens to scan** (frontmatter only)  and **500–2,000 tokens to fully load** (complete workflow). This progressive disclosure architecture lets agents search all 754 skills in a single pass without blowing context windows. 

```
User prompt: "Analyze this memory dump for signs of credential theft"

Agent's internal process:

  1. Scans 754 skill frontmatters (~30 tokens each)
     → identifies 12 relevant skills by matching tags, description, domain

  2. Loads top 3 matches:
     • performing-memory-forensics-with-volatility3
     • hunting-for-credential-dumping-lsass
     • analyzing-windows-event-logs-for-credential-access

  3. Executes the structured Workflow section step-by-step
     → runs Volatility3 plugins, checks LSASS access patterns,
        correlates with event log evidence

  4. Validates results using the Verification section
     → confirms IOCs, maps findings to ATT&CK T1003 (Credential Dumping)
```

**Without these skills**, the agent guesses at tool commands and misses critical steps. **With them**, it follows the same playbook a senior DFIR analyst would use. 

## Skill anatomy

Every skill follows a consistent directory structure:

```
skills/performing-memory-forensics-with-volatility3/
├── SKILL.md              ← Skill definition (YAML frontmatter + Markdown body)
├── references/
│   ├── standards.md      ← MITRE ATT&CK, ATLAS, D3FEND, NIST mappings
│   └── workflows.md      ← Deep technical procedure reference
├── 
