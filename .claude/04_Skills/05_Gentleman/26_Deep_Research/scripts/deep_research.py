#!/usr/bin/env python3
"""
Deep Research Helper - PersonalOS
Ayuda a estructurar y validar procesos de investigación profunda.
"""

import sys

def create_research_plan(topic):
    print(f"--- 🔍 Plan de Investigación Profunda: {topic} ---")
    print("1. Preguntas de investigación:")
    print(f"   - ¿Qué es {topic} en su núcleo?")
    print(f"   - ¿Cuáles son los 3 mayores innovadores en este campo?")
    print(f"   - ¿Cuál es el estado del arte actual?")
    print("\n2. Fuentes recomendadas:")
    print("   - Papers académicos (ArXiv, Google Scholar)")
    print("   - Documentación técnica oficial")
    print("   - Newsletters especializadas (Every, TLDR)")
    print("\n3. Estructura del Reporte:")
    print("   - Resumen Ejecutivo")
    print("   - Contexto Histórico")
    print("   - Análisis Técnico")
    print("   - Conclusiones y Próximos Pasos")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_research_plan(sys.argv[1])
    else:
        print("Uso: python deep_research.py 'Tema de investigación'")
