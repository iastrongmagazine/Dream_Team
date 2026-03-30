---
name: genesis
description: Workflow de inicio de sesión — carga reglas, memoria y notas de proceso del PersonalOS.
argument-hint: "[opcional: tarea específica del día o contexto a priorizar]"
---

# 🧬 Workflow: Génesis (Iron Man Boot)

Ejecutar al inicio de cada sesión para cargar el contexto completo del sistema: reglas vigentes, memoria de largo plazo y estado actual de tareas.

## Pasos

1. **Leer Reglas de Sesión**:
   - Leer `01_Core/01_Rules/` — revisar cualquier regla con `alwaysApply: true`.

2. **Cargar Memoria de Largo Plazo (AGENTE)**:
   - Ejecutar `mem_search()` con project="Think_Different" para recuperar contexto previo.
   - Leer `04_Operations/04_Memory_Brain/` — mapa del sistema actualizado.

3. **Revisar Notas de Proceso (USUARIO)**:
   - Leer los archivos más recientes en `04_Operations/03_Process_Notes/`.
   - Ejecutar `mem_save()` para guardar aprendizajes clave de cada sesión.

4. **Sincronizar Estado de Tareas**:
   - Leer `03_Tasks/` — identificar tareas `status: s` (en progreso) y `status: b` (bloqueadas).
   - Leer `00_Winter_is_Coming/GOALS.md` para alinear foco del día.

5. **Verificar MCPs disponibles** (opcional):
   - Playwright MCP: disponible para navegación web y screenshots.
   - Fireflies MCP: disponible si `FIREFLIES_API_KEY` está configurada en `.mcp.json`.

6. **Resumen de Contexto al Chat**:
   - Reportar en bullet points:
     - Estado actual del proyecto (último commit, cambios recientes).
     - Reglas críticas de esta sesión.
     - Tareas en progreso / bloqueadas inmediatas.
     - Agentes y herramientas disponibles (`.agent/01_Agents/`, `.agent/01_Agents/`).

// turbo-all
