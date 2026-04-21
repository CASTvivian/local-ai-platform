Local AI Platform Windows Bundle

目录说明：
- backend/  : 后端服务代码
- scripts/  : 启停脚本
- 桌面启动器会优先尝试调用 scripts/start_all.bat

要求：
1. Windows 已安装 Python 3.11+ 并加入 PATH
2. 已安装 Ollama（后续版本可自动引导安装）
3. 如无模型，可通过 bootstrap 流程下载 qwen2.5:7b / qwen2.5-coder:7b

首次建议：
1. 打开桌面程序
2. 点击"启动后端"
3. 点击"检查健康状态"
4. 点击"打开控制台"
