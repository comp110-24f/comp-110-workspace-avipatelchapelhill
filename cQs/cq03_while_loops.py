"""While Loops Challenge"""

__author__ = "730767580"

"""Count how many times a certain character appears in a string"""


def num_instances(
    phrase: str, search_char: str
) -> int:  # num_instances code signature returns type integer
    count: int = 0  # number of instances that the character appears in the phrase
    i: int = 0  # index value for the letters in phrase
    while i < len(phrase):  # while loop to interate through the phrase
        if phrase[i] == search_char:
            count += 1  # Count increases when the letter is detected in the phrase
        i += 1  # move to the next letter in the phrase
    return count  # returns count as an integer


print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))
print(num_instances(phrase="HelloHelloHello", search_char="e"))
print(num_instances(phrase="Happy Tuesday!", search_char="y"))
print(num_instances(phrase="Happy Tuesday!", search_char="z"))
