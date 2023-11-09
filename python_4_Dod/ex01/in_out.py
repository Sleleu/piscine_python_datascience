def square(x: int | float) -> int | float:
    """Calculate the square of a number."""
    return x * x


def pow(x: int | float) -> int | float:
    """Calculate the exponentiation of a number by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Generate a closure that calculates the result of applying the provided
    function to its previous result.
    
    Parameters:
    x (int | float): The initial number to use in the calculation.
    function (callable): The function to apply to the number.

    Returns:
    A function that when called, returns the result of the function 
    applied to its last returned value.
    """
    count = 0

    def inner() -> float:
        """
        When called, calculate and return the next value in the sequence
        based on the outer function's parameters.

        Returns:
        float: The next number in the sequence after applying the function.
        """
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
