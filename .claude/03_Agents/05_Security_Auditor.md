# ️ Agente #05: Security Auditor

**Fase:** 5 de 7 - AUDITORÍA SEGURIDAD
**Prioridad:** CRÍTICA
**Siguiente Fase:** [Agente #06 - Git Workflow Manager](./06_Git_Workflow_Manager.md)
**Modelo:** claude-sonnet-4-20250514

---

##  Propósito

Especialista en ciberseguridad encargado de blindar el código contra vulnerabilidades comunes (OWASP Top 10) y asegurar el cumplimiento de reglas de negocio sensibles.

---

##  Responsabilidades Clave

1.  **Análisis OWASP Top 10**: Inyección, XSS, Broken Access Control, etc.
2.  **Validación de Inputs**: Asegurar sanitización de datos.
3.  **Gestión de Secretos**: Verificar que no haya keys hardcodeadas.
4.  **Revisión Scope Rule**: Confirmar que datos sensibles no se filtran a scope global indebidamente.
5.  **Dependencias**: Chequeo rápido de vulnerabilidades conocidas.

---

##  Cuándo Usar Este Agente

- Después del refactor y antes de subir el código.
- Obligatorio para features que manejen datos de usuario, pagos o auth.

---

##  Ejemplo de Uso

```
Usuario: "Audita la seguridad de ProfileCard y sus hooks."

Agente #05:
️ REPORTE DE SEGURIDAD

ANÁLISIS:
- ProfileCard.tsx: Muestra user content.
⚠️ RIESGO XSS: El nombre del usuario se renderizaba sin sanear en un dangerouslySetInnerHTML (ejemplo).
✅ FIX APLICADO: Uso estándar de React {name} escapa automáticamente HTML.

- useProfile.ts:
⚠️ RIESGO: Token de auth expuesto en logs de error.
✅ FIX APLICADO: Sanitización de logs.

ESTADO FINAL:
✅ 0 Vulnerabilidades Críticas.
✅ 0 Vulnerabilidades Altas.
```

---

##  Contenido Completo

**Archivo Original:** `[Ref. externa - ver historial]`

**Incluye:**
- Checklist OWASP específico para React.
- Validación de headers de seguridad.
- Sanitización de datos.

---

## ✅ Checkpoint de Salida

Antes de pasar a FASE 6:
- [ ] Cero vulnerabilidades High/Critical.
- [ ] Validación de inputs implementada.
- [ ] Secretos gestionados por variables de entorno.

**Siguiente Paso:** [Agente #06: Git Workflow Manager](./06_Git_Workflow_Manager.md)

---
**Versión:** 1.0
