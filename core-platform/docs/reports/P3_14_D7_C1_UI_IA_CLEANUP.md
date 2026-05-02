# P3.14-D7-C1 Desktop Information Architecture Cleanup

## Status

**IMPLEMENTED**

## Product Decisions

1. ✅ Hide Launch Center from main navigation
2. ✅ Hide Brain Status from main navigation (renamed to "系统状态")
3. ✅ Hide Skill Store from main navigation (renamed to "能力管理")
4. ✅ Hide Documents from main navigation (renamed to "文档能力")
5. ✅ Default app entry is Chat / New Session
6. ✅ Preserved old pages for internal/diagnostic use

## Implemented Changes

### Navigation Cleanup
- Added `hidden-internal` CSS class to low-level nav entries:
  - `nav-launch` (启动中心)
  - `nav-brain` (大脑状态)
  - `nav-skills` (技能商店)
  - `nav-documents` (文档处理)
- Updated labels to be more product-friendly:
  - 大脑状态 → 系统状态
  - 技能商店 → 能力管理
  - 文档处理 → 文档能力

### Default Route
- Forced default view to "chat" on app open
- Injected localStorage cleanup to prevent old views from persisting
- Users now land on chat page instead of internal launch center

### Auto-Start Services
- Created `auto-start-services.js` with best-effort service startup
- Supports multiple command name variations for compatibility
- Gracefully handles Tauri unavailability
- Refreshes health panel after auto-start attempt

### CSS Updates
- Added styles for `hidden-internal` class
- Added status indicator styles for auto-start feedback

## Preserved Entries

The following entries remain visible in main navigation:
- 新建会话
- 工作流
- 产物中心
- 代码审查
- 仓库记忆
- 设计系统
- 模型设置
- 设置

## Testing Checklist

- [ ] Open app defaults to chat/new session
- [ ] Hidden nav entries (launch/brain/skills/documents) not visible
- [ ] Right-side service health panel still accessible
- [ ] Services auto-start on app open (if Tauri commands available)

## Next

D7-C2 should verify auto-start works inside packaged app and complete remaining product-level navigation cleanup.
