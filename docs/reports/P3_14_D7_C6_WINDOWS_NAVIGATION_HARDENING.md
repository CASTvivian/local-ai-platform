# P3.14-D7-C6 Windows Navigation Hardening
## Status
Implemented.
## Problem
On Windows, sidebar items could show hover state but clicking them did not reliably route to pages.
## Fix
Added `windows-demo-stable-router.js`, loaded as the final script.
It provides:
- global event delegation
- pointerdown and click capture
- automatic data-view inference from Chinese labels
- stable fallback pages
- guaranteed local model page routing
- no silent click failures
## Demo Impact
The following sidebar items should now work in Windows demo builds:
- 新对话
- 文件与结果
- 代码检查
- 本地模型
- 设置
