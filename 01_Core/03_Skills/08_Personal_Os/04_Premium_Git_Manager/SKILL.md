---
name: premium-git-manager
description: QUÉ HACE: Gestiona el ciclo de vida de Git (ramas, verificación, commits atómicos y push) con estándares premium. CUÁNDO SE EJECUTA: Para cualquier operación de control de versiones que requiera trazabilidad y seguridad. Triggers on: personalos, workflow, automation.
---

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido

- Estado actual de Git identificado (`git status`).
- Cambios verificados mediante tests o revisión visual.
- Staging area preparada o intención de commit clara.

### 📦 Output Esperado

- Commits con mensajes semánticos: `feat:`, `fix:`, `chore:`, `docs:`, `refactor:`, `style:`, `test:`.
- Ramas con nombres descriptivos (ej: `feature/`, `bugfix/`).
- Repositorio en estado "Pure Green" tras cada operación.

### 🚫 Limitaciones

- **Prohibido commits "bulk"** sin descripción atómica.
- No realizar push a `main` directamente si existen ramas de desarrollo (opcional según política).
- Ignorar archivos grandes o binarios no deseados (validar `.gitignore`).

## 🛠️ Workflow: El Camino del Operador

1.  **Auditoría de Cambios:** Ejecutar `git status` y `git diff --cached`.
2.  **Verificación Pre-Commit:** Asegurar que `00_Context_Reset.py` se ha ejecutado y los tests pasan.
3.  **Generación de Mensaje Atómico:** Construir el mensaje siguiendo: `<type>(<scope>): <subject>`.
4.  **Ejecución del Commit:** Realizar el commit y verificar el hash generado.
5.  **Sincronización:** Consultar al usuario antes de realizar `push`.

## 📚 Estructura de Mensajes (Atomic Standards)

- `feat`: Nueva funcionalidad para el usuario.
- `fix`: Resolución de un bug.
- `docs`: Cambios solo en la documentación.
- `style`: Cambios que no afectan el significado del código (espacios, formato).
- `refactor`: Cambio en el código que ni arregla un bug ni añade una funcionalidad.
- `chore`: Tareas de mantenimiento, actualización de dependencias, etc.
- `test`: Añadir o corregir tests.

---

© 2026 PersonalOS | Git Operations Grade Silicon Valley

## Esencia Original
> **Propósito:** Gestionar ciclo de vida de Git con estándares premium — branches, verification, atomic commits, push
> **Flujo:** Verificar cambios → Crear branch → Commit atómico → Push con trazabilidad

## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `02_Operations/` — Estado
