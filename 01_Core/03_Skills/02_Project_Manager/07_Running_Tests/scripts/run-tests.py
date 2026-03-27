#!/usr/bin/env python3
"""
Test Runner Helper

Runs tests for skills and scripts, generating a status report.
"""

import subprocess
import sys
from pathlib import Path


def find_project_root():
    """Find the project root."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".agent").exists():
            return parent
    return Path.cwd()


def run_tests():
    """Run all available tests."""
    print("=" * 50)
    print("🧪 TEST RUNNER")
    print("=" * 50)

    project_root = find_project_root()
    tests_passed = 0
    tests_failed = 0

    # Check for Python tests
    test_dirs = list(project_root.rglob("tests/"))
    if test_dirs:
        print(f"\n📂 Found {len(test_dirs)} test directories")

        for test_dir in test_dirs:
            py_tests = list(test_dir.glob("test_*.py"))
            if py_tests:
                print(f"\n🐍 Running tests in {test_dir}")
                try:
                    result = subprocess.run(
                        [sys.executable, "-m", "pytest", str(test_dir), "-v"],
                        capture_output=True,
                        text=True,
                        timeout=60,
                    )
                    if result.returncode == 0:
                        tests_passed += 1
                        print("   ✅ PASSED")
                    else:
                        tests_failed += 1
                        print("   ❌ FAILED")
                        print(
                            result.stdout[-200:]
                            if len(result.stdout) > 200
                            else result.stdout
                        )
                except subprocess.TimeoutExpired:
                    tests_failed += 1
                    print("   ⏱️  TIMEOUT")
    else:
        print("\n⚠️  No test directories found")

    # Summary
    print("\n" + "=" * 50)
    print(f"📊 Results: {tests_passed} passed, {tests_failed} failed")
    print("=" * 50)


if __name__ == "__main__":
    run_tests()
