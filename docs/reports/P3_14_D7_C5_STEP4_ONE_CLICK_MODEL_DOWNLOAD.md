# P3.14-D7-C5 Step 4: One-click Model Download

## Status
**Implemented** ✅

## Product Behavior

Users no longer need to operate the terminal. They choose a capability inside the app:

- **Standard conversation capability** (标准对话能力)
- **Code capability** (代码能力)  
- **Lightweight fast capability** (轻量快速能力)

The app then automatically:
1. Checks local inference backend (检查本地推理后端)
2. Starts local inference backend (启动本地推理服务)
3. Downloads the selected capability (下载能力)
4. Verifies availability (验证能力是否可用)
5. Connects back to chat (连接到聊天)

## Important Fix

The Windows script now uses:
```text
ollama serve
ollama pull <model>
ollama list
```

It no longer opens the interactive Ollama menu (which would show options like OpenClaw, Codex, Claude Code, etc.).

## Files Modified

1. **core-platform/scripts/windows/bootstrap_runtime.ps1**
   - Added `Ensure-Ollama-Serve` function (non-interactive ollama serve)
   - Added `Get-Model-For-Profile` function (maps profiles to models)
   - Added `Pull-Model` function (non-interactive ollama pull)
   - Removed all interactive menu triggers

2. **core-platform/services/model_bootstrap_service/main.py**
   - Updated version to `0.1.0-d7-c5-one-click`
   - Added `PROFILE_MODEL_MAP` with 3 profiles (standard, code, light)
   - Modified `/bootstrap/start` to use pull_model action

3. **core-platform/apps/desktop/src/js/windows-click-model-setup.js**
   - Rewrote `startLocalModelDownload()` with 5-step progress
   - Added 3 model profile buttons (standard, code, light)
   - Added detailed progress feedback
   - Prevents duplicate downloads with `window.__maomiaiDownloadingModel`

## User Flow

```
1. User opens MAOMIAI
2. Goes to "准备本地 AI" (Local AI Setup)
3. If Ollama not installed → Click "安装本地推理后端"
4. Click "下载标准对话能力" (or code/light)
5. App shows progress:
   - 检查本地推理后端 ✓
   - 启动本地推理服务 ✓
   - 下载标准对话能力 ... (with progress bar)
   - 验证能力是否可用 ✓
   - 连接到聊天 ✓
6. User clicks "返回对话"
7. User inputs: "你好，请介绍一下你自己"
8. Local AI responds in Chinese
```

## Testing Checklist

- [ ] Install Ollama if not present
- [ ] Start Ollama service automatically
- [ ] Download model without terminal interaction
- [ ] Show progress during download
- [ ] Verify model is available after download
- [ ] Chat returns Chinese responses
- [ ] No Ollama interactive menu appears
- [ ] No "OpenClaw Node.js" errors

## Next Steps

Trigger Windows build and test on actual Windows machine to verify the complete flow works end-to-end.
