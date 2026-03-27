import sys
import subprocess
import os
from config_paths import ROOT_DIR


def run_audit(audit_script, subprocess_module=subprocess):
    """Ejecuta el script de auditoría y retorna el resultado."""
    print(f"Running audit: {audit_script}...")
    try:
        result = subprocess_module.run([sys.executable, audit_script])
        return result
    except Exception as e:
        print(f"Error running audit script: {e}")
        return None


def run_git_commit(git_args, subprocess_module=subprocess):
    """Ejecuta el commit de git."""
    print(f"Running: {' '.join(git_args)}")
    try:
        subprocess_module.run(git_args, check=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Git commit failed: {e}")
        return e.returncode


def main(subprocess_module=subprocess):
    # Path to the audit script
    audit_script = os.path.join(ROOT_DIR, "04_Engine", "08_Scripts_Os", "42_Audit_Engineering.py")

    # 1. Run the audit script
    audit_result = run_audit(audit_script, subprocess_module)
    if audit_result is None:
        sys.exit(1)

    # 2. Check exit code
    if audit_result.returncode != 0:
        print("COMMIT ABORTED: System not Pure Green")
        sys.exit(1)

    # 3. Run git commit with arguments
    git_args = ["git", "commit"] + sys.argv[1:]
    exit_code = run_git_commit(git_args, subprocess_module)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
