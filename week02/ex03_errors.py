"""
Week 2 · Exercise 3: Exception handling, the interview question.
Run:  pytest week02/test_ex03_errors.py -v

Watch first: Corey Schafer's video "Python Tutorial: Using Try/Except Blocks for Error Handling".
Key syntax:

    try:
        risky()
    except SomeSpecificError as e:   # runs only if that error happened
        ...
    else:                            # runs only if NO error happened
        ...
    finally:                         # ALWAYS runs: cleanup goes here
        ...

    raise ValueError("helpful message")   # signal an error yourself
"""


class InsufficientFundsError(Exception):
    """A custom exception. Already done for you; just raise it where needed."""


def safe_divide(a, b):
    """Return a / b. If b is zero, return None instead of crashing.
    Use try/except ZeroDivisionError. Don't use an `if` check.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_age(text):
    """Convert user input to an int age.
    - Not a whole number (e.g. 'abc', '12.5')? raise ValueError("Age must be a whole number")
    - Below 0 or above 150? raise ValueError("Age out of range")
    Hint: int('abc') already raises ValueError. Catch it and raise your own message.
    """
    try:
        age = int(text)
    except ValueError:
        raise ValueError("Age must be a whole number")
    else:
        if not 0 <= age <= 150:
            raise ValueError("Age out of range")
        return age


def withdraw(balance, amount):
    """Return the new balance.
    - amount <= 0  -> raise ValueError("Amount must be positive")
    - amount > balance -> raise InsufficientFundsError(f"Need {amount}, have {balance}")"""
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(f"Need {amount}, have {balance}")
    return balance - amount


def get_port(config):
    """config is a dict that may contain "port" (an int or a numeric string).
    - Key missing          -> return default 8080  (practice: catch KeyError)
    - Not a number         -> raise ValueError("Invalid port")
    - Outside 1..65535     -> raise ValueError("Invalid port")
    - Otherwise return the port as an int
    """
    try:
        port = int(config["port"])
    except KeyError:
        return 8080
    except (ValueError, TypeError):
        raise ValueError("Invalid port")
    else:
        if not 1 <= port <= 65535:
            raise ValueError("Invalid port")
        return port


def run_with_cleanup(func, log):
    """Call func() and return its result.
    WHATEVER happens (success or exception), append the string "cleanup" to `log`.
    If func raises, the exception must still propagate to the caller (don't swallow it!).
    This is exactly what `finally` is for.
    """
    pass


# ---------------------------------------------------------------------------
# EXPLAIN IT (these ARE the interview questions you missed; see INTERVIEW_BANK.md)
# 1. What's the difference between except, else and finally?
# 2. Why is a bare `except:` (catching everything) usually a bad idea?
# 3. When should you catch an exception, and when should you let the program crash?
# ---------------------------------------------------------------------------
