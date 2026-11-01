# Week 1: Python Basics (from zero)

**This week you learn:** how a program runs, variables, data types, operators, input/output, f-strings, conditions, loops, and strings.
**Main video course:** Harvard **CS50P** ("CS50's Introduction to Programming with Python", free on YouTube and cs50.harvard.edu/python).
**Milestone project:** Number Guessing Game + Calculator (`PROJECT.md`).

## The rule for every video
Watch **without coding** → close the video → open a blank file → rebuild the examples **from memory** → only re-watch the parts you couldn't rebuild.
That struggle is the learning. Typing along with a video feels productive but sticks much less.

---

## Day-by-day

### Day 1: Setup + first programs
1. Do **Day 0 setup** in the main `README.md` (venv, pytest, Git). ~45 min.
2. 🎥 Watch **CS50P Lecture 0: Functions, Variables** (first half, up to "functions").
3. ✍️ In a scratch file `week01/play.py`, write a program that asks your name and age and prints `"Hi <name>, in 10 years you'll be <age+10>"`. Run it. Then **break it**: type letters for the age. Read the red error (traceback) line by line. Which line? Which error type?
4. ✍️ Start `ex01_basics.py`: get `celsius_to_fahrenheit` and `circle_area` green.
5. 📝 `PROGRESS.md`: log the day. `git commit`.

### Day 2: Types, operators, f-strings
1. 🎥 Rest of CS50P Lecture 0.
2. 🧠 Predict-then-run in the Python REPL (type `python` in the terminal): `7 / 2`, `7 // 2`, `7 % 2`, `2 ** 10`, `"ab" * 3`, `int("5") + 1`, `"5" + 1`, `0.1 + 0.2`, `round(2.675, 2)`. Write down your guess **before** pressing Enter.
3. ✍️ Finish `ex01_basics.py` (all green).
4. 🗣️ Answer the EXPLAIN IT questions at the bottom of ex01, out loud then in writing.

### Day 3: Conditions
1. 🎥 **CS50P Lecture 1: Conditionals**.
2. ✍️ `ex02_conditions_loops.py`: `grade`, `is_prime` (the plain version first).
3. 🧠 Truthy/falsy: predict `bool(0)`, `bool("")`, `bool("0")`, `bool([])`, `bool(None)`, `bool(" ")`.

### Day 4: Loops
1. 🎥 **CS50P Lecture 2: Loops**.
2. ✍️ Finish `ex02_conditions_loops.py`. For `is_prime`, do the bonus (check only up to √n) and explain **why** that's enough. This is your first taste of making an algorithm faster.
3. 🔁 Warm-up habit starts today: re-solve `seconds_to_hms` from a blank file before anything else.

### Day 5: Strings
1. 🎥 Watch: Corey Schafer, **"Python Tutorial for Beginners 2: Strings - Working with Textual Data"** (~20 min), then **"Python Tutorial: Slicing Lists and Strings"** (~10 min). Then do the predict-then-run drills below without the video.
   Predict, then run: `"python"[0]`, `"python"[-1]`, `"python"[1:4]`, `"python"[::-1]`, `"a,b,c".split(",")`, `"-".join(["a", "b"])`, `"hello".replace("l", "L")`, `"Hi".find("i")`
2. ✍️ `ex03_strings.py`. `compress` is your **first real algorithm**. Solve it on **paper first**: walk through "aaabbc" by hand and write down what you have to remember at each step. Then code it.
3. 🗣️ INTERVIEW_BANK: Week 1 questions 1–3.

### Day 6: Milestone project
1. ✍️ Build `PROJECT.md` (guessing game + calculator) **from blank files, no AI, no tutorial**.
2. 💥 Try to break both programs. Fix what breaks.
3. 🎤 Ask Claude: `mock interview week 1` (15 min).

### Day 7: Rest. Your brain consolidates while you rest.

---

## Running the tests
```powershell
pytest week01 -v                                # everything
pytest week01/test_ex02_conditions_loops.py -v  # one file
pytest week01 -k prime -v                       # only tests with "prime" in the name
```
All red at the start is correct. Turn them green.

## Gate: pass ALL of these before Week 2
- [ ] `pytest week01`: all green
- [ ] Rewrite `fizzbuzz`, `is_prime` and `compress` **from a blank file, from memory**, in under 10 minutes each
- [ ] Milestone project done, committed, and you can explain every line
- [ ] EXPLAIN IT questions from all 3 files answered and graded ≥ 4/5 by Claude

Then tell Claude: **`review my week 1`**.
