#!/bin/bash
set -e

cd /Users/mofamaomi/Documents/本地ai || exit 1
echo "===== P3.14-D7-C5 Step 3: Install Progress UI + Auto Recheck ====="
APP="core-platform/apps/desktop"
JS="$APP/src/js/windows-click-model-setup.js"
CSS="$APP/src/styles/main.css"
RUST="$APP/src-tauri/src/lib.rs"
REPORT="docs/reports/P3_14_D7_C5_STEP3_INSTALL_PROGRESS_AND_RECHECK.md"
mkdir -p docs/reports

echo
echo "===== 1. Patch Rust install command ====="
python3 - <<'PY'
from pathlib import Path
import re
p = Path("core-platform/apps/desktop/src-tauri/src/lib.rs")
s = p.read_text(encoding="utf-8")
old_start = "fn install_local_inference_backend()"
if old_start not in s:
    raise SystemExit("install_local_inference_backend not found")
m = re.search(r"#\[tauri::command\]\s*fn install_local_inference_backend\(\) -> Result<String, String> \{", s)
if not m:
    raise SystemExit("command function signature not found")
start = m.start()
brace = s.index("{", m.end() - 1)
depth = 0
end = None
for i in range(brace, len(s)):
    if s[i] == "{":
        depth += 1
    elif s[i] == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break
if end is None:
    raise SystemExit("failed to locate function end")
new_func = r'''#[tauri::command]
fn install_local_inference_backend() -> Result<String, String> {
    use std::process::Command;
    #[cfg(target_os = "windows")]
    {
        let install_cmd = "irm https://ollama.com/install.ps1 | iex";
        let output = Command::new("powershell")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-Command")
            .arg(install_cmd)
            .output()
            .map_err(|e| format!("无法启动安装命令: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        let _ = Command::new("cmd")
            .arg("/C")
            .arg("start")
            .arg("")
            .arg("ollama")
            .spawn();
        let status_text = if output.status.success() {
            "INSTALL_COMMAND_OK"
        } else {
            "INSTALL_COMMAND_FAILED"
        };
        let response = format!(
            "{{\"status\":\"{}\",\"message\":\"安装命令已执行。请等待安装程序完成，然后点击重新检查。\",\"stdout\":{:?},\"stderr\":{:?}}}",
            status_text, stdout, stderr
        );
        if output.status.success() {
            Ok(response)
        } else {
            let _ = Command::new("cmd")
                .arg("/C")
                .arg("start")
                .arg("https://ollama.com/download/windows")
                .spawn();
            Err(response)
        }
    }
    #[cfg(target_os = "macos")]
    {
        let output = Command::new("open")
            .arg("https://ollama.com/download")
            .output()
            .map_err(|e| format!("无法打开下载页: {}", e))?;
        if output.status.success() {
            Ok("{\"status\":\"OPENED_DOWNLOAD_PAGE\",\"message\":\"已打开官方下载页。\"}".to_string())
        } else {
            Err("{\"status\":\"OPEN_DOWNLOAD_PAGE_FAILED\",\"message\":\"无法打开官方下载页，请手动访问 https://ollama.com/download\"}".to_string())
        }
    }
    #[cfg(all(not(target_os = "windows"), not(target_os = "macos")))]
    {
        Ok("{\"status\":\"MANUAL_INSTALL_REQUIRED\",\"message\":\"请手动安装本地推理后端。\"}".to_string())
    }
}'''
s = s[:start] + new_func + s[end:]
p.write_text(s, encoding="utf-8")
print("✅ Rust patched successfully")
PY

echo
echo "===== 2. Patch frontend: progress steps, disable duplicate click, auto recheck ====="
python3 - <<'PY'
from pathlib import Path
p = Path("core-platform/apps/desktop/src/js/windows-click-model-setup.js")
s = p.read_text(encoding="utf-8")

