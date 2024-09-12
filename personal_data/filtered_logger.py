#!/usr/bin/env python3


"""Filtered logger"""
import re
from typing import List


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
