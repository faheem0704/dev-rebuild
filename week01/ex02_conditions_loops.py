"""
Week 1 · Exercise 2: Conditions and loops
Run:  pytest week01/test_ex02_conditions_loops.py -v
"""
import math


def grade(score):
    """Return a letter grade.
    90-100 -> 'A', 80-89 -> 'B', 70-79 -> 'C', 0-69 -> 'F'
    Anything below 0 or above 100 -> 'Invalid'
    """
    if score > 100 or score < 0:
        return "Invalid"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


def fizzbuzz(n):
    """Return a LIST of strings for numbers 1..n (inclusive):
    multiples of 3 -> 'Fizz', of 5 -> 'Buzz', of both -> 'FizzBuzz', else the number as a string.

    fizzbuzz(5) -> ['1', '2', 'Fizz', '4', 'Buzz']
    """
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            results.append("Buzz")
        else:
            results.append(str(i))
    return results

def is_prime(n):
    """True if n is a prime number, else False. Numbers below 2 are not prime.
    Bonus: only check divisors up to the square root of n. Why does that work?
    """
    if n < 2:
        return False
    for divisor in range(2, math.isqrt(n) + 1):
        if n % divisor == 0:
            return False
    return True


def multiplication_table(n, upto=10):
    """Return a list of strings like '7 x 1 = 7' for 1..upto.

    multiplication_table(7, 3) -> ['7 x 1 = 7', '7 x 2 = 14', '7 x 3 = 21']
    """
    answer = []
    for i in range(1, upto + 1):
        answer.append(f"{n} x {i} = {n*i}")
    return answer


def sum_of_digits(n):
    """Sum the digits of an integer using a while loop with % and // (NOT str()).
    Negative numbers: use the absolute value.

    sum_of_digits(1234) -> 10
    sum_of_digits(-56)  -> 11
    """
    total = 0
    n = abs(n)
    while n > 0:
        total = total + n % 10
        n //= 10

    return total


def count_vowels(text):
    """Count vowels (a, e, i, o, u), case-insensitive.

    count_vowels("Hello World") -> 3
    """
    count = 0
    text = text.lower()
    for letter in text:
        if letter in "aeiou":
            count += 1
    return count


def guessing_game_result(secret, guesses, max_tries=3):
    """The logic of a number-guessing game (you'll build the full game as this week's project).

    `guesses` is a list of numbers the player typed, in order.
    Only the first `max_tries` guesses count.
    - If one of those equals `secret`: return 'Correct on try N' (N starts at 1)
    - Otherwise: return 'Out of tries'

    guessing_game_result(7, [3, 7])        -> 'Correct on try 2'
    guessing_game_result(7, [1, 2, 3, 7])  -> 'Out of tries'
    Hint: enumerate() gives you the index and the value together.
    """
    guesses = guesses[:max_tries]
    for position, number in enumerate(guesses, start=1):
        if number == secret:
            return f"Correct on try {position}"
    return "Out of tries"


# ---------------------------------------------------------------------------
# EXPLAIN IT
# 1. When would you choose a while loop over a for loop?
#answer. we should use while loop over for loop when the number of iterations are unkown in advance and it depends on a dynamic condition being met. we should use for loops when iterating over a fixed sequence, collection or a number of steps.
# 2. What's the difference between break, continue, and pass?
#answer. break is usef to break out of a loop. continue is used to skip the current step and continue the loop, and pass is used to do nothing.. it says do nothing in here in the code block...
# 3. Name 5 "falsy" values in Python.
#answer. False, None, 0, 0.0, "", [], {},()
# ---------------------------------------------------------------------------
