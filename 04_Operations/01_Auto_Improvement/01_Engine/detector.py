"""
🔍 DETECTOR - Módulo de Detección de Issues
=============================================
Detecta problemas, deuda técnica y desviaciones en el sistema.

Tipos de detección:
- Archivos huérfanos
- Imports rotos
- Duplicados
- Inconsistencias de naming
- Scripts que fallan
- Deuda técnica
"""

import os
import json
import ast
import importlib.util
from pathlib import Path
from typing import List, Dict, Any, Set, Optional


class Detector:
    """Motor de detección de issues del sistema"""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.issues = []
        self.config = self._load_config()

        # Detection rules
        self.detection_rules = {
            "orphan_files": {
                "enabled": True,
                "description": "Archivos sin referencias",
                "severity": "medium",
            },
            "broken_imports": {
                "enabled": True,
                "description": "Imports que fallan",
                "severity": "high",
            },
            "naming_inconsistencies": {
                "enabled": True,
                "description": "Nombres inconsistentes",
                "severity": "low",
            },
            "duplicate_scripts": {
                "enabled": True,
                "description": "Scripts duplicados",
                "severity": "medium",
            },
            "missing_docstrings": {
                "enabled": True,
                "description": "Funciones sin docstring",
                "severity": "low",
            },
            "large_files": {
                "enabled": True,
                "description": "Archivos demasiado grandes",
                "severity": "low",
            },
        }

    def _load_config(self) -> Dict[str, Any]:
        """Load exclusion patterns from config file"""
        config_path = (
            self.project_root
            / "04_Operations"
            / "01_Auto_Improvement"
            / "02_Rules"
            / "detector_config.json"
        )

        default_config = {
            "exclusion_patterns": {
                "directories_to_skip": [
                    "Legacy_Backup",
                    "node_modules",
                    ".git",
                    "venv",
                    "__pycache__",
                    ".venv",
                ],
                "file_exceptions": [
                    "README.md",
                    "README.txt",
                    "setup.py",
                    "setup.cfg",
                    "pyproject.toml",
                    "__init__.py",
                    "conftest.py",
                    ".env",
                    ".env.example",
                    ".gitignore",
                    ".dockerignore",
                ],
                "legacy_prefixes_to_exclude": ["04_", "05_", "Legacy_"],
            },
            "naming_rules": {
                "python_pattern": r"^\d{2}_[A-Za-z0-9_]*\.py$",
                "markdown_pattern": r"^\d{2}_[A-Za-z0-9_\-\s]*\.md$",
            },
        }

        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return default_config
        return default_config

    def scan_critical(self) -> List[Dict[str, Any]]:
        """Scan rápido - solo issues críticos"""
        issues = []

        print("   🔍 Escaneando issues críticos...")

        # Check broken imports
        issues.extend(self._check_broken_imports())

        # Check critical naming issues
        issues.extend(self._check_naming_critical())

        self.issues = issues
        return issues

    def scan_all(self) -> List[Dict[str, Any]]:
        """Scan completo - todos los tipos de issues"""
        issues = []

        print("   🔍 Escaneando todos los tipos de issues...")

        # Run all detectors
        issues.extend(self._check_orphan_files())
        issues.extend(self._check_broken_imports())
        issues.extend(self._check_naming_inconsistencies())
        issues.extend(self._check_duplicate_scripts())
        issues.extend(self._check_missing_docstrings())
        issues.extend(self._check_large_files())

        self.issues = issues
        return issues

    def _check_orphan_files(self) -> List[Dict[str, Any]]:
        """Detectar archivos huérfanos (sin referencias)"""
        issues = []

        # Scan scripts directory
        scripts_dir = self.project_root / "08_Scripts_Os"
        if not scripts_dir.exists():
            return issues

        # Get all Python files
        py_files = list(scripts_dir.glob("**/*.py"))

        # Simple orphan detection: files with no clear references
        # This is a simplified version - could be enhanced
        for py_file in py_files:
            if py_file.name.startswith("_"):
                continue

            # Check if file is referenced in other files
            content = py_file.read_text(errors="ignore")

            # Skip if it's a hub or main script
            if "_Hub.py" in py_file.name:
                continue

            # Check for minimal content
            if len(content) < 200:
                issues.append(
                    {
                        "type": "orphan_file",
                        "severity": "low",
                        "file": str(py_file.relative_to(self.project_root)),
                        "description": f"Archivo muy pequeño: {py_file.name}",
                        "auto_fixable": True,
                        "suggestion": "Mover a carpeta de archive o eliminar",
                    }
                )

        return issues

    def _check_broken_imports(self) -> List[Dict[str, Any]]:
        """Detectar imports rotos o obsoletos usando AST parsing"""
        issues = []

        scripts_dir = self.project_root / "08_Scripts_Os"
        if not scripts_dir.exists():
            return issues

        # Directories to skip
        directories_to_skip = self.config.get("exclusion_patterns", {}).get(
            "directories_to_skip", []
        )

        class ImportVisitor(ast.NodeVisitor):
            """AST visitor to extract import statements"""

            def __init__(self):
                self.imports: List[Dict[str, str]] = []
                self.in_try_except = False

            def visit_Try(self, node):
                """Track try/except blocks to handle conditional imports"""
                # Mark that we're in a try block - imports here might be conditional
                old_in_try = self.in_try_except
                self.in_try_except = True
                self.generic_visit(node)
                self.in_try_except = old_in_try

            def visit_Import(self, node):
                """Handle: import X, import X as Y, import X.Y"""
                for alias in node.names:
                    module_name = alias.name
                    self.imports.append(
                        {
                            "module": module_name,
                            "full_statement": f"import {module_name}",
                            "conditional": self.in_try_except,
                        }
                    )
                self.generic_visit(node)

            def visit_ImportFrom(self, node):
                """Handle: from X import Y, from X.Y import Z"""
                if node.module:
                    module_name = node.module
                    for alias in node.names:
                        self.imports.append(
                            {
                                "module": module_name,
                                "name": alias.name,
                                "full_statement": f"from {module_name} import {alias.name}",
                                "conditional": self.in_try_except,
                            }
                        )
                self.generic_visit(node)

        for py_file in scripts_dir.glob("**/*.py"):
            if py_file.name.startswith("_"):
                continue

            # Skip excluded directories
            should_skip = False
            for parent in py_file.parts:
                if parent in directories_to_skip:
                    should_skip = True
                    break
            if should_skip:
                continue

            try:
                content = py_file.read_text(errors="ignore")
            except:
                continue

            try:
                tree = ast.parse(content, filename=str(py_file))
            except SyntaxError:
                # Skip files with syntax errors
                continue

            # Extract imports using AST visitor
            visitor = ImportVisitor()
            visitor.visit(tree)

            # Check each import for validity
            for imp in visitor.imports:
                # Skip conditional imports (in try/except)
                if imp.get("conditional", False):
                    continue

                module_name = imp["module"]

                # Check if module can be imported
                if not self._is_module_available(module_name, py_file.parent):
                    issues.append(
                        {
                            "type": "broken_import",
                            "severity": "high",
                            "file": str(py_file.relative_to(self.project_root)),
                            "description": f"Import roto: {imp['full_statement']}",
                            "module": module_name,
                            "auto_fixable": True,
                            "suggestion": "Verificar que el módulo esté instalado o existe",
                        }
                    )

        return issues

    def _is_module_available(self, module_name: str, file_dir: Path) -> bool:
        """Check if a module can be imported"""
        # Check built-in modules
        import sys

        if module_name in sys.builtin_module_names:
            return True

        # Try to find the module (handle ModuleNotFoundError)
        try:
            spec = importlib.util.find_spec(module_name)
            if spec is not None:
                return True
        except ModuleNotFoundError:
            pass
        except Exception:
            pass

        # Check if it's a local module (relative to file location)
        module_path = file_dir / f"{module_name}.py"
        if module_path.exists():
            return True

        # Check if it's a package
        package_path = file_dir / module_name
        if package_path.exists() and (package_path / "__init__.py").exists():
            return True

        # Check in parent directories
        for parent in file_dir.parents:
            module_path = parent / f"{module_name}.py"
            if module_path.exists():
                return True
            package_path = parent / module_name
            if package_path.exists() and (package_path / "__init__.py").exists():
                return True

        return False

    def _check_naming_critical(self) -> List[Dict[str, Any]]:
        """Verificar naming conventions críticos"""
        return self._check_naming_inconsistencies()

    def _check_naming_inconsistencies(self) -> List[Dict[str, Any]]:
        """Detectar inconsistencias de naming - VERSION EQUILIBRADA"""
        issues = []

        # Load exclusion patterns from config
        exclusion_patterns = self.config.get("exclusion_patterns", {})
        directories_to_skip = exclusion_patterns.get("directories_to_skip", [])
        file_exceptions = exclusion_patterns.get("file_exceptions", [])
        legacy_prefixes = exclusion_patterns.get("legacy_prefixes_to_exclude", [])

        # Valid naming patterns - relaxed but still meaningful
        # Python: XX_Name.py where XX is 2 digits and Name starts with letter (any case)
        # Markdown: XX_Name.md where XX is 2 digits
        valid_patterns = {
            "py": r"^\d{2}_[A-Za-z][A-Za-z0-9_]*\.py$",
            "md": r"^\d{2}_[A-Za-z0-9_\- ]*\.md$",
        }

        # Invalid patterns - these are clearly wrong
        invalid_patterns = {
            "py": r"^\d+_[0-9]",  # Starts with digits_ digits (e.g., 01_2023_script.py)
            "md": r"^\d+_[0-9]",
        }

        import re

        # Check scripts directory
        for dir_name in ["08_Scripts_Os", "01_Core", "04_Operations"]:
            dir_path = self.project_root / dir_name
            if not dir_path.exists():
                continue

            # Skip entire directories in exclusion list
            if dir_path.name in directories_to_skip:
                continue

            for ext, valid_pattern in valid_patterns.items():
                invalid_pattern = invalid_patterns.get(ext, r"^\d+_[0-9]")

                for file_path in dir_path.glob(f"**/*.{ext}"):
                    if file_path.name.startswith("_") or file_path.name.startswith("."):
                        continue

                    # Check if any parent directory should be skipped
                    should_skip = False
                    for parent in file_path.parts:
                        if parent in directories_to_skip:
                            should_skip = True
                            break
                    if should_skip:
                        continue

                    # Skip file exceptions
                    if file_path.name in file_exceptions:
                        continue

                    # Skip legacy prefixes
                    should_skip_legacy = False
                    for prefix in legacy_prefixes:
                        if file_path.name.startswith(prefix):
                            should_skip_legacy = True
                            break
                    if should_skip_legacy:
                        continue

                    file_name = file_path.name

                    # Check if it matches valid pattern
                    if re.match(valid_pattern, file_name):
                        continue  # Valid - skip

                    # Check if it has a number prefix
                    if re.match(r"^\d+_", file_name):
                        # Has prefix but invalid - flag it
                        issues.append(
                            {
                                "type": "naming_inconsistency",
                                "severity": "low",
                                "file": str(file_path.relative_to(self.project_root)),
                                "description": f"Archivo con naming inválido: {file_name}",
                                "auto_fixable": True,
                                "suggestion": "Usar formato: XX_Nombre.ext",
                            }
                        )
                    # Files without number prefix are now IGNORED (too many false positives)

        return issues

    def _check_duplicate_scripts(self) -> List[Dict[str, Any]]:
        """Detectar scripts duplicados (simplificado)"""
        issues = []

        # This is a simplified version
        # In production, would use file hashing or similarity detection

        scripts_dir = self.project_root / "08_Scripts_Os"
        if not scripts_dir.exists():
            return issues

        # Load exclusion patterns from config
        directories_to_skip = (
            self._load_config()
            .get("exclusion_patterns", {})
            .get("directories_to_skip", [])
        )

        # Add _Fixed to skip list
        skip_dirs = set(directories_to_skip + ["_Fixed"])

        # Check for exact duplicate names in different locations
        file_names = {}
        for py_file in scripts_dir.glob("**/*.py"):
            # Skip excluded directories
            if any(d in py_file.parts for d in skip_dirs):
                continue
            name = py_file.stem  # filename without extension
            if name not in file_names:
                file_names[name] = []
            file_names[name].append(py_file)

        # Report duplicates only if real (not in _Fixed or Legacy_Backup)
        for name, paths in file_names.items():
            if len(paths) > 1:
                # Filter out paths in excluded directories
                valid_paths = [
                    p for p in paths if not any(d in p.parts for d in skip_dirs)
                ]
                if valid_paths and len(valid_paths) > 1:
                    issues.append(
                        {
                            "type": "duplicate_script",
                            "severity": "medium",
                            "file": str(valid_paths[0].relative_to(self.project_root)),
                            "files": [
                                str(p.relative_to(self.project_root))
                                for p in valid_paths
                            ],
                            "description": f"Script duplicado: {name} ({len(valid_paths)} locations)",
                            "auto_fixable": False,
                            "suggestion": "Consolidar o mantener uno solo",
                        }
                    )

        return issues

    def _check_missing_docstrings(self) -> List[Dict[str, Any]]:
        """Detectar funciones sin docstrings"""
        issues = []

        scripts_dir = self.project_root / "08_Scripts_Os"
        if not scripts_dir.exists():
            return issues

        import re

        for py_file in scripts_dir.glob("**/*.py"):
            if py_file.name.startswith("_"):
                continue
            # Skip _Fixed directories
            if "_Fixed" in py_file.parts:
                continue

            try:
                content = py_file.read_text(errors="ignore")
            except:
                continue

            # Look for functions without docstrings
            # Simple pattern: def without """ after
            lines = content.split("\n")
            in_function = False
            function_name = None

            for i, line in enumerate(lines):
                if line.strip().startswith("def ") and "(" in line:
                    in_function = True
                    function_name = line.strip()

                    # Check next few lines for docstring
                    has_docstring = False
                    for j in range(i + 1, min(i + 4, len(lines))):
                        if '"""' in lines[j] or "'''" in lines[j]:
                            has_docstring = True
                            break

                    if not has_docstring and function_name:
                        # Only report for important functions
                        if "def run_" in function_name or "def main" in function_name:
                            issues.append(
                                {
                                    "type": "missing_docstring",
                                    "severity": "low",
                                    "file": str(py_file.relative_to(self.project_root)),
                                    "function": function_name,
                                    "description": f"Función sin docstring: {function_name}",
                                    "auto_fixable": True,
                                    "suggestion": "Agregar docstring",
                                }
                            )

            # Limit to prevent too many issues
            if len(issues) > 20:
                break

        return issues

    def _check_large_files(self) -> List[Dict[str, Any]]:
        """Detectar archivos demasiado grandes"""
        issues = []

        threshold_lines = 500

        for dir_name in ["08_Scripts_Os", "01_Core"]:
            dir_path = self.project_root / dir_name
            if not dir_path.exists():
                continue

            for py_file in dir_path.glob("**/*.py"):
                # Skip Legacy_Backup, _Fixed, and 10_Backup directories
                if (
                    "Legacy_Backup" in py_file.parts
                    or "_Fixed" in py_file.parts
                    or "10_Backup" in py_file.parts
                ):
                    continue

                try:
                    lines = len(py_file.read_text(errors="ignore").split("\n"))
                except:
                    continue

                if lines > threshold_lines:
                    issues.append(
                        {
                            "type": "large_file",
                            "severity": "low",
                            "file": str(py_file.relative_to(self.project_root)),
                            "description": f"Archivo grande: {lines} líneas",
                            "lines": lines,
                            "auto_fixable": False,
                            "suggestion": f"Considerar separar en módulos (>{threshold_lines} líneas)",
                        }
                    )

        return issues
