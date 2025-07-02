def mean(args: tuple) -> float:
    """Calculate and return the mean of given arguments."""
    return sum(args) / len(args)


def median(args: tuple) -> float:
    """Calculate and return the median of given arguments."""
    sorted_args = sorted(args)
    n = len(args)
    if (n % 2 == 0):
        return (sorted_args[n // 2] + sorted_args[n // 2 - 1]) / 2
    return sorted_args[n // 2]


def quartile(args: tuple) -> list:
    """
    Calculate and return the first and third quartiles
    of given arguments.
    """
    sorted_args = sorted(args)
    inf_index = len(args) // 4
    sup_index = len(args) // 2 + len(args) // 4
    lst = [float(sorted_args[inf_index]), float(sorted_args[sup_index])]
    return lst


def std(args: tuple) -> float:
    """Calculate and return the standard deviation of given arguments."""
    m = mean(args)
    deviation = sum((i - m) ** 2 for i in args) / (len(args))
    std_dev = deviation ** 0.5
    return std_dev


def var(args: tuple) -> float:
    """Calculate and return the variance of given arguments."""
    return mean([(i - mean(args)) ** 2 for i in args])


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print the requested statistics for given arguments."""
    if not args:
        print("ERROR: No args provided")
    if not all(isinstance(i, int | float) for i in args):
        print("ERROR: Only int or float is accepted")
    try:
        for key, value in kwargs.items():
            if value == "mean":
                print(f"mean : {mean(args)}")
            elif value == "median":
                print(f"median : {median(args)}")
            elif value == "quartile":
                print(f"quartile : {quartile(args)}")
            elif value == "std":
                print(f"std : {std(args)}")
            elif value == "var":
                print(f"var : {var(args)}")
    except (ZeroDivisionError, TypeError, IndexError) as error:
        print(f"{__name__}: {type(error).__name__}: {error}")
