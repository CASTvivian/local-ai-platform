param(
  [string]$Root = ""
)
$ErrorActionPreference = "Continue"

function Write-Json {
  param([object]$Obj)
  $Obj | ConvertTo-Json -Depth 20 -Compress
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
  return $ScriptDir
}

function Test-Http {
  param([string]$Url)
  try {
    $R = Invoke-RestMethod -Uri $Url -Method Get -TimeoutSec 3
    return @{ ok = $true; data = $R }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message }
  }
}

$RuntimeRoot = Resolve-RuntimeRoot $Root
$Checks = [ordered]@{
  model_bootstrap_service = "http://127.0.0.1:18100/health"
  model_gateway = "http://127.0.0.1:18080/health"
  repo_memory_service = "http://127.0.0.1:18125/health"
  skill_store_service = "http://127.0.0.1:18121/health"
  workflow_store_service = "http://127.0.0.1:18126/health"
  agent_runtime_service = "http://127.0.0.1:18131/health"
  ollama = "http://127.0.0.1:11434/api/tags"
}

$Result = [ordered]@{
  ok = $true
  runtime_root = $RuntimeRoot
  checked_at = (Get-Date).ToString("s")
  checks = [ordered]@{}
}

foreach ($Name in $Checks.Keys) {
  $R = Test-Http $Checks[$Name]
  $Result.checks[$Name] = $R
  if (-not $R.ok) {
    $Result.ok = $false
  }
}

Write-Json $Result
