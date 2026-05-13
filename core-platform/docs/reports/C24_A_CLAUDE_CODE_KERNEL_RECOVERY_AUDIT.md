# C24-A Claude Code / Claw Code Kernel Recovery Audit

Generated at: Wed May 13 18:22:57 CST 2026

## 0. Purpose

Verify whether MAOMIAI Windows desktop currently uses the original Claude Code / Claw Code based agent architecture, or whether the desktop path has drifted into direct local model chat.

## 1. Expected Source Repositories

- https://github.com/CASTvivian/claw-code
- https://github.com/CASTvivian/claude-code-source-code

## 2. Git HEAD
bfdaabc feat: add runtime context router for chat grounding
4743166 docs: record final Windows package preflight
89bffc4 docs: add context engine research direction for brain upgrade
805601b feat: seed brain assets into repo memory
bc1ba78 data: compare stars with local repos and ingest missing summaries
53e9aba data: compare stars with local repos and ingest missing summaries
c6deaba data: add brain asset catalogs and starred repo ingestion
0070ba3 fix: pass Chinese prompt as utf8 base64 to Windows runtime
eb84212 fix: encode Windows runtime JSON output as utf8 base64 envelope
3b470b8 fix: make Windows bootstrap runtime ASCII only
e55621b fix: pass chat prompt via utf8 file and use ollama chat api
bf603b3 debug: add observable chat send pipeline for Windows inference

