"""Practicing with Lists"""

___author__ = "730767580"

"""Checks to see if every element in the list equals the number"""


def all(my_list: list[int], num: int) -> bool:
    i: int = 0
    if len(my_list) > 0:  # only goes through these actions if the list is not empty
        while i < len(my_list):
            if my_list[i] != num:
                return False
            else:
                i += 1
        return True
    else:
        return False


"""Returns the maximum value of a list"""


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError(
            "max() arg is an empty List"
        )  # Raises an error if the list is empty
    else:
        i: int = 0
        x = input[i]
        while i < len(input):
            if input[i] > x:
                x = input[i]
                i += 1
            else:
                i += 1
    return x


"""Checks to see if two lists are exactly equal to each other"""


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(
        list2
    ):  # Only goes through the actions if the lists are equal in length
        return False
    else:
        i: int = 0
        while i < len(list1):
            if list1[i] == list2[i]:
                i += 1
            else:
                return False
        return True


"""Appends a new list to the original list"""


def extend(original: list[int], new: list[int]) -> None:
    i: int = 0
    while i < len(new):
        original.append(new[i])
        i += 1
    return None


# I won't lie I have had 0 struggle on this assignment (took me less than 10 minutes) so I kinda just added random comments
