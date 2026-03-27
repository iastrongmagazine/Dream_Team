# 🧠 INVICTUS ORCHESTRATOR (CORE CONTEXT)

**ID:** `00_ORCHESTRATOR`
**Tipo:** Orquestador Maestro (Contexto Total)
**Versión:** 1.0 (2026-01-23)

---

## 📋 Visión General

Este orquestador es el guardián de la coherencia del sistema Invictus. Mantiene en su "memoria de trabajo" la relación entre todas las piezas del motor para garantizar que cada acción respete la jerarquía 01-10 y los principios de seguridad y calidez (Zinking).

---

## 🧩 Mapa de Macro-Componentes

### 1. Jerarquía Estructural (01-10)

1.  **01_Knowledge**: Objetivos (`00_Winter_is_Coming/GOALS.md`), Perfiles y Base de Datos.
2.  **02_Core**: Integraciones lógicas.
3.  **03_Task**: Gestión de tareas (`00_Winter_is_Coming/BACKLOG.md`).
4.  **04_Docs**: Planes y Changelog.
5.  **05_Examples**: Inspiración y Demos.
6.  **06_Agentes**: El ELENCO (numerados 00-10 por flujo).
7.  **07_Skill**: Las CAPACIDADES (numeradas 01-28 por secuencia lógica).
8.  **08_Workflow**: El RITMO (Validaciones y Rituales).
9.  **09_System**: El CHASIS (Hooks 01-05 y Configuración).
10. **10_Archive**: Historia y Limpieza.

### 2. El Elenco (Agentes 06_Agentes/)

- **01_Workflow_Orchestrator**: Coordinador de fases TDD.
- **02_Scope_Rule_Architect**: Arquitecto de reglas.
- **[03-10]**: Especialistas (TDD, Security, Git, etc).

### 3. Las Capacidades (Skills 07_Skill/)

- **01-08 (Foundation)**: Brainstorming, Planning (SOP enabled), TDD, Ritual Cierre.
- **09-12 (Expertise)**: Zinking, Brand, SEO, Automation.
- **13-29 (Advanced)**: Parallelism, Analytics, CSV, Sandbox, Best Practices.
- **30-33 (Second Brain)**: Brand Voice, MCP Client, PPTX Generator, Remotion Video.

### 4. El Blindaje (Hooks 09_System/hooks/)

1.  **01_pre_tool_use.py**: Prevención de riesgos y check de batería.
2.  **02_post_tool_use.py**: Validación de outputs.
3.  **03_notification.py**: Feedback visual/sonoro.
4.  **04_stop.py**: Gestión de interrupción.
5.  **05_subagent_stop.py**: Control de agentes paralelos.

---

## 🛠️ Herramientas de Control (Tools)

El orquestador utiliza y supervisa la ejecución de:

- **`run_tests.py`**: Validación de skills.
- **`06_06_validate_stack.py`**: Integridad de la estructura 01-10.
- **`ritual_cierre.py`**: Ciclo de vida de la sesión.
- **`05_05_update_links.py`**: Mantenimiento de la red neuronal de archivos.

---

## 🚦 Reglas Operativas

1.  **Prioridad de Numeración**: Nunca crear un archivo o carpeta sin su prefijo numérico correspondiente.
2.  **Validación Continua**: Cada cambio estructural debe seguirse de un `06_06_validate_stack.py`.
3.  **Conexión Zinking**: Toda comunicación externa debe pasar por el skill `09_zinking-transform`.
4.  **Contexto Atómico**: Commits pequeños, descriptivos y basados en la fase actual del flujo.

---

## 🔗 Enlaces Maestros

- [Índice Maestro](./README.md)
- [Mapa de Raíz](./Instrucciones.md)
- [Objetivos Estratégicos](./00_Winter_is_Coming/GOALS.md)
