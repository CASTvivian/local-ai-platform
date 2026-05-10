# P3.14-D7 Windows Package Content and Full Delivery

## Status

Created full Windows delivery package.

## Why only three files appeared before

GitHub Actions artifact normally contains only build outputs:

- setup.exe
- msi
- raw exe

Runtime resources are expected to be inside the installer bundle after installation.
For debugging and customer delivery, a full delivery folder is now created.

## Source Package

```text
core-platform/releases/windows-d7-verified-complete
```

## Full Delivery Package

```text
core-platform/releases/windows-d7-full-delivery
core-platform/releases/windows-d7-full-delivery.tar.gz
```

## Included

- Windows installers
- runtime scripts
- backend services
- manual backend start/status scripts
- README

## Next

Use setup.exe for normal install.
Use runtime/manual_start_backend.ps1 only for troubleshooting backend startup.
