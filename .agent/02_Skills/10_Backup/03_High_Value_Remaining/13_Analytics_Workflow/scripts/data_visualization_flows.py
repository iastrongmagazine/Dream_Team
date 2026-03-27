#!/usr/bin/env python3
"""
SKILL 5: META-ANALYSIS VISUALIZATION
Archivo: data_visualization_flows.py
Descripción: Genera visualizaciones de flujos de trabajo y linaje de datos.

Use Cases:
- Diagramas de flujo de notebooks
- Grafos de dependencias SQL
- Mapas de transformación de datos
- Explicabilidad de pipelines ML

Execution Mode: Isolated subprocess (matplotlib/networkx rendering)
"""

import sys
import json
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Backend sin GUI para modo servidor
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass
import base64
from io import BytesIO

@dataclass
class FlowNode:
    """Nodo en el flujo de análisis"""
    id: str
    type: str  # 'data', 'transform', 'model', 'output'
    label: str
    metadata: Dict[str, Any]

@dataclass
class FlowEdge:
    """Conexión entre nodos"""
    source: str
    target: str
    label: Optional[str] = None

class FlowVisualizer:
    """
    Visualizador de flujos analíticos y linaje de datos.
    Genera diagramas explicativos de pipelines complejos.
    """

    def __init__(self):
        self.graphs = {}
        self.color_scheme = {
            'data': '#3498db',      # Azul
            'transform': '#2ecc71', # Verde
            'model': '#e74c3c',     # Rojo
            'output': '#f39c12',    # Naranja
            'code': '#9b59b6',      # Púrpura
            'markdown': '#95a5a6'   # Gris
        }

    def create_notebook_flow_diagram(
        self,
        notebook_structure: Dict,
        output_path: str = 'notebook_flow.png'
    ) -> str:
        """
        Crea un grafo dirigido de celdas de notebook mostrando flujo de ejecución.

        Args:
            notebook_structure: Estructura JSON del notebook
            output_path: Ruta donde guardar el diagrama

        Returns:
            Path del archivo generado
        """
        G = nx.DiGraph()

        cells = notebook_structure.get('cells', [])

        # Crear nodos
        for i, cell in enumerate(cells):
            node_id = f"Cell_{i}"
            cell_type = cell.get('cell_type', 'unknown')

            # Extraer preview del contenido
            source = cell.get('source', [])
            if isinstance(source, list):
                preview = ''.join(source)[:50]
            else:
                preview = str(source)[:50]

            preview = preview.replace('\n', ' ')

            G.add_node(
                node_id,
                type=cell_type,
                label=f"{cell_type.capitalize()}\n{preview}...",
                color=self.color_scheme.get(cell_type, '#cccccc')
            )

            # Crear edge secuencial
            if i > 0:
                G.add_edge(f"Cell_{i-1}", node_id)

        # Detectar dependencias adicionales (imports, variables)
        self._detect_notebook_dependencies(G, cells)

        # Renderizar
        output_path = Path(output_path)
        self._render_graph(G, output_path, title="Notebook Execution Flow")

        print(f"📊 Diagrama de flujo generado: {output_path}")
        print(f"   - Nodos: {len(G.nodes)}")
        print(f"   - Conexiones: {len(G.edges)}")

        return str(output_path)

    def _detect_notebook_dependencies(self, G: nx.DiGraph, cells: List[Dict]):
        """
        Detecta dependencias entre celdas basándose en variables.
        (Versión simplificada - producción requeriría AST parsing)
        """
        import re

        # Rastrear variables definidas
        variables_defined = {}

        for i, cell in enumerate(cells):
            if cell.get('cell_type') != 'code':
                continue

            source = ''.join(cell.get('source', []))
            node_id = f"Cell_{i}"

            # Detectar asignaciones (pattern simple)
            assignments = re.findall(r'^(\w+)\s*=', source, re.MULTILINE)
            for var in assignments:
                variables_defined[var] = node_id

            # Detectar usos de variables
            for var, def_node in variables_defined.items():
                if var in source and def_node != node_id:
                    # Agregar edge de dependencia
                    if not G.has_edge(def_node, node_id):
                        G.add_edge(def_node, node_id, style='dashed', label=f'uses {var}')

    def create_data_lineage_graph(
        self,
        transformations: List[Dict[str, Any]],
        output_path: str = 'data_lineage.png'
    ) -> str:
        """
        Crea grafo de linaje de datos mostrando origen y transformaciones.

        Args:
            transformations: Lista de transformaciones aplicadas
                [
                    {"type": "source", "name": "customers.csv"},
                    {"type": "filter", "name": "Active customers", "condition": "status='active'"},
                    {"type": "join", "name": "Add revenue", "with": "transactions.csv"},
                    {"type": "aggregate", "name": "Total by customer"},
                    {"type": "output", "name": "customer_summary.csv"}
                ]

        Returns:
            Path del archivo generado
        """
        G = nx.DiGraph()

        for i, transform in enumerate(transformations):
            node_id = f"step_{i}"
            node_type = transform.get('type', 'transform')

            G.add_node(
                node_id,
                label=transform.get('name', f'Step {i}'),
                type=node_type,
                color=self.color_scheme.get(node_type, '#95a5a6')
            )

            # Conectar con paso anterior
            if i > 0:
                G.add_edge(f"step_{i-1}", node_id)

            # Agregar detalles como atributos
            if 'condition' in transform:
                G.nodes[node_id]['condition'] = transform['condition']
            if 'with' in transform:
                # Agregar nodo de fuente adicional
                extra_source = f"source_{transform['with']}"
                if not G.has_node(extra_source):
                    G.add_node(extra_source, label=transform['with'], type='data', color=self.color_scheme['data'])
                G.add_edge(extra_source, node_id, label='join')

        output_path = Path(output_path)
        self._render_graph(G, output_path, title="Data Lineage", layout='hierarchical')

        return str(output_path)

    def create_ml_pipeline_diagram(
        self,
        pipeline_steps: List[Dict[str, Any]],
        output_path: str = 'ml_pipeline.png'
    ) -> str:
        """
        Visualiza pipeline de ML: data → preprocessing → model → evaluation.

        Args:
            pipeline_steps: Pasos del pipeline
                [
                    {"type": "data", "name": "Raw Data", "shape": [1000, 20]},
                    {"type": "transform", "name": "Impute Missing", "method": "median"},
                    {"type": "transform", "name": "Scale Features", "method": "StandardScaler"},
                    {"type": "model", "name": "RandomForest", "params": {"n_estimators": 100}},
                    {"type": "output", "name": "Predictions", "metrics": {"auc": 0.87}}
                ]
        """
        G = nx.DiGraph()

        for i, step in enumerate(pipeline_steps):
            node_id = f"step_{i}"
            step_type = step.get('type', 'transform')

            # Crear label con detalles
            label_parts = [step.get('name', f'Step {i}')]

            if 'shape' in step:
                label_parts.append(f"Shape: {step['shape']}")
            if 'method' in step:
                label_parts.append(f"Method: {step['method']}")
            if 'metrics' in step:
                metrics_str = ', '.join(f"{k}={v}" for k, v in step['metrics'].items())
                label_parts.append(metrics_str)

            G.add_node(
                node_id,
                label='\n'.join(label_parts),
                type=step_type,
                color=self.color_scheme.get(step_type, '#95a5a6')
            )

            if i > 0:
                G.add_edge(f"step_{i-1}", node_id)

        output_path = Path(output_path)
        self._render_graph(
            G,
            output_path,
            title="ML Pipeline",
            layout='hierarchical',
            figsize=(14, 8)
        )

        return str(output_path)

    def create_sql_dependency_graph(
        self,
        queries: List[str],
        output_path: str = 'sql_dependencies.png'
    ) -> str:
        """
        Genera grafo de dependencias entre tablas basándose en queries SQL.
        """
        import re

        G = nx.DiGraph()

        # Extraer tablas de cada query
        for i, query in enumerate(queries):
            # Detectar tablas en FROM, JOIN
            from_tables = re.findall(r'FROM\s+([a-zA-Z0-9_.]+)', query, re.IGNORECASE)
            join_tables = re.findall(r'JOIN\s+([a-zA-Z0-9_.]+)', query, re.IGNORECASE)
            into_tables = re.findall(r'INTO\s+([a-zA-Z0-9_.]+)', query, re.IGNORECASE)

            all_source_tables = set(from_tables + join_tables)
            all_target_tables = set(into_tables)

            # Agregar nodos
            for table in all_source_tables:
                if not G.has_node(table):
                    G.add_node(table, type='source', color=self.color_scheme['data'])

            for table in all_target_tables:
                if not G.has_node(table):
                    G.add_node(table, type='derived', color=self.color_scheme['transform'])

            # Agregar edges
            for target in all_target_tables:
                for source in all_source_tables:
                    G.add_edge(source, target, label=f'Query {i+1}')

        output_path = Path(output_path)
        self._render_graph(G, output_path, title="SQL Table Dependencies")

        return str(output_path)

    def _render_graph(
        self,
        G: nx.DiGraph,
        output_path: Path,
        title: str = "Flow Diagram",
        layout: str = 'spring',
        figsize: Tuple[int, int] = (12, 8)
    ):
        """
        Renderiza grafo a imagen PNG.

        Args:
            layout: 'spring', 'hierarchical', 'circular'
        """
        plt.figure(figsize=figsize)

        # Seleccionar layout
        if layout == 'hierarchical':
            pos = nx.spring_layout(G, k=2, iterations=50)
        elif layout == 'circular':
            pos = nx.circular_layout(G)
        else:
            pos = nx.spring_layout(G)

        # Extraer colores de nodos
        node_colors = [G.nodes[node].get('color', '#cccccc') for node in G.nodes()]

        # Dibujar
        nx.draw_networkx_nodes(
            G, pos,
            node_color=node_colors,
            node_size=3000,
            alpha=0.9
        )

        nx.draw_networkx_labels(
            G, pos,
            labels={node: G.nodes[node].get('label', node) for node in G.nodes()},
            font_size=8,
            font_weight='bold'
        )

        nx.draw_networkx_edges(
            G, pos,
            edge_color='#7f8c8d',
            arrows=True,
            arrowsize=20,
            arrowstyle='->',
            width=2
        )

        # Edge labels si existen
        edge_labels = nx.get_edge_attributes(G, 'label')
        if edge_labels:
            nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=7)

        plt.title(title, fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()

        # Guardar
        plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()

    def generate_base64_image(self, image_path: str) -> str:
        """
        Convierte imagen a base64 para embedding en notebooks/HTML.
        """
        with open(image_path, 'rb') as f:
            img_data = f.read()

        b64_data = base64.b64encode(img_data).decode('utf-8')
        return f"data:image/png;base64,{b64_data}"

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_visualization(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta visualización en modo aislado.
    """
    visualizer = FlowVisualizer()

    viz_type = params.get('viz_type', 'notebook')
    output_path = params.get('output_path', 'flow_diagram.png')

    if viz_type == 'notebook':
        notebook_data = params.get('notebook_structure')
        if not notebook_data:
            raise ValueError("notebook_structure required for notebook visualization")

        result_path = visualizer.create_notebook_flow_diagram(notebook_data, output_path)

    elif viz_type == 'lineage':
        transformations = params.get('transformations', [])
        result_path = visualizer.create_data_lineage_graph(transformations, output_path)

    elif viz_type == 'ml_pipeline':
        pipeline_steps = params.get('pipeline_steps', [])
        result_path = visualizer.create_ml_pipeline_diagram(pipeline_steps, output_path)

    elif viz_type == 'sql_dependencies':
        queries = params.get('queries', [])
        result_path = visualizer.create_sql_dependency_graph(queries, output_path)

    else:
        raise ValueError(f"Unknown visualization type: {viz_type}")

    # Generar base64 si se solicita
    include_base64 = params.get('include_base64', False)
    base64_image = None
    if include_base64:
        base64_image = visualizer.generate_base64_image(result_path)

    return {
        "diagram_path": result_path,
        "base64_image": base64_image,
        "viz_type": viz_type
    }

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: data_visualization_flows.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_visualization(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {
                    "agent": "flow_visualizer",
                    "version": "2.0",
                    "supported_types": ["notebook", "lineage", "ml_pipeline", "sql_dependencies"]
                }
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {
                    "error": str(e),
                    "agent": "flow_visualizer"
                }
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
