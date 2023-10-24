from ft_filter import ft_filter
import sys


def is_punct(word: str) -> bool:
    """
    Check if the given word contains any punctuation or whitespace characters.

    Args:
    - word (str): The word to check.

    Returns:
    - bool: True if the word contains punctuation or whitespace characters,
            False otherwise.
    """
    punctuations = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    for char in word:
        if char.isspace() or char in punctuations:
            return True
    return False


def filterstring(string: str, integer: int) -> None:
    """
    Filter and print words from a given string based on their
    length and absence of punctuation.

    Args:
    - string (str): The input string.
    - integer (int): The length threshold.

    Prints:
    - List of words from the string that are longer than the provided
      integer and don't contain punctuation.
    """
    words_list = [word for word in string.split() if is_punct(word) is False]
    filtered_str = ft_filter(lambda x: len(x) > integer, words_list)
    print(filtered_str)


def main():
    try:
        assert len(sys.argv) == 3
        try:
            integer = int(sys.argv[2])
        except ValueError:
            integer = None
        assert isinstance(integer, int)
    except AssertionError:
        print("AssertionError: the arguments are bad")
        exit(1)
    filterstring(sys.argv[1], integer)


if __name__ == "__main__":
    main()
