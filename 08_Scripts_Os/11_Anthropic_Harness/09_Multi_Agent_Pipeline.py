"""
Multi-Agent Roles Workflow
Pipeline con agentes especializados para desarrollo de software.

Inspirado en: "Scaling Agentic Systems" article (Feb 25, 2026)
"""

from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import json


class AgentRole(Enum):
    """Roles disponibles para agentes."""

    GENERATOR = "generator"  # Construye features
    QA = "qa"  # Testing y validación
    CODE_REVIEWER = "code_reviewer"  # Calidad de código
    DOCUMENTATION = "documentation"  # Documentación
    PERFORMANCE = "performance"  # Optimización
    SECURITY = "security"  # Seguridad
    ARCHITECT = "architect"  # Diseño de arquitectura


@dataclass
class AgentSpec:
    """Especificación de un agente."""

    name: str
    role: AgentRole
    prompt: str
    capabilities: List[str] = field(default_factory=list)
    max_retries: int = 3
    timeout_seconds: int = 300


@dataclass
class TaskResult:
    """Resultado de una tarea ejecutada por un agente."""

    task_id: str
    agent_name: str
    role: AgentRole
    status: str  # "success", "failed", "timeout"
    output: str = ""
    error: Optional[str] = None
    duration_seconds: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class MultiAgentPipeline:
    """
    Pipeline que coordina múltiples agentes especializados.

    Flujo típico:
    generator → qa → code_reviewer → docs → (optional) performance → merge
    """

    def __init__(self, name: str):
        self.name = name
        self.agents: Dict[str, AgentSpec] = {}
        self.pipeline_steps: List[str] = []
        self.results: List[TaskResult] = []

    def register_agent(self, agent: AgentSpec) -> None:
        """Registra un agente en el pipeline."""
        self.agents[agent.name] = agent

    def add_step(
        self, from_agent: str, to_agent: str, condition: Optional[str] = None
    ) -> None:
        """
        Agrega un paso al pipeline.

        Args:
            from_agent: Agent name de origen
            to_agent: Agent name de destino
            condition: Condición opcional ("success", "failed", "always")
        """
        self.pipeline_steps.append(
            f"{from_agent}->{to_agent}" + (f":{condition}" if condition else "")
        )

    def execute_task(self, task: str, initial_input: str) -> List[TaskResult]:
        """
        Ejecuta una tarea a través del pipeline.

        Args:
            task: Nombre de la tarea
            initial_input: Input inicial para el primer agente

        Returns:
            Lista de resultados por cada agente
        """
        results = []

        # Encontrar el primer agente (el que no es destino de ningún paso)
        first_agent = self._find_first_agent()
        if not first_agent:
            # Si no hay steps, ejecutar todos los agentes en orden de registro
            for agent in self.agents.values():
                result = self._execute_agent(
                    agent, task, initial_input if not results else results[-1].output
                )
                results.append(result)
            return results

        # Ejecutar el primer agente
        current_output = initial_input
        current_agent_name = first_agent.name
        result = self._execute_agent(first_agent, task, current_output)
        results.append(result)
        current_output = result.output

        # Ejecutar el resto según los pasos del pipeline
        executed_agents = {first_agent.name}

        for step in self.pipeline_steps:
            parts = step.split("->")
            from_name = parts[0]
            to_name = parts[1].split(":")[0] if ":" in parts[1] else parts[1]
            condition = parts[1].split(":")[1] if ":" in parts[1] else "success"

            # Solo ejecutar si es el turno correcto
            if from_name != current_agent_name:
                continue

            # Verificar condición
            if condition == "success" and results[-1].status != "success":
                break
            if condition == "failed" and results[-1].status != "failed":
                continue

            # Ejecutar siguiente agente
            agent = self.agents.get(to_name)
            if not agent or to_name in executed_agents:
                continue

            result = self._execute_agent(agent, task, current_output)
            results.append(result)
            current_output = result.output
            current_agent_name = agent.name
            executed_agents.add(to_name)

        self.results.extend(results)
        return results

    def _find_first_agent(self) -> Optional[AgentSpec]:
        """Encuentra el primer agente (sin dependencias entrantes)."""
        # Encontrar agentes que no son destino de ningún paso
        targets = set()
        for step in self.pipeline_steps:
            to_name = step.split("->")[1].split(":")[0]
            targets.add(to_name)

        for name, agent in self.agents.items():
            if name not in targets:
                return agent

        # Si todos son objetivo, devolver el primero
        return list(self.agents.values())[0] if self.agents else None

    def _execute_agent(
        self, agent: AgentSpec, task: str, input_data: str
    ) -> TaskResult:
        """Simula la ejecución de un agente (en producción sería una llamada real)."""
        start_time = datetime.now()

        # Simular procesamiento
        # En producción, esto sería una llamada al agente real
        output = f"[{agent.role.value}] Processed: {input_data[:50]}..."

        duration = (datetime.now() - start_time).total_seconds()

        return TaskResult(
            task_id=f"{task}_{agent.name}",
            agent_name=agent.name,
            role=agent.role,
            status="success",
            output=output,
            duration_seconds=duration,
        )

    def get_pipeline_status(self) -> Dict[str, Any]:
        """Obtiene el estado del pipeline."""
        return {
            "name": self.name,
            "total_agents": len(self.agents),
            "total_steps": len(self.pipeline_steps),
            "total_executions": len(self.results),
            "agents": {
                name: {
                    "role": agent.role.value,
                    "capabilities": agent.capabilities,
                    "max_retries": agent.max_retries,
                }
                for name, agent in self.agents.items()
            },
            "steps": self.pipeline_steps,
        }

    def to_workflow_yaml(self) -> str:
        """Exporta el pipeline como workflow YAML."""
        lines = [
            f"name: {self.name}",
            "description: Multi-Agent Pipeline",
            "",
            "agents:",
        ]

        for name, agent in self.agents.items():
            lines.append(f"  - name: {name}")
            lines.append(f"    role: {agent.role.value}")
            lines.append(f'    prompt: "{agent.prompt[:50]}..."')
            lines.append(f"    capabilities:")
            for cap in agent.capabilities:
                lines.append(f"      - {cap}")
            lines.append(f"    max_retries: {agent.max_retries}")
            lines.append("")

        lines.append("pipeline:")
        for step in self.pipeline_steps:
            lines.append(f"  - {step}")

        return "\n".join(lines)


