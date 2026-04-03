---
type: lesson
area: engineering
date: 2026-03-29
status: active
tags: [tool-shed, skill-harmonizer, mcp, automation]
---

## Created Tool Shed and Skill Harmonizer Scripts

### Context
Need for evolution scripts to improve PersonalOS MCP detection and skill validation.

### What Happened
Created 2 new evolution scripts:

**1. 62_Tool_Shed.py**
- Auto-detects work context
- Suggests MCPs by tier

**2. 63_Skill_Harmonizer.py**
- Validates skills parity vs folders
- Results: 20 categories, 125 subfolders validated

### Why
Improve MCP detection and ensure skill/folder consistency.

### Application
Run Tool Shed before starting work to get contextual MCPs.
Run Skill Harmonizer during audits to validate parity.

### Location
`08_Scripts_Os/Tool_Fixed/`