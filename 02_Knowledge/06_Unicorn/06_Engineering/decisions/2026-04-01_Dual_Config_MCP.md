---
type: decision
area: engineering
date: 2026-04-01
status: active
tags: [mcp, opencode, claude-code, dual-config]
---

## Dual-Config MCP Pattern — Claude Code vs OpenCode

### Context
PersonalOS uses two separate MCP configs — one for Claude Code, one for OpenCode. Both have 31 active MCPs.

### Problem
Claude Code and OpenCode read configs from different paths and with different formats. Original error: config at wrong path for OpenCode.

### Decision
Keep two separate MCP config files documented:
- Claude Code: `.mcp.json` at root
- OpenCode: `opencode.mcp.json` at root

### Application
Validate that both files exist and have the same MCPs in each audit.

### Related Lessons
- OpenCode v1.3.13 changed `env` → `environment` (breaking change)