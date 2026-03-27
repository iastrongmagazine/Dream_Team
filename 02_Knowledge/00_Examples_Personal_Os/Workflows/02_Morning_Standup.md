# Morning Standup Workflow

A quick 2-minute check-in to set your focus for the day.

## The Prompts

```
What should I work on today?
```

## Enhanced Workflow (with Fireflies)

### Step 1: Check Fireflies (NEW)
```
1. Search meetings from last 7 days
2. Extract action items and follow-ups
3. Cross-reference with Tasks
```

### Step 2: Check PersonalOS Tasks
```
1. List P0/P1 tasks
2. Check blocked tasks
3. Verify alignment with GOALS.md
```

### Step 3: Present "The Big 3"
```
Combine Fireflies context + Tasks + Goals
```

---

## Example Conversation

**You:** What should I work on today?

**Claude:** Good morning! Let me check your recent meetings and tasks...

**📅 From Fireflies (Last 7 Days):**
- **Mar 26 - Q1 Planning**: Action item - Send API strategy doc by Friday
- **Mar 25 - 1:1 with Manager**: Follow-up - Review roadmap with Sarah
- **Mar 24 - Team Standup**: Decision needed on mobile vs web priority

**📋 From PersonalOS Tasks:**
- 3 P0 tasks, 5 P1 tasks

**🎯 THE BIG 3 FOR TODAY:**

**1. [P0] Complete API strategy doc** (estimated: 90 min)
- 🔥 From Fireflies: "Send API strategy by Friday"
- Aligns with quarterly objective: "Ship Q1 roadmap"

**2. [P1] Send roadmap to Sarah** (estimated: 20 min)
- 🔥 From Fireflies: 1:1 follow-up
- Quick win before deep work

**3. [P1] Research AI Agents** (estimated: 60 min)
- From Weekly Review
- Supports goal: "Professional Development"

**⚠️ BLOCKED TASKS (2):**
- "API integration spec" - waiting on engineering estimates
- "User research synthesis" - waiting on interview transcripts

---

## Step-by-Step Protocol

### 1. Fireflies Integration
```markdown
1. Execute: `search_meetings` for last 7 days
2. Extract: Action items, follow-ups, decisions
3. Flag: Deadlines and commitments made in meetings
```

### 2. PersonalOS Context
```markdown
1. Read: 00_Winter_is_Coming/GOALS.md
2. List: Tasks in 03_Tasks/ (P0/P1)
3. Check: Blocked tasks (status: b)
```

### 3. Prioritization
```markdown
1. Match: Fireflies commitments → Tasks
2. Prioritize: Based on deadlines (Fireflies) + Goals alignment
3. Present: "The Big 3" with context
```

---

## Variations

### When You're Overwhelmed

```
I'm overwhelmed. What's the ONE thing I should focus on?
```

### When You Have Limited Time

```
I only have 2 hours before meetings. What can I realistically finish?
```

### When You Need Context

```
Remind me what I was working on yesterday and what's next.
```

### Fireflies-Only (No Tasks)

```
What action items did I commit to in my recent meetings?
```

---

## MCP Integration

| MCP | Tool | Purpose |
|-----|------|---------|
| **Fireflies** | `search_meetings` | Find recent meetings |
| **Fireflies** | `get_meeting_details` | Get action items |
| **Engram** | `mem_context` | Recent session context |

---

## Tips

- Do this first thing, before checking email/Slack
- Keep it under 2 minutes - just pick and start
- If you're stuck deciding, ask Claude to pick for you
- Fireflies context makes commitments visible immediately

---

## Files Reference

| File | Location |
|------|----------|
| Fireflies Tool Guide | `01_Core/05_Mcp/00_Config_Mcp/mcp-tools/06_productivity/02_fireflies.md` |
| Goals | `00_Winter_is_Coming/GOALS.md` |
| Tasks | `03_Tasks/*.md` |
| Meeting Transcripts | `03_Knowledge/Transcripts/` |

---

*Updated: 2026-03-27 — Now includes Fireflies integration*
