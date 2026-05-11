# P3.14-D7 Full Local Project Integrity Audit

Generated at: Mon May 11 00:39:21 CST 2026

## 1. Git / Root

```text
/Users/mofamaomi/Documents/本地ai
/Users/mofamaomi/Documents/本地ai
main
c97bc96 docs: update professional README for MAOMIAI desktop platform
3b2249c docs: verify project integrity and complete Windows package
cd27199 fix: restore enterprise services into canonical packaging path
d33da8b chore: normalize Mac and Windows desktop source paths
d379074 docs: add D7 source sync audit report
98b89d7 docs: record D7-C5 self-contained runtime package
245a2b1 feat: add Windows self-contained backend runtime manager
415611c fix: patch all Tauri resource paths for Windows runtime - remove duplicates
f875993 fix: correct Tauri Windows runtime resource paths
5edd1bb feat: add Windows auto bootstrap installer for local AI
8160ebc fix: add missing Windows runtime files to package path
7deaf9d docs: record D7-C4 Windows runtime package download
ea066c0 feat: bundle Windows runtime bootstrap resources
855aff9 feat: add Windows runtime bootstrap for local AI setup
f11fb39 feat: add Windows runtime bootstrap for local AI setup
69c16a2 fix: improve product UI and model setup feedback
f6e6971 fix: add Windows click fallback and local model setup entry
b881758 feat: add ChatGPT-like desktop home UI
ab8f726 docs: accept D7-C1 Windows current UI build
c3ecabf fix: restore correct MAOMIAI UI to Windows build source path with D7-C1 cleanup

---- git status ----
 M .github/workflows/build-win-release.yml
 D core-platform/core-platform/apps/desktop/package.json
 D core-platform/core-platform/apps/desktop/scripts/scripts/build-frontend.mjs
 D core-platform/core-platform/apps/desktop/scripts/scripts/preflight.mjs
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/128x128.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/128x128@2x.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/32x32.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square107x107Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square142x142Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square150x150Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square284x284Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square30x30Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square310x310Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square44x44Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square71x71Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square89x89Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/StoreLogo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.icns
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.ico
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.png
 D core-platform/core-platform/apps/desktop/src-tauri/resources/resources/scripts/start_all.sh
 D core-platform/core-platform/apps/desktop/src-tauri/resources/resources/scripts/stop_all.sh
 D core-platform/core-platform/apps/desktop/src-tauri/tauri.conf.json
 D core-platform/core-platform/scripts/start_all.sh
 D core-platform/core-platform/scripts/stop_all.sh
?? .venv/
?? AlphaAgent/
?? D4_B_ACCEPTANCE_REPORT.md
?? LLaVA-NeXT/
?? LLaVA-OneVision-1.5/
?? MASTER/
?? OpenHands/
?? Qwen3-VL/
?? RAG-Anything/
?? VoxCPM/
?? andrej-karpathy-skills/
?? anything-llm/
?? archive/quarantine/
?? capability-registry/claude-code-best-practice/
?? capability-registry/gstack/
?? core-platform/archive/
?? core-platform/data/
?? core-platform/fix_workflow_paths.py
?? core-platform/releases/final-demo/
?? core-platform/releases/maomiai-cross-platform-demo-package.tar.gz
?? core-platform/releases/maomiai-desktop-demo.tar.gz
?? core-platform/releases/maomiai-desktop-demo/
?? core-platform/releases/windows-current-ui-final.tar.gz
?? core-platform/releases/windows-current-ui-final/BUILD_INFO.json
?? "core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64-setup.exe"
?? "core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64_en-US.msi"
?? core-platform/releases/windows-current-ui-final/desktop_lib.exe
?? core-platform/releases/windows-d7-c1-fixed/
?? core-platform/releases/windows-d7-c4-runtime-bundled/
?? core-platform/releases/windows-d7-c5-self-contained-runtime/
?? core-platform/releases/windows-d7-verified-complete/
?? core-platform/releases/windows/
?? core-platform/tmp_fix_workflow_paths.py
?? data/
?? docs/reports/P3_14_D2_C3_WORKFLOW_STORE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_D_ARTIFACT_REGISTRY_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_E_SKILL_STORE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_F_CODE_REVIEW_GATE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_G_REPO_MEMORY_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D7_A_ACCEPTANCE_REPORT.md
?? docs/reports/P3_14_D7_FULL_LOCAL_PROJECT_INTEGRITY_AUDIT.md
?? full_integrity_audit.sh
?? generated/audio/
?? generated/browser/
?? generated/crawler/
?? generated/finance/
?? generated/hyperframes/
?? generated/rag/
?? generated/research/
?? generated/stock_research/
?? generated/videos/video_job_20260417_212451.json
?? generated/videos/video_job_20260417_212506.json
?? generated/videos/video_job_20260417_214458.json
?? generated/videos/video_job_20260417_222053.json
?? generated/videos/video_job_20260417_225316.json
?? generated/vision/
?? generated/web_research/
?? langflow/
?? qlib/
?? scripts/acceptance/
?? services/
?? test_service_health.html
?? vnpy/
```

## 2. Top-level Directory Inventory

```text
.
./.git
./.git/hooks
./.git/info
./.git/logs
./.git/objects
./.git/refs
./.github
./.github/workflows
./.venv
./.venv/bin
./.venv/include
./.venv/lib
./AlphaAgent
./AlphaAgent/.git
./AlphaAgent/.github
./AlphaAgent/.streamlit
./AlphaAgent/alphaagent
./AlphaAgent/constraints
./AlphaAgent/docs
./AlphaAgent/requirements
./LLaVA-NeXT
./LLaVA-NeXT/.git
./LLaVA-NeXT/docs
./LLaVA-NeXT/llava
./LLaVA-NeXT/llava-critic-r1
./LLaVA-NeXT/playground
./LLaVA-NeXT/scripts
./LLaVA-NeXT/trl
./LLaVA-OneVision-1.5
./LLaVA-OneVision-1.5/.git
./LLaVA-OneVision-1.5/.github
./LLaVA-OneVision-1.5/aiak_megatron
./LLaVA-OneVision-1.5/aiak_training_llm
./LLaVA-OneVision-1.5/asset
./LLaVA-OneVision-1.5/configs
./LLaVA-OneVision-1.5/docs
./LLaVA-OneVision-1.5/ds
./LLaVA-OneVision-1.5/examples
./LLaVA-OneVision-1.5/examples_offline_packing
./LLaVA-OneVision-1.5/tools
./MASTER
./MASTER/.git
./MASTER/data
./MASTER/model
./MASTER/qlib-update
./OpenHands
./OpenHands/.agents
./OpenHands/.devcontainer
./OpenHands/.git
./OpenHands/.github
./OpenHands/.openhands
./OpenHands/.vscode
./OpenHands/containers
./OpenHands/dev_config
./OpenHands/enterprise
./OpenHands/frontend
./OpenHands/kind
./OpenHands/openhands
./OpenHands/openhands-ui
./OpenHands/scripts
./OpenHands/skills
./OpenHands/tests
./OpenHands/third_party
./Qwen3-VL
./Qwen3-VL/.git
./Qwen3-VL/cookbooks
./Qwen3-VL/docker
./Qwen3-VL/evaluation
./Qwen3-VL/qwen-vl-finetune
./Qwen3-VL/qwen-vl-utils
./RAG-Anything
./RAG-Anything/.git
./RAG-Anything/.github
./RAG-Anything/assets
./RAG-Anything/docs
./RAG-Anything/examples
./RAG-Anything/raganything
./RAG-Anything/reproduce
./RAG-Anything/scripts
./RAG-Anything/tests
./VoxCPM
./VoxCPM/.git
./VoxCPM/.github
./VoxCPM/assets
./VoxCPM/conf
./VoxCPM/examples
./VoxCPM/scripts
./VoxCPM/src
./VoxCPM/tests
./andrej-karpathy-skills
./andrej-karpathy-skills/.claude-plugin
./andrej-karpathy-skills/.git
./andrej-karpathy-skills/skills
./anything-llm
./anything-llm/.devcontainer
./anything-llm/.git
./anything-llm/.github
./anything-llm/.vscode
./anything-llm/browser-extension
./anything-llm/cloud-deployments
./anything-llm/collector
./anything-llm/docker
./anything-llm/embed
./anything-llm/extras
./anything-llm/frontend
./anything-llm/images
./anything-llm/locales
./anything-llm/server
./apps
./apps/desktop
./archive
./archive/d7-sync-d-before-enterprise-service-repair
./archive/quarantine
./capability-registry
./capability-registry/claude-code-best-practice
./capability-registry/gstack
./core-platform
./core-platform/.github
./core-platform/.venv
./core-platform/apps
./core-platform/archive
./core-platform/config
./core-platform/core-platform
./core-platform/data
./core-platform/docs
./core-platform/logs
./core-platform/manifests
./core-platform/packages
./core-platform/plugins
./core-platform/prompts
./core-platform/releases
./core-platform/scripts
./core-platform/services
./data
./data/artifact_registry
./data/code_review_gate
./data/design_system
./data/document_ingestion
./data/repo_memory
./data/skill_store
./data/workflow_store
./docs
./docs/reports
./generated
./generated/audio
./generated/browser
./generated/crawler
./generated/finance
./generated/hyperframes
./generated/images
./generated/rag
./generated/research
./generated/stock_research
./generated/videos
./generated/vision
./generated/web_research
./langflow
./langflow/.agents
./langflow/.cursor
./langflow/.devcontainer
./langflow/.git
./langflow/.github
./langflow/.vscode
./langflow/deploy
./langflow/docker
./langflow/docker_example
./langflow/docs
./langflow/scripts
./langflow/src
./langflow/test-results
./logs
./manifests
./manifests/plugins 2
./models
./models/cogvideo
./plugins
./plugins/crawler_media_plugin 2
./plugins/finance_vnpy_plugin 2
./plugins/image_simple_plugin 2
./plugins/tts_voxcpm_plugin 2
./qlib
./qlib/.git
./qlib/.github
./qlib/docs
./qlib/examples
./qlib/qlib
./qlib/scripts
./qlib/tests
./references
./references/500-AI-Agents-Projects
./references/AINEWPROJECT
./references/AirSim
./references/Archon
./references/AutoGPT
./references/BitNet
./references/BlenderMCP-AI-AGNO-agent
./references/BlenderMCP-aasurjya
./references/CLI-Anything
./references/CodexBar
./references/CogVideo
./references/Cognizant-Early-Engagement
./references/ComfyUI
./references/DataFlex
./references/DataFlex-Doc
./references/EvoSkill
./references/Flowise
./references/Fooocus
./references/GAIA
./references/GPTs
./references/GitHub-Chinese-Top-Charts
./references/GitHub-Chinese-Top-Charts-2
./references/GitTaskBench
./references/LibreChat
./references/MOSS-TTS-Nano
./references/MOSS-TTS-Nano-Reader
./references/MOSS-TTS-Nano-Win
./references/MinerU
./references/MinerU-Diffusion
./references/MinerU-Document-Explorer
./references/Open-AutoGLM
./references/Open-AutoGLM-Android
./references/Open-AutoGLM-Hybrid
./references/Open-AutoGLM-SIGI
./references/OpenClaw_BlenderMCP-Skill
./references/OpenHands
./references/OpenHarness
./references/PandaWiki
./references/RepoGenesis
./references/RepoMaster
./references/SWE-agent
./references/Seedance2-Storyboard-Generator
./references/SuperAGI
./references/Toonflow-app
./references/Toonflow-app-herooutput
./references/Toonflow-cuiyucheng
./references/Toonflow-web
./references/TrendRadar
./references/agent-browser
./references/agent-skill-creator
./references/agent-skills-md
./references/agenta
./references/agentskills
./references/agi
./references/ai-shotlive
./references/aider
./references/andrej-karpathy-skills
./references/antigravity-awesome-skills
./references/anything-llm
./references/architecture.of.internet-product
./references/autoclip
./references/autoclip_mvp
./references/autoclipper-pt-local
./references/autogen
./references/autoresearch
./references/awesome-ai-agents
./references/awesome-design-md
./references/awesome-design-md-pre-paywall
./references/awesome-design-md-skye
./references/awesome-mcp-servers
./references/awesome-mcp-servers-2
./references/big-AGI
./references/blender-mcp-ahujasid
./references/browser-harness
./references/browser-use
./references/camel
./references/ccusage
./references/claude-code-local
./references/claude-howto
./references/claude-memory-compiler
./references/cline
./references/continue
./references/crawl4ai
./references/crewAI
./references/darwin-skill
./references/deer-flow
./references/dify
./references/dspy
./references/easy-vibe
./references/everything-claude-code
./references/firecrawl
./references/get-shit-done
./references/giskard
./references/godogen
./references/gpt4all
./references/gpt4free
./references/gpt_academic
./references/graphify
./references/graphrag
./references/happy-cli
./references/haystack
./references/heima-ruoyi-vue3-ai
./references/hello-agents
./references/hermes-agent
./references/hyperframes
./references/inference-gateway
./references/jan
./references/judgeval
./references/lancedb
./references/langchain-opendataloader-pdf
./references/langflow
./references/langfuse
./references/langgraph
./references/learn-claude-code
./references/litellm
./references/llama.cpp
./references/llama_index
./references/llemonstack
./references/llm-gateway
./references/lobe-chat
./references/localai
./references/marketingskills
./references/math-curve-loaders
./references/mem0
./references/mineru-tianshu
./references/mlc-llm
./references/multica
./references/nanoGPT
./references/oh-my-codex
./references/ollama
./references/onnxruntime-genai
./references/open-webui
./references/openOii
./references/openOii-doubao
./references/openai-codex
./references/openai-codex-plugin-cc
./references/openai-skills
./references/openalgo
./references/openclaw
./references/opencow
./references/opendataloader-pdf
./references/opendataloader_docker
./references/openllmetry
./references/opik
./references/parlant
./references/phoenix
./references/playwright-mcp
./references/promptfoo
./references/pskoett-ai-skills
./references/qdrant
./references/ragflow
./references/ruoyi-admin
./references/ruoyi-ai-ageerle
./references/ruoyi-ai-ryu-shen
./references/ruoyi-element-ai
./references/ruoyi-vue-pro
./references/ruoyi-web
./references/see-through
./references/self-improving-agent
./references/sglang
./references/sim
./references/skill-sample-nodejs-college-finder
./references/skyvern
./references/stagehand
./references/supergemma4-26b-abliterated-multimodal-nvfp4
./references/supermemory
./references/tabby
./references/tetsuo.26
./references/toonflow
./references/uptrain
./references/vision-agent
./references/vllm
./references/yudao-cloud
./releases
./scripts
./scripts/acceptance
./services
./services/artifact_registry_service
./services/code_review_gate_service
./services/design_system_service
./services/repo_memory_service
./services/service_control 2
./services/skill_store_service
./services/universal_registry 2
./services/workflow_store_service
./vnpy
./vnpy/.git
./vnpy/.github
./vnpy/docs
./vnpy/examples
./vnpy/tests
./vnpy/vnpy
```

## 3. Duplicate / Nested Project Roots

