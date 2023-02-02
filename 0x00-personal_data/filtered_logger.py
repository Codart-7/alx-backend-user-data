#!/usr/bin/env python3
"""A function that returns an obfuscated log message"""
import re
import typing


def filter_datum(fields: List[str], redaction: str, message: str,
                separator: str) -> str:
    """obfuscator function"""
    for field in fields:
        message = re.sub(field + "=" + ".*?" + separator,
                        field + "=" + redaction + separator,
                        message)
    return message