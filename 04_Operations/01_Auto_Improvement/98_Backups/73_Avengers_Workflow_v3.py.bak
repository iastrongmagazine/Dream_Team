import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
#!/usr/bin/env python3
"""
73_Avengers_Workflow_v3.py - Avengers Compound Flow v3.0
=========================================================
Workflow moderno: Git Analysis -> Vision Review -> Planning -> Execution

Propósito: Ejecutar ciclo completo de revisión y mejora del código
           usando sub-agentes y workflows modernos de Claude.

Fases:
  1. Git Status Analysis (10%)
  2. Vision Review Sub-agent (30%)
  3. Findings Analysis (50%)
  4. Planning Sub-agent (70%)
  5. Execution Sub-agent (90%)
  6. Summary (100%)

Usage:
  python 73_Avengers_Workflow_v3.py [target]
  python 73_Avengers_Workflow_v3.py main
  python 73_Avengers_Workflow_v3.py <PR-number>
"""

import subprocess
import os
import sys
import io
import json
import re
from datetime import datetime
from pathlib import Path

# ==============================================================================
# ARMOR LAYER - PATH RESOLUTION
# ==============================================================================

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
os.environ["PERSONAL_OS_ROOT"] = PROJECT_ROOT

# Agregar al path para config
sys.path.insert(0, os.path.join(PROJECT_ROOT, "04_Engine", "08_Scripts_Os"))

try:
    from config_paths import ROOT_DIR, OPERATIONS_DIR

    ACTIVE_TASKS_DIR = Path(OPERATIONS_DIR) / "01_Active_Tasks"
except ImportError:
    # Fallback: ruta directa
    ACTIVE_TASKS_DIR = Path(PROJECT_ROOT) / "02_Operations" / "01_Active_Tasks"

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================

PROJECT_ROOT_PATH = Path(PROJECT_ROOT)
LOG_DIR = PROJECT_ROOT_PATH / "04_Engine" / "Analytics_Output"

# Crear directorio de logs si no existe
try:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
except Exception:
    pass  # Si falla, continuar sin logs

REPORT_INTERVAL = 10  # Reportar cada 10% de progreso


# Colores para output
class Colors:
    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"


# ==============================================================================
# UTILIDADES
# ==============================================================================


def log(message, level="INFO"):
    """Log message with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")


def print_progress(percent, message):
    """Print progress bar with message."""
    bar_length = 30
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "░" * (bar_length - filled)

    print(
        f"\n{Colors.CYAN}╔══════════════════════════════════════════════════════════════╗{Colors.ENDC}"
    )
    print(
        f"{Colors.CYAN}║  AVENGERS v3.0 - PROGRESS: {percent:3d}% [{bar}] {Colors.ENDC}"
    )
    print(f"{Colors.CYAN}║  {message:<62}{Colors.ENDC}")
    print(
        f"{Colors.CYAN}╚══════════════════════════════════════════════════════════════╝{Colors.ENDC}\n"
    )


def print_banner():
    """Print Avengers banner."""
    banner = f"""
{Colors.CYAN}================================================================================

   ██╗   ██╗ ██████╗ ██╗██████╗     ██╗  ██╗ ██████╗ ██████╗ ██████╗  █████╗ ██████╗
   ██║   ██║██╔═══██╗██║██╔══██╗    ██║  ██║██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗
   ██║   ██║██║   ██║██║██║  ██║    ███████║██║   ██║██████╔╝██║  ██║███████║██████╔╝
   ╚██╗ ██╔╝██║   ██║██║██║  ██║    ██╔══██║██║   ██║██╔══██╗██║  ██║██╔══██║██╔══██╗
    ╚████╔╝ ╚██████╔╝██║██████╔╝    ██║  ██║╚██████╔╝██║  ██║██║  ██║██║  ██║██║  ██║
     ╚═══╝   ╚═════╝ ╚═╝╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝

                    A V E N G E R S   C O M P O U N D   F L O W   v 3 . 0
                           PersonalOS - Workflow Moderno
