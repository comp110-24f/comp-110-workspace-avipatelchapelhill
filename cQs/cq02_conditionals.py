"""Practicing with Conditionals"""

__author__ = "730767580"


def guess_a_number() -> None:  # Function signature for guess_a_number
    secret: int = 7  # defining the variable secret
    x = int(input("Guess a number: "))  # defining the variable x with user input
    print(f"Your guess was {x}")
    # Conditional statements to show whether the users guess equaled the secret number
    if x == secret:
        print("You got it!")
    elif x < secret:
        print(f"Your guess was too low! The secret number is {secret}")
    else:
        print(f"Your guess was too high! The secret number is {secret}")
    return None


# Calling the guess_a_number function
if __name__ == "__main__":
    guess_a_number()
