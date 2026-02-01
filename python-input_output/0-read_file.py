#!/usr/bin/python3
"""
read - write - excute .. files
"""


def read_file(filename=""):
    with open(filename, "r") as f:
        print(f.read(), end="")
