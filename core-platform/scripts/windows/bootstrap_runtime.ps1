param(
  [string]$Action = 'status',
  [string]$Profile = 'standard',
  [string]$Root = ''
)
$ErrorActionPreference = 'Continue'
$MAOMIAI_BOOTSTRAP_RUNTIME_VERSION = 'c25-c11-fix6-powershell-path-quoting'

function Add-Bootstrap-Version {
  param([object]$Obj)
  try {
    if ($Obj -is [hashtable] -or $Obj -is [System.Collections.Specialized.OrderedDictionary]) {
      $Obj['bootstrap_version'] = $MAOMIAI_BOOTSTRAP_RUNTIME_VERSION
    } else {
      $Obj | Add-Member -NotePropertyName bootstrap_version -NotePropertyValue $MAOMIAI_BOOTSTRAP_RUNTIME_VERSION -Force
    }
  } catch {}
  return $Obj
}

function Write-Json {
  param([object]$Obj)
  try {
    $Obj = Add-Bootstrap-Version $Obj
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
  try {
    $Response = Invoke-RestMethod -Uri 'http://127.0.0.1:11434/api/tags' -Method Get -TimeoutSec 5
    $Names = @()
    if ($Response.models) {
      foreach ($Item in $Response.models) {
        if ($Item.name) {
          $Names += [string]$Item.name
        }
      }
    }
    return @{
      ok = $true;
      provider = 'ollama_http_tags';
      raw = ($Names -join "`n");
      models = $Response.models
    }
  } catch {
    $Ollama = Find-Ollama
    if (!$Ollama) {
      return @{ ok = $false; message = 'Ollama was not found.'; raw = ''; error = $_.Exception.Message }
    }
    try {
      $Output = & $Ollama list 2>&1 | Out-String
      return @{ ok = $true; provider = 'ollama_cli_list'; raw = $Output }
    } catch {
      return @{ ok = $false; error = $_.Exception.Message; raw = '' }
    }
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

function Test-Model-Installed {
  param([string]$Model)
  $List = Get-Ollama-List
  return [bool]($List.raw -and ($List.raw -match [regex]::Escape($Model)))
}

function Test-Process-Alive {
  param([object]$PidValue)
  if (!$PidValue) {
    return $false
  }
  try {
    $ProcessId = [int]$PidValue
    $Process = Get-Process -Id $ProcessId -ErrorAction SilentlyContinue
    return ($null -ne $Process)
  } catch {
    return $false
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
    [string]$ErrorLog = '',
    [string]$ErrorMessage = '',
    [object]$PidValue = $null,
    [object]$ExitCode = $null,
    [object]$Completed = $null,
    [object]$Total = $null
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
  if ($null -eq $PidValue -and $Existing -and $Existing.pid) {
    $PidValue = $Existing.pid
  }
  if ($null -eq $ExitCode -and $Existing -and $null -ne $Existing.exit_code) {
    $ExitCode = $Existing.exit_code
  }
  if ($null -eq $Completed -and $Existing -and $null -ne $Existing.completed) {
    $Completed = $Existing.completed
  }
  if ($null -eq $Total -and $Existing -and $null -ne $Existing.total) {
    $Total = $Existing.total
  }
  $Elapsed = 0
  try {
    $Elapsed = [int]((Get-Date) - [datetime]$StartedAt).TotalSeconds
  } catch {}
  $Alive = Test-Process-Alive $PidValue
  $Job = @{
    ok = ($Status -ne 'failed' -and $Status -ne 'unknown');
    bootstrap_version = $MAOMIAI_BOOTSTRAP_RUNTIME_VERSION;
    provider = 'ollama_cli_pull_stable';
    profile = $ProfileName;
    model = $Model;
    status = $Status;
    progress = $Progress;
    message = $Message;
    last_log = $LastLog;
    error_log = $ErrorLog;
    installed = $Installed;
    pid = $PidValue;
    process_alive = $Alive;
    exit_code = $ExitCode;
    completed = $Completed;
    total = $Total;
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
  $WorkerScript = Join-Path $JobDir ('model-download-' + $ProfileName + '-stable.ps1')
  $StdoutFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.err.log')
  $WorkerOutFile = Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.out.log')
  $WorkerErrFile = Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.err.log')
  $OldFiles = @(
    $JobFile,
    (Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.out.log')),
    (Join-Path $LogDir ('ollama-pull-' + $ProfileName + '.err.log')),
    (Join-Path $LogDir ('ollama-http-pull-' + $ProfileName + '.out.log')),
    (Join-Path $LogDir ('ollama-http-pull-' + $ProfileName + '.err.log')),
    (Join-Path $LogDir ('ollama-http-worker-' + $ProfileName + '.out.log')),
    (Join-Path $LogDir ('ollama-http-worker-' + $ProfileName + '.err.log')),
    (Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.out.log')),
    (Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.err.log')),
    (Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.out.log')),
    (Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.err.log')),
    (Join-Path $JobDir ('model-download-' + $ProfileName + '.log')),
    (Join-Path $JobDir ('model-download-' + $ProfileName + '.err')),
    (Join-Path $JobDir ('model-download-' + $ProfileName + '.ps1')),
    (Join-Path $JobDir ('model-download-' + $ProfileName + '-http.ps1')),
    (Join-Path $JobDir ('model-download-' + $ProfileName + '-worker.ps1')),
    $WorkerScript
  )
  foreach ($File in $OldFiles) {
    if (Test-Path $File) {
      Remove-Item $File -Force -ErrorAction SilentlyContinue
    }
  }
  $Ollama = Find-Ollama
  if (!$Ollama) {
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'failed' `
      -Message 'Ollama executable was not found.' `
      -Progress 0 `
      -Installed $false `
      -ErrorMessage 'ollama_not_found' | Out-Null
    return @{
      ok = $false;
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
      status = 'failed';
      message = 'Ollama executable was not found.';
      job_file = $JobFile
    }
  }
  $ProfileEsc = $ProfileName.Replace("'", "''")
  $ModelEsc = $Model.Replace("'", "''")
  $OllamaEsc = $Ollama.Replace("'", "''")
  $JobFileEsc = $JobFile.Replace("'", "''")
  $StartedAt = (Get-Date).ToString('s')
  $Worker = @'
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$BootstrapVersion = '__BOOTSTRAP_VERSION__'
$Profile = '__PROFILE__'
$Model = '__MODEL__'
$Ollama = '__OLLAMA__'
$JobFile = '__JOB_FILE__'
$StdoutFile = '__STDOUT_FILE__'
$StderrFile = '__STDERR_FILE__'
$StartedAt = '__STARTED_AT__'

function Write-State {
  param(
    [string]$Status,
    [string]$Message,
    [int]$Progress = 0,
    [string]$LastLog = '',
    [string]$ErrorLog = '',
    [bool]$Installed = $false,
    [object]$Completed = $null,
    [object]$Total = $null,
    [object]$ExitCode = $null
  )
  try { $Started = [datetime]::Parse($StartedAt) } catch { $Started = Get-Date }
  $Elapsed = [int]((Get-Date) - $Started).TotalSeconds
  $Payload = [ordered]@{
    ok = ($Status -ne 'failed');
    bootstrap_version = $BootstrapVersion;
    provider = 'ollama_cli_pull_stable';
    profile = $Profile;
    model = $Model;
    status = $Status;
    message = $Message;
    progress = $Progress;
    completed = $Completed;
    total = $Total;
    installed = $Installed;
    pid = $PID;
    process_alive = $true;
    exit_code = $ExitCode;
    error = $(if ($Status -eq 'failed') { $Message } else { '' });
    started_at = $StartedAt;
    elapsed_seconds = $Elapsed;
    stdout_file = $StdoutFile;
    stderr_file = $StderrFile;
    stdout_tail = Tail $StdoutFile;
    stderr_tail = Tail $StderrFile;
    last_log = $LastLog;
    error_log = $ErrorLog;
    updated_at = (Get-Date).ToString('s')
  }
  $Payload | ConvertTo-Json -Depth 20 | Set-Content -Path $JobFile -Encoding UTF8
}

function Tail {
  param([string]$Path)
  if (!(Test-Path $Path)) { return '' }
  try { return (Get-Content $Path -Tail 40 -ErrorAction SilentlyContinue) -join "`n" } catch { return '' }
}

function Test-ModelInstalled {
  try {
    $List = & $Ollama list 2>$null | Out-String
    return ($List -like "*$Model*")
  } catch {
    return $false
  }
}

try {
  Write-State -Status 'starting' -Message 'Stable Ollama CLI worker started.' -Progress 1
  if (Test-ModelInstalled) {
    Write-State -Status 'completed' -Message 'Model already installed.' -Progress 100 -Installed $true -ExitCode 0
    exit 0
  }
  Write-State -Status 'running' -Message 'Running stable ollama pull command.' -Progress 5
  $Pull = Start-Process -FilePath $Ollama -ArgumentList @('pull', $Model) -NoNewWindow -PassThru -RedirectStandardOutput $StdoutFile -RedirectStandardError $StderrFile
  while (-not $Pull.HasExited) {
    $Log = Tail $StdoutFile
    $Err = Tail $StderrFile
    $Progress = 10
    if ($Log -match 'pulling') { $Progress = 20 }
    if ($Log -match 'verifying') { $Progress = 80 }
    if ($Log -match 'writing') { $Progress = 90 }
    Write-State -Status 'running' -Message 'Downloading model through stable Ollama CLI.' -Progress $Progress -LastLog $Log -ErrorLog $Err -Installed (Test-ModelInstalled)
    Start-Sleep -Seconds 2
    try { $Pull.Refresh() } catch {}
  }
  $Exit = $Pull.ExitCode
  if (Test-ModelInstalled) {
    Write-State -Status 'completed' -Message 'Model download completed and verified.' -Progress 100 -LastLog (Tail $StdoutFile) -ErrorLog (Tail $StderrFile) -Installed $true -ExitCode $Exit
    exit 0
  }
  if ($Exit -eq 0) {
    Write-State -Status 'completed' -Message 'Ollama pull completed. Model verification is pending.' -Progress 95 -LastLog (Tail $StdoutFile) -ErrorLog (Tail $StderrFile) -Installed $false -ExitCode $Exit
    exit 0
  }
  Write-State -Status 'failed' -Message ('Ollama pull failed. ExitCode=' + $Exit) -Progress 0 -LastLog (Tail $StdoutFile) -ErrorLog (Tail $StderrFile) -Installed $false -ExitCode $Exit
  exit $Exit
} catch {
  try { $_.Exception.ToString() | Set-Content -Path $StderrFile -Encoding UTF8 } catch {}
  Write-State -Status 'failed' -Message $_.Exception.Message -Progress 0 -LastLog (Tail $StdoutFile) -ErrorLog (Tail $StderrFile) -Installed $false -ExitCode 10
  exit 10
}
'@
  $Worker = $Worker.Replace('__BOOTSTRAP_VERSION__', $MAOMIAI_BOOTSTRAP_RUNTIME_VERSION)
  $Worker = $Worker.Replace('__PROFILE__', $ProfileEsc)
  $Worker = $Worker.Replace('__MODEL__', $ModelEsc)
  $Worker = $Worker.Replace('__OLLAMA__', $OllamaEsc)
  $Worker = $Worker.Replace('__JOB_FILE__', $JobFileEsc)
  $Worker = $Worker.Replace('__STDOUT_FILE__', $StdoutFile.Replace("'", "''"))
  $Worker = $Worker.Replace('__STDERR_FILE__', $StderrFile.Replace("'", "''"))
  $Worker = $Worker.Replace('__STARTED_AT__', $StartedAt)
  $Worker | Set-Content -Path $WorkerScript -Encoding UTF8
  Update-Model-Pull-Job `
    -ProfileName $ProfileName `
    -Status 'starting' `
    -Message 'Starting stable Ollama CLI download worker.' `
    -Progress 1 `
    -Installed $false | Out-Null
  try {
    # Windows PowerShell 5.1 can split -File paths containing spaces. Encode "& '<path>'" instead.
    $EncodedCommandText = "& '" + $WorkerScript.Replace("'", "''") + "'"
    $EncodedCommand = [Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes($EncodedCommandText))
    $Launcher = Start-Process -FilePath 'powershell' -ArgumentList @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-EncodedCommand', $EncodedCommand) -WindowStyle Hidden -PassThru -RedirectStandardOutput $WorkerOutFile -RedirectStandardError $WorkerErrFile
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'running' `
      -Message 'Stable Ollama CLI download worker started.' `
      -Progress 5 `
      -Installed $false `
      -PidValue $Launcher.Id | Out-Null
    return @{
      ok = $true;
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
      status = 'started';
      progress = 5;
      pid = $Launcher.Id;
      message = 'Stable Ollama CLI download worker started.';
      job_file = $JobFile;
      worker_script = $WorkerScript;
      stdout_file = $StdoutFile;
      stderr_file = $StderrFile;
      worker_stdout_file = $WorkerOutFile;
      worker_stderr_file = $WorkerErrFile
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
      provider = 'ollama_cli_pull_stable';
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
  $StdoutFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.err.log')
  $WorkerOutFile = Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.out.log')
  $WorkerErrFile = Join-Path $LogDir ('ollama-stable-worker-' + $ProfileName + '.err.log')
  $Status = 'not_started'
  $Progress = 0
  $ExistingMessage = ''
  $ExistingError = ''
  $ExistingPid = $null
  $ExistingExitCode = $null
  $ExistingCompleted = $null
  $ExistingTotal = $null
  if (Test-Path $JobFile) {
    try {
      $Existing = Get-Content $JobFile -Raw | ConvertFrom-Json
      $Status = $Existing.status
      $Progress = [int]$Existing.progress
      $ExistingMessage = $Existing.message
      $ExistingError = $Existing.error
      $ExistingPid = $Existing.pid
      $ExistingExitCode = $Existing.exit_code
      $ExistingCompleted = $Existing.completed
      $ExistingTotal = $Existing.total
    } catch {}
  }
  $Stdout = Get-Log-Tail $StdoutFile 6000
  $WorkerStdout = Get-Log-Tail $WorkerOutFile 3000
  $WorkerStderr = Get-Log-Tail $WorkerErrFile 3000
  $Stderr = ((Get-Log-Tail $StderrFile 6000) + "`n" + $WorkerStdout + "`n" + $WorkerStderr).Trim()
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
      -LastLog $Stdout `
      -ErrorLog $Stderr `
      -PidValue $ExistingPid `
      -ExitCode $ExistingExitCode `
      -Completed $ExistingCompleted `
      -Total $ExistingTotal | Out-Null
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
      $ExistingPid = $Existing.pid
      $ExistingExitCode = $Existing.exit_code
      $ExistingCompleted = $Existing.completed
      $ExistingTotal = $Existing.total
      if ($StartedAt) {
        $Elapsed = [int]((Get-Date) - [datetime]$StartedAt).TotalSeconds
      }
    } catch {}
  }
  $Alive = Test-Process-Alive $ExistingPid
  if (($Status -eq 'running' -or $Status -eq 'starting') -and (-not $Alive) -and (-not $Exists) -and $Elapsed -gt 10) {
    $Status = 'failed'
    $ExistingMessage = 'Stable Ollama CLI worker exited before model was installed. Check stderr_tail and stdout_tail.'
    $ExistingError = 'stable_ollama_pull_worker_exited'
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status 'failed' `
      -Message $ExistingMessage `
      -Progress $Progress `
      -Installed $false `
      -LastLog $Stdout `
      -ErrorLog $Stderr `
      -ErrorMessage $ExistingError `
      -PidValue $ExistingPid `
      -ExitCode $ExistingExitCode `
      -Completed $ExistingCompleted `
      -Total $ExistingTotal | Out-Null
  }
  return @{
    ok = $true;
    bootstrap_version = $MAOMIAI_BOOTSTRAP_RUNTIME_VERSION;
    provider = 'ollama_cli_pull_stable';
    profile = $ProfileName;
    model = $Model;
    status = $Status;
    progress = $Progress;
    message = $(if ($ExistingMessage) { $ExistingMessage } elseif ($Status -eq 'completed') { 'Model download completed.' } elseif ($Status -eq 'failed') { 'Model download failed.' } elseif ($Status -eq 'running') { 'Downloading model. Please keep the app open.' } else { 'No model download job is running.' });
    job_file = $JobFile;
    stdout_file = $StdoutFile;
    stderr_file = $StderrFile;
    worker_stdout_file = $WorkerOutFile;
    worker_stderr_file = $WorkerErrFile;
    stdout_tail = $Stdout;
    stderr_tail = $Stderr;
    last_log = $Combined;
    error_log = $Stderr;
    elapsed_seconds = $Elapsed;
    pid = $ExistingPid;
    process_alive = $Alive;
    exit_code = $ExistingExitCode;
    completed = $ExistingCompleted;
    total = $ExistingTotal;
    error = $ExistingError;
    installed = $Exists;
    list = $List
  }
}

function Pull-Model {
  param([string]$ProfileName)
  $Model = Get-Model-For-Profile $ProfileName
  $Ollama = Find-Ollama
  if (!$Ollama) {
    return @{
      ok = $false;
      stage = 'pull_cli';
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
      message = 'Ollama executable was not found.'
    }
  }
  $ListBefore = Get-Ollama-List
  if ($ListBefore.raw -and ($ListBefore.raw -match [regex]::Escape($Model))) {
    return @{
      ok = $true;
      stage = 'already_exists';
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
      message = 'Selected capability is already installed.';
      list = $ListBefore
    }
  }
  $LogDir = Join-Path $Root 'logs\windows'
  Ensure-Dir $LogDir
  $StdoutFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.out.log')
  $StderrFile = Join-Path $LogDir ('ollama-stable-pull-' + $ProfileName + '.err.log')
  if (Test-Path $StdoutFile) {
    Remove-Item $StdoutFile -Force -ErrorAction SilentlyContinue
  }
  if (Test-Path $StderrFile) {
    Remove-Item $StderrFile -Force -ErrorAction SilentlyContinue
  }
  Update-Model-Pull-Job `
    -ProfileName $ProfileName `
    -Status 'running' `
    -Message 'Running stable ollama pull command.' `
    -Progress 5 `
    -Installed $false | Out-Null
  try {
    $Process = Start-Process -FilePath $Ollama -ArgumentList @('pull', $Model) -WindowStyle Hidden -PassThru -Wait -RedirectStandardOutput $StdoutFile -RedirectStandardError $StderrFile
    $ListAfter = Get-Ollama-List
    $Exists = $false
    if ($ListAfter.raw -and ($ListAfter.raw -match [regex]::Escape($Model))) {
      $Exists = $true
    }
    $Tail = Get-Log-Tail $StdoutFile 6000
    $ErrTail = Get-Log-Tail $StderrFile 3000
    Update-Model-Pull-Job `
      -ProfileName $ProfileName `
      -Status $(if ($Exists) { 'completed' } else { 'failed' }) `
      -Message $(if ($Exists) { 'Model download completed and verified.' } else { 'Ollama pull ended but model was not confirmed.' }) `
      -Progress $(if ($Exists) { 100 } else { 0 }) `
      -Installed $Exists `
      -LastLog $Tail `
      -ErrorLog $ErrTail `
      -ExitCode $Process.ExitCode `
      -ErrorMessage $(if ($Exists) { '' } else { 'model_not_confirmed_after_cli_pull' }) | Out-Null
    return @{
      ok = $Exists;
      stage = 'pull_cli';
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
      exit_code = $Process.ExitCode;
      progress = $(if ($Exists) { 100 } else { 0 });
      message = $(if ($Exists) { 'Model capability is downloaded and ready.' } else { 'Ollama pull ended but model was not confirmed.' });
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
      -ErrorLog (Get-Log-Tail $StderrFile 3000) `
      -ErrorMessage $_.Exception.Message | Out-Null
    return @{
      ok = $false;
      stage = 'pull_cli';
      profile = $ProfileName;
      model = $Model;
      provider = 'ollama_cli_pull_stable';
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
