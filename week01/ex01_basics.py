"""
Week 1 · Exercise 1: Variables, types, operators, f-strings

HOW TO WORK:
  1. Replace each `pass` with your code. Don't change function names or parameters.
  2. Run:  pytest week01/test_ex01_basics.py -v
  3. Red = read the error message carefully. Green = move on.
  4. No AI-written code. Stuck for 20 min? Ask Claude for a HINT.
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit. Formula: F = C * 9/5 + 32

    celsius_to_fahrenheit(100) -> 212.0
    celsius_to_fahrenheit(-40) -> -40.0
    """
    pass


def circle_area(radius):
    """Return the area of a circle, rounded to 2 decimal places.
    Use math.pi (you'll need an import at the top of the file).

    circle_area(1) -> 3.14
    circle_area(2.5) -> 19.63
    """
    pass


def seconds_to_hms(total_seconds):
    """Convert seconds into an 'HH:MM:SS' string, each part 2 digits.

    seconds_to_hms(3725) -> '01:02:05'
    seconds_to_hms(59)   -> '00:00:59'
    Hint: the operators // and % are your friends. f-strings can pad: f"{5:02d}" -> '05'
    """
    pass


def price_after_discount(price, quantity, discount_percent):
    """Total price after a percentage discount, rounded to 2 decimals.

    price_after_discount(100, 3, 10) -> 270.0
    price_after_discount(19.99, 2, 0) -> 39.98
    """
    pass


def format_receipt_line(product, total, currency="AED"):
    """Return a receipt line with the total shown to exactly 2 decimals.

    format_receipt_line("Laptop", 5000)          -> 'Laptop: AED 5000.00'
    format_receipt_line("Mouse", 45.5, "USD")    -> 'Mouse: USD 45.50'
    """
    pass


def age_from_birth_year(birth_year, current_year):
    """Return age in years. If birth_year is in the future, return 0.

    age_from_birth_year(2002, 2026) -> 24
    """
    pass


def to_number(text):
    """Convert a numeric string to int if it has no decimal point, otherwise float.
    Also strip surrounding spaces first.

    to_number("42")    -> 42      (an int)
    to_number(" 3.5 ") -> 3.5     (a float)
    """
    pass


# ---------------------------------------------------------------------------
# EXPLAIN IT (answer out loud, then in a comment below; Claude can grade it)
# 1. What's the difference between / and // ? What does % return?
# 2. Why does 0.1 + 0.2 == 0.3 give False? (Predict first, then try it in the REPL)
# 3. What does type(5 / 1) return and why?
# ---------------------------------------------------------------------------
