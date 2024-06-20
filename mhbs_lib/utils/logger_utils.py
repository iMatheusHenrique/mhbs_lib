"""
This module provides a configured logger for the project.
"""

import logging

LOGGING_FORMAT: str = (
    "[%(levelname)s] %(asctime)s - (%(filename)s: %(lineno)s - %(name)s) \n%(message)s"
    )

LOGGING_LEVEL: int = logging.INFO


logging.basicConfig(
    level=LOGGING_LEVEL,
    format=LOGGING_FORMAT,
)

logging_var = logging.getLogger(__name__)
