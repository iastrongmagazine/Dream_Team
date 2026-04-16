# 06_Playground — Pruebas y Experimentos

**Version:** 6.1
**Ultima actualizacion:** 2026-04-15
**Estado:** Activo — Estructura enumerada SOTA

---

## Estructura

```
06_Playground/
|--- 01_Focus_Now_Lab/          # Laboratorio de enfoque y pruebas activas
|    |--- README.md
|    |--- Resumen/               # CVs y resumenes (JAO)
|    +--- Test_Plan.md
|
|--- 02_Hillary_Life_OS/        # Sistema Life OS v1 (estructura base)
|    |--- 01_Quick_Capture/
|    |--- 02_Plan_My_Day/
|    |--- 03_Daily_Notes/
|    |--- 04_Recording_Mode/
|    |--- 05_Returns_Tracker/
|    |--- Plan_Hillary_OS.md     # Plan maestro del Life OS
|    |--- RUNBOOK.md
|    +--- SESSION_SUMMARY.md
|
|--- 03_Hillary_Life_OS_Lab/    # Lab extendido con SDD y OpenSpec
|    |--- 01_Quick_Capture/
|    |--- .atl/                  # SDD artifacts
|    +--- openspec/
|
|--- 04_Maerks/                 # Entorno de testing, validacion y docs legacy
|    |--- 00_Dream_Team_Full.md
|    |--- 00_Test_Anthropic_Harness/
|    |--- 01_Create_Agent_Skills/
|    |--- 02_Skill_Creator/
|    |--- 03_File_Todos/
|    |--- 04_Process_Notes_Legacy/
|    |--- 05_Tests/
|    |--- 06_Reports/
|    |--- 07_Tools/
|    |--- 08_SOP_Prompts/
|    +--- 09_Claude_Code_Learn/
|
|--- 05_New_Skills/             # Skills en evaluacion antes de integrar a 01_Core
|    |--- Top_20_Skills.md       # Ranking de skills prioritarias
|    |--- *.txt                  # Prompts de referencia
|    +--- *.skill                # Archivos .skill listos para instalar
|
+--- 06_Integration_Tests/      # Tests de integracion del sistema
     |--- test_configs.py
     |--- test_runner.py
     +--- test_scripts.py
```

---

## Skills en 05_New_Skills

| Skill                | Estado        | Ubicacion en 01_Core                        |
|----------------------|---------------|---------------------------------------------|
| brand-voice          | Integrado     | `09_Marketing/11_Brand_Voice_Guardian`      |
| content-ideation     | Integrado     | `09_Marketing/12_Content_Ideation`          |
| video-prompt-builder | Integrado     | `20_James_Cameron/01_Video_Prompt_Builder`  |
| offer-and-bio-writer | Integrado     | `09_Marketing/13_Offer_And_Bio_Writer`      |

---

## Proposito

Espacio para **pruebas, experimentos y prototipos** sin afectar el sistema principal (`01_Core/`).

**Regla de oro:** Todo lo que se valida aqui se integra a `01_Core/03_Skills/` o `07_Projects/`. Nada queda huerfano.

---

*Think Different PersonalOS v6.1 — Playground SOTA 2026-04-15*
