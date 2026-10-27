import pytest

from ex02_conditions_loops import (
    guessing_game_result,
    count_vowels,
    fizzbuzz,
    grade,
    is_prime,
    multiplication_table,
    sum_of_digits,
)


@pytest.mark.parametrize(
    "score, expected",
    [(100, "A"), (90, "A"), (89, "B"), (80, "B"), (75, "C"), (69, "F"), (0, "F"),
     (-1, "Invalid"), (101, "Invalid")],
)
def test_grade(score, expected):
    assert grade(score) == expected


def test_fizzbuzz():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    result = fizzbuzz(15)
    assert len(result) == 15
    assert result[14] == "FizzBuzz"
    assert fizzbuzz(0) == []


@pytest.mark.parametrize("n", [2, 3, 5, 7, 13, 97, 7919])
def test_primes(n):
    assert is_prime(n) is True


@pytest.mark.parametrize("n", [-7, 0, 1, 4, 9, 15, 100, 7917])
def test_not_primes(n):
    assert is_prime(n) is False


def test_multiplication_table():
    assert multiplication_table(7, 3) == ["7 x 1 = 7", "7 x 2 = 14", "7 x 3 = 21"]
    assert len(multiplication_table(2)) == 10


@pytest.mark.parametrize("n, expected", [(1234, 10), (-56, 11), (0, 0), (9, 9)])
def test_sum_of_digits(n, expected):
    assert sum_of_digits(n) == expected


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU aeiou") == 10
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0


def test_guess_correct():
    assert guessing_game_result(7, [3, 7]) == "Correct on try 2"
    assert guessing_game_result(7, [7]) == "Correct on try 1"


def test_guess_out_of_tries():
    assert guessing_game_result(7, [1, 2, 3, 7]) == "Out of tries"
    assert guessing_game_result(7, []) == "Out of tries"


def test_guess_custom_max_tries():
    assert guessing_game_result(7, [1, 2, 3, 7], max_tries=5) == "Correct on try 4"
