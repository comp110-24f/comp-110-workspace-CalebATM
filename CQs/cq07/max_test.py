"""Tests for remove_and_find_max"""

__author__ = "730745780"

from CQs.cq07.find_max import find_and_remove_max


# test of behavior (use case)
def test_find_and_remove_max1() -> None:
    """Ensuring find_and_remove_max returns the expected value"""
    a: list[int] = [1, 2, 3, 9, 3, 6, 2, 6, 9, 7]
    assert find_and_remove_max(a) == 9


# another test of behavior
def test_find_and_remove_max2() -> None:
    """Ensuring find_and_remove_max mutates the input in the expected way"""
    b: list[int] = [1, 2, 3, 9, 3, 6, 2, 6, 9, 7]
    find_and_remove_max(b)
    assert b == [1, 2, 3, 3, 6, 2, 6, 7]


# edge case
def test_find_and_remove_max_edge_case() -> None:
    """Returns the correct value in case of an unconventional input"""
    c: list[int] = []
    assert find_and_remove_max(c) == -1
