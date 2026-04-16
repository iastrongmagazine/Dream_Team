# ⚔️ PLAN MAQUINA DE GUERRA — Think Different AI

> **Fecha:** 2026-03-26
> **Objetivo:** Convertir Think Different en una máquina de guerra SOTA

---

## 🎯 MISIÓN

Implementar los 10 gaps identificados desde los artículos de Anthropic Engineering para tener un sistema de desarrollo autónomo de última generación.

---

## 📋 ROADMAP DE IMPLEMENTACIÓN

### FASE 1: FUNDAMENTOS VITALES (Esta Semana)

#### 1.1 Auto Mode Security Classifier 🔴
**Ubicación:** `.agent/02_Skills/14_Anthropic_Harness/04_Auto_Mode_Security/`

**Archivos a crear:**
```
04_Auto_Mode_Security/
├── SKILL.md                    # Definición de la skill
├── 00_Prompt_Injection_Probe.py # Escanea outputs de tools
├── 01_Transcript_Classifier.py # Clasifica acciones
├── 02_Stage1_Fast_Filter.py    # Filtro single-token
├── 03_Stage2_CoT_Reasoning.py   # Chain-of-thought
├── 04_Decision_Engine.py       # Decide approve/deny
└── README.md
```

**Funcionalidad:**
- Input Layer: Detecta prompt injection antes de que llegue al agente
- Output Layer: Evalúa cada acción contra criterios de seguridad
- Stage 1: Filtro rápido (yes/no) - latency <10ms
- Stage 2: Solo si flaggea → CoT reasoning

**Métricas objetivo:**
- 83% de reducción de acciones overeager
- <1% de false positives
- Latencia <50ms por decisión

---

#### 1.2 Evaluator/Generator Separation ✅
**Ya implementado en:** `.agent/02_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/`

**Verificar que esté funcionando:**
- El workflow 17_Anthropic_Harness tiene las 3 fases separadas
- El generador NO es el mismo que el evaluador

---

### FASE 2: MÉTRICAS Y DETECCIÓN (Próxima Semana)

#### 2.1 pass@k Metrics Script 🟠
**Ubicación:** `04_Operations/08_Scripts_Os/11_Anthropic_Harness/05_Pass_At_Metrics.py`

```python
def pass_at_k(results: list, k: int) -> float:
    """Calcula pass@k: probabilidad de al menos 1 éxito en k intentos"""
    successes = sum(1 for r in results if r.passed)
    return 1 - ((len(results) - successes) / len(results)) ** k

def pass_all_k(results: list, k: int) -> float:
    """Calcula pass^k: probabilidad de TODOS k intentos exitosos"""
    successes = sum(1 for r in results if r.passed)
    return (successes / len(results)) ** k
```

**Uso:**
- Evaluar agentes en tareas difíciles
- Distinguir "no puede" vs "tuvo mala suerte"
- Medir consistency

---

#### 2.2 Eval Awareness Detection Hook 🟠
**Ubicación:** `.agent/04_Extensions/hooks/05_Harness/eval_awareness_detector.py`

**Patrones a detectar:**
```python
TRIGGERS = [
    "extremely specific nature",
    "might be from an LLM benchmark",
    "is this a test question",
    "GAIA", "BrowseComp", "FRAMES", "SimpleQA", "WebArena",
    "decrypt the answer",
    "benchmark identification"
]
```

**Acción cuando detecta:**
1. Loggear la intento
2. Bloquear la búsqueda
3. Alertar al usuario
4. Marcar el trial como "contaminated"

---

#### 2.3 Feature List JSON Generator 🟠
**Ubicación:** `04_Operations/08_Scripts_Os/11_Anthropic_Harness/06_Feature_List_Generator.py`

```json
{
  "project": "mi-proyecto",
  "version": "1.0.0",
  "features": [
    {
      "id": "feat_001",
      "category": "functional",
      "description": "User can create a new chat",
      "steps": [
        "Click New Chat button",
        "Verify new conversation appears",
        "Verify input is focused"
      ],
      "passes": false,
      "priority": "high"
    }
  ],
  "stats": {
    "total": 50,
    "passed": 12,
    "failed": 38
  }
}
```

**Workflow:**
1. Initializer agent genera feature list desde prompt del usuario
2. Cada Coding agent actualiza "passes" cuando termina una feature
3. El progreso se puede visualizar en cualquier momento

---

### FASE 3: TRABAJO PARALELO (Este Mes)

#### 3.1 Agent Teams con Git Locks 🟡
**Ubicación:** `04_Operations/08_Scripts_Os/11_Anthropic_Harness/07_Agent_Teams_Locks.py`

**Arquitectura:**
```python
# Lock mechanism
def take_lock(task_name: str) -> bool:
    """Toma un lock en una tarea"""
    lock_file = f"current_tasks/{task_name}.lock"
    if os.path.exists(lock_file):
        return False  # Ya tomada
    with open(lock_file, 'w') as f:
        f.write(f"{os.getpid()}|{datetime.now()}")
    return True

def release_lock(task_name: str):
    """Libera un lock"""
    lock_file = f"current_tasks/{task_name}.lock"
    if os.path.exists(lock_file):
        os.remove(lock_file)
```

**Comandos:**
```bash
# Iniciar 16 agentes en paralelo
./run_agent_team.sh --agents 16 --task "build-c-compiler"

# Ver estado de locks
./agent_teams status

# Ver trabajo realizado
./agent_teams report
```

---

