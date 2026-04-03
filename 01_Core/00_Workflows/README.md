# 🗺️ Workflows — PersonalOS

Workflows reutilizables del sistema. Invocar según el contexto de la tarea.

## 🌅 Workflows de Inicio/Cierre de Sesión

| Workflow                                         | Cuándo usar                        | Tiempo   |
|--------------------------------------------------|------------------------------------|----------|
| [Génesis — Iron Man](01_Iron_Man_Gen.md)         | Inicio de cada sesión              | 2 min    |
| [Ritual de Cierre](12_Ritual_Cierre_Protocol.md) | Fin de cada sesión                 | 3 min    |
| [Context Recovery](13_Context_Recovery.md)       | Contexto degradado / AI confundido | 5 min    |

## 📅 Workflows Diarios

| Workflow                                       | Cuándo usar                             | Tiempo   |
|------------------------------------------------|-----------------------------------------|----------|
| [Morning Standup](23_Morning_Standup.md)       | Inicio del día — elegir foco            | 2 min    |
| [Backlog Processing](21_Backlog_Processing.md) | Fin del día o cuando se acumula backlog | 5-10 min |

## 📆 Workflows Semanales

| Workflow                                         | Cuándo usar                  | Tiempo    |
|--------------------------------------------------|------------------------------|-----------|
| [Weekly Review](00_Weekly_Review.md)             | Viernes PM o Domingo/Lunes   | 15-30 min |
| [System Health Audit](13_System_Health_Audit.md) | Revisión semanal del sistema | 10 min    |

## 🚀 Workflows de Ingeniería Autónoma (LFG)

| Workflow                                          | Cuándo usar                                           | Pasos   |
|---------------------------------------------------|-------------------------------------------------------|---------|
| [LFG Lite — Ant-Man](06_AntMan_Lfg_Lite.md)       | Tasks P2/P3, bugs simples, mejoras menores            | 12      |
| [LFG Pro — Doctor Strange](07_Doc_Strange_Lfg.md) | Tasks P0/P1, features nuevas, cambios arquitectónicos | 18      |

## 🧠 Workflows de Planificación

| Workflow                                           | Cuándo usar                           |
|----------------------------------------------------|---------------------------------------|
| [Brainstorm — Spider-Man](01_Spider_Brainstorm.md) | Explorar opciones antes de planear    |
| [Plan — Professor X](02_Professor_X_Plan.md)       | Transformar idea en plan estructurado |
| [AI Task Template](10_AI_Task_Template.md)         | Plantilla completa para tareas IA     |
| [Redacción de Docs](09_Redaccion_de_Docs.md)       | Memo estratégico de una página        |

## ⚙️ Workflows de Ejecución y Calidad

| Workflow                               | Cuándo usar                                |
|----------------------------------------|--------------------------------------------|
| [Work — Thor](04_Thor_Work.md)         | Ejecutar un plan con checkpoints           |
| [Review — Vision](03_Vision_Review.md) | Revisión exhaustiva de código (13 agentes) |
| [Compound — Hulk](05_Hulk_Compound.md) | Documentar soluciones para compounding     |
| [Validar Reglas](08_Validar_Reglas.md) | Verificar cumplimiento de Cursor Rules     |

## ⚡ Workflows de Productividad Personal

| Workflow                                     | Cuándo usar                             | Tiempo     |
|----------------------------------------------|-----------------------------------------|------------|
| [Captura Rápida](14_Captura_Rapida.md)       | Idea, insight o tarea nueva → BACKLOG   | <60 seg    |
| [Deep Work Session](15_Deep_Work_Session.md) | Ejecutar tarea P0/P1 con foco total     | 45-120 min |
| [Ship It](16_Ship_It.md)                     | Proyecto terminado → publicado al mundo | 45 min     |

## ✍️ Workflows de Contenido

| Workflow                                       | Cuándo usar                           |
|------------------------------------------------|---------------------------------------|
| [Content Generation](00_Content_Generation.md) | Escribir en voz auténtica del usuario |

---

## ⚡ Referencia Rápida — Prompts Comunes

**Inicio de día:**
- "¿En qué debo trabajar hoy?" → `00_Morning_Standup`
- "Carga el contexto del sistema" → `01_Iron_Man_Gen`

**Durante el día:**
- "Procesa mi backlog" → `00_Backlog_Processing`
- "Implementa [feature] de cabo a rabo" → `06_AntMan_Lfg_Lite` o `07_Doc_Strange_Lfg`
- "Revisa este código" → `03_Vision_Review`

**Fin del día:**
- "Cierra la sesión" → `11_Ritual_Cierre_Protocol`
- "El AI está confundido" → `12_Context_Recovery`

**Semanal:**
- "Revisión semanal" → `00_Weekly_Review`
- "Audita el sistema" → `13_System_Health_Audit`
