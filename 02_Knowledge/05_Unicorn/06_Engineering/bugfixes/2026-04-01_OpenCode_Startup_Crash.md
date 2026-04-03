---
type: bugfix
area: engineering
date: 2026-04-01
status: resolved
tags: [opencode, startup-crash, compound-plugin]
---

## OpenCode Startup Crash Fix & Compound Plugin Updates

### Context
OpenCode crashed with "unrecognized key: plugin" - violated Pure Green state.

### Problem
Legacy `plugins` key in OpenCode config caused crash on startup.

### Solution
- Removed legacy `plugins` key from OpenCode config
- Documented `compound-engineering-plugin` v2.60.0 capabilities in `01_Report_Status.md`

### Lesson
Deprecated keys must be removed completely. Not using them is not enough.