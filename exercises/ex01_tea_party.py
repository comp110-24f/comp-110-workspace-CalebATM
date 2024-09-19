"""Calculating the cost of a tea party for a user"""

__author__: str = "730745780"


def main_planner(guests: int) -> None:
    """Gets things going"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    # calling functions in functions bc we didn't save anything in variables
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


def tea_bags(people: int) -> int:
    """Returns the number of teabags needed for the party"""
    # take the attendee number and just multiply by 2 in the return statement
    return people * 2


def treats(people: int) -> int:
    """Returns the number of treats needed for the party"""
    # use tea bags function and multiply by 1.5, then return
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the tea party"""
    # multiply each argument by a predetermined float
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
