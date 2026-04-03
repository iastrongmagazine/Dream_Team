# Frontend Premium Workflow

## Trigger
Cuando el usuario pide crear/editar frontend: landing pages, webapps, dashboards, invitaciones, o cualquier proyecto con UI.

## Pasos

### 1. Identificar el tipo de proyecto

| Tipo                        | Skills a usar                                           |
|-----------------------------|---------------------------------------------------------|
| Landing / Webapp nueva      | `@taste-skill/SKILL.md` + `@output-skill/SKILL.md`      |
| Invitación / Evento premium | `@soft-skill/SKILL.md` + `@output-skill/SKILL.md`       |
| Dashboard / Data-heavy      | `@minimalist-skill/SKILL.md` + `@output-skill/SKILL.md` |
| Legacy upgrade              | `@redesign-skill/SKILL.md` + `@output-skill/SKILL.md`   |
| Siempre                     | `@output-skill/SKILL.md`                                |

### 2. Cargar skills

```
@taste-skill/SKILL.md
@output-skill/SKILL.md
```

### 3. Configurar taste-skill

```markdown
DESIGN_VARIANCE (1-10): 8   # Ajustar según proyecto
MOTION_INTENSITY (1-10): 6  # 1=static, 10=animated
VISUAL_DENSITY (1-10): 4    # 1=airy, 10=dense
```

### 4. Verificar entorno

Antes de generar código:
- [ ] Verificar package.json (Tailwind v3 o v4)
- [ ] Verificar node_modules/react
- [ ] Detectar stack: Next.js, React, Vue, etc.

### 5. Reglas Anti-Emoji

**EMOJIS BANEADOS** — Usar:
- Radix Icons
- Phosphor Icons
- SVG inline

### 6. Generar código

1. Crear componentes limpios y reutilizables
2. Usar Tailwind con clases legibles
3. Agregar animaciones sutiles (fade-in, scroll)
4. Implementar dark mode si aplica
5. Responsive por defecto

### 7. Verificar output

- [ ] No hay emojis
- [ ] Dependencias verificadas en package.json
- [ ] Código completo (no placeholders)
- [ ] Animaciones suaves
- [ ] Responsive

## Ubicación de Skills

```
01_Core/03_Skills/04_Product_Design/
├── taste-skill/SKILL.md       # Diseño premium desde cero
├── soft-skill/SKILL.md        # Look premium/lujoso
├── minimalist-skill/SKILL.md    # Estilo Notion/Linear
├── redesign-skill/SKILL.md      # Mejorar existentes
└── output-skill/SKILL.md      # Código completo
```
