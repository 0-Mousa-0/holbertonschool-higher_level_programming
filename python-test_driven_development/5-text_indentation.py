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
    line = ""
    if isinstance(text, str):
        for char in text:
            if char == "." or char == "?" or char == ":":
                line += char
                print(line, end="\n\n")
                line = ""
        
            elif not line and char == " ":
                continue
            else:
                line += char
        if line:
            print(line, end="")
