"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730767580"


"""Function to prompt for a 5-character word"""


def input_word() -> str:
    word = input("Enter a 5-character word: ")
    if len(word) != 5:  # Checks to make sure the inputted word is 5 characters long
        print("Error: Word must contain 5 characters.")
        exit()  # stops the program if the word was not 5 characters long
    return word


"""Function to prompt for a single character"""


def input_letter() -> str:
    letter = input("Enter a single character: ")
    if (
        len(letter) != 1
    ):  # Checks to make sure the inputted letter is only 1 character long
        print("Error: Character must be a single character.")
        exit()  # stops the program if the letter is not a single character
    return letter


"""Function to check the indices and count matches"""


def contains_char(word: str, letter: str) -> None:
    print(f"Searching for {letter} in {word}")
    count = 0  # Counter for matches
    # Check each index in the word
    for i in range(
        len(word)
    ):  # the for loop will iterate through every letter in the word
        if word[i] == letter:
            print(f"{letter} found at index {i}")
            count += 1  # increases the count if the letter was found in the word
    # Display results
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


"""Main function to coordinate everything"""


def main() -> None:
    word = input_word()  # Get 5-character word
    letter = input_letter()  # Get single character
    contains_char(word, letter)  # Search for character in the word


"""Start"""
if __name__ == "__main__":
    main()
