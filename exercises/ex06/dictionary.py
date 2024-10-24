"""Exercie 06 with Caleb Almer Matias!"""

__author__ = "730745780"


def invert(pairs: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and the values of a given dictionary"""
    # for storing a list of all the keys
    keys_list: list[str] = list()
    # for storing a list of all the values
    values_list: list[str] = list()
    # dict that will eventually be our return value
    inverted_dict: dict[str, str] = dict()
    # loop that puts all the keys in keys_list and all the values in values_list
    for key in pairs:
        keys_list.append(key)
        values_list.append(pairs[key])
    # after adding all the values to a list,
    # this next segement basically checks for a duplicate
    # value in the values_list by iterating over the list
    # with a nested for loop
    for value1 in values_list:
        duplicates: int = 0
        for value2 in values_list:
            if value2 == value1:
                duplicates += 1
        if duplicates > 1:
            raise KeyError("Every key in a dictionary must be unique!")
    # adds the keys and values to the new dict but in swapped order
    for idx in range(0, len(keys_list)):
        inverted_dict[values_list[idx]] = keys_list[idx]
    return inverted_dict


def favorite_color(ppl_colors: dict[str, str]) -> str:
    """Returns the mode color (appears most often)"""
    color_list: list[str] = list()
    # puts all the colors in a list
    for key in ppl_colors:
        color_list.append(ppl_colors[key])
    # stores the number of times that the mode appeared
    max_count: int = 0
    # stores the idx position of the item that was found to be the mode
    idx_of_mode: int = 0
    # this nested for loop iterates through color_list
    # when it finds a value that repeats more time than the
    # current value of max_count, it changes max_count to be
    # however many times the new value appears and changes
    # idx_of_mode to the idx of whatever the new repeating value is
    for idx in range(0, len(color_list)):
        duplicates: int = 0
        for value2 in color_list:
            if color_list[idx] == value2:
                duplicates += 1
        if duplicates > max_count:
            max_count = duplicates
            idx_of_mode -= idx_of_mode  # sets variable back to zero
            idx_of_mode += idx  # sets variable equal to idx
    return color_list[idx_of_mode]


def count(input: list[str]) -> dict[str, int]:
    """Returns a dictionary of the counts of each of the items in the input list"""
    counts: dict[str, int] = dict()  # an empty dictionary that will store our values
    for idx in range(0, len(input)):
        if input[idx] in counts:
            counts[input[idx]] += 1  # adds to value if key already exists
        else:
            # makes a new key-value pair if key doesn't exist yet
            counts[input[idx]] = 1
    return counts


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Produces a dict that groups items from a given list by their starting letter"""
    sorted: dict[str, list[str]] = dict()  # dict for storing our sorted values
    for item in input:  # iterates over each item in the given list
        # determines if the first letter of current item is already a key in dict
        if item[0].lower() in sorted:
            sorted[item[0]].append(item)
        else:
            # only makes a new key-value pair if a key for the letter is not found
            sorted[item[0].lower()] = [item]
    return sorted


# THANK YOU for ending this exercise with something simple
def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """Updates the given dict with the new attendance information"""
    if day in input:  # checks if the day argument is already a key
        # adds the student argument under the appropriate day key
        input[day].append(student)
    else:
        # makes a new key-value pair if a particular day does not have a key yet
        input[day] = [student]
