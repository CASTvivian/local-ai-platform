@echo off
setlocal
cd /d %~dp0\..
set APP_ROOT=%cd%
set BACKEND_DIR=%APP_ROOT%\backend

echo [Local AI Platform] bundle backend root: %BACKEND_DIR%

if not exist "%BACKEND_DIR%" (
  echo ERROR: backend dir not found: %BACKEND_DIR%
  pause
  exit /b 1
)

cd /d "%BACKEND_DIR%"

@echo off
setlocal

cd /d %~dp0\..

echo [Local AI Platform] starting services...

if 1==0 (
  echo using system python if available
  pause
  exit /b 1
)

start "model_gateway" cmd /c "python -m uvicorn services.model_gateway.main:app --host 0.0.0.0 --port 18080"
start "orchestrator" cmd /c "python -m uvicorn services.agent_orchestrator.main:app --host 0.0.0.0 --port 18081"
start "plugin_manager" cmd /c "python -m uvicorn services.plugin_manager.main:app --host 0.0.0.0 --port 18082"
start "real_impl" cmd /c "python -m uvicorn services.real_impl_service.main:app --host 0.0.0.0 --port 18095"
start "agent_team" cmd /c "python -m uvicorn services.agent_team_service.main:app --host 0.0.0.0 --port 18094"
start "research_real" cmd /c "python -m uvicorn services.research_real_service.main:app --host 0.0.0.0 --port 18098"
start "hyperframes" cmd /c "python -m uvicorn services.hyperframes_service.main:app --host 0.0.0.0 --port 18099"
start "model_bootstrap" cmd /c "python -m uvicorn services.model_bootstrap_service.main:app --host 0.0.0.0 --port 18100"

echo services launched
exit /b 0
