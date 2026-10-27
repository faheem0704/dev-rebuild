import pytest

from ex01_basics import (
    age_from_birth_year,
    celsius_to_fahrenheit,
    circle_area,
    format_receipt_line,
    price_after_discount,
    seconds_to_hms,
    to_number,
)


@pytest.mark.parametrize("c, f", [(100, 212.0), (0, 32.0), (-40, -40.0), (37, 98.6)])
def test_celsius_to_fahrenheit(c, f):
    assert celsius_to_fahrenheit(c) == pytest.approx(f)


@pytest.mark.parametrize("r, area", [(1, 3.14), (2.5, 19.63), (0, 0.0)])
def test_circle_area(r, area):
    assert circle_area(r) == area


@pytest.mark.parametrize(
    "secs, expected",
    [(3725, "01:02:05"), (59, "00:00:59"), (0, "00:00:00"), (86399, "23:59:59")],
)
def test_seconds_to_hms(secs, expected):
    assert seconds_to_hms(secs) == expected


def test_price_after_discount():
    assert price_after_discount(100, 3, 10) == 270.0
    assert price_after_discount(19.99, 2, 0) == 39.98
    assert price_after_discount(50, 1, 100) == 0.0


def test_format_receipt_line():
    assert format_receipt_line("Laptop", 5000) == "Laptop: AED 5000.00"
    assert format_receipt_line("Mouse", 45.5, "USD") == "Mouse: USD 45.50"


def test_age_from_birth_year():
    assert age_from_birth_year(2002, 2026) == 24
    assert age_from_birth_year(2030, 2026) == 0


def test_to_number():
    assert to_number("42") == 42 and type(to_number("42")) is int
    assert to_number(" 3.5 ") == 3.5 and type(to_number(" 3.5 ")) is float
    assert to_number("-7") == -7
