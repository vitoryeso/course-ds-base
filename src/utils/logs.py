"""
    Provides functions to create a logger objects.
"""

import logging
import sys
from typing import Text, Union


def get_console_handler() -> logging.StreamHandler:
    """Get console handler.
    Returns:
        logging.StreamHandler which logs into stdout.
    """

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname) - %(message)")
    console_handler.setFormatter(formatter)

    return console_handler

def get_file_handler(log_file: Text) -> logging.FileHandler:
    """Get file handlero.
    Returns:
        logging.FileHandler which logs into the specified file
    """
    pass;


def get_logger(name: Text = __name__,
               log_level: Union[Text, int] =
               logging.DEBUG) -> logging.Logger:
    """Get logger.
    Args:
        name {Text}: logger name
        log_level {Text or int}: logging level; string or int value
    Returns:
        logging.Logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # Prevent duplicated outputs in jupyter notebook
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(get_console_handler())
    logger.propagate = False

    return logger
