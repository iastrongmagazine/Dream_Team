---
name: evaluation-skill
description: >
  Agent and system evaluation frameworks. Includes performance metrics, quality assessment, and benchmarking.
  Trigger: evaluation, benchmark, performance metrics, quality assessment, agent evaluation, LLM evaluation.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# Evaluation Skill — Agent & System Evaluation

## When to Use

- Evaluating AI agent outputs
- Benchmarking system performance
- Measuring quality of generated code
- Comparing different approaches
- A/B testing for AI systems

## Critical Patterns

### 1. Evaluation Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    EVALUATION PYRAMID                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                        ┌─────────┐                              │
│                       /   GOLD   \                             │
│                      /  STANDARD  \                            │
│                     /───────────────\                           │
│                    │  UNIT TESTS   │                          │
│                    │  (Correctness)│                          │
│                    └───────────────┘                           │
│                                                                 │
│              ┌─────────────────────────┐                       │
│             /    INTEGRATION TESTS     \                      │
│            /     (Functionality)         \                     │
│           └─────────────────────────────┘                       │
│                                                                 │
│         ┌───────────────────────────────────┐                  │
│        /         E2E EVALUATION              \                │
│       /          (User Satisfaction)           \              │
│      └─────────────────────────────────────────┘                │
└─────────────────────────────────────────────────────────────────┘
```

### 2. RAGAS Metrics (RAG Evaluation)

| Metric | Purpose | Formula |
|--------|---------|---------|
| **Faithfulness** | Answer matches context | `correct_statements / total_statements` |
| **Answer Relevancy** | Answer addresses question | `semantic_similarity(question, answer)` |
| **Context Precision** | Relevant chunks ranked high | `Σ precision@k / total_relevant` |
| **Context Recall** | All relevant info retrieved | `retrieved_relevant / total_relevant` |

### 3. LLM-as-Judge Evaluation

```python
# Prompt for LLM evaluation
EVALUATION_PROMPT = """
You are an expert evaluator. Evaluate the following response:

Question: {question}
Response: {response}

Rate on scale 1-5 for:
1. Correctness
2. Completeness
3. Coherence
4. Helpfulness

Provide a JSON score with reasoning.
"""

# Structured output parsing
from pydantic import BaseModel

class EvaluationScore(BaseModel):
    correctness: int  # 1-5
    completeness: int  # 1-5
    coherence: int  # 1-5
    helpfulness: int  # 1-5
    reasoning: str
```

## Code Examples

### Agent Evaluation Framework

```python
from dataclasses import dataclass
from typing import Callable
import time

@dataclass
class EvaluationResult:
    metric: str
    score: float  # 0.0 - 1.0
    latency_ms: float
    metadata: dict

class AgentEvaluator:
    def __init__(self, agent: Callable):
        self.agent = agent
    
    def evaluate(
        self,
        test_cases: list[dict],
        metrics: list[str]
    ) -> list[EvaluationResult]:
        results = []
        
        for test_case in test_cases:
            start = time.perf_counter()
            
            try:
                output = self.agent(test_case['input'])
                latency = (time.perf_counter() - start) * 1000
                
                for metric in metrics:
                    score = self._calculate_metric(
                        metric,
                        output,
                        test_case['expected']
                    )
                    results.append(EvaluationResult(
                        metric=metric,
                        score=score,
                        latency_ms=latency,
                        metadata={'test_case': test_case['id']}
                    ))
            except Exception as e:
                results.append(EvaluationResult(
                    metric='error',
                    score=0.0,
                    latency_ms=latency,
                    metadata={'error': str(e)}
                ))
        
        return results
    
    def _calculate_metric(self, metric: str, output: str, expected: str) -> float:
        if metric == 'exact_match':
            return float(output.strip() == expected.strip())
        elif metric == 'contains':
            return float(expected in output)
        elif metric == 'similarity':
            return self._ cosine_similarity(output, expected)
        raise ValueError(f"Unknown metric: {metric}")
```

### Benchmarking Framework

```python
import statistics
from dataclasses import dataclass

@dataclass
class BenchmarkResult:
    name: str
    iterations: int
    mean_ms: float
    median_ms: float
    p95_ms: float
    p99_ms: float
    std_dev: float

def benchmark(fn: Callable, iterations: int = 1000) -> BenchmarkResult:
    times = []
    
    for _ in range(iterations):
        start = time.perf_counter()
        fn()
        elapsed = (time.perf_counter() - start) * 1000
        times.append(elapsed)
    
    return BenchmarkResult(
        name=fn.__name__,
        iterations=iterations,
        mean_ms=statistics.mean(times),
        median_ms=statistics.median(times),
        p95_ms=sorted(times)[int(iterations * 0.95)],
        p99_ms=sorted(times)[int(iterations * 0.99)],
        std_dev=statistics.stdev(times)
    )
```

## Commands

```bash
# Run evaluations with Evals
openai evals run --template=fact-checking my_eval.jsonl

# A/B test with Prometheus
curl "http://localhost:9090/api/v1/query?query=agent_accuracy{version=\"B\"}"

# Run benchmark suite
pytest tests/benchmarks/ -v --benchmark-only

# Generate evaluation report
python -m evaluation.report --format=markdown --output=eval_report.md
```

## Resources

- **Evals**: https://github.com/openai/evals
- **RAGAS**: https://docs.ragas.io/
- **Prometheus**: https://prometheus.io/
- **LM-Eval**: https://github.com/EleutherAI/lm-evaluation-harness
