import pytest
from ex03_write_tests import(
    split_bill,
    apply_discount,
    count_words,
)

@pytest.mark.parametrize("total, people, expected", [(100, 4, 25.0), (10, 3, 3.33), (200, 5, 40.0)])
def test_split_bill(total, people, expected):
    assert split_bill(total, people) == expected

def test_less_than_one_raises():
    with pytest.raises(ValueError):
        split_bill(100, 0)

@pytest.mark.parametrize("price, percent, expected", [(200, 10, 180.0), (50, 0, 50.0), (50, 100, 0.0)])
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected

def test_above_hundred_raises():
    with pytest.raises(ValueError):
        apply_discount(200, 105)

@pytest.mark.parametrize("text, expected", [("hello big  world", 3), ("", 0), ("   ", 0), ("one\ntwo", 2)])
def test_count_words(text, expected):
    assert count_words(text) == expected
