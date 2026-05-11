# P3.14-D7-C5 Step 5 Local Model Store

## Status
Implemented.

## Goal
The local model page is now a model/capability store.
Users choose a capability and the software automatically downloads, deploys, verifies, and connects it.

## Model Catalog
- Standard conversation capability (qwen2.5:7b)
- Lightweight fast capability (qwen2.5:1.5b)
- Code capability (qwen2.5-coder:7b)
- Reasoning capability (deepseek-r1:7b)
- English general capability (llama3.1:8b)
- Small general capability (llama3.2:3b)
- Document embedding capability (nomic-embed-text)
- Multilingual document embedding capability (bge-m3)

## UX Principle
Customers should not operate terminal commands or see the Ollama interactive menu.
All interactions happen through the desktop UI.

## Implementation Details

### Frontend (windows-click-model-setup.js)
- Replaced old setup wizard with model store UI
- Added MODEL_CATALOG array with 8 models
- One-click download via `/bootstrap/start` API
- Progress indicator with step-by-step status
- Model status display (installed/missing)
- Return to chat button

### Backend Changes
#### bootstrap_runtime.ps1
- Added Get-Model-For-Profile function mapping profile names to Ollama models
- Removed all bare `ollama` calls (interactive menu)
- Ensured `ollama serve` is called with arguments, not bare

#### model_bootstrap_service/main.py
- Added PROFILE_MODEL_MAP dictionary with all 8 profiles
- Maps profile names to model names for automatic selection

### CSS (main.css)
- Added .model-store-page, .model-store-hero, .model-store-grid
- Added .model-store-card with metadata display
- Added progress styles (.model-progress-card, .model-progress-bar)
- Added status colors (installed: green, missing: red)

## Files Modified
- core-platform/apps/desktop/src/js/windows-click-model-setup.js
- core-platform/apps/desktop/src/styles/main.css
- core-platform/scripts/windows/bootstrap_runtime.ps1
- core-platform/services/model_bootstrap_service/main.py

## Verification
- Python syntax check passed
- JavaScript syntax check passed

## Next
Search for any remaining bare ollama calls and remove them.
