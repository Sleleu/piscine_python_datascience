def mean(args: tuple) -> float:
    return sum(args) / len(args)

def median(args: tuple) -> float:
    sorted_args = sorted(args)
    middle_index = len(args) // 2
    return sorted_args[middle_index]

def quartile(args: tuple) -> list:
    sorted_args = sorted(args)
    inf_index = len(args) // 4
    sup_index = len(args) // 2 + len(args) // 4
    lst = [float(sorted_args[inf_index]), float(sorted_args[sup_index])]
    return lst

def ft_statistics(*args: any, **kwargs: any) -> None:
    try:
        for key, value in kwargs.items():
            if value == "mean":
                print(f"mean : {mean(args)}")
            elif value == "median":
                print(f"median : {median(args)}")
            elif value == "quartile":
                print(f"quartile : {quartile(args)}")
    except ZeroDivisionError:
        print("ERROR")
