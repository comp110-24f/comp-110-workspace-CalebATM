"""Stuff for Monday, October 14th lesson"""


def get_first(input: list[str]) -> str:
    """Returns first element in list of strings"""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Removes first element from a list of strings"""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Removes and returns the first element in a list of strings"""
    first: str = input[0]
    input.pop(0)
    return first
