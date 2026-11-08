# Week 3 Project: Expense Tracker v6 (saving, modules, tests)

Upgrade your Week 2 tracker into something closer to real software. Copy `week02/expense_tracker.py` into `week03/` as a starting point.

**Proves you can:** save and load data, organise code into modules, and protect it with your own tests.

## Requirements
1. **It remembers.** Expenses are saved to `expenses.json`:
   - **load** at start-up (a missing file → start with an empty list; a broken file → start empty **and warn the user**),
   - **save** after every change (add, delete).
2. **Split into 3 modules** (files), each with one kind of job:
   | File | Job | Contains |
   |---|---|---|
   | `storage.py` | talk to the disk | `load_expenses(path)`, `save_expenses(path, expenses)` |
   | `expenses.py` | pure calculations, no `input()`/`print()` | `total_by_category`, `biggest_expense`, `make_expense(description, amount, category)` … |
   | `tracker.py` | talk to the user | menu, `get_amount`, `get_text`, the display functions, `main()` and the `__name__` guard |
   `tracker.py` uses `from expenses import ...` and `from storage import ...`.
3. **Tests:** `test_expenses.py` with **at least 10 tests** for `expenses.py` and `storage.py` (use `tmp_path` for storage tests). No tests for `input()`/`print()` code; that's why the pure functions live in their own module.
4. **Logging:** use the `logging` module to write a line to `tracker.log` when the JSON file is broken, and when an expense is deleted.
   ```python
   import logging
   logging.basicConfig(filename="tracker.log", level=logging.INFO,
                       format="%(asctime)s %(levelname)s %(message)s")
   logging.info("Deleted expense: %s", description)
   logging.warning("Could not read %s, starting empty", path)
   ```
5. Everything from Week 2 still works (validation, Ctrl+C, empty cases).

## Stretch goals (pick at least 1)
- **Export to CSV** (menu option): `expenses.csv` with a header row
- **Import from CSV:** add expenses from a CSV file; bad rows are skipped and counted ("Imported 12, skipped 2")
- **Dates:** store the date of each expense (`datetime.date.today().isoformat()`) and show totals for one month

## Done =
- `pytest week03` green (exercises + your tracker tests)
- Close the program, open it again, and your expenses are still there
- Break it: delete `expenses.json`, then write `{oops` into it; neither should crash
- Committed and pushed