## 3. Find Local Claude / Claw Repositories
./AlphaAgent
./AlphaAgent/alphaagent
./AlphaAgent/alphaagent/utils/agent
./OpenHands/.agents
./OpenHands/.openhands/microagents
./OpenHands/openhands/agenthub
./OpenHands/openhands/agenthub/browsing_agent
./OpenHands/openhands/agenthub/codeact_agent
./OpenHands/openhands/agenthub/dummy_agent
./OpenHands/openhands/agenthub/loc_agent
./OpenHands/openhands/agenthub/readonly_agent
./OpenHands/openhands/agenthub/visualbrowsing_agent
./OpenHands/openhands/microagent
./OpenHands/openhands/runtime/plugins/agent_skills
./OpenHands/tests/unit/agenthub
./OpenHands/tests/unit/agenthub/browsing_agent
./OpenHands/tests/unit/microagent
./Qwen3-VL/cookbooks/assets/agent_function_call
./Qwen3-VL/cookbooks/assets/qwenagent
./andrej-karpathy-skills/.claude-plugin
./anything-llm/frontend/src/media/agents
./anything-llm/server/__tests__/utils/agentFlows
./anything-llm/server/__tests__/utils/agents
./anything-llm/server/utils/agentFlows
./anything-llm/server/utils/agents
./capability-registry/claude-code-best-practice
./capability-registry/claude-code-best-practice/.claude
./capability-registry/claude-code-best-practice/.claude/agent-memory
./capability-registry/claude-code-best-practice/.claude/agent-memory/weather-agent
./capability-registry/claude-code-best-practice/.claude/agents
./capability-registry/claude-code-best-practice/.claude/skills/agent-browser
./capability-registry/claude-code-best-practice/.codex
./capability-registry/claude-code-best-practice/agent-teams
./capability-registry/claude-code-best-practice/agent-teams/.claude
./capability-registry/claude-code-best-practice/agent-teams/.claude/agents
./capability-registry/claude-code-best-practice/best-practice/assets/claude-memory
./capability-registry/claude-code-best-practice/best-practice/assets/claude-power-ups
./capability-registry/claude-code-best-practice/changelog/best-practice/claude-commands
./capability-registry/claude-code-best-practice/changelog/best-practice/claude-settings
./capability-registry/claude-code-best-practice/changelog/best-practice/claude-skills
./capability-registry/claude-code-best-practice/changelog/best-practice/claude-subagents
./capability-registry/claude-code-best-practice/development-workflows/rpi/.claude
./capability-registry/claude-code-best-practice/presentation/vibe-coding-to-agentic-engineering
./capability-registry/gstack/agents
./capability-registry/gstack/codex
./capability-registry/gstack/openclaw
./capability-registry/gstack/openclaw/skills/gstack-openclaw-ceo-review
./capability-registry/gstack/openclaw/skills/gstack-openclaw-investigate
./capability-registry/gstack/openclaw/skills/gstack-openclaw-office-hours
./capability-registry/gstack/openclaw/skills/gstack-openclaw-retro
./capability-registry/gstack/pair-agent
./core-platform/data/agent_core_audit
./core-platform/data/agent_team
./core-platform/prompts/agent_team 2
./core-platform/services/agent_orchestrator
./core-platform/services/agent_runtime_service
./core-platform/services/code_agent
./langflow/.agents
./langflow/docs/docs/Agents
./langflow/docs/versioned_docs/version-1.8.0/Agents
./langflow/docs/versioned_docs/version-1.9.0/Agents
./references/500-AI-Agents-Projects
./references/Archon/.claude
./references/Archon/.claude/agents
./references/Archon/.claude/skills/agent-browser
./references/Archon/.github/agents
./references/AutoGPT/.agents
./references/AutoGPT/.claude
./references/AutoGPT/autogpt_platform/backend/agents
./references/AutoGPT/classic/original_autogpt/.claude
./references/BlenderMCP-AI-AGNO-agent
./references/CLI-Anything/.claude-plugin
./references/CLI-Anything/QGIS/agent-harness
./references/CLI-Anything/adguardhome/agent-harness
./references/CLI-Anything/anygen/agent-harness
./references/CLI-Anything/audacity/agent-harness
./references/CLI-Anything/blender/agent-harness
./references/CLI-Anything/browser/agent-harness
./references/CLI-Anything/chromadb/agent-harness
./references/CLI-Anything/cli-anything-plugin/.claude-plugin
./references/CLI-Anything/cloudanalyzer/agent-harness
./references/CLI-Anything/cloudcompare/agent-harness
./references/CLI-Anything/codex-skill
./references/CLI-Anything/codex-skill/agents
./references/CLI-Anything/comfyui/agent-harness
./references/CLI-Anything/dify-workflow/agent-harness
./references/CLI-Anything/drawio/agent-harness
./references/CLI-Anything/eth2-quickstart/agent-harness
./references/CLI-Anything/exa/agent-harness
./references/CLI-Anything/freecad/agent-harness
./references/CLI-Anything/gimp/agent-harness
./references/CLI-Anything/godot/agent-harness
./references/CLI-Anything/inkscape/agent-harness
./references/CLI-Anything/intelwatch/agent-harness
./references/CLI-Anything/iterm2/agent-harness
./references/CLI-Anything/kdenlive/agent-harness
./references/CLI-Anything/krita/agent-harness
./references/CLI-Anything/libreoffice/agent-harness
./references/CLI-Anything/lldb/agent-harness
./references/CLI-Anything/mermaid/agent-harness
./references/CLI-Anything/mubu/agent-harness
./references/CLI-Anything/musescore/agent-harness
./references/CLI-Anything/n8n/agent-harness
./references/CLI-Anything/notebooklm/agent-harness
./references/CLI-Anything/novita/agent-harness
./references/CLI-Anything/nsight-graphics/agent-harness
./references/CLI-Anything/obs-studio/agent-harness
./references/CLI-Anything/obsidian/agent-harness
./references/CLI-Anything/ollama/agent-harness
./references/CLI-Anything/openclaw-skill
./references/CLI-Anything/openclaw-skill/agent-harness
./references/CLI-Anything/openscreen/agent-harness
./references/CLI-Anything/pm2/agent-harness
./references/CLI-Anything/renderdoc/agent-harness
./references/CLI-Anything/rms/agent-harness
./references/CLI-Anything/safari/agent-harness
./references/CLI-Anything/seaclip/agent-harness
./references/CLI-Anything/shotcut/agent-harness
./references/CLI-Anything/sketch/agent-harness
./references/CLI-Anything/skills/cli-anything-openclaw
./references/CLI-Anything/slay_the_spire_ii/agent-harness
./references/CLI-Anything/unimol_tools/agent-harness
./references/CLI-Anything/unrealinsights/agent-harness
./references/CLI-Anything/videocaptioner/agent-harness
./references/CLI-Anything/wiremock/agent-harness
./references/CLI-Anything/zoom/agent-harness
./references/CLI-Anything/zotero/agent-harness
./references/CodexBar
./references/CodexBar/Sources/CodexBar
./references/CodexBar/Sources/CodexBarCLI
./references/CodexBar/Sources/CodexBarClaudeWatchdog
./references/CodexBar/Sources/CodexBarClaudeWebProbe
./references/CodexBar/Sources/CodexBarCore
./references/CodexBar/Sources/CodexBarMacroSupport
./references/CodexBar/Sources/CodexBarMacros
./references/CodexBar/Sources/CodexBarWidget
./references/CodexBar/Tests/CodexBarTests
./references/EvoSkill/.claude
./references/EvoSkill/src/agent_profiles
./references/EvoSkill/src/agent_profiles/base_agent
./references/EvoSkill/src/agent_profiles/dabstep_agent
./references/EvoSkill/src/agent_profiles/livecodebench_agent
./references/EvoSkill/src/agent_profiles/sealqa_agent
./references/EvoSkill/src/harness/claude
./references/EvoSkill/src/harness/codex
./references/Flowise/packages/agentflow
./references/GitTaskBench/OpenHands/.openhands/microagents
./references/GitTaskBench/OpenHands/microagents
./references/GitTaskBench/OpenHands/openhands/agenthub
./references/GitTaskBench/OpenHands/openhands/microagent
./references/GitTaskBench/SWE_agent
./references/GitTaskBench/SWE_agent/sweagent
./references/GitTaskBench/SWE_agent/sweagent/agent
./references/MinerU-Document-Explorer/.claude-plugin
./references/Open-AutoGLM/phone_agent
./references/OpenClaw_BlenderMCP-Skill
./references/OpenHands/.agents
./references/OpenHands/.openhands/microagents
./references/OpenHands/openhands/agenthub
./references/OpenHands/openhands/agenthub/browsing_agent
./references/OpenHands/openhands/agenthub/codeact_agent
./references/OpenHands/openhands/agenthub/dummy_agent
./references/OpenHands/openhands/agenthub/loc_agent
./references/OpenHands/openhands/agenthub/readonly_agent
./references/OpenHands/openhands/agenthub/visualbrowsing_agent
./references/OpenHands/openhands/microagent
./references/OpenHands/tests/unit/agenthub
./references/OpenHands/tests/unit/microagent
./references/OpenHarness/.agents
./references/OpenHarness/.claude
./references/RepoMaster/src/services/agents
./references/RepoMaster/src/utils/web_search_agent
./references/SWE-agent
./references/SWE-agent/config/sweagent_0_7
./references/SWE-agent/sweagent
./references/SWE-agent/sweagent/agent
./references/Seedance2-Storyboard-Generator/.claude
./references/SuperAGI/superagi/agent
./references/SuperAGI/tests/unit_tests/agent
./references/Toonflow-app-herooutput/backup/agents
./references/Toonflow-app-herooutput/src/agents
./references/Toonflow-app/src/agents
./references/Toonflow-app/src/agents/productionAgent
./references/Toonflow-app/src/agents/scriptAgent
./references/Toonflow-app/src/routes/agents
./references/Toonflow-app/src/routes/scriptAgent
./references/Toonflow-app/src/utils/agent
./references/Toonflow-web/src/views/scriptAgent
./references/agent-browser
./references/agent-browser/.claude-plugin
./references/agent-browser/skill-data/agentcore
./references/agent-browser/skills/agent-browser
./references/agent-skill-creator
./references/agent-skills-md
./references/agenta
./references/agenta/.claude
./references/agenta/.claude/agents
./references/agenta/agents
./references/agenta/hosting/helm/agenta-oss
./references/agenta/sdk/agenta
./references/agenta/web/packages/agenta-annotation
./references/agenta/web/packages/agenta-annotation-ui
./references/agenta/web/packages/agenta-entities
./references/agenta/web/packages/agenta-entity-ui
./references/agenta/web/packages/agenta-playground
./references/agenta/web/packages/agenta-playground-ui
./references/agenta/web/packages/agenta-shared
./references/agenta/web/packages/agenta-ui
./references/agentskills
./references/agi/agents
./references/ai-shotlive/.claude
./references/andrej-karpathy-skills/.claude-plugin
./references/antigravity-awesome-skills/.agents
./references/antigravity-awesome-skills/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-agent-architect
./references/antigravity-awesome-skills/plugins/antigravity-bundle-agent-architect/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-agent-architect/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-apple-platform-design/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-apple-platform-design/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-architecture-design/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-architecture-design/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-automation-builder/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-automation-builder/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-azure-ai-cloud/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-azure-ai-cloud/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-business-analyst/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-business-analyst/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-commerce-payments/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-commerce-payments/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-creative-director/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-creative-director/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-data-analytics/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-data-analytics/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-data-engineering/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-data-engineering/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-ddd-evented-architecture/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-ddd-evented-architecture/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-devops-cloud/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-devops-cloud/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-essentials/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-essentials/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-indie-game-dev/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-indie-game-dev/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-integration-apis/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-integration-apis/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-llm-application-developer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-llm-application-developer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-makepad-builder/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-makepad-builder/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-marketing-growth/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-marketing-growth/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-observability-monitoring/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-observability-monitoring/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-odoo-erp/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-odoo-erp/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-oss-maintainer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-oss-maintainer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-python-pro/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-python-pro/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-qa-testing/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-qa-testing/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-revops-crm-automation/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-revops-crm-automation/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-security-developer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-security-developer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-security-engineer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-security-engineer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-seo-specialist/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-seo-specialist/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-startup-founder/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-startup-founder/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-systems-programming/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-systems-programming/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-typescript-javascript/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-typescript-javascript/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-designer/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-designer/.codex-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-wizard/.claude-plugin
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-wizard/.codex-plugin
./references/antigravity-awesome-skills/skills/agent-evaluation
./references/antigravity-awesome-skills/skills/agent-framework-azure-ai-py
./references/antigravity-awesome-skills/skills/agent-manager-skill
./references/antigravity-awesome-skills/skills/agent-memory-mcp
./references/antigravity-awesome-skills/skills/agent-memory-systems
./references/antigravity-awesome-skills/skills/agent-orchestration-improve-agent
./references/antigravity-awesome-skills/skills/agent-orchestration-multi-agent-optimize
./references/antigravity-awesome-skills/skills/agent-orchestrator
./references/antigravity-awesome-skills/skills/agent-tool-builder
./references/antigravity-awesome-skills/skills/agentflow
./references/antigravity-awesome-skills/skills/agentfolio
./references/antigravity-awesome-skills/skills/agentic-actions-auditor
./references/antigravity-awesome-skills/skills/agentmail
./references/antigravity-awesome-skills/skills/agentphone
./references/antigravity-awesome-skills/skills/agents-md
./references/antigravity-awesome-skills/skills/agents-v2-py
./references/antigravity-awesome-skills/skills/ai-agent-development
./references/antigravity-awesome-skills/skills/ai-agents-architect
./references/antigravity-awesome-skills/skills/app-store-changelog/agents
./references/antigravity-awesome-skills/skills/autonomous-agent-patterns
./references/antigravity-awesome-skills/skills/autonomous-agents
./references/antigravity-awesome-skills/skills/azure-ai-agents-persistent-dotnet
./references/antigravity-awesome-skills/skills/azure-ai-agents-persistent-java
./references/antigravity-awesome-skills/skills/claude-ally-health
./references/antigravity-awesome-skills/skills/claude-api
./references/antigravity-awesome-skills/skills/claude-code-expert
./references/antigravity-awesome-skills/skills/claude-code-guide
./references/antigravity-awesome-skills/skills/claude-d3js-skill
./references/antigravity-awesome-skills/skills/claude-in-chrome-troubleshooting
./references/antigravity-awesome-skills/skills/claude-monitor
./references/antigravity-awesome-skills/skills/claude-scientific-skills
./references/antigravity-awesome-skills/skills/claude-settings-audit
./references/antigravity-awesome-skills/skills/claude-speed-reader
./references/antigravity-awesome-skills/skills/claude-win11-speckit-update-skill
./references/antigravity-awesome-skills/skills/codex-review
./references/antigravity-awesome-skills/skills/computer-use-agents
./references/antigravity-awesome-skills/skills/context-agent
./references/antigravity-awesome-skills/skills/crypto-bd-agent
./references/antigravity-awesome-skills/skills/dispatching-parallel-agents
./references/antigravity-awesome-skills/skills/error-debugging-multi-agent-review
./references/antigravity-awesome-skills/skills/ffuf-claude-skill
./references/antigravity-awesome-skills/skills/github/agents
./references/antigravity-awesome-skills/skills/global-chat-agent-discovery
./references/antigravity-awesome-skills/skills/hierarchical-agent-memory
./references/antigravity-awesome-skills/skills/hosted-agents
./references/antigravity-awesome-skills/skills/hosted-agents-v2-py
./references/antigravity-awesome-skills/skills/hugging-face-trackio/.claude-plugin
./references/antigravity-awesome-skills/skills/ios-debugger-agent
./references/antigravity-awesome-skills/skills/ios-debugger-agent/agents
./references/antigravity-awesome-skills/skills/lambdatest-agent-skills
./references/antigravity-awesome-skills/skills/linear-claude-skill
./references/antigravity-awesome-skills/skills/llm-application-dev-langchain-agent
./references/antigravity-awesome-skills/skills/m365-agents-dotnet
./references/antigravity-awesome-skills/skills/m365-agents-py
./references/antigravity-awesome-skills/skills/m365-agents-ts
./references/antigravity-awesome-skills/skills/macos-menubar-tuist-app/agents
./references/antigravity-awesome-skills/skills/macos-spm-app-packaging/agents
./references/antigravity-awesome-skills/skills/multi-agent-brainstorming
./references/antigravity-awesome-skills/skills/multi-agent-patterns
./references/antigravity-awesome-skills/skills/multi-agent-task-orchestrator
./references/antigravity-awesome-skills/skills/openclaw-github-repo-commander
./references/antigravity-awesome-skills/skills/orchestrate-batch-refactor/agents
./references/antigravity-awesome-skills/skills/parallel-agents
./references/antigravity-awesome-skills/skills/performance-testing-review-multi-agent-review
./references/antigravity-awesome-skills/skills/pipecat-friday-agent
./references/antigravity-awesome-skills/skills/project-skill-audit/agents
./references/antigravity-awesome-skills/skills/react-component-performance/agents
./references/antigravity-awesome-skills/skills/shadcn/agents
./references/antigravity-awesome-skills/skills/subagent-driven-development
./references/antigravity-awesome-skills/skills/swift-concurrency-expert/agents
./references/antigravity-awesome-skills/skills/swiftui-liquid-glass/agents
./references/antigravity-awesome-skills/skills/swiftui-performance-audit/agents
./references/antigravity-awesome-skills/skills/swiftui-ui-patterns/agents
./references/antigravity-awesome-skills/skills/swiftui-view-refactor/agents
./references/antigravity-awesome-skills/skills/varlock-claude-skill
./references/antigravity-awesome-skills/skills/voice-agents
./references/anything-llm/server/utils/agentFlows
./references/anything-llm/server/utils/agents
./references/autogen/dotnet/samples/AgentChat
./references/autogen/dotnet/test/Microsoft.AutoGen.AgentChat.Tests
./references/autogen/python/packages/autogen-agentchat
./references/autogen/python/packages/autogen-magentic-one
./references/autogen/python/packages/magentic-one-cli
./references/autogen/python/samples/agentchat_azure_postgresql
./references/autogen/python/samples/agentchat_chainlit
./references/autogen/python/samples/agentchat_chess_game
./references/autogen/python/samples/agentchat_dspy
./references/autogen/python/samples/agentchat_fastapi
./references/autogen/python/samples/agentchat_graphrag
./references/autogen/python/samples/agentchat_streamlit
./references/autogen/python/samples/core_xlang_hello_python_agent
./references/awesome-ai-agents
./references/awesome-design-md-pre-paywall/design-md/claude
./references/awesome-design-md-pre-paywall/design-md/voltagent
./references/awesome-design-md-skye/design-md/claude
./references/awesome-design-md-skye/design-md/voltagent
./references/awesome-design-md/design-md/claude
./references/awesome-design-md/design-md/voltagent
./references/big-AGI/.claude
./references/browser-use/browser_use/agent
./references/browser-use/examples/integrations/agentmail
./references/browser-use/tests/agent_tasks
./references/camel/apps/agents
./references/camel/camel/agents
./references/camel/camel/agents/tool_agents
./references/camel/camel/types/agents
./references/camel/docs/cookbooks/multi_agent_society
./references/camel/examples/agents
./references/camel/examples/agents/mcp_agent
./references/camel/examples/deductive_reasoner_agent
./references/camel/examples/usecases/multi_agent_research_assistant
./references/camel/services/agent_mcp
./references/camel/test/agents
./references/camel/test/agents/tool_agents
./references/ccusage/.claude
./references/ccusage/.codex
./references/ccusage/apps/codex
./references/ccusage/docs/guide/codex
./references/claude-code-local
./references/claude-howto
./references/claude-howto/.claude
./references/claude-howto/03-skills/claude-md
./references/claude-howto/04-subagents
./references/claude-howto/07-plugins/devops-automation/.claude-plugin
./references/claude-howto/07-plugins/devops-automation/agents
./references/claude-howto/07-plugins/documentation/.claude-plugin
./references/claude-howto/07-plugins/documentation/agents
./references/claude-howto/07-plugins/pr-review/.claude-plugin
./references/claude-howto/07-plugins/pr-review/agents
./references/claude-howto/uk/03-skills/claude-md
./references/claude-howto/uk/04-subagents
./references/claude-howto/vi/03-skills/claude-md
./references/claude-howto/vi/04-subagents
./references/claude-howto/zh/03-skills/claude-md
./references/claude-howto/zh/04-subagents
./references/claude-memory-compiler
./references/claude-memory-compiler/.claude
./references/cline/.agents
./references/cline/.claude
./references/cline/.codex
./references/cline/cli/src/agent
./references/cline/src/integrations/claude-code
./references/cline/src/integrations/openai-codex
./references/continue/.claude
./references/continue/.continue/agents
./references/continue/docs/agents
./references/continue/docs/guides/cloud-agents
./references/continue/docs/ide-extensions/agent
./references/crawl4ai/.claude
./references/deer-flow/.agent
./references/deer-flow/skills/public/claude-to-deerflow
./references/dify/.agents
./references/dify/.claude
./references/dify/api/core/agent
./references/everything-claude-code
./references/everything-claude-code/.agents
./references/everything-claude-code/.agents/skills/agent-introspection-debugging
./references/everything-claude-code/.agents/skills/agent-sort
./references/everything-claude-code/.agents/skills/claude-api
./references/everything-claude-code/.agents/skills/everything-claude-code
./references/everything-claude-code/.claude
./references/everything-claude-code/.claude-plugin
./references/everything-claude-code/.claude/skills/everything-claude-code
./references/everything-claude-code/.codex
./references/everything-claude-code/.codex-plugin
./references/everything-claude-code/.codex/agents
./references/everything-claude-code/.kiro/agents
./references/everything-claude-code/.kiro/skills/agentic-engineering
./references/everything-claude-code/.opencode/prompts/agents
./references/everything-claude-code/agents
./references/everything-claude-code/docs/ja-JP/agents
./references/everything-claude-code/docs/ko-KR/agents
./references/everything-claude-code/docs/pt-BR/agents
./references/everything-claude-code/docs/tr/agents
./references/everything-claude-code/docs/zh-CN/agents
./references/everything-claude-code/docs/zh-TW/agents
./references/everything-claude-code/scripts/codex
./references/everything-claude-code/scripts/codex-git-hooks
./references/everything-claude-code/skills/agent-eval
./references/everything-claude-code/skills/agent-harness-construction
./references/everything-claude-code/skills/agent-introspection-debugging
./references/everything-claude-code/skills/agent-payment-x402
./references/everything-claude-code/skills/agent-sort
./references/everything-claude-code/skills/agentic-engineering
./references/everything-claude-code/skills/autonomous-agent-harness
./references/everything-claude-code/skills/claude-api
./references/everything-claude-code/skills/claude-devfleet
./references/everything-claude-code/skills/continuous-agent-loop
./references/everything-claude-code/skills/continuous-learning-v2/agents
./references/everything-claude-code/skills/data-scraper-agent
./references/everything-claude-code/skills/enterprise-agent-ops
./references/everything-claude-code/skills/lead-intelligence/agents
./references/everything-claude-code/skills/llm-trading-agent-security
./references/everything-claude-code/skills/nanoclaw-repl
./references/everything-claude-code/skills/openclaw-persona-forge
./references/firecrawl/examples/claude-3.7-stock-analyzer
./references/firecrawl/examples/claude3.7-web-crawler
./references/firecrawl/examples/claude3.7-web-extractor
./references/firecrawl/examples/claude_stock_analyzer
./references/firecrawl/examples/simple_web_data_extraction_with_claude
./references/get-shit-done/agents
./references/get-shit-done/sdk/prompts/agents
./references/giskard/libs/giskard-agents
./references/godogen/claude
./references/godogen/codex
./references/gpt_academic/crazy_functions/agent_fns
./references/gpt_academic/docs/features/agents
./references/happy-cli/src/agent
./references/happy-cli/src/claude
./references/happy-cli/src/codex
./references/haystack/haystack/components/agents
./references/haystack/test/components/agents
./references/hello-agents
./references/hello-agents/Co-creation-projects/1zrj-DataAnalysisAgent
./references/hello-agents/Co-creation-projects/Apricity-InnocoreAI/agents
./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent
./references/hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/.helloagents
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/agents
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/code_agent
./references/hello-agents/Co-creation-projects/Yixiang-Wu-LearningAgent
./references/hello-agents/Co-creation-projects/Yixiang-Wu-LearningAgent/agents
./references/hello-agents/Co-creation-projects/alexrunner-DataAnalysisAgent
./references/hello-agents/Co-creation-projects/alexrunner-DataAnalysisAgent/agents
./references/hello-agents/Co-creation-projects/czxgg0630-ProductAnalysisAgent
./references/hello-agents/Co-creation-projects/haoye2-UnivesalAgent
./references/hello-agents/Co-creation-projects/healer-666-Academic-Data-Agent
./references/hello-agents/Co-creation-projects/jack6249-GiftGeniusAgent
./references/hello-agents/Co-creation-projects/jjyaoao-CodeReviewAgent
./references/hello-agents/Co-creation-projects/kkkano-FinReportAgent
./references/hello-agents/Co-creation-projects/lgs-only-NovelGenerator/agents
./references/hello-agents/Co-creation-projects/lll0807-CodeTutorAgent
./references/hello-agents/Co-creation-projects/megg-ops-roleplay_agent
./references/hello-agents/Co-creation-projects/meiguanxiHXX-historyReviewAgent
./references/hello-agents/Co-creation-projects/pamdla-MindEchoAgent
./references/hello-agents/Co-creation-projects/tino-chen-HelloClaw
./references/hello-agents/code/chapter13/helloagents-trip-planner
./references/hello-agents/code/chapter14/helloagents-deepresearch
./references/hello-agents/code/chapter15/Helloagents-AI-Town
./references/hello-agents/code/chapter6/AgentScopeDemo
./references/hermes-agent
./references/hermes-agent/agent
./references/hermes-agent/optional-skills/autonomous-ai-agents
./references/hermes-agent/optional-skills/email/agentmail
./references/hermes-agent/optional-skills/migration/openclaw-migration
./references/hermes-agent/skills/autonomous-ai-agents
./references/hermes-agent/skills/autonomous-ai-agents/claude-code
./references/hermes-agent/skills/autonomous-ai-agents/codex
./references/hermes-agent/skills/autonomous-ai-agents/hermes-agent
./references/hermes-agent/skills/software-development/subagent-driven-development
./references/hermes-agent/tests/agent
./references/hermes-agent/tests/run_agent
./references/hyperframes/.claude
./references/inference-gateway/examples/kubernetes/agent
./references/judgeval/examples/claude-agent-sdk
./references/langflow/.agents
./references/langflow/docs/docs/Agents
./references/langfuse/.agents
./references/langfuse/.agents/skills/agent-setup-maintenance
./references/langfuse/scripts/agents
./references/langfuse/scripts/codex
./references/langfuse/web/.agents
./references/langgraph/examples/multi_agent
./references/langgraph/libs/prebuilt/.claude
./references/learn-claude-code
./references/learn-claude-code/agents
./references/learn-claude-code/skills/agent-builder
./references/litellm/cookbook/ai_coding_tool_guides/claude_code_quickstart
./references/litellm/cookbook/anthropic_agent_sdk
./references/litellm/cookbook/gollem_go_agent_framework
./references/litellm/cookbook/livekit_agent_sdk
./references/litellm/litellm/integrations/agentops
./references/litellm/litellm/integrations/litellm_agent
./references/litellm/litellm/proxy/agent_endpoints
./references/litellm/tests/agent_tests
./references/litellm/tests/agent_tests/local_only_agent_tests
./references/llama_index/docs/examples/agent
./references/llama_index/llama-index-core/tests/agent
./references/llama_index/llama-index-core/tests/voice_agents
./references/llama_index/llama-index-integrations/agent
./references/llama_index/llama-index-integrations/agent/llama-index-agent-agentmesh
./references/llama_index/llama-index-integrations/agent/llama-index-agent-azure
./references/llama_index/llama-index-integrations/callbacks/llama-index-callbacks-agentops
./references/llama_index/llama-index-integrations/memory/llama-index-memory-bedrock-agentcore
./references/llama_index/llama-index-integrations/readers/llama-index-readers-agent-search
./references/llama_index/llama-index-integrations/tools/llama-index-tools-agentql
./references/llama_index/llama-index-integrations/tools/llama-index-tools-aws-bedrock-agentcore
./references/llama_index/llama-index-integrations/voice_agents
./references/llama_index/llama-index-integrations/voice_agents/llama-index-voice-agents-elevenlabs
./references/llama_index/llama-index-integrations/voice_agents/llama-index-voice-agents-gemini-live
./references/llama_index/llama-index-integrations/voice_agents/llama-index-voice-agents-openai
./references/lobe-chat/.agents
./references/lobe-chat/.agents/skills/agent-tracing
./references/lobe-chat/.claude
./references/lobe-chat/.codex
./references/lobe-chat/docs/usage/agent
./references/lobe-chat/packages/agent-gateway-client
./references/lobe-chat/packages/agent-manager-runtime
./references/lobe-chat/packages/agent-runtime
./references/lobe-chat/packages/agent-templates
./references/lobe-chat/packages/agent-tracing
./references/lobe-chat/packages/builtin-agents
./references/lobe-chat/packages/builtin-tool-agent-builder
./references/lobe-chat/packages/builtin-tool-agent-documents
./references/lobe-chat/packages/builtin-tool-agent-management
./references/lobe-chat/packages/builtin-tool-group-agent-builder
./references/lobe-chat/packages/builtin-tool-page-agent
./references/lobe-chat/src/features/AgentBuilder
./references/lobe-chat/src/features/AgentGroupAvatar
./references/lobe-chat/src/features/AgentHome
./references/lobe-chat/src/features/AgentInfo
./references/lobe-chat/src/features/AgentSetting
./references/lobe-chat/src/features/AgentSkillDetail
./references/lobe-chat/src/features/AgentSkillEdit
./references/lobe-chat/src/services/agentRuntime
./references/lobe-chat/src/store/agent
./references/lobe-chat/src/store/agentGroup
./references/localai/.agents
./references/localai/.github/gallery-agent
./references/localai/core/services/agentpool
./references/localai/core/services/agents
./references/marketingskills/.claude-plugin
./references/mem0/.agents
./references/mem0/.claude-plugin
./references/mem0/examples/multiagents
./references/mem0/examples/nemoclaw
./references/mem0/mem0-plugin/.claude-plugin
./references/mem0/mem0-plugin/.codex-plugin
./references/mem0/mem0-plugin/skills/mem0-codex
./references/mem0/openclaw
./references/multica/packages/views/agents
./references/multica/server/pkg/agent
./references/oh-my-codex
./references/oh-my-codex/skills/ask-claude
./references/oh-my-codex/src/agents
./references/oh-my-codex/src/openclaw
./references/oh-my-codex/src/subagents
./references/ollama/x/agent
./references/openOii/backend/app/agents
./references/openOii/backend/tests/test_agents
./references/openai-codex
./references/openai-codex-plugin-cc
./references/openai-codex-plugin-cc/.claude-plugin
./references/openai-codex-plugin-cc/plugins/codex
./references/openai-codex-plugin-cc/plugins/codex/.claude-plugin
./references/openai-codex-plugin-cc/plugins/codex/agents
./references/openai-codex/.codex
./references/openai-codex/.codex/skills/codex-bug
./references/openai-codex/.codex/skills/codex-pr-body
./references/openai-codex/.github/codex
./references/openai-codex/codex-cli
./references/openai-codex/codex-rs
./references/openai-codex/codex-rs/agent-identity
./references/openai-codex/codex-rs/codex-api
./references/openai-codex/codex-rs/codex-backend-openapi-models
./references/openai-codex/codex-rs/codex-client
./references/openai-codex/codex-rs/codex-experimental-api-macros
./references/openai-codex/codex-rs/codex-mcp
./references/openclaw
./references/openclaw/.agents
./references/openclaw/.agents/skills/openclaw-ghsa-maintainer
./references/openclaw/.agents/skills/openclaw-parallels-smoke
./references/openclaw/.agents/skills/openclaw-pr-maintainer
./references/openclaw/.agents/skills/openclaw-qa-testing
./references/openclaw/.agents/skills/openclaw-release-maintainer
./references/openclaw/.agents/skills/openclaw-secret-scanning-maintainer
./references/openclaw/.agents/skills/openclaw-test-heap-leaks
./references/openclaw/.agents/skills/openclaw-test-performance
./references/openclaw/.github/codex
./references/openclaw/apps/shared/OpenClawKit
./references/openclaw/extensions/codex
./references/openclaw/qa/scenarios/agents
./references/openclaw/scripts/clawdock
./references/openclaw/skills/clawhub
./references/openclaw/skills/coding-agent
./references/openclaw/src/agents
./references/openclaw/src/commands/agent
./references/openclaw/src/cron/isolated-agent
./references/openclaw/test/helpers/agents
./references/openllmetry/packages/opentelemetry-instrumentation-openai-agents
./references/opik/.agents
./references/opik/.agents/agents
./references/opik/.claude
./references/phoenix/.agents
./references/phoenix/.agents/skills/agent-browser
./references/phoenix/.claude
./references/phoenix/.codex
./references/phoenix/app/src/agent
./references/phoenix/examples/agent_framework_comparison
./references/phoenix/examples/agent_framework_comparison/autogen_multi_agent
./references/phoenix/examples/agent_framework_comparison/code_based_agent
./references/phoenix/examples/agent_framework_comparison/crewai_multi_agent
./references/phoenix/examples/agents
./references/phoenix/examples/agents/tau_bench_openai_agents
./references/phoenix/examples/code_gen_agent
./references/phoenix/examples/computer_use_agent
./references/phoenix/examples/llamaindex-workflows-research-agent
./references/phoenix/examples/rag_agent
./references/phoenix/tutorials/agents
./references/phoenix/tutorials/agents/smolagents
./references/promptfoo/.agents
./references/promptfoo/.claude
./references/promptfoo/.claude-plugin
./references/promptfoo/docs/agents
./references/promptfoo/examples/amazon-bedrock/agents
./references/promptfoo/examples/anthropic/claude-code-session
./references/promptfoo/examples/azure/claude
./references/promptfoo/examples/azure/foundry-agent
./references/promptfoo/examples/claude-agent-sdk
./references/promptfoo/examples/claude-thinking
./references/promptfoo/examples/claude-vision
./references/promptfoo/examples/compare-agentic-sdks
./references/promptfoo/examples/compare-claude-vs-gpt
./references/promptfoo/examples/compare-claude-vs-gpt-image
./references/promptfoo/examples/compare-gpt-vs-claude-vs-gemini
./references/promptfoo/examples/integration-google-adk/weather_agent
./references/promptfoo/examples/integration-strands-agents
./references/promptfoo/examples/openai-agents
./references/promptfoo/examples/openai-agents-basic
./references/promptfoo/examples/openai-agents-basic/agents
./references/promptfoo/examples/openai-codex-app-server
./references/promptfoo/examples/openai-codex-sdk
./references/promptfoo/examples/provider-elevenlabs/agents
./references/promptfoo/examples/provider-openclaw
./references/promptfoo/examples/redteam-coding-agent
./references/promptfoo/examples/redteam-mcp-agent
./references/promptfoo/examples/redteam-medical-agent
./references/promptfoo/examples/redteam-travel-agent
./references/promptfoo/plugins/promptfoo-evals/.claude-plugin
./references/promptfoo/plugins/promptfoo/.codex-plugin
./references/promptfoo/src/providers/openclaw
./references/promptfoo/src/util/agent
./references/promptfoo/test/agentSkills
./references/promptfoo/test/fixtures/agent-skills
./references/promptfoo/test/util/agent
./references/pskoett-ai-skills/.agents
./references/pskoett-ai-skills/.agents/skills/intent-framed-agent
./references/pskoett-ai-skills/.claude-plugin
./references/pskoett-ai-skills/plugin/.claude-plugin
./references/pskoett-ai-skills/plugin/.codex-plugin
./references/pskoett-ai-skills/plugin/.copilot-plugin/agents
./references/pskoett-ai-skills/plugin/agents
./references/pskoett-ai-skills/plugin/skills/agent-teams-simplify-and-harden
./references/pskoett-ai-skills/plugin/skills/intent-framed-agent
./references/pskoett-ai-skills/skills/agent-teams-simplify-and-harden
./references/pskoett-ai-skills/skills/intent-framed-agent
./references/ragflow/.agents
./references/ragflow/agent
./references/ragflow/docs/guides/agent
./references/ragflow/web/.agents
./references/ruoyi-admin/apps/web-antd/.claude
./references/self-improving-agent
./references/self-improving-agent/hooks/openclaw
./references/sglang/.claude
./references/sglang/benchmark/generative_agents
./references/sim/.agents
./references/sim/.claude
./references/skyvern/.claude
./references/supermemory/packages/agent-framework-python
./references/tabby/clients/tabby-agent
./references/vision-agent
./references/vision-agent/vision_agent
./references/vision-agent/vision_agent/agent

