# Skill 48: Test Resource Management

## 🎯 Objetivo Triggers on: testing, QA, quality, validation.

Gestionar los recursos del sistema durante la ejecución de pruebas para evitar el agotamiento de CPU/RAM y mantener el estado "Pure Green".

## 🛠️ Especificaciones Técnicas

- **Máximo de Workers**: 4 (Limitación estricta para CPUs móviles/domésticas).
- **Timeouts**: 30s por test unitario, 2min por test E2E.
- **Limpieza**: Borrado automático de DBs de prueba tras ejecución exitosa.

## 📋 Comandos de Referencia

- Vitest: `vitest --maxWorkers=4`
- Playwright: `playwright test --workers=4`
- Jest: `jest --maxWorkers=4`

## 🛡️ Regla Asociada

Referirse a `.cursor/rules/10_testing-resource-management.mdc` para la aplicación automática de estos límites.

## Esencia Original
> **Propósito:** 05_Test_Resource_Management - propósito del skill
> **Flujo:** Pasos principales del flujo de trabajo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 📁 Progressive Disclosure

> Para información detallada:
- [references/guide.md](references/guide.md) — Guía completa

## 🛠️ Scripts

- [scripts/run.py](scripts/run.py) — Script principal

## 💾 State Persistence

Guardar en:
-  — Evaluaciones
-  — Documentación

