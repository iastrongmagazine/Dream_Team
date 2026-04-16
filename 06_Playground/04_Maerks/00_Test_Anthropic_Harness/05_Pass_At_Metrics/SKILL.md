# Pass@k Metrics Skill

**CATEGORÍA:** Anthropic Harness Patterns
**SUBCATEGORÍA:** pass@k Metrics
**VERSIÓN:** 1.0

---

## Propósito

Mide la probabilidad de que un agente succeeda en al menos 1 de k intentos.

> **Inspirado en:** "Demystifying Evals for AI Agents" article (Jan 09, 2026)

---

## Definiciones

### pass@k
Mide la probabilidad de que al menos 1 de k intentos succeeda.

```
pass@k = 1 - (1 - p)^k
```
donde p = per-trial success rate

### pass^k
Mide la probabilidad de que TODOS k intentos succeedan.

```
pass^k = p^k
```

---

## Cuándo Usar

| Escenario                                 | Métrica   | Por qué                        |
|-------------------------------------------|-----------|--------------------------------|
| Tool donde una solución basta             | pass@1    | Primera oportunidad cuenta     |
| Coding donde try-try-allowed              | pass@5    | Múltiples intentos posibles    |
| Tareas críticas que requieren consistency | pass^k    | Debe funcionar todas las veces |

---

## Implementación

### Scripts

| Script                  | Función                     |
|-------------------------|-----------------------------|
| `00_Pass_At_Metrics.py` | Calcula pass@k y pass^k     |
| `01_Eval_Analyzer.py`   | Analiza resultados de evals |

### Uso Básico

```python
from 00_Pass_At_Metrics import calculate_pass_at_k, calculate_pass_all_k

# Resultados de 10 trials
results = [True, False, True, True, False, True, True, False, True, True]

# pass@1 = proporción de successes en primer intento
pass_at_1 = calculate_pass_at_k(results, k=1)

# pass@5 = probabilidad de al menos 1 éxito en 5 intentos
pass_at_5 = calculate_pass_at_k(results, k=5)

# pass^3 = probabilidad de 3 successes consecutivos
pass_3 = calculate_pass_all_k(results, k=3)
```

---

## Ejemplo de Evaluación

| Task        | 10 Trials Results   | pass@1   | pass@5   | pass^3   |
|-------------|---------------------|----------|----------|----------|
| Easy task   | T,T,T,T,T,T,T,T,T,T | 100%     | 100%     | 100%     |
| Medium task | T,F,T,T,F,T,T,T,T,F | 70%      | 100%     | 34%      |
| Hard task   | F,F,F,F,T,F,F,F,F,F | 10%      | 50%      | 0.1%     |

---

## Integración con Perfiles

| Perfil            | Uso de pass@k                               |
|-------------------|---------------------------------------------|
| Product Builder   | Evaluar si feature es "solvable eventually" |
| Data Engineer     | Medir reliability de pipelines              |
| Marketing Tech    | Medir consistency de campaigns              |
| Design Ops        | Medir consistency de designs                |
| Platform Engineer | Medir reliability de deployments            |

---

## Referencias

- Artículo: `01_Core/02_Knowledge_Brain/13_Anthropic_Engineering_01_07.md` (Post 7)
- Docs: https://docs.anthropic.com/docs/build-with-claude/prompt-engineering

---

*Creado: 2026-03-26 | Filosofía: "No te traiciones, no te abandones"*
