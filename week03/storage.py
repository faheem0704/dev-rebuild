import json
from pathlib import Path

HERE = Path(__file__).parent
EXPENSES_FILE = HERE / "expenses.json"


def load_expenses(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: the expense file is damaged. Starting with an empty list.")
        return []


def save_expenses(path, expenses):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2)

