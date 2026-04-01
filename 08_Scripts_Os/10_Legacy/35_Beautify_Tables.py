import sys
import re
import os
import subprocess
import io
from colorama import init, Fore, Style

# Initialize Colorama
init()

# =============================================================================
# ARMOR LAYER - PATH RESOLUTION (3-LEVEL)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

def dynamic_speak(text):
    """Interfaz de Voz SOTA v2.2"""
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")
    if sys.platform == "win32":
        try:
            cmd = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def print_banner():
    banner = rf"""
{Fore.MAGENTA}    ###########################################################################
    #                                                                         #
    #      ____  ______       _    _ _______ _____ ________     __            #
    #     |  _ \|  ____|/\   | |  | |__   __|_   _|  ____\ \   / /            #
    #     | |_) | |__  /  \  | |  | |  | |    | | | |__   \ \_/ /             #
    #     |  _ <|  __|/ /\ \ | |  | |  | |    | | |  __|   \   /              #
    #     | |_) | |__/ ____ \| |__| |  | |   _| |_| |       | |               #
    #     |____/|____/_/    \_\____/   |_|  |_____|_|       |_|               #
    #                                                                         #
    #                        B E A U T I F I E R                              #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

ROOT_DIR = PROJECT_ROOT


def align_table(table_block):
    lines = table_block.strip().split("\n")
    if len(lines) < 2:
        return table_block

    # Parse rows
    rows = []
    for line in lines:
        # Split by pipe, but we need to handle the outer pipes correctly
        # Assuming standard markdown table format like | val | val |
        if not line.strip().startswith("|"):
            return table_block  # Not a standard pipe table

        # Split and strip whitespace
        cells = [c.strip() for c in line.split("|")]

        # Usually split('|') on "| a | b |" gives ["", "a", "b", ""]
        if cells and cells[0] == "":
            cells.pop(0)
        if cells and cells[-1] == "":
            cells.pop(-1)

        rows.append(cells)

    if not rows:
        return table_block

    # Calculate max width for each column
    col_widths = {}
    for row in rows:
        for i, cell in enumerate(row):
            # Check length of cell, treat emojis as 1 char? No, len() is usually fine for monospace
            # But specific complex emojis might be wide. Python len() is decent enough.
            col_widths[i] = max(col_widths.get(i, 0), len(cell))
            # Separator lines (---) need to be at least 3 chars
            if set(cell) == {"-"}:  # It's a separator line
                col_widths[i] = max(col_widths.get(i, 0), 3)

    # Reconstruct lines
    new_lines = []
    for row in rows:
        new_row = "|"
        for i, cell in enumerate(row):
            width = col_widths.get(i, 0)

            # Formatting separator line
            if set(cell) == {"-"} or (set(cell) == {"-", ":"} and len(cell) > 1):
                # Handle align markers :---, ---:, :---:
                # For simplicity in this script, we just standardise to dashes or preserve colons if sophisticated logic added
                # But simple version: just fill with dashes
                content = "-" * (width + 2)
            else:
                content = f" {cell.ljust(width)} "

            new_row += content + "|"
        new_lines.append(new_row)

    return "\n".join(new_lines)


def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}: Not found")
        return

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    original_content = content

    # Simple state machine parser
    new_lines = []
    current_table = []
    in_table = False

    for line in content.splitlines():
        is_table_row = line.strip().startswith("|") and "|" in line

        if is_table_row:
            current_table.append(line)
            in_table = True
        else:
            if in_table:
                # Process the accumulated table
                table_block = "\n".join(current_table)
                # For safety, blindly validating it looks like a table
                if len(current_table) >= 2 and any("---" in l for l in current_table):
                    new_lines.append(align_table(table_block))
                else:
                    new_lines.extend(current_table)
                current_table = []
                in_table = False

            new_lines.append(line)

    # Handle case where file ends exactly with a table
    if in_table and current_table:
        table_block = "\n".join(current_table)
        if len(current_table) >= 2 and any("---" in l for l in current_table):
            new_lines.append(align_table(table_block))
        else:
            new_lines.extend(current_table)

    new_content = "\n".join(new_lines) + "\n"  # Ensure single trailing newline

    if new_content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"{Fore.GREEN}Beautified: {os.path.basename(file_path)}{Style.RESET_ALL}")
        dynamic_speak(f"Tabla embellecida en {os.path.basename(file_path)}")
    else:
        print(f"{Fore.CYAN}Already perfect: {os.path.basename(file_path)}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(
            "Usage: python 29_beautify_tables.py target=<file_path> or just <file_path>"
        )
        sys.exit(1)

    target = sys.argv[1]
    if target.startswith("target="):
        target = target.split("=")[1]

    process_file(target)
