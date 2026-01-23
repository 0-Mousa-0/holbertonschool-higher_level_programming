#!/usr/bin/python3
"""
this module is to print text in correctly way
"""


def text_indentation(text):
    """
    :param text: to be printed in correctly way
    :return: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if isinstance(text, str):
        for char in text:
            if char == "." or char == "?" or char == ":":
                print(char + "$")
                print("$")
            elif char == '"':
                pass
            else:
                print(char, end="")
