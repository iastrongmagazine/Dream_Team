# SDD: Integración "Hillary Life OS" en PersonalOS v6.1

> **Documento de Planificación SDD (Spec-Driven Development)** basado en el ecosistema Gentleman.
> **Objetivo:** Migrar los hallazgos exitosos del laboratorio (`06_Playground/Hillary_Life_OS_Lab`) hacia el núcleo operativo (`01_Core` y `04_Operations`).

---

## 1. Explore (Exploración de Ecosistema Actual)

### Estado Actual
- **Lab Probado:** El laboratorio estructuró correctamente 5 fases extraídas de la metodología de Hilary Gridley: Quick Capture (Yappers API), Plan My Day (Energía), Daily Notes, Recording Mode (Privacidad V2) y Returns Tracker (Generador de Skills pasivo).
- **Core de PersonalOS:** El sistema actual se basa en un Backlog rígido (`BACKLOG.md`), metas estáticas (`GOALS.md`) y flujos muy orientados al desarrollo (SDD/CE), careciendo de flexibilidad nativa para lidiar con fricción logística de vida personal (Life Admin).
- **Sistema de Memoria:** Contamos con Engram (memoria persistente) que puede reemplazar los registros en texto crudo de la "Fase 3" de Life OS.

### Impacto (La regla 10x)
Integrar esto impacta 10x la productividad diaria, combinando el enfoque técnico de la *Máquina de Guerra* con la administración invisible de logística diaria.

---

## 2. Propose (Propuesta de Cambio)

**Visión:**
Integrar un módulo de `Life_Admin` de forma modular y asincrónica al núcleo de PersonalOS, asegurando que las rutinas personales no contaminen el flujo de ingeniería de software, pero se beneficien de las automatizaciones transversales.

**Alcance de la Integración (Scope):**
1. **Infraestructura Life Admin:** Crear contenedor en `04_Operations/10_Life_Admin`.
2. **Transferencia de Skills Mapeadas:** Mover los 5 skills desarrollados en Playgrounds hacia `01_Core/03_Skills/18_Life_Admin/`.
3. **Elevación Global:** Skills genéricos de altísimo valor (`recording_mode` y `returns_tracker`) se separan como herramientas "System Master" (Core) para que operen globalmente.
4. **Acoplamiento con Workflows:** Conectar `plan-my-day` al ritual existente de `22_Morning_Standup.md`.

---

## 3. Spec (Especificaciones de Implementación)

### 3.1. Requerimientos Funcionales (FRs)
- **FR1 (Quick Capture):** Cualquier input que caiga etiquetado deberá ir a `04_Operations/10_Life_Admin/01_Inbox/`.
- **FR2 (Plan My Day):** Debe cruzar el inbox contra `04_Operations/10_Life_Admin/00_Preferences.md` y priorizar descartando basado en la "Regla 10x".
- **FR3 (Yappers API / Engram):** Reemplazar `03_Daily_Notes` con una instrucción global en `AGENTS.md` de invocar `mem_save(type="activity")` rutinariamente al reportar la voz.
- **FR4 (Recording Mode):** Modificar subagentes para que respeten una variable global o *flag* de privacidad en línea de comandos o frontmatter.

### 3.2. Criterios de Aceptación
- Ejecutar `/sdd:plan-my-day` con un archivo de preferencias existente genera un horario sin errores de sintaxis Markdown y añade emojis `🦛` a bloques libres.
- Al reportar una actividad simple, Engram MCP guarda el evento.

---

## 4. Design (Diseño Técnico)

### 4.1. Nueva Topología de Módulos (Filesystem)

```markdown
Think_Different/
├── 01_Core/03_Skills/
│   ├── 13_System_Master/
│   │   ├── recording_mode.md      <- (Elevado desde Lab)
│   │   └── pattern_tracker.md     <- (Evolución de Returns_Tracker)
│   └── 18_Life_Admin/
│       ├── plan_my_day.md
│       └── quick_capture_os.md
│
├── 04_Operations/10_Life_Admin/
│   ├── 00_Preferences.md          <- (Dinámico, editado por IA)
│   ├── 01_Logistics_Inbox/        <- (Markdown crudo para Yappers API)
│   └── 02_Templates/              <- (Plantillas de calendario)
│
└── .agent/03_Workflows/
    └── 22_Morning_Standup.md      <- (Modificado para invocar Yappers API o Plan My Day)
```

### 4.2. Estrategia de Interacción (Privacidad vs Trabajo)
- Se establece una directiva: Tareas o capturas que tengan el tag `[trabajo]` serán parseadas por un Hub Script para mandarlas a `00_Winter_is_Coming/BACKLOG.md`. 
- Todo lo que no tenga tag o posea uno diferente (`[salud]`, `[personal]`) queda blindado en `04_Operations/10_Life_Admin/`.

---

## 5. Tasks (Desglose de Implementación)

### Tareas Nucleares (Fase de Trabajo: `/sdd:apply`)

- [ ] **T1. Setup de Infraestructura:**
  - Crear carpeta `04_Operations/10_Life_Admin/`.
  - Crear `00_Preferences.md` y carpeta `01_Logistics_Inbox/`.
- [ ] **T2. Reubicación de Skills Estratégicos:**
  - Mover y renombrar `Recording_Mode/SKILL.md` a `01_Core/03_Skills/13_System_Master/recording_mode.md`.
  - Mover y refactorizar `Returns_Tracker` como `pattern_tracker.md` al mismo directorio.
- [ ] **T3. Migrar Life Admin Skills:**
  - Mover `Quick_Capture` y `Plan_My_Day` a `01_Core/03_Skills/18_Life_Admin/`.
- [ ] **T4. Acoplamiento de Standup:**
  - Editar `.agent/03_Workflows/22_Morning_Standup.md` para incluir la llamada al Skill `plan-my-day`.
- [ ] **T5. Integración de Engram "Yappers":**
  - Añadir en `AGENTS.md` (y su contraparte local) la norma de que las notas diarias se gestionan directamente vía Engram (`mem_save`), descontinuando la necesidad del folder `03_Daily_Notes`.

---

## 6. Verify (Plan de Validación)

- Cargar 3 tareas "basura" en el Inbox.
- Ejecutar de prueba la carga de `Morning_Standup.md`.
- Verificar que el asistente (yo) logre particionar tareas grandes en bloques de 15 minutos alineados con la energía dictada en `Preferences`.
- Ejecutar *Auditor_Hub* (`gr`) para certificar pureza estructural de `01_Core`.

---

> **Requiere tu aprobación:** ¿Deseas que proceda con este plan ejecutando directamente las tareas (creación y movimiento de archivos) o hay alguna modificación que quieras hacer sobre qué skills se elevan a System Master vs los que se quedan en Life Admin?
