"""Creating A Pre-Wordle Game"""

__author__ = "730767580"

"""Checks that the users guess is equal to the secret word length"""


def input_guess(secret_word_len: int) -> str:
    guess_input: str = input(f"Enter a {secret_word_len} character word: ")
    while (
        len(guess_input) != secret_word_len
    ):  # if the lengths don't match continue asking for a valid guess
        guess_input: str = input(f"That wasn't {secret_word_len} chars! Try Again: ")
    return guess_input


"""Checks to see if a character is anywhere in the secret word"""


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert (
        len(char_guess) == 1
    )  # Will raise and error if the length of the character guessed is not 1
    i: int = 0
    while i < len(secret_word):
        if char_guess != secret_word[i]:
            i += 1
        else:
            return True
    return False


"""Represent the accuracy of the guess in terms of emojis"""


def emojified(guess_made: str, secret: str) -> str:
    assert len(guess_made) == len(
        secret
    )  # Will raise an error if the length of the guess and secret word don't match
    white: str = "\U00002B1C"  # white unicode for emoji block
    green: str = "\U0001F7E9"  # green unicode for emoji block
    yellow: str = "\U0001F7E8"  # yellow unicode for emoji block
    i: int = 0
    emojis: str = ""  # sets up a string for the emojis to printed in
    while i < len(secret):
        if (
            contains_char(
                secret_word=secret, char_guess=guess_made[i]
            )  # character correct and in correct position
            and guess_made[i] == secret[i]
        ):
            emojis += green
            i += 1
        elif (
            contains_char(
                secret_word=secret, char_guess=guess_made[i]
            )  # character correct but wrong position
            and guess_made[i] != secret[i]
        ):
            emojis += yellow
            i += 1
        else:
            emojis += white  # character is not used in word
            i += 1
    return emojis  # prints the string of emojis


"""Runs the entire program from start to finish"""


def main(secret: str) -> None:
    i: int = 1
    # Since the unicode for the green block wasn't global variables i made it local in this function
    green: str = "\U0001F7E9"
    while (
        i <= 6
    ):  # While loop to keep track of how many turns remain for the user to guess
        print(f"=== Turn {i}/6 ===")
        user_guess = input_guess(secret_word_len=len(secret))
        print(emojified(guess_made=user_guess, secret=secret))
        if emojified(guess_made=user_guess, secret=secret) == (green * len(secret)):
            print(f"You won in {i}/6 turns!")
            return None
        else:
            i += 1
    print("X/6 - Sorry, try again tomorrow!")
    return None


"""Allows the code to run as a module"""
if __name__ == "__main__":
    main(secret="codes")
