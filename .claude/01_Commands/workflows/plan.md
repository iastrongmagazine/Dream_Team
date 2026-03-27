---
description: Plan - Transforma una idea en un plan estructurado (Professor X)
argument-hint: "[descripción de la feature o tarea]"
allowed-tools: Bash(python 04_Engine/08_Scripts_Os/*.py), Read(*), Glob(*)
---

# Workflows: Plan Command

Transforma feature descriptions, bug reports, o improvement ideas en planes estructurados.

## Usage
```
/workflows:plan "Añadir dashboard de análisis"
/workflows:plan @docs/specs/feature.md
```

## Action
Execute the Professor X planning workflow:

```bash
python 04_Engine/08_Scripts_Os/02_Professor_X_Plan.py "$ARGUMENTS"
```
