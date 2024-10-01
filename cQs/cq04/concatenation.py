"""Creates a concatentation of two strings"""

__author__ = "730767580"

"""Global Variables"""
word1: str = "happy"
word2: str = "tuesday"

"""Concatentation of two strings"""


def concat(string1: str, string2: str) -> str:
    output: str = string1 + string2
    return output


"""Call Function"""
if __name__ == "__main__":
    print(
        concat(string1=word1, string2=word2)
    )  # Call the function using the global variables defined above
