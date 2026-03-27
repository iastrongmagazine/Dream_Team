---
model: opus
description: QUÉ HACE: Manipula y genera reportes sobre archivos CSV con integridad garantizada. CUÁNDO SE EJECUTA: Al realizar modificaciones, limpiezas o análisis de datos en formato CSV.
argument-hint: [csv_file] [user_request]
allowed-tools: Glob, Grep, Read, Edit, Write
disable-model-invocation: false
hooks:
  PostToolUse:
    - matcher: "Read|Edit|Write"
      hooks:
        - type: command
          command: "uv run $CLAUDE_PROJECT_DIR/09_System/hooks/validators/csv-single-validator.py"
---

# CSV Management Skill

Expert skill for handling CSV data manipulation, reporting, and validation.

## Purpose

Make modifications or report on csv files with guaranteed data integrity via automated `PostToolUse` validation.

## Technical Configuration (Claude Hook)

This skill is designed to work with an automated validation hook.

**Logic:**

- **Model**: Claude 3 Opus (recommended)
- **Argument Hint**: `[csv_file] [user_request]`
- **Allowed Tools**: Glob, Grep, Read, Edit, Write
- **Validation Hook**:
  - Triggers on: `Read`, `Edit`, `Write`
  - Action: Runs `uv run $CLAUDE_PROJECT_DIR/09_System/hooks/validators/csv-single-validator.py`

## Tools and Scripts

- **`scripts/csv_manager.py`**: Main utility for generating summaries, cleaning data, and converting formats.
- **`validators/csv-single-validator.py`**: Automated hook for structural integrity verification.

## Workflow

1. **Read the CSV File**: Identify the target file using `Glob` or `Grep` if necessary, then `Read` the content.
2. **Analysis/Modification**: Based on the user request, either generate a report or apply edits using `Edit`.
3. **Automated Validation**: The `PostToolUse` hook automatically validates the file structure after any modification.
4. **Report Results**: Provide a clear summary of the changes or the data analysis performed.

## Examples

### Reporting

_Task_: "Summary of sales in data.csv"

1. Read `data.csv`.
2. Calculate totals/averages.
3. Present table.

### Modification

_Task_: "Update price of item 'X' to 20 in inventory.csv"

1. Locate row in `inventory.csv`.
2. Apply `Edit`.
3. Validator confirms CSV syntax is still correct.
