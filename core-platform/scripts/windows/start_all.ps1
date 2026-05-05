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
$LogDir = Join-Path $Root "logs\windows"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

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

Write-Host "Startup requested."
