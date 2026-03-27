"""
ZINKING WRITER - Sistema de Transformación de Comunicación
==========================================================

Transforma cualquier contenido en una experiencia de conexión humana profunda,
siguiendo los principios de comunicación transformacional Zinking.

Autor: Sistema Zinking
Versión: 1.0
"""

import random
import re
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class ZinkingPatterns:
    """Patrones lingüísticos característicos de Zinking"""

    openings: List[str] = None
    transitions: List[str] = None
    validations: List[str] = None
    invitations: List[str] = None
    closings: List[str] = None
    sensorial_details: List[str] = None
    reflective_questions: List[str] = None

    def __post_init__(self):
        self.openings = [
            "Recuerdo cuando",
            "Hace tiempo, me encontré",
            "Hubo un momento en mi vida en que",
            "Nunca olvidaré aquella vez que",
            "Permíteme contarte algo que aprendí",
            "Había una época en la que",
            "Un día descubrí algo que cambió todo:"
        ]

        self.transitions = [
            "Esa experiencia me enseñó que",
            "Desde entonces entendí que",
            "Lo que descubrí fue simple pero profundo:",
            "Y ahí estaba la lección:",
            "Eso transformó mi forma de ver",
            "Fue entonces cuando comprendí:",
            "La revelación llegó en ese preciso instante:"
        ]

        self.validations = [
            "Si alguna vez has sentido",
            "Quizás tú también has experimentado",
            "Sé que esto puede parecer",
            "Es completamente normal",
            "No estás solo en esto",
            "Muchos hemos pasado por",
            "Reconozco esa sensación de"
        ]

        self.invitations = [
            "Te invito a explorar",
            "¿Qué pasaría si",
            "Prueba esto y observa",
            "Permítete",
            "Considera la posibilidad de",
            "Imagina por un momento",
            "Experimenta con"
        ]

        self.closings = [
            "La magia sucede cuando",
            "Cada paso cuenta",
            "El viaje apenas comienza",
            "Y así, poco a poco",
            "Eso es lo que hace la diferencia",
            "Ahí es donde todo cambia",
            "Ese es el momento en que"
        ]

        self.sensorial_details = [
            "El aroma a café llenaba la habitación.",
            "La luz suave entraba por la ventana como una invitación.",
            "Podía escuchar el silencio a mi alrededor.",
            "Las manos me temblaban ligeramente.",
            "El aire se sentía denso de posibilidad.",
            "La quietud del momento era casi palpable.",
            "Una brisa fresca movía las cortinas suavemente.",
            "El tic-tac del reloj marcaba cada segundo con presencia."
        ]

        self.reflective_questions = [
            "¿Qué pequeño paso podrías dar hoy?",
            "¿Qué te gustaría descubrir en este camino?",
            "¿Cómo se sentiría permitirte explorar sin juicio?",
            "¿Qué cambiaría si simplificaras un poco más?",
            "¿Dónde está tu atención en este momento?",
            "¿Qué verdad estás listo para abrazar?",
            "¿Qué te está susurrando tu intuición?",
            "¿Qué sucedería si confiaras en el proceso?"
        ]


