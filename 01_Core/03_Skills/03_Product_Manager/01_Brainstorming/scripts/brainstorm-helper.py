#!/usr/bin/env python3
"""
Brainstorm Helper

Generates exploration questions for brainstorming sessions.
"""

import sys


QUESTIONS_TEMPLATE = {
    "purpose": [
        "¿Qué problema resuelve esta feature?",
        "¿Quién es el usuario principal que se beneficia?",
        "¿Cómo medimos el éxito de esta implementación?",
    ],
    "constraints": [
        "¿Qué NO debe cambiar en el sistema actual?",
        "¿Hay deadlines o dependencias externas?",
        "¿Hay integraciones obligatorias (APIs, servicios)?",
    ],
    "scope": [
        "¿Es MVP o versión completa?",
        "¿Qué features son must-have vs nice-to-have?",
        "¿Hay límites de tiempo o presupuesto?",
    ],
    "preferences": [
        "¿Prefieres simplicidad o flexibilidad?",
        "¿Prefieres rápido de implementar o fácil de mantener?",
        "¿El rendimiento es crítico para esta feature?",
    ],
}


def generate_questions(category=None):
    """Generate brainstorming questions."""
    print("=" * 50)
    print("🧠 BRAINSTORM HELPER")
    print("=" * 50)

    if category and category in QUESTIONS_TEMPLATE:
        questions = QUESTIONS_TEMPLATE[category]
        print(f"\nCategory: {category.upper()}\n")
        for i, q in enumerate(questions, 1):
            print(f"{i}. {q}")
    else:
        print("\nAvailable categories:")
        for cat in QUESTIONS_TEMPLATE.keys():
            print(f"  - {cat}")
        print("\nUsage: python brainstorm-helper.py <category>")


if __name__ == "__main__":
    category = sys.argv[1] if len(sys.argv) > 1 else None
    generate_questions(category)
