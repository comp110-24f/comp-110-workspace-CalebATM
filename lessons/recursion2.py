"""Another lesson on recursion."""


def factorial(n: int) -> int:
    """A factorial function."""
    if n == 0:
        return 1
    else:
        rest: int = factorial(n - 1)
        return n * rest


print(factorial(4))
