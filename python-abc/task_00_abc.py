#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    This class should be inherited by any class
    that represents a specific type of animal.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses.
        Should return the sound made by the animal.
        """
        pass


class Dog(Animal):
    """
    Concrete class representing a dog.
    Inherits from the Animal class and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound made by a dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Concrete class representing a cat.
    Inherits from the Animal class and implements the sound method.
    """
    def sound(self):
        """
        Returns the sound made by a cat.
        """
        return "Meow"
