// P3.14-D4-D3-C: robust message send handling for composer.

// Save original sendMessage if it exists
const __originalSendMessage = window.__originalSendMessage || window.sendMessage;

// Robust fallback send message
async function fallbackSendMessage() {
  const input = document.getElementById("prompt");
  if (!input) {
    console.error("[composer-fix] prompt input not found");
    return;
  }
  const text = input.value.trim();
  if (!text) return;

  input.value = "";
  userMessage(text);
  
  addRun({
    title: "P3 Runtime Task",
    status: "running",
    steps: [
      { text: "1. 接收任务", ok: true },
      { text: "2. 调用 Auto Router / Capability Learning" }
    ],
    log: "任务已进入 P3 执行链路..."
  });

  try {
    const route = await postJson(`${API.router}/route`, { prompt: text });
    patchLastRun({
      steps: [
        { text: "1. 接收任务", ok: true },
        { text: "2. 能力路由完成", ok: true },
        { text: "3. Runtime dry-run" }
      ],
      log: "ROUTE:\n" + JSON.stringify(route, null, 2)
    });
    const dry = await postJson(`${API.runtime}/execute`, {
      repo: route.task_type || "general",
      prompt: text,
      dry_run: true,
      metadata: { session_id: currentSession().id, shared_learning: true }
    });
    patchLastRun({
      status: dry.requires_review ? "review" : "done",
      steps: [
        { text: "1. 接收任务", ok: true },
        { text: "2. 能力路由完成", ok: true },
        { text: "3. Runtime dry-run 完成", ok: true },
        { text: dry.requires_review ? "4. 需要人工审核" : "4. 可安全继续", ok: !dry.requires_review, warn: !!dry.requires_review }
      ],
      trace_id: dry.trace_id,
      policy: dry.policy,
      log: "ROUTE:\n" + JSON.stringify(route, null, 2) + "\n\nRUNTIME:\n" + JSON.stringify(dry, null, 2)
    });
    if (dry.trace_id) document.getElementById("traceBox").textContent = dry.trace_id;
    if (dry.policy) document.getElementById("policyBox").textContent = JSON.stringify(dry.policy, null, 2);
    if (dry.requires_review) {
      currentReview = {
        prompt: text,
        route,
        dry,
        task_type: route.task_type || "general"
      };
      const lastRun = currentSession().runs.at(-1);
      currentReviewRunId = lastRun ? lastRun.id : null;
      document.getElementById("reviewJson").textContent = JSON.stringify(dry, null, 2);
      document.getElementById("reviewModal").classList.add("show");
    } else {
      await runRealExecution({
        prompt: text,
        route,
        dry,
        task_type: route.task_type || "general",
        run_id: currentSession().runs.at(-1)?.id
      });
    }
  } catch (e) {
    patchLastRun({
      status: "error",
      log: "ERROR: " + (e.message || String(e))
    });
  }
}

// Robust send message wrapper
async function robustSendMessage() {
  const original = window.__originalSendMessage || window.sendMessage;
  if (typeof original === "function") {
    try {
      await original();
      return;
    } catch (err) {
      console.warn("[composer-fix] original sendMessage failed, fallback", err);
    }
  }
  await fallbackSendMessage();
}

// Expose to global scope
window.robustSendMessage = robustSendMessage;
window.fallbackSendMessage = fallbackSendMessage;

// Also bind to submitTask for compatibility
if (!window.submitTask || typeof window.submitTask !== "function") {
  window.submitTask = robustSendMessage;
}
