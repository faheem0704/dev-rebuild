"""
Week 3 · Exercise 3: YOU write the tests.

These 3 functions look finished, but TWO of them contain a bug.
Your job:
  1. Create a new file:  week03/test_ex03_write_tests.py
  2. Write at least 8 tests for these functions (see the worked example in README Day 5):
     a normal case · edge cases (0, empty, one item) · invalid input (pytest.raises)
     Use @pytest.mark.parametrize at least once.
  3. Run them:  pytest week03/test_ex03_write_tests.py -v
     Tests that FAIL are pointing at a bug. Read the failure carefully.
  4. Fix the bugs IN THIS FILE, until all your tests pass.

Don't read the code looking for the bugs first. Write tests from the DESCRIPTIONS (the docstrings).
That's how testing works in real teams: you test what the function PROMISES to do.
"""


def split_bill(total, people):
    """Split a bill equally. Return each person's share, rounded to 2 decimals.
    people must be at least 1, otherwise raise ValueError("people must be at least 1").

    split_bill(100, 4) -> 25.0
    split_bill(10, 3)  -> 3.33
    """
    if people < 0:
        raise ValueError("people must be at least 1")
    return round(total / people, 2)


def apply_discount(price, percent):
    """Return the price AFTER a percentage discount, rounded to 2 decimals.
    percent must be between 0 and 100 (inclusive), otherwise raise ValueError.

    apply_discount(200, 10)  -> 180.0
    apply_discount(50, 0)    -> 50.0
    apply_discount(50, 100)  -> 0.0
    """
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * percent / 100, 2)


def count_words(text):
    """Return how many words are in the text (words are separated by any whitespace).

    count_words("hello big  world") -> 3
    count_words("")                 -> 0
    """
    return len(text.split())
