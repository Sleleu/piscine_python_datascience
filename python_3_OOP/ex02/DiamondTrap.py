from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing class King who herited from Baratheon and Lannister."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a King."""
        super().__init__(first_name, is_alive)

    def get_eyes(self):
        """Return the eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """Return the hairs attribute"""
        return self.hairs

    def set_eyes(self, eyes: str):
        """Set the eyes attribute to the eyes parameter"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """Set the hairs attribute to the hairs parameter"""
        self.hairs = hairs
