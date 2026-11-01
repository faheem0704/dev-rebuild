"""
Week 1 · Exercise 3: Strings (indexing, slicing, methods, loops over text)
Run:  pytest week01/test_ex03_strings.py -v

Useful methods: .lower() .upper() .strip() .split() .join() .replace() .title()
Slicing: text[start:stop:step]    "python"[::-1] -> "nohtyp"
"""


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and spaces.

    is_palindrome("Never odd or even") -> True
    is_palindrome("python")            -> False
    """
    text = text.lower().replace(" ", "")
    return text == text[::-1]


def reverse_words(sentence):
    """Reverse the ORDER of the words (not the letters). Extra spaces collapse to one.

    reverse_words("hello big world") -> "world big hello"
    """
    result = " ".join(sentence.split()[::-1])
    return result


def initials(full_name):
    """initials("ada lovelace")      -> "A.L."
    initials("grace brewster hopper") -> "G.B.H."
    """
    words = full_name.split()
    result = ""
    for word in words:
        result += word[0].upper() + "."
    return result

def clean_name(raw):
    """Strip outer spaces, collapse inner spaces, capitalize each word.

    clean_name("  aDA    lovelace ") -> "Ada Lovelace"
    """
    pass


def count_char(text, ch):
    """Count how many times ch appears in text, using a FOR LOOP (no .count()).

    count_char("banana", "a") -> 3
    """
    pass


def longest_word(sentence):
    """Return the longest word. If there's a tie, return the FIRST one. Empty -> "".

    longest_word("I love machine learning") -> "learning"
    """
    pass


def is_anagram(a, b):
    """True if a and b use exactly the same letters, ignoring case and spaces.

    is_anagram("Listen", "Silent")         -> True
    is_anagram("Dormitory", "dirty room")  -> True
    """
    pass


def compress(text):
    """Your first real ALGORITHM: run-length encoding (used in image/file compression).
    Replace each run of the same character with the character + run length.

    compress("aaabbc") -> "a3b2c1"
    compress("")       -> ""
    Think first, on paper: what do you need to remember while walking through the string?
    """
    pass


# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. Strings are immutable. What does that mean, and what does s.upper() actually do?
# 2. What does "python"[1:4] return? What about "python"[-2:]? (Predict, then run.)
# 3. Why is " ".join(words) better than adding strings with + inside a loop?
# ---------------------------------------------------------------------------
