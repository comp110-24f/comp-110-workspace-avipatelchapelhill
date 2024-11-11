"""File to define Bear class."""

__author__ = "730767580"


class Bear:

    age: int
    hunger_score: int

    def __init__(self):
        """New Bears with fish 0 and hunger 0"""
        self.age: int = 0
        self.hunger_score: int = 0
        return None

    def one_day(self):
        """Simulate one day for a Bear."""
        self.age += 1  # increasing age by 1
        self.hunger_score -= 1  # decreasing hunger by 1 cuz bears get hungry
        return None

    def eat(self, num_fish: int):
        """Change the hunger score by eating"""
        self.hunger_score += (
            num_fish  # Increase the hunger_score by the number of fish eaten.
        )
        return None