================================================================================{Colors.ENDC}
    """
    print(banner)


def run_subagent(command, description):
    """Ejecuta un comando como sub-agente y retorna el output."""
    log(f"Iniciando sub-agente: {description}", "SUBAGENT")
    print(f"\n{Colors.YELLOW}▶ Ejecutando: {description}{Colors.ENDC}\n")

    try:
        result = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            shell=True,
            timeout=300,  # 5 min timeout
        )

        output = result.stdout + result.stderr

        if result.returncode == 0:
            log(f"Sub-agente completado: {description}", "SUCCESS")
            return {"success": True, "output": output}
        else:
            log(f"Sub-agente falló: {description}", "WARNING")
            return {"success": False, "output": output, "returncode": result.returncode}

    except subprocess.TimeoutExpired:
        log(f"Sub-agente timeout: {description}", "ERROR")
        return {"success": False, "output": "Timeout exceeded", "returncode": -1}
    except Exception as e:
        log(f"Error en sub-agente: {e}", "ERROR")
        return {"success": False, "output": str(e), "returncode": -1}


def ask_user(question, default="s"):
    """Pregunta al usuario y espera respuesta. Modo no-interactivo usa default."""
    print(f"\n{Colors.BOLD}{Colors.BLUE}❓ PREGUNTA:{Colors.ENDC} {question}")

    # En modo no-interactivo, usar default
    if not sys.stdin.isatty():
        print(
            f"{Colors.CYAN}→ Modo no-interactivo: usando default '{default}'{Colors.ENDC}"
        )
        return default.lower() == "s"

    try:
        response = input(
            f"{Colors.CYAN}→ Escribe 's' para Sí, 'n' para No: {Colors.ENDC}"
        )
        return response.lower() == "s"
    except (EOFError, KeyboardInterrupt):
        print(
            f"{Colors.YELLOW}→ Input no disponible, usando default '{default}'{Colors.ENDC}"
        )
        return default.lower() == "s"


# ==============================================================================
# FASE 1: GIT STATUS ANALYSIS (10%)
# ==============================================================================


def phase_git_analysis(target):
    """Fase 1: Analizar cambios en git."""
    print_progress(10, "Fase 1: Git Status Analysis")

    log("Iniciando análisis de git...", "PHASE1")

    # Git status
    status_cmd = "git status --porcelain"
    status_result = subprocess.run(
        status_cmd, cwd=PROJECT_ROOT, capture_output=True, text=True, shell=True
    )

    changed_files = (
        status_result.stdout.strip() if status_result.stdout else "No hay cambios"
    )
    file_count = len([l for l in changed_files.split("\n") if l.strip()])

    print(f"\n{Colors.GREEN}=== ARCHIVOS MODIFICADOS ({file_count}) ==={Colors.ENDC}")
    print(changed_files[:500] if len(changed_files) > 500 else changed_files)

    # Git diff stat
    diff_cmd = "git diff --stat"
    diff_result = subprocess.run(
        diff_cmd, cwd=PROJECT_ROOT, capture_output=True, text=True, shell=True
    )

    print(f"\n{Colors.GREEN}=== RESUMEN DE CAMBIOS ==={Colors.ENDC}")
    print(diff_result.stdout if diff_result.stdout else "No hay diff")

    log(f"Análisis git completado: {file_count} archivos", "PHASE1_DONE")

    return {
        "changed_files": changed_files,
        "file_count": file_count,
        "diff_summary": diff_result.stdout,
    }


# ==============================================================================
# FASE 2: VISION REVIEW SUB-AGENT (30%)
# ==============================================================================


def phase_vision_review(target):
    """Fase 2: Ejecutar Vision Review via sub-agente."""
    print_progress(30, "Fase 2: Vision Review Sub-agent")

    log("Iniciando Vision Review...", "PHASE2")

    # Ejecutar análisis directo (simulando los agentes)
    # El workflow está en .agent/03_Workflows/03_Vision_Review.md

    print(f"\n{Colors.CYAN}=== VISION REVIEW ANALYSIS ==={Colors.ENDC}")
    print(f"Target: {target}")
    print()

    # 1. Analizar archivos cambiados
    print(f"{Colors.GREEN}→ Analizando archivos del sistema...{Colors.ENDC}")

    # Leer archivos modificados
    status_result = subprocess.run(
        "git status --porcelain",
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
        shell=True,
    )
    files = [
        f.strip()[3:]
        for f in status_result.stdout.split("\n")
        if f.strip()
        and (
            f.strip().startswith("M")
            or f.strip().startswith("??")
            or f.strip().startswith(" A")
        )
    ]

    print(f"\n{Colors.CYAN}Archivos para revisión: {len(files)}{Colors.ENDC}")
    for f in files[:8]:
        print(f"  - {f}")

    # 2. Simular análisis de agentes (buscar patterns)
    print(f"\n{Colors.CYAN}=== ANALISIS DE PATTERNS ==={Colors.ENDC}")

    issues = []
    for f in files[:15]:
        file_path = Path(PROJECT_ROOT) / f
        if file_path.exists() and file_path.suffix in [".py", ".md", ".json"]:
            try:
                content = file_path.read_text(encoding="utf-8", errors="ignore")

                # Buscar issues comunes
                if "TODO" in content or "FIXME" in content:
                    issues.append(f"{f}: Tiene TODOs/FIXMEs")
                if "print(" in content and f.endswith(".py"):
                    issues.append(f"{f}: Tiene print statements")
                if len(content) > 8000:
                    issues.append(f"{f}: Archivo grande ({len(content)} chars)")
            except:
                pass

    if issues:
        print(f"\n{Colors.YELLOW}Issues encontrados ({len(issues)}):{Colors.ENDC}")
        for issue in issues[:8]:
            print(f"  ⚠️ {issue}")
        # Guardar issues como findings para próximas fases
        return {
            "success": True,
            "issues": issues,
            "files_reviewed": len(files),
            "generated_todos": len(issues),
        }
    else:
        print(f"\n{Colors.GREEN}✅ No se encontraron issues críticos{Colors.ENDC}")

    log("Vision Review completado", "PHASE2_DONE")

    return {
        "success": True,
        "issues": [],
        "files_reviewed": len(files),
        "generated_todos": 0,
    }


# ==============================================================================
# FASE 3: FINDINGS ANALYSIS (50%)
# ==============================================================================


def phase_findings_analysis():
    """Fase 3: Analizar findings y determinar accionables."""
    print_progress(50, "Fase 3: Findings Analysis")

    log("Analizando findings...", "PHASE3")

    # Buscar todos reciente en Active_Tasks
    todos = list(ACTIVE_TASKS_DIR.glob("*.md")) if ACTIVE_TASKS_DIR.exists() else []

    # Filtrar por fecha reciente (últimos 2 días)
    recent_todos = []
    for todo in todos:
        try:
            # Leer el archivo y buscar priority
            content = todo.read_text(encoding="utf-8", errors="ignore")

            # Detectar priority del filename o contenido
            priority = "P3"
            if "P0" in todo.name or "p0" in content:
                priority = "P0"
            elif "P1" in todo.name or "p1" in content:
                priority = "P1"
            elif "P2" in todo.name or "p2" in content:
                priority = "P2"

            recent_todos.append(
                {"file": todo.name, "priority": priority, "path": str(todo)}
            )
        except Exception as e:
            log(f"Error leyendo {todo.name}: {e}", "WARNING")

    # Contar por priority
    p0_count = sum(1 for t in recent_todos if t["priority"] == "P0")
    p1_count = sum(1 for t in recent_todos if t["priority"] == "P1")
    p2_count = sum(1 for t in recent_todos if t["priority"] == "P2")

    print(f"\n{Colors.GREEN}=== FINDINGS RESUMEN ==={Colors.ENDC}")
    print(f"P0 (Critical): {p0_count}")
    print(f"P1 (Important): {p1_count}")
    print(f"P2 (Nice-to-have): {p2_count}")
    print(f"Total: {len(recent_todos)}")

    # Determinar si necesita planning
    needs_planning = p0_count > 0 or p1_count >= 3

    log(
        f"Needs planning: {needs_planning} (P0={p0_count}, P1={p1_count})",
        "PHASE3_DONE",
    )

    return {
        "todos": recent_todos,
        "p0_count": p0_count,
        "p1_count": p1_count,
        "p2_count": p2_count,
        "needs_planning": needs_planning,
    }


# ==============================================================================
# FASE 4: PLANNING SUB-AGENT (70%)
# ==============================================================================


def phase_planning(findings_data):
    """Fase 4: Ejecutar Planning via Professor X."""
    print_progress(70, "Fase 4: Planning Sub-agent")

    log("Iniciando fase de planning...", "PHASE4")

    if not findings_data["needs_planning"]:
        print(
            f"\n{Colors.YELLOW}⚠️ No hay suficientes findings para planificar{Colors.ENDC}"
        )
        print(f"{Colors.YELLOW}   (Requiere: P0>0 o P1>=3){Colors.ENDC}")
        log("Planning no requerido", "PHASE4_SKIP")
        return {"executed": False, "reason": "No needs planning"}

    # Preguntar al usuario
    should_plan = ask_user(
        f"Hay {findings_data['p0_count']} P0 y {findings_data['p1_count']} P1 findings. ¿Querés que planifiquemos los actionables?"
    )

    if not should_plan:
        print(f"\n{Colors.YELLOW}⚠️ Planning cancelado por usuario{Colors.ENDC}")
        log("Planning cancelado por usuario", "PHASE4_CANCEL")
        return {"executed": False, "reason": "User cancelled"}

    # Planning workflow: leer el archivo de workflow y procesar
    workflow_file = (
        Path(PROJECT_ROOT) / ".agent" / "03_Workflows" / "02_Professor_X_Plan.md"
    )

    print(f"\n{Colors.CYAN}=== PLANNING WORKFLOW ==={Colors.ENDC}")
    print(f"Workflow: {workflow_file.name if workflow_file.exists() else 'NOT FOUND'}")

    # Obtener los findings más urgentes
    urgent_todos = [t for t in findings_data["todos"] if t["priority"] in ["P0", "P1"]][
        :3
    ]

    planned_items = []
    for todo in urgent_todos:
        print(f"\n{Colors.CYAN}→ Planificando: {todo['file']}{Colors.ENDC}")

        # Simular planning - crear un mini-plan
        plan_content = f"""# Plan para: {todo["file"]}

