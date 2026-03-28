import pandas as pd
import sys

def get_population_insights(df):
    """
    Calcula KPIs clave de salud poblacional.
    Aplica KISS: Métricas simples y directas.
    """
    # Verificación defensiva básica de columnas esperadas
    required_cols = ['age', 'region', 'priority']
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        return {"Error": f"Faltan columnas requeridas: {missing}"}

    insights = {
        "total_pacientes": len(df),
        "promedio_edad": df['age'].mean(),
        "casos_por_region": df['region'].value_counts().to_dict(),
        # Asumiendo que 'priority' tiene valores como 'High', 'Low', etc.
        "tasa_prioridad_alta": (df['priority'] == 'High').mean() * 100
    }
    return insights

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        try:
            df = pd.read_csv(input_file)
            stats = get_population_insights(df)
            print("--- Insights Poblacionales ---")
            for key, value in stats.items():
                print(f"{key}: {value}")
        except Exception as e:
            print(f"Error analizando datos: {e}")
    else:
        print("Uso: python calc_population_metrics.py <archivo_datos.csv>")
