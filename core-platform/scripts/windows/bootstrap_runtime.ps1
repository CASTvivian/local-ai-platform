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
    if ($r -and (Test-Path (Join-Path $r.Path "services"))) {
      return $r.Path
    }
  }
  return (Resolve-Path (Join-Path $ScriptDir "..\..\..") -ErrorAction SilentlyContinue).Path
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
    "code" { return "qwen2.5-coder:7b" }
    "light" { return "qwen2.5:1.5b" }
    default { return "qwen2.5:7b" }
  }
}

function Test-Port {
  param([int]$Port)
  $conn = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
  return [bool]$conn
}

function Ensure-Ollama-Serve {
  $ollama = Find-Ollama
  if (!$ollama) {
    return @{
      ok = $false
      stage = "find_ollama"
      message = "未检测到本地推理后端。"
      install_url = "https://ollama.com/download/windows"
    }
  }
  if (Test-Port 11434) {
    return @{
      ok = $true
      stage = "serve"
      message = "本地推理后端已运行。"
      ollama = $ollama
      port = 11434
    }
  }
  try {
    Start-Process -FilePath $ollama -ArgumentList @("serve") -WindowStyle Hidden
    Start-Sleep -Seconds 4
  } catch {
    return @{
      ok = $false
      stage = "serve"
      message = "启动本地推理后端失败。"
      error = $_.Exception.Message
      ollama = $ollama
    }
  }
  if (Test-Port 11434) {
    return @{
      ok = $true
      stage = "serve"
      message = "本地推理后端已启动。"
      ollama = $ollama
      port = 11434
    }
  }
  return @{
    ok = $false
    stage = "serve"
    message = "已尝试启动本地推理后端，但 11434 端口暂未就绪。"
    ollama = $ollama
  }
}

function Get-Ollama-List {
  $ollama = Find-Ollama
  if (!$ollama) {
    return @{
      ok = $false
      message = "未检测到本地推理后端。"
      models = @()
    }
  }
  try {
    $out = & $ollama list 2>&1 | Out-String
    return @{
      ok = $true
      raw = $out
      models = $out
    }
  } catch {
    return @{
      ok = $false
      message = "读取本地模型列表失败。"
      error = $_.Exception.Message
      models = @()
    }
  }
}

function Pull-Model {
  param([string]$Profile)
  $ollama = Find-Ollama
  if (!$ollama) {
    return @{
      ok = $false
      stage = "pull"
      message = "未检测到本地推理后端，请先安装。"
      install_url = "https://ollama.com/download/windows"
    }
  }
  $serve = Ensure-Ollama-Serve
  if (!$serve.ok) {
    return @{
      ok = $false
      stage = "serve_before_pull"
      message = "本地推理后端未能启动，无法下载能力。"
      serve = $serve
    }
  }
  $model = Get-Model-For-Profile $Profile
  $before = Get-Ollama-List
  if ($before.raw -and ($before.raw -match [regex]::Escape($model))) {
    return @{
      ok = $true
      stage = "already_exists"
      profile = $Profile
      model = $model
      message = "所选能力已准备完成，无需重复下载。"
      list = $before
    }
  }
  $LogDir = Join-Path $Root "logs\windows"
  New-Item -ItemType Directory -Force -Path $LogDir | Out-Null
  $logFile = Join-Path $LogDir ("ollama-pull-" + $Profile + ".log")
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
    return @{
      ok = ($p.ExitCode -eq 0 -and $exists)
      stage = "pull"
      profile = $Profile
      model = $model
      exit_code = $p.ExitCode
      message = $(if ($p.ExitCode -eq 0 -and $exists) { "能力下载完成，已可以使用。" } else { "下载命令已结束，但未确认能力可用。" })
      log_file = $logFile
      raw_tail = $(if ($raw.Length -gt 4000) { $raw.Substring($raw.Length - 4000) } else { $raw })
      list = $after
    }
  } catch {
    return @{
      ok = $false
      stage = "pull"
      profile = $Profile
      model = $model
      message = "下载能力失败。"
      error = $_.Exception.Message
      log_file = $logFile
    }
  }
}

function Install-Ollama {
  $cmd = "irm https://ollama.com/install.ps1 | iex"
  try {
    $out = powershell -ExecutionPolicy Bypass -Command $cmd 2>&1 | Out-String
    return @{
      ok = $true
      stage = "install"
      message = "安装命令已执行。安装完成后会自动检查。"
      raw_tail = $(if ($out.Length -gt 4000) { $out.Substring($out.Length - 4000) } else { $out })
    }
  } catch {
    return @{
      ok = $false
      stage = "install"
      message = "自动安装失败，请使用官方下载页安装。"
      install_url = "https://ollama.com/download/windows"
      error = $_.Exception.Message
    }
  }
}

$Root = Resolve-Root $Root

switch ($Action) {
  "status" {
    $ollama = Find-Ollama
    $serve = Ensure-Ollama-Serve
    $list = Get-Ollama-List
    Write-Json @{
      ok = $true
      action = "status"
      root = $Root
      ollama_found = [bool]$ollama
      ollama = $ollama
      serve = $serve
      list = $list
      ready = ($serve.ok -and $list.ok)
    }
  }
  "install_ollama" {
    $install = Install-Ollama
    $serve = Ensure-Ollama-Serve
    Write-Json @{
      ok = ($install.ok -and $serve.ok)
      action = "install_ollama"
      install = $install
      serve = $serve
      message = $(if ($serve.ok) { "本地推理后端安装并启动完成。" } else { "安装命令已执行，请等待安装完成后重新检查。" })
    }
  }
  "ensure_ollama" {
    $serve = Ensure-Ollama-Serve
    Write-Json $serve
  }
  "pull_model" {
    $pull = Pull-Model $Profile
    Write-Json $pull
  }
  default {
    Write-Json @{
      ok = $false
      message = "未知操作。"
      action = $Action
    }
  }
}
