"""List Basics"""

# a list is a data structure - something that lets your reason
# about multiple items

# syntax:
# <list name>: list[<item type>]
# grocery_list: list[str]
# With a constructor:
# ● <list name>: list[<item type>] = list()
# ● grocery_list: list[str] = list()
# With a literal:
# ● <list name>: list[<item type>] = []
# ● grocery_list: list[str] = []

# Creating an empty list
my_numbers: list[float] = []  # literal
my_numbers: list[float] = list()  # constructor

print(my_numbers)

# String analogy
# my_name : str = "" # literal
# my_name: str = str() # constructor

# Adding an item to a list
# <list name>.append(<item>)
# grocery_list.append(“bananas”)

my_numbers.append(1.0)

print(my_numbers)

# Initializing An Already Populated List
# <list name>: list[<item type>] = [<item 0>, <item 1>, … , <item n>]
# grocery_list: list[str] = [“bananas”, “milk”, “bread”]

game_points: list[int] = [102, 86, 94]

print(game_points)

# Indexing
# grocery_list: list[str] = [“bananas”, “milk”, “bread”]
# grocery_list[0]

print(game_points[2])

# Modifying by Index
# grocery_list: list[str] = [“bananas”, “milk”, “bread”]
# grocery_list[1] = “eggs”

game_points[1] = 72

# Getting the length

print(len(game_points))

# Remove an item from a list

game_points.pop(1)


def display(my_list: list[int]) -> None:
    idx = 0
    while idx < len(my_list):
        print(my_list[idx])
        idx += 1


display(game_points)
