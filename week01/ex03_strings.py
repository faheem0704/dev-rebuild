"""
Week 1 · Exercise 3: Strings (indexing, slicing, methods, loops over text)
Run:  pytest week01/test_ex03_strings.py -v

Useful methods: .lower() .upper() .strip() .split() .join() .replace() .title()
Slicing: text[start:stop:step]    "python"[::-1] -> "nohtyp"
"""


def text_cleanup(text):
    return text.lower().replace(" ", "")


def is_palindrome(text):
    """True if text reads the same backwards, ignoring case and spaces.

    is_palindrome("Never odd or even") -> True
    is_palindrome("python")            -> False
    """
    cleaned = text_cleanup(text)
    return  cleaned == cleaned[::-1]


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
    return " ".join(raw.split()).title()


def count_char(text, ch):
    """Count how many times ch appears in text, using a FOR LOOP (no .count()).

    count_char("banana", "a") -> 3
    """
    count = 0
    for letter in text:
        if letter == ch:
            count += 1
    return count


def longest_word(sentence):
    """Return the longest word. If there's a tie, return the FIRST one. Empty -> "".

    longest_word("I love machine learning") -> "learning"
    """
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def is_anagram(a, b):
    """True if a and b use exactly the same letters, ignoring case and spaces.

    is_anagram("Listen", "Silent")         -> True
    is_anagram("Dormitory", "dirty room")  -> True
    """
    return sorted(text_cleanup(a)) == sorted(text_cleanup(b))


def compress(text):
    """Your first real ALGORITHM: run-length encoding (used in image/file compression).
    Replace each run of the same character with the character + run length.

    compress("aaabbc") -> "a3b2c1"
    compress("")       -> ""
    Think first, on paper: what do you need to remember while walking through the string?
    """
    if text == "":
        return ""
    result = ""
    current = text[0]
    run_length = 0
    for char in text:
        if char == current:
            run_length += 1
        else:
            result += f"{current}{run_length}"
            current = char
            run_length = 1
    result += f"{current}{run_length}"
    return result



# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. Strings are immutable. What does that mean, and what does s.upper() actually do?
# answer. it means text inside a string object cannot be changed after it is created. if we use functions like .replace() it doesnt change the original string instead it creates a brand new string in the memory. s.upper() makes the characters of the string to upper case and stores in a new string object.
# 2. What does "python"[1:4] return? What about "python"[-2:]? (Predict, then run.)
# answer. it returns 'yth' that is it slices the text from the 1th index till the the 4th index but it does not include the 4th index. "pyhton"[-2:] returns 'on' -2 is the second last index and it returns the the characters from second last index till the end because no end indexed is mentioned.
# 3. Why is " ".join(words) better than adding strings with + inside a loop?
# answer. adding strings with + concatnates the string without spaces unless we hard code space in the string itself. but " ".join() stitches the string together with the character mentioned inside the double quotes as the seperator in between the words, in this case a blank space.
# ---------------------------------------------------------------------------
