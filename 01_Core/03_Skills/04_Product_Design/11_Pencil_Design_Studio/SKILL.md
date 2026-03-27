# 🎨 Skill 35: Pencil Design Studio (AI-Assisted Design & UI/UX Orchestra)

## Esencia Original
> **Propósito:** Orquestar flujos de diseño asistido por IA usando Pencil.dev vía MCP — prototipos visuales, componentes UI, infinite canvas.
> **Flujo:** Conceptualizar → Generar con MCP → Refinar en canvas → Validar estilo → Implementar código

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: No verificar MCP server instalado
  - **Por qué**: Herramientas MCP no funcionan
  - **Solución**: Verificar `@open-pencil/mcp` está instalado

- **[ERROR]**: Saltar validación de estilo
  - **Por qué**: Diseños no coinciden con estándares HSL/Glassmorphism
  - **Solución**: Siempre validar contra reglas antes de implementar

- **[ERROR]**: No usar Infinite Canvas correctamente
  - **Por qué**: Pierdes contexto visual completo
  - **Solución**: Usar canvas para relaciones entre pantallas

- **[ERROR]**: Implementar sin sync
  - **Por qué**: Código y diseño se desincronizan
  - **Solución**: Usar export_to_code para sync final

## 📁 Progressive Disclosure

> Para información detallada:
- [references/mcp-tools.md](references/mcp-tools.md) — Herramientas MCP
- [references/design-workflow.md](references/design-workflow.md) — Workflow de diseño

## 🛠️ Scripts

- [scripts/generate-screen.py](scripts/generate-screen.py) — Genera pantalla desde prompt

## 💾 State Persistence

Guardar diseños en:
- `04_Docs/designs/pencil/YYYY-MM-DD-<name>.pen`
- Exportar código a `src/components/`

## Overview
Esta Skill permite la orquestación de flujos de diseño asistido por IA utilizando **Pencil.dev** y su servidor MCP. Facilita la creación de prototipos visuales, componentes UI y sistemas de diseño directamente desde el código, integrando el concepto de "Infinite Canvas" en el flujo del desarrollador.

## Triggers
- "Diseña una pantalla para [X]"
- "Crea un componente de [Y] con estilo Premium"
- "Genera un prototipo de flujo para [Z]"
- "Convierte este diseño de Pencil a código"

## Tooling (MCP)
- **Servidor**: `@open-pencil/mcp`
- **Herramientas**:
  - `generate_screen`: Crea pantallas completas basadas en prompts.
  - `modify_component`: Ajusta estilos y propiedades de componentes existentes.
  - `export_to_code`: Genera snippets de código (React/Tailwind/CSS) desde el diseño.

## Workflow Premium
1. **Conceptualización**: Definición de la arquitectura visual basada en el *Manifesto de Diseño*.
2. **Generación IA**: Uso de herramientas MCP para crear estructuras base en archivos `.pen`.
3. **Refinamiento Visual**: El usuario o el agente manipulan el diseño en el "Infinite Canvas" de Pencil.
4. **Validación de Estilo**: Comprobación contra reglas de HSL, Glassmorphism y espaciado.
5. **Implementación**: Sincronización final del diseño con el repositorio de código.

---
*Alineado con el Estándar AIPM: "Diseño indestructible, código de autor."*
