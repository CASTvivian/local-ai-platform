// P3.14-D3-X3-B extracted state module
const STATE_KEY = "maomiai:desktop:v01";
let currentView = "chat";
let currentReviewRunId = null;
let artifactPageItems = [];
let selectedArtifactId = null;
let skillPageItems = [];
let selectedSkillId = null;
let workflowPageItems = [];
let selectedWorkflowId = null;

let sessions = [];
let currentSessionId = null;

function saveState() {
  localStorage.setItem("maomiai:desktop:v01", JSON.stringify(state));
}

function loadState() {
  const raw = localStorage.getItem("maomiai:desktop:v01");
  if (raw) return JSON.parse(raw);
  const first = {
    id: "session_" + Date.now(),
    title: "New Chat",
    messages: [],
    runs: [],
    createdAt: Date.now()
  };
  return { current: first.id, sessions: [first], settings: { autoApprove: false } };
}

function currentSession() {
  return state.sessions.find(x => x.id === state.current) || state.sessions[0];
}
