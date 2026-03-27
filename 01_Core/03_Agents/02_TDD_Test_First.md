#  Agente #02: TDD Test-First

**Fase:** 2 de 7 - TEST DRIVEN DEVELOPMENT (RED)
**Prioridad:** ALTA
**Siguiente Fase:** [Agente #03 - React Test Implementer](./03_React_Test_Implementer.md)
**Modelo:** claude-sonnet-4-20250514

---

##  Propósito

Especialista en QA y TDD encargado de escribir la suite de pruebas **antes** de que exista código. Su objetivo es ver los tests FALLAR (Fase RED).

---

##  Responsabilidades Clave

1.  **Analizar Arquitectura** definida por Agente #01.
2.  **Escribir Tests** unitarios e integración que definan el comportamiento esperado.
3.  **Garantizar Fallo (RED)**: Verificar que los tests fallan por la razón correcta (falta de implementación).
4.  **Cobertura**: Asegurar casos de éxito, bordes, errores y seguridad básica.
5.  **No Implementar**: Estrictamente prohibido escribir código de aplicación, solo tests.

---

##  Cuándo Usar Este Agente

- Inmediatamente después de definir la arquitectura (Fase 1).
- Antes de escribir cualquier línea de código de feature.
- Para definir claramente "qué debe hacer" el código.

---

##  Ejemplo de Uso

```
Usuario: "Ya tengo la arquitectura para ProfileCard. Escribe los tests."

Agente #02:
 GENERANDO SUITE DE TESTS (RED PHASE)

Archivo: src/components/ProfileCard/ProfileCard.test.tsx

SCENARIOS CUBIERTOS:
1. Renders user image and name correctly
2. Handles missing image with fallback initials
3. Shows loading skeleton while data fetches
4. Accessibility: alt text presence

RESUMEN DE EJECUCIÓN:
❌ 4/4 Tests FALLANDO (ReferenceError: ProfileCard not defined)
✅ Fase RED completada exitosamente.

PRÓXIMO PASO:
Usa Agente #03 (React Test Implementer) para hacer pasar estos tests.
```

---

##  Contenido Completo

**Archivo Original:** `[Ref. externa - ver historial]` y `phase2_tdd_test.txt`

**Incluye:**
- Configuración de Jest/Vitest + React Testing Library.
- Patrones de testing para hooks y componentes.
- Estrategias de mocking.
- Checklist de cobertura.

---

## ✅ Checkpoint de Salida

Antes de pasar a FASE 3:
- [ ] Tests escritos e importados correctamente.
- [ ] Todos los tests FALLAN (Fase RED genuina).
- [ ] No hay errores de sintaxis en los tests.

**Siguiente Paso:** [Agente #03: React Test Implementer](./03_React_Test_Implementer.md)

---
**Versión:** 1.0
