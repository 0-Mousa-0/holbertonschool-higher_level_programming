#!/usr/bin/python3
"""save json into file"""
import json


def save_to_json_file(my_obj, filename):
    """object json into file"""
    with open(filename, "w") as f:
<<<<<<< HEAD
        json.dump(my_obj , f)
=======
        json.dump(my_obj, f)
>>>>>>> a2fdb4a9e5f570e213b2dbac71c444e23b324593
