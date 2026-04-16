# Slash_Commands - System_Guardian

## /gr

Activa System Guardian para validar y auditar el proyecto.

* *Uso**: `/gr [flags]`

* *Flags**:
- sin flag → Dry-run (solo reporte)
- `--apply` → Aplica fixes automáticamente
- `--agents` → Solo lanza 3 agentes de revisión

* *Descripción**:
Valida estructura, naming, links, y ejecuta beautify + review de 3 agentes.

- --

## /gra

Activa System Guardian con `--apply` para auto-corregir issues.

- --

## /gr-agents

Solo lanza los 3 agentes de revisión sin ejecutar los pasos 1-8.

- --

## Ejemplo

```
/gr
→ Ejecuta System Guardian en modo dry-run

/gr --apply
→ Ejecuta y aplica fixes automáticamente

/gr --agents
→ Solo lanza agentes de revisión
```
