# Priority Guide

## P0 — Critical
- Security issues
- Production bugs
- Blocker for other team members
- Deadline TODAY

## P1 — Important
- Core feature work
- Technical debt that affects velocity
- Deadline this week

## P2 — Nice to Have
- Improvements
- Refactoring
- Documentation

## P3 — Backlog
- Ideas
- Future work
- Nice to have someday

## Decision Tree

```
Is it blocking someone?
  YES → P0
  
NO → Is it breaking production?
  YES → P0
  
NO → Is deadline today?
  YES → P0
  
NO → Does it affect >50% of users?
  YES → P1
  
NO → Is it core to current goal?
  YES → P1
  
NO → P2/P3
```

## Standup Rules

| Priority | Include in Standup? | Frequency |
|----------|---------------------|-----------|
| P0 | ✅ ALWAYS | Daily |
| P1 | ✅ Max 3 | Daily |
| P2 | ❌ NO | Weekly review |
| P3 | ❌ NO | Monthly review |
