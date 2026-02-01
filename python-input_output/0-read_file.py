#!/usr/bin/python3
"""
read - write - excute .. files
"""


def read_file(filename=""):
    with open(filename, 'r' ,encoding='utf-8') as f:
        print(f.read(), end="")
