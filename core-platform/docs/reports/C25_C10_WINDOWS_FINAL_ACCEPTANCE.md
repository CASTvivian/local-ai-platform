# C25-C10 Windows Final Acceptance

## Purpose
Final Windows acceptance after C25 Runtime rebuild.

## Current HEAD
\`853944b262f8c186f6d10c06c2a55af96708724c\`

## Acceptance script
\`core-platform/scripts/windows/acceptance/c25_final_acceptance.ps1\`

## Windows test steps

1. Download latest successful \`local-ai-platform-win\` artifact.
2. Install \`Local AI Platform_0.1.0_x64-setup.exe\`.
3. Launch MAOMIAI once.
4. Open PowerShell.
5. Run:
   \`\`\`powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
   powershell -ExecutionPolicy Bypass -File .\\c25_final_acceptance.ps1
   \`\`\`
6. Send back:
   \`\`\`text
   Desktop\\maomiai-c25-acceptance\\c25-final-acceptance-result.json
   \`\`\`

## Must pass

- Agent Runtime 18131
- Model Gateway 18080
- MCP tools
- Capability registry
- Planner health
- Agent run
- Timeline replay
- Team registry
- Team run