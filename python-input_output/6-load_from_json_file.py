#!/usr/bin/python3
"""load data from json file"""
import json


def load_from_json_file(filename):
    """load data into python object"""
    with open(filename, "r") as f:
        data = json.load(f)
        return data
