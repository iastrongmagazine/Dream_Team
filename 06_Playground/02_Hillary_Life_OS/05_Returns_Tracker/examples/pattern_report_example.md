# Returns Tracker Report - 2026-03-31

---
created: 2026-03-31T18:00:00Z
type: pattern-report
total_patterns: 5
viable_skills: 2
monitoring: 3
---

# Monthly Pattern Analysis

## Detected Patterns

| Pattern ID            | Type           | Frequency   | Confidence   | Action         |
|-----------------------|----------------|-------------|--------------|----------------|
| daily-standup         | tag_recurrence | 30/30 days  | 92%          | Generate skill |
| bug-investigation     | workflow_chain | 15/30 days  | 65%          | Monitor        |
| code-review-session   | time_pattern   | 45/30 days  | 85%          | Generate skill |
| weekly-planning       | temporal       | 4/4 weeks   | 78%          | Monitor        |
| meeting-transcription | tag_recurrence | 20/30 days  | 71%          | Needs review   |

## Top Recommendation

### Skill: Auto Standup Summary

**Pattern**: Daily standup every weekday at 9am for 30 days

**Evidence**:
- 30 captures with tag "standup"
- Consistent time: 9:00am (±15min)
- Duration: 15-30 minutes
- Team: Same participants

**Proposed triggers**:
- "standup", "daily meeting", "team sync"

**Proposed output**:
```markdown
## Standup - {date}

### What I did
- {extracted from transcript}

### Blockers
- {extracted from transcript}

### Next
- {extracted from transcript}
```

## Monitoring Patterns

These patterns need more data:

1. **Bug Investigation**: 15 occurrences - needs 10 more for skill generation
2. **Weekly Planning**: Only 4 weeks of data - needs more consistency
3. **Meeting Transcription**: 71% confidence - borderline, needs review
