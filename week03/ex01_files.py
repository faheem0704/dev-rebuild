"""
Week 3 · Exercise 1: Reading and writing files, `with`, pathlib
Run:  pytest week03/test_ex01_files.py -v

Always: open(..., encoding="utf-8"), and use `with` so files close automatically.
`path` arguments may be a string or a pathlib.Path; open() accepts both.
"""
from pathlib import Path


def write_lines(path, lines):
    """Write each string in `lines` to the file, one per line. Overwrite the file if it exists.

    write_lines("a.txt", ["hello", "world"])  ->  file contains "hello\\nworld\\n"
    """
    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")



def read_lines(path):
    """Return the file's lines as a list of strings, WITHOUT the "\\n" at the end of each.

    (file contains "hello\\nworld\\n")  ->  ["hello", "world"]
    Hint: loop over the file object, and use .rstrip("\\n") on each line.
    """
    lines = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            lines.append(line.rstrip())
    return lines


def append_line(path, line):
    """Add one line to the END of the file (create the file if it doesn't exist).
    Which open() mode adds instead of overwriting?
    """
    with open(path, "a", encoding="utf-8") as file:
        file.write(f"{line}\n")


def file_stats(path):
    """Return {"lines": ..., "words": ..., "chars": ...} for a text file.

    "chars" = the length of the whole file's text, including "\\n" characters.
    (file contains "hi there\\nbye\\n")  ->  {"lines": 2, "words": 3, "chars": 13}
    """
    with open(path, encoding="utf-8") as file:
        text = file.read()
    return {"lines": len(text.splitlines()), "words": len(text.split()), "chars": len(text)}


def read_or_default(path, default=""):
    """Return the whole text of the file. If the file doesn't exist, return `default`.
    Use try/except FileNotFoundError. A missing file is a NORMAL situation here.
    """
    try:
        with open(path, encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return default


def find_files(folder, extension):
    """Return a SORTED list of the file NAMES (strings, not paths) in `folder`
    that end with `extension` (like ".csv"). Don't look inside sub-folders.

    find_files("data", ".csv")  ->  ["jan.csv", "mar.csv"]
    Hint: Path(folder).glob(...) and each path's .name
    """
    return sorted([file.name for file in Path(folder).glob("*" + extension)])


# ---------------------------------------------------------------------------
# EXPLAIN IT (optional, but this is how you get interview-ready)
# 1. What does `with` do, and why is it better than calling f.close() yourself?
# 2. What's the difference between the modes "r", "w" and "a"? Which one can destroy data?
# 3. Why is `for line in f:` better than f.read() for a 10 GB log file?
# ---------------------------------------------------------------------------
