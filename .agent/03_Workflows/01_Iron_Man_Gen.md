---
name: genesis
description: Workflow de inicio de sesión — carga reglas, memoria y notas de proceso del PersonalOS.
argument-hint: "[opcional: tarea específica del día o contexto a priorizar]"
---

# 🧬 Workflow: Génesis (Iron Man Boot)

Ejecutar al inicio de cada sesión para cargar el contexto completo del sistema: reglas vigentes, memoria de largo plazo y estado actual de tareas.

## Pasos

1. **Leer Reglas de Sesión**:
   - Leer `.cursor/00_Rules/01_Context_Protocol.mdc` (protocolo de inicio, obligatorio).
   - Leer `.cursor/00_Rules/` — revisar cualquier regla con `alwaysApply: true`.

2. **Cargar Memoria de Largo Plazo**:
   - Leer los archivos más recientes en `01_Brain/01_Context_Memory/`.
   - Leer `01_Brain/07_Memory_Brain/00_MAPEOS/01_System_Map_2026-03-24.md` (mapa del sistema actualizado).

3. **Revisar Notas de Proceso**:
   - Leer los archivos más recientes en `01_Brain/03_Process_Notes/`.

4. **Sincronizar Estado de Tareas**:
   - Leer `02_Operations/Tasks/` — identificar tareas `status: s` (en progreso) y `status: b` (bloqueadas).
   - Leer `00_Core/GOALS.md` para alinear foco del día.

5. **Verificar MCPs disponibles** (opcional):
   - Playwright MCP: disponible para navegación web y screenshots.
   - Fireflies MCP: disponible si `FIREFLIES_API_KEY` está configurada en `.mcp.json`.

6. **Resumen de Contexto al Chat**:
   - Reportar en bullet points:
     - Estado actual del proyecto (último commit, cambios recientes).
     - Reglas críticas de esta sesión.
     - Tareas en progreso / bloqueadas inmediatas.
     - Agentes y herramientas disponibles (`.claude/agents/`, `.agent/01_Agents/`).

// turbo-all
