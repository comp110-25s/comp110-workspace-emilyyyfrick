"""Exercise 03 Dictionary Test"""

___author___ = "730566891"

from exercises.ex03.dictionary import invert, count, favorite_color, bin_len
import pytest


def test_invert_1() -> None:
    """Invert Use Case 01"""
    dictionary: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    inverted_dictionary: dict[str, str] = {"z": "a", "y": "b", "x": "c"}
    assert invert(dictionary) == inverted_dictionary


def test_invert_2() -> None:
    """Invert Use Case 02"""
    dictionary: dict[str, str] = {"apple": "cat"}
    inverted_dictionary: dict[str, str] = {"cat": "apple"}
    assert invert(dictionary) == inverted_dictionary


def test_invert_3() -> None:
    """Invert Edge Case"""
    dictionary: dict[str, str] = {"kris": "jordan", "michael": "jordan"}
    with pytest.raises(KeyError):
        invert(dictionary)


def test_count_1() -> None:
    """Count Use Case 01"""
    count_1: list[str] = ["dog", "cat", "dog", "fish", "bird"]
    count_2: dict[str, int] = {"dog ": 2, "cat": 1, "fish": 1, "bird": 1}
    assert count(count_1) == count_2


def test_count_2() -> None:
    """Count Use Case 02"""
    count_1: list[str] = ["beach", "beach", "lake", "mountains", "lake"]
    count_2: dict[str, int] = {"beach": 2, "lake": 2, "mountains": 1}
    assert count(count_1) == count_2


def test_count_3() -> None:
    """Count Edge Case"""
    assert count([]) == {}


def test_favorite_color_1() -> None:
    """Favorite Color Use Case 01"""
    favorite_color_1: dict[str, str] = {
        "Emily": "Pink",
        "Willow": "Green",
        "Elizabeth": "Pink",
        "Maddie": "Blue",
    }
    favorite_color_2: str = "Pink"
    assert favorite_color(favorite_color_1) == favorite_color_2


def test_favorite_color_2() -> None:
    """Favorite Color Use Case 02"""
    favorite_color_1: dict[str, str] = {"Unc": "Blue", "State": "Red", "Duke": "Blue"}
    favorite_color_2: str = "Blue"
    assert favorite_color(favorite_color_1) == favorite_color_2


def test_favorite_color_3() -> None:
    """Favorite Color Edge Case"""
    assert favorite_color({}) == ""


def test_bin_len_1() -> None:
    """Bin Len Use Case 01"""
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_ben_len_2() -> None:
    """Bin Len Use Case 02"""
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_ben_len_3() -> None:
    """Bin Len Edge Case"""
    assert bin_len([]) == {}
