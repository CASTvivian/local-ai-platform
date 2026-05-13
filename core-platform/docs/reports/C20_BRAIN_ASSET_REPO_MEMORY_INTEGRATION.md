# C20 Brain Asset Repo Memory Integration

## Status

Implemented.

## Outputs

- `core-platform/data/brain_assets/manifests/brain_asset_index.json`
- `core-platform/data/brain_assets/manifests/brain_asset_category_index.json`
- `core-platform/data/brain_assets/reports/brain_asset_summary_catalog.md`
- `core-platform/data/repo_memory/brain_asset_seed.json`

## Service Integration

- `GET /brain/assets`
- `POST /brain/seed`
- `POST /brain/search`

`/brain/search` seeds the repo memory store on first use when no brain asset knowledge entries exist.

## Desktop Integration

The Windows desktop chat router now exposes a `项目知识查询` action. It queries `repo_memory_service` on port `18125` and shows matching brain asset entries in the conversation surface.

## Coverage

- GitHub starred repos represented in the brain index: `147`
- Brain asset seed entries: `147`
- Search categories are derived from asset tags and buckets.
