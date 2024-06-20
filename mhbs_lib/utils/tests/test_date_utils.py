"""
This module contains unit tests for the date manipulation functions defined in date_utils.py.
"""

from datetime import datetime
from mhbs_lib.utils.date_utils import (
    first_day_of_month,
    last_day_of_month,
    format_date,
    get_next_month,
    get_last_month
)


def test_first_day_of_month():
    """
    Test the first_day_of_month function.
    """
    date = datetime.strptime("2024-06-19", "%Y-%m-%d")
    expected = datetime.strptime("2024-06-01", "%Y-%m-%d")
    assert first_day_of_month(date) == expected


def test_last_day_of_month():
    """
    Test the last_day_of_month function.
    """
    date = datetime.strptime("2024-07-03", "%Y-%m-%d")
    expected = datetime.strptime("2024-07-31", "%Y-%m-%d")
    assert last_day_of_month(date) == expected


def test_format_date():
    """
    Test the format_date function.
    """
    date = datetime.strptime("2024-06-19", "%Y-%m-%d")
    expected = "2024-06-19"
    assert format_date(date, "%Y-%m-%d") == expected


def test_get_next_month():
    """
    Test the get_next_month function.
    """
    date = datetime.strptime("2024-06-19", "%Y-%m-%d")
    expected = datetime.strptime("2024-07-31", "%Y-%m-%d")
    assert get_next_month(date) == expected


def test_get_last_month():
    """
    Test the get_last_month function.
    """
    date = datetime.strptime("2024-06-19", "%Y-%m-%d")
    expected = datetime.strptime("2024-05-31", "%Y-%m-%d")
    assert get_last_month(date) == expected
