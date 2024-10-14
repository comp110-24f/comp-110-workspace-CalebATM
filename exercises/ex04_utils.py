"""Exercise 4!"""

__author__ = "730745780"


def all(list: list[int], num: int) -> bool:
    """Returns True if all int in list are equal to num"""
    if len(list) == 0:
        return False
    idx: int = 0
    while idx < len(list):
        # checks if list item is not equal to num
        if list[idx] != num:
            return False
        idx += 1
    return True


def max(list1: list[int]) -> int:
    """Returns the max integer in a given list"""
    # sets max to first item in list by default
    max: int = list1[0]
    # counter variable
    idx: int = 0
    while idx < len(list1):
        if list1[idx] > max:
            # sets max to current list item if current list item is greater
            max = list1[idx]
        idx += 1
    return max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Returns True if all corresponding values in lists are equal"""
    if len(list1) != len(list2):
        return False
    # counter variable
    idx: int = 0
    while idx < len(list1):
        # checks whether same-index items in each list are not equal
        if list1[idx] != list2[idx]:
            return False
        # crucial "incrementer" to prevent infinite loops
        idx += 1
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    """Attaches one list of integers to the end of another list of int"""
    idx: int = 0
    # loop that iterates through list2 and adds each item individually to list1
    while idx < len(list2):
        list1.append(list2[idx])
        # important incrementer
        idx += 1


# backup commit was completed using the command line (my brother taught me)