```text
Potential desktop roots:
./apps/desktop
./archive/quarantine/nested_core-platform_20260425-100633/apps/desktop
./core-platform/apps/desktop
./references/lobe-chat/apps/desktop
./references/multica/apps/desktop

Potential services roots:
./OpenHands/enterprise/server/services
./OpenHands/enterprise/tests/unit/server/services
./OpenHands/frontend/__tests__/services
./OpenHands/frontend/src/services
./OpenHands/openhands/app_server/services
./OpenHands/openhands/server/services
./OpenHands/tests/unit/server/services
./archive/quarantine/nested_core-platform_20260425-100633/apps/desktop/bundle/backend/services
./core-platform/apps/desktop/src-tauri/target/debug/_up_/_up_/_up_/services
./core-platform/services
./langflow/src/backend/base/langflow/agentic/services
./langflow/src/backend/base/langflow/services
./langflow/src/backend/base/langflow/tests/services
./langflow/src/backend/tests/unit/agentic/services
./langflow/src/backend/tests/unit/services
./langflow/src/frontend/src/controllers/API/services
./langflow/src/lfx/src/lfx/services
./langflow/src/lfx/tests/unit/services
./references/AINEWPROJECT/web/admin/src/services
./references/Archon/packages/core/src/services
./references/AutoGPT/autogpt_platform/frontend/src/services
./references/ComfyUI/api_server/services
./references/ComfyUI/app/assets/services
./references/ComfyUI/tests-unit/assets_test/services
./references/Flowise/packages/server/src/enterprise/services
./references/Flowise/packages/server/src/services
./references/GitTaskBench/OpenHands/frontend/__tests__/services
./references/GitTaskBench/OpenHands/frontend/src/services
./references/LibreChat/api/server/services
./references/LibreChat/api/test/services
./references/OpenHands/enterprise/server/services
./references/OpenHands/enterprise/tests/unit/server/services
./references/OpenHands/frontend/__tests__/services
./references/OpenHands/frontend/src/services
./references/OpenHands/openhands/app_server/services
./references/OpenHands/openhands/server/services
./references/OpenHands/tests/unit/server/services
./references/OpenHarness/src/openharness/services
./references/PandaWiki/web/admin/src/services
./references/RepoMaster/src/services
./references/TrendRadar/mcp_server/services
./references/agenta/api/ee/src/services
./references/agenta/api/ee/tests/pytest/unit/services
./references/agenta/api/oss/src/services
./references/agenta/hosting/railway/oss/services
./references/agenta/services
./references/agenta/web/ee/src/services
./references/agenta/web/oss/src/services
./references/ai-shotlive/server/src/services
./references/ai-shotlive/services
./references/autoclip/backend/services
./references/autoclip/frontend/src/services
./references/autoclip_mvp/frontend/src/services
./references/camel/camel/services
./references/camel/examples/services
./references/camel/services
./references/camel/test/services
./references/cline/src/services
./references/cline/src/shared/services
./references/cline/src/test/services
./references/cline/webview-ui/src/services
./references/continue/extensions/cli/src/__mocks__/services
./references/continue/extensions/cli/src/services
./references/continue/extensions/intellij/src/main/kotlin/com/github/continuedev/continueintellijextension/services
./references/dify/api/services
./references/dify/api/tests/integration_tests/services
./references/dify/api/tests/test_containers_integration_tests/services
./references/dify/api/tests/unit_tests/services
./references/dify/web/app/components/workflow/collaboration/services
./references/firecrawl/apps/api/src/services
./references/hello-agents/Co-creation-projects/Apricity-InnocoreAI/services
./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/src/services
./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/frontend/src/services
./references/hello-agents/Co-creation-projects/lll0807-CodeTutorAgent/programmer/services
./references/hello-agents/Co-creation-projects/usernamedadad-AutoFlow/backend/app/services
./references/hello-agents/Co-creation-projects/usernamedadad-AutoFlow/frontend/src/services
./references/hello-agents/code/chapter13/helloagents-trip-planner/backend/app/services
./references/hello-agents/code/chapter13/helloagents-trip-planner/frontend/src/services
./references/hello-agents/code/chapter14/helloagents-deepresearch/backend/src/services
./references/hello-agents/code/chapter14/helloagents-deepresearch/frontend/src/services
./references/hyperframes/packages/engine/src/services
./references/hyperframes/packages/producer/src/services
./references/jan/web-app/src/services
./references/langflow/src/backend/base/langflow/agentic/services
./references/langflow/src/backend/base/langflow/services
./references/langflow/src/backend/base/langflow/tests/services
./references/langflow/src/backend/tests/unit/agentic/services
./references/langflow/src/backend/tests/unit/services
./references/langflow/src/frontend/src/controllers/API/services
./references/langflow/src/lfx/src/lfx/services
./references/langflow/src/lfx/tests/unit/services
./references/langfuse/packages/shared/src/server/services
./references/langfuse/web/src/server/api/services
./references/langfuse/worker/src/services
./references/llama.cpp/tools/server/webui/src/lib/services
./references/llemonstack/services
./references/llemonstack/src/core/services
./references/lobe-chat/apps/desktop/src/main/services
./references/lobe-chat/packages/memory-user-memory/src/services
./references/lobe-chat/packages/openapi/src/services
./references/lobe-chat/src/business/client/services
./references/lobe-chat/src/server/services
./references/lobe-chat/src/services
./references/localai/core/services
./references/onnxruntime-genai/src/java/src/test/resources/META-INF/services
./references/openOii/backend/app/services
./references/openOii/frontend/app/services
./references/openalgo/services
./references/opencow/electron/services
./references/opencow/tests/unit/services
./references/opik/apps/opik-backend/opik-telemetry-extension/src/main/resources/META-INF/services
./references/opik/apps/opik-guardrails-backend/opik_guardrails/services
./references/opik/apps/opik-guardrails-backend/tests/unit/services
./references/parlant/src/parlant/core/services
./references/parlant/tests/core/stable/services
./references/phoenix/internal_docs/vignettes/json-jsonb-demo/src/services
./references/promptfoo/src/server/services
./references/promptfoo/test/server/services
./references/ragflow/agent/sandbox/executor_manager/services
./references/ragflow/api/apps/services
./references/ragflow/api/db/services
./references/ragflow/memory/services
./references/ragflow/test/unit_test/api/db/services
./references/ragflow/web/src/services
./references/ruoyi-vue-pro/sql/dm/flowable-patch/src/main/resources/META-INF/services
./references/ruoyi-vue-pro/yudao-module-system/src/main/resources/META-INF/services
./references/skyvern/skyvern/forge/sdk/services
./references/skyvern/skyvern/services
./references/skyvern/tests/unit/services
./references/stagehand/packages/server-v4/src/services
./references/tabby/crates/tabby/src/services
./references/yudao-cloud/sql/dm/flowable-patch/src/main/resources/META-INF/services
./references/yudao-cloud/yudao-module-system/yudao-module-system-server/src/main/resources/META-INF/services
./services

Potential scripts roots:
./LLaVA-NeXT/llava-critic-r1/EasyR1/scripts
./LLaVA-NeXT/scripts
./LLaVA-OneVision-1.5/ds/scripts
./OpenHands/.github/scripts
./OpenHands/frontend/scripts
./OpenHands/scripts
./Qwen3-VL/qwen-vl-finetune/scripts
./RAG-Anything/scripts
./VoxCPM/scripts
./anything-llm/extras/scripts
./anything-llm/frontend/scripts
./anything-llm/server/utils/AiProviders/perplexity/scripts
./capability-registry/claude-code-best-practice/.claude/hooks/scripts
./capability-registry/claude-code-best-practice/.codex/hooks/scripts
./capability-registry/gstack/browse/scripts
./capability-registry/gstack/scripts
./core-platform/.venv/lib/python3.12/site-packages/accelerate/test_utils/scripts
./core-platform/.venv/lib/python3.12/site-packages/comfyui_frontend_package/static/scripts
./core-platform/apps/desktop/bundle/scripts
./core-platform/apps/desktop/scripts
./core-platform/apps/desktop/src-tauri/resources/scripts
./core-platform/apps/desktop/src-tauri/target/debug/_up_/_up_/_up_/scripts
./core-platform/apps/desktop/src-tauri/target/debug/resources/scripts
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/Resources/resources/scripts
./core-platform/apps/desktop/src-tauri/target/release/resources/scripts
./core-platform/releases/maomiai-desktop-demo/Local AI Platform.app/Contents/Resources/resources/scripts
./core-platform/releases/maomiai-desktop-demo/scripts
./core-platform/scripts
./langflow/scripts
./langflow/src/backend/tests/unit/scripts
./qlib/examples/rl_order_execution/scripts
./qlib/scripts
./references/AINEWPROJECT/web/admin/scripts
./references/AINEWPROJECT/web/packages/icons/scripts
./references/AirSim/ros/src/airsim_ros_pkgs/scripts
./references/AirSim/ros/src/airsim_tutorial_pkgs/scripts
./references/AirSim/ros2/src/airsim_ros_pkgs/scripts
./references/Archon/.archon/scripts
./references/Archon/packages/server/src/scripts
./references/Archon/scripts
./references/AutoGPT/.claude/skills/orchestrate/scripts
./references/AutoGPT/.github/scripts
./references/AutoGPT/.github/workflows/scripts
./references/AutoGPT/autogpt_platform/backend/scripts
./references/AutoGPT/autogpt_platform/frontend/scripts
./references/AutoGPT/autogpt_platform/frontend/src/services/scripts
./references/AutoGPT/classic/original_autogpt/scripts
./references/CLI-Anything/.github/scripts
./references/CLI-Anything/cli-anything-plugin/scripts
./references/CLI-Anything/codex-skill/scripts
./references/CLI-Anything/safari/agent-harness/scripts
./references/CogVideo/.venv/lib/python3.12/site-packages/accelerate/test_utils/scripts
./references/CogVideo/finetune/scripts
./references/ComfyUI/.github/scripts
./references/ComfyUI/.venv/lib/python3.12/site-packages/comfyui_frontend_package/static/scripts
./references/EvoSkill/.claude/skills/skill-creator/scripts
./references/EvoSkill/scripts
./references/GitHub-Chinese-Top-Charts-2/scripts
./references/GitHub-Chinese-Top-Charts/content/scripts
./references/GitTaskBench/Aider/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/EDA/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/agent_bench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/aider_bench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/biocoder/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/bird/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/browsing_delegation/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/commit0/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/discoverybench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/gaia/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/gorilla/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/gpqa/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/humanevalfix/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/logic_reasoning/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/miniwob/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/mint/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/ml_bench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/scienceagentbench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/swe_bench/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/testgeneval/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/the_agent_company/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/toolqa/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/visualwebarena/scripts
./references/GitTaskBench/OpenHands/evaluation/benchmarks/webarena/scripts
./references/GitTaskBench/OpenHands/evaluation/integration_tests/scripts
./references/GitTaskBench/OpenHands/evaluation/utils/scripts
./references/GitTaskBench/OpenHands/frontend/scripts
./references/GitTaskBench/code_base/PyPDF2/.github/scripts
./references/GitTaskBench/code_base/PyPDF2/tests/scripts
./references/GitTaskBench/code_base/SpeechBrain/recipes/Aishell1Mix/separation/scripts
./references/GitTaskBench/code_base/SuperResolution/scripts
./references/LibreChat/client/scripts
./references/MinerU-Diffusion/scripts
./references/MinerU-Document-Explorer/scripts
./references/Open-AutoGLM/scripts
./references/OpenClaw_BlenderMCP-Skill/scripts
./references/OpenHands/.github/scripts
./references/OpenHands/frontend/scripts
./references/OpenHands/scripts
./references/OpenHarness/scripts
./references/PandaWiki/web/admin/scripts
./references/PandaWiki/web/packages/icons/scripts
./references/RepoGenesis/eval_harness/scripts
./references/SuperAGI/tgwui/scripts
./references/Toonflow-app-herooutput/scripts
./references/Toonflow-app/scripts
./references/Toonflow-web/scripts
./references/agent-browser/examples/environments/scripts
./references/agent-browser/scripts
./references/agent-skill-creator/references/examples/stock-analyzer/scripts
./references/agent-skill-creator/scripts
./references/agenta/docs/scripts
./references/agenta/examples/python/RAG_QA_chatbot/scripts
./references/agenta/hosting/railway/oss/scripts
./references/agenta/sdk/scripts
./references/agenta/web/tests/playwright/scripts
./references/agi/.github/scripts
./references/ai-shotlive/scripts
./references/ai-shotlive/server/src/scripts
./references/aider/scripts
./references/antigravity-awesome-skills/apps/web-app/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/007/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/agent-orchestrator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ai-studio-image/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/android_ui_verification/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/api-patterns/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-audience-analysis/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-brand-reputation-monitoring/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-competitor-intelligence/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-content-analytics/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-ecommerce/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-influencer-discovery/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-lead-generation/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-market-research/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-trend-analysis/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/apify-ultimate-scraper/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/app-store-changelog/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/audio-transcriber/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/claude-monitor/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/content-creator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/context-agent/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/context-guardian/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/database-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/docx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/docx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/frontend-slides/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/geo-fundamentals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/git-pushing/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/helm-chart-scaffolding/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/hugging-face-community-evals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/hugging-face-jobs/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/hugging-face-model-trainer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/hugging-face-paper-publisher/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/hugging-face-vision-trainer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/i18n-localization/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/instagram/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/junta-leiloeiros/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/landing-page-generator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/last30days/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-avaliacao/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-edital/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-ia/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-juridico/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-mercado/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/leiloeiro-risco/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/lint-and-validate/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/loki-mode/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/matematico-tao/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/mcp-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/mobile-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/monte-carlo-push-ingestion/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/monte-carlo-validation-notebook/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/pdf-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/performance-profiling/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/pipecat-friday-agent/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/planning-with-files/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/pptx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/pptx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/product-manager-toolkit/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/prompt-engineering-patterns/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/senior-architect/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/senior-frontend/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/senior-fullstack/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/seo-fundamentals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/shopify-development/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/skill-installer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/skill-sentinel/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/stability-ai/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/telegram/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/typescript-expert/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/ui-ux-pro-max/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/videodb/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/vulnerability-scanner/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/web-artifacts-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/webapp-testing/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/whatsapp-cloud-api/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/youtube-summarizer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/007/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/agent-orchestrator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ai-studio-image/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/android_ui_verification/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/api-patterns/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-audience-analysis/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-brand-reputation-monitoring/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-competitor-intelligence/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-content-analytics/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-influencer-discovery/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-lead-generation/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-market-research/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-trend-analysis/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/apify-ultimate-scraper/reference/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/app-store-changelog/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/audio-transcriber/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/claude-monitor/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/content-creator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/context-agent/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/context-guardian/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/database-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/docx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/docx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/frontend-slides/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/geo-fundamentals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/git-pushing/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/helm-chart-scaffolding/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/hugging-face-community-evals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/hugging-face-jobs/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/hugging-face-model-trainer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/hugging-face-paper-publisher/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/hugging-face-vision-trainer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/i18n-localization/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/instagram/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/junta-leiloeiros/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/landing-page-generator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-avaliacao/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-edital/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-ia/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-juridico/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-mercado/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/leiloeiro-risco/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/lint-and-validate/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/matematico-tao/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/mcp-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/mobile-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/monte-carlo-push-ingestion/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/monte-carlo-validation-notebook/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/pdf-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/performance-profiling/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/pipecat-friday-agent/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/planning-with-files/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/pptx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/pptx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/product-manager-toolkit/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/prompt-engineering-patterns/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/senior-architect/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/senior-frontend/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/senior-fullstack/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/seo-fundamentals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/shopify-development/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/skill-installer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/skill-sentinel/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/stability-ai/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/telegram/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/typescript-expert/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/ui-ux-pro-max/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/videodb/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/vulnerability-scanner/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/web-artifacts-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/webapp-testing/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/whatsapp-cloud-api/scripts
./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/youtube-summarizer/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-agent-architect/skills/mcp-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-architecture-design/skills/senior-architect/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-automation-builder/skills/mcp-builder/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-creative-director/skills/content-creator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/skills/docx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/skills/docx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/skills/pdf-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/skills/pptx-official/ooxml/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-documents-presentations/skills/pptx-official/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-essentials/skills/git-pushing/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-essentials/skills/lint-and-validate/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/api-patterns/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/database-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-full-stack-developer/skills/senior-fullstack/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-marketing-growth/skills/content-creator/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-security-engineer/skills/vulnerability-scanner/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-seo-specialist/skills/seo-fundamentals/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-startup-founder/skills/product-manager-toolkit/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-typescript-javascript/skills/typescript-expert/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-designer/skills/mobile-design/scripts
./references/antigravity-awesome-skills/plugins/antigravity-bundle-web-designer/skills/ui-ux-pro-max/scripts
./references/antigravity-awesome-skills/scripts
./references/antigravity-awesome-skills/skill_categorization/tools/scripts
./references/antigravity-awesome-skills/skills/007/scripts
./references/antigravity-awesome-skills/skills/agent-orchestrator/scripts
./references/antigravity-awesome-skills/skills/ai-studio-image/scripts
./references/antigravity-awesome-skills/skills/android_ui_verification/scripts
./references/antigravity-awesome-skills/skills/api-patterns/scripts
./references/antigravity-awesome-skills/skills/apify-audience-analysis/reference/scripts
./references/antigravity-awesome-skills/skills/apify-brand-reputation-monitoring/reference/scripts
./references/antigravity-awesome-skills/skills/apify-competitor-intelligence/reference/scripts
./references/antigravity-awesome-skills/skills/apify-content-analytics/reference/scripts
./references/antigravity-awesome-skills/skills/apify-ecommerce/reference/scripts
./references/antigravity-awesome-skills/skills/apify-influencer-discovery/reference/scripts
./references/antigravity-awesome-skills/skills/apify-lead-generation/reference/scripts
./references/antigravity-awesome-skills/skills/apify-market-research/reference/scripts
./references/antigravity-awesome-skills/skills/apify-trend-analysis/reference/scripts
./references/antigravity-awesome-skills/skills/apify-ultimate-scraper/reference/scripts
./references/antigravity-awesome-skills/skills/app-store-changelog/scripts
./references/antigravity-awesome-skills/skills/audio-transcriber/scripts
./references/antigravity-awesome-skills/skills/claude-monitor/scripts
./references/antigravity-awesome-skills/skills/content-creator/scripts
./references/antigravity-awesome-skills/skills/context-agent/scripts
./references/antigravity-awesome-skills/skills/context-guardian/scripts
./references/antigravity-awesome-skills/skills/database-design/scripts
./references/antigravity-awesome-skills/skills/diary/scripts
./references/antigravity-awesome-skills/skills/docx-official/ooxml/scripts
./references/antigravity-awesome-skills/skills/docx-official/scripts
./references/antigravity-awesome-skills/skills/frontend-slides/scripts
./references/antigravity-awesome-skills/skills/geo-fundamentals/scripts
./references/antigravity-awesome-skills/skills/git-pushing/scripts
./references/antigravity-awesome-skills/skills/helm-chart-scaffolding/scripts
./references/antigravity-awesome-skills/skills/hugging-face-community-evals/scripts
./references/antigravity-awesome-skills/skills/hugging-face-jobs/scripts
./references/antigravity-awesome-skills/skills/hugging-face-model-trainer/scripts
./references/antigravity-awesome-skills/skills/hugging-face-paper-publisher/scripts
./references/antigravity-awesome-skills/skills/hugging-face-vision-trainer/scripts
./references/antigravity-awesome-skills/skills/i18n-localization/scripts
./references/antigravity-awesome-skills/skills/instagram/scripts
./references/antigravity-awesome-skills/skills/junta-leiloeiros/scripts
./references/antigravity-awesome-skills/skills/landing-page-generator/scripts
./references/antigravity-awesome-skills/skills/last30days/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-avaliacao/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-edital/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-ia/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-juridico/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-mercado/scripts
./references/antigravity-awesome-skills/skills/leiloeiro-risco/scripts
./references/antigravity-awesome-skills/skills/lint-and-validate/scripts
./references/antigravity-awesome-skills/skills/loki-mode/scripts
./references/antigravity-awesome-skills/skills/matematico-tao/scripts
./references/antigravity-awesome-skills/skills/mcp-builder/scripts
./references/antigravity-awesome-skills/skills/mobile-design/scripts
./references/antigravity-awesome-skills/skills/monte-carlo-push-ingestion/scripts
./references/antigravity-awesome-skills/skills/monte-carlo-validation-notebook/scripts
./references/antigravity-awesome-skills/skills/notebooklm/scripts
./references/antigravity-awesome-skills/skills/pdf-official/scripts
./references/antigravity-awesome-skills/skills/performance-profiling/scripts
./references/antigravity-awesome-skills/skills/pipecat-friday-agent/scripts
./references/antigravity-awesome-skills/skills/planning-with-files/scripts
./references/antigravity-awesome-skills/skills/pptx-official/ooxml/scripts
./references/antigravity-awesome-skills/skills/pptx-official/scripts
./references/antigravity-awesome-skills/skills/product-manager-toolkit/scripts
./references/antigravity-awesome-skills/skills/prompt-engineering-patterns/scripts
./references/antigravity-awesome-skills/skills/senior-architect/scripts
./references/antigravity-awesome-skills/skills/senior-frontend/scripts
./references/antigravity-awesome-skills/skills/senior-fullstack/scripts
./references/antigravity-awesome-skills/skills/seo-fundamentals/scripts
./references/antigravity-awesome-skills/skills/shopify-development/scripts
./references/antigravity-awesome-skills/skills/skill-creator/scripts
./references/antigravity-awesome-skills/skills/skill-installer/scripts
./references/antigravity-awesome-skills/skills/skill-sentinel/scripts
./references/antigravity-awesome-skills/skills/stability-ai/scripts
./references/antigravity-awesome-skills/skills/telegram/scripts
./references/antigravity-awesome-skills/skills/typescript-expert/scripts
./references/antigravity-awesome-skills/skills/ui-ux-pro-max/scripts
./references/antigravity-awesome-skills/skills/videodb/scripts
./references/antigravity-awesome-skills/skills/vulnerability-scanner/scripts
./references/antigravity-awesome-skills/skills/web-artifacts-builder/scripts
./references/antigravity-awesome-skills/skills/webapp-testing/scripts
./references/antigravity-awesome-skills/skills/whatsapp-cloud-api/scripts
./references/antigravity-awesome-skills/skills/youtube-summarizer/scripts
./references/antigravity-awesome-skills/tools/scripts
./references/anything-llm/extras/scripts
./references/anything-llm/frontend/scripts
./references/anything-llm/server/utils/AiProviders/perplexity/scripts
./references/autoclip/backend/scripts
./references/autoclip/frontend/node_modules/ajv/scripts
./references/autoclip/scripts
./references/awesome-design-md-skye/scripts
./references/big-AGI/.claude/scripts
./references/browser-use/tests/scripts
./references/camel/.camel/skills/docs-incremental-update/scripts
./references/camel/.camel/skills/skill-creator/scripts
./references/camel/docs/mintlify/scripts
./references/camel/examples/toolkits/skill_toolkit_example/.camel/skills/data-analyzer/scripts
./references/ccusage/apps/ccusage/scripts
./references/claude-code-local/scripts
./references/claude-howto/03-skills/code-review/scripts
./references/claude-howto/03-skills/refactor/scripts
./references/claude-howto/07-plugins/devops-automation/scripts
./references/claude-howto/scripts
./references/claude-howto/uk/03-skills/code-review/scripts
./references/claude-howto/uk/03-skills/refactor/scripts
./references/claude-howto/uk/07-plugins/devops-automation/scripts
./references/claude-howto/uk/scripts
./references/claude-howto/vi/07-plugins/devops-automation/scripts
./references/claude-howto/zh/scripts
./references/claude-memory-compiler/scripts
./references/cline/.github/scripts
./references/cline/cli/scripts
./references/cline/scripts
./references/continue/actions/general-review/scripts
./references/continue/extensions/cli/scripts
./references/continue/extensions/vscode/scripts
./references/continue/packages/config-yaml/src/scripts
./references/continue/scripts
./references/crawl4ai/docs/examples/c4a_script/tutorial/scripts
./references/crawl4ai/docs/md_v2/apps/c4a-script/scripts
./references/crawl4ai/scripts
./references/crewAI/lib/crewai/tests/skills/fixtures/valid-skill/scripts
./references/darwin-skill/scripts
./references/deer-flow/.agent/skills/smoke-test/scripts
./references/deer-flow/frontend/scripts
./references/deer-flow/scripts
./references/deer-flow/skills/public/chart-visualization/scripts
./references/deer-flow/skills/public/claude-to-deerflow/scripts
./references/deer-flow/skills/public/data-analysis/scripts
./references/deer-flow/skills/public/find-skills/scripts
./references/deer-flow/skills/public/github-deep-research/scripts
./references/deer-flow/skills/public/image-generation/scripts
./references/deer-flow/skills/public/podcast-generation/scripts
./references/deer-flow/skills/public/ppt-generation/scripts
./references/deer-flow/skills/public/skill-creator/scripts
./references/deer-flow/skills/public/systematic-literature-review/scripts
./references/deer-flow/skills/public/vercel-deploy-claimable/scripts
./references/deer-flow/skills/public/video-generation/scripts
./references/dify/.github/scripts
./references/dify/e2e/scripts
./references/dify/packages/iconify-collections/scripts
./references/dify/scripts
./references/dify/sdks/nodejs-client/scripts
./references/dify/web/scripts
./references/dspy/docs/scripts
./references/easy-vibe/scripts
./references/everything-claude-code/.kiro/scripts
./references/everything-claude-code/scripts
./references/everything-claude-code/skills/continuous-learning-v2/scripts
./references/everything-claude-code/skills/rules-distill/scripts
./references/everything-claude-code/skills/skill-comply/scripts
./references/everything-claude-code/skills/skill-stocktake/scripts
./references/everything-claude-code/skills/videodb/scripts
./references/everything-claude-code/tests/scripts
./references/firecrawl/.github/scripts
./references/firecrawl/apps/redis/scripts
./references/firecrawl/examples/blog-articles/scheduling_scrapers/scripts
./references/get-shit-done/scripts
./references/get-shit-done/sdk/scripts
./references/godogen/claude/skills/visual-qa/scripts
./references/godogen/codex/skills/visual-qa/scripts
./references/gpt4all/gpt4all-bindings/typescript/scripts
./references/gpt4free/scripts
./references/graphrag/docs/scripts
./references/graphrag/scripts
./references/happy-cli/scripts
./references/haystack/docs-website/scripts
./references/haystack/scripts
./references/heima-ruoyi-vue3-ai/01-基础篇/资料/02-入门案例/客达天下页面原型/客达天下页面原型/resources/scripts
./references/heima-ruoyi-vue3-ai/01-基础篇/资料/04-二次开发/苍穹外卖_管理端_页面原型/resources/scripts
./references/hello-agents/Co-creation-projects/JJason-DeepCastAgent/backend/scripts
./references/hello-agents/Co-creation-projects/Shawnxyxy-HealthRecordAgent/backend/scripts
./references/hello-agents/code/chapter15/Helloagents-AI-Town/helloagents-ai-town/scripts
./references/hermes-agent/optional-skills/blockchain/base/scripts
./references/hermes-agent/optional-skills/blockchain/solana/scripts
./references/hermes-agent/optional-skills/creative/meme-generation/scripts
./references/hermes-agent/optional-skills/mcp/fastmcp/scripts
./references/hermes-agent/optional-skills/migration/openclaw-migration/scripts
./references/hermes-agent/optional-skills/productivity/canvas/scripts
./references/hermes-agent/optional-skills/productivity/memento-flashcards/scripts
./references/hermes-agent/optional-skills/productivity/telephony/scripts
./references/hermes-agent/optional-skills/research/domain-intel/scripts
./references/hermes-agent/optional-skills/research/duckduckgo-search/scripts
./references/hermes-agent/optional-skills/research/gitnexus-explorer/scripts
./references/hermes-agent/optional-skills/security/oss-forensics/scripts
./references/hermes-agent/scripts
./references/hermes-agent/skills/creative/excalidraw/scripts
./references/hermes-agent/skills/creative/manim-video/scripts
./references/hermes-agent/skills/creative/p5js/scripts
./references/hermes-agent/skills/github/github-auth/scripts
./references/hermes-agent/skills/leisure/find-nearby/scripts
./references/hermes-agent/skills/media/youtube-content/scripts
./references/hermes-agent/skills/productivity/google-workspace/scripts
./references/hermes-agent/skills/productivity/ocr-and-documents/scripts
./references/hermes-agent/skills/productivity/powerpoint/scripts
./references/hermes-agent/skills/red-teaming/godmode/scripts
./references/hermes-agent/skills/research/arxiv/scripts
./references/hermes-agent/skills/research/polymarket/scripts
./references/hermes-agent/website/scripts
./references/hyperframes/packages/cli/scripts
./references/hyperframes/packages/core/scripts
./references/hyperframes/packages/engine/scripts
./references/hyperframes/packages/producer/scripts
./references/hyperframes/scripts
./references/hyperframes/skills/gsap/scripts
./references/hyperframes/skills/hyperframes/scripts
./references/inference-gateway/scripts
./references/jan/.github/scripts
./references/jan/autoqa/scripts
./references/jan/scripts
./references/judgeval/scripts
./references/langflow/scripts
./references/langflow/src/backend/tests/unit/scripts
./references/langfuse/.agents/skills/add-model-price/scripts
./references/langfuse/.agents/skills/pnpm-upgrade-package/scripts
./references/langfuse/packages/shared/clickhouse/scripts
./references/langfuse/packages/shared/scripts
./references/langfuse/scripts
./references/langfuse/worker/src/scripts
./references/langgraph/.github/scripts
./references/learn-claude-code/skills/agent-builder/scripts
./references/learn-claude-code/web/scripts
./references/litellm/.github/scripts
./references/litellm/scripts
./references/litellm/ui/litellm-dashboard/scripts
./references/llama.cpp/examples/model-conversion/scripts
./references/llama.cpp/gguf-py/gguf/scripts
./references/llama.cpp/scripts
./references/llama.cpp/tools/server/webui/scripts
./references/llama_index/docs/scripts
./references/llama_index/scripts
./references/llemonstack/scripts
./references/lobe-chat/.agents/skills/local-testing/scripts
./references/lobe-chat/.github/scripts
./references/lobe-chat/apps/desktop/scripts
./references/lobe-chat/apps/device-gateway/scripts
./references/lobe-chat/e2e/scripts
./references/lobe-chat/packages/openapi/scripts
./references/lobe-chat/scripts
./references/localai/scripts
./references/marketingskills/.github/scripts
./references/mem0/mem0-plugin/scripts
./references/mem0/mem0-plugin/skills/mem0/scripts
./references/mem0/openclaw/scripts
./references/mem0/scripts
./references/mem0/server/scripts
./references/mem0/skills/mem0/scripts
./references/mineru-tianshu/scripts
./references/mlc-llm/scripts
./references/multica/apps/desktop/scripts
./references/multica/scripts
./references/oh-my-codex/.github/scripts
./references/oh-my-codex/src/scripts
./references/ollama/scripts
./references/onnxruntime-genai/tools/ci_build/github/linux/docker/inference/aarch64/default/cpu/scripts
./references/onnxruntime-genai/tools/ci_build/github/linux/docker/manylinux/scripts
./references/open-webui/scripts
./references/openai-codex-plugin-cc/plugins/codex/scripts
./references/openai-codex-plugin-cc/scripts
./references/openai-codex/.codex/skills/babysit-pr/scripts
./references/openai-codex/.github/scripts
./references/openai-codex/codex-cli/scripts
./references/openai-codex/codex-rs/app-server-test-client/scripts
./references/openai-codex/codex-rs/config/scripts
./references/openai-codex/codex-rs/scripts
./references/openai-codex/codex-rs/skills/src/assets/samples/imagegen/scripts
./references/openai-codex/codex-rs/skills/src/assets/samples/openai-docs/scripts
./references/openai-codex/codex-rs/skills/src/assets/samples/plugin-creator/scripts
./references/openai-codex/codex-rs/skills/src/assets/samples/skill-creator/scripts
./references/openai-codex/codex-rs/skills/src/assets/samples/skill-installer/scripts
./references/openai-codex/codex-rs/thread-store/scripts
./references/openai-codex/scripts
./references/openai-codex/sdk/python/scripts
./references/openai-skills/skills/.curated/chatgpt-apps/scripts
./references/openai-skills/skills/.curated/doc/scripts
./references/openai-skills/skills/.curated/figma-code-connect-components/scripts
./references/openai-skills/skills/.curated/figma-create-design-system-rules/scripts
./references/openai-skills/skills/.curated/figma-generate-library/scripts
./references/openai-skills/skills/.curated/gh-address-comments/scripts
./references/openai-skills/skills/.curated/gh-fix-ci/scripts
./references/openai-skills/skills/.curated/jupyter-notebook/scripts
./references/openai-skills/skills/.curated/openai-docs/scripts
./references/openai-skills/skills/.curated/playwright/scripts
./references/openai-skills/skills/.curated/screenshot/scripts
./references/openai-skills/skills/.curated/security-ownership-map/scripts
./references/openai-skills/skills/.curated/sora/scripts
./references/openai-skills/skills/.curated/speech/scripts
./references/openai-skills/skills/.curated/transcribe/scripts
./references/openai-skills/skills/.curated/vercel-deploy/scripts
./references/openai-skills/skills/.system/imagegen/scripts
./references/openai-skills/skills/.system/openai-docs/scripts
./references/openai-skills/skills/.system/plugin-creator/scripts
./references/openai-skills/skills/.system/skill-creator/scripts
./references/openai-skills/skills/.system/skill-installer/scripts
./references/openalgo/strategies/scripts
./references/openclaw/.agents/skills/openclaw-secret-scanning-maintainer/scripts
./references/openclaw/.agents/skills/openclaw-test-heap-leaks/scripts
./references/openclaw/Swabble/scripts
./references/openclaw/apps/android/scripts
./references/openclaw/scripts
./references/openclaw/skills/model-usage/scripts
./references/openclaw/skills/openai-whisper-api/scripts
./references/openclaw/skills/skill-creator/scripts
./references/openclaw/skills/tmux/scripts
./references/openclaw/skills/video-frames/scripts
./references/openclaw/src/scripts
./references/openclaw/test/scripts
./references/opencow/scripts
./references/opendataloader-pdf/node/opendataloader-pdf/scripts
./references/opendataloader-pdf/scripts
./references/opendataloader_docker/scripts
./references/openllmetry/scripts
./references/opik/.github/scripts
./references/opik/apps/opik-backend/data-migrations/1.0.3/scripts
./references/opik/apps/opik-documentation/documentation/scripts
./references/opik/apps/opik-guardrails-backend/scripts
./references/opik/scripts
./references/opik/sdks/opik_optimizer/scripts
./references/parlant/scripts
./references/phoenix/.agents/skills/phoenix-frontend/scripts
./references/phoenix/js/examples/apps/cli-agent-starter-kit/scripts
./references/phoenix/js/scripts
./references/phoenix/packages/phoenix-client/scripts
./references/phoenix/scripts
./references/phoenix/scripts/docker/devops/scripts
./references/phoenix/tutorials/ai_evals_course/hw3_phoenix/scripts
./references/promptfoo/.github/scripts
./references/promptfoo/examples/redteam-api-top-10/scripts
./references/promptfoo/plugins/promptfoo/skills/promptfoo-provider-setup/scripts
./references/promptfoo/plugins/promptfoo/skills/promptfoo-redteam-setup/scripts
./references/promptfoo/scripts
./references/promptfoo/site/scripts
./references/promptfoo/test/scripts
./references/promptfoo/test/smoke/fixtures/scripts
./references/pskoett-ai-skills/.agents/skills/self-improvement/scripts
./references/pskoett-ai-skills/plugin/scripts
./references/pskoett-ai-skills/plugin/skills/context-surfing/scripts
./references/pskoett-ai-skills/plugin/skills/pre-flight-check/scripts
./references/pskoett-ai-skills/plugin/skills/self-improvement/scripts
./references/pskoett-ai-skills/scripts
./references/pskoett-ai-skills/skills/context-surfing/scripts
./references/pskoett-ai-skills/skills/pre-flight-check/scripts
./references/pskoett-ai-skills/skills/self-improvement/scripts
./references/pskoett-ai-skills/skills/skill-tester-ci/scripts
./references/pskoett-ai-skills/skills/skill-tester/scripts
./references/ragflow/agent/sandbox/scripts
./references/ragflow/tools/scripts
./references/ruoyi-admin/scripts
./references/ruoyi-ai-ageerle/ruoyi-admin/src/main/resources/skills/docx/scripts
./references/ruoyi-ai-ageerle/ruoyi-admin/src/main/resources/skills/pdf/scripts
./references/see-through/inference/scripts
./references/see-through/training/scripts
./references/self-improving-agent/scripts
./references/sglang/.claude/skills/sglang-torch-profiler-analysis/scripts
./references/sglang/docs_new/scripts
./references/sglang/python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-ako4all-kernel/scripts
./references/sglang/python/sglang/multimodal_gen/.claude/skills/sglang-diffusion-benchmark-profile/scripts
./references/sglang/python/sglang/multimodal_gen/test/scripts
./references/sglang/scripts
./references/sglang/sgl-model-gateway/bindings/golang/examples/oai_server/scripts
./references/sglang/sgl-model-gateway/scripts
./references/sim/apps/sim/scripts
./references/sim/packages/db/scripts
./references/sim/scripts
./references/skyvern/scripts
./references/skyvern/skyvern-ts/client/scripts
./references/skyvern/skyvern-ts/client/src/api/resources/scripts
./references/skyvern/skyvern/client/scripts
./references/stagehand/packages/core/scripts
./references/stagehand/packages/docs/scripts
./references/stagehand/packages/evals/scripts
./references/stagehand/packages/server-v3/scripts
./references/stagehand/packages/server-v4/scripts
./references/supermemory/packages/memory-graph/scripts
./references/tabby/clients/eclipse/scripts
./references/tabby/clients/tabby-openapi/scripts
./references/tabby/clients/vscode/scripts
./references/toonflow/electron/scripts
./references/vllm/.buildkite/performance-benchmarks/scripts
./references/vllm/.buildkite/scripts
./references/vllm/.github/workflows/scripts
./references/vllm/scripts
./references/vllm/tests/cuda/scripts
./scripts

Potential nested core-platform dirs:
./core-platform
./core-platform/core-platform
```

