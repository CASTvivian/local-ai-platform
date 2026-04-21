@echo off
setlocal

cd /d %~dp0\..

echo [Local AI Platform] starting services...

if not exist .venv\Scripts\python.exe (
  echo ERROR: .venv\Scripts\python.exe not found
  pause
  exit /b 1
)

start "model_gateway" cmd /c ".venv\Scripts\python.exe -m uvicorn services.model_gateway.main:app --host 0.0.0.0 --port 18080"
start "orchestrator" cmd /c ".venv\Scripts\python.exe -m uvicorn services.agent_orchestrator.main:app --host 0.0.0.0 --port 18081"
start "plugin_manager" cmd /c ".venv\Scripts\python.exe -m uvicorn services.plugin_manager.main:app --host 0.0.0.0 --port 18082"
start "real_impl" cmd /c ".venv\Scripts\python.exe -m uvicorn services.real_impl_service.main:app --host 0.0.0.0 --port 18095"
start "agent_team" cmd /c ".venv\Scripts\python.exe -m uvicorn services.agent_team_service.main:app --host 0.0.0.0 --port 18094"
start "research_real" cmd /c ".venv\Scripts\python.exe -m uvicorn services.research_real_service.main:app --host 0.0.0.0 --port 18098"
start "hyperframes" cmd /c ".venv\Scripts\python.exe -m uvicorn services.hyperframes_service.main:app --host 0.0.0.0 --port 18099"
start "model_bootstrap" cmd /c ".venv\Scripts\python.exe -m uvicorn services.model_bootstrap_service.main:app --host 0.0.0.0 --port 18100"

echo services launched
exit /b 0
