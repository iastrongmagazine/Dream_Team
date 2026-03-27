# Scripts Index — PersonalOS UltraThink

> **Total Scripts:** 89 (numerados 00-95, con gaps) + config = 90 archivos
> **Last Updated:** 2026-03-26
> **Validation:** Pure Green Audit v6.1 — LOS ARCHIVOS NO MIENTAN

## 📊 Estado Real (Audit 2026-03-24)

| Rango   | Cantidad   | Scripts           |
|---------|------------|-------------------|
| 00-08   | 9          | Core workflows    |
| 09-19   | 11         | Operations        |
| 20      | 1          | Analytics         |
| 22-34   | 13         | AIPM + Quality    |
| 35-40   | 6          | Quality           |
| 43-50   | 8          | System            |
| 51-61   | 11         | System + Git      |
| 63-78   | 17         | System + Workflow |
| 79-86   | 8          | Observability     |
| 87-90   | 4          | Workflows         |
| config  | 1          | config_paths.py   |

## Gaps Confirmados (NO existen)

| #   | Razón                             |
|-----|-----------------------------------|
| 21  | Oil drilling legacy (archivado)   |
| 41  | Oil drilling legacy (archivado)   |
| 42  | Oil drilling legacy (archivado)   |
| 62  | Pollution placeholder (eliminado) |

## 🏗️ Orchestration Hubs (Raíz 08_Scripts_Os)

| #   | Script                  | Purpose                            | Category      |
|-----|-------------------------|------------------------------------|---------------|
| 01  | Auditor_Hub.py          | Orquestador de Auditorías          | Orchestration |
| 02  | Git_Hub.py              | Orquestador de Git/Repos           | Orchestration |
| 03  | AIPM_Hub.py             | Orquestador de métricas AIPM       | Orchestration |
| 04  | Ritual_Hub.py           | Orquestador de Rituales (Start/End)| Orchestration |
| 05  | Validator_Hub.py        | Orquestador de Validaciones        | Orchestration |
| 06  | Tool_Hub.py             | Orquestador de Herramientas        | Orchestration |
| 07  | Integration_Hub.py      | Orquestador de Integraciones       | Orchestration |
| 08  | Workflow_Hub.py         | Orquestador de Workflows SOTA      | Orchestration |
| 09  | Data_Hub.py             | Orquestador de Datos/Sync          | Orchestration |
| 10  | General_Hub.py          | Orquestador General                | Orchestration |

## Scripts Activos (Legacy_Backup)

