---
name: Best_Practices
description: QUÉ HACE: Implementa arquitecturas de coordinación explícita y scaffolding basado en tareas atómicas y DAGs. CUÁNDO SE EJECUTA: Al estructurar proyectos complejos para asegurar orden, blindaje y seguimiento total.
---

# Best Practices & Advanced Scaffolding 🏆

Skill definitiva para la implementación de arquitecturas de coordinación explícita y automatización de procesos siguiendo los estándares de **Claude Code Tasks**.

## 🎯 Objetivo

Eliminar la coordinación implícita y los errores de contexto mediante la creación de estructuras de proyectos basadas en **DAGs (Directed Acyclic Graphs)**, tareas atómicas y ejecución en oleadas (waves).

## 🛠️ Herramientas y Scripts

- **`python_mcp_skill1.py`**: Servidor MCP que permite automatizar el scaffolding de proyectos con tracking de tareas integrado.
- **`python_setup_files1.py`**: Utilidad para la configuración rápida de entornos de desarrollo blindados.

## 🔄 Workflow de Mejores Prácticas

1.  **Fundación (Wave 1)**:
    - Definir estructura de carpetas mínima.
    - Configurar `tasks.json` con el DAG de misiones.
    - Establecer reglas de blindaje (`.cursorrules`, `.claudecode.json`).
2.  **Configuración (Wave 2)**:
    - Inyectar dependencias core.
    - Establecer hooks de validación automática.
3.  **Ejecución (Wave 3)**:
    - Procesar tareas de forma atómica (< 100 líneas por cambio).
    - Validar en cada paso con hooks de stop/post-tool.

## 💡 Principios de Diseño Invictus

- **Coordinación Explícita**: Todo estado debe ser consultable en archivos JSON/MD.
- **Contexto Fresco**: Tratar cada tarea como una sesión independiente para evitar alucinaciones por "deriva de contexto".
- **Blindaje Total**: El sistema debe detectar y auto-sanar errores de configuración antes de que afecten la lógica de negocio.

## 🚀 Comandos de la Skill

Para crear un nuevo proyecto coordinado:

```bash
python 07_Skill/29_Best_Practices/scripts/python_mcp_skill1.py --new [ProjectName]
```

Para auditar el estado de mejores prácticas:

```bash
python 07_Skill/29_Best_Practices/scripts/python_mcp_skill1.py --audit
```

---

> [!IMPORTANT]
> Esta skill no es solo una utilidad, es un estándar arquitectónico. Su uso es obligatorio para proyectos de escala "Bunker" o superiores.
