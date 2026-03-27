# CTX_005 — Sistema SOTA de Skills v2.0 — 2026-03-20

## Resumen

Reorganización completa del sistema de skills de PersonalOS. `.agent/02_Skills/` es ahora el Source of Truth con jerarquía por prioridad y sync unidireccional a `.cursor/`.

- --

## Arquitectura

```
.agent/02_Skills/ (MAESTRO - 287 SKILL.md)
    ↓
.cursor/02_Skills/ (ESPEJO - sincronizado)
```

### Jerarquía por Prioridad

| #     | Carpeta               | Skills     | Propósito                       |

|-----------------------------|---------------------------------------------|----------------------------------|-------------------------------------------------------|
| 1                           | 01_Core                                     | 3                                | Sistema (Fork, Parallel, Git)                         |
| 2                           | 02_High_Value                               | 31                               | Workflows especializados                              |
| 3                           | 03_Utilities                                | 30                               | Herramientas                                          |
| 4                           | 04_Agent_Teams_Lite                         | 10                               | SDD phases                                            |
| 5                           | 05_Gentleman                                | 41                               | Ecosistema                                            |
| 6                           | 07_Every                                    | 91                               | TODO consolidado                                      |
| 7                           | 08_Taste_Skills                             | 5                                | Diseño premium                                        |

- --

## SOTA Testing Suite

8 skills de última generación en `07_Every/05_Utilities/`:
- Observability, Evaluation, Test_Coverage, Integration_Testing, E2E_Testing, Edge_Case, RTM, MCP_Integration

- --

## Sync Script

* *Ubicación:** `04_Engine/08_Scripts_Os/55_Sync_Skills.py`

```bash
python 04_Engine/08_Scripts_Os/55_Sync_Skills.py --confirm
```

- --

## Documentación

| Archivo                                                        | Descripción                               |
|----------------------------------------------------------------|-------------------------------------------|
| `Sistema_SOTA_Skills.md`                                       | Guía maestra                              |
| `Skills_Top_20.md`                                             | Rankings v2.0                             |
| `Reporte_Skills_Duplicados_vs_SOTA.md`                         | Análisis completo                         |

- --

## Pendientes

1. QMD Embeddings (~2GB)
2. QMD MCP Integration

- --

* Actualizado: 2026-03-20*
