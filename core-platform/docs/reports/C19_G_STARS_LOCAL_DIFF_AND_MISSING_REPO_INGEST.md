# C19-G Stars Local Diff and Missing Repo Ingest

## Status

Completed.

## Numbers

- Local git roots detected: 14
- Starred repos already local: 4
- Starred repos missing locally: 143
- Missing repos cloned or already present: 140
- Missing repos failed/no clone: 3
- Missing repo summaries generated: 140

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

- **coreyhaines31/marketingskills**: failed: Command '['git', 'clone', '--depth', '1', 'https://github.com/coreyhaines31/marketingskills.git', 'c
- **hyperspaceai/agi**: failed: Command '['git', 'clone', '--depth', '1', 'https://github.com/hyperspaceai/agi.git', 'core-platform/
- **perkfly/ex-skill**: failed: Command '['git', 'clone', '--depth', '1', 'https://github.com/perkfly/ex-skill.git', 'core-platform/