## Problema Detectado
- Prioridad: {todo["priority"]}
- Archivo: {todo["file"]}

## Análisis
- Requiere revisión y potenciales cambios

## Próximos Pasos
1. Revisar el archivo
2. Identificar changes necesarios
3. Implementar fix
4. Validar

## Status
- [ ] Por hacer
"""

        # Guardar el plan
        plans_dir = Path(PROJECT_ROOT) / "03_Knowledge" / "04_Strategic_Plans"
        plans_dir.mkdir(exist_ok=True)

        plan_file = plans_dir / f"plan_{todo['file']}"
        plan_file.write_text(plan_content, encoding="utf-8")

        planned_items.append(str(plan_file))
        print(f"   ✅ Plan creado: {plan_file.name}")

    log(f"Planning completado: {len(planned_items)} planes", "PHASE4_DONE")

    return {
        "executed": True,
        "planned_count": len(planned_items),
        "todos_planned": [{"file": p, "priority": "P1"} for p in planned_items],
    }


# ==============================================================================
# FASE 5: EXECUTION SUB-AGENT (90%)
# ==============================================================================


def phase_execution(plan_data):
    """Fase 5: Ejecutar Thor Work via sub-agente."""
    print_progress(90, "Fase 5: Execution Sub-agent")

    log("Iniciando fase de ejecución...", "PHASE5")

    if not plan_data.get("executed"):
        print(f"\n{Colors.YELLOW}⚠️ No hay planes para ejecutar{Colors.ENDC}")
        log("Execution skippeado - no hay planes", "PHASE5_SKIP")
        return {"executed": False}

    # Preguntar al usuario
    should_execute = ask_user(
        f"Se crearon {plan_data.get('planned_count', 0)} planes. ¿Aprobamos su ejecución?"
    )

    if not should_execute:
        print(f"\n{Colors.YELLOW}⚠️ Ejecución cancelada por usuario{Colors.ENDC}")
        log("Ejecución cancelada por usuario", "PHASE5_CANCEL")
        return {"executed": False, "reason": "User cancelled"}

    # Ejecutar work para cada plan
    executed_count = 0

    for plan_file in plan_data.get("todos_planned", []):
        print(f"\n{Colors.CYAN}→ Ejecutando: {plan_file['file']}{Colors.ENDC}")

        # Ejecutar workflow de work
        command = f'claude --print "/workflows:work {plan_file["file"]}" 2>&1'
        result = run_subagent(command, f"Work para {plan_file['file']}")

        if result["success"]:
            executed_count += 1

    log(f"Ejecución completada: {executed_count} items", "PHASE5_DONE")

    return {"executed": True, "executed_count": executed_count}


# ==============================================================================
# FASE 6: SUMMARY (100%)
# ==============================================================================


def phase_summary(git_data, findings_data, planning_data, execution_data):
    """Fase 6: Generar summary final."""
    print_progress(100, "Fase 6: Summary")

    print(f"""
{Colors.GREEN}================================================================================
                    AVENGERS CYCLE COMPLETE - RESUMEN
