# P3.14-D7-C5 Step 3 Install Progress and Auto Recheck

## Status
Implemented and tested.

## Problem
The install button executed the installer but gave poor feedback:
- raw PowerShell output was shown directly
- repeated clicks could freeze the UI
- no post-install recheck
- users could not tell whether the backend became available

## Fix
Added:
1. **Progress UI with stages** - Shows 4 stages with visual progress bar
2. **Duplicate-click guard** - `window.__maomiaiInstallingLocalBackend` flag prevents multiple simultaneous installs
3. **Install stages** - "准备安装命令", "请求 Windows 执行安装", "等待安装程序完成", "自动重新检查状态"
4. **Automatic post-install recheck** - `recheckAfterInstall()` function checks backend 3 times with 2s intervals
5. **Clearer failure guidance** - Next steps shown when backend not detected

## Result
The install flow now behaves like a product workflow:
- Users see clear progress stages
- Cannot accidentally trigger multiple installs
- Automatically verifies if backend is ready
- Gives actionable next steps if still failed

## Files Modified
- `core-platform/apps/desktop/src-tauri/src/lib.rs` - Structured JSON response from install command
- `core-platform/apps/desktop/src/js/windows-click-model-setup.js` - Progress UI, auto recheck
- `core-platform/apps/desktop/src/styles/main.css` - Progress card and step styles