# ==================== BUILDER ====================


class PipelineBuilder:
    """Builder para crear pipelines fácilmente."""

    def __init__(self, name: str):
        self.pipeline = MultiAgentPipeline(name)

    def with_generator(self, name: str = "generator", **kwargs) -> "PipelineBuilder":
        """Agrega un agente generator."""
        prompt = kwargs.get(
            "prompt", "Eres un генератор. Construye features una a la vez."
        )
        self.pipeline.register_agent(
            AgentSpec(
                name=name,
                role=AgentRole.GENERATOR,
                prompt=prompt,
                capabilities=kwargs.get(
                    "capabilities", ["code_generation", "implementation"]
                ),
                max_retries=kwargs.get("max_retries", 3),
            )
        )
        return self

    def with_qa(self, name: str = "qa", **kwargs) -> "PipelineBuilder":
        """Agrega un agente QA."""
        prompt = kwargs.get(
            "prompt", "Eres un QA agent. Testea lo que el generator hizo."
        )
        self.pipeline.register_agent(
            AgentSpec(
                name=name,
                role=AgentRole.QA,
                prompt=prompt,
                capabilities=kwargs.get("capabilities", ["testing", "validation"]),
                max_retries=kwargs.get("max_retries", 2),
            )
        )
        return self

    def with_code_reviewer(self, name: str = "reviewer", **kwargs) -> "PipelineBuilder":
        """Agrega un agente code reviewer."""
        prompt = kwargs.get(
            "prompt", "Eres un code reviewer. Revisa calidad del código."
        )
        self.pipeline.register_agent(
            AgentSpec(
                name=name,
                role=AgentRole.CODE_REVIEWER,
                prompt=prompt,
                capabilities=kwargs.get("capabilities", ["code_review", "quality"]),
                max_retries=kwargs.get("max_retries", 2),
            )
        )
        return self

    def with_docs(self, name: str = "docs", **kwargs) -> "PipelineBuilder":
        """Agrega un agente de documentación."""
        prompt = kwargs.get("prompt", "Eres un docs agent. Mantén la documentación.")
        self.pipeline.register_agent(
            AgentSpec(
                name=name,
                role=AgentRole.DOCUMENTATION,
                prompt=prompt,
                capabilities=kwargs.get("capabilities", ["documentation", "readmes"]),
                max_retries=kwargs.get("max_retries", 1),
            )
        )
        return self

    def with_performance(self, name: str = "perf", **kwargs) -> "PipelineBuilder":
        """Agrega un agente de performance."""
        prompt = kwargs.get(
            "prompt", "Eres un performance agent. Optimiza donde sea necesario."
        )
        self.pipeline.register_agent(
            AgentSpec(
                name=name,
                role=AgentRole.PERFORMANCE,
                prompt=prompt,
                capabilities=kwargs.get("capabilities", ["optimization", "profiling"]),
                max_retries=kwargs.get("max_retries", 2),
            )
        )
        return self

    def with_step(
        self, from_agent: str, to_agent: str, condition: str = "success"
    ) -> "PipelineBuilder":
        """Agrega un paso al pipeline."""
        self.pipeline.add_step(from_agent, to_agent, condition)
        return self

    def build(self) -> MultiAgentPipeline:
        """Construye el pipeline."""
        return self.pipeline


