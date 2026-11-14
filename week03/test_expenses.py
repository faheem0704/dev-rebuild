import pytest
from storage import load_expenses, save_expenses
from expenses import total_by_category, biggest_expense


def test_load_damaged_file(tmp_path):
    path = tmp_path / "note.txt"
    path.write_text("{oops", encoding="utf-8")
    assert load_expenses(path) == []

@pytest.mark.parametrize("expenses, expected", [
    ([{"description": "burger", "amount": 35.0, "category": "food"}], [{"description": "burger", "amount": 35.0, "category": "food"}] ),
    ([], [])
])
def test_save_then_load(tmp_path, expenses, expected):
    path = tmp_path / "expenses.json"
    save_expenses(path, expenses)
    assert load_expenses(path) == expected


def test_load_missing_file(tmp_path):
    path = tmp_path / "extensions.json"
    assert load_expenses(path) == []


@pytest.mark.parametrize("expenses, expected", [
    ([{"description": "burger", "amount": 35.0, "category": "food"}], {"food": 35.0}),
    ([], {}),
    ([{"description": "pizza", "amount": 55.0, "category": "food"}, {"description": "burger", "amount": 35.0, "category": "food"}, {"description": "taxi", "amount": 100.0, "category": "travel"}], {"food": 90.0, "travel": 100.0})
])
def test_total_by_category(expenses, expected):
    assert total_by_category(expenses) == expected


@pytest.mark.parametrize("expenses, expected", [
    ([{"description": "burger", "amount": 35.0, "category": "food"}], {"description": "burger", "amount": 35.0, "category": "food"}),
    ([], None),
    ([{"description": "pizza", "amount": 55.0, "category": "food"}, {"description": "burger", "amount": 35.0, "category": "food"}, {"description": "taxi", "amount": 100.0, "category": "travel"}], {"description": "taxi", "amount": 100.0, "category": "travel"})
])
def test_biggest_expense(expenses, expected):
    assert biggest_expense(expenses) == expected



