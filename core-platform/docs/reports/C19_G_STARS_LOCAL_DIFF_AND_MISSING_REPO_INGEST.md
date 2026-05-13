# C19-G Stars Local Diff and Missing Repo Ingest

## Status

Completed.

## Numbers

- Local git roots detected: 211
- Starred repos already local: 144
- Starred repos missing locally: 3
- Missing repos cloned or already present: 3
- Missing repos failed/no clone: 0
- Missing repo summaries generated: 3

## Output Files

- `core-platform/data/brain_assets/manifests/local_repo_roots_detected.json`
- `core-platform/data/brain_assets/manifests/stars_local_existing.json`
- `core-platform/data/brain_assets/manifests/stars_local_missing.json`
- `core-platform/data/brain_assets/manifests/stars_local_diff.md`
- `core-platform/data/brain_assets/manifests/stars_missing_clone_results.json`
- `core-platform/data/brain_assets/manifests/stars_missing_summary_index.json`
- `core-platform/data/brain_assets/reports/missing_repo_summaries/`

## Note

Third-party repositories are cloned locally under `core-platform/data/brain_assets/repos/github_stars_missing/` for analysis, but should not be committed wholesale into the main repository.

Only manifests, summaries, and reports should be committed.

## Failed / Skipped
