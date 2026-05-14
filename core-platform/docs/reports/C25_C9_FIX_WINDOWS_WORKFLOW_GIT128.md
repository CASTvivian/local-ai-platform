# C25-C9-FIX Windows Workflow Git 128

## Problem
Windows build produced an artifact but the workflow ended with:
```text
git.exe failed with exit code 128
Process completed with exit code 1
```

A produced artifact from a failed workflow is not acceptable as final package evidence.

## Fix
* Disable recursive submodule checkout
* Disable LFS
* Use shallow clean checkout
* Add Git checkout diagnostics
* Add artifact/resource marker verification step

## Goal
The next Windows build must end with conclusion=success, not only produce artifacts.
