# Missing Repo Summary Source: appcypher/awesome-mcp-servers

- URL: https://github.com/appcypher/awesome-mcp-servers
- Local Path: core-platform/data/brain_assets/repos/github_stars_missing/appcypher__awesome-mcp-servers
- Clone Status: cloned
- Language: None
- Stars: 5532
- Topics: ai, anthropic-claude, awesome, context, mcp, model-context-protocol, servers, tool-use, tools
- Description: Awesome MCP Servers - A curated list of Model Context Protocol servers

## Extracted README / Docs / Examples



# FILE: README.md

# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

A curated list of awesome Model Context Protocol (MCP) servers. MCP is an open protocol that enables AI models to securely interact with local and remote resources through standardized server implementations. This list focuses on production-ready and experimental MCP servers that extend AI capabilities through file access, database connections, API integrations, and other contextual services.

<br />

## ⚠️ Security Warning

> [!WARNING]
>  When running MCP servers without proper sandboxing, they can execute arbitrary code on your system with the same permissions as the host process. This creates significant security risks.
>
> **Security Risks:**
> - **System Access**: Full access to files, network, and system resources
> - **Code Execution**: Can run any command on your machine
> - **Prompt Injection**: Malicious prompts could trigger unintended server actions
> - **Data Exposure**: Sensitive data may be accessed or leaked
>
> **Best Practices:**
> - Use official implementations (marked with ⭐) when available
> - Run servers in VMs or isolated environments
> - Review code before installation
> - Limit permissions to minimum required
> - Monitor server activity

<br />

## Examples of Supported Clients

