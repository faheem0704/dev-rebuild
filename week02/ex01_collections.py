"""
Week 2 · Exercise 1: Lists, tuples, dicts, sets, comprehensions
Run:  pytest week02/test_ex01_collections.py -v

Goal: pick the RIGHT data structure instead of using lists for everything.
"""


def word_frequency(text):
    """Count how often each word appears. Lowercase everything and
    remove these punctuation characters: . , ! ?

    word_frequency("The cat. The hat!") -> {'the': 2, 'cat': 1, 'hat': 1}
    """
    pass


def top_student(students):
    """students is a list of dicts like {"name": "Sara", "score": 94}.
    Return the NAME of the student with the highest score.
    Return None for an empty list.
    Hint: max() accepts key=...
    """
    pass


def remove_duplicates_keep_order(items):
    """Remove duplicates but keep the first-seen order.

    remove_duplicates_keep_order([3, 1, 3, 2, 1]) -> [3, 1, 2]
    Think: why doesn't list(set(items)) work here?
    """
    pass


def common_elements(a, b):
    """Return the elements present in both lists, as a SORTED list without duplicates.
    Use sets.

    common_elements([1, 2, 2, 3], [2, 3, 4]) -> [2, 3]
    """
    pass


def total_by_category(expenses):
    """expenses: list of dicts like {"desc": "Pizza", "amount": 30, "category": "food"}
    Return a dict mapping category -> total amount.

    -> {"food": 75, "transport": 20}
    """
    pass


def invert_dict(d):
    """Swap keys and values using a dict comprehension.

    invert_dict({"a": 1, "b": 2}) -> {1: "a", 2: "b"}
    """
    pass


def even_squares(numbers):
    """Use a LIST COMPREHENSION to return the squares of the even numbers only.

    even_squares([1, 2, 3, 4]) -> [4, 16]
    """
    pass


def revenue_by_product(sales_lines):
    """Each line is a sale: 'date product quantity unit_price', e.g.
        '2026-10-27 Laptop 2 2500.00'
        '2026-10-27 Mouse 3 45.50'
    Return a dict product -> total revenue (quantity * unit_price), rounded to 2.
    Hint: str.split() gives you a list of 4 parts. Convert the numbers!
    """
    pass


def top_n(counts, n):
    """Given a dict name -> number, return the top n as a list of (name, number) tuples,
    sorted by number (highest first). Ties: sort by name alphabetically.

    top_n({"tea": 5, "coffee": 9, "juice": 5}, 2) -> [("coffee", 9), ("juice", 5)]
    Hint: sorted(..., key=lambda pair: (-pair[1], pair[0]))
    """
    pass


# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. Why is checking `x in my_set` faster than `x in my_list` for large data?
# 2. Why can a tuple be a dict key but a list cannot?
# 3. a = [1, 2]; b = a; b.append(3). What is a now? Why? (Predict, then run.)
# ---------------------------------------------------------------------------
