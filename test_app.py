import pytest

from src.app import add_two_numbers


def test_add_two_positive_numbers():
    assert add_two_numbers(2, 3) == 5


def test_add_positive_and_negative_number():
    assert add_two_numbers(10, -4) == 6


def test_add_zero_and_number():
    assert add_two_numbers(0, 7) == 7


def test_add_two_floats():
    assert add_two_numbers(2.5, 3.1) == pytest.approx(5.6)


def test_add_large_numbers():
    assert add_two_numbers(1_000_000, 2_000_000) == 3_000_000
