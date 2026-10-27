from ex01_collections import (
    common_elements,
    even_squares,
    revenue_by_product,
    invert_dict,
    remove_duplicates_keep_order,
    top_n,
    top_student,
    total_by_category,
    word_frequency,
)


def test_word_frequency():
    assert word_frequency("The cat. The hat!") == {"the": 2, "cat": 1, "hat": 1}
    assert word_frequency("") == {}
    assert word_frequency("Hi, hi? HI!") == {"hi": 3}


def test_top_student():
    students = [
        {"name": "Ali", "score": 85},
        {"name": "Sara", "score": 94},
        {"name": "Omar", "score": 78},
    ]
    assert top_student(students) == "Sara"
    assert top_student([]) is None


def test_remove_duplicates_keep_order():
    assert remove_duplicates_keep_order([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert remove_duplicates_keep_order(["b", "a", "b"]) == ["b", "a"]
    assert remove_duplicates_keep_order([]) == []


def test_common_elements():
    assert common_elements([1, 2, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements([1], [2]) == []


def test_total_by_category():
    expenses = [
        {"desc": "Pizza", "amount": 30, "category": "food"},
        {"desc": "Taxi", "amount": 20, "category": "transport"},
        {"desc": "Groceries", "amount": 45, "category": "food"},
    ]
    assert total_by_category(expenses) == {"food": 75, "transport": 20}
    assert total_by_category([]) == {}


def test_invert_dict():
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_even_squares():
    assert even_squares([1, 2, 3, 4]) == [4, 16]
    assert even_squares([1, 3]) == []


SALES = [
    "2026-10-27 Laptop 2 2500.00",
    "2026-10-27 Mouse 3 45.50",
    "2026-10-28 Laptop 1 2400.00",
    "2026-10-28 Keyboard 1 120.00",
]


def test_revenue_by_product():
    assert revenue_by_product(SALES) == {"Laptop": 7400.0, "Mouse": 136.5, "Keyboard": 120.0}
    assert revenue_by_product([]) == {}


def test_top_n():
    counts = {"tea": 5, "coffee": 9, "juice": 5}
    assert top_n(counts, 2) == [("coffee", 9), ("juice", 5)]
    assert top_n(counts, 10) == [("coffee", 9), ("juice", 5), ("tea", 5)]
