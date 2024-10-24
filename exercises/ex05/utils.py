"""List utility functions EX05"""

__author__ = "730745780"


def only_evens(input: list[int]) -> list:
    """Returns only the even ints from the list given to it"""
    evens_list: list[int] = list()
    # for loop to iterate over each int in input
    for elem in input:
        # testing if even
        if elem % 2 == 0:
            evens_list.append(elem)
    return evens_list


def sub(input: list[int], start: int, end: int) -> list:
    """Generates a list which is a subset of the input list"""
    # Correcting nonsense start values
    if start < 0:
        start = 0
    # Correcting nonsense end values
    if end > len(input):
        end = len(input)
    # Establishing empty list return for 3 different cases
    if len(input) == 0 or start >= len(input) or end <= 0:
        return []
    sub_list: list[int] = list()
    for idx in range(start, end):
        sub_list.append(input[idx])
    return sub_list


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Modifies the input list to place the element at the given index."""
    if idx > len(input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)
    # This feels a bit convoluted, so here's an explanation:
    # The range function starts at the second to last element
    # This means that it ignores the 0 appended above
    # Then, it works its way backwards, moving each element
    # one spot to the right until it reaches the idx argument
    for num in range(len(input) - 2, idx - 1, -1):
        input[num + 1] = input[num]
    input[idx] = elem
