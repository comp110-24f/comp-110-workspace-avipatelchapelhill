"""File to define Fish class."""

__author__ = "730767580"


class Fish:

    age: int

    def __init__(self):
        """New Fish with age 0"""
        self.age: int = 0
        return None

    def one_day(self):
        """Simulate one day for a Fish by increasing its age by 1."""
        self.age += 1  # increase age of a fish by 1 each day
        return None