class ZinkingAnalogy:
    """Generador de analogías cotidianas y memorables"""

    ANALOGIES = [
        {
            "concepts": ["proceso", "aprender", "práctica", "mejorar"],
            "analogy": "afinar un instrumento",
            "elaboration": "no lo haces una vez y olvidas; es un ajuste constante, sutil, que requiere oído atento"
        },
        {
            "concepts": ["simplificar", "reducir", "esencial", "minimalismo"],
            "analogy": "ir de mochilero en lugar de en casa rodante",
            "elaboration": "te mueves más rápido, llegas a lugares inaccesibles, y la experiencia se vuelve íntima"
        },
        {
            "concepts": ["intuición", "experiencia", "maestría"],
            "analogy": "cocinar sin receta",
            "elaboration": "al principio necesitas medir todo con precisión, pero con el tiempo tus manos 'saben' cuánto agregar"
        },
        {
            "concepts": ["editar", "refinar", "pulir", "mejorar"],
            "analogy": "tallar una escultura",
            "elaboration": "no agregas material, quitas lo que sobra hasta revelar la forma que siempre estuvo ahí"
        },
        {
            "concepts": ["crecimiento", "desarrollo", "evolución", "progreso"],
            "analogy": "cultivar un jardín",
            "elaboration": "no ves el cambio diario, pero de repente florece algo hermoso. La paciencia es parte del proceso"
        },
        {
            "concepts": ["atención", "enfoque", "concentración", "presencia"],
            "analogy": "encender una linterna en la oscuridad",
            "elaboration": "solo puedes iluminar una parte a la vez, pero esa luz revela detalles que antes eran invisibles"
        },
        {
            "concepts": ["conexión", "relación", "comunicación"],
            "analogy": "bailar con alguien",
            "elaboration": "requiere escuchar, ajustarse, moverse al ritmo del otro sin perder tu propia esencia"
        },
        {
            "concepts": ["paciencia", "tiempo", "espera"],
            "analogy": "esperar que hierva el agua",
            "elaboration": "observar el proceso no lo acelera, pero estar presente transforma la experiencia de la espera"
        }
    ]

    @classmethod
    def find_matching_analogy(cls, text: str) -> Dict:
        """Encuentra la analogía más relevante para el texto dado"""
        text_lower = text.lower()

        for analogy in cls.ANALOGIES:
            for concept in analogy["concepts"]:
                if concept in text_lower:
                    return analogy

        # Si no hay coincidencia, devolver una analogía aleatoria
        return random.choice(cls.ANALOGIES)


class ZinkingTransformer:
    """Motor principal de transformación Zinking"""

    def __init__(self):
        self.patterns = ZinkingPatterns()

    def clean_technical_language(self, text: str) -> str:
        """Suaviza el lenguaje técnico y autoritario"""

        replacements = {
            r'\bdebes\b': 'podrías considerar',
            r'\btienes que\b': 'podrías',
            r'\bes necesario\b': 'puede ser útil',
            r'\bes obligatorio\b': 'es valioso',
            r'\bsiempre\b': 'a menudo',
            r'\bnunca\b': 'rara vez',
            r'\bLos expertos\b': 'He descubierto que',
            r'\bSe recomienda\b': 'Una opción es',
            r'\bLa única forma\b': 'Una forma efectiva',
            r'\bincorrecto\b': 'diferente',
            r'\berror\b': 'oportunidad de aprendizaje'
        }

        result = text
        for pattern, replacement in replacements.items():
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

        return result

    def remove_formatting(self, text: str) -> List[str]:
        """Elimina bullets, números y formato excesivo"""
        lines = text.split('\n')
        cleaned = []

        for line in lines:
            # Eliminar bullets, números, asteriscos
            line = re.sub(r'^[\d\-\*\•►]+\.?\s*', '', line.strip())
            if line:
                cleaned.append(line)

        return cleaned

    def create_opening(self, content_type: str) -> str:
        """Genera una apertura con historia personal"""
        opening = random.choice(self.patterns.openings)
        sensorial = random.choice(self.patterns.sensorial_details)

        context = {
            'educativo': 'algo que cambió mi perspectiva sobre este tema.',
            'inspiracional': 'algo que transformó mi forma de ver las cosas.',
            'tecnico': 'un momento que me ayudó a entender esto de una manera completamente nueva.',
            'general': 'algo que resonó profundamente conmigo.'
        }

        intro = f"{opening} {context.get(content_type, context['general'])} "
        intro += "Estaba enfrentando exactamente lo que tú podrías estar explorando ahora. "
        intro += f"Había dudas, incertidumbre... {sensorial}\n\n"

        return intro

    def create_main_content(self, cleaned_lines: List[str], text: str) -> str:
        """Transforma el contenido principal con voz Zinking"""
        transition = random.choice(self.patterns.transitions)

        # Unir y limpiar contenido
        main_text = '. '.join(cleaned_lines)
        main_text = self.clean_technical_language(main_text)

        # Encontrar analogía relevante
        analogy = ZinkingAnalogy.find_matching_analogy(text)

        result = f"{transition} {main_text}\n\n"
        result += f"Piénsalo como {analogy['analogy']}: {analogy['elaboration']}. "
        result += "Así funciona esto también.\n\n"

        return result

    def create_validation(self) -> str:
        """Genera validación empática"""
        validation = random.choice(self.patterns.validations)

        return (f"{validation} esta sensación de incertidumbre, "
                "estás en el camino correcto. "
                "La incomodidad es donde sucede el crecimiento. "
                "No necesitas tener todas las respuestas ahora.\n\n")

    def create_action_steps(self, content_type: str) -> str:
        """Crea pasos accionables según el tipo de contenido"""
        if content_type not in ['educativo', 'tecnico']:
            return ""

        return ("**Ahora es tu turno:**\n\n"
                "Empieza pequeño. Elige una sola cosa de lo que hemos explorado. "
                "No todas. Una. "
                "Practícala durante tres días. "
                "Observa qué descubres. "
                "No busques perfección, busca presencia.\n\n")

    def create_closing(self) -> str:
        """Genera cierre inspirador con invitación"""
        invitation = random.choice(self.patterns.invitations)
        closing = random.choice(self.patterns.closings)
        question = random.choice(self.patterns.reflective_questions)

        result = f"{invitation} este enfoque con curiosidad, sin presión de perfección. "
        result += f"{closing} nos permitimos ser aprendices perpetuos. "
        result += "Cada paso, por pequeño que parezca, te transforma.\n\n"
        result += f"{question}"

        return result

    def transform(self, text: str, content_type: str = 'general') -> str:
        """
        Transforma texto a estilo Zinking

        Args:
            text: Contenido original a transformar
            content_type: Tipo de contenido ('educativo', 'inspiracional', 'tecnico', 'general')

        Returns:
            Texto transformado con esencia Zinking
        """
        if not text.strip():
            return ""

        # 1. Preparar contenido
        cleaned_lines = self.remove_formatting(text)

        # 2. Construir transformación
        result = ""

        # Apertura con historia personal
        result += self.create_opening(content_type)

        # Contenido principal con analogía
        result += self.create_main_content(cleaned_lines, text)

        # Validación empática
        result += self.create_validation()

        # Pasos accionables (si aplica)
        result += self.create_action_steps(content_type)

        # Cierre inspirador
        result += self.create_closing()

        return result


