# Week 2 Project: CLI Expense Tracker

Build this in `week02/expense_tracker.py` **from a blank file**. No tests are given. Test it by using it, and try to break it.

## Requirements
1. A menu loop that runs until the user chooses Quit:
   ```
   1) Add expense   2) List expenses   3) Totals by category   4) Biggest expense   5) Quit
   ```
2. **Add expense:** ask for description, amount, and category. Store each expense as a dict in a list.
3. **List expenses:** print a numbered, aligned table (f-string padding: `f"{desc:<20}{amount:>10.2f}"`).
4. **Totals by category:** reuse your `total_by_category` idea from ex01_collections, plus a grand total.
5. **Biggest expense:** show the single largest expense.
6. **Input validation, so it never crashes:**
   - amount that isn't a number → friendly message, ask again (use `try/except ValueError`)
   - negative or zero amount → reject it
   - empty description → reject it
   - invalid menu choice → message, show the menu again
7. **One function per operation** (`add_expense(expenses)`, `list_expenses(expenses)`, …). The main loop should be short.
8. Use `if __name__ == "__main__": main()` at the bottom (look up why).

## Stretch goals (pick at least 1)
- Delete an expense by number
- Filter the list by category
- Monthly budget: warn when the total exceeds it
- Sort the list by amount or description

## Break it on purpose
Before you call it done, type in: letters for the amount, `-50`, an empty string, `999999999999`, menu option `7`, and press Ctrl+C. Decide how each should behave and fix it.

## Done = committed to Git, with a short note in `PROGRESS.md` on what was hardest.
(In week 3 you will make it save to a JSON file and split it into modules.)
