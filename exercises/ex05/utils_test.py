import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""List utility functions unit tests EX05"""

__author__ = "730745780"


# use case
def test_only_evens_rv1() -> None:
    """only_evens should return the even numbers in my_list"""
    my_list: list[int] = [1, 5, 3, 7, 8, 9, 13]
    assert only_evens(my_list) == [8]


# return value test
def test_only_evens_rv2() -> None:
    """only_evens should return a list"""
    my_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert type(only_evens(my_list)) == list


# edge case
def test_only_evens_edge_case() -> None:
    """An empty input for only_evens should result in an empty output"""
    assert only_evens([]) == []


# use case
def test_sub_rv1() -> None:
    """sub should only return the specified values"""
    assert sub([1, 2, 3, 4, 5, 6, 7, 8], 3, 6) == [4, 5, 6]


# return value test
def test_sub_rv2() -> None:
    """sub should return a list"""
    assert type(sub([13, 24, 7, 893, 66], 1, 2)) == list


# edge case
def test_sub_edge_case() -> None:
    """An empty list input should result in an empty list output"""
    assert sub([], 1, 4) == []


# use case
def test_add_at_index_rv1() -> None:
    """The function should insert the value as intended"""
    my_list: list[int] = [5, 2, 3, 1]
    add_at_index(my_list, 7, 2)
    assert my_list == [5, 2, 7, 3, 1]


# return value test
def test_add_at_index_rv2() -> None:
    """The function should return None"""
    my_list: list[int] = [5, 2, 3, 1]
    assert add_at_index(my_list, 7, 2) is None


# edge case
def test_add_at_index_edge_case() -> None:
    """If the idx is unusable, an IndexError should be raised"""
    my_list: list[int] = []
    assert pytest.raises(IndexError, add_at_index, my_list, 7, 2)
