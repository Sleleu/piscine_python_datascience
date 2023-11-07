class calculator:
    """A calculator class that performs vector operations with a scalar."""
    def __init__(self, object):
        """Initialize the Calculator with a vector (list of numbers)."""
        self.object = object

    def __add__(self, object) -> None:
        """Add a number for each element and print the result."""
        self.object = [i + object for i in self.object]
        print(self.object)

    def __mul__(self, object) -> None:
        """Multiply each element by a number and print the result."""
        self.object = [i * object for i in self.object]
        print(self.object)

    def __sub__(self, object) -> None:
        """Substract a number for each element and print the result."""
        self.object = [i - object for i in self.object]
        print(self.object)

    def __truediv__(self, object) -> None:
        """Divide each element by a number and print the result."""
        try:
            self.object = [i / object for i in self.object]
            print(self.object)
        except ZeroDivisionError as error:
            print(f"{error.__class__.__name__}: {error}")
