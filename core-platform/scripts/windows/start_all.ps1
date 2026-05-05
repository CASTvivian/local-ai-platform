param(
  [string]$Root = ""
)

$ErrorActionPreference = "Continue"

if ([string]::IsNullOrWhiteSpace($Root)) {
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $Root = Resolve-Path (Join-Path $ScriptDir "..\..")
}

Write-Host "MAOMIAI Windows service startup"
Write-Host "Root: $Root"

$LogDir = Join-Path $Root "logs\windows"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

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

  $LogFile = Join-Path $LogDir "$Name.log"
  $Args = @(
    "-m", "uvicorn",
    $Module,
    "--host", "127.0.0.1",
    "--port", "$Port"
  )

  Start-Process `
    -FilePath "python" `
    -ArgumentList $Args `
    -WorkingDirectory $Root `
    -WindowStyle Hidden `
    -RedirectStandardOutput $LogFile `
    -RedirectStandardError $LogFile

  Start-Sleep -Milliseconds 500
}

Start-PythonService -Name "model_gateway" -Module "services.model_gateway.main:app" -Port 18080
Start-PythonService -Name "model_bootstrap" -Module "core-platform.services.model_bootstrap_service.main:app" -Port 18100

Write-Host "Startup requested."
