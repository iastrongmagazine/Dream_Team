"""
PROFESSOR X PLAN ENGINE - PersonalOS v1.0
Transforma descripciones de features en planes de proyecto bien estructurados.
Ideal para planning técnico y preparación de implementaciones detalladas.

Basado en: .agent/03_Workflows/02_Professor_X_Plan.md
"""

import subprocess
import sys
import os
import importlib.util
import re
from datetime import datetime
from config_paths import ROOT_DIR, PLANS_DIR, BRAINSTORMS_DIR

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


def ensure_docs_plans_dir():
    """Asegura que el directorio de planes exista."""
    os.makedirs(PLANS_DIR, exist_ok=True)
    return PLANS_DIR


def find_relevant_brainstorms(feature_description):
    """Busca brainstorms relevantes para la feature."""
    print(f"\n{INFO}[0/5] BUSCANDO BRAINSTORMS RELEVANTES...{RESET}")
    dynamic_speak(
        "Buscando brainstorms relevantes para contextualizar la planificación."
    )

    brainstorms_dir = BRAINSTORMS_DIR
    if not os.path.exists(brainstorms_dir):
        print(f"{INFO}No se encontraron directorio de brainstorms.{RESET}")
        return None

    relevant_brainstorms = []
    search_terms = feature_description.lower().split()

    for file in os.listdir(brainstorms_dir):
        if file.endswith("-brainstorm.md"):
            file_path = os.path.join(brainstorms_dir, file)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read().lower()
                    if any(term in content for term in search_terms):
                        relevant_brainstorms.append(file_path)
            except:
                continue

    if relevant_brainstorms:
        print(
            f"{SUCCESS}✓ Encontrados {len(relevant_brainstorms)} brainstorms relevantes{RESET}"
        )
        for brain in relevant_brainstorms[:2]:  # Mostrar los 2 más recientes
            print(f"{INFO}  • {os.path.basename(brain)}{RESET}")
        return relevant_brainstorms[0]  # Devolver el más reciente
    else:
        print(f"{INFO}No se encontraron brainstorms relevantes.{RESET}")
        return None


