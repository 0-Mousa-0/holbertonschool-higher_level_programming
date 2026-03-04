#!/usr/bin/python3
"""CSV to JSON conversion module"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convert CSV file data to JSON and save it into data.json

    Args:
        filename (str): CSV file name

    Returns:
        bool: True if success, False if failure
    """
    try:
        data_list = []

        # Read CSV file
        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        # Write JSON file
        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (FileNotFoundError, OSError, csv.Error):
        return False
