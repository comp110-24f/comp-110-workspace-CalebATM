"""Challenge question 02!"""

__author__ = "730745780"


def guess_a_number() -> None:
    secret: int = 7
    guess: str = input("Guess a number: ")
    print("Your guess was " + guess)
    if int(guess) == secret:
        print("You got it!")
    elif int(guess) < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    elif int(guess) > secret:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
