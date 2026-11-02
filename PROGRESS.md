# Progress Log

Started: 2026-10-27, the day after the interview. This is day one.

## Gates passed
| Week | Gate | Date passed | Notes |
|---|---|---|---|
| 0 | Setup: venv, pytest, Git, GitHub push | 2026-10-28 | Repo `dev-rebuild` pushed to GitHub ✅ |
| 1 | week01 tests green + Guessing Game & Calculator + from-memory rewrites | | ex01 ✅ 15/15 · ex02 ✅ 34/34 (2026-11-01) · ex03 ✅ 17/17 (2026-11-02): all week01 tests 66/66 · project ⬜ · rewrites ⬜ · EXPLAIN IT ⬜ |
| 2 | week02 tests green + Expense Tracker + 4 interview Qs scored ≥ 4/5 | | |

## Videos watched
- [x] CS50P Lecture 0: Functions, Variables
- [x] CS50P Lecture 1: Conditionals (2026-10-31)
- [x] CS50P Lecture 2: Loops (2026-11-01)
- [ ] Corey Schafer: Strings + Slicing (Day 5). Tick this if you watched them.
- [ ] CS50P Lecture 3: Exceptions (Week 2)

## Weak spots (things to re-review; Claude adds these after quizzes)
- **`round()` vs f-string**: mixed them up twice. Number for calculating → `round(x, 2)`; text for display → `f"{x:.2f}"`.
- **Checking with only one example**: two formulas passed with 100 by luck. Check with 2–3 awkward numbers by hand.
- **`print` vs `return`**: return hands the value back; print only shows it.
- **Loop boundaries (off-by-one)**: `range(start, stop)` EXCLUDES stop. Check the first and last value of every loop.
- **`or` with strings**: `x == 'a' or 'e'` is always True. Use `x in "ae"`.
- **The two meanings of `in`**: `for x in items:` loops; `x in items` asks True/False.
- **Running the tests yourself before asking for review**: several reviews were for code with a SyntaxError.
- **Trailing whitespace / 2 blank lines between functions**: flagged in 4 reviews. Turn on VS Code "trim trailing whitespace".
- **Committing**: only 2 commits so far. Commit every time something turns green.
- **EXPLAIN IT answers** (gate needs ≥ 4 each): ex01 3 / 4 / 4 (not rewritten yet) · ex02 4 / 4 / 4 ✅ after fixes (2026-11-02) · ex03 4 / 4.5 / **2**. Pattern: concepts mostly right, but **examples from my own code** and **the follow-up/gotcha** are missing. ex03 Q3 missed the real reason (performance: immutability → `+=` copies everything each time).

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
| 2026-10-31 | grade: `'invalid' == 'Invalid'` failed | Strings are case-sensitive | Copy the spec's exact text; read the `^` marker in the error |
| 2026-10-31 | sum_of_digits froze (infinite loop) on `-56` | `//` rounds down, so `-1 // 10` stays `-1` | Check every `while` loop ends for negatives/zero; Ctrl+C stops a frozen program |
| 2026-10-31 | Named a variable `sum` | Hides the built-in `sum()` function | Never name variables `sum`, `list`, `str`, `max`, `input`, `type` |
| 2026-10-31 | `results[]` → SyntaxError | Forgot `=` to assign | Create a variable with `name = value`; colons only open blocks |
| 2026-10-31 | fizzbuzz started at 0 / missed n | `range(n)` starts at 0; `range(1, n)` stops before n | Off-by-one: `range(1, n + 1)` for 1..n |
| 2026-10-31 | fizzbuzz returned after 1 item | `return` indented inside the loop | `return` goes AFTER the loop, at the `for`'s level |
| 2026-10-31 | fizzbuzz appended `1` not `'1'`, `"buzz"` not `"Buzz"` | int vs str; case-sensitivity | `str()` turns numbers into text; match the spec exactly |
| 2026-10-31 | Typed `1 % 5` instead of `i % 5` | The digit 1 looks like the letter i | Silent bugs: code runs but is wrong; tests catch them |
| 2026-10-31 | `letter == 'a' or 'e'` counted every letter | Each side of `or` is separate; `'e'` alone is truthy | Repeat the full comparison, or use `letter in "aeiou"` |
| 2026-10-31 | `for "aeiou" in text:` → SyntaxError | Mixed the two meanings of `in` | `for x in items:` loops; `x in items` asks True/False |
| 2026-11-01 | guessing game returned "Out of tries" after the 1st wrong guess | `else: return` inside the loop ends the function early | Decide "not found" only AFTER the loop |
| 2026-11-01 | Slice kept 4 guesses instead of 3 | Used `+1` like in `range` | `[:k]` gives exactly k items |
| 2026-11-02 | "Never odd or even" not a palindrome | `.strip()` only removes spaces at the ends | `.replace(" ", "")` removes all spaces |
| 2026-11-02 | `AttributeError: 'list' object has no attribute 'join'` | `join` is a string method | `"sep".join(list)`; AttributeError = method called on the wrong type |
| 2026-11-02 | Extra spaces made empty words | `.split(" ")` splits on every single space | `.split()` with no argument handles any whitespace |
| 2026-11-02 | `initials`: UnboundLocalError, then only the last letter was kept | Looped over `result` instead of `words`; `=` overwrote instead of adding | Start empty before the loop, `+=` inside (accumulator) |
| 2026-11-02 | ex03 Q3: explained `join` by separators only | Missed the real reason | Immutable strings → `+=` copies everything each time → O(n²); `join` is O(n) |

