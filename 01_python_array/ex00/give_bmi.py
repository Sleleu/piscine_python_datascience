import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """
    Calculate BMI for given lists of heights and weights.

    Parameters:
    - height (list[int | float]): List of heights in meters.
    - weight (list[int | float]): List of weights in kilograms.

    Returns:
    - list[int | float]: List of BMIs.
    """
    try:
        if isinstance(height, list) is False\
                or isinstance(weight, list) is False:
            raise ValueError("Bad type of parameters")
        height_array = np.array(height)
        weight_array = np.array(weight)
        bmi = weight_array / height_array ** 2
        return list(bmi)
    except (ValueError, TypeError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check if each BMI in the list is below a given limit.

    Parameters:
    - bmi (list[int | float]): List of BMIs.
    - limit (int): Threshold value.

    Returns:
    - list[bool]: List indicating if each BMI is below the limit.
    """
    try:
        limit_list: list = [True if i > limit else False for i in bmi]
        return limit_list
    except TypeError as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
        exit(1)
