import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Prints the shape of a 2D array and returns a truncated
    version based on start and end arguments.

    Parameters:
    - family (list): 2D list to be sliced.
    - start (int): Starting index.
    - end (int): Ending index.

    Returns:
    - list: Sliced 2D list.
    """
    try:
        if isinstance(family, list) is False:
            raise ValueError("Bad type of parameters")
        print(f"My shape is : {np.shape(family)}")
        sliced_family = family[start:end]
        print(f"My new shape is : {np.shape(sliced_family)}")
        return sliced_family
    except (ValueError, TypeError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)
