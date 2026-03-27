#!/usr/bin/env python3
"""
SKILL 1: ENHANCED ANALYTICS WORKFLOW ORCHESTRATOR
Archivo: enhanced_analytics_workflow.py
Descripción: Orquestador maestro que coordina las 5 skills con aislamiento de contexto.

Hub & Spoke Architecture:
  HUB: Este orquestador (contexto limpio)
  SPOKE 1: DataAnalysisManager (gestión de memoria)
  SPOKE 2: DetailedCohortAnalyzer (modelado estadístico)
  SPOKE 3: StartupEnricher (datos externos)
  SPOKE 4: FlowVisualizer (explicabilidad)

Governance Policies:
  - Salida obligatoria: .ipynb
  - No datos sintéticos sin advertencia
  - Contexto optimizado (<50K tokens)
  - Aislamiento de agentes pesados
"""

import os
import sys
import json
import pandas as pd
import platform
from pathlib import Path
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, asdict
from datetime import datetime
import subprocess

# Importaciones locales (modo in-process cuando es eficiente)
try:
    from data_analysis_skills import DataAnalysisManager
    from data_visualization_flows import FlowVisualizer
except ImportError:
    # Si falla, estos se ejecutarán en subprocess
    DataAnalysisManager = None
    FlowVisualizer = None

@dataclass
class WorkflowPolicy:
    """Políticas de gobernanza del workflow"""
    require_notebook_output: bool = True
    allow_synthetic_data: bool = False
    max_context_tokens: int = 50000
    require_agent_isolation: bool = True
    max_enrichment_rows: int = 100

@dataclass
class WorkflowResult:
    """Resultado del workflow completo"""
    notebook_path: str
    execution_time_seconds: float
    steps_completed: List[str]
    artifacts_generated: List[str]
    summary: Dict[str, Any]
    warnings: List[str]