## 4. Local Git Remotes Related to Claude / Claw
- .
  - origin: https://github.com/CASTvivian/local-ai-platform.git
- ./capability-registry/claude-code-best-practice
  - origin: https://github.com/shanraisshan/claude-code-best-practice.git
- ./core-platform/data/brain_assets/repos/github_stars/affaan-m__everything-claude-code
  - origin: https://github.com/affaan-m/everything-claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars/shareAI-lab__learn-claude-code
  - origin: https://github.com/shareAI-lab/learn-claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/CASTvivian__chenzaikuaipao.io
  - origin: https://github.com/CASTvivian/chenzaikuaipao.io.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/T-Lab-CUHKSZ__claude-code
  - origin: https://github.com/T-Lab-CUHKSZ/claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/VoltAgent__awesome-claude-design
  - origin: https://github.com/VoltAgent/awesome-claude-design.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/affaan-m__everything-claude-code
  - origin: https://github.com/affaan-m/everything-claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/claude-code-best__claude-code
  - origin: https://github.com/claude-code-best/claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/coleam00__claude-memory-compiler
  - origin: https://github.com/coleam00/claude-memory-compiler.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/luongnv89__claude-howto
  - origin: https://github.com/luongnv89/claude-howto.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/nicedreamzapp__claude-code-local
  - origin: https://github.com/nicedreamzapp/claude-code-local.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/oboard__claude-code-rev
  - origin: https://github.com/oboard/claude-code-rev.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/openclaw__openclaw
  - origin: https://github.com/openclaw/openclaw.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/shanraisshan__claude-code-best-practice
  - origin: https://github.com/shanraisshan/claude-code-best-practice.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/shareAI-lab__learn-claude-code
  - origin: https://github.com/shareAI-lab/learn-claude-code.git
