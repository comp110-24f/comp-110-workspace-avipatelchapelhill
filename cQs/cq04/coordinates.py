"""Prints the pairs of each character as strings"""

__author__ = "730767580"

"""Creates coordinates for the strings inputted into the function"""


def get_coords(xs: str, ys: str) -> None:
    i: int = 0  # Index tracking for string xs
    while i < len(xs):
        j: int = 0  # Index tracking for string ys
        while j < len(ys):
            print(f"{xs[i]},{ys[j]}")
            j += 1
        i += 1
    return None


if __name__ == "__main__":
    get_coords("12", "34")
