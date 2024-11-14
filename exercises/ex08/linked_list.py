"""EX08: [Singly] Linked List Utils."""

from __future__ import annotations

__author__ = "730745780"


class Node:
    """Nodes for making singly linked lists."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing attributes at Node instantiation."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


my_list: Node = Node(10, Node(20, Node(30, None)))


def value_at(head: Node | None, index: int) -> int:
    """Return the value at a specific Node in a linked list."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:  # THE base case that ends the recursion and starts the backward loop
        return head.value
    else:
        # decrements the index every time the function gets called
        rest: int = value_at(head.next, index - 1)
        return rest


print(value_at(my_list, 2))


def max(head: Node | None) -> int:
    """Returns the max value in a singly-linked list."""
    # if the list is empty, raises an error
    if head is None:
        raise ValueError("Cannot call max with None.")
    # if the Node currently being accessed is the last one, return its value
    if head.next is None:
        return head.value
    else:
        # I'm realy showing love to this 'rest' variable name
        # This rest variable saves the value of the Node when the base case applies
        # Then, checks for larger values and adjusts as the
        # recursive process loops backwards
        rest: int = max(head.next)
        if head.value > rest:
            rest = head.value
        return rest


print(max(my_list))


def linkify(items: list[int]) -> Node | None:
    """Given a list[int], returns a Linked List of Nodes with the same values."""
    if len(items) == 0:
        return None  # edge case
    # Checks if the list item being accessed is the last in the list
    # If so, returns a Node with a value of the list item and next value of None
    if len(items) == 1:
        return Node(items[0], None)
    else:
        # when the list item being accessed isn't the last one,
        # it calls the function again, but starting from the item AFTER
        # the one currently being accessed (made possible by slice
        # subscription notation)
        rest: Node | None = linkify(items[1:])
        return Node(items[0], rest)


print(linkify([1, 2, 3, 4]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Returns a linked list of Nodes where the original list's values are scaled."""
    # checks if Node being accessed is either the tail end or has no next value
    if head is None:
        return None
    else:
        # If Node being accessed isn't the last, calls fucntion again on next Node
        rest: Node | None = scale(head.next, factor)
        # Multiplies the value of Node being accessed and sets its .next value
        # to whatever the rest variable brought back
        return Node(head.value * factor, rest)
