import sys


def text_analyzer(text=None) -> None:
    """
    Analyze and provide statistics about the given text.

    This function takes a text input, either provided as an argument
    or prompted to the user, and prints out the number of:
    - Total characters (including whitespace and punctuation)
    - Uppercase letters
    - Lowercase letters
    - Punctuation marks
    - Whitespaces (spaces, tabs, and newlines)
    - Digits

    Parameters:
    - text (str, optional): The string to be analyzed. If not provided,
                            the user will be prompted to input the text.

    Returns:
    - None: This function does not return any value.
            It prints the statistics directly.
    """

    if (text is None):
        text = input('What is the text to analyze?\n >> ') + '\n'
    try:
        assert isinstance(text, str), "argument is not a string"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return

    punctuations = r'!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
    upper, lower, punctuation, space, digit = 0, 0, 0, 0, 0

    for letter in text:
        if letter.isupper():
            upper += 1
        elif letter.islower():
            lower += 1
        elif letter in punctuations:
            punctuation += 1
        elif letter.isspace():
            space += 1
        elif letter.isdigit():
            digit += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


def main():
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
    except AssertionError as error:
        print(f"AssertionError: {error}")
        return
    text = sys.argv[1] if len(sys.argv) == 2 else None
    text_analyzer(text)


if __name__ == "__main__":
    main()
