param(
  [string]$Action = 'status',
  [string]$Profile = 'standard',
  [string]$Root = ''
)
$ErrorActionPreference = 'Continue'

function Write-Json {
  param([object]$Obj)
  try {
    $Json = $Obj | ConvertTo-Json -Depth 16 -Compress
    $Bytes = [System.Text.Encoding]::UTF8.GetBytes($Json)
    $B64 = [System.Convert]::ToBase64String($Bytes)
    $Envelope = @{
      ok = $true;
      maomiai_payload_encoding = 'utf8-base64-json';
      maomiai_payload_b64 = $B64
    }
    $Envelope | ConvertTo-Json -Depth 4 -Compress
  } catch {
    $Fallback = @{
      ok = $false;
      maomiai_payload_encoding = 'plain';
      message = 'Failed to serialize JSON payload.';
      error = $_.Exception.Message
    }
    $Fallback | ConvertTo-Json -Depth 4 -Compress
  }
}

function Ensure-Dir {
  param([string]$Path)
  if (!(Test-Path $Path)) {
    New-Item -ItemType Directory -Force -Path $Path | Out-Null
  }
}

function Resolve-Root {
  param([string]$InputRoot)
  if (![string]::IsNullOrWhiteSpace($InputRoot) -and (Test-Path $InputRoot)) {
    return (Resolve-Path $InputRoot).Path
  }
  $ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
  $Candidate = Resolve-Path (Join-Path $ScriptDir '..\..\..') -ErrorAction SilentlyContinue
  if ($Candidate) {
    return $Candidate.Path
  }
  return $ScriptDir
}

function Find-Ollama {
  $Cmd = Get-Command ollama -ErrorAction SilentlyContinue
  if ($Cmd) {
    return $Cmd.Source
  }
  $Candidates = @(
    "$env:LOCALAPPDATA\Programs\Ollama\ollama.exe",
    "$env:ProgramFiles\Ollama\ollama.exe",
    "$env:ProgramFiles(x86)\Ollama\ollama.exe"
  )
  foreach ($Item in $Candidates) {
    if (Test-Path $Item) {
      return $Item
    }
  }
  return $null
}

function Get-Model-For-Profile {
  param([string]$ProfileName)
  switch ($ProfileName) {
    'standard' { return 'qwen2.5:7b' }
    'light' { return 'qwen2.5:1.5b' }
    'code' { return 'qwen2.5-coder:7b' }
    'reasoning' { return 'deepseek-r1:7b' }
    'english' { return 'llama3.1:8b' }
    'small' { return 'llama3.2:3b' }
    'embed' { return 'nomic-embed-text' }
    'embed_multi' { return 'bge-m3' }
    default { return 'qwen2.5:7b' }
  }
}

function Test-Ollama-Api {
  try {
    $Response = Invoke-RestMethod -Uri 'http://127.0.0.1:11434/api/tags' -TimeoutSec 3
    return @{ ok = $true; response = $Response }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message }
  }
}

function Ensure-Ollama-Installed {
  $Ollama = Find-Ollama
  if ($Ollama) {
    return @{
      ok = $true;
      installed = $true;
      ollama = $Ollama;
      message = 'Ollama is installed.'
    }
  }
  $LogDir = Join-Path $Root 'logs\windows'
  Ensure-Dir $LogDir
  $LogFile = Join-Path $LogDir 'install-ollama.log'
  try {
    $InstallCommand = 'irm https://ollama.com/install.ps1 | iex'
    $Output = powershell -NoProfile -ExecutionPolicy Bypass -Command $InstallCommand 2>&1 | Out-String
    Set-Content -Path $LogFile -Value $Output -Encoding UTF8
    Start-Sleep -Seconds 3
    $OllamaAfter = Find-Ollama
    return @{
      ok = [bool]$OllamaAfter;
      installed = [bool]$OllamaAfter;
      ollama = $OllamaAfter;
      message = $(if ($OllamaAfter) { 'Ollama installed.' } else { 'Install command executed, but ollama.exe was not found yet.' });
      log_file = $LogFile;
      raw_tail = $(if ($Output.Length -gt 4000) { $Output.Substring($Output.Length - 4000) } else { $Output })
    }
  } catch {
    return @{
      ok = $false;
      installed = $false;
      message = 'Failed to install Ollama.';
      error = $_.Exception.Message;
      log_file = $LogFile;
      install_url = 'https://ollama.com/download/windows'
    }
  }
}

