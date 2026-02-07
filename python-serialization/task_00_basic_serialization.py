#!/usr/bin/python3
"""Basic Serialization Module"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Dictionary to serialize
        filename (str): Output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Deserialized data
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
