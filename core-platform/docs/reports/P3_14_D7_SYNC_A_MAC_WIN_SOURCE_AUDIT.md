# P3.14-D7-SYNC-A Mac / Windows Source Audit
## Purpose
Audit whether macOS and Windows builds are using the same desktop source, scripts, and services.
## Expected Target
The unified source should be:
```text
core-platform/apps/desktop
core-platform/scripts
core-platform/services
```

Both macOS and Windows builds should use the same desktop source.

## Next Step
After audit output is reviewed, perform D7-SYNC-B to normalize paths.
