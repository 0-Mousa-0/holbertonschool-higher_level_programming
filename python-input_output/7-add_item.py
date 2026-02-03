#!/usr/bin/python3
"""json representation saved in a file"""
import sys

load = __import__("6-load_from_json_file").load
dump = __import__("5-save_to_json_file").dump

filename = sys.argv[0]

try:
    my_list = load(filename)
except Exception as e:
    my_list = []

my_list.extend(sys.argv[1:])
dump(my_list)
