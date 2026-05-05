param(
  [string]$Root = "",
  [switch]$Force = $false
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
  $candidates = @(
    (Join-Path $ScriptDir "..\..\.."),
    (Join-Path $ScriptDir "..\.."),
    (Join-Path $ScriptDir "..")
  )
  foreach ($c in $candidates) {
    $r = Resolve-Path $c -ErrorAction SilentlyContinue
    if ($r -and (Test-Path (Join-Path $r.Path "services"))) {
      return $r.Path
    }
  }
  return (Resolve-Path (Join-Path $ScriptDir "..\..\..") -ErrorAction SilentlyContinue).Path
}

$Root = Resolve-Root $Root
$RuntimeDir = Join-Path $Root "runtime"
$PythonDir = Join-Path $RuntimeDir "python"
$PythonExe = Join-Path $PythonDir "python.exe"
$GetPip = Join-Path $RuntimeDir "get-pip.py"
$LogDir = Join-Path $Root "logs\windows"

New-Item -ItemType Directory -Force -Path $RuntimeDir | Out-Null
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

function Download-File {
  param([string]$Url, [string]$OutFile)
  try {
    Invoke-WebRequest -Uri $Url -OutFile $OutFile -UseBasicParsing
    return @{ ok = $true; url = $Url; file = $OutFile }
  } catch {
    return @{ ok = $false; url = $Url; file = $OutFile; error = $_.Exception.Message }
  }
}

function Enable-EmbeddedPythonImports {
  param([string]$Dir)
  $pth = Get-ChildItem $Dir -Filter "*._pth" -ErrorAction SilentlyContinue | Select-Object -First 1
  if ($pth) {
    $txt = Get-Content $pth.FullName -Raw
    if ($txt -notmatch "import site") {
      $txt = $txt + "`nimport site`n"
      Set-Content -Path $pth.FullName -Value $txt -Encoding ASCII
    }
  }
}

function Ensure-EmbeddedPython {
  if ((Test-Path $PythonExe) -and !$Force) {
    return @{ ok = $true; python = $PythonExe; message = "内置 Python 已存在。" }
  }
  $zip = Join-Path $RuntimeDir "python-embed.zip"
  # 先使用稳定版本。后续可以改为 manifest 配置。
  $url = "https://www.python.org/ftp/python/3.12.8/python-3.12.8-embed-amd64.zip"
  $dl = Download-File $url $zip
  if (-not $dl.ok) {
    return @{
      ok = $false
      stage = "download_python"
      message = "下载内置 Python 失败。"
      detail = $dl
      next_steps = @(
        "请检查网络。",
        "或手动安装 Python 3.11/3.12 后重试。"
      )
    }
  }
  try {
    if (Test-Path $PythonDir) { Remove-Item $PythonDir -Recurse -Force }
    New-Item -ItemType Directory -Force -Path $PythonDir | Out-Null
    Expand-Archive -Path $zip -DestinationPath $PythonDir -Force
    Enable-EmbeddedPythonImports $PythonDir
  } catch {
    return @{
      ok = $false
      stage = "extract_python"
      message = "解压内置 Python 失败。"
      error = $_.Exception.Message
    }
  }
  if (!(Test-Path $PythonExe)) {
    return @{
      ok = $false
      stage = "verify_python"
      message = "内置 Python 解压后未找到 python.exe。"
    }
  }
  return @{ ok = $true; python = $PythonExe; message = "内置 Python 已准备完成。" }
}

function Run-Python {
  param([string[]]$Args)
  try {
    $p = Start-Process -FilePath $PythonExe -ArgumentList $Args -NoNewWindow -PassThru -Wait -RedirectStandardOutput "$env:TEMP\maomiai_py_stdout.txt" -RedirectStandardError "$env:TEMP\maomiai_py_stderr.txt"
    $stdout = ""
    $stderr = ""
    if (Test-Path "$env:TEMP\maomiai_py_stdout.txt") { $stdout = Get-Content "$env:TEMP\maomiai_py_stdout.txt" -Raw }
    if (Test-Path "$env:TEMP\maomiai_py_stderr.txt") { $stderr = Get-Content "$env:TEMP\maomiai_py_stderr.txt" -Raw }
    return @{
      ok = ($p.ExitCode -eq 0)
      exit_code = $p.ExitCode
      stdout = $stdout
      stderr = $stderr
      args = $Args
    }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message; args = $Args }
  }
}

function Ensure-Pip {
  $check = Run-Python @("-m", "pip", "--version")
  if ($check.ok) {
    return @{ ok = $true; message = "pip 已存在。"; detail = $check }
  }
  $url = "https://bootstrap.pypa.io/get-pip.py"
  $dl = Download-File $url $GetPip
  if (-not $dl.ok) {
    return @{
      ok = $false
      stage = "download_get_pip"
      message = "下载 get-pip.py 失败。"
      detail = $dl
    }
  }
  $install = Run-Python @($GetPip, "--no-warn-script-location")
  $recheck = Run-Python @("-m", "pip", "--version")
  return @{
    ok = $recheck.ok
    message = $(if ($recheck.ok) { "pip 安装完成。" } else { "pip 安装失败。" })
    install = $install
    recheck = $recheck
  }
}

function Ensure-BackendDeps {
  $check = Run-Python @("-c", "import fastapi, uvicorn, pydantic; print('deps ok')")
  if ($check.ok) {
    return @{ ok = $true; message = "后端依赖已存在。"; detail = $check }
  }
  $install = Run-Python @("-m", "pip", "install", "--no-warn-script-location", "fastapi", "uvicorn", "pydantic")
  $recheck = Run-Python @("-c", "import fastapi, uvicorn, pydantic; print('deps ok')")
  return @{
    ok = $recheck.ok
    message = $(if ($recheck.ok) { "后端依赖安装完成。" } else { "后端依赖安装失败。" })
    install = $install
    recheck = $recheck
  }
}

$py = Ensure-EmbeddedPython
if (-not $py.ok) {
  Write-Json @{
    ok = $false
    root = $Root
    runtime = $RuntimeDir
    python = $py
  }
  exit
}
$pip = Ensure-Pip
$deps = if ($pip.ok) { Ensure-BackendDeps } else { @{ ok = $false; message = "pip 未就绪，跳过后端依赖安装。"; pip = $pip } }
Write-Json @{
  ok = ($py.ok -and $pip.ok -and $deps.ok)
  root = $Root
  runtime = $RuntimeDir
  python_exe = $PythonExe
  python = $py
  pip = $pip
  deps = $deps
}
