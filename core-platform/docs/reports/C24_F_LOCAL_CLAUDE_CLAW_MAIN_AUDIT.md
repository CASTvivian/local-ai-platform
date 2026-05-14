# C24-F Local Claude / Claw Main Audit

Generated at: Thu May 14 16:33:54 CST 2026

## 1. Local candidate directories
### claude-code-source-code-main
- exists: yes
- file_count: 1937
claude-code-source-code-main/stubs/macros.ts
claude-code-source-code-main/stubs/bun-bundle.ts
claude-code-source-code-main/stubs/macros.d.ts
claude-code-source-code-main/stubs/global.d.ts
claude-code-source-code-main/types/connectorText.js
claude-code-source-code-main/README_JA.md
claude-code-source-code-main/README_KR.md
claude-code-source-code-main/QUICKSTART.md
claude-code-source-code-main/utils/attributionHooks.js
claude-code-source-code-main/utils/udsClient.js
claude-code-source-code-main/utils/systemThemeWatcher.js
claude-code-source-code-main/README.md
claude-code-source-code-main/README_CN.md
claude-code-source-code-main/.gitignore
claude-code-source-code-main/package-lock.json
claude-code-source-code-main/package.json
claude-code-source-code-main/scripts/prepare-src.mjs
claude-code-source-code-main/scripts/stub-modules.mjs
claude-code-source-code-main/scripts/build.mjs
claude-code-source-code-main/scripts/transform.mjs
claude-code-source-code-main/tsconfig.json
claude-code-source-code-main/src/history.ts
claude-code-source-code-main/src/main.tsx
claude-code-source-code-main/src/Tool.ts
claude-code-source-code-main/src/commands.ts
claude-code-source-code-main/src/dialogLaunchers.tsx
claude-code-source-code-main/src/replLauncher.tsx
claude-code-source-code-main/src/context.ts
claude-code-source-code-main/src/setup.ts
claude-code-source-code-main/src/QueryEngine.ts
claude-code-source-code-main/src/costHook.ts
claude-code-source-code-main/src/tools.ts
claude-code-source-code-main/src/query.ts
claude-code-source-code-main/src/cost-tracker.ts
claude-code-source-code-main/src/interactiveHelpers.tsx
claude-code-source-code-main/src/tasks.ts
claude-code-source-code-main/src/ink.ts
claude-code-source-code-main/src/Task.ts
claude-code-source-code-main/src/projectOnboardingState.ts

### claw-code-main
- exists: yes
- file_count: 202
claw-code-main/rust/Cargo.toml
claw-code-main/rust/.clawd-todos.json
claw-code-main/rust/Cargo.lock
claw-code-main/rust/README.md
claw-code-main/rust/.gitignore
claw-code-main/rust/TUI-ENHANCEMENT-PLAN.md
claw-code-main/tests/test_porting_workspace.py
claw-code-main/README.md
claw-code-main/PARITY.md
claw-code-main/.gitignore
claw-code-main/.github/FUNDING.yml
claw-code-main/.claude.json
claw-code-main/assets/star-history.png
claw-code-main/assets/clawd-hero.jpeg
claw-code-main/assets/wsj-feature.png
claw-code-main/assets/instructkr.png
claw-code-main/assets/tweet-screenshot.png
claw-code-main/CLAUDE.md
claw-code-main/src/projectOnboardingState.py
claw-code-main/src/query_engine.py
claw-code-main/src/task.py
claw-code-main/src/ink.py
claw-code-main/src/cost_tracker.py
claw-code-main/src/tasks.py
claw-code-main/src/models.py
claw-code-main/src/query.py
claw-code-main/src/transcript.py
claw-code-main/src/bootstrap_graph.py
claw-code-main/src/execution_registry.py
claw-code-main/src/tools.py
claw-code-main/src/remote_runtime.py
claw-code-main/src/__init__.py
claw-code-main/src/system_init.py
claw-code-main/src/interactiveHelpers.py
claw-code-main/src/costHook.py
claw-code-main/src/port_manifest.py
claw-code-main/src/runtime.py
claw-code-main/src/deferred_init.py
claw-code-main/src/dialogLaunchers.py
claw-code-main/src/QueryEngine.py
claw-code-main/src/setup.py
claw-code-main/src/context.py
claw-code-main/src/command_graph.py
claw-code-main/src/direct_modes.py
claw-code-main/src/permissions.py
claw-code-main/src/prefetch.py
claw-code-main/src/tool_pool.py
claw-code-main/src/parity_audit.py
claw-code-main/src/session_store.py
claw-code-main/src/main.py
claw-code-main/src/commands.py
claw-code-main/src/Tool.py
claw-code-main/src/replLauncher.py
claw-code-main/src/history.py

### core-platform/references/agent_kernels/claude-code-source-code
- exists: yes
- file_count: 1979
core-platform/references/agent_kernels/claude-code-source-code/stubs/macros.ts
core-platform/references/agent_kernels/claude-code-source-code/stubs/bun-bundle.ts
core-platform/references/agent_kernels/claude-code-source-code/stubs/macros.d.ts
core-platform/references/agent_kernels/claude-code-source-code/stubs/global.d.ts
core-platform/references/agent_kernels/claude-code-source-code/types/connectorText.js
core-platform/references/agent_kernels/claude-code-source-code/README_JA.md
core-platform/references/agent_kernels/claude-code-source-code/README_KR.md
core-platform/references/agent_kernels/claude-code-source-code/QUICKSTART.md
core-platform/references/agent_kernels/claude-code-source-code/utils/attributionHooks.js
core-platform/references/agent_kernels/claude-code-source-code/utils/udsClient.js
core-platform/references/agent_kernels/claude-code-source-code/utils/systemThemeWatcher.js
core-platform/references/agent_kernels/claude-code-source-code/README.md
core-platform/references/agent_kernels/claude-code-source-code/README_CN.md
core-platform/references/agent_kernels/claude-code-source-code/.gitignore
core-platform/references/agent_kernels/claude-code-source-code/package-lock.json
core-platform/references/agent_kernels/claude-code-source-code/package.json
core-platform/references/agent_kernels/claude-code-source-code/scripts/prepare-src.mjs
core-platform/references/agent_kernels/claude-code-source-code/scripts/stub-modules.mjs
core-platform/references/agent_kernels/claude-code-source-code/scripts/build.mjs
core-platform/references/agent_kernels/claude-code-source-code/scripts/transform.mjs
core-platform/references/agent_kernels/claude-code-source-code/tsconfig.json
core-platform/references/agent_kernels/claude-code-source-code/.git/config
core-platform/references/agent_kernels/claude-code-source-code/.git/shallow
core-platform/references/agent_kernels/claude-code-source-code/.git/HEAD
core-platform/references/agent_kernels/claude-code-source-code/.git/description
core-platform/references/agent_kernels/claude-code-source-code/.git/index
core-platform/references/agent_kernels/claude-code-source-code/.git/packed-refs
core-platform/references/agent_kernels/claude-code-source-code/src/history.ts
core-platform/references/agent_kernels/claude-code-source-code/src/main.tsx
core-platform/references/agent_kernels/claude-code-source-code/src/Tool.ts
core-platform/references/agent_kernels/claude-code-source-code/src/commands.ts
core-platform/references/agent_kernels/claude-code-source-code/src/dialogLaunchers.tsx
core-platform/references/agent_kernels/claude-code-source-code/src/replLauncher.tsx
core-platform/references/agent_kernels/claude-code-source-code/src/context.ts
core-platform/references/agent_kernels/claude-code-source-code/src/setup.ts
core-platform/references/agent_kernels/claude-code-source-code/src/QueryEngine.ts
core-platform/references/agent_kernels/claude-code-source-code/src/costHook.ts
core-platform/references/agent_kernels/claude-code-source-code/src/tools.ts
core-platform/references/agent_kernels/claude-code-source-code/src/query.ts
core-platform/references/agent_kernels/claude-code-source-code/src/cost-tracker.ts
core-platform/references/agent_kernels/claude-code-source-code/src/interactiveHelpers.tsx
core-platform/references/agent_kernels/claude-code-source-code/src/tasks.ts
core-platform/references/agent_kernels/claude-code-source-code/src/ink.ts
core-platform/references/agent_kernels/claude-code-source-code/src/Task.ts
core-platform/references/agent_kernels/claude-code-source-code/src/projectOnboardingState.ts

### core-platform/references/agent_kernels/claw-code
- exists: no

