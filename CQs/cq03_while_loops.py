"""Challenge question 03!"""

__author__ = "730745780"


def num_instances(phrase: str, search_char: str) -> int:
    """Tells you how many times a character appears in a string"""
    # used to assign what index we're currently using
    current: int = 0
    # counter variable
    count: int = 0
    # tells us whether or not we've used every character in phrase yet
    while current < len(phrase):
        if phrase[current] == search_char:
            # adds one to count variable every time we find the specified character
            count += 1
        current += 1
    return count
