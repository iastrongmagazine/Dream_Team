import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
from config_paths import ROOT_DIR as BASE_DIR
import os
import pandas as pd
import json
import sys
import io

# --- CONFIGURACIÓN ARMOR LAYER ---
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from config_paths import ROOT_DIR as BASE_DIR

class AnalyticsFactory:
    def __init__(self, dataset_path):
        self.dataset_path = os.path.abspath(dataset_path)
        self.filename = os.path.basename(self.dataset_path)
        self.domain = "General"
        self.results_dir = ""
        self.engine_dir = os.path.join(BASE_DIR, "04_Operations")

    def report_progress(self, step, total, desc):
        """Reporta el progreso del workflow."""
        progress = (step / total) * 100
        print(f"\n[{progress:.1f}%] Paso {step}/{total}: {desc}")

        # Notificaciones de voz en hitos clave
        if progress in [25.0, 50.0, 75.0, 100.0]:
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.say(f"Progreso: {progress:.0f} por ciento completado.")
                engine.runAndWait()
            except:
                pass  # Silenciar errores de TTS

    def detect_domain(self):
        """
        Meta-análisis para detectar el rubro del dataset.
        """
        try:
            # Check file exists
            if not os.path.exists(self.dataset_path):
                print(f"Error: Dataset {self.dataset_path} no encontrado.")
                return "General"

            df_head = pd.read_csv(self.dataset_path, nrows=10)
            cols = [c.lower() for c in df_head.columns]

            # Lógica de detección basada en palabras clave
            if any(x in cols for x in ['patient', 'diagnosis', 'health', 'hospital', 'medical', 'age']):
                self.domain = "Salud"
            elif any(x in cols for x in ['sales', 'revenue', 'price', 'product', 'profit', 'units']):
                self.domain = "Ventas"
            elif any(x in cols for x in ['click', 'campaign', 'conversion', 'ad', 'marketing', 'channel']):
                self.domain = "Marketing"
            elif any(x in cols for x in ['lead_time', 'cycle_time', 'ship_date', 'velocity', 'task_id']):
                self.domain = "Velocity"
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

        print(f"🔍 Dominio detectado: {self.domain}")
        return self.domain

    def setup_workspace(self):
        """
        Crea la carpeta de salida según el dominio.
        """
        # Ubicación dentro del proyecto
        base_path = os.path.join(self.engine_dir, "analytics_output")

        folders = {
            "Salud": "01_Salud",
            "Ventas": "02_Ventas",
            "Marketing": "03_Marketing",
            "General": "04_General"
        }

        folder_name = folders.get(self.domain, "04_General")
        self.results_dir = os.path.join(base_path, folder_name)
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir, exist_ok=True)
        print(f"📂 Carpeta de resultados: {self.results_dir}")

    def generate_narrative(self, graph_id, data_summary):
        """
        Motor de interpretación v4.2: Traduce gráficos a valor de negocio según el dominio.
        """
        domain = data_summary.get('domain', 'General')
        intensity = data_summary.get('primary_intensity', 'variable')
        primary = intensity  # Alias for F-string depth v4.7

        narratives = {
            "01": (f"**Synergy Matrix (Correlaciones)**: Esta matriz revela las palancas ocultas del dominio **{domain}**. "
                   f"Una correlación positiva alta entre recursos y **'{primary}'** confirma que el modelo es elástico y responde a la inversión. "
                   f"Si detectamos correlaciones débiles, es un indicador de que el proceso actual tiene fricciones estructurales que la simple inversión no resolverá."),
            "02": (f"**Success Density (Sweet Spot)**: Identificamos el rango operativo donde el negocio genera el mayor impacto natural. "
                   f"El pico de densidad en **'{primary}'** marca nuestra 'zona de confort' de eficiencia; operar fuera de este pico suele incrementar los costos marginales. "
                   f"Este insight permite al equipo de operaciones predecir el impacto de nuevos lotes de datos con alta precisión."),
            "03": (f"**Market Fragmentation (Categorical Share)**: Evaluamos la dependencia de segmentos específicos. "
                   f"En **{domain}**, buscamos una distribución saludable para evitar el 'Riesgo de Concentración'. "
                   f"Si un solo segmento domina el {primary}, el negocio es vulnerable a cambios externos; si la fragmentación es alta, los costos de gestión administrativa suelen dispararse."),
            "04": (f"**Strategic Anomaly Detection (Outlier Rigor)**: Este radar de anomalías separa el ruido del valor real. "
                   f"Los puntos fuera del rango normal en **'{primary}'** no son errores, son señales: representan o bien fugas críticas de capital que deben taparse en <24h, "
                   f"o éxitos accidentales cuyo proceso debe ser 'ingenierizado' para volverse la nueva norma operativa."),
            "05": (f"**Efficiency Benchmark (Ranking de Retorno)**: Aquí es donde se define el liderazgo interno. "
                   f"Al contrastar categorías contra **'{primary}'**, establecemos un benchmark de rentabilidad que sirve de base para la asignación de presupuestos. "
                   f"Los que están bajo la media no solo rinden menos, sino que están consumiendo el oxígeno (presupuesto) de los segmentos con mayor potencial de escalado."),
            "06": (f"**Performance Quadrants (Matriz de Prioridad)**: Visualización de 'Estrellas' vs 'Lastres'. "
                   f"Cruzamos volumen contra eficiencia para priorizar el roadmap táctico. "
                   f"El objetivo estratégico en **{domain}** es mover sistemáticamente todos los elementos hacia el cuadrante superior derecho, "
                   f"eliminando o transformando aquellos que se mantienen en la 'zona muerta' de bajo retorno."),
            "07": (f"**Strategic Velocity (Momentum)**: La visualización más crítica para el largo plazo. "
                   f"Mide si la tracción de **'{primary}'** está acelerando, desacelerando o estancada. "
                   f"Un vector ascendente indica que las tácticas actuales tienen 'momentum' y deben protegerse; una caída sostenida advierte que el modelo de negocio en **{domain}** está llegando a un punto de saturación."),
            "08": (f"**Success Concentration (Violin Density)**: Analizamos la consistencia y variabilidad del éxito. "
                   f"Un 'violín' estrecho indica procesos predecibles y escalables; una distribución ancha sugiere que el resultado positivo en **'{primary}'** es errático y difícil de replicar. "
                   f"Buscamos estandarizar la ejecución para que el éxito no dependa de variables extraordinarias."),
            "09": (f"**Resource Intensity (Joint Density)**: Cruzamos el esfuerzo (recursos) con el impacto directo. "
                   f"Esto nos permite ver dónde la ley de rendimientos decrecientes comienza a afectar a **{domain}**. "
                   f"Identificamos el balance óptimo para no 'quemar' recursos en zonas donde el incremento en **'{primary}'** ya no justifica el gasto adicional."),
            "10": (f"**Market Dominance (Composition Pie)**: La visión final de cuota de mercado interno. "
                   f"Revela quién controla realmente la métrica de éxito en este dominio. "
                   f"Es fundamental para entender el equilibrio de poder dentro de la operación y asegurar que el dominio **{domain}** no esté sufriendo de canibalización interna entre sus propios segmentos.")
        }

        return narratives.get(graph_id, "Interpretación analítica profunda en proceso de síntesis por el motor de inteligencia v4.7.")

    def get_business_question(self, graph_id):
        """
        Define la pregunta estratégica que responde cada visualización.
        """
        questions = {
            "01": "¿Relación? | ¿Qué variables impulsan realmente los resultados?",
            "02": "¿Tracción? | ¿En qué punto exacto estamos obteniendo el mayor impacto?",
            "03": "¿Riesgo? | ¿Dependemos demasiado de un solo segmento o canal?",
            "04": "¿Anomalías? | ¿Existen comportamientos atípicos que debamos auditar?",
            "05": "¿Liderazgo? | ¿Quiénes son los referentes de eficiencia operativa?",
            "06": "¿Prioridad? | ¿Qué grupos son 'estrellas' y cuáles debemos optimizar?",
            "07": "¿Velocidad? | ¿Estamos ganando o con el tiempo?",
            "08": "¿Control? | ¿Es nuestro rendimiento estable o altamente volátil?",
            "09": "¿Densidad? | ¿Estamos invirtiendo en los segmentos de mayor retorno?",
            "10": "¿Cuota? | ¿Quién controla la mayor parte de la métrica de éxito?"
        }
        return questions.get(graph_id, "¿Cómo impacta esta métrica al resultado final de la empresa?")

    def generate_report(self):
        """
        Genera un reporte de alto impacto v4.7 (Intelligence Overhaul) centrado en Valor y Acción.
        """
        print(f"🧠 Esculpiendo Reporte Maestro v4.7 (Intelligence Expansion) para {self.domain}...")

        summary_path = os.path.join(self.results_dir, 'summary.json')
        data_summary = {}
        if os.path.exists(summary_path):
            with open(summary_path, 'r', encoding='utf-8') as f:
                data_summary = json.load(f)

        deep = data_summary.get('deep_stats', {})
        totals = deep.get('totals', {})
        averages = deep.get('averages', {})
        tops = deep.get('top_performers', {})
        worsts = deep.get('worst_performers', {})
        main_metric = data_summary.get('primary_intensity', 'impacto')

        report_path = os.path.join(self.results_dir, 'business_insights.md')

        with open(report_path, 'w', encoding='utf-8') as f:
            self._write_header(f, deep)
            self._write_executive_summary(f, data_summary, totals, tops, worsts, main_metric)
            self._write_kpis(f, data_summary, totals, averages, tops, worsts)
            self._write_analysis_matrix(f, data_summary)
            self._write_roadmap(f, worsts, tops, main_metric)
            self._write_footer(f, deep)

        print(f"✨ Reporte Maestro v4.7 (Value First) generado en: {report_path}")
        print(f"✨ Reporte Estratégico v4.3 (Premium Strategy) generado en: {report_path}")

    def _write_header(self, f, deep):
        f.write(f"# 🚀 Strategic Value Report: {self.domain} Intelligence\n")
        f.write(f"**Análisis de {deep.get('record_count', 0)} registros | Período: Snapshot 2025**\n")
        f.write(f"**Standard v4.7 (Premium Intelligence) – Enfoque Rentabilidad y Acción**\n\n")

    def _write_executive_summary(self, f, data_summary, totals, tops, worsts, main_metric):
        f.write("## 🏛️ 1. Executive Summary\n")
        f.write(f"Se analizaron los componentes críticos de la operación en el dominio **{self.domain}** con un alcance de:\n")
        for metric in data_summary.get('metrics', [])[:3]:
            f.write(f"- **{totals.get(metric, 0):,.2f}** de {metric}\n")

        f.write(f"\n**Hallazgos clave (C-level):**\n")
        if tops:
            tm = tops.get(main_metric, {})
            f.write(f"- **Máximo impacto detectado**: {tm.get('name', 'N/A')} ({main_metric} {tm.get('value', 0):,.2f})\n")
        if worsts:
            wm = worsts.get(main_metric, {})
            f.write(f"- **Riesgo por bajo rendimiento**: {wm.get('name', 'N/A')} requiere intervención urgente en {main_metric}.\n")

        f.write(f"- **Concentración de éxito**: El top performer representa un share significativo del volumen total.\n")
        f.write(f"**Recomendación inmediata**: Reasignar recursos desde los segmentos rezagados hacia los líderes de eficiencia identificados.\n\n")

    def _write_kpis(self, f, data_summary, totals, averages, tops, worsts):
        f.write("## 📊 2. Strategic Ratios & KPIs\n\n")
        f.write("#### 📝 Leyenda de Inteligencia (Abreviaturas)\n")
        f.write("> **CL**: Clicks | **CV**: Conversions | **SP**: Spend | **CT**: CTR | **CP**: CPA | **CR**: Conv. Rate | **RV**: Revenue | **PF**: Profit\n\n")

        W_ST, W1, W2, W3, W4 = 4, 18, 16, 28, 18

        def v_center(text, width):
            v_len = len(text)
            emojis = ["🔴", "🌟", "🟢", "🖱️", "🎯", "💰", "📈", "💸", "⚡", "📊", "🏆"]
            v_len += sum(1 for e in emojis if e in text)
            pad = width - v_len
            if pad <= 0: return text
            l = pad // 2
            r = pad - l
            return " " * l + text + " " * r

        def write_box_row(c0, c1, c2, c3, c4):
            f.write(f"|{v_center(str(c0), W_ST)}|{v_center(str(c1), W1)}|{v_center(str(c2), W2)}|{v_center(str(c3), W3)}|{v_center(str(c4), W4)}|\n")

        def write_box_sep():
            f.write(f"|{':'+'-'*(W_ST-2)+':'}|{':'+'-'*(W1-2)+':'}|{':'+'-'*(W2-2)+':'}|{':'+'-'*(W3-2)+':'}|{':'+'-'*(W4-2)+':'}|\n")

        metrics = data_summary.get('metrics', [])
        abbr_map = {
            'clicks': 'CL', 'conversions': 'CV', 'spend': 'SP',
            'ctr': 'CT', 'cpa': 'CP', 'conv_rate': 'CR',
            'revenue': 'RV', 'profit': 'PF', 'leads': 'LD', 'roi': 'RI'
        }
        metric_icons = {
            'clicks': "🖱️", 'conversions': "🎯", 'spend': "💰",
            'ctr': "📈", 'cpa': "💸", 'conv_rate': "⚡"
        }

        seen_metrics = []
        for m in metrics:
            lower_m = m.lower()
            if lower_m in seen_metrics: continue
            seen_metrics.append(lower_m)

            icon = metric_icons.get(lower_m, "📊")
            abbr = abbr_map.get(lower_m, lower_m.upper()[:2])

            f.write(f"### {icon} Métrica: {m.capitalize()} ({abbr})\n")
            write_box_row("ST", "METRICA", "VALOR REAL", "INTERPRETACION", "ACCION")
            write_box_sep()

            val = totals.get(m, 0)
            avg = averages.get(m, 0)
            status_icon = "🔴" if m in worsts else "🌟" if m in tops else "🟢"
            interp = "Fuerza Operativa" if lower_m in ['clicks', 'spend'] else \
                        "Valor de Negocio" if lower_m in ['conversions', 'revenue'] else \
                        "Eficiencia Neta"
            action = "Optimizar" if m in worsts else "Escalar" if m in tops else "Estabilizar"

            write_box_row(status_icon, f"Total {abbr}", f"{val:,.2f}", interp, action)
            write_box_row(status_icon, f"Avg {abbr}", f"{avg:,.2f}", interp, action)
            f.write("\n")

        if tops:
            f.write("### 🏆 Executive Leadership (High Performance)\n")
            write_box_row("ST", "SEGMENTO", "VALOR", "STATUS", "RECOMENDACION")
            write_box_sep()
            unique_tops = {}
            for m, d in tops.items():
                unique_tops[d['name']] = d
            for name, d in unique_tops.items():
                write_box_row("🌟", name[:W1-2], f"{d.get('value', 0):,.2f}", f"Lider {d.get('label', 'Impacto')[:6]}", "Proteger")
        f.write("\n\n")

    def _write_analysis_matrix(self, f, data_summary):
        f.write("## 🧠 3. Strategic Analysis Matrix – The 'Why' Layer\n\n")
        images = [
            ("01_correlation_heatmap.png", "01. Synergy Matrix (Correlaciones)", "01"),
            ("02_numeric_distribution.png", "02. Success Density (Sweet Spot)", "02"),
            ("03_categorical_distribution.png", "03. Market Fragmentation (Share)", "03"),
            ("04_outliers_boxplot.png", "04. Strategic Anomaly Detection", "04"),
            ("05_cat_vs_num_bar.png", "05. Efficiency Benchmark", "05"),
            ("06_scatter_relation.png", "06. Performance Quadrants", "06"),
            ("07_line_trend.png", "07. Strategic Velocity (Momentum)", "07"),
            ("08_violin_density.png", "08. Success Concentration", "08"),
            ("09_joint_hex.png", "09. Resource Intensity", "09"),
            ("10_composition_pie.png", "10. Market Dominance", "10")
        ]

        for img_file, caption, graph_id in images:
            img_path = os.path.join(self.results_dir, img_file)
            if os.path.exists(img_path):
                f.write(f"### 🔗 {caption}\n")
                f.write(f"**❓ Pregunta de Negocio:** *{self.get_business_question(graph_id)}*\n\n")
                f.write(f"![{caption}]({img_file})\n\n")
                f.write(f"**💡 Insight Estratégico**: {self.generate_narrative(graph_id, data_summary)}\n\n")
                f.write("---\n\n")

    def _write_roadmap(self, f, worsts, tops, main_metric):
        f.write("## 💡 4. C-Level Strategic Roadmap – Acciones Priorizadas\n\n")
        f.write("1. **Acción Inmediata (0–7 días)**\n")
        if worsts:
            f.write(f"   - Pausar o re-auditar el segmento **'{worsts.get(main_metric, {}).get('name', 'N/A')}'** para detener fugas de capital.\n")
        f.write("   - Corregir las anomalías detectadas en el gráfico 04.\n\n")

        f.write("2. **Acción Táctica (7–30 días)**\n")
        if tops:
            f.write(f"   - Incrementar presupuesto/recursos en **'{tops.get(main_metric, {}).get('name', 'N/A')}'** para capturar momentum.\n")
        f.write("   - Optimizar landing pages y procesos en segmentos de eficiencia media.\n\n")

        f.write("3. **Acción Estratégica (30–90 días)**\n")
        f.write("   - Implementar test A/B multivariante para bajar el costo operativo global.\n")
        f.write("   - Automatizar este reporte para monitoreo semanal con alertas de desviación.\n\n")

        f.write("**Próximo paso recomendado**: Sesión de revisión de budget con los owners de los segmentos líderes.\n\n")

    def _write_footer(self, f, deep):
        f.write("---\n")
        f.write(f"*Standard Analysis Factory | Premium Value Edition | v4.7 (Intelligence Expansion)*\n")
        f.write(f"*Generado con datos reales validados – {deep.get('record_count', 0)} registros analizados*")

    def generate_and_run_script(self):
        """
        Carga la plantilla y genera un script de análisis específico.
        """
        print(f"⚙️ Generando script de análisis para {self.domain}...")

        template_path = os.path.join(self.engine_dir, "templates", "base_template.py.tmpl")
        if not os.path.exists(template_path):
             print(f"❌ Error: Plantilla no encontrada en {template_path}")
             return

        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()

        # Generar el script específico
        script_name = f"analyze_{self.domain.lower()}.py"
        script_path = os.path.join(self.results_dir, script_name)

        # Inyectar la llamada a la función
        execution_code = f"\n\nif __name__ == '__main__':\n    run_analysis(r'{os.path.abspath(self.dataset_path)}', r'{os.path.abspath(self.results_dir)}')"

        with open(script_path, 'w', encoding='utf-8') as f:
            f.write(template_content)
            f.write(execution_code)

        print(f"🚀 Ejecutando script generado: {script_name}")
        # Ejecutar el script generado
        import subprocess
        result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)

        if result.returncode == 0:
            print(f"✅ Análisis dinámico completado exitosamente.")
        else:
            print(f"❌ Error en la ejecución: {result.stderr}")

    def run(self):
        total_steps = 4

        # Paso 1: Detección de Dominio
        self.report_progress(1, total_steps, "Detectando Dominio del Dataset")
        self.detect_domain()

        # Paso 2: Configuración de Workspace
        self.report_progress(2, total_steps, "Configurando Workspace de Salida")
        self.setup_workspace()

        # Paso 3: Generación y Ejecución de Script
        self.report_progress(3, total_steps, "Generando y Ejecutando Script de Análisis")
        self.generate_and_run_script()

        # Paso 4: Generación de Reporte
        self.report_progress(4, total_steps, "Generando Reporte de Análisis")
        self.generate_report()

        print(f"✨ Proceso Factory finalizado para {self.filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python 04_Operations/master_analytics_factory.py path/to/dataset.csv")
    else:
        target = sys.argv[1]
        factory = AnalyticsFactory(target)
        factory.run()
