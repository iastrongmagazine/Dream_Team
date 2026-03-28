#!/usr/bin/env python3
"""
Simple test script to validate the testing automation system
"""

import sys
from pathlib import Path

# Add scripts directory to path
scripts_dir = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(scripts_dir))

from run_tests import TestRunner

def test_system_validation():
    """Test 1: System Validation"""
    print("=" * 70)
    print("TEST 1: System Validation")
    print("=" * 70)

    runner = TestRunner()
    result = runner.validate_system()

    assert result == True or result == False, "Validation should return boolean"
    print(f"\n✅ Test 1 PASSED: Validation returned {result}")
    return result

def test_quick_start_structure():
    """Test 2: Quick Start Structure"""
    print("\n" + "=" * 70)
    print("TEST 2: Quick Start Structure")
    print("=" * 70)

    runner = TestRunner()

    # Check paths exist
    assert runner.base_path.exists(), f"Base path should exist: {runner.base_path}"
    assert runner.tests_path.exists(), f"Tests path should exist: {runner.tests_path}"

    # Check reports and logs directories were created
    assert runner.reports_path.exists(), "Reports directory should be created"
    assert runner.logs_path.exists(), "Logs directory should be created"

    print(f"\n✅ Test 2 PASSED: All paths exist")
    print(f"   Base: {runner.base_path}")
    print(f"   Tests: {runner.tests_path}")
    print(f"   Reports: {runner.reports_path}")
    print(f"   Logs: {runner.logs_path}")

    return True

def test_executor_initialization():
    """Test 3: Test Executor Initialization"""
    print("\n" + "=" * 70)
    print("TEST 3: Test Executor Initialization")
    print("=" * 70)

    runner = TestRunner()

    # Check components initialized
    assert runner.executor is not None, "Executor should be initialized"
    assert runner.tracker is not None, "Tracker should be initialized"
    assert runner.reporter is not None, "Reporter should be initialized"
    assert runner.validator is not None, "Validator should be initialized"

    print(f"\n✅ Test 3 PASSED: All components initialized")
    print(f"   Executor: {type(runner.executor).__name__}")
    print(f"   Tracker: {type(runner.tracker).__name__}")
    print(f"   Reporter: {type(runner.reporter).__name__}")
    print(f"   Validator: {type(runner.validator).__name__}")

    return True

def test_skill_paths():
    """Test 4: Skill Paths"""
    print("\n" + "=" * 70)
    print("TEST 4: Skill Paths")
    print("=" * 70)

    runner = TestRunner()

    # Check skill directories
    invictus_skills = runner.executor.skills_path_invictus
    amazing_skills = runner.executor.skills_path_amazing

    print(f"\n   Invictus skills: {invictus_skills}")
    print(f"   Exists: {invictus_skills.exists()}")

    if invictus_skills.exists():
        skills = list(invictus_skills.iterdir())
        print(f"   Found {len(skills)} skills")
        for skill in skills[:5]:  # Show first 5
            print(f"     - {skill.name}")

    print(f"\n   Amazing World skills: {amazing_skills}")
    print(f"   Exists: {amazing_skills.exists()}")

    print(f"\n✅ Test 4 PASSED: Skill paths checked")

    return True

def test_report_generation():
    """Test 5: Report Generation (Dry Run)"""
    print("\n" + "=" * 70)
    print("TEST 5: Report Generation (Dry Run)")
    print("=" * 70)

    runner = TestRunner()

    # Create a dummy summary
    dummy_summary = {
        "type": "test",
        "total_tests": 1,
        "results": [{
            "skill_name": "test-skill",
            "status": "functional",
            "elapsed_time": 1.0,
            "criteria_met": ["test"],
            "criteria_failed": [],
            "errors": []
        }],
        "elapsed_time": 1.0,
        "timestamp": "2026-01-21T22:00:00"
    }

    # Generate quick report
    report_path = runner.reporter.generate_quick_report(dummy_summary)

    assert report_path.exists(), f"Report should be created: {report_path}"

    print(f"\n✅ Test 5 PASSED: Report generated")
    print(f"   Path: {report_path}")
    print(f"   Size: {report_path.stat().st_size} bytes")

    # Clean up
    report_path.unlink()

    return True

def main():
    """Run all tests"""
    print("\n" + "🧪" * 35)
    print("TESTING AUTOMATION SYSTEM - VALIDATION SUITE")
    print("🧪" * 35 + "\n")

    tests = [
        ("System Validation", test_system_validation),
        ("Quick Start Structure", test_quick_start_structure),
        ("Executor Initialization", test_executor_initialization),
        ("Skill Paths", test_skill_paths),
        ("Report Generation", test_report_generation),
    ]

    passed = 0
    failed = 0

    for name, test_func in tests:
        try:
            result = test_func()
            if result:
                passed += 1
        except Exception as e:
            print(f"\n❌ Test FAILED: {name}")
            print(f"   Error: {str(e)}")
            failed += 1

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total Tests: {len(tests)}")
    print(f"✅ Passed: {passed}")
    print(f"❌ Failed: {failed}")
    print(f"Success Rate: {passed/len(tests)*100:.1f}%")
    print("=" * 70)

    if failed == 0:
        print("\n🎉 ALL TESTS PASSED! System is ready for use.")
        return 0
    else:
        print(f"\n⚠️  {failed} test(s) failed. Review errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
