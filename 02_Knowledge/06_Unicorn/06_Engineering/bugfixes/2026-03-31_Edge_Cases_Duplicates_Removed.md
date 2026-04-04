---
type: bugfix
area: engineering
date: 2026-03-31
status: resolved
tags: [duplicates, cleanup, edge-cases]
---

## Fixed Edge Cases - Duplicates Removed

### Context
User requested to get OS to 100%.

### Problem
- `.mcp.json` was markdown, not JSON (corrupt file)
- Duplicates in Maerks: OpenCode_Commands_Reference.md, OpenCode_Active_Configuration.md, OpenCode_Integration.md

### Solution
- Removed corrupt `.mcp.json`
- Removed duplicates in Maerks/Otros/
- Pending: API keys to rotate, placeholder tokens in MCPs

### Location
- `.mcp.json` (root)
- `Maerks/Otros/`

### Lesson
Verify file types before assuming format. Duplicates reduce quality.