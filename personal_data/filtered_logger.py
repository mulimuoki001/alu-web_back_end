#!/usr/bin/env python3


"""Filtered logger"""
import re
from typing import List
import logging
import os
import mysql.connector


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Constructor"""
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records

        Args:
            record (logging.LogRecord): incoming log record
        Returns:
            str: formatted log record
        """
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Filter a log line

    Args:
        fields (List[str]): list of fields
        redaction (str): string to replace with
        message (str): message to filter
        separator (str): separator for fields
    Returns:
        str: filtered message
    """
    for field in fields:
        pattern = rf"{field}=([^{separator}]*)"
        message = re.sub(
            pattern,
            lambda m: m.group(0).split("=")[0] + "=" + redaction,
            message,
            flags=re.IGNORECASE,
        )
    return message


PII_FIELDS = (
    "name",
    "email",
    "phone",
    "ssn",
    "password",
)


def get_logger() -> logging.Logger:
    """Get a logger"""
    # Create a logger with the specified name and level
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False  # Do not propagate messages to other loggers

    # Create a StreamHandler with a RedactingFormatter
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(piis=PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Get a database"""
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "guru1")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "15121")
    database = os.getenv("PERSONAL_DATA_DB_NAME")
    db = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    return db
