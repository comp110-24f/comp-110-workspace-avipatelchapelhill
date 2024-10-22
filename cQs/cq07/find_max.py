"""Finding and Removing Max Numbers"""

__author__ = "730767580"

"""Finds the max number in a list and removes all instances of that number"""


def find_and_remove_max(nums: list[int]) -> int:
    if nums == []:
        return -1
    max_value: int = max(nums)
    i: int = 0
    while i < len(nums):
        if nums[i] == max_value:
            nums.pop(i)  # remove all instances of the max number
        else:
            i += 1
    return max_value