## 2. Agent kernel files in local main dirs
claude-code-source-code-main/src/Tool.ts
claude-code-source-code-main/src/assistant/sessionHistory.ts
claude-code-source-code-main/src/bridge/codeSessionApi.ts
claude-code-source-code-main/src/bridge/createSession.ts
claude-code-source-code-main/src/bridge/sessionIdCompat.ts
claude-code-source-code-main/src/bridge/sessionRunner.ts
claude-code-source-code-main/src/cli/handlers/agents.ts
claude-code-source-code-main/src/commands/agents/agents.tsx
claude-code-source-code-main/src/commands/rename/generateSessionName.ts
claude-code-source-code-main/src/commands/sandbox-toggle/sandbox-toggle.tsx
claude-code-source-code-main/src/commands/session/session.tsx
claude-code-source-code-main/src/components/AgentProgressLine.tsx
claude-code-source-code-main/src/components/CoordinatorAgentStatus.tsx
claude-code-source-code-main/src/components/FallbackToolUseErrorMessage.tsx
claude-code-source-code-main/src/components/FallbackToolUseRejectedMessage.tsx
claude-code-source-code-main/src/components/FileEditToolDiff.tsx
claude-code-source-code-main/src/components/FileEditToolUpdatedMessage.tsx
claude-code-source-code-main/src/components/FileEditToolUseRejectedMessage.tsx
claude-code-source-code-main/src/components/MCPServerApprovalDialog.tsx
claude-code-source-code-main/src/components/NotebookEditToolUseRejectedMessage.tsx
claude-code-source-code-main/src/components/PromptInput/SandboxPromptFooterHint.tsx
claude-code-source-code-main/src/components/PromptInput/useMaybeTruncateInput.ts
claude-code-source-code-main/src/components/SandboxViolationExpandedView.tsx
claude-code-source-code-main/src/components/SessionBackgroundHint.tsx
claude-code-source-code-main/src/components/SessionPreview.tsx
claude-code-source-code-main/src/components/ToolUseLoader.tsx
claude-code-source-code-main/src/components/agents/AgentDetail.tsx
claude-code-source-code-main/src/components/agents/AgentEditor.tsx
claude-code-source-code-main/src/components/agents/AgentNavigationFooter.tsx
claude-code-source-code-main/src/components/agents/AgentsList.tsx
claude-code-source-code-main/src/components/agents/AgentsMenu.tsx
claude-code-source-code-main/src/components/agents/ToolSelector.tsx
claude-code-source-code-main/src/components/agents/agentFileUtils.ts
claude-code-source-code-main/src/components/agents/generateAgent.ts
claude-code-source-code-main/src/components/agents/new-agent-creation/CreateAgentWizard.tsx
claude-code-source-code-main/src/components/agents/new-agent-creation/wizard-steps/ToolsStep.tsx
claude-code-source-code-main/src/components/agents/validateAgent.ts
claude-code-source-code-main/src/components/mcp/MCPAgentServerMenu.tsx
claude-code-source-code-main/src/components/mcp/MCPToolDetailView.tsx
claude-code-source-code-main/src/components/mcp/MCPToolListView.tsx
claude-code-source-code-main/src/components/messages/AssistantToolUseMessage.tsx
claude-code-source-code-main/src/components/messages/GroupedToolUseContent.tsx
claude-code-source-code-main/src/components/messages/PlanApprovalMessage.tsx
claude-code-source-code-main/src/components/messages/UserAgentNotificationMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/RejectedToolUseMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/UserToolCanceledMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/UserToolErrorMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/UserToolRejectMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/UserToolResultMessage.tsx
claude-code-source-code-main/src/components/messages/UserToolResultMessage/UserToolSuccessMessage.tsx
claude-code-source-code-main/src/components/permissions/BashPermissionRequest/bashToolUseOptions.tsx
claude-code-source-code-main/src/components/permissions/ComputerUseApproval/ComputerUseApproval.tsx
claude-code-source-code-main/src/components/permissions/FileWritePermissionRequest/FileWriteToolDiff.tsx
claude-code-source-code-main/src/components/permissions/NotebookEditPermissionRequest/NotebookEditToolDiff.tsx
claude-code-source-code-main/src/components/permissions/PowerShellPermissionRequest/powershellToolUseOptions.tsx
claude-code-source-code-main/src/components/permissions/SandboxPermissionRequest.tsx
claude-code-source-code-main/src/components/sandbox/SandboxConfigTab.tsx
claude-code-source-code-main/src/components/sandbox/SandboxDependenciesTab.tsx
claude-code-source-code-main/src/components/sandbox/SandboxDoctorSection.tsx
claude-code-source-code-main/src/components/sandbox/SandboxOverridesTab.tsx
claude-code-source-code-main/src/components/sandbox/SandboxSettings.tsx
claude-code-source-code-main/src/components/tasks/AsyncAgentDetailDialog.tsx
claude-code-source-code-main/src/components/tasks/RemoteSessionDetailDialog.tsx
claude-code-source-code-main/src/components/tasks/RemoteSessionProgress.tsx
claude-code-source-code-main/src/components/tasks/renderToolActivity.tsx
claude-code-source-code-main/src/constants/toolLimits.ts
claude-code-source-code-main/src/constants/tools.ts
claude-code-source-code-main/src/entrypoints/agentSdkTypes.ts
claude-code-source-code-main/src/entrypoints/sandboxTypes.ts
claude-code-source-code-main/src/hooks/useCanUseTool.tsx
claude-code-source-code-main/src/hooks/useMergedTools.ts
claude-code-source-code-main/src/hooks/useRemoteSession.ts
claude-code-source-code-main/src/hooks/useSSHSession.ts
claude-code-source-code-main/src/hooks/useSessionBackgrounding.ts
claude-code-source-code-main/src/remote/RemoteSessionManager.ts
claude-code-source-code-main/src/remote/SessionsWebSocket.ts
claude-code-source-code-main/src/server/createDirectConnectSession.ts
claude-code-source-code-main/src/services/AgentSummary/agentSummary.ts
claude-code-source-code-main/src/services/SessionMemory/sessionMemory.ts
claude-code-source-code-main/src/services/SessionMemory/sessionMemoryUtils.ts
claude-code-source-code-main/src/services/api/sessionIngress.ts
claude-code-source-code-main/src/services/compact/sessionMemoryCompact.ts
claude-code-source-code-main/src/services/mcpServerApproval.tsx
claude-code-source-code-main/src/services/toolUseSummary/toolUseSummaryGenerator.ts
claude-code-source-code-main/src/services/tools/StreamingToolExecutor.ts
claude-code-source-code-main/src/services/tools/toolExecution.ts
claude-code-source-code-main/src/services/tools/toolHooks.ts
claude-code-source-code-main/src/services/tools/toolOrchestration.ts
claude-code-source-code-main/src/skills/bundled/scheduleRemoteAgents.ts
claude-code-source-code-main/src/tasks/LocalAgentTask/LocalAgentTask.tsx
claude-code-source-code-main/src/tasks/LocalMainSessionTask.ts
claude-code-source-code-main/src/tasks/RemoteAgentTask/RemoteAgentTask.tsx
claude-code-source-code-main/src/tools.ts
claude-code-source-code-main/src/tools/AgentTool/AgentTool.tsx
claude-code-source-code-main/src/tools/AgentTool/agentColorManager.ts
claude-code-source-code-main/src/tools/AgentTool/agentDisplay.ts
claude-code-source-code-main/src/tools/AgentTool/agentMemory.ts
claude-code-source-code-main/src/tools/AgentTool/agentMemorySnapshot.ts
claude-code-source-code-main/src/tools/AgentTool/agentToolUtils.ts
claude-code-source-code-main/src/tools/AgentTool/built-in/claudeCodeGuideAgent.ts
claude-code-source-code-main/src/tools/AgentTool/built-in/exploreAgent.ts
claude-code-source-code-main/src/tools/AgentTool/built-in/generalPurposeAgent.ts
claude-code-source-code-main/src/tools/AgentTool/built-in/planAgent.ts
claude-code-source-code-main/src/tools/AgentTool/built-in/verificationAgent.ts
claude-code-source-code-main/src/tools/AgentTool/builtInAgents.ts
claude-code-source-code-main/src/tools/AgentTool/forkSubagent.ts
claude-code-source-code-main/src/tools/AgentTool/loadAgentsDir.ts
claude-code-source-code-main/src/tools/AgentTool/resumeAgent.ts
claude-code-source-code-main/src/tools/AgentTool/runAgent.ts
claude-code-source-code-main/src/tools/AskUserQuestionTool/AskUserQuestionTool.tsx
claude-code-source-code-main/src/tools/BashTool/BashTool.tsx
claude-code-source-code-main/src/tools/BashTool/BashToolResultMessage.tsx
claude-code-source-code-main/src/tools/BashTool/shouldUseSandbox.ts
claude-code-source-code-main/src/tools/BashTool/toolName.ts
claude-code-source-code-main/src/tools/BriefTool/BriefTool.ts
claude-code-source-code-main/src/tools/ConfigTool/ConfigTool.ts
claude-code-source-code-main/src/tools/EnterPlanModeTool/EnterPlanModeTool.ts
claude-code-source-code-main/src/tools/EnterWorktreeTool/EnterWorktreeTool.ts
claude-code-source-code-main/src/tools/ExitPlanModeTool/ExitPlanModeV2Tool.ts
claude-code-source-code-main/src/tools/ExitWorktreeTool/ExitWorktreeTool.ts
claude-code-source-code-main/src/tools/FileEditTool/FileEditTool.ts
claude-code-source-code-main/src/tools/FileReadTool/FileReadTool.ts
claude-code-source-code-main/src/tools/FileWriteTool/FileWriteTool.ts
claude-code-source-code-main/src/tools/GlobTool/GlobTool.ts
claude-code-source-code-main/src/tools/GrepTool/GrepTool.ts
claude-code-source-code-main/src/tools/LSPTool/LSPTool.ts
claude-code-source-code-main/src/tools/ListMcpResourcesTool/ListMcpResourcesTool.ts
claude-code-source-code-main/src/tools/MCPTool/MCPTool.ts
claude-code-source-code-main/src/tools/McpAuthTool/McpAuthTool.ts
claude-code-source-code-main/src/tools/NotebookEditTool/NotebookEditTool.ts
claude-code-source-code-main/src/tools/PowerShellTool/PowerShellTool.tsx
claude-code-source-code-main/src/tools/PowerShellTool/toolName.ts
claude-code-source-code-main/src/tools/REPLTool/primitiveTools.ts
claude-code-source-code-main/src/tools/ReadMcpResourceTool/ReadMcpResourceTool.ts
claude-code-source-code-main/src/tools/RemoteTriggerTool/RemoteTriggerTool.ts
claude-code-source-code-main/src/tools/ScheduleCronTool/CronCreateTool.ts
claude-code-source-code-main/src/tools/ScheduleCronTool/CronDeleteTool.ts
claude-code-source-code-main/src/tools/ScheduleCronTool/CronListTool.ts
claude-code-source-code-main/src/tools/SendMessageTool/SendMessageTool.ts
claude-code-source-code-main/src/tools/SkillTool/SkillTool.ts
claude-code-source-code-main/src/tools/SyntheticOutputTool/SyntheticOutputTool.ts
claude-code-source-code-main/src/tools/TaskCreateTool/TaskCreateTool.ts
claude-code-source-code-main/src/tools/TaskGetTool/TaskGetTool.ts
claude-code-source-code-main/src/tools/TaskListTool/TaskListTool.ts
claude-code-source-code-main/src/tools/TaskOutputTool/TaskOutputTool.tsx
claude-code-source-code-main/src/tools/TaskStopTool/TaskStopTool.ts
claude-code-source-code-main/src/tools/TaskUpdateTool/TaskUpdateTool.ts
claude-code-source-code-main/src/tools/TeamCreateTool/TeamCreateTool.ts
claude-code-source-code-main/src/tools/TeamDeleteTool/TeamDeleteTool.ts
claude-code-source-code-main/src/tools/TodoWriteTool/TodoWriteTool.ts
claude-code-source-code-main/src/tools/ToolSearchTool/ToolSearchTool.ts
claude-code-source-code-main/src/tools/WebFetchTool/WebFetchTool.ts
claude-code-source-code-main/src/tools/WebSearchTool/WebSearchTool.ts
claude-code-source-code-main/src/tools/shared/spawnMultiAgent.ts
claude-code-source-code-main/src/tools/testing/TestingPermissionTool.tsx
claude-code-source-code-main/src/utils/agentContext.ts
claude-code-source-code-main/src/utils/agentId.ts
claude-code-source-code-main/src/utils/agentSwarmsEnabled.ts
claude-code-source-code-main/src/utils/agenticSessionSearch.ts
claude-code-source-code-main/src/utils/autoRunIssue.tsx
claude-code-source-code-main/src/utils/background/remote/remoteSession.ts
claude-code-source-code-main/src/utils/bash/specs/srun.ts
claude-code-source-code-main/src/utils/classifierApprovals.ts
claude-code-source-code-main/src/utils/classifierApprovalsHook.ts
claude-code-source-code-main/src/utils/claudeInChrome/toolRendering.tsx
claude-code-source-code-main/src/utils/computerUse/drainRunLoop.ts
claude-code-source-code-main/src/utils/computerUse/executor.ts
claude-code-source-code-main/src/utils/computerUse/toolRendering.tsx
claude-code-source-code-main/src/utils/concurrentSessions.ts
claude-code-source-code-main/src/utils/embeddedTools.ts
claude-code-source-code-main/src/utils/forkedAgent.ts
claude-code-source-code-main/src/utils/groupToolUses.ts
claude-code-source-code-main/src/utils/hooks/execAgentHook.ts
claude-code-source-code-main/src/utils/hooks/sessionHooks.ts
claude-code-source-code-main/src/utils/listSessionsImpl.ts
claude-code-source-code-main/src/utils/model/agent.ts
claude-code-source-code-main/src/utils/permissions/PermissionPromptToolResultSchema.ts
claude-code-source-code-main/src/utils/plugins/loadPluginAgents.ts
claude-code-source-code-main/src/utils/sandbox/sandbox-adapter.ts
claude-code-source-code-main/src/utils/sandbox/sandbox-ui-utils.ts
claude-code-source-code-main/src/utils/sessionActivity.ts
claude-code-source-code-main/src/utils/sessionEnvVars.ts
claude-code-source-code-main/src/utils/sessionEnvironment.ts
claude-code-source-code-main/src/utils/sessionFileAccessHooks.ts
claude-code-source-code-main/src/utils/sessionIngressAuth.ts
claude-code-source-code-main/src/utils/sessionRestore.ts
claude-code-source-code-main/src/utils/sessionStart.ts
claude-code-source-code-main/src/utils/sessionState.ts
claude-code-source-code-main/src/utils/sessionStorage.ts
claude-code-source-code-main/src/utils/sessionStoragePortable.ts
claude-code-source-code-main/src/utils/sessionTitle.ts
claude-code-source-code-main/src/utils/sessionUrl.ts
claude-code-source-code-main/src/utils/settings/toolValidationConfig.ts
claude-code-source-code-main/src/utils/settings/validateEditTool.ts
claude-code-source-code-main/src/utils/shell/shellToolUtils.ts
claude-code-source-code-main/src/utils/standaloneAgent.ts
claude-code-source-code-main/src/utils/swarm/backends/PaneBackendExecutor.ts
claude-code-source-code-main/src/utils/swarm/inProcessRunner.ts
claude-code-source-code-main/src/utils/telemetry/betaSessionTracing.ts
claude-code-source-code-main/src/utils/telemetry/sessionTracing.ts
claude-code-source-code-main/src/utils/toolErrors.ts
claude-code-source-code-main/src/utils/toolPool.ts
claude-code-source-code-main/src/utils/toolResultStorage.ts
claude-code-source-code-main/src/utils/toolSchemaCache.ts
claude-code-source-code-main/src/utils/toolSearch.ts
claude-code-source-code-main/src/utils/truncate.ts
claude-code-source-code-main/src/utils/ultraplan/ccrSession.ts
claude-code-source-code-main/src/utils/userAgent.ts
claude-code-source-code-main/tools/OverflowTestTool/OverflowTestTool.js
claude-code-source-code-main/tools/TungstenTool/TungstenTool.js
claw-code-main/.claude/sessions/session-1774998936453.json
claw-code-main/.claude/sessions/session-1774998994373.json
claw-code-main/.claude/sessions/session-1775007533836.json
claw-code-main/.claude/sessions/session-1775007622154.json
claw-code-main/.claude/sessions/session-1775007632904.json
claw-code-main/.claude/sessions/session-1775007846522.json
claw-code-main/.claude/sessions/session-1775009126105.json
claw-code-main/.claude/sessions/session-1775009583240.json
claw-code-main/.claude/sessions/session-1775009651284.json
claw-code-main/.claude/sessions/session-1775010002596.json
claw-code-main/.claude/sessions/session-1775010229294.json
claw-code-main/.claude/sessions/session-1775010237519.json
claw-code-main/rust/.claude/sessions/session-1775007453382.json
claw-code-main/rust/.claude/sessions/session-1775007484031.json
claw-code-main/rust/.claude/sessions/session-1775007490104.json
claw-code-main/rust/.claude/sessions/session-1775007981374.json
claw-code-main/rust/.claude/sessions/session-1775008007069.json
claw-code-main/rust/.claude/sessions/session-1775008071886.json
claw-code-main/rust/.claude/sessions/session-1775008137143.json
claw-code-main/rust/.claude/sessions/session-1775008161929.json
claw-code-main/rust/.claude/sessions/session-1775008308936.json
claw-code-main/rust/.claude/sessions/session-1775008427969.json
claw-code-main/rust/.claude/sessions/session-1775008464519.json
claw-code-main/rust/.claude/sessions/session-1775008997307.json
claw-code-main/rust/.claude/sessions/session-1775009119214.json
claw-code-main/rust/.claude/sessions/session-1775009126336.json
claw-code-main/rust/.claude/sessions/session-1775009145469.json
claw-code-main/rust/.claude/sessions/session-1775009431231.json
claw-code-main/rust/.claude/sessions/session-1775009769569.json
claw-code-main/rust/.claude/sessions/session-1775009841982.json
claw-code-main/rust/.claude/sessions/session-1775009869734.json
claw-code-main/rust/.claude/sessions/session-1775010047738.json
claw-code-main/rust/.claude/sessions/session-1775010333630.json
claw-code-main/rust/.claude/sessions/session-1775010384918.json
claw-code-main/rust/.claude/sessions/session-1775010909274.json
claw-code-main/rust/.claude/sessions/session-1775011146355.json
claw-code-main/rust/.claude/sessions/session-1775011562247.json
claw-code-main/rust/.claude/sessions/session-1775012674485.json
claw-code-main/rust/.claude/sessions/session-1775012687059.json
claw-code-main/rust/.claude/sessions/session-1775013221875.json
claw-code-main/rust/crates/runtime/src/sandbox.rs
claw-code-main/rust/crates/runtime/src/session.rs
claw-code-main/src/Tool.py
claw-code-main/src/reference_data/tools_snapshot.json
claw-code-main/src/remote_runtime.py
claw-code-main/src/runtime.py
claw-code-main/src/session_store.py
claw-code-main/src/tool_pool.py
claw-code-main/src/tools.py

