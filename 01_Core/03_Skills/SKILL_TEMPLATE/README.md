# Skill Template

Plantilla oficial para crear nuevas skills en PersonalOS.

## Uso

```bash
# Copiar el template
cp -r 01_Core/03_Skills/SKILL_TEMPLATE/ 01_Core/03_Skills/NN_Nueva_Skill/

# Renombrar y personalizar
cd 01_Core/03_Skills/NN_Nueva_Skill/
mv SKILL.md NN_Nueva_Skill.md
```

## Estructura

```
SKILL_TEMPLATE/
├── SKILL.md              # Template principal
├── README.md             # Este archivo
├── LICENSE               # MIT License
├── references/           # Documentación de referencia
├── scripts/              # Código ejecutable
├── assets/               # Recursos estáticos
└── examples/             # Casos de uso
```

## Validación

Antes de integrar, ejecutar:

```bash
# Security scan
python 08_Scripts_Os\Validator_Fixed\skill_security_scan.py --skill 01_Core\03_Skills\NN_Skill\

# Skill auditor
python 08_Scripts_Os\Validator_Fixed\34_Skill_Auditor.py --skill 01_Core\03_Skills\NN_Skill\
```

## Requisitos

- Score ≥ 70% en Skill Auditor
- 0 CRITICAL en security scan
- examples/ con good + bad examples

---

**Versión:** 2.0 (2026-03-30)
