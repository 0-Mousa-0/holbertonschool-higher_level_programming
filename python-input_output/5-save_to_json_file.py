#!/usr/bin/python3
"""save json into file"""
import json


def save_to_json_file(my_obj, filename):
    """object json into file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
