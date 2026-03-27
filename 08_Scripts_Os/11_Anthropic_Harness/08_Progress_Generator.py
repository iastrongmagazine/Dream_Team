"""
Progress File Template Generator
Genera templates de progreso para sesiones de desarrollo.

Inspirado en: Claude Code session tracking patterns
"""

import os
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class SessionProgress:
    """Estado de una sesión de desarrollo."""

    # Meta
    project_name: str
    session_date: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d")
    )
    last_commit: Optional[str] = None
    branches: List[str] = field(default_factory=lambda: ["main"])

    # Trabajo realizado
    completed_items: List[str] = field(default_factory=list)
    in_progress_items: List[str] = field(default_factory=list)

    # Estado del proyecto
    features_total: int = 0
    features_completed: int = 0
    tests_passing: float = 0.0
    tech_debt_items: int = 0

    # Próximos pasos
    next_steps: List[str] = field(default_factory=list)

    # Bugs conocidos
    known_bugs: List[Dict[str, str]] = field(default_factory=list)

    # Notas de sesión
    session_notes: List[str] = field(default_factory=list)


class ProgressFileGenerator:
    """Genera archivos de progreso en formato Markdown."""

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.progress = SessionProgress(project_name=project_name)

    def add_completed(self, item: str) -> None:
        """Agrega un item completado."""
        self.progress.completed_items.append(item)

    def add_in_progress(self, item: str) -> None:
        """Agrega un item en progreso."""
        self.progress.in_progress_items.append(item)

    def set_features_status(self, completed: int, total: int) -> None:
        """Setea estado de features."""
        self.progress.features_completed = completed
        self.progress.features_total = total

    def set_tests_status(self, percentage: float) -> None:
        """Setea estado de tests."""
        self.progress.tests_passing = percentage

    def add_next_step(self, step: str) -> None:
        """Agrega un próximo paso."""
        self.progress.next_steps.append(step)

    def add_bug(self, bug_id: str, description: str, severity: str = "medium") -> None:
        """Agrega un bug conocido."""
        self.progress.known_bugs.append(
            {"id": bug_id, "description": description, "severity": severity}
        )

    def add_note(self, note: str) -> None:
        """Agrega una nota de sesión."""
        self.progress.session_notes.append(note)

    def set_branches(self, branches: List[str]) -> None:
        """Setea branches activas."""
        self.progress.branches = branches

    def set_last_commit(self, commit: str) -> None:
        """Setea último commit."""
        self.progress.last_commit = commit

    def to_markdown(self) -> str:
        """Genera el archivo en formato Markdown."""
        p = self.progress

        lines = [
            f"# Claude Progress - {p.project_name}",
            "",
            "## Estado Actual",
            f"- **Última sesión:** {p.session_date}",
        ]

        if p.last_commit:
            lines.append(f"- **Último commit:** `{p.last_commit}`")

        lines.append(f"- **Branches:** {', '.join(f'`{b}`' for b in p.branches)}")
        lines.append("")

        # Lo que se hizo esta sesión
        lines.append("## Lo Que Se Hizo Esta Sesión")

        if p.completed_items:
            for item in p.completed_items:
                lines.append(f"- ✅ {item}")
        else:
            lines.append("- (Nada completado aún)")

        if p.in_progress_items:
            lines.append("")
            for item in p.in_progress_items:
                lines.append(f"- 🔄 {item}")

        lines.append("")

        # Estado del proyecto
        lines.append("## Estado del Proyecto")
        if p.features_total > 0:
            pct = (p.features_completed / p.features_total) * 100
            lines.append(
                f"- **Features completadas:** {p.features_completed}/{p.features_total} ({pct:.0f}%)"
            )
        else:
            lines.append("- **Features completadas:** 0/0")

        lines.append(f"- **Tests pasando:** {p.tests_passing:.1f}%")
        lines.append(f"- **Tech debt:** {p.tech_debt_items} items")
        lines.append("")

        # Próximos pasos
        lines.append("## Próximos Pasos")
        if p.next_steps:
            for i, step in enumerate(p.next_steps, 1):
                lines.append(f"{i}. {step}")
        else:
            lines.append("- (Sin pasos definidos)")
        lines.append("")

        # Bugs conocidos
        lines.append("## Bugs Conocidos")
        if p.known_bugs:
            for bug in p.known_bugs:
                lines.append(
                    f"- [{bug['id']}] {bug['description']} (`{bug['severity']}`)"
                )
        else:
            lines.append("- (Sin bugs conocidos)")
        lines.append("")

        # Notas de sesión
        lines.append("## Notas de la Sesión")
        if p.session_notes:
            for note in p.session_notes:
                lines.append(f"- {note}")
        else:
            lines.append("- (Sin notas)")

        return "\n".join(lines)

    def to_json(self) -> str:
        """Genera el archivo en formato JSON."""
        return json.dumps(self.progress.__dict__, indent=2)

    def save(self, filepath: str, format: str = "markdown") -> None:
        """Guarda el archivo de progreso."""
        content = self.to_markdown() if format == "markdown" else self.to_json()

        os.makedirs(
            os.path.dirname(filepath) if os.path.dirname(filepath) else ".",
            exist_ok=True,
        )

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)


