# Progress Log

Started: 2026-10-27, the day after the interview. This is day one.

## Gates passed
| Week | Gate | Date passed | Notes |
|---|---|---|---|
| 0 | Setup: venv, pytest, Git, GitHub push | 2026-10-28 | Repo `dev-rebuild` pushed to GitHub ✅ |
| 1 | week01 tests green + Guessing Game & Calculator + from-memory rewrites | | ex01 ✅ 15/15 (2026-10-31) · ex02 ⬜ · ex03 ⬜ · project ⬜ · rewrites ⬜ |
| 2 | week02 tests green + Expense Tracker + 4 interview Qs scored ≥ 4/5 | | |

## Weak spots (things to re-review; Claude adds these after quizzes)
- **`round()` vs f-string**: mixed them up twice (circle_area, then the first discount attempt). Rule: number for calculating → `round(x, 2)`; text for display → `f"{x:.2f}"`.
- **Checking with only one example**: two formulas passed with the number 100 by luck. Check with 2–3 awkward numbers (37, 250) by hand.
- **`print` vs `return`**: return hands the value back; print only shows it.
- **Reading a one-line `if/else`**: swapped the two results in `to_number`. Read it aloud as a sentence.
- **EXPLAIN IT questions in ex01**: not answered yet.

## Mistake journal (every bug you hit = one line. This becomes gold before interviews)
| Date | What went wrong | Why | Lesson |
|---|---|---|---|
| 2026-10-29 | Code "wasn't there" when reviewed | File not saved in VS Code | Ctrl+S / turn on Auto Save |
| 2026-10-30 | `area(:.2f)` → SyntaxError, and NO tests ran | Format codes only work inside f-string `{}` | One syntax error breaks the whole file. `round()` = number, f-string = text |
| 2026-10-30 | circle_area used `3.14` | Not precise enough; 2nd decimal was wrong | Use `math.pi` (needs `import math` at the top) |
| 2026-10-31 | seconds_to_hms test got `None` | Used `print` instead of `return` | A function without `return` gives back `None` |
| 2026-10-31 | Wrong minutes/seconds | Divided `h` and `m` instead of the seconds | Trace each variable's value line by line on paper |
| 2026-10-31 | Discount formula right only for price 100 | Tested with one easy example (100 hides mistakes) | Check formulas with awkward numbers |
| 2026-10-31 | `IndentationError: unexpected indent` | `return` indented further than its block | Indentation is part of Python's meaning |
| 2026-10-31 | `to_number("42")` returned `42.0` | int/float swapped in the `if/else` | Read the condition out loud; trace one input |

## Concepts learned so far
- `/` vs `//` vs `%`, `**`, operator precedence
- `import math`, `math.pi`, `round(x, 2)`
- f-strings: `{x:.2f}` (2 decimals), `{x:02d}` (pad to 2 digits)
- `divmod()` returns a **tuple** (ordered), not a set → indexing `[0]` / unpacking `a, b = ...`
- percent = per hundred → `discount_percent / 100 * price`
- default parameters (`currency="AED"`)
- one-line conditional: `a if condition else b`, and `max(x, 0)` as an alternative
- `.strip()` returns a NEW string (strings are immutable); `"." in text` → `True`/`False`
- `int()` vs `float()` conversion

## Daily log
### 2026-10-28 | Week 1 Day 1
- **Built / committed:** Day 0 setup done: venv, pytest, Git, pushed to GitHub. Started `play.py` (input + f-string).
- **Tomorrow:** make `play.py` actually calculate age + 10.

### 2026-10-29 | Week 1 Day 2
- **Built:** `celsius_to_fahrenheit` ✅ (first green function!)
- **Learned:** return vs print, PEP 8 naming (lowercase variables).

### 2026-10-30 | Week 1 Day 2–3
- **Built:** `circle_area` ✅ after a SyntaxError.
- **Learned:** `import`, `math.pi`, `round()` vs f-string formatting.

### 2026-10-31 | Week 1 Day 3 | hours: _
- **Learned:** `//` and `%`, `divmod` + tuple unpacking, tuple vs set, percentages, default parameters, one-line conditionals, `.strip()`, `in`.
- **Built:** `seconds_to_hms`, `price_after_discount`, `format_receipt_line`, `age_from_birth_year`, `to_number` → **ex01 complete, 15/15 green** 🎉
- **Watched:** CS50P Lecture 1: Conditionals ✅
- **Confused me:** Job 2 of `to_number` (how to make Python decide between two options).
- **Explained out loud:** _
- **Tomorrow:** commit ex01 · answer ex01 EXPLAIN IT · start `ex02_conditions_loops.py` (`grade`, `is_prime`).

<!-- Copy this block each day -->
### YYYY-MM-DD | Week _ Day _ | hours: _
- **Learned:**
- **Built / committed:**
- **Confused me:**
- **Explained out loud:**
- **Tomorrow:**
