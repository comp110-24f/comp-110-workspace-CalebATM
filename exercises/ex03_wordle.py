"""WORDLE EXERCISE"""

__author__ = "730745780"


def input_guess(word_len: int) -> str:
    """Gets a guess of the correct length from the user"""

    user_guess: str = input(f"Enter a {word_len} character word: ")
    while len(user_guess) != word_len:
        user_guess = input(f"That wasn't {word_len} chars! Try again: ")
    return user_guess


def contains_char(word: str, char: str) -> bool:
    """Searches a given word for a given character"""
    assert len(char) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == char:
            return True
        # increments the idx "counter variable" if char not found
        else:
            idx += 1
    return False


def emojified(user_guess: str, secret_word: str) -> str:
    """Uses green, yellow, and white emojis to represent guess accuracy"""
    assert len(user_guess) == len(secret_word)
    # blank list for emojis to populate
    emojis: str = str()
    # special emoji characters definitions
    white: str = "\U00002B1C"
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    idx: int = 0
    while idx < len(user_guess):
        # adds green for correct char in correct position
        if user_guess[idx] == secret_word[idx]:
            emojis += green
        # uses contains_char to determine if yellow or white
        elif contains_char(secret_word, user_guess[idx]):
            emojis += yellow
        else:
            emojis += white
        idx += 1
    return emojis


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # increments every time user finishes a round of guessing
    turns: int = 1
    # maintans state of user's victory
    user_win: bool = False
    while turns < 7 and not user_win:
        print(f"=== Turn {turns}/6 ===")
        # stores the user's guess in a variable so it can be accessed later
        # it uses the length of the secret word as the argument for input_guess
        user_word: str = input_guess(len(secret))
        # compares user's word to the sercet word determined when main was called
        print(emojified(user_word, secret))
        if user_word == secret:
            print(f"You won in {turns}/6 turns!")
            user_win = True
        # increments turn if user has not won yet or used all their turns
        else:
            turns += 1
    # bad ending message
    if turns == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
