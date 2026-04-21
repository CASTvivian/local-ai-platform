# Local AI Platform

本仓库用于维护本地 AI 平台的主工程、自动化脚本、构建流程与交付产物说明。

## 仓库结构

```text
.
├── .github/workflows/        # GitHub Actions 工作流（含 Windows 打包）
├── core-platform/            # 本地 AI 平台主工程
├── generated/                # 本地产物目录（音频 / 视频 / 图片等）
├── scripts/                  # 仓库级辅助脚本
└── README.md                 # 当前说明文件
```

## 主要功能

### 核心能力
- **多 Agent 系统**: Planner、Researcher、Coder、Reviewer、Operator、Synthesizer 六种角色协作
- **研究服务**: 深度研究与知识提取
- **TTS 服务**: 语音合成（VoxCPM + macOS say 双后端）
- **视频生成**: 文本到视频生成
- **超帧服务**: 视频处理与增强
- **浏览器代理**: 自动化网页操作
- **模型引导服务**: Ollama 模型一键初始化

### 技术栈
- **后端**: FastAPI (Python)
- **前端**: React + Tauri
- **数据库**: SQLite + JSON 文件存储
- **模型**: Ollama + 自研模型集成
- **部署**: Docker + GitHub Actions

## 快速开始

### 环境要求
- Python 3.11+
- Node.js 24+
- Rust (用于 Tauri 构建)
- Ollama (可选，用于本地模型运行)

### 安装依赖

```bash
# 克隆仓库
git clone https://github.com/CASTvivian/local-ai-platform.git
cd local-ai-platform

# 安装 Python 依赖
cd core-platform
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或 .venv\Scripts\activate  # Windows
pip install -r requirements.txt

# 安装前端依赖
cd apps/desktop
npm install
```

### 启动服务

```bash
# 启动所有服务
cd core-platform
bash scripts/start_all.sh

# 检查服务状态
bash scripts/status_all.sh

# 停止所有服务
bash scripts/stop_all.sh
```

### 启动桌面应用

```bash
cd core-platform/apps/desktop
npm run tauri dev
```

## 服务端口

| 服务 | 端口 | 说明 |
|------|------|------|
| model_gateway | 18080 | 模型网关 |
| orchestrator | 18081 | 编排器 |
| agent_team_service | 18094 | Agent 团队服务 |
| real_impl_service | 18095 | 实现服务 |
| research_real_service | 18098 | 研究服务 |
| hyperframes_service | 18099 | 超帧服务 |
| model_bootstrap_service | 18100 | 模型引导服务 |

## 构建

### 桌面应用

```bash
cd core-platform/apps/desktop

# 开发模式
npm run tauri dev

# 构建生产版本
npm run tauri build
```

### Windows 构建（GitHub Actions）

项目配置了自动化的 Windows 构建工作流，可以通过以下方式触发：

```bash
# 使用 GitHub CLI
gh workflow run build-win-release.yml -f tag_name=win-test-20260421

# 或在 GitHub 网页界面手动触发
# https://github.com/CASTvivian/local-ai-platform/actions
```

## 文档

详细的文档和说明请参考：

- [核心平台文档](core-platform/docs/)
- [插件开发指南](core-platform/plugins/)
- [API 文档](core-platform/docs/api/)
- [部署指南](core-platform/docs/deployment/)

## 贡献

欢迎贡献代码、报告问题或提出改进建议！

## 许可证

[待添加]

## 联系方式

- GitHub Issues: [CASTvivian/local-ai-platform/issues](https://github.com/CASTvivian/local-ai-platform/issues)
