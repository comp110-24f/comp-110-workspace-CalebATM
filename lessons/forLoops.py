"""for...in...loops"""

xs: list[str] = ["w", "x", "y", "z"]
# Print every element of xs

for elem in xs:
    print(elem)


my_list: list[str] = ["hello", "world"]
new_list: list[str] = []
for elem in my_list:
    new_list.append(elem)
print(new_list)


pets: list[str] = ["Louie", "Bo", "Bear"]
for elem in pets:
    print(f"Good boy, {elem}!")


# a while loop may be better than a for loop if you...
# have condiitons that don't involve sequences
# are adding/removing elements to a sequence
# want to know what the index of an element is

# range() is a type of sequence you can loop over
# includes start point, does not include end point, and steps through
# every point in between
# Constructor: range(start, end, step)
# examples:
# range(1, 5) stops at numbers 1, 2, 3, 4
# range(1, 6, 2) stops at numbers 1, 3, 5

names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for idx in range(len(names)):
    print(f"{idx}: {names[idx]}")
