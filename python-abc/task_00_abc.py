#!/usr/bin/python3
"""abc class"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """abc for Animal"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """docstring for Dog"""

    def sound(self):
        """docstring for Dog"""

        return "Bark"


class Cat(Animal):
    """docstring for Cat"""

    def sound(self):
        """docstring for Cat"""
        return "Meow"
