#!/usr/bin/env python3
""""0. Regex-ing"""
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """a function that returns the log message obfuscated"""
    for field in fields:
        message = re.sub(field + "=" + ".*?" + separator,
                         field + "=" + redaction + separator,
                         message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """a funtion that returns the log message obfuscated"""
        msg = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """A logger function"""
    log = logging.getLogger('user_data')
    log.propagate = False
    stream = logging.StreamHandler()
    stream.setFormatter(RedactingFormatter(PII_FIELDS))
    log.addHandler(stream)
    return log
