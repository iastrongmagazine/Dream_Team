# Taste-Skill Integration — Think Different PersonalOS

## What is Taste-Skill

Colección de 5 skills que mejoran radicalmente cómo la IA genera código frontend. En lugar de interfaces genéricas, produce diseños premium con animaciones, espaciado y calidad visual de alto nivel.

## Las 5 Skills

| Skill                            | Propósito                                  | Cuándo Usar                                     |
|----------------------------------|--------------------------------------------|-------------------------------------------------|
| **taste-skill**                  | Diseño principal premium                   | Proyectos desde cero                            |
| **soft-skill**                   | Look & feel premium/lujoso                 | Invitaciones, landing pages premium             |
| **minimalist-skill**             | Estilo Notion/Linear editorial             | Dashboards limpios                              |
| **redesign-skill**               | Mejorar proyectos existentes               | Legacy, upgrades                                |
| **output-skill**                 | Código completo sin shortcuts              | Siempre (evita código incompleto)               |

## Configuración de Taste-Skills

```markdown
DESIGN_VARIANCE (1-10): 8  # 8=Artsy Chaos, layouts experimentales
MOTION_INTENSITY (1-10): 6 # 6=Fade-ins, smooth scrolling
VISUAL_DENSITY (1-10): 4   # 4=Espaciado normal de app típica
```

| Setting                          | 1-3                         | 4-7                              | 8-10                                 |
|----------------------------------|-----------------------------|----------------------------------|--------------------------------------|
| **DESIGN_VARIANCE**              | Limpio/centrado             | Overlapping elements             | Asimétrico/moderno                   |
| **MOTION_INTENSITY**             | Casi nada                   | Fade-ins, scroll                 | Magnetic, spring physics             |
| **VISUAL_DENSITY**               | Airy/Lujo                   | Normal                           | Denso/Dashboard                      |

## Ubicación de Skills (INSTALADAS)

```
.cursor/02_Skills/11_Taste_Skills/     # Para Cursor IDE
└── taste-skill/                         # Diseño principal
    ├── taste-skill/SKILL.md            # Premium desde cero
    ├── soft-skill/SKILL.md             # Lujoso/exclusivo
    ├── minimalist-skill/SKILL.md        # Notion/Linear
    ├── redesign-skill/SKILL.md         # Mejorar existentes
    └── output-skill/SKILL.md           # Código completo

.agent/02_Skills/11_Taste_Skills/       # Para OpenCode
└── taste-skill/                         # Diseño principal
    ├── taste-skill/SKILL.md            # Premium desde cero
    ├── soft-skill/SKILL.md             # Lujoso/exclusivo
    ├── minimalist-skill/SKILL.md        # Notion/Linear
    ├── redesign-skill/SKILL.md         # Mejorar existentes
    └── output-skill/SKILL.md           # Código completo
```

## Cómo Activar en Claude Code / Cursor

1. **Referenciar en el prompt**:
   ```
   @.cursor/02_Skills/11_Taste_Skills/taste-skill/SKILL.md
   @.cursor/02_Skills/11_Taste_Skills/output-skill/SKILL.md
   ```

2. **En Cursor**:可以直接 @SKILL.md archivos.

## Integración con PersonalOS

El PersonalOS ya tiene Taste-Skills documentado en:
- `CLAUDE.md` → Sección TASTE-SKILLS
- `00_Core/AGENTS.md` → Sección 2.4
- `README.md` → Highlights + Ubicación correcta

## Reglas Clave de Taste-Skills

- **ANTI-EMOJI POLICY**: Emojis BANEADOS — usar Radix, Phosphor icons o SVG
- **DEPENDENCY VERIFICATION**: Siempre verificar `package.json` antes de importar
- **TAILWIND VERSION LOCK**: Checkear `package.json` para v3/v4
- **RSC SAFETY**: Global state solo en Client Components
- **Viewport Stability**: Usar `min-h-[100dvh]` en lugar de `h-screen`

## Uso Recomendado por Contexto

```
Frontend nuevo (landing, webapp)  → taste-skill + output-skill
Invitación premium / evento       → soft-skill + output-skill
Dashboard / data-heavy            → minimalist-skill + output-skill
Legacy upgrade                    → redesign-skill + output-skill
```

---

*Nota: Este archivo es referencia. Las skills están INSTALADAS en `.cursor/` y `.agent/`.*
