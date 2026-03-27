---
description: Review - Revisión de código exhaustiva multi-agente (Vision)
argument-hint: "[PR number, GitHub URL, branch name, or latest]"
allowed-tools: Bash(python 08_Scripts_Os/*.py), Read(*), Glob(*), Bash(gh *)
---

# Workflows: Review Command

Realiza revisiones de código exhaustivas usando análisis multi-agente.

## Usage
```
/workflows:review 123
/workflows:review main
/workflows:review latest
```

## Action
Execute the Vision review workflow:

```bash
python 08_Scripts_Os/04_Vision_Review.py "$ARGUMENTS"
```
