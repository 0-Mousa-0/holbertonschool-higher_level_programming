#!/usr/bin/python3
"""module to write in a file"""


def append_write(filename="", text=""):
    """Append Write a text file"""
    with open(filename, mode="a", encoding="utf-8") as f:
        t = f.write(text)
        return t
