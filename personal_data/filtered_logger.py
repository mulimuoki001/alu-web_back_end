#!/usr/bin/env python3


"""Filtered logger"""
import re
from typing import List
import logging


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
