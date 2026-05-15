param(
  [string]$Root = ""
)
$ErrorActionPreference = "Continue"

function Write-Json {
  param([object]$Obj)
  $Obj | ConvertTo-Json -Depth 20 -Compress
}

function Ensure-Dir {
  param([string]$Path)
  if (!(Test-Path $Path)) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
  }
}

function Resolve-RuntimeRoot {
  param([string]$InputRoot)
  if (![string]::IsNullOrWhiteSpace($InputRoot) -and (Test-Path $InputRoot)) {
    return (Resolve-Path $InputRoot).Path
  }
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $Candidates = @(
    (Join-Path $ScriptDir "..\..\.."),
    (Join-Path $ScriptDir "..\.."),
    (Join-Path $ScriptDir "..")
  )
  foreach ($Candidate in $Candidates) {
    $Resolved = Resolve-Path $Candidate -ErrorAction SilentlyContinue
    if ($Resolved -and (Test-Path (Join-Path $Resolved.Path "services"))) {
      return $Resolved.Path
    }
  }
  $Fallback = Resolve-Path (Join-Path $ScriptDir "..\..\..") -ErrorAction SilentlyContinue
  if ($Fallback) {
    return $Fallback.Path
  }
  return $ScriptDir
}

function Find-Python {
  param([string]$RuntimeRoot)
  $Embedded = Join-Path $RuntimeRoot "runtime\python\python.exe"
  $Candidates = @(
    $Embedded,
    "python",
    "python3",
    "$env:LOCALAPPDATA\Programs\Python\Python312\python.exe",
    "$env:LOCALAPPDATA\Programs\Python\Python311\python.exe",
    "$env:ProgramFiles\Python312\python.exe",
    "$env:ProgramFiles\Python311\python.exe"
  )
  foreach ($Item in $Candidates) {
    try {
      if (Test-Path $Item) {
        return $Item
      }
      $Cmd = Get-Command $Item -ErrorAction SilentlyContinue
      if ($Cmd) {
        return $Cmd.Source
      }
    } catch {}
  }
  return $null
}

function Test-Http {
  param([string]$Url)
  try {
    Invoke-RestMethod -Uri $Url -Method Get -TimeoutSec 3 | Out-Null
    return $true
  } catch {
    return $false
  }
}

function Read-Tail {
  param(
    [string]$Path,
    [int]$Lines = 80
  )
  if (!(Test-Path $Path)) {
    return ""
  }
  try {
    return (Get-Content $Path -Tail $Lines -ErrorAction SilentlyContinue) -join "`n"
  } catch {
    return ""
  }
}

function Ensure-PythonRuntime {
  param([string]$RuntimeRoot)
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $EnsureScript = Join-Path $ScriptDir "ensure_runtime.ps1"
  if (!(Test-Path $EnsureScript)) {
    return @{ ok = $true; skipped = $true; reason = "ensure_runtime_missing" }
  }
  try {
    $Output = powershell.exe -NoProfile -ExecutionPolicy Bypass -File $EnsureScript -Root $RuntimeRoot
    try {
      return ($Output | ConvertFrom-Json)
    } catch {
      return @{ ok = $true; raw = ($Output | Out-String) }
    }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message }
  }
}

function Start-ServiceProcess {
  param(
    [string]$Name,
    [string]$Module,
    [int]$Port,
    [string]$RuntimeRoot,
    [string]$Python,
    [string]$LogDir,
    [string]$PidDir
  )
  $HealthUrl = "http://127.0.0.1:$Port/health"
  if (Test-Http $HealthUrl) {
    return @{
      name = $Name
      ok = $true
      already_running = $true
      port = $Port
      health = $HealthUrl
    }
  }
  if (-not $Python) {
    return @{
      name = $Name
      ok = $false
      error = "python_not_found"
      port = $Port
    }
  }
  $Stdout = Join-Path $LogDir "$Name.out.log"
  $Stderr = Join-Path $LogDir "$Name.err.log"
  $PidFile = Join-Path $PidDir "$Name.pid"
  $Args = @("-m", "uvicorn", $Module, "--host", "127.0.0.1", "--port", "$Port")
  try {
    $Proc = Start-Process `
      -FilePath $Python `
      -ArgumentList $Args `
      -WorkingDirectory $RuntimeRoot `
      -WindowStyle Hidden `
      -PassThru `
      -RedirectStandardOutput $Stdout `
      -RedirectStandardError $Stderr
    $Proc.Id | Set-Content -Path $PidFile -Encoding ASCII
  } catch {
    return @{
      name = $Name
      ok = $false
      error = "process_start_failed"
      message = $_.Exception.Message
      port = $Port
      stdout = $Stdout
      stderr = $Stderr
    }
  }
  for ($i = 0; $i -lt 35; $i++) {
    Start-Sleep -Milliseconds 800
    if (Test-Http $HealthUrl) {
      return @{
        name = $Name
        ok = $true
        pid = $Proc.Id
        port = $Port
        health = $HealthUrl
        stdout = $Stdout
        stderr = $Stderr
      }
    }
  }
  return @{
    name = $Name
    ok = $false
    pid = $Proc.Id
    port = $Port
    health = $HealthUrl
    stdout = $Stdout
    stderr = $Stderr
    error = "health_timeout"
    stdout_tail = (Read-Tail $Stdout)
    stderr_tail = (Read-Tail $Stderr)
  }
}

$RuntimeRoot = Resolve-RuntimeRoot $Root
$LogDir = Join-Path $RuntimeRoot "logs\windows"
$PidDir = Join-Path $RuntimeRoot "runtime\pids"
Ensure-Dir $LogDir
Ensure-Dir $PidDir

$Runtime = Ensure-PythonRuntime $RuntimeRoot
$Python = Find-Python $RuntimeRoot

$Services = @(
  @{ name = "model_bootstrap_service"; module = "services.model_bootstrap_service.main:app"; port = 18100 },
  @{ name = "model_gateway"; module = "services.model_gateway.main:app"; port = 18080 },
  @{ name = "repo_memory_service"; module = "services.repo_memory_service.main:app"; port = 18125 },
  @{ name = "skill_store_service"; module = "services.skill_store_service.main:app"; port = 18121 },
  @{ name = "workflow_store_service"; module = "services.workflow_store_service.main:app"; port = 18126 },
  @{ name = "agent_runtime_service"; module = "services.agent_runtime_service.main:app"; port = 18131 }
)

$Result = [ordered]@{
  ok = $true
  runtime_root = $RuntimeRoot
  python = $Python
  runtime = $Runtime
  started_at = (Get-Date).ToString("s")
  services = @()
}

foreach ($Svc in $Services) {
  $R = Start-ServiceProcess `
    -Name $Svc.name `
    -Module $Svc.module `
    -Port $Svc.port `
    -RuntimeRoot $RuntimeRoot `
    -Python $Python `
    -LogDir $LogDir `
    -PidDir $PidDir
  $Result.services += $R
  if (-not $R.ok) {
    $Result.ok = $false
  }
}

Write-Json $Result
