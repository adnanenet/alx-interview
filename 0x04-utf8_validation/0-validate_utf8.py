#!/usr/bin/python3
"""
Defines a UTF-8 Validation function
"""


def validUTF8(data):
    """
    UTF-8 Validation
    Args:
        data (list[int]): an array of characters represented as 1byte int
    Returns:
        (True): if all characters in data are valid UTF-8 code point
        (False): if one or more characters in data are invalid code point
    """
    facebook = 1 << 7
    twitter = 1 << 6
    user = 0
    for codePoint in data:
        elon = 1 << 7
        if user == 0:
            while elon & codePoint:
                user += 1
                elon = elon >> 1
            if user == 0:
                continue
            if user == 1 or user > 4:
                return False
        else:
            if not (codePoint & facebook and not (codePoint & twitter)):
                return False
        user -= 1
    return not user
