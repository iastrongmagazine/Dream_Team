"""
SPIDER BRAINSTORM ENGINE - PersonalOS v1.0
Explora requisitos y enfoques a través de diálogo colaborativo antes de planificar implementación.
Ideal para explorar ideas complejas y problemas multifacéticos.

Basado en: .agent/03_Workflows/01_Spider_Brainstorm.md
"""

import subprocess
import sys
import os
import importlib.util
from datetime import datetime
from config_paths import ROOT_DIR, BRAINSTORMS_DIR

# --- CONFIGURACIÓN ARMOR LAYER ---
if sys.stdout.encoding != "utf-8":
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=1)

# Configuración de Colores
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    SUCCESS = Fore.GREEN
    INFO = Fore.CYAN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    RESET = Style.RESET_ALL
except ImportError:
    SUCCESS = ""
    INFO = ""
    WARNING = ""
    ERROR = ""
    RESET = ""


def dynamic_speak(text):
    """Interfaz de voz para comunicación interactiva."""
    try:
        hooks_dir = os.path.join(ROOT_DIR, ".agent", "04_Extensions", "hooks")
        hook_path = os.path.join(hooks_dir, "utils", "common.py")
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location("common", str(hook_path))
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.speak(text)
        else:
            print(f"[VOZ] {text}")
    except Exception as e:
        print(f"[VOZ] Error en interfaz de voz: {e}")
        print(f"[VOZ] {text}")


def run_command(command, description, cwd=None):
    """Ejecuta un comando de forma segura con manejo de errores."""
    print(f"\n{INFO}>>> {description}...{RESET}")

    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, cwd=cwd
        )
        if result.returncode == 0:
            print(f"{SUCCESS}[OK] {description} completado.{RESET}")
            if result.stdout:
                print(f"{INFO}Salida: {result.stdout[:200]}...{RESET}")
            return True
        else:
            print(
                f"{ERROR}[ERR] {description} falló. Código: {result.returncode}{RESET}"
            )
            if result.stderr:
                print(f"{ERROR}Error: {result.stderr[:200]}...{RESET}")
            return False
    except Exception as e:
        print(f"{ERROR}[ERR] Error ejecutando {description}: {e}{RESET}")
        return False


def ensure_brainstorms_dir():
    """Asegura que el directorio de brainstorms exista."""
    os.makedirs(BRAINSTORMS_DIR, exist_ok=True)
    return BRAINSTORMS_DIR