## 4. Desktop Source Candidates

### apps/desktop

```text
EXISTS

```

### core-platform/apps/desktop

```text
EXISTS
core-platform/apps/desktop/dist/index.html
core-platform/apps/desktop/dist/js/api.js
core-platform/apps/desktop/dist/js/chat-session-manager.js
core-platform/apps/desktop/dist/js/composer-fix.js
core-platform/apps/desktop/dist/js/desktop-chat-stable.js
core-platform/apps/desktop/dist/js/desktop-runtime-stable.js
core-platform/apps/desktop/dist/js/inspector.js
core-platform/apps/desktop/dist/js/navigation-fix.js
core-platform/apps/desktop/dist/js/page-helpers.js
core-platform/apps/desktop/dist/js/services.js
core-platform/apps/desktop/dist/js/state.js
core-platform/apps/desktop/dist/js/tauri-bridge.js
core-platform/apps/desktop/dist/js/utils.js
core-platform/apps/desktop/dist/js/window-bindings.js
core-platform/apps/desktop/dist/main.js
core-platform/apps/desktop/index.html
core-platform/apps/desktop/package.json
core-platform/apps/desktop/src-tauri/tauri.conf.json
core-platform/apps/desktop/src/index.html
core-platform/apps/desktop/src/js/api.js
core-platform/apps/desktop/src/js/auto-start-services.js
core-platform/apps/desktop/src/js/chatgpt-like-ui.js
core-platform/apps/desktop/src/js/inspector.js
core-platform/apps/desktop/src/js/services.js
core-platform/apps/desktop/src/js/state.js
core-platform/apps/desktop/src/js/tauri-bridge.js
core-platform/apps/desktop/src/js/utils.js
core-platform/apps/desktop/src/js/windows-click-model-setup.js
core-platform/apps/desktop/src/main.js

--- src/index.html markers ---
5:  <title>MAOMIAI Desktop</title>
28:      <div>MAOMIAI</div>
32:      <button id="nav-launch" class="hidden-internal hidden-internal" onclick="setView('launch')">🚀 Launch</button>
33:      <button id="nav-brain" class="hidden-internal hidden-internal" onclick="setView('brain')">🧠 Brain Status</button>
34:      <button id="nav-skills" class="hidden-internal hidden-internal" onclick="setView('skills')">🧩 Skill Store</button>
35:      <button id="nav-documents" class="hidden-internal hidden-internal" onclick="setView('documents')">📄 Documents</button>
36:      <button id="nav-workflows" class="hidden-internal hidden-internal" onclick="setView('workflows')">🧬 Workflows</button>
39:      <button id="nav-design-system" class="hidden-internal hidden-internal" onclick="setView('design-system')">🎨 Design System</button>
49:        <div class="top-title">MAOMIAI 本地 AI</div>
53:        <div class="select-pill">本地 AI 已准备</div>
61:        <textarea id="prompt" placeholder="给 MAOMIAI 发送消息，或让它处理文档、检查代码、整理结果..."></textarea>
400:name: MAOMIAI Desktop
402:brand: MAOMIAI
405:# MAOMIAI Desktop Design System
2481:  <script src="./js/windows-click-model-setup.js"></script>
    2483 core-platform/apps/desktop/src/index.html
--- dist/index.html markers ---
5:  <title>MAOMIAI Desktop</title>
14:      <div>MAOMIAI</div>
36:        <div class="top-title">P3 大脑工作台</div>
     978 core-platform/apps/desktop/dist/index.html
```

