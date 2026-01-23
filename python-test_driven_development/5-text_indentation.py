#!/usr/bin/python3
"""
module print the text in a role
"""


def text_indentation(text):
    """

    :param text: to be printed
    :return: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] == " " and (i == 0 or text[i - 1] in ".?:"):
            i += 1
            continue

        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue

        i += 1
