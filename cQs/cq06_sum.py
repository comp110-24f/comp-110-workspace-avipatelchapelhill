"""Summing the elements of a list using different loops"""

__author__ = "730767580"

"""Find sum of a list using a while loop"""


def w_sum(vals: list[float]) -> float:
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


"""Find sum of a list using a for in loop"""


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in vals:
        sum += i
    return sum


"""Find sum of a list using the range keyword"""


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum


# I have had 0 challenges with this question thus why I did not write any comments
