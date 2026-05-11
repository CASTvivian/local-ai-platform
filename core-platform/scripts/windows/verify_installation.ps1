# Windows Installation Verification Script
# Run this after installing the MSI/EXE to verify resources are bundled

Write-Host "===== Local AI Platform Installation Verification =====" -ForegroundColor Cyan
Write-Host "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Write-Host ""

# 1. Find installation directory
Write-Host "Step 1: Finding installation directory..." -ForegroundColor Yellow
$dirs = @(
  "$env:LOCALAPPDATA\Programs\Local AI Platform",
  "$env:ProgramFiles\Local AI Platform",
  "$env:ProgramFiles(x86)\Local AI Platform"
)

$installDir = $null
foreach ($d in $dirs) {
  if (Test-Path $d) {
    Write-Host "  FOUND: $d" -ForegroundColor Green
    $installDir = $d
    break
  }
}

if (-not $installDir) {
  Write-Host "  ERROR: Installation directory not found!" -ForegroundColor Red
  Write-Host "  Checked: $dirs"
  exit 1
}

Write-Host ""

# 2. List installation directory structure
Write-Host "Step 2: Listing installation directory..." -ForegroundColor Yellow
Get-ChildItem $installDir -Recurse -ErrorAction SilentlyContinue | 
  Select-Object FullName, Length | 
  Format-Table -AutoSize

Write-Host ""

# 3. Check for resources directory
Write-Host "Step 3: Checking for resources directory..." -ForegroundColor Yellow
$resourcesDirs = Get-ChildItem $installDir -Recurse -Directory -Filter "resources" -ErrorAction SilentlyContinue

if ($resourcesDirs) {
  Write-Host "  FOUND $($resourcesDirs.Count) resources directories:" -ForegroundColor Green
  foreach ($r in $resourcesDirs) {
    Write-Host "    - $($r.FullName)"
  }
} else {
  Write-Host "  WARNING: No resources directory found!" -ForegroundColor Red
}

Write-Host ""

# 4. Check for critical Windows scripts
Write-Host "Step 4: Checking for Windows scripts..." -ForegroundColor Yellow
$scriptsToCheck = @(
  "start_all.ps1",
  "stop_all.ps1",
  "status_all.ps1",
  "ensure_runtime.ps1",
  "bootstrap_runtime.ps1"
)

foreach ($script in $scriptsToCheck) {
  $found = Get-ChildItem $installDir -Recurse -Filter $script -ErrorAction SilentlyContinue
  if ($found) {
    Write-Host "  ✓ Found: $script" -ForegroundColor Green
    foreach ($f in $found) {
      Write-Host "    - $($f.FullName) ($([math]::Round($f.Length / 1KB, 2)) KB)"
    }
  } else {
    Write-Host "  ✗ Missing: $script" -ForegroundColor Red
  }
}

Write-Host ""

# 5. Check for critical services
Write-Host "Step 5: Checking for core services..." -ForegroundColor Yellow
$servicesToCheck = @(
  "model_gateway\main.py",
  "model_bootstrap_service\main.py"
)

foreach ($service in $servicesToCheck) {
  $found = Get-ChildItem $installDir -Recurse -Filter $service -ErrorAction SilentlyContinue
  if ($found) {
    Write-Host "  ✓ Found: $service" -ForegroundColor Green
    foreach ($f in $found) {
      Write-Host "    - $($f.FullName) ($([math]::Round($f.Length / 1KB, 2)) KB)"
    }
  } else {
    Write-Host "  ✗ Missing: $service" -ForegroundColor Red
  }
}

Write-Host ""

# 6. Check for enterprise services
Write-Host "Step 6: Checking for enterprise services..." -ForegroundColor Yellow
$enterpriseServices = @(
  "skill_store_service\main.py",
  "artifact_registry_service\main.py",
  "code_review_gate_service\main.py",
  "repo_memory_service\main.py",
  "workflow_store_service\main.py",
  "design_system_service\main.py"
)

foreach ($service in $enterpriseServices) {
  $found = Get-ChildItem $installDir -Recurse -Filter $service -ErrorAction SilentlyContinue
  if ($found) {
    Write-Host "  ✓ Found: $service" -ForegroundColor Green
  } else {
    Write-Host "  ✗ Missing: $service" -ForegroundColor Red
  }
}

Write-Host ""

# 7. Summary
Write-Host "===== Verification Summary =====" -ForegroundColor Cyan
Write-Host "Installation Directory: $installDir"
Write-Host ""

$totalResources = @(Get-ChildItem $installDir -Recurse -Directory -Filter "resources" -ErrorAction SilentlyContinue).Count
$totalScripts = @(Get-ChildItem $installDir -Recurse -Filter "*.ps1" -ErrorAction SilentlyContinue).Count
$totalServices = @(Get-ChildItem $installDir -Recurse -Filter "main.py" -ErrorAction SilentlyContinue).Count

Write-Host "Resources directories: $totalResources"
Write-Host "PowerShell scripts: $totalScripts"
Write-Host "Service main.py files: $totalServices"
Write-Host ""

if ($totalResources -gt 0 -and $totalScripts -gt 0 -and $totalServices -gt 0) {
  Write-Host "✓ Installation appears complete with bundled resources" -ForegroundColor Green
} else {
  Write-Host "✗ Installation incomplete - resources may not be bundled" -ForegroundColor Red
}
