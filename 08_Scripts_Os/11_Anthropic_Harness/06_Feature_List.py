"""
Feature List JSON Generator

Inspirado en: "Effective harnesses for long-running agents" (Nov 26, 2025)
"""

import json
import uuid
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class Feature:
    """Una feature individual."""

    id: str
    category: str
    description: str
    steps: List[str]
    passes: bool = False
    priority: str = "medium"
    notes: Optional[str] = None


class FeatureListGenerator:
    """
    Genera feature list desde prompt del usuario.
    """

    CATEGORIES = [
        "functional",
        "ui",
        "performance",
        "security",
        "accessibility",
        "data",
    ]

    def __init__(self):
        self.current_features: List[Feature] = []

    def generate_from_prompt(self, prompt: str) -> List[Feature]:
        """
        Genera lista de features desde el prompt del usuario.

        Args:
            prompt: Descripción del proyecto

        Returns:
            Lista de Features
        """
        features = []

        # Simple parsing - en producción usar un LLM para esto
        lines = prompt.strip().split("\n")
        current_category = "functional"
        feature_id = 1

        for line in lines:
            line = line.strip()
            if not line:
                continue

            # Detectar categorías
            lower_line = line.lower()
            for cat in self.CATEGORIES:
                if cat in lower_line and ":" in line:
                    current_category = cat
                    break

            # Es una feature (empieza con - o • o numbering)
            if line.startswith("-") or line.startswith("•") or line[0].isdigit():
                # Limpiar el texto
                feature_text = line.lstrip("-•0123456789. ").strip()

                if feature_text:
                    feature = Feature(
                        id=f"feat_{str(feature_id).zfill(3)}",
                        category=current_category,
                        description=feature_text,
                        steps=[],  # El agente rellenará esto
                        passes=False,
                        priority="medium",
                    )
                    features.append(feature)
                    feature_id += 1

        self.current_features = features
        return features

    def save_to_json(self, features: List[Feature], filepath: str):
        """Guarda features a archivo JSON."""
        data = {
            "features": [asdict(f) for f in features],
            "stats": self.get_stats(features),
        }

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_json(self, filepath: str) -> List[Feature]:
        """Carga features desde archivo JSON."""
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        features = [Feature(**f) for f in data["features"]]
        self.current_features = features
        return features

    def mark_complete(self, features: List[Feature], feature_id: str):
        """Marca una feature como completada."""
        for f in features:
            if f.id == feature_id:
                f.passes = True
                break

    def mark_incomplete(self, features: List[Feature], feature_id: str):
        """Marca una feature como no completada."""
        for f in features:
            if f.id == feature_id:
                f.passes = False
                break

    def get_stats(self, features: List[Feature]) -> Dict[str, int]:
        """Obtiene estadísticas del feature list."""
        total = len(features)
        passed = sum(1 for f in features if f.passes)
        failed = total - passed

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "progress": f"{passed}/{total} ({passed / total * 100:.1f}%)"
            if total > 0
            else "0%",
        }

    def get_pending_features(self, features: List[Feature]) -> List[Feature]:
        """Obtiene features pendientes."""
        return [f for f in features if not f.passes]

    def get_completed_features(self, features: List[Feature]) -> List[Feature]:
        """Obtiene features completadas."""
        return [f for f in features if f.passes]


class FeatureTracker:
    """
    Tracking de progreso de features a lo largo de múltiples sesiones.
    """

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.session_history: List[Dict[str, Any]] = []

    def add_session(self, features: List[Feature], session_info: str):
        """Registra una sesión de trabajo."""
        stats = FeatureListGenerator().get_stats(features)

        self.session_history.append(
            {
                "session": len(self.session_history) + 1,
                "info": session_info,
                "timestamp": "",  # Will be added
                "stats": stats,
            }
        )

    def get_progress_report(self) -> str:
        """Genera reporte de progreso."""
        if not self.session_history:
            return "No sessions recorded yet."

        lines = [f"Progress Report: {self.project_name}"]
        lines.append("=" * 50)

        for session in self.session_history:
            lines.append(f"Session {session['session']}: {session['info']}")
            stats = session["stats"]
            lines.append(f"  Progress: {stats['progress']}")
            lines.append("")

        return "\n".join(lines)


# ==================== EJEMPLO ====================

if __name__ == "__main__":
    generator = FeatureListGenerator()

    # Prompt de ejemplo
    prompt = """
Build a chat app with:
- User authentication
- Real-time messaging
- File uploads
- Theme switching
- Message search
    """

    # Generar features
    features = generator.generate_from_prompt(prompt)

    # Mostrar stats
    print(f"Generated {len(features)} features")
    print(json.dumps(generator.get_stats(features), indent=2))

    # Marcar algunas como completadas
    generator.mark_complete(features, "feat_001")
    generator.mark_complete(features, "feat_003")

    # Mostrar stats de nuevo
    print()
    print("After marking some complete:")
    print(json.dumps(generator.get_stats(features), indent=2))

    # Guardar a archivo
    generator.save_to_json(features, "test_features.json")
    print("\nSaved to test_features.json")
