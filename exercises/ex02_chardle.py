"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730745780"


def input_word() -> str:
    """Gets a word the user"""
    user_word: str = input("Enter a 5-character word: ")
    # determines if length of user input is satisfactory
    if len(user_word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return user_word


def input_letter() -> str:
    """Prompts the user for a single character input"""
    user_char: str = input("Enter a single character: ")
    # determines whether or not user entered one character
    if len(user_char) != 1:
        print("Error: Character must be a single character.")
        exit()
    return user_char


def contains_char(word: str, letter: str) -> None:
    """Checks if input character matches any characters in the input word"""
    # records how many instances of char is in word
    count: int = 0
    print("Searching for " + letter + " in " + word)
    # goes on to check each individual index with 5 if statements
    if letter == word[0]:
        print(letter + " found at index 0")
        count += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


def main() -> None:
    """Calls everything in the order we need"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
