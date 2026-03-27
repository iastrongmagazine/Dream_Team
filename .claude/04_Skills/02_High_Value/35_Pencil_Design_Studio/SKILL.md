# 🎨 Skill 35: Pencil Design Studio (AI-Assisted Design & UI/UX Orchestra)
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
