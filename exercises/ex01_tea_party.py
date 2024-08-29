"""Planning a Tea Party"""

__author__ = "730767580"


def main_planner(guests: int):
    """Display all the relevant information for the party"""
    print(f"A Cozy Tea Party for {guests} People!")
    # Getting the parameter values by calling defined functions
    tea_count = tea_bags(guests)
    treat_count = treats(guests)
    print(f"Tea Bags: {tea_count}")
    print(f"Treats: {treat_count}")
    print(f"Cost: ${cost(tea_count, treat_count)}")


def tea_bags(people: int) -> int:
    """Calculate the amount of tea bags that will be used"""
    # Two tea bags per person
    tea_count = people * 2
    return tea_count


def treats(people: int) -> int:
    """Calculate the amount of treats that will be eaten"""
    # Essentially 3 treats per person
    treat_count = int(tea_bags(people) * 1.5)
    return treat_count


def cost(tea_count: int, treat_count: int) -> float:
    # Essentially $3.25 per person
    """Calculate the cost of the tea party"""
    total = (tea_count * 0.5) + (treat_count * 0.75)
    return total


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