## Concepts learned so far
- `/` vs `//` vs `%`, `**`, operator precedence
- `import math`, `math.pi`, `round(x, 2)`
- f-strings: `{x:.2f}`, `{x:02d}`, and calculations inside `{}` like `{n * i}`
- `divmod()` returns a **tuple** (ordered), not a set → indexing `[0]` / unpacking `a, b = ...`
- percent = per hundred → `discount_percent / 100 * price`
- default parameters (`currency="AED"`, `upto=10`)
- one-line conditional: `a if condition else b`, and `max(x, 0)` as an alternative
- `.strip()`, `.lower()` return NEW strings (strings are immutable)
- `int()` vs `float()` vs `str()` conversion
- `if / elif / else`, order of conditions (most specific first), `and` / `or`
- **Guard clause** (reject bad input first) · **DRY** (Don't Repeat Yourself) · **refactoring** with tests as a safety net
- `while` loops, making sure they end · `abs()` · `+=` / `//=`
- `for` loops, `range(start, stop)` (stop excluded), off-by-one errors
- build a list: `results = []` → `.append()` in the loop → `return` after the loop
- the two meanings of `in`
- first Big-O: digits loop = O(log n); looping over text = O(n)
- `enumerate(items, start=1)`, list slicing `[:k]`, **linear search** (return early when found; "not found" after the loop)
- `math.isqrt`, divisor pairs → `is_prime` in **O(√n)**
- strings: `[::-1]`, `.replace()`, `.split()`, `"sep".join()`, `.title()`, `sorted()` on a string, method chaining
- `return a == b` directly instead of `if/else` returning True/False
- **accumulator pattern** (numbers, lists, strings) · **"champion" pattern** (best so far) · **helper functions** for DRY
- first real algorithm: **run-length encoding** (`compress`)

## Daily log
### 2026-10-28 | Week 1 Day 1
- **Built / committed:** Day 0 setup done: venv, pytest, Git, pushed to GitHub. Started `play.py` (input + f-string).

### 2026-10-29 | Week 1 Day 2
- **Built:** `celsius_to_fahrenheit` ✅ (first green function!)
- **Learned:** return vs print, PEP 8 naming (lowercase variables).

### 2026-10-30 | Week 1 Day 2–3
- **Built:** `circle_area` ✅ after a SyntaxError.
- **Learned:** `import`, `math.pi`, `round()` vs f-string formatting.

### 2026-10-31 | Week 1 Day 3 | hours: _
- **Learned:** `//` and `%`, `divmod` + tuple unpacking, tuple vs set, percentages, default parameters, one-line conditionals, `.strip()`, `in`.
- **Built:** ex01 complete, **15/15 green** 🎉 · committed.
- **Watched:** CS50P Lecture 1: Conditionals ✅
- **Confused me:** Job 2 of `to_number` (how to make Python decide between two options).

### 2026-10-31 (later) | Week 1 Day 3–4 | hours: _
- **Built (ex02):** `grade` ✅ (guard clause + refactor), `sum_of_digits` ✅ (fixed an infinite loop), `fizzbuzz` ✅ (7 bugs over 3 rounds), `multiplication_table` ✅ (green on the first run!), `count_vowels` ✅
- **Learned:** if/elif ordering, guard clauses, DRY, while/for loops, `range`, off-by-one, list building, two meanings of `in`, `or` pitfall.
- **Explained out loud:** _

### 2026-11-01 | Week 1 Day 4 | hours: _
- **Watched:** CS50P Lecture 2: Loops ✅
- **Built / committed:** `guessing_game_result` ✅ (first linear search), `is_prime` ✅, then refactored to **O(√n)** (a trillion-sized prime in 0.16 s) → **ex02 complete, 34/34** · committed `0c0fa86`
- **Learned:** `enumerate(start=1)`, list slicing `[:k]`, "decide 'not found' only after the loop", divisor pairs → √n, Big-O O(n) vs O(√n)
- **Explained out loud:** EXPLAIN IT ex01 + ex02 first drafts written (graded 3.7 and 3.3)

### 2026-11-02 | Week 1 Day 5 | hours: _
- **Built / committed:** ex03: `is_palindrome`, `reverse_words`, `initials` (committed `1f482a9`), then `clean_name`, `count_char`, `longest_word`, `is_anagram`, a `text_cleanup` helper, and `compress` → **all week01 exercises done, 66/66 green** 🎉 (last 5 functions NOT committed yet)
- **Learned:** slicing `[::-1]`, `.replace()`, `.split()` vs `.split(" ")`, `"sep".join(list)`, method chaining, returning a comparison directly (no `if/else`), the accumulator pattern (number / list / string), the "champion" pattern, helper functions + DRY, run-length encoding
- **Confused me:** `compress` needed the plain-English plan (hint level 3), so rewrite it from memory to prove it
- **Explained out loud:** ex02 answers rewritten → 4/4/4 ✅ · ex03 answers graded 4 / 4.5 / 2
- **Tomorrow:** commit · from-memory rewrites (fizzbuzz, is_prime, compress) · rewrite ex01 Q1 + ex03 Q3 · start the milestone project

<!-- Copy this block each day -->
### YYYY-MM-DD | Week _ Day _ | hours: _
- **Learned:**
- **Built / committed:**
- **Confused me:**
- **Explained out loud:**
- **Tomorrow:**
