import csv
import os
import argparse
import json
from typing import List, Dict, Any

class CSVManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self._validate_path()

    def _validate_path(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"CSV file not found: {self.file_path}")

    def get_summary(self) -> Dict[str, Any]:
        """Provides a quick summary of the CSV structure and content."""
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, [])
                rows = list(reader)

                return {
                    "filename": os.path.basename(self.file_path),
                    "columns": header,
                    "column_count": len(header),
                    "row_count": len(rows),
                    "size_bytes": os.path.getsize(self.file_path)
                }
        except Exception as e:
            return {"error": str(e)}

    def clean_csv(self, output_path: str = None) -> str:
        """Removes empty rows and trims whitespace from values."""
        if not output_path:
            output_path = self.file_path + ".cleaned.csv"

        try:
            cleaned_rows = []
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    if any(field.strip() for field in row):
                        cleaned_rows.append([field.strip() for field in row])

            with open(output_path, mode='w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(cleaned_rows)

            return f"Cleaned CSV saved to: {output_path}"
        except Exception as e:
            return f"Error during cleaning: {e}"

    def convert_to_json(self, output_path: str = None) -> str:
        """Converts the CSV to a JSON array of objects."""
        if not output_path:
            output_path = self.file_path.rsplit('.', 1)[0] + ".json"

        try:
            data = []
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    data.append(row)

            with open(output_path, mode='w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)

            return f"Converted JSON saved to: {output_path}"
        except Exception as e:
            return f"Error during conversion: {e}"

def main():
    parser = argparse.ArgumentParser(description="CSV Manager Utility")
    parser.add_argument("file", help="Path to the CSV file")
    parser.add_argument("--summary", action="store_true", help="Show CSV summary")
    parser.add_argument("--clean", action="store_true", help="Clean CSV (remove empty rows, trim whitespace)")
    parser.add_argument("--json", action="store_true", help="Convert CSV to JSON")
    args = parser.parse_args()

    try:
        manager = CSVManager(args.file)

        if args.summary:
            summary = manager.get_summary()
            print(json.dumps(summary, indent=2))

        if args.clean:
            result = manager.clean_csv()
            print(result)

        if args.json:
            result = manager.convert_to_json()
            print(result)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
