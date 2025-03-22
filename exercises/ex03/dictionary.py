"""Exercise 03 Dictionary"""

___author___ = "730566891"


def invert(list_01: dict[str, str]) -> dict[str, str]:
    """Function that inverts keys and values"""
    inverted_list: dict[str, str] = {}
    for key in list_01:
        if list_01[key] in inverted_list:
            raise KeyError("Repeat key error.")
        inverted_list[list_01[key]] = key
    return inverted_list


def count(list_02: list[str]) -> dict[str, int]:
    """Function that given a unique key is associated with the count of a number."""
    empty_list: dict[str, int] = {}
    for key in list_02:
        if key in empty_list:
            empty_list[key] += 1
        else:
            empty_list[key] = 1
    return empty_list


def favorite_color(list_03: dict[str, str]) -> str:
    """Function that returns the color which appears most frequently."""
    results: str = ""
    colors: list[str] = []
    favorite = 0
    for key in list_03:
        colors.append(list_03[key])
    number_count: dict[str, int] = count(colors)
    for key in number_count:
        if favorite < number_count[key]:
            favorite = number_count[key]
            results = key
    return results


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Function that sorts words based on length"""
    sorted: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in sorted:
            sorted[length].add(word)
        else:
            sorted[length] = {word}
    return sorted
