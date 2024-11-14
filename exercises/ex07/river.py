"""File to define River class."""

__author__ = "730745780"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """The River class (very HUGE)."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self) -> None:
        """Removes animals that are too old to exist."""
        # initializing lists to store animals that will continue to survive
        fish_temp: list[Fish] = list()
        bears_temp: list[Bear] = list()
        # loops that iterate over each animal list
        # if animals are still under a certain age,
        # they will be added to the above lists
        for idx in range(0, len(self.fish)):
            if self.fish[idx].age <= 3:
                fish_temp.append(self.fish[idx])
        for idx in range(0, len(self.bears)):
            if self.bears[idx].age <= 5:
                bears_temp.append(self.bears[idx])
        self.fish = fish_temp
        self.bears = bears_temp

    def bears_eating(self) -> None:
        """Giving the bears a chance to eat."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                # calling the Bear#eat and River#remove_fish methods
                bear.eat(3)
                self.remove_fish(3)

    def check_hunger(self) -> None:
        """Essentially removes Bears that starve."""
        # list for storing surviving bears
        temp_bears: list[Bear] = list()
        # loop that appends only bears with hunger score of 0
        # or higher to temp_bears
        for bear in self.bears:
            if bear.hunger_score >= 0:
                temp_bears.append(bear)
        self.bears = temp_bears

    def repopulate_fish(self) -> None:
        """Allow fish to reproduce."""
        # loop that iterates n//2 times
        # where n is the total fish population
        for _ in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())

    def repopulate_bears(self) -> None:
        """Allow bears to reproduce."""
        # loop that iterates n//2 times
        # where n is the total bear population
        for _ in range(len(self.bears) // 2):
            self.bears.append(Bear())

    def view_river(self) -> None:
        """Some print statements conveying animal populations."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Calls one_river_day seven times."""
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int) -> None:
        """Removes a specified number of fish."""
        for _ in range(amount):
            self.fish.pop(0)
