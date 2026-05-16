# C26-C Desktop Skill Store

## Goal
Show generated default skills in the desktop skill store with search, tag filtering, and skill cards.

## Implemented

### Router (windows-demo-stable-router.js)
- `maomiaiLoadDefaultSkills()` — loads `data/skill_brain/default_skills.json` via fetch
- `maomiaiSkillTags(skills)` — computes tag frequency distribution for filter buttons
- `maomiaiRenderSkillCard(skill)` — renders a skill card with title, description, source repo, stars, tags, language
- `renderDefaultSkillStorePage(filterTag, searchText)` — full page renderer with:
  - Search input (real-time filtering by title/id/description/tags/source/language)
  - Tag filter buttons (top 14 tags with counts, "全部" button)
  - Skill count stat display (filtered / total)
  - Grid of skill cards (max 120 displayed)
  - Error state when default_skills.json unavailable
- Route: `skills` / `skill-store` → calls `renderDefaultSkillStorePage()`
- Nav inference: `技能` / `skill` → `skills` view

### HTML (index.html)
- Nav button `🧩 技能商店` changed from `hidden-internal` to visible
- `renderPage("skills")` now calls `renderDefaultSkillStorePage()` when available

### CSS (main.css)
- `.skill-brain-page` — page container
- `.skill-brain-hero` — hero section with title, description, stat counter
- `.skill-brain-toolbar` — search + filter button bar
- `.skill-brain-search` — search input
- `.skill-brain-filter` — tag filter pills with `.active` state
- `.skill-brain-grid` — responsive card grid (auto-fill, minmax 290px)
- `.skill-brain-card` — card with head/title/source/stars, description, tags
- `.skill-brain-tag` — indigo tag pills
- `.skill-brain-lang` — green language pills
- `.skill-brain-warning` — error state
- `.skill-brain-stars` — star count badge

### Tauri Resources (tauri.conf.json)
- Added `../../../data/skill_brain` to bundle resources

## Validation
- ✅ JS syntax: OK
- ✅ Hardcode guard: OK
- ✅ skill_count: 147 (≥ 100)
- ✅ router_has_loader: true
- ✅ router_has_render_page: true
- ✅ router_has_route: true
- ✅ css_has_skill_brain: true
- ✅ tauri_resource_includes_skill_brain: true
- ✅ html_nav_visible: true
- ✅ html_renderPage_skills: true

## Data Flow
```
brain_assets / github_stars / repo_memory
→ generate_default_skills.py
→ data/skill_brain/default_skills.json
→ maomiaiLoadDefaultSkills() fetch
→ renderDefaultSkillStorePage() with search + tag filters
→ Desktop Skill Store UI
```

## Next
- C26-E: 技能自动更新/学习
- C26-F: 技能启用/禁用/评分
