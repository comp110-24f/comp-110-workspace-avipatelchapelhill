"""My First Function"""

__author__ = "730767580"


def mimic(message: str) -> str:
    """Repeat input back to user"""
    return message


if __name__ == "__main__":
    print(mimic(message=input("What is your message?")))