class ZinkingWriter:
    """Interfaz principal para el sistema Zinking"""

    def __init__(self):
        self.transformer = ZinkingTransformer()

    def write(self, text: str, content_type: str = 'general') -> str:
        """
        Método principal para transformar texto

        Args:
            text: Texto original
            content_type: 'educativo', 'inspiracional', 'tecnico', 'general'

        Returns:
            Texto transformado estilo Zinking
        """
        return self.transformer.transform(text, content_type)

    def get_principles(self) -> Dict[str, str]:
        """Retorna los principios fundamentales de Zinking"""
        return {
            "Vulnerabilidad": "Compartir procesos, no solo éxitos",
            "Analogías": "Comparar con experiencias universales",
            "Validación": "Reconocer lo que el receptor siente",
            "Simplificación": "Reducir al núcleo esencial",
            "Presencia": "Invitar al momento presente",
            "Gratitud": "Enmarcar como privilegio, no derecho",
            "Autenticidad": "La humanidad sobre la perfección",
            "Proceso": "El camino importa más que el destino"
        }

    def analyze_text(self, text: str) -> Dict[str, any]:
        """Analiza un texto y sugiere mejoras Zinking"""

        analysis = {
            "tiene_historia_personal": bool(re.search(r'\b(recuerdo|una vez|cuando yo|mi experiencia)\b', text, re.IGNORECASE)),
            "tiene_analogia": bool(re.search(r'\b(como|es como|similar a|piensa en)\b', text, re.IGNORECASE)),
            "usa_primera_persona": bool(re.search(r'\b(yo|mi|me|nosotros)\b', text, re.IGNORECASE)),
            "tiene_pregunta_reflexiva": bool(re.search(r'\?', text)),
            "lenguaje_autoritario": len(re.findall(r'\b(debes|tienes que|es obligatorio|siempre|nunca)\b', text, re.IGNORECASE)),
            "longitud_parrafos": self._analyze_paragraph_length(text),
            "tiene_validacion": bool(re.search(r'\b(sé que|comprendo|entiendo que|si alguna vez)\b', text, re.IGNORECASE))
        }

        # Puntuación Zinking (0-100)
        score = 0
        if analysis["tiene_historia_personal"]: score += 20
        if analysis["tiene_analogia"]: score += 15
        if analysis["usa_primera_persona"]: score += 15
        if analysis["tiene_pregunta_reflexiva"]: score += 10
        if analysis["lenguaje_autoritario"] == 0: score += 15
        if analysis["longitud_parrafos"] == "adecuada": score += 15
        if analysis["tiene_validacion"]: score += 10

        analysis["zinking_score"] = score
        analysis["nivel"] = self._get_zinking_level(score)

        return analysis

    def _analyze_paragraph_length(self, text: str) -> str:
        """Analiza la longitud de los párrafos"""
        paragraphs = [p for p in text.split('\n\n') if p.strip()]
        avg_length = sum(len(p.split()) for p in paragraphs) / len(paragraphs) if paragraphs else 0

        if avg_length < 30:
            return "muy_corta"
        elif avg_length <= 80:
            return "adecuada"
        else:
            return "muy_larga"

    def _get_zinking_level(self, score: int) -> str:
        """Determina el nivel de Zinking del texto"""
        if score >= 80:
            return "Excelente - Auténtico Zinking"
        elif score >= 60:
            return "Bueno - Tiene elementos Zinking"
        elif score >= 40:
            return "Aceptable - Necesita más calidez"
        else:
            return "Inicial - Requiere transformación profunda"


