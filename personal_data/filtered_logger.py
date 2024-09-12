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
        if field in message:
            value = message.split(field + "=")[1].split(";")[0]
        message = re.sub(value, redaction, message)
    return message


fields = ["password", "date_of_birth"]
messages = [
    "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
    "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;",
]

for message in messages:
    print(filter_datum(fields, "xxx", message, ";"))
