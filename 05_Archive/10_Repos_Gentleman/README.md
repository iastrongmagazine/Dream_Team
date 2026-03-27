# 10_Repos_Gentleman

---
### ⚙️ Gentleman README Template
- **Propósito:** Repositorios externos de referencia (Gentleman.Dots, recursos externos) integrados al PersonalOS para desarrollo frontend de calidad premium.
- **Estado:** Active
- **Dependencias:** Ninguna (recursos externos clonados/añadidos)
- **Dueño/Agente:** AI Agent (Think Different)
- **Ref:** Ver `00_Core/AGENTS.md` para configuración de skills.
- **Nota importante:** Estos son **copias locales**, NO submodules de git.

---

## 📚 Repositorios Oficiales Gentleman-Programming

> **NOTA:** Estos repos se actualizan frecuentemente. Verificar versiones antes de clonar.

| Repo | URL GitHub | Versión Actual | Notas |
|------|------------|----------------|-------|
| **engram** | https://github.com/Gentleman-Programming/engram | v1.10.4 | Memoria persistente |
| **gentle-ai** | https://github.com/Gentleman-Programming/gentle-ai | v1.7.18 | Ecosistema configurador |
| **Gentleman.Dots** | https://github.com/Gentleman-Programming/Gentleman.Dots | v2.9.2 | Dotfiles + config |
| **agent-teams-lite** | https://github.com/Gentleman-Programming/agent-teams-lite | v4.0.0+ | SDD workflow |
| **gentleman-guardian-angel** | https://github.com/Gentleman-Programming/gentleman-guardian-angel | v2.7.3 | Code review AI |
| **gentleman-skills** | https://github.com/Gentleman-Programming/gentleman-skills | - | Skills curadas |
| **qmd** | https://github.com/tobi/qmd | v2.0.1 | Búsqueda local (NO clonado - instalar global) |

### Repositorios Adicionales

| Repo | URL GitHub | Notas |
|------|------------|-------|
| **taste-skill** | https://github.com/Leonxlnx/taste-skill | Diseño premium |
| **obsidian-digital-garden** | https://github.com/oleeskild/obsidian-digital-garden | Publicación notas |
| **compound-engineering-plugin** | https://github.com/EveryInc/compound-engineering-plugin | Compound Engineering (NUEVO) |

---

## 📦 Estado de Clonación (2026-03-25)

| Repo | Clonado | Ubicación |
|------|---------|-----------|
| agent-teams-lite | ✅ | `10_Repos_Gentleman/agent-teams-lite/` |
| Gentleman.Dots | ✅ | `10_Repos_Gentleman/Gentleman.Dots/` |
| engram | ✅ | `10_Repos_Gentleman/engram/` |
| gentle-ai | ✅ | `10_Repos_Gentleman/gentle-ai/` |
| gentleman-guardian-angel | ✅ | `.agent/05_GGA/` (local) |
| gentleman-skills | ✅ | `10_Repos_Gentleman/gentleman-skills/` |
| obsidian-digital-garden | ✅ | `10_Repos_Gentleman/obsidian-digital-garden/` |
| qmd | ⚠️ | NO clonado - usar `bun add -g @tobilu/qmd` |

### Taste-Skills (Leonxlnx)

> **Repo Original:** https://github.com/Leonxlnx/taste-skill
> **⭐ Stars:** 3.9k | **🍴 Forks:** 314

> **IMPORTANTE:** Las Taste-Skills están instaladas en `.cursor/` y `.agent/`, NO en este directorio.

| Skill            | Propósito                    | Cuándo Usar                     |
| ---------------- | ---------------------------- | ------------------------------- |
| `taste-skill`    | Diseño premium desde cero    | Webs, landing pages             |
| `soft-skill`     | Look expensive               | Proyectos premium, invitaciones |
| `minimalist-skill` | Estilo Notion/Linear         | Dashboards, interfaces clean    |
| `redesign-skill` | Mejorar proyectos existentes | Actualizar proyectos legacy     |
| `output-skill`   | Evita código incompleto      | SIEMPRE                         |

### Configuración (Taste-Skills)

```markdown
DESIGN_VARIANCE (1-10)
├── 1-3: Clean, centered, standard grids
├── 4-7: Overlapping elements, varied sizes
└── 8-10: Asymmetric, lots of whitespace

MOTION_INTENSITY (1-10)
├── 1-3: Almost none, simple hover
├── 4-7: Fade-ins, smooth scrolling
└── 8-10: Magnetic effects, spring physics

VISUAL_DENSITY (1-10)
├── 1-3: Big and spacious, luxury feel
├── 4-7: Normal spacing, typical app
└── 8-10: Dense and compact, dashboards
```

## Estructura

```
.cursor/02_Skills/11_Taste_Skills/     # Para Cursor IDE
└── taste-skill/                        # Diseño principal
    ├── taste-skill/SKILL.md            # Diseño premium desde cero
    ├── soft-skill/SKILL.md             # Look premium/lujoso
    ├── minimalist-skill/SKILL.md       # Estilo Notion/Linear
    ├── redesign-skill/SKILL.md         # Mejorar existentes
    └── output-skill/SKILL.md           # Código completo

.agent/02_Skills/11_Taste_Skills/       # Para OpenCode
└── taste-skill/                        # Diseño principal
    ├── taste-skill/SKILL.md            # Diseño premium desde cero
    ├── soft-skill/SKILL.md             # Look premium/lujoso
    ├── minimalist-skill/SKILL.md       # Estilo Notion/Linear
    ├── redesign-skill/SKILL.md         # Mejorar existentes
    └── output-skill/SKILL.md           # Código completo
```

## Uso

### Referencia Directa (Cursor/Claude Code)

```markdown
# Diseño principal (Cursor):
@.cursor/02_Skills/11_Taste_Skills/taste-skill/SKILL.md

# Look expensive (Cursor):
@.cursor/02_Skills/11_Taste_Skills/soft-skill/SKILL.md

# Minimalist Notion/Linear (Cursor):
@.cursor/02_Skills/11_Taste_Skills/minimalist-skill/SKILL.md

# Mejorar proyectos (Cursor):
@.cursor/02_Skills/11_Taste_Skills/redesign-skill/SKILL.md

# Output completo (Cursor):
@.cursor/02_Skills/11_Taste_Skills/output-skill/SKILL.md

# Diseño principal (OpenCode):
@.agent/02_Skills/11_Taste_Skills/taste-skill/SKILL.md

# Look expensive (OpenCode):
@.agent/02_Skills/11_Taste_Skills/soft-skill/SKILL.md
```

## Regla de Uso (OBLIGATORIO)

> **Para TODO trabajo frontend, USAR SIEMPRE las Taste-Skills:**
> - ✅ Webs
> - ✅ Landing pages
> - ✅ Invitaciones
> - ✅ Formularios
> - ✅ Dashboards
> - ✅ Cualquier proyecto UI/UX

## Integración PersonalOS

| Archivo           | Estado                                        |
| ----------------- | --------------------------------------------- |
| `00_Core/AGENTS.md` | ✅ Actualizado con Taste-Skills PRIORIDAD ALTA |
| `CLAUDE.md`       | ✅ Actualizado con PRIORIDAD MAXIMA            |
| `.cursor/CLAUDE.md` | ✅ Actualizado con ubicación correcta          |
| `README.md`       | ✅ Highlights + Ubicación correcta             |
| `README_DRAFT.md` | ✅ Metodología documentada                     |

---

*Última actualización: 2026-03-19*
