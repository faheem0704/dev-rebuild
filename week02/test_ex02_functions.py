import pytest

from ex02_functions import (
    add_item,
    apply_to_all,
    average,
    build_profile,
    calculate_total,
    factorial,
    flatten,
)


def test_calculate_total():
    assert calculate_total(100, 3, 0.10) == 270.0
    assert calculate_total(100, 3) == 300.0
    assert calculate_total(price=10, quantity=2, discount=0.5) == 10.0


def test_average():
    assert average(1, 2, 3, 4) == 2.5
    assert average(10) == 10
    assert average() == 0.0


def test_build_profile():
    assert build_profile("Sara", role="analyst", team="ML") == {
        "name": "Sara",
        "role": "analyst",
        "team": "ML",
    }
    assert build_profile("Ali") == {"name": "Ali"}


@pytest.mark.parametrize("n, expected", [(0, 1), (1, 1), (5, 120), (10, 3628800)])
def test_factorial(n, expected):
    assert factorial(n) == expected


def test_flatten():
    assert flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []
    assert flatten([[[]]]) == []


def test_add_item_does_not_share_default():
    assert add_item("a") == ["a"]
    assert add_item("b") == ["b"]
    existing = ["x"]
    assert add_item("y", existing) == ["x", "y"]


def test_apply_to_all():
    assert apply_to_all(str.upper, ["a", "b"]) == ["A", "B"]
    assert apply_to_all(len, ["hi", "hello"]) == [2, 5]