## 3. Claude Code / Claw Code markers
claude-code-source-code-main/README_JA.md:103:| `sessionTranscript/sessionTranscript.js` | セッショントランスクリプトサービス | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_JA.md:104:| `commands/agents-platform/index.js` | 内部エージェントプラットフォーム | `ant`（内部） |
claude-code-source-code-main/README_JA.md:116:| `services/sessionTranscript/sessionTranscript.js` | セッショントランスクリプト | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_JA.md:117:| `tasks/LocalWorkflowTask/LocalWorkflowTask.js` | ローカルワークフロータスク | `WORKFLOW_SCRIPTS` |
claude-code-source-code-main/README_JA.md:146:| `VerifyPlanExecutionTool` | 計画実行検証 | `CLAUDE_CODE_VERIFY_PLAN` |
claude-code-source-code-main/README_JA.md:162:| `yolo-classifier-prompts/permissions_anthropic.txt` | Anthropic内部権限プロンプト |
claude-code-source-code-main/README_JA.md:163:| `yolo-classifier-prompts/permissions_external.txt` | 外部ユーザー権限プロンプト |
claude-code-source-code-main/README_JA.md:223:                                stop_reason == "tool_use"?
claude-code-source-code-main/README_JA.md:228:                        tool_result追加
claude-code-source-code-main/README_JA.md:247:├── Task.ts                  # タスクタイプ、ID、状態ベースクラス
claude-code-source-code-main/README_JA.md:259:│   ├── sessionRunner.ts     #   プロセススポーン
claude-code-source-code-main/README_KR.md:96:| `sessionTranscript/sessionTranscript.js` | 세션 트랜스크립트 서비스 | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_KR.md:97:| `commands/agents-platform/index.js` | 내부 에이전트 플랫폼 | `ant` (내부) |
claude-code-source-code-main/README_KR.md:109:| `services/sessionTranscript/sessionTranscript.js` | 세션 트랜스크립트 | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_KR.md:110:| `tasks/LocalWorkflowTask/LocalWorkflowTask.js` | 로컬 워크플로우 태스크 | `WORKFLOW_SCRIPTS` |
claude-code-source-code-main/README_KR.md:139:| `VerifyPlanExecutionTool` | 계획 실행 검증 | `CLAUDE_CODE_VERIFY_PLAN` |
claude-code-source-code-main/README_KR.md:155:| `yolo-classifier-prompts/permissions_anthropic.txt` | Anthropic 내부 권한 프롬프트 |
claude-code-source-code-main/README_KR.md:156:| `yolo-classifier-prompts/permissions_external.txt` | 외부 사용자 권한 프롬프트 |
claude-code-source-code-main/README_KR.md:216:                                stop_reason == "tool_use"?
claude-code-source-code-main/README_KR.md:221:                        tool_result 추가
claude-code-source-code-main/README_KR.md:240:├── Task.ts                  # 태스크 타입, ID, 상태 베이스 클래스
claude-code-source-code-main/README_KR.md:252:│   ├── sessionRunner.ts     #   프로세스 스폰
claude-code-source-code-main/docs/en/02-hidden-features-and-codenames.md:47:2. **Empty tool_result causes zero output**
claude-code-source-code-main/docs/en/02-hidden-features-and-codenames.md:75:| `tengu_hive_evidence` | Verification agent |
claude-code-source-code-main/docs/en/02-hidden-features-and-codenames.md:90:| Verification agent | None | Required for non-trivial changes |
claude-code-source-code-main/docs/en/02-hidden-features-and-codenames.md:100:- `VerifyPlanExecutionTool` — plan verification
claude-code-source-code-main/docs/en/02-hidden-features-and-codenames.md:101:- Agent nesting (agents spawning agents)
claude-code-source-code-main/docs/en/01-telemetry-and-privacy.md:58:- session ID, user ID, device ID
claude-code-source-code-main/docs/en/01-telemetry-and-privacy.md:62:- agent type, team name, parent session ID
claude-code-source-code-main/docs/en/01-telemetry-and-privacy.md:111:- id, sessionId, deviceID
claude-code-source-code-main/docs/en/01-telemetry-and-privacy.md:119:1. **Volume**: Hundreds of events per session are collected
claude-code-source-code-main/docs/en/05-future-roadmap.md:57:The largest unreleased feature, KAIROS transforms Claude Code from a reactive assistant into a proactive autonomous agent.
claude-code-source-code-main/docs/en/05-future-roadmap.md:119:| **RemoteTriggerTool** | `AGENT_TRIGGERS_REMOTE` | Remote agent triggering |
claude-code-source-code-main/docs/en/05-future-roadmap.md:121:| **VerifyPlanExecutionTool** | VERIFY_PLAN env | Plan execution verification |
claude-code-source-code-main/docs/en/05-future-roadmap.md:127:Multi-agent coordination system:
claude-code-source-code-main/docs/en/05-future-roadmap.md:134:Enables coordinated task execution across multiple agents with shared state and messaging.
claude-code-source-code-main/docs/en/05-future-roadmap.md:149:## 7. Dream Task
claude-code-source-code-main/docs/en/05-future-roadmap.md:151:Background memory consolidation subagent:
claude-code-source-code-main/docs/en/05-future-roadmap.md:154:// src/tasks/DreamTask/
claude-code-source-code-main/docs/en/05-future-roadmap.md:167:Claude Code is evolving from a **coding assistant** into an **always-on autonomous development agent**.
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:13:Every eligible session fetches settings from:
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:75:// src/utils/permissions/bypassPermissionsKillswitch.ts
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:76:// Checks a Statsig gate to disable bypass permissions
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:79:Can disable permission bypass capabilities without user consent.
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:84:// src/utils/permissions/autoModeState.ts
claude-code-source-code-main/docs/en/04-remote-control-and-killswitches.md:110:// src/utils/agentSwarmsEnabled.ts
claude-code-source-code-main/docs/en/03-undercover-mode.md:107:The phrase "Do not blow your cover" frames the AI as an undercover agent. The intentional concealment of AI authorship in public code contributions raises questions about:
claude-code-source-code-main/README.md:17:- [Tool System & Permissions](#tool-system-architecture) — 40+ tools, permission flow, sub-agents
claude-code-source-code-main/README.md:18:- [The 12 Progressive Harness Mechanisms](#the-12-progressive-harness-mechanisms) — How Claude Code layers production features on the agent loop
claude-code-source-code-main/README.md:63:| 02 | **Hidden Features & Codenames** | Animal codenames (Capybara v8, Tengu, Fennec→Opus 4.6, **Numbat** next). Feature flags use random word pairs (`tengu_frond_boric`) to obscure purpose. Internal users get better prompts, verification agents, and effort anchors. Hidden commands: `/btw`, `/stickers`. |
claude-code-source-code-main/README.md:65:| 04 | **Remote Control** | Hourly polling of `/api/claude_code/settings`. Dangerous changes show blocking dialog — **reject = app exits**. 6+ killswitches (bypass permissions, fast mode, voice mode, analytics sink). GrowthBook flags can change any user's behavior without consent. |
claude-code-source-code-main/README.md:66:| 05 | **Future Roadmap** | **Numbat** codename confirmed. Opus 4.7 / Sonnet 4.8 in development. **KAIROS** = fully autonomous agent mode with `<tick>` heartbeats, push notifications, PR subscriptions. Voice mode (push-to-talk) ready but gated. 17 unreleased tools found. |
claude-code-source-code-main/README.md:97:| `coordinator/workerAgent.js` | Multi-agent coordinator worker | `COORDINATOR_MODE` |
claude-code-source-code-main/README.md:98:| `bridge/peerSessions.js` | Bridge peer session management | `BRIDGE_MODE` |
claude-code-source-code-main/README.md:100:| `assistant/AssistantSessionChooser.js` | Assistant session picker | `KAIROS` |
claude-code-source-code-main/README.md:105:| `sessionTranscript/sessionTranscript.js` | Session transcript service | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README.md:106:| `commands/agents-platform/index.js` | Internal agents platform | `ant` (internal) |
claude-code-source-code-main/README.md:109:| `commands/fork/index.js` | Fork subagent command | `FORK_SUBAGENT` |
claude-code-source-code-main/README.md:118:| `services/sessionTranscript/sessionTranscript.js` | Session transcript | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README.md:119:| `tasks/LocalWorkflowTask/LocalWorkflowTask.js` | Local workflow task | `WORKFLOW_SCRIPTS` |
claude-code-source-code-main/README.md:140:| `REPLTool` | Interactive REPL (VM sandbox) | `ant` (internal) |
claude-code-source-code-main/README.md:142:| `SleepTool` | Sleep/delay in agent loop | `PROACTIVE` / `KAIROS` |
claude-code-source-code-main/README.md:149:| `VerifyPlanExecutionTool` | Plan verification | `CLAUDE_CODE_VERIFY_PLAN` |
claude-code-source-code-main/README.md:170:| `yolo-classifier-prompts/permissions_anthropic.txt` | Anthropic-internal permission prompt |
claude-code-source-code-main/README.md:171:| `yolo-classifier-prompts/permissions_external.txt` | External user permission prompt |
claude-code-source-code-main/README.md:234:                                stop_reason == "tool_use"?
claude-code-source-code-main/README.md:239:                        append tool_result
claude-code-source-code-main/README.md:243:    That is the minimal agent loop. Claude Code wraps this loop
claude-code-source-code-main/README.md:244:    with a production-grade harness: permissions, streaming,
claude-code-source-code-main/README.md:245:    concurrency, compaction, sub-agents, persistence, and MCP.
claude-code-source-code-main/README.md:256:├── query.ts                 # Main agent loop (785KB, largest file)
claude-code-source-code-main/README.md:258:├── Task.ts                  # Task types, IDs, state base
claude-code-source-code-main/README.md:270:│   ├── sessionRunner.ts     #   Process spawning
claude-code-source-code-main/README.md:280:│   ├── agents/              #   Agent management
claude-code-source-code-main/README.md:287:│   ├── plan/                #   Plan mode
claude-code-source-code-main/README.md:295:│   ├── permissions/         #   Permission dialogs
claude-code-source-code-main/README.md:304:│   ├── sdk/                 #   Agent SDK (types, sessions)
claude-code-source-code-main/README.md:311:│   └── toolPermission/      #   Tool permission handlers
claude-code-source-code-main/README.md:331:├── tasks/                   # Task implementations
claude-code-source-code-main/README.md:332:│   ├── LocalShellTask/      #   Bash command execution
claude-code-source-code-main/README.md:333:│   ├── LocalAgentTask/      #   Sub-agent execution
claude-code-source-code-main/README.md:334:│   ├── RemoteAgentTask/     #   Remote agent via bridge
claude-code-source-code-main/README.md:335:│   ├── InProcessTeammateTask/ # In-process teammate
claude-code-source-code-main/README.md:336:│   └── DreamTask/           #   Background thinking
claude-code-source-code-main/README.md:339:│   ├── AgentTool/           #   Sub-agent spawning + fork
claude-code-source-code-main/README.md:355:│   ├── permissions.ts       #   Permission types
claude-code-source-code-main/README.md:360:│   ├── permissions/         #   Permission rule engine
claude-code-source-code-main/README.md:364:│   ├── sandbox/             #   Sandbox runtime adapter
claude-code-source-code-main/README.md:370:│   ├── swarm/               #   Multi-agent swarm
claude-code-source-code-main/README.md:399:│    ├── query()                     ──> main agent loop              │
claude-code-source-code-main/README.md:412:│  ├─ call()       │ │  API client     │ │  ├─ permissions  │
claude-code-source-code-main/README.md:414:│  ├─ checkPerms() │ │  auto-compact   │ │  ├─ agents       │
claude-code-source-code-main/README.md:420:│  ├─ FileRead     │ │  executor       │ │                  │
claude-code-source-code-main/README.md:433:│ Task Types:      │ │ bridgeMain.ts   │
claude-code-source-code-main/README.md:434:│  ├─ local_bash   │ │  session mgmt   │
claude-code-source-code-main/README.md:435:│  ├─ local_agent  │ │ bridgeApi.ts    │
claude-code-source-code-main/README.md:436:│  ├─ remote_agent │ │  HTTP client    │
claude-code-source-code-main/README.md:439:│  └─ workflow     │ │ sessionRunner   │
claude-code-source-code-main/README.md:442:│  b=bash a=agent  │
claude-code-source-code-main/README.md:474: │   └─ tool_use block?
claude-code-source-code-main/README.md:480: │   canUseTool()                  ← permission check (hooks + rules + UI prompt)
claude-code-source-code-main/README.md:482: │       ├─ DENY ────────────────→ append tool_result(error), continue loop
claude-code-source-code-main/README.md:490: │       append tool_result        ← push to messages[], recordTranscript()
claude-code-source-code-main/README.md:494:     ▼ (stop_reason != "tool_use")
claude-code-source-code-main/README.md:495: yield result message              ← final text, usage, cost, session_id
claude-code-source-code-main/README.md:550:    MCP PROTOCOL             TeamDeleteTool            EnterPlanModeTool
claude-code-source-code-main/README.md:551:    ══════════════           TaskCreateTool            ExitPlanModeTool
claude-code-source-code-main/README.md:552:    MCPTool                  TaskGetTool               EnterWorktreeTool
claude-code-source-code-main/README.md:553:    ListMcpResourcesTool     TaskUpdateTool            ExitWorktreeTool
claude-code-source-code-main/README.md:554:    ReadMcpResourceTool      TaskListTool              TodoWriteTool
claude-code-source-code-main/README.md:555:                             TaskStopTool
claude-code-source-code-main/README.md:556:                             TaskOutputTool            SYSTEM
claude-code-source-code-main/README.md:574:    │  reject invalid inputs before any permission check │
claude-code-source-code-main/README.md:588:    │  Sources: settings, CLI args, session decisions    │
claude-code-source-code-main/README.md:601:    │  Tool-specific logic (e.g. path sandboxing)        │
claude-code-source-code-main/README.md:621:     │ Shared cache │ │ session  │ │ Async context│
claude-code-source-code-main/README.md:632:    ├─ SendMessageTool     → agent-to-agent messages
claude-code-source-code-main/README.md:633:    ├─ TaskCreate/Update   → shared task board
claude-code-source-code-main/README.md:639:    │    ├── Teammate A ──> claims Task 1         │
claude-code-source-code-main/README.md:640:    │    ├── Teammate B ──> claims Task 2         │
claude-code-source-code-main/README.md:641:    │    └── Teammate C ──> claims Task 3         │
claude-code-source-code-main/README.md:657:    │  System Prompt (tools, permissions, CLAUDE.md)      │
claude-code-source-code-main/README.md:667:    │  │ user → assistant → tool_use → tool_result   │    │
claude-code-source-code-main/README.md:757:    ~/.claude/projects/<hash>/sessions/
claude-code-source-code-main/README.md:758:    └── <session-id>.jsonl           ← append-only log
claude-code-source-code-main/README.md:767:         ├── --continue     → last session in cwd
claude-code-source-code-main/README.md:768:         ├── --resume <id>  → specific session
claude-code-source-code-main/README.md:769:         └── --fork-session → new ID, copy history
claude-code-source-code-main/README.md:790:    ├─ COORDINATOR_MODE      → multi-agent coordinator
claude-code-source-code-main/README.md:853:This source code demonstrates 12 layered mechanisms that a production AI agent harness needs beyond the basic loop. Each builds on the previous:
claude-code-source-code-main/README.md:865:    s03  PLANNING             "An agent without a plan drifts"
claude-code-source-code-main/README.md:866:         EnterPlanModeTool/ExitPlanModeTool + TodoWriteTool:
claude-code-source-code-main/README.md:870:         AgentTool + forkSubagent.ts: each child gets fresh messages[],
claude-code-source-code-main/README.md:874:         SkillTool + memdir/: inject via tool_result, not system prompt.
claude-code-source-code-main/README.md:882:         TaskCreate/Update/Get/List: file-based task graph with
claude-code-source-code-main/README.md:885:    s08  BACKGROUND TASKS     "Slow ops in background; agent keeps thinking"
claude-code-source-code-main/README.md:886:         DreamTask + LocalShellTask: daemon threads run commands,
claude-code-source-code-main/README.md:890:         TeamCreate/Delete + InProcessTeammateTask: persistent
claude-code-source-code-main/README.md:895:         all negotiation between agents.
claude-code-source-code-main/README.md:919:| **Ring Buffer** | Error log | Bounded memory for long sessions |
claude-code-source-code-main/README.md:922:| **Context Isolation** | `AsyncLocalStorage` | Per-agent context in shared process |
claude-code-source-code-main/README_CN.md:89:| `sessionTranscript/sessionTranscript.js` | 会话转录服务 | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_CN.md:90:| `commands/agents-platform/index.js` | 内部代理平台 | `ant` (内部) |
claude-code-source-code-main/README_CN.md:102:| `services/sessionTranscript/sessionTranscript.js` | 会话转录 | `TRANSCRIPT_CLASSIFIER` |
claude-code-source-code-main/README_CN.md:103:| `tasks/LocalWorkflowTask/LocalWorkflowTask.js` | 本地工作流任务 | `WORKFLOW_SCRIPTS` |
claude-code-source-code-main/README_CN.md:132:| `VerifyPlanExecutionTool` | 计划验证 | `CLAUDE_CODE_VERIFY_PLAN` |
claude-code-source-code-main/README_CN.md:148:| `yolo-classifier-prompts/permissions_anthropic.txt` | Anthropic 内部权限提示 |
claude-code-source-code-main/README_CN.md:149:| `yolo-classifier-prompts/permissions_external.txt` | 外部用户权限提示 |
claude-code-source-code-main/README_CN.md:209:                                stop_reason == "tool_use"?
claude-code-source-code-main/README_CN.md:214:                        追加 tool_result
claude-code-source-code-main/README_CN.md:233:├── Task.ts                  # 任务类型、ID、状态基类
claude-code-source-code-main/README_CN.md:245:│   ├── sessionRunner.ts     #   进程生成
claude-code-source-code-main/vendor/audio-capture-src/index.ts:15:  // Linux: always returns 3 (authorized) — no system-level microphone permission API.
claude-code-source-code-main/vendor/audio-capture-src/index.ts:142:// On Linux, always returns 3 (authorized) — no system-level mic permission API.
claude-code-source-code-main/src/assistant/sessionHistory.ts:3:import type { SDKMessage } from '../entrypoints/agentSdkTypes.js'
claude-code-source-code-main/src/assistant/sessionHistory.ts:32:  sessionId: string,
claude-code-source-code-main/src/assistant/sessionHistory.ts:36:    baseUrl: `${getOauthConfig().BASE_API_URL}/v1/sessions/${sessionId}/events`,
claude-code-source-code-main/src/history.ts:125:          entry.sessionId === currentSession &&
claude-code-source-code-main/src/history.ts:183: * Get history entries for the current project, with current session's entries first.
claude-code-source-code-main/src/history.ts:185: * Entries from the current session are yielded before entries from other sessions,
claude-code-source-code-main/src/history.ts:186: * so concurrent sessions don't interleave their up-arrow history. Within each group,
claude-code-source-code-main/src/history.ts:201:    if (entry.sessionId === currentSession) {
claude-code-source-code-main/src/history.ts:224:  sessionId?: string
claude-code-source-code-main/src/history.ts:402:    sessionId: getSessionId(),
claude-code-source-code-main/src/history.ts:412:  // Skip history when running in a tmux session spawned by Claude Code's Tungsten tool.
claude-code-source-code-main/src/history.ts:413:  // This prevents verification/test sessions from polluting the user's real command history.
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:4: * When running inside a CCR session container with upstreamproxy configured,
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:6: *   1. Reads the session token from /run/ccr/session_token
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:12: *      the agent loop can see it, but only after the relay is confirmed up
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:14: *   6. Exposes HTTPS_PROXY / SSL_CERT_FILE env vars for all agent subprocesses
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:17: * A broken proxy setup must never break an otherwise-working session.
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:31:export const SESSION_TOKEN_PATH = '/run/ccr/session_token'
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:36:// reach directly. Mirrors airlock/scripts/sandbox-shell-ccr.sh.
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:90:  // Every CCR session is a fresh container with no GB cache, so a client-side
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:96:  const sessionId = process.env.CLAUDE_CODE_REMOTE_SESSION_ID
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:97:  if (!sessionId) {
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:108:    logForDebugging('[upstreamproxy] no session token file; proxy disabled')
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:114:  // CCR injects ANTHROPIC_BASE_URL via StartupContext (sessionExecutor.ts /
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:115:  // sessionHandler.ts). getOauthConfig() is wrong here: it keys off
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:134:    const relay = await startUpstreamProxyRelay({ wsUrl, sessionId, token })
claude-code-source-code-main/src/upstreamproxy/upstreamproxy.ts:156: * Env vars to merge into every agent subprocess. Empty when the proxy is
claude-code-source-code-main/src/upstreamproxy/relay.ts:11: * routing; there's no connect_matcher in cdk-constructs. The session-ingress
claude-code-source-code-main/src/upstreamproxy/relay.ts:12: * tunnel (sessions/tunnel/v1alpha/tunnel.proto) already uses this pattern.
claude-code-source-code-main/src/upstreamproxy/relay.ts:28:// with an explicit agent (same pattern as SessionsWebSocket). Bun's native
claude-code-source-code-main/src/upstreamproxy/relay.ts:157:  sessionId: string
claude-code-source-code-main/src/upstreamproxy/relay.ts:161:    'Basic ' + Buffer.from(`${opts.sessionId}:${opts.token}`).toString('base64')
claude-code-source-code-main/src/upstreamproxy/relay.ts:163:  // wants the session-ingress JWT on the upgrade request, separate from the
claude-code-source-code-main/src/upstreamproxy/relay.ts:364:      agent: getWebSocketProxyAgent(wsUrl),
claude-code-source-code-main/src/ink/output.ts:34: * styleId is safe to cache: StylePool is session-lived (never reset).
claude-code-source-code-main/src/ink/render-node-to-output.ts:1193:          // on re-render → /permissions body blanked on Down arrow, #25436).
claude-code-source-code-main/src/ink/colorize.ts:58:// Computed once at module load — terminal/tmux environment doesn't change mid-session.
claude-code-source-code-main/src/ink/colorize.ts:91:      case 'magenta':
claude-code-source-code-main/src/ink/colorize.ts:92:        return type === 'foreground' ? chalk.magenta(str) : chalk.bgMagenta(str)
claude-code-source-code-main/src/ink/colorize.ts:117:      case 'magentaBright':
claude-code-source-code-main/src/ink/colorize.ts:119:          ? chalk.magentaBright(str)
claude-code-source-code-main/src/ink/colorize.ts:120:          : chalk.bgMagentaBright(str)
claude-code-source-code-main/src/ink/ink.tsx:598:    // during long sessions. 5 minutes is infrequent enough that the O(cells)
claude-code-source-code-main/src/ink/ink.tsx:1555:   * growth during long sessions. Migrates the front frame's screen IDs into
claude-code-source-code-main/src/ink/styles.ts:24:  | 'ansi:magenta'
claude-code-source-code-main/src/ink/styles.ts:32:  | 'ansi:magentaBright'
claude-code-source-code-main/src/ink/Ansi.tsx:180:  magenta: 'ansi:magenta',
claude-code-source-code-main/src/ink/Ansi.tsx:188:  brightMagenta: 'ansi:magentaBright',
claude-code-source-code-main/src/ink/components/App.tsx:357:      // the session freezes permanently (stdin reader dead, event loop alive).
claude-code-source-code-main/src/ink/hooks/use-tab-status.ts:50: * `null` emits CLEAR_TAB_STATUS so toggling off mid-session doesn't leave
claude-code-source-code-main/src/ink/hooks/use-tab-status.ts:59:    // showStatusInTerminalTab mid-session), clear the stale dot.
claude-code-source-code-main/src/ink/terminal.ts:41:    process.env.ConEmuTask
claude-code-source-code-main/src/ink/terminal.ts:181:// Computed once at module load — terminal capabilities don't change mid-session.
claude-code-source-code-main/src/ink/termio/types.ts:19:  | 'magenta'
claude-code-source-code-main/src/ink/termio/types.ts:27:  | 'brightMagenta'
claude-code-source-code-main/src/ink/termio/osc.ts:86: * crashes the iTerm2 session over SSH.
claude-code-source-code-main/src/ink/termio/osc.ts:131: * OSC 52 by default, VS Code shows a permission prompt on first use. Native
claude-code-source-code-main/src/ink/termio/osc.ts:167: * Only called when not in an SSH session (over SSH, these would write to
claude-code-source-code-main/src/ink/termio/sgr.ts:17:  'magenta',
claude-code-source-code-main/src/ink/termio/sgr.ts:25:  'brightMagenta',
claude-code-source-code-main/src/migrations/migrateBypassPermissionsAcceptedToSettings.ts:28:    logEvent('tengu_migrate_bypass_permissions_accepted', {})
claude-code-source-code-main/src/migrations/migrateBypassPermissionsAcceptedToSettings.ts:37:      new Error(`Failed to migrate bypass permissions accepted: ${error}`),
claude-code-source-code-main/src/migrations/resetAutoModeOptInForDefaultOffer.ts:5:import { getAutoModeEnabledState } from '../utils/permissions/permissionSetup.js'
claude-code-source-code-main/src/migrations/resetAutoModeOptInForDefaultOffer.ts:20: * (permissionSetup.ts:988) — the dialog would become unreachable and the
claude-code-source-code-main/src/migrations/resetAutoModeOptInForDefaultOffer.ts:35:        user?.permissions?.defaultMode !== 'auto'
claude-code-source-code-main/src/migrations/migrateEnableAllProjectMcpServersToSettings.ts:13: * Migration: Move MCP server approval fields from project config to local settings
claude-code-source-code-main/src/migrations/migrateEnableAllProjectMcpServersToSettings.ts:110:    logEvent('tengu_migrate_mcp_approval_fields_success', {
claude-code-source-code-main/src/migrations/migrateEnableAllProjectMcpServersToSettings.ts:116:    logEvent('tengu_migrate_mcp_approval_fields_error', {})
claude-code-source-code-main/src/main.tsx:48:import { isAgentSwarmsEnabled } from './utils/agentSwarmsEnabled.js';
claude-code-source-code-main/src/main.tsx:60:import { getSessionIngressAuthToken } from './utils/sessionIngressAuth.js';
claude-code-source-code-main/src/main.tsx:99:import type { AgentColorName } from './tools/AgentTool/agentColorManager.js';
claude-code-source-code-main/src/main.tsx:120:import { PERMISSION_MODES } from './utils/permissions/PermissionMode.js';
claude-code-source-code-main/src/main.tsx:121:import { checkAndDisableBypassPermissions, getAutoModeEnabledStateIfCached, initializeToolPermissionContext, initialPermissionModeFromCLI, isDefaultPermissionModeAuto, parseToolListFromCLI, removeDangerousPermissions, stripDangerousPermissionsForAutoMode, verifyAutoModeGateAccess } from './utils/permissions/permissionSetup.js';
claude-code-source-code-main/src/main.tsx:128:import { processSessionStartHooks, processSetupHooks } from './utils/sessionStart.js';
claude-code-source-code-main/src/main.tsx:129:import { cacheSessionTitle, getSessionIdFromLog, loadTranscriptFromFile, saveAgentSetting, saveMode, searchSessionsByCustomTitle, sessionIdExists } from './utils/sessionStorage.js';
claude-code-source-code-main/src/main.tsx:165:import { type ProcessedResume, processResumedConversation } from 'src/utils/sessionRestore.js';
claude-code-source-code-main/src/main.tsx:171:const autoModeStateModule = feature('TRANSCRIPT_CLASSIFIER') ? require('./utils/permissions/autoModeState.js') as typeof import('./utils/permissions/autoModeState.js') : null;
claude-code-source-code-main/src/main.tsx:201:import { SandboxManager } from './utils/sandbox/sandbox-adapter.js';
claude-code-source-code-main/src/main.tsx:274: * Per-session skill/plugin telemetry. Called from both the interactive path
claude-code-source-code-main/src/main.tsx:314:    sandbox_enabled: SandboxManager.isSandboxingEnabled(),
claude-code-source-code-main/src/main.tsx:315:    are_unsandboxed_commands_allowed: SandboxManager.areUnsandboxedCommandsAllowed(),
claude-code-source-code-main/src/main.tsx:316:    is_auto_bash_allowed_if_sandbox_enabled: SandboxManager.isAutoAllowBashIfSandboxedEnabled(),
claude-code-source-code-main/src/main.tsx:448:      // in the Bash tool's sandbox denyWithinAllow list, which is part of
claude-code-source-code-main/src/main.tsx:535:  // Note: 'local-agent' entrypoint is set by the local agent mode launcher
claude-code-source-code-main/src/main.tsx:554:// Set by early argv processing when `claude assistant [sessionId]` is detected
claude-code-source-code-main/src/main.tsx:556:  sessionId?: string;
claude-code-source-code-main/src/main.tsx:560:  sessionId: undefined,
claude-code-source-code-main/src/main.tsx:566:// the REPL an SSH-backed session instead of a local one.
claude-code-source-code-main/src/main.tsx:570:  permissionMode: string | undefined;
claude-code-source-code-main/src/main.tsx:580:  permissionMode: undefined,
claude-code-source-code-main/src/main.tsx:621:      _pendingConnect.dangerouslySkipPermissions = rawCliArgs.includes('--dangerously-skip-permissions');
claude-code-source-code-main/src/main.tsx:625:        const dspIdx = stripped.indexOf('--dangerously-skip-permissions');
claude-code-source-code-main/src/main.tsx:635:        const dspIdx = stripped.indexOf('--dangerously-skip-permissions');
claude-code-source-code-main/src/main.tsx:679:  // `claude assistant [sessionId]` — stash and strip so the main
claude-code-source-code-main/src/main.tsx:690:        _pendingAssistantChat.sessionId = nextArg;
claude-code-source-code-main/src/main.tsx:691:        rawArgs.splice(0, 2); // drop 'assistant' and sessionId
claude-code-source-code-main/src/main.tsx:705:  // sessions need the local REPL to drive them (interrupt, permissions).
claude-code-source-code-main/src/main.tsx:709:    // `ssh --permission-mode auto host /tmp` — standard POSIX flags-before-
claude-code-source-code-main/src/main.tsx:711:    // given, so `claude ssh --permission-mode auto host` and `claude ssh host
claude-code-source-code-main/src/main.tsx:712:    // --permission-mode auto` are equivalent. The host check below only needs
claude-code-source-code-main/src/main.tsx:720:      const dspIdx = rawCliArgs.indexOf('--dangerously-skip-permissions');
claude-code-source-code-main/src/main.tsx:725:      const pmIdx = rawCliArgs.indexOf('--permission-mode');
claude-code-source-code-main/src/main.tsx:727:        _pendingSSH.permissionMode = rawCliArgs[pmIdx + 1];
claude-code-source-code-main/src/main.tsx:730:      const pmEqIdx = rawCliArgs.findIndex(a => a.startsWith('--permission-mode='));
claude-code-source-code-main/src/main.tsx:732:        _pendingSSH.permissionMode = rawCliArgs[pmEqIdx]!.split('=')[1];
claude-code-source-code-main/src/main.tsx:735:      // Forward session-resume + model flags to the remote CLI's initial spawn.
claude-code-source-code-main/src/main.tsx:736:      // --continue/-c and --resume <uuid> operate on the REMOTE session history
claude-code-source-code-main/src/main.tsx:824:    if (process.env.CLAUDE_CODE_ENTRYPOINT === 'local-agent') return 'local-agent';
claude-code-source-code-main/src/main.tsx:827:    // Check if session-ingress token is provided (indicates remote session)
claude-code-source-code-main/src/main.tsx:841:  clientType !== 'claude-desktop' && clientType !== 'local-agent' && clientType !== 'remote') {
claude-code-source-code-main/src/main.tsx:845:  // Tag sessions created via `claude remote-control` so the backend can identify them
claude-code-source-code-main/src/main.tsx:968:  program.name('claude').description(`Claude Code - starts an interactive session by default, use -p/--print for non-interactive output`).argument('[prompt]', 'Your prompt', String)
claude-code-source-code-main/src/main.tsx:976:  }).addOption(new Option('-d2e, --debug-to-stderr', 'Enable debug mode (to stderr)').argParser(Boolean).hideHelp()).option('--debug-file <path>', 'Write debug logs to a specific file path (implicitly enables debug mode)', () => true).option('--verbose', 'Override verbose mode setting from config', () => true).option('-p, --print', 'Print response and exit (useful for pipes). Note: The workspace trust dialog is skipped when Claude is run with the -p mode. Only use this flag in directories you trust.', () => true).option('--bare', 'Minimal mode: skip hooks, LSP, plugin sync, attribution, auto-memory, background prefetches, keychain reads, and CLAUDE.md auto-discovery. Sets CLAUDE_CODE_SIMPLE=1. Anthropic auth is strictly ANTHROPIC_API_KEY or apiKeyHelper via --settings (OAuth and keychain are never read). 3P providers (Bedrock/Vertex/Foundry) use their own credentials. Skills still resolve via /skill-name. Explicitly provide context via: --system-prompt[-file], --append-system-prompt[-file], --add-dir (CLAUDE.md dirs), --mcp-config, --settings, --agents, --plugin-dir.', () => true).addOption(new Option('--init', 'Run Setup hooks with init trigger, then continue').hideHelp()).addOption(new Option('--init-only', 'Run Setup and SessionStart:startup hooks, then exit').hideHelp()).addOption(new Option('--maintenance', 'Run Setup hooks with maintenance trigger, then continue').hideHelp()).addOption(new Option('--output-format <format>', 'Output format (only works with --print): "text" (default), "json" (single result), or "stream-json" (realtime streaming)').choices(['text', 'json', 'stream-json'])).addOption(new Option('--json-schema <schema>', 'JSON Schema for structured output validation. ' + 'Example: {"type":"object","properties":{"name":{"type":"string"}},"required":["name"]}').argParser(String)).option('--include-hook-events', 'Include all hook lifecycle events in the output stream (only works with --output-format=stream-json)', () => true).option('--include-partial-messages', 'Include partial message chunks as they arrive (only works with --print and --output-format=stream-json)', () => true).addOption(new Option('--input-format <format>', 'Input format (only works with --print): "text" (default), or "stream-json" (realtime streaming input)').choices(['text', 'stream-json'])).option('--mcp-debug', '[DEPRECATED. Use --debug instead] Enable MCP debug mode (shows MCP server errors)', () => true).option('--dangerously-skip-permissions', 'Bypass all permission checks. Recommended only for sandboxes with no internet access.', () => true).option('--allow-dangerously-skip-permissions', 'Enable bypassing all permission checks as an option, without it being enabled by default. Recommended only for sandboxes with no internet access.', () => true).addOption(new Option('--thinking <mode>', 'Thinking mode: enabled (equivalent to adaptive), disabled').choices(['enabled', 'adaptive', 'disabled']).hideHelp()).addOption(new Option('--max-thinking-tokens <tokens>', '[DEPRECATED. Use --thinking instead for newer models] Maximum number of thinking tokens (only works with --print)').argParser(Number).hideHelp()).addOption(new Option('--max-turns <turns>', 'Maximum number of agentic turns in non-interactive mode. This will early exit the conversation after the specified number of turns. (only works with --print)').argParser(Number).hideHelp()).addOption(new Option('--max-budget-usd <amount>', 'Maximum dollar amount to spend on API calls (only works with --print)').argParser(value => {
claude-code-source-code-main/src/main.tsx:988:  }).hideHelp()).option('--replay-user-messages', 'Re-emit user messages from stdin back on stdout for acknowledgment (only works with --input-format=stream-json and --output-format=stream-json)', () => true).addOption(new Option('--enable-auth-status', 'Enable auth status messages in SDK mode').default(false).hideHelp()).option('--allowedTools, --allowed-tools <tools...>', 'Comma or space-separated list of tool names to allow (e.g. "Bash(git:*) Edit")').option('--tools <tools...>', 'Specify the list of available tools from the built-in set. Use "" to disable all tools, "default" to use all tools, or specify tool names (e.g. "Bash,Edit,Read").').option('--disallowedTools, --disallowed-tools <tools...>', 'Comma or space-separated list of tool names to deny (e.g. "Bash(git:*) Edit")').option('--mcp-config <configs...>', 'Load MCP servers from JSON files or strings (space-separated)').addOption(new Option('--permission-prompt-tool <tool>', 'MCP tool to use for permission prompts (only works with --print)').argParser(String).hideHelp()).addOption(new Option('--system-prompt <prompt>', 'System prompt to use for the session').argParser(String)).addOption(new Option('--system-prompt-file <file>', 'Read system prompt from a file').argParser(String).hideHelp()).addOption(new Option('--append-system-prompt <prompt>', 'Append a system prompt to the default system prompt').argParser(String)).addOption(new Option('--append-system-prompt-file <file>', 'Read system prompt from a file and append to the default system prompt').argParser(String).hideHelp()).addOption(new Option('--permission-mode <mode>', 'Permission mode to use for the session').argParser(String).choices(PERMISSION_MODES)).option('-c, --continue', 'Continue the most recent conversation in the current directory', () => true).option('-r, --resume [value]', 'Resume a conversation by session ID, or open interactive picker with optional search term', value => value || true).option('--fork-session', 'When resuming, create a new session ID instead of reusing the original (use with --resume or --continue)', () => true).addOption(new Option('--prefill <text>', 'Pre-fill the prompt input with text without submitting it').hideHelp()).addOption(new Option('--deep-link-origin', 'Signal that this session was launched from a deep link').hideHelp()).addOption(new Option('--deep-link-repo <slug>', 'Repo slug the deep link ?repo= parameter resolved to the current cwd').hideHelp()).addOption(new Option('--deep-link-last-fetch <ms>', 'FETCH_HEAD mtime in epoch ms, precomputed by the deep link trampoline').argParser(v => {
claude-code-source-code-main/src/main.tsx:991:  }).hideHelp()).option('--from-pr [value]', 'Resume a session linked to a PR by PR number/URL, or open interactive picker with optional search term', value => value || true).option('--no-session-persistence', 'Disable session persistence - sessions will not be saved to disk and cannot be resumed (only works with --print)').addOption(new Option('--resume-session-at <message id>', 'When resuming, only messages up to and including the assistant message with <message.id> (use with --resume in print mode)').argParser(String).hideHelp()).addOption(new Option('--rewind-files <user-message-id>', 'Restore files to state at the specified user message and exit (requires --resume)').hideHelp())
claude-code-source-code-main/src/main.tsx:993:  .option('--model <model>', `Model for the current session. Provide an alias for the latest model (e.g. 'sonnet' or 'opus') or a model's full name (e.g. 'claude-sonnet-4-6').`).addOption(new Option('--effort <level>', `Effort level for the current session (low, medium, high, max)`).argParser((rawValue: string) => {
claude-code-source-code-main/src/main.tsx:1000:  })).option('--agent <agent>', `Agent for the current session. Overrides the 'agent' setting.`).option('--betas <betas...>', 'Beta headers to include in API requests (API key users only)').option('--fallback-model <model>', 'Enable automatic fallback to specified model when default model is overloaded (only works with --print)').addOption(new Option('--workload <tag>', 'Workload tag for billing-header attribution (cc_workload). Process-scoped; set by SDK daemon callers that spawn subprocesses for cron work. (only works with --print)').hideHelp()).option('--settings <file-or-json>', 'Path to a settings JSON file or a JSON string to load additional settings from').option('--add-dir <directories...>', 'Additional directories to allow tool access to').option('--ide', 'Automatically connect to IDE on startup if exactly one valid IDE is available', () => true).option('--strict-mcp-config', 'Only use MCP servers from --mcp-config, ignoring all other MCP configurations', () => true).option('--session-id <uuid>', 'Use a specific session ID for the conversation (must be a valid UUID)').option('-n, --name <name>', 'Set a display name for this session (shown in /resume and terminal title)').option('--agents <json>', 'JSON object defining custom agents (e.g. \'{"reviewer": {"description": "Reviews code", "prompt": "You are a code reviewer"}}\')').option('--setting-sources <sources>', 'Comma-separated list of setting sources to load (user, project, local).')
claude-code-source-code-main/src/main.tsx:1006:  .option('--plugin-dir <path>', 'Load plugins from a directory for this session only (repeatable: --plugin-dir A --plugin-dir B)', (val: string, prev: string[]) => [...prev, val], [] as string[]).option('--disable-slash-commands', 'Disable all skills', () => true).option('--chrome', 'Enable Claude in Chrome integration').option('--no-chrome', 'Disable Claude in Chrome integration').option('--file <specs...>', 'File resources to download at startup. Format: file_id:relative_path (e.g., --file file_abc:doc.txt file_def:img.png)').action(async (prompt, options) => {
claude-code-source-code-main/src/main.tsx:1010:    // gates fire (CLAUDE.md, skills, hooks inside executeHooks, agent
claude-code-source-code-main/src/main.tsx:1035:    // mode is left to the user — settings defaultMode or --permission-mode
claude-code-source-code-main/src/main.tsx:1046:    // .claude/agents/assistant.md to the system prompt. Refuse to activate
claude-code-source-code-main/src/main.tsx:1060:    // isAssistantMode() is true for them too. --agent-id being set
claude-code-source-code-main/src/main.tsx:1065:      agentId?: unknown;
claude-code-source-code-main/src/main.tsx:1066:    }).agentId && kairosGate) {
claude-code-source-code-main/src/main.tsx:1099:      permissionMode: permissionModeCli,
claude-code-source-code-main/src/main.tsx:1104:      sessionId,
claude-code-source-code-main/src/main.tsx:1114:    const agentsJson = options.agents;
claude-code-source-code-main/src/main.tsx:1115:    const agentCli = options.agent;
claude-code-source-code-main/src/main.tsx:1116:    if (feature('BG_SESSIONS') && agentCli) {
claude-code-source-code-main/src/main.tsx:1117:      process.env.CLAUDE_CODE_AGENT = agentCli;
claude-code-source-code-main/src/main.tsx:1184:    // Extract teammate options (for tmux-spawned agents)
claude-code-source-code-main/src/main.tsx:1188:      // Extract agent identity options (for tmux-spawned agents)
claude-code-source-code-main/src/main.tsx:1194:      const hasAnyTeammateOpt = teammateOpts.agentId || teammateOpts.agentName || teammateOpts.teamName;
claude-code-source-code-main/src/main.tsx:1195:      const hasAllRequiredTeammateOpts = teammateOpts.agentId && teammateOpts.agentName && teammateOpts.teamName;
claude-code-source-code-main/src/main.tsx:1197:        process.stderr.write(chalk.red('Error: --agent-id, --agent-name, and --team-name must all be provided together\n'));
claude-code-source-code-main/src/main.tsx:1202:      if (teammateOpts.agentId && teammateOpts.agentName && teammateOpts.teamName) {
claude-code-source-code-main/src/main.tsx:1204:          agentId: teammateOpts.agentId,
claude-code-source-code-main/src/main.tsx:1205:          agentName: teammateOpts.agentName,
claude-code-source-code-main/src/main.tsx:1207:          color: teammateOpts.agentColor,
claude-code-source-code-main/src/main.tsx:1225:    // Allow env var to enable partial messages (used by sandbox gateway for baku)
claude-code-source-code-main/src/main.tsx:1265:    // Extract --remote-control / --rc flag (enable bridge in interactive session)
claude-code-source-code-main/src/main.tsx:1276:    // Validate session ID if provided
claude-code-source-code-main/src/main.tsx:1277:    if (sessionId) {
claude-code-source-code-main/src/main.tsx:1279:      // --session-id can be used with --continue or --resume when --fork-session is also provided
claude-code-source-code-main/src/main.tsx:1280:      // (to specify a custom ID for the forked session)
claude-code-source-code-main/src/main.tsx:1282:        process.stderr.write(chalk.red('Error: --session-id can only be used with --continue or --resume if --fork-session is also specified.\n'));
claude-code-source-code-main/src/main.tsx:1286:      // When --sdk-url is provided (bridge/remote mode), the session ID is a
claude-code-source-code-main/src/main.tsx:1287:      // server-assigned tagged ID (e.g. "session_local_01...") rather than a
claude-code-source-code-main/src/main.tsx:1290:        const validatedSessionId = validateUuid(sessionId);
claude-code-source-code-main/src/main.tsx:1292:          process.stderr.write(chalk.red('Error: Invalid session ID. Must be a valid UUID.\n'));
claude-code-source-code-main/src/main.tsx:1296:        // Check if session ID already exists
claude-code-source-code-main/src/main.tsx:1297:        if (sessionIdExists(validatedSessionId)) {
claude-code-source-code-main/src/main.tsx:1309:      // Get session ingress token (provided by EnvManager via CLAUDE_CODE_SESSION_ACCESS_TOKEN)
claude-code-source-code-main/src/main.tsx:1310:      const sessionToken = getSessionIngressAuthToken();
claude-code-source-code-main/src/main.tsx:1311:      if (!sessionToken) {
claude-code-source-code-main/src/main.tsx:1316:      // Resolve session ID: prefer remote session ID, fall back to internal session ID
claude-code-source-code-main/src/main.tsx:1321:        // This ensures consistency with session ingress API in all environments
claude-code-source-code-main/src/main.tsx:1324:          oauthToken: sessionToken,
claude-code-source-code-main/src/main.tsx:1325:          sessionId: fileSessionId
claude-code-source-code-main/src/main.tsx:1385:    if (isAgentSwarmsEnabled() && storedTeammateOpts?.agentId && storedTeammateOpts?.agentName && storedTeammateOpts?.teamName) {
claude-code-source-code-main/src/main.tsx:1390:      mode: permissionMode,
claude-code-source-code-main/src/main.tsx:1391:      notification: permissionModeNotification
claude-code-source-code-main/src/main.tsx:1393:      permissionModeCli,
claude-code-source-code-main/src/main.tsx:1397:    // Store session bypass permissions mode for trust dialog check
claude-code-source-code-main/src/main.tsx:1398:    setSessionBypassPermissionsMode(permissionMode === 'bypassPermissions');
claude-code-source-code-main/src/main.tsx:1400:      // autoModeFlagCli is the "did the user intend auto this session" signal.
claude-code-source-code-main/src/main.tsx:1401:      // Set when: --enable-auto-mode, --permission-mode auto, resolved mode
claude-code-source-code-main/src/main.tsx:1403:      // (permissionMode resolved to default with no explicit CLI override).
claude-code-source-code-main/src/main.tsx:1408:      }).enableAutoMode || permissionModeCli === 'auto' || permissionMode === 'auto' || !permissionModeCli && isDefaultPermissionModeAuto()) {
claude-code-source-code-main/src/main.tsx:1636:    // inbound push notifications should register this session. The option
claude-code-source-code-main/src/main.tsx:1722:    // SDK opt-in for SendUserMessage via --tools. All sessions require
claude-code-source-code-main/src/main.tsx:1751:      permissionMode,
claude-code-source-code-main/src/main.tsx:1764:      for (const permission of overlyBroadBashPermissions) {
claude-code-source-code-main/src/main.tsx:1765:        logForDebugging(`Ignoring overly broad shell permission ${permission.ruleDisplay} from ${permission.sourceDisplay}`);
claude-code-source-code-main/src/main.tsx:1855:    // Validate --no-session-persistence is only used with print mode
claude-code-source-code-main/src/main.tsx:1856:    if (options.sessionPersistence === false && !isNonInteractiveSession) {
claude-code-source-code-main/src/main.tsx:1857:      writeToStderr(`Error: --no-session-persistence can only be used with --print mode.`);
claude-code-source-code-main/src/main.tsx:1913:    // Parallelize setup() with commands+agents loading. setup()'s ~28ms is
claude-code-source-code-main/src/main.tsx:1917:    // commands/agents need the post-chdir cwd.
claude-code-source-code-main/src/main.tsx:1923:    if (process.env.CLAUDE_CODE_ENTRYPOINT !== 'local-agent') {
claude-code-source-code-main/src/main.tsx:1927:    const setupPromise = setup(preSetupCwd, permissionMode, allowDangerouslySkipPermissions, worktreeEnabled, worktreeName, tmuxEnabled, sessionId ? validateUuid(sessionId) : undefined, worktreePRNumber, messagingSocketPath);
claude-code-source-code-main/src/main.tsx:1929:    const agentDefsPromise = worktreeEnabled ? null : getAgentDefinitionsWithOverrides(preSetupCwd);
claude-code-source-code-main/src/main.tsx:1933:    agentDefsPromise?.catch(() => {});
claude-code-source-code-main/src/main.tsx:1993:    // session ID is finalized by --continue/--resume. materializeSessionFile
claude-code-source-code-main/src/main.tsx:1996:    const sessionNameArg = options.name?.trim();
claude-code-source-code-main/src/main.tsx:1997:    if (sessionNameArg) {
claude-code-source-code-main/src/main.tsx:1998:      cacheSessionTitle(sessionNameArg);
claude-code-source-code-main/src/main.tsx:2025:    logForDebugging('[STARTUP] Loading commands and agents...');
claude-code-source-code-main/src/main.tsx:2029:    const [commands, agentDefinitionsResult] = await Promise.all([commandsPromise ?? getCommands(currentCwd), agentDefsPromise ?? getAgentDefinitionsWithOverrides(currentCwd)]);
claude-code-source-code-main/src/main.tsx:2030:    logForDebugging(`[STARTUP] Commands and agents loaded in ${Date.now() - commandsStart}ms`);
claude-code-source-code-main/src/main.tsx:2033:    // Parse CLI agents if provided via --agents flag
claude-code-source-code-main/src/main.tsx:2034:    let cliAgents: typeof agentDefinitionsResult.activeAgents = [];
claude-code-source-code-main/src/main.tsx:2035:    if (agentsJson) {
claude-code-source-code-main/src/main.tsx:2037:        const parsedAgents = safeParseJSON(agentsJson);
claude-code-source-code-main/src/main.tsx:2046:    // Merge CLI agents with existing ones
claude-code-source-code-main/src/main.tsx:2047:    const allAgents = [...agentDefinitionsResult.allAgents, ...cliAgents];
claude-code-source-code-main/src/main.tsx:2048:    const agentDefinitions = {
claude-code-source-code-main/src/main.tsx:2049:      ...agentDefinitionsResult,
claude-code-source-code-main/src/main.tsx:2054:    // Look up main thread agent from CLI flag or settings
claude-code-source-code-main/src/main.tsx:2055:    const agentSetting = agentCli ?? getInitialSettings().agent;
claude-code-source-code-main/src/main.tsx:2056:    let mainThreadAgentDefinition: (typeof agentDefinitions.activeAgents)[number] | undefined;
claude-code-source-code-main/src/main.tsx:2057:    if (agentSetting) {
claude-code-source-code-main/src/main.tsx:2058:      mainThreadAgentDefinition = agentDefinitions.activeAgents.find(agent => agent.agentType === agentSetting);
claude-code-source-code-main/src/main.tsx:2060:        logForDebugging(`Warning: agent "${agentSetting}" not found. ` + `Available agents: ${agentDefinitions.activeAgents.map(a => a.agentType).join(', ')}. ` + `Using default behavior.`);
claude-code-source-code-main/src/main.tsx:2064:    // Store the main thread agent type in bootstrap state so hooks can access it
claude-code-source-code-main/src/main.tsx:2065:    setMainThreadAgentType(mainThreadAgentDefinition?.agentType);
claude-code-source-code-main/src/main.tsx:2067:    // Log agent flag usage — only log agent name for built-in agents to avoid leaking custom agent names
claude-code-source-code-main/src/main.tsx:2069:      logEvent('tengu_agent_flag', {
claude-code-source-code-main/src/main.tsx:2070:        agentType: isBuiltInAgent(mainThreadAgentDefinition) ? mainThreadAgentDefinition.agentType as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS : 'custom' as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS,
claude-code-source-code-main/src/main.tsx:2071:        ...(agentCli && {
claude-code-source-code-main/src/main.tsx:2077:    // Persist agent setting to session transcript for resume view display and restoration
claude-code-source-code-main/src/main.tsx:2078:    if (mainThreadAgentDefinition?.agentType) {
claude-code-source-code-main/src/main.tsx:2079:      saveAgentSetting(mainThreadAgentDefinition.agentType);
claude-code-source-code-main/src/main.tsx:2082:    // Apply the agent's system prompt for non-interactive sessions
claude-code-source-code-main/src/main.tsx:2085:      const agentSystemPrompt = mainThreadAgentDefinition.getSystemPrompt();
claude-code-source-code-main/src/main.tsx:2086:      if (agentSystemPrompt) {
claude-code-source-code-main/src/main.tsx:2087:        systemPrompt = agentSystemPrompt;
claude-code-source-code-main/src/main.tsx:2106:    // If user didn't specify a model but agent has one, use the agent's model
claude-code-source-code-main/src/main.tsx:2140:    // For tmux teammates with --agent-type, append the custom agent's prompt
claude-code-source-code-main/src/main.tsx:2141:    if (isAgentSwarmsEnabled() && storedTeammateOpts?.agentId && storedTeammateOpts?.agentName && storedTeammateOpts?.teamName && storedTeammateOpts?.agentType) {
claude-code-source-code-main/src/main.tsx:2142:      // Look up the custom agent definition
claude-code-source-code-main/src/main.tsx:2143:      const customAgent = agentDefinitions.activeAgents.find(a => a.agentType === storedTeammateOpts.agentType);
claude-code-source-code-main/src/main.tsx:2145:        // Get the prompt - need to handle both built-in and custom agents
claude-code-source-code-main/src/main.tsx:2148:          // Built-in agents have getSystemPrompt that takes toolUseContext
claude-code-source-code-main/src/main.tsx:2150:          logForDebugging(`[teammate] Built-in agent ${storedTeammateOpts.agentType} - skipping custom prompt (not supported)`);
claude-code-source-code-main/src/main.tsx:2152:          // Custom agents have getSystemPrompt that takes no args
claude-code-source-code-main/src/main.tsx:2156:        // Log agent memory loaded event for tmux teammates
claude-code-source-code-main/src/main.tsx:2158:          logEvent('tengu_agent_memory_loaded', {
claude-code-source-code-main/src/main.tsx:2160:              agent_type: customAgent.agentType as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS
claude-code-source-code-main/src/main.tsx:2171:        logForDebugging(`[teammate] Custom agent ${storedTeammateOpts.agentType} not found in available agents`);
claude-code-source-code-main/src/main.tsx:2177:    // defaultView is a display preference; SDK sessions have no display, and
claude-code-source-code-main/src/main.tsx:2179:    // which would otherwise leak into --print sessions in the same directory.
claude-code-source-code-main/src/main.tsx:2211:    // Ink root is only needed for interactive sessions — patchConsole in the
claude-code-source-code-main/src/main.tsx:2241:      const onboardingShown = await showSetupScreens(root, permissionMode, allowDangerouslySkipPermissions, commands, enableClaudeInChrome, devChannels);
claude-code-source-code-main/src/main.tsx:2257:      // Check for pending agent memory snapshot updates (only for --agent mode, ant-only)
claude-code-source-code-main/src/main.tsx:2259:        const agentDef = mainThreadAgentDefinition;
claude-code-source-code-main/src/main.tsx:2261:          agentType: agentDef.agentType,
claude-code-source-code-main/src/main.tsx:2262:          scope: agentDef.memory!,
claude-code-source-code-main/src/main.tsx:2263:          snapshotTimestamp: agentDef.pendingSnapshotUpdate!.snapshotTimestamp
claude-code-source-code-main/src/main.tsx:2268:          } = await import('./components/agents/SnapshotUpdateDialog.js');
claude-code-source-code-main/src/main.tsx:2269:          const mergePrompt = buildMergePrompt(agentDef.agentType, agentDef.memory!);
claude-code-source-code-main/src/main.tsx:2272:        agentDef.pendingSnapshotUpdate = undefined;
claude-code-source-code-main/src/main.tsx:2289:        // Both self-gate on tengu_sessions_elevated_auth_enforcement internally
claude-code-source-code-main/src/main.tsx:2438:      agentType: mainThreadAgentDefinition?.agentType,
claude-code-source-code-main/src/main.tsx:2512:      permissionMode,
claude-code-source-code-main/src/main.tsx:2513:      modeIsBypass: permissionMode === 'bypassPermissions',
claude-code-source-code-main/src/main.tsx:2526:    // Register PID file for concurrent-session detection (~/.claude/sessions/)
claude-code-source-code-main/src/main.tsx:2532:      if (sessionNameArg) {
claude-code-source-code-main/src/main.tsx:2533:        void updateSessionName(sessionNameArg);
claude-code-source-code-main/src/main.tsx:2537:          logEvent('tengu_concurrent_sessions', {
claude-code-source-code-main/src/main.tsx:2538:            num_sessions: count
claude-code-source-code-main/src/main.tsx:2550:    // can orphan this session's active version underneath us.
claude-code-source-code-main/src/main.tsx:2553:    // the next interactive session will reconcile. The await here was
claude-code-source-code-main/src/main.tsx:2564:      // that doesn't affect runtime behavior of the current session
claude-code-source-code-main/src/main.tsx:2605:      // set — those paths run setup hooks first (print.ts:544), and session
claude-code-source-code-main/src/main.tsx:2607:      const sessionStartHooksPromise = options.continue || options.resume || teleport || setupTrigger ? undefined : processSessionStartHooks('startup');
claude-code-source-code-main/src/main.tsx:2611:      sessionStartHooksPromise?.catch(() => {});
claude-code-source-code-main/src/main.tsx:2613:      // Validate org restriction for non-interactive sessions
claude-code-source-code-main/src/main.tsx:2645:        // overdue cron tasks on spawn = N serial subagent turns blocking
claude-code-source-code-main/src/main.tsx:2678:      // Set global state for session persistence
claude-code-source-code-main/src/main.tsx:2679:      if (options.sessionPersistence === false) {
claude-code-source-code-main/src/main.tsx:2815:      // that scripted calls don't need — the next interactive session reconciles.
claude-code-source-code-main/src/main.tsx:2829:      void runHeadless(inputPrompt, () => headlessStore.getState(), headlessStore.setState, commandsHeadless, tools, sdkMcpConfigs, agentDefinitions.activeAgents, {
claude-code-source-code-main/src/main.tsx:2835:        permissionPromptToolName: options.permissionPromptTool,
claude-code-source-code-main/src/main.tsx:2855:        agent: agentCli,
claude-code-source-code-main/src/main.tsx:2858:        sessionStartHooksPromise
claude-code-source-code-main/src/main.tsx:2869:      agent: agentSetting as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS
claude-code-source-code-main/src/main.tsx:2882:    if (permissionModeNotification) {
claude-code-source-code-main/src/main.tsx:2884:        key: 'permission-mode-notification',
claude-code-source-code-main/src/main.tsx:2885:        text: permissionModeNotification,
claude-code-source-code-main/src/main.tsx:2911:      mode: isAgentSwarmsEnabled() && getTeammateUtils().isPlanModeRequired() ? 'plan' as const : toolPermissionContext.mode
claude-code-source-code-main/src/main.tsx:2929:      agentNameRegistry: new Map(),
claude-code-source-code-main/src/main.tsx:2937:      coordinatorTaskIndex: -1,
claude-code-source-code-main/src/main.tsx:2941:      agent: mainThreadAgentDefinition?.agentType,
claude-code-source-code-main/src/main.tsx:2942:      agentDefinitions,
claude-code-source-code-main/src/main.tsx:2965:      remoteBackgroundTaskCount: 0,
claude-code-source-code-main/src/main.tsx:2987:      remoteAgentTaskSuggestions: [],
claude-code-source-code-main/src/main.tsx:2996:      sessionHooks: new Map(),
claude-code-source-code-main/src/main.tsx:3056:    // Set up per-turn session environment data uploader (ant-only build).
claude-code-source-code-main/src/main.tsx:3064:    const sessionUploaderPromise = "external" === 'ant' ? import('./utils/sessionDataUploader.js') : null;
claude-code-source-code-main/src/main.tsx:3066:    // Defer session uploader resolution to the onTurnComplete callback to avoid
claude-code-source-code-main/src/main.tsx:3068:    // The per-turn auth logic in sessionDataUploader.ts handles unauthenticated
claude-code-source-code-main/src/main.tsx:3069:    // state gracefully (re-checks each turn, so auth recovery mid-session works).
claude-code-source-code-main/src/main.tsx:3070:    const uploaderReady = sessionUploaderPromise ? sessionUploaderPromise.then(mod => mod.createSessionTurnUploader()).catch(() => null) : null;
claude-code-source-code-main/src/main.tsx:3071:    const sessionConfig = {
claude-code-source-code-main/src/main.tsx:3096:      agentDefinitions,
claude-code-source-code-main/src/main.tsx:3112:        const result = await loadConversationForResume(undefined /* sessionId */, undefined /* sourceFile */);
claude-code-source-code-main/src/main.tsx:3139:          ...sessionConfig,
claude-code-source-code-main/src/main.tsx:3144:          initialAgentName: loaded.agentName,
claude-code-source-code-main/src/main.tsx:3145:          initialAgentColor: loaded.agentColor
claude-code-source-code-main/src/main.tsx:3160:        const session = await createDirectConnectSession({
claude-code-source-code-main/src/main.tsx:3166:        if (session.workDir) {
claude-code-source-code-main/src/main.tsx:3167:          setOriginalCwd(session.workDir);
claude-code-source-code-main/src/main.tsx:3168:          setCwdState(session.workDir);
claude-code-source-code-main/src/main.tsx:3171:        directConnectConfig = session.config;
claude-code-source-code-main/src/main.tsx:3175:      const connectInfoMessage = createSystemMessage(`Connected to server at ${_pendingConnect.url}\nSession: ${directConnectConfig.sessionId}`, 'info');
claude-code-source-code-main/src/main.tsx:3207:          process.stderr.write('Starting local ssh-proxy test session...\n');
claude-code-source-code-main/src/main.tsx:3210:            permissionMode: _pendingSSH.permissionMode,
claude-code-source-code-main/src/main.tsx:3224:            permissionMode: _pendingSSH.permissionMode,
claude-code-source-code-main/src/main.tsx:3241:      const sshInfoMessage = createSystemMessage(_pendingSSH.local ? `Local ssh-proxy test session\ncwd: ${sshSession.remoteCwd}\nAuth: unix socket → local proxy` : `SSH session to ${_pendingSSH.host}\nRemote cwd: ${sshSession.remoteCwd}\nAuth: unix socket -R → local proxy`, 'info');
claude-code-source-code-main/src/main.tsx:3259:    } else if (feature('KAIROS') && _pendingAssistantChat && (_pendingAssistantChat.sessionId || _pendingAssistantChat.discover)) {
claude-code-source-code-main/src/main.tsx:3260:      // `claude assistant [sessionId]` — REPL as a pure viewer client
claude-code-source-code-main/src/main.tsx:3261:      // of a remote assistant session. The agentic loop runs remotely; this
claude-code-source-code-main/src/main.tsx:3266:      } = await import('./assistant/sessionDiscovery.js');
claude-code-source-code-main/src/main.tsx:3267:      let targetSessionId = _pendingAssistantChat.sessionId;
claude-code-source-code-main/src/main.tsx:3269:      // Discovery flow — list bridge environments, filter sessions
claude-code-source-code-main/src/main.tsx:3271:        let sessions;
claude-code-source-code-main/src/main.tsx:3273:          sessions = await discoverAssistantSessions();
claude-code-source-code-main/src/main.tsx:3275:          return await exitWithError(root, `Failed to discover sessions: ${e instanceof Error ? e.message : e}`, () => gracefulShutdown(1));
claude-code-source-code-main/src/main.tsx:3277:        if (sessions.length === 0) {
claude-code-source-code-main/src/main.tsx:3289:          // establish a bridge session before discovery will find it.
claude-code-source-code-main/src/main.tsx:3295:        if (sessions.length === 1) {
claude-code-source-code-main/src/main.tsx:3296:          targetSessionId = sessions[0]!.id;
claude-code-source-code-main/src/main.tsx:3299:            sessions
claude-code-source-code-main/src/main.tsx:3330:      const infoMessage = createSystemMessage(`Attached to assistant session ${targetSessionId.slice(0, 8)}…`, 'info');
claude-code-source-code-main/src/main.tsx:3356:      // Handle resume flow - from file (ant-only), session ID, or interactive selector
claude-code-source-code-main/src/main.tsx:3375:          // Show all sessions with linked PRs
claude-code-source-code-main/src/main.tsx:3401:      // --remote and --teleport both create/resume Claude Code Web (CCR) sessions.
claude-code-source-code-main/src/main.tsx:3405:        if (!isPolicyAllowed('allow_remote_sessions')) {
claude-code-source-code-main/src/main.tsx:3406:          return await exitWithError(root, "Error: Remote sessions are disabled by your organization's policy.", () => gracefulShutdown(1));
claude-code-source-code-main/src/main.tsx:3410:        // Create remote session (optionally with initial prompt)
claude-code-source-code-main/src/main.tsx:3418:        logEvent('tengu_remote_create_session', {
claude-code-source-code-main/src/main.tsx:3426:          logEvent('tengu_remote_create_session_error', {
claude-code-source-code-main/src/main.tsx:3427:            error: 'unable_to_create_session' as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS
claude-code-source-code-main/src/main.tsx:3429:          return await exitWithError(root, 'Error: Unable to create remote session', () => gracefulShutdown(1));
claude-code-source-code-main/src/main.tsx:3431:        logEvent('tengu_remote_create_session_success', {
claude-code-source-code-main/src/main.tsx:3432:          session_id: createdSession.id as AnalyticsMetadata_I_VERIFIED_THIS_IS_NOT_CODE_OR_FILEPATHS
claude-code-source-code-main/src/main.tsx:3437:          // Original behavior: print session info and exit
claude-code-source-code-main/src/main.tsx:3438:          process.stdout.write(`Created remote session: ${createdSession.title}\n`);
claude-code-source-code-main/src/main.tsx:3450:        // Get OAuth credentials for remote session
claude-code-source-code-main/src/main.tsx:3462:        // Create remote session config for the REPL
claude-code-source-code-main/src/main.tsx:3469:        // Add remote session info as initial system message
claude-code-source-code-main/src/main.tsx:3478:        // Set remote session URL in app state for footer indicator
claude-code-source-code-main/src/main.tsx:3508:          logForDebugging('selectAndResumeTeleportTask: Starting teleport flow...');
claude-code-source-code-main/src/main.tsx:3520:          logEvent('tengu_teleport_resume_session', {
claude-code-source-code-main/src/main.tsx:3524:            // First, fetch session and validate repository before checking git state
claude-code-source-code-main/src/main.tsx:3525:            const sessionData = await fetchSession(teleport);
claude-code-source-code-main/src/main.tsx:3526:            const repoValidation = await validateSessionRepository(sessionData);
claude-code-source-code-main/src/main.tsx:3530:              const sessionRepo = repoValidation.sessionRepo;
claude-code-source-code-main/src/main.tsx:3531:              if (sessionRepo) {
claude-code-source-code-main/src/main.tsx:3533:                const knownPaths = getKnownPathsForRepo(sessionRepo);
claude-code-source-code-main/src/main.tsx:3538:                    targetRepo: sessionRepo,
claude-code-source-code-main/src/main.tsx:3552:                  throw new TeleportOperationError(`You must run claude --teleport ${teleport} from a checkout of ${sessionRepo}.`, chalk.red(`You must run claude --teleport ${teleport} from a checkout of ${chalk.bold(sessionRepo)}.\n`));
claude-code-source-code-main/src/main.tsx:3556:              throw new TeleportOperationError(repoValidation.errorMessage || 'Failed to validate session', chalk.red(`Error: ${repoValidation.errorMessage || 'Failed to validate session'}\n`));
claude-code-source-code-main/src/main.tsx:3565:            // Track teleported session for reliability logging
claude-code-source-code-main/src/main.tsx:3567:              sessionId: teleport

## 4. Compare with current platform agent runtime
core-platform/services/agent_orchestrator/__init__.py
core-platform/services/agent_orchestrator/__pycache__/__init__.cpython-312.pyc
core-platform/services/agent_orchestrator/__pycache__/main.cpython-312.pyc
core-platform/services/agent_orchestrator/main.py
core-platform/services/agent_runtime_service/app/__init__.py
core-platform/services/agent_runtime_service/app/executor.py
core-platform/services/agent_runtime_service/app/models.py
core-platform/services/agent_runtime_service/app/planner.py
core-platform/services/agent_runtime_service/app/renderer.py
core-platform/services/agent_runtime_service/app/service.py
core-platform/services/agent_runtime_service/app/tools.py
core-platform/services/agent_runtime_service/app/validator.py
core-platform/services/agent_runtime_service/main.py

