# MAOMIAI Windows Full Delivery Package

这个目录是 Windows 完整交付包，不只是 GitHub Actions 的安装产物。

## 目录说明

```text
installers/
  Local AI Platform_*.exe      普通安装器
  Local AI Platform_*.msi      MSI 安装包
  desktop_lib.exe              裸可执行文件

runtime/
  scripts/windows/             Windows 后端启动、停止、状态、运行时准备脚本
  services/                    本地后端服务源码
  manual_start_backend.ps1     手动启动后端测试脚本
  manual_status_backend.ps1    手动检查后端状态脚本

BUILD_INFO.json                构建信息
```

## 推荐安装

优先使用：
```
installers/Local AI Platform_0.1.0_x64-setup.exe
```

## 如果 App 显示"本地 AI 暂未连接"

可以在 PowerShell 中执行：

```powershell
cd runtime
powershell -ExecutionPolicy Bypass -File .\manual_start_backend.ps1
powershell -ExecutionPolicy Bypass -File .\manual_status_backend.ps1
```

## 说明

GitHub Actions artifact 中通常只包含安装器、MSI 和 exe。

本 full delivery package 额外带上 runtime scripts 与 services，方便排查 Windows 后端启动问题。
