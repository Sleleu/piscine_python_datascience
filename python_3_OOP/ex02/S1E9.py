from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class representing a character."""
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a character with a first name
        and an indication of whether they are alive.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Abstract method to indicate that the character dies."""
        pass


class Stark(Character):
    """Class representing a character from the Stark family."""
    def die(self):
        """
        Indicates that the Stark character dies
        by setting is_alive to False.
        """
        self.is_alive = False