- ./core-platform/data/brain_assets/repos/github_stars_missing/ultraworkers__claw-code
  - origin: https://github.com/ultraworkers/claw-code.git
- ./references/claude-howto
  - origin: https://github.com/luongnv89/claude-howto
- ./references/everything-claude-code
  - origin: https://github.com/affaan-m/everything-claude-code.git
- ./references/learn-claude-code
  - origin: https://github.com/shareAI-lab/learn-claude-code.git

## 5. Agent Kernel Files
./OpenHands/enterprise/storage/saas_conversation_validator.py
./OpenHands/openhands/storage/conversation/conversation_validator.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/run_agent/test_tool_executor_contextvar_propagation.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tools/approval.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/code_executor.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dict.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dynamic_fields.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_execution_mode.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_responses_api.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_tool_dedup.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator_test.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/backend/test/agent_generator/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/classic/forge/forge/components/code_executor/code_executor.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/classic/forge/forge/components/code_executor/test_code_executor.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/classic/forge/forge/utils/test_url_validator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/classic/forge/forge/utils/url_validator.py
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/classic/original_autogpt/autogpt/app/settings/validators.py
./core-platform/data/brain_assets/repos/github_stars/TransformerOptimus__SuperAGI/superagi/agent/tool_executor.py
./core-platform/data/brain_assets/repos/github_stars/TransformerOptimus__SuperAGI/superagi/jobs/agent_executor.py
./core-platform/data/brain_assets/repos/github_stars/TransformerOptimus__SuperAGI/superagi/jobs/scheduling_executor.py
./core-platform/data/brain_assets/repos/github_stars/TransformerOptimus__SuperAGI/tests/unit_tests/agent/test_tool_executor.py
./core-platform/data/brain_assets/repos/github_stars/TransformerOptimus__SuperAGI/tests/unit_tests/jobs/test_scheduling_executor.py
./core-platform/data/brain_assets/repos/github_stars/affaan-m__everything-claude-code/src/llm/tools/executor.py
./core-platform/data/brain_assets/repos/github_stars/affaan-m__everything-claude-code/tests/test_executor.py
./core-platform/data/brain_assets/repos/github_stars/bytedance__deer-flow/backend/packages/harness/deerflow/subagents/executor.py
./core-platform/data/brain_assets/repos/github_stars/bytedance__deer-flow/backend/tests/test_subagent_executor.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/Apricity-InnocoreAI/agents/validator.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/code_agent/executors/apply_patch_executor.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/tools/async_executor.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/meiguanxiHXX-historyReviewAgent/historical_review/debate_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/melxy1997-ColumnWriter/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/usernamedadad-AutoFlow/backend/app/tools/mermaid_validator_tool.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/xujikai-SentenceExpandAgent/backend/src/agents/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars/safishamsi__graphify/worked/example/raw/validator.py
./core-platform/data/brain_assets/repos/github_stars/sansan0__TrendRadar/mcp_server/utils/validators.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/slack-gif-creator/core/validators.py
./core-platform/data/brain_assets/repos/github_stars/zhouxiaoka__autoclip/backend/services/processing_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/actions/orchestrator_hub.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/env_interaction/command_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/env_interaction/turn_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/orchestrator_agent.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/orchestrator_agent_stateful.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/state/orchestrator_state.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/src/multi_agent_coding_system/agents/tbench_orchestrator_agent.py
./core-platform/data/brain_assets/repos/github_stars_missing/Danau5tin__multi-agent-coding-system/tests/test_orchestrator_real.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__CLI-Anything/eth2-quickstart/agent-harness/cli_anything/eth2_quickstart/core/validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__CLI-Anything/sbox/agent-harness/cli_anything/sbox/core/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__CLI-Anything/sbox/agent-harness/cli_anything/sbox/tests/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/src/openharness/hooks/executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/src/openharness/sandbox/path_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/tests/test_hooks/test_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/tests/test_sandbox/test_path_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/K-Dense-AI__scientific-agent-skills/scientific-skills/clinical-reports/scripts/terminology_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/run_agent/test_tool_executor_contextvar_propagation.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tools/approval.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/code_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dict.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dynamic_fields.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_execution_mode.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_responses_api.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_tool_dedup.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator_test.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/backend/test/agent_generator/test_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/classic/forge/forge/components/code_executor/code_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/classic/forge/forge/components/code_executor/test_code_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/classic/forge/forge/utils/test_url_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/classic/forge/forge/utils/url_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/classic/original_autogpt/autogpt/app/settings/validators.py
./core-platform/data/brain_assets/repos/github_stars_missing/TransformerOptimus__SuperAGI/superagi/agent/tool_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/TransformerOptimus__SuperAGI/superagi/jobs/agent_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/TransformerOptimus__SuperAGI/superagi/jobs/scheduling_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/TransformerOptimus__SuperAGI/tests/unit_tests/agent/test_tool_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/TransformerOptimus__SuperAGI/tests/unit_tests/jobs/test_scheduling_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/affaan-m__everything-claude-code/src/llm/tools/executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/affaan-m__everything-claude-code/tests/test_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/agentskills__agentskills/skills-ref/src/skills_ref/validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/agentskills__agentskills/skills-ref/tests/test_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/anthropics__skills/skills/slack-gif-creator/core/validators.py
./core-platform/data/brain_assets/repos/github_stars_missing/bytedance__deer-flow/backend/packages/harness/deerflow/subagents/executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/bytedance__deer-flow/backend/tests/test_subagent_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/Apricity-InnocoreAI/agents/validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/code_agent/executors/apply_patch_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/tools/async_executor.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/meiguanxiHXX-historyReviewAgent/historical_review/debate_orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/melxy1997-ColumnWriter/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/usernamedadad-AutoFlow/backend/app/tools/mermaid_validator_tool.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/xujikai-SentenceExpandAgent/backend/src/agents/orchestrator.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/src/parlant/core/engines/alpha/planners.py
./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/tests/sdk/test_planners.py
./core-platform/data/brain_assets/repos/github_stars_missing/marketcalls__openalgo/services/flow_executor_service.py
./core-platform/data/brain_assets/repos/github_stars_missing/openai__codex/sdk/python/tests/test_app_server_approvals.py
./core-platform/data/brain_assets/repos/github_stars_missing/safishamsi__graphify/worked/example/raw/validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sansan0__TrendRadar/mcp_server/utils/validators.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/slack-gif-creator/core/validators.py
./core-platform/data/brain_assets/repos/github_stars_missing/soxoj__maigret/maigret/executors.py
./core-platform/data/brain_assets/repos/github_stars_missing/soxoj__maigret/tests/test_executors.py
./core-platform/data/brain_assets/repos/github_stars_missing/zhouxiaoka__autoclip/backend/services/processing_orchestrator.py
./core-platform/services/agent_runtime_service/app/executor.py
./core-platform/services/agent_runtime_service/app/planner.py
./core-platform/services/agent_runtime_service/app/validator.py
./langflow/scripts/test_validator.py
./langflow/src/backend/base/langflow/agentic/services/flow_executor.py
./langflow/src/backend/base/langflow/alembic/migration_validator.py
./langflow/src/backend/base/langflow/inputs/validators.py
./langflow/src/backend/base/langflow/schema/validators.py
./langflow/src/backend/tests/unit/agentic/services/test_flow_executor.py
./langflow/src/backend/tests/unit/alembic/test_migration_validator.py
./langflow/src/backend/tests/unit/components/bundles/google/test_google_bq_sql_executor_component.py
./langflow/src/backend/tests/unit/components/data_source/test_sql_executor.py
./langflow/src/lfx/src/lfx/components/data_source/sql_executor.py
./langflow/src/lfx/src/lfx/components/google/google_bq_sql_executor.py
./langflow/src/lfx/src/lfx/components/langchain_utilities/runnable_executor.py
./langflow/src/lfx/src/lfx/inputs/validators.py
./langflow/src/lfx/src/lfx/schema/validators.py
./qlib/qlib/backtest/executor.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/code_executor.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/orchestrator.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dict.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_dynamic_fields.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_execution_mode.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_per_iteration_cost.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_responses_api.py
./references/AutoGPT/autogpt_platform/backend/backend/blocks/test/test_orchestrator_tool_dedup.py
./references/AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator.py
./references/AutoGPT/autogpt_platform/backend/backend/copilot/tools/agent_generator/validator_test.py
./references/AutoGPT/autogpt_platform/backend/test/agent_generator/test_orchestrator.py
./references/AutoGPT/classic/forge/forge/components/code_executor/code_executor.py
./references/AutoGPT/classic/forge/forge/components/code_executor/test_code_executor.py
./references/AutoGPT/classic/forge/forge/utils/test_url_validator.py
./references/AutoGPT/classic/forge/forge/utils/url_validator.py
./references/AutoGPT/classic/original_autogpt/autogpt/app/settings/validators.py
./references/CLI-Anything/eth2-quickstart/agent-harness/cli_anything/eth2_quickstart/core/validator.py
./references/EvoSkill/src/harness/claude/executor.py
./references/EvoSkill/src/harness/codex/executor.py
./references/EvoSkill/src/harness/goose/executor.py
./references/EvoSkill/src/harness/opencode/executor.py
./references/EvoSkill/src/harness/openhands/executor.py
./references/GitTaskBench/OpenHands/openhands/storage/conversation/conversation_validator.py
./references/GitTaskBench/code_base/Faker/faker/sphinx/validator.py
./references/GitTaskBench/code_base/Faker/tests/sphinx/test_validator.py
./references/OpenHands/enterprise/storage/saas_conversation_validator.py
./references/OpenHands/openhands/storage/conversation/conversation_validator.py
./references/OpenHarness/src/openharness/hooks/executor.py
./references/OpenHarness/src/openharness/sandbox/path_validator.py
./references/OpenHarness/tests/test_hooks/test_executor.py
./references/OpenHarness/tests/test_sandbox/test_path_validator.py
./references/RepoMaster/src/core/agent_docker_executor.py
./references/SuperAGI/superagi/agent/tool_executor.py
./references/SuperAGI/superagi/jobs/agent_executor.py
./references/SuperAGI/superagi/jobs/scheduling_executor.py
./references/SuperAGI/tests/unit_tests/agent/test_tool_executor.py
./references/SuperAGI/tests/unit_tests/jobs/test_scheduling_executor.py
./references/TrendRadar/mcp_server/utils/validators.py
./references/agenta/api/oss/src/utils/validators.py
./references/agenta/api/oss/tests/pytest/unit/auth/test_validators.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/api-patterns/scripts/api_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/database-design/scripts/schema_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/api-patterns/scripts/api_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/database-design/scripts/schema_validator.py
./references/antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
./references/antigravity-awesome-skills/skills/api-patterns/scripts/api_validator.py
./references/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
./references/antigravity-awesome-skills/skills/database-design/scripts/schema_validator.py
./references/antigravity-awesome-skills/skills/slack-gif-creator/core/validators.py
./references/autoclip/backend/services/processing_orchestrator.py
./references/autogen/python/packages/agbench/benchmarks/HumanEval/Templates/AgentChat/custom_code_executor.py
./references/autogen/python/packages/autogen-agentchat/src/autogen_agentchat/agents/_code_executor_agent.py
./references/autogen/python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/_magentic_one/_magentic_one_orchestrator.py
./references/autogen/python/packages/autogen-agentchat/tests/test_code_executor_agent.py
./references/autogen/python/packages/autogen-core/tests/test_code_executor.py
./references/autogen/python/packages/autogen-ext/src/autogen_ext/code_executors/azure/_azure_container_code_executor.py
./references/autogen/python/packages/autogen-ext/src/autogen_ext/code_executors/docker/_docker_code_executor.py
./references/autogen/python/packages/autogen-ext/src/autogen_ext/code_executors/jupyter/_jupyter_code_executor.py
./references/autogen/python/packages/autogen-ext/tests/code_executors/test_commandline_code_executor.py
./references/autogen/python/packages/autogen-ext/tests/code_executors/test_docker_commandline_code_executor.py
./references/autogen/python/packages/autogen-ext/tests/code_executors/test_docker_jupyter_code_executor.py
./references/autogen/python/packages/autogen-ext/tests/code_executors/test_jupyter_code_executor.py
./references/autogen/python/packages/autogen-ext/tests/tools/test_python_code_executor_tool.py
./references/autogen/python/packages/autogen-studio/autogenstudio/eval/orchestrator.py
./references/crawl4ai/crawl4ai/cache_validator.py
./references/crewAI/lib/crewai-files/src/crewai_files/processing/validators.py
./references/crewAI/lib/crewai-files/tests/processing/test_validators.py
./references/crewAI/lib/crewai/src/crewai/a2a/extensions/a2ui/validator.py
./references/crewAI/lib/crewai/src/crewai/agents/agent_builder/base_agent_executor.py
./references/crewAI/lib/crewai/src/crewai/agents/crew_agent_executor.py
./references/crewAI/lib/crewai/src/crewai/agents/planner_observer.py
./references/crewAI/lib/crewai/src/crewai/agents/step_executor.py
./references/crewAI/lib/crewai/src/crewai/experimental/agent_executor.py
./references/crewAI/lib/crewai/tests/agents/test_agent_executor.py
./references/crewAI/lib/crewai/tests/agents/test_async_agent_executor.py
./references/crewAI/lib/crewai/tests/hooks/test_human_approval.py
./references/deer-flow/backend/packages/harness/deerflow/subagents/executor.py
./references/deer-flow/backend/tests/test_subagent_executor.py
./references/dify/api/core/helper/code_executor/code_executor.py
./references/dify/api/libs/validators.py
./references/dify/api/tests/integration_tests/workflow/nodes/__mock/code_executor.py
./references/dify/api/tests/test_containers_integration_tests/workflow/nodes/code_executor/test_code_executor.py
./references/dify/api/tests/unit_tests/core/helper/code_executor/test_code_executor.py
./references/dify/api/tests/unit_tests/core/workflow/nodes/http_request/test_http_request_executor.py
./references/everything-claude-code/src/llm/tools/executor.py
./references/everything-claude-code/tests/test_executor.py
./references/graphify/worked/example/raw/validator.py
./references/graphrag/packages/graphrag/graphrag/index/operations/build_noun_graph/np_extractors/np_validator.py
./references/hello-agents/Co-creation-projects/Apricity-InnocoreAI/agents/validator.py
./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
./references/hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/code_agent/executors/apply_patch_executor.py
./references/hello-agents/Co-creation-projects/YYHDBL-HelloCodeAgentCli/tools/async_executor.py
./references/hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
./references/hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
./references/hello-agents/Co-creation-projects/meiguanxiHXX-historyReviewAgent/historical_review/debate_orchestrator.py
./references/hello-agents/Co-creation-projects/melxy1997-ColumnWriter/orchestrator.py
./references/hello-agents/Co-creation-projects/usernamedadad-AutoFlow/backend/app/tools/mermaid_validator_tool.py
./references/hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
./references/hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
./references/hermes-agent/tests/cli/test_cli_approval_ui.py
./references/hermes-agent/tests/gateway/test_feishu_approval_buttons.py
./references/hermes-agent/tests/gateway/test_slack_approval_buttons.py
./references/hermes-agent/tests/gateway/test_telegram_approval_buttons.py
./references/hermes-agent/tests/tools/test_approval.py
./references/hermes-agent/tools/approval.py
./references/langflow/scripts/test_validator.py
./references/langflow/src/backend/base/langflow/agentic/services/flow_executor.py
./references/langflow/src/backend/base/langflow/alembic/migration_validator.py
./references/langflow/src/backend/base/langflow/inputs/validators.py
./references/langflow/src/backend/base/langflow/schema/validators.py
./references/langflow/src/backend/tests/unit/agentic/services/test_flow_executor.py
./references/langflow/src/backend/tests/unit/alembic/test_migration_validator.py
./references/langflow/src/backend/tests/unit/components/bundles/google/test_google_bq_sql_executor_component.py
./references/langflow/src/backend/tests/unit/components/data_source/test_sql_executor.py
./references/langflow/src/lfx/src/lfx/components/data_source/sql_executor.py
./references/langflow/src/lfx/src/lfx/components/google/google_bq_sql_executor.py
./references/langflow/src/lfx/src/lfx/components/langchain_utilities/runnable_executor.py
./references/langflow/src/lfx/src/lfx/inputs/validators.py
./references/langflow/src/lfx/src/lfx/schema/validators.py
./references/langgraph/libs/langgraph/langgraph/pregel/_executor.py
./references/langgraph/libs/prebuilt/langgraph/prebuilt/chat_agent_executor.py
./references/langgraph/libs/prebuilt/langgraph/prebuilt/tool_validator.py
./references/litellm/litellm/litellm_core_utils/thread_pool_executor.py
./references/litellm/litellm/llms/litellm_proxy/skills/sandbox_executor.py
./references/litellm/litellm/proxy/policy_engine/pipeline_executor.py
./references/litellm/litellm/proxy/policy_engine/policy_validator.py
./references/litellm/tests/llm_translation/test_skills_data/slack-gif-creator/core/validators.py
./references/litellm/tests/test_litellm/llms/litellm_proxy/test_sandbox_executor.py
./references/litellm/tests/test_litellm/proxy/policy_engine/test_pipeline_executor.py
./references/litellm/tests/test_litellm/proxy/policy_engine/test_policy_validator.py
./references/llama_index/llama-index-integrations/tools/llama-index-tools-neo4j/llama_index/tools/neo4j/query_validator.py
./references/openOii/backend/app/agents/orchestrator.py
./references/openOii/backend/tests/test_agents/test_orchestrator.py
./references/openalgo/services/flow_executor_service.py
./references/opik/apps/opik-guardrails-backend/opik_guardrails/services/validators/base_validator.py
./references/opik/apps/opik-guardrails-backend/opik_guardrails/services/validators/pii/validator.py
./references/opik/apps/opik-guardrails-backend/opik_guardrails/services/validators/topic/validator.py
./references/opik/apps/opik-guardrails-backend/tests/unit/services/test_pii_validator.py
./references/opik/apps/opik-guardrails-backend/tests/unit/services/test_topic_match_validator.py
./references/opik/apps/opik-python-backend/src/opik_backend/executor.py
./references/opik/apps/opik-python-backend/src/opik_backend/executor_docker.py
./references/opik/apps/opik-python-backend/src/opik_backend/executor_isolated.py
./references/opik/apps/opik-python-backend/src/opik_backend/executor_process.py
./references/opik/apps/opik-python-backend/tests/test_executor_docker.py
./references/opik/apps/opik-python-backend/tests/test_executor_isolated.py
./references/opik/sdks/python/src/opik/api_objects/dataset/validators.py
./references/opik/sdks/python/src/opik/evaluation/engine/evaluation_tasks_executor.py
./references/opik/sdks/python/src/opik/evaluation/metrics/arguments_validator.py
./references/opik/sdks/python/src/opik/validation/parameters_validator.py
./references/opik/sdks/python/src/opik/validation/validator.py
./references/opik/sdks/python/src/opik/validation/validator_helpers.py
./references/opik/sdks/python/tests/unit/validation/test_chat_prompt_messages_validator.py
./references/opik/sdks/python/tests/unit/validation/test_feedback_score_validator.py
./references/opik/sdks/python/tests/unit/validation/test_parameters_validator.py
./references/opik/sdks/python/tests/unit/validation/test_validator_helpers.py
./references/parlant/src/parlant/core/engines/alpha/planners.py
./references/parlant/tests/sdk/test_planners.py
./references/phoenix/packages/phoenix-client/src/phoenix/client/utils/executors.py
./references/phoenix/packages/phoenix-client/tests/client/utils/test_executors.py
./references/phoenix/packages/phoenix-evals/src/phoenix/evals/executors.py
./references/phoenix/packages/phoenix-evals/tests/phoenix/evals/test_executor.py
./references/phoenix/src/phoenix/server/api/routers/v1/validators.py
./references/ragflow/rag/svr/task_executor.py
./references/sglang/python/sglang/multimodal_gen/runtime/disaggregation/orchestrator.py
./references/sglang/python/sglang/multimodal_gen/runtime/pipelines_core/executors/parallel_executor.py
./references/sglang/python/sglang/multimodal_gen/runtime/pipelines_core/executors/pipeline_executor.py
./references/sglang/python/sglang/multimodal_gen/runtime/pipelines_core/executors/sync_executor.py
./references/sglang/python/sglang/multimodal_gen/runtime/pipelines_core/stages/validators.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/entrypoint/executor.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/entrypoint/planner.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/reorderer/executor.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/reorderer/planner.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/token_aligner/concat_steps/executor.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/token_aligner/smart/executor.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/token_aligner/smart/planner.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/unsharder/executor.py
./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/unsharder/planner.py
./references/sglang/python/sglang/srt/sampling/penaltylib/orchestrator.py
./references/sglang/test/registered/debug_utils/comparator/aligner/entrypoint/test_executor.py
./references/sglang/test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py
./references/sglang/test/registered/debug_utils/comparator/aligner/reorderer/test_executor.py
./references/sglang/test/registered/debug_utils/comparator/aligner/reorderer/test_planner.py
./references/sglang/test/registered/debug_utils/comparator/aligner/token_aligner/test_executor.py
./references/sglang/test/registered/debug_utils/comparator/aligner/token_aligner/test_planner.py
./references/sglang/test/registered/debug_utils/comparator/aligner/unsharder/test_executor.py
./references/sglang/test/registered/debug_utils/comparator/aligner/unsharder/test_planner.py
./references/skyvern/skyvern/forge/sdk/api/llm/schema_validator.py
./references/skyvern/skyvern/forge/sdk/executor/async_executor.py
./references/skyvern/skyvern/forge/sdk/executor/background_task_executor.py
./references/skyvern/skyvern/forge/sdk/workflow/models/validators.py
./references/skyvern/skyvern/utils/url_validators.py
./references/skyvern/tests/unit/test_script_reviewer_validators.py
./references/skyvern/tests/unit/test_url_validators.py
./references/skyvern/tests/unit_tests/test_schema_validator.py
./references/skyvern/tests/unit_tests/test_url_validators.py
./references/skyvern/tests/unit_tests/test_url_validators_extended.py
./references/vision-agent/tests/unit/test_planner_tools.py
./references/vision-agent/vision_agent/agent/vision_agent_planner_prompts_v2.py
./references/vision-agent/vision_agent/agent/vision_agent_planner_v2.py
./references/vision-agent/vision_agent/tools/planner_tools.py
./references/vision-agent/vision_agent/tools/planner_v3_tools.py
./references/vllm/tests/distributed/test_multiproc_executor.py
./references/vllm/tests/distributed/test_ray_v2_executor.py
./references/vllm/tests/distributed/test_ray_v2_executor_e2e.py
./references/vllm/tests/tools/test_config_validator.py
./references/vllm/tests/v1/executor/test_executor.py
./references/vllm/vllm/v1/executor/multiproc_executor.py
./references/vllm/vllm/v1/executor/ray_executor.py
./references/vllm/vllm/v1/executor/ray_executor_v2.py
./references/vllm/vllm/v1/executor/uniproc_executor.py

