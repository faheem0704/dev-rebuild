# Week 1 Milestone Project: Number Guessing Game + Calculator

**Proves you can:** write a complete program from an empty file using variables, input/output, conditions, loops and strings, with **no tutorial and no AI**.

Build both in `week01/` from blank files. No tests are given. You test by playing, and by trying to break it.

## Part 1: `guessing_game.py`
1. The computer picks a random number (`import random` → `random.randint`).
2. Player picks a difficulty: easy (1–50, 10 tries), medium (1–100, 7 tries), hard (1–500, 9 tries).
3. After each guess print "Too high", "Too low" or "Correct!", and how many tries are left.
4. Invalid input (letters, empty, out of range) → friendly message, and it **doesn't** use up a try.
   (You haven't learned `try/except` yet. Use `str.isdigit()`.)
5. At the end: win/lose message, then "Play again? (y/n)".
6. Track and show the best score (fewest tries) across rounds in the same session.

## Part 2: `calculator.py`
1. A menu loop: add, subtract, multiply, divide, power, quit.
2. Asks for two numbers and prints the result formatted to 2 decimals.
3. Division by zero → message, not a crash (use an `if` for now).
4. Keeps a history list of the last 5 calculations and shows it with menu option `h`.

## Stretch (pick 1)
- Guessing game: the computer guesses YOUR number using **binary search** (always guess the middle of the remaining range). Count how many tries it needs for 1–1000. Can it always do it in 10? Why? (This is your first preview of `ALGORITHMS.md` → Binary Search.)
- Calculator: accept a single line like `12 * 3.5` and split it into parts.

## Done = both programs work, you tried to break them, everything is committed to Git, and you can explain every line out loud.
