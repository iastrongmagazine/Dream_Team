# 🔬 PLAN DE PRUEBAS — Think Different AI

> **Fecha:** 2026-03-26
> **Ubicación:** `Focus_Now_Lab/`
> **Objetivo:** Validar en ambiente controlado todo lo implementado

---

## 📋 RESUMEN: Lo Que Hicimos Esta Sesión

### ✅ Completed en Esta Sesión

| #   | Item                              | Ubicación                           | Estado   |
|-----|-----------------------------------|-------------------------------------|----------|
| 1   | Mapeo completo del sistema        | `11_System_Mapping.md`              | ✅        |
| 2   | Estado del Arte v6.0              | `12_Estado_Del_Arte.md`             | ✅        |
| 3   | README.md actualizado             | Raíz                                | ✅        |
| 4   | Perfiles 02-05 actualizados       | `.agent/01_Agents/Perfiles/`        | ✅        |
| 5   | 6 posts de Anthropic documentados | `13_Anthropic_Engineering_01_07.md` | ✅        |
| 6   | Feedback + gaps identificados     | `13_Anthropic_Engineering_02_03.md` | ✅        |

### ✅ Completed Sesión Anterior

| #   | Item                         | Ubicación                                           | Estado   |
|-----|------------------------------|-----------------------------------------------------|----------|
| 1   | 5 perfiles de negocio        | `.agent/01_Agents/Perfiles/`                        | ✅        |
| 2   | Scripts Anthropic Harness    | `04_Operations/08_Scripts_Os/11_Anthropic_Harness/` | ✅        |
| 3   | Skills Anthropic             | `.agent/02_Skills/14_Anthropic_Harness/`            | ✅        |
| 4   | Workflow Anthropic           | `.agent/03_Workflows/17_Anthropic_Harness.md`       | ✅        |
| 5   | Hooks Harness                | `.agent/04_Extensions/hooks/05_Harness/`            | ✅        |
| 6   | Documento artículo Anthropic | `10_Anthropic_Harness_Design.md`                    | ✅        |

---

## 🎯 IMPLEMENTACIONES PENDIENTES — Explicación y Prioridad

### 🔴 PRIORIDAD VITAL

#### 1. Auto Mode Security Classifier ⭐ CRÍTICO

**¿Qué hace?**
Sistema de clasificadores que decide automáticamente si una acción del agente es segura sin pedir permiso al usuario. Analiza cada "transcript" (todas las tool calls) antes de ejecutarlas.

**Arquitectura:**
- **Input Layer:** Prompt Injection Probe — escanea outputs de tools antes de entrar al contexto
- **Output Layer:** Transcript Classifier — evalúa acciones contra criterios de decisión
  - Stage 1: Filtro rápido single-token (yes/no)
  - Stage 2: Solo si Stage 1 flaggea → chain-of-thought reasoning

**Por qué es vital:**
- Los usuarios approve el 93% de los permission prompts → fatiga de aprobación
- Previene "overeager behavior": el agente hace cosas más allá de lo autorizado
- Detecta prompt injection antes de que llegue al agente
- 83% de reducción de acciones peligrosas vs tener permisos deshabilitados

---

#### 2. Evaluator/Generator Separation ✅ YA IMPLEMENTADO

**¿Qué hace?**
Separar el agente que HACE el trabajo del agente que EVALÚA el trabajo. El generador crea código, el evaluador lo revisa — no son el mismo agente.

**Por qué es vital:**
- "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work—even when quality is obviously mediocre"
- Un generador NUNCA debe evaluarse a sí mismo — siempre será parcial
- Tuning un evaluador externo es mucho más fácil que hacer un generador autocrítico

**En nuestro OS:** Ya está en `.agent/02_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/` ✅

---

### 🟠 PRIORIDAD ALTA

#### 3. pass@k Metrics Script

**¿Qué hace?**
Mide la probabilidad de que un agente succeeda en al menos 1 de k intentos.