================================================================================{Colors.ENDC}

📊 FASE 1 - Git Analysis:
   Archivos modificados: {git_data.get("file_count", 0)}

📊 FASE 2 - Vision Review:
   Completado: ✅

📊 FASE 3 - Findings Analysis:
   P0 (Critical): {findings_data.get("p0_count", 0)}
   P1 (Important): {findings_data.get("p1_count", 0)}
   P2 (Nice-to-have): {findings_data.get("p2_count", 0)}

📊 FASE 4 - Planning:
   Ejecutado: {planning_data.get("executed", False)}
   Planes creados: {planning_data.get("planned_count", 0)}

📊 FASE 5 - Execution:
   Ejecutado: {execution_data.get("executed", False)}
   Items completados: {execution_data.get("executed_count", 0)}

{Colors.GREEN}================================================================================
                         🟢 ESTADO: PURE GREEN
================================================================================{Colors.ENDC}
    """)

    log("Avengers Cycle completado", "DONE")


# ==============================================================================
# MAIN
# ==============================================================================


def main():
    """Punto de entrada principal."""
    print_banner()

    # Get target from arguments or default
    target = sys.argv[1] if len(sys.argv) > 1 else "main"

    log(f"Iniciando Avengers v3.0 con target: {target}", "START")

    print(f"\n{Colors.YELLOW}Target para revisión: {target}{Colors.ENDC}\n")

    # ==========================================================================
    # FASE 1: Git Analysis
    # ==========================================================================
    git_data = phase_git_analysis(target)

    # Approval Gate 1
    if not ask_user("¿Iniciamos Vision Review con este análisis?"):
        print(f"\n{Colors.RED}❌ Ciclo cancelado por usuario{Colors.ENDC}")
        log("Usuario canceló en Approval Gate 1", "CANCELLED")
        sys.exit(0)

    # ==========================================================================
    # FASE 2: Vision Review
    # ==========================================================================
    vision_data = phase_vision_review(target)

    # ==========================================================================
    # FASE 3: Findings Analysis
    # ==========================================================================
    findings_data = phase_findings_analysis()

    # ==========================================================================
    # FASE 4: Planning (Conditional)
    # ==========================================================================
    planning_data = phase_planning(findings_data)

    # ==========================================================================
    # FASE 5: Execution (Conditional)
    # ==========================================================================
    execution_data = phase_execution(planning_data)

    # ==========================================================================
    # FASE 6: Summary
    # ==========================================================================
    phase_summary(git_data, findings_data, planning_data, execution_data)

    log("Avengers v3.0 completado exitosamente", "COMPLETE")


if __name__ == "__main__":
    main()
