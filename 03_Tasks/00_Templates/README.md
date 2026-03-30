# 05_Templates — PersonalOS Task Templates

> **Versión:** 2.0
> **Última actualización:** 2026-03-20
> **Propósito:** Templates para planificar y documentar tareas

- --

## 📋 Plantillas Disponibles

| Plantilla                          | Uso                            | Secciones        | Esfuerzo     |
|------------------------------------|--------------------------------|------------------|--------------|
| **03_Task_Template_SOTA.md**       | Tareas complejas, producción   | 14 + SDD + GGA   | 1-8 horas    |
| **04_Task_Template_Medio.md**      | Features estándar              | 12               | 1-4 horas    |
| **05_Task_Template_Corto.md**      | Quick fixes, tareas simples    | 5                | 30min-2h     |
| **00_Task_Template_Skeleton.md**   | Referencia completa            | 13               | —            |
| **01_ai_task_template.md**         | ShipKit Original               | 14               | —            |
| **02_process_note_template.md**    | Session Notes                  | 6                | —            |

- --

## 🎯 Guía de Uso

### ¿Cuál usar?

| Situación                  | Plantilla          |
|----------------------------|--------------------|
| Nuevo feature grande       | **SOTA**           |
| Feature medio              | **Medio**          |
| Bug fix, refactor rápido   | **Corto**          |
| Documentar sesión          | **process_note**   |

### Flujo Recomendado

```
1. Crear tarea usando template adecuado
2. Llenar Context + Next Actions
3. Desarrollar siguiendo secciones
4. Actualizar Progress Log
5. Al cerrar: process_note_template.md
```

- --

## 📌 Metadata Standard

```yaml
- --
Title: [Nombre]
Category: [feature/fix/refactor/system_design]
Priority: [P0/P1/P2/P3]
Status: [draft/active/done]
Created_Date: [YYYY-MM-DD]
Estimated_Effort: [X hours]
Dependencies: [task refs]
Tags: [lista]
Resource_Refs:
  - 01_Core/04_Rules/
  - 04_Agent_Teams_Lite/
  - 06_Taste_Skills/
- --
```

- --

## 🔗 Referencias

- **Rules:** `01_Core/04_Rules/`
- **SDD Workflow:** `04_Agent_Teams_Lite/`
- **Taste-Skills:** `06_Taste_Skills/`
- **GGA Code Review:** `.agent/05_GGA/`
- **Skills:** `.agent/02_Skills/`

## Claude Context

- [Claude AI Announcements 2026](../../03_Knowledge/01_Research_Knowledge/Claude_AI_Announcements_2026.md)

- --

## 📝 Ejemplos

Ver carpeta `examples/`:

- `examples/TASK_SOTA_EJEMPLO.md`
- `examples/TASK_MEDIO_EJEMPLO.md`
- `examples/TASK_CORTO_EJEMPLO.md`

- --

## 🎨 Design Audit (Dieter Rams)

Todas las tareas deben incluir:

- [ ] ¿Es innovador y útil?
- [ ] ¿Es estético y comprensible?
- [ ] ¿Es discreto y honesto?
- [ ] ¿Es duradero y cuida cada detalle?

- --

© 2026 PersonalOS
