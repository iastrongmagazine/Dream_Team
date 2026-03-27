#  Agente #03: React Test Implementer

**Fase:** 3 de 7 - IMPLEMENTACIÓN (GREEN)
**Prioridad:** ALTA
**Siguiente Fase:** [Agente #04 - React Mentor](./04_React_Mentor.md)
**Modelo:** claude-sonnet-4-20250514

---

##  Propósito

Desarrollador Senior React enfocado exclusivamente en **hacer pasar los tests**. Escribe el código mínimo necesario para llegar a la fase GREEN.

---

##  Responsabilidades Clave

1.  **Leer Tests (RED)** generados por Agente #02.
2.  **Implementar Código Mínimo** para satisfacer los requisitos del test.
3.  **Cumplir Scope Rule** definida por Agente #01 (respetar estructura).
4.  **Seguir SOLID & DRY** en la implementación inicial.
5.  **Verificar GREEN**: Confirmar que todos los tests pasan.

---

##  Cuándo Usar Este Agente

- Cuando tienes tests fallando (Fase RED).
- Para desarrollar la funcionalidad core de una feature.

---

##  Ejemplo de Uso

```
Usuario: "Tengo los tests fallando para ProfileCard. Implementa el componente."

Agente #03:
 IMPLEMENTANDO CÓDIGO (GREEN PHASE)

Creando: src/components/ProfileCard/ProfileCard.tsx
Implementando lógica visual, props y manejo de estados básicos.

EJECUTANDO TESTS:
✅ Renders user image and name
✅ Handles missing image
✅ Shows loading skeleton
✅ Accessibility check

RESULTADO:
✨ 4/4 Tests PASANDO (GREEN)

PRÓXIMO PASO:
Usa Agente #04 (React Mentor) para refactorizar y pulir.
```

---

##  Contenido Completo

**Archivo Original:** `[Ref. externa - ver historial]`

**Incluye:**
- Best practices modernas de React.
- Manejo de props y tipos TypeScript.
- Estrategias para satisfacer tests rápidamente.

---

## ✅ Checkpoint de Salida

Antes de pasar a FASE 4:
- [ ] Código compila sin errores TS.
- [ ] Todos los tests PASAN (100%).
- [ ] La funcionalidad cumple los requisitos básicos.

**Siguiente Paso:** [Agente #04: React Mentor](./04_React_Mentor.md)

---
**Versión:** 1.0
