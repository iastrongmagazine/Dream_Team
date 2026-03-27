---
description: Carga el contexto completo del sistema (Iron Man Boot)
argument-hint: "[tarea específica o contexto a priorizar]"
allowed-tools: Bash(python 04_Engine/08_Scripts_Os/*.py), Read(*), Glob(*)
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
python 04_Engine/08_Scripts_Os/08_Ritual_Cierre.py --mode genesis
```

This loads:
- Session rules (.claude/02_Rules/)
- Long-term memory (01_Brain/01_Context_Memory/)
- Process notes (01_Brain/03_Process_Notes/)
- Task status (02_Operations/01_Active_Tasks/)
