# 📝 SOP Prompt: 02_Evals

> **Carpeta destino:** `01_Core/02_Evals/`
> **Complementa:** `Maerks/00_Test_Anthropic_Harness/`, `01_Core/03_Skills/14_Anthropic_Harness/`

---

## 🎯 Propósito del Prompt

Crear una evaluación (eval) para medir el rendimiento de agentes, workflows o el sistema completo.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Evaluador de Sistemas AI. Crea una evaluación completa para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre de la eval:** [NOMBRE_DE_LA_EVAL]
- **Tipo:** [AGENT_EVAL/WORKFLOW_EVAL/SYSTEM_EVAL/BENCHMARK]
- **Agente a evaluar:** [nombre del agente si aplica]

## 📂 Estructura Requerida
Guardar en: `01_Core/02_Evals/NN_Nombre_Eval.md`

## 📝 Estructura del Documento

```markdown
---
name: [Nombre de la Evaluación]
date: YYYY-MM-DD
agent: [si aplica]
type: [AGENT|WORKFLOW|SYSTEM]
---

# 📊 [Nombre de la Evaluación]

## 🎯 Objetivo
[Qué mide esta evaluación]

## 📋 Configuración

### Input
- **Prompt inicial:** [prompt que se usa]
- **Contexto:** [qué contexto se provee]

### Expected Output
- **Output esperado:** [qué debería devolver]
- **Criterios de éxito:** [lista de criterios]

## 🧪 Casos de Prueba

### Caso 1: [Nombre]
- **Input:** [input]
- **Expected:** [expected output]
- **Criterios:** [criterios de aceptación]

### Caso 2: [Nombre]
[Igual estructura]

## 📊 Métricas

| Métrica     | Target   | Actual   |
|-------------|----------|----------|
| [Métrica 1] | [valor]  | [valor]  |
| [Métrica 2] | [valor]  | [valor]  |

## 🔧 Herramientas de Evaluación
- Usar: `01_Core/03_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/`
- Para comparaciones: `01_Core/03_Skills/14_Anthropic_Harness/05_Pass_At_Metrics/`

## 📈 Resultados

### Run 1 - YYYY-MM-DD
- **Score:** [X]%
- **Pass/Fail:** [✓/✗]
- **Issues:** [lista]

### Run 2 - YYYY-MM-DD
[Igual estructura]
```

## 🛠️ Integración con Anthropic Harness

### Patterns SOTA a Usar
- **Evaluator Pattern:** `01_Core/03_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/`
- **Pass@K Metrics:** `01_Core/03_Skills/14_Anthropic_Harness/05_Pass_At_Metrics/`
- **Context Management:** `01_Core/03_Skills/14_Anthropic_Harness/02_Context_Management/`

### Framework de Evaluación
1. **Generator** → Produce output
2. **Evaluator** → Lo cuestiona/adversarial
3. **Grader** → Da score numérico

## ⚡ Best Practices SOTA

1. **Adversarial**: El evaluator debe intentar romper el output
2. **Múltiples runs**: Al menos 3 runs para métricas estables
3. **Pass@K**: Medir no solo "pasa una vez", sino "pasa K de N veces"
4. **Edge cases**: Incluir casos difíciles, no solo los fáciles

## 🎬 Ejemplo de Uso

```
Crear una eval para el agente Product Builder.

Nombre: Product Builder PRD Eval
Tipo: AGENT_EVAL
Agente: 01_Core/04_Agents/01_Dream_Team/01_Product_Builder.md
```

## ✅ Checklist de Calidad

- [ ] Define input/output claramente
- [ ] Tiene al menos 5 casos de prueba
- [ ] Incluye casos difíciles/edge cases
- [ ] Usa framework adversarial
- [ ] Métricas cuantificables
- [ ] Resultados documentados con fechas
- [ ] Referencias a skills de evaluación
