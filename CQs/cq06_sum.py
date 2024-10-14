"""Summing the elements of a list using different loops"""

__author__ = "730745780"


def w_sum(vals: list[float]) -> float:
    """Sums all floats in a list with while loop"""
    # sum storage variable
    sum: float = 0.0
    idx: int = 0
    while idx < len(vals):
        # adds each individual list value to sum storage valuable
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sums all floats in list using for...in...loop"""
    # sum storage variable
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Sums all floats in list using for...in...range loop"""
    # sum storage variable
    sum: float = 0.0
    # using range function to get appropriate index positions
    for num in range(len(vals)):
        sum += vals[num]
    return sum
