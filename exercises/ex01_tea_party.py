"""Planning a Tea Party"""

__author__ = "730767580"


def main_planner(guests: int) -> None:
    """Display all the relevant information for the party"""
    print(f"A Cozy Tea Party for {guests} People!")
    # Getting the parameter values by calling defined functions
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")
    return None


def tea_bags(people: int) -> int:
    """Calculate the amount of tea bags that will be used"""
    # Two tea bags per person
    return people * 2


def treats(people: int) -> int:
    """Calculate the amount of treats that will be eaten"""
    # Essentially 3 treats per person
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    # Essentially $3.25 per person
    """Calculate the cost of the tea party"""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
