---
name: verify-and-commit
description: QUÉ HACE: Automatiza la verificación final y crea un commit siguiendo estándares atómicos. CUÁNDO SE EJECUTA: Tras pasar la validación (Skill 06) y antes de terminar la sesión.
---

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido

- Validación de Skill 06 completada con éxito.
- Staging area limpia (solo cambios deseados).
- Entendimiento claro del "scope" del cambio.

### 📦 Output Esperado

- Commit realizado con mensaje en formato `tipo(scope): descripción`.
- Push al repositorio remoto (si procede).
- Historial de Git limpio y trazable.

### 🚫 Limitaciones

- **Prohibido commits "bulk"** (muchas tareas en uno solo).
- No ignora fallos en el hook de pre-commit.

# Verify and Commit

## Overview

This skill handles the final verification and commit process.

## Usage

Run verification steps then commit.
