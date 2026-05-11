param(
  [string]$Action = "status",
  [string]$Profile = "standard",
  [string]$Root = ""
)
$ErrorActionPreference = "Continue"

function Write-Json($obj) {
  $obj | ConvertTo-Json -Depth 12 -Compress
}

function Resolve-Root {
  param([string]$InputRoot)
  if (![string]::IsNullOrWhiteSpace($InputRoot) -and (Test-Path $InputRoot)) {
    return (Resolve-Path $InputRoot).Path
  }
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  foreach ($c in @(
    (Join-Path $ScriptDir "..\..\.."),
    (Join-Path $ScriptDir "..\.."),
    (Join-Path $ScriptDir "..")
  )) {
    $r = Resolve-Path $c -ErrorAction SilentlyContinue
    if ($r) { return $r.Path }
  }
  return $ScriptDir
}

function Find-Ollama {
  $cmd = Get-Command ollama -ErrorAction SilentlyContinue
  if ($cmd) { return $cmd.Source }
  $candidates = @(
    "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe",
    "$env:ProgramFiles\Ollama\ollama.exe",
    "$env:ProgramFiles(x86)\Ollama\ollama.exe"
  )
  foreach ($c in $candidates) {
    if (Test-Path $c) { return $c }
  }
  return $null
}

function Get-Model-For-Profile {
  param([string]$Profile)
  switch ($Profile) {
    "standard" { return "qwen2.5:7b" }
    "light" { return "qwen2.5:1.5b" }
    "code" { return "qwen2.5-coder:7b" }
    "reasoning" { return "deepseek-r1:7b" }
    "english" { return "llama3.1:8b" }
    "small" { return "llama3.2:3b" }
    "embed" { return "nomic-embed-text" }
    "embed_multi" { return "bge-m3" }
    default { return "qwen2.5:7b" }
  }
}

function Test-OllamaApi {
  try {
    $r = Invoke-RestMethod "http://127.0.0.1:11434/api/tags" -TimeoutSec 3
    return @{ ok = $true; response = $r }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message }
  }
}

function Ensure-Ollama-Installed {
  $ollama = Find-Ollama
  if ($ollama) {
    return @{
      ok = $true
      installed = $true
      ollama = $ollama
      message = "本地推理后端已安装。"
    }
  }
  $InstallDir = Join-Path $Root "runtime\downloads"
  New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
  $logFile = Join-Path $Root "logs\windows\install-ollama.log"
  New-Item -ItemType Directory -Force -Path (Split-Path $logFile -Parent) | Out-Null
  try {
    $cmd = "irm https://ollama.com/install.ps1 | iex"
    $out = powershell -ExecutionPolicy Bypass -Command $cmd 2>&1 | Out-String
    Set-Content -Path $logFile -Value $out -Encoding UTF8
    Start-Sleep -Seconds 3
    $ollama2 = Find-Ollama
    return @{
      ok = [bool]$ollama2
      installed = [bool]$ollama2
      ollama = $ollama2
      message = $(if ($ollama2) { "本地推理后端安装完成。" } else { "安装命令已执行，但暂未检测到可执行文件。" })
      log_file = $logFile
      raw_tail = $(if ($out.Length -gt 4000) { $out.Substring($out.Length - 4000) } else { $out })
    }
  } catch {
    return @{
      ok = $false
      installed = $false
      message = "自动安装本地推理后端失败。"
      error = $_.Exception.Message
      log_file = $logFile
      install_url = "https://ollama.com/download/windows"
    }
  }
}

function Ensure-Ollama-Serve {
  $install = Ensure-Ollama-Installed
  if (!$install.ok) {
    return @{
      ok = $false
      stage = "install"
      install = $install
      message = "本地推理后端未安装，无法启动。"
    }
  }
  $ollama = $install.ollama
  $api = Test-OllamaApi
  if ($api.ok) {
    return @{
      ok = $true
      stage = "serve"
      message = "本地推理服务已运行。"
      ollama = $ollama
      api = $api
    }
  }
  try {
    Start-Process -FilePath $ollama -ArgumentList @("serve") -WindowStyle Hidden
    Start-Sleep -Seconds 5
  } catch {
    return @{
      ok = $false
      stage = "serve"
      message = "启动本地推理服务失败。"
      error = $_.Exception.Message
      ollama = $ollama
    }
  }
  $api2 = Test-OllamaApi
  return @{
    ok = $api2.ok
    stage = "serve"
    message = $(if ($api2.ok) { "本地推理服务已启动。" } else { "已尝试启动，但 API 暂未就绪。" })
    ollama = $ollama
    api = $api2
  }
}

