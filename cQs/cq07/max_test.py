"""Unit Tests for Max Function"""

__author__ = "730767580"

from find_max import find_and_remove_max

"""Expected Value Test"""


def test_returns_expected_value() -> None:
    nums: list[int] = [4, 2, 9, 5, 9, 3]
    result: int = find_and_remove_max(nums)
    assert result == 9  # Should return the largest number


"""Mutation Test"""


def test_mutates_input_correctly() -> None:
    nums: list[int] = [4, 2, 9, 5, 9, 3]
    find_and_remove_max(nums)
    assert nums == [4, 2, 5, 3]  # should remove all instances of 9 from the list


"""Empty List Test"""


def test_handles_empty_list() -> None:
    nums: list[int] = []
    result: int = find_and_remove_max(nums)
    assert result == -1  # Should return -1 for empty list
    assert nums == []  # should not modify an empty list
