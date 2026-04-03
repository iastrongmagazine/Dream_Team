# 18 Multi-Agent Roles Pipeline

> **Fecha:** 2026-03-26
> **Inspirado en:** "Scaling Agentic Systems" article (Feb 25, 2026)

---

## Overview

Pipeline que coordina múltiples agentes especializados para desarrollo de software autónomo.

```
generator → qa → code_reviewer → docs → (optional) performance → merge
```

---

## Agentes Disponibles

| Rol               | Descripción                     | Capabilities                            |
|-------------------|---------------------------------|-----------------------------------------|
| **generator**     | Construye features una a la vez | code_generation, implementation         |
| **qa**            | Testea lo que el generator hizo | testing, validation                     |
| **code_reviewer** | Revisa calidad del código       | code_review, quality                    |
| **docs**          | Mantiene la documentación       | documentation, readmes                  |
| **performance**   | Optimiza donde sea necesario    | optimization, profiling                 |
| **security**      | Revisa aspectos de seguridad    | security_audit, vulnerability_detection |
| **architect**     | Diseño de arquitectura          | system_design, patterns                 |

---

## Pipeline Definition

```yaml
name: Multi-Agent Roles Pipeline
description: Workflow con agentes especializados para desarrollo de software

agents:
  - name: generator
    role: feature_development
    prompt: "You are a generator. Build features one at a time..."
    capabilities:
      - code_generation
      - implementation
    max_retries: 3

  - name: qa
    role: testing
    prompt: "You are a QA agent. Test what the generator did..."
    capabilities:
      - testing
      - validation
    max_retries: 2

  - name: code_reviewer
    role: code_quality
    prompt: "You are a code reviewer. Review code quality..."
    capabilities:
      - code_review
      - quality
    max_retries: 2

  - name: docs
    role: documentation
    prompt: "You are a docs agent. Keep documentation updated..."
    capabilities:
      - documentation
      - readmes
    max_retries: 1

  - name: performance
    role: optimization
    prompt: "You are a performance agent. Optimize where needed..."
    capabilities:
      - optimization
      - profiling
    max_retries: 2

pipeline:
  - generator → qa (loop until pass)
  - qa → code_reviewer
  - code_reviewer → docs
  - docs → performance (optional)
  - all → merge
```

---

## Uso

### Python API

```python
# Legacy - API anterior a v6.1
# from 08_Scripts_Os.11_Anthropic_Harness.multi_agent_pipeline import (
#     PipelineBuilder, AgentRole
# )

# Crear pipeline
pipeline = (
    PipelineBuilder("mi-proyecto")
    .with_generator()
    .with_qa()
    .with_code_reviewer()
    .with_docs()
    .with_step("generator", "qa")
    .with_step("qa", "reviewer")
    .with_step("reviewer", "docs")
    .build()
)

# Ejecutar tarea
results = pipeline.execute_task("build-login", "Build a login feature")

# Ver resultados
for r in results:
    print(f"{r.agent_name}: {r.status}")
```

---

## Integración con Agent Teams

Este workflow se complementa con `07_Agent_Teams_Locks.py`:

- **Agent Teams**: Coordina múltiples agentes en paralelo
- **Multi-Agent Roles**: Define roles especializados y flujos

```python
# Legacy - API anterior a v6.1
# from 08_Scripts_Os.11_Anthropic_Harness.07_Agent_Teams_Locks import AgentTeam, GitLockManager

# Crear equipo con locks
manager = GitLockManager()
team = AgentTeam("dev-team", num_agents=16, lock_manager=manager)

# Integrar con pipeline de roles
#Cada agente del team ejecuta su rol especializado
```

---

## Métricas

| Métrica                     | Target   |
|-----------------------------|----------|
| Latencia por decisión       | <50ms    |
| Agentes en paralelo         | 16       |
| Tasa de éxito               | >90%     |
| Tiempo promedio por feature | <5min    |

---

## Archivos Relacionados

- `08_Scripts_Os/Legacy_Backup/11_Anthropic_Harness/07_Agent_Teams_Locks.py` (legacy)
- `01_Core/03_Skills/14_Anthropic_Harness/08_Graders_Framework/`
- `01_Core/03_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/`