function Ensure-Ollama-Serve {
  $Install = Ensure-Ollama-Installed
  if (!$Install.ok) {
    return @{
      ok = $false;
      stage = 'install';
      install = $Install;
      message = 'Ollama is not installed.'
    }
  }
  $Ollama = $Install.ollama
  $Api = Test-Ollama-Api
  if ($Api.ok) {
    return @{
      ok = $true;
      stage = 'serve';
      message = 'Ollama service is already running.';
      ollama = $Ollama;
      api = $Api
    }
  }
  try {
    Start-Process -FilePath $Ollama -ArgumentList @('serve') -WindowStyle Hidden
    Start-Sleep -Seconds 5
  } catch {
    return @{
      ok = $false;
      stage = 'serve';
      message = 'Failed to start Ollama service.';
      error = $_.Exception.Message;
      ollama = $Ollama
    }
  }
  $ApiAfter = Test-Ollama-Api
  return @{
    ok = $ApiAfter.ok;
    stage = 'serve';
    message = $(if ($ApiAfter.ok) { 'Ollama service started.' } else { 'Ollama service started, but API is not ready yet.' });
    ollama = $Ollama;
    api = $ApiAfter
  }
}

function Get-Ollama-List {
  $Ollama = Find-Ollama
  if (!$Ollama) {
    return @{ ok = $false; message = 'Ollama was not found.'; raw = '' }
  }
  try {
    $Output = & $Ollama list 2>&1 | Out-String
    return @{ ok = $true; raw = $Output }
  } catch {
    return @{ ok = $false; error = $_.Exception.Message; raw = '' }
  }
}

function Save-Job {
  param([hashtable]$Job)
  $JobDir = Join-Path $Root 'runtime\jobs'
  Ensure-Dir $JobDir
  $File = Join-Path $JobDir ('model-download-' + $Job.profile + '.json')
  $Job | ConvertTo-Json -Depth 16 | Set-Content -Path $File -Encoding UTF8
  return $File
}

function Get-Log-Tail {
  param(
    [string]$Path,
    [int]$MaxChars = 3000
  )
  if (!(Test-Path $Path)) {
    return ''
  }
  try {
    $Text = Get-Content $Path -Raw -ErrorAction SilentlyContinue
    if ($Text.Length -gt $MaxChars) {
      return $Text.Substring($Text.Length - $MaxChars)
    }
    return $Text
  } catch {
    return ''
  }
}

function Update-Model-Pull-Job {
  param(
    [string]$ProfileName,
    [string]$Status,
    [string]$Message,
    [int]$Progress = 0,
    [bool]$Installed = $false,
    [string]$LastLog = '',
    [string]$ErrorMessage = ''
  )
  $Model = Get-Model-For-Profile $ProfileName
  $JobDir = Join-Path $Root 'runtime\jobs'
  Ensure-Dir $JobDir
  $JobFile = Join-Path $JobDir ('model-download-' + $ProfileName + '.json')
  $Existing = $null
  if (Test-Path $JobFile) {
    try {
      $Existing = Get-Content $JobFile -Raw | ConvertFrom-Json
    } catch {}
  }
  $StartedAt = $(if ($Existing -and $Existing.started_at) { $Existing.started_at } else { (Get-Date).ToString('s') })
  $Elapsed = 0
  try {
    $Elapsed = [int]((Get-Date) - [datetime]$StartedAt).TotalSeconds
  } catch {}
  $Job = @{
    ok = ($Status -ne 'failed');
    profile = $ProfileName;
    model = $Model;
    status = $Status;
    progress = $Progress;
    message = $Message;
    last_log = $LastLog;
    installed = $Installed;
    error = $ErrorMessage;
    started_at = $StartedAt;
    updated_at = (Get-Date).ToString('s');
    elapsed_seconds = $Elapsed
  }
  $Job | ConvertTo-Json -Depth 16 | Set-Content -Path $JobFile -Encoding UTF8
  return $JobFile
}

