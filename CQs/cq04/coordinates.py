"""Coordinates file for challenge question 4"""

__author__ = "730745780"


def get_coords(xs: str, ys: str) -> None:
    index1: int = 0
    while index1 < len(xs):
        # turns out, I needed to put index 2 AFTER the first while, not before
        index2: int = 0
        while index2 < len(ys):
            # f string to make formatting easier
            print(f"({xs[index1]},{ys[index2]})")
            index2 += 1
        index1 += 1


# THAT took longer than it should have...


if __name__ == "__main__":
    get_coords("hi", "bye")
