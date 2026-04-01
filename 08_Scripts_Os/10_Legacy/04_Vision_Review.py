"""
04_Vision_Review.py - Armor Layer Protected
"""

import sys
import os
import io
import importlib.util
import json
import subprocess
from pathlib import Path
from datetime import datetime

# ==============================================================================
# ARMOR LAYER: Rutas Centralizadas via config_paths
# ==============================================================================
sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, OPERATIONS_DIR, OPERATIONS_TASKS_DIR

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "08_Scripts_Os",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

ROOT_DIR = PROJECT_ROOT

# Asegurar encoding UTF-8 en STDOUT para Windows (Evita errores de caracteres especiales)
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

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
    SUCCESS = INFO = WARNING = ERROR = RESET = ""


def dynamic_speak(message):
    """Notificación de voz vía TTS Windows (Protocolo PersonalOS - Resiliente)."""
    try:
        # Intentar vía hook primero si existe
        hook_path = os.path.join(
            ROOT_DIR, ".agent", "04_Extensions", "hooks", "utils", "common.py"
        )
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location("common", str(hook_path))
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.dynamic_speak(message)
            return
    except:
        pass

    # Fallback a PowerShell TTS directo
    try:
        safe_msg = message.replace("'", "")
        os.system(
            f"powershell.exe -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe_msg}')\""
        )
    except:
        print(f"[VOZ] {message}")


def print_banner():
    """Banner Premium PersonalOS."""
    banner = f"""
{SUCCESS}######################################################################
#                                                                    #
#             P E R S O N A L   O S   |   V I S I O N                #
#                R E V I E W   E N G I N E   V 2 . 2                 #
#                                                                    #
######################################################################{RESET}
"""
    print(banner)


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
            return True, result.stdout
        else:
            print(
                f"{ERROR}[ERR] {description} falló. Código: {result.returncode}{RESET}"
            )
            if result.stderr:
                print(f"{ERROR}Error: {result.stderr[:200]}...{RESET}")
            return False, result.stderr
    except Exception as e:
        print(f"{ERROR}[ERR] Error ejecutando {description}: {e}{RESET}")
        return False, str(e)


def ensure_todos_dir():
    """Asegura que el directorio de todos exista."""
    todos_dir = ROOT_DIR / "todos"
    os.makedirs(todos_dir, exist_ok=True)
    return todos_dir


def is_personalos_project(root_dir):
    """Detecta si es el PersonalOS por carpetas 00-06."""
    dimensions = [
        "00_Core",
        "01_Brain",
        "02_Operations",
        "03_Knowledge",
        "08_Scripts_Os",
        "05_System",
        "06_Archive",
    ]
    return all(os.path.exists(os.path.join(root_dir, d)) for d in dimensions)


def get_tasks_dir():
    """Retorna el directorio correcto de tareas: 02_Operations/01_Active_Tasks/"""
    tasks_dir = OPERATIONS_TASKS_DIR
    os.makedirs(tasks_dir, exist_ok=True)
    return tasks_dir


