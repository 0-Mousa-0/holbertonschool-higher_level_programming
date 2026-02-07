#!/usr/bin/python3
"""XML Serialization and Deserialization Module"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML file.

    Args:
        dictionary (dict): Data to serialize
        filename (str): Output XML file
    """
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as children
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Create tree and write to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML file into a Python dictionary.

    Args:
        filename (str): XML file name

    Returns:
        dict: Deserialized data
    """
    result = {}

    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Rebuild dictionary
    for child in root:
        result[child.tag] = child.text

    return result
