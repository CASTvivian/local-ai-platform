param(
  [string]$InstallDir = "$env:LOCALAPPDATA\Local AI Platform",
  [string]$ProgramDir = "$env:LOCALAPPDATA\Programs\Local AI Platform"
)

$ErrorActionPreference = "Continue"

function Write-Section($Text) {
  Write-Host ""
  Write-Host "=============================="
  Write-Host $Text
  Write-Host "=============================="
}

function Test-HttpJson($Name, $Url) {
  Write-Host "Testing $Name -> $Url"
  try {
    $r = Invoke-RestMethod -Uri $Url -Method Get -TimeoutSec 5
    Write-Host "OK $Name"
    return @{ ok = $true; data = $r }
  } catch {
    Write-Host "FAIL $Name : $($_.Exception.Message)"
    return @{ ok = $false; error = $_.Exception.Message }
  }
}

Write-Section "C25 Windows Final Acceptance"

$Result = [ordered]@{
  checked_at = (Get-Date).ToString("s")
  install_dirs = @{}
  files = @{}
  services = @{}
  agent_runtime = @{}
  model = @{}
  final = @{}
}

Write-Section "1. Locate install directories"
$CandidateDirs = @(
  $InstallDir,
  $ProgramDir,
  "$env:LOCALAPPDATA\Programs\MAOMIAI",
  "$env:LOCALAPPDATA\MAOMIAI"
)

foreach ($d in $CandidateDirs) {
  $exists = Test-Path $d
  $Result.install_dirs[$d] = $exists
  Write-Host "$d -> $exists"
}

Write-Section "2. Check runtime files"
$RuntimeRootCandidates = @(
  "$env:LOCALAPPDATA\Local AI Platform\maomiai-runtime",
  "$env:LOCALAPPDATA\Programs\Local AI Platform\maomiai-runtime",
  "$env:LOCALAPPDATA\MAOMIAI\maomiai-runtime"
)

$RuntimeRoot = $null
foreach ($r in $RuntimeRootCandidates) {
  if (Test-Path $r) {
    $RuntimeRoot = $r
    break
  }
}

if (!$RuntimeRoot) {
  Write-Host "Runtime root not found yet. It may be created after first app launch."
} else {
  Write-Host "Runtime root: $RuntimeRoot"
}

$RequiredRelative = @(
  "scripts\windows\bootstrap_runtime.ps1",
  "scripts\windows\start_all.ps1",
  "scripts\windows\status_all.ps1",
  "services\agent_runtime_service\main.py",
  "services\model_gateway\main.py",
  "services\model_bootstrap_service\main.py",
  "services\repo_memory_service\main.py",
  "services\skill_store_service\main.py",
  "services\workflow_store_service\main.py",
  "data\agent_policy\planner_policy.json",
  "data\sandbox_policy\sandbox_policy.json",
  "data\agent_team\team_registry.json"
)

foreach ($rel in $RequiredRelative) {
  $path = if ($RuntimeRoot) { Join-Path $RuntimeRoot $rel } else { "" }
  $ok = ($RuntimeRoot -and (Test-Path $path))
  $Result.files[$rel] = $ok
  Write-Host "$rel -> $ok"
}

Write-Section "3. Check service health"
$Result.services["agent_runtime_18131"] = Test-HttpJson "agent_runtime" "http://127.0.0.1:18131/health"
$Result.services["model_gateway_18080"] = Test-HttpJson "model_gateway" "http://127.0.0.1:18080/health"
$Result.services["repo_memory_18125"] = Test-HttpJson "repo_memory" "http://127.0.0.1:18125/health"
$Result.services["skill_store_18121"] = Test-HttpJson "skill_store" "http://127.0.0.1:18121/health"
$Result.services["workflow_store_18126"] = Test-HttpJson "workflow_store" "http://127.0.0.1:18126/health"

Write-Section "4. Agent Runtime APIs"
try {
  $body = @{
    input = "请用一句话介绍你自己"
    session_id = "windows-c25-acceptance"
    source = "windows-acceptance"
  } | ConvertTo-Json -Depth 8

  $agentRun = Invoke-RestMethod -Uri "http://127.0.0.1:18131/agent/run" -Method Post -Body $body -ContentType "application/json" -TimeoutSec 30
  $Result.agent_runtime["agent_run"] = @{ ok = $true; data = $agentRun }
  Write-Host "OK /agent/run"

  $runId = $agentRun.run_id
  if (!$runId -and $agentRun.raw) { $runId = $agentRun.raw.run_id }

  if ($runId) {
    $timeline = Invoke-RestMethod -Uri "http://127.0.0.1:18131/agent/replay/timeline/$runId" -Method Get -TimeoutSec 10
    $Result.agent_runtime["timeline"] = @{ ok = $true; run_id = $runId; events = $timeline.events.Count }
    Write-Host "OK timeline events: $($timeline.events.Count)"
  } else {
    $Result.agent_runtime["timeline"] = @{ ok = $false; error = "no run_id returned" }
    Write-Host "WARN no run_id returned"
  }
} catch {
  $Result.agent_runtime["agent_run"] = @{ ok = $false; error = $_.Exception.Message }
  Write-Host "FAIL /agent/run : $($_.Exception.Message)"
}

Write-Section "5. MCP / Capability / Team APIs"
$Result.agent_runtime["mcp_tools"] = Test-HttpJson "mcp_tools" "http://127.0.0.1:18131/agent/mcp/tools"
$Result.agent_runtime["capabilities"] = Test-HttpJson "capabilities" "http://127.0.0.1:18131/agent/capabilities"
$Result.agent_runtime["team_registry"] = Test-HttpJson "team_registry" "http://127.0.0.1:18131/agent/team/registry"
$Result.agent_runtime["planner_health"] = Test-HttpJson "planner_health" "http://127.0.0.1:18131/agent/health/planner"

Write-Section "6. Team run smoke"
try {
  $teamBody = @{
    input = "请检查当前平台具备哪些智能体能力"
    session_id = "windows-c25-team-acceptance"
    max_rounds = 1
  } | ConvertTo-Json -Depth 8

  $team = Invoke-RestMethod -Uri "http://127.0.0.1:18131/agent/team/run" -Method Post -Body $teamBody -ContentType "application/json" -TimeoutSec 60
  $Result.agent_runtime["team_run"] = @{ ok = $true; team_run_id = $team.team_run_id; data = $team }
  Write-Host "OK team_run: $($team.team_run_id)"
} catch {
  $Result.agent_runtime["team_run"] = @{ ok = $false; error = $_.Exception.Message }
  Write-Host "FAIL team_run : $($_.Exception.Message)"
}

Write-Section "7. Save acceptance result"
$OutDir = "$env:USERPROFILE\Desktop\maomiai-c25-acceptance"
New-Item -ItemType Directory -Force -Path $OutDir | Out-Null
$OutFile = Join-Path $OutDir "c25-final-acceptance-result.json"
$Result | ConvertTo-Json -Depth 20 | Set-Content -Path $OutFile -Encoding UTF8
Write-Host "Saved: $OutFile"

Write-Section "Acceptance summary"
Write-Host "Please send this file back:"
Write-Host $OutFile