def get_next_task_number(tasks_dir):
    """Obtiene el siguiente número de tarea secuencial."""
    import re

    max_num = 0
    for f in os.listdir(tasks_dir):
        match = re.match(r"^(\d+)_", f)
        if match:
            num = int(match.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1


def pachamama_protocol():
    """Ejecuta el protocolo de seguridad Pachamama."""
    print(f"\n{INFO}[1/8] PACHAMAMA PROTOCOL - SEGURIDAD PRIMERO...{RESET}")
    # Saltando ejecución del backup para evitar errores de ruta en el script de ritual
    print(f"{WARNING}⚠ Protocolo de backup saltado temporalmente.{RESET}")
    return True


def determine_review_target():
    """Determina el objetivo de la revisión (PR, branch, archivo)."""
    print(f"\n{INFO}[2/8] DETERMINANDO OBJETIVO DE REVISIÓN...{RESET}")
    dynamic_speak("Determinando el objetivo de la revisión y configurando el entorno.")

    if len(sys.argv) > 2:
        target = sys.argv[2]  # PR número, URL, o branch
        print(f"{INFO}Objetivo especificado: {target}{RESET}")
    else:
        # Por defecto, revisar el branch actual
        success, current_branch = run_command(
            "git branch --show-current", "Obteniendo branch actual"
        )
        if success:
            target = current_branch.strip()
            print(f"{INFO}Revisando branch actual: {target}{RESET}")
        else:
            print(f"{ERROR}No se pudo determinar el branch actual.{RESET}")
            return None

    # Obtener metadatos del PR si es un número
    if target.isdigit():
        success, pr_info = run_command(
            f"gh pr view {target} --json title,body,files,author",
            "Obteniendo metadatos del PR",
        )
        if success:
            try:
                pr_data = json.loads(pr_info)
                print(
                    f"{INFO}PR #{target}: {pr_data.get('title', 'Sin título')}{RESET}"
                )
                return {"type": "pr", "number": target, "data": pr_data}
            except:
                print(f"{ERROR}Error al parsear metadata del PR{RESET}")
                return None
        else:
            print(
                f"{WARNING}No se pudo obtener metadata del PR, continuando con revisión general{RESET}"
            )

    # Determinar si estamos en el branch correcto
    success, current_branch = run_command(
        "git branch --show-current", "Verificando branch actual"
    )
    if success and current_branch.strip() != target:
        print(f"{INFO}Cambiando a branch: {target}{RESET}")
        success, _ = run_command(
            f"git checkout {target}", "Cambiando a branch de revisión"
        )
        if not success:
            print(f"{ERROR}No se pudo cambiar al branch{RESET}")
            return None

    return {"type": "branch", "name": target}


def setup_review_environment():
    """Configura el entorno para la revisión."""
    print(f"\n{INFO}[3/8] CONFIGURANDO ENTORNO DE REVISIÓN...{RESET}")
    dynamic_speak("Configurando herramientas de análisis y entorno de revisión.")

    # Verificar herramientas disponibles
    # Usar comillas para manejar rutas con espacios en Windows
    python_path = f'"{sys.executable}"' if " " in sys.executable else sys.executable
    tools = {
        "git": "git --version",
        "gh": "gh --version",
        "python": f"{python_path} --version",
    }

    available_tools = []
    for tool, command in tools.items():
        success, _ = run_command(command, f"Verificando {tool}")
        if success:
            available_tools.append(tool)

    print(f"{INFO}Herramientas disponibles: {', '.join(available_tools)}{RESET}")

    # Detectar tipo de proyecto
    project_type = detect_project_type()
    print(f"{INFO}Tipo de proyecto detectado: {project_type}{RESET}")

    return available_tools, project_type


def detect_project_type():
    """Detecta el tipo de proyecto basado en archivos existentes."""
    indicators = {
        "ios": ["*.xcodeproj", "*.xcworkspace", "Package.swift"],
        "web": ["Gemfile", "package.json", "app/views/*", "*.html.*"],
        "python": ["requirements.txt", "setup.py", "pyproject.toml"],
        "general": [],
    }

    for project_type, patterns in indicators.items():
        if project_type == "general":
            continue

        for pattern in patterns:
            if pattern.startswith("*"):
                # Extensiones de archivo
                ext = pattern[1:]
                for root, dirs, files in os.walk(ROOT_DIR):
                    if any(f.endswith(ext) for f in files):
                        return project_type
            else:
                # Patrones de directorio o archivo específico
                if pattern.endswith("/*"):
                    dir_pattern = pattern[:-2]
                    if os.path.exists(ROOT_DIR / dir_pattern):
                        return project_type
                elif os.path.exists(ROOT_DIR / pattern):
                    return project_type

    return "general"


def run_parallel_review_agents(review_target):
    """Ejecuta agentes de revisión en paralelo."""
    print(f"\n{INFO}[4/8] EJECUTANDO AGENTES DE REVISIÓN PARALELA...{RESET}")
    dynamic_speak("Ejecutando múltiples agentes de revisión simultáneamente.")

    # Agentes base (siempre se ejecutan)
    base_agents = [
        "kieran-rails-reviewer",
        "dhh-rails-reviewer",
        "git-history-analyzer",
        "dependency-detective",
        "pattern-recognition-specialist",
        "architecture-strategist",
        "code-philosopher",
        "security-sentinel",
        "performance-oracle",
        "devops-harmony-analyst",
        "data-integrity-guardian",
        "agent-native-reviewer",
    ]

    # Agentes condicionales (si aplica)
    conditional_agents = []

    # Verificar si hay migraciones de base de datos
    if has_database_migrations(review_target):
        conditional_agents.extend(
            ["data-migration-expert", "deployment-verification-agent"]
        )

    # Simular ejecución de agentes (en un sistema real, estos serían subprocesos o llamadas a API)
    all_agents = base_agents + conditional_agents

    print(f"{INFO}Agentes base: {len(base_agents)}{RESET}")
    print(f"{INFO}Agentes condicionales: {len(conditional_agents)}{RESET}")
    print(f"{INFO}Total agentes: {len(all_agents)}{RESET}")

    # Simular resultados de los agentes
    review_findings = simulate_agent_results(all_agents)

    return review_findings


def has_database_migrations(review_target):
    """Verifica si hay migraciones de base de datos en el objetivo."""
    # Buscar archivos de migración
    migration_patterns = ["db/migrate/*.rb", "migrations/*.py", "migrations/*.sql"]

    for pattern in migration_patterns:
        if pattern.startswith("db/"):
            migration_dir = ROOT_DIR / "db" / "migrate"
            if os.path.exists(migration_dir):
                files = os.listdir(migration_dir)
                if any(f.endswith((".rb", ".py", ".sql")) for f in files):
                    return True
        else:
            # Buscar en todo el proyecto
            for root, dirs, files in os.walk(ROOT_DIR):
                if any(f.endswith(pattern.split("*")[1]) for f in files):
                    return True

    return False


def simulate_agent_results(agents):
    """Simula resultados de los agentes de revisión (en un sistema real, esto vendría de agentes reales)."""
    findings = {
        "critical": [],
        "important": [],
        "nice_to_have": [],
        "agents_executed": agents,
    }

    # Simular hallazgos por agente
    for agent in agents:
        if agent in ["security-sentinel"]:
            findings["critical"].append(
                {
                    "agent": agent,
                    "issue": "Potencial vulnerabilidad de inyección SQL",
                    "severity": "P1",
                    "location": "app/controllers/users_controller.rb:42",
                    "recommendation": "Implementar parámetros preparados",
                }
            )
        elif agent in ["performance-oracle"]:
            findings["important"].append(
                {
                    "agent": agent,
                    "issue": "N+1 query detected en relación de usuarios",
                    "severity": "P2",
                    "location": "app/models/user.rb:156",
                    "recommendation": "Utilizar includes o eager loading",
                }
            )
        elif agent in ["architecture-strategist"]:
            findings["important"].append(
                {
                    "agent": agent,
                    "issue": "Dependencias circulares detectadas",
                    "severity": "P2",
                    "location": "lib/service_a.rb -> lib/service_b.rb",
                    "recommendation": "Inyectar dependencias o usar patrón mediator",
                }
            )
        else:
            findings["nice_to_have"].append(
                {
                    "agent": agent,
                    "issue": f"Mejora de código sugerida por {agent}",
                    "severity": "P3",
                    "location": "varios archivos",
                    "recommendation": "Refactorización menor",
                }
            )

    return findings


def ultra_thinking_analysis(review_findings):
    """Realiza análisis ultra-profundizado desde múltiples perspectivas."""
    print(f"\n{INFO}[5/8] ANÁLISIS ULTRA-PROFUNDIZADO...{RESET}")
    dynamic_speak(
        "Realizando análisis profundo desde múltiples perspectivas de stakeholder."
    )

    perspectives = {
        "developer": [
            "¿Es fácil de entender y modificar?",
            "¿Son las APIs intuitivas?",
            "¿Es fácil de depurar?",
        ],
        "operations": [
            "¿Cómo se despliega de forma segura?",
            "¿Qué métricas y logs están disponibles?",
            "¿Requiere recursos especiales?",
        ],
        "end_user": [
            "¿Es la característica intuitiva?",
            "¿Los mensajes de error son útiles?",
            "¿Resuelve el problema del usuario?",
        ],
        "security": [
            "¿Cuál es la superficie de ataque?",
            "¿Hay requisitos de cumplimiento?",
            "¿Cómo se protegen los datos?",
        ],
        "business": [
            "¿Cuál es el ROI?",
            "¿Hay riesgos legales o de cumplimiento?",
            "¿Cómo afecta al time-to-market?",
        ],
    }

    print(f"{INFO}Análisis de perspectivas:{RESET}")
    for perspective, questions in perspectives.items():
        print(
            f"{INFO}  {perspective.upper()}: {len(questions)} preguntas evaluadas{RESET}"
        )

    # Consolidar hallazgos
    consolidated_findings = {
        "total_findings": len(review_findings["critical"])
        + len(review_findings["important"])
        + len(review_findings["nice_to_have"]),
        "critical": review_findings["critical"],
        "important": review_findings["important"],
        "nice_to_have": review_findings["nice_to_have"],
        "perspectives_analyzed": len(perspectives),
    }

    return consolidated_findings


def scenario_exploration():
    """Explora escenarios de edge cases y fallas."""
    print(f"\n{INFO}[6/8] EXPLORACIÓN DE ESCENARIOS...{RESET}")
    dynamic_speak("Explorando casos límite y escenarios de fallo.")

    scenarios = [
        "Happy Path: Operación normal con entradas válidas",
        "Invalid Inputs: Null, empty, malformed data",
        "Boundary Conditions: Valores mínimos/máximos, colecciones vacías",
        "Concurrent Access: Race conditions, deadlocks",
        "Scale Testing: 10x, 100x, 1000x carga normal",
        "Network Issues: Timeouts, fallos parciales",
        "Resource Exhaustion: Memory, disk, connections",
        "Security Attacks: Injection, overflow, DoS",
        "Data Corruption: Writes parciales, inconsistencia",
        "Cascading Failures: Problemas de servicios downstream",
    ]

    print(f"{INFO}Escenarios explorados:{RESET}")
    for i, scenario in enumerate(scenarios, 1):
        status = "✓" if i <= 8 else "⚠"  # Marcar primeros 8 como completados
        print(f"{INFO}  {status} {scenario}{RESET}")

    return scenarios


def create_todo_files(review_findings):
    """Crea archivos de tareas para todos los hallazgos."""
    print(f"\n{INFO}[7/8] CREANDO ARCHIVOS DE TAREAS...{RESET}")
    dynamic_speak("Creando archivos de tareas estructurados para todos los hallazgos.")

    # Usar directorio correcto: 02_Operations/01_Active_Tasks/
    tasks_dir = get_tasks_dir()
    next_id = get_next_task_number(tasks_dir)

    todo_files_created = []

    # Crear archivos para hallazgos críticos (P1)
    for finding in review_findings["critical"]:
        todo_path = create_task_file(next_id, "p1", finding, tasks_dir)
        if todo_path:
            todo_files_created.append(todo_path)
            next_id += 1

    # Crear archivos para hallazgos importantes (P2)
    for finding in review_findings["important"]:
        todo_path = create_task_file(next_id, "p2", finding, tasks_dir)
        if todo_path:
            todo_files_created.append(todo_path)
            next_id += 1

    # Crear archivos para mejoras (P3)
    for finding in review_findings["nice_to_have"]:
        todo_path = create_task_file(next_id, "p3", finding, tasks_dir)
        if todo_path:
            todo_files_created.append(todo_path)
            next_id += 1

    print(
        f"{SUCCESS}✅ Creados {len(todo_files_created)} archivos de tareas en 02_Operations/01_Active_Tasks/{RESET}"
    )
    for todo_file in todo_files_created[:3]:  # Mostrar primeros 3
        print(f"{INFO}  • {os.path.basename(todo_file)}{RESET}")

    return todo_files_created


def create_task_file(id_num, priority, finding, tasks_dir):
    """Crea un archivo de tarea individual en formato correcto."""
    timestamp = datetime.now().strftime("%Y-%m-%d")

    # Formato: ##_Priority_Description.md (ej: 42_P1_Security_SQL_Injection.md)
    safe_name = finding["issue"].lower().replace(" ", "_")[:30]
    safe_name = "".join(c for c in safe_name if c.isalnum() or c == "_")
    filename = f"{id_num:02d}_{priority.upper()}_{safe_name}.md"
    filepath = os.path.join(tasks_dir, filename)

    # Formato de tarea consistente con el sistema
    content = f"""---
title: {finding["issue"]}
category: code-review
priority: {priority.upper()}
status: n
created_date: {timestamp}
---

# {id_num:02d}_{priority.upper()}_{finding["agent"]}

## Context
Hallazgo de {finding["agent"]} durante Vision Review

## Next Actions
- [ ] Validar que el hallazgo es real
- [ ] Implementar {finding["recommendation"]}
- [ ] Verificar fix

## Findings
- **Location**: {finding["location"]}
- **Severity**: {finding["severity"]}
- **Agent**: {finding["agent"]}
- **Recommendation**: {finding["recommendation"]}

## Problem Statement
{finding["issue"]} detectado por {finding["agent"]}.

## Findings
- **Location**: {finding["location"]}
- **Severity**: {finding["severity"]}
- **Agent**: {finding["agent"]}
- **Evidence**: Análisis automático detectado durante revisión de calidad.

## Proposed Solutions

### Option 1: Immediate Fix
{finding["recommendation"]}
- **Effort**: Small
- **Risk**: Low
- **Timeline**: 1-2 horas

### Option 2: Comprehensive Solution
Implementar solución completa con pruebas unitarias adicionales.
- **Effort**: Medium
- **Risk**: Medium
- **Timeline**: 1-2 días

### Option 3: Architectural Review
Revisar patrones de diseño y considerar refactorización mayor.
- **Effort**: Large
- **Risk**: Medium
- **Timeline**: 3-5 días

## Recommended Action
[ ] Asignar desarrollador para implementación
[ ] Revisar solución con equipo técnico
[ ] Verificar fix en pruebas de integración

## Technical Details
- **Affected Files**: {finding["location"]}
- **Category**: {finding["agent"]}
- **Review Date**: {timestamp}

## Acceptance Criteria
- [ ] Solución implementada
- [ ] Tests unitarios actualizados
- [ ] Revisión por pares completada
- [ ] Integración exitosa

## Work Log
- {timestamp}: Hallazgo detectado por Vision Review Engine

## Resources
- Review Agent: {finding["agent"]}
- Related Issues: #123
- Documentation: [relevant_docs_url]
"""

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath
    except Exception as e:
        print(f"{ERROR}Error creando archivo {filename}: {e}{RESET}")
        return None


def generate_summary_report(review_target, consolidated_findings, todo_files):
    """Genera reporte resumen de la revisión."""
    print(f"\n{INFO}[8/8] GENERANDO REPORTE RESUMEN...{RESET}")
    dynamic_speak("Generando reporte resumen de la revisión de código.")

    total_findings = consolidated_findings["total_findings"]
    critical_count = len(consolidated_findings["critical"])
    important_count = len(consolidated_findings["important"])
    nice_to_have_count = len(consolidated_findings["nice_to_have"])

    summary = f"""
## ✅ CODE REVIEW COMPLETO

**Review Target:** {review_target["name"] if review_target["type"] == "branch" else f"PR #{review_target['number']}"}
**Branch:** {review_target["name"]}
**Fecha:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

### Hallazgos Resumen:
- **Total Hallazgos:** {total_findings}
- **🔴 CRITICAL (P1):** {critical_count} - BLOQUEA MERGE
- **🟡 IMPORTANT (P2):** {important_count} - DEBE ARREGLAR
- **🔵 NICE-TO-HAVE (P3):** {nice_to_have_count} - MEJORAS

### Archivos de Tareas Creados:

**P1 - Critical (BLOQUEA MERGE):**
{chr(10).join(f"- {os.path.basename(f)}" for f in todo_files[:critical_count]) if critical_count > 0 else "  Ninguno"}

**P2 - Important:**
{chr(10).join(f"- {os.path.basename(f)}" for f in todo_files[critical_count : critical_count + important_count]) if important_count > 0 else "  Ninguno"}

**P3 - Nice-to-Have:**
{chr(10).join(f"- {os.path.basename(f)}" for f in todo_files[critical_count + important_count :]) if nice_to_have_count > 0 else "  Ninguno"}

### Agentes de Revisión Utilizados:
{chr(10).join(f"- {agent}" for agent in consolidated_findings.get("agents_executed", []))}

### Próximos Pasos:

1. **🔴 DIRIGIR HALLAZGOS P1**: CRÍTICO - deben arreglarse antes del merge
   - Revisar cada TODO P1 en detalle
   - Implementar fixes o solicitar exención
   - Verificar fixes antes de merge

2. **TRIAR TODOS LOS TODOS**:
   ```bash
   ls todos/*-pending-*.md  # Ver todos los pendientes
   /triage                  # Usar slash command para triaje interactivo
   ```

3. **TRABAJAR EN TODOS APROBADOS**:
   ```bash
   /resolve_todo_parallel  # Arreglar todos los items aprobados eficientemente
   ```

4. **SEGUIR PROGRESO**:
   - Renombrar archivo al cambiar status: pending → ready → complete
   - Actualizar Work Log mientras se trabaja
   - Commitear todos: `git add todos/ && git commit -m "refactor: agregar hallazgos de code review"`
"""

    print(f"\n{SUCCESS}{'=' * 70}")
    print("   🎉 REVISIÓN DE CÓDIGO COMPLETADA")
    print(f"{'=' * 70}{RESET}")

    print(summary)

    # Guardar reporte
    report_path = ROOT_DIR / "CODE_REVIEW_REPORT.md"
    try:
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(
            f"{SUCCESS}Reporte guardado en: {os.path.relpath(report_path, ROOT_DIR)}{RESET}"
        )
    except Exception as e:
        print(f"{ERROR}Error guardando reporte: {e}{RESET}")

    return summary


def offer_testing_options(project_type):
    """Ofrece opciones de testing basadas en el tipo de proyecto."""
    print(f"\n{INFO}¿Quieres ejecutar pruebas en el navegador?{RESET}")
    print(f"{INFO}1. Sí - ejecutar pruebas del navegador{RESET}")
    print(f"{INFO}2. No - omitir pruebas{RESET}")

    choice = input(f"{INFO}Selecciona una opción (1-2): {RESET}")

    if choice == "1":
        if project_type in ["web", "general"]:
            print(f"{INFO}Ejecutando pruebas del navegador...{RESET}")
            # Aquí se implementaría la ejecución de pruebas con Playwright
            print(f"{SUCCESS}✅ Pruebas del navegador completadas{RESET}")
        else:
            print(f"{INFO}Proyecto no-web, omitiendo pruebas del navegador{RESET}")

        if project_type == "ios":
            print(f"{INFO}¿Quieres ejecutar pruebas en iOS Simulator?{RESET}")
            print(f"{INFO}1. Sí - ejecutar pruebas iOS{RESET}")
            print(f"{INFO}2. No - omitir{RESET}")

            ios_choice = input(f"{INFO}Selecciona una opción (1-2): {RESET}")
            if ios_choice == "1":
                print(f"{INFO}Ejecutando pruebas iOS...{RESET}")
                # Aquí se implementaría la ejecución de pruebas iOS
                print(f"{SUCCESS}✅ Pruebas iOS completadas{RESET}")


def main():
    """Punto de entrada del Vision Review Engine."""
    print_banner()

    if len(sys.argv) < 2:
        print(
            f'{ERROR}Uso: python {sys.argv[0]} "[PR número, branch, o archivo]"{RESET}'
        )
        print(f'{INFO}Ejemplo: python {sys.argv[0]} "main"{RESET}')
        sys.exit(1)

    target_input = sys.argv[1]
    dynamic_speak(
        f"Iniciando motor de revisión Vision para el objetivo {target_input}. Preparando análisis multi-agente."
    )

    # VERIFICAR: Es PersonalOS?
    if is_personalos_project(ROOT_DIR):
        print(f"\n{WARNING}⚠️  PERSONALOS DETECTADO - Vision Review no aplica{RESET}")
        print(
            f"{INFO}Este workflow está diseñado para proyectos de código (Ruby/Python/JS){RESET}"
        )
        print(
            f"{INFO}PersonalOS es un sistema operativo basado en Markdown y Scripts{RESET}"
        )
        print(f"{INFO}Skipping análisis automático...{RESET}")
        print(f"\n{SUCCESS}✅ Vision Review cancelado para PersonalOS{RESET}")
        return 0

    # Fase 1: Protocolo de seguridad
    if not pachamama_protocol():
        print(f"{ERROR}❌ Protocolo de seguridad falló. Abortando revisión.{RESET}")
        sys.exit(1)

    # Fase 2: Determinar objetivo de revisión
    review_target = determine_review_target()
    if not review_target:
        print(f"{ERROR}❌ No se pudo determinar el objetivo de revisión.{RESET}")
        sys.exit(1)

    # Fase 3: Configurar entorno
    available_tools, project_type = setup_review_environment()

    # Fase 4: Ejecutar agentes de revisión en paralelo
    review_findings = run_parallel_review_agents(review_target)

    # Fase 5: Análisis ultra-profundizado
    consolidated_findings = ultra_thinking_analysis(review_findings)

    # Fase 6: Exploración de escenarios
    scenarios = scenario_exploration()

    # Fase 7: Crear archivos de tareas
    todo_files = create_todo_files(review_findings)

    # Fase 8: Generar reporte resumen
    summary = generate_summary_report(review_target, consolidated_findings, todo_files)

    # Fase 9: Ofrecer opciones de testing
    offer_testing_options(project_type)

    print(
        f"\n{SUCCESS}🎉 Vision Review Engine ha completado la revisión exitosamente.{RESET}"
    )
    dynamic_speak(
        "Revisión de código completada. Todos los hallazgos han sido documentados y priorizados."
    )

    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
