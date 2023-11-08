from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Initialize a Baratheon family member."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return the string representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return representation of the Baratheon character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Indicates that the Baratheon character dies
        by setting is_alive to False.
        """
        self.is_alive = False

    def create_baratheon(first_name, is_alive=True):
        """Class method to create a Baratheon family member."""
        return Baratheon(first_name, is_alive)


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        """Initialize a Lannister family member."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __repr__(self):
        """Return the string representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __str__(self):
        """Return representation of the Lannister character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Indicates that the Lannister character dies
        by setting is_alive to False.
        """
        self.is_alive = False

    def create_lannister(first_name, is_alive=True):
        """Class method to create a Lannister family member."""
        return Lannister(first_name, is_alive)
