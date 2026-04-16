# Auto Mode Security Skill

**CATEGORÍA:** Anthropic Harness Patterns
**SUBCATEGORÍA:** Auto Mode Security
**VERSIÓN:** 1.0

---

## Propósito

Sistema de clasificadores que decide automáticamente si una acción del agente es segura sin pedir permiso al usuario. Analiza cada "transcript" (todas las tool calls) antes de ejecutarlas.

> **Inspirado en:** Claude Code auto mode article (Mar 25, 2026)

---

## Arquitectura

### Input Layer: Prompt Injection Probe

Escanea outputs de tools antes de entrar al contexto del agente.

```python
def scan_for_prompt_injection(tool_output: str) -> bool:
    """
    Detecta posibles intentos de prompt injection.
    Retorna True si detecta sospecha.
    """
    INJECTION_PATTERNS = [
        "ignore previous",
        "disregard instructions",
        "forget everything",
        "new instructions:",
        "you are now",
        "system prompt",
        "<|system|>",
        "[SYSTEM]"
    ]

    for pattern in INJECTION_PATTERNS:
        if pattern.lower() in tool_output.lower():
            return True
    return False
```

### Output Layer: Transcript Classifier

Evalúa cada acción contra criterios de decisión. Dos etapas:

| Stage   | Propósito                                            | Latencia   |
|---------|------------------------------------------------------|------------|
| Stage 1 | Filtro rápido single-token (yes/no)                  | <10ms      |
| Stage 2 | Chain-of-thought reasoning (solo si Stage 1 flaggea) | <50ms      |

---

## Niveles de Riesgo

| Nivel        | Acción                   | Ejemplos                      |
|--------------|--------------------------|-------------------------------|
| **LOW**      | Ejecutar automáticamente | `ls`, `cat`, `read`           |
| **MEDIUM**   | Ejecutar con logging     | `write`, `edit`               |
| **HIGH**     | Solicitar confirmación   | `delete`, `rm`, `exec`        |
| **CRITICAL** | Bloquear                 | `rm -rf`, `format`, `--force` |

---

## Métricas Objetivo

| Métrica                      | Target   |
|------------------------------|----------|
| Reducción acciones overeager | >83%     |
| False positives              | <1%      |
| Latencia por decisión        | <50ms    |
| Blocks en prompt injection   | 100%     |

---

## Cuándo Usar

- Cuando quieres que el agente trabaje autonomía sin pedir aprobación constante
- Para reducir fatiga de aprobación (93% son aprobados)
- Como capa de seguridad antes de ejecutar actions peligrosas

---

## Implementación

### Scripts Disponibles

| Script                         | Propósito                  |
|--------------------------------|----------------------------|
| `00_Prompt_Injection_Probe.py` | Escanea outputs de tools   |
| `01_Transcript_Classifier.py`  | Clasifica acciones         |
| `02_Stage1_Fast_Filter.py`     | Filtro rápido single-token |
| `03_Stage2_CoT_Reasoning.py`   | Chain-of-thought reasoning |
| `04_Decision_Engine.py`        | Decide approve/deny        |

### Uso Básico

```python
from 04_Auto_Mode_Security import AutoModeSecurity

security = AutoModeSecurity()

# Analizar una acción antes de ejecutar
decision = security.evaluate(
    action="delete_file",
    target="/tmp/test.txt",
    context={"file_exists": True}
)

print(decision)
# Output: Decision(level="MEDIUM", approved=True, reason="Non-critical delete")
```

### Integración con Hooks

```python
# En un hook PreToolUse
def evaluate_action(tool_name, tool_input):
    security = AutoModeSecurity()
    decision = security.evaluate(tool_name, tool_input)

    if decision.level == "CRITICAL":
        return {"blocked": True, "reason": decision.reason}
    elif decision.level == "HIGH":
        return {"confirm": True, "message": decision.reason}

    return {"approved": True}
```

---

## Reglas Clave

1. **Defense in depth** — Múltiples capas de seguridad
2. **Fail secure** — Si hay duda, denegar
3. **Log everything** — Para auditoría
4. **Never trust output** — Siempre escanear antes de pasar al contexto

---

## Referencias

- Artículo: `01_Core/02_Knowledge_Brain/13_Anthropic_Engineering_01_07.md` (Post 2)
- Scripts: `.agent/02_Skills/14_Anthropic_Harness/04_Auto_Mode_Security/`

---

*Creado: 2026-03-26 | Filosofía: "No te traiciones, no te abandones"*
