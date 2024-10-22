"""Mutating Functions"""

__author__ = "730767580"

"""Global Variables"""
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1  # set list_2 equal to list_1

"""Append an integer to a list"""


def manual_append(my_list: list[int], num: int) -> None:
    my_list.append(num)  # forces the number to be added to the end of the list
    return None


"""Double the values of everything in a list"""


def double(my_list: list[int]) -> None:
    i: int = 0
    while i < len(my_list):  # Search through every element in the list
        my_list[i] = my_list[i] * 2
        i += 1
    return None


double(list_2)
print(list_1)
print(list_2)
