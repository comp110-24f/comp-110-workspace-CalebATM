import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""List utility functions unit tests EX05"""

__author__ = "730745780"


# use case for only_evens()
def test_only_evens_rv1() -> None:
    """only_evens should return the even numbers in my_list"""
    my_list: list[int] = [1, 5, 3, 7, 8, 9, 13]
    assert only_evens(my_list) == [8]


# return value test for only_evens()
def test_only_evens_rv2() -> None:
    """only_evens should return a list"""
    my_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert type(only_evens(my_list)) == list


# edge case for only_evens()
def test_only_evens_edge_case() -> None:
    """only_evens should return an empty list if given one"""
    assert only_evens([]) == []


# use case for sub()
def test_sub_rv1() -> None:
    """sub should only return the specified values"""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8], 3, 6) == [4, 5, 6]


# return value test for sub()
def test_sub_rv2() -> None:
    """sub should return a list"""
    assert type(sub([13, 24, 7, 893, 66], 1, 2)) == list


# edge case for sub()
def test_sub_edge_case() -> None:
    """sub should return an empty list if given one"""
    assert sub([], 1, 4) == []


# use case for add_at_index()
def test_add_at_index_rv1() -> None:
    """add_at_index should insert the value as intended"""
    my_list: list[int] = [5, 2, 3, 1]
    add_at_index(my_list, 7, 2)
    assert my_list == [5, 2, 7, 3, 1]


# return value test for add_at_index()
def test_add_at_index_rv2() -> None:
    """add_at_index should return None"""
    my_list: list[int] = [5, 2, 3, 1]
    assert add_at_index(my_list, 7, 2) is None


# edge case for add_at_index()
def test_add_at_index_edge_case() -> None:
    """If the idx is unusable, an IndexError should be raised by add_at_index"""
    my_list: list[int] = []
    assert pytest.raises(IndexError, add_at_index, my_list, 7, 2)
