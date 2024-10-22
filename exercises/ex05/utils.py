"""Implement List Utility Functions"""

__author__ = "730767580"

"""Creates a list of only even numbers"""


def only_evens(vals: list[int]) -> list[int]:
    even: list[int] = []
    for i in vals:
        if (i % 2) == 0:
            even.append(i)
    return even  # returns a new list of only even numbers


"""Creates a sublist of elements within a certain range"""


def sub(vals: list[int], start: int, end: int) -> list[int]:
    if start < 0:
        start = 0
    if end > len(vals):
        end = len(vals)
    if len(vals) == 0 or start >= len(vals) or end <= 0:
        return (
            []
        )  # returns empty list if there is an empty starting list or if the indexes are out of range
    return vals[start:end]  # returns a sublist of the original list


"""Adds an element in a list at a certain index"""


def add_at_index(vals: list[int], element: int, index: int) -> None:
    if index > len(vals) or index < 0:
        raise IndexError(
            "Index is out of bounds for the input list"
        )  # raises an error if index is greater than the length of the list
    vals.append(0)  # expands original list with a blank slot
    for i in range(len(vals) - 1, index, -1):
        vals[i] = vals[i - 1]  # shifts values to the right in a list
    vals[index] = element  # adds element at the index specified
    return None