### core-platform/core-platform/apps/desktop

MISSING

### apps/desktop/bundle/backend/apps/desktop

MISSING

## 5. Service Inventory

### services

```text
services/artifact_registry_service/main.py
services/code_review_gate_service/main.py
services/design_system_service/main.py
services/repo_memory_service/main.py
services/skill_store_service/main.py
services/workflow_store_service/main.py

--- service summary ---
artifact_registry_service | py_files=7 | main.py=YES | app = FastAPI(title="Artifact Registry Service", version="0.3.1-enterprise") 
code_review_gate_service | py_files=7 | main.py=YES | app = FastAPI(title="Code Review Gate Service", version="0.3.1-enterprise") 
design_system_service | py_files=9 | main.py=YES | app = FastAPI(title="Design System Service", version="0.3.1-enterprise") 
repo_memory_service | py_files=7 | main.py=YES | app = FastAPI(title="Repo Memory Service", version="0.3.1-enterprise") 
service_control 2 | py_files=0 | main.py=NO | 
skill_store_service | py_files=8 | main.py=YES | app = FastAPI(title="Skill Store Service", version="0.3.1-enterprise") 
universal_registry 2 | py_files=0 | main.py=NO | 
workflow_store_service | py_files=7 | main.py=YES | app = FastAPI(title="Workflow Store Service", version="0.3.1-enterprise")         "version": "0.3.1-enterprise",         "store_version": store.store_version, 
```

### core-platform/services

```text
core-platform/services/__init__.py
core-platform/services/agent_orchestrator/__init__.py
core-platform/services/agent_orchestrator/main.py
core-platform/services/artifact_registry_service/main.py
core-platform/services/auto_router_service/__init__.py
core-platform/services/code_review_gate_service/main.py
core-platform/services/design_system_service/main.py
core-platform/services/document_ingestion_service/__init__.py
core-platform/services/eval_engine/__init__.py
core-platform/services/eval_engine/main.py
core-platform/services/eval_gateway_service/__init__.py
core-platform/services/model_bootstrap_service/__init__.py
core-platform/services/model_bootstrap_service/main.py
core-platform/services/model_gateway/__init__.py
core-platform/services/model_gateway/main.py
core-platform/services/plugin_manager/__init__.py
core-platform/services/plugin_manager/main.py
core-platform/services/policy_engine_service/__init__.py
core-platform/services/repo_memory_service/main.py
core-platform/services/runtime_execution_service/__init__.py
core-platform/services/service_control/__init__.py
core-platform/services/skill_store_service/main.py
core-platform/services/trace_observability_service/__init__.py
core-platform/services/workflow_store_service/main.py

--- service summary ---
__pycache__ | py_files=0 | main.py=NO | 
agent_orchestrator | py_files=2 | main.py=YES | 
artifact_registry_service | py_files=7 | main.py=YES | app = FastAPI(title="Artifact Registry Service", version="0.3.1-enterprise") 
auto_router_service | py_files=1 | main.py=NO | 
code_agent | py_files=0 | main.py=NO | 
code_review_gate_service | py_files=7 | main.py=YES | app = FastAPI(title="Code Review Gate Service", version="0.3.1-enterprise") 
config_service | py_files=0 | main.py=NO | 
design_system_service | py_files=9 | main.py=YES | app = FastAPI(title="Design System Service", version="0.3.1-enterprise") 
document_ingestion_service | py_files=1 | main.py=NO | 
eval_engine | py_files=2 | main.py=YES | 
eval_gateway_service | py_files=1 | main.py=NO | 
model_bootstrap_service | py_files=3 | main.py=YES | app = FastAPI(title="MAOMIAI Model Bootstrap Service", version=APP_VERSION)         "version": APP_VERSION,         "version": APP_VERSION, 
model_gateway | py_files=2 | main.py=YES | 
plugin_manager | py_files=2 | main.py=YES | 
policy_engine_service | py_files=1 | main.py=NO | 
repo_memory_service | py_files=7 | main.py=YES | app = FastAPI(title="Repo Memory Service", version="0.3.1-enterprise") 
runtime_execution_service | py_files=1 | main.py=NO | 
service_control | py_files=1 | main.py=NO | 
skill_store_service | py_files=8 | main.py=YES | app = FastAPI(title="Skill Store Service", version="0.3.1-enterprise") 
trace_observability_service | py_files=1 | main.py=NO | 
workflow_store_service | py_files=7 | main.py=YES | app = FastAPI(title="Workflow Store Service", version="0.3.1-enterprise")         "version": "0.3.1-enterprise",         "store_version": store.store_version, 
```

