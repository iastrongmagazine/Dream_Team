# Fireflies MCP — Meeting Intelligence

## Overview

**Purpose:** Search meetings, retrieve transcripts, and sync action items to PersonalOS.

**MCP Config:** Fireflies MCP configured in `.mcp.json` with API key.

---

## Tools Available

| Tool | Description | When to Use |
|------|-------------|-------------|
| `search_meetings` | Search Fireflies meetings by keyword/date | Find specific meeting context |
| `get_meeting_details` | Get full meeting metadata | Get attendees, duration, notes |
| `get_transcript` | Retrieve full transcript | Deep dive into conversation |
| `check_new_meetings` | List meetings since last sync | Morning standup prep |

---

## Morning Standup Integration

### Workflow: "What should I work on today?"

```
1. Check Fireflies for meetings in last 7 days
2. Extract action items and follow-ups
3. Cross-reference with Tasks (P0/P1)
4. Show "The Big 3" including Fireflies context
```

### Example Prompt

```
"What's my most important task today considering my recent meetings?"
```

### Response Format

```
🎯 TODAY'S PRIORITIES (based on Fireflies + Tasks)

📅 From Recent Meetings:
- Meeting: "Q1 Planning" (Mar 25)
  - Action: Follow up on API strategy → Create task
  - Follow-up: Send roadmap to Sarah by Friday

📋 From PersonalOS Tasks:
1. [P0] Complete API strategy doc (linked to Q1 Planning)
2. [P1] Send roadmap to Sarah (from Fireflies action item)
3. [P1] Research AI Agents (from Weekly Review)
```

---

## Syncing to PersonalOS

### Auto-Sync Flow

1. `check_new_meetings` → identify unsynced meetings
2. `get_transcript` → retrieve content
3. Save to `03_Knowledge/Transcripts/YYYY-MM-DD_Meeting_Title.md`
4. Extract action items to Tasks

### Sync Script

```bash
python 08_Scripts_Os/fireflies_sync.py
```

---

## Usage Examples

### Search Recent Meetings
```
Search meetings from last week for action items
```

### Get Meeting Context
```
Get details from yesterday's 1:1 with manager
```

### Extract Action Items
```
What were the action items from my meetings this week?
```

---

## Files Generated

| File | Location | Purpose |
|------|----------|---------|
| `YYYY-MM-DD_Title.md` | `03_Knowledge/Transcripts/` | Full transcript |
| `action_items.json` | `04_Operations/00_Context_Memory/` | Extracted tasks |

---

## Status

| Component | Status |
|-----------|--------|
| MCP Config | ✅ Active |
| Tool Guide | ✅ This file |
| Morning Standup | 🔄 Integrating |
| Sync Script | 🔄 Pending |
| Auto-extract Actions | 🔄 Pending |

---

*Last updated: 2026-03-27*
