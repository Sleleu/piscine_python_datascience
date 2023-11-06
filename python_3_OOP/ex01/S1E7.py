from S1E9 import Character


class Baratheon(Character):

    def __init__(self, first_name, is_alive=True, eyes="brown", hairs="dark"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return "yoo"

    def die(self):
        self.is_alive = False

    def create_baratheon(first_name, is_alive=True):
        return Baratheon(first_name, is_alive)


class Lannister(Character):

    def __init__(self, first_name, is_alive=True, eyes="blue", hairs="light"):
        self.first_name = first_name
        self.is_alive = is_alive
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return "yoo"

    def die(self):
        self.is_alive = False

    def create_lannister(first_name, is_alive=True):
        return Lannister(first_name, is_alive)