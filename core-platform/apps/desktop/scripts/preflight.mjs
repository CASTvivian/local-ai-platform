import fs from "node:fs";
import path from "node:path";

const root = process.cwd();

const required = [
  "src/index.html",
  "src/styles/main.css",
  "src/js/api.js",
  "src/js/services.js",
  "src/js/state.js",
  "src/js/inspector.js",
  "src/js/pages/artifacts.js",
  "src/js/pages/skills.js",
  "src/js/pages/workflows.js",
  "src/js/pages/repo-memory.js",
  "src/js/pages/code-review.js",
  "src/js/pages/design-system.js",
  "src/js/pages/models.js",
  "src-tauri/tauri.conf.json",
  "src-tauri/Cargo.toml",
];

let fail = 0;
for (const rel of required) {
  const p = path.join(root, rel);
  if (fs.existsSync(p)) {
    console.log("OK", rel);
  } else {
    console.error("MISSING", rel);
    fail++;
  }
}

const forbidden = [
  "src/index.html.bak",
  "src/data",
  "src/logs",
  "src/references",
  "src/services",
  "src/scripts",
  "src/docs",
  "bundle/backend/services",
  "bundle/backend/data",
  "bundle/backend/logs",
  "bundle/backend/references",
];

for (const rel of forbidden) {
  const p = path.join(root, rel);
  if (fs.existsSync(p)) {
    console.error("FORBIDDEN", rel);
    fail++;
  }
}

if (fail) {
  console.error("desktop preflight failed:", fail);
  process.exit(1);
}

console.log("desktop preflight PASS");
