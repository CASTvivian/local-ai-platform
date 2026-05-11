# P3.14-D7-C9 Embedded Windows Bootstrap Runtime

## Status
Implemented.

## Problem
Windows model download failed with:
```
未找到打包内的 bootstrap_runtime.ps1
```

The Tauri command reached Rust, but the runtime script was not found in the installed package.

## Fix
`bootstrap_runtime.ps1` is now embedded into the Rust binary with `include_str!`.

At runtime, the app writes it into:
```
<app_dir>/maomiai-runtime/scripts/windows/bootstrap_runtime.ps1
```

Then Rust executes that released script directly.

## Result
Model download no longer depends on Tauri resource path resolution.
