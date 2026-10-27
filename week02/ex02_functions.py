"""
Week 2 · Exercise 2: Functions, *args/**kwargs, recursion, scope
Run:  pytest week02/test_ex02_functions.py -v
"""


def calculate_total(price, quantity, discount=0.0):
    """discount is a fraction (0.10 = 10%). RETURN (don't print!) the total, rounded to 2.

    calculate_total(100, 3, 0.10) -> 270.0
    calculate_total(100, 3)       -> 300.0
    """
    pass


def average(*numbers):
    """Average of any number of arguments. Return 0.0 if none are given.

    average(1, 2, 3, 4) -> 2.5
    average()           -> 0.0
    """
    pass


def build_profile(name, **details):
    """Return a dict with 'name' plus every keyword argument passed.

    build_profile("Sara", role="analyst", team="ML")
        -> {"name": "Sara", "role": "analyst", "team": "ML"}
    """
    pass


def factorial(n):
    """Recursive factorial. factorial(0) == 1. No loops allowed!"""
    pass


def flatten(nested):
    """Recursively flatten arbitrarily nested lists.

    flatten([1, [2, [3, [4]], 5]]) -> [1, 2, 3, 4, 5]
    Hint: isinstance(x, list)
    """
    pass


def add_item(item, items=None):
    """Append item to items and return the list. If no list is given, start a new one.
    The test calls add_item("a") then add_item("b") and expects ['b'] the second time.
    Read week 9 of the PDF roadmap on 'mutable default arguments' to see why a
    default of [] would break this.
    """
    pass


def apply_to_all(func, items):
    """Functions are values! Return a new list with func applied to each item.

    apply_to_all(str.upper, ["a", "b"]) -> ["A", "B"]
    apply_to_all(len, ["hi", "hello"])  -> [2, 5]
    """
    pass


# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. What's the difference between `return` and `print`? Why do the tests need return?
# 2. What are *args and **kwargs? What types are they inside the function?
# 3. What happens if a recursive function has no base case? What error do you get?
# ---------------------------------------------------------------------------