function Start-Model-Pull-Job {
  param([string]$ProfileName)
  $Model = Get-Model-For-Profile $ProfileName
  $JobDir = Join-Path $Root 'runtime\jobs'
  $LogDir = Join-Path $Root 'logs\windows'
  Ensure-Dir $JobDir
  Ensure-Dir $LogDir
  $JobFile = Join-Path $JobDir ('model-download-' + $ProfileName + '.json')
  $StdoutFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.err.log')
  $Serve = Ensure-Ollama-Serve
  if (!$Serve.ok) {
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'failed' `
      -Message 'Ollama service could not be started.' `
      -Progress 0 `
      -Installed $false `
      -ErrorMessage 'serve_failed' | Out-Null
    return @{
      ok = $false;
      profile = $ProfileName;
      model = $Model;
      status = 'failed';
      message = 'Ollama service could not be started.';
      job_file = $JobFile;
      serve = $Serve
    }
  }
  $ListBefore = Get-Ollama-List
  if ($ListBefore.raw -and ($ListBefore.raw -match [regex]::Escape($Model))) {
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'completed' `
      -Message 'Selected capability is already installed.' `
      -Progress 100 `
      -Installed $true | Out-Null
    return @{
      ok = $true;
      profile = $ProfileName;
      model = $Model;
      status = 'completed';
      progress = 100;
      installed = $true;
      message = 'Selected capability is already installed.';
      job_file = $JobFile
    }
  }
  Update-Model-Pull-Job `
    -ProfileName $ProfileName `
    -Status 'running' `
    -Message 'Downloading model. Please keep the app open.' `
    -Progress 10 `
    -Installed $false | Out-Null
  $ScriptPath = $MyInvocation.MyCommand.Path
  $CommandLine = '-NoProfile -ExecutionPolicy Bypass -File "' + $ScriptPath + '" -Action pull_model -Profile "' + $ProfileName + '" -Root "' + $Root + '"'
  try {
    Start-Process -FilePath 'powershell' -ArgumentList $CommandLine -WindowStyle Hidden | Out-Null
    return @{
      ok = $true;
      profile = $ProfileName;
      model = $Model;
      status = 'started';
      progress = 10;
      message = 'Model download started in background.';
      job_file = $JobFile;
      stdout_file = $StdoutFile;
      stderr_file = $StderrFile
    }
  } catch {
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'failed' `
      -Message 'Failed to start background download.' `
      -Progress 0 `
      -Installed $false `
      -ErrorMessage $_.Exception.Message | Out-Null
    return @{
      ok = $false;
      profile = $ProfileName;
      model = $Model;
      status = 'failed';
      message = 'Failed to start background download.';
      error = $_.Exception.Message;
      job_file = $JobFile
    }
  }
}

function Get-Model-Pull-Job {
  param([string]$ProfileName)
  $Model = Get-Model-For-Profile $ProfileName
  $JobDir = Join-Path $Root 'runtime\jobs'
  $LogDir = Join-Path $Root 'logs\windows'
  $JobFile = Join-Path $JobDir ('model-download-' + $ProfileName + '.json')
  $StdoutFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.err.log')
  $Status = 'not_started'
  $Progress = 0
  $ExistingError = ''
  if (Test-Path $JobFile) {
    try {
      $Existing = Get-Content $JobFile -Raw | ConvertFrom-Json
      $Status = $Existing.status
      $Progress = [int]$Existing.progress
      $ExistingError = $Existing.error
    } catch {}
  }
  $Stdout = Get-Log-Tail $StdoutFile 6000
  $Stderr = Get-Log-Tail $StderrFile 6000
  $Combined = ($Stdout + "`n" + $Stderr)
  $Matches = [regex]::Matches($Combined, '([0-9]{1,3})\.?[0-9]*%')
  if ($Matches.Count -gt 0) {
    $Last = $Matches[$Matches.Count - 1].Groups[1].Value
    [int]::TryParse($Last, [ref]$Progress) | Out-Null
  }
  $List = Get-Ollama-List
  $Exists = $false
  if ($List.raw -and ($List.raw -match [regex]::Escape($Model))) {
    $Exists = $true
  }
  if ($Exists) {
    $Status = 'completed'
    $Progress = 100
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'completed' `
      -Message 'Model download completed.' `
      -Progress 100 `
      -Installed $true `
      -LastLog $Combined | Out-Null
  } elseif ($Status -eq 'downloading') {
    $Status = 'running'
  } elseif ($Status -eq 'done') {
    $Status = 'completed'
  }
  $StartedAt = $null
  $Elapsed = 0
  if (Test-Path $JobFile) {
    try {
      $Existing = Get-Content $JobFile -Raw | ConvertFrom-Json
      $StartedAt = $Existing.started_at
      if ($StartedAt) {
        $Elapsed = [int]((Get-Date) - [datetime]$StartedAt).TotalSeconds
      }
    } catch {}
  }
  return @{
    ok = $true;
    profile = $ProfileName;
    model = $Model;
    status = $Status;
    progress = $Progress;
    message = $(if ($Status -eq 'completed') { 'Model download completed.' } elseif ($Status -eq 'failed') { 'Model download failed.' } elseif ($Status -eq 'running') { 'Downloading model. Please keep the app open.' } else { 'No model download job is running.' });
    job_file = $JobFile;
    stdout_file = $StdoutFile;
    stderr_file = $StderrFile;
    stdout_tail = $Stdout;
    stderr_tail = $Stderr;
    last_log = $Combined;
    elapsed_seconds = $Elapsed;
    error = $ExistingError;
    installed = $Exists;
    list = $List
  }
}

function Pull-Model {
  param([string]$ProfileName)
  $Model = Get-Model-For-Profile $ProfileName
  $Serve = Ensure-Ollama-Serve
  if (!$Serve.ok) {
    return @{
      ok = $false;
      stage = 'serve';
      profile = $ProfileName;
      model = $Model;
      message = 'Ollama service could not be started.';
      serve = $Serve
    }
  }
  $ListBefore = Get-Ollama-List
  if ($ListBefore.raw -and ($ListBefore.raw -match [regex]::Escape($Model))) {
    return @{
      ok = $true;
      stage = 'already_exists';
      profile = $ProfileName;
      model = $Model;
      message = 'Selected capability is already installed.';
      list = $ListBefore
    }
  }
  $LogDir = Join-Path $Root 'logs\windows'
  Ensure-Dir $LogDir
  $StdoutFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.err.log')
  $Ollama = Find-Ollama
  try {
    $Process = Start-Process -FilePath $Ollama -ArgumentList @('pull', $Model) -WindowStyle Hidden -PassThru -Wait -RedirectStandardOutput $StdoutFile -RedirectStandardError $StderrFile
    $ListAfter = Get-Ollama-List
    $Exists = $false
    if ($ListAfter.raw -and ($ListAfter.raw -match [regex]::Escape($Model))) {
      $Exists = $true
    }
    $Tail = (Get-Log-Tail $StdoutFile 3000) + "`n" + (Get-Log-Tail $StderrFile 3000)
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status $(if ($Exists) { 'completed' } else { 'failed' }) `
      -Message $(if ($Exists) { 'Model download completed.' } else { 'Pull command finished, but model was not confirmed.' }) `
      -Progress $(if ($Exists) { 100 } else { 0 }) `
      -Installed $Exists `
      -LastLog $Tail `
      -ErrorMessage $(if ($Exists) { '' } else { 'model_not_confirmed' }) | Out-Null
    return @{
      ok = $Exists;
      stage = 'pull';
      profile = $ProfileName;
      model = $Model;
      exit_code = $Process.ExitCode;
      message = $(if ($Exists) { 'Model capability is downloaded and ready.' } else { 'Pull command finished, but model was not confirmed.' });
      stdout_file = $StdoutFile;
      stderr_file = $StderrFile;
      list = $ListAfter
    }
  } catch {
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'failed' `
      -Message 'Model download failed.' `
      -Progress 0 `
      -Installed $false `
      -LastLog ((Get-Log-Tail $StdoutFile 3000) + "`n" + (Get-Log-Tail $StderrFile 3000)) `
      -ErrorMessage $_.Exception.Message | Out-Null
    return @{
      ok = $false;
      stage = 'pull';
      profile = $ProfileName;
      model = $Model;
      message = 'Model download failed.';
      error = $_.Exception.Message;
      stdout_file = $StdoutFile;
      stderr_file = $StderrFile
    }
  }
}

function Generate-Text {
  param(
    [string]$ProfileName,
    [string]$Prompt
  )
  $Model = Get-Model-For-Profile $ProfileName
  if ($env:MAOMIAI_PROMPT_B64) {
    try {
      $PromptBytes = [System.Convert]::FromBase64String($env:MAOMIAI_PROMPT_B64)
      $Prompt = [System.Text.Encoding]::UTF8.GetString($PromptBytes)
    } catch {
      $Prompt = ''
    }
  } elseif ($env:MAOMIAI_PROMPT_FILE -and (Test-Path $env:MAOMIAI_PROMPT_FILE)) {
    try {
      $Prompt = Get-Content -Path $env:MAOMIAI_PROMPT_FILE -Raw -Encoding UTF8
    } catch {
      $Prompt = ''
    }
  }
  if ([string]::IsNullOrWhiteSpace($Prompt)) {
    return @{
      ok = $false;
      stage = 'prompt';
      profile = $ProfileName;
      model = $Model;
      message = 'Prompt is empty.'
    }
  }
  $Serve = Ensure-Ollama-Serve
  if (!$Serve.ok) {
    return @{
      ok = $false;
      stage = 'serve';
      profile = $ProfileName;
      model = $Model;
      message = 'Ollama service could not be started.';
      serve = $Serve
    }
  }
  $List = Get-Ollama-List
  if (!($List.raw -and ($List.raw -match [regex]::Escape($Model)))) {
    return @{
      ok = $false;
      stage = 'model_missing';
      profile = $ProfileName;
      model = $Model;
      message = 'Selected model is not installed. Please download it first.';
      list = $List
    }
  }
  try {
    $SystemPrompt = 'You are MAOMIAI local AI assistant. Always answer in Simplified Chinese. Be concise, direct, and helpful. The user has already provided a question. Do not say you did not receive a prompt unless the prompt is empty.'
    $BodyObj = @{
      model = $Model;
      stream = $false;
      messages = @(
        @{ role = 'system'; content = $SystemPrompt },
        @{ role = 'user'; content = $Prompt }
      );
      options = @{ temperature = 0.7 }
    }
    $Body = $BodyObj | ConvertTo-Json -Depth 16
    $BodyBytes = [System.Text.Encoding]::UTF8.GetBytes($Body)
    $Response = Invoke-RestMethod -Uri 'http://127.0.0.1:11434/api/chat' -Method Post -ContentType 'application/json; charset=utf-8' -Body $BodyBytes -TimeoutSec 300
    $Text = ''
    if ($Response.message -and $Response.message.content) {
      $Text = $Response.message.content
    } elseif ($Response.response) {
      $Text = $Response.response
    }
    return @{
      ok = $true;
      stage = 'chat';
      profile = $ProfileName;
      model = $Model;
      response = $Text;
      raw = $Response
    }
  } catch {
    return @{
      ok = $false;
      stage = 'chat';
      profile = $ProfileName;
      model = $Model;
      message = 'Local inference request failed.';
      error = $_.Exception.Message
    }
  }
}

$Root = Resolve-Root $Root

switch ($Action) {
  'status' {
    $Serve = Ensure-Ollama-Serve
    $List = Get-Ollama-List
    Write-Json @{
      ok = $true;
      action = 'status';
      root = $Root;
      serve = $Serve;
      list = $List;
      ready = ($Serve.ok -and $List.ok)
    }
  }
  'install_ollama' {
    $Install = Ensure-Ollama-Installed
    $Serve = Ensure-Ollama-Serve
    Write-Json @{
      ok = ($Install.ok -and $Serve.ok);
      action = 'install_ollama';
      install = $Install;
      serve = $Serve;
      message = $(if ($Serve.ok) { 'Ollama is installed and running.' } else { 'Install command executed, but service is not ready yet.' })
    }
  }
  'start_pull_model' {
    $Started = Start-Model-Pull-Job $Profile
    Write-Json $Started
  }
  'job_status' {
    $Status = Get-Model-Pull-Job $Profile
    Write-Json $Status
  }
  'pull_model' {
    $Pull = Pull-Model $Profile
    Write-Json $Pull
  }
  'generate_text' {
    $Text = ''
    if ($env:MAOMIAI_PROMPT_B64) {
      try {
        $TextBytes = [System.Convert]::FromBase64String($env:MAOMIAI_PROMPT_B64)
        $Text = [System.Text.Encoding]::UTF8.GetString($TextBytes)
      } catch {
        $Text = ''
      }
    } elseif ($env:MAOMIAI_PROMPT_FILE -and (Test-Path $env:MAOMIAI_PROMPT_FILE)) {
      try {
        $Text = Get-Content -Path $env:MAOMIAI_PROMPT_FILE -Raw -Encoding UTF8
      } catch {
        $Text = ''
      }
    } elseif ($env:MAOMIAI_PROMPT) {
      $Text = $env:MAOMIAI_PROMPT
    }
    $Generated = Generate-Text $Profile $Text
    Write-Json $Generated
  }
  default {
    Write-Json @{
      ok = $false;
      action = $Action;
      message = 'Unknown action.'
    }
  }
}
