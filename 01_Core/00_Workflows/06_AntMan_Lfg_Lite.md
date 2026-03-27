---
name: lfg-lite
description: Ciclo autónomo estándar para tareas cotidianas (12 pasos optimizados). Usar para features pequeñas/medianas.
argument-hint: "[descripción de la tarea o feature]"
---

# 🐜 Workflow: LFG Lite (Ant-Man — Pequeño pero poderoso)

Ciclo de ingeniería autónomo para tareas cotidianas. Completa desde análisis hasta commit en 12 pasos.

## 📋 Pasos de Ejecución

1. **Cargar contexto**: Leer `CLAUDE.md` + `.cursor/00_Rules/01_Context_Protocol.mdc`
2. **Entender estado actual**: `git status` + revisar tareas activas en `02_Operations/Tasks/`
3. **Analizar impacto**: Identificar archivos y módulos afectados por `$ARGUMENTS`
4. **Reproducir bug** *(solo si es bug)*: Documentar pasos mínimos para reproducir + logs
5. **Planear**: Ejecutar `02_Professor_X_Plan` — crear plan en `02_Operations/Tasks/`
6. **Implementar**: Ejecutar `04_Thor_Work` — cambios incrementales con commits atómicos
7. **Resolver TODOs pendientes**: Revisar y cerrar cualquier TODO generado durante implementación
8. **Calidad de código**: `python 04_Engine/37_Linter_Autofix.py` + verificar tests
9. **Validar reglas**: `python 04_Engine/40_Validate_Rules.py`
10. **Revisar**: Ejecutar `03_Vision_Review` — revisión de código completa
11. **Playwright** *(si hay UI)*: Screenshot antes/después con MCP Playwright
12. **Cerrar**: Commit final + `python 04_Engine/08_Ritual_Cierre.py` → reportar `✅ DONE`

## ⚡ Cuándo usar Lite vs Pro

- **Lite**: Tasks P2/P3, bugs simples, mejoras menores, docs
- **Pro** (`07_Doc_Strange_Lfg`): Tasks P0/P1, features nuevas, cambios arquitectónicos

---

© 2026 PersonalOS | Lite & Fast Engineering.
