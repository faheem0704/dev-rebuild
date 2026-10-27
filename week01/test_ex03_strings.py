import pytest

from ex03_strings import (
    clean_name,
    compress,
    count_char,
    initials,
    is_anagram,
    is_palindrome,
    longest_word,
    reverse_words,
)


@pytest.mark.parametrize(
    "text, expected",
    [("Never odd or even", True), ("racecar", True), ("python", False), ("", True)],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


def test_reverse_words():
    assert reverse_words("hello big world") == "world big hello"
    assert reverse_words("  one   two ") == "two one"
    assert reverse_words("") == ""


def test_initials():
    assert initials("ada lovelace") == "A.L."
    assert initials("grace brewster hopper") == "G.B.H."


def test_clean_name():
    assert clean_name("  aDA    lovelace ") == "Ada Lovelace"
    assert clean_name("alan") == "Alan"


def test_count_char():
    assert count_char("banana", "a") == 3
    assert count_char("banana", "z") == 0
    assert count_char("", "a") == 0


def test_longest_word():
    assert longest_word("I love machine learning") == "learning"
    assert longest_word("cat dog") == "cat"
    assert longest_word("") == ""


@pytest.mark.parametrize(
    "a, b, expected",
    [("Listen", "Silent", True), ("Dormitory", "dirty room", True), ("abc", "abd", False)],
)
def test_is_anagram(a, b, expected):
    assert is_anagram(a, b) is expected


@pytest.mark.parametrize(
    "text, expected",
    [("aaabbc", "a3b2c1"), ("", ""), ("a", "a1"), ("abca", "a1b1c1a1"), ("zzzz", "z4")],
)
def test_compress(text, expected):
    assert compress(text) == expected
