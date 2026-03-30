---
name: managing-image-assets
description: QUÉ HACE: Organiza, cataloga y optimiza activos de imagen generados para su uso en proyectos. CUÁNDO SE EJECUTA: Después de generar imágenes con herramientas de IA o al organizar la librería multimedia. Triggers on: personalos, workflow, automation.
---

# Managing Image Assets

## When to use this skill

- After generating images with the `generate_image` tool.
- When the user wants to organize their asset library.
- Before using images in a web application or project.

## Workflow

1.  **Catalog**: Move images from output directory to `assets/images/`.
2.  **Rename**: Use descriptive, snake_case names for all files.
3.  **Optimize**: Ensure file sizes are appropriate for web use.
4.  **Reference**: Update project files to point to the new asset locations.

## Instructions

- Always use the `assets/images/` directory for project images.
- Create subdirectories for specific features (e.g., `assets/images/hero/`, `assets/images/icons/`).
- Document all assets in an `assets/01_README.md` file.

## Resources

- `scripts/optimize_images.py` (Hypothetical script to provide in the future)

## Esencia Original
> **Propósito:** Organizar, catalogar y optimizar activos de imagen generados para uso en proyectos
> **Flujo:** Escannear imágenes → Renombrar con convención → Mover a categoría → Generar metadata

## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `04_Operations/` — Estado
