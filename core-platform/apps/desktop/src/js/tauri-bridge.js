// P3.14-D3-X2 extracted Tauri bridge helpers
async function tauriInvoke(cmd, args = {}) {
  const w = window;
  if (w.__TAURI__ && w.__TAURI__.core && w.__TAURI__.core.invoke) {
    return await w.__TAURI__.core.invoke(cmd, args);
  }
  if (w.__TAURI__ && w.__TAURI__.tauri && w.__TAURI__.tauri.invoke) {
    return await w.__TAURI__.tauri.invoke(cmd, args);
  }
  throw new Error("Tauri invoke is not available. Open this UI inside the desktop app.");
}

async function openArtifactPath(path) {
  try {
    const res = await tauriInvoke("open_file", { path });
    systemMessage("已调用系统打开文件：" + JSON.stringify(res));
  } catch (e) {
    systemMessage("打开文件失败：" + e.message);
  }
}

async function revealArtifactPath(path) {
  try {
    const res = await tauriInvoke("reveal_in_file_manager", { path });
    systemMessage("已在文件夹中显示：" + JSON.stringify(res));
  } catch (e) {
    systemMessage("显示文件失败：" + e.message);
  }
}
