# Priority Matrix Guide

## Priority Definitions

| Priority | Meaning | Timeframe | Max Items |
|----------|---------|-----------|-----------|
| **P0** | Critical - Do today | Today | 3 |
| **P1** | Important - This week | 7 days | 7 |
| **P2** | Scheduled - This month | 30 days | ∞ |
| **P3** | Someday/Maybe | Backlog | ∞ |

## Decision Matrix

Ask these questions to assign priority:

### Question 1: Is it blocking something?
- **YES** → P0
- **NO** → Continue

### Question 2: Is there a deadline?
- **< 24h** → P0
- **< 7 days** → P1
- **> 7 days** → P2
- **No deadline** → P3

### Question 3: Does it align with current goals?
- **Directly aligns** → P0/P1
- **Partially aligns** → P2
- **No alignment** → P3 or Archive

## Category Examples

| Category | Typical Priority | Notes |
|----------|-----------------|-------|
| Bug blocking users | P0 | Always |
| Security issue | P0 | Always |
| Technical debt | P2/P3 | Depends on impact |
| Learning/Research | P1/P2 | Time-sensitive? |
| Admin tasks | P1 | Often overlooked |
| Meeting prep | P1 | If meeting is soon |

## Quick Reference

```
Priority = min(deadline_priority, goal_alignment, impact)

- Deadline today → P0
- Goal-aligned + high impact → P0/P1
- No deadline + no goal → P3 or Archive
```

---

*Part of Backlog Processing Skill - Progressive Disclosure*
