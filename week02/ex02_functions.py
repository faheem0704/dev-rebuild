"""
Week 2 · Exercise 2: Functions, *args/**kwargs, recursion, scope
Run:  pytest week02/test_ex02_functions.py -v
"""


def calculate_total(price, quantity, discount=0.0):
    """discount is a fraction (0.10 = 10%). RETURN (don't print!) the total, rounded to 2.

    calculate_total(100, 3, 0.10) -> 270.0
    calculate_total(100, 3)       -> 300.0
    """
    total = (price - price * discount) * quantity
    return round(total, 2)


def average(*numbers):
    """Average of any number of arguments. Return 0.0 if none are given.

    average(1, 2, 3, 4) -> 2.5
    average()           -> 0.0
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def build_profile(name, **details):
    """Return a dict with 'name' plus every keyword argument passed.

    build_profile("Sara", role="analyst", team="ML")
        -> {"name": "Sara", "role": "analyst", "team": "ML"}
    """
    return {"name": name, **details}


def factorial(n):
    """Recursive factorial. factorial(0) == 1. No loops allowed!"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def flatten(nested):
    """Recursively flatten arbitrarily nested lists.

    flatten([1, [2, [3, [4]], 5]]) -> [1, 2, 3, 4, 5]
    Hint: isinstance(x, list)
    """
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat


def add_item(item, items=None):
    """Append item to items and return the list. If no list is given, start a new one.
    The test calls add_item("a") then add_item("b") and expects ['b'] the second time.
    Read week 9 of the PDF roadmap on 'mutable default arguments' to see why a
    default of [] would break this.
    """
    if items is None:
        items = []
    items.append(item)
    return items


def apply_to_all(func, items):
    """Functions are values! Return a new list with func applied to each item.

    apply_to_all(str.upper, ["a", "b"]) -> ["A", "B"]
    apply_to_all(len, ["hi", "hello"])  -> [2, 5]
    """
    return [func(item) for item in items]



# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. What's the difference between `return` and `print`? Why do the tests need return?
# answer print is a built-in function displays the text or data for a human to read, it does not pass any value back to the program. where as the return is a keyword inside a function sends a value of that function to where it was called. the tests need return because only then it can use those values to pass custom or pre defined inputs.
# 2. What are *args and **kwargs? What types are they inside the function?
# answer. *args and **kwargs allow you to pass a multiple number of arguments to a function. *args is tuple inside a function and **kwargs is dictionaries type inside a function.
# 3. What happens if a recursive function has no base case? What error do you get?
# answer. if a recursive function has no base case it run for infinite time. it gives a recirsion error saying maximum recursion depth exeeded because python has built in safety limit typically 1000 calls to intentionally crash the program.
# ---------------------------------------------------------------------------