# ============================================================================
# EJEMPLOS DE USO
# ============================================================================

def main():
    """Función principal con ejemplos de uso"""

    print("=" * 70)
    print("ZINKING WRITER - Sistema de Transformación de Comunicación")
    print("=" * 70)
    print()

    # Inicializar escritor
    writer = ZinkingWriter()

    # Ejemplo 1: Contenido Educativo
    print("📚 EJEMPLO 1: Contenido Educativo")
    print("-" * 70)

    original_educativo = """
    La gestión del tiempo es importante para la productividad.
    Debes planificar tus tareas diariamente.
    Usa listas de pendientes.
    Elimina todas las distracciones.
    Siempre prioriza lo urgente.
    """

    print("ORIGINAL:")
    print(original_educativo)
    print("\nTRANSFORMADO:")
    print(writer.write(original_educativo, 'educativo'))
    print("\n" + "=" * 70 + "\n")

    # Ejemplo 2: Contenido Técnico
    print("💻 EJEMPLO 2: Contenido Técnico")
    print("-" * 70)

    original_tecnico = """
    Para optimizar tu código:
    - Usa variables con nombres descriptivos
    - Evita la repetición de código
    - Comenta las secciones complejas
    - Siempre sigue las mejores prácticas
    """

    print("ORIGINAL:")
    print(original_tecnico)
    print("\nTRANSFORMADO:")
    print(writer.write(original_tecnico, 'tecnico'))
    print("\n" + "=" * 70 + "\n")

    # Ejemplo 3: Análisis de texto
    print("🔍 EJEMPLO 3: Análisis de Texto")
    print("-" * 70)

    texto_a_analizar = """
    Recuerdo cuando empecé a programar. Tenía miedo de cometer errores.
    Pero cada bug me enseñó algo valioso. ¿Sabes esa sensación?
    """

    analysis = writer.analyze_text(texto_a_analizar)

    print("TEXTO ANALIZADO:")
    print(texto_a_analizar)
    print("\nRESULTADOS:")
    for key, value in analysis.items():
        print(f"  • {key}: {value}")

    print("\n" + "=" * 70 + "\n")

    # Mostrar principios
    print("🎯 PRINCIPIOS ZINKING:")
    print("-" * 70)
    for principio, descripcion in writer.get_principles().items():
        print(f"  • {principio}: {descripcion}")

    print("\n" + "=" * 70)
    print("✨ La magia sucede cuando la estructura se vuelve invisible")
    print("   y solo queda la verdad.")
    print("=" * 70)


if __name__ == "__main__":
    main()
