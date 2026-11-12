"""
Week 3 · Exercise 2: JSON and CSV
Run:  pytest week03/test_ex02_json_csv.py -v

JSON: json.dump(data, f, indent=2) / json.load(f)
CSV:  csv.DictReader / csv.DictWriter, and open(..., newline="", encoding="utf-8")
"""
import csv
import json


def save_json(path, data):
    """Save any list/dict to a JSON file, nicely indented (indent=2)."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_json(path, default):
    """Load and return the data from a JSON file.
    - File missing            -> return `default`
    - File is not valid JSON  -> return `default`   (json.JSONDecodeError)
    """
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default

def read_csv(path):
    """Return the rows of a CSV file (with a header row) as a list of dicts.
    All values stay as strings.

    title,price            ->  [{"title": "Dune", "price": "9.5"}]
    Dune,9.5
    """
    result = []
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            result.append(row)
    return result


def write_csv(path, rows, fieldnames):
    """Write a list of dicts to a CSV file: a header row first, then one row per dict."""
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def sum_column(path, column):
    """Add up a numeric column of a CSV file. Real files contain bad values, so:
    rows whose value can't be converted to a float are SKIPPED and counted.
    Return a tuple: (total rounded to 2, number of skipped rows).

    amount          ->  sum_column(path, "amount")  ->  (40.5, 1)
    30
    oops
    10.5
    """
    pass


def csv_to_json(csv_path, json_path):
    """Convert a CSV file into a JSON file (a list of dicts). Return how many rows were converted.
    Reuse your own functions above!
    """
    data = read_csv(csv_path)
    save_json(json_path, data)
    return len(data)



# ---------------------------------------------------------------------------
# EXPLAIN IT (optional)
# 1. JSON vs CSV: when would you choose each one?
# 2. Why does every value read from a CSV come back as a string?
# 3. In sum_column, why skip bad rows instead of crashing? When would crashing be better?
# ---------------------------------------------------------------------------
