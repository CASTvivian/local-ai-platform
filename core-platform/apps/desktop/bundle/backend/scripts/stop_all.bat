@echo off
setlocal

cd /d %~dp0\..

echo [Local AI Platform] stopping services...

taskkill /F /IM python.exe /FI "WINDOWTITLE eq model_gateway*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq orchestrator*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq plugin_manager*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq real_impl*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq agent_team*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq research_real*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq hyperframes*" 2>nul
taskkill /F /IM python.exe /FI "WINDOWTITLE eq model_bootstrap*" 2>nul

echo services stopped
exit /b 0