## 6. Existing Python Packages Named agent_core / service_plane / console_api
./core-platform/data/brain_assets/repos/github_stars/JuliusBrussee__caveman/evals
./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
./core-platform/data/brain_assets/repos/github_stars/bytedance__deer-flow/skills/public/systematic-literature-review/evals
./core-platform/data/brain_assets/repos/github_stars/garrytan__gstack/docs/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars_missing/JuliusBrussee__caveman/evals
./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
./core-platform/data/brain_assets/repos/github_stars_missing/bytedance__deer-flow/skills/public/systematic-literature-review/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/ab-test-setup/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/analytics-tracking/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/competitor-alternatives/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/copy-editing/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/copywriting/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/customer-research/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/email-sequence/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/form-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/free-tool-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/launch-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/marketing-ideas/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/marketing-psychology/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/onboarding-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/page-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/paid-ads/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/paywall-upgrade-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/popup-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/pricing-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/programmatic-seo/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/referral-program/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/schema-markup/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/seo-audit/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/signup-flow-cro/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars_missing/coreyhaines31__marketingskills/skills/social-content/evals
./core-platform/data/brain_assets/repos/github_stars_missing/garrytan__gbrain/evals
./core-platform/data/brain_assets/repos/github_stars_missing/garrytan__gstack/docs/evals
./core-platform/data/brain_assets/repos/github_stars_missing/openclaw__openclaw/docs/diagnostics
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/ad-creative/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/ai-seo/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/churn-prevention/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/cold-email/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/content-strategy/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/product-marketing-context/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/revops/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/sales-enablement/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/shadcn/evals
./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/site-architecture/evals
./core-platform/data/brain_assets/repos/github_stars_missing/tanweai__pua/evals
./core-platform/data/brain_assets/repos/github_stars_missing/vercel-labs__agent-browser/evals
./references/AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
./references/MinerU-Document-Explorer/finetune/evals
./references/agent-browser/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ad-creative/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ai-seo/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/churn-prevention/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/cold-email/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/content-strategy/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/product-marketing-context/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/revops/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/sales-enablement/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/shadcn/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/site-architecture/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ad-creative/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ai-seo/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/churn-prevention/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/cold-email/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/content-strategy/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/product-marketing-context/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/revops/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/sales-enablement/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/shadcn/evals
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/site-architecture/evals
./references/antigravity-awesome-skills/skills/ad-creative/evals
./references/antigravity-awesome-skills/skills/ai-seo/evals
./references/antigravity-awesome-skills/skills/churn-prevention/evals
./references/antigravity-awesome-skills/skills/cold-email/evals
./references/antigravity-awesome-skills/skills/content-strategy/evals
./references/antigravity-awesome-skills/skills/product-marketing-context/evals
./references/antigravity-awesome-skills/skills/revops/evals
./references/antigravity-awesome-skills/skills/sales-enablement/evals
./references/antigravity-awesome-skills/skills/shadcn/evals
./references/antigravity-awesome-skills/skills/site-architecture/evals
./references/cline/evals
./references/cline/src/integrations/diagnostics
./references/deer-flow/skills/public/systematic-literature-review/evals
./references/langfuse/packages/shared/src/features/evals
./references/langfuse/web/src/features/evals
./references/langfuse/web/src/pages/project/[projectId]/evals
./references/litellm/litellm/evals
./references/litellm/litellm/llms/base_llm/evals
./references/litellm/litellm/llms/openai/evals
./references/litellm/litellm/proxy/guardrails/guardrail_hooks/litellm_content_filter/guardrail_benchmarks/evals
./references/litellm/litellm/router_strategy/complexity_router/evals
./references/litellm/tests/test_litellm/llms/openai/evals
./references/marketingskills/skills/ab-test-setup/evals
./references/marketingskills/skills/ad-creative/evals
./references/marketingskills/skills/ai-seo/evals
./references/marketingskills/skills/analytics-tracking/evals
./references/marketingskills/skills/churn-prevention/evals
./references/marketingskills/skills/cold-email/evals
./references/marketingskills/skills/competitor-alternatives/evals
./references/marketingskills/skills/content-strategy/evals
./references/marketingskills/skills/copy-editing/evals
./references/marketingskills/skills/copywriting/evals
./references/marketingskills/skills/customer-research/evals
./references/marketingskills/skills/email-sequence/evals
./references/marketingskills/skills/form-cro/evals
./references/marketingskills/skills/free-tool-strategy/evals
./references/marketingskills/skills/launch-strategy/evals
./references/marketingskills/skills/marketing-ideas/evals
./references/marketingskills/skills/marketing-psychology/evals
./references/marketingskills/skills/onboarding-cro/evals
./references/marketingskills/skills/page-cro/evals
./references/marketingskills/skills/paid-ads/evals
./references/marketingskills/skills/paywall-upgrade-cro/evals
./references/marketingskills/skills/popup-cro/evals
./references/marketingskills/skills/pricing-strategy/evals
./references/marketingskills/skills/product-marketing-context/evals
./references/marketingskills/skills/programmatic-seo/evals
./references/marketingskills/skills/referral-program/evals
./references/marketingskills/skills/revops/evals
./references/marketingskills/skills/sales-enablement/evals
./references/marketingskills/skills/schema-markup/evals
./references/marketingskills/skills/seo-audit/evals
./references/marketingskills/skills/signup-flow-cro/evals
./references/marketingskills/skills/site-architecture/evals
./references/marketingskills/skills/social-content/evals
./references/openclaw/docs/diagnostics
./references/phoenix/app/evals
./references/phoenix/js/examples/apps/cli-agent-starter-kit/evals
./references/phoenix/js/examples/apps/mastra-quickstart/src/mastra/evals
./references/phoenix/packages/phoenix-evals/src/phoenix/evals
./references/phoenix/packages/phoenix-evals/tests/phoenix/evals
./references/phoenix/src/phoenix/experimental/evals
./references/phoenix/tutorials/evals
./references/promptfoo/src/app/src/pages/evals
./references/promptfoo/src/redteam/plugins/policy/evals
./references/stagehand/packages/evals
./references/uptrain/uptrain/operators/language/openai_eval_custom/custom_registry/evals
./references/vllm/tests/evals

