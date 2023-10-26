import sys

morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}


def ft_sos() -> None:
    """
    Converts command-line arguments into Morse code and prints the result.

    Raises:
        AssertionError: If there are command-line arguments or invalid
        characters in the input.
    """
    if len(sys.argv) != 2:
        raise AssertionError
    morse_code = ''
    for arg in sys.argv[1:]:
        for letter in arg:
            if letter.upper() not in morse_dict:
                raise AssertionError
            morse_code += morse_dict[letter.upper()] + ' '
        morse_code += '/ '
    print(morse_code.rstrip('/ '))


def main():
    try:
        ft_sos()
    except AssertionError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
