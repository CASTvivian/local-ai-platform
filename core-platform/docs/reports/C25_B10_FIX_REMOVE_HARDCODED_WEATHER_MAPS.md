# C25-B10 Fix: Remove Hardcoded Weather Maps

## Status
Implemented.

## What Changed
- Added clean weather runtime without hardcoded city maps.
- Added Open-Meteo geocoding for all locations.
- Added Open-Meteo forecast query.
- Added MCP `weather.query` runtime integration.
- Enabled `weather.query` capability.
- Renderer now displays provider `weather_code` instead of hardcoded weather text.
- Weather execution writes audit records.

## Removed By Design
- No `CN_LOCATION_MAP`.
- No `WEATHER_CODE` table.
- No city-specific branches such as Guangzhou, Shenzhen, Beijing or Shanghai.

## Runtime Direction
Weather handling now follows:

```text
user location text -> generic extraction -> geocoding -> provider weather API -> evidence answer
```