# ==================== TESTS ====================


def test_pipeline_creation():
    """Test creación de pipeline."""
    pipeline = (
        PipelineBuilder("test-pipeline")
        .with_generator()
        .with_qa()
        .with_code_reviewer()
        .with_step("generator", "qa")
        .with_step("qa", "reviewer")
        .build()
    )

    print(f"DEBUG: agents={list(pipeline.agents.keys())}")
    print(f"DEBUG: pipeline_steps={pipeline.pipeline_steps}")

    assert len(pipeline.agents) == 3
    assert len(pipeline.pipeline_steps) == 2
    assert any("generator" in step and "qa" in step for step in pipeline.pipeline_steps)


def test_pipeline_execution():
    """Test ejecución de pipeline."""
    pipeline = (
        PipelineBuilder("test")
        .with_generator()
        .with_qa()
        .with_step("generator", "qa")
        .build()
    )

    results = pipeline.execute_task("build-login", "Build a login feature")

    print(f"DEBUG: results={len(results)}, agents={list(pipeline.agents.keys())}")
    for r in results:
        print(f"  - {r.agent_name}: {r.role}")

    assert len(results) >= 1  # At least one agent should run
    assert results[0].role == AgentRole.GENERATOR


def test_yaml_export():
    """Test exportación YAML."""
    pipeline = PipelineBuilder("export-test").with_generator().with_qa().build()

    yaml = pipeline.to_workflow_yaml()

    assert "export-test" in yaml
    assert "generator" in yaml
    assert "qa" in yaml


def test_pipeline_status():
    """Test estado del pipeline."""
    pipeline = (
        PipelineBuilder("status-test")
        .with_generator()
        .with_qa()
        .with_code_reviewer()
        .with_step("generator", "qa")
        .with_step("qa", "reviewer")
        .build()
    )

    status = pipeline.get_pipeline_status()

    assert status["total_agents"] == 3
    assert status["total_steps"] == 2


if __name__ == "__main__":
    print("=" * 60)
    print("Multi-Agent Roles Workflow - Tests")
    print("=" * 60)

    test_pipeline_creation()
    print("[PASS] test_pipeline_creation")

    test_pipeline_execution()
    print("[PASS] test_pipeline_execution")

    test_yaml_export()
    print("[PASS] test_yaml_export")

    test_pipeline_status()
    print("[PASS] test_pipeline_status")

    print()
    print("*** ALL TESTS PASSED ***")
    print()
    print("=" * 60)
    print("Example Pipeline:")
    print("=" * 60)

    # Ejemplo - usar prompts en inglés para evitar Unicode
    pipeline = (
        PipelineBuilder("full-pipeline")
        .with_generator(prompt="You are a generator. Build features one at a time.")
        .with_qa(prompt="You are a QA agent. Test what the generator built.")
        .with_code_reviewer(prompt="You are a code reviewer. Review code quality.")
        .with_docs(prompt="You are a docs agent. Maintain documentation.")
        .with_performance(prompt="You are a performance agent. Optimize where needed.")
        .with_step("generator", "qa")
        .with_step("qa", "reviewer")
        .with_step("reviewer", "docs")
        .with_step("docs", "perf", "optional")
        .build()
    )

    try:
        print(pipeline.to_workflow_yaml())
    except UnicodeEncodeError:
        print("(Unicode not supported)")
        print(f"Pipeline: {pipeline.name} with {len(pipeline.agents)} agents")
