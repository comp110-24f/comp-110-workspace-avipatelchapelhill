"""Define Unit Tests for Utility Functions"""

__author__ = "730767580"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""only_evens Unit Tests"""
"""Expected Value"""


def test_oe_returns_expected_value() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    result: list[int] = only_evens(nums)
    assert result == [4, 2, 4]  # should return only even numbers in a list


"""Mutations Test"""


def test_oe_mutates_input_correctly() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    only_evens(nums)
    assert nums == [4, 2, 9, 5, 4, 3]  # should not mutate the inputted list


"""Edge Case Test"""


def test_oe_handles_no_even_numbers() -> None:
    nums: list[int] = [5, 3, 7, 9, 3]
    result: list[int] = only_evens(nums)
    assert result == []  # should return empty list if no evens


"""sub Unit Tests"""
"""Expected Value"""


def test_sub_returns_expected_value() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    result: list[int] = sub(nums, 1, 4)
    assert result == [2, 9, 5]  # should return only elements in specific range


"""Mutations Test"""


def test_sub_mutates_input_correctly() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    sub(nums, 1, 4)
    assert nums == [4, 2, 9, 5, 4, 3]  # should not mutate the inputted list


"""Edge Case Test"""


def test_sub_handles_negative_start_index() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    result: list[int] = sub(nums, -1, 4)
    assert result == [4, 2, 9, 5]  # function starts at beginning of list


"""add_at_index Tests"""
"""Expected Value"""


def test_aai_returns_expected_value() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    result = add_at_index(nums, 5, 2)
    assert result == None  # Should not return anything


"""Mutations Test"""


def test_aai_mutates_input_correctly() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    nums == add_at_index(nums, 5, 2)
    assert nums == [4, 2, 5, 9, 5, 4, 3]  # should mutate the inputted list


"""Edge Case Test"""


def test_aai_handles_raises_indexerror() -> None:
    nums: list[int] = [4, 2, 9, 5, 4, 3]
    with pytest.raises(IndexError):
        add_at_index(nums, 5, 10)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