| #   | Script                          | Purpose                                     | Category      |
|-----|---------------------------------|---------------------------------------------|---------------|
| 00  | Context_Reset.py                | Reset contexto del AI                       | Core          |
| 01  | Spider_Brainstorm.py            | Lluvia de ideas colaborativa                | Workflow      |
| 02  | Professor_X_Plan.py             | Planificación estratégica                   | Workflow      |
| 03  | Thor_Work.py                    | Ejecución de tareas                         | Workflow      |
| 04  | Vision_Review.py                | Revisión exhaustiva código                  | Quality       |
| 05  | Hulk_Compound.py                | Compounding de inteligencia                 | Compound      |
| 06  | AntMan_Lfg_Lite.py              | Ciclo autónomo lite (12 pasos)              | Workflow      |
| 07  | Doc_Strange_Lfg.py              | Ciclo autónomo completo (18 pasos)          | Workflow      |
| 08  | Ritual_Cierre.py                | Cierre de sesión seguro                     | Ritual        |
| 09  | Backlog_Triage.py               | Organización de backlog                     | Operations    |
| 10  | AI_Task_Planner.py              | Enriquece tareas con AI                     | Operations    |
| 11  | Sync_Notes.py                   | Sincroniza notas                            | Sync          |
| 12  | Update_Links.py                 | Mantiene referencias                        | Sync          |
| 13  | Validate_Stack.py               | Valida dependencias                         | System        |
| 14  | Morning_Standup.py              | Standup matutino                            | Ritual        |
| 15  | Weekly_Review.py                | Review semanal                              | Ritual        |
| 16  | Clean_System.py                 | Limpia archivos                             | System        |
| 17  | Ritual_Dominical.py             | Ritual dominical                            | Ritual        |
| 18  | Generacion_Contenido.py         | Generación de contenido                     | Marketing     |
| 19  | Generate_Progress.py            | Reporte de progreso                         | Analytics     |
| 20  | Master_Analytics_Factory.py     | Analytics avanzado                          | Analytics     |
| 21  | Skill_Script_Mapper.py          | Mapea skills↔scripts (RE-ID v6.1)           | Utilities     |
| 22  | AIPM_Trace_Logger.py            | Logging de traces                           | AIPM          |
| 23  | AIPM_Evaluator.py               | Evaluador AIPM                              | AIPM          |
| 24  | AIPM_Interview_Sim.py           | Simulador entrevistas                       | AIPM          |
| 25  | Token_Budget_Guard.py           | Vigila budget tokens                        | AIPM          |
| 26  | RAG_Optimizer_Pro.py            | Optimizador RAG                             | AIPM          |
| 27  | Probabilistic_Risk_Audit.py     | Auditoría de risks                          | AIPM          |
| 28  | AIPM_Control_Center.py          | Centro de control                           | AIPM          |
| 29  | Guardrails_Service.py           | Validación de seguridad                     | AIPM          |
| 30  | AIPM_Consolidated_Report.py     | Reporte consolidado                         | AIPM          |
| 31  | Silicon_Valley_Auditor.py       | Auditor SV                                  | Quality       |
| 32  | Multi_Agent_Final_Validation.py | Validación multi-agente                     | Quality       |
| 33  | Parallel_Audit_Pro.py           | Auditoría paralela                          | Quality       |
| 34  | Skill_Auditor.py                | Audita skills                               | Quality       |
| 35  | Beautify_Tables.py              | Embellece tablas                            | Beauty        |
| 36  | Beauty_Doc.py                   | Embellece documentos                        | Beauty        |
| 37  | Linter_Autofix.py               | Auto-fix de estilo                          | Quality       |
| 38  | Recap_Planning.py               | Recap + planning                            | Planning      |
| 39  | Repair_Corruption.py            | Repara corrupción                           | System        |
| 40  | Validate_Rules.py               | Valida reglas                               | Quality       |
| 43  | Marketing_Skills_Distributor.py | Distribuidor marketing                      | Marketing     |
| 44  | Auto_Compound_Intelligence.py   | Compound auto                               | Compound      |
| 45  | Migration_Master.py             | Migraciones                                 | System        |
| 46  | Sync_MCP_OpenCode.py            | Sync MCPs                                   | Sync          |
| 47  | Verify_OpenCode_Status.py       | Verifica OpenCode                           | System        |
| 48  | Design_Critique_Expert.py       | Crítica de diseño                           | Quality       |
| 49  | Path_Optimization.py            | Optimiza paths                              | System        |
| 50  | System_Health_Monitor.py        | Monitor de salud                            | System        |
| 51  | Commit_Lint_Guard.py            | Valida commits                              | Git           |
| 52  | Safe_Commit.py                  | Commit seguro                               | Git           |
| 53  | Structure_Auditor.py            | Auditor estructura                          | Quality       |
| 54  | Commit_Guard.py                 | Compound commit                             | Git           |
| 55  | Sync_Skills.py                  | Sync skills                                 | Sync          |
| 56  | Organize_Solutions.py           | Organiza soluciones                         | Sync          |
| 57  | Repo_Sync_Auditor.py            | Auditor de repos                            | Quality       |
| 58  | Batch_Beautify_README.py        | Beautify batch                              | Beauty        |
| 59  | Task_Classifier.py              | Clasificador tareas                         | Operations    |
| 60  | Fast_Vision.py                  | Visión rápida                               | Quality       |
| 61  | MCP_Health_Check.py             | Health check MCP                            | System        |
| 63  | Audit_Sync_Master.py            | Auditor sync                                | Quality       |
| 64  | Campanilla.py                   | Notificaciones                              | System        |
| 65  | CTX_Generator.py                | Generador ctx                               | Operations    |
| 66  | Alert_Manager.py                | Manager alertas                             | System        |
| 67  | Retry_Decorator.py              | Decorador retry                             | Utilities     |
| 68  | Benchmark_Baseline.py           | Benchmark                                   | System        |
| 69  | Health_Check_Pro.py             | Health check pro                            | System        |
| 70  | Ship_It.py                      | Validaciones pre-ship                       | Ship          |
| 71  | Script_Template.py.deprecated | Plantilla base para scripts (Legacy)      | Utilities     |
| 72  | Validate_Skills_Duplicates.py   | Valida duplicados                           | Quality       |
| 73  | Avengers_Workflow_v3.py         | Workflow Avengers SOTA v3                   | Workflow      |
| 74  | MCP_Top_Tests.py                | Tests MCP                                   | System        |
| 75  | Update_QMD_Index.py             | Update index                                | System        |
| 76  | Obsidian_Exporter.py            | Exporta a Obsidian                          | Sync          |
| 77  | Notify_System.py                | Sistema notificaciones                      | System        |
| 78  | Context_Switcher.py             | Switcher contexto                           | Utilities     |
| 79  | System_Guardian.py              | Guardian sistema                            | Utilities     |
| 80  | Edge_Case_Validator.py          | Validador edge cases                        | Testing       |
| 81  | RTM_Generator.py                | Generador RTM                               | Testing       |
| 82  | Health_Monitor.py               | Monitor salud                               | Observability |
| 83  | Universal_Parser.py             | Parser universal (RE-ID v6.1)               | Utilities     |
| 84  | Batch_Parser.py                 | Parser batch                                | Utilities     |
| 85  | Resumen_Extractor.py            | Extrae resúmenes                            | Utilities     |
| 86  | -                               | - VACANTE / PLACEHOLDER -                   | -             |
| 87  | Iron_Man_Gen.py                 | Genesis (Iron Man Boot) workflow            | Core          |
| 88  | Frontend_Premium.py             | Frontend Premium UI workflow                | Workflow      |
| 89  | Redaccion_de_Docs.py            | Strategy Memo generator                     | Writing       |
| 90  | Deep_Work_Session.py            | Deep Work session protocol                  | Productivity  |
| 95  | Documentation_Updater.py        | Actualizador masivo de docs (Pure Green)    | System        |

