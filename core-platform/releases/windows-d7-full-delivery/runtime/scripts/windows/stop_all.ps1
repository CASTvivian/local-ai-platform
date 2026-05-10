$Ports = @(18080,18100,18093,18104,18110,18111,18112,18120,18121,18123,18124,18125,18126,18127)

foreach ($p in $Ports) {
  $conns = Get-NetTCPConnection -LocalPort $p -ErrorAction SilentlyContinue
  foreach ($c in $conns) {
    try {
      $proc = Get-Process -Id $c.OwningProcess -ErrorAction SilentlyContinue
      if ($proc) {
        Write-Host "Stopping port $p pid $($proc.Id) $($proc.ProcessName)"
        Stop-Process -Id $proc.Id -Force
      }
    } catch {}
  }
}
