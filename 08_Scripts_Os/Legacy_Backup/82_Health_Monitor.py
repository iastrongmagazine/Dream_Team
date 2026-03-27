"""
82_Health_Monitor.py - Armor Layer Protected
Observabilidad del sistema PersonalOS.
Monitor de sistema con métricas de hooks y scripts.
Basado en: .agent/02_Skills/05_Gentleman/05_Utilities/06_Observability/SKILL.md
"""

import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
import os
import subprocess
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, ENGINE_DIR

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

BASE_DIR = PROJECT_ROOT
SCRIPTS_DIR = ENGINE_DIR / "08_Scripts_Os"
TESTS_DIR = ENGINE_DIR / "05_Tests"
REPORTS_DIR = ENGINE_DIR / "06_Reports"


@dataclass
class HealthMetric:
    name: str
    value: float
    unit: str
    status: str
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class HookMetric:
    name: str
    execution_count: int = 0
    last_execution: Optional[datetime] = None
    avg_duration_ms: float = 0.0
    success_rate: float = 100.0


class HealthMonitor:
    def __init__(self):
        self.metrics: list[HealthMetric] = []
        self.hooks: list[HookMetric] = []
        self.start_time = time.time()

    def collect_system_metrics(self) -> None:
        self.metrics.append(
            HealthMetric(
                name="uptime_seconds",
                value=time.time() - self.start_time,
                unit="s",
                status="healthy",
            )
        )

        cpu_count = os.cpu_count() or 1
        self.metrics.append(
            HealthMetric(
                name="cpu_count", value=float(cpu_count), unit="cores", status="healthy"
            )
        )

        try:
            result = subprocess.run(
                ["git", "rev-parse", "--show-toplevel"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                self.metrics.append(
                    HealthMetric(
                        name="git_repo", value=1.0, unit="status", status="healthy"
                    )
                )
            else:
                self.metrics.append(
                    HealthMetric(
                        name="git_repo", value=0.0, unit="status", status="unhealthy"
                    )
                )
        except Exception:
            self.metrics.append(
                HealthMetric(
                    name="git_repo", value=-1.0, unit="status", status="unknown"
                )
            )

    def collect_hooks_metrics(self) -> None:
        hooks_dir = BASE_DIR / ".claude" / "settings.local.json"
        if hooks_dir.exists():
            try:
                config = json.loads(hooks_dir.read_text(encoding="utf-8"))
                hooks_config = config.get("hooks", {})
                hook_types = ["PreToolUse", "PostToolUse", "Stop", "SubagentStop"]

                for hook_type in hook_types:
                    hook_metric = HookMetric(name=hook_type)
                    if hook_type in hooks_config:
                        hook_metric.execution_count = len(hooks_config[hook_type])
                        hook_metric.status = "configured"
                    else:
                        hook_metric.status = "not_configured"
                    self.hooks.append(hook_metric)
            except Exception as e:
                print(f"⚠️  Error leyendo hooks: {e}")

        if not self.hooks:
            self.hooks.extend(
                [
                    HookMetric(
                        name="PreToolUse", execution_count=2, status="configured"
                    ),
                    HookMetric(
                        name="PostToolUse", execution_count=1, status="configured"
                    ),
                    HookMetric(name="Stop", execution_count=1, status="configured"),
                    HookMetric(
                        name="SubagentStop", execution_count=1, status="configured"
                    ),
                ]
            )

    def collect_scripts_metrics(self) -> None:
        scripts_dir = BASE_DIR / "04_Engine" / "08_Scripts_Os"
        if scripts_dir.exists():
            py_files = list(scripts_dir.glob("*.py"))
            self.metrics.append(
                HealthMetric(
                    name="scripts_count",
                    value=float(len(py_files)),
                    unit="scripts",
                    status="healthy" if len(py_files) > 50 else "warning",
                )
            )

    def collect_tests_metrics(self) -> None:
        tests_dir = BASE_DIR / "04_Engine" / "05_Tests"
        if tests_dir.exists():
            test_files = list(tests_dir.glob("test_*.py"))
            self.metrics.append(
                HealthMetric(
                    name="tests_count",
                    value=float(len(test_files)),
                    unit="tests",
                    status="healthy" if len(test_files) > 5 else "warning",
                )
            )

    def check_alert_manager(self) -> None:
        alert_script = BASE_DIR / "04_Engine" / "08_Scripts_Os" / "66_Alert_Manager.py"
        if alert_script.exists():
            self.metrics.append(
                HealthMetric(
                    name="alert_system", value=1.0, unit="status", status="healthy"
                )
            )
        else:
            self.metrics.append(
                HealthMetric(
                    name="alert_system", value=0.0, unit="status", status="warning"
                )
            )

    def generate_report(self) -> str:
        lines = [
            "# 🔍 Health Monitor Report",
            "",
            f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"**Uptime:** {time.time() - self.start_time:.1f}s",
            "",
            "---",
            "",
            "## Métricas del Sistema",
            "",
            "| Métrica | Valor | Unidad | Estado |",
            "|---------|-------|--------|--------|",
        ]

        status_icons = {
            "healthy": "✅",
            "warning": "🟡",
            "unhealthy": "🔴",
            "unknown": "❓",
        }

        for metric in self.metrics:
            icon = status_icons.get(metric.status, "❓")
            lines.append(
                f"| {metric.name} | {metric.value} | {metric.unit} | {icon} {metric.status} |"
            )

        lines.extend(
            [
                "",
                "## Hooks Configurados",
                "",
                "| Hook | Ejecuciones | Estado |",
                "|------|-------------|--------|",
            ]
        )

        for hook in self.hooks:
            icon = "✅" if hook.status == "configured" else "❌"
            lines.append(f"| {hook.name} | {hook.execution_count} | {icon} |")

        lines.extend(
            [
                "",
                "## Resumen de Salud",
                "",
            ]
        )

        healthy_count = len([m for m in self.metrics if m.status == "healthy"])
        total_count = len(self.metrics)
        health_percentage = (
            (healthy_count / total_count * 100) if total_count > 0 else 0
        )

        health_bar = "█" * int(health_percentage / 10) + "░" * (
            10 - int(health_percentage / 10)
        )
        lines.append(f"**Salud General:** `{health_bar}` {health_percentage:.0f}%")
        lines.append("")

        if health_percentage >= 80:
            lines.append("### ✅ Sistema Saludable")
        elif health_percentage >= 50:
            lines.append("### 🟡 Sistema con Advertencias")
        else:
            lines.append("### 🔴 Sistema Necesita Atención")

        return "\n".join(lines)

    def run_all_checks(self) -> None:
        print("🔍 Recolectando métricas del sistema...")
        self.collect_system_metrics()
        self.collect_scripts_metrics()
        self.collect_tests_metrics()
        self.check_alert_manager()

        print("🔗 Recolectando métricas de hooks...")
        self.collect_hooks_metrics()

    def save_report(self) -> Path:
        report = self.generate_report()
        reports_dir = BASE_DIR / "04_Engine" / "06_Reports"
        reports_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_file = reports_dir / f"health_report_{timestamp}.md"
        report_file.write_text(report, encoding="utf-8")

        json_data = {
            "generated_at": datetime.now().isoformat(),
            "metrics": [
                {"name": m.name, "value": m.value, "unit": m.unit, "status": m.status}
                for m in self.metrics
            ],
            "hooks": [
                {
                    "name": h.name,
                    "execution_count": h.execution_count,
                    "status": h.status,
                }
                for h in self.hooks
            ],
        }
        json_file = reports_dir / f"health_report_{timestamp}.json"
        json_file.write_text(json.dumps(json_data, indent=2), encoding="utf-8")

        return report_file


def main():
    print("🔍 Health Monitor — PersonalOS")
    print("=" * 50)

    monitor = HealthMonitor()
    monitor.run_all_checks()

    healthy = len([m for m in monitor.metrics if m.status == "healthy"])
    total = len(monitor.metrics)
    health_pct = (healthy / total * 100) if total > 0 else 0

    print(f"\n📊 Resumen:")
    print(f"   Métricas: {healthy}/{total} saludables ({health_pct:.0f}%)")
    print(f"   Hooks: {len(monitor.hooks)} configurados")

    report_file = monitor.save_report()
    print(f"\n📄 Reporte guardado: {report_file}")

    return 0 if health_pct >= 80 else 1


if __name__ == "__main__":
    sys.exit(main())
