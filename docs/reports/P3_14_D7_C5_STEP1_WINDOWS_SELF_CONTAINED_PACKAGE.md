# P3.14-D7-C5 Step 1 Windows Self-contained Runtime Package
## Status
Downloaded for Windows real-machine validation.
## Workflow
- Run ID: 25360366066
- Status: success
- Conclusion: success
## Source Commit
`245a2b1`
## Artifact
```
releases/windows-d7-c5-self-contained-runtime/
├── desktop_lib.exe
├── BUILD_INFO.json
├── Local AI Platform_0.1.0_x64-setup.exe
└── Local AI Platform_0.1.0_x64_en-US.msi
```
Size: 13M
## Included
- Self-contained Python runtime manager
- Automatic Python embeddable download
- Automatic pip installation
- Automatic FastAPI / Uvicorn / Pydantic dependency installation
- Backend service startup through embedded Python
## Windows Test
Install the setup exe and test:
1. Open MAOMIAI.
2. Go to 本地 AI 准备.
3. Click 检查本地 AI 状态.
4. Observe whether runtime/python is downloaded.
5. Observe whether ports 18100 / 18080 start.
6. Then test Ollama detection.
