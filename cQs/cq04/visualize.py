"""See a function in action from a different file"""

__author__ = "730767580"

"""Imports list of functions"""
from concatenation import concat
from coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))  # Calls the imported function with the new global variables
get_coords(x, y)  # Calls the imported function with the new global variables
