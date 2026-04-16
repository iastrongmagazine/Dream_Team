import os


def generate_tree(path, prefix=""):
    items = sorted(os.listdir(path))
    items = [item for item in items if not item.startswith(".") and item != "tree.txt"]
    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1
        connector = "+-- " if is_last else "|-- "
        print(f"{prefix}{connector}{item}")
        if os.path.isdir(full_path):
            generate_tree(full_path, prefix + ("    " if is_last else "|   "))


dirs = [
    "00_Core",
    "01_Brain",
    "04_Operations",
    "03_Knowledge",
    "04_Operations",
    "05_System",
    "06_Archive",
]
for d in dirs:
    print(f"Generating tree for {d}...")
    with open(os.path.join(d, "tree.txt"), "w") as f:
        import sys

        old_stdout = sys.stdout
        sys.stdout = f
        print(f"{d}/")
        generate_tree(d)
        sys.stdout = old_stdout
