#!/usr/bin/python3
"""Module to print text with 2 new lines after specific punctuation.

This module contains the function text_indentation(), which prints
a given text with two new lines after each occurrence of '.', '?', or ':'.
It also removes leading and trailing spaces from each printed line.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    The function processes the input text character by character.
    After encountering '.', '?', or ':', it prints the character followed
    by two new lines, and skips any whitespace characters that follow
    (spaces, tabs, or newlines) before the next non-whitespace character.

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    line = ""
    i = 0
    length = len(text)

    while i < length:
        ch = text[i]

        if ch in separators:
            line = line.rstrip()
            line += ch
            print(line, end="\n\n")
            line = ""

            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue

        if not line and ch == " ":
            i += 1
            continue

        line += ch
        i += 1

    line = line.strip()
    if line:
        print(line, end="")
