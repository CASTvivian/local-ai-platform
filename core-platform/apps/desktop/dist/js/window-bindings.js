// P3.14-D4-D3: expose functions used by inline onclick handlers.
(function bindDesktopGlobals() {
  const names = [
    // core
    "setView",
    "switchInspector",
    "sendMessage",
    "refreshHealth",
    "refreshServices",
    "previewText",
    "previewArtifact",
    "runEval",
    // artifacts
    "loadArtifacts",
    "loadArtifactsPage",
    "selectArtifact",
    "changeArtifactLifecycle",
    // skills
    "loadSkills",
    "loadSkillsPage",
    "parseSkillMd",
    "installSkillMd",
    "enableSkill",
    "disableSkill",
    "selectSkill",
    // workflows
    "loadWorkflows",
    "loadWorkflowsPage",
    "validateWorkflowJson",
    "registerWorkflowJson",
    "importWorkflowJson",
    "dryRunWorkflow",
    "exportWorkflow",
    "registerWorkflow",
    "selectWorkflow",
    // documents
    "ingestDocument",
    "loadRecentDocuments",
    "showCachedDoc",
    "clearDocInput",
    // repo memory
    "registerRepoMemory",
    "selectRepoMemory",
    "loadRepoFixes",
    "recordRepoFix",
    "saveRepoSnapshot",
    "compressRepoContext",
    "addRepoKnowledge",
    "searchRepoKnowledge",
    // code review
    "reviewCodeDiff",
    "loadCodeReviewRules",
    "loadCodeReviewSummary",
    "sendCodeReviewToPreview",
    // design system
    "parseDesignMd",
    "registerDesignSystem",
    "selectDesignSystem",
    "exportDesignSystem",
    "suggestDesignUi",
    "sendDesignSuggestionToPreview",
    "clearDesignMd",
    // models
    "selectDeviceProfile",
    "renderModelCards",
    "requestModelDownload",
    // launcher
    "previewLauncherCommands"
  ];
  for (const name of names) {
    try {
      if (typeof window[name] === "undefined" && typeof globalThis[name] === "function") {
        window[name] = globalThis[name];
      }
    } catch (_) {}
  }
  // Compatibility aliases
  if (typeof window.refreshServices === "undefined" && typeof window.refreshHealth === "function") {
    window.refreshServices = window.refreshHealth;
  }
})();
