#!/usr/bin/env python3
"""This module holds filter_datum method"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str):
    """Replace sensitive info with an alternate string"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message