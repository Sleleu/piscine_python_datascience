def ft_tqdm(lst: range) -> None:
    """
    Display a progress bar for each item in lst.

    Args:
    - lst (range): Iterable of items to process.
    """
    count = len(lst)
    bar_length = 67
    for i in range(count):
        percentage = (i / count * 100) + 1
        bar = '=' * int((percentage / 100) * bar_length) + '>'
        print(f"\r{str(int(percentage)).rjust(3, ' ')}%|", end="")
        print(f"[{bar.ljust(bar_length,' ')}]| ", end="")
        print(f"{i + 1}/{count} ", end="")
        yield i
