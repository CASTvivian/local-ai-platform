$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Root = $Here
Write-Host "===== MAOMIAI manual backend start ====="
Write-Host "Root: $Root"
$Start = Join-Path $Root "scripts\windows\start_all.ps1"
if (!(Test-Path $Start)) {
  Write-Host "start_all.ps1 not found: $Start"
  exit 1
}
powershell -ExecutionPolicy Bypass -File $Start -Root $Root
