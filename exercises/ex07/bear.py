"""File to define Bear class."""

__author__ = "730745780"


class Bear:
    """The Bear class."""

    age: int
    hunger_score: int

    def __init__(self):
        """Initialize a Bear instance."""
        self.age = 0
        self.hunger_score = 0

    def one_day(self) -> None:
        """Simulates a day for an individual bear."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int) -> None:
        """Affects bear's hunger_score attribute."""
        self.hunger_score += num_fish
