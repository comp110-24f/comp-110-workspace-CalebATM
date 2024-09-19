"""Practice with conditionals"""

# A boolean is something that evaluates to True or False
# ^ Typically shown with relational operator and/or boolean operator
#
# Relational operators: ==, !=, >=, <=
# Boolean operators: not, and, or

# Ordering of operations
# P
# E
# MD
# AS
# not
# and
# or

# example
print((1 > 2) or not (3 > 2))
# "not (3 > 2)"" is evaluated Before "or"

# Conditional statement syntax:
#
# if <something>:
#   <do something>
# else:
#   <do something else>
# <rest of program>


def less_than_10(num: int) -> bool:
    """Tell me if num is less than 10"""
    if num < 10:
        return True
    else:
        return False


print(less_than_10(num=11))


def less_than_ten(num: int) -> None:
    """Tell me if num is less than 10"""
    if num < 10:
        print("Small number!")
    else:
        print("Big number!")
    print("Have a nice day!")


less_than_ten(num=11)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether I should eat based on hunger"""
    if hungry:
        print("Eat!")
    else:
        print("WORK!")


should_i_eat(hungry=False)


def check_first_letter(word: str, letter: str) -> str:
    """Determines if the first character of word is letter"""
    # if statement retrieves first letter of word
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
