"""
This module contains unit tests for the logging setup defined in logger.py.
"""

import logging
from ..logger_utils import logging_var


def test_logger_format():
    """
    Test if the logger instance is correctly formatted.

    This test checks whether the logging_var is an instance of the
    logging.Logger class. It ensures that the logger is properly
    initialized and formatted.

    Assertions:
        - logging_var is an instance of logging.Logger.
    """
    assert isinstance(logging_var, logging.Logger)


def test_logger_info_level(caplog):
    """
    Test logging at INFO level.

    This test checks whether a message logged at INFO level is correctly
    captured by the logger.

    Assertions:
        - The log message is captured.
        - The log message level is INFO.
    """
    with caplog.at_level(logging.INFO):
        logging_var.info("This is an info message.")
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "INFO"
    assert caplog.records[0].message == "This is an info message."


def test_logger_error_level(caplog):
    """
    Test logging at ERROR level.

    This test checks whether a message logged at ERROR level is correctly
    captured by the logger.

    Assertions:
        - The log message is captured.
        - The log message level is ERROR.
    """
    with caplog.at_level(logging.ERROR):
        logging_var.error("This is an error message.")
    assert len(caplog.records) == 1
    assert caplog.records[0].levelname == "ERROR"
    assert caplog.records[0].message == "This is an error message."

