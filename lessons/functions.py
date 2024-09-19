"""Functions Review and Examples"""

from random import randint, random, choice

# print()
# round() - rounds to the nearest int, but .5 rounds down
# len() - retrieves number of characters in a string
# randint() - returns a random integer within the specified range, inclusive
# random() - generates random float from 0 to 1
# choice() - chooses random character from given string

# Syntax for calling a function:
# function_name(<argument list>)

print(randint(3, 17))
print(random())
print(choice("hello"))

# User-defined function syntax
#
# def function_name(<parameter list>) -> <return type>:
#   """Docstring describing function"""
#   <what your function does>


def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2"""
    return num1 + num2


# Function call
print(sum(num1=2, num2=13))
# Arguments are used in function calls while parameters are found in the signature
