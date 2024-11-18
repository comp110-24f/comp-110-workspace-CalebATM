from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self):
        """Produce a string representation of a linked list."""
        rest: str = "TODO"
        # TODO: Figure out the rest of the list.
        if self.next is None:
            rest = "None"
        else:
            rest = self.next.__str__()
        return f"{self.value} -> {rest}"


two: Node = Node(2, None)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a Linked List as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


print(to_str(one))
print(to_str(courses))
print(str(courses))


def last(head: Node) -> int:
    """Return the last value of a non-empty list."""
    print(f"Enter last({head.value})")
    if head.next is None:
        print(f"Return base case: {head.value}")
        return head.value
    else:
        rest: int = last(head.next)
        print(f"Return recur: {head.value} -> {rest}")
        return rest


def last2(head: Node) -> int:
    """Return the last value of a non-empty list."""
    if head.next is None:
        return head.value
    else:
        rest: int = last2(head.next)
        return rest


print(last(one))
print(last(courses))
print(last2(one))
print(last2(courses))


def recursive_range(start: int, end: int) -> Node | None:
    """Recursively build a linked list from start to end, not inclusive."""
    if start > end:
        raise ValueError("Invalid arguments, start > end.")
    if start == end:
        return None
    else:
        rest: Node | None = recursive_range(start + 1, end)
        return Node(start, rest)


linked_list: Node | None = recursive_range(110, 113)
print(linked_list)
