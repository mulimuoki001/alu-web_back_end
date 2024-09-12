#!/usr/bin/env python3


"""Filtered logger"""
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
        message = message.replace(
            f"{field}={message.split(f'{field}=')[1].split(';')[0]}",
            f"{field}={redaction}",
        )
    return message
