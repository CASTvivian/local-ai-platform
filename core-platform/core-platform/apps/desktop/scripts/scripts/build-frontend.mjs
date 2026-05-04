import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const src = path.join(root, "src");
const dist = path.join(root, "dist");

const denyNames = new Set([
  "data",
  "logs",
  "references",
  "services",
  "scripts",
  "docs",
  "archive",
  "quarantine",
  "node_modules",
]);

function rmrf(p) {
  if (fs.existsSync(p)) {
    fs.rmSync(p, { recursive: true, force: true });
  }
}

function copyDir(from, to) {
  fs.mkdirSync(to, { recursive: true });
  for (const entry of fs.readdirSync(from, { withFileTypes: true })) {
    if (entry.name === ".DS_Store") continue;
    if (entry.name.endsWith(".bak")) continue;
    if (denyNames.has(entry.name)) continue;
    const a = path.join(from, entry.name);
    const b = path.join(to, entry.name);
    if (entry.isDirectory()) {
      copyDir(a, b);
    } else if (entry.isFile()) {
      fs.copyFileSync(a, b);
    }
  }
}

if (!fs.existsSync(path.join(src, "index.html"))) {
  console.error("missing src/index.html");
  process.exit(1);
}

rmrf(dist);
copyDir(src, dist);
console.log("frontend built:", dist);
