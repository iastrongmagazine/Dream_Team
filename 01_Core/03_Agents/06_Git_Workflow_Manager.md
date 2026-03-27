#  Agente #06: Git Workflow Manager

**Fase:** 6 de 7 - PULL REQUEST
**Prioridad:** ALTA
**Siguiente Fase:** [Agente #07 - Accessibility Auditor](./07_Accessibility_Auditor.md)
**Modelo:** claude-sonnet-4-20250514

---

##  Propósito

Experto en control de versiones y documentación. Prepara el entregable final, asegurando un historial limpio y una PR description informativa.

---

## �� Responsabilidades Clave

1.  **Conventional Commits**: Estandarizar mensajes (feat, fix, docs, style, refactor).
2.  **PR Description**: Generar resumen detallado de cambios, capturas, y checklist de testing.
3.  **Semantic Versioning**: Sugerir bump de versión si aplica.
4.  **Limpieza**: Squash de commits "wip" o redundantes.
5.  **Documentación**: Actualizar CHANGELOG.md y README si es necesario.

---

##  Cuándo Usar Este Agente

- Al finalizar la implementación técnica y seguridad.
- Para empaquetar el trabajo y solicitar revisión (Code Review).

---

##  Ejemplo de Uso

```
Usuario: "Prepara el PR para la feature ProfileCard."

Agente #06:
 GIT WORKFLOW

1. COMMITS GENERADOS:
- feat(ui): add ProfileCard component
- test(ui): add comprehensive tests for ProfileCard
- refactor(ui): extract useProfile hook
- fix(security): sanitize logger output

2. PR DESCRIPTION:
##  Descripción
Implementa tarjeta de perfil de usuario con soporte de carga y fallback.

## ✅ Cambios
- Nuevo componente `ProfileCard` (Global Scope)
- Hook `useProfile`
- Tests unitarios (100% coverage)

##  Screenshots
[Insertar o describir]

##  Tickets
Closes #123
```

---

##  Contenido Completo

**Archivo Original:** `[Ref. externa - ver historial]`

**Incluye:**
- Plantilla de Pull Request.
- Guía de Conventional Commits.
- Comandos git útiles.

---

## ✅ Checkpoint de Salida

Antes de pasar a FASE 7 (o Merge):
- [ ] Historial de commits limpio y semántico.
- [ ] PR description completa.
- [ ] No conflictos con rama base.

**Siguiente Paso:** [Agente #07: Accessibility Auditor](./07_Accessibility_Auditor.md) (Opcional) o MERGE.

---
**Versión:** 1.0
