#!/usr/bin/env python3
"""
Dashboard Simple para Visualizar Resultados del Procesamiento
Genera reporte HTML interactivo
"""

import pandas as pd
import json
from pathlib import Path
from datetime import datetime
from typing import Optional


def generate_html_dashboard(csv_file: str, output_file: str = "dashboard.html"):
    """
    Genera dashboard HTML interactivo de los resultados

    Args:
        csv_file: Archivo CSV con resultados
        output_file: Archivo HTML de salida
    """

    print(f"📊 Generando dashboard desde: {csv_file}")

    # Cargar datos
    df = pd.read_csv(csv_file)

    # Estadísticas
    total = len(df)
    success = len(df[df['status'] == 'success'])
    failed = len(df[df['status'] == 'error'])
    success_rate = (success / total * 100) if total > 0 else 0

    # Montos
    total_amount = df['total_amount'].sum() if 'total_amount' in df.columns else 0
    avg_amount = df['total_amount'].mean() if 'total_amount' in df.columns else 0

    # Tiempo promedio
    avg_time = df['processing_time'].mean() if 'processing_time' in df.columns else 0

    # Agrupar por mes si hay fechas
    monthly_data = None
    if 'invoice_date' in df.columns:
        # Intentar parsear fechas
        try:
            df['date_parsed'] = pd.to_datetime(df['invoice_date'], format='%d/%m/%Y', errors='coerce')
            df['month'] = df['date_parsed'].dt.to_period('M')
            monthly_data = df.groupby('month').agg({
                'total_amount': 'sum',
                'filename': 'count'
            }).reset_index()
            monthly_data.columns = ['Mes', 'Total', 'Cantidad']
        except:
            pass

    # Generar HTML
    html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - Procesamiento de Facturas</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        .header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}

        .header h1 {{
            color: #667eea;
            margin-bottom: 10px;
        }}

        .header p {{
            color: #666;
        }}

        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 20px;
        }}

        .stat-card {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-5px);
        }}

        .stat-card .label {{
            font-size: 14px;
            color: #666;
            margin-bottom: 10px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .stat-card .value {{
            font-size: 32px;
            font-weight: bold;
            color: #667eea;
        }}

        .stat-card .subvalue {{
            font-size: 14px;
            color: #999;
            margin-top: 5px;
        }}

        .success {{ color: #10b981 !important; }}
        .error {{ color: #ef4444 !important; }}
        .warning {{ color: #f59e0b !important; }}

        .table-container {{
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            overflow-x: auto;
        }}

        .table-container h2 {{
            margin-bottom: 20px;
            color: #667eea;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
        }}

        thead {{
            background: #f8f9fa;
        }}

        th {{
            padding: 12px;
            text-align: left;
            font-weight: 600;
            color: #666;
            border-bottom: 2px solid #e5e7eb;
        }}

        td {{
            padding: 12px;
            border-bottom: 1px solid #e5e7eb;
        }}

        tbody tr:hover {{
            background: #f8f9fa;
        }}

        .badge {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
        }}

        .badge-success {{
            background: #d1fae5;
            color: #065f46;
        }}

        .badge-error {{
            background: #fee2e2;
            color: #991b1b;
        }}

        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 10px;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #10b981 0%, #059669 100%);
            transition: width 0.3s;
        }}

        .footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            opacity: 0.8;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📊 Dashboard de Procesamiento de Facturas</h1>
            <p>Generado el {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}</p>
        </div>

        <div class="stats-grid">
            <div class="stat-card">
                <div class="label">Total Facturas</div>
                <div class="value">{total}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: 100%"></div>
                </div>
            </div>

            <div class="stat-card">
                <div class="label">Tasa de Éxito</div>
                <div class="value success">{success_rate:.1f}%</div>
                <div class="subvalue">{success} exitosas, {failed} fallidas</div>
            </div>

            <div class="stat-card">
                <div class="label">Monto Total</div>
                <div class="value">${total_amount:,.2f}</div>
                <div class="subvalue">Promedio: ${avg_amount:,.2f}</div>
            </div>

            <div class="stat-card">
                <div class="label">Tiempo Promedio</div>
                <div class="value warning">{avg_time:.2f}s</div>
                <div class="subvalue">Por factura</div>
            </div>
        </div>
"""

    # Tabla de facturas por mes si existe
    if monthly_data is not None and len(monthly_data) > 0:
        html += """
        <div class="table-container" style="margin-bottom: 20px;">
            <h2>📅 Facturas por Mes</h2>
            <table>
                <thead>
                    <tr>
                        <th>Mes</th>
                        <th>Cantidad</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody>
"""
        for _, row in monthly_data.iterrows():
            html += f"""
                    <tr>
                        <td>{row['Mes']}</td>
                        <td>{row['Cantidad']}</td>
                        <td>${row['Total']:,.2f}</td>
                    </tr>
"""
        html += """
                </tbody>
            </table>
        </div>
"""

    # Tabla de todas las facturas
    html += """
        <div class="table-container">
            <h2>📋 Detalle de Facturas</h2>
            <table>
                <thead>
                    <tr>
                        <th>Archivo</th>
                        <th>Número</th>
                        <th>Fecha</th>
                        <th>Total</th>
                        <th>Estado</th>
                        <th>Tiempo</th>
                    </tr>
                </thead>
                <tbody>
"""

    for _, row in df.iterrows():
        status_class = 'badge-success' if row.get('status') == 'success' else 'badge-error'
        status_text = '✅ Exitosa' if row.get('status') == 'success' else '❌ Error'

        invoice_num = row.get('invoice_number', 'N/A')
        invoice_date = row.get('invoice_date', 'N/A')
        total = f"${row['total_amount']:,.2f}" if pd.notna(row.get('total_amount')) else 'N/A'
        proc_time = f"{row['processing_time']:.2f}s" if pd.notna(row.get('processing_time')) else 'N/A'

        html += f"""
                    <tr>
                        <td>{row.get('filename', 'N/A')}</td>
                        <td>{invoice_num}</td>
                        <td>{invoice_date}</td>
                        <td>{total}</td>
                        <td><span class="badge {status_class}">{status_text}</span></td>
                        <td>{proc_time}</td>
                    </tr>
"""

    html += """
                </tbody>
            </table>
        </div>

        <div class="footer">
            <p>Sistema de Procesamiento Paralelo de Facturas con OCR</p>
            <p>Desarrollado con Python + Tesseract OCR</p>
        </div>
    </div>
</body>
</html>
"""

    # Guardar HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"✅ Dashboard generado: {output_file}")
    print(f"📂 Abre en tu navegador para ver los resultados")

    return output_file


def find_latest_results(results_dir: str = "./processed_invoices") -> Optional[str]:
    """Encuentra el CSV más reciente en el directorio de resultados"""

    results_path = Path(results_dir)

    if not results_path.exists():
        print(f"❌ Directorio no encontrado: {results_dir}")
        return None

    # Buscar CSVs
    csv_files = list(results_path.glob("invoices_*.csv"))

    if not csv_files:
        print(f"❌ No se encontraron archivos CSV en {results_dir}")
        return None

    # Ordenar por fecha de modificación
    latest_csv = max(csv_files, key=lambda p: p.stat().st_mtime)

    return str(latest_csv)


def main():
    """Función principal"""
    import sys

    if len(sys.argv) > 1:
        csv_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "dashboard.html"
    else:
        # Buscar último CSV
        csv_file = find_latest_results()
        if not csv_file:
            print("\n❌ No se encontraron resultados")
            print("Uso:")
            print("  python dashboard.py <archivo.csv> [output.html]")
            print("\nO procesa facturas primero:")
            print("  python invoice_processor.py ./facturas")
            return

        output_file = "dashboard.html"
        print(f"📊 Usando CSV más reciente: {Path(csv_file).name}\n")

    # Generar dashboard
    html_file = generate_html_dashboard(csv_file, output_file)

    # Intentar abrir en navegador
    try:
        import webbrowser
        webbrowser.open(f'file://{Path(html_file).absolute()}')
        print("🌐 Dashboard abierto en navegador")
    except:
        print(f"💡 Abre manualmente: {Path(html_file).absolute()}")


if __name__ == "__main__":
    main()
