# C25 Mac Latest Brand Pack

## Goal

Update product introduction and build latest macOS package for local testing and demo.

## Branding

Updated product introduction:

- Local AI Agent Platform
- Local model runtime
- Agent Runtime
- Code Agent
- Memory/RAG
- Browser research
- Permission approval
- 140+ builtin skills
- Desktop app

No reference to internal rebuild/history wording.

## Artifacts

- App: `core-platform/releases/macos-latest-brand-pack/app/Local AI Platform.app`
- DMG: `core-platform/releases/macos-latest-brand-pack/dmg/Local AI Platform_0.1.0_aarch64.dmg`

## Validation Results

| Check | Result |
|-------|--------|
| Forbidden wording | 0 hits |
| py_compile (12 files) | ALL PASS |
| JS syntax (5 files) | ALL PASS |
| Hardcode guard | PASS |
| Mac resources (17) | ALL present |
| App resources (10) | ALL present |
| APP size | ~57.6 MB |
| DMG size | ~6.3 MB |

## Test Prompts

1. 你好，请用一句话介绍你自己
2. 今天是几月几号，现在几点
3. 我们现在有哪些 Agent 和 MCP 相关技能
4. 请用代码智能体检查项目文件并生成 patch
5. 帮我做浏览器自动化和网页研究

## Notes

This package is for macOS local validation and route/demo preparation.