### core-platform/core-platform/services

MISSING

### apps/desktop/bundle/backend/services

MISSING

## 6. Required Core Services Check

```text
--- model_gateway ---
FOUND: core-platform/services/model_gateway
core-platform/services/model_gateway/__init__.py
core-platform/services/model_gateway/main.py
PY_COMPILE_OK: core-platform/services/model_gateway/main.py

--- model_bootstrap_service ---
FOUND: core-platform/services/model_bootstrap_service
core-platform/services/model_bootstrap_service/__init__.py
core-platform/services/model_bootstrap_service/app/__init__.py
core-platform/services/model_bootstrap_service/main.py
PY_COMPILE_OK: core-platform/services/model_bootstrap_service/main.py
12:APP_VERSION = "0.1.0-d7-c4-auto-bootstrap"
15:app = FastAPI(title="MAOMIAI Model Bootstrap Service", version=APP_VERSION)
137:        "version": APP_VERSION,
150:        "version": APP_VERSION,
168:    version = run_cmd([ollama, "--version"], timeout=15)
170:    status["ollama_version"] = version

--- skill_store_service ---
FOUND: services/skill_store_service
services/skill_store_service/app/__init__.py
services/skill_store_service/app/models.py
services/skill_store_service/app/parser.py
services/skill_store_service/app/service.py
services/skill_store_service/app/storage.py
services/skill_store_service/app/validation.py
services/skill_store_service/main.py
services/skill_store_service/tests/test_skill_store.py
PY_COMPILE_OK: services/skill_store_service/main.py
43:app = FastAPI(title="Skill Store Service", version="0.3.1-enterprise")
FOUND: core-platform/services/skill_store_service
core-platform/services/skill_store_service/app/__init__.py
core-platform/services/skill_store_service/app/models.py
core-platform/services/skill_store_service/app/parser.py
core-platform/services/skill_store_service/app/service.py
core-platform/services/skill_store_service/app/storage.py
core-platform/services/skill_store_service/app/validation.py
core-platform/services/skill_store_service/main.py
core-platform/services/skill_store_service/tests/test_skill_store.py
PY_COMPILE_OK: core-platform/services/skill_store_service/main.py
43:app = FastAPI(title="Skill Store Service", version="0.3.1-enterprise")

--- artifact_registry_service ---
FOUND: services/artifact_registry_service
services/artifact_registry_service/app/__init__.py
services/artifact_registry_service/app/models.py
services/artifact_registry_service/app/service.py
services/artifact_registry_service/app/storage.py
services/artifact_registry_service/app/validation.py
services/artifact_registry_service/main.py
services/artifact_registry_service/tests/test_artifact_registry.py
PY_COMPILE_OK: services/artifact_registry_service/main.py
40:app = FastAPI(title="Artifact Registry Service", version="0.3.1-enterprise")
FOUND: core-platform/services/artifact_registry_service
core-platform/services/artifact_registry_service/app/__init__.py
core-platform/services/artifact_registry_service/app/models.py
core-platform/services/artifact_registry_service/app/service.py
core-platform/services/artifact_registry_service/app/storage.py
core-platform/services/artifact_registry_service/app/validation.py
core-platform/services/artifact_registry_service/main.py
core-platform/services/artifact_registry_service/tests/test_artifact_registry.py
PY_COMPILE_OK: core-platform/services/artifact_registry_service/main.py
40:app = FastAPI(title="Artifact Registry Service", version="0.3.1-enterprise")

--- code_review_gate_service ---
FOUND: services/code_review_gate_service
services/code_review_gate_service/app/__init__.py
services/code_review_gate_service/app/models.py
services/code_review_gate_service/app/rules.py
services/code_review_gate_service/app/service.py
services/code_review_gate_service/app/storage.py
services/code_review_gate_service/main.py
services/code_review_gate_service/tests/test_code_review_gate.py
PY_COMPILE_OK: services/code_review_gate_service/main.py
37:app = FastAPI(title="Code Review Gate Service", version="0.3.1-enterprise")
FOUND: core-platform/services/code_review_gate_service
core-platform/services/code_review_gate_service/app/__init__.py
core-platform/services/code_review_gate_service/app/models.py
core-platform/services/code_review_gate_service/app/rules.py
core-platform/services/code_review_gate_service/app/service.py
core-platform/services/code_review_gate_service/app/storage.py
core-platform/services/code_review_gate_service/main.py
core-platform/services/code_review_gate_service/tests/test_code_review_gate.py
PY_COMPILE_OK: core-platform/services/code_review_gate_service/main.py
37:app = FastAPI(title="Code Review Gate Service", version="0.3.1-enterprise")

--- repo_memory_service ---
FOUND: services/repo_memory_service
services/repo_memory_service/app/__init__.py
services/repo_memory_service/app/models.py
services/repo_memory_service/app/service.py
services/repo_memory_service/app/storage.py
services/repo_memory_service/app/validation.py
services/repo_memory_service/main.py
services/repo_memory_service/tests/test_repo_memory.py
PY_COMPILE_OK: services/repo_memory_service/main.py
47:app = FastAPI(title="Repo Memory Service", version="0.3.1-enterprise")
FOUND: core-platform/services/repo_memory_service
core-platform/services/repo_memory_service/app/__init__.py
core-platform/services/repo_memory_service/app/models.py
core-platform/services/repo_memory_service/app/service.py
core-platform/services/repo_memory_service/app/storage.py
core-platform/services/repo_memory_service/app/validation.py
core-platform/services/repo_memory_service/main.py
core-platform/services/repo_memory_service/tests/test_repo_memory.py
PY_COMPILE_OK: core-platform/services/repo_memory_service/main.py
47:app = FastAPI(title="Repo Memory Service", version="0.3.1-enterprise")

--- workflow_store_service ---
FOUND: services/workflow_store_service
services/workflow_store_service/app/__init__.py
services/workflow_store_service/app/models.py
services/workflow_store_service/app/service.py
services/workflow_store_service/app/storage.py
services/workflow_store_service/app/validation.py
services/workflow_store_service/main.py
services/workflow_store_service/tests/test_workflow_store.py
PY_COMPILE_OK: services/workflow_store_service/main.py
45:app = FastAPI(title="Workflow Store Service", version="0.3.1-enterprise")
66:        "version": "0.3.1-enterprise",
67:        "store_version": store.store_version,
FOUND: core-platform/services/workflow_store_service
core-platform/services/workflow_store_service/app/__init__.py
core-platform/services/workflow_store_service/app/models.py
core-platform/services/workflow_store_service/app/service.py
core-platform/services/workflow_store_service/app/storage.py
core-platform/services/workflow_store_service/app/validation.py
core-platform/services/workflow_store_service/main.py
core-platform/services/workflow_store_service/tests/test_workflow_store.py
PY_COMPILE_OK: core-platform/services/workflow_store_service/main.py
45:app = FastAPI(title="Workflow Store Service", version="0.3.1-enterprise")
66:        "version": "0.3.1-enterprise",
67:        "store_version": store.store_version,

--- design_system_service ---
FOUND: services/design_system_service
services/design_system_service/app/__init__.py
services/design_system_service/app/models.py
services/design_system_service/app/parser.py
services/design_system_service/app/service.py
services/design_system_service/app/storage.py
services/design_system_service/app/validation.py
services/design_system_service/main.py
services/design_system_service/tests/acceptance_test.py
services/design_system_service/tests/test_design_system.py
PY_COMPILE_OK: services/design_system_service/main.py
48:app = FastAPI(title="Design System Service", version="0.3.1-enterprise")
FOUND: core-platform/services/design_system_service
core-platform/services/design_system_service/app/__init__.py
core-platform/services/design_system_service/app/models.py
core-platform/services/design_system_service/app/parser.py
core-platform/services/design_system_service/app/service.py
core-platform/services/design_system_service/app/storage.py
core-platform/services/design_system_service/app/validation.py
core-platform/services/design_system_service/main.py
core-platform/services/design_system_service/tests/acceptance_test.py
core-platform/services/design_system_service/tests/test_design_system.py
PY_COMPILE_OK: core-platform/services/design_system_service/main.py
48:app = FastAPI(title="Design System Service", version="0.3.1-enterprise")

--- auto_router_service ---
FOUND: core-platform/services/auto_router_service
core-platform/services/auto_router_service/__init__.py
NO_MAIN_PY

--- runtime_execution_service ---
FOUND: core-platform/services/runtime_execution_service
core-platform/services/runtime_execution_service/__init__.py
NO_MAIN_PY

--- policy_engine_service ---
FOUND: core-platform/services/policy_engine_service
core-platform/services/policy_engine_service/__init__.py
NO_MAIN_PY

--- trace_observability_service ---
FOUND: core-platform/services/trace_observability_service
core-platform/services/trace_observability_service/__init__.py
NO_MAIN_PY

--- eval_gateway_service ---
FOUND: core-platform/services/eval_gateway_service
core-platform/services/eval_gateway_service/__init__.py
NO_MAIN_PY

--- document_ingestion_service ---
FOUND: core-platform/services/document_ingestion_service
core-platform/services/document_ingestion_service/__init__.py
NO_MAIN_PY

```

## 7. Empty / Suspicious Directories

```text
--- empty dirs under core-platform/services and services ---
core-platform/services/code_agent
core-platform/services/config_service
services/service_control 2
services/universal_registry 2

--- dirs with only __init__.py ---
core-platform/services
core-platform/services/auto_router_service
core-platform/services/document_ingestion_service
core-platform/services/eval_gateway_service
core-platform/services/model_bootstrap_service/app
core-platform/services/policy_engine_service
core-platform/services/runtime_execution_service
core-platform/services/service_control
core-platform/services/trace_observability_service
```

## 8. Windows Runtime Scripts

### scripts/windows

MISSING

### core-platform/scripts/windows

```text
core-platform/scripts/windows/bootstrap_runtime.ps1
core-platform/scripts/windows/ensure_runtime.ps1
core-platform/scripts/windows/start_all.ps1
core-platform/scripts/windows/status_all.ps1
core-platform/scripts/windows/stop_all.ps1

--- core-platform/scripts/windows/bootstrap_runtime.ps1 ---
     248 core-platform/scripts/windows/bootstrap_runtime.ps1
12:  $python = Get-Command python -ErrorAction SilentlyContinue
13:  if ($python) { return $python.Source }
44:  $ollama = Get-Command ollama -ErrorAction SilentlyContinue
45:  if ($ollama) { return $ollama.Source }
47:    "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe",
48:    "$env:ProgramFiles\Ollama\ollama.exe",
49:    "$env:ProgramFiles(x86)\Ollama\ollama.exe"
64:  $python = Find-Python
65:  if (-not $python) {
68:      reason = "python_missing"
77:  $check = Run-Cmd $python @("-c", "import fastapi,uvicorn,pydantic; print('deps ok')")
81:      python = $python
86:  $install = Run-Cmd $python @("-m", "pip", "install", "--user", "fastapi", "uvicorn", "pydantic")
87:  $recheck = Run-Cmd $python @("-c", "import fastapi,uvicorn,pydantic; print('deps ok')")
90:    python = $python
98:  $python = Find-Python
99:  $ollama = Find-Ollama
100:  $ollamaApi = $false
104:    $ollamaApi = $true
111:    python_found = [bool]$python
112:    python_path = $python
115:    ollama_found = [bool]$ollama
116:    ollama_path = $ollama
117:    ollama_api = $ollamaApi
125:    $cmd = "irm https://ollama.com/install.ps1 | iex"
131:      source = "https://ollama.com/download/windows"
139:        "请打开 https://ollama.com/download/windows 下载安装。",
147:  $ollama = Find-Ollama
148:  if (-not $ollama) {
151:      reason = "ollama_missing"
--- core-platform/scripts/windows/ensure_runtime.ps1 ---
     186 core-platform/scripts/windows/ensure_runtime.ps1
33:$PythonDir = Join-Path $RuntimeDir "python"
34:$PythonExe = Join-Path $PythonDir "python.exe"
65:    return @{ ok = $true; python = $PythonExe; message = "内置 Python 已存在。" }
67:  $zip = Join-Path $RuntimeDir "python-embed.zip"
69:  $url = "https://www.python.org/ftp/python/3.12.8/python-3.12.8-embed-amd64.zip"
74:      stage = "download_python"
91:      stage = "extract_python"
99:      stage = "verify_python"
100:      message = "内置 Python 解压后未找到 python.exe。"
103:  return @{ ok = $true; python = $PythonExe; message = "内置 Python 已准备完成。" }
152:  $check = Run-Python @("-c", "import fastapi, uvicorn, pydantic; print('deps ok')")
156:  $install = Run-Python @("-m", "pip", "install", "--no-warn-script-location", "fastapi", "uvicorn", "pydantic")
157:  $recheck = Run-Python @("-c", "import fastapi, uvicorn, pydantic; print('deps ok')")
172:    python = $py
182:  python_exe = $PythonExe
183:  python = $py
--- core-platform/scripts/windows/start_all.ps1 ---
     109 core-platform/scripts/windows/start_all.ps1
32:$EnsureRuntimeScript = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "ensure_runtime.ps1"
40:    if ($runtimeResult.ok -and $runtimeResult.python_exe) {
41:      $EmbeddedPython = $runtimeResult.python_exe
53:$BootstrapScript = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "bootstrap_runtime.ps1"
60:  $py = Get-Command python -ErrorAction SilentlyContinue
90:  $Args = @("-m", "uvicorn", $Module, "--host", "127.0.0.1", "--port", "$Port")
--- core-platform/scripts/windows/status_all.ps1 ---
      10 core-platform/scripts/windows/status_all.ps1
--- core-platform/scripts/windows/stop_all.ps1 ---
      14 core-platform/scripts/windows/stop_all.ps1
```

