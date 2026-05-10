$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Status = Join-Path $Here "scripts\windows\status_all.ps1"
if (Test-Path $Status) {
  powershell -ExecutionPolicy Bypass -File $Status
}
Write-Host "`n===== API health ====="
try {
  Invoke-RestMethod http://127.0.0.1:18100/health -TimeoutSec 5 | ConvertTo-Json -Depth 8
} catch {
  Write-Host "18100 failed: $($_.Exception.Message)"
}
try {
  Invoke-RestMethod http://127.0.0.1:18080/health -TimeoutSec 5 | ConvertTo-Json -Depth 8
} catch {
  Write-Host "18080 failed: $($_.Exception.Message)"
}
