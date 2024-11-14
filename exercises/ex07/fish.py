"""File to define Fish class."""

__author__ = "730745780"


class Fish:
    """The Fish class."""

    age: int

    def __init__(self):
        """Initializes an instance of Fish."""
        self.age = 0

    def one_day(self) -> None:
        """Simulates a day for an individual fish."""
        self.age += 1
