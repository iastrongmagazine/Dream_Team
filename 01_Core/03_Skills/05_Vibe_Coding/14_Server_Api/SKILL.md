---
name: engram-server-api
description: > Triggers on: 15_Server_Api, patterns, coding.
  API contract guardrails for Engram server changes.
  Trigger: Any route, handler, payload, or status code modification.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## When to Use

Use this skill when:
- Adding or changing HTTP routes
- Updating handler request/response schemas
- Modifying status code behavior

---

## Contract Rules

1. Every new/changed endpoint must have tests.
2. Cover both success and error paths.
3. Keep scripts and docs aligned with real handlers.
4. Do not reference non-existent endpoints in plugins/hooks.

---

## Required Validation

- Handler-level tests for parsing/validation errors
- E2E tests for route behavior and response body
- Regression test for every bugfix related to API contracts

---

## Docs Rules

If payload or route changes, update docs in the same PR.

## Esencia Original
> **Propósito:** Propósito del skill aquí
> **Flujo:** Pasos principales del flujo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 💾 State Persistence

Guardar en:
- `03_Knowledge/` — Documentación
- `02_Operations/` — Estado activo
