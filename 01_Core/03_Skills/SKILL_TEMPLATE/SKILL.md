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

## Errores Comunes

### ❌ BAD: Sin validación de inputs

```python
# NO HACER: Input sin validar
def process(data):
    return data.upper()  # Qué pasa si data es None?
```

### ✅ GOOD: Con validación

```python
# HACER: Input validado
def process(data):
    if not data:
        raise ValueError("data no puede ser vacío")
    return data.upper()
```

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
