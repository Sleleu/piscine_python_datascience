class calculator:
    """
    A class offering static methods for vector calculations.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.

        Args:
        V1: A list of floats representing the first vector.
        V2: A list of floats representing the second vector.
        """
        print(f"Dot product is: {sum(a * b for a, b in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Add two vectors and print the resulting vector.

        Args:
        V1: A list of floats representing the first vector.
        V2: A list of floats representing the second vector.
        """
        print(f"Add Vector is : {[float(a) + b for a, b in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtract one vector from another and print the resulting vector.

        Args:
        V1: A list of floats representing the vector to be subtracted from.
        V2: A list of floats representing the vector to subtract.
        """
        print(f"Sous Vector is: {[float(a) - b for a, b in zip(V1, V2)]}")
