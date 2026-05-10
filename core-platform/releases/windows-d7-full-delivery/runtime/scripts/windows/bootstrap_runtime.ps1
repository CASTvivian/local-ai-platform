param(
  [string]$Action = "status",
  [string]$Profile = "standard"
)
$ErrorActionPreference = "Continue"

function Write-Json($obj) {
  $obj | ConvertTo-Json -Depth 12 -Compress
}

function Find-Python {
  $python = Get-Command python -ErrorAction SilentlyContinue
  if ($python) { return $python.Source }
  $py = Get-Command py -ErrorAction SilentlyContinue
  if ($py) { return $py.Source }
  return $null
}

function Run-Cmd {
  param([string]$File, [string[]]$Args)
  try {
    $p = Start-Process -FilePath $File -ArgumentList $Args -NoNewWindow -PassThru -Wait -RedirectStandardOutput "$env:TEMP\maomiai_stdout.txt" -RedirectStandardError "$env:TEMP\maomiai_stderr.txt"
    $stdout = ""
    $stderr = ""
    if (Test-Path "$env:TEMP\maomiai_stdout.txt") { $stdout = Get-Content "$env:TEMP\maomiai_stdout.txt" -Raw }
    if (Test-Path "$env:TEMP\maomiai_stderr.txt") { $stderr = Get-Content "$env:TEMP\maomiai_stderr.txt" -Raw }
    return @{
      ok = ($p.ExitCode -eq 0)
      exit_code = $p.ExitCode
      stdout = $stdout
      stderr = $stderr
      command = "$File $($Args -join ' ')"
    }
  } catch {
    return @{
      ok = $false
      error = $_.Exception.Message
      command = "$File $($Args -join ' ')"
    }
  }
}

function Find-Ollama {
  $ollama = Get-Command ollama -ErrorAction SilentlyContinue
  if ($ollama) { return $ollama.Source }
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

function Test-Port {
  param([int]$Port)
  $c = Get-NetTCPConnection -LocalPort $Port -ErrorAction SilentlyContinue
  return [bool]$c
}

function Ensure-PythonDeps {
  $python = Find-Python
  if (-not $python) {
    return @{
      ok = $false
      reason = "python_missing"
      message = "未检测到 Python，无法启动本地后端服务。"
      next_steps = @(
        "请先安装 Python 3.11 或 3.12。",
        "安装时勾选 Add Python to PATH。",
        "安装后重新打开 MAOMIAI。"
      )
    }
  }
  $check = Run-Cmd $python @("-c", "import fastapi,uvicorn,pydantic; print('deps ok')")
  if ($check.ok) {
    return @{
      ok = $true
      python = $python
      message = "Python 依赖已就绪。"
      detail = $check
    }
  }
  $install = Run-Cmd $python @("-m", "pip", "install", "--user", "fastapi", "uvicorn", "pydantic")
  $recheck = Run-Cmd $python @("-c", "import fastapi,uvicorn,pydantic; print('deps ok')")
  return @{
    ok = $recheck.ok
    python = $python
    message = $(if ($recheck.ok) { "Python 依赖安装完成。" } else { "Python 依赖安装失败。" })
    install = $install
    recheck = $recheck
  }
}

function Get-Status {
  $python = Find-Python
  $ollama = Find-Ollama
  $ollamaApi = $false
  $models = @()
  try {
    $r = Invoke-RestMethod "http://127.0.0.1:11434/api/tags" -TimeoutSec 3
    $ollamaApi = $true
    $models = $r.models
  } catch {
    # Ignore errors
  }
  return @{
    ok = $true
    python_found = [bool]$python
    python_path = $python
    port_18080 = Test-Port 18080
    port_18100 = Test-Port 18100
    ollama_found = [bool]$ollama
    ollama_path = $ollama
    ollama_api = $ollamaApi
    models = $models
    message = "诊断完成。"
  }
}

function Install-Ollama {
  try {
    $cmd = "irm https://ollama.com/install.ps1 | iex"
    $p = Start-Process -FilePath "powershell" -ArgumentList @("-ExecutionPolicy", "Bypass", "-Command", $cmd) -Wait -PassThru
    return @{
      ok = ($p.ExitCode -eq 0)
      exit_code = $p.ExitCode
      message = $(if ($p.ExitCode -eq 0) { "Ollama 安装命令已执行。" } else { "Ollama 安装命令执行失败。" })
      source = "https://ollama.com/download/windows"
    }
  } catch {
    return @{
      ok = $false
      error = $_.Exception.Message
      message = "无法自动执行 Ollama 安装。"
      next_steps = @(
        "请打开 https://ollama.com/download/windows 下载安装。",
        "安装完成后重新点击检查。"
      )
    }
  }
}

function Ensure-Ollama {
  $ollama = Find-Ollama
  if (-not $ollama) {
    return @{
      ok = $false
      reason = "ollama_missing"
      message = "未检测到本地推理后端。"
      install_url = "https://ollama.com/download/windows"
      install_command = "irm https://ollama.com/install.ps1 | iex"
      next_steps = @(
        "点击安装或打开官方下载页安装。",
        "安装完成后重新打开 MAOMIAI。",
        "再点击检查本地 AI 状态。"
      )
    }
  }
  try {
    Invoke-RestMethod "http://127.0.0.1:11434/api/tags" -TimeoutSec 3 | Out-Null
    return @{
      ok = $true
      ollama = $ollama
      api = $true
      message = "本地推理后端已运行。"
    }
  } catch {
    try {
      Start-Process -FilePath $ollama -WindowStyle Hidden
      Start-Sleep -Seconds 3
      Invoke-RestMethod "http://127.0.0.1:11434/api/tags" -TimeoutSec 5 | Out-Null
      return @{
        ok = $true
        ollama = $ollama
        api = $true
        message = "本地推理后端已启动。"
      }
    } catch {
      return @{
        ok = $false
        ollama = $ollama
        api = $false
        error = $_.Exception.Message
        message = "已检测到本地推理后端，但无法启动 API。"
      }
    }
  }
}

function Pull-Model {
  param([string]$Profile)
  $ollama = Find-Ollama
  if (-not $ollama) {
    return @{
      ok = $false
      reason = "ollama_missing"
      message = "无法下载模型：未检测到本地推理后端。"
    }
  }
  $model = if ($Profile -eq "code") {
    if ($env:MAOMIAI_CODE_MODEL) { $env:MAOMIAI_CODE_MODEL } else { "qwen2.5-coder:7b" }
  } else {
    if ($env:MAOMIAI_STANDARD_MODEL) { $env:MAOMIAI_STANDARD_MODEL } else { "qwen2.5:7b" }
  }
  $res = Run-Cmd $ollama @("pull", $model)
  return @{
    ok = $res.ok
    profile = $Profile
    model = $model
    message = $(if ($res.ok) { "本地 AI 能力准备完成。" } else { "模型下载失败。" })
    result = $res
  }
}

# Main dispatcher
if ($Action -eq "status") {
  Write-Json (Get-Status)
  exit
}

if ($Action -eq "ensure_deps") {
  Write-Json (Ensure-PythonDeps)
  exit
}

if ($Action -eq "install_ollama") {
  Write-Json (Install-Ollama)
  exit
}

if ($Action -eq "ensure_ollama") {
  Write-Json (Ensure-Ollama)
  exit
}

if ($Action -eq "pull_model") {
  Write-Json (Pull-Model $Profile)
  exit
}

Write-Json @{
  ok = $false
  message = "未知操作。"
  action = $Action
}
