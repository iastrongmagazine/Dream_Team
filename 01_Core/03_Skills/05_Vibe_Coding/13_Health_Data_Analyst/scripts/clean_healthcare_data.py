import pandas as pd
import sys

def clean_healthcare_data(df):
    """
    Función única para estandarizar datasets de salud.
    Aplica DRY: Limpieza centralizada y automática.
    """
    # 1. KISS: Formateo de fechas consistente
    # Busca columnas que contengan 'date' (case insensitive)
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # 2. DRY: Manejo de nulos según tipo de dato
    for col in df.columns:
        # Usar 'O' para object o verificar si es string
        if df[col].dtype == 'object' or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].fillna('Unknown').astype(str).str.strip().str.title()
        elif col not in date_cols:
            # Solo para numéricos que NO son fechas
            df[col] = df[col].fillna(0)

    return df

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        try:
            # Detectar csv o excel básico
            if input_file.endswith('.csv'):
                raw_data = pd.read_csv(input_file)
            elif input_file.endswith(('.xls', '.xlsx')):
                raw_data = pd.read_excel(input_file)
            else:
                print("Formato no soportado. Use CSV o Excel.")
                sys.exit(1)

            df = clean_healthcare_data(raw_data)
            output_file = "cleaned_" + input_file
            df.to_csv(output_file, index=False)
            print(f"Datos limpios guardados en: {output_file}")
        except Exception as e:
            print(f"Error procesando el archivo: {e}")
    else:
        print("Uso: python clean_healthcare_data.py <archivo_datos.csv>")
