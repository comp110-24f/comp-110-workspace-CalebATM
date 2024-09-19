"""First Challenge question!"""

__author__ = "730745780"


def mimic(message: str) -> str:
    """Takes a string input and repeat it back to you"""
    return message


def main() -> None:
    """Prints the result of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
