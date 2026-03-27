---
description: Compound - Documenta soluciones para compounding (Hulk)
argument-hint: "[brief context about the fix]"
allowed-tools: Bash(python 08_Scripts_Os/*.py), Read(*), Glob(*)
---

# Workflows: Compound Command

Documenta un problema recientemente resuelto para capturar conocimiento.

## Usage
```
/workflows:compound
/workflows:compound "fix: N+1 query en brief generation"
```

## Action
Execute the Hulk compound workflow:

```bash
python 08_Scripts_Os/05_Hulk_Compound.py "$ARGUMENTS"
```