---

## 📁 Other Scripts

| Script                | Purpose            | Location                |
|-----------------------|--------------------|-------------------------|
| config_paths.py       | Rutas del proyecto | Root                    |
| setup_dependencies.py | Instala deps       | 04_Engine/07_Installer/ |
| detect_machine.py     | Detecta máquina    | 04_Engine/07_Installer/ |
| configure_paths.py    | Configura paths    | 04_Engine/07_Installer/ |
| installer.py          | Instalador         | 04_Engine/07_Installer/ |
| test_*.py             | Tests              | 04_Engine/05_Tests/     |
| generate_tree.py      | Genera árbol       | 04_Engine/04_Tools/     |
| cleanup_tabs.py       | Limpia tabs        | 04_Engine/04_Tools/     |

---

## Usage

```bash
# Ejecutar script
python 04_Engine/08_Scripts_Os/14_Morning_Standup.py

# Con argumentos
python 04_Engine/08_Scripts_Os/54_Commit_Guard.py --apply -m "feat: desc"

# Dry run
python 04_Engine/08_Scripts_Os/55_Sync_Skills.py
```

---

## Validación

> ⚠️ SIEMPRE verificar con `ls -1 04_Engine/08_Scripts_Os/*.py | wc -l` antes de reportar números.

*Actualizado: 2026-03-24 — UltraThink Audit Protocol*