## 9. Tauri Configs

```text
./core-platform/apps/desktop/src-tauri/tauri.conf.json
./references/jan/src-tauri/tauri.conf.json
```

### ./core-platform/apps/desktop/src-tauri/tauri.conf.json

```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "Local AI Platform",
  "version": "0.1.0",
  "identifier": "com.castvivian.localaiplatform",
  "build": {
    "beforeDevCommand": "",
    "beforeBuildCommand": "",
    "devUrl": "http://127.0.0.1:19000",
    "frontendDist": "../dist"
  },
  "app": {
    "windows": [
      {
        "title": "Local AI Platform",
        "width": 1440,
        "height": 980,
        "resizable": true
      }
    ],
    "security": {
      "csp": null
    }
  },
  "bundle": {
    "active": true,
    "targets": "all",
    "icon": [
      "icons/icon.ico",
      "icons/icon.png"
    ],
    "resources": [
      "resources/scripts/start_all.sh",
      "resources/scripts/stop_all.sh",
      "../../../scripts/windows/ensure_runtime.ps1",
      "../../../scripts/windows/bootstrap_runtime.ps1",
      "../../../scripts/windows/start_all.ps1",
      "../../../scripts/windows/stop_all.ps1",
      "../../../scripts/windows/status_all.ps1",
      "../../../services/model_bootstrap_service",
      "../../../services/model_gateway"
    ]
  }
}
```

```text
--- resource path verification from ./core-platform/apps/desktop/src-tauri ---
OK resources/scripts/start_all.sh -> /Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src-tauri/resources/scripts/start_all.sh
OK resources/scripts/stop_all.sh -> /Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src-tauri/resources/scripts/stop_all.sh
OK ../../../scripts/windows/ensure_runtime.ps1 -> /Users/mofamaomi/Documents/本地ai/core-platform/scripts/windows/ensure_runtime.ps1
OK ../../../scripts/windows/bootstrap_runtime.ps1 -> /Users/mofamaomi/Documents/本地ai/core-platform/scripts/windows/bootstrap_runtime.ps1
OK ../../../scripts/windows/start_all.ps1 -> /Users/mofamaomi/Documents/本地ai/core-platform/scripts/windows/start_all.ps1
OK ../../../scripts/windows/stop_all.ps1 -> /Users/mofamaomi/Documents/本地ai/core-platform/scripts/windows/stop_all.ps1
OK ../../../scripts/windows/status_all.ps1 -> /Users/mofamaomi/Documents/本地ai/core-platform/scripts/windows/status_all.ps1
OK ../../../services/model_bootstrap_service -> /Users/mofamaomi/Documents/本地ai/core-platform/services/model_bootstrap_service
OK ../../../services/model_gateway -> /Users/mofamaomi/Documents/本地ai/core-platform/services/model_gateway
```

### ./references/jan/src-tauri/tauri.conf.json

```json
{
  "$schema": "https://schema.tauri.app/config/2",
  "productName": "Jan",
  "version": "0.6.599",
  "identifier": "jan.ai.app",
  "build": {
    "frontendDist": "../web-app/dist",
    "devUrl": "http://localhost:1420",
    "beforeDevCommand": "cross-env IS_TAURI=true IS_DEV=true yarn dev:web",
    "beforeBuildCommand": "cross-env IS_TAURI=true yarn build:web"
  },
  "app": {
    "macOSPrivateApi": true,
    "security": {
      "capabilities": [
        "default",
        "log-app-window",
        "logs-window",
        "system-monitor-window"
      ],
      "csp": {
        "default-src": "'self' customprotocol: asset: http://localhost:* http://127.0.0.1:* ws://localhost:* ws://127.0.0.1:*",
        "connect-src": "'self' asset: ipc: data: http://asset.localhost http://ipc.localhost http://127.0.0.1:* ws://localhost:* ws://127.0.0.1:* https: http:",
        "font-src": [
          "https://fonts.gstatic.com blob: data: tauri://localhost http://tauri.localhost"
        ],
        "img-src": "'self' asset: http://asset.localhost blob: data: https:",
        "style-src": "'unsafe-inline' 'self' https://fonts.googleapis.com",
        "script-src": "'self' 'unsafe-eval' asset: $APPDATA/**.* http://asset.localhost https://eu-assets.i.posthog.com https://posthog.com"
      },
      "assetProtocol": {
        "enable": true,
        "scope": {
          "requireLiteralLeadingDot": false,
          "allow": ["**/*"]
        }
      }
    }
  },
  "plugins": {
    "os": {
      "version": "latest",
      "resolve": true
    },
    "updater": {
      "pubkey": "dW50cnVzdGVkIGNvbW1lbnQ6IG1pbmlzaWduIHB1YmxpYyBrZXk6IDJFNDEzMEVCMUEzNUFENDQKUldSRXJUVWE2ekJCTGc1Mm1BVXgrWmtES3huUlBFR0lCdG5qbWFvMzgyNDhGN3VTTko5Q1NtTW0K",
      "endpoints": [
        "https://apps.jan.ai/update-check",
        "https://github.com/janhq/jan/releases/latest/download/latest.json"
      ],
      "windows": {
        "installMode": "passive"
      }
    }
  },
  "bundle": {
    "publisher": "Menlo Research Pte. Ltd.",
    "active": true,
    "createUpdaterArtifacts": false,
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      "icons/128x128@2x.png",
      "icons/icon.icns",
      "icons/icon.ico"
    ],
    "resources": ["resources/LICENSE"]
  }
}
```

```text
--- resource path verification from ./references/jan/src-tauri ---
OK resources/LICENSE -> /Users/mofamaomi/Documents/本地ai/references/jan/src-tauri/resources/LICENSE
```

## 10. GitHub Workflow Audit

### .github/workflows/build-win-release.yml

```yaml
1:name: build-win-release
6:      tag_name:
13:      - "core-platform/apps/desktop/**"
28:      - name: Checkout
33:      - name: Show commit and tree
38:          Get-ChildItem core-platform/apps/desktop/src -Recurse | Select-Object -First 100 FullName, Length
40:      - name: Setup Node
45:      - name: Setup Rust
48:      - name: Install frontend deps
49:        working-directory: ./core-platform/apps/desktop
54:      - name: Prepare frontend dist from latest source
55:        working-directory: ./core-platform/apps/desktop
86:      - name: Verify D7-C1 UI changes are in dist
87:        working-directory: ./core-platform/apps/desktop
93:          if (!(Test-Path dist\js\auto-start-services.js)) {
94:            throw "auto-start-services.js missing from dist; Windows package would be old"
99:      - name: Verify enterprise services exist
100:        working-directory: ./core-platform/apps/desktop
104:            "..\..\services\skill_store_service\main.py",
105:            "..\..\services\artifact_registry_service\main.py",
106:            "..\..\services\code_review_gate_service\main.py",
107:            "..\..\services\repo_memory_service\main.py",
108:            "..\..\services\workflow_store_service\main.py",
109:            "..\..\services\design_system_service\main.py"
118:      - name: Debug Tauri config
119:        working-directory: ./core-platform/apps/desktop
124:      - name: Build Tauri Windows bundle
125:        working-directory: ./core-platform/apps/desktop
130:      - name: Collect artifacts
135:            "core-platform/apps/desktop/src-tauri/target/release/bundle/msi/*.msi",
136:            "core-platform/apps/desktop/src-tauri/target/release/bundle/nsis/*.exe",
137:            "core-platform/apps/desktop/src-tauri/target/release/*.exe"
143:          Copy-Item "core-platform/apps/desktop/dist/BUILD_INFO.json" -Destination dist-win -Force
152:      - name: Upload Windows artifact
155:          name: local-ai-platform-win
```

## 11. Build and Release Artifacts

