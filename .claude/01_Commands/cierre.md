---
description: Ritual de Cierre - Backup, validación y sync (Fin de sesión)
argument-hint: "[--backup-only para solo backup]"
allowed-tools: Bash(python 08_Scripts_Os/*.py), Read(*), Glob(*), Bash(git *)
---

# Cierre Command (Ritual de Cierre)

Ejecuta el ritual de cierre de sesión: backup, validación y sincronización.

## Usage
```
/cierre
/cierre --backup-only
```

## Action
Execute the Ritual de Cierre workflow:

```bash
python 08_Scripts_Os/08_Ritual_Cierre.py $ARGUMENTS
```
