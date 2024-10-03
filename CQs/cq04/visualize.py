"""Visualize file for challenge question 4"""

__author__ = "730745780"

# when I hit the run file button, it doesnt work, but
# when I run it from the command line, the module works fine
# and I think it has to do with how I import the files

# if I do "from CQs.cq04.concatenation import concat"
# it only works if run by the command line

# But if I do "from concatenation import concat"
# it only works with the run file button
from CQs.cq04.concatenation import concat
from CQs.cq04.coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))
get_coords(x, y)
