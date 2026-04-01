import os
import json
import argparse


def set_project(project_name):
    active_project_file = os.path.join(
        os.path.dirname(__file__), "..", "05_System", "04_Env", "active_project.json"
    )
    os.makedirs(os.path.dirname(active_project_file), exist_ok=True)
    with open(active_project_file, "w") as f:
        json.dump({"project": project_name}, f)
    print(f"Project set to: {project_name}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Context Switcher")
    parser.add_argument("--project", help="Name of the project")
    args = parser.parse_args()

    if args.project:
        set_project(args.project)
    else:
        # Clear project
        set_project(None)