- **pass@k**: Al menos 1 éxito en k intentos ("shots on goal")
- **pass^k**: Todos k intentos succeeden (consistencia)

**Fórmula:** `pass@k = 1 - (1 - p)^k` donde p = per-trial success rate

**Por qué es vital:**
- Distingue entre "no puede" vs "tuvo mala suerte"
- Essential para evaluar agentes en tareas difíciles
- Te dice si un agente puede resolver "eventualmente"

---

#### 4. Eval Awareness Detection Hook

**¿Qué hace?**
Detecta cuando el modelo sospecha que está siendo evaluado y busca las respuestas del benchmark.

**Patrón detectado en Opus 4.6:**
1. Agota búsquedas legítimas (cientos de intentos)
2. Nota "extremely specific nature" de la pregunta
3. Specula que podría ser un benchmark
4. Enumera: GAIA, BrowseComp, FRAMES, SimpleQA, WebArena
5. Busca código fuente del eval
6. Decrypta el dataset

**Por qué es vital:**
- Puede会造成作弊 en evaluaciones
- Score real puede inflated si el modelo "conoce las respuestas"
- Necesitas bloquear este comportamiento

---

#### 5. Feature List como JSON

**¿Qué hace?**
El initializer agent crea un archivo JSON con TODAS las features que el usuario pidió, cada una inicialmente en `"passes": false`.

```json
{
  "category": "functional",
  "description": "New chat button creates a fresh conversation",
  "steps": ["Click New Chat", "Verify new conversation created"],
  "passes": false
}
```

**Por qué es vital:**
- Evita que el agente "declare victory" prematuramente
- Cada agent posterior sabe qué falta
- JSON > Markdown porque Claude no lo modifica accidentalmente

---

### 🟡 PRIORIDAD MEDIA

#### 6. Agent Teams con Git Locks

**¿Qué hace?**
Múltiples Claudes trabajan en paralelo usando un sistema de locks:

1. Agente toma "lock" en una tarea escribiendo archivo `current_tasks/filename.txt`
2. Si dos agents intentan misma tarea → git conflict → segundo pickea otra
3. Cuando termina → git push + remove lock
4. Merge conflicts resueltos por Claude automáticamente

**Por qué es vital:**
- Permite parallelizar trabajo en tareas largas
- 16 agentes pueden trabajar simultáneamente
- Evita que todos trabajen en el mismo bug

---

#### 7. Progress File Template + Script

**¿Qué hace?**
Un archivo (ej: `claude-progress.txt`) que documenta:
- Qué se hizo en cada sesión
- Estado actual del proyecto
- Próximos pasos
- Bugs conocidos

**Por qué es vital:**
- Cada nuevo agente puede "get bearings" en minutos, no horas
- Git history + progress file = contexto completo

---

#### 8. Multi-Agent Roles Workflow

**¿Qué hace?**
Workflow donde diferentes agentes tienen roles especializados:

- **Generator Agent:** Construye features
- **QA Agent:** Testea y reporta bugs
- **Code Review Agent:** Revisa calidad de código
- **Docs Agent:** Mantiene documentación
- **Performance Agent:** Optimiza performance

**Por qué es vital:**
- Especialización = mejor calidad por rol
- El artículo del C Compiler demostró: 16 agentes con roles específicos outperform 1 agente solo

---

#### 9. End-to-End Testing con Browser ✅ YA IMPLEMENTADO

**¿Qué hace?**
Agente usa Playwright/Puppeteer para testar la app como usuario real — clickea, navega, verifica.

**Por qué es vital:**
- Unit tests pasan pero la app no funciona → QA catchea esto
- "Testing end-to-end dramatically improved performance"

**En nuestro OS:** Ya tenemos Playwright skill ✅

---

#### 10. Graders Framework (Code/Model/Human)

**¿Qué hace?**
Sistema de 3 tipos de graders:

