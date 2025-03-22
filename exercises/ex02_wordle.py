"""Exercise 02 Wordle."""

__author__: str = "730566891"


def contains_char(string_to_search: str, character_to_find: str) -> bool:
    """Function to check if a specified character is in a word."""
    assert len(character_to_find) == 1, f"len('{character_to_find}') is not 1"
    i = 0
    # Loop through string to search's indices for character to find.
    while i < len(string_to_search):
        if string_to_search[i] == character_to_find:
            return True
        i += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis comparing guess word and secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result_string: str = ""

    i = 0
    # Loops through guess and returns corresponding emojis for characters.
    while i < len(guess):
        if guess[i] == secret[i]:
            result_string += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result_string += YELLOW_BOX
        else:
            result_string += WHITE_BOX
        i += 1

    return result_string


def input_guess(guess_length: int) -> str:
    """Function to verify guess length"""
    # Prompts user for a guess.
    guess_input = input(f"Enter a {guess_length} character word: ")
    # Checks if input length is valid and asks for new input if not.
    while len(guess_input) != guess_length:
        guess_input = input(f"That wasn't {guess_length} chars! Try again: ")

    return guess_input


def main(secret: str) -> None:
    """The entry point of the program and main game"""
    turn = 1
    playing = True
    # While loop to run through games turns.
    while turn <= 6 and playing is True:
        print(f"===Turn {turn}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret))
        # Checks if guess correct. Success message if correct, moves on for incorrect.
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            playing = False
        elif turn == 6:
            print("X/6 - Sorry, try again tomorrow!")
            playing = False
        else:
            turn += 1


if __name__ == "__main__":
    main(secret="codes")