#### 3.2 Progress File Template 🟡
**Ubicación:** `04_Operations/08_Scripts_Os/11_Anthropic_Harness/08_Progress_Template.md`

```markdown
# Claude Progress - [PROJECT NAME]

## Estado Actual
- **Última sesión:** 2026-03-26
- **Último commit:** abc1234
- **Branches:** main, feature/auth

## Lo Que Se Hizo Esta Sesión
- [ ] Implementado login con JWT
- [ ] Corregido bug en password reset
- [ ] Agregados tests para auth middleware

## Estado del Proyecto
- **Features completadas:** 12/50
- **Tests pasando:** 89%
- **Tech debt:** 3 items

## Próximos Pasos
1. Implementar logout
2. Agregar 2FA
3. Mejorar UX del login

## Bugs Conocidos
- [BUG-001] Session expira antes de lo esperado
- [BUG-002] Memory leak en dashboard

## Notas de la Sesión
- El auth middleware necesita refactor
- Decidimos usar JWT en vez de sesiones

---
```

---

#### 3.3 Multi-Agent Roles Workflow 🟡
**Ubicación:** `.agent/03_Workflows/18_Multi_Agent_Roles.md`

```yaml
name: Multi-Agent Roles Pipeline
description: Workflow con agentes especializados

agents:
  - name: generator
    role: feature_development
    prompt: "Eres un генератор. Construye features una a la vez..."

  - name: qa
    role: testing
    prompt: "Eres un QA agent. Testea lo que el generator hizo..."

  - name: code_reviewer
    role: code_quality
    prompt: "Eres un code reviewer. Revisa calidad del código..."

  - name: docs
    role: documentation
    prompt: "Eres un docs agent. Mantén la documentación..."

  - name: performance
    role: optimization
    prompt: "Eres un performance agent. Optimiza donde sea necesario..."

pipeline:
  - generator → qa (loop until pass)
  - qa → code_reviewer
  - code_reviewer → docs
  - docs → performance (optional)
  - all → merge
```

---

### FASE 4: EVALUATION FRAMEWORK (Este Mes)

#### 4.1 Graders Framework 🟢
**Ubicación:** `.agent/02_Skills/14_Anthropic_Harness/05_Graders_Framework/`

```
05_Graders_Framework/
├── SKILL.md
├── 01_Code_Grader.py      # Objetivo: assertions, regex, binary tests
├── 02_Model_Grader.py     # Flexible: LLM-as-judge, rubrics
├── 03_Human_Grader.py    # Gold: SME review
├── 04_Grader_Mux.py       # Elige el mejor grader
└── examples/
    ├── code_grader_examples.yaml
    └── model_grader_examples.yaml
```

**Ejemplo de uso:**
```python
from graders import CodeGrader, ModelGrader, HumanGrader

# Código que debe pasar tests → CodeGrader
task = Task(type="unit_tests", files=["auth_test.py"])
result = CodeGrader.evaluate(task)

# Diseño subjetivo → ModelGrader
task = Task(type="design_review", files=["design.png"])
result = ModelGrader.evaluate(task, rubric="design_quality.md")

# Decisión final → HumanGrader
task = Task(type="security_audit")
result = HumanGrader.evaluate(task)
```

---

## 📊 CRONOGRAMA

| Semana             | Fase                          | Entregables                              | Estado             |
|--------------------|-------------------------------|------------------------------------------|--------------------|
| 1                  | FASE 1: Fundamentos           | Auto Mode Security                       | ✅                  |
| 1                  | FASE 1: Fundamentos           | Evaluator/Generator Separation           | ✅                  |
| 2                  | FASE 2: Métricas              | pass@k Metrics                           | ✅                  |
| 2                  | FASE 2: Métricas              | Eval Awareness                           | ✅                  |
| 2                  | FASE 2: Métricas              | Feature List JSON                        | ✅                  |
| 3                  | FASE 3: Paralelo              | Agent Teams + Git Locks                  | ✅                  |
| 3                  | FASE 3: Paralelo              | Progress File Template                   | ✅                  |
| 3                  | FASE 3: Paralelo              | Multi-Agent Roles                        | ✅                  |
| 4                  | FASE 4: Evaluation            | Graders Framework                        | ✅                  |

---

## ✅ DEFINICIÓN DE "DONE"

### Para cada implementación:
- [x] Código escrito
- [x] Tests pasando
- [ ] Documentación actualizada
- [ ] Skills/Workflows registrados
- [x] Engram actualizado

> **Nota:** Todo testeado en `Focus_Now_Lab/01_Test_Anthropic_Harness/` sin tocar el OS.

---

## 🏆 METAS FINALES

| Métrica                      | Target                                       |
|------------------------------|----------------------------------------------|
| Auto Mode Security           | <50ms latencia, >83% reducción               |
| pass@k                       | Script funcionando con ejemplos              |
| Eval Awareness               | Hook bloqueando patrones conocidos           |
| Feature List                 | Generator → JSON → Tracking                  |
| Agent Teams                  | 16 agentes en paralelo                       |
| Progress File                | Template + script                            |
| Multi-Agent Roles            | 5 roles especializados                       |
| Graders                      | 3 tipos funcionando                          |

---

## 🔗 RECURSOS

- Documentación Anthropic: `01_Core/02_Knowledge_Brain/13_Anthropic_Engineering_*.md`
- Test Plan: `Focus_Now_Lab/README_Test_Plan.md`
- Engram: `anthropic-gaps-plan`

---

*Plan creado: 2026-03-26*
