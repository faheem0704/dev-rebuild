# Week 2: Collections, Functions, Errors

**This week you learn:** lists, tuples, dicts, sets, comprehensions, functions (`*args`, `**kwargs`, defaults, scope), recursion, and exception handling.
**Milestone project:** CLI Expense Tracker (`PROJECT.md`).

## Day-by-day

### Day 1: Lists and tuples
1. 🎥 Corey Schafer: "Python Tutorial for Beginners 4: Lists, Tuples, and Sets".
2. 🧠 Predict-then-run: `a = [1, 2]; b = a; b.append(3); print(a)`. Then `b = a.copy()` and repeat. Why the difference? (Draw boxes and arrows on paper.)
3. ✍️ `ex01_collections.py`: `remove_duplicates_keep_order`, `common_elements`, `even_squares`.

### Day 2: Dictionaries and sets
1. 🎥 Corey Schafer: "Python Tutorial for Beginners 5: Dictionaries".
2. ✍️ Finish `ex01_collections.py`.
3. 📖 Read `ALGORITHMS.md` → **Hash tables**. That's *why* `x in my_dict` is instant and `x in my_list` is slow.

### Day 3: Functions
1. 🎥 Corey Schafer: "Python Tutorial for Beginners 8: Functions".
2. ✍️ `ex02_functions.py`: everything except `factorial` and `flatten`.
3. 🗣️ Out loud: difference between **return** and **print**. Why do the tests need `return`?

### Day 4: Recursion
1. 📖 Read `ALGORITHMS.md` → **Recursion**. Trace `factorial(4)` on paper, one box per call.
2. ✍️ `factorial` and `flatten`.
3. 🧠 Remove the base case from `factorial` and run it. Read the error. Explain what happened.

### Day 5: Exceptions (the interview question)
1. 🎥 **CS50P Lecture 3: Exceptions** + Corey Schafer "Using Try/Except Blocks for Error Handling".
2. ✍️ `ex03_errors.py`.
3. 🗣️ INTERVIEW_BANK ⭐ questions 1 and 2, out loud and written. Ask Claude to grade them.

### Day 6: Milestone project
Build the Expense Tracker from a blank file. Break it. Fix it. Commit. Then `mock interview week 2`.

### Day 7: Rest.

## Gate
- [ ] `pytest week02`: all green
- [ ] From memory: `word_frequency`, `flatten`, `parse_age` (under 10 min each)
- [ ] Expense Tracker done and committed
- [ ] ⭐ exception-handling questions scored ≥ 4/5
