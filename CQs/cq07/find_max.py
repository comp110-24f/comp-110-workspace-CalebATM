"""Challenge question 07 function"""

__author__ = "730745780"


def find_and_remove_max(input: list[int]) -> int:
    """Finds, returns, and removes all instances of largest number in a list"""
    if len(input) == 0:
        return -1
    max: int = 0
    for elem in input:
        if elem > max:
            max = elem
    # at this point, the max value in the list has been found
    idx2: int = 0
    while idx2 < len(input):
        if input[idx2] == max:
            # removes the max value if found
            input.pop(idx2)
            # sets the counter variable back to the beginning of the list
            idx2 = 0
        else:
            idx2 += 1
    return max
