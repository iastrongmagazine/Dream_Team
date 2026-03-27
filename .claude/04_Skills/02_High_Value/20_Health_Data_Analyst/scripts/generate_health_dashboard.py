import pandas as pd
import matplotlib
matplotlib.use('Agg') # Usar backend no interactivo
import matplotlib.pyplot as plt
import seaborn as sns
import sys

def plot_health_trends(df, target_col):
    """
    Genera un gráfico limpio y directo y lo guarda como imagen.
    Aplica KISS: Menos es más.
    """
    if target_col not in df.columns:
        print(f"Error: La columna '{target_col}' no existe en el dataset.")
        return

    plt.figure(figsize=(10, 6))
    # Usando countplot para variables categóricas
    sns.countplot(data=df, x=target_col, palette='viridis')
    plt.title(f'Distribución de {target_col.title()} en la Población')
    plt.ylabel('Cantidad de Pacientes')
    plt.xlabel(None)
    plt.tight_layout()
    output_img = f"dashboard_{target_col}.png"
    plt.savefig(output_img)
    print(f"Gráfico guardado en: {output_img}")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        input_file = sys.argv[1]
        target_column = sys.argv[2]
        try:
            df = pd.read_csv(input_file)
            plot_health_trends(df, target_column)
        except Exception as e:
            print(f"Error generando dashboard: {e}")
    else:
        print("Uso: python generate_health_dashboard.py <archivo_datos.csv> <columna_objetivo>")
