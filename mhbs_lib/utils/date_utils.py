"""
This module provides date manipulation functions such as:
- Getting the first and last day of the month.
- Formatting dates.
- Getting the last day of the next and previous months.
"""

from datetime import datetime, timedelta
from .logger_utils import logging_var


def first_day_of_month(date: datetime) -> datetime:
    """
    Get the first day of the month for the given date.

    :param date: The input date.
    :return: A datetime object representing the first day of the month.
    :example:
    >>> today_str = "2024-06-19"
    >>> today = datetime.strptime(today_str, "%Y-%m-%d")
    >>> first_day_of_month(today)
    datetime.datetime(2024, 6, 1, 0, 0)
    """
    return date.replace(day=1)


def last_day_of_month(date: datetime) -> datetime:
    """
    Get the last day of the month for the given date.

    :param date: The input date.
    :return: A datetime object representing the last day of the month.
    :example:
    >>> today_str = "2024-06-19"
    >>> today = datetime.strptime(today_str, "%Y-%m-%d")
    >>> last_day_of_month(today)
    datetime.datetime(2024, 6, 30, 0, 0)
    """
    logging_var(f"Input: {datetime=}")

    date_28_day = date.replace(day=28)
    logging_var(f"{date_28_day=}")

    next_month_date = date_28_day + timedelta(days=4)
    logging_var(f"{next_month_date=}")

    next_month_date_days = next_month_date.day
    logging_var(f"{next_month_date_days=}")
    return next_month_date - timedelta(next_month_date_days)

print(last_day_of_month(datetime.strptime("2024-02-12", "%Y-%m-%d")))

def format_date(date: datetime, format_string: str) -> str:
    """
    Format a datetime object as a string.

    :param date: The input date.
    :param format_string: The format string.
    :return: A formatted date string.
    :example:
    >>> today_str = "2024-06-19"
    >>> today = datetime.strptime(today_str, "%Y-%m-%d")
    >>> format_date(today, "%Y-%m-%d")
    '2024-06-19'
    """
    return date.strftime(format_string)


def get_next_month(date: datetime) -> datetime:
    """
    Get the last day of the next month for the given date.

    :param date: The input date.
    :return: A datetime object representing the last day of the next month.
    :example:
    >>> today_str = "2024-06-19"
    >>> today = datetime.strptime(today_str, "%Y-%m-%d")
    >>> get_next_month(today)
    datetime.datetime(2024, 7, 31, 0, 0)
    """
    first_day_next_month = (date.replace(day=28) + timedelta(days=4)).replace(day=1)
    last_day_next_month = first_day_next_month.replace(day=28) + timedelta(days=4)
    return last_day_next_month - timedelta(days=last_day_next_month.day)


def get_last_month(date: datetime) -> datetime:
    """
    Get the last day of the previous month for the given date.

    :param date: The input date.
    :return: A datetime object representing the last day of the previous month.
    :example:
    >>> today_str = "2024-06-19"
    >>> today = datetime.strptime(today_str, "%Y-%m-%d")
    >>> get_last_month(today)
    datetime.datetime(2024, 5, 31, 0, 0)
    """
    first_day_of_current_month = date.replace(day=1)
    last_day_previous_month = first_day_of_current_month - timedelta(days=1)
    return last_day_previous_month
