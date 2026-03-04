#!/usr/bin/python3
"""module to write in a file"""


def write_file(filename="", text=""):
    """Write a text file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        t = f.write(text)

    return t