```text
--- release dirs ---
./core-platform/releases/final-demo/PACKAGE_INDEX.md
./core-platform/releases/maomiai-cross-platform-demo-package.tar.gz
./core-platform/releases/maomiai-desktop-demo.tar.gz
./core-platform/releases/maomiai-desktop-demo/Local AI Platform_0.1.0_aarch64.dmg
./core-platform/releases/maomiai-desktop-demo/docs/MAOMIAI_DESKTOP_DEMO_GUIDE.md
./core-platform/releases/maomiai-desktop-demo/docs/P3_14_D6_DESKTOP_DEMO_PACKAGE_REPORT.md
./core-platform/releases/maomiai-desktop-demo/docs/P3_14_D7_DESKTOP_INTERACTION_REGRESSION_CHECKLIST.md
./core-platform/releases/maomiai-desktop-demo/scripts/desktop_services.env
./core-platform/releases/maomiai-desktop-demo/scripts/run_desktop_demo.sh
./core-platform/releases/maomiai-desktop-demo/scripts/start_desktop_services.sh
./core-platform/releases/maomiai-desktop-demo/scripts/status_desktop_services.sh
./core-platform/releases/maomiai-desktop-demo/scripts/stop_desktop_demo.sh
./core-platform/releases/maomiai-desktop-demo/scripts/stop_desktop_services.sh
./core-platform/releases/windows-current-ui-final.tar.gz
./core-platform/releases/windows-current-ui-final/BUILD_INFO.json
./core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows-current-ui-final/README.md
./core-platform/releases/windows-current-ui-final/desktop_lib.exe
./core-platform/releases/windows-d7-c1-fixed/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows-d7-c1-fixed/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows-d7-c1-fixed/desktop_lib.exe
./core-platform/releases/windows-d7-c4-runtime-bundled/BUILD_INFO.json
./core-platform/releases/windows-d7-c4-runtime-bundled/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows-d7-c4-runtime-bundled/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows-d7-c4-runtime-bundled/desktop_lib.exe
./core-platform/releases/windows-d7-c5-self-contained-runtime/BUILD_INFO.json
./core-platform/releases/windows-d7-c5-self-contained-runtime/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows-d7-c5-self-contained-runtime/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows-d7-c5-self-contained-runtime/desktop_lib.exe
./core-platform/releases/windows-d7-verified-complete/BUILD_INFO.json
./core-platform/releases/windows-d7-verified-complete/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows-d7-verified-complete/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows-d7-verified-complete/desktop_lib.exe
./core-platform/releases/windows/Local AI Platform_0.1.0_x64-setup.exe
./core-platform/releases/windows/Local AI Platform_0.1.0_x64_en-US.msi
./core-platform/releases/windows/desktop_lib.exe
./references/crawl4ai/tests/releases/test_release_0.6.4.py
./references/crawl4ai/tests/releases/test_release_0.7.0.py
./releases/.DS_Store

--- tauri bundle dirs ---
./core-platform/apps/desktop/src-tauri/target/release/bundle/.DS_Store
./core-platform/apps/desktop/src-tauri/target/release/bundle/dmg/Local AI Platform.icns
./core-platform/apps/desktop/src-tauri/target/release/bundle/dmg/Local AI Platform_0.1.0_aarch64.dmg
./core-platform/apps/desktop/src-tauri/target/release/bundle/dmg/bundle_dmg.sh
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/.DS_Store
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/Info.plist
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/MacOS/desktop_lib
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/Resources/Local AI Platform.icns
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/Resources/resources/scripts/start_all.sh
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app/Contents/Resources/resources/scripts/stop_all.sh
./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/rw.54454.Local AI Platform_0.1.0_aarch64.dmg
./core-platform/apps/desktop/src-tauri/target/release/bundle/share/create-dmg/support/eula-resources-template.xml
./core-platform/apps/desktop/src-tauri/target/release/bundle/share/create-dmg/support/template.applescript

--- package sizes ---
-rw-r--r--  1 mofamaomi  staff    10M Apr 24 15:16 ./references/happy-cli/tools/archives/difftastic-x64-win32.tar.gz
-rw-r--r--  1 mofamaomi  staff    10M Apr 24 15:16 ./references/happy-cli/tools/archives/ripgrep-x64-linux.tar.gz
-rw-r--r--  1 mofamaomi  staff    11K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.12.tar.gz
-rw-r--r--  1 mofamaomi  staff    11M Apr 24 15:16 ./references/happy-cli/tools/archives/difftastic-arm64-darwin.tar.gz
-rw-r--r--  1 mofamaomi  staff    11M Apr 24 15:16 ./references/happy-cli/tools/archives/difftastic-arm64-linux.tar.gz
-rw-r--r--  1 mofamaomi  staff    11M Apr 24 15:16 ./references/happy-cli/tools/archives/difftastic-x64-darwin.tar.gz
-rw-r--r--  1 mofamaomi  staff    11M Apr 24 15:16 ./references/happy-cli/tools/archives/difftastic-x64-linux.tar.gz
-rw-r--r--  1 mofamaomi  staff    11M Apr 24 15:16 ./references/happy-cli/tools/archives/ripgrep-x64-win32.tar.gz
-rw-r--r--  1 mofamaomi  staff    12K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.14.tar.gz
-rw-r--r--  1 mofamaomi  staff    12K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.15.tar.gz
-rw-r--r--  1 mofamaomi  staff    12K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.17.tar.gz
-rw-r--r--  1 mofamaomi  staff    12K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.18.tar.gz
-rw-r--r--  1 mofamaomi  staff    12M Apr 28 19:09 ./core-platform/releases/maomiai-cross-platform-demo-package.tar.gz
-rw-r--r--  1 mofamaomi  staff    13K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.19.tar.gz
-rw-r--r--  1 mofamaomi  staff    13K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.20.tar.gz
-rw-r--r--  1 mofamaomi  staff    13K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.21.tar.gz
-rw-r--r--  1 mofamaomi  staff    13K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.2.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.1.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.10.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.4.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.5.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.7.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.8.tar.gz
-rw-r--r--  1 mofamaomi  staff    14K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.9.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.14.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.16.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.17.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.18.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.19.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.20.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.21.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.22.tar.gz
-rw-r--r--  1 mofamaomi  staff    15K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.23.tar.gz
-rw-r--r--  1 mofamaomi  staff    16K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.25.tar.gz
-rw-r--r--  1 mofamaomi  staff    16K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.26.tar.gz
-rw-r--r--  1 mofamaomi  staff    16K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.29.tar.gz
-rw-r--r--  1 mofamaomi  staff    16K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.2.31.tar.gz
-rw-r--r--  1 mofamaomi  staff    16K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.2.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.3.0.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.1.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.3.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.4.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.5.tar.gz
-rw-r--r--  1 mofamaomi  staff    17K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.6.tar.gz
-rw-r--r--  1 mofamaomi  staff    18K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.10.tar.gz
-rw-r--r--  1 mofamaomi  staff    18K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.7.tar.gz
-rw-r--r--  1 mofamaomi  staff    18K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.8.tar.gz
-rw-r--r--  1 mofamaomi  staff    18K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.9.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 21 10:24 ./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills-claude/skills/web-artifacts-builder/scripts/shadcn-components.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 21 10:24 ./references/antigravity-awesome-skills/plugins/antigravity-awesome-skills/skills/web-artifacts-builder/scripts/shadcn-components.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 21 10:24 ./references/antigravity-awesome-skills/skills/web-artifacts-builder/scripts/shadcn-components.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.11.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.12.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.13.tar.gz
-rw-r--r--  1 mofamaomi  staff    19K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.14.tar.gz
-rw-r--r--  1 mofamaomi  staff    20K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.17.tar.gz
-rw-r--r--  1 mofamaomi  staff    20K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.18.tar.gz
-rw-r--r--  1 mofamaomi  staff    20K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.19.tar.gz
-rw-r--r--  1 mofamaomi  staff    21K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.15.tar.gz
-rw-r--r--  1 mofamaomi  staff    21K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.20.tar.gz
-rw-r--r--  1 mofamaomi  staff    21K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.21.tar.gz
-rw-r--r--  1 mofamaomi  staff    22K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.22.tar.gz
-rw-r--r--  1 mofamaomi  staff    22K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.23.tar.gz
-rw-r--r--  1 mofamaomi  staff    22K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.25.tar.gz
-rw-r--r--  1 mofamaomi  staff    22K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.26.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.3.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.27.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.28.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.29.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.30.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.31.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.32.tar.gz
-rw-r--r--  1 mofamaomi  staff    23K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.33.tar.gz
-rw-r--r--  1 mofamaomi  staff    24K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.34.tar.gz
-rw-r--r--  1 mofamaomi  staff    24K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.35.tar.gz
-rw-r--r--  1 mofamaomi  staff    24K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.36.tar.gz
-rw-r--r--  1 mofamaomi  staff    24K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.37.tar.gz
-rw-r--r--  1 mofamaomi  staff    25K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.40.tar.gz
-rw-r--r--  1 mofamaomi  staff    25K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.41.tar.gz
-rw-r--r--  1 mofamaomi  staff    26K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.42.tar.gz
-rw-r--r--  1 mofamaomi  staff    26K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.43.tar.gz
-rw-r--r--  1 mofamaomi  staff    26K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.44.tar.gz
-rw-r--r--  1 mofamaomi  staff    26K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.45.tar.gz
-rw-r--r--  1 mofamaomi  staff    27K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.47.tar.gz
-rw-r--r--  1 mofamaomi  staff    28K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.4.tar.gz
-rw-r--r--  1 mofamaomi  staff    28K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.5.tar.gz
-rw-r--r--  1 mofamaomi  staff    28K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.48.tar.gz
-rw-r--r--  1 mofamaomi  staff    28K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.49.tar.gz
-rw-r--r--  1 mofamaomi  staff    29K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.51.tar.gz
-rw-r--r--  1 mofamaomi  staff    30K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.52.tar.gz
-rw-r--r--  1 mofamaomi  staff    30K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.53.tar.gz
-rw-r--r--  1 mofamaomi  staff    31K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.54.tar.gz
-rw-r--r--  1 mofamaomi  staff    31K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.56.tar.gz
-rw-r--r--  1 mofamaomi  staff    31K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.57.tar.gz
-rw-r--r--  1 mofamaomi  staff    31K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.58.tar.gz
-rw-r--r--  1 mofamaomi  staff    31K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.4.60.tar.gz
-rw-r--r--  1 mofamaomi  staff    32K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.7.tar.gz
-rw-r--r--  1 mofamaomi  staff    32K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.8.tar.gz
-rw-r--r--  1 mofamaomi  staff    33K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.6.tar.gz
-rw-r--r--  1 mofamaomi  staff    33K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.9.tar.gz
-rw-r--r--  1 mofamaomi  staff    41K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.10.tar.gz
-rw-r--r--  1 mofamaomi  staff    41K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.11.tar.gz
-rw-r--r--  1 mofamaomi  staff    42K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.12.tar.gz
-rw-r--r--  1 mofamaomi  staff    42K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.23.tar.gz
-rw-r--r--  1 mofamaomi  staff    42K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.24.tar.gz
-rw-r--r--  1 mofamaomi  staff    42K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.25.tar.gz
-rw-r--r--  1 mofamaomi  staff    43K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.13.tar.gz
-rw-r--r--  1 mofamaomi  staff    44K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.22.tar.gz
-rw-r--r--  1 mofamaomi  staff    45K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.26.tar.gz
-rw-r--r--  1 mofamaomi  staff    46K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.27.tar.gz
-rw-r--r--  1 mofamaomi  staff    48K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.29.tar.gz
-rw-r--r--  1 mofamaomi  staff    49K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.30.tar.gz
-rw-r--r--  1 mofamaomi  staff    49K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.31.tar.gz
-rw-r--r--  1 mofamaomi  staff    52K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.32.tar.gz
-rw-r--r--  1 mofamaomi  staff    58K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.15.tar.gz
-rw-r--r--  1 mofamaomi  staff    58K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.17.tar.gz
-rw-r--r--  1 mofamaomi  staff    58K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.19.tar.gz
-rw-r--r--  1 mofamaomi  staff    64B Apr 24 18:47 ./references/litellm/dist/litellm-1.79.1.tar.gz
-rw-r--r--  1 mofamaomi  staff   1.7M Apr 28 18:48 ./core-platform/releases/windows/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   1.7M May  4 12:32 ./core-platform/releases/windows-d7-c1-fixed/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   1.8M May  5 06:11 ./core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   1.8M May  5 11:23 ./core-platform/releases/windows-d7-c4-runtime-bundled/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   1.8M May  5 14:30 ./core-platform/releases/windows-d7-c5-self-contained-runtime/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   1.8M May  5 16:01 ./core-platform/releases/windows-d7-verified-complete/Local AI Platform_0.1.0_x64-setup.exe
-rw-r--r--  1 mofamaomi  staff   141K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.21.tar.gz
-rw-r--r--  1 mofamaomi  staff   153K Apr 14 11:34 ./references/OpenHarness/.venv/lib/python3.12/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz
-rw-r--r--  1 mofamaomi  staff   153K Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz
-rw-r--r--  1 mofamaomi  staff   153K Apr 17 14:59 ./core-platform/.venv/lib/python3.12/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz
-rw-r--r--  1 mofamaomi  staff   2.7M Apr 28 18:48 ./core-platform/releases/windows/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   2.7M May  4 12:32 ./core-platform/releases/windows-d7-c1-fixed/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   2.8M May  5 06:11 ./core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   2.8M May  5 11:23 ./core-platform/releases/windows-d7-c4-runtime-bundled/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   2.8M May  5 14:30 ./core-platform/releases/windows-d7-c5-self-contained-runtime/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   2.8M May  5 16:01 ./core-platform/releases/windows-d7-verified-complete/Local AI Platform_0.1.0_x64_en-US.msi
-rw-r--r--  1 mofamaomi  staff   3.3K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.0.tar.gz
-rw-r--r--  1 mofamaomi  staff   4.1K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.1.tar.gz
-rw-r--r--  1 mofamaomi  staff   4.3M Apr 24 15:16 ./references/happy-cli/tools/archives/ripgrep-arm64-darwin.tar.gz
-rw-r--r--  1 mofamaomi  staff   4.7M Apr 24 15:16 ./references/happy-cli/tools/archives/ripgrep-x64-darwin.tar.gz
-rw-r--r--  1 mofamaomi  staff   5.4M Apr 28 15:50 ./core-platform/releases/maomiai-desktop-demo.tar.gz
-rw-r--r--  1 mofamaomi  staff   5.6K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.2.tar.gz
-rw-r--r--  1 mofamaomi  staff   6.6M May  5 06:12 ./core-platform/releases/windows-current-ui-final.tar.gz
-rw-r--r--  1 mofamaomi  staff   7.4K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.1.tar.gz
-rw-r--r--  1 mofamaomi  staff   7.8K Apr 24 18:47 ./references/litellm/enterprise/dist/litellm_enterprise-0.1.2.tar.gz
-rw-r--r--  1 mofamaomi  staff   8.5K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.3.tar.gz
-rw-r--r--  1 mofamaomi  staff   8.7K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.4.tar.gz
-rw-r--r--  1 mofamaomi  staff   9.6K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.7.tar.gz
-rw-r--r--  1 mofamaomi  staff   9.6M Apr 24 15:16 ./references/happy-cli/tools/archives/ripgrep-arm64-linux.tar.gz
-rw-r--r--  1 mofamaomi  staff   9.8K Apr 24 18:47 ./references/litellm/litellm-proxy-extras/dist/litellm_proxy_extras-0.1.8.tar.gz
-rw-r--r--@ 1 mofamaomi  staff    34M May  4 12:10 ./core-platform/apps/desktop/src-tauri/target/release/bundle/macos/rw.54454.Local AI Platform_0.1.0_aarch64.dmg
-rw-r--r--@ 1 mofamaomi  staff   2.7M Apr 28 15:49 ./core-platform/releases/maomiai-desktop-demo/Local AI Platform_0.1.0_aarch64.dmg
-rw-r--r--@ 1 mofamaomi  staff   2.7M May  2 15:32 ./core-platform/apps/desktop/src-tauri/target/release/bundle/dmg/Local AI Platform_0.1.0_aarch64.dmg
```

## 12. Large Files / Git Ignore Risk

