---
description: Work - Ejecuta un plan con calidad y eficiencia (Thor)
argument-hint: "[plan file, specification, or todo file path]"
allowed-tools: Bash(python 04_Engine/08_Scripts_Os/*.py), Read(*), Glob(*), Bash(git *)
---

# Workflows: Work Command

Ejecuta un plan de trabajo eficientemente manteniendo calidad y terminando features.

## Usage
```
/workflows:work docs/plans/2026-03-10-feature-plan.md
/workflows:work @current-todo
```

## Action
Execute the Thor work workflow:

```bash
python 04_Engine/08_Scripts_Os/03_Thor_Work.py "$ARGUMENTS"
```
