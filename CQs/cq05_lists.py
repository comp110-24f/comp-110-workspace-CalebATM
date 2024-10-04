"""Mutating functions."""

__author__ = "730745780"


def manual_append(list: list[int], num: int) -> None:
    """A user-defined append function for lists (useless)"""
    # adds argument to end of list
    list.append(num)


def double(list: list[int]) -> None:
    """Doubles all the integers in an integer list"""
    # counter variable for indexing
    idx: int = 0
    while idx < len(list):
        # doubles the values
        list[idx] *= 2
        # Very important "incrementer"
        idx += 1


list1: list[int] = [1, 2, 3]
list2: list[int] = list1

double(list2)
print(list1)
print(list2)
