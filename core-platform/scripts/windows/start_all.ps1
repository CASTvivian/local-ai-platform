param(
  [string]$Root = ""
)
$ErrorActionPreference = "Continue"
Write-Host "===== MAOMIAI Windows service startup ====="

if ([string]::IsNullOrWhiteSpace($Root)) {
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

  # Installed Tauri resources may place this under:
  # resources\scripts\windows\start_all.ps1
  # or directly under scripts\windows\start_all.ps1
  $Candidates = @(
    (Resolve-Path (Join-Path $ScriptDir "..\..\..") -ErrorAction SilentlyContinue),
    (Resolve-Path (Join-Path $ScriptDir "..\..") -ErrorAction SilentlyContinue),
    (Resolve-Path (Join-Path $ScriptDir "..") -ErrorAction SilentlyContinue)
  )
  foreach ($c in $Candidates) {
    if ($c -and (Test-Path (Join-Path $c "services"))) {
      $Root = $c.Path
      break
    }
  }
  if ([string]::IsNullOrWhiteSpace($Root)) {
    $Root = Resolve-Path (Join-Path $ScriptDir "..\..\..") -ErrorAction SilentlyContinue
    if ($Root) { $Root = $Root.Path }
  }
}

Write-Host "Root: $Root"

$EnsureRuntimeScript = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "ensure_runtime.ps1"
$EmbeddedPython = $null
if (Test-Path $EnsureRuntimeScript) {
  Write-Host "Preparing embedded runtime..."
  $runtimeResultRaw = powershell -ExecutionPolicy Bypass -File $EnsureRuntimeScript -Root $Root
  Write-Host $runtimeResultRaw
  try {
    $runtimeResult = $runtimeResultRaw | ConvertFrom-Json
    if ($runtimeResult.ok -and $runtimeResult.python_exe) {
      $EmbeddedPython = $runtimeResult.python_exe
      Write-Host "Embedded Python ready: $EmbeddedPython"
    }
  } catch {
    Write-Host "Failed to parse runtime result: $($_.Exception.Message)"
  }
}

$LogDir = Join-Path $Root "logs\windows"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

# Ensure Python dependencies before starting services.
$BootstrapScript = Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) "bootstrap_runtime.ps1"
if (Test-Path $BootstrapScript) {
  Write-Host "Checking Python dependencies..."
  powershell -ExecutionPolicy Bypass -File $BootstrapScript -Action ensure_deps
}

function Find-Python {
  $py = Get-Command python -ErrorAction SilentlyContinue
  if ($py) { return $py.Source }

  $pyLauncher = Get-Command py -ErrorAction SilentlyContinue
  if ($pyLauncher) { return $pyLauncher.Source }

  return $null
}

function Start-PythonService {
  param(
    [string]$Name,
    [string]$Module,
    [int]$Port
  )

  Write-Host "Starting $Name on $Port..."
  $Existing = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
  if ($Existing) {
    Write-Host "$Name already has port $Port in use."
    return
  }

  $Python = Find-Python
  if (-not $Python) {
    Write-Host "Python not found. Cannot start $Name."
    return
  }

  $LogFile = Join-Path $LogDir "$Name.log"
  $Args = @("-m", "uvicorn", $Module, "--host", "127.0.0.1", "--port", "$Port")
  Write-Host "Command: $Python $($Args -join ' ')"
  Write-Host "Log: $LogFile"

  Start-Process `
    -FilePath $Python `
    -ArgumentList $Args `
    -WorkingDirectory $Root `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $LogFile

  Start-Sleep -Milliseconds 800
}

# Module paths are relative to resource root.
Start-PythonService -Name "model_gateway" -Module "services.model_gateway.main:app" -Port 18080
Start-PythonService -Name "model_bootstrap" -Module "services.model_bootstrap_service.main:app" -Port 18100
Start-PythonService -Name "skill_store" -Module "services.skill_store_service.main:app" -Port 18121
Start-PythonService -Name "repo_memory" -Module "services.repo_memory_service.main:app" -Port 18125
Start-PythonService -Name "workflow_store" -Module "services.workflow_store_service.main:app" -Port 18126
Start-PythonService -Name "agent_runtime" -Module "services.agent_runtime_service.main:app" -Port 18131

Write-Host "Startup requested."
