# Batch Execution Guide

## Why Batches?

- Smaller scope = easier to debug
- Regular checkpoints = early error detection
- Architect review = quality control

## Default Batch Size

**3 tasks per batch**

Adjust based on:
- Task complexity (complex = 2, simple = 5)
- Risk level (high risk = 1-2)
- Time available

## Execution Flow

```
[Batch 1] → Checkpoint → [Batch 2] → Checkpoint → [Batch 3] → Final Review
    ↑                         ↑                         ↑
 Task 1                    Task 4                    Task 7
 Task 2                    Task 5                    Task 8
 Task 3                    Task 6                    Task 9
```

## Checkpoint Report Format

```markdown
## Checkpoint: Batch N Complete

### Completed
- [x] Task N: Description
- [x] Task N+1: Description

### Verification Output
[paste test results]

### Issues Found
- [Any issues]

### Ready for feedback.
```
