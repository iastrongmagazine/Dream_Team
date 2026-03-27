#!/usr/bin/env python3
"""
Report Generator - Creates test reports

Generates markdown reports for test runs including summaries,
detailed results, and recommendations.
"""

from pathlib import Path
from typing import Dict, List
from datetime import datetime


class ReportGenerator:
    """Generates test reports"""

    def __init__(self, reports_path: Path):
        """Initialize report generator

        Args:
            reports_path: Path to reports directory
        """
        self.reports_path = Path(reports_path)
        self.reports_path.mkdir(exist_ok=True)

    def generate_quick_report(self, summary: Dict) -> Path:
        """Generate quick start report

        Args:
            summary: Test summary dictionary

        Returns:
            Path to generated report
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = self.reports_path / f"quick_start_{timestamp}.md"

        functional = sum(1 for r in summary['results'] if r['status'] == 'functional')
        partial = sum(1 for r in summary['results'] if r['status'] == 'partial')
        failed = sum(1 for r in summary['results'] if r['status'] == 'failed')

        content = f"""# Quick Start Test Report

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Duration**: {summary['elapsed_time']/60:.1f} minutes
**Tests**: {summary['total_tests']}

## Summary

- ✅ Functional: {functional}
- ⚠️ Partial: {partial}
- ❌ Failed: {failed}

## Results

"""

        for result in summary['results']:
            status_emoji = "✅" if result['status'] == 'functional' else "⚠️" if result['status'] == 'partial' else "❌"
            content += f"### {status_emoji} {result['skill_name']}\n\n"
            content += f"- **Status**: {result['status'].upper()}\n"
            content += f"- **Time**: {result['elapsed_time']:.1f}s\n"
            if result['criteria_met']:
                content += f"- **Criteria Met**: {len(result['criteria_met'])}\n"
            if result['criteria_failed']:
                content += f"- **Criteria Failed**: {len(result['criteria_failed'])}\n"
            if result['errors']:
                content += f"- **Errors**: {', '.join(result['errors'])}\n"
            content += "\n"

        content += f"\n## Recommendation\n\n"
        if failed == 0:
            content += "✅ **GO**: All tests passed or partial. Safe to proceed with full suite.\n"
        else:
            content += "⚠️ **REVIEW**: Some tests failed. Investigate before full suite.\n"

        report_path.write_text(content, encoding='utf-8')
        return report_path

    def generate_phase_report(self, summary: Dict) -> Path:
        """Generate phase report

        Args:
            summary: Phase summary dictionary

        Returns:
            Path to generated report
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = self.reports_path / f"phase_{summary['phase_num']}_{timestamp}.md"

        functional = sum(1 for r in summary['results'] if r['status'] == 'functional')
        partial = sum(1 for r in summary['results'] if r['status'] == 'partial')
        failed = sum(1 for r in summary['results'] if r['status'] == 'failed')

        content = f"""# Phase {summary['phase_num']}: {summary['phase_name']} Report

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Tests**: {len(summary['results'])}

## Summary

- ✅ Functional: {functional}
- ⚠️ Partial: {partial}
- ❌ Failed: {failed}

## Detailed Results

"""

        for i, result in enumerate(summary['results'], 1):
            status_emoji = "✅" if result['status'] == 'functional' else "⚠️" if result['status'] == 'partial' else "❌"
            content += f"### Test {i}: {status_emoji} {result['skill_name']}\n\n"
            content += f"- **Status**: {result['status'].upper()}\n"
            content += f"- **Time**: {result['elapsed_time']:.1f}s\n"
            content += "\n"

        report_path.write_text(content, encoding='utf-8')
        return report_path

    def generate_full_report(self, summary: Dict) -> Path:
        """Generate full suite report

        Args:
            summary: Full suite summary dictionary

        Returns:
            Path to generated report
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = self.reports_path / f"full_suite_{timestamp}.md"

        functional = sum(1 for r in summary['results'] if r['status'] == 'functional')
        partial = sum(1 for r in summary['results'] if r['status'] == 'partial')
        failed = sum(1 for r in summary['results'] if r['status'] == 'failed')
        success_rate = (functional / summary['total_tests'] * 100) if summary['total_tests'] > 0 else 0

        content = f"""# Full Test Suite Report

**Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Duration**: {summary['elapsed_time']/3600:.2f} hours
**Tests**: {summary['total_tests']}
**Success Rate**: {success_rate:.1f}%

## Executive Summary

- ✅ Functional: {functional} ({functional/summary['total_tests']*100:.1f}%)
- ⚠️ Partial: {partial} ({partial/summary['total_tests']*100:.1f}%)
- ❌ Failed: {failed} ({failed/summary['total_tests']*100:.1f}%)

## All Results

"""

        for i, result in enumerate(summary['results'], 1):
            status_emoji = "✅" if result['status'] == 'functional' else "⚠️" if result['status'] == 'partial' else "❌"
            content += f"{i}. {status_emoji} **{result['skill_name']}** - {result['status'].upper()} ({result['elapsed_time']:.1f}s)\n"

        content += "\n## Recommendations\n\n"
        if failed == 0:
            content += "✅ Excellent! All skills are functional or partially working.\n"
        elif failed <= 3:
            content += "⚠️ A few skills need attention. Review failed tests.\n"
        else:
            content += "❌ Multiple skills failing. System needs review.\n"

        report_path.write_text(content, encoding='utf-8')
        return report_path