|                                                                                                                                                                                          | MCP Host                                                                    | Documentation                                                                                       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| [<div align="center"><img src="https://github.com/user-attachments/assets/b0ea1e57-df16-4b04-9276-1980e17ab6ec" height="20"/></div>](https://www.claudedesktop.com/)                                                                       | [Claude Desktop](https://claude.ai)                            | [Claude x MCP](https://modelcontextprotocol.io/quickstart)                                           |
| [<div align="center"><img src="https://zed.dev/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Flogo_icon.d67dc948.webp&w=64&q=100" height="20"/></div>](https://zed.dev/)                                                          | [Zed Editor](https://zed.dev/)                                              | [Zed x MCP](https://zed.dev/blog/mcp)                                                      |
| [<div align="center"><img src="https://storage.googleapis.com/sourcegraph-assets/docs/images/cody/cody-logomark-default.svg" height="20"/></div>](https://sourcegraph.com/cody)          | [Sourcegraph Cody](https://sourcegraph.com/cody)                            | [Cody x MCP](https://sourcegraph.com/blog/cody-supports-anthropic-model-context-protocol) |
| [<div align="center"><img src="https://cdn.prod.website-files.com/663e06c56841363663ffbbcf/664c918ec47bacdd3acdc167_favicon%408x.png" height="20"/></div>](https://sourcegraph.com/cody) | [Continue](https://www.continue.dev/)                                       | [Continue x MCP](https://blog.continue.dev/model-context-protocol)                                  |
| [<div align="center"><img src="https://github.com/user-attachments/assets/211d0c2b-04de-471e-b1ed-97da94a58d82" height="20"/></div>](https://github.com/Upsonic/gpt-computer-assistant)  | [GPT Computer Assistant](https://github.com/Upsonic/gpt-computer-assistant) | [GCA x MCP](https://github.com/Upsonic/gpt-computer-assistant)                                      |
| [<div align="center"><img src="https://raw.githubusercontent.com/danny-avila/LibreChat/0855677a36d76cafa5e064b7e346eb3f74c6af2a/client/public/assets/logo.svg" height="20"/></div>](https://www.librechat.ai/) | [LibreChat](https://www.librechat.ai/) | [LibreChat Agents x MCP](https://www.librechat.ai/docs/features/agents#model-context-protocol-mcp) |
| [<div align="center"><img src="https://cursor.com/favicon.ico" height="20"/></div>](https://www.cursor.com/) | [Cursor](https://www.cursor.com/) | [Cursor x MCP](https://docs.cursor.com/advanced/model-context-protocol) |
| [<div align="center"><img src="https://www.enconvo.com/favicon.ico" height="20"/></div>](https://www.enconvo.com/) | [Enconvo](https://www.enconvo.com/) | [Enconvo x MCP](https://docs.enconvo.com/docs/features/model-context-protocol) |
| [<div align="center"><img src="https://block.github.io/goose/img/logo_light.png" height="20"/></div>](https://block.github.io/goose/) | [Goose](https://block.github.io/goose/) | [Goose x MCP](https://block.github.io/goose/docs/getting-started/using-extensions) | 
| [<div align="center"><img src="https://raw.githubusercontent.com/evilsocket/search/refs/heads/main/logo.png" height="20"/></div>](https://github.com/evilsocket/nerve) | [Nerve](https://github.com/evilsocket/nerve) | [Nerve x MCP](https://github.com/evilsocket/nerve/blob/main/docs/index.md#%EF%B8%8F-adding-tools) | 
| [<div align="center"><img src="https://raw.githubusercontent.com/mcp-router/mcp-router/refs/heads/main/static/img/logo.svg" height="20"/></div>](https://mcp-router.net) | [MCP Router](https://github.com/mcp-router/mcp-router) | [MCP Router x MCP](https://mcp-router.net) |
| [<div align="center"><img src="https://raw.githubusercontent.com/pietrozullo/mcp-use/refs/heads/main/docs/favicon.svg" height="20"/></div>](https://github.com/pietrozullo/mcp-use) | [mcp-use](https://github.com/pietrozullo/mcp-use) | [mcp-use x MCP](https://docs.mcp-use.io/introduction) |
| [<div align="center"><img src="https://wassist.app/whatsmcp.png" height="20"/></div>](https://wassist.app/mcp/) | [WhatsMCP](https://wassist.app/mcp/) | [WhatsApp x MCP](https://wassist.app/mcp/) |
| [<div align="center"><img src="https://github.com/user-attachments/assets/7d5442e5-4542-4942-afde-a55d5288a40c" height="20"/></div>](https://code.visualstudio.com/) | [Visual Studio Code](https://code.visualstudio.com/) | [VS Code x MCP](https://code.visualstudio.com/docs/copilot/chat/mcp-servers) |


<br />

## Server Implementations

- 📂 - [File Systems](#file-systems)
- 📦 - [Sandbox & Virtualization](#virtualization)
- 🔄 - [Version Control](#version-control)
- ☁️ - [Cloud Storage](#cloud-storage)
- 🗒️ - [Document Processing](#document-processing)
- 🗄️ - [Databases](#databases)
- 💬 - [Communication](#communication)
- 📈 - [Monitoring](#monitoring)
- 🔍 - [Search & Web](#search-web)
- 🗺️ - [Location Services](#location-services)
- 🎯 - [Marketing](#marketing)
- 📝 - [Note Taking](#note-taking)
- ⚡ - [Cloud Platforms](#cloud-platforms)
- ⚙️ - [Workflow Automation](#workflow-automation)
- 🤖 - [System Automation](#system-automation)
- 📱 - [Social Media](#social-media)
- 🎮 - [Gaming](#gaming)
- 💹 - [Finance](#finance)
- 🧬 - [Research & Data](#research-data)
- 🤝 - [AI Services](#ai-services)
- 💻 - [Development Tools](#development-tools)
- 📊 - [Data Visualization](#data-visualization)
- 🆔 - [Identity](#identity)
- 🔗 - [Aggregators](#aggregators)
- 💬 - [Language & Translation](#language)
- 🔒 - [Security](#security)
- 🔌 - [IoT](#iot)
- 🧑‍🎨 - [Art & Literature](#art-literature)
- 🛒 - [E-Commerce](#e-commerce)
- 📦 - [Data Platforms](#data-platforms)
- 🤖 - [Robotics & Physical AI](#robotics)

<sup><details>

<summary>Legend</summary>

- <sup>⭐</sup> Official protocol implementation
- <sup>1</sup> First implementation (when multiple implementations exist)
- <sup>2</sup> Second implementation
- <sup>3</sup> Third implementation
- <sup>n</sup> Subsequent implementations
</details></sup>

<br />

## Tools & Utilities

See [Helpful Tools & Utilities](#helpful-tools-&-utilities) section for tools to help manage, configure, and work with MCP servers.

<br />

## 📂 <a name="file-systems"></a>File Systems

> Provides direct access to local file systems with configurable permissions. Enables AI models to read, write, and manage files within specified directories.
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [Backup](https://github.com/hexitex/MCP-Backup-Server) - Provides file and folder backup and restoration capabilities for AI agents and code editing tools
- <img src="https://cdn.simpleicons.org/files/9AD1ED" height="14"/> [FileStash](https://github.com/mickael-kerjean/filestash/tree/master/server/plugin/plg_handler_mcp) - Remote Storage Access: SFTP, S3, FTP, SMB, NFS, WebDAV, GIT, FTPS, gcloud, azure blob, sharepoint, etc... 
- <img src="https://cdn.simpleicons.org/files/2196F3" height="14"/> [FileSystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)<sup><sup>1</sup></sup> - Direct local file system access
- <img src="https://cdn.simpleicons.org/files/4A90E2" height="14"/> [FileSystem](https://github.com/mark3labs/mcp-filesystem-server)<sup><sup>2</sup></sup> - Golang implementation for local file system access
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [Everything Search](https://github.com/mamertofabian/mcp-everything-search) - Lightning-fast Windows file search powered by Everything SDK
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [fast-filesystem-mcp](https://github.com/efforthye/fast-filesystem-mcp) - Advanced filesystem operations with large file handling capabilities and Claude-optimized features. Provides fast file reading/writing, sequential reading for large files, directory operations, file search, and streaming writes with backup & recovery.
- <img src="https://cdn.simpleicons.org/files/4CAF50" height="14"/> [llm-context](https://github.com/cyberchitta/llm-context.py) - S
