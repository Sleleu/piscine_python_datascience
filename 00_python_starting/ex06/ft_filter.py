def ft_filter(function, iterable):
    """
    filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable
    for which function(item) is true. If function is None,
    return the items that are true.
    """
    if function is None:
        return [i for i in iterable if i]
    else:
        return [i for i in iterable if function(i)]


if __name__ == "__main__":
    print("----- EVEN FUNCTION -----")
    print(ft_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

    print("----- NONE FUNCTION -----")
    print(ft_filter(None, [1, 'a', 0, False, True, '0']))

    print("----- VOWEL FUNCTION -----")

    def filter_vowels(letter):
        vowels = ['a', 'e', 'i', 'o', 'u']
        return True if letter in vowels else False
    print(ft_filter(filter_vowels, 'salutyoyo'))
