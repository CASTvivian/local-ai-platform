# C25-C12 Build Fix: MSI-only Windows Bundle

## Problem

Windows build reached Tauri bundle stage, built the application and MSI, then failed while downloading NSIS:

```text
Downloading nsis-3.11.zip
failed to bundle project `http status: 504`
```

This is an external dependency download failure, not an app code failure.

## Fix

Temporarily force Windows CI to build MSI only:

```text
--bundles msi
```

## Result Expected

- Avoid NSIS download.
- Produce MSI installer.
- Keep `desktop_lib.exe` artifact.
- Use MSI for Windows acceptance test.
