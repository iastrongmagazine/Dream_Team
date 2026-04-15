---
name: template-skill
description: >
  DESCRIPCION: Esta es una skill template que sirve como punto de partida.
  Incluir: (1) Qué hace la skill, (2) Triggers específicos para activarse,
  (3) Cuándo NO usarla. La descripción es el mecanismo PRIMARY de activación.
  Ejemplo: "Patrones de testing con Pytest. Úsalo cuando: (1) escribas tests,
  (2) configures CI, (3) necesites fixtures. NO usar para E2E."
author: gentleman-programming
version: 1.0.0
compatibility: all
category: 1
tags: [template, example]
---

# TODO: Nombre de la Skill

> Reemplaza este contenido con la descripción de tu skill.

## Quick Start

```bash
# TODO: Comando de ejemplo
echo "Hola mundo"
```

## Cuándo Usar Esta Skill

- TODO: Primer trigger específico
- TODO: Segundo trigger específico
- TODO: Tercer trigger específico

## Cuándo NO Usar Esta Skill

- TODO: Primer caso donde NO aplicarla
- TODO: Segundo caso donde NO aplicarla

## Estructura de la Skill

```
nombre-skill/
├── SKILL.md                  # Este archivo
├── references/               # Documentación de referencia
│   └── *.md                 # Guías específicas
├── scripts/                 # Código ejecutable
│   └── *.py                 # Scripts
├── assets/                  # Recursos estáticos
│   └── templates/           # Plantillas
└── examples/                 # Casos de uso
    ├── good_example.md      # Ejemplo correcto
    └── bad_example.md       # Ejemplo incorrecto
```

## Guías de Referencia

- **Patrones generales**: Ver [references/PATTERNS.md](references/PATTERNS.md)
- **Configuración**: Ver [references/CONFIG.md](references/CONFIG.md)
- **Ejemplos avanzados**: Ver [references/ADVANCED.md](references/ADVANCED.md)

## ⚠️ Gotchas

### ERROR 1: Sin validación de inputs
- **Por qué**: Input sin validar causa errores en runtime que pudieron prevenirse
- **Solución**: Siempre validar inputs al inicio de la función

### ERROR 2: Documentación genérica
- **Por qué**: "No cometas errores" no aporta valor - es demasiado obvio
- **Solución**: Ser específico: "Sin yt-dlp instalado, la extracción de metadata falla"

### ERROR 3: No seguir la estructura
- **Por qué**: Sin estructura consistente, las skills son difíciles de mantener
- **Solución**: Siempre usar el template con las secciones requeridas

### ERROR 4: Description sin triggers
- **Por qué**: Sin triggers, el modelo no sabe cuándo activar la skill
- **Solución**: Incluir siempre "triggers on:" seguido de palabras clave específicas

## Integración con Agent Teams Lite

Si esta skill es parte del workflow SDD:
1. Añadir a `10_Agent_Teams_Lite/skills/<skill-name>/examples/`
2. Incluir escenarios específicos del workflow
3. Documentar en `examples/scenario_N.md`

---

## TODO: Pasos para Completar

1. [ ] Renombrar folder a `NN_Nombre_Skill`
2. [ ] Actualizar frontmatter (name, description, category)
3. [ ] Escribir documentación en body
4. [ ] Crear examples/ con casos de uso
5. [ ] Implementar scripts/ si aplica
6. [ ] Añadir references/ si aplica
7. [ ] Ejecutar security scan
8. [ ] Run skill auditor (score ≥ 70%)
9. [ ] Registrar en skill registry

---

**Nota:** Esta es una skill template. Modifica según las necesidades específicas del caso de uso.

---

## Esencia Original

> **Metaskill**: Template base para crear nuevas skills siguiendo estándares PersonalOS.

**Por qué existe esta skill:**
- Cada nueva skill necesita un punto de partida consistente
- Sin template, cada skill tiene formato diferente
- El template asegura que todas las skills cumplan los estándares SOTA

**Caso de uso principal:**
1. Se crea una nueva carpeta para la skill
2. Se copia este template como SKILL.md base
3. Se personalizan las secciones vacías
4. Se audita con Skill Auditor antes de integrar

---

*Skill Version: 1.0.0*
