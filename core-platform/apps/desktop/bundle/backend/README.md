# Core Platform

这是 Local AI Platform 的主工程目录。

## 模块概览

```
core-platform/
├── services/         # 微服务层
├── plugins/          # 插件能力层
├── apps/desktop/     # 桌面客户端（Tauri）
├── docs/             # 实验文档 / 提炼文档
├── manifests/        # 能力注册与配置
├── scripts/          # 服务启停与状态检查
└── packages/         # 共享包与 SDK
```

## 已完成能力

### Agent 团队系统
- **异步任务执行**: Planner、Researcher、Coder、Reviewer、Operator、Synthesizer 六种角色
- **Phase 日志**: 实时任务执行状态追踪
- **工具桥接**: HTTP 代理模式支持外部服务调用

### 研究服务
- **深度研究**: 基于多模型的智能研究
- **网关直连**: 直接连接模型网关，减少调用链路
- **知识提取**: 自动化知识提取与总结

### TTS 服务
- **VoxCPM 集成**: 真实 VoxCPM TTS 服务
- **双后端机制**: VoxCPM + macOS say 自动降级
- **音频路由**: 自动选择最优 TTS 后端

### 视频生成
- **工作流编排**: research → tts → video 完整流程
- **异步状态查询**: video_run 实时状态跟踪
- **多种模型支持**: LLaVA、Qwen-VL 等视觉模型

### 超帧服务
- **视频处理**: 视频超分辨率与帧插值
- **批量处理**: 支持多视频并发处理

### 浏览器代理
- **自动化操作**: 基于指令的网页交互
- **内容提取**: 智能网页信息抓取
- **表单填写**: 自动化表单提交

### 模型引导服务
- **一键初始化**: 自动下载配置 Ollama 模型
- **状态持久化**: JSON 格式的下载状态管理
- **智能跳过**: 已存在模型自动跳过下载

## 常用命令

### 服务管理

```bash
# 启动所有服务
bash scripts/start_all.sh

# 检查所有服务状态
bash scripts/status_all.sh

# 停止所有服务
bash scripts/stop_all.sh
```

### 桌面应用

```bash
# 开发模式
cd apps/desktop
npm run tauri dev

# 构建生产版本
npm run tauri build

# 构建并打包
npm run tauri build
```

### 独立服务启动

```bash
# 启动模型网关
uvicorn services.model_gateway.main:app --host 0.0.0.0 --port 18080

# 启动编排器
uvicorn services.orchestrator.main:app --host 0.0.0.0 --port 18081

# 启动 Agent 团队服务
uvicorn services.agent_team_service.main:app --host 0.0.0.0 --port 18094

# 启动模型引导服务
uvicorn services.model_bootstrap_service.main:app --host 0.0.0.0 --port 18100
```

## 服务端口

| 服务 | 端口 | 路径 |
|------|------|------|
| model_gateway | 18080 | `services/model_gateway/main.py` |
| orchestrator | 18081 | `services/orchestrator/main.py` |
| agent_team_service | 18094 | `services/agent_team_service/main.py` |
| real_impl_service | 18095 | `services/real_impl_service/main.py` |
| research_real_service | 18098 | `services/research_real_service/main.py` |
| hyperframes_service | 18099 | `services/hyperframes_service/main.py` |
| model_bootstrap_service | 18100 | `services/model_bootstrap_service/main.py` |

## 插件系统

插件位于 `plugins/` 目录，每个插件实现特定的 AI 能力：

### 插件列表
- `research_real_plugin`: 研究服务真实实现
- `tts_voxcpm_plugin`: VoxCPM TTS 集成
- `video_impl_plugin`: 视频生成实现
- `browser_use_plugin`: 浏览器自动化
- `hyperframes_plugin`: 超帧服务
- `finance_*_plugin`: 金融相关插件

### 插件开发

插件开发遵循以下模式：

```python
# 插件基类
class MyPlugin(PluginBase):
    async def execute(self, context: dict) -> dict:
        # 实现插件逻辑
        result = await self.process(context)
        return result
```

## 数据存储

### 目录结构
```
data/
├── research_cache/      # 研究缓存
├── router/              # 路由器状态
├── model_bootstrap/     # 模型引导状态
└── ...                  # 其他数据目录
```

### 缓存策略
- 研究结果缓存: 7 天
- TTS 音频缓存: 30 天
- 视频缓存: 30 天

## 开发指南

### 环境要求
- Python 3.11+
- Node.js 24+
- Rust 1.70+

### 代码结构
```
core-platform/
├── services/            # FastAPI 微服务
│   ├── model_gateway/
│   ├── orchestrator/
│   └── ...
├── plugins/             # 能力插件
│   ├── research_real_plugin/
│   └── ...
├── apps/desktop/        # Tauri 桌面应用
│   ├── src/             # React 源码
│   ├── src-tauri/       # Rust 后端
│   └── package.json
└── packages/            # 共享包
```

### API 文档

启动服务后访问:
- 模型网关: http://localhost:18080/docs
- 编排器: http://localhost:18081/docs
- Agent 团队: http://localhost:18094/docs

## 测试

### 单元测试
```bash
# Python 测试
pytest services/

# 前端测试
cd apps/desktop
npm test
```

### 集成测试
```bash
# 服务健康检查
bash scripts/status_all.sh

# 端到端测试
pytest tests/integration/
```

## 故障排查

### 常见问题

**服务启动失败**
- 检查端口是否被占用: `lsof -i :18080`
- 查看服务日志: `tail -f logs/*.log`

**模型下载失败**
- 检查 Ollama 是否运行: `ollama list`
- 重新启动模型引导服务: `bash scripts/stop_all.sh && bash scripts/start_all.sh`

**TTS 无声音**
- 检查音频设备: `ls /dev/audio*`
- 查看错误日志: `tail -f logs/tts.log`

## 性能优化

### 并发控制
- 服务默认并发数: 10
- 可通过环境变量调整: `WORKER_CONCURRENCY=20`

### 缓存优化
- 启用 Redis 缓存（可选）
- 调整缓存 TTL: `CACHE_TTL=3600`

## 部署

### Docker 部署
```bash
# 构建镜像
docker-compose build

# 启动服务
docker-compose up -d
```

### 生产环境
- 使用反向代理 (Nginx)
- 配置 HTTPS
- 设置日志轮转
- 配置监控告警

## 贡献

请遵循以下贡献流程:
1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 许可证

与主仓库保持一致
