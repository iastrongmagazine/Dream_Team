# CTX_005 — Sistema SOTA de Skills v2.0 — 2026-03-20

## Resumen

Reorganización completa del sistema de PersonalOS.

### 🔐 FUENTE DE VERDAD (Source of Truth)

| Nivel | Ubicación | Propósito |
|-------|-----------|-----------|
| **Proyecto** | `01_Core/` | Fuente de verdad para TODO el proyecto |
| **Skills** | `01_Core/03_Skills/` | 160+ skills específicas |

> ⚠️ **IMPORTANTE:** Para OpenCode, `01_Core/` es la carpeta raíz. Las skills están en `01_Core/03_Skills/`.

- --

## Arquitectura

```
01_Core/                    (MAESTRO - Todo el sistema)
├── 03_Skills/             (160+ skills organizadas)
├── 03_Agents/             (Dream Team + Specialists)
├── 00_Workflows/          (26 workflows)
└── 05_Mcp/                (27 MCPs configurados)
```

### Estructura Actual de Skills (`01_Core/03_Skills/`)

| #  | Carpeta | Skills | Propósito |
|----|---------|--------|-----------|
| 00 | `00_Compound_Engineering` | CE Workflows | Compound Engineering |
| 00 | `00_Skill_Auditor` | Auditoría | Validación de skills |
| 01 | `01_Agent_Teams_Lite` | 11 | SDD phases |
| 02 | `02_Project_Manager` | 9 | PM workflows |
| 03 | `03_Product_Manager` | 9 | PRD, Planning |
| 04 | `04_Product_Design` | 13 | Diseño premium |
| 05 | `05_Vibe_Coding` | 18 | Dev Frameworks |
| 06 | `06_Testing` | 18 | Testing + GGA |
| 07 | `07_DevOps` | 13 | DevOps |
| 08 | `08_Personal_Os` | 9 | Personal OS |
| 09 | `09_Marketing` | 11 | Marketing |
| 10 | `10_Backup` | 5 | Legacy |
| 11 | `11_Doc_Processing` | 4 | Documentos |
| 12 | `12_N8N` | 7 | n8n Automation |
| 13 | `13_System_Master` | 5 | Sistema |
| 14 | `14_Anthropic_Harness` | 9 | Anthropic Patterns |

**Total: 160+ skills**

- --

## 📋 REGLA DEL SISTEMA

> **Para OpenCode:** `01_Core/` es la fuente de verdad del proyecto.
> **Para Skills específicamente:** `01_Core/03_Skills/`

- --

## Pendientes

1. QMD Embeddings (~2GB)
2. QMD MCP Integration

- --

*Actualizado: 2026-03-27 — Corregido para usar 01_Core/ como fuente de verdad*
