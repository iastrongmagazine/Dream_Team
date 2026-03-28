#!/usr/bin/env python3
"""
Skill Validator - Validates skill structure and dependencies

Checks that all skills have proper structure, SKILL.md files exist,
and dependencies are available before running tests.
"""

import sys
import io
from pathlib import Path
from typing import Dict

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')


class SkillValidator:
    """Validates skill structure and system readiness"""

    def __init__(self, base_path: Path):
        """Initialize skill validator

        Args:
            base_path: Base path to Amazing_World directory
        """
        self.base_path = Path(base_path)
        # Consolidated skills path (2026)
        self.skills_path_amazing = self.base_path / "02_Voldemort_Backend" / "07_Skill"
        self.skills_path_invictus = self.base_path / "02_Voldemort_Backend" / "07_Skill"

    def validate_all(self) -> Dict[str, Dict]:
        """Validate entire system

        Returns:
            Dict of validation results
        """
        results = {}

        # Check skill directories exist
        results['invictus_skills'] = self._check_directory(self.skills_path_invictus)

        # Check test definitions exist
        tests_path = self.base_path / "02_Voldemort_Backend" / "05_Examples" / "tests"
        results['test_definitions'] = self._check_directory(tests_path)

        # Check RESULTS.md exists
        results_md = tests_path / "RESULTS.md"
        results['results_md'] = {
            'valid': results_md.exists(),
            'message': 'RESULTS.md found' if results_md.exists() else 'RESULTS.md missing'
        }

        # Check output directories are writable
        reports_path = self.base_path / ".claude" / "reports"
        results['reports_writable'] = self._check_writable(reports_path)

        logs_path = self.base_path / ".claude" / "logs"
        results['logs_writable'] = self._check_writable(logs_path)

        return results

    def _check_directory(self, path: Path) -> Dict:
        """Check if directory exists

        Args:
            path: Directory path to check

        Returns:
            Validation result dict
        """
        exists = path.exists() and path.is_dir()
        return {
            'valid': exists,
            'message': f'Directory found: {path}' if exists else f'Directory missing: {path}'
        }

    def _check_writable(self, path: Path) -> Dict:
        """Check if directory is writable

        Args:
            path: Directory path to check

        Returns:
            Validation result dict
        """
        try:
            path.mkdir(exist_ok=True)
            test_file = path / '.write_test'
            test_file.write_text('test')
            test_file.unlink()
            return {
                'valid': True,
                'message': f'Directory writable: {path}'
            }
        except Exception as e:
            return {
                'valid': False,
                'message': f'Directory not writable: {path} - {str(e)}'
            }
