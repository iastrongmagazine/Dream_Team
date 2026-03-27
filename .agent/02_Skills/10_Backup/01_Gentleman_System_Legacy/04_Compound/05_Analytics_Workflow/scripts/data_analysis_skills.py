#!/usr/bin/env python3
"""
SKILL 2: DATA ANALYSIS MANAGER
Archivo: data_analysis_skills.py
Descripción: Gestión de tokens, resúmenes inteligentes y dependencias SQL.

Execution Mode: Can run both in-process and isolated
"""

import sys
import json
import pandas as pd
import re
from pathlib import Path
from typing import Dict, List, Optional, Any

class DataAnalysisManager:
    """
    Gestor de contexto y memoria técnica.
    Optimiza el uso de tokens creando resúmenes inteligentes.
    """

    def __init__(self):
        self.context_budget = 50000  # tokens
        self.summaries_cache = {}

    def create_data_summary(self, df: pd.DataFrame, max_rows: int = 5) -> str:
        """
        Crea una representación eficiente en tokens del DataFrame.
        Evita saturar el contexto con datos completos.
        """
        buffer = []
        buffer.append(f"📊 Dataset Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
        buffer.append(f"💾 Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB\n")

        buffer.append("📋 Column Metadata:")
        for col in df.columns:
            dtype = df[col].dtype
            missing = df[col].isna().sum()
            missing_pct = (missing / len(df)) * 100
            unique = df[col].nunique()

            buffer.append(f"  • {col}")
            buffer.append(f"    - Type: {dtype}")
            buffer.append(f"    - Missing: {missing:,} ({missing_pct:.1f}%)")
            buffer.append(f"    - Unique: {unique:,}")

            # Stats para columnas numéricas
            if pd.api.types.is_numeric_dtype(dtype):
                buffer.append(f"    - Range: [{df[col].min():.2f}, {df[col].max():.2f}]")
                buffer.append(f"    - Mean: {df[col].mean():.2f}")

        buffer.append(f"\n🔍 Sample (first {max_rows} rows):")
        buffer.append(df.head(max_rows).to_markdown(index=False))

        summary = "\n".join(buffer)

        # Cachear para reutilización
        cache_key = f"summary_{id(df)}"
        self.summaries_cache[cache_key] = summary

        return summary

    def track_sql_dependencies(self, query: str) -> List[str]:
        """
        Extrae nombres de tablas de una query SQL para crear grafos de dependencia.
        Útil para análisis de linaje de datos.
        """
        # Regex para detectar tablas en FROM, JOIN, INTO
        patterns = [
            r'FROM\s+([a-zA-Z0-9_.`\[\]]+)',
            r'JOIN\s+([a-zA-Z0-9_.`\[\]]+)',
            r'INTO\s+([a-zA-Z0-9_.`\[\]]+)',
            r'UPDATE\s+([a-zA-Z0-9_.`\[\]]+)'
        ]

        tables = set()
        for pattern in patterns:
            matches = re.findall(pattern, query, re.IGNORECASE)
            tables.update([m.strip('`[]') for m in matches])

        return sorted(list(tables))

    def analyze_notebook_structure(self, nb_path: str) -> Dict[str, Any]:
        """
        Lee un .ipynb y devuelve su estructura lógica.
        Identifica imports, dependencias y flujo de ejecución.
        """
        nb_path = Path(nb_path)

        if not nb_path.exists():
            return {"error": f"Notebook not found: {nb_path}"}

        try:
            with open(nb_path, 'r', encoding='utf-8') as f:
                nb_data = json.load(f)
        except Exception as e:
            return {"error": f"Failed to parse notebook: {e}"}

        cells = nb_data.get('cells', [])

        # Análisis de imports
        imports = set()
        code_cells = 0
        markdown_cells = 0

        for cell in cells:
            if cell.get('cell_type') == 'code':
                code_cells += 1
                source = ''.join(cell.get('source', []))

                # Detectar imports
                import_patterns = [
                    r'import\s+([a-zA-Z0-9_.]+)',
                    r'from\s+([a-zA-Z0-9_.]+)\s+import'
                ]
                for pattern in import_patterns:
                    matches = re.findall(pattern, source)
                    imports.update(matches)

            elif cell.get('cell_type') == 'markdown':
                markdown_cells += 1

        return {
            "total_cells": len(cells),
            "code_cells": code_cells,
            "markdown_cells": markdown_cells,
            "imports": sorted(list(imports)),
            "has_outputs": any(cell.get('outputs') for cell in cells if cell.get('cell_type') == 'code'),
            "notebook_format": nb_data.get('nbformat', 'unknown')
        }

    def estimate_token_usage(self, text: str) -> int:
        """
        Estimación aproximada de tokens (1 token ≈ 4 caracteres).
        """
        return len(text) // 4

    def optimize_dataframe_for_context(self, df: pd.DataFrame, max_tokens: int = 10000) -> str:
        """
        Crea la representación más compacta posible del DataFrame
        que quepa en el budget de tokens especificado.
        """
        # Estrategia adaptativa
        max_rows = 10
        summary = self.create_data_summary(df, max_rows)

        while self.estimate_token_usage(summary) > max_tokens and max_rows > 1:
            max_rows //= 2
            summary = self.create_data_summary(df, max_rows)

        return summary

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_task(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta tareas del Manager en modo aislado.
    """
    manager = DataAnalysisManager()
    task_type = params.get('task_type')

    if task_type == 'summarize':
        df = pd.read_csv(params['dataset_path'])
        summary = manager.create_data_summary(df, params.get('max_rows', 5))
        return {"summary": summary}

    elif task_type == 'analyze_notebook':
        result = manager.analyze_notebook_structure(params['notebook_path'])
        return result

    elif task_type == 'track_sql':
        tables = manager.track_sql_dependencies(params['query'])
        return {"tables": tables}

    else:
        return {"error": f"Unknown task type: {task_type}"}

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: data_analysis_skills.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_task(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {"agent": "data_analysis_manager", "version": "2.0"}
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {"error": str(e), "agent": "data_analysis_manager"}
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
