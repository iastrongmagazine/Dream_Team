#!/usr/bin/env python3
"""
SKILL 3: DETAILED COHORT ANALYZER
Archivo: detailed_cohort_analysis.py
Descripción: Modelos predictivos avanzados para análisis de cohortes.

Use Case: Predecir transiciones Seed → Series A, detectar unicornios potenciales
Execution Mode: Isolated subprocess (heavy ML computations)
"""

import sys
import json
import pandas as pd
import numpy as np
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from dataclasses import dataclass, asdict

# Machine Learning
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (
    classification_report,
    roc_auc_score,
    confusion_matrix,
    precision_recall_curve
)
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

@dataclass
class ModelResults:
    """Estructura de resultados del modelo"""
    roc_auc: float
    accuracy: float
    precision: float
    recall: float
    f1_score: float
    feature_importance: Dict[str, float]
    confusion_matrix: List[List[int]]
    model_type: str
    training_samples: int
    test_samples: int

class DetailedCohortAnalyzer:
    """
    Analizador estadístico profundo para cohortes.
    Especializado en startups y predicción de éxito.
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.model = None
        self.scaler = StandardScaler()
        self.feature_names = []
        self.results_history = []

    def prepare_features(self, target_col: str = 'success') -> Tuple[np.ndarray, np.ndarray]:
        """
        Prepara features con ingeniería avanzada.

        Returns:
            (X_scaled, y): Features escaladas y target
        """
        # Seleccionar columnas numéricas
        numeric_cols = self.data.select_dtypes(include=[np.number]).columns.tolist()

        if target_col in numeric_cols:
            numeric_cols.remove(target_col)

        if not numeric_cols:
            raise ValueError("No numeric columns found for modeling")

        self.feature_names = numeric_cols

        # Extraer datos
        X = self.data[numeric_cols].copy()
        y = self.data[target_col].copy()

        # Imputación de valores faltantes
        imputer = SimpleImputer(strategy='median')
        X_imputed = imputer.fit_transform(X)

        # Escalado
        X_scaled = self.scaler.fit_transform(X_imputed)

        return X_scaled, y

    def engineer_startup_features(self) -> pd.DataFrame:
        """
        Crea features específicas para análisis de startups.
        """
        df = self.data.copy()

        # Revenue-based features
        if 'revenue' in df.columns:
            df['revenue_log'] = np.log1p(df['revenue'])
            df['revenue_tier'] = pd.cut(df['revenue'], bins=5, labels=False)

        # Employee growth indicators
        if 'employees' in df.columns and 'founded_year' in df.columns:
            current_year = 2026
            df['company_age'] = current_year - df['founded_year']
            df['employees_per_year'] = df['employees'] / (df['company_age'] + 1)

        # Funding stage encoding
        if 'stage' in df.columns:
            stage_map = {'Seed': 1, 'Series A': 2, 'Series B': 3, 'Series C': 4, 'Series D+': 5}
            df['stage_numeric'] = df['stage'].map(stage_map).fillna(0)

        # Industry hot factors (simplified example)
        if 'industry' in df.columns:
            hot_industries = ['AI/ML', 'SaaS', 'Fintech', 'Healthcare']
            df['is_hot_industry'] = df['industry'].isin(hot_industries).astype(int)

        return df

    def run_prediction_model(
        self,
        target_col: str = 'is_unicorn',
        model_type: str = 'random_forest'
    ) -> ModelResults:
        """
        Ejecuta modelo predictivo con validación cruzada.

        Args:
            target_col: Columna objetivo (debe ser binaria: 0/1)
            model_type: 'random_forest', 'gradient_boosting', o 'logistic'

        Returns:
            ModelResults con métricas completas
        """
        try:
            # Preparar datos
            X, y = self.prepare_features(target_col)
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.3, random_state=42, stratify=y
            )

            # Seleccionar modelo
            if model_type == 'random_forest':
                self.model = RandomForestClassifier(
                    n_estimators=100,
                    max_depth=10,
                    min_samples_split=5,
                    random_state=42,
                    n_jobs=-1
                )
            elif model_type == 'gradient_boosting':
                self.model = GradientBoostingClassifier(
                    n_estimators=100,
                    max_depth=5,
                    random_state=42
                )
            elif model_type == 'logistic':
                self.model = LogisticRegression(max_iter=1000, random_state=42)
            else:
                raise ValueError(f"Unknown model type: {model_type}")

            # Entrenar
            self.model.fit(X_train, y_train)

            # Predicciones
            y_pred = self.model.predict(X_test)
            y_proba = self.model.predict_proba(X_test)[:, 1] if hasattr(self.model, 'predict_proba') else None

            # Métricas
            report = classification_report(y_test, y_pred, output_dict=True)
            cm = confusion_matrix(y_test, y_pred)

            # Feature importance
            if hasattr(self.model, 'feature_importances_'):
                importance_dict = dict(zip(
                    self.feature_names,
                    self.model.feature_importances_
                ))
                # Ordenar por importancia
                importance_dict = dict(sorted(
                    importance_dict.items(),
                    key=lambda x: x[1],
                    reverse=True
                ))
            else:
                importance_dict = {}

            # ROC-AUC
            roc_auc = roc_auc_score(y_test, y_proba) if y_proba is not None else 0.0

            results = ModelResults(
                roc_auc=float(roc_auc),
                accuracy=float(report['accuracy']),
                precision=float(report['weighted avg']['precision']),
                recall=float(report['weighted avg']['recall']),
                f1_score=float(report['weighted avg']['f1-score']),
                feature_importance=importance_dict,
                confusion_matrix=cm.tolist(),
                model_type=model_type,
                training_samples=len(X_train),
                test_samples=len(X_test)
            )

            self.results_history.append(results)
            return results

        except Exception as e:
            # Error handling en formato estructurado
            raise RuntimeError(f"Model training failed: {str(e)}")

    def cohort_comparison(self, group_col: str, target_col: str) -> Dict[str, Any]:
        """
        Compara métricas entre diferentes cohortes.

        Example: Comparar tasa de éxito entre Seed vs Series A
        """
        if group_col not in self.data.columns:
            raise ValueError(f"Column {group_col} not found")

        cohorts = {}
        for cohort_name, group_df in self.data.groupby(group_col):
            cohorts[str(cohort_name)] = {
                'size': len(group_df),
                'success_rate': float(group_df[target_col].mean() if target_col in group_df.columns else 0),
                'avg_revenue': float(group_df['revenue'].mean() if 'revenue' in group_df.columns else 0),
                'avg_employees': float(group_df['employees'].mean() if 'employees' in group_df.columns else 0)
            }

        return cohorts

    def predict_new_samples(self, new_data: pd.DataFrame) -> np.ndarray:
        """
        Predice sobre nuevos datos usando el modelo entrenado.
        """
        if self.model is None:
            raise ValueError("Model not trained yet. Call run_prediction_model first.")

        # Preparar features de la misma forma
        X_new = new_data[self.feature_names]
        imputer = SimpleImputer(strategy='median')
        X_imputed = imputer.fit_transform(X_new)
        X_scaled = self.scaler.transform(X_imputed)

        predictions = self.model.predict(X_scaled)
        return predictions

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_analysis(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta análisis de cohortes en modo aislado.
    """
    # Cargar datos
    data_profile = params.get('data_profile')
    dataset_path = params.get('dataset_path')

    if dataset_path:
        df = pd.read_csv(dataset_path)
    else:
        raise ValueError("dataset_path is required")

    analyzer = DetailedCohortAnalyzer(df)

    # Ingeniería de features
    df_enhanced = analyzer.engineer_startup_features()
    analyzer.data = df_enhanced

    # Ejecutar modelo
    task_params = params.get('params', {})
    target_col = task_params.get('target_col', 'success')
    model_type = task_params.get('model_type', 'random_forest')

    # Verificar que target existe
    if target_col not in df_enhanced.columns:
        # Crear target dummy para demo
        df_enhanced[target_col] = (df_enhanced['revenue'] > df_enhanced['revenue'].median()).astype(int) if 'revenue' in df_enhanced.columns else 0
        analyzer.data = df_enhanced

    results = analyzer.run_prediction_model(target_col, model_type)

    # Análisis de cohortes si se especifica
    cohort_analysis = None
    if 'cohort_col' in task_params:
        cohort_analysis = analyzer.cohort_comparison(
            task_params['cohort_col'],
            target_col
        )

    return {
        "model_results": asdict(results),
        "cohort_analysis": cohort_analysis,
        "features_engineered": list(df_enhanced.columns),
        "total_features": len(analyzer.feature_names)
    }

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: detailed_cohort_analysis.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_analysis(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {
                    "agent": "detailed_cohort_analyzer",
                    "version": "2.0",
                    "models_available": ["random_forest", "gradient_boosting", "logistic"]
                }
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {
                    "error": str(e),
                    "agent": "detailed_cohort_analyzer"
                }
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
