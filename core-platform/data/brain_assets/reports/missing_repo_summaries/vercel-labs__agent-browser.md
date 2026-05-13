# Missing Repo Summary Source: vercel-labs/agent-browser

- URL: https://github.com/vercel-labs/agent-browser
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/vercel-labs__agent-browser
- Clone Status: cloned
- Language: Rust
- Stars: 32819
- Topics: 
- Description: Browser automation CLI for AI agents

## Extracted README / Docs / Examples



# FILE: README.md

# agent-browser

Browser automation CLI for AI agents. Fast native Rust CLI.

[![skills.sh](https://skills.sh/b/vercel-labs/agent-browser)](https://skills.sh/vercel-labs/agent-browser)

## Installation

### Global Installation (recommended)

Installs the native Rust binary:

```bash
npm install -g agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### Project Installation (local dependency)

For projects that want to pin the version in `package.json`:

```bash
npm install agent-browser
agent-browser install
```

Then use via `package.json` scripts or by invoking `agent-browser` directly.

### Homebrew (macOS)

```bash
brew install agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### Cargo (Rust)

```bash
cargo install agent-browser
agent-browser install  # Download Chrome from Chrome for Testing (first time only)
```

### From Source

```bash
git clone https://github.com/vercel-labs/agent-browser
cd agent-browser
pnpm install
pnpm build
pnpm build:native   # Requires Rust (https://rustup.rs)
pnpm link --global  # Makes agent-browser available globally
agent-browser install
```

### Linux Dependencies

On Linux, install system dependencies:

```bash
agent-browser install --with-deps
```

### Updating

Upgrade to the latest version:

```bash
agent-browser upgrade
```

Detects your installation method (npm, Homebrew, or Cargo) and runs the appropriate update command automatically.

### Requirements

- **Chrome** - Run `agent-browser install` to download Chrome from [Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) (Google's official automation channel). Existing Chrome, Brave, Playwright, and Puppeteer installations are detected automatically. No Playwright or Node.js required for the daemon.
- **Rust** - Only needed when building from source (see From Source above).

## Quick Start

```bash
agent-browser open example.com
agent-browser snapshot                    # Get accessibility tree with refs
agent-browser click @e2                   # Click by ref from snapshot
agent-browser fill @e3 "test@example.com" # Fill by ref
agent-browser get text @e1                # Get text by ref
agent-browser screenshot page.png
agent-browser close
```

### Traditional Selectors (also supported)

```bash
agent-browser click "#submit"
agent-browser fill "#email" "test@example.com"
agent-browser find role button click --name "Submit"
```

## Commands

### Core Commands

```bash
agent-browser open                    # Launch browser (no navigation); stays on about:blank
agent-browser open <url>              # Launch + navigate to URL (aliases: goto, navigate)
agent-browser click <sel>             # Click element (--new-tab to open in new tab)
agent-browser dblclick <sel>          # Double-click element
agent-browser focus <sel>             # Focus element
agent-browser type <sel> <text>       # Type into element
agent-browser fill <sel> <text>       # Clear and fill
agent-browser press <key>             # Press key (Enter, Tab, Control+a) (alias: key)
agent-browser keyboard type <text>    # Type with real keystrokes (no selector, current focus)
agent-browser keyboard inserttext <text>  # Insert text without key events (no selector)
agent-browser keydown <key>           # Hold key down
agent-browser keyup <key>             # Release key
agent-browser hover <sel>             # Hover element
agent-browser select <sel> <val>      # Select dropdown option
agent-browser check <sel>             # Check checkbox
agent-browser uncheck <sel>           # Uncheck checkbox
agent-browser scroll <dir> [px]       # Scroll (up/down/left/right, --selector <sel>)
agent-browser scrollintoview <sel>    # Scroll element into view (alias: scrollinto)
agent-browser drag <src> <tgt>        # Drag and drop
agent-browser upload <sel> <files>    # Upload files
agent-browser screenshot [path]       # Take screenshot (--full for full page, saves to a temporary directory if no path)
agent-browser screenshot --annotate   # Annotated screenshot with numbered element labels
agent-browser screenshot --screenshot-dir ./shots    # Save to custom directory
agent-browser screenshot --screenshot-format jpeg --screenshot-quality 80
agent-browser pdf <path>              # Save as PDF
agent-browser snapshot                # Accessibility tree with refs (best for AI)
agent-browser eval <js>               # Run JavaScript (-b for base64, --stdin for piped input)
agent-browser connect <port>          # Connect to browser via CDP
agent-browser stream enable [--port <port>]  # Start runtime WebSocket streaming
agent-browser stream status           # Show runtime streaming state and bound port
agent-browser stream disable          # Stop runtime WebSocket streaming
agent-browser close                   # Close browser (aliases: quit, exit)
agent-browser close --all             # Close all active sessions
agent-browser chat "<instruction>"    # AI chat: natural language browser control (single-shot)
agent-browser chat                    # AI chat: interactive REPL mode
```

### Get Info

```bash
agent-browser get text <sel>          # Get text content
agent-browser get html <sel>          # Get innerHTML
agent-browser get value <sel>         # Get input value
agent-browser get attr <sel> <attr>   # Get attribute
agent-browser get title               # Get page title
agent-browser get url                 # Get current URL
agent-browser get cdp-url             # Get CDP WebSocket URL (for DevTools, debugging)
agent-browser get count <sel>         # Count matching elements
agent-browser get box <sel>           # Get bounding box
agent-browser get styles <sel>        # Get computed styles
```

### Check State

```bash
agent-browser is visible <sel>        # Check if visible
agent-browser is enabled <sel>        # Check if enabled
agent-browser is checked <sel>        # Check if checked
```

### Find Elements (Semantic Locators)

```bash
agent-browser find role <role> <action> [value]       # By ARIA role
agent-browser find text <text> <action>               # By text content
agent-browser find label <label> <action> [value]     # By label
agent-browser find placeholder <ph> <action> [value]  # By placeholder
agent-browser find alt <text> <action>                # By alt text
agent-browser find title <text> <action>              # By title attr
agent-browser find testid <id> <action> [value]       # By data-testid
agent-browser find first <sel> <action> [value]       # First match
agent-browser find last <sel> <action> [value]        # Last match
agent-browser find nth <n> <sel> <action> [value]     # Nth match
```

**Actions:** `click`, `fill`, `type`, `hover`, `focus`, `check`, `uncheck`, `text`

**Options:** `--name <name>` (filter role by accessible name), `--exact` (require exact text match)

**Examples:**

```bash
agent-browser find role button click --name "Submit"
agent-browser find text "Sign In" click
agent-browser find label "Email" fill "test@test.com"
agent-browser find first ".item" click
agent-browser find nth 2 "a" text
```

### Wait

```bash
agent-browser wait <selector>         # Wait for element to be visible
agent-browser wait <ms>               # Wait for time (milliseconds)
agent-browser wait --text "Welcome"   # Wait for text to appear (substring match)
agent-browser wait --url "**/dash"    # Wait for URL pattern
agent-browser wait --load networkidle # Wait for load state
agent-browser wait --fn "window.ready === true"  # Wait for JS condition

# Wait for text/element to disappear
agent-browser wait --fn "!document.body.innerText.includes('Loading...')"
agent-browser wait "#spinner" --state hidden
```

**Load states:** `load`, `domcontentloaded`, `networkidle`

### Batch Execution

Execute multiple commands in a single invocation. Commands can be passed as
quoted arguments or piped as JSON via stdin. This avoids per-command process
startup overhead when running multi-step workflows.

```bash
# Argument mode: each quoted argument is a full command
agent-browser batch "open https://example.com" "snapshot -i" "screenshot"

# With --bail to stop on first error
agent-browser batch --bail "open https://example.com" "click @e1" "screenshot"

# Stdin mode: pipe commands as JSON
echo '[
  ["open", "https://example.com"],
  ["snapshot", "-i"],
  ["click", "@e1"],
  ["screenshot", "result.png"]
]' | agent-browser batch --json
```

### Clipboard

```bash
agent-browser clipboard read                      # Read text from clipboard
agent-browser clipboard write "Hello, World!"     # Write text to clipboard
agent-browser clipboard copy                      # Copy current selection (Ctrl+C)
agent-browser clipboard paste                     # Paste from clipboard (Ctrl+V)
```

### Mouse Control

```bash
agent-browser mouse move <x> <y>      # Move mouse
agent-browser mouse down [button]     # Press button (left/right/middle)
agent-browser mouse up [button]       # Release button
agent-browser mouse wheel <dy> [dx]   # Scroll wheel
```

### Browser Settings

```bash
agent-browser set viewport <w> <h> [scale]  # Set viewport size (scale for retina, e.g. 2)
agent-browser set device <name>       # Emulate device ("iPhone 14")
agent-browser set geo <lat> <lng>     # Set geolocation
agent-browser set offline [on|off]    # Toggle offline mode
agent-browser set headers <json>      # Extra HTTP headers
agent-browser set credentials <u> <p> # HTTP basic auth
agent-browser set media [dark|light]  # Emulate color scheme
```

### Cookies & Storage

```bash
agent-browser cookies                 # Get all cookies
agent-browser cookies set <name> <val> # Set cookie
agent-browser cookies set --curl <file> # Import cookies from a Copy-as-cURL dump,
                                        # JSON array, or bare Cookie header (auto-detected)
agent-browser cookies clear           # Clear cookies

agent-browser storage local           # Get all localStorage
agent-browser s

# FILE: examples/environments/pnpm-lock.yaml

lockfileVersion: '9.0'

settings:
  autoInstallPeers: true
  excludeLinksFromLockfile: false

importers:

  .:
    dependencies:
      '@base-ui/react':
        specifier: ^1.2.0
        version: 1.2.0(@types/react@19.2.14)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      '@tailwindcss/postcss':
        specifier: ^4.2.1
        version: 4.2.1
      '@upstash/ratelimit':
        specifier: ^2.0.8
        version: 2.0.8(@upstash/redis@1.36.4)
      '@upstash/redis':
        specifier: ^1.36.4
        version: 1.36.4
      '@vercel/sandbox':
        specifier: ^1.0.0
        version: 1.8.0
      class-variance-authority:
        specifier: ^0.7.1
        version: 0.7.1
      clsx:
        specifier: ^2.1.1
        version: 2.1.1
      dotenv:
        specifier: ^17.3.1
        version: 17.3.1
      geist:
        specifier: ^1.7.0
        version: 1.7.0(next@16.1.6(@babel/core@7.29.0)(react-dom@19.2.4(react@19.2.4))(react@19.2.4))
      lucide-react:
        specifier: ^0.577.0
        version: 0.577.0(react@19.2.4)
      next:
        specifier: ^16.1.6
        version: 16.1.6(@babel/core@7.29.0)(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      postcss:
        specifier: ^8.5.8
        version: 8.5.8
      react:
        specifier: ^19.2.4
        version: 19.2.4
      react-dom:
        specifier: ^19.2.4
        version: 19.2.4(react@19.2.4)
      react-resizable-panels:
        specifier: ^4.7.2
        version: 4.7.2(react-dom@19.2.4(react@19.2.4))(react@19.2.4)
      shadcn:
        specifier: ^4.0.2
        version: 4.0.2(@types/node@22.19.15)(typescript@5.9.3)
      tailwind-merge:
        specifier: ^3.5.0
        version: 3.5.0
      tailwindcss:
        specifier: ^4.2.1
        version: 4.2.1
      tw-animate-css:
        specifier: ^1.4.0
        version: 1.4.0
    devDependencies:
      '@types/node':
        specifier: ^22.0.0
        version: 22.19.15
      '@types/react':
        specifier: ^19.2.14
        version: 19.2.14
      '@types/react-dom':
        specifier: ^19.2.3
        version: 19.2.3(@types/react@19.2.14)
      typescript:
        specifier: ^5.6.0
        version: 5.9.3

packages:

  '@alloc/quick-lru@5.2.0':
    resolution: {integrity: sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==}
    engines: {node: '>=10'}

  '@antfu/ni@25.0.0':
    resolution: {integrity: sha512-9q/yCljni37pkMr4sPrI3G4jqdIk074+iukc5aFJl7kmDCCsiJrbZ6zKxnES1Gwg+i9RcDZwvktl23puGslmvA==}
    hasBin: true

  '@babel/code-frame@7.29.0':
    resolution: {integrity: sha512-9NhCeYjq9+3uxgdtp20LSiJXJvN0FeCtNGpJxuMFZ1Kv3cWUNb6DOhJwUvcVCzKGR66cw4njwM6hrJLqgOwbcw==}
    engines: {node: '>=6.9.0'}

  '@babel/compat-data@7.29.0':
    resolution: {integrity: sha512-T1NCJqT/j9+cn8fvkt7jtwbLBfLC/1y1c7NtCeXFRgzGTsafi68MRv8yzkYSapBnFA6L3U2VSc02ciDzoAJhJg==}
    engines: {node: '>=6.9.0'}

  '@babel/core@7.29.0':
    resolution: {integrity: sha512-CGOfOJqWjg2qW/Mb6zNsDm+u5vFQ8DxXfbM09z69p5Z6+mE1ikP2jUXw+j42P

# FILE: examples/environments/README.md

# agent-browser Environments

A demo of agent-browser running in a Vercel Sandbox. Pick a URL, take a screenshot or accessibility snapshot, and watch each command execute in real time.

## How It Works

The app runs agent-browser + Chrome inside an ephemeral Vercel Sandbox microVM. A Linux VM spins up on demand, executes agent-browser commands, and shuts down. No binary size limits, no Chromium bundling complexity.

The UI streams progress via Server-Sent Events so you can see each step as it runs (sandbox creation, browser startup, navigation, screenshot/snapshot, cleanup).

## Getting Started

```bash
cd examples/environments
pnpm install
pnpm dev
```

For local development, set `VERCEL_TOKEN`, `VERCEL_TEAM_ID`, and `VERCEL_PROJECT_ID` in `.env.local` so the Sandbox SDK can authenticate.

## Sandbox Snapshots

Without optimization, each Sandbox run installs system dependencies + agent-browser + Chromium from scratch (~30s). A **sandbox snapshot** is a saved VM image with everything pre-installed -- the sandbox boots from the image instead of installing, bringing startup down to sub-second. (This is unrelated to agent-browser's *accessibility snapshot* feature, which dumps a page's accessibility tree.)

Create a sandbox snapshot by running the helper script once:

```bash
npx tsx scripts/create-snapshot.ts
# Output: AGENT_BROWSER_SNAPSHOT_ID=snap_xxxxxxxxxxxx
```

Add the ID to your Vercel project environment variables or `.env.local`. Recommended for production.

## Environment Variables

| Variable | Description |
|---|---|
| `AGENT_BROWSER_SNAPSHOT_ID` | Sandbox snapshot ID for sub-second startup (see above) |
| `VERCEL_TOKEN` | Vercel personal access token (for local dev; OIDC is automatic on Vercel) |
| `VERCEL_TEAM_ID` | Vercel team ID (for local dev) |
| `VERCEL_PROJECT_ID` | Vercel project ID (for local dev) |
| `KV_REST_API_URL` | Upstash Redis URL for rate limiting (optional) |
| `KV_REST_API_TOKEN` | Upstash Redis token for rate limiting (optional) |
| `RATE_LIMIT_PER_MINUTE` | Max requests per minute per IP (default: 10) |
| `RATE_LIMIT_PER_DAY` | Max requests per day per IP (default: 100) |

## Project Structure

```
examples/environments/
  app/
    page.tsx                  # Demo UI with streaming progress
    actions/browse.ts         # Server action (env status check)
    api/browse/route.ts       # Streaming SSE endpoint
  lib/
    agent-browser-sandbox.ts  # Vercel Sandbox client with progress callbacks
    constants.ts              # Allowed URLs
    rate-limit.ts             # Upstash rate limiting
  scripts/
    create-snapshot.ts        # Create sandbox snapshot
```


# FILE: examples/environments/package.json

{
  "name": "agent-browser-environments",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@base-ui/react": "^1.2.0",
    "@tailwindcss/postcss": "^4.2.1",
    "@upstash/ratelimit": "^2.0.8",
    "@upstash/redis": "^1.36.4",
    "@vercel/sandbox": "^1.0.0",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "dotenv": "^17.3.1",
    "geist": "^1.7.0",
    "lucide-react": "^0.577.0",
    "next": "^16.1.6",
    "postcss": "^8.5.8",
    "react": "^19.2.4",
    "react-dom": "^19.2.4",
    "react-resizable-panels": "^4.7.2",
    "shadcn": "^4.0.2",
    "tailwind-merge": "^3.5.0",
    "tailwindcss": "^4.2.1",
    "tw-animate-css": "^1.4.0"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "typescript": "^5.6.0"
  }
}


# FILE: examples/environments/components.json

{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "base-nova",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "",
    "css": "app/globals.css",
    "baseColor": "neutral",
    "cssVariables": true,
    "prefix": ""
  },
  "iconLibrary": "lucide",
  "rtl": false,
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui",
    "lib": "@/lib",
    "hooks": "@/hooks"
  },
  "menuColor": "default",
  "menuAccent": "subtle",
  "registries": {}
}


# FILE: examples/environments/tsconfig.json

{
  "compilerOptions": {
    "target": "ES2017",
    "lib": [
      "dom",
      "dom.iterable",
      "esnext"
    ],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": [
        "./*"
      ]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts"
  ],
  "exclude": [
    "node_modules",
    "server"
  ]
}


# FILE: examples/environments/next.config.ts

import type { NextConfig } from "next";

const nextConfig: NextConfig = {};

export default nextConfig;


# FILE: examples/environments/scripts/create-snapshot.ts

/**
 * Create a Vercel Sandbox snapshot with agent-browser + Chromium pre-installed.
 *
 * Run once:   npx tsx scripts/create-snapshot.ts
 * Then set:   AGENT_BROWSER_SNAPSHOT_ID=<output id>
 *
 * Authentication (one of):
 *   - VERCEL_TOKEN + VERCEL_TEAM_ID + VERCEL_PROJECT_ID
 *   - VERCEL_OIDC_TOKEN (automatically available on Vercel deployments)
 *
 * This makes sandbox creation sub-second instead of ~30s.
 */

import "dotenv/config";
import { createSnapshot, getSandboxCredentials } from "../lib/agent-browser-sandbox";

const hasExplicitCreds = !!(
  process.env.VERCEL_TOKEN &&
  process.env.VERCEL_TEAM_ID &&
  process.env.VERCEL_PROJECT_ID
);
const hasOidc = !!process.env.VERCEL_OIDC_TOKEN;

if (!hasExplicitCreds && !hasOidc) {
  console.error(
    "Missing sandbox credentials. Provide either:\n" +
      "  1. VERCEL_TOKEN + VERCEL_TEAM_ID + VERCEL_PROJECT_ID\n" +
      "  2. VERCEL_OIDC_TOKEN",
  );
  process.exit(1);
}

const creds = getSandboxCredentials();
console.log(
  creds.token
    ? `Authenticating with explicit credentials (team: ${creds.teamId})`
    : "Authenticating via VERCEL_OIDC_TOKEN",
);

async function main() {
  console.log("Creating Vercel Sandbox with agent-browser + Chromium...");
  console.log("This takes ~30-60 seconds on first run.\n");

  const snapshotId = await createSnapshot();

  console.log("\nSnapshot created successfully!");
  console.log(`\n  AGENT_BROWSER_SNAPSHOT_ID=${snapshotId}\n`);
  console.log("Add this to your .env.local or Vercel environment variables.");
}

main().catch((err) => {
  console.error("Failed to create snapshot:", err.message || err);
  process.exit(1);
});


# FILE: examples/environments/lib/agent-browser-sandbox.ts

/**
 * Run agent-browser inside a Vercel Sandbox.
 *
 * No external server needed -- a Linux microVM spins up on demand,
 * runs agent-browser + headless Chrome, and shuts down when done.
 *
 * For production, create a snapshot with agent-browser and Chromium
 * pre-installed so startup is sub-second instead of ~30s.
 */

import { Sandbox } from "@vercel/sandbox";

export type SandboxResult = {
  exitCode: number;
  stdout: string;
  stderr: string;
};

export type StepEvent = {
  step: string;
  status: "running" | "done" | "error";
  elapsed?: number;
};

export type OnStep = (event: StepEvent) => void;

const SNAPSHOT_ID = process.env.AGENT_BROWSER_SNAPSHOT_ID;

const CHROMIUM_SYSTEM_DEPS = [
  "nss",
  "nspr",
  "libxkbcommon",
  "atk",
  "at-spi2-atk",
  "at-spi2-core",
  "libXcomposite",
  "libXdamage",
  "libXrandr",
  "libXfixes",
  "libXcursor",
  "libXi",
  "libXtst",
  "libXScrnSaver",
  "libXext",
  "mesa-libgbm",
  "libdrm",
  "mesa-libGL",
  "mesa-libEGL",
  "cups-libs",
  "alsa-lib",
  "pango",
  "cairo",
  "gtk3",
  "dbus-libs",
];

/**
 * Returns credentials to spread into Sandbox.create() calls.
 * When explicit env vars are set they take precedence; otherwise returns
 * an empty object so the SDK falls back to VERCEL_OIDC_TOKEN automatically.
 */
export function getSandboxCredentials():
  | { token: string; teamId: string; projectId: string }
  | Record<string, never> {
  if (
    process.env.VERCEL_TOKEN &&
    process.env.VERCEL_TEAM_ID &&
    process.env.VERCEL_PROJECT_ID
  ) {
    return {
      token: process.env.VERCEL_TOKEN,
      teamId: process.env.VERCEL_TEAM_ID,
      projectId: process.env.VERCEL_PROJECT_ID,
    };
  }
  return {};
}

async function runStep<T>(
  step: string,
  fn: () => Promise<T>,
  onStep?: OnStep,
): Promise<T> {
  const start = Date.now();
  onStep?.({ step, status: "running" });
  try {
    const result = await fn();
    onStep?.({ step, status: "done", elapsed: Date.now() - start });
    return result;
  } catch (err) {
    onStep?.({ step, status: "error", elapsed: Date.now() - start });
    throw err;
  }
}

/**
 * Install system dependencies + agent-browser + Chromium into a fresh sandbox.
 * The sandbox base image is Amazon Linux (dnf).
 */
async function bootstrapSandbox(
  sandbox: InstanceType<typeof Sandbox>,
  onStep?: OnStep,
): Promise<void> {
  await runStep("Installing system dependencies", async () => {
    await sandbox.runCommand("sh", [
      "-c",
      `sudo dnf clean all 2>&1 && sudo dnf install -y --skip-broken ${CHROMIUM_SYSTEM_DEPS.join(" ")} 2>&1 && sudo ldconfig 2>&1`,
    ]);
  }, onStep);

  await runStep("Installing agent-browser", async () => {
    await sandbox.runCommand("npm", ["install", "-g", "agent-browser"]);
    await sandbox.runCommand("npx", ["agent-browser", "install"]);
  }, onStep);
}

async function createSandbox(
  onStep?: OnStep,
): Promise<InstanceType<typeof Sandbox>> {
  const credentials = getSandboxCredentials();

  return runStep(
    SNAPS