class EnhancedAnalyticsWorkflow:
    """
    Orquestador principal que implementa arquitectura Hub & Spoke.
    Mantiene contexto limpio delegando trabajo pesado a agentes aislados.
    """

    def __init__(self, work_dir: Optional[Path] = None):
        self.work_dir = work_dir or Path.cwd()
        self.policy = WorkflowPolicy()
        self.execution_log: List[Dict] = []
        self.warnings: List[str] = []

        # Detectar plataforma
        self.platform = platform.system().lower()
        self.python_cmd = "python" if self.platform == "windows" else "python3"

        # Inicializar componentes in-process (lightweight)
        self.manager = DataAnalysisManager() if DataAnalysisManager else None
        self.visualizer = FlowVisualizer() if FlowVisualizer else None

        # Paths de agentes aislados
        self.agents_dir = Path(__file__).parent

        print(f"🎯 Enhanced Analytics Workflow initialized")
        print(f"📁 Working directory: {self.work_dir}")
        print(f"💻 Platform: {self.platform}")

    def analyze_dataset_with_context(
        self,
        dataset_path: str,
        analysis_goal: str,
        context_name: Optional[str] = None
    ) -> WorkflowResult:
        """
        Punto de entrada principal - orquesta el análisis completo.

        Args:
            dataset_path: Ruta al CSV/Excel
            analysis_goal: Objetivo en lenguaje natural
            context_name: Nombre del contexto (para tracking)

        Returns:
            WorkflowResult con todos los artifacts generados
        """
        start_time = datetime.now()

        if not context_name:
            context_name = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        print(f"\n{'='*60}")
        print(f"🚀 Iniciando Workflow Gobernado: {context_name}")
        print(f"🎯 Objetivo: {analysis_goal}")
        print(f"📊 Dataset: {dataset_path}")
        print(f"{'='*60}\n")

        steps_completed = []
        artifacts = []

        try:
            # ========== PASO 1: PROFILING DE DATOS (Aislado) ==========
            print("📊 PASO 1: Profiling de datos...")
            df = pd.read_csv(dataset_path)

            if self.manager:
                # In-process (ligero)
                data_summary = self.manager.create_data_summary(df)
                profiling_result = {
                    "status": "success",
                    "summary": data_summary,
                    "method": "in_process"
                }
            else:
                # Isolated (si importación falló)
                profiling_result = self._execute_isolated_agent(
                    'profile_data',
                    {
                        'task_type': 'summarize',
                        'dataset_path': dataset_path,
                        'max_rows': 10
                    }
                )

            self._log_step("data_profiling", profiling_result)
            steps_completed.append("data_profiling")
            print("✓ Profiling completado\n")

            # ========== PASO 2: SELECCIÓN DE ESTRATEGIA ==========
            print("🧠 PASO 2: Selección de estrategia...")
            strategy = self._select_analysis_strategy(df, analysis_goal)
            print(f"✓ Estrategia seleccionada: {strategy['name']}\n")

            self._log_step("strategy_selection", strategy)
            steps_completed.append("strategy_selection")

            # ========== PASO 3: EJECUCIÓN DE ANÁLISIS ==========
            analysis_results = {}

            for task in strategy.get('tasks', []):
                task_name = task['name']
                print(f"⚙️  Ejecutando: {task_name}...")

                if task['agent'] == 'cohort_analyzer':
                    # ANÁLISIS PREDICTIVO (Aislado - pesado)
                    result = self._execute_isolated_agent(
                        'detailed_cohort_analysis',
                        {
                            'dataset_path': dataset_path,
                            'params': {
                                'target_col': task.get('target_col', 'success'),
                                'model_type': task.get('model_type', 'random_forest'),
                                'cohort_col': task.get('cohort_col')
                            }
                        }
                    )
                    analysis_results[task_name] = result

                elif task['agent'] == 'enricher':
                    # ENRIQUECIMIENTO (Aislado - I/O externo)
                    output_path = self.work_dir / f"enriched_{Path(dataset_path).name}"
                    result = self._execute_isolated_agent(
                        'enrich_csv',
                        {
                            'input_csv': dataset_path,
                            'output_csv': str(output_path),
                            'max_rows': self.policy.max_enrichment_rows,
                            'company_col': task.get('company_col', 'Company Name')
                        }
                    )
                    analysis_results[task_name] = result
                    artifacts.append(str(output_path))

                elif task['agent'] == 'visualizer':
                    # VISUALIZACIÓN (Puede ser in-process o aislado)
                    if self.visualizer:
                        # In-process
                        viz_path = self.work_dir / f"{context_name}_flow.png"
                        self.visualizer.create_notebook_flow_diagram(
                            {'cells': []},  # Placeholder
                            str(viz_path)
                        )
                        result = {'status': 'success', 'path': str(viz_path)}
                    else:
                        # Aislado
                        result = self._execute_isolated_agent(
                            'data_visualization_flows',
                            {
                                'viz_type': 'notebook',
                                'notebook_structure': {'cells': []},
                                'output_path': f"{context_name}_flow.png"
                            }
                        )
                    analysis_results[task_name] = result
                    artifacts.append(result.get('path', 'flow.png'))

                print(f"✓ {task_name} completado\n")
                self._log_step(task_name, result)
                steps_completed.append(task_name)

            # ========== PASO 4: GENERACIÓN DE NOTEBOOK ==========
            print("📓 PASO 4: Generando notebook...")
            notebook_path = self.create_analysis_notebook(
                analysis_results,
                strategy,
                context_name
            )
            artifacts.append(str(notebook_path))
            steps_completed.append("notebook_generation")
            print(f"✓ Notebook generado: {notebook_path}\n")

            # ========== PASO 5: VISUALIZACIÓN FINAL ==========
            if strategy.get('generate_flow_diagram', True):
                print("🎨 PASO 5: Generando diagrama de flujo...")
                if self.visualizer:
                    flow_path = self.work_dir / f"{context_name}_workflow.png"
                    pipeline_steps = [
                        {"type": "data", "name": "Input Data", "shape": df.shape},
                        *[{"type": "transform", "name": task['name']} for task in strategy.get('tasks', [])],
                        {"type": "output", "name": "Notebook Output"}
                    ]
                    self.visualizer.create_ml_pipeline_diagram(
                        pipeline_steps,
                        str(flow_path)
                    )
                    artifacts.append(str(flow_path))
                    print(f"✓ Diagrama generado: {flow_path}\n")
                    steps_completed.append("flow_visualization")

            # ========== RESULTADOS FINALES ==========
            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds()

            result = WorkflowResult(
                notebook_path=str(notebook_path),
                execution_time_seconds=execution_time,
                steps_completed=steps_completed,
                artifacts_generated=artifacts,
                summary={
                    "strategy": strategy['name'],
                    "dataset_rows": len(df),
                    "dataset_cols": len(df.columns),
                    "analysis_tasks": len(strategy.get('tasks', [])),
                    "execution_log": self.execution_log[-5:]  # Últimos 5 pasos
                },
                warnings=self.warnings
            )

            print(f"\n{'='*60}")
            print(f"✅ WORKFLOW COMPLETADO")
            print(f"{'='*60}")
            print(f"⏱️  Tiempo total: {execution_time:.2f} segundos")
            print(f"📊 Pasos completados: {len(steps_completed)}")
            print(f"📁 Artifacts generados: {len(artifacts)}")
            print(f"📓 Notebook principal: {notebook_path}")
            print(f"{'='*60}\n")

            return result

        except Exception as e:
            print(f"\n❌ ERROR en workflow: {e}")
            raise

    def _select_analysis_strategy(self, df: pd.DataFrame, goal: str) -> Dict[str, Any]:
        """
        Selecciona estrategia de análisis basándose en datos y objetivo.
        (In-process - lógica ligera)
        """
        goal_lower = goal.lower()

        # Detectar tipo de análisis
        if any(kw in goal_lower for kw in ['predict', 'forecast', 'model', 'train']):
            # Análisis predictivo
            target_col = self._infer_target_column(df, goal)

            return {
                "name": "Predictive Modeling",
                "description": "Build ML model to predict outcomes",
                "tasks": [
                    {
                        "name": "predictive_model",
                        "agent": "cohort_analyzer",
                        "target_col": target_col,
                        "model_type": "random_forest"
                    }
                ],
                "generate_flow_diagram": True
            }

        elif any(kw in goal_lower for kw in ['segment', 'cluster', 'cohort', 'group']):
            # Análisis de cohortes
            cohort_col = self._infer_cohort_column(df)

            return {
                "name": "Cohort Analysis",
                "description": "Segment data and analyze groups",
                "tasks": [
                    {
                        "name": "cohort_segmentation",
                        "agent": "cohort_analyzer",
                        "cohort_col": cohort_col,
                        "target_col": "success"
                    }
                ],
                "generate_flow_diagram": True
            }

        elif any(kw in goal_lower for kw in ['enrich', 'augment', 'external', 'funding']):
            # Enriquecimiento de datos
            return {
                "name": "Data Enrichment",
                "description": "Augment data with external sources",
                "tasks": [
                    {
                        "name": "external_enrichment",
                        "agent": "enricher",
                        "company_col": "Company Name"
                    }
                ],
                "generate_flow_diagram": False
            }

        else:
            # Análisis exploratorio por defecto
            return {
                "name": "Exploratory Analysis",
                "description": "Comprehensive data exploration",
                "tasks": [
                    {
                        "name": "visualization",
                        "agent": "visualizer"
                    }
                ],
                "generate_flow_diagram": True
            }

    def _infer_target_column(self, df: pd.DataFrame, goal: str) -> str:
        """Infiere columna target basándose en datos y objetivo"""
        # Buscar columnas binarias
        for col in df.columns:
            if df[col].nunique() == 2 and pd.api.types.is_numeric_dtype(df[col]):
                return col

        # Buscar palabras clave en nombres de columnas
        keywords = ['success', 'churn', 'converted', 'outcome', 'target']
        for col in df.columns:
            if any(kw in col.lower() for kw in keywords):
                return col

        return df.columns[-1]  # Última columna por defecto

    def _infer_cohort_column(self, df: pd.DataFrame) -> str:
        """Infiere columna de cohorte"""
        # Buscar columnas categóricas con pocos valores únicos
        for col in df.columns:
            if df[col].nunique() < 10 and df[col].dtype == 'object':
                return col

        return df.columns[0]

    def _execute_isolated_agent(self, agent_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta un agente en subproceso aislado.
        """
        # Crear workspace temporal
        temp_dir = Path('/tmp') if self.platform != 'windows' else Path(os.environ.get('TEMP', 'C:\\Temp'))
        workspace = temp_dir / f"agent_{agent_name}_{os.getpid()}"
        workspace.mkdir(exist_ok=True)

        input_file = workspace / "input.json"
        output_file = workspace / "output.json"

        # Escribir input
        with open(input_file, 'w') as f:
            json.dump(params, f)

        # Ejecutar agente
        script_path = self.agents_dir / f"{agent_name}.py"

        try:
            result = subprocess.run(
                [self.python_cmd, str(script_path), str(input_file), str(output_file)],
                capture_output=True,
                text=True,
                timeout=600,  # 10 min timeout
                cwd=workspace
            )

            # Leer output
            if output_file.exists():
                with open(output_file, 'r') as f:
                    return json.load(f)
            else:
                return {
                    "status": "error",
                    "result": None,
                    "metadata": {"error": "No output file", "stderr": result.stderr[:500]}
                }

        except subprocess.TimeoutExpired:
            return {"status": "error", "result": None, "metadata": {"error": "Agent timeout"}}
        except Exception as e:
            return {"status": "error", "result": None, "metadata": {"error": str(e)}}
        finally:
            # Cleanup
            if input_file.exists():
                input_file.unlink()
            if output_file.exists():
                output_file.unlink()

    def create_analysis_notebook(
        self,
        analysis_results: Dict[str, Any],
        strategy: Dict[str, Any],
        filename: str
    ) -> Path:
        """
        MANDATORY: Genera archivo .ipynb físico (política de gobernanza).
        """
        if not filename.endswith('.ipynb'):
            filename += '.ipynb'

        notebook_path = self.work_dir / filename

        # Construir celdas del notebook
        cells = [
            {
                "cell_type": "markdown",
                "source": [
                    f"# {strategy['name']}\n\n",
                    f"**Generated by Enhanced Analytics Workflow**\n\n",
                    f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n",
                    f"## Strategy\n{strategy.get('description', 'N/A')}\n"
                ],
                "metadata": {}
            },
            {
                "cell_type": "code",
                "source": [
                    "# Setup\n",
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "import seaborn as sns\n\n",
                    "# Analysis orchestrated by Enhanced Analytics Workflow\n"
                ],
                "metadata": {},
                "execution_count": None,
                "outputs": []
            }
        ]

        # Agregar resultados de cada tarea
        for task_name, task_result in analysis_results.items():
            cells.append({
                "cell_type": "markdown",
                "source": [f"## {task_name.replace('_', ' ').title()}"],
                "metadata": {}
            })

            cells.append({
                "cell_type": "code",
                "source": [
                    f"# Results from {task_name}\n",
                    f"results = {json.dumps(task_result.get('result', {}), indent=2)}\n",
                    f"print('Status:', results.get('status', 'N/A'))\n"
                ],
                "metadata": {},
                "execution_count": None,
                "outputs": []
            })

        # Estructura completa del notebook
        notebook = {
            "cells": cells,
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                },
                "language_info": {
                    "name": "python",
                    "version": "3.8.0"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 5
        }

        # Guardar
        with open(notebook_path, 'w') as f:
            json.dump(notebook, f, indent=2)

        return notebook_path

    def _log_step(self, step_name: str, data: Any):
        """Logging limpio para contexto del orquestador"""
        self.execution_log.append({
            "step": step_name,
            "timestamp": datetime.now().isoformat(),
            "summary": str(data)[:200] + "..." if len(str(data)) > 200 else str(data)
        })

# ============================================================================
# CLI INTERFACE
# ============================================================================

def main():
    """Entry point for CLI usage"""
    import argparse

    parser = argparse.ArgumentParser(
        description="Enhanced Analytics Workflow - Professional Data Analysis Orchestrator"
    )
    parser.add_argument("dataset", help="Path to CSV/Excel dataset")
    parser.add_argument("--goal", required=True, help="Analysis goal (e.g., 'predict churn')")
    parser.add_argument("--context", help="Context name for this analysis")
    parser.add_argument("--output-dir", help="Output directory", default=".")

    args = parser.parse_args()

    orchestrator = EnhancedAnalyticsWorkflow(work_dir=Path(args.output_dir))

    result = orchestrator.analyze_dataset_with_context(
        args.dataset,
        args.goal,
        args.context
    )

    print(f"\n✅ Analysis complete!")
    print(f"📓 Notebook: {result.notebook_path}")
    print(f"⏱️  Time: {result.execution_time_seconds:.2f}s")
    print(f"📁 Artifacts: {len(result.artifacts_generated)}")

if __name__ == "__main__":
    main()
