#!/usr/bin/env python3
"""
Task Template Classifier
Clasifica tareas y recomienda template: SOTA / MEDIO / CORTO
"""

CRITERIOS = {
    "SOTA": {
        "esfuerzo_min": 8,
        "archivos_min": 10,
        "keywords": [
            "sistema",
            "arquitectura",
            "reestructurar",
            "migración",
            "breaking",
            "multi",
            "complejo",
            "estrategico",
        ],
        "score_min": 8,
    },
    "MEDIO": {
        "esfuerzo_min": 2,
        "archivos_min": 3,
        "keywords": [
            "feature",
            "nuevo",
            "agregar",
            "endpoint",
            "componente",
            "refactorizar",
            "actualizar",
        ],
        "score_min": 4,
    },
    "CORTO": {
        "esfuerzo_min": 0,
        "archivos_min": 1,
        "keywords": [
            "fix",
            "bug",
            "typo",
            "docs",
            "readme",
            "quick",
            "simple",
            "quick-fix",
            "quickfix",
        ],
        "score_min": 1,
    },
}


def classify(descripcion, esfuerzo=None, archivos=None):
    """Clasifica tarea y retorna template recomendado."""
    score = 0
    matched_kw = []

    desc_lower = descripcion.lower()

    # Keywords matching
    for tier, config in CRITERIOS.items():
        for kw in config["keywords"]:
            if kw.lower() in desc_lower:
                score += 2
                matched_kw.append(kw)

    # Esfuerzo
    if esfuerzo:
        if esfuerzo >= 8:
            score += 5
        elif esfuerzo >= 2:
            score += 3
        else:
            score += 1

    # Archivos
    if archivos:
        if archivos >= 10:
            score += 4
        elif archivos >= 3:
            score += 2
        else:
            score += 1

    # Decisión
    if score >= 8:
        return "SOTA", score, matched_kw
    elif score >= 4:
        return "MEDIO", score, matched_kw
    else:
        return "CORTO", score, matched_kw


def main():
    import sys

    if len(sys.argv) < 2:
        print(
            "Uso: python 59_Task_Classifier.py 'descripción tarea' [esfuerzo horas] [archivos]"
        )
        print("Ejemplo: python 59_Task_Classifier.py 'Agregar backup automático' 2 3")
        sys.exit(1)

    desc = sys.argv[1]
    esfuerzo = int(sys.argv[2]) if len(sys.argv) > 2 else None
    archivos = int(sys.argv[3]) if len(sys.argv) > 3 else None

    template, score, keywords = classify(desc, esfuerzo, archivos)

    print(f"")
    print(f"  Clasificacion: {template}")
    print(f"  Score: {score}")
    print(f"  Keywords: {', '.join(keywords) if keywords else 'ninguno'}")
    print(f"")
    print(f"  Template sugerido: 03_Task_Template_{template.upper()}.md")
    print(f"")


if __name__ == "__main__":
    main()
