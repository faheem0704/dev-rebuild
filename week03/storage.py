import json
import logging
import csv
from pathlib import Path

HERE = Path(__file__).parent
CSV_FILE = HERE / "expenses.csv"
EXPENSES_FILE = HERE / "expenses.json"


def load_expenses(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: the expense file is damaged. Starting with an empty list.")
        logging.warning("Could not read %s, starting with an empty list", path)
        return []


def save_expenses(path, expenses):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)

def export_expenses(path, expenses):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["description", "amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    return f"Exported {len(expenses)} expenses to {path.name}"

