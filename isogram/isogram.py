"""
Isogram module.
"""

import re


def is_isogram(string):
    """
    Analyzes if the word is an isogram.

    :param str Word to analyze.
    """

    letters = re.findall(r"[a-zA-Z]", string.lower())
    return len(letters) == len(set(letters))