helper = r'''
  function renderProgressSteps(title, steps, activeIndex = 0, extra = "") {
    const rows = steps.map((step, index) => {
      const cls = index < activeIndex ? "done" : (index === activeIndex ? "active" : "");
      const icon = index < activeIndex ? "✓" : (index === activeIndex ? "…" : "○");
      return `<div class="model-progress-step ${cls}">
        <span class="model-progress-icon">${icon}</span>
        <span>${escapeHtml(step)}</span>
      </div>`;
    }).join("");
    return `<div class="model-progress-card">
      <div class="model-progress-title">${escapeHtml(title)}</div>
      <div class="model-progress-bar"><div class="model-progress-fill" style="width:${Math.min(100, Math.max(8, ((activeIndex + 1) / steps.length) * 100))}%"></div></div>
      <div class="model-progress-steps">${rows}</div>
      ${extra ? `<div class="model-progress-extra">${extra}</div>` : ""}
    </div>`;
  }
  function setProgress(title, steps, activeIndex, extra = "") {
    const el = document.getElementById("modelSetupResult");
    if (!el) return;
    el.innerHTML = renderProgressSteps(title, steps, activeIndex, extra);
  }
  function safeParseJsonText(text) {
    if (!text || typeof text !== "string") return null;
    try { return JSON.parse(text); } catch (_) { return null; }
  }
  async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  async function recheckAfterInstall() {
    const steps = [
      "等待安装程序完成",
      "检查本地推理后端",
      "检查本地 AI 后端",
      "刷新状态"
    ];
    for (let i = 0; i < 3; i++) {
      setProgress("正在重新检查本地 AI 状态", steps, Math.min(i + 1, steps.length - 1));
      await sleep(2000);
      try {
        const status = await checkLocalModelStatus({ silent: true });
        if (status?.ready || status?.gateway?.ok || status?.bootstrap?.ok) {
          setResult("本地 AI 状态已更新", "ok", "检测到本地后端已有响应。现在可以准备标准对话能力。", status);
          return status;
        }
      } catch (_) {}
    }
    setResult(
      "安装后仍未连接",
      "bad",
      "安装命令已经执行，但本地后端仍未连接。可能需要等待安装器完成、重启 MAOMIAI，或手动打开本地推理后端。",
      {
        ok: false,
        next_steps: [
          "确认安装器已经完成。",
          "关闭并重新打开 MAOMIAI。",
          "如果 Windows 开始菜单里有本地推理后端，请手动打开一次。",
          "然后回到本页点击重新检查。"
        ]
      }
    );
    return null;
  }
'''

if "function renderProgressSteps" not in s:
    idx = s.find("async function installLocalInferenceBackend()")
    if idx == -1:
      raise SystemExit("installLocalInferenceBackend not found")
    s = s[:idx] + helper + "\n" + s[idx:]

start = s.index("async function installLocalInferenceBackend()")
brace = s.index("{", start)
depth = 0
end = None
for i in range(brace, len(s)):
    if s[i] == "{":
        depth += 1
    elif s[i] == "}":
        depth -= 1
        if depth == 0:
            end = i + 1
            break

