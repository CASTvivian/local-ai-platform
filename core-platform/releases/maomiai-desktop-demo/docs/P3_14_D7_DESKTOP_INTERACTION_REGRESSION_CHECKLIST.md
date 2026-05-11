# P3.14-D7 Desktop Interaction Regression Checklist
## 目标
对 MAOMIAI Desktop 做完整交互回归，先固定问题，再逐步清理 runtime override。

## 当前临时层
当前桌面端包含以下稳定覆盖层：
- `page-helpers.js`
- `navigation-fix.js`
- `composer-fix.js`
- `desktop-runtime-stable.js`
- `desktop-chat-stable.js`
- `chat-session-manager.js`

D7 的目标不是马上删除它们，而是：
1. 先确认当前可演示功能稳定
2. 再逐页把逻辑回归到正式模块
3. 最后移除临时覆盖层

## D7-A 验收目标
### A. App 启动
- [ ] 后端服务 13 个全部健康
- [ ] App 可启动
- [ ] 页面无红框错误
- [ ] 右侧服务健康面板可刷新

### B. 左侧页面
逐个点击并确认不报错：
- [ ] 新建会话
- [ ] 启动中心
- [ ] 大脑状态
- [ ] 技能商店
- [ ] 文档处理
- [ ] 工作流
- [ ] 产物中心
- [ ] 代码审查
- [ ] 仓库记忆
- [ ] 设计系统
- [ ] 模型设置
- [ ] 设置

### C. 右侧 Inspector
逐个点击并确认有响应：
- [ ] 服务
- [ ] 追踪
- [ ] 策略
- [ ] 产物中心
- [ ] 预览
- [ ] 评测

### D. 本地模型对话
- [ ] 输入：你好，请用一句中文介绍你自己
- [ ] 模型返回自然语言中文
- [ ] 不出现"本地模型暂未接通"
- [ ] 不只显示 route/runtime JSON

### E. 会话上下文
- [ ] 新建会话 1
- [ ] 输入：你好，我叫小明
- [ ] 输入：我叫什么？
- [ ] 预期：回答小明
- [ ] 新建会话 2
- [ ] 输入：我叫什么？
- [ ] 预期：不知道小明或说"你还没告诉我"
- [ ] 切回会话 1
- [ ] 会话 1 消息还在
- [ ] 重启 App 后会话仍在

### F. 页面专项交互
#### 代码审查
- [ ] 输入 `rm -rf /`
- [ ] 点击执行审查
- [ ] 返回高危/拒绝/风险项

#### 文档处理
- [ ] 输入一段文本
- [ ] 点击摄取
- [ ] 返回 doc_id / chunks

#### 产物中心
- [ ] 能看到 artifact 列表
- [ ] 点击刷新有响应

#### 仓库记忆
- [ ] 能看到 repo 列表或空状态
- [ ] 不再报旧 repo-memory.js 错误

#### 代码审查
- [ ] 能看到 repo 列表或空状态
- [ ] 不再报旧 repo-memory.js 错误

## D7-B 入口
如果 D7-A 中会话相关失败，则进入：
`P3.14-D7-B Session Manager Regression Fix`

专门修复你刚才说的新建会话、上下文隔离、聊天不保留这些问题。

## D7-C 入口
如果页面相关失败，则逐页修复：
- D7-C1 Skill Store
- D7-C2 Workflows
- D7-C3 Artifacts
- D7-C4 Repo Memory
- D7-C5 Code Review
- D7-C6 Design System
- D7-C7 Models

## D7-D 入口
所有页面正式模块通过后，移除临时覆盖层。
