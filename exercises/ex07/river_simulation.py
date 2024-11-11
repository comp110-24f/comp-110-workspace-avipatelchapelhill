"""File to simulate river class"""

__author__ = "730767580"

from ex07.river import River

# Create a new River instance with 10 Fish and 2 Bears
my_river = River(10, 2)

# Test the one_river_week method
my_river.one_river_week()

# Call the view_river method to see the river status
my_river.view_river()
