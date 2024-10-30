"""Practicing with Dictionaries"""

__author__ = "730767580"

"""Invert a dictionary"""


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    inverted_dict = {}
    for key in input_dict:
        value = input_dict[key]  # Access the value associated with the key
        if value in inverted_dict:
            raise KeyError(
                f"Duplicate key detected in the inverted dictionary: {value}"
            )
        inverted_dict[value] = key
    return inverted_dict


"""Find the color in a dictionary with the  most occurances"""


def favorite_color(color_dict: dict[str, str]) -> str:
    # Collect the color frequencies
    frequency = {}
    for name in color_dict:
        color = color_dict[name]
        if color in frequency:
            frequency[color] += 1
        else:
            frequency[color] = 1
    # Find the color with the highest frequency
    most_common_color = ""
    highest_count = 0
    for color in frequency:
        freq = frequency[color]
        if freq > highest_count:
            most_common_color = color
            highest_count = freq
    return most_common_color


"""Return the counts of the frequencies of items in a list"""


def count(values: list[str]) -> dict[str, int]:
    result = {}
    for item in values:
        # Check if the item is already in the dictionary
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


"""Update the attendance logs with inputted information"""


def update_attendance(
    attendance_dict: dict[str, list[str]], day: str, student: str
) -> None:
    if day in attendance_dict:
        if student not in attendance_dict[day]:
            attendance_dict[day].append(student)
    else:
        # add the day with the student in a new list
        attendance_dict[day] = [student]
