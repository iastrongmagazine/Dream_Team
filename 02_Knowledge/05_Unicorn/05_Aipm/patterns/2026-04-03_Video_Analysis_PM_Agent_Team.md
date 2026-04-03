---
type: pattern
area: aipm
date: 2026-04-03
status: active
tags: [video-analysis, product-school, agents, pm-workflow, lessons, agent-manager]
---

# Video Analysis: Product Manager + Agent Team - What Could Go Wrong?

**Source:** Product School Live + Unwind AI Analysis  
**Key Article:** "Best AI PMs in 2026 Will Be Agent Managers" by Shubham Saboo  
**URL:** https://www.theunwindai.com/p/best-ai-pms-in-2026-will-be-agent-managers  
**Date:** 2026-03-28  
**Context:** Running 8 AI agents for 2 months - lessons learned

---

## Overview

Running AI agents is NOT a technical skill - it's a management skill. This analysis covers what PMs need to know when managing agent teams.

---

## The Core Insight

> "Everyone thinks running AI agents is a technical skill. It's not. It's a management skill."

Running one agent as a tool = different from managing a team of agents that improve over time.

---

## The 3 Management Mistakes That Break Agent Teams

### Mistake 1: Over-Specifying

**What happens:**
- Detailed step-by-step instructions: "Search these 5 sources, in this order, format results like this"
- Output is rigid and misses things it would catch with more freedom

**The fix:**
- Replace procedures with principles
- Example: "Only surface tools developers can use today. Verify every claim. Skip corporate news."
- Output quality jumps immediately

**Lesson:** Tell agents what good looks like, not how to get there.

---

### Mistake 2: Stepping In Too Early

**What happens:**
- First two weeks are painful - agent flags 47 stories when only 7 are worth reading
- Instinct is to scrap it and do the work yourself
- Most people quit here

**The fix:**
- DON'T quit
- Those bad outputs are the most valuable data you'll collect
- Each correction can be stored permanently
- Example: After two weeks of reviewing noise, wrote rule: "If the reader can't do something with this today, skip it."
- Result: 47 stories → 7 stories

**Lesson:** Bad outputs → corrections → permanent improvements. Let the learning compound.

---

### Mistake 3: Treating All Agents the Same

**What happens:**
- Apply same constraints to research agent and content agent
- Research needs: tight constraints, verified sources, primary links, no speculation
- Content needs: creative latitude, energy, personality

**The fix:**
- Different roles need different management styles
- Manage content agent like research agent = technically correct posts that nobody wants to read

**Lesson:** Customize management style per agent role.

---

## What Agent Management Actually Looks Like

### File Stack System

Each agent loads files at session start:
- Identity file
- Role file
- Principles file
- Operating instructions file

**Key insight:** Not what's in the files - it's how they CHANGE over time.

### Review Process

```
Review output structurally (not every line)
├── Is the agent repeating the same mistake?
├── Is it drifting from the brief?
└── Is quality trending up or down?
```

When pattern found → give feedback → agent updates its own files → next session fix is loaded.

### Shared Layer

One correction to one agent propagates to rest:
- Write once in shared feedback log
- Every agent picks it up next session
- **Not prompting - that's management**

### Examples

- Content agent learned: no emojis, no hashtags (writing voice)
- Research agent learned: which stories audience actually cares about (filter automatically)
- These files didn't exist on day one - all grew from corrections

---

## Why PMs Are Built for This

| Traditional PM Skill | Agent Management Equivalent |
|---------------------|---------------------------|
| Problem shaping | Agent scoping - define each role through personality file |
| Context curation | File engineering - agents build/maintain their own file stacks |
| Stakeholder management | Agent coordination - order matters, downstream uses upstream output |
| Feedback | Permanent - correction written to files, never give same feedback twice |

### Key Insight

> "When an agent produces technically correct output that misses the point, the engineer sees working code. The PM sees a product that doesn't solve the problem."

**Taste matters more than syntax** when reviewing agent output.

---

## The Compounding Curve

| Phase | Output Quality | Time Spent |
|-------|---------------|------------|
| Day 1 | Mediocre | Fixing everything |
| Day 10 | Improving | Fixing edge cases |
| Day 30 | 90% ready to ship | Reviewing |
| Day 50 | Mostly done | Strategy time |

**This is identical to onboarding a human hire:**
- First month: net negative
- Second month: breaks even
- Third month: runs independently

**PMs who understand this curve will build the best agent teams.**

---

## Three Stages of Agent Management

### Stage 1: Agents as Tools
- Using agents to build prototypes faster
- Real but limited

### Stage 2: Managing Agents That Build For You
- Personality files
- Shared memory
- Cron schedules
- Feedback loops that compound
- Ship daily what stage one PMs ship weekly

### Stage 3: Agents Managing Other Agents
- Content agent runs weekly performance reviews on her own posts
- Chief of Staff agent monitors cron jobs and force-restarts stalled ones
- Management moves up a level

---

## Key Takeaways for PMs

1. **Agent management = management skill, not technical skill**
2. **Principles > procedures** - define what good looks like
3. **Let bad outputs teach** - don't step in too early
4. **Customize per agent** - different roles need different constraints
5. **Feedback compounds** - corrections become permanent improvements
6. **Taste over syntax** - PM eye for quality matters more than coding skills
7. **Compounding takes time** - push through first 2 weeks of pain

---

## Connection to Unicorn Knowledge Base

This content relates to:
- **05_AIPM/patterns/Agent_Orchestration.md** - Orchestrating multiple agents
- **05_AIPM/patterns/Compound_Engineering.md** - Multi-agent patterns
- **05_AIPM/patterns/2026-04-03_AI_PM_Career_Guide_2026.md** - AI PM skills
- **06_Engineering/patterns/2026-04-03_Engineering_SOTA_2026.md** - Agentic coding

---

## Tags

video-analysis, agent-manager, pm-skills, lessons, management, feedback-loop, compounding, stages, 2026, silicon-valley

---

*Analysis based on Shubham Saboo's 2-month experience running 8 AI agents at Unwind AI.*