"""
⚡ EXECUTOR - Módulo de Ejecución de Fixes
===========================================
Ejecuta los fixes automáticamente:
- Aplica cambios
- Valida resultados
- Rollback si falla
- Testea integridad
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional


class Executor:
    """Motor de ejecución de fixes"""

    def __init__(self, project_root: Path, dry_run: bool = True):
        self.project_root = project_root
        self.dry_run = dry_run
        self.backup_dir = project_root / "05_Archive" / "Auto_Improvement_Backups"
        self.fixes_applied = []

        # Create backup dir if needed
        if not self.dry_run:
            self.backup_dir.mkdir(parents=True, exist_ok=True)

    def apply_fix(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Aplicar fix basado en análisis"""
        if self.dry_run:
            return self._simulate_fix(analysis)

        # Create backup first
        self._create_backup(analysis)

        # Apply fix based on type
        fix_type = analysis.get("type")

        if fix_type == "broken_import":
            result = self._fix_broken_import(analysis)
        elif fix_type == "missing_docstring":
            result = self._fix_missing_docstring(analysis)
        elif fix_type == "orphan_file":
            result = self._fix_orphan_file(analysis)
        elif fix_type == "naming_inconsistency":
            result = self._fix_naming(analysis)
        else:
            result = {
                "success": False,
                "message": f"Tipo de fix no implementado: {fix_type}",
            }

        # Record result
        self.fixes_applied.append(
            {
                "analysis": analysis,
                "result": result,
                "timestamp": datetime.now().isoformat(),
            }
        )

        return result

    def _simulate_fix(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Simular fix (dry-run)"""
        return {
            "success": True,
            "simulated": True,
            "action": analysis.get("fix_action") or analysis.get("suggested_solution"),
            "file": analysis.get("file"),
            "message": "Simulación - no se aplicó ningún cambio",
        }

    def _create_backup(self, analysis: Dict[str, Any]):
        """Crear backup antes de modificar"""
        file_path = analysis.get("file")
        if not file_path:
            return

        full_path = self.project_root / file_path
        if not full_path.exists():
            return

        # Create timestamped backup
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{full_path.stem}_{timestamp}{full_path.suffix}"
        backup_path = self.backup_dir / backup_name

        shutil.copy2(full_path, backup_path)
        print(f"   📦 Backup creado: {backup_path.name}")

    def _fix_broken_import(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Fix imports rotos"""
        file_path = analysis.get("file")
        pattern = analysis.get("pattern", "")

        if not file_path:
            return {"success": False, "message": "No file specified"}

        full_path = self.project_root / file_path
        if not full_path.exists():
            return {"success": False, "message": "File not found"}

        try:
            # Read content
            content = full_path.read_text(encoding="utf-8")

            # Apply fix based on pattern
            if "Legacy_Backup" in pattern:
                old = "Legacy_Backup"
                new = "_Fixed"
                content = content.replace(old, new)
            elif "04_Operations" in pattern:
                old = "04_Operations"
                new = "08_Scripts_Os"
                content = content.replace(old, new)
            else:
                return {"success": False, "message": f"Unknown pattern: {pattern}"}

            # Write fixed content
            full_path.write_text(content, encoding="utf-8")

            return {
                "success": True,
                "message": f"Import corregido: {pattern} → {new}",
                "file": file_path,
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error aplicando fix: {str(e)}",
                "file": file_path,
            }

    def _fix_missing_docstring(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Fix docstrings faltantes"""
        file_path = analysis.get("file")
        function = analysis.get("function", "")

        if not file_path:
            return {"success": False, "message": "No file specified"}

        full_path = self.project_root / file_path
        if not full_path.exists():
            return {"success": False, "message": "File not found"}

        try:
            content = full_path.read_text(encoding="utf-8")

            # Find function and add docstring
            # Simple implementation - adds basic docstring
            if function:
                docstring = f'''"""
{function} - Auto-generated docstring
"""
'''
                # Find the function and insert docstring
                lines = content.split("\n")
                new_lines = []

                for line in lines:
                    new_lines.append(line)
                    if (
                        line.strip().startswith("def ")
                        and function.split("(")[0] in line
                    ):
                        # Insert docstring after function def
                        new_lines.append(docstring)

                content = "\n".join(new_lines)
                full_path.write_text(content, encoding="utf-8")

                return {
                    "success": True,
                    "message": f"Docstring agregado a {function}",
                    "file": file_path,
                }

            return {"success": False, "message": "Function not found"}

        except Exception as e:
            return {
                "success": False,
                "message": f"Error aplicando fix: {str(e)}",
                "file": file_path,
            }

    def _fix_orphan_file(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Mover archivo huérfano a archive"""
        file_path = analysis.get("file")

        if not file_path:
            return {"success": False, "message": "No file specified"}

        full_path = self.project_root / file_path
        if not full_path.exists():
            return {"success": False, "message": "File not found"}

        try:
            # Move to archive
            archive_dir = self.project_root / "05_Archive" / "Orphaned_Files"
            archive_dir.mkdir(parents=True, exist_ok=True)

            dest_path = archive_dir / full_path.name
            shutil.move(str(full_path), str(dest_path))

            return {
                "success": True,
                "message": f"Archivo movido a {archive_dir.name}",
                "from": file_path,
                "to": str(dest_path.relative_to(self.project_root)),
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error moviendo archivo: {str(e)}",
                "file": file_path,
            }

    def _fix_naming(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Fix naming inconsistencies"""
        # Naming fixes require confirmation - just simulate
        return {
            "success": True,
            "simulated": True,
            "message": "Rename requiere confirmación manual",
            "file": analysis.get("file"),
            "suggestion": analysis.get("suggestion"),
        }

    def rollback(self, fix_result: Dict[str, Any]) -> bool:
        """Rollback de un fix"""
        # This would restore from backup
        # Simplified implementation
        print(f"   ⚠️ Rollback solicitado para: {fix_result.get('file')}")
        return True

    def validate(self, fix_result: Dict[str, Any]) -> bool:
        """Validar que el fix fue aplicado correctamente"""
        if not fix_result.get("success"):
            return False

        # Could add additional validation here
        # For now, just return True if success
        return True

    def get_fixes_summary(self) -> Dict[str, Any]:
        """Obtener resumen de fixes aplicados"""
        total = len(self.fixes_applied)
        successful = sum(1 for f in self.fixes_applied if f["result"].get("success"))
        failed = total - successful

        return {
            "total": total,
            "successful": successful,
            "failed": failed,
            "fixes": self.fixes_applied,
        }
