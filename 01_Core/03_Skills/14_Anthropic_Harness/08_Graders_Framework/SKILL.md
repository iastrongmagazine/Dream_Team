# Graders Framework Skill

**CATEGORÍA:** Anthropic Harness Patterns  
**SUBCATEGORÍA:** Graders Framework  
**VERSIÓN:** 1.0

---

## Propósito

Framework con 3 tipos de graders para diferentes tipos de evaluación.

> **Inspirado en:** "Demystifying Evals for AI Agents" article (Jan 09, 2026)

---

## Los 3 Tipos de Graders

| Grader | Cuándo usar | Ejemplo |
|--------|-------------|---------|
| **Code-based** | Verificaciones objetivas | `assert response.status == 200` |
| **Model-based** | Evaluaciones subjetivas | "Does this design look good?" (LLM judge) |
| **Human** | Gold standard final | SME review |

---

## Implementación

### Scripts

| Script | Función |
|--------|---------|
| `00_Code_Grader.py` | Assertions, regex, binary tests |
| `01_Model_Grader.py` | LLM-as-judge con rubrics |
| `02_Human_Grader.py` | Templates para SME review |
| `03_Grader_Mux.py` | Multiplexor que elige el mejor grader |

### Uso

```python
from 00_Code_Grader import CodeGrader
from 01_Model_Grader import ModelGrader
from 02_Human_Grader import HumanGrader
from 03_Grader_Mux import GraderMux

# Para código → CodeGrader
task = Task(type="unit_tests", files=["auth_test.py"])
result = CodeGrader.evaluate(task)

# Para diseño → ModelGrader
task = Task(type="design_review", files=["design.png"])
result = ModelGrader.evaluate(task, rubric="design_quality.md")

# Para decisiones críticas → HumanGrader
task = Task(type="security_audit")
result = HumanGrader.evaluate(task)

# Automático → GraderMux
mux = GraderMux()
result = mux.evaluate(task)
```

---

## Código Grader

```python
class CodeGrader:
    """Grader basado en código para verificaciones objetivas."""
    
    def evaluate(self, task: Task) -> GraderResult:
        # Binary tests: pass/fail
        # Static analysis: lint, type check
        # Outcome verification: database state
        # Tool call verification: correct tools used
```

---

## Model Grader

```python
class ModelGrader:
    """Grader basado en LLM para evaluaciones subjetivas."""
    
    def evaluate(self, task: Task, rubric: str) -> GraderResult:
        # Rubric-based scoring
        # Natural language assertions
        # Pairwise comparison
        # Reference-based evaluation
```

---

## Human Grader

```python
class HumanGrader:
    """Grader humano para gold standard."""
    
    def create_task(self, task: Task) -> HumanReviewTask:
        # Genera tarea para SME review
        # Incluye rúbrica y ejemplos
```

---

## Integración con Perfiles

| Perfil | Grader recomendado |
|--------|-------------------|
| Product Builder | Code + Model |
| Data Engineer | Code |
| Marketing Tech | Model |
| Design Ops | Model + Human |
| Platform Engineer | Code |

---

## Referencias

- Artículo: `01_Brain/02_Knowledge_Brain/13_Anthropic_Engineering_01_07.md` (Post 7)

---

*Creado: 2026-03-26 | Filosofía: "No te traiciones, no te abandonones"*