function Get-Ollama-List {
  $ollama = Find-Ollama
  if (!$ollama) {
    return @{
      ok = $false
      message = "未检测到本地推理后端。"
      raw = ""
    }
  }
  try {
    $out = & $ollama list 2>&1 | Out-String
    return @{
      ok = $true
      raw = $out
    }
  } catch {
    return @{
      ok = $false
      error = $_.Exception.Message
      raw = ""
    }
  }
}

function Save-Job {
  param([hashtable]$Job)
  $JobDir = Join-Path $Root "runtime\jobs"
  New-Item -ItemType Directory -Force -Path $JobDir | Out-Null
  $file = Join-Path $JobDir ("model-download-" + $Job.profile + ".json")
  $Job | ConvertTo-Json -Depth 12 | Set-Content -Path $file -Encoding UTF8
  return $file
}

function Pull-Model {
  param([string]$Profile)
  $model = Get-Model-For-Profile $Profile
  $job = @{
    profile = $Profile
    model = $model
    status = "starting"
    started_at = (Get-Date).ToString("s")
    progress = 0
  }
  $jobFile = Save-Job $job

  $serve = Ensure-Ollama-Serve
  if (!$serve.ok) {
    $job.status = "failed"
    $job.error = "serve_failed"
    $job.serve = $serve
    Save-Job $job | Out-Null
    return @{
      ok = $false
      stage = "serve"
      profile = $Profile
      model = $model
      message = "本地推理服务未能启动，无法下载模型。"
      job_file = $jobFile
      serve = $serve
    }
  }

  $listBefore = Get-Ollama-List
  if ($listBefore.raw -and ($listBefore.raw -match [regex]::Escape($model))) {
    $job.status = "done"
    $job.progress = 100
    Save-Job $job | Out-Null
    return @{
      ok = $true
      stage = "already_exists"
      profile = $Profile
      model = $model
      message = "该能力已安装，可以直接启用。"
      job_file = $jobFile
      list = $listBefore
    }
  }

  $LogDir = Join-Path $Root "logs\windows"
  New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
  $logFile = Join-Path $LogDir ("ollama-pull-" + $Profile + ".log")
  $ollama = Find-Ollama

  $job.status = "downloading"
  $job.progress = 10
  $job.log_file = $logFile
  Save-Job $job | Out-Null

  try {
    $p = Start-Process `
      -FilePath $ollama `
      -ArgumentList @("pull", $model) `
      -WindowStyle Hidden `
      -PassThru `
      -Wait `
      -RedirectStandardOutput $logFile `
      -RedirectStandardError $logFile

    $raw = ""
    if (Test-Path $logFile) {
      $raw = Get-Content $logFile -Raw -ErrorAction SilentlyContinue
    }

    $after = Get-Ollama-List
    $exists = $false
    if ($after.raw -and ($after.raw -match [regex]::Escape($model))) {
      $exists = $true
    }

    $job.status = $(if ($exists) { "done" } else { "failed" })
    $job.progress = $(if ($exists) { 100 } else { 80 })
    $job.exit_code = $p.ExitCode
    Save-Job $job | Out-Null

    return @{
      ok = $exists
      stage = "pull"
      profile = $Profile
      model = $model
      exit_code = $p.ExitCode
      message = $(if ($exists) { "模型能力已下载并启用。" } else { "下载命令结束，但未确认模型可用。" })
      job_file = $jobFile
      log_file = $logFile
      raw_tail = $(if ($raw.Length -gt 4000) { $raw.Substring($raw.Length - 4000) } else { $raw })
      list = $after
    }
  } catch {
    $job.status = "failed"
    $job.error = $_.Exception.Message
    Save-Job $job | Out-Null
    return @{
      ok = $false
      stage = "pull"
      profile = $Profile
      model = $model
      message = "模型下载失败。"
      error = $_.Exception.Message
      job_file = $jobFile
      log_file = $logFile
    }
  }
}

$Root = Resolve-Root $Root

switch ($Action) {
  "status" {
    $serve = Ensure-Ollama-Serve
    $list = Get-Ollama-List
    Write-Json @{
      ok = $true
      action = "status"
      root = $Root
      serve = $serve
      list = $list
      ready = ($serve.ok -and $list.ok)
    }
  }
  "install_ollama" {
    $install = Ensure-Ollama-Installed
    $serve = Ensure-Ollama-Serve
    Write-Json @{
      ok = ($install.ok -and $serve.ok)
      action = "install_ollama"
      install = $install
      serve = $serve
      message = $(if ($serve.ok) { "本地推理后端已安装并启动。" } else { "安装已执行，但服务暂未就绪。" })
    }
  }
  "pull_model" {
    $pull = Pull-Model $Profile
    Write-Json $pull
  }
  default {
    Write-Json @{
      ok = $false
      action = $Action
      message = "未知操作。"
    }
  }
}
