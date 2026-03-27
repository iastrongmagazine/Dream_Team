#!/usr/bin/env python3
import sys
import json
import re
from pathlib import Path

class ZinkingTransformer:
    """
    Motor de transformación Zinking.
    Transforma texto frío en comunicación cálida y humana.
    """

    def __init__(self):
        self.rules = {
            "authoritarian": [
                (r"\bdebes\b", "te invito a"),
                (r"\bes obligatorio\b", "se siente natural"),
                (r"\btienes que\b", "podemos explorar juntos"),
            ],
            "technical_to_human": [
                (r"\boptimizar rendimiento\b", "honrar la fluidez de cada proceso"),
                (r"\bejecutar proceso\b", "dar vida a este movimiento"),
                (r"\bfuncionalidad\b", "oportunidad de conexión"),
                (r"\busuario\b", "persona que busca claridad"),
            ]
        }

    def transform(self, text, style="educativo"):
        transformed = text
        for category in self.rules.values():
            for pattern, replacement in category:
                transformed = re.sub(pattern, replacement, transformed, flags=re.IGNORECASE)

        # Estructura Zinking: Vulnerabilidad -> Contexto -> Analogía -> Acción
        opening = "Hubo un momento en que el ruido digital me impedía ver lo esencial. Perdí la conexión con el propósito real."
        analogy = "\n\nComo dice Dieter Rams, el buen diseño es honesto. No busca impresionar con lo superfluo, sino servir con verdad."
        reflection = "\n\nAl final, no estamos construyendo herramientas, estamos diseñando el contexto para que otros respiren."
        action = "\n\n**Invitación:** Siéntate derecho, respira profundo y mira lo que has creado hoy. ¿Tiene alma?"

        return f"{opening}\n\n{transformed}{analogy}\n\n{reflection}\n\n{action}"

def main():
    if len(sys.argv) < 3:
        print("Usage: zinking_transformer.py <input.json> <output.json>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    text = data.get("text", "")
    style = data.get("style", "educativo")

    transformer = ZinkingTransformer()
    result = transformer.transform(text, style)

    output = {
        "status": "success",
        "original_text": text,
        "transformed_text": result,
        "style_applied": style
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
