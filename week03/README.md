# Week 3: Files, JSON, CSV, Modules & Testing

**This week you learn:** reading and writing files, `with`, `pathlib`, JSON, CSV, splitting code into modules, writing your **own** tests with pytest, and `logging`.
**Why it matters:** until now, every program forgot everything when it closed. Real software **saves data**: backends, ML datasets and config files are all files, JSON and CSV.
**Milestone project:** Expense Tracker **v6**: it saves to a JSON file, is split into modules, and has its own tests (`PROJECT.md`).

Each day has a **worked example**. Read it, run it, and make sure you understand every line *before* starting the exercise.

---

## Day 1: Files and `with`
🎥 **Corey Schafer: "Python Tutorial: File Objects - Reading and Writing to Files"** (or CS50P Lecture 6, first half)

**Worked example:**
```python
# write (mode "w" = overwrite; creates the file if missing)
with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("first line\n")
    f.write("second line\n")

# append (mode "a" = add to the end)
with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("third line\n")

# read everything as one string
with open("notes.txt", encoding="utf-8") as f:
    text = f.read()            # "first line\nsecond line\nthird line\n"

# read line by line (memory-friendly for huge files)
with open("notes.txt", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))   # each line ends with "\n"; remove it
```
- **`with`** closes the file automatically, even if an error happens. It's your `run_with_cleanup` idea (`finally`), built into Python.
- **`encoding="utf-8"`** always. Windows otherwise uses an old encoding, and names like "Muñoz" or "محمد" break.
- **`"w"` erases the file first!** Use `"a"` to add.

✍️ `ex01_files.py`: `write_lines`, `read_lines`, `append_line`, `file_stats`

## Day 2: Missing files and `pathlib`
📖 Python docs: **pathlib → "Basic use"** (docs.python.org/3/library/pathlib.html)

**Worked example:**
```python
from pathlib import Path

folder = Path("data")
folder.mkdir(exist_ok=True)                 # create the folder (no error if it exists)
report = folder / "report.txt"              # "/" joins paths, works on Windows AND Linux
print(report.exists(), report.name, report.suffix)   # False report.txt .txt

for file in Path(".").glob("*.py"):         # every .py file in this folder
    print(file.name)

try:
    with open("missing.txt", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    text = ""                               # a normal situation → use a default
```
✍️ Finish `ex01_files.py`: `read_or_default`, `find_files`

## Day 3: JSON
🎥 **Corey Schafer: "Python Tutorial: Working with JSON Data using the json Module"**

**Worked example:**
```python
import json

books = [{"title": "Dune", "price": 9.5}, {"title": "Emma", "price": 4.0}]

with open("books.json", "w", encoding="utf-8") as f:
    json.dump(books, f, indent=2)           # Python → JSON text in a file

with open("books.json", encoding="utf-8") as f:
    loaded = json.load(f)                   # JSON text → Python lists/dicts
print(loaded[0]["title"])                   # Dune
```
- JSON is the language of **web APIs** (you'll use it every day from Week 8).
- `dump`/`load` work with **files**; `dumps`/`loads` (with an *s*, for **string**) work with text.
- A broken JSON file raises **`json.JSONDecodeError`**. Try it: put `{oops` in a file and load it.

✍️ `ex02_json_csv.py`: `save_json`, `load_json`

## Day 4: CSV
🎥 **Corey Schafer: "Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files"**

**Worked example:**
```python
import csv

rows = [{"title": "Dune", "price": "9.5"}, {"title": "Emma", "price": "4.0"}]

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(rows)

with open("books.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):           # each row is a dict, keyed by the header
        print(row["title"], float(row["price"]))   # ⚠️ every CSV value is TEXT
```
- **`newline=""`** is required by the csv module. Without it, Windows writes blank lines between rows.
- **Every value comes back as a string.** Convert numbers yourself (and expect bad ones!).
- CSV is how most **ML datasets** arrive (Week 17: pandas reads them for you).

✍️ Finish `ex02_json_csv.py`: `read_csv`, `write_csv`, `sum_column`, `csv_to_json`

## Day 5: Modules and writing your OWN tests
🎥 **CS50P Lecture 4: Libraries** (modules, `import`) and **CS50P Lecture 5: Unit Tests** (pytest)

**Worked example: a module and its tests**
```python
# file: shop.py
def add_tax(price, rate=0.05):
    if price < 0:
        raise ValueError("price can't be negative")
    return round(price * (1 + rate), 2)
```
```python
# file: test_shop.py   (pytest finds files named test_*.py)
import pytest
from shop import add_tax            # import your own module by its file name

def test_default_rate():
    assert add_tax(100) == 105.0

@pytest.mark.parametrize("price, rate, expected", [(0, 0.05, 0.0), (10, 0.2, 12.0)])
def test_many_cases(price, rate, expected):
    assert add_tax(price, rate) == expected

def test_negative_price_raises():
    with pytest.raises(ValueError):
        add_tax(-1)
```
A good set of tests covers: **a normal case · edge cases (0, empty, one item) · invalid input (raises).**

✍️ `ex03_write_tests.py`: **this time YOU write the tests.** The file has 3 functions; 2 of them contain a hidden bug. Write tests in a new file `test_ex03_write_tests.py`, let them find the bugs, then fix the bugs.

## Day 6: Project, Expense Tracker v6 (`PROJECT.md`)

## Day 7: Rest

---

## Running the tests
```powershell
pytest week03 -v
```
(Files are created in a temporary folder by pytest's `tmp_path`, so your folder stays clean.)

## Gate (pass ALL before Week 4)
- [ ] `pytest week03`: all green, **including your own `test_ex03_write_tests.py`** with ≥ 8 tests, and both bugs found and fixed
- [ ] Expense Tracker v6 done: saves/loads JSON, split into modules, ≥ 10 tests of its own, committed
- [ ] From memory, in 10 minutes: a function that saves a list of dicts to JSON and one that loads it back (with a default for a missing file)
