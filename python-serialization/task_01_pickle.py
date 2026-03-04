#!/usr/bin/python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """A simple custom object for serialization"""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print object attributes in required format"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object to a file using pickle.
        Returns True if success, None if failure.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except (FileNotFoundError, pickle.PickleError, OSError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a pickle file.
        Returns CustomObject instance or None if failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except (FileNotFoundError, pickle.PickleError, EOFError, OSError):
            return None
