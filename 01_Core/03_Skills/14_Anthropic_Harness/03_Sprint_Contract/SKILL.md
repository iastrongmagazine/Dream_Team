# Sprint Contract Skill

**CATEGORÍA:** Anthropic Harness Patterns  
**SUBCATEGORÍA:** Sprint Contract  
**VERSIÓN:** 1.0

---

## Propósito

Implementa el patrón de Sprint Contract de Anthropic:
- Generator + Evaluator **negocian "done"** antes de cada sprint
- Evita que el Generator **"mueva el goalpost"** durante el build
- Define **criterios verificables** antes de escribir código

---

## Contexto (del artículo de Anthropic)

> "It was defining the definition of done up front before it actually started building anything"  
> "So that way, the generator agent couldn't move the goalpost halfway through the build to say, 'Ah, it's done'"

---

## Cuándo Usar

- Para features complejas (no tasks simples)
- Cuando hay riesgo de scope creep
- Para trabajo en equipo (contrato entre agentes)
- Cuando necesitas definición clara de "done"

---

## Flujo del Sprint Contract

```
1. GENERATOR propone: "Voy a build X"
2. EVALUATOR responde: "Para que esté done, necesito A, B, C"
3. NEGOCIACIÓN: Ajustan hasta agreed
4. CONTRATO FIRMADO: Ambos aceptan criterios
5. GENERATOR build
6. EVALUATOR verifica contra criterios acordados
```

---

## Implementación

Usa `03_Sprint_Contract.py`:

```python
from 08_Scripts_Os/11_Anthropic_Harness/03_Sprint_Contract import run_sprint_contract

# Crear contrato
contract = run_sprint_contract(
    sprint_id="sprint_01",
    feature="User Dashboard",
    proposal="Build dashboard with stats and charts",
    requirements=[
        "Must show 3 stat cards",
        "Must have interactive chart",
        "Must be responsive mobile",
        "Must pass a11y audit"
    ]
)

# Verificar después de build
results = manager.verify_contract(contract, actual_output)
print(results['summary'])
```

---

## Criterios del Contrato

| Tipo | Descripción |
|------|-------------|
| `manual` | Requiere revisión humana |
| `automated` | Test automático pasa |
| `test` | Unit/E2E test coverage |

---

## Integración con Perfiles

| Perfil | Cómo usa |
|--------|----------|
| Product Builder | Antes de cada feature/sprint |
| Design Ops | Antes de cada componente |
| Data Engineer | Antes de cada pipeline |

---

## Ejemplo de Contract

```
📜 SPRINT CONTRACT
====================
Sprint ID: sprint_01
Feature: User Dashboard
Status: AGREED

📋 AGREED CRITERIA:
  1. ✅ Must show 3 stat cards with real data (verification: automated)
  2. ✅ Must have interactive chart (verification: test)
  3. ✅ Must be responsive on mobile (verification: automated)
  4. ✅ Must pass accessibility audit (verification: manual)

====================
✅ CONTRACT FULFILLED: 4/4 criteria passed
```

---

## Reglas Clave

1. **Negocia ANTES** — Nunca empieces a build sin contract
2. **Criterios específicos** — "Funciona" → "Stats cards muestran datos reales"
3. **Verificable** — Cada criterio debe poder verificarse
4. **Binding** — Ambos agentes cumplen lo acordado

---

## Scripts Relacionados

- `02_Evaluator_Runner.py` — Para verificar criterios
- `04_Playwright_QA.py` — Para testing interactivo
- `03_Sprint_Contract.py` — Lógica del contract

---

## Referencias

- Artículo: `01_Brain/02_Knowledge_Brain/10_Anthropic_Harness_Design.md`
- Script: `08_Scripts_Os/11_Anthropic_Harness/03_Sprint_Contract.py`

---

*Creado: 2026-03-26 | Filosofía: "No te traiciones, no te abandones"*
