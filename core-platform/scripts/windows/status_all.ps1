$Ports = @(18080,18100,18093,18104,18110,18111,18112,18120,18121,18123,18124,18125,18126,18127)

foreach ($p in $Ports) {
  $c = Get-NetTCPConnection -LocalPort $p -ErrorAction SilentlyContinue
  if ($c) {
    Write-Host "OK  $p"
  } else {
    Write-Host "BAD $p"
  }
}