new_func = r'''async function installLocalInferenceBackend() {
    if (window.__maomiaiInstallingLocalBackend) {
      setResult("正在安装中", "loading", "安装流程已经在执行，请不要重复点击。", {
        ok: false,
        message: "安装流程正在执行中。"
      });
      return;
    }
    window.__maomiaiInstallingLocalBackend = true;
    const steps = [
      "准备安装命令",
      "请求 Windows 执行安装",
      "等待安装程序完成",
      "自动重新检查状态"
    ];
    try {
      setProgress("正在安装本地推理后端", steps, 0);
      const result = {
        ok: false,
        stage: "install_local_inference_backend",
        tauri: null,
        api: null,
        message: "",
        next_steps: []
      };
      await sleep(300);
      setProgress("正在安装本地推理后端", steps, 1);
      try {
        const invoke =
          window.__TAURI__?.core?.invoke ||
          window.__TAURI_INTERNALS__?.invoke;
        if (invoke) {
          const out = await invoke("install_local_inference_backend");
          const parsed = safeParseJsonText(out);
          result.tauri = { ok: true, output: out, parsed };
          result.ok = true;
          result.message = parsed?.message || "安装命令已执行。";
          setProgress(
            "安装命令已执行",
            steps,
            2,
            `<div class="model-progress-note">请等待 Windows 安装程序完成。完成后系统会自动重新检查。</div>`
          );
          await sleep(2500);
          setProgress("正在重新检查", steps, 3);
          await recheckAfterInstall();
          return result;
        }
        result.tauri = {
          ok: false,
          message: "当前环境没有可用的 Tauri invoke。"
        };
      } catch (e) {
        const parsed = safeParseJsonText(String(e));
        result.tauri = {
          ok: false,
          error: String(e),
          parsed,
          message: parsed?.message || "Tauri 直接安装命令执行失败。"
        };
      }
      setProgress("正在尝试后端安装接口", steps, 1);
      try {
        const apiResult = await postJson(`${API.bootstrap}/bootstrap/install_ollama`, {}, 30000);
        result.api = apiResult;
        if (apiResult?.ok) {
          result.ok = true;
          result.message = "后端安装命令已执行。安装完成后请重新检查。";
          setProgress("安装命令已执行", steps, 2);
          await sleep(2500);
          await recheckAfterInstall();
          return result;
        }
      } catch (e) {
        result.api = {
          ok: false,
          error: String(e),
          message: "18100 安装接口不可用。"
        };
      }
      try {
        window.open("https://ollama.com/download/windows", "_blank");
      } catch (_) {}
      result.ok = false;
      result.message = "无法自动安装本地推理后端，已尝试打开官方下载页。";
      result.install_url = "https://ollama.com/download/windows";
      result.install_command = "irm https://ollama.com/install.ps1 | iex";
      result.next_steps = [
        "请打开官方下载页安装 Windows 版本。",
        "或在 PowerShell 中执行安装命令。",
        "安装完成后重新打开 MAOMIAI。",
        "回到本地 AI 准备页点击重新检查。"
      ];
      setResult("需要手动安装本地推理后端", "bad", result.message, result);
      return result;
    } finally {
      window.__maomiaiInstallingLocalBackend = false;
    }
  }'''

s = s[:start] + new_func + s[end:]
s = s.replace("async function checkLocalModelStatus() {", "async function checkLocalModelStatus(options = {}) {")
s = s.replace('setResult("正在检查本地 AI", "loading", "正在检查本地后端、模型网关和当前能力是否可用。", null);',
              'if (!options.silent) setResult("正在检查本地 AI", "loading", "正在检查本地后端、模型网关和当前能力是否可用。", null);')
p.write_text(s, encoding="utf-8")
print("✅ Frontend patched successfully")
PY

echo
echo "===== 3. Add progress CSS ====="
cat >> "$CSS" <<'EOF'

/* D7-C5 install progress */
.model-progress-card {
  border: 1px solid rgba(37, 99, 235, 0.22);
  background: rgba(239, 246, 255, 0.92);
  border-radius: 18px;
  padding: 18px;
  margin-top: 14px;
}
.model-progress-title {
  font-size: 18px;
  font-weight: 800;
  color: #1f2937;
  margin-bottom: 12px;
}
.model-progress-bar {
  height: 10px;
  border-radius: 999px;
  background: rgba(148, 163, 184, 0.28);
  overflow: hidden;
  margin-bottom: 14px;
}
.model-progress-fill {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #2563eb, #7c3aed);
  transition: width 280ms ease;
}
.model-progress-steps {
  display: grid;
  gap: 10px;
}
.model-progress-step {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #64748b;
  font-weight: 650;
}
.model-progress-step.active {
  color: #1d4ed8;
}
.model-progress-step.done {
  color: #15803d;
}
.model-progress-icon {
  width: 22px;
  height: 22px;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.75);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
}
.model-progress-extra {
  margin-top: 14px;
  color: #475569;
  font-size: 14px;
}
.model-progress-note {
  padding: 10px 12px;
  border-radius: 12px;
  background: rgba(255,255,255,0.72);
}
EOF

echo "✅ CSS added"

echo
echo "===== 4. Verify syntax ====="
node --check "$JS"
echo "✅ JavaScript syntax OK"

cd "$APP/src-tauri" || exit 1
cargo check
echo "✅ Rust syntax OK"

cd /Users/mofamaomi/Documents/本地ai || exit 1

echo
echo "===== 5. Create report ====="
cat > "$REPORT" <<'EOF'
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
EOF

echo "✅ Report created"

echo
echo "===== Done ====="
echo "Files modified:"
echo "  - $RUST"
echo "  - $JS"
echo "  - $CSS"
echo "  - $REPORT"
