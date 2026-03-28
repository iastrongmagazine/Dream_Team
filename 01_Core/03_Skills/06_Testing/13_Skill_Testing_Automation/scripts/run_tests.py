#!/usr/bin/env python3
"""
Skill Testing Automation - Main Test Runner

This script orchestrates the execution of skill tests, manages results,
and generates reports.

Usage:
    python run_tests.py --quick              # Run 3 essential skills
    python run_tests.py --full               # Run all 23 skills
    python run_tests.py --phase 1            # Run specific phase
    python run_tests.py --skill brainstorming # Run specific skill
    python run_tests.py --report             # Generate report only
"""

import argparse
import json
import sys
import io
from pathlib import Path
from datetime import datetime

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    # Usar modo compatible
    pass
from typing import List, Dict, Optional
import time

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from test_executor import TestExecutor
from result_tracker import ResultTracker
from report_generator import ReportGenerator
from skill_validator import SkillValidator


class TestRunner:
    """Main test runner orchestrator"""

    def __init__(self, base_path: Optional[Path] = None):
        """Initialize test runner

        Args:
            base_path: Base path to Amazing_World directory
        """
        if base_path is None:
            # Assume we're in 07_Skill/skill-testing-automation/scripts/
            # Go up 5 levels: scripts -> 12_skill -> 07_Skill -> 02_Voldemort -> Amazing_World
            self.base_path = Path(__file__).parent.parent.parent.parent.parent
        else:
            self.base_path = Path(base_path)

        # Adjusted paths for 2026 structure
        self.tests_path = self.base_path / "02_Voldemort_Backend" / "05_Examples" / "tests"
        self.results_path = self.tests_path / "RESULTS.md"
        self.reports_path = self.base_path / ".claude" / "reports"
        self.logs_path = self.base_path / ".claude" / "logs"

        # Create directories if they don't exist
        self.reports_path.mkdir(exist_ok=True, parents=True)
        self.logs_path.mkdir(exist_ok=True, parents=True)

        # Initialize components
        self.executor = TestExecutor(self.base_path)
        self.tracker = ResultTracker(self.results_path)
        self.reporter = ReportGenerator(self.reports_path)
        self.validator = SkillValidator(self.base_path)

    def run_quick_start(self) -> Dict:
        """Run quick start tests (3 essential skills)

        Returns:
            Dict with test results
        """
        print("Running Quick Start Tests (3 skills, ~15 minutes)")
        print("=" * 60)

        quick_tests = [
            {
                "name": "brainstorming",
                "location": "Amazing World/07_Skill/brainstorming",
                "exercise": "Sistema de notificaciones push para usuarios"
            },
            {
                "name": "content-creation",
                "location": "Invictus/07_Skill/content-creation",
                "exercise": "Hilo de 5 tweets sobre 'Productividad con IA'"
            },
            {
                "name": "systematic-debugging",
                "location": "Amazing World/07_Skill/systematic-debugging",
                "exercise": "TypeError: Cannot read property 'name' of undefined"
            }
        ]

        results = []
        start_time = time.time()

        for i, test in enumerate(quick_tests, 1):
            print(f"\n[{i}/3] Testing: {test['name']}")
            print("-" * 60)

            result = self.executor.execute_test(
                skill_name=test['name'],
                exercise=test['exercise'],
                location=test['location']
            )

            results.append(result)
            self.tracker.update_result(test['name'], result)

            status_emoji = "[OK]" if result['status'] == 'functional' else "[WARN]" if result['status'] == 'partial' else "[ERR]"
            print(f"{status_emoji} {test['name']}: {result['status'].upper()}")

        elapsed = time.time() - start_time

        summary = {
            "type": "quick_start",
            "total_tests": 3,
            "results": results,
            "elapsed_time": elapsed,
            "timestamp": datetime.now().isoformat()
        }

        # Generate report
        report_path = self.reporter.generate_quick_report(summary)

        print("\n" + "=" * 60)
        print(f"✅ Quick Start Complete in {elapsed/60:.1f} minutes")
        print(f"📊 Report: {report_path}")
        print(f"📝 Results updated in: {self.results_path}")

        return summary

    def run_full_suite(self, parallel: bool = False) -> Dict:
        """Run full test suite (23 skills)

        Args:
            parallel: Whether to run independent tests in parallel

        Returns:
            Dict with test results
        """
        print("Running Full Test Suite (23 skills, ~4-5 hours)")
        print("=" * 60)

        # Load all test definitions
        test_definitions = self._load_all_tests()

        results = []
        start_time = time.time()

        for phase_num, phase in enumerate(test_definitions, 1):
            print(f"\n📋 Phase {phase_num}: {phase['name']} ({len(phase['tests'])} tests)")
            print("=" * 60)

            phase_results = []

            for i, test in enumerate(phase['tests'], 1):
                print(f"\n[{i}/{len(phase['tests'])}] Testing: {test['skill_name']}")
                print("-" * 60)

                result = self.executor.execute_test(
                    skill_name=test['skill_name'],
                    exercise=test['exercise'],
                    location=test['location'],
                    criteria=test.get('criteria', [])
                )

                phase_results.append(result)
                results.append(result)
                self.tracker.update_result(test['skill_name'], result)

                status_emoji = "[OK]" if result['status'] == 'functional' else "[WARN]" if result['status'] == 'partial' else "[ERR]"
                print(f"{status_emoji} {test['skill_name']}: {result['status'].upper()}")

            # Generate phase report
            phase_summary = {
                "phase_num": phase_num,
                "phase_name": phase['name'],
                "results": phase_results
            }
            self.reporter.generate_phase_report(phase_summary)

        elapsed = time.time() - start_time

        summary = {
            "type": "full_suite",
            "total_tests": 23,
            "results": results,
            "elapsed_time": elapsed,
            "timestamp": datetime.now().isoformat()
        }

        # Generate final report
        report_path = self.reporter.generate_full_report(summary)

        print("\n" + "=" * 60)
        print("Done. Full Suite Complete")
        print(f"📊 Report: {report_path}")
        print(f"📝 Results updated in: {self.results_path}")

        return summary

    def run_phase(self, phase_num: int) -> Dict:
        """Run tests for a specific phase

        Args:
            phase_num: Phase number (1-7)

        Returns:
            Dict with test results
        """
        print(f"Running Phase {phase_num} Tests")
        print("=" * 60)

        # Load phase tests
        phase_tests = self._load_phase_tests(phase_num)

        if not phase_tests:
            print(f"❌ Phase {phase_num} not found")
            return {}

        results = []
        start_time = time.time()

        for i, test in enumerate(phase_tests['tests'], 1):
            print(f"\n[{i}/{len(phase_tests['tests'])}] Testing: {test['skill_name']}")
            print("-" * 60)

            result = self.executor.execute_test(
                skill_name=test['skill_name'],
                exercise=test['exercise'],
                location=test['location'],
                criteria=test.get('criteria', [])
            )

            results.append(result)
            self.tracker.update_result(test['skill_name'], result)

            status_emoji = "[OK]" if result['status'] == 'functional' else "[WARN]" if result['status'] == 'partial' else "[ERR]"
            print(f"{status_emoji} {test['skill_name']}: {result['status'].upper()}")

        elapsed = time.time() - start_time

        summary = {
            "type": "phase",
            "phase_num": phase_num,
            "phase_name": phase_tests['name'],
            "total_tests": len(results),
            "results": results,
            "elapsed_time": elapsed,
            "timestamp": datetime.now().isoformat()
        }

        # Generate phase report
        report_path = self.reporter.generate_phase_report(summary)

        print("\n" + "=" * 60)
        print(f"✅ Phase {phase_num} Complete in {elapsed/60:.1f} minutes")
        print(f"📊 Report: {report_path}")

        return summary

    def run_single_skill(self, skill_name: str) -> Dict:
        """Run test for a single skill

        Args:
            skill_name: Name of the skill to test

        Returns:
            Dict with test result
        """
        print(f"Testing Skill: {skill_name}")
        print("=" * 60)

        # Find test definition
        test_def = self._find_test_definition(skill_name)

        if not test_def:
            print(f"❌ Test definition not found for: {skill_name}")
            return {}

        start_time = time.time()

        result = self.executor.execute_test(
            skill_name=test_def['skill_name'],
            exercise=test_def['exercise'],
            location=test_def['location'],
            criteria=test_def.get('criteria', [])
        )

        self.tracker.update_result(skill_name, result)

        elapsed = time.time() - start_time

        status_emoji = "[OK]" if result['status'] == 'functional' else "[WARN]" if result['status'] == 'partial' else "[ERR]"
        print(f"\n{status_emoji} {skill_name}: {result['status'].upper()}")
        print(f"⏱️  Completed in {elapsed:.1f} seconds")

        return result

    def validate_system(self) -> bool:
        """Validate system before running tests

        Returns:
            True if system is valid, False otherwise
        """
        print("Validating System...")
        print("=" * 60)

        validation_results = self.validator.validate_all()

        all_valid = True
        for check, result in validation_results.items():
            status = "[OK]" if result['valid'] else "[ERR]"
            print(f"{status} {check}: {result['message']}")
            if not result['valid']:
                all_valid = False

        print("=" * 60)

        if all_valid:
            print("System validation passed")
        else:
            print("System validation failed - fix issues before running tests")

        return all_valid

    def _load_all_tests(self) -> List[Dict]:
        """Load all test definitions from test files

        Returns:
            List of phase dictionaries with test definitions
        """
        # This is a simplified version - in production, parse from markdown files
        phases = [
            {
                "name": "Planificación y Diseño",
                "tests": [
                    {"skill_name": "brainstorming", "exercise": "...", "location": "...", "criteria": []},
                    # ... more tests
                ]
            },
            # ... more phases
        ]
        return phases

    def _load_phase_tests(self, phase_num: int) -> Optional[Dict]:
        """Load tests for a specific phase

        Args:
            phase_num: Phase number (1-7)

        Returns:
            Phase dictionary with tests, or None if not found
        """
        all_phases = self._load_all_tests()
        if 1 <= phase_num <= len(all_phases):
            return all_phases[phase_num - 1]
        return None

    def _find_test_definition(self, skill_name: str) -> Optional[Dict]:
        """Find test definition for a specific skill

        Args:
            skill_name: Name of the skill

        Returns:
            Test definition dict, or None if not found
        """
        all_phases = self._load_all_tests()
        for phase in all_phases:
            for test in phase['tests']:
                if test['skill_name'] == skill_name:
                    return test
        return None


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="Skill Testing Automation - Run automated tests for skills"
    )

    parser.add_argument(
        '--quick',
        action='store_true',
        help='Run quick start tests (3 skills, ~15 min)'
    )

    parser.add_argument(
        '--full',
        action='store_true',
        help='Run full test suite (23 skills, ~4-5 hours)'
    )

    parser.add_argument(
        '--phase',
        type=int,
        choices=range(1, 8),
        help='Run specific phase (1-7)'
    )

    parser.add_argument(
        '--skill',
        type=str,
        help='Run test for specific skill'
    )

    parser.add_argument(
        '--validate',
        action='store_true',
        help='Validate system before running tests'
    )

    parser.add_argument(
        '--report',
        action='store_true',
        help='Generate report from existing results'
    )

    parser.add_argument(
        '--parallel',
        action='store_true',
        help='Run independent tests in parallel (full suite only)'
    )

    args = parser.parse_args()

    # Initialize runner
    runner = TestRunner()

    # Validate system if requested
    if args.validate or args.full:
        if not runner.validate_system():
            sys.exit(1)

    # Execute requested action
    if args.quick:
        runner.run_quick_start()
    elif args.full:
        runner.run_full_suite(parallel=args.parallel)
    elif args.phase:
        runner.run_phase(args.phase)
    elif args.skill:
        runner.run_single_skill(args.skill)
    elif args.report:
        print("📊 Generating report from existing results...")
        # TODO: Implement report-only generation
    elif not args.validate:
        parser.print_help()


if __name__ == "__main__":
    main()
