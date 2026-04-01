---
description: Carga el contexto completo del sistema (Iron Man Boot)
argument-hint: "[tarea específica o contexto a priorizar]"
allowed-tools: Bash(python 08_Scripts_Os/*.py), Read(*), Glob(*)
---

# Genesis Command

Ejecuta el workflow de inicio de sesión para cargar el contexto completo del sistema.

## Usage
```
/genesis
/genesis "tarea específica del día"
```

## Action
Execute the Iron Man startup workflow:

```bash
python 08_Scripts_Os/04_Ritual_Hub.py --mode genesis $ARGUMENTS
```

This loads:
- Session rules (.claude/02_Rules/)
- Long-term memory (engram_mem_context)
- Process notes (04_Operations/03_Process_Notes/)
- Task status (03_Tasks/)
- Goals & Backlog (00_Winter_is_Coming/)