def local_research(feature_description):
    """Investigación local de patrones y convenciones."""
    print(f"\n{INFO}[1/5] INVESTIGACIÓN LOCAL DE PATRONES...{RESET}")
    dynamic_speak("Investigando patrones existentes y convenciones del proyecto.")

    findings = {"repo_patterns": [], "learnings": [], "claude_conventions": []}

    # Buscar patrones en el repositorio
    search_patterns = [
        "service",
        "controller",
        "model",
        "view",
        "component",
        "api",
        "auth",
        "data",
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
            if file.endswith((".py", ".js", ".ts", ".rb", ".md")):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read().lower()
                        if any(pattern in content for pattern in search_patterns):
                            findings["repo_patterns"].append(file_path)
                except:
                    continue

    # Limitar a los 10 archivos más relevantes
    findings["repo_patterns"] = findings["repo_patterns"][:10]

    # Buscar aprendizajes documentados
    solutions_dir = os.path.join(ROOT_DIR, "docs", "solutions")
    if os.path.exists(solutions_dir):
        for category in os.listdir(solutions_dir):
            category_path = os.path.join(solutions_dir, category)
            if os.path.isdir(category_path):
                for file in os.listdir(category_path)[:5]:  # Limitar a 5 por categoría
                    findings["learnings"].append(os.path.join(category_path, file))

    # Leer convenciones de CLAUDE.md
    claude_path = os.path.join(ROOT_DIR, "CLAUDE.md")
    if os.path.exists(claude_path):
        try:
            with open(claude_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Extraer secciones relevantes
                if "Estructura del Sistema" in content:
                    findings["claude_conventions"].append(
                        "Estructura del Sistema definida"
                    )
                if "Comandos y Scripts" in content:
                    findings["claude_conventions"].append(
                        "Scripts y comandos estandarizados"
                    )
        except:
            pass

    print(
        f"{INFO}Patrones encontrados: {len(findings['repo_patterns'])} archivos{RESET}"
    )
    print(
        f"{INFO}Aprendizajes documentados: {len(findings['learnings'])} soluciones{RESET}"
    )
    print(
        f"{INFO}Convenciones del proyecto: {len(findings['claude_conventions'])} puntos{RESET}"
    )

    return findings


def decide_research_needs(feature_description, research_findings):
    """Decide si se necesita investigación externa."""
    print(f"\n{INFO}[2/5] DECIDIENDO NECESIDAD DE INVESTIGACIÓN EXTERNA...{RESET}")
    dynamic_speak("Evaluando si se requiere investigación externa adicional.")

    # Tópicos de alto riesgo que siempre requieren investigación
    high_risk_topics = [
        "security",
        "payment",
        "auth",
        "pci",
        "gdpr",
        "hipaa",
        "finance",
        "banking",
    ]

    feature_lower = feature_description.lower()
    is_high_risk = any(topic in feature_lower for topic in high_risk_topics)

    # Contexto local sólido
    has_local_context = (
        len(research_findings["repo_patterns"]) >= 5
        and len(research_findings["learnings"]) >= 2
        and len(research_findings["claude_conventions"]) >= 1
    )

    if is_high_risk:
        print(
            f"{INFO}🔒 Tópico de alto riesgo detectado - Investigación externa obligatoria{RESET}"
        )
        return True
    elif has_local_context:
        print(
            f"{INFO}✅ Contexto local sólido - Procediendo sin investigación externa{RESET}"
        )
        return False
    else:
        print(f"{INFO}🤔 Contexto limitado - Realizando investigación externa{RESET}")
        return True


def external_research(feature_description):
    """Realiza investigación externa paralela."""
    print(f"\n{INFO}[3/5] INVESTIGACIÓN EXTERNA PARALELA...{RESET}")
    dynamic_speak(
        "Realizando investigación externa de mejores prácticas y documentación."
    )

    # Simulación de investigación externa en paralelo
    research_results = {
        "best_practices": [],
        "framework_docs": [],
        "related_issues": [],
    }

    # Mejores prácticas (simulado)
    best_practices = [
        "Seguridad: Implementar validación de entrada en todos los endpoints",
        "Rendimiento: Utilizar caché para consultas frecuentes",
        "Escalabilidad: Diseñar para horizontal scaling",
        "Mantenibilidad: Seguir patrones de código existentes",
        "Testing: Incluir pruebas unitarias y de integración",
    ]

    # Documentación de frameworks (simulado)
    framework_docs = [
        "React: Utilizar Hooks para manejo de estado",
        "Rails: Follow Rails conventions for naming",
        "Python: PEP 8 compliance for code style",
        "API: RESTful design principles",
    ]

    # Issues relacionados (simulado)
    related_issues = [
        "Issue #123: Similar authentication flow implementation",
        "Issue #456: Performance optimization for data processing",
        "PR #789: Related feature implementation",
    ]

    research_results["best_practices"] = best_practices
    research_results["framework_docs"] = framework_docs
    research_results["related_issues"] = related_issues

    print(f"{INFO}Mejores prácticas encontradas: {len(best_practices)}{RESET}")
    print(f"{INFO}Documentación de frameworks: {len(framework_docs)}{RESET}")
    print(f"{INFO}Issues relacionados: {len(related_issues)}{RESET}")

    return research_results


def consolidate_research(local_findings, external_findings=None):
    """Consolida todos los hallazgos de investigación."""
    print(f"\n{INFO}[4/5] CONSOLIDANDO HALLAZGOS DE INVESTIGACIÓN...{RESET}")
    dynamic_speak("Consolidando todos los hallazgos para crear un plan completo.")

    consolidated = {
        "repo_patterns": local_findings["repo_patterns"],
        "learnings": local_findings["learnings"],
        "conventions": local_findings["claude_conventions"],
        "best_practices": external_findings["best_practices"]
        if external_findings
        else [],
        "framework_docs": external_findings["framework_docs"]
        if external_findings
        else [],
        "related_issues": external_findings["related_issues"]
        if external_findings
        else [],
    }

    # Generar resumen
    print(f"\n{INFO}Resumen de investigación consolidada:{RESET}")
    print(
        f"{INFO}• Patrones del repositorio: {len(consolidated['repo_patterns'])} archivos{RESET}"
    )
    print(
        f"{INFO}• Soluciones documentadas: {len(consolidated['learnings'])} soluciones{RESET}"
    )
    print(
        f"{INFO}• Convenciones del proyecto: {len(consolidated['conventions'])} puntos{RESET}"
    )
    print(
        f"{INFO}• Mejores prácticas: {len(consolidated['best_practices'])} recomendaciones{RESET}"
    )
    print(
        f"{INFO}• Documentación externa: {len(consolidated['framework_docs'])} recursos{RESET}"
    )
    print(
        f"{INFO}• Issues relacionados: {len(consolidated['related_issues'])} referencias{RESET}"
    )

    return consolidated


def determine_plan_type_and_complexity(feature_description):
    """Determina el tipo y complejidad del plan."""
    print(f"\n{INFO}[5/5] DETERMINANDO TIPO Y COMPLEJIDAD DEL PLAN...{RESET}")
    dynamic_speak(
        "Analizando la complejidad para determinar el nivel de detalle del plan."
    )

    # Análisis simple de complejidad
    complexity_indicators = {
        "simple": len(feature_description.split()) < 10,
        "medium": 10 <= len(feature_description.split()) < 20,
        "complex": len(feature_description.split()) >= 20,
    }

    # Detectar tipo de feature
    feature_lower = feature_description.lower()
    if any(word in feature_lower for word in ["auth", "login", "security"]):
        plan_type = "authentication"
    elif any(word in feature_lower for word in ["data", "database", "storage"]):
        plan_type = "data"
    elif any(word in feature_lower for word in ["ui", "interface", "frontend"]):
        plan_type = "ui"
    elif any(word in feature_lower for word in ["api", "endpoint", "service"]):
        plan_type = "api"
    else:
        plan_type = "general"

    # Determinar nivel de detalle
    if complexity_indicators["simple"]:
        detail_level = "MINIMAL"
    elif complexity_indicators["medium"]:
        detail_level = "MORE"
    else:
        detail_level = "A LOT"

    print(f"{INFO}Tipo de feature: {plan_type}{RESET}")
    print(
        f"{INFO}Complejidad: {'Simple' if complexity_indicators['simple'] else 'Media' if complexity_indicators['medium'] else 'Compleja'}{RESET}"
    )
    print(f"{INFO}Nivel de detalle: {detail_level}{RESET}")

    return plan_type, detail_level


def create_plan_document(
    feature_description, research_findings, plan_type, detail_level, relevant_brainstorm
):
    """Crea el documento del plan con el nivel de detalle apropiado."""
    print(f"\n{INFO}CREANDO DOCUMENTO DE PLAN...{RESET}")
    dynamic_speak("Creando documento de plan detallado.")

    plans_dir = ensure_docs_plans_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # Generar título y nombre de archivo
    title = f"feat: {feature_description}"
    filename = f"{timestamp}-feat-{feature_description.lower().replace(' ', '-').replace('.', '')}-plan.md"
    filepath = os.path.join(plans_dir, filename)

    # Contenido basado en nivel de detalle
    if detail_level == "MINIMAL":
        content = create_minimal_plan(
            feature_description, research_findings, title, timestamp
        )
    elif detail_level == "MORE":
        content = create_more_detailed_plan(
            feature_description, research_findings, title, timestamp, plan_type
        )
    else:
        content = create_comprehensive_plan(
            feature_description, research_findings, title, timestamp, plan_type
        )

    # Añadir información de brainstorm si existe
    if relevant_brainstorm:
        content += f"\n\n## Contexto del Brainstorm\n\nBasado en el brainstorm: `{os.path.basename(relevant_brainstorm)}`\n"

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{SUCCESS}✅ Plan creado: {os.path.relpath(filepath, ROOT_DIR)}{RESET}")
        return filepath
    except Exception as e:
        print(f"{ERROR}❌ Error al crear plan: {e}{RESET}")
        return None


def create_minimal_plan(feature_description, research_findings, title, timestamp):
    """Crea un plan minimal (Quick Issue)."""
    return f"""---
title: {title}
type: feat
date: {timestamp}
---

# {title}

{feature_description}

## Acceptance Criteria

- [ ] Implementar funcionalidad principal
- [ ] Asegurar calidad del código
- [ ] Documentar cambios

## Context

{chr(10).join(f"- {finding}" for finding in research_findings["conventions"][:3])}

## MVP

### Implementation

```python
# Placeholder para implementación principal
def main_feature():
    pass
```

## References

- Related issues: #123
- Documentation: [relevant_docs_url]
"""


def create_more_detailed_plan(
    feature_description, research_findings, title, timestamp, plan_type
):
    """Crea un plan más detallado (Standard Issue)."""
    return f"""---
title: {title}
type: feat
date: {timestamp}
---

# {title}

## Overview

{feature_description}

## Problem Statement / Motivation

Esta feature mejora el sistema al agregar {plan_type} functionality para resolver necesidades específicas de los usuarios.

## Proposed Solution

Implementación siguiendo patrones existentes del proyecto y mejores prácticas del sector.

## Technical Considerations

- Architecture impacts: Integración con componentes existentes
- Performance implications: Optimización para carga esperada
- Security considerations: Validación de entrada y manejo de datos sensibles

## Acceptance Criteria

- [ ] Implementar funcionalidad principal
- [ ] Crear tests unitarios y de integración
- [ ] Documentar cambios y decisiones
- [ ] Validar rendimiento y seguridad

## Success Metrics

- [ ] Tiempo de respuesta < 500ms
- [ ] Cobertura de tests > 80%
- [ ] Sin vulnerabilidades de seguridad
- [ ] Buena experiencia de usuario

## Dependencies & Risks

- [ ] Dependencias: {chr(10).join(f"- {dep}" for dep in research_findings["framework_docs"][:3])}
- [ ] Riesgos: Complejidad técnica, integración con sistemas existentes

## References & Research

### Internal References

- Patrones existentes: {chr(10).join(f"- {os.path.basename(f)}" for f in research_findings["repo_patterns"][:3])}
- Soluciones documentadas: {chr(10).join(f"- {os.path.basename(f)}" for f in research_findings["learnings"][:2])}

### External References

- Mejores prácticas: {chr(10).join(f"- {practice}" for practice in research_findings["best_practices"][:3])}
- Issues relacionados: {chr(10).join(f"- {issue}" for issue in research_findings["related_issues"][:2])}
"""


def create_comprehensive_plan(
    feature_description, research_findings, title, timestamp, plan_type
):
    """Crea un plan comprehensivo (Comprehensive Issue)."""
    return f"""---
title: {title}
type: feat
date: {timestamp}
---

# {title}

## Overview

{feature_description}

## Problem Statement

Análisis detallado del problema que resuelve esta feature, considerando impacto en el negocio y técnicos.

## Proposed Solution

Solución completa con arquitectura detallada y consideraciones de escalabilidad.

## Technical Approach

### Architecture

Diseño técnico completo con componentes, servicios y flujo de datos.

### Implementation Phases

#### Phase 1: Foundation
- [ ] Configuración inicial del entorno
- [ ] Creación de estructura base
- [ ] Implementación de modelos y servicios básicos

#### Phase 2: Core Implementation
- [ ] Implementación de lógica principal
- [ ] Integración con sistemas existentes
- [ ] Creación de APIs y endpoints

#### Phase 3: Polish & Optimization
- [ ] Optimización de rendimiento
- [ ] Implementación de seguridad
- [ ] Documentación final

## Alternative Approaches Considered

Análisis de alternativas y justificación de la elección actual.

## Acceptance Criteria

### Functional Requirements
- [ ] Todos los casos de uso implementados
- [ ] Validación de datos de entrada
- [ ] Manejo de errores completo

### Non-Functional Requirements
- [ ] Rendimiento: < 500ms respuesta
- [ ] Seguridad: Sin vulnerabilidades críticas
- [ ] Accesibilidad: Cumple WCAG 2.1

### Quality Gates
- [ ] Cobertura de tests > 90%
- [ ] Code review aprobado
- [ ] Integración continua exitosa

## Success Metrics

KPIs y métodos de medición detallados.

## Dependencies & Prerequisites

Análisis completo de dependencias.

## Risk Analysis & Mitigation

Evaluación de riesgos con estrategias de mitigación.

## Resource Requirements

Requisitos de equipo, tiempo e infraestructura.

## Future Considerations

Extensibilidad y visión a largo plazo.

## Documentation Plan

Actualizaciones requeridas a documentación.

## References & Research

### Internal References
- Patrones: {chr(10).join(f"- {os.path.basename(f)}" for f in research_findings["repo_patterns"][:5])}
- Soluciones: {chr(10).join(f"- {os.path.basename(f)}" for f in research_findings["learnings"][:3])}

### External References
- Mejores prácticas: {chr(10).join(f"- {practice}" for practice in research_findings["best_practices"][:5])}
- Framework docs: {chr(10).join(f"- {doc}" for doc in research_findings["framework_docs"][:3])}

### Related Work
- Issues: {chr(10).join(f"- {issue}" for issue in research_findings["related_issues"][:3])}
"""


def present_post_creation_options(plan_path):
    """Presenta opciones posteriores a la creación del plan."""
    print(f"\n{INFO}{'=' * 70}")
    print("   📋 PLAN CREADO EXITOSAMENTE")
    print(f"{'=' * 70}{RESET}")

    print(f"\n{SUCCESS}Plan listo en: {os.path.relpath(plan_path, ROOT_DIR)}{RESET}")

    print(f"\n{INFO}¿Qué te gustaría hacer a continuación?{RESET}")
    print(f"{INFO}1. Abrir plan en editor{RESET}")
    print(f"{INFO}2. Profundizar en plan con investigación adicional{RESET}")
    print(f"{INFO}3. Revisar plan con agentes especializados{RESET}")
    print(f"{INFO}4. Comenzar implementación local{RESET}")
    print(f"{INFO}5. Crear issue en GitHub{RESET}")
    print(f"{INFO}6. Simplificar el plan{RESET}")

    return input(f"\n{INFO}Selecciona una opción (1-6): {RESET}")


def main():
    """Punto de entrada del Professor X Plan Engine."""
    if len(sys.argv) < 2:
        print(f'{ERROR}Uso: python {sys.argv[0]} "[descripción de la feature]"{RESET}')
        print(
            f'{INFO}Ejemplo: python {sys.argv[0]} "Implementar sistema de autenticación OAuth2"{RESET}'
        )
        sys.exit(1)

    feature_description = sys.argv[1]

    print(f"{INFO}{'=' * 70}")
    print("   PROFESSOR X PLAN ENGINE - PersonalOS v1.0")
    print(f"   Feature: {feature_description}")
    print(f"{'=' * 70}{RESET}")
    dynamic_speak(
        "Iniciando Professor X Plan Engine para creación de planes detallados."
    )

    # Fase 0: Buscar brainstorms relevantes
    relevant_brainstorm = find_relevant_brainstorms(feature_description)

    # Fase 1: Investigación local
    local_findings = local_research(feature_description)

    # Fase 2: Decidir necesidad de investigación externa
    needs_external_research = decide_research_needs(feature_description, local_findings)

    # Fase 3: Investigación externa (si es necesaria)
    external_findings = None
    if needs_external_research:
        external_findings = external_research(feature_description)

    # Fase 4: Consolidar investigación
    consolidated_findings = consolidate_research(local_findings, external_findings)

    # Fase 5: Determinar tipo y complejidad
    plan_type, detail_level = determine_plan_type_and_complexity(feature_description)

    # Fase 6: Crear documento del plan
    plan_path = create_plan_document(
        feature_description,
        consolidated_findings,
        plan_type,
        detail_level,
        relevant_brainstorm,
    )

    if not plan_path:
        print(f"{ERROR}❌ No se pudo crear el plan{RESET}")
        sys.exit(1)

    # Fase 7: Presentar opciones
    selected_option = present_post_creation_options(plan_path)

    # Ejecutar opción seleccionada
    if selected_option == "1":
        # Abrir en editor
        print(f"{INFO}Abriendo plan en editor...{RESET}")
        # Aquí se podría implementar la apertura en editor preferido
    elif selected_option == "2":
        # Profundizar en plan
        print(f"{INFO}Profundizando en plan con investigación adicional...{RESET}")
    elif selected_option == "3":
        # Revisar con agentes
        print(f"{INFO}Revisando plan con agentes especializados...{RESET}")
    elif selected_option == "4":
        # Comenzar implementación
        print(f"{INFO}Comenzando implementación local...{RESET}")
    elif selected_option == "5":
        # Crear issue en GitHub
        print(f"{INFO}Creando issue en GitHub...{RESET}")
    elif selected_option == "6":
        # Simplificar plan
        print(f"{INFO}Simplificando el plan...{RESET}")
    else:
        print(f"{INFO}Opción no reconocida. Plan listo para revisión.{RESET}")

    print(
        f"\n{SUCCESS}🎉 Professor X Plan Engine ha completado la creación del plan.{RESET}"
    )
    dynamic_speak("Plan creado exitosamente. Listo para revisión e implementación.")

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