def write_brainstorm_document(topic, approaches, decisions, open_questions):
    """Escribe el documento de brainstorm en el directorio adecuado."""
    brainstorms_dir = ensure_brainstorms_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"{timestamp}-{topic}-brainstorm.md"
    filepath = os.path.join(brainstorms_dir, filename)

    content = f"""# 🧠 Brainstorm: {topic}

**Fecha:** {timestamp}
**Tipo:** Spider Brainstorm Session
**Estado:** Completado

---

## 📝 What We're Building

{topic}

### Contexto del Problema
Este brainstorm explora diferentes enfoques para resolver el problema o implementar la feature solicitada. El objetivo es identificar la mejor estrategia antes de entrar en la fase de planificación detallada.

---

## 🎯 Why This Approach Matters

Explorar múltiples ángulos nos permite:

1. **Evitar soluciones prematuras** - Entender el problema a fondo antes de resolverlo
2. **Identificar trade-offs** - Evaluar pros y contras de cada enfoque
3. **Reducir riesgo de rework** - Validar la dirección antes de invertir tiempo en implementación
4. **Mejor diseño** - Considerar aspectos de escalabilidad, mantenibilidad y rendimiento

---

## 🔍 Approach Exploration

### Enfoque 1: Solución Minimalista
**Descripción:** Enfoque rápido y enfocado en resolver el problema principal con la menor complejidad posible.

**Ventajas:**
- Rápidos tiempos de implementación (días vs semanas)
- Menor riesgo técnico
- Fácil de entender y mantener
- Buena para validación temprana

**Desventajas:**
- Alcange limitado
- Mayor deuda técnica futura
- Menor escalabilidad
- Posible necesidad de rework completo

**Ideal para:** MVPs, validación de conceptos, proyectos con plazos ajustados

### Enfoque 2: Solución Completa
**Descripción:** Arquitectura robusta con todos los requisitos, escalabilidad y mantenibilidad en mente.

**Ventajas:**
- Arquitectura limpia y extensible
- Menor deuda técnica a largo plazo
- Escalabilidad óptima
- Sigue mejores prácticas del sector

**Desventajas:**
- Mayor tiempo de implementación (semanas vs días)
- Complejidad inicial más alta
- Requiere más planificación
- Riesgo de sobrediseño

**Ideal para:** Productos maduros, sistemas críticos, proyectos a largo plazo

### Enfoque 3: Solución Híbrida
**Descripción:** Balance entre velocidad y arquitectura, implementando lo esencial con estructura extensible.

**Ventajas:**
- Balance entre velocidad y calidad
- Arquitectura modular para extensión futura
- Menor riesgo que solución completa
- Más rápido que solución completa

**Desventajas:**
- Trade-offs en diseño
- Posible deuda técnica moderada
- Requiere buen criterio de diseño
- Menos predecible que los otros enfoques

**Ideal para:** La mayoría de proyectos comerciales, startups en crecimiento

---

## 🎯 Key Decisions

{chr(10).join(f"- {decision}" for decision in decisions)}

---

## ❓ Open Questions

{chr(10).join(f"- {question}" for question in open_questions)}

---

## 📊 Next Steps

1. **✅ Brainstorm completado** - {len(approaches)} enfoques explorados
2. **🎯 Recomendación:** {approaches[0]["name"]} if approaches else 'Requiere validación'
3. **🚀 Próximo paso:** Ejecutar `/workflows:plan` para implementación

---

*"El buen diseño no es lo que hay de bueno, sino lo que es adecuado."*
— Spider Brainstorm Engine v1.0
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"{ERROR}[ERR] Error escribiendo documento de brainstorm: {e}{RESET}")
        return None


def assess_requirements_clarity(task_description):
    """Evalúa si los requisitos son claros para determinar si se necesita brainstorm."""
    print(f"\n{INFO}[1/4] EVALUANDO CLARIDAD DE REQUISITOS...{RESET}")
    dynamic_speak("Evaluando claridad de los requisitos antes de continuar.")

    # Indicadores de requisitos claros
    clarity_indicators = {
        "Criterios específicos": False,
        "Patrones existentes": False,
        "Comportamiento esperado": False,
        "Alcance definido": False,
    }

    # Análisis simple de la descripción
    description_lower = task_description.lower()

    if any(
        word in description_lower
        for word in ["debe", "requiere", "necesita", "debería"]
    ):
        clarity_indicators["Criterios específicos"] = True

    if any(
        word in description_lower for word in ["similar", "como", "seguir", "patrón"]
    ):
        clarity_indicators["Patrones existentes"] = True

    if any(
        word in description_lower
        for word in ["funcionalidad", "característica", "comportamiento"]
    ):
        clarity_indicators["Comportamiento esperado"] = True

    if any(
        word in description_lower
        for word in ["solo", "solamente", "exclusivamente", "limitado"]
    ):
        clarity_indicators["Alcance definido"] = True

    # Contar indicadores
    clear_count = sum(clarity_indicators.values())

    print(f"{INFO}Indicadores de claridad evaluados:{RESET}")
    for indicator, is_clear in clarity_indicators.items():
        status = "✓" if is_clear else "✗"
        print(f"{INFO}  {status} {indicator}{RESET}")

    print(f"\n{INFO}Resultado: {clear_count}/4 indicadores de claridad{RESET}")

    # Determinar si se necesita brainstorm
    needs_brainstorm = clear_count < 3

    if needs_brainstorm:
        print(f"{INFO}Requieren exploración adicional - Brainstorm recomendado{RESET}")
    else:
        print(
            f"{SUCCESS}Requisitos claros - Podría proceder directamente a planificación{RESET}"
        )

    return needs_brainstorm


def repo_research_analyst(task_description):
    """Investigación de patrones existentes en el repositorio."""
    print(f"\n{INFO}[2/4] INVESTIGACIÓN DE PATRONES EXISTENTES...{RESET}")
    dynamic_speak(
        "Investigando patrones existentes y soluciones similares en el códigobase."
    )

    # Buscar archivos relevantes
    relevant_files = []
    search_terms = [
        "feature",
        "component",
        "service",
        "api",
        "auth",
        "user",
        "data",
        "ui",
    ]

    for root, dirs, files in os.walk(ROOT_DIR):
        # Evitar directorios irrelevantes
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".")
            and d not in ["__pycache__", "node_modules", "venv"]
        ]

        for file in files:
            if file.endswith((".py", ".js", ".ts", ".md", ".json")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().lower()
                        if any(term in content for term in search_terms):
                            relevant_files.append(file_path)
                except:
                    continue

    # Limitar a los archivos más relevantes
    relevant_files = relevant_files[:10]

    print(f"{INFO}Patrones encontrados en {len(relevant_files)} archivos:{RESET}")
    for file_path in relevant_files[:5]:  # Mostrar primeros 5
        relative_path = os.path.relpath(file_path, ROOT_DIR)
        print(f"{INFO}  • {relative_path}{RESET}")

    return relevant_files


def explore_approaches(task_description, existing_patterns):
    """Explora 2-3 enfoques concretos basados en investigación."""
    print(f"\n{INFO}[3/4] EXPLORANDO ENFOQUES CONCRETOS...{RESET}")
    dynamic_speak("Explorando enfoques concretos para la implementación.")

    # Definir enfoques basados en la tarea
    approaches = []

    if "autentic" in task_description.lower() or "auth" in task_description.lower():
        approaches = [
            {
                "name": "OAuth2 con JWT",
                "description": "Implementación estándar con tokens JSON web y refresh tokens",
                "pros": [
                    "Estándar de la industria",
                    "Escalable",
                    "Seguro",
                    "Buen soporte",
                ],
                "cons": [
                    "Complejidad inicial",
                    "Requiere gestión de tokens",
                    "Mayor superficie de ataque",
                ],
                "best_for": "Aplicaciones web modernas con múltiples clientes",
            },
            {
                "name": "Session Simple",
                "description": "Manejo tradicional de sesiones con servidor stateful",
                "pros": [
                    "Simple de implementar",
                    "Familiar",
                    "Menor complejidad",
                    "Buen para prototipos",
                ],
                "cons": [
                    "Menos escalable",
                    "Dependencia de servidor",
                    "Problemas de CORS",
                ],
                "best_for": "Aplicaciones simples o proyectos pequeños",
            },
            {
                "name": "Magic Link",
                "description": "Autenticación mediante enlaces mágicos por email",
                "pros": ["Excelente UX", "Sin contraseñas", "Seguro", "Fácil de usar"],
                "cons": [
                    "Requiere servicio de email",
                    "Menos control",
                    "Dependencia externa",
                ],
                "best_for": "Aplicaciones orientadas a usuarios finales",
            },
        ]
    elif "data" in task_description.lower() or "base" in task_description.lower():
        approaches = [
            {
                "name": "SQL Relacional",
                "description": "Base de datos relacional con esquema fijo y transacciones ACID",
                "pros": [
                    "Integridad de datos",
                    "Transacciones",
                    "Consultas complejas",
                    "Maduro",
                ],
                "cons": ["Menos flexible", "Esquema rígido", "Escalabilidad limitada"],
                "best_for": "Sistemas con datos estructurados y relaciones complejas",
            },
            {
                "name": "NoSQL Documental",
                "description": "Base de datos documental como MongoDB para datos flexibles",
                "pros": [
                    "Flexibilidad esquemática",
                    "Escalabilidad horizontal",
                    "Rendimiento",
                    "Schema-less",
                ],
                "cons": [
                    "Menor consistencia",
                    "Consultas complejas difíciles",
                    "Menos maduro",
                ],
                "best_for": "Aplicaciones con datos no estructurados o alta escalabilidad",
            },
            {
                "name": "Híbrida",
                "description": "Combinación de SQL para datos estructurados y NoSQL para flexibilidad",
                "pros": [
                    "Lo mejor de ambos mundos",
                    "Flexibilidad + integridad",
                    "Adaptable",
                ],
                "cons": [
                    "Complejidad adicional",
                    "Gestión de dos sistemas",
                    "Mayor costo",
                ],
                "best_for": "Sistemas complejos con múltiples tipos de datos",
            },
        ]
    else:
        # Enfoques genéricos
        approaches = [
            {
                "name": "Minimal Viable",
                "description": "Implementación mínima que resuelve el problema principal",
                "pros": ["Rápido", "Bajo riesgo", "Fácil de entender"],
                "cons": ["Alcange limitado", "Mayor deuda técnica"],
                "best_for": "MVPs y validación temprana",
            },
            {
                "name": "Robust Architecture",
                "description": "Arquitectura completa con patrones de diseño probados",
                "pros": ["Escalable", "Mantenible", "Menor deuda técnica"],
                "cons": ["Mayor tiempo", "Complejidad inicial"],
                "best_for": "Sistemas a largo plazo",
            },
            {
                "name": "Incremental",
                "description": "Implementación incremental con mejora continua",
                "pros": ["Balance velocidad/calidad", "Adaptable", "Bajo riesgo"],
                "cons": ["Requiere planificación", "Menos predecible"],
                "best_for": "Proyectos en evolución",
            },
        ]

    # Mostrar enfoques
    print(f"{INFO}Enfoques explorados:{RESET}")
    for i, approach in enumerate(approaches, 1):
        print(f"\n{INFO}{i}. {approach['name']}{RESET}")
        print(f"{INFO}   Descripción: {approach['description']}{RESET}")
        print(f"{INFO}   Ventajas: {', '.join(approach['pros'])}{RESET}")
        print(f"{INFO}   Desventajas: {', '.join(approach['cons'])}{RESET}")
        print(f"{INFO}   Ideal para: {approach['best_for']}{RESET}")

    # Recomendación
    recommended = approaches[0]  # Por defecto el primero
    print(f"\n{SUCCESS}🎯 Recomendación: {recommended['name']}{RESET}")
    print(f"{INFO}Motivo: {recommended['description']}{RESET}")

    return approaches, recommended


def capture_design_decisions(approaches, recommended):
    """Captura decisiones de diseño clave."""
    print(f"\n{INFO}[4/4] CAPTURANDO DECISIONES DE DISEÑO...{RESET}")
    dynamic_speak("Capturando decisiones de diseño y capturando el documento.")

    # Decisiones basadas en el enfoque recomendado
    decisions = [
        f"Enfoque seleccionado: {recommended['name']}",
        f"Arquitectura base: {recommended['description']}",
        "Requiere pruebas unitarias y de integración",
        "Debe seguir patrones existentes del códigobase",
        "Documentación técnica requerida",
    ]

    # Preguntas abiertas
    open_questions = [
        "¿Requiere integración con sistemas externos?",
        "¿Consideraciones de seguridad adicionales?",
        "¿Requisitos de rendimiento específicos?",
        "¿Escenarios de uso no contemplados?",
        "¿Dependencias técnicas a considerar?",
    ]

    # Crear documento de brainstorm
    topic = f"feature-{task_description.lower().replace(' ', '-').replace('.', '')}"
    doc_path = write_brainstorm_document(
        topic=task_description,
        approaches=approaches,
        decisions=decisions,
        open_questions=open_questions,
    )

    if doc_path:
        print(
            f"{SUCCESS}✅ Documento de brainstorm creado: {os.path.relpath(doc_path, ROOT_DIR)}{RESET}"
        )
    else:
        print(f"{ERROR}❌ Error al crear documento de brainstorm{RESET}")

    return decisions, open_questions, doc_path


def main():
    """Punto de entrada del Spider Brainstorm Engine."""
    if len(sys.argv) < 2:
        print(
            f'{ERROR}Uso: python {sys.argv[0]} "descripción de la feature o problema"{RESET}'
        )
        print(
            f'{INFO}Ejemplo: python {sys.argv[0]} "Implementar sistema de autenticación OAuth2"{RESET}'
        )
        sys.exit(1)

    task_description = sys.argv[1]

    print(f"{INFO}{'=' * 70}")
    print("   SPIDER BRAINSTORM ENGINE - PersonalOS v1.0")
    print(f"   Exploración: {task_description}")
    print(f"{'=' * 70}{RESET}")
    dynamic_speak("Iniciando sesión de brainstorm colaborativa.")

    # Fase 0: Evaluar claridad de requisitos
    needs_brainstorm = assess_requirements_clarity(task_description)

    if not needs_brainstorm:
        print(f"\n{SUCCESS}🎯 Los requisitos parecen claros.{RESET}")
        print(
            f"{INFO}Sugerencia: Podría proceder directamente a `/workflows:plan`{RESET}"
        )
        response = input(
            f"{INFO}¿Continuar con brainstorm de todos modos? (s/n): {RESET}"
        )
        if response.lower() != "s":
            print(
                f"{INFO}Brainstorm omitido. Recomendado usar `/workflows:plan`{RESET}"
            )
            return

    # Fase 1: Entender la idea
    existing_patterns = repo_research_analyst(task_description)

    # Fase 2: Explorar enfoques
    approaches, recommended = explore_approaches(task_description, existing_patterns)

    # Fase 3: Capturar diseño
    decisions, open_questions, doc_path = capture_design_decisions(
        approaches, recommended
    )

    # Fase 4: Handoff
    print(f"\n{INFO}{'=' * 70}")
    print("   🧠 BRAINSTORM COMPLETADO")
    print(f"{'=' * 70}{RESET}")

    print(f"\n{SUCCESS}Resumen del brainstorm:{RESET}")
    print(f"{INFO}• Tarea explorada: {task_description}{RESET}")
    print(f"{INFO}• Enfoques evaluados: {len(approaches)}{RESET}")
    print(f"{INFO}• Recomendación: {recommended['name']}{RESET}")
    print(
        f"{INFO}• Documento: {os.path.basename(doc_path) if doc_path else 'No creado'}{RESET}"
    )

    print(f"\n{INFO}Próximos pasos:{RESET}")
    print(f"{INFO}1. Ejecutar `/workflows:plan` para implementación{RESET}")
    print(f"{INFO}2. Refinar diseño adicional si es necesario{RESET}")
    print(f"{INFO}3. Documentar aprendizajes en el sistema{RESET}")

    print(f"\n{SUCCESS}🎉 Brainstorm listo para la fase de planificación.{RESET}")
    dynamic_speak("Brainstorm completado. Listo para la fase de planificación.")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
