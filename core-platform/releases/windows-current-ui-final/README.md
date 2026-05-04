# Windows Current UI Final Package

## Status
Accepted.

## Source Commit
`c3ecabf`

## Verification
GitHub Actions build passed.
Workflow log confirmed:
```text
D7-C1 markers verified in dist.
```

This Windows package uses the corrected MAOMIAI Desktop UI, not the old Windows test page.

## Included
- `Local AI Platform_0.1.0_x64_en-US.msi`
- `Local AI Platform_0.1.0_x64-setup.exe`
- `desktop_lib.exe`
- `BUILD_INFO.json`

## Notes
This package includes D7-C1 navigation cleanup:
- Hides low-level internal entries from main navigation
- Defaults to chat/new session
- Includes auto-start-services.js
