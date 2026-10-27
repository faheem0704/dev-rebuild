import pytest

from ex03_errors import (
    InsufficientFundsError,
    get_port,
    parse_age,
    run_with_cleanup,
    safe_divide,
    withdraw,
)


def test_safe_divide():
    assert safe_divide(10, 4) == 2.5
    assert safe_divide(1, 0) is None


def test_parse_age_valid():
    assert parse_age("25") == 25
    assert parse_age(" 0 ") == 0


@pytest.mark.parametrize("bad", ["abc", "12.5", ""])
def test_parse_age_not_a_number(bad):
    with pytest.raises(ValueError, match="whole number"):
        parse_age(bad)


@pytest.mark.parametrize("bad", ["-1", "151"])
def test_parse_age_out_of_range(bad):
    with pytest.raises(ValueError, match="out of range"):
        parse_age(bad)


def test_withdraw():
    assert withdraw(100, 30) == 70
    with pytest.raises(ValueError):
        withdraw(100, 0)
    with pytest.raises(InsufficientFundsError, match="Need 500, have 100"):
        withdraw(100, 500)


def test_get_port():
    assert get_port({}) == 8080
    assert get_port({"port": 5432}) == 5432
    assert get_port({"port": "8000"}) == 8000
    for bad in ["http", 0, 70000, "-5"]:
        with pytest.raises(ValueError, match="Invalid port"):
            get_port({"port": bad})


def test_run_with_cleanup_success():
    log = []
    assert run_with_cleanup(lambda: 42, log) == 42
    assert log == ["cleanup"]


def test_run_with_cleanup_failure_still_cleans_up():
    log = []

    def boom():
        raise RuntimeError("disk on fire")

    with pytest.raises(RuntimeError):
        run_with_cleanup(boom, log)
    assert log == ["cleanup"]
