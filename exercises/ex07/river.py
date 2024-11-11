"""File to define River class."""

__author__ = "730767580"

from ex07.fish import Fish
from ex07.bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for i in range(0, num_fish):
            self.fish.append(Fish())
        for i in range(0, num_bears):
            self.bears.append(Bear())
        return None

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5."""
        # Remove fish older than 3
        surviving_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                surviving_fish.append(fish)
        self.fish = surviving_fish
        # Remove bears older than 5
        surviving_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                surviving_bears.append(bear)
        self.bears = surviving_bears
        return None

    def bears_eating(self):
        """Each Bear eats 3 Fish if there are at least 5 Fish available."""
        for bear in self.bears:  # iterate through every bear
            if len(self.fish) >= 5:
                bear.eat(3)  # feed the bears that are itereated through
                self.remove_fish(3)
        return None

    def check_hunger(self):
        """Remove bears with a hunger_score less than 0."""
        surviving_bears = []
        for bear in self.bears:  # iterate through every bear
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)  # add to the bears that are surviving
        self.bears = surviving_bears  # define the old bears equal to ones that survived

    def remove_fish(self, amount: int):
        """Remove the specified number of fish from the front of the list."""
        for i in range(amount):
            if self.fish:
                self.fish.pop(0)  # removes fish from river
        return None

    def repopulate_fish(self):
        """Each pair of Fish produces 4 new Fish."""
        num_new_fish = (len(self.fish) // 2) * 4
        for i in range(num_new_fish):
            self.fish.append(Fish())  # continuously adds fish if condition is met
        return None

    def repopulate_bears(self):
        """Each pair of Bears produces 1 new Bear."""
        num_new_bears = len(self.bears) // 2
        for i in range(num_new_bears):
            self.bears.append(Bear())  # continuously adds bears if condition is met
        return None

    def view_river(self):
        """Print the current status of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")  # fish population
        print(f"Bear population: {len(self.bears)}")  # bear population
        return None

    def one_river_week(self):
        """Simulate one week in the river"""
        for i in range(7):  # 7 days in the river
            self.one_river_day()
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
        return None