## 7. Current Desktop Chat Chain Evidence
core-platform/apps/desktop/src/index.html:88:18125 Repo Memory
core-platform/apps/desktop/src/index.html:163:  [18125, "Repo Memory"],
core-platform/apps/desktop/src/index.html:1034:  content.innerHTML = pageHero("Repo Memory", "18125：仓库记忆、修复历史、上下文快照、知识搜索。") + `
core-platform/apps/desktop/src/index.html:1039:        <input class="field" id="repoMemoryServiceFilter" placeholder="Service 过滤，例如 18125" oninput="renderRepoMemoryList()" />
core-platform/apps/desktop/src/index.html:1050:        <input class="field" id="repoServices" placeholder="services，逗号分隔，例如 18120,18125,18126" />
core-platform/apps/desktop/src/index.html:1375:    "services": ["18120","18125","18104"],
core-platform/apps/desktop/src/js/windows-click-model-setup.js:168:    if (msg.includes("bootstrap_runtime.ps1") || msg.includes("运行时脚本")) {
core-platform/apps/desktop/src/js/services.js:15:  { name: "Repo Memory", port: 18125 },
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:219:      return { type: "repo_memory", reason: "project_or_asset_query" };
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:287:        url: "http://127.0.0.1:18125/brain/search",
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:291:        url: "http://127.0.0.1:18125/brain/search",
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:347:        "请确认 18125 repo_memory_service 已启动。",
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:357:    const raw = await invoke("generate_local_ai_response", {
core-platform/apps/desktop/src/js/windows-demo-stable-router.js:411:    if (intent.type === "repo_memory") return await answerRepoMemoryQuestion(query);
core-platform/apps/desktop/src/js/api.js:12:  repoMemory: "http://127.0.0.1:18125",
core-platform/apps/desktop/src/index.html.d7c3a.bak:88:18125 Repo Memory
core-platform/apps/desktop/src/index.html.d7c3a.bak:163:  [18125, "Repo Memory"],
core-platform/apps/desktop/src/index.html.d7c3a.bak:1034:  content.innerHTML = pageHero("Repo Memory", "18125：仓库记忆、修复历史、上下文快照、知识搜索。") + `
core-platform/apps/desktop/src/index.html.d7c3a.bak:1039:        <input class="field" id="repoMemoryServiceFilter" placeholder="Service 过滤，例如 18125" oninput="renderRepoMemoryList()" />
core-platform/apps/desktop/src/index.html.d7c3a.bak:1050:        <input class="field" id="repoServices" placeholder="services，逗号分隔，例如 18120,18125,18126" />
core-platform/apps/desktop/src/index.html.d7c3a.bak:1375:    "services": ["18120","18125","18104"],
core-platform/apps/desktop/src-tauri/src/lib.rs:146:        let script_content = include_str!("../../../../scripts/windows/bootstrap_runtime.ps1");
core-platform/apps/desktop/src-tauri/src/lib.rs:152:        let script_path = runtime_dir.join("bootstrap_runtime.ps1");
core-platform/apps/desktop/src-tauri/src/lib.rs:154:            .map_err(|e| format!("无法写入 bootstrap_runtime.ps1: {}", e))?;
core-platform/apps/desktop/src-tauri/src/lib.rs:156:            .map_err(|e| format!("写入 bootstrap_runtime.ps1 失败: {}", e))?;
core-platform/apps/desktop/src-tauri/src/lib.rs:287:fn generate_local_ai_response(profile: String, prompt: String) -> Result<String, String> {
core-platform/apps/desktop/src-tauri/src/lib.rs:303:            generate_local_ai_response

## 8. Current Windows Bundle Resource Evidence
core-platform/apps/desktop/src-tauri/tauri.conf.json:32:    "resources": [
core-platform/apps/desktop/src-tauri/tauri.conf.json:33:      "resources/scripts/start_all.sh",
core-platform/apps/desktop/src-tauri/tauri.conf.json:34:      "resources/scripts/stop_all.sh",
core-platform/apps/desktop/src-tauri/tauri.conf.json:35:      "../../../scripts/windows/ensure_runtime.ps1",
core-platform/apps/desktop/src-tauri/tauri.conf.json:36:      "../../../scripts/windows/bootstrap_runtime.ps1",
core-platform/apps/desktop/src-tauri/tauri.conf.json:37:      "../../../scripts/windows/start_all.ps1",
core-platform/apps/desktop/src-tauri/tauri.conf.json:38:      "../../../scripts/windows/stop_all.ps1",
core-platform/apps/desktop/src-tauri/tauri.conf.json:39:      "../../../scripts/windows/status_all.ps1",
core-platform/apps/desktop/src-tauri/tauri.conf.json:40:      "../../../services/model_bootstrap_service",
core-platform/apps/desktop/src-tauri/tauri.conf.json:41:      "../../../services/model_gateway"
.github/workflows/build-win-release.yml:93:          if (!(Test-Path dist\js\auto-start-services.js)) {
.github/workflows/build-win-release.yml:94:            throw "auto-start-services.js missing from dist; Windows package would be old"

## 9. Services Present
core-platform/services/agent_orchestrator/main.py
core-platform/services/agent_runtime_service/main.py
core-platform/services/artifact_registry_service/main.py
core-platform/services/code_review_gate_service/main.py
core-platform/services/design_system_service/main.py
core-platform/services/eval_engine/main.py
core-platform/services/model_bootstrap_service/main.py
core-platform/services/model_gateway/main.py
core-platform/services/plugin_manager/main.py
core-platform/services/repo_memory_service/main.py
core-platform/services/skill_store_service/main.py
core-platform/services/workflow_store_service/main.py

## 10. Check Dataless / Unreadable Files
### core-platform/services/agent_orchestrator/main.py
-rw-r--r--  1 mofamaomi  staff  3172 Apr 21 21:56 core-platform/services/agent_orchestrator/main.py
core-platform/services/agent_orchestrator/main.py: Python script text executable, ASCII text
readable=true
chars= 3172
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

GATEWAY_URL = "http://127.0.0.1:18080/generate"
PLUGIN_URL = "http://127.0.0.1:18082/run"
EVAL_URL = "http://127.0.0.1:18083/task-runs"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskReq(BaseModel):
    task_type: str
    prompt: str

def route_plugin(task_type: str, prompt: str):
    text = pr

### core-platform/services/model_gateway/main.py
-rw-r--r--  1 mofamaomi  staff  854 Apr 14 14:03 core-platform/services/model_gateway/main.py
core-platform/services/model_gateway/main.py: Python script text executable, ASCII text
readable=true
chars= 854
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateReq(BaseModel):
    model: str
    prompt: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/generate")
def generate(req: GenerateReq):
    r = requests.post(
       

### core-platform/services/agent_runtime_service/main.py
-rw-r--r--  1 mofamaomi  staff  2046 May 13 15:34 core-platform/services/agent_runtime_service/main.py
core-platform/services/agent_runtime_service/main.py: Python script text executable, ASCII text
readable=true
chars= 2046
"""FastAPI entrypoint for the MAOMIAI agent runtime service."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from services.agent_runtime_service.app.models import AgentRunRequest
from services.agent_runtime_service.app.planner import build_plan
from services.agent_runtime_service.app.service import run_agent


app = FastAPI(title="MAOMIAI Agent Runtime Service", version=

### core-platform/services/repo_memory_service/main.py
-rw-r--r--  1 mofamaomi  staff  7120 May 13 13:45 core-platform/services/repo_memory_service/main.py
core-platform/services/repo_memory_service/main.py: Python script text executable, ASCII text
readable=true
chars= 7120
"""FastAPI main application for repo memory service."""

import sys
from pathlib import Path
from typing import Optional

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from services.repo_memory_service.app.models import (
    RepoRecord,
    FixRecord,
    ContextSnapshot,
    KnowledgeEntry,
    RegisterRepoRequest,
    RecordFixRequest,
    SnapshotContextRequest,
    AddKnowledgeRe

### core-platform/services/skill_store_service/main.py
-rw-r--r--  1 mofamaomi  staff  5955 Apr 26 00:52 core-platform/services/skill_store_service/main.py
core-platform/services/skill_store_service/main.py: Python script text executable, ASCII text
readable=true
chars= 5955
"""FastAPI main application for skill store service."""

import sys
from pathlib import Path
from typing import Optional

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from services.skill_store_service.app.models import (
    SkillRecord,
    ParseSkillMdRequest,
    InstallSkillMdRequest,
    UpdateSkillRequest,
    EnableSkillRequest,
    SkillSt

## 11. Search for Claude Code Style Loop Markers
Binary file core-platform/releases/windows-current-ui-final/desktop_lib.exe matches
core-platform/releases/windows-current-ui-final/README.md:27:- Defaults to chat/new session
Binary file core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-latest-after-full-delivery/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-latest-after-full-delivery/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-c9-latest-embedded-bootstrap/desktop_lib.exe matches
Binary file core-platform/releases/windows-c9-latest-embedded-bootstrap/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-final-latest/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-final-latest/Local AI Platform_0.1.0_x64_en-US.msi matches
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:191:            approval_rate=0.0,
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:201:    # Calculate approval rate
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:203:    approval_rate = approved / len(items) if items else 0.0
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:214:        approval_rate=approval_rate,
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/models.py:95:    approval_rate: float
core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/rules.py:142:                    "execute(sql",
core-platform/releases/windows-d7-full-delivery/runtime/services/design_system_service/tests/acceptance_test.py:232:        import traceback
core-platform/releases/windows-d7-full-delivery/runtime/services/design_system_service/tests/acceptance_test.py:233:        traceback.print_exc()
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/service.py:49:    run_id = req.run_id or req.trace_id or make_artifact_id(name)
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/service.py:65:        trace_id=req.trace_id,
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/models.py:37:    trace_id: str = ""
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/models.py:64:    trace_id: str = ""
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/validation.py:65:    if not req.run_id and not req.trace_id:
core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/validation.py:66:        errors.append("run_id or trace_id is required")
core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/app/service.py:119:    """Generate dry run execution plan."""
core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/app/service.py:126:    # Build execution plan
core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/main.py:158:    """Generate dry run execution plan."""
Binary file core-platform/releases/windows-d7-full-delivery/installers/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-full-delivery/installers/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-c1-fixed/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-c1-fixed/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-c5-self-contained-runtime/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-c5-self-contained-runtime/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/maomiai-desktop-demo/Local AI Platform.app/Contents/MacOS/desktop_lib matches
core-platform/releases/maomiai-desktop-demo/docs/MAOMIAI_DESKTOP_DEMO_GUIDE.md:131:当前已实现 `chat-session-manager.js`：
core-platform/releases/maomiai-desktop-demo/docs/MAOMIAI_DESKTOP_DEMO_GUIDE.md:146:- `chat-session-manager.js`
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:9:The desktop application can be built and launched, and the local model gateway chain is verified. However, full manual regression of chat session isolation and all page-level interactions is still pending.
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:27:* ✅ Chat session manager implementation
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:43:* ⚠️ Full chat session isolation
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:44:* ⚠️ New session behavior
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:65:1. **Session manager regression** - Full manual testing of session isolation, context memory, persistence
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:74:- Chat sessions properly isolated
core-platform/releases/maomiai-desktop-demo/docs/P3_14_D7_DESKTOP_INTERACTION_REGRESSION_CHECKLIST.md:12:- `chat-session-manager.js`
core-platform/releases/maomiai-desktop-demo/scripts/desktop_services.env:7:18111|trace_observability|services.trace_observability_service.main:app|trace-observability.log
Binary file core-platform/releases/windows/desktop_lib.exe matches
Binary file core-platform/releases/windows/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-c4-runtime-bundled/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-c4-runtime-bundled/Local AI Platform_0.1.0_x64_en-US.msi matches
Binary file core-platform/releases/windows-d7-verified-complete/desktop_lib.exe matches
Binary file core-platform/releases/windows-d7-verified-complete/Local AI Platform_0.1.0_x64_en-US.msi matches
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:28:    <div id="sessions" class="sessions"></div>
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:34:        <div class="top-sub" id="sessionMeta">session: -</div>
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:38:        <div class="select-pill">Manual approval</div>
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:55:        <button class="tab" onclick="switchInspector('trace')">Trace</button>
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:76:    <div id="inspector-trace" class="inspector-section hidden">
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:79:        <div id="traceBox" class="mono">暂无</div>
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:165:    id: "session_" + Date.now(),
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:171:  state.sessions.unshift(s);
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:216:  document.getElementById("sessionMeta").textContent = currentView === "chat" ? ("session: " + s.id) : ("view: " + currentView);
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1130:  const box = document.getElementById("sessions");
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1132:  for (const s of state.sessions) {
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1134:    b.className = "session-btn" + (s.id === state.current ? " active" : "");
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1160:      ${r.trace_id ? `<button class="btn-soft" onclick="loadTrace('${r.trace_id}')">查看 Trace</button>` : ""}
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1179:    const real = await postJson(`${API.runtime}/execute`, {
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1184:        session_id: currentSession().id,
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1205:      trace_id: real.trace_id || real.result?.trace_id || ctx.dry?.trace_id,
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1210:    if (real.trace_id || real.result?.trace_id || ctx.dry?.trace_id) {
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1211:      document.getElementById("traceBox").textContent = real.trace_id || real.result?.trace_id || ctx.dry?.trace_id;
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1265:    const dry = await postJson(`${API.runtime}/execute`, {
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1269:      metadata: { session_id: currentSession().id, shared_learning: true }
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1279:      trace_id: dry.trace_id,
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1283:    if (dry.trace_id) document.getElementById("traceBox").textContent = dry.trace_id;
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1405:      trace_id: result.trace_id || result.result?.trace_id || ctx.dry?.trace_id || "",
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1479:    trace_id: x.trace_id || payload.trace_id || "",
core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:2105:        session_id: currentSession().id,
core-platform/docs/brain/context_engine_architecture.md:51:Uses retrieval as a step inside planning, not as a one-shot vector search.
core-platform/docs/brain/no_hallucination_policy.md:9:3. Capability claims must reflect enabled modules.
core-platform/docs/reports/C23_B_AGENT_RUNTIME_SERVICE.md:33:- `POST /agent/plan`
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:556:./references/hello-agents/code/chapter13/helloagents-trip-planner
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:725:./references/promptfoo/examples/anthropic/claude-code-session
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:829:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:830:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:831:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:832:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:833:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:834:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:836:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:837:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:838:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:839:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:840:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tools/approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:867:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:868:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:871:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:872:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:873:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:878:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:879:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:883:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:886:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:888:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:891:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:893:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:909:./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/src/openharness/sandbox/path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:911:./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/tests/test_sandbox/test_path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:913:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:914:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:915:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:916:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:917:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:918:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:920:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:921:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:922:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:923:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:924:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tools/approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:954:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:955:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:958:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:959:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:960:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:965:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:966:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:967:./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/src/parlant/core/engines/alpha/planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:968:./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/tests/sdk/test_planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:970:./core-platform/data/brain_assets/repos/github_stars_missing/openai__codex/sdk/python/tests/test_app_server_approvals.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:974:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:977:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:979:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:982:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:984:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:991:./core-platform/services/agent_runtime_service/app/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1037:./references/OpenHarness/src/openharness/sandbox/path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1039:./references/OpenHarness/tests/test_sandbox/test_path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1050:./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1053:./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1055:./references/antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1058:./references/antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1060:./references/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1084:./references/crewAI/lib/crewai/src/crewai/agents/planner_observer.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1089:./references/crewAI/lib/crewai/tests/hooks/test_human_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1103:./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1104:./references/hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1107:./references/hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1108:./references/hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1112:./references/hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1113:./references/hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1114:./references/hermes-agent/tests/cli/test_cli_approval_ui.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1115:./references/hermes-agent/tests/gateway/test_feishu_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1116:./references/hermes-agent/tests/gateway/test_slack_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1117:./references/hermes-agent/tests/gateway/test_telegram_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1118:./references/hermes-agent/tests/tools/test_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1119:./references/hermes-agent/tools/approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1138:./references/litellm/litellm/llms/litellm_proxy/skills/sandbox_executor.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1142:./references/litellm/tests/test_litellm/llms/litellm_proxy/test_sandbox_executor.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1170:./references/parlant/src/parlant/core/engines/alpha/planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1171:./references/parlant/tests/sdk/test_planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1184:./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/entrypoint/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1186:./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/reorderer/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1189:./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/token_aligner/smart/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1191:./references/sglang/python/sglang/srt/debug_utils/comparator/aligner/unsharder/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1194:./references/sglang/test/registered/debug_utils/comparator/aligner/entrypoint/test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1196:./references/sglang/test/registered/debug_utils/comparator/aligner/reorderer/test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1198:./references/sglang/test/registered/debug_utils/comparator/aligner/token_aligner/test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1200:./references/sglang/test/registered/debug_utils/comparator/aligner/unsharder/test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1211:./references/vision-agent/tests/unit/test_planner_tools.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1212:./references/vision-agent/vision_agent/agent/vision_agent_planner_prompts_v2.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1213:./references/vision-agent/vision_agent/agent/vision_agent_planner_v2.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1214:./references/vision-agent/vision_agent/tools/planner_tools.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1215:./references/vision-agent/vision_agent/tools/planner_v3_tools.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1226:## 6. Existing Python Packages Named agent_core / service_plane / console_api
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1228:./core-platform/data/brain_assets/repos/github_stars/Significant-Gravitas__AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1262:./core-platform/data/brain_assets/repos/github_stars_missing/Significant-Gravitas__AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1299:./core-platform/data/brain_assets/repos/github_stars_missing/openclaw__openclaw/docs/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1332:./references/AutoGPT/autogpt_platform/frontend/src/app/(platform)/admin/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1366:./references/cline/src/integrations/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1410:./references/openclaw/docs/diagnostics
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1569:from services.agent_runtime_service.app.planner import build_plan
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1634:core-platform/releases/windows-current-ui-final/README.md:27:- Defaults to chat/new session
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1642:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:191:            approval_rate=0.0,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1643:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:201:    # Calculate approval rate
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1644:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:203:    approval_rate = approved / len(items) if items else 0.0
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1645:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/service.py:214:        approval_rate=approval_rate,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1646:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/models.py:95:    approval_rate: float
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1647:core-platform/releases/windows-d7-full-delivery/runtime/services/code_review_gate_service/app/rules.py:142:                    "execute(sql",
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1648:core-platform/releases/windows-d7-full-delivery/runtime/services/design_system_service/tests/acceptance_test.py:232:        import traceback
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1649:core-platform/releases/windows-d7-full-delivery/runtime/services/design_system_service/tests/acceptance_test.py:233:        traceback.print_exc()
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1650:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/service.py:49:    run_id = req.run_id or req.trace_id or make_artifact_id(name)
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1651:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/service.py:65:        trace_id=req.trace_id,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1652:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/models.py:37:    trace_id: str = ""
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1653:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/models.py:64:    trace_id: str = ""
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1654:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/validation.py:65:    if not req.run_id and not req.trace_id:
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1655:core-platform/releases/windows-d7-full-delivery/runtime/services/artifact_registry_service/app/validation.py:66:        errors.append("run_id or trace_id is required")
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1656:core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/app/service.py:119:    """Generate dry run execution plan."""
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1657:core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/app/service.py:126:    # Build execution plan
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1658:core-platform/releases/windows-d7-full-delivery/runtime/services/workflow_store_service/main.py:158:    """Generate dry run execution plan."""
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1666:core-platform/releases/maomiai-desktop-demo/docs/MAOMIAI_DESKTOP_DEMO_GUIDE.md:131:当前已实现 `chat-session-manager.js`：
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1667:core-platform/releases/maomiai-desktop-demo/docs/MAOMIAI_DESKTOP_DEMO_GUIDE.md:146:- `chat-session-manager.js`
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1668:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:9:The desktop application can be built and launched, and the local model gateway chain is verified. However, full manual regression of chat session isolation and all page-level interactions is still pending.
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1669:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:27:* ✅ Chat session manager implementation
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1670:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:43:* ⚠️ Full chat session isolation
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1671:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:44:* ⚠️ New session behavior
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1672:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:65:1. **Session manager regression** - Full manual testing of session isolation, context memory, persistence
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1673:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md:74:- Chat sessions properly isolated
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1674:core-platform/releases/maomiai-desktop-demo/docs/P3_14_D7_DESKTOP_INTERACTION_REGRESSION_CHECKLIST.md:12:- `chat-session-manager.js`
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1675:core-platform/releases/maomiai-desktop-demo/scripts/desktop_services.env:7:18111|trace_observability|services.trace_observability_service.main:app|trace-observability.log
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1682:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:28:    <div id="sessions" class="sessions"></div>
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1683:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:34:        <div class="top-sub" id="sessionMeta">session: -</div>
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1684:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:38:        <div class="select-pill">Manual approval</div>
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1685:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:55:        <button class="tab" onclick="switchInspector('trace')">Trace</button>
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1686:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:76:    <div id="inspector-trace" class="inspector-section hidden">
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1687:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:79:        <div id="traceBox" class="mono">暂无</div>
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1688:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:165:    id: "session_" + Date.now(),
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1689:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:171:  state.sessions.unshift(s);
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1690:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:216:  document.getElementById("sessionMeta").textContent = currentView === "chat" ? ("session: " + s.id) : ("view: " + currentView);
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1691:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1130:  const box = document.getElementById("sessions");
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1692:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1132:  for (const s of state.sessions) {
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1693:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1134:    b.className = "session-btn" + (s.id === state.current ? " active" : "");
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1694:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1160:      ${r.trace_id ? `<button class="btn-soft" onclick="loadTrace('${r.trace_id}')">查看 Trace</button>` : ""}
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1695:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1179:    const real = await postJson(`${API.runtime}/execute`, {
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1696:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1184:        session_id: currentSession().id,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1697:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1205:      trace_id: real.trace_id || real.result?.trace_id || ctx.dry?.trace_id,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1698:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1210:    if (real.trace_id || real.result?.trace_id || ctx.dry?.trace_id) {
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1699:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1211:      document.getElementById("traceBox").textContent = real.trace_id || real.result?.trace_id || ctx.dry?.trace_id;
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1700:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1265:    const dry = await postJson(`${API.runtime}/execute`, {
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1701:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1269:      metadata: { session_id: currentSession().id, shared_learning: true }
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1702:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1279:      trace_id: dry.trace_id,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1703:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1283:    if (dry.trace_id) document.getElementById("traceBox").textContent = dry.trace_id;
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1704:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1405:      trace_id: result.trace_id || result.result?.trace_id || ctx.dry?.trace_id || "",
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1705:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:1479:    trace_id: x.trace_id || payload.trace_id || "",
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1706:core-platform/archive/desktop-cleanup/index.html.20260426-105756.bak:2105:        session_id: currentSession().id,
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1707:core-platform/docs/brain/context_engine_architecture.md:51:Uses retrieval as a step inside planning, not as a one-shot vector search.
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1708:core-platform/docs/brain/no_hallucination_policy.md:9:3. Capability claims must reflect enabled modules.
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1709:core-platform/docs/reports/C23_B_AGENT_RUNTIME_SERVICE.md:33:- `POST /agent/plan`
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1710:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:556:./references/hello-agents/code/chapter13/helloagents-trip-planner
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1711:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:725:./references/promptfoo/examples/anthropic/claude-code-session
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1712:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:829:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1713:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:830:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1714:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:831:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1715:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:832:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1716:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:833:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1717:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:834:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1718:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:836:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1719:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:837:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1720:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:838:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1721:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:839:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1722:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:840:./core-platform/data/brain_assets/repos/github_stars/NousResearch__hermes-agent/tools/approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1723:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:867:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1724:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:868:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1725:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:871:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1726:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:872:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1727:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:873:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1728:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:878:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1729:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:879:./core-platform/data/brain_assets/repos/github_stars/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1730:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:883:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1731:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:886:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1732:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:888:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1733:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:891:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1734:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:893:./core-platform/data/brain_assets/repos/github_stars/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1735:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:909:./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/src/openharness/sandbox/path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1736:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:911:./core-platform/data/brain_assets/repos/github_stars_missing/HKUDS__OpenHarness/tests/test_sandbox/test_path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1737:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:913:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/acp/test_approval_isolation.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1738:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:914:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/cli/test_cli_approval_ui.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1739:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:915:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_feishu_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1740:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:916:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_matrix_exec_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1741:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:917:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_slack_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1742:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:918:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/gateway/test_telegram_approval_buttons.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1743:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:920:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1744:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:921:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_heartbeat.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1745:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:922:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_approval_plugin_hooks.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1746:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:923:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tests/tools/test_cron_approval_mode.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1747:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:924:./core-platform/data/brain_assets/repos/github_stars_missing/NousResearch__hermes-agent/tools/approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1748:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:954:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1749:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:955:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1750:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:958:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1751:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:959:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/huailishang-AgentPlatformBase/agents/deep_research/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1752:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:960:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1753:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:965:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter13/helloagents-trip-planner/backend/app/agents/trip_planner_agent.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1754:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:966:./core-platform/data/brain_assets/repos/github_stars_missing/datawhalechina__hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1755:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:967:./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/src/parlant/core/engines/alpha/planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1756:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:968:./core-platform/data/brain_assets/repos/github_stars_missing/emcie-co__parlant/tests/sdk/test_planners.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1757:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:970:./core-platform/data/brain_assets/repos/github_stars_missing/openai__codex/sdk/python/tests/test_app_server_approvals.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1758:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:974:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1759:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:977:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1760:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:979:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1761:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:982:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1762:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:984:./core-platform/data/brain_assets/repos/github_stars_missing/sickn33__antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1763:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:991:./core-platform/services/agent_runtime_service/app/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1764:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1037:./references/OpenHarness/src/openharness/sandbox/path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1765:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1039:./references/OpenHarness/tests/test_sandbox/test_path_validator.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1766:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1050:./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1767:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1053:./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1768:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1055:./references/antigravity-awesome-skills/plugins/antigravity-bundle-expo-react-native/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1769:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1058:./references/antigravity-awesome-skills/plugins/antigravity-bundle-mobile-developer/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1770:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1060:./references/antigravity-awesome-skills/skills/app-store-optimization/ab_test_planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1771:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1084:./references/crewAI/lib/crewai/src/crewai/agents/planner_observer.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1772:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1089:./references/crewAI/lib/crewai/tests/hooks/test_human_approval.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1773:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1103:./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1774:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1104:./references/hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1775:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1107:./references/hello-agents/Co-creation-projects/chen070808-ProgrammingTutor/src/agents/planner.py
core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1776:core-platform/docs/reports/C24_A_CLAUDE_CODE_KERNEL_RECOVERY_AUDIT.md:1108:./references/hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/agents/planner.py

## 12. Preliminary Conclusion

This report should be reviewed to decide whether the original Claude Code / Claw Code agent kernel exists locally and whether desktop chat is wired into it.
