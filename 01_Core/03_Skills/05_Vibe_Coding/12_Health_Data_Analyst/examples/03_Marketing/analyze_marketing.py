import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


def run_analysis(csv_path, output_dir):
    """
    Standard Analytics Engine v3.0 (Smart Insights)
    - Re-ingeniería de selección de variables.
    - Generación de Data Peek (Markdown).
    - Power Dash Print-Ready (300 DPI).
    """
    df = pd.read_csv(csv_path)

    # 1. Limpieza y Normalización (Pure Data Layer)
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].fillna("Unknown").str.strip()
        else:
            df[col] = df[col].fillna(0)

    # 2. Heurística de Datos: Identificar Métricas vs Identificadores
    all_num = df.select_dtypes(include=["number"]).columns.tolist()
    id_terms = ["id", "key", "pk", "fk", "index", "uid", "codigo"]
    metric_cols = [
        c for c in all_num if not any(term in c.lower() for term in id_terms)
    ]
    id_cols = [c for c in all_num if c not in metric_cols]
    cat_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    # --- Standard v4.0: Ingeniería de Ratios (Value First) ---
    ratios = {}
    cols_lower = [c.lower() for c in df.columns]

    # 2.1 Detección de Ratios Críticos
    if "clicks" in cols_lower and "impressions" in cols_lower:
        df["CTR"] = (df["clicks"] / df["impressions"]).fillna(0)
        metric_cols.append("CTR")
        ratios["CTR"] = "Efficiency (Clicks/Impressions)"

    if "conversions" in cols_lower and "clicks" in cols_lower:
        df["Conv_Rate"] = (df["conversions"] / df["clicks"]).fillna(0)
        metric_cols.append("Conv_Rate")
        ratios["Conv_Rate"] = "Intent (Conversions/Clicks)"

    if "spend" in cols_lower and "conversions" in cols_lower:
        df["CPA"] = (
            (df["spend"] / df["conversions"])
            .replace([float("inf"), -float("inf")], 0)
            .fillna(0)
        )
        metric_cols.append("CPA")
        ratios["CPA"] = "Efficiency (Spend/Conversions)"

    # 3. Generar Data Peek (Vista previa para verificación humana/AI)
    peek_path = os.path.join(output_dir, "data_preview.md")
    try:
        with open(peek_path, "w", encoding="utf-8") as f:
            f.write("# 📋 Data Peek: Cleaned Dataset Preview\n\n")
            f.write(
                f"**Registros Totales:** {len(df)} | **Columnas:** {len(df.columns)}\n\n"
            )
            f.write("## 🔍 Muestra de Datos (Fact-Checking)\n\n")
            try:
                f.write(df.head(10).to_markdown(index=False))
            except:
                f.write("```\n" + str(df.head(10)) + "\n```")
            f.write("\n\n## 🧠 Clasificación Heurística v4.0\n")
            f.write(
                f"- **Métricas de Negocio:** {', '.join(metric_cols) if metric_cols else 'Ninguna'}\n"
            )
            f.write(
                f"- **Ratios Calculados:** {', '.join(ratios.keys()) if ratios else 'Ninguno'}\n"
            )
            f.write(
                f"- **Segmentos Categóricos:** {', '.join(cat_cols) if cat_cols else 'Ninguno'}\n"
            )
            f.write(
                f"- **IDs Técnicos (Excluidos):** {', '.join(id_cols) if id_cols else 'Ninguno'}\n"
            )
    except Exception as e:
        print(f"⚠️ Error al generar Data Peek: {e}")

    # 4. Insights Dinámicos
    import json

    summary = {
        "status": "Smart Analysis v4.0",
        "ratios": ratios,
        "metrics": metric_cols,
        "categories": cat_cols,
        "numeric_stats": df[metric_cols].describe().to_dict() if metric_cols else {},
    }
    with open(os.path.join(output_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=4)

    # 5. Motor de Visualización (Power Dash v4.0 - Value First)
    generate_dashboards(df, output_dir, metric_cols, cat_cols)
    return df


def generate_dashboards(df, output_dir, num_cols, cat_cols):
    """
    Motor v4.0: Cada gráfico responde a una pregunta de negocio.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    import os

    plt.rcParams.update({"font.size": 10, "axes.titlesize": 12, "axes.labelsize": 10})
    sns.set_theme(style="whitegrid", palette="muted")
    errors = []

    def save_plot(filename, title):
        try:
            plt.title(title, pad=20, fontweight="bold")
            plt.tight_layout()
            plt.savefig(
                os.path.join(output_dir, filename), dpi=300, bbox_inches="tight"
            )
            plt.close()
        except Exception as e:
            errors.append(f"Error en {filename}: {str(e)}")
            plt.close()

    if not num_cols:
        return

    # 1. Synergy Matrix
    try:
        if len(num_cols) > 1:
            plt.figure(figsize=(10, 8))
            sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
            save_plot(
                "01_correlation_heatmap.png", "01. Inter-variable Synergy Analysis"
            )
    except Exception as e:
        errors.append(f"01: {str(e)}")

    # 2. Probability Density (Advanced Refinement v4.1.1)
    try:
        plt.figure(figsize=(10, 6))
        main_metric = "conversions" if "conversions" in df.columns else num_cols[0]
        # clip=(0, None) asegura que no mostremos valores negativos imposibles
        sns.kdeplot(
            data=df,
            x=main_metric,
            fill=True,
            color="#4A90E2",
            clip=(0, None),
            bw_adjust=1.0,
        )
        # Añadir Rug Plot para mostrar los puntos reales (transparencia de datos)
        sns.rugplot(data=df, x=main_metric, color="#D0021B", alpha=0.5)
        plt.xlim(left=0)  # Refuerzo de límite X
        save_plot(
            "02_numeric_distribution.png",
            f"02. Success Density: {main_metric} Intensity",
        )
    except Exception as e:
        errors.append(f"02: {str(e)}")

    # 3. Market Fragmentation (Share Analysis v4.1.2)
    try:
        if cat_cols and num_cols:
            plt.figure(figsize=(10, 6))
            cat = cat_cols[0]
            # Priorizar clicks o conversions para el share de mercado
            intensity_metric = (
                "clicks"
                if "clicks" in df.columns
                else (num_cols[0] if num_cols else None)
            )

            if intensity_metric:
                plot_data = (
                    df.groupby(cat)[intensity_metric]
                    .sum()
                    .sort_values(ascending=False)
                    .reset_index()
                )
                total = plot_data[intensity_metric].sum()
                plot_data["share"] = (plot_data[intensity_metric] / total) * 100

                bars = plt.bar(
                    plot_data[cat],
                    plot_data["share"],
                    color=plt.cm.plasma(np.linspace(0, 0.8, len(plot_data))),
                )

                for bar in bars:
                    height = bar.get_height()
                    plt.text(
                        bar.get_x() + bar.get_width() / 2.0,
                        height + 0.5,
                        f"{height:.1f}%",
                        ha="center",
                        va="bottom",
                        fontweight="bold",
                    )

                plt.ylabel(f"Share of {intensity_metric} (%)")
                plt.title(
                    f"03. Market Fragmentation: {cat} Share by {intensity_metric}"
                )
            else:
                sns.countplot(data=df, x=cat, palette="viridis")

            plt.xticks(rotation=45)
            save_plot(
                "03_categorical_distribution.png", f"03. Market Fragmentation by {cat}"
            )
    except Exception as e:
        errors.append(f"03: {str(e)}")

    # 4. Strategic Anomaly Detection (Visual Boxplot v4.1.6)
    try:
        # Seleccionar solo numéricas con escalas comparables para evitar aplanamiento excesivo
        # O simplemente graficar todo como pide la referencia visual
        plt.figure(figsize=(12, 6))
        cols_to_plot = [
            c for c in num_cols if df[c].max() > 0.1
        ]  # Filtro básico para evitar ruido near-zero

        if cols_to_plot:
            sns.boxplot(
                data=df[cols_to_plot],
                palette="Set3",
                showmeans=True,
                meanprops={
                    "marker": "o",
                    "markerfacecolor": "white",
                    "markeredgecolor": "black",
                    "markersize": "8",
                },
            )
            # Añadir puntos individuales (stripplot) para total transparencia en datasets pequeños
            sns.stripplot(
                data=df[cols_to_plot], color=".3", size=4, jitter=True, alpha=0.5
            )

            plt.title("04. Strategic Anomaly Detection (Boxplot Analysis)")
            plt.ylabel("Value Range")
            plt.xticks(rotation=45)
            save_plot("04_outliers_boxplot.png", "04. Strategic Anomaly Detection")
    except Exception as e:
        errors.append(f"04: {str(e)}")

    # 5. Efficiency Benchmark (Precision Fix)
    try:
        if cat_cols and num_cols:
            plt.figure(figsize=(10, 6))
            target = "CPA" if "CPA" in df.columns else num_cols[0]
            # Agrupar para asegurar que mostramos el valor exacto por categoría
            plot_data = (
                df.groupby(cat_cols[0])[target]
                .mean()
                .sort_values(ascending=False)
                .reset_index()
            )

            bars = plt.bar(
                plot_data[cat_cols[0]],
                plot_data[target],
                color=plt.cm.viridis(np.linspace(0, 1, len(plot_data))),
            )

            # Añadir etiquetas de valor exactas sobre las barras
            for bar in bars:
                height = bar.get_height()
                plt.text(
                    bar.get_x() + bar.get_width() / 2.0,
                    height + (height * 0.01),
                    f"{height:.2f}",
                    ha="center",
                    va="bottom",
                    fontweight="bold",
                    fontsize=9,
                )

            plt.xticks(rotation=45)
            plt.ylabel(target)
            save_plot(
                "05_cat_vs_num_bar.png",
                f"05. Efficiency Benchmark: {target} by {cat_cols[0]}",
            )
    except Exception as e:
        errors.append(f"05: {str(e)}")

    # 6. Performance Quadrants
    try:
        if len(num_cols) > 1:
            plt.figure(figsize=(10, 6))
            x_m, y_m = num_cols[0], num_cols[1]
            sns.scatterplot(
                data=df,
                x=x_m,
                y=y_m,
                hue=cat_cols[0] if cat_cols else None,
                s=150,
                alpha=0.9,
            )
            plt.axvline(df[x_m].mean(), color="red", linestyle="--", alpha=0.5)
            plt.axhline(df[y_m].mean(), color="red", linestyle="--", alpha=0.5)
            save_plot(
                "06_scatter_relation.png", f"06. Performance Quadrants: {x_m} vs {y_m}"
            )
    except Exception as e:
        errors.append(f"06: {str(e)}")

    # 7. Strategic Velocity (v4.1.4)
    try:
        plt.figure(figsize=(12, 6))
        sns.lineplot(
            data=df,
            x=df.index,
            y=num_cols[0],
            marker="o",
            linewidth=2.5,
            color="#E67E22",
        )
        plt.xlabel("Campaign Order (Sequence)")
        plt.ylabel(num_cols[0])
        save_plot("07_line_trend.png", f"07. Strategic Velocity Trend: {num_cols[0]}")
    except Exception as e:
        errors.append(f"07: {str(e)}")

    # 8. Success Concentration (Absolute Bar v4.1.4)
    try:
        if cat_cols and num_cols:
            plt.figure(figsize=(10, 6))
            cat, val = cat_cols[0], num_cols[0]
            # Usar valores agrupados para asegurar barra única por categoría
            plot_data = (
                df.groupby(cat)[val].sum().sort_values(ascending=False).reset_index()
            )
            sns.barplot(data=plot_data, x=cat, y=val, palette="viridis")
            plt.xticks(rotation=45)
            plt.title(f"08. Success Concentration: {val} by {cat}")
            save_plot("08_violin_density.png", f"08. Success Concentration by {cat}")
    except Exception as e:
        errors.append(f"08: {str(e)}")

    # 9. Resource Intensity (Adaptive Visualization v4.1.3)
    try:
        if len(num_cols) > 1:
            x_m, y_m = num_cols[0], num_cols[1]
            # Usar scatter para pocos datos (evitar artefactos de hexbin), hex para muchos
            plot_kind = "scatter" if len(df) < 30 else "hex"

            g = sns.jointplot(data=df, x=x_m, y=y_m, kind=plot_kind, color="#4CB391")

            # Mejorar estética: añadir título y ajustar layout
            g.fig.suptitle(
                f"09. Multi-dimensional Resource Intensity ({plot_kind})",
                y=1.02,
                fontweight="bold",
            )
            plt.savefig(
                os.path.join(output_dir, "09_joint_hex.png"),
                dpi=300,
                bbox_inches="tight",
            )
            plt.close()
    except Exception as e:
        errors.append(f"09: {str(e)}")

    # 10. Market Dominance (Volume Share v4.1.2)
    try:
        if cat_cols:
            plt.figure(figsize=(8, 8))
            cat = cat_cols[0]
            # Priorizar spend para dominancia de mercado, luego clicks
            dominance_metric = (
                "spend"
                if "spend" in df.columns
                else ("clicks" if "clicks" in df.columns else None)
            )

            if dominance_metric:
                plot_data = (
                    df.groupby(cat)[dominance_metric].sum().sort_values(ascending=False)
                )
                plt.pie(
                    plot_data,
                    labels=plot_data.index,
                    autopct="%1.1f%%",
                    colors=sns.color_palette("pastel"),
                    startangle=140,
                    pctdistance=0.85,
                )
                # Dibujar un círculo blanco en el centro para convertirlo en donut (estética premium)
                centre_circle = plt.Circle((0, 0), 0.70, fc="white")
                fig = plt.gcf()
                fig.gca().add_artist(centre_circle)
                plt.title(f"10. Market Dominance: {cat} Share by {dominance_metric}")
            else:
                counts = df[cat].value_counts()
                plt.pie(
                    counts,
                    labels=counts.index,
                    autopct="%1.1f%%",
                    colors=sns.color_palette("pastel"),
                )

            save_plot("10_composition_pie.png", f"10. Market Dominance: {cat} Share")
    except Exception as e:
        errors.append(f"10: {str(e)}")

    # Reporte de Resiliencia
    if errors:
        with open(
            os.path.join(output_dir, "visual_errors.log"), "w", encoding="utf-8"
        ) as f:
            f.write(
                "⚠️ INSTRUC_UPDATE: Se detectaron inconsistencias visuales que requieren atención:\n"
            )
            for err in errors:
                f.write(f"- {err}\n")
        print(f"❌ Se detectaron {len(errors)} errores visuales. Ver visual_errors.log")
    else:
        log_path = os.path.join(output_dir, "visual_errors.log")
        if os.path.exists(log_path):
            os.remove(log_path)
        print(f"✨ Dashboard Power Dash (v2.1) generado con éxito en {output_dir}")


if __name__ == "__main__":
    # Usar paths relativos al directorio del script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "test_marketing_data.csv")
    output_dir = script_dir
    run_analysis(data_path, output_dir)