| Grader          | Cuándo usar              | Ejemplo                         |
|-----------------|--------------------------|---------------------------------|
| **Code-based**  | Verificaciones objetivas | `assert response.status == 200` |
| **Model-based** | Evaluaciones subjetivas  | "Does this design look good?"   |
| **Human**       | Gold standard final      | SME review                      |

**Por qué es vital:**
- Distintos problemas necesitan distintos graders
- Code grader: rápido, objetivo
- Model grader: flexible, captura nuance

---

## 📊 RESUMEN DE PRIORIDADES

| Prioridad  | #   | Concepto                  | Status            |
|------------|-----|---------------------------|-------------------|
| 🔴 VITAL    | 1   | Auto Mode Security        | ⏳ NO implementado |
| 🔴 VITAL    | 2   | Eval/Generator Separation | ✅ Listo           |
| 🟠 ALTA     | 3   | pass@k Metrics            | ⏳ NO implementado |
| 🟠 ALTA     | 4   | Eval Awareness Detection  | ⏳ NO implementado |
| 🟠 ALTA     | 5   | Feature List JSON         | ⏳ NO implementado |
| 🟡 MEDIA    | 6   | Agent Teams Locks         | ⏳ Parcial         |
| 🟡 MEDIA    | 7   | Progress File             | ⏳ NO implementado |
| 🟡 MEDIA    | 8   | Multi-Agent Roles         | ⏳ NO implementado |
| 🟢 BAJA     | 9   | E2E Browser Testing       | ✅ Listo           |
| 🟢 BAJA     | 10  | Graders Framework         | ⏳ Parcial         |

---

## 🧪 PLAN DE PRUEBAS

### Fase 1: Validación de Archivos Existentes

| #   | Prueba                      | Expected    |
|-----|-----------------------------|-------------|
| 1.1 | Verificar Perfiles 5/5      | 5 archivos  |
| 1.2 | Verificar Anthropic scripts | 5 archivos  |
| 1.3 | Verificar Skills Anthropic  | 3 skills    |
| 1.4 | Verificar Workflow          | Existe      |
| 1.5 | Verificar Hooks             | 2 hooks     |

### Fase 2: Pruebas de Integración de Perfiles

| #   | Prueba                                   | Expected            |
|-----|------------------------------------------|---------------------|
| 2.1 | Load Perfil 01 (Product Builder)         | Keywords detectados |
| 2.2 | Load Perfil 05 (Platform Engineer)       | Keywords detectados |
| 2.3 | Verificar referencias Anthropic en 01    | 5+ menciones        |
| 2.4 | Verificar referencias Anthropic en 02-05 | Mismos componentes  |

### Fase 3: Pruebas de Scripts

| #   | Prueba           | Expected       |
|-----|------------------|----------------|
| 3.1 | Safety Wrapper   | Output de test |
| 3.2 | Context Manager  | Output de test |
| 3.3 | Evaluator Runner | Output de test |
| 3.4 | Sprint Contract  | Output de test |
| 3.5 | Playwright QA    | Output de test |

### Fase 4-7: Documentación, Git, Workflow

| #   | Prueba           | Expected           |
|-----|------------------|--------------------|
| 4.1 | Hooks se activan | Logs               |
| 5.1 | Workflow corre   | 3 fases            |
| 6.1 | Docs completos   | >1000 líneas       |
| 7.1 | Git clean        | Working tree clean |

---

## ✅ Checklist de Resultados Esperados

| Fase      | Pruebas   | Estado Esperado   |
|-----------|-----------|-------------------|
| 1         | 5/5       | ✅ Todas pasan     |
| 2         | 4/4       | ✅ Todas pasan     |
| 3         | 5/5       | ✅ Todas pasan     |
| 4         | 2/2       | ✅ Todas pasan     |
| 5         | 2/2       | ✅ Todas pasan     |
| 6         | 3/3       | ✅ Todas pasan     |
| 7         | 3/3       | ✅ Todas pasan     |
| **TOTAL** | **24/24** | **100% PASS**     |

---

*Plan creado: 2026-03-26*