```text
--- largest files under repo excluding .git/node_modules/target ---
-rw-r--r--  1 mofamaomi  staff    20M Apr 17 10:10 ./references/skyvern/docs/images/skyvern-agent-local.mp4
-rw-r--r--  1 mofamaomi  staff    20M Apr 24 15:43 ./references/architecture.of.internet-product/ChatGPT-LLM-Diffusion/2209.00796 Diffusion Models - A Comprehensive Survey of Methods and Applications.pdf
-rw-r--r--  1 mofamaomi  staff    20M Apr 24 23:18 ./references/SWE-agent/tests/test_data/data_sources/ctf/forensics/flash/flash_c8429a430278283c0e571baebca3d139.zip
-rw-r--r--  1 mofamaomi  staff    20M Apr 24 23:19 ./references/GitTaskBench/SWE_agent/tests/test_data/data_sources/ctf/forensics/flash/flash_c8429a430278283c0e571baebca3d139.zip
-rwxr-xr-x  1 mofamaomi  staff    20M Apr 14 11:34 ./references/OpenHarness/.venv/lib/python3.12/site-packages/cryptography/hazmat/bindings/_rust.abi3.so
-r--------  1 mofamaomi  staff    21M Apr 17 06:01 ./AlphaAgent/.git/objects/pack/pack-65934da538317c21fabebff743335613f04327fb.pack
-rw-r--r--  1 mofamaomi  staff    21M Apr 25 08:49 ./references/sim/apps/sim/public/static/knowledge.gif
-rw-r--r--  1 mofamaomi  staff    22M Apr 24 18:47 ./references/litellm/docs/my-website/img/ngrok_public_url.gif
-rw-r--r--  1 mofamaomi  staff    22M Apr 24 23:18 ./references/continue/extensions/vscode/models/all-MiniLM-L6-v2/onnx/model_quantized.onnx
-rwxr-xr-x  1 mofamaomi  staff    22M Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/numpy/.dylibs/libopenblas64_.0.dylib
-rw-r--r--  1 mofamaomi  staff    23M Apr 25 08:50 ./references/MinerU-Diffusion/docs/MinerU-Diffusion-V1.pdf
-rw-r--r--  1 mofamaomi  staff    25M Apr 17 10:10 ./references/skyvern/docs/images/zapier/zap1.gif
-rw-r--r--  1 mofamaomi  staff    25M Apr 24 23:18 ./references/continue/docs/images/plan-mode-compressed.gif
-rw-r--r--  1 mofamaomi  staff    26M Apr 24 18:18 ./references/Toonflow-app/data/web/index.html
-rw-r--r--  1 mofamaomi  staff    27M Apr 24 15:43 ./references/architecture.of.internet-product/B.基础架构-Docker-容器架构/动态资源管理和容器技术在金融行业的架构探索.pdf
-rw-r--r--  1 mofamaomi  staff    27M Apr 24 15:43 ./references/architecture.of.internet-product/C.运维架构-自动化运维DevOps/美团云运维体系建设与实践 -FCNUTCon2017_huxiangtao.pdf
-rwxr-xr-x  1 mofamaomi  staff    28M Apr 14 17:12 ./references/ComfyUI/.venv/lib/python3.12/site-packages/torch/lib/libtorch_python.dylib
-rwxr-xr-x  1 mofamaomi  staff    28M Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/torch/lib/libtorch_python.dylib
-rwxr-xr-x  1 mofamaomi  staff    28M Apr 16 16:57 ./core-platform/.venv/lib/python3.12/site-packages/torch/lib/libtorch_python.dylib
-r--r--r--  1 mofamaomi  staff    29M Apr 14 11:31 ./references/everything-claude-code/.git/objects/pack/pack-a53f6c52b77b2762f68927d1c864cb7af9b5d7df.pack
-rw-r--r--  1 mofamaomi  staff    29M Apr 17 06:01 ./langflow/docs/static/img/star-langflow.gif
-rw-r--r--  1 mofamaomi  staff    29M Apr 17 10:16 ./references/langflow/docs/static/img/star-langflow.gif
-rw-r--r--  1 mofamaomi  staff    30M Apr 24 23:20 ./references/autogen/dotnet/samples/dev-team/seed-memory/azure-well-architected.pdf
-r--r--r--  1 mofamaomi  staff    31M Apr 17 09:54 ./references/browser-use/.git/objects/pack/pack-88008b6d9bc0eff20107e50be8447d0c937451e5.pack
-r--r--r--  1 mofamaomi  staff    31M Apr 20 16:43 ./references/deer-flow/.git/objects/pack/pack-79534e89671866f7aeaf7466cf8245be01f5c352.pack
-rw-r--r--  1 mofamaomi  staff    32M Apr 24 15:43 ./references/architecture.of.internet-product/1.Google.Facebook.eBay.Amazon/Google-What-does-it-take-to-make-Google-work-at-scale.pdf
-r--r--r--  1 mofamaomi  staff    33M Apr 14 16:59 ./references/Fooocus/.git/objects/pack/pack-185efa109c63cff24ea4b7deb2d04f356873a40f.pack
-rw-r--r--  1 mofamaomi  staff    35M Apr 24 23:19 ./references/GitTaskBench/OpenHands/docs/static/img/teaser.mp4
-rw-r--r--  1 mofamaomi  staff    37M Apr 24 23:22 ./references/opik/apps/opik-documentation/documentation/fern/img/v2/evaluation/prevent-regressions.mp4
-r--r--r--  1 mofamaomi  staff    40M Apr 17 09:37 ./capability-registry/claude-code-best-practice/.git/objects/pack/pack-1b657037da2ffd237ae3493fdad52dc08f63f63d.pack
-rw-r--r--  1 mofamaomi  staff    40M Apr 24 18:47 ./references/litellm/docs/my-website/img/retool_litellm_connection.gif
-rw-r--r--  1 mofamaomi  staff    41M Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/pyarrow/libarrow.2300.dylib
-rw-r--r--  1 mofamaomi  staff    43M Apr 24 18:18 ./references/Toonflow-app/data/models/all-MiniLM-L6-v2/onnx/model_fp16.onnx
-rw-r--r--  1 mofamaomi  staff    45M Apr 24 23:22 ./references/opik/apps/opik-documentation/documentation/fern/img/v2/observability/getting-started.mp4
-rw-r--r--  1 mofamaomi  staff    46M Apr 24 23:23 ./references/jan/docs/src/pages/docs/desktop/_assets/jan-v2-vl-demo.gif
-rwxr-xr-x  1 mofamaomi  staff    47M Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1
-rwxr-xr-x  1 mofamaomi  staff    47M Apr 16 16:57 ./core-platform/.venv/lib/python3.12/site-packages/imageio_ffmpeg/binaries/ffmpeg-macos-aarch64-v7.1
-rw-r--r--  1 mofamaomi  staff    50M Apr 17 14:59 ./core-platform/.venv/lib/python3.12/site-packages/py_mini_racer/libmini_racer.dylib
-r--------  1 mofamaomi  staff    56M Apr 17 06:11 ./anything-llm/.git/objects/pack/pack-070094dcd688c35ef50e9e1570eac24b7767b16b.pack
-r--r--r--  1 mofamaomi  staff    57M Apr 17 09:55 ./references/anything-llm/.git/objects/pack/pack-9cd42db0ccfa52546b1160ad40281be6486a09b7.pack
-rw-r--r--  1 mofamaomi  staff    57M Apr 24 15:43 ./references/architecture.of.internet-product/9.50-favorite-technical-papers/A Few Billion Lines of Code Later - Using Static Analysis to Find Bugs in the Real World - ACM - 2010 (BLOC-coverity).pdf
-rw-r--r--  1 mofamaomi  staff    58M Apr 24 23:19 ./references/GitTaskBench/code_base/TransparentBackground/figures/demo_b5.gif
-rw-r--r--  1 mofamaomi  staff    72M Apr 24 23:19 ./references/GitTaskBench/code_base/TransparentBackground/samples/b5.mp4
-r--r--r--  1 mofamaomi  staff    77M Apr 18 04:54 ./references/hyperframes/.git/objects/pack/pack-c60e7f1d3c9bfd39361e9a0d42f3347e05bc7ec1.pack
-r--r--r--  1 mofamaomi  staff    79M Apr 14 16:59 ./references/ComfyUI/.git/objects/pack/pack-9de211e73d479f25804f982eb104da2b17d7dbb4.pack
-r--r--r--  1 mofamaomi  staff    81M Apr 17 04:44 ./capability-registry/gstack/.git/objects/pack/pack-13766c6b2974f4f457feb309fcb710ab39d5a562.pack
-r--r--r--  1 mofamaomi  staff    83M Apr 17 09:57 ./references/stagehand/.git/objects/pack/pack-01bfe469864856dee128305d390e221322024e47.pack
-rw-r--r--  1 mofamaomi  staff    89M Apr 17 10:10 ./references/skyvern/docs/images/skyvern_demo_video_v2.1.mp4
-rw-r--r--  1 mofamaomi  staff    89M Apr 17 10:10 ./references/skyvern/fern/images/skyvern_demo_video_v2.1.mp4
-r--r--r--  1 mofamaomi  staff   120M Apr 14 11:32 ./references/hermes-agent/.git/objects/pack/pack-81dffb00068b4bd62a5073c6dd607466084172b7.pack
-r--------  1 mofamaomi  staff   121M Apr 17 06:12 ./LLaVA-NeXT/.git/objects/pack/pack-a6215cefb9f9b16b27f62ab89b11348a763e3e95.pack
-r--r--r--  1 mofamaomi  staff   135M Apr 17 06:02 ./Qwen3-VL/.git/objects/pack/pack-933b08cb3dade81c49e21c8f228e2ad46feea521.pack
-r--r--r--  1 mofamaomi  staff   159M Apr 17 10:00 ./references/LibreChat/.git/objects/pack/pack-56bf61b8f63bcc12b423ce50e753012d75f50f9d.pack
-r--------  1 mofamaomi  staff   178M Apr 14 17:00 ./references/CogVideo/.git/objects/pack/pack-2eca8564004fd3e3d503068e8ac02e1a51969515.pack
-rwxr-xr-x  1 mofamaomi  staff   206M Apr 14 17:12 ./references/ComfyUI/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.dylib
-rwxr-xr-x  1 mofamaomi  staff   206M Apr 14 18:11 ./references/CogVideo/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.dylib
-rwxr-xr-x  1 mofamaomi  staff   206M Apr 16 16:57 ./core-platform/.venv/lib/python3.12/site-packages/torch/lib/libtorch_cpu.dylib
-r--------  1 mofamaomi  staff   296M Apr 17 04:46 ./vnpy/.git/objects/pack/pack-41481d21ebc72c71cc7f7f9bd6abf7317e2787e2.pack
-r--------  1 mofamaomi  staff   302M Apr 17 05:54 ./OpenHands/.git/objects/pack/pack-3de6686b609e92f6d0697c42e8692003ab8f73db.pack
-r--r--r--  1 mofamaomi  staff   306M Apr 17 10:05 ./references/OpenHands/.git/objects/pack/pack-47330205124564ad715ed0751d321eba16610097.pack
-r--r--r--  1 mofamaomi  staff   346M Apr 17 05:50 ./references/open-webui/.git/objects/pack/pack-1cc418d2f2f338d7e9d3eaacacfd5cbd51f8d51b.pack
-r--r--r--  1 mofamaomi  staff   380M Apr 17 10:07 ./references/cline/.git/objects/pack/pack-37dfe7387490d7ab34020c58851ddc2d212e4b25.pack
-r--r--r--  1 mofamaomi  staff   536M Apr 17 10:10 ./references/skyvern/.git/objects/pack/pack-8d85d125b2c520df8eac0726d27cad88dd3568ff.pack
-rw-r--r--  1 mofamaomi  staff   683M Apr 16 16:57 ./models/cogvideo/.cache/huggingface/download/text_encoder/aoe4E07IMh7reFyUkVoVk040mQk=.4f2751ceeb2a96edd693e539dc5d6bba0b8d3814f49a9b3798403a0cec4b2e3d.incomplete
-r--r--r--  1 mofamaomi  staff   701M Apr 17 10:12 ./references/lobe-chat/.git/objects/pack/pack-0dda3bf89786e115fdc42e9818ecea69bc7134ad.pack
-rw-r--r--  1 mofamaomi  staff   1.0G Apr 16 16:56 ./models/cogvideo/.cache/huggingface/download/transformer/4SfAgk9U607e8pVunEB9nSiU10k=.8fbb6a5e67c70885a8ed8e33df144ac61253e45977be5035fa18cfdf77d386c7.incomplete
-r--r--r--  1 mofamaomi  staff   1.2G Apr 17 06:01 ./langflow/.git/objects/pack/pack-899ff03c61e4d4de91abb7b4e269b4c8ad08d915.pack
-r--r--r--  1 mofamaomi  staff   1.2G Apr 17 10:16 ./references/langflow/.git/objects/pack/pack-4c06c796a89c2be4f57e8a4b1e4d3dc97112ded5.pack
-rw-r--r--  1 mofamaomi  staff   1.4G Apr 16 16:56 ./models/cogvideo/.cache/huggingface/download/text_encoder/Dr_lZJDwE1cnGAQMwA77jJEQIk8=.f63154532130422309532ff56f11945fbea8266c958e3133e8e5aef85c6293c7.incomplete
-rw-r--r--  1 mofamaomi  staff   6.5G Apr 16 19:07 ./references/ComfyUI/models/checkpoints/sd_xl_base_1.0.safetensors

--- git ignored files sample ---
 M .github/workflows/build-win-release.yml
 D core-platform/core-platform/apps/desktop/package.json
 D core-platform/core-platform/apps/desktop/scripts/scripts/build-frontend.mjs
 D core-platform/core-platform/apps/desktop/scripts/scripts/preflight.mjs
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/128x128.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/128x128@2x.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/32x32.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square107x107Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square142x142Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square150x150Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square284x284Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square30x30Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square310x310Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square44x44Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square71x71Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/Square89x89Logo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/StoreLogo.png
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.icns
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.ico
 D core-platform/core-platform/apps/desktop/src-tauri/icons/icons/icon.png
 D core-platform/core-platform/apps/desktop/src-tauri/resources/resources/scripts/start_all.sh
 D core-platform/core-platform/apps/desktop/src-tauri/resources/resources/scripts/stop_all.sh
 D core-platform/core-platform/apps/desktop/src-tauri/tauri.conf.json
 D core-platform/core-platform/scripts/start_all.sh
 D core-platform/core-platform/scripts/stop_all.sh
?? .venv/
?? AlphaAgent/
?? D4_B_ACCEPTANCE_REPORT.md
?? LLaVA-NeXT/
?? LLaVA-OneVision-1.5/
?? MASTER/
?? OpenHands/
?? Qwen3-VL/
?? RAG-Anything/
?? VoxCPM/
?? andrej-karpathy-skills/
?? anything-llm/
?? archive/quarantine/
?? capability-registry/claude-code-best-practice/
?? capability-registry/gstack/
?? core-platform/archive/
?? core-platform/data/
?? core-platform/fix_workflow_paths.py
?? core-platform/releases/final-demo/
?? core-platform/releases/maomiai-cross-platform-demo-package.tar.gz
?? core-platform/releases/maomiai-desktop-demo.tar.gz
?? core-platform/releases/maomiai-desktop-demo/
?? core-platform/releases/windows-current-ui-final.tar.gz
?? core-platform/releases/windows-current-ui-final/BUILD_INFO.json
?? "core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64-setup.exe"
?? "core-platform/releases/windows-current-ui-final/Local AI Platform_0.1.0_x64_en-US.msi"
?? core-platform/releases/windows-current-ui-final/desktop_lib.exe
?? core-platform/releases/windows-d7-c1-fixed/
?? core-platform/releases/windows-d7-c4-runtime-bundled/
?? core-platform/releases/windows-d7-c5-self-contained-runtime/
?? core-platform/releases/windows-d7-verified-complete/
?? core-platform/releases/windows/
?? core-platform/tmp_fix_workflow_paths.py
?? data/
?? docs/reports/P3_14_D2_C3_WORKFLOW_STORE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_D_ARTIFACT_REGISTRY_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_E_SKILL_STORE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_F_CODE_REVIEW_GATE_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D2_G_REPO_MEMORY_ENTERPRISE_ACCEPTED.md
?? docs/reports/P3_14_D7_A_ACCEPTANCE_REPORT.md
?? docs/reports/P3_14_D7_FULL_LOCAL_PROJECT_INTEGRITY_AUDIT.md
?? full_integrity_audit.sh
?? generated/audio/
?? generated/browser/
?? generated/crawler/
?? generated/finance/
?? generated/hyperframes/
?? generated/rag/
?? generated/research/
?? generated/stock_research/
?? generated/videos/video_job_20260417_212451.json
?? generated/videos/video_job_20260417_212506.json
?? generated/videos/video_job_20260417_214458.json
?? generated/videos/video_job_20260417_222053.json
?? generated/videos/video_job_20260417_225316.json
?? generated/vision/
?? generated/web_research/
?? langflow/
?? qlib/
?? scripts/acceptance/
?? services/
?? test_service_health.html
?? vnpy/
!! .DS_Store
!! .venv/lib/python3.12/site-packages/fastapi/.agents/skills/fastapi/references/
!! agent-orchestrator.log
!! archive/quarantine/nested_core-platform_20260425-100633/apps/desktop/bundle/backend/.DS_Store
!! archive/quarantine/nested_core-platform_20260425-100633/apps/desktop/bundle/backend/apps/
!! core-platform/.DS_Store
!! core-platform/.venv/
!! core-platform/apps/.DS_Store
!! core-platform/apps/desktop/.DS_Store
!! core-platform/apps/desktop/node_modules/
!! core-platform/apps/desktop/src-tauri/.DS_Store
!! core-platform/apps/desktop/src-tauri/gen/
!! core-platform/apps/desktop/src-tauri/target/
!! core-platform/data/sqlite/
!! core-platform/logs/
!! core-platform/services/__pycache__/
!! core-platform/services/agent_orchestrator/__pycache__/
!! core-platform/services/artifact_registry_service/__pycache__/
!! core-platform/services/auto_router_service/__pycache__/
!! core-platform/services/code_review_gate_service/__pycache__/
!! core-platform/services/design_system_service/__pycache__/
!! core-platform/services/document_ingestion_service/__pycache__/
!! core-platform/services/eval_engine/__pycache__/
!! core-platform/services/eval_gateway_service/__pycache__/
!! core-platform/services/model_bootstrap_service/__pycache__/
!! core-platform/services/model_gateway/__pycache__/
!! core-platform/services/plugin_manager/__pycache__/
!! core-platform/services/policy_engine_service/__pycache__/
!! core-platform/services/repo_memory_service/__pycache__/
!! core-platform/services/runtime_execution_service/__pycache__/
!! core-platform/services/skill_store_service/__pycache__/
!! core-platform/services/trace_observability_service/__pycache__/
!! core-platform/services/workflow_store_service/__pycache__/
!! generated/.DS_Store
!! logs/
!! model-gateway.log
!! models/
!! references/
!! releases/
```

## 13. Python Syntax Check

```text
--- core-platform/services/agent_orchestrator/main.py ---
OK
--- core-platform/services/artifact_registry_service/main.py ---
OK
--- core-platform/services/code_review_gate_service/main.py ---
OK
--- core-platform/services/design_system_service/main.py ---
OK
--- core-platform/services/eval_engine/main.py ---
OK
--- core-platform/services/model_bootstrap_service/main.py ---
OK
--- core-platform/services/model_gateway/main.py ---
OK
--- core-platform/services/plugin_manager/main.py ---
OK
--- core-platform/services/repo_memory_service/main.py ---
OK
--- core-platform/services/skill_store_service/main.py ---
OK
--- core-platform/services/workflow_store_service/main.py ---
OK
--- services/artifact_registry_service/main.py ---
OK
--- services/code_review_gate_service/main.py ---
OK
--- services/design_system_service/main.py ---
OK
--- services/repo_memory_service/main.py ---
OK
--- services/skill_store_service/main.py ---
OK
--- services/workflow_store_service/main.py ---
OK
PY_SYNTAX_FAIL=0
```

## 14. JavaScript Syntax Check

```text
--- core-platform/apps/desktop/src/js/api.js ---
OK
--- core-platform/apps/desktop/src/js/auto-start-services.js ---
OK
--- core-platform/apps/desktop/src/js/chatgpt-like-ui.js ---
OK
--- core-platform/apps/desktop/src/js/inspector.js ---
OK
--- core-platform/apps/desktop/src/js/services.js ---
OK
--- core-platform/apps/desktop/src/js/state.js ---
OK
--- core-platform/apps/desktop/src/js/tauri-bridge.js ---
OK
--- core-platform/apps/desktop/src/js/utils.js ---
OK
--- core-platform/apps/desktop/src/js/windows-click-model-setup.js ---
OK
JS_SYNTAX_FAIL=0
```

## 15. Summary

- Full local project audit completed.
- This report audits the whole local Git repository, not just one packaging path.
- Review sections for duplicate roots, empty service directories, stale desktop copies, and packaging resources.

