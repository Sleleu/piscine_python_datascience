import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a 15-character random string composed of lowercase ASCII letters.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    A class representing a student with a unique login and ID.
    """
    name: str
    surname: str
    active: bool = field(default=True)
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """
        Post-initialization method to generate the login and id attributes
        based on the student's name and surname.
        """
        self.login: str = (self.name[0].upper() + self.surname[0:7].lower())
        self.id: str = generate_id()