# ==================== EXAMPLE ====================


def example_usage():
    """Ejemplo de uso del generador."""
    gen = ProgressFileGenerator("Mi Proyecto")

    # Completados
    gen.add_completed("Implementado login con JWT")
    gen.add_completed("Corregido bug en password reset")
    gen.add_completed("Agregados tests para auth middleware")

    # En progreso
    gen.add_in_progress("Implementando logout")

    # Estado del proyecto
    gen.set_features_status(12, 50)
    gen.set_tests_status(89.5)
    gen.set_branches(["main", "feature/auth"])
    gen.set_last_commit("abc1234")

    # Próximos pasos
    gen.add_next_step("Terminar logout")
    gen.add_next_step("Agregar 2FA")
    gen.add_next_step("Mejorar UX del login")

    # Bugs
    gen.add_bug("BUG-001", "Session expira antes de lo esperado", "high")
    gen.add_bug("BUG-002", "Memory leak en dashboard", "medium")

    # Notas
    gen.add_note("El auth middleware necesita refactor")
    gen.add_note("Decidimos usar JWT en vez de sesiones")

    # Guardar
    print(gen.to_markdown())
    print()
    print("--- JSON ---")
    print(gen.to_json())


# ==================== TESTS ====================


def test_basic_generation():
    """Test generación básica."""
    gen = ProgressFileGenerator("Test Project")
    gen.add_completed("Task 1")
    gen.add_completed("Task 2")
    gen.add_in_progress("Task 3")
    gen.set_features_status(5, 20)
    gen.set_tests_status(75.0)
    gen.add_next_step("Do something")
    gen.add_bug("BUG-001", "Test bug", "low")

    md = gen.to_markdown()

    assert "Test Project" in md
    assert "Task 1" in md
    assert "Task 2" in md
    assert "Task 3" in md
    assert "5/20" in md  # Features count
    assert "75.0" in md  # Tests percentage
    assert "Do something" in md
    assert "BUG-001" in md


def test_json_output():
    """Test salida JSON."""
    gen = ProgressFileGenerator("Test")
    gen.add_completed("Done")

    json_str = gen.to_json()
    data = json.loads(json_str)

    assert data["project_name"] == "Test"
    assert "Done" in data["completed_items"]


def test_empty_state():
    """Test con estado vacío."""
    gen = ProgressFileGenerator("Empty")

    md = gen.to_markdown()

    assert "Empty" in md
    assert "(Nada completado aún)" in md


if __name__ == "__main__":
    print("=" * 60)
    print("Progress File Template - Tests")
    print("=" * 60)

    test_basic_generation()
    print("[PASS] test_basic_generation")

    test_json_output()
    print("[PASS] test_json_output")

    test_empty_state()
    print("[PASS] test_empty_state")

    print()
    print("*** ALL TESTS PASSED ***")
    print("=" * 60)
    print("Example Output:")
    print("=" * 60)
    try:
        example_usage()
    except UnicodeEncodeError:
        print("(Unicode characters not supported in terminal)")
        # Still print JSON which is ASCII-safe
        gen = ProgressFileGenerator("Demo Project")
        gen.add_completed("Test completed")
        print(gen.to_json())
