#!/usr/bin/env python3
"""
Result Tracker - Updates RESULTS.md with test outcomes

This module handles updating the RESULTS.md file with test results,
maintaining checkboxes and progress tracking.
"""

from pathlib import Path
from typing import Dict
from datetime import datetime
import re


class ResultTracker:
    """Tracks and updates test results in RESULTS.md"""

    def __init__(self, results_path: Path):
        """Initialize result tracker

        Args:
            results_path: Path to RESULTS.md file
        """
        self.results_path = Path(results_path)

    def update_result(self, skill_name: str, result: Dict) -> None:
        """Update RESULTS.md with test result

        Args:
            skill_name: Name of the skill tested
            result: Test result dictionary
        """
        if not self.results_path.exists():
            print(f"⚠️  RESULTS.md not found at: {self.results_path}")
            return

        # Read current content
        content = self.results_path.read_text(encoding='utf-8')

        # Update checkbox for this skill
        content = self._update_checkbox(content, skill_name, result['status'])

        # Update progress counters
        content = self._update_progress(content)

        # Add to appropriate section (Quick Wins, Attention, Blocked)
        content = self._add_to_section(content, skill_name, result)

        # Write back
        self.results_path.write_text(content, encoding='utf-8')

        print(f"   📝 Updated RESULTS.md for {skill_name}")

    def _update_checkbox(self, content: str, skill_name: str, status: str) -> str:
        """Update checkbox for a skill

        Args:
            content: Current RESULTS.md content
            skill_name: Skill name
            status: Test status (functional, partial, failed)

        Returns:
            Updated content
        """
        # Find the checkbox line for this skill
        # Pattern: - [ ] Test XX: skill-name
        pattern = rf'(- \[ \] )(Test \d+: {re.escape(skill_name)})'

        if status == 'functional':
            checkbox = '- [x] '
        elif status == 'partial':
            checkbox = '- [~] '  # Use ~ for partial
        elif status == 'failed':
            checkbox = '- [!] '  # Use ! for failed
        else:
            checkbox = '- [ ] '  # Keep unchecked for skipped/pending

        replacement = rf'\g<1>{checkbox}\2'
        content = re.sub(pattern, replacement, content)

        return content

    def _update_progress(self, content: str) -> str:
        """Update progress counters

        Args:
            content: Current RESULTS.md content

        Returns:
            Updated content with new progress numbers
        """
        # Count checkboxes
        total = content.count('- [ ] Test') + content.count('- [x] Test') + \
                content.count('- [~] Test') + content.count('- [!] Test')
        completed = content.count('- [x] Test')
        partial = content.count('- [~] Test')
        failed = content.count('- [!] Test')
        pending = content.count('- [ ] Test')

        # Update global progress section
        progress_pattern = r'```\nTotal Skills: \d+\nCompletados: \d+\nFuncionales: \d+\nParciales: \d+\nFallidos: \d+\nPendientes: \d+\n\nTasa de éxito: \d+%\n```'

        success_rate = int((completed / total * 100)) if total > 0 else 0

        new_progress = f'''```
Total Skills: {total}
Completados: {completed + partial + failed}
Funcionales: {completed}
Parciales: {partial}
Fallidos: {failed}
Pendientes: {pending}

Tasa de éxito: {success_rate}%
```'''

        content = re.sub(progress_pattern, new_progress, content)

        return content

    def _add_to_section(self, content: str, skill_name: str, result: Dict) -> str:
        """Add skill to appropriate section (Quick Wins, Attention, Blocked)

        Args:
            content: Current RESULTS.md content
            skill_name: Skill name
            result: Test result

        Returns:
            Updated content
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        if result['status'] == 'functional':
            # Add to Quick Wins
            section_pattern = r'(## ✅ Quick Wins \(Completados\)\n\n.*?\n\n```\n)(.*?)(```)'
            entry = f"- ✅ {skill_name} - {timestamp}\n"
            content = re.sub(
                section_pattern,
                rf'\1\2{entry}\3',
                content,
                flags=re.DOTALL
            )

        elif result['status'] == 'partial':
            # Add to Necesitan Atención
            section_pattern = r'(## ⚠️ Necesitan Atención \(Parciales\)\n\n.*?\n\n```\n)(.*?)(```)'
            entry = f"- ⚠️ {skill_name} - {timestamp} - {', '.join(result['criteria_failed'][:2])}\n"
            content = re.sub(
                section_pattern,
                rf'\1\2{entry}\3',
                content,
                flags=re.DOTALL
            )

        elif result['status'] == 'failed':
            # Add to Bloqueados
            section_pattern = r'(## ❌ Bloqueados \(Fallidos\)\n\n.*?\n\n```\n)(.*?)(```)'
            error_msg = result['errors'][0] if result['errors'] else "Unknown error"
            entry = f"- ❌ {skill_name} - {timestamp} - {error_msg[:50]}\n"
            content = re.sub(
                section_pattern,
                rf'\1\2{entry}\3',
                content,
                flags=re.DOTALL
            )

        